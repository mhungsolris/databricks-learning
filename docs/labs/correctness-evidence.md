---
title: Correctness runtime evidence
description: Business states, Delta histories, replay hashes và reconciliation từ local correctness labs.
---

# Correctness runtime evidence

Chạy trên accepted Spark 4.0.4/local[*], Java 17, Delta 4.0.1, official Docker image digest trong [runtime pin](/evidence/correctness/manifest.json). Money integer USD cents, UTC, stable source/app/event identity và ordered source revisions là explicit fixture contracts. Không có Databricks workspace hay advertising API calls.

## Read evidence by invariant

| Lab | Purpose | Selected artifacts |
|---|---|---|
| 09 | Responsibilities/grain; conserve revenue 170/cost 140 | [Result](/evidence/correctness/lab09/result.json), [grain contracts](/evidence/correctness/lab09/grain-contracts.json), [source-faithful deliveries](/evidence/correctness/lab09/bronze-payloads.json) |
| 10 | Created cursor drops B/E; ties/completeness assumptions | [Source snapshots and strategy decisions](/evidence/correctness/lab10/result.json) |
| 11 | Replay/ack retry keeps 100; append produces 300 | [Invariant summary](/evidence/correctness/lab11/result.json), [once](/evidence/correctness/lab11/once.json), [replay](/evidence/correctness/lab11/replay.json), [after-commit retry](/evidence/correctness/lab11/after-ack-failure-retry.json), [bad append](/evidence/correctness/lab11/append-duplicates.json) |
| 12 | Exact MERGE matrix; ambiguous source; bad additive update | [Matrix states/hashes](/evidence/correctness/lab12/result.json), [newer state/history](/evidence/correctness/lab12/newer.json), [actual engine ambiguity](/evidence/correctness/lab12/ambiguous-source-error.json), [additive history](/evidence/correctness/lab12/non-idempotent-merge.json) |
| 13 | Event date vs wrong processing date | [Timestamp trace and metrics](/evidence/correctness/lab13/result.json) |
| 14 | E1 latest 120, replay stable; corrupted 220 detected | [Timeline/reconciliation](/evidence/correctness/lab14/result.json), [final state/history](/evidence/correctness/lab14/t2.json), [replay history](/evidence/correctness/lab14/replay-all-snapshots.json), [mismatch output](/evidence/correctness/lab14/mismatch-reconciliation.json) |
| 15 | Failure 37/resume 53; validation before scoped publish; historical rerun stability | [Scope/resume/hash summary](/evidence/correctness/lab15/result.json), [validation before publish](/evidence/correctness/lab15/validation-before-publish.json), [rerun state/history](/evidence/correctness/lab15/rerun-with-live-update.json) |
| Adversarial | Unmatched source duplicates can insert 2 rows; preprocessed source 1 | [Observed results](/evidence/correctness/unmatched-duplicates/result.json) |

## Version and business state

Each actual Delta state snapshot has sorted business rows, SHA-256 and DESCRIBE HISTORY version/operation/metrics. Replay can add a MERGE commit without changing business state. Compare state/hash, not only version count. Named ambiguity error is intentionally asserted, including no-new-commit check.

Model Labs 09/10/13 prove deterministic business decisions; they do not claim deployed Medallion tables, source API completeness or streaming state. Labs 11/12/14/15 execute actual Delta writes. Lab 15 has 90 rows covering 90 days and two 37/53 chunks; LIVE outside scope is sequentially updated between publishes, not a simultaneous-writer stress test.

## Reproduce and provenance

```powershell
python scripts/run_correctness.py --lab all
python scripts/test_correctness.py
```

Open the printed run directory. [Manifest](/evidence/correctness/manifest.json) records source run, source/file hashes, runtime pin and observed completed-stage count; [integration summary](/evidence/correctness/test-summary.json) requires 9 tests, zero failures/errors/skips. [Runtime metadata](/evidence/correctness/runtime.json) records actual process configuration; [shutdown](/evidence/correctness/shutdown.json) confirms clean stop.

To refresh selected website artifacts, pass a successful 9-test run to `python scripts/snapshot_correctness_evidence.py --run <run-directory>`, then rebuild and browser-check. Raw data/logs remain ignored under .skills-test; only states/history/contract summaries needed for learning are published. Source hash checks detect later code drift.

## Limits

Python exceptions simulate read/write/ack and day 37 failures; process kill/checkpoint/distributed transaction recovery chưa test. Source revision and 72h mutation behavior are assumptions. Real API paging/retention/delete semantics, same-scope writer coordination, FX and production-sized distributed dedup need source-specific implementation. Streaming remains future curriculum.
