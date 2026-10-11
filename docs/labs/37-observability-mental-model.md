---
title: 'Lab 37 · Observability mental model'
prev:
  text: 'Chapter 37'
  link: /production/37-observability-mental-model
next:
  text: 'Next competency'
  link: /production/38-databricks-observability
---

# Lab 37 · Observability mental model

Evidence tier: **PORTABLE**. Additional managed capability: **DATABRICKS WORKSPACE**, `PENDING USER WORKSPACE`. [Reproduction commands and artifact scope](/labs/production-evidence).

## Task

PORTABLE health test. Reproduce SUCCESS with stale cost and wrong reconciliation. Define four-layer metrics, timestamp meanings, alert owner, bounded action and release correlation.

## Submit evidence

Nộp source/config version, input grain/cutoff, actual output/plan hoặc design-only label, hypothesis, selected decision và limits. Khi dùng selected runtime artifacts, đọc [manifest](/evidence/production/manifest.json), rồi giải thích observation thay vì chép kết luận. Không ghi scenario durations thành measured evidence.

## Acceptance

PASS: Correlate business cutoff, run/query IDs, release version and source delivery. Answer what happened, where, since when, affected scopes and what changed; avoid alerts without owners or actions.

NOT YET: Treat execution status as freshness; one global threshold for all apps; alert without scope/owner/runbook; hide stale cost behind fresh revenue.

Cloud steps require approved workspace/identity, isolated namespace và redacted output. Local/static checks không xác nhận deploy, Job run, expectation metrics, Photon, liquid clustering hoặc system-table access.
