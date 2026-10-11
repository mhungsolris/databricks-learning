---
title: 'Lab 53 · Databricks versus BigQuery'
description: 'Produce semantic or architecture evidence for Chapter 53.'
prev:
  text: Chapter 53
  link: /system-design/53-databricks-vs-bigquery
next:
  text: Next dependency
  link: /system-design/54-databricks-vs-snowflake
---

# Lab 53 · Databricks versus BigQuery

Read [Chapter 53](/system-design/53-databricks-vs-bigquery) first. This exercise uses synthetic data or an explicit architecture brief; no cloud account is needed.

## Brief

GCS → BigQuery → dbt → Looker is stable. Three DEs, 90% SQL, hourly dashboard; CTO proposes Databricks because it supports Spark and Iceberg. No unmet SLA is identified.

## Work

1. Write a stay/migrate decision for the3-DE scenario.
2. List one concrete trigger that reverses the decision.
3. Specify shadow reconciliation, IAM, cost and rollback acceptance before cutover.

## Evidence packet

Submit inputs/assumptions, a hypothesis, observed output or sourced capabilities, a rejected alternative, failure analysis and a decision with acceptance/reversal criteria. Tag each item LOCAL ICEBERG, SOURCED PLATFORM or ARCHITECTURE EVIDENCE.


Use [current platform support](/iceberg/current-platform-support) and [decision ADRs](/adr/ADR-002-platform-choice). No platform benchmark or cloud deployment is claimed by this exercise.

## Failure review

Migration duplicates transforms in dbt and notebooks. Different timezone/rounding or stale attribution cutoffs changes ROAS. The new platform meets job SUCCESS but Finance output disagrees.

Name the violated invariant, responsible layer and a test that distinguishes the cause from a competing hypothesis.

## PASS criteria

PASS requires every work item and an evidence-scoped conclusion. NOT YET: feature checklist, unqualified speed claims, or format/catalog/platform conflation.
