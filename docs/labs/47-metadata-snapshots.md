---
title: 'Lab 47 · Iceberg metadata, snapshots and history'
description: 'Produce semantic or architecture evidence for Chapter 47.'
prev:
  text: Chapter 47
  link: /iceberg/47-metadata-snapshots
next:
  text: Next dependency
  link: /iceberg/48-catalogs
---

# Lab 47 · Iceberg metadata, snapshots and history

Read [Chapter 47](/iceberg/47-metadata-snapshots) first. This exercise uses synthetic data or an explicit architecture brief; no cloud account is needed.

## Brief

S1 references A.parquet and B.parquet. S2 references B.parquet and C.parquet after rewriting A. All three files still exist. A reader globbing A/B/C disagrees with a table query. Which state should finance use?

## Work

1. Capture snapshot before append.
2. Query the older snapshot and compare2 vs3 rows.
3. Inspect table-metadata.json and SQL-decoded metadata-tables.json.
4. Explain shared files and absolute-path migration risk.

## Evidence packet

Submit inputs/assumptions, a hypothesis, observed output or sourced capabilities, a rejected alternative, failure analysis and a decision with acceptance/reversal criteria. Tag each item LOCAL ICEBERG, SOURCED PLATFORM or ARCHITECTURE EVIDENCE.


Run `python scripts/test_iceberg.py` and identify the relevant contract in `labs/iceberg/experiments.py`. [Selected runtime artifacts](/labs/iceberg-evidence) are a worked reference, not your own execution.

## Failure review

Copy a table folder to a new path and retain absolute metadata references: reader can still point at the old location or fail. Expire snapshots/remove required data too early: historical queries become unavailable.

Name the violated invariant, responsible layer and a test that distinguishes the cause from a competing hypothesis.

## PASS criteria

PASS requires every work item and an evidence-scoped conclusion. NOT YET: feature checklist, unqualified speed claims, or format/catalog/platform conflation.
