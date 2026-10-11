# Platform conceptual and evidence audit

Scope: Chapters25-30, optional Free Edition setup, labs/platform artifacts and Platform Design gate. Official claims checked 2026-10-11. Local tests measure artifact/SQL contracts; actual workspace execution remains PENDING USER WORKSPACE.

| Review question | Treatment / evidence home | Boundary |
|---|---|---|
| Serverless interpreted as no compute? | Chapter25 names managed allocation, quotas/cost and compatibility | No managed compute executed |
| Jobs confused with compute? | Chapter26 separates workflow task from per-task execution | Config DAG tested, scheduler pending |
| Jobs confused with pipelines? | Chapter27 compares task coordination and dataset/flow processing | Static source graph vs inferred runtime graph explicitly separated |
| SDP/Lakeflow treated as interchangeable names? | SOURCES.md current terminology and extension matrix | Expectations are platform-only; Spark4.0.4 runtime unchanged |
| UC said to physically store data? | Chapter28 logical namespace and cloud backing diagram | No cloud storage credential configured |
| UC reduced to permissions? | Chapter28 ownership, lineage, audit, discovery and storage lifecycle | Metadata/persona tests pending |
| SQL described as only a Spark UI? | Chapter29 warehouse/BI/API/job interfaces | Actual SQL logic local; warehouse/history pending |
| BigQuery comparison obsolete? | Chapter29 compares two managed SQL offerings, capacity and data placement | Official Google/Databricks sources, no speed ranking |
| Airflow migration mandatory? | Chapters26/30 and gate accept an explicit hybrid boundary | One schedule/write owner required |
| Free Edition overclaimed? | Setup and every chapter name production limitations | No scale/network/SLA/admin/concurrency/cost/multi-workspace proof |

## Artifact review

The seven-task sample has two parallel ingest roots, a validation barrier, Silver/Gold/reconciliation and a failure report. It stores no account/profile/host, schedule or external notification destination. The sample replaces learner-owned retained snapshot tables; this is not production incremental publication.

Pipeline source uses distinct output names and batch materialized views over the same retained snapshot. Upstream validation rejects equal-revision conflicts; pipeline expectations demonstrate a proposed invalid-row fail policy. Static source tests and SQL tests do not claim actual platform graph/update behavior.

Governance fixture is an explicit access design, with PII separation and environment roles. Its predicate tests fixture rows only; it is not a UC privilege evaluator for ownership, group membership or inheritance. Enterprise identity/IAM/multi-workspace execution requires a separate authorized environment.

SQL tests include scoped identity/revision handling, repeat-result stability, ratio-of-sums, zero cost, duplicate dimension fan-out and conflicting equal revision. All money uses integer USD cents and dates/currency remain in the reporting grain.

## Known gaps

No Databricks CLI is available in this host, and no workspace/profile has been selected. Strict CLI/API config acceptance, deployment, Jobs failure/repair, real pipeline expectation failure/inferred graph, effective UC persona access and warehouse query history remain pending. No authenticated actions or signup automation were attempted.

Production acceptance needs external API/network contracts, workload identity/access review, representative load, end-to-end cutoff observability, target-specific writer isolation and retained-truth repair tests. Declarative Automation Bundles here is a sample representation; production deployment/CI gates remain planned.
