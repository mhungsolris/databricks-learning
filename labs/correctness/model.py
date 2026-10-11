"""Deterministic ROAS contracts. Money: integer USD cents. Times: UTC."""
from collections import Counter, defaultdict
from datetime import date, datetime, timedelta, timezone
import hashlib
import json

KEY = ('source_system', 'app_id', 'event_id')
STATE = (*KEY, 'revision', 'revenue', 'event_time', 'updated_at', 'platform',
         'account_id', 'campaign_id', 'currency', 'is_deleted')
GOLD_KEY = ('date', 'platform', 'account_id', 'app_id', 'campaign_id', 'currency')


class ContractError(ValueError):
    pass


class InjectedFailure(RuntimeError):
    pass


class BatchJob:
    """In-memory target/cursor fault model, not a distributed transaction protocol."""
    def __init__(self):
        self.target = []
        self.cursor = None

    def run(self, source, upper, *, fail_at=None):
        if self.cursor is not None and upper < self.cursor:
            raise ContractError('Cursor cannot move backwards')
        if fail_at not in (None, 'after_read', 'after_write'):
            raise ContractError('Unknown fault boundary')
        lower = None if self.cursor is None else (
            datetime.fromisoformat(self.cursor.replace('Z', '+00:00')) - timedelta(minutes=1)).isoformat().replace('+00:00', 'Z')
        selected = [r for r in source if (lower is None or r['updated_at'] >= lower) and r['updated_at'] <= upper]
        if fail_at == 'after_read':
            raise InjectedFailure('after_read')
        self.target = advance(self.target, selected)
        if fail_at == 'after_write':
            raise InjectedFailure('after_write_before_cursor')
        self.cursor = upper
        return self.target


def event(event_id='E1', revenue=100, revision=1, **changes):
    row = dict(source_system='adjust', app_id='appA', event_id=event_id, revision=revision,
               revenue=revenue, event_time='2026-10-01T10:00:00Z', updated_at='2026-10-01T10:01:00Z',
               ingested_at='2026-10-01T10:03:00Z', processed_at='2026-10-01T10:15:00Z',
               platform='google', account_id='account-1', campaign_id='C1', currency='USD',
               is_deleted=False, channel='callback')
    row.update(changes)
    # A changed synthetic source state arrives/processes after its mutation by default.
    # Explicit timestamp overrides remain available for clock-skew/late-arrival cases.
    if 'updated_at' in changes:
        mutation = datetime.fromisoformat(row['updated_at'].replace('Z', '+00:00'))
        for name, minutes in [('ingested_at', 2), ('processed_at', 14)]:
            if name not in changes:
                row[name] = (mutation + timedelta(minutes=minutes)).isoformat().replace('+00:00', 'Z')
    return row


def identity(row):
    return tuple(row[k] for k in KEY)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False)


def fingerprint(row):
    # Detect content disagreement; this hash does not create business identity.
    return hashlib.sha256(canonical({k: row[k] for k in STATE}).encode()).hexdigest()


def validate(row):
    if any(not row.get(k) for k in KEY):
        raise ContractError('Null/incomplete business identity')
    if type(row['revision']) is not int or row['revision'] < 1:
        raise ContractError('Positive source revision required')
    if type(row['revenue']) is not int or row['currency'] != 'USD':
        raise ContractError('Fixture expects integer USD cents')
    for name in ('event_time', 'updated_at', 'ingested_at', 'processed_at'):
        stamp = datetime.fromisoformat(row[name].replace('Z', '+00:00'))
        if stamp.utcoffset() != timedelta(0):
            raise ContractError('UTC timestamps required')
    if not row['campaign_id']:
        row = {**row, 'campaign_id': 'UNKNOWN'}
    return row


def resolve(rows):
    seen, latest = {}, {}
    for raw in rows:
        row = validate(raw)
        key = identity(row)
        version = (*key, row['revision'])
        payload = canonical({k: row[k] for k in STATE})
        if version in seen and seen[version] != payload:
            raise ContractError('Equal-revision conflicting payload; source semantics required')
        seen[version] = payload
        if key not in latest or row['revision'] > latest[key]['revision']:
            latest[key] = row
    return [latest[k] for k in sorted(latest)]


