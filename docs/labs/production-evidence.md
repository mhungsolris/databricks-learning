---
title: Production hardening evidence
description: Actual local performance/quality/release observations and explicit workspace boundaries.
---

# Production hardening evidence

Selected evidence proves bounded Spark4.0.4/Delta4.0.1 behavior and portable release contracts. Databricks execution remains **PENDING USER WORKSPACE**. No local elapsed time is a production benchmark.

## Evidence tiers

| Tier | Labs | Evidence | Does not prove |
|---|---|---|---|
| PORTABLE | 31,34-44 design/config/tests | Hypotheses, pure pytest, AST, parsed YAML, isolation contracts | Grants, API acceptance, cloud execution |
| LOCAL SPARK | 32,36,39-41 | Real plans/AQE, shuffle/task metrics, skew, schema and rows | Distributed production speedup, Photon |
| LOCAL DELTA | 33,45 | Active files/stats, staged failure, restore commit | Liquid clustering/AUTO, managed optimization |
| DATABRICKS WORKSPACE | Optional 34-35,38,40,43-45 | Required strict validation/deploy/run/log/profile/access evidence | Not present in this baseline |

## Reproduce local checks

Run from repository root using the existing [local runtime setup](/setup/local-spark). Test packages are isolated from the Spark runtime and website dependencies.

```powershell
python -m venv .skills-test/production-venv
.skills-test/production-venv/Scripts/python.exe -m pip install -r labs/production/requirements-test.txt
.skills-test/production-venv/Scripts/python.exe -m pytest labs/production/tests -q
python scripts/check_production_config.py
python scripts/test_production.py
python scripts/check_production_evidence.py
```

Use venv/bin/python on Linux. The runtime suite creates a unique evidence folder, records source hashes at startup, runs eight tests, stops Spark cleanly and captures plans/events/tasks. Publish only a successful run whose source hashes still match:

```powershell
python scripts/check_production_evidence.py --snapshot .skills-test/spark/tests-production/<successful-run>
```

The selected [manifest](/evidence/production/manifest.json) binds14 files and source fingerprints; the build guard checks them. [Results](/evidence/production/result.json), [task metrics](/evidence/production/tasks.json), [stages](/evidence/production/stages.json) and [test summary](/evidence/production/test-summary.json) expose actual observations. Raw event logs and Delta files remain ignored local evidence.

## Performance observations

Read [filter/select](/evidence/production/filter-select-plan.txt), [aggregate](/evidence/production/aggregate-plan.txt), [shuffle join](/evidence/production/shuffle-join-plan.txt), [broadcast join](/evidence/production/broadcast-join-plan.txt), [adaptive final plan](/evidence/production/adaptive-aggregate-plan.txt) and [skew](/evidence/production/skew-plan.txt). A filter/project has no Exchange, aggregate/shuffle join have movement, explicit bounded dimension broadcast produces BroadcastHashJoin. AQE is tested separately from the default disabled baseline.

The controlled10000-row skew case has9000 UNKNOWN rows and a hot hash partition. Two-phase salted counts preserve exact campaign counts. This validates aggregation algebra and observed distribution; no performance speedup is asserted.

Same4096-row local Delta snapshot produces32 tiny files versus2 fewer files with stats. Both narrow filters select512 rows and preserve sum(id). See [tiny scan](/evidence/production/tiny-scan-plan.txt), [compact scan](/evidence/production/compact-scan-plan.txt) and recorded file sizes/input partitions. Planning partitions may combine files. No skipping improvement, universal target size or production latency claim follows from this dataset.

Task metrics include durations, shuffle read/write and spill counters from actual SparkListenerTaskEnd events. They describe this run only; zero local spill is not production memory proof. Scenario8→35m,40m and5→25m figures in chapters/gates are synthetic incident inputs.

### Selected local layout measurements

| Layout | Active files | Min/median/max bytes | Planning input partitions | Narrow output rows |
|---|---|---|---|---|
| tiny | 32 | 1411/1416/1422 | 8 | 512 |
| compact | 2 | 9821/9828/9835 | 2 | 512 |

Both commits have add-file statistics. Uniform day values across the write partitions provide no measured skipping benefit here. File count and planning partitions are separate observations; no elapsed-time ranking is asserted.

