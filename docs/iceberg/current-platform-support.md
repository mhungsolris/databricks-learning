---
title: Current open-table platform boundaries
description: Date-scoped ownership, compatibility and read/write boundaries from official documentation.
---

# Current open-table platform boundaries

SOURCED PLATFORM, verified 2026-10-11. Đây là capability ledger, không phải benchmark hay cloud execution evidence. Apache format spec, engine support, catalog implementation và platform integration là bốn contracts riêng.

## Apache runtime and format

Apache released Iceberg 1.12.0 on 2026-09-29 and lists a dedicated Spark 4.0/Scala 2.13 runtime: `org.apache.iceberg:iceberg-spark-runtime-4.0_2.13:1.12.0`. The course uses Spark 4.0.4 with Iceberg formatv2; local code verifies actual Iceberg/Scala versions. [Apache releases](https://iceberg.apache.org/releases/).

Numbered1.12.0 integration documentation routes returned404 during archival. Current `latest` pages identify1.12.0 and are archived with date; the artifact is pinned independently. [Spark integration](https://iceberg.apache.org/docs/latest/spark-getting-started/).

Formatv2 defines position and equality deletes. Formatv3 adds deletion-vector and other capabilities; an engine may implement only a subset. Local tests generate a v2 position delete, not equality deletes or v3. [Specification](https://iceberg.apache.org/spec/).

## Databricks on AWS

Databricks documents Parquet-backed Iceberg versions1/2/3. Managed/foreign access requires Unity Catalog and DBR 16.4 LTS+; managed additionally needs serverless enabled with storage connectivity and predictive optimization. UC owns managed lifecycle/maintenance, while foreign metadata remains under an external catalog. Foreign Iceberg is read-only in Databricks. [Iceberg overview and limitations](https://docs.databricks.com/aws/en/iceberg/).

| Access path | Catalog authority | Supported Iceberg-client boundary |
|---|---|---|
| UC managed Iceberg | Unity Catalog | Read/write via supported current REST endpoint |
| Foreign Iceberg | External catalog | Read-only; REST reads require explicit refresh for new snapshots |
| Managed/external Delta with Iceberg reads | Delta writer plus generated Iceberg metadata | Iceberg-client reads; no Iceberg-client writes |

Current REST endpoint: `/api/2.1/unity-catalog/iceberg-rest`; a legacy read-only endpoint also exists. External metastore access, `EXTERNAL USE SCHEMA`, supported auth/client/storage permissions are prerequisites. Credential vending is unavailable for foreign Iceberg and default-storage workspaces; filtered/masked access has client/configuration requirements. [External Iceberg access](https://docs.databricks.com/aws/en/external-access/iceberg).

Databricks does not support v2 position/equality delete files, while v3 deletion vectors provide a row-delete path. Managed partition evolution is through external engines; expression transforms such as days/bucket are restricted. Foreign partition evolution and branching/tagging are unsupported. These constraints are narrower than the Apache spec/local runtime. Managed Iceberg materialized views are Public Preview. [Current limitations](https://docs.databricks.com/aws/en/iceberg/), [v3 requirements](https://docs.databricks.com/aws/en/iceberg/iceberg-v3).

## Delta Iceberg reads and UniForm

Databricks Iceberg reads configures UniForm to generate Iceberg metadata asynchronously alongside Delta metadata over the same Parquet files. DBR 14.3 LTS+, UC registration, column mapping and required reader/writer protocol/features apply. The documented IcebergCompatV2 path excludes deletion vectors and upgrades writer compatibility; pipeline-managed objects have a distinct IcebergCompatV3 route. [Iceberg reads](https://docs.databricks.com/aws/en/delta/iceberg-reads).

External readers need supported types/features and current metadata. Track `converted_delta_version` and `converted_delta_timestamp`; several Delta commits may map to one generated Iceberg state. A pinned metadata JSON path may require refresh. Name-based writes trigger automatic generation; path-based writes do not establish that trigger. Retention must protect every accepted reader horizon. This is read interoperability, not arbitrary bidirectional mutation.

## Google Cloud

BigQuery Apache Iceberg managed tables, formerly BigLake tables for Apache Iceberg in BigQuery, store data in customer-owned GCS buckets. BigQuery controls supported DML, Storage Write API ingestion, automatic maintenance and exported Icebergv2 snapshot refresh. Storage, storage optimization and query/job usage are separate cost components. External tools must follow the managed-table storage/write rules instead of independently altering managed files. [Managed Iceberg architecture, pricing and limitations](https://docs.cloud.google.com/bigquery/docs/biglake-iceberg-tables-in-bigquery).

Google Lakehouse runtime/REST-managed Iceberg is a separate architecture. Official docs mark read/write interoperability, automatic management, BigQuery DDL and credential vending capabilities as Preview. Catalog selection and table options determine the boundary; do not transfer its external-write promises to every BigQuery-managed table. [REST-managed table options](https://docs.cloud.google.com/lakehouse/docs/manage-tables).

Native BigQuery storage remains a valid SQL analytics choice. Open-table support leaves IAM, region, operations and developer workflow decisions unresolved. [BigQuery overview](https://docs.cloud.google.com/bigquery/docs/introduction).

## Snowflake

Snowflake-managed Iceberg uses Snowflake catalog/lifecycle and can use customer-managed external volumes or Snowflake-managed storage. External-catalog tables retain an external authority and have narrower Snowflake platform/lifecycle support. Current docs cover v2/v3, position-delete/v3-vector constraints and Horizon REST external-engine access for supported managed tables. [Iceberg table architecture and limitations](https://docs.snowflake.com/en/user-guide/tables-iceberg).

Horizon REST read/write support and storage/governance rules are version/client/deployment-specific. Compute/cloud services, refresh/external-engine access and egress can be billed independently. New Snowflake Open Catalog customers are directed to Horizon; existing Open Catalog customers have separate account rules. [Open Catalog availability](https://docs.snowflake.com/en/user-guide/opencatalog/overview).

Snowflake's compute/storage/cloud-services separation supports a managed warehouse operating model alongside these open-table paths. A Spark requirement or existing SQL investment must be evaluated explicitly. [Architecture](https://docs.snowflake.com/en/user-guide/intro-key-concepts).

## Fabric and OneLake

OneLake offers Delta/Iceberg interoperability through metadata virtualization and shortcuts. Fabric native analytics experiences use Delta by default; supported Iceberg sources can appear as virtual Delta, while Delta data can be exposed with generated Iceberg metadata to external readers. [OneLake](https://learn.microsoft.com/en-us/fabric/onelake/onelake-overview), [format interoperability](https://learn.microsoft.com/en-us/fabric/fundamentals/delta-lake-interoperability).

Current virtualization emits Icebergv2 metadata, supports v2 inputs and selected v3 features. Iceberg equality deletes and multiple partition specs fail conversion. Some unsupported v3 columns/features are dropped, with conversion-log evidence; position deletes/v3 deletion vectors have supported translation paths. Source schema-only changes may wait for a data change before reconversion. [Conversion limitations](https://learn.microsoft.com/en-us/fabric/onelake/onelake-iceberg-tables).

Conversion failure can leave the last successfully converted state. Required freshness, schema and access must be tested at the actual Fabric consumer. Current documented limits include certain regions, private links and same-region OneLake shortcuts. Broad statements that Fabric reads every Iceberg table would violate these boundaries.

## Acceptance contract

For each reader/writer, record engine/client version, format/features, catalog endpoint, commit authority, storage IAM, governance enforcement, refresh cutoff and maintenance owner. Run data and negative access tests in the selected workspace before claiming production readiness.

Local evidence: [Iceberg experiments](/labs/iceberg-evidence). Architecture judgment: [decision framework](/system-design/56-decision-framework). No workspace or managed service has been executed.
