---
title: 'Lab 39 · Data quality and ROAS contracts'
prev:
  text: 'Chapter 39'
  link: /production/39-data-quality
next:
  text: 'Next competency'
  link: /production/40-expectations
---

# Lab 39 · Data quality and ROAS contracts

Evidence tier: **PORTABLE**. Additional managed capability: **DATABRICKS WORKSPACE**, `PENDING USER WORKSPACE`. [Reproduction commands and artifact scope](/labs/production-evidence).

## Task

PORTABLE and LOCAL SPARK: inject invalid identities, negative amount, invalid date, duplicate cost and missing cost. Classify violations and prove accounting, scoped uniqueness and publication barrier.

## Submit evidence

Nộp source/config version, input grain/cutoff, actual output/plan hoặc design-only label, hypothesis, selected decision và limits. Khi dùng selected runtime artifacts, đọc [manifest](/evidence/production/manifest.json), rồi giải thích observation thay vì chép kết luận. Không ghi scenario durations thành measured evidence.

## Acceptance

PASS: Use scoped identity source_system/app_id/event_id, full reporting grain and separate source cutoffs. Negative completed revenue is invalid only under the stated non-refund contract; refunds require explicit signed transaction semantics.

NOT YET: event_id globally unique assumption; nonnegative rule applied to legitimate refunds; total-only reconciliation; quality equated with unit-test percentage.

Cloud steps require approved workspace/identity, isolated namespace và redacted output. Local/static checks không xác nhận deploy, Job run, expectation metrics, Photon, liquid clustering hoặc system-table access.
