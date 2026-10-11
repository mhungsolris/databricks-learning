---
title: Iceberg and architecture evidence
description: Local semantic proof, current official platform sources and explicit architecture decisions.
---

# Iceberg and architecture evidence

LOCAL ICEBERG proves bounded table semantics on Spark 4.0.4/Iceberg 1.12.0/Scala 2.13 with Hadoop catalog and formatv2. It does not prove managed cloud behavior, cross-engine compatibility, concurrent writers or platform performance.

## Evidence tiers

| Tier | What qualifies | Limits |
|---|---|---|
| LOCAL ICEBERG | Executed create/query, metadata, snapshots, evolution and mutations | One local engine/catalog, tiny fixtures |
| SOURCED PLATFORM | Current official requirements and read/write boundaries | No workspace operation |
| ARCHITECTURE EVIDENCE | Requirements, alternatives, trade-offs, rejected designs, failure analysis and ADR | Conditional judgment, not measured throughput |
| DATABRICKS WORKSPACE | Actual approved workspace acceptance | PENDING USER WORKSPACE |

Architecture records: [table format ADR](/adr/ADR-001-table-format), [platform ADR](/adr/ADR-002-platform-choice), [four case studies](/system-design/60-system-design-cases). Official capabilities: [support ledger](/iceberg/current-platform-support).

## Reproduce

Follow [local setup](/setup/local-iceberg), then run from repository root:

```powershell
python scripts/verify_iceberg.py
python scripts/test_iceberg.py
python scripts/check_iceberg_evidence.py
```

Fresh runtime output lives under ignored `.skills-test/spark/iceberg-smoke/<run>` and `.skills-test/spark/tests-iceberg/<run>`. The last command checks the selected public evidence against its source fingerprints; it does not execute Spark again.

## Semantic observations

| Contract | Measured result | Scope |
|---|---|---|
| Create/insert/query |2 rows, revenue300, snapshot exists | Real Spark SQL |
| Snapshot/time travel | Old2 rows, appended current3 rows; parent lineage | Retained files, no expiration |
| Schema | Renamed campaign retains field ID3; old country=NULL | Add optional field and rename |
| Partition evolution | Spec IDs0/1; old paths remain; 3 rows, total350 | days(event_time) → bucket(4, campaign) |
| COW UPDATE/DELETE/MERGE | Final id1=120, id3=50, total170 | Explicit copy-on-write modes, data files |
| MOR delete | One2-row data file plus position delete for1row; result id2=200 | Explicit merge-on-read, formatv2 |
| Metadata integrity |3 snapshots, 3 manifests, 4current data files; referenced paths exist | JSON plus engine-decoded metadata tables |

Snapshot IDs and filenames vary by run. The S1=A/B, S2=B/C example in Chapter 47 is conceptual; the executed snapshot test appends a third row. Do not present those file labels as captured runtime filenames.

## Selected artifacts

[Manifest](/evidence/iceberg/manifest.json) identifies the selected run, hashes and evidence tier. Nine bounded files are published:

- [Spark runtime](/evidence/iceberg/runtime.json) and [Iceberg/Scala runtime](/evidence/iceberg/iceberg-runtime.json).
- [Startup source hashes](/evidence/iceberg/source-hashes.json).
- [Semantic results](/evidence/iceberg/results.json) and [test receipt](/evidence/iceberg/tests.json).
- [Clean shutdown](/evidence/iceberg/shutdown.json) and [completed stages](/evidence/iceberg/stages.json).
- [Actual table metadata JSON](/evidence/iceberg/table-metadata.json).
- [SQL-decoded metadata tables](/evidence/iceberg/metadata-tables.json).

Raw Parquet/Avro data and full Spark event logs remain in ignored local runs. Public metadata contains synthetic container paths; these point to the measured run and are inspection evidence, not a downloadable/relocatable table backup.

The integrity guard requires all7 tests passing without errors/skips, actual versions, semantic assertions, clean shutdown, selected-file hashes and seven startup-source hashes. A source change requires a new integration run before selecting fresh evidence.

## Unexecuted boundaries

Equality-delete generation, Icebergv3, REST catalog server, Trino/Flink, actual concurrent commits, object storage and cloud IAM are not executed. The local v2 position-delete table is not claimed as Databricks-compatible. UniForm, UC managed/foreign tables, BigQuery, Snowflake and Fabric are official-source/design evidence only.

No Delta-versus-Iceberg speed race is performed. Stage counts and elapsed times are runtime diagnostics, not comparative platform benchmarks.
