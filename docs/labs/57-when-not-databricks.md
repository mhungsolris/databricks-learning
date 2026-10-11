---
title: 'Lab 57 · When not to use Databricks'
description: 'Produce semantic or architecture evidence for Chapter 57.'
prev:
  text: Chapter 57
  link: /system-design/57-when-not-databricks
next:
  text: Next dependency
  link: /system-design/58-lock-in-layers
---

# Lab 57 · When not to use Databricks

Read [Chapter 57](/system-design/57-when-not-databricks) first. This exercise uses synthetic data or an explicit architecture brief; no cloud account is needed.

## Brief

5 GB/day, dashboard every30 minutes. Proposed design: Kafka → Spark Streaming → Databricks → Iceberg → Kubernetes. One engineer owns it; sources are rate-limited APIs and no per-event response SLA exists.

## Work

1. Simplify the5 GB/day proposal and allocate latency budget.
2. Reject each extra component with a requirement/owner argument.
3. Retain idempotency, source cutoff, quarantine and publication checks.
4. Define two measurable triggers for reevaluation.

## Evidence packet

Submit inputs/assumptions, a hypothesis, observed output or sourced capabilities, a rejected alternative, failure analysis and a decision with acceptance/reversal criteria. Tag each item LOCAL ICEBERG, SOURCED PLATFORM or ARCHITECTURE EVIDENCE.


Use [current platform support](/iceberg/current-platform-support) and [decision ADRs](/adr/ADR-002-platform-choice). No platform benchmark or cloud deployment is claimed by this exercise.

## Failure review

The overengineered design needs stateful checkpoints, Kafka retention, multiple identities and Kubernetes on-call. A missed API cutoff still produces stale revenue. Complexity increases repair paths without achieving fresher source data.

Name the violated invariant, responsible layer and a test that distinguishes the cause from a competing hypothesis.

## PASS criteria

PASS requires every work item and an evidence-scoped conclusion. NOT YET: feature checklist, unqualified speed claims, or format/catalog/platform conflation.
