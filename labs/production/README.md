# Production hardening ROAS labs

Run bounded performance, quality, transformation and Delta recovery tests before preparing a workspace release. All input is synthetic, retained full-snapshot data. No live callbacks/cost connector, credentials or schedule is included.

## Artifacts and boundaries

| Artifact | Tier | What is checked |
|---|---|---|
| model.py, tests/test_contracts.py | PORTABLE | Scoped versions, quality, reconciliation, freshness and release contracts |
| src/transforms.py, scripts/test_production.py | LOCAL SPARK | Actual plans, skew, schema/rows and quality SQL |
| Same runtime suite | LOCAL DELTA | File layout, failed candidate and RESTORE commits |
| databricks.yml, resources/roas.job.yml | PORTABLE / CLI schema | Fields, paths, targets, identities and retry policy |
| src/roas.py | DATABRICKS WORKSPACE | Sandbox notebook, one staged/reconciled publication boundary |
| src/expectations.py | PORTABLE / LOCAL SPARK / WORKSPACE | AST and predicates locally; managed policies/metrics pending |
| .github/workflows/roas-release.yml | PORTABLE / WORKSPACE | Parsed control/privilege contracts; live workflow pending |
| quality-policy.json | PORTABLE | Policy decision fixture including invalid timestamp and delivery retry |
| sql/observability.sql | DATABRICKS WORKSPACE | Design-only query/job/billing investigations, not executed |

Full commands and acceptance policy: [production evidence](../../docs/labs/production-evidence.md). Course chapters31-45 and two gates cover evidence-ranked performance diagnosis and production readiness.

## Local checks

```powershell
python -m venv .skills-test/production-venv
.skills-test/production-venv/Scripts/python.exe -m pip install -r labs/production/requirements-test.txt
.skills-test/production-venv/Scripts/python.exe -m pytest labs/production/tests -q
python scripts/check_production_config.py
python scripts/test_production.py
python scripts/check_production_evidence.py
```

Linux uses `.skills-test/production-venv/bin/python` instead of the Windows executable. Docker runtime uses the existing Spark4.0.4/Delta4.0.1 pins, read-only source mount, disposable container and evidence mount.

CLI schema capture is archived in `.researches/2026-10-11-production-extra/cli-evidence/schema.json` and pinned by schema-provenance.json. Run the schema checker with the isolated test environment; Windows native-dependency policy may require the Linux container path documented in the evidence page. This checks field types against CLI1.20.0, not authenticated variable resolution or remote resource acceptance.

## Workspace acceptance

Status: **PENDING USER WORKSPACE**. Choose approved target workspace/profile, UC catalog, sandbox schema and service principal before authenticated commands. A paid enterprise release needs run/deploy privileges and workspace/UC permissions; Free Edition does not establish those capabilities.

Supply workspace_host/catalog/run_identity/operator_group variables outside Git. The root config uses dev/staging/prod targets, direct engine, enabled deployment lock, separate course sandbox schemas and target-specific workspace root. The run identity is an approved service principal; the observer group gets CAN_VIEW only. Source/namespace grants are administered outside this bundle.

Provision approved existing sandbox schemas before running. Review the notebook: it overwrites only the named bounded course fixture tables, stages Gold, validates exact expected rows and can intentionally fail before publication. It imports adjacent transforms/fixture from the deployed notebook directory; confirm that path/import behavior in the selected runtime during workspace acceptance. No table is a live production source or shared mart.

From this directory, after approved authentication:

```powershell
databricks --version
databricks bundle validate --strict -t dev --profile <approved-profile>
databricks bundle plan -t dev --profile <approved-profile>
databricks bundle deploy -t dev --fail-on-active-runs --profile <approved-profile>
databricks bundle run -t dev roas --profile <approved-profile>
```

Placeholders must be replaced in the learner's own terminal. Capture run identity, resolved resources/namespace, exact Gold1250/700, quality counters and forced-failure serving preservation; redact identifiers. Strict validation, deployment, notebook import/fixture paths, Job execution and serverless compatibility are all pending.

## Release policy

Manual cloud workflow uses a pinned CLI1.20.0 and pinned Action commits. Configure GitHub dev/staging/prod environments, environment variables, required reviewers and trusted-main branch restrictions. Configure narrow service-principal federation policies using the exact observed OIDC issuer/audience/subject. No PAT/client secret belongs in the repository.

The example promotes the same workflow commit through dev then staging; optional prod follows staging and its protected environment. It validates, creates/applies a target-specific plan and executes the sandbox integration run. No live Actions execution, environment protection or federation policy exists as evidence here.

Before adapting to real production, replace fixtures with approved retained manifests/source connectors, remove fixed1250/700 expectations in favor of authoritative scoped reconciliation, coordinate all writers and define notification/runbook owners. max_concurrent_runs1 only serializes this Job; root_path isolates deployment state, not table writes.

Code redeployment restores future behavior. Already committed wrong data requires independent retained-source repair/RESTORE and downstream reconciliation; bundle destroy is resource deletion, not rollback.
