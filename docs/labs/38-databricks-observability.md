---
title: 'Lab 38 · Databricks observability signals'
prev:
  text: 'Chapter 38'
  link: /production/38-databricks-observability
next:
  text: 'Next competency'
  link: /production/39-data-quality
---

# Lab 38 · Databricks observability signals

Evidence tier: **PORTABLE**. Additional managed capability: **DATABRICKS WORKSPACE**, `PENDING USER WORKSPACE`. [Reproduction commands and artifact scope](/labs/production-evidence).

## Task

Inspect the design-only queries in `labs/production/sql/observability.sql`. For an approved workspace, verify each system schema/table and SELECT privileges before running scoped queries. For Lakeflow, inspect update/flow events and expectation counters through an approved event-log view or the documented event_log function. Keep sensitive query/user/payload details private. Define a scheduled SQL alert for stale cost or reconciliation mismatch with a named response owner, without configuring a destination in this exercise.

PORTABLE incident analysis; DATABRICKS WORKSPACE optional queries. Submit an evidence-availability matrix and hypothesis for each of query change, growth, queue/scale, layout, skew and upstream delay. Cloud status PENDING USER WORKSPACE.

## Submit evidence

Nộp source/config version, input grain/cutoff, actual output/plan hoặc design-only label, hypothesis, selected decision và limits. Khi dùng selected runtime artifacts, đọc [manifest](/evidence/production/manifest.json), rồi giải thích observation thay vì chép kết luận. Không ghi scenario durations thành measured evidence.

## Acceptance

PASS: Query history identifies statement/run timing and compute; profile locates operators/IO. Jobs history adds retries/startup; pipeline event log adds update/data-quality context. Billing describes usage, not a complete invoice by itself.

NOT YET: Assume all system tables in Free Edition; use DBU totals as exact cloud bill; claim event-log expectations observed from local predicate tests.

Cloud steps require approved workspace/identity, isolated namespace và redacted output. Local/static checks không xác nhận deploy, Job run, expectation metrics, Photon, liquid clustering hoặc system-table access.
