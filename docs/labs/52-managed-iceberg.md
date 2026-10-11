---
title: 'Lab 52 · Managed Iceberg on Databricks'
description: 'Produce semantic or architecture evidence for Chapter 52.'
prev:
  text: Chapter 52
  link: /iceberg/52-managed-iceberg
next:
  text: Next dependency
  link: /system-design/53-databricks-vs-bigquery
---

# Lab 52 · Managed Iceberg on Databricks

Read [Chapter 52](/iceberg/52-managed-iceberg) first. This exercise uses synthetic data or an explicit architecture brief; no cloud account is needed.

## Brief

Finance wants governed multi-engine tables; an existing Glue table must remain externally owned. The team labels both managed and lets every engine write directly to the bucket.

## Work

1. Assign owner for storage, metadata, commit, compaction and retention.
2. Compare all three access patterns with the current support ledger.
3. List workspace acceptance evidence without configuring credentials.

## Evidence packet

Submit inputs/assumptions, a hypothesis, observed output or sourced capabilities, a rejected alternative, failure analysis and a decision with acceptance/reversal criteria. Tag each item LOCAL ICEBERG, SOURCED PLATFORM or ARCHITECTURE EVIDENCE.


Use [current platform support](/iceberg/current-platform-support) and [decision ADRs](/adr/ADR-002-platform-choice). No platform benchmark or cloud deployment is claimed by this exercise.

## Failure review

External engine bypasses UC and writes files or maintains a second pointer. A foreign reader assumes auto-refresh through REST and serves stale snapshot. Unified naming does not establish shared write authority.

Name the violated invariant, responsible layer and a test that distinguishes the cause from a competing hypothesis.

## PASS criteria

PASS requires every work item and an evidence-scoped conclusion. NOT YET: feature checklist, unqualified speed claims, or format/catalog/platform conflation.
