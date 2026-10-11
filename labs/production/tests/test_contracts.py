"""Portable pytest checks, including deliberate failures and release contracts."""
import ast
from copy import deepcopy
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import sys
import pytest
import yaml

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from labs.production.model import gold, silver, quality, reconcile, health
from scripts.check_production_config import validate

@pytest.fixture
def fixture():
    data = json.loads((ROOT / "labs/production/src/fixtures.json").read_text())
    events = "delivery_id source_system app_id event_id revision campaign_id event_date currency amount_cents".split()
    costs = "source_system app_id event_date campaign_id currency cost_cents".split()
    return {"events": [dict(zip(events, r)) for r in data["events"]],
            "costs": [dict(zip(costs, r)) for r in data["costs"]]}

def test_transformation_scoped_revision_and_retry(fixture):
    result = silver(fixture["events"])
    assert len(result) == 4 and sum(r["amount_cents"] for r in result) == 1250
    assert silver(fixture["events"] * 2) == result
    candidate = gold(result, fixture["costs"])
    assert reconcile(result, fixture["costs"], candidate) == dict(revenue_cents=1250, cost_cents=700, rows=3)

def test_conflicting_equal_revision_rejected(fixture):
    bad = dict(fixture["events"][0], amount_cents=999)
    with pytest.raises(ValueError, match="EQUAL_REVISION_CONFLICT"):
        silver(fixture["events"] + [bad])

@pytest.mark.parametrize("change,reason", [({"event_id": None}, "identity"), ({"amount_cents": -1}, "amount"), ({"event_date": "not-a-date"}, "date")])
def test_quarantine_accounts_for_loss(fixture, change, reason):
    rows = fixture["events"] + [dict(fixture["events"][0], **change)]
    q = quality(rows)
    assert len(q["valid"]) + len(q["quarantine"]) == q["input_rows"] == 7
    assert reason in q["quarantine"][0]["reasons"]

def test_country_warning_retains_business_row(fixture):
    row = dict(fixture["events"][0], country="UNKNOWN")
    assert quality([row])["valid"] == [row]
    assert quality([row])["warnings"]

def test_duplicate_cost_and_missing_cost_block_publication(fixture):
    events = silver(fixture["events"])
    with pytest.raises(ValueError, match="INVALID_COST_GRAIN"):
        gold(events, fixture["costs"] * 2)
    with pytest.raises(ValueError, match="UNKNOWN_COST"):
        gold(events, fixture["costs"][1:])

def test_zero_cost_and_wrong_candidate(fixture):
    events = silver(fixture["events"])
    costs = [dict(r, cost_cents=0) for r in fixture["costs"]]
    assert all(r["roas"] is None for r in gold(events, costs))
    with pytest.raises(ValueError, match="RECONCILIATION_FAILED"):
        reconcile(events, fixture["costs"], gold(events, fixture["costs"]) * 2)

def test_success_stale_is_not_ready():
    now = datetime(2026, 10, 1, 12, tzinfo=timezone.utc)
    assert not health(now=now, revenue_cutoff=now, cost_cutoff=now-timedelta(hours=1), max_age_seconds=900, job_status="SUCCESS", mismatch=False)["publish_ready"]
    assert health(now=now, revenue_cutoff=now, cost_cutoff=now, max_age_seconds=900, job_status="SUCCESS", mismatch=False)["publish_ready"]

def test_target_isolation_and_mutation_rejection():
    bundle, job = validate()
    bad = deepcopy(bundle)
    bad["targets"]["prod"]["variables"]["schema"] = bad["targets"]["dev"]["variables"]["schema"]
    with pytest.raises(AssertionError):
        validate(bad, job)

def test_expectation_decorators_are_design_examples():
    tree = ast.parse((ROOT / "labs/production/src/expectations.py").read_text())
    calls = [n for n in ast.walk(tree) if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) and n.func.attr.startswith("expect")]
    assert {n.func.attr for n in calls} == {"expect", "expect_or_drop", "expect_or_fail"}
    assert all(len(n.args) == 2 and all(isinstance(a, ast.Constant) and isinstance(a.value, str) for a in n.args) for n in calls)

def test_ci_yaml_privileges_and_promotion():
    w = yaml.safe_load((ROOT / ".github/workflows/roas-release.yml").read_text())
    assert set(w["on"]) == {"workflow_dispatch"}
    assert w["permissions"] == {"contents": "read"}
    assert w["concurrency"]["cancel-in-progress"] is False
    assert set(w["jobs"]) == {"checks", "dev", "staging", "prod"}
    for name, predecessor in [("dev", "checks"), ("staging", "dev"), ("prod", "staging")]:
        j = w["jobs"][name]
        assert j["needs"] == [predecessor] and j["environment"] == name
        assert "refs/heads/main" in j["if"]
        assert j["permissions"] == {"contents": "read", "id-token": "write"}
        assert j["env"]["DATABRICKS_AUTH_TYPE"] == "github-oidc"
        text = "\n".join(s.get("run", "") for s in j["steps"])
        assert text.index("bundle validate --strict") < text.index("bundle plan") < text.index("bundle deploy") < text.index("bundle run")
        assert "--fail-on-active-runs" in text and "--plan plan.json" in text
        assert all(len(s["uses"].split("@")[1]) == 40 for s in j["steps"] if "uses" in s)
    assert "inputs.release_prod" in w["jobs"]["prod"]["if"]
    assert "TOKEN" not in json.dumps(w) and "secrets." not in json.dumps(w)

def test_existing_pages_yaml_is_parseable():
    w = yaml.safe_load((ROOT / ".github/workflows/pages.yml").read_text())
    assert w["permissions"] == {"contents": "read"}
    assert set(w["jobs"]["deploy"]["needs"]) == {"build", "spark"}
    assert "pull_request" in w["jobs"]["deploy"]["if"]

def test_notebook_publication_barrier():
    text = (ROOT / "labs/production/src/roas.py").read_text()
    ast.parse(text)
    assert text.index('raise ValueError("QUALITY_GATE_FAILED")') < text.index('saveAsTable("gold_candidate")')
    assert text.index('EXACT_SCOPED_RECONCILIATION_FAILED') < text.index('INTENTIONAL_FAILURE_BEFORE_PUBLICATION') < text.index('CREATE OR REPLACE TABLE gold_roas')
    assert 'exceptAll(expected)' in text and 'expected.exceptAll(ordered)' in text
