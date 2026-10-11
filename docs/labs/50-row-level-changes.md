---
title: 'Lab 50 · Iceberg row-level changes'
description: 'Produce semantic or architecture evidence for Chapter 50.'
prev:
  text: Chapter 50
  link: /iceberg/50-row-level-changes
next:
  text: Next dependency
  link: /iceberg/51-delta-vs-iceberg
---

# Lab 50 · Iceberg row-level changes

Read [Chapter 50](/iceberg/50-row-level-changes) first. This exercise uses synthetic data or an explicit architecture brief; no cloud account is needed.

## Brief

id1 revenue100 is corrected to120; id2 must be deleted; id3 revenue50 arrives. Files cannot be updated in place. How can UPDATE/DELETE/MERGE produce exactly170?

## Work

1. Compare COW final rows with the expected170 cents.
2. Inspect content1 delete file evidence from the MOR table.
3. Build a reader compatibility failure analysis without claiming equality-delete/v3 execution.

## Evidence packet

Submit inputs/assumptions, a hypothesis, observed output or sourced capabilities, a rejected alternative, failure analysis and a decision with acceptance/reversal criteria. Tag each item LOCAL ICEBERG, SOURCED PLATFORM or ARCHITECTURE EVIDENCE.


Run `python scripts/test_iceberg.py` and identify the relevant contract in `labs/iceberg/experiments.py`. [Selected runtime artifacts](/labs/iceberg-evidence) are a worked reference, not your own execution.

## Failure review

A BI engine ignores delete files and returns deleted id1. A valid MERGE uses an unscoped event_id and overwrites another app. Table ACID does not validate business grain.

Name the violated invariant, responsible layer and a test that distinguishes the cause from a competing hypothesis.

## PASS criteria

PASS requires every work item and an evidence-scoped conclusion. NOT YET: feature checklist, unqualified speed claims, or format/catalog/platform conflation.
