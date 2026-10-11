---
title: Streaming runtime evidence
description: Selected actual Spark/Delta query progress, checkpoints and target states.
---

# Streaming runtime evidence

Các artifacts được chọn từ `python scripts/test_streaming.py`, actual local Spark 4.0.4 + Delta 4.0.1. [Manifest](/evidence/streaming/manifest.json) ghi source run, runtime pin, completed stage count, raw file SHA-256 và normalized source hashes. Dataset tiny, single-writer; không benchmark và không Databricks workspace execution.

## Read the evidence

| Lab | Observation / contract | Artifact |
|---|---|---|
| 16 | Three controlled arrivals, active query, progress and clean stop | [JSON](/evidence/streaming/lab16/result.json) |
| 17 | Running aggregate state survives same-cp restart; query ID stable/run ID changes | [JSON](/evidence/streaming/lab17/result.json) |
| 18 | Same cp continuation; new cp rereads retained files into existing append target | [JSON](/evidence/streaming/lab18/result.json) |
| 19 | Controlled event-time advance, actual short-policy late drops/state removals vs long/no WM | [JSON](/evidence/streaming/lab19/result.json) |
| 20 | Within-horizon suppression, original-time late drop, refreshed-time duplicate after eviction | [JSON](/evidence/streaming/lab20/result.json) |
| 21 | Two-input progress, matching/delayed matches and unmatched outer NULL after closure | [JSON](/evidence/streaming/lab21/result.json) |
| 22 | Changed aggregate vs full snapshot vs finalized append rows | [JSON](/evidence/streaming/lab22/result.json) |
| 23 | Durable sink write then controlled failure; same batch retry, unsafe vs transactional effects | [JSON](/evidence/streaming/lab23/result.json) |
| 24 | Actual incompatible state-schema error; staged replay, reconciliation, original target preserved | [JSON](/evidence/streaming/lab24/result.json) |

[Runtime metadata](/evidence/streaming/runtime.json), [observed streaming configuration](/evidence/streaming/streaming-config.json), [test summary](/evidence/streaming/test-summary.json), [clean shutdown](/evidence/streaming/shutdown.json).

Progress snapshots include actual batch IDs, input rows/rates/durations, eventTime and stateOperators when applicable. foreachBatch actions can influence input-row metrics; use exact business states for correctness assertions. Processing-time warnings demonstrate trigger is not a deadline. No-data batches can advance cleanup without business rows; the tests do not assume a universal batch count.

Checkpoint inventories list actual metadata/source/offset/commit/state files. Raw checkpoint state, source paths and full Delta data files remain in the local run; published JSON records enough structure to explain boundaries. Artifacts are immutable evidence examples, not production recovery inputs.

## Failure and guarantee boundaries

Lab23 raises an exception **after** one durable Delta write and **before** the Spark engine commit. It reproduces retry uncertainty; it does not kill a process or prove remote REST guarantees. Native Delta streaming writes and ordinary DataFrameWriter inside foreachBatch have different transaction identities.

Lab24 changes aggregation grouping keys on a diagnostic copy of a real checkpoint. It reproduces state-schema incompatibility and replays retained input into isolated staging; it does not reproduce cloud checkpoint corruption or implement production cutover. Deleted checkpoint behavior is represented by new-cp file discovery in Lab18 and recovery fact patterns in Lab24.

Watermark proofs are conditional on controlled input order and observed progress. The policy is one-sided, not a universal exact lateness cutoff. Two-hour late-arrival tolerance does not solve 72-hour attribution corrections; source truth/reconciliation still matters.

## Reproduce and verify

```powershell
python scripts/test_streaming.py
python scripts/snapshot_streaming_evidence.py --run .skills-test/spark/tests-streaming/<successful-run>
python scripts/check_streaming_evidence.py
```

Snapshot accepts only a complete nine-test successful run with clean shutdown and source hashes matching those captured at execution start. The build checks selected file/source hashes and business/state/retry invariants. A changed source needs fresh execution and evidence; matching hashes do not prove the source contract is adequate for production.
