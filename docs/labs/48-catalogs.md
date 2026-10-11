---
title: 'Lab 48 · Catalogs and Iceberg REST resolution'
description: 'Produce semantic or architecture evidence for Chapter 48.'
prev:
  text: Chapter 48
  link: /iceberg/48-catalogs
next:
  text: Next dependency
  link: /iceberg/49-schema-partition-evolution
---

# Lab 48 · Catalogs and Iceberg REST resolution

Read [Chapter 48](/iceberg/48-catalogs) first. This exercise uses synthetic data or an explicit architecture brief; no cloud account is needed.

## Brief

Spark knows prod.marketing.events. Storage has five metadata JSON files. Which file is current, who may commit, and how does a BI engine get credentials?

## Work

1. Trace identifier to metadata and files in the selected local evidence.
2. Design REST load, storage read and commit interactions.
3. Assign one owner for commit, retention, backup and IAM; predict two-writer conflicts.

## Evidence packet

Submit inputs/assumptions, a hypothesis, observed output or sourced capabilities, a rejected alternative, failure analysis and a decision with acceptance/reversal criteria. Tag each item LOCAL ICEBERG, SOURCED PLATFORM or ARCHITECTURE EVIDENCE.


Run `python scripts/test_iceberg.py` and identify the relevant contract in `labs/iceberg/experiments.py`. [Selected runtime artifacts](/labs/iceberg-evidence) are a worked reference, not your own execution.

## Failure review

Two writers use different catalog registrations for the same data path. Both believe they own current state. Open files do not prevent split-brain catalog pointers; maintenance can delete files another catalog needs.

Name the violated invariant, responsible layer and a test that distinguishes the cause from a competing hypothesis.

## PASS criteria

PASS requires every work item and an evidence-scoped conclusion. NOT YET: feature checklist, unqualified speed claims, or format/catalog/platform conflation.
