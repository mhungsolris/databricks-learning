---
title: Optional Databricks Free Edition learning environment
description: Workspace prerequisites, quota boundaries and evidence policy.
---

# Optional Databricks Free Edition learning environment

Free Edition là đường học platform thật cho cá nhân, trong môi trường serverless-only và quota-limited. Repository vẫn chạy được local labs khi người học chưa có workspace. Current workspace evidence: `PENDING USER WORKSPACE`.

## Evidence tiers

| Label | What it proves | Boundary |
|---|---|---|
| LOCAL LAB | Portable contracts/config checks or actual pinned local Spark/Delta queries | Không là Databricks execution |
| DATABRICKS FREE EDITION LAB | Run trên workspace của người học, có redacted outputs/run evidence | Quota-limited personal learning |
| PAID/PRODUCTION-ONLY CONCEPT | Enterprise administration, custom networking/IAM, multi-workspace design or classic compute | Design discussion; needs authorized production-like environment |

[Platform evidence](/labs/platform-evidence) owns evidence status. Lab instructions below describe proposed learner actions; no workspace action has been executed by this repository setup.

## Current limits

Official Free Edition pages checked 2026-10-11, AWS documentation. Free Edition is non-commercial, has no SLA/support guarantee, and restricts outbound access to trusted domains. Custom compute/configurations are unavailable. One SQL warehouse is limited to 2X-Small; Jobs allows at most five concurrent tasks per account; one pipeline per type may be active. These are documented limits, not observed account availability.

Fair-use exhaustion can shut compute down for the rest of a day, or in extreme cases a month; data/settings remain. Public documentation does not supply a universal numeric daily usage budget for these labs. Stop extra runs on quota errors and resume after reset.

There is one workspace/metastore, no account console/account APIs, and no enterprise private-network/security customization or SSO/SCIM. R/Scala and custom workspace storage are unavailable. Feature visibility can vary; record an unavailable capability rather than inventing an enterprise workaround.

Sources: [Free Edition overview](https://docs.databricks.com/aws/en/getting-started/free-edition), [current limits](https://docs.databricks.com/aws/en/getting-started/free-edition-limitations).

## Learner-owned setup and access preflight

1. If desired, create your own Free Edition account using the official page. Signup and login stay under your control. Do not send credentials to the repository or assistant.
2. In the workspace, inventory notebook serverless, Jobs, pipelines, catalog explorer and the existing SQL warehouse. Record only labels, availability and limitations, without workspace URL, emails or IDs.
3. Select an existing accessible learning catalog. Choose a unique schema starting with course_roas_, owned by you. Review creation/table privileges before running code. Do not use an existing production schema.
4. Confirm your principal can use notebook/job compute, create tables in that schema and read them through the warehouse. SQL warehouse access and Unity Catalog data access are separate.
5. Import labs/platform/src/roas_task.py as a notebook or deploy the bundle after optional local auth. Set catalog/schema explicitly. Use synthetic data only.
6. Run Lab26 stages before Lab27/29 because they create retained inputs and Gold. Stop pipeline updates/extra job runs after the exercise; use the existing small warehouse and its auto-stop behavior.

No external API, cloud credential, storage credential or custom IAM setup is needed for the sample. Table replacement is limited to learner-owned lab tables; repeat ingestion intentionally restores the sample snapshot. Remove only your own lab resources if you choose to clean up.

## Course lab mapping

| Lab | Free Edition use | Local path / unavailable branch |
|---|---|---|
| 25 | Inspect available compute categories | Ten classification scenarios, no resources |
| 26 | Notebook-based Jobs DAG, failed validation and repair | Config graph checks; run/repair evidence pending |
| 27 | One triggered serverless pipeline, batch materialized views | AST and underlying SQL checks; no local SDP execution |
| 28 | Owned schema/table hierarchy and metadata/grant inspection if supported | Governance design; group/SP/admin/IAM validation deferred |
| 29 | Existing SQL warehouse and sample Gold queries | Actual local Spark SELECT validation; warehouse/history pending |
| 30 | Architecture design only | Two boundary diagrams and platform gate |

Chapters16-24 processingTime streaming labs remain local. Current serverless notebooks/jobs require supported bounded streaming triggers such as AvailableNow; managed pipeline continuous mode is a separate option. Do not port those labs unchanged.

## Optional authentication

CLI/SDK is optional for this learning path. No CLI/auth is configured here. Supported tool authentication uses unified auth; interactive user OAuth U2M is preferred for supported clients. Production automation usually uses an approved service principal with OAuth M2M or an appropriate supported identity/federation mechanism, reviewed against the target environment. Free Edition account login restrictions and absence of account APIs are separate from workspace-tool OAuth availability; if tool auth is unavailable, use manual notebook/config entry.

Only after the learner chooses a workspace/profile locally:

```powershell
databricks --version
databricks auth login --host "<your-workspace-url>" --profile "<your-chosen-profile>"
# Work in labs/platform; values are identifiers, not secrets:
$env:BUNDLE_VAR_catalog = "<accessible-catalog>"
$env:BUNDLE_VAR_schema = "<unique-course_roas_schema>"
databricks bundle validate --strict --target dev --profile "<your-chosen-profile>"
```

Check installed command help before use. These commands have not been run here. Local bundle contract tests do not replace strict CLI validation, workspace permission checks or deployed runs. Review the resolved resources after validation and only deploy/run intentionally in your own learning workspace.

Never commit tokens, auth caches, profiles, workspace URLs/IDs, exported notebook credentials or screenshots showing account/email identifiers. An .env.example is unnecessary because this lab uses user-owned OAuth profiles and non-secret bundle variables. Sources: [OAuth U2M](https://docs.databricks.com/aws/en/dev-tools/auth/oauth-u2m), [OAuth M2M](https://docs.databricks.com/aws/en/dev-tools/auth/oauth-m2m), [unified auth](https://docs.databricks.com/aws/en/dev-tools/auth/), [bundles](https://docs.databricks.com/aws/en/dev-tools/bundles/).

## Limits of a successful lab

A passing sample proves that the recorded feature/run and bounded outputs work in that environment. Production scale, networking, enterprise administration, SLA, concurrency, production cost and multi-workspace governance need independent evidence. Never infer those from a Free Edition screenshot.
