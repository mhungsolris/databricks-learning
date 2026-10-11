---
title: 'Lab 49 · Schema evolution and hidden partitioning'
description: 'Produce semantic or architecture evidence for Chapter 49.'
prev:
  text: Chapter 49
  link: /iceberg/49-schema-partition-evolution
next:
  text: Next dependency
  link: /iceberg/50-row-level-changes
---

# Lab 49 · Schema evolution and hidden partitioning

Read [Chapter 49](/iceberg/49-schema-partition-evolution) first. This exercise uses synthetic data or an explicit architecture brief; no cloud account is needed.

## Brief

An events table initially partitions by day. New workloads filter campaign; country and creative_id are added. Must every old file be rewritten before new writes or queries can work?

## Work

1. Run schema and partition contracts.
2. Show the unchanged campaign field ID and old NULL country.
3. Show two spec IDs and retained old files.
4. Assess whether the same mixed-spec table can be virtualized in Fabric.

## Evidence packet

Submit inputs/assumptions, a hypothesis, observed output or sourced capabilities, a rejected alternative, failure analysis and a decision with acceptance/reversal criteria. Tag each item LOCAL ICEBERG, SOURCED PLATFORM or ARCHITECTURE EVIDENCE.


Run `python scripts/test_iceberg.py` and identify the relevant contract in `labs/iceberg/experiments.py`. [Selected runtime artifacts](/labs/iceberg-evidence) are a worked reference, not your own execution.

## Failure review

Downstream parser uses column position after schema change; values silently shift. An external compatibility path rejects multiple specs even when Apache Iceberg reader succeeds. Fabric virtualization currently lists multi-spec evolution as failing.

Name the violated invariant, responsible layer and a test that distinguishes the cause from a competing hypothesis.

## PASS criteria

PASS requires every work item and an evidence-scoped conclusion. NOT YET: feature checklist, unqualified speed claims, or format/catalog/platform conflation.
