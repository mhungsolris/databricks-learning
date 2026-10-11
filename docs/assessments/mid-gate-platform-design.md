---
title: Mid Gate · Databricks Platform Design
description: Reasoned platform migration with explicit boundaries and evidence tiers.
prev:
  text: 'Lab 30'
  link: /labs/30-platform-boundaries
next:
  text: Performance engineering
  link: /production/31-performance-mental-model
---

# Mid Gate · Databricks Platform Design

Design a migration that preserves business correctness while introducing useful Databricks capabilities. Feature count earns no credit. Keeping Airflow or dbt is a valid choice when supported by requirements.

## Case

Current stack: Airflow, GCS, BigQuery and dbt. External adapters extract API data. The company wants to incorporate Databricks for a callback path with 15-minute freshness, hourly cost ingestion, late arrivals and mutable 72-hour attribution. BI users include Marketing and Finance. Environments are dev/staging/prod; sensitive donor/customer PII is separately governed. Consumers need source lineage and safe repair/replay.

These are synthetic assessment requirements, not guarantees from any API vendor. The freshness target needs a decision: provisional revenue versus finalized cost-adjusted ROAS.

## Required design

1. State what moves and stays, with source adapters/auth/network responsibilities, retained input and authoritative repair boundary.
2. Choose compute per task/interface, including serverless compatibility checks and classic fallback conditions.
3. Separate Jobs task graph from pipeline dataset graph. Explain where Spark/dbt imperative or declarative processing belongs.
4. Design UC hierarchy, principal/run identity, ownership and least privilege for DE, Marketing, Finance and service principal. Keep raw PII isolated; explain lineage/audit gaps.
5. Choose SQL serving/BI access and warehouse/data privileges; specify grain, currencies and freshness cutoffs.
6. Give a Databricks-centric and a hybrid design, one schedule owner per boundary, retry/repair behavior and a migration rollback/cutover plan.
7. Trace validation failure, uncertain run submission, late correction, missing retained truth and unauthorized Finance PII access.
8. State evidence tier for every claim. Provide local/config proofs and list required workspace/production tests without fabricating them.

## Submission and rubric

Submit two diagrams, a workload/compute table, task and dataset dependencies, ownership/access matrix, retained-truth/recovery contracts and expected/actual evidence by tier.

| Competence | Full-credit reasoning | Critical failure |
|---|---|---|
| Responsibilities | Moves/stays tied to SLA, source constraints and team ownership | “Databricks handles everything” |
| Compute | Per workload support/compatibility and quota/cost owner | Serverless interpreted as no compute |
| Orchestration | One owner, task DAG separate from dataset dependencies | Job = cluster or Jobs = pipelines |
| Processing correctness | Full key/version, retained truth, mutation/replay and reconciliation | Scheduler success presented as data correctness |
| Governance | Ownership, traversal/action privileges, PII isolation, lineage/audit | UC interpreted as physical data storage or grants only |
| SQL serving | BI and data access, stable grain/freshness | Databricks SQL interpreted as notebook UI |
| Hybrid trade-offs | Two defensible designs, conditions for changing choice | Airflow migration assumed mandatory |
| Evidence | Portable/local/workspace/production scope clearly separated | Free Edition claimed as production proof |

PASS requires all critical competencies and correction of any critical failure. NOT YET until assumptions and failure paths are consistent. Workspace execution may remain PENDING USER WORKSPACE, without blocking a reasoned design submission. Reviewer asks which new constraint would change a decision; memorized product descriptions do not satisfy the gate.
