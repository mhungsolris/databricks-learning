"""Bounded snapshot contracts. Integer cents, UTC dates, source-scoped identity."""
from datetime import datetime, timezone

KEY = ("source_system", "app_id", "event_id")
GRAIN = ("source_system", "app_id", "event_date", "campaign_id", "currency")

def key(row, fields):
    return tuple(row[f] for f in fields)

def reasons(row):
    errors = []
    if any(not row.get(f) for f in KEY):
        errors.append("identity")
    if not isinstance(row.get("amount_cents"), int) or isinstance(row.get("amount_cents"), bool) or row["amount_cents"] < 0:
        errors.append("amount")
    if row.get("currency") != "USD":
        errors.append("currency")
    try:
        datetime.strptime(row.get("event_date", ""), "%Y-%m-%d")
    except (TypeError, ValueError):
        errors.append("date")
    if not isinstance(row.get("revision"), int) or isinstance(row.get("revision"), bool) or row["revision"] < 1:
        errors.append("revision")
    return errors

def quality(rows):
    good, quarantine, warnings = [], [], []
    for row in rows:
        failures = reasons(row)
        if failures:
            quarantine.append(dict(row=row, reasons=failures))
        else:
            good.append(dict(row))
            if row.get("country") == "UNKNOWN":
                warnings.append(dict(delivery_id=row["delivery_id"], reason="country"))
    return dict(valid=good, quarantine=quarantine, warnings=warnings,
                input_rows=len(rows), invalid_rows=len(quarantine))

def silver(rows):
    latest, versions = {}, {}
    for row in rows:
        if reasons(row):
            raise ValueError("INVALID_INPUT")
        k = key(row, KEY)
        payload = key(row, GRAIN) + (row["amount_cents"],)
        version = k + (row["revision"],)
        if version in versions and versions[version] != payload:
            raise ValueError("EQUAL_REVISION_CONFLICT")
        versions[version] = payload
        if k not in latest or (row["revision"], row["delivery_id"]) > (latest[k]["revision"], latest[k]["delivery_id"]):
            latest[k] = dict(row)
    return sorted(latest.values(), key=lambda r: key(r, KEY))

def gold(events, costs):
    revenue, cost_index = {}, {}
    for r in events:
        k = key(r, GRAIN)
        revenue[k] = revenue.get(k, 0) + r["amount_cents"]
    for r in costs:
        k = key(r, GRAIN)
        if k in cost_index or r["cost_cents"] < 0:
            raise ValueError("INVALID_COST_GRAIN")
        cost_index[k] = r["cost_cents"]
    if set(revenue) - set(cost_index):
        raise ValueError("UNKNOWN_COST")
    return [dict(zip(GRAIN, k), revenue_cents=revenue.get(k, 0), cost_cents=c,
                 roas=(revenue.get(k, 0) / c if c else None))
            for k, c in sorted(cost_index.items())]

def reconcile(events, costs, candidate):
    expected = gold(events, costs)
    if candidate != expected:
        raise ValueError("RECONCILIATION_FAILED")
    return dict(revenue_cents=sum(r["revenue_cents"] for r in candidate),
                cost_cents=sum(r["cost_cents"] for r in candidate), rows=len(candidate))

def health(*, now, revenue_cutoff, cost_cutoff, max_age_seconds, job_status, mismatch):
    for t in (now, revenue_cutoff, cost_cutoff):
        if t.tzinfo is None or t.utcoffset() != timezone.utc.utcoffset(t):
            raise ValueError("UTC_REQUIRED")
    age = (now - min(revenue_cutoff, cost_cutoff)).total_seconds()
    if age < 0:
        raise ValueError("FUTURE_CUTOFF")
    return dict(job_status=job_status, age_seconds=age,
                publish_ready=job_status == "SUCCESS" and age <= max_age_seconds and not mismatch)
