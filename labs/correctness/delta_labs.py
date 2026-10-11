"""Actual Delta correctness experiments, each with bounded state assertions."""
import json
from pathlib import Path
from labs.correctness import model as M
from labs.spark.common import write_json

SCHEMA = ('source_system string, app_id string, event_id string, revision long, revenue long, '
          'event_time string, updated_at string, ingested_at string, processed_at string, '
          'platform string, account_id string, campaign_id string, currency string, is_deleted boolean, channel string')
COLUMNS = [part.strip().split()[0] for part in SCHEMA.split(',')]


def frame(spark, rows):
    return spark.createDataFrame([tuple(r[k] for k in COLUMNS) for r in rows], SCHEMA)


def read(spark, target):
    return [r.asDict() for r in spark.read.format('delta').load(str(target)).collect()]


def create(spark, target, rows):
    frame(spark, rows).coalesce(1).write.format('delta').mode('errorifexists').save(str(target))


def merge(spark, target, source):
    current = read(spark, target)
    candidates = M.resolve(source)
    # Preflight defines source uniqueness and rejects equal-version ambiguity before SQL.
    M.advance(current, candidates)
    frame(spark, candidates).createOrReplaceTempView('correctness_changes')
    predicate = ' AND '.join(f't.{k} = s.{k}' for k in M.KEY)
    assignments = ', '.join(f't.{k} = s.{k}' for k in COLUMNS if k not in M.KEY)
    cols = ', '.join(COLUMNS)
    values = ', '.join(f's.{k}' for k in COLUMNS)
    spark.sql(f'''MERGE INTO delta.`{target}` t USING correctness_changes s ON {predicate}
                  WHEN MATCHED AND s.revision > t.revision THEN UPDATE SET {assignments}
                  WHEN NOT MATCHED THEN INSERT ({cols}) VALUES ({values})''')
    return read(spark, target)


def capture(spark, target, out, name):
    rows = read(spark, target)
    history = [r.asDict() for r in spark.sql(f'DESCRIBE HISTORY delta.`{target}`')
               .select('version', 'operation', 'operationMetrics').collect()]
    state = {'rows': M.business_state(rows), 'hash': M.state_hash(rows), 'history': history}
    write_json(out / (name + '.json'), state)
    return state


def lab09(spark, out):
    result = M.medallion()
    # Source-faithful Bronze retains duplicate delivery and original missing field.
    write_json(out / 'bronze-payloads.json', M.deliveries())
    write_json(out / 'silver-contract.json', M.business_state(M.resolve(M.deliveries())))
    write_json(out / 'grain-contracts.json', {'bronze': 'one delivery', 'silver': list(M.KEY),
               'dailyCostAndGold': list(M.GOLD_KEY), 'money': 'integer USD cents', 'timezone': 'UTC'})
    return result


def lab10(spark, out):
    return M.incremental()


def lab11(spark, out):
    batch = [M.event('E123', 100)] * 3
    safe, broken = out / 'safe', out / 'broken'
    create(spark, safe, [])
    # Fault between read and write leaves target empty; retry materializes intended state.
    pre_failure = capture(spark, safe, out, 'before-write-failure')
    faults = []
    try:
        read(spark, safe)
        raise M.InjectedFailure('after_read_before_write')
    except M.InjectedFailure as exc:
        faults.append(str(exc))
    assert pre_failure['rows'] == []
    merge(spark, safe, batch)
    once = capture(spark, safe, out, 'once')
    merge(spark, safe, batch)
    twice = capture(spark, safe, out, 'replay')
    assert once['hash'] == twice['hash'] and twice['rows'][0]['revenue'] == 100 and len(twice['rows']) == 1
    # Commit happened but cursor/ack did not. Retrying the same source is business-idempotent.
    try:
        merge(spark, safe, batch)
        raise M.InjectedFailure('after_commit_before_ack')
    except M.InjectedFailure as exc:
        faults.append(str(exc))
    merge(spark, safe, batch)
    ack_retry = capture(spark, safe, out, 'after-ack-failure-retry')
    assert ack_retry['hash'] == once['hash']
    create(spark, broken, batch)
    wrong = capture(spark, broken, out, 'append-duplicates')
    assert sum(r['revenue'] for r in wrong['rows']) == 300
    fixed = read(spark, safe)
    return {'safeRevenue': 100, 'appendRevenue': 300, 'onceHash': once['hash'], 'replayHash': twice['hash'],
            'ackRetryHash': ack_retry['hash'], 'reconciliation': M.reconcile(M.resolve(batch), fixed),
            'faultsObserved': faults, 'businessStateStableDespiteHistoryChanges': True}