def advance(target, source):
    result = {identity(r): validate(r) for r in target}
    if len(result) != len(target):
        raise ContractError('Target grain is not unique')
    for row in resolve(source):
        key = identity(row)
        old = result.get(key)
        if old and row['revision'] == old['revision'] and fingerprint(row) != fingerprint(old):
            raise ContractError('Equal revision disagrees with committed state')
        if old is None or row['revision'] > old['revision']:
            result[key] = row
    return [result[k] for k in sorted(result)]


def business_state(rows):
    return sorted([{k: r[k] for k in STATE} for r in rows], key=identity)


def state_hash(rows):
    return hashlib.sha256(canonical(business_state(rows)).encode()).hexdigest()


def costs():
    return [dict(date='2026-10-01', platform=p, account_id='account-1', app_id='appA',
                 campaign_id=c, currency='USD', cost=amount)
            for p, c, amount in [('google', 'C1', 50), ('meta', 'C2', 40),
                                  ('tiktok', 'C3', 30), ('unity', 'C4', 20)]]


def deliveries():
    first = event('E1', 0)
    changed = event('E1', 100, 2, updated_at='2026-10-02T08:00:00Z',
                    ingested_at='2026-10-02T08:03:00Z', channel='file')
    return [first, dict(first), changed, event('E2', 50, platform='meta', campaign_id='C2'),
            event('E3', 20, platform='unknown', campaign_id=None)]


def gold(events, daily_costs):
    output = {}
    for r in resolve(events):
        if r['is_deleted']:
            continue
        key = (r['event_time'][:10], *(r[k] for k in GOLD_KEY[1:]))
        row = output.setdefault(key, dict(zip(GOLD_KEY, key), revenue=0, cost=0, cost_present=False))
        row['revenue'] += r['revenue']
    seen = set()
    for c in daily_costs:
        key = tuple(c[k] for k in GOLD_KEY)
        if key in seen:
            raise ContractError('Duplicate daily cost grain')
        seen.add(key)
        row = output.setdefault(key, dict(zip(GOLD_KEY, key), revenue=0, cost=0, cost_present=False))
        row.update(cost=c['cost'], cost_present=True)
    for r in output.values():
        r['roas'] = r['revenue'] / r['cost'] if r['cost_present'] and r['cost'] else None
    return [output[k] for k in sorted(output)]


def reconcile(expected, actual, *, tolerance=0):
    if tolerance < 0:
        raise ContractError('Tolerance cannot be negative')
    if len({identity(r) for r in expected}) != len(expected) or any(any(not r[k] for k in KEY) for r in expected):
        raise ContractError('Expected truth must have complete unique keys')
    expected_by_key = {identity(r): r for r in expected}
    counts = Counter(identity(r) for r in actual)
    actual_by_key = {identity(r): r for r in actual}
    mismatched = [list(k) for k in sorted(expected_by_key.keys() & actual_by_key.keys(), key=repr)
                  if fingerprint(expected_by_key[k]) != fingerprint(actual_by_key[k])]
    total = lambda rows: sum(r['revenue'] for r in rows if not r['is_deleted'])
    result = {'missing': [list(k) for k in sorted(expected_by_key.keys() - actual_by_key.keys(), key=repr)],
              'extra': [list(k) for k in sorted(actual_by_key.keys() - expected_by_key.keys(), key=repr)],
              'duplicates': [list(k) for k, n in sorted(counts.items(), key=lambda entry: repr(entry[0])) if n > 1],
              'mismatched': mismatched, 'nullKeys': sum(any(not r[k] for k in KEY) for r in actual),
              'expectedRows': len(expected), 'actualRows': len(actual),
              'expectedRevenue': total(expected), 'actualRevenue': total(actual), 'tolerance': tolerance,
              'expectedByDay': dict(sorted(_day_totals(expected).items())),
              'actualByDay': dict(sorted(_day_totals(actual).items()))}
    result['pass'] = (not any(result[k] for k in ('missing', 'extra', 'duplicates', 'mismatched', 'nullKeys'))
                      and abs(result['expectedRevenue'] - result['actualRevenue']) <= tolerance
                      and result['expectedByDay'] == result['actualByDay'])
    return result


