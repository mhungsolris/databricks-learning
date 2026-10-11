---
title: 'Lab 58 · Lock-in is multi-layered'
description: 'Produce semantic or architecture evidence for Chapter 58.'
prev:
  text: Chapter 58
  link: /system-design/58-lock-in-layers
next:
  text: Next dependency
  link: /system-design/59-open-lakehouse
---

# Lab 58 · Lock-in is multi-layered

Read [Chapter 58](/system-design/58-lock-in-layers) first. This exercise uses synthetic data or an explicit architecture brief; no cloud account is needed.

## Brief

Data is Iceberg. The pipeline uses Unity Catalog grants, Lakeflow orchestration, Jobs parameters, SQL extensions and Databricks release/observability APIs. Procurement calls the whole application portable.

## Work

1. Build an11-layer coupling register.
2. Choose an exit acceptance test for every critical layer.
3. Identify one accepted coupling and its measured reversal trigger.

## Evidence packet

Submit inputs/assumptions, a hypothesis, observed output or sourced capabilities, a rejected alternative, failure analysis and a decision with acceptance/reversal criteria. Tag each item LOCAL ICEBERG, SOURCED PLATFORM or ARCHITECTURE EVIDENCE.


Use [current platform support](/iceberg/current-platform-support) and [decision ADRs](/adr/ADR-002-platform-choice). No platform benchmark or cloud deployment is claimed by this exercise.

## Failure review

New reader loads Iceberg files but bypasses row masks via raw storage IAM. Numeric output matches, security contract fails. Pipeline rerun semantics duplicate data after orchestration port.

Name the violated invariant, responsible layer and a test that distinguishes the cause from a competing hypothesis.

## PASS criteria

PASS requires every work item and an evidence-scoped conclusion. NOT YET: feature checklist, unqualified speed claims, or format/catalog/platform conflation.
