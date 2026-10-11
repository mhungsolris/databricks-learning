---
title: 'Lab 59 · Open lakehouse architecture'
description: 'Produce semantic or architecture evidence for Chapter 59.'
prev:
  text: Chapter 59
  link: /system-design/59-open-lakehouse
next:
  text: Next dependency
  link: /system-design/60-system-design-cases
---

# Lab 59 · Open lakehouse architecture

Read [Chapter 59](/system-design/59-open-lakehouse) first. This exercise uses synthetic data or an explicit architecture brief; no cloud account is needed.

## Brief

Object storage holds Iceberg; Spark produces transformations; Trino serves BI; optional Flink handles streams. Two engines want to write the same table. Who commits, who cleans up, and who enforces finance access?

## Work

1. Trace catalog resolution, metadata and storage paths for Spark and BI.
2. Draw conflict handling for two writers with one catalog.
3. Assign maintenance, availability, backup and policy owners.
4. Compare managed REST service versus self-operated service.

## Evidence packet

Submit inputs/assumptions, a hypothesis, observed output or sourced capabilities, a rejected alternative, failure analysis and a decision with acceptance/reversal criteria. Tag each item LOCAL ICEBERG, SOURCED PLATFORM or ARCHITECTURE EVIDENCE.


Use [current platform support](/iceberg/current-platform-support) and [decision ADRs](/adr/ADR-002-platform-choice). No platform benchmark or cloud deployment is claimed by this exercise.

## Failure review

Two writers conflict after changing the same rows. Blindly retrying MERGE against stale business revisions corrupts results. Separate retention jobs race a long-running reader and remove required files.

Name the violated invariant, responsible layer and a test that distinguishes the cause from a competing hypothesis.

## PASS criteria

PASS requires every work item and an evidence-scoped conclusion. NOT YET: feature checklist, unqualified speed claims, or format/catalog/platform conflation.
