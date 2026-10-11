---
title: Local Iceberg runtime
description: Reproduce Iceberg semantics with Spark4.0.4 and a compatible official runtime in Docker.
---

# Local Iceberg runtime

FREE LOCAL. Chạy từ repository root bằng PowerShell với Python3.10+ và Docker Desktop Linux containers. [Spark setup](/setup/local-spark) owns the shared image/Java/resource contract; no host Java/PySpark installation is required.

## Compatibility

| Component | Course pin |
|---|---|
| Spark |4.0.4, image digest in runtime/spark.json |
| Iceberg |1.12.0, released 2026-09-29 |
| Scala artifact |2.13, iceberg-spark-runtime-4.0_2.13 |
| Maven coordinate |org.apache.iceberg: iceberg-spark-runtime-4.0_2.13: 1.12.0 |
| Catalog |local, SparkCatalog, type=hadoop |
| Table format |v2, intentionally separate from platform v3 paths |

Official compatibility verified 2026-10-11 against [Apache release artifacts](https://iceberg.apache.org/releases/) and [Spark integration](https://iceberg.apache.org/docs/latest/spark-getting-started/). Do not substitute a Spark 3.5 runtime or Scala 2.12 JAR.

## Run

```powershell
docker info --format '{{.OSType}}'
python scripts/verify_iceberg.py
python scripts/test_iceberg.py
```

Expected Docker OS is linux. First run resolves the pinned JAR into ignored `.skills-test/spark/ivy`; network is needed. The launcher reads `runtime/iceberg.json` and shared Spark image settings, then mounts repository read-only and evidence read/write. No global configuration, credentials or billable resource is created.

## Catalog configuration

The launcher sets these Spark-submit configurations:

```text
spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions
spark.sql.catalog.local=org.apache.iceberg.spark.SparkCatalog
spark.sql.catalog.local.type=hadoop
spark.jars.ivy=/evidence/ivy
```

Before the first catalog load, the experiment sets `spark.sql.catalog.local.warehouse` to `file:/evidence/<suite>/<unique-run>/iceberg-warehouse`. Table identifier is `local.course.events`; namespace and table creation use real Spark SQL. Each run isolates warehouse state.

Hadoop catalog here uses a local filesystem and its commit operations. This setup does not validate object-store HadoopCatalog safety, distributed catalog availability, concurrent writers or REST authentication.

## Smoke and integration evidence

Smoke verifies actual Spark/Iceberg/Scala versions, creates a table, inserts two rows, checks a snapshot and queries revenue300. Integration tests add snapshot lineage/time travel, schema rename/add, partition evolution, UPDATE/DELETE/MERGE and metadata integrity. [Evidence guide](/labs/iceberg-evidence) owns actual selected results.

Output reports unittest status, clean SparkSession shutdown and an evidence directory. Inspect `tests.json`, `runtime.json`, `iceberg-runtime.json`, `results.json` and `shutdown.json`; success requires no failed/error/skipped tests.

## Troubleshooting

| Symptom | Inspect | Recovery |
|---|---|---|
| Docker pipe missing/denied | Docker Desktop state and Linux daemon permissions | Start approved Docker Desktop; retry |
| Maven resolution fails | Network, artifact coordinate and Ivy output | Restore network; retain pinned compatible coordinate |
| Iceberg class/extension missing | Spark-submit packages/extensions | Use repository launcher; avoid mismatched runtime JAR |
| No catalog/namespace | Catalog name, warehouse config before first access | Use local.course and run-specific warehouse |
| DELETE creates no delete file | Data distribution and whole-file delete optimization | Keep two rows in one file and delete one, as integration fixture does |

No security policy workaround is required. A failed run remains under its unique evidence directory; do not label it as selected passing evidence.

## Windows and shutdown

PowerShell does not use Bash line continuation/environment syntax; commands above are complete host wrappers. Linux warehouse paths exist inside the container, host artifacts under `.skills-test/spark`. Metadata contains absolute file references, so exported JSON is inspection evidence rather than a relocatable table backup.

Shared session context calls `spark.stop()` in finally and verifies the SparkContext is stopped. Docker runs with `--rm`. To interrupt a running lab, use Ctrl+C and inspect `docker ps`; stop only the identified lab container if needed. Docker Desktop can remain available for later labs.
