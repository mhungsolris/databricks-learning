"""Portable course contracts, not Databricks CLI/schema or remote validation."""
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "labs/production"

def validate(bundle=None, job=None):
    bundle = bundle or json.loads((BASE / "databricks.yml").read_text())
    job = job or json.loads((BASE / "resources/roas.job.yml").read_text())["resources"]["jobs"]["roas"]
    assert set(bundle["targets"]) == {"dev", "staging", "prod"}
    assert bundle["include"] == ["resources/*.yml"]
    assert bundle["bundle"]["engine"] == "direct"
    assert bundle["bundle"]["deployment"]["lock"]["enabled"] is True
    for name in ("workspace_host", "catalog", "run_identity", "operator_group"):
        assert "default" not in bundle["variables"][name], name
    roots, schemas = set(), set()
    for name, target in bundle["targets"].items():
        assert target["mode"] == ("development" if name == "dev" else "production")
        schema = target["variables"]["schema"]
        assert schema == f"course_roas_{name}_sandbox"
        schemas.add(schema)
        root = target["workspace"]["root_path"]
        assert "${bundle.target}" in root and "${bundle.name}" in root
        roots.add(root.replace("${bundle.target}", name))
        assert target["workspace"]["host"] == "${var.workspace_host}"
        assert target["run_as"]["service_principal_name"] == "${var.run_identity}"
    assert len(roots) == len(schemas) == 3
    assert job["max_concurrent_runs"] == 1 and "schedule" not in job
    assert len(job["tasks"]) == 1
    task = job["tasks"][0]
    assert task["max_retries"] == 1 and task["retry_on_timeout"] is False
    assert task["notebook_task"]["notebook_path"] == "../src/roas.py"
    assert (BASE / "resources" / task["notebook_task"]["notebook_path"]).resolve().is_file()
    assert job["permissions"] == [{"group_name": "${var.operator_group}", "level": "CAN_VIEW"}]
    assert {p["name"]: p["default"] for p in job["parameters"]} == {
        "catalog": "${var.catalog}", "schema": "${var.schema}", "force_failure": "false"}
    text = json.dumps(bundle) + json.dumps(job)
    assert not re.search(r"dapi[a-f0-9]{32}|DATABRICKS_TOKEN|https://[^ ]*cloud.databricks.com", text)
    return bundle, job

if __name__ == "__main__":
    validate()
    print("PASS portable bundle contracts: paths, isolation, identity variables, bounded retries; CLI/cloud pending")
