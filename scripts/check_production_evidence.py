"""Validate selected actual local performance/quality/Delta evidence, never cloud."""
import argparse
from hashlib import sha256
import json
from pathlib import Path
import shutil
from production_evidence import ROOT, source_hashes

PUBLIC = ROOT / "docs/public/evidence/production"
FILES = ["runtime.json", "shutdown.json", "test-summary.json", "result.json", "stages.json", "tasks.json"] + [n+"-plan.txt" for n in ["filter-select", "aggregate", "shuffle-join", "broadcast-join", "adaptive-aggregate", "skew", "tiny-scan", "compact-scan"]]

def validate(folder):
    read = lambda n: json.loads((folder/n).read_text(encoding="utf-8"))
    s=read("test-summary.json")
    assert s["success"] and s["tests"]==8 and (s["failures"],s["errors"],s["skipped"])==(0,0,0)
    assert s["sourceHashes"]==source_hashes() and s["sourceEncoding"]=="UTF-8 LF"
    assert read("shutdown.json")["clean"]
    assert read("runtime.json")["sparkVersion"]=="4.0.4" and read("runtime.json")["master"]=="local[*]"
    assert len(read("stages.json"))==s["completedStages"]>0
    tasks=read("tasks.json")
    assert tasks and sum(t["shuffleWriteBytes"] for t in tasks)>0
    r=read("result.json")
    assert r["evidenceTier"]=="LOCAL SPARK / LOCAL DELTA" and r["workspaceStatus"]=="PENDING USER WORKSPACE"
    assert not r["plans"]["filter-select"]["exchange"] and r["plans"]["aggregate"]["exchange"]
    assert r["plans"]["shuffle-join"]["exchange"] and r["plans"]["broadcast-join"]["broadcast"]
    assert r["adaptive"]["finalPlan"] and r["adaptive"]["configured"]
    assert r["skew"]["hotKeyRows"]==9000 and r["skew"]["total"]==10000 and r["skew"]["algebraPreserved"]
    assert not r["skew"]["productionSpeedupProven"]
    assert (r["layouts"]["tiny"]["files"], r["layouts"]["compact"]["files"])==(32,2)
    assert all(v["selectedRows"]==512 and v["addStatsPresent"] for v in r["layouts"].values())
    assert len(r["gold"])==3 and sum(x["revenue_cents"] for x in r["gold"])==1250 and sum(x["cost_cents"] for x in r["gold"])==700
    assert (r["quality"]["inputRows"],r["quality"]["validRows"],r["quality"]["quarantineRows"])==(9,6,3)
    assert not r["quality"]["platformExpectationExecuted"]
    assert r["failures"]==dict(unknownCostRows=1,fanoutRows=6,fanoutRevenue=2500)
    assert r["rollback"]["afterRestore"]==1250 and r["rollback"]["newVersion"]==2
    assert r["publication"]["originalPreserved"] and r["publication"]["servingRevenue"]==1250
    for n in FILES:
        assert (folder/n).is_file()
    assert "BroadcastHashJoin" in (folder/"broadcast-join-plan.txt").read_text()
    return s

def main():
    cli=argparse.ArgumentParser(); cli.add_argument("--snapshot",type=Path); args=cli.parse_args()
    if args.snapshot:
        folder=args.snapshot.resolve()
        assert folder.is_relative_to(ROOT/".skills-test/spark/tests-production")
        summary=validate(folder)
        PUBLIC.mkdir(parents=True,exist_ok=True)
        for name in FILES:
            shutil.copyfile(folder/name,PUBLIC/name)
        manifest=dict(evidenceTier="LOCAL SPARK / LOCAL DELTA",workspaceStatus="PENDING USER WORKSPACE",
                      verifiedDate="2026-10-11",sourceRun=folder.relative_to(ROOT).as_posix(),sourceEncoding="UTF-8 LF",
                      sourceHashes=summary["sourceHashes"],files={n:sha256((PUBLIC/n).read_bytes()).hexdigest() for n in FILES})
        (PUBLIC/"manifest.json").write_text(json.dumps(manifest,indent=2),encoding="utf-8")
    validate(PUBLIC)
    m=json.loads((PUBLIC/"manifest.json").read_text())
    assert m["sourceHashes"]==source_hashes() and set(m["files"])==set(FILES)
    assert m["evidenceTier"]=="LOCAL SPARK / LOCAL DELTA" and m["workspaceStatus"]=="PENDING USER WORKSPACE"
    for n,h in m["files"].items():
        assert sha256((PUBLIC/n).read_bytes()).hexdigest()==h,n
    print(f"PASS production evidence: {len(FILES)} artifacts, {len(m['sourceHashes'])} startup source hashes; cloud pending")

if __name__=="__main__":
    main()