def lab12(spark, out):
    target = out / 'matrix'
    create(spark, target, [])
    e1 = M.event('E123', 0)
    merge(spark, target, [e1])
    states = {'insert': capture(spark, target, out, 'insert')}
    updated = M.event('E123', 100, 2, updated_at='2026-10-02T08:00:00Z')
    merge(spark, target, [updated])
    states['update'] = capture(spark, target, out, 'update')
    merge(spark, target, [updated])
    states['replay'] = capture(spark, target, out, 'replay')
    assert states['update']['hash'] == states['replay']['hash']
    merge(spark, target, [e1])
    states['stale'] = capture(spark, target, out, 'stale')
    assert states['stale']['hash'] == states['replay']['hash']
    newer = M.event('E123', 120, 3, updated_at='2026-10-03T08:00:00Z')
    additive = M.event('E124', 100)
    merge(spark, target, [newer, additive])
    states['newer-and-distinct-event'] = capture(spark, target, out, 'newer')
    assert [(r['event_id'], r['revenue']) for r in states['newer-and-distinct-event']['rows']] == [('E123', 120), ('E124', 100)]
    for row in states['insert']['rows']: assert row['revenue'] == 0
    for key in ['update', 'replay', 'stale']: assert states[key]['rows'][0]['revenue'] == 100
    conflict = [M.event('E123', 100, 4), M.event('E123', 200, 4)]
    try:
        merge(spark, target, conflict)
    except M.ContractError:
        pass
    else:
        raise AssertionError('Source conflict accepted')
    assert capture(spark, target, out, 'preflight-conflict')['hash'] == states['newer-and-distinct-event']['hash']
    # Bypass preprocessing deliberately to observe the actual engine ambiguity failure.
    frame(spark, conflict).createOrReplaceTempView('ambiguous_changes')
    before_versions = len(list((target / '_delta_log').glob('*.json')))
    engine_error = None
    try:
        spark.sql(f'''MERGE INTO delta.`{target}` t USING ambiguous_changes s
                      ON t.source_system=s.source_system AND t.app_id=s.app_id AND t.event_id=s.event_id
                      WHEN MATCHED THEN UPDATE SET t.revenue=s.revenue''')
    except Exception as exc:
        engine_error = str(exc)
        assert 'DELTA_MULTIPLE_SOURCE_ROW_MATCHING_TARGET_ROW_IN_MERGE' in engine_error
    assert engine_error and len(list((target / '_delta_log').glob('*.json'))) == before_versions
    write_json(out / 'ambiguous-source-error.json', {'errorClass': 'DELTA_MULTIPLE_SOURCE_ROW_MATCHING_TARGET_ROW_IN_MERGE', 'noNewCommit': True})
    bad = out / 'additive-merge'
    create(spark, bad, [M.event('E123', 100)])
    frame(spark, [M.event('E123', 100)]).createOrReplaceTempView('additive_changes')
    additive_states = [100]
    for _ in range(2):
        spark.sql(f'''MERGE INTO delta.`{bad}` t USING additive_changes s
                      ON t.source_system=s.source_system AND t.app_id=s.app_id AND t.event_id=s.event_id
                      WHEN MATCHED THEN UPDATE SET t.revenue=t.revenue+s.revenue''')
        additive_states.append(read(spark, bad)[0]['revenue'])
    assert additive_states == [100, 200, 300]
    capture(spark, bad, out, 'non-idempotent-merge')
    return {'matrixHashes': {k: v['hash'] for k, v in states.items()}, 'states': {k: v['rows'] for k, v in states.items()},
            'duplicateSourceRejected': True, 'engineAmbiguityRejected': True, 'additiveReplay': additive_states}


def lab13(spark, out):
    result = M.time_semantics()
    assert result['eventDate'] == '2026-10-01' and result['incorrectProcessingDate'] == '2026-10-02'
    return result


