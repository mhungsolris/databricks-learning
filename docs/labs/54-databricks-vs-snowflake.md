---
title: 'Lab 54 · Databricks versus Snowflake'
description: 'Produce semantic or architecture evidence for Chapter 54.'
prev:
  text: Chapter 54
  link: /system-design/54-databricks-vs-snowflake
next:
  text: Next dependency
  link: /system-design/55-databricks-vs-fabric
---

# Lab 54 · Databricks versus Snowflake

Read [Chapter 54](/system-design/54-databricks-vs-snowflake) first. This exercise uses synthetic data or an explicit architecture brief; no cloud account is needed.

## Brief

Finance runs governed SQL with isolated reporting compute on Snowflake. Engineering wants external Iceberg consumers and some Spark jobs. Does this require migrating all reporting to Databricks?

## Work

1. Design a no-migration option and a hybrid option.
2. Assign maintenance and commit authority for each.
3. Document consumer version, region, access and cost acceptance.

## Evidence packet

Submit inputs/assumptions, a hypothesis, observed output or sourced capabilities, a rejected alternative, failure analysis and a decision with acceptance/reversal criteria. Tag each item LOCAL ICEBERG, SOURCED PLATFORM or ARCHITECTURE EVIDENCE.


Use [current platform support](/iceberg/current-platform-support) and [decision ADRs](/adr/ADR-002-platform-choice). No platform benchmark or cloud deployment is claimed by this exercise.

## Failure review

Two engines write with mismatched feature/delete support; a catalog sync lags after schema change. Engineers bypass row governance using storage credentials.

Name the violated invariant, responsible layer and a test that distinguishes the cause from a competing hypothesis.

## PASS criteria

PASS requires every work item and an evidence-scoped conclusion. NOT YET: feature checklist, unqualified speed claims, or format/catalog/platform conflation.
