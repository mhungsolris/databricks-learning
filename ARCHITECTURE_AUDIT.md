# Architecture judgment audit

Scope: Chapters46-60, local Iceberg lab, support ledger, two teaching ADRs and Platform/Lakehouse System Design gate. Quality audit examines prose and evidence boundaries; verification receipts are owned by PROGRESS.md.

| Requested check | Finding and evidence |
|---|---|
| Iceberg confused with compute | Chapter 46 separates format, engine, catalog and storage explicitly |
| Catalog collapsed into format | Chapter 48 traces identifier, pointer, commit requirements and IAM |
| Metadata presented as one file | Chapter 47 traces snapshots, manifest lists, manifests and data/delete files |
| Delta restricted to Databricks | Chapter 51 identifies open-source Delta and engine-specific protocols |
| Iceberg treated as no lock-in | Chapter 58 maps11coupling layers and exit contracts |
| Outdated platform stereotypes | Chapters53-55 use current official architectures and ownership |
| Snowflake lakehouse ignored | Chapter 54 and support ledger cover managed/external Iceberg and Horizon |
| BigQuery managed Iceberg ignored | Chapter 53 distinguishes BigQuery-managed and Google REST-managed paths |
| Fabric open formats ignored | Chapter 55 covers OneLake virtualization/shortcuts and conversion failures |
| Every design chooses Databricks | CaseA chooses BigQuery; CaseD conditionally chooses Fabric |
| Migration without business benefit | Chapter 53 and ADR-002 recommend staying when the existing stack meets requirements |
| Format equals full portability | Chapters51/58/59 require catalog, feature, IAM and operation acceptance |
| Toy benchmark ranks platforms | Local tests assert semantics only; no speed race or universal ranking |
| Five layers collapsed | Chapters46/48/59 maintain platform, format, storage, compute and catalog boundaries |

## Runtime and source boundaries

Official Apache artifact supports Spark 4.0/Scala 2.13; the course pins Iceberg 1.12.0 on Spark 4.0.4 and tests formatv2. Seven real contracts inspect snapshots, schema IDs, mixed specs, COW mutations, MOR position deletes and metadata references.

Local v2 position deletes and hidden transforms do not imply Databricks managed compatibility. Current Databricks, BigQuery, Snowflake and Fabric paths have separate read/write, maintenance and feature rules in docs/iceberg/current-platform-support.md.

The first MOR fixture produced a whole-file delete rather than a delete file. The corrected fixture writes two rows in one file and deletes one; tests assert content1 metadata. Failed runs remain isolated and are not selected as passing evidence.

## Assessment and architecture evidence

Public gate uses an unseen GCP brief and a100-point rubric. Any justified platform, including rejection of Databricks, can score fully. The reviewer rubric remains outside docs and carries the existing private marker; site search/build privacy checks enforce exclusion.

ADRs are conditional worked scenario decisions, not user approval or live deployment. REST server, multiple engines, cloud IAM and concurrent commits remain unexecuted. Architecture evidence records assumptions, alternatives, failure analysis, owners and reversal tests.

## Remaining production acceptance

Select an approved workspace/catalog/client matrix before authenticated operations. Run realistic source-cutoff reconciliation, denied-access, refresh/feature, concurrent commit, maintenance/retention and cost/recovery acceptance. Local semantics and official sources do not establish those results.