def _day_totals(rows):
    totals = defaultdict(int)
    for row in rows:
        if not row['is_deleted']:
            totals[row['event_time'][:10]] += row['revenue']
    return totals


def medallion():
    bronze = deliveries()
    silver = resolve(bronze)
    report = gold(silver, costs())
    # Wrong detail-to-daily join repeats cost for each matching transaction.
    two_events = [event('E10', 40), event('E11', 60)]
    wrong_cost = sum(c['cost'] for r in two_events for c in costs()
                     if r['campaign_id'] == c['campaign_id'] and r['platform'] == c['platform'])
    correct = gold(two_events, [costs()[0]])
    assert (len(bronze), len(silver), sum(r['revenue'] for r in report), sum(r['cost'] for r in report)) == (5, 3, 170, 140)
    assert wrong_cost == 100 and correct[0]['cost'] == 50
    return {'bronzeRows': 5, 'silverRows': 3, 'gold': report, 'wrongDetailCost': wrong_cost,
            'correctCost': 50, 'revenueConserved': 170, 'costConserved': 140}


def incremental():
    run1 = [dict(id=x, created_at=f'2026-10-01T10:0{i}:00Z', updated_at=f'2026-10-01T10:0{i}:00Z', value=10)
            for i, x in enumerate('ABC')]
    run2 = [run1[0], {**run1[1], 'updated_at': '2026-10-01T10:15:00Z', 'value': 20}, run1[2],
            dict(id='D', created_at='2026-10-01T10:15:00Z', updated_at='2026-10-01T10:15:00Z', value=10),
            dict(id='E', created_at='2026-09-30T08:00:00Z', updated_at='2026-10-01T10:15:00Z', value=30)]
    cursor = max(r['created_at'] for r in run1)
    naive = [r['id'] for r in run2 if r['created_at'] > cursor]
    updated = [r['id'] for r in run2 if cursor < r['updated_at'] <= '2026-10-01T10:15:00Z']
    tied_late = dict(id='F', created_at='2026-09-30T07:00:00Z', updated_at='2026-10-01T10:15:00Z', value=40)
    exclusive = [r for r in [tied_late] if r['updated_at'] > '2026-10-01T10:15:00Z']
    overlap = [r for r in [tied_late] if r['updated_at'] >= '2026-10-01T10:14:00Z']
    snapshot1 = {r['id']: r for r in run1}
    snapshot2 = {r['id']: r for r in run2}
    diff = [k for k in snapshot2 if snapshot2[k] != snapshot1.get(k)]
    deleted = sorted(snapshot2.keys() - {'A', 'C', 'D', 'E'})
    assert naive == ['D'] and updated == diff == ['B', 'D', 'E'] and not exclusive and overlap
    return {'run1': run1, 'run2': run2, 'naiveCreatedIds': naive, 'updatedIds': updated,
            'snapshotDiffIds': diff, 'sameTimestampMiss': 'F', 'lookbackRecovers': 'F',
            'snapshotDeleteKeys': deleted, 'requiresCompleteSnapshotForDeletes': True,
            'cursorRule': 'Publish cursor only after target commit; replay overlap on cursor-store failure'}


def time_semantics():
    late = event('L1', 100, event_time='2026-10-01T23:59:00Z', ingested_at='2026-10-02T00:03:00Z',
                 processed_at='2026-10-02T00:15:00Z', updated_at='2026-10-02T08:00:00Z')
    return {'eventDate': late['event_time'][:10], 'incorrectProcessingDate': late['processed_at'][:10],
            'event': late, 'businessDateRevenue': {'2026-10-01': 100}, 'wrongDateRevenue': {'2026-10-02': 100}}


def backfill_source():
    return [event(f'BF{i+1:03}', 10, revision=2,
                  event_time=(date(2026, 1, 1) + timedelta(days=i)).isoformat() + 'T10:00:00Z') for i in range(90)]
