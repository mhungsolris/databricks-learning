"""Verify selected local SQL evidence; optional snapshot requires a successful fresh run."""
import argparse
from hashlib import sha256
import json
from pathlib import Path
import shutil
from platform_evidence import ROOT, source_hashes

PUBLIC = ROOT / "docs/public/evidence/platform"
FILES = ["runtime.json", "shutdown.json", "test-summary.json", "result.json", "stages.json"]

def validate(folder):
    read = lambda name: json.loads((folder / name).read_text(encoding="utf-8"))
    summary = read("test-summary.json")
    assert summary["success"] and summary["tests"] == 6
    assert (summary["failures"], summary["errors"], summary["skipped"]) == (0, 0, 0)
    assert summary["sourceEncoding"] == "UTF-8 LF" and summary["sourceHashes"] == source_hashes()
    assert read("shutdown.json")["clean"]
    runtime = read("runtime.json")
    assert (runtime["sparkVersion"], runtime["master"]) == ("4.0.4", "local[*]")
    stages = read("stages.json")
    assert stages and len(stages) == summary["completedStages"]
    result = read("result.json")
    assert result["evidenceTier"] == "LOCAL SPARK TEST"
    assert result["workspaceStatus"] == "PENDING USER WORKSPACE"
    assert len(result["silver"]) == 4 and sum(r["amount_cents"] for r in result["silver"]) == 1250
    actual = {(r["app_id"], r["campaign_id"]): (r["revenue_cents"], r["cost_cents"]) for r in result["gold"]}
    assert actual == {("a", "A"): (1100, 400), ("a", "B"): (100, 200), ("b", "A"): (50, 100)}
    assert result["failureFanout"] == {"rows": 6, "revenueCents": 2500}
    assert result["zeroCost"]["allRoasNull"]
    assert result["equalRevisionConflict"]["groupsRejected"] == 1
    assert not result["expectationInputCounterexample"]["platformExpectationExecuted"]
    assert sum(r["revenue_cents"] for r in result["pipelineQuery"]) == 1250
    return summary

def main():
    cli = argparse.ArgumentParser()
    cli.add_argument("--snapshot", type=Path)
    args = cli.parse_args()
    if args.snapshot:
        run = args.snapshot.resolve()
        assert run.is_relative_to(ROOT / ".skills-test/spark/tests-platform"), "Unexpected evidence root"
        summary = validate(run)
        PUBLIC.mkdir(parents=True, exist_ok=True)
        for name in FILES:
            shutil.copyfile(run / name, PUBLIC / name)
        manifest = {"evidenceTier": "LOCAL SPARK TEST", "workspaceStatus": "PENDING USER WORKSPACE",
                    "verifiedDate": "2026-10-11", "timezone": "Asia/Saigon",
                    "sourceRun": run.relative_to(ROOT).as_posix(), "sourceEncoding": "UTF-8 LF",
                    "sourceHashes": summary["sourceHashes"],
                    "files": {n: sha256((PUBLIC / n).read_bytes()).hexdigest() for n in FILES}}
        (PUBLIC / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    validate(PUBLIC)
    manifest = json.loads((PUBLIC / "manifest.json").read_text(encoding="utf-8"))
    assert set(manifest["files"]) == set(FILES)
    assert manifest["sourceHashes"] == source_hashes()
    assert manifest["evidenceTier"] == "LOCAL SPARK TEST"
    assert manifest["workspaceStatus"] == "PENDING USER WORKSPACE"
    for name, expected in manifest["files"].items():
        assert sha256((PUBLIC / name).read_bytes()).hexdigest() == expected, name
    print(f"PASS platform local evidence: {len(FILES)} files, {len(manifest['sourceHashes'])} source hashes; cloud pending")

if __name__ == "__main__":
    main()
