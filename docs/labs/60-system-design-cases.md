---
title: 'Lab 60 · System design case studies'
description: 'Produce semantic or architecture evidence for Chapter 60.'
prev:
  text: Chapter 60
  link: /system-design/60-system-design-cases
next:
  text: Next dependency
  link: /assessments/mid-gate-platform-lakehouse-system-design
---

# Lab 60 · System design case studies

Read [Chapter 60](/system-design/60-system-design-cases) first. This exercise uses synthetic data or an explicit architecture brief; no cloud account is needed.

## Brief

Review four synthetic briefs: startup analytics, 15-minute advertising ROAS, enterprise multi-domain lakehouse, Microsoft-centered analytics. All request governance; only some need stateful streaming or multiple engines.

## Work

1. Submit four architecture diagrams with owners.
2. Defend at least one BigQuery decision and one non-Databricks enterprise decision.
3. Attach rejection reasons, failure analysis, cost envelope and reversal triggers.
4. Complete the Platform and Lakehouse System Design gate.

## Evidence packet

Submit inputs/assumptions, a hypothesis, observed output or sourced capabilities, a rejected alternative, failure analysis and a decision with acceptance/reversal criteria. Tag each item LOCAL ICEBERG, SOURCED PLATFORM or ARCHITECTURE EVIDENCE.


Use [current platform support](/iceberg/current-platform-support) and [decision ADRs](/adr/ADR-002-platform-choice). No platform benchmark or cloud deployment is claimed by this exercise.

## Failure review

Executive preference overrides evidence and all cases migrate. A design mistakes20 GB/day for20 GB/min or treats speculative ML as a mandatory platform trigger. A required governance control is silently bypassed for interoperability.

Name the violated invariant, responsible layer and a test that distinguishes the cause from a competing hypothesis.

## PASS criteria

PASS requires every work item and an evidence-scoped conclusion. NOT YET: feature checklist, unqualified speed claims, or format/catalog/platform conflation.
