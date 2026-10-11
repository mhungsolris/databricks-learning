---
title: 'Lab 55 · Databricks versus Microsoft Fabric'
description: 'Produce semantic or architecture evidence for Chapter 55.'
prev:
  text: Chapter 55
  link: /system-design/55-databricks-vs-fabric
next:
  text: Next dependency
  link: /system-design/56-decision-framework
---

# Lab 55 · Databricks versus Microsoft Fabric

Read [Chapter 55](/system-design/55-databricks-vs-fabric) first. This exercise uses synthetic data or an explicit architecture brief; no cloud account is needed.

## Brief

Azure enterprise already uses Power BI, Entra identities and Fabric capacity. A team proposes a second platform just to obtain Spark and Iceberg; current reports meet business needs.

## Work

1. Choose platform for the Azure/Power BI scenario.
2. Trace OneLake shortcut and virtualization freshness.
3. Define schema/partition/delete compatibility tests and a fallback when conversion fails.

## Evidence packet

Submit inputs/assumptions, a hypothesis, observed output or sourced capabilities, a rejected alternative, failure analysis and a decision with acceptance/reversal criteria. Tag each item LOCAL ICEBERG, SOURCED PLATFORM or ARCHITECTURE EVIDENCE.


Use [current platform support](/iceberg/current-platform-support) and [decision ADRs](/adr/ADR-002-platform-choice). No platform benchmark or cloud deployment is claimed by this exercise.

## Failure review

A source evolves partition specs. Spark Iceberg query remains correct but OneLake conversion fails and keeps last converted state. A dropped v3 column changes report schema. Success in source engine does not mean fresh Fabric report.

Name the violated invariant, responsible layer and a test that distinguishes the cause from a competing hypothesis.

## PASS criteria

PASS requires every work item and an evidence-scoped conclusion. NOT YET: feature checklist, unqualified speed claims, or format/catalog/platform conflation.
