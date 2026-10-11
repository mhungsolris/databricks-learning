---
title: 'Lab 56 · Platform decision framework'
description: 'Produce semantic or architecture evidence for Chapter 56.'
prev:
  text: Chapter 56
  link: /system-design/56-decision-framework
next:
  text: Next dependency
  link: /system-design/57-when-not-databricks
---

# Lab 56 · Platform decision framework

Read [Chapter 56](/system-design/56-decision-framework) first. This exercise uses synthetic data or an explicit architecture brief; no cloud account is needed.

## Brief

Two teams both process20 GB/day. One has3 DEs, 90% SQL on GCP, hourly stable BigQuery; the other has Spark-heavy features, batch+stream, ML and multiple governed consumers. Same volume leads to different decisions.

## Work

1. Produce two requirement→importance→implication scorecards.
2. Cost at least operations, migration and maintenance alongside compute.
3. Record assumptions, rejection conditions and measurable reversal triggers.

## Evidence packet

Submit inputs/assumptions, a hypothesis, observed output or sourced capabilities, a rejected alternative, failure analysis and a decision with acceptance/reversal criteria. Tag each item LOCAL ICEBERG, SOURCED PLATFORM or ARCHITECTURE EVIDENCE.


Use [current platform support](/iceberg/current-platform-support) and [decision ADRs](/adr/ADR-002-platform-choice). No platform benchmark or cloud deployment is claimed by this exercise.

## Failure review

A weighted matrix gives speculative AI10 points and ignores hourly correctness or missing access enforcement. A team migrates because of sunk hype, or refuses needed change because of sunk cost.

Name the violated invariant, responsible layer and a test that distinguishes the cause from a competing hypothesis.

## PASS criteria

PASS requires every work item and an evidence-scoped conclusion. NOT YET: feature checklist, unqualified speed claims, or format/catalog/platform conflation.
