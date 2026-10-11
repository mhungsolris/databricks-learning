---
title: 'Lab 45 · Release safety, code rollback and data repair'
prev:
  text: 'Chapter 45'
  link: /production/45-release-rollback
next:
  text: 'Next competency'
  link: /assessments/mid-gate-production-readiness
---

# Lab 45 · Release safety, code rollback and data repair

Evidence tier: **LOCAL DELTA**. Additional managed capability: **DATABRICKS WORKSPACE**, `PENDING USER WORKSPACE`. [Reproduction commands and artifact scope](/labs/production-evidence).

## Task

Run local Delta restore and failed-candidate tests. Submit release runbook and [Production Readiness gate](/assessments/mid-gate-production-readiness). Define what happens when history/files are unavailable.

## Submit evidence

Nộp source/config version, input grain/cutoff, actual output/plan hoặc design-only label, hypothesis, selected decision và limits. Khi dùng selected runtime artifacts, đọc [manifest](/evidence/production/manifest.json), rồi giải thích observation thay vì chép kết luận. Không ghi scenario durations thành measured evidence.

## Acceptance

PASS: Hold bad downstream publication first; identify affected cutoffs/keys/releases. Restore a known code version for future writes, then choose Delta RESTORE, staged backfill or retained-source replay for data. Reconcile exact state and dependent reports before unblocking.

NOT YET: bundle destroy as rollback; code redeploy repairs data; RESTORE is free of downstream effects; table history is indefinite backup.

Cloud steps require approved workspace/identity, isolated namespace và redacted output. Local/static checks không xác nhận deploy, Job run, expectation metrics, Photon, liquid clustering hoặc system-table access.
