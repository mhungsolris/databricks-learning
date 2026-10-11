---
title: ADR-002 · Keep a stable GCP SQL analytics stack
description: A reversible stay decision when a proposed platform migration has no measured business gap.
---

# ADR-002 · Keep a stable GCP SQL analytics stack

Status: conditional teaching decision, dated 2026-10-11. Scenario A in Chapter 60, separate from the final assessment brief. ARCHITECTURE EVIDENCE; staffing/volume/SLA inputs are synthetic.

## Requirements

Three DEs, 90% SQL, GCP, hourly dashboards, BigQuery/dbt/Looker already within approved SLA and cost. No committed ML requirement, Spark-only transformation or external writer need exists.

## Decision

Keep GCS retained landing → BigQuery → dbt → Looker with the existing supported scheduler. Improve source-cutoff observability and scoped reconciliation where needed. Do not migrate solely because Databricks offers Spark or Iceberg.

## Requirement scorecard

| Requirement | Importance | Implication |
|---|---|---|
| Hourly correct reports | Mandatory | End-to-end cutoff and replay tests |
| Small team and low operations | High | Preserve established managed warehouse workflow |
| Existing GCP/SQL skills | High | Avoid unsupported migration burden |
| ML may happen later | Low until committed | Isolated pilot when a workload exists |
| Open formats | Conditional on consumer | Compare managed Iceberg paths before a whole-platform move |

## Alternatives and trade-offs

Databricks can address a real Spark/batch/stream/ML workload gap; it adds training, access models, orchestration and dual-run costs. Snowflake is viable for a SQL estate but current switching costs need business return. Fabric becomes relevant when enterprise Microsoft integration is a requirement.

Accepted coupling includes GoogleSQL/IAM and current tooling. Quantify exit tests and avoidable switching costs; existing investment does not justify keeping an architecture that fails mandatory requirements.

## Cost and failure analysis

Estimate query/compute, storage, optimization, egress, operations and migration/dual-run cost. No universal vendor price ranking is implied. Bad migration can change timezone, attribution cutoffs or join grain even when counts match.

Data lead owns exact source-cutoff comparison and dashboard acceptance. Platform lead owns access/cost envelope and operations. Business owner agrees hourly freshness and recovery targets.

## Reversal conditions

Reevaluate when a measured transformation/latency/ML requirement cannot meet its agreed envelope through a bounded change, or enterprise strategy changes. Pilot the missing workload with explicit cost, correctness, denied-access and rollback acceptance before approving wider cutover.

## Sources

[BigQuery operating model](https://docs.cloud.google.com/bigquery/docs/introduction), [managed Iceberg](https://docs.cloud.google.com/bigquery/docs/biglake-iceberg-tables-in-bigquery), [Databricks Iceberg](https://docs.databricks.com/aws/en/iceberg/), verified 2026-10-11 GCP/AWS. [Decision framework](/system-design/56-decision-framework) owns the general method.
