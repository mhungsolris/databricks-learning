# Platform lab artifacts

These are bounded synthetic learning artifacts, with cloud execution PENDING USER WORKSPACE. See docs/setup/databricks-free-edition.md and docs/labs/platform-evidence.md for prerequisites and evidence policy.

databricks.yml and resources/*.yml use JSON-compatible YAML. They define one seven-task notebook Job and one triggered serverless Lakeflow pipeline. catalog/schema variables are required; choose an existing accessible catalog and a unique learner-owned course_roas_ schema. No host, profile, token, schedule or notification destination is stored here.

| Artifact | Purpose | Validation boundary |
|---|---|---|
| src/roas_task.py | Six data stages and failure-report branch | AST + extracted actual SQL tested locally, scheduler pending |
| src/medallion.py | Bronze/Silver/Gold materialized-view definitions and fail expectations | AST + SQL semantics; SDP/DBR execution pending |
| fixtures.json | Six deliveries, three costs, scoped identities/revisions | Local SQL and retry/grain counterexamples |
| sql/silver.sql, gold.sql | Standalone equivalent transformation queries | Actual local Spark |
| sql/serving.sql | Four analyst query types | Actual local Spark |
| sql/governance.sql | Administrator-reviewed design example | Syntax/read review only, not applied |
| governance-policy.json | Environment/PII/role design fixture | Contract assertions, not UC access enforcement |

Pipeline input is raw_events produced by the Jobs ingest stage. Its outputs use distinct names to avoid competing with Jobs writers. The batch snapshot resolves revisions and requires upstream equal-revision conflict validation. It is not an append streaming/CDC demonstration. Expectations use a Lakeflow-only extension, so this entire source is not OSS-portable.

Learner sequence: run Job once, inspect expected output, inject validation failure and repair with a retained snapshot, then run the pipeline and its quality failure exercise, inspect owned UC objects and serve SQL. Stop extra runs when done. Never apply these CREATE OR REPLACE statements to a production schema.

Local commands from repository root:

```powershell
python -m unittest discover -s tests -v
python scripts/test_platform.py
```

After user-owned OAuth/profile selection, work here and set BUNDLE_VAR_catalog and BUNDLE_VAR_schema. Run databricks bundle validate --strict --target dev --profile with the chosen profile. Strict workspace validation has not run here. Deployment/run remains a deliberate learner action; the course introduces the representation only, leaving production CI/CD to the planned track.