## Quality and release observations

Retried/revised scoped inputs produce4 Silver identities and3 Gold grains, revenue1250/cost700. DataFrame tests check exact rows, schema, uniqueness, source/candidate sums and repeat stability.

Null ID, negative money and invalid date yield3 quarantine rows from9 inputs. Local SQL evaluates expectation expressions, but managed decorators/metrics are not executed. Duplicate cost yields6 Gold rows/revenue2500; missing cost remains visible as an unmatched row and blocks the portable publication contract.

Local Delta wrong commit doubles revenue1250→2500. Selecting good code leaves2500 in storage; restoreToVersion(0) creates a new version2 and returns1250. No VACUUM ran. Failed staged candidate leaves original serving1250 unchanged. No multi-table atomicity, concurrent cloud writers, retention-expired restore or downstream streaming RESTORE was executed.

## Bundle and CI acceptance

Course config is JSON-compatible YAML, parsed by Python and PyYAML. Static contracts check three schemas, deployment roots, required external identity/host/catalog variables, relative source paths, one necessary Job, serialized runs and bounded retries. CLI-generated JSON schema validation is local; strict resolved-target validation still needs a workspace.

Pinned CLI1.20.0 is downloaded only into an ignored repository folder for unauthenticated help/schema capture, not installed globally or authenticated. The release workflow is manual and uses narrow environment-scoped GitHub OIDC. Review exact federation trust and configure required reviewers/branch protection administratively; YAML cannot prove those settings.

With an approved current CLI already available, the unauthenticated schema commands are:

```powershell
databricks version --output json
databricks bundle schema | Set-Content -Encoding UTF8 .skills-test/bundle-schema.json
.skills-test/production-venv/Scripts/python.exe scripts/check_bundle_schema.py .skills-test/bundle-schema.json
```

The validator uses the captured schema unchanged and a Unicode-capable regex engine for CLI patterns. Type violations are rejected; some semantic mode strings are allowed by the CLI schema and are enforced by the separate course config contract. Windows application control blocked the validator's native dependency during this verification, so the actual schema check ran in a disposable Linux container with the same pinned validator packages. No system security policy was changed.

The optional cloud runbook lives in `labs/production/README.md`. Workspace acceptance must cover resolved variables/grants, deployed imports/fixture path, successful Job, forced pre-publication failure, scoped Gold values and redacted logs. Photon/profile, liquid clustering/AUTO, predictive maintenance, system tables and expectation metrics each need separate supported-capability evidence. Free Edition capability gaps remain explicit.

The exact CLI schema/help/provenance capture is archived under `.researches/2026-10-11-production-extra/cli-evidence/`; `labs/production/schema-provenance.json` pins its canonical hash. The checker refuses an unreviewed schema change. You can validate the saved schema without installing a CLI:

```powershell
.skills-test/production-venv/Scripts/python.exe scripts/check_bundle_schema.py .researches/2026-10-11-production-extra/cli-evidence/schema.json
```

If Windows application control blocks the native validator dependency, run the same check in the pinned Linux image. Source is read-only; packages and temporary data stay in the ignored evidence mount:

```powershell
$sparkPin = Get-Content runtime/spark.json -Raw | ConvertFrom-Json
$repoPath = (Get-Location).Path
$evidencePath = Join-Path $repoPath '.skills-test/spark'
docker run --rm --user 0:0 `
  --mount "type=bind,source=$repoPath,target=/workspace,readonly" `
  --mount "type=bind,source=$evidencePath,target=/evidence" `
  --entrypoint /bin/sh $sparkPin.image -c 'python3 -m pip install --quiet --target /evidence/production-schema-deps -r /workspace/labs/production/requirements-test.txt && PYTHONPATH=/evidence/production-schema-deps python3 /workspace/scripts/check_bundle_schema.py /workspace/.researches/2026-10-11-production-extra/cli-evidence/schema.json'
```

## Privacy

Use synthetic identities in public artifacts. Never publish credentials, account/workspace/job/pipeline/warehouse identifiers, private workspace URLs, user emails, sensitive query text or payloads. Pattern guards supplement manual redaction; private cloud screenshots and operational logs require human review before sharing.
