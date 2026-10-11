---
title: 'Lab 26 · ROAS Job DAG'
prev:
  text: 'Chapter 26'
  link: /platform/26-lakeflow-jobs
next:
  text: 'Chapter 27'
  link: /platform/27-declarative-pipelines
---

# Lab 26 · ROAS Job DAG

DATABRICKS FREE EDITION LAB: proposed execution, currently PENDING USER WORKSPACE. PORTABLE TEST checks artifact dependencies, not scheduler behavior.

1. Complete [setup preflight](/setup/databricks-free-edition). Choose catalog and a unique course_roas_ schema. Review labs/platform/databricks.yml/resources/roas.job.yml. Two ingest roots → validate → silver → gold → reconcile; failure_report runs on AT_LEAST_ONE_FAILED across data stages.
2. Use a manually entered equivalent notebook Job, or user-owned strict bundle validation followed by deliberate deployment. Each task calls src/roas_task.py with stage matching task_key. Supply catalog/schema and force_validation_failure=false as job parameters. Keep max_concurrent_runs=1, sample timeout600s, validation retries0; reuse notebook serverless compute where supported.
3. Run once. Expected six raw deliveries, four Silver identities, three Gold rows, revenue1250/cost700 cents; a/A=1100/400, a/B=100/200, b/A=50/100. Capture redacted actual task DAG/states and reconciliation output.
4. Start a new run with force_validation_failure=true. Ingest overwrites only these owned snapshot tables; validation fails intentionally before Gold refresh. Predict downstream states first. Expected Silver/Gold/reconcile upstream-failed; failure_report executes. Existing Gold may retain its last successful snapshot, so freshness needs inspection.
5. Fix the parameter and repair unsuccessful data tasks/dependents. Inspect repair selection so successful ingestion stays untouched when its retained snapshot remains valid. Capture old/new task attempts, input counts/cutoff, output invariant and any automatic platform retries. No failure notification destination is configured.
6. Retry a data stage safely and compare exact owned snapshot values, not only task status. Stop further runs after evidence capture.

If a feature/repair option is unavailable, record its observed limitation and mark that part pending. Do not simulate a Jobs run screenshot. [Local evidence](/labs/platform-evidence) validates SQL separately. Production writers need scoped merge/replay/publish contracts from Chapters11-15; this lab's full overwrite is safe only for its isolated sample snapshot.

PASS: successful and failed runs/repair traced if executed, or correct predicted path with pending evidence clearly labeled. NOT YET: retry claimed as idempotency without target proof.

