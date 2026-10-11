---
title: Platform evidence and workspace boundary
description: Distinguish artifact checks, local SQL execution and real workspace evidence.
---

# Platform evidence and workspace boundary

Platform artifacts live in labs/platform/. The repository distinguishes portable validation from local Spark execution and Databricks workspace execution. Current cloud state: `PENDING USER WORKSPACE`.

| Capability | PORTABLE TEST | LOCAL SPARK TEST | DATABRICKS WORKSPACE TEST |
|---|---|---|---|
| Compute | Ten workload reasoning cards | Existing engine baseline; no managed compute | Pending availability evidence |
| Jobs | DAG/dependency, task config and source checks | Notebook SQL extraction/outputs, not scheduler | Pending run/failure/repair |
| Pipeline | Source AST, named dependency graph | Same bounded SQL semantics; no SDP engine | Pending inferred graph/update/expectation failure |
| Unity Catalog | Policy-fixture separation and traversal checks | No UC enforcement | Pending owned hierarchy; enterprise persona tests deferred |
| Databricks SQL | Query-source contracts | Aggregation/filter/join/serving and failure counterexamples | Pending warehouse/query history |
| Platform gate | Reasoning rubric and two architecture designs | No migration execution | Pending production acceptance exercises |

## Reproduce local evidence

```powershell
python -m unittest discover -s tests -v
python scripts/test_platform.py
```

The integration script uses the pinned local Spark4.0.4/Delta4.0.1 Docker runtime, reads the actual notebook SQL and pipeline source, and writes results/runtime/shutdown/stages under ignored .skills-test/spark/tests-platform/. It does not mock a Databricks API, import the unavailable SDP module or submit cloud jobs. [Selected local evidence](/evidence/platform/manifest.json) links exact files and source hashes; [results](/evidence/platform/result.json) contains bounded outputs. The build checks integrity and runtime-source hashes.

Measured local run: six tests passing, 83 completed Spark stages and clean session shutdown. The selected manifest contains five files and 18 normalized-source hashes captured at execution start. SELECT semantics ran on Spark4.0.4; this test does not use Delta writes, managed Jobs, SDP, UC or a SQL warehouse. The separate accepted runtime suites verify Delta4.0.1.

## Workspace evidence collection

Use [Free Edition preflight](/setup/databricks-free-edition) and the relevant lab. Record feature availability, compute/environment label, redacted DAG or inferred graph, named task states/attempts, query outputs, expected/actual invariants and failure diagnosis. Retain original evidence privately; submit a redacted copy only after review.

Recommended record fields:

```json
{
  "evidenceTier": "DATABRICKS WORKSPACE TEST",
  "status": "PENDING USER WORKSPACE",
  "lab": 26,
  "features": {},
  "compute": "not yet observed",
  "attempts": [],
  "invariants": [],
  "redactionReviewed": false
}
```

Change status to executed only when actual observations exist. Static config, expected task states, hand-drawn Mermaid and screenshots from documentation are not workspace evidence.

Before committing evidence, remove account/metastore/job/pipeline/warehouse IDs, workspace URLs, names/emails, tokens, request headers and sensitive paths. Replace correlated identifiers with stable labels such as run-A and task-validate. Review image pixels as well as JSON fields and filenames. Do not put unreviewed exports into docs/public. The repository private-data guard catches common patterns but human redaction review remains necessary.

## Known unverified boundaries

CLI strict bundle validation/deploy, real scheduler retries/repair, pipeline graph/update and expectation failure, effective UC grants across identities, SQL warehouse/query history and platform networking have not run. One local run does not establish cloud scale, concurrency, SLA or cost. Detailed verification records belong to PROGRESS.md.
