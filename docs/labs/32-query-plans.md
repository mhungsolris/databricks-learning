---
title: 'Lab 32 · Query plans and Spark UI reasoning'
prev:
  text: 'Chapter 32'
  link: /production/32-query-plans
next:
  text: 'Next competency'
  link: /production/33-small-files
---

# Lab 32 · Query plans and Spark UI reasoning

Evidence tier: **LOCAL SPARK**. Additional managed capability: **DATABRICKS WORKSPACE**, `PENDING USER WORKSPACE`. [Reproduction commands and artifact scope](/labs/production-evidence).

## Task

Run python scripts/test_production.py. Với A-E, nộp plan excerpt, movement, join strategy, expensive-stage candidates và metric cần thêm. Dùng plans/tasks của selected evidence; thay threshold phải rerun và ghi config.

## Submit evidence

Nộp source/config version, input grain/cutoff, actual output/plan hoặc design-only label, hypothesis, selected decision và limits. Khi dùng selected runtime artifacts, đọc [manifest](/evidence/production/manifest.json), rồi giải thích observation thay vì chép kết luận. Không ghi scenario durations thành measured evidence.

## Acceptance

PASS: Theo scan → filter/project → join/aggregate → Exchange. Filter/select không tự yêu cầu shuffle. GroupBy cần đưa cùng key tới aggregation; broadcast chuyển build side tới executors thay vì shuffle cả hai phía theo join key.

NOT YET: Memorize operators; equate every Exchange with a bug; broadcast a dimension without size evidence; diagnose only from elapsed time.

Cloud steps require approved workspace/identity, isolated namespace và redacted output. Local/static checks không xác nhận deploy, Job run, expectation metrics, Photon, liquid clustering hoặc system-table access.