def lab14(spark, out):
    target = out / 'attribution'
    snapshots = [M.event('E1', 0), M.event('E1', 100, 2, updated_at='2026-10-02T08:00:00Z'),
                 M.event('E1', 120, 3, updated_at='2026-10-03T08:00:00Z')]
    create(spark, target, [])
    results = []
    for index, e in enumerate(snapshots):
        current = merge(spark, target, [e])
        observed = capture(spark, target, out, f't{index}')
        expected = [e]
        recon = M.reconcile(expected, current)
        assert recon['pass'] and current[0]['revenue'] == [0, 100, 120][index]
        results.append({'revision': e['revision'], 'revenue': e['revenue'], 'hash': observed['hash'], 'reconciliation': recon})
    replay = merge(spark, target, snapshots)
    assert M.state_hash(replay) == results[-1]['hash']
    capture(spark, target, out, 'replay-all-snapshots')
    # Query scopes distinguish retrieval mechanisms; event-time-only15min selection misses both corrections.
    missed = [e for e in snapshots[1:] if e['event_time'] >= '2026-10-03T07:45:00Z']
    recovered = [e for e in snapshots if e['event_time'] >= '2026-09-30T08:00:00Z']
    assert not missed and len(recovered) == 3
    corrupted = [dict(replay[0], revenue=220)]
    bad = M.reconcile([snapshots[-1]], corrupted)
    assert not bad['pass']
    write_json(out / 'mismatch-reconciliation.json', bad)
    return {'timeline': results, 'finalRevenue': 120, 'naiveMissesCorrections': True,
            'lookbackHours': 72, 'recoveredRevisions': 3, 'replayHash': M.state_hash(replay), 'mismatchDetected': bad}


def lab15(spark, out):
    source = M.backfill_source()
    frozen_hash = M.state_hash(source)
    target, staging = out / 'production', out / 'staging'
    outside = M.event('LIVE', 77, event_time='2026-10-11T10:00:00Z')
    initial = [dict(r, revenue=1, revision=1) for r in source] + [outside]
    create(spark, target, initial)
    original = capture(spark, target, out, 'before-backfill')
    # A frozen snapshot feeds staging; failure occurs after37 completed day rows, before publication.
    create(spark, staging, source[:37])
    failure = None
    try:
        raise M.InjectedFailure('after_day37_before_publish')
    except M.InjectedFailure as exc:
        failure = str(exc)
    partial = capture(spark, staging, out, 'failed-after37')
    assert len(partial['rows']) == 37 and M.state_hash(read(spark, target)) == original['hash']
    completed = {r['event_id'] for r in read(spark, staging)}
    resume = [r for r in source if r['event_id'] not in completed]
    assert len(resume) == 53
    merge(spark, staging, resume)
    staged = read(spark, staging)
    validation = M.reconcile(source, staged)
    assert validation['pass'] and len(staged) == 90
    write_json(out / 'validation-before-publish.json', validation)
    predicate = "event_time >= '2026-01-01T00:00:00Z' AND event_time < '2026-04-01T00:00:00Z'"
    frame(spark, staged).coalesce(1).write.format('delta').mode('overwrite').option('replaceWhere', predicate).save(str(target))
    first = capture(spark, target, out, 'published')
    expected = source + [outside]
    recon = M.reconcile(expected, read(spark, target))
    assert recon['pass'] and first['hash'] == M.state_hash(expected)
    # Entire historical request rerun, with a newer live row outside the publish scope.
    live_new = dict(outside, revenue=88, revision=2)
    merge(spark, target, [live_new])
    merge(spark, staging, source)
    replay_validation = M.reconcile(source, read(spark, staging))
    assert replay_validation['pass'] and M.state_hash(source) == frozen_hash
    frame(spark, read(spark, staging)).coalesce(1).write.format('delta').mode('overwrite').option('replaceWhere', predicate).save(str(target))
    final = capture(spark, target, out, 'rerun-with-live-update')
    final_expected = source + [live_new]
    assert final['hash'] == M.state_hash(final_expected)
    # Compare affected scope exactly, even though unrelated live state legitimately changes.
    historical = [r for r in read(spark, target) if r['event_time'] < '2026-04-01T00:00:00Z']
    assert M.state_hash(historical) == frozen_hash
    return {'scope': '[2026-01-01,2026-04-01)', 'faultObserved': failure, 'completedBeforeFailure': 37, 'resumedDays': 53,
            'sourceSnapshotHash': frozen_hash, 'historicalRevenue': 900, 'liveRevenue': 88,
            'historicalHashAfterRerun': M.state_hash(historical), 'productionUnchangedBeforePublish': True,
            'validationBeforePublish': validation, 'finalReconciliation': M.reconcile(final_expected, read(spark, target))}


LABS = {'09': lab09, '10': lab10, '11': lab11, '12': lab12, '13': lab13, '14': lab14, '15': lab15}
