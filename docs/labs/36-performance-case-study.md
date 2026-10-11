---
title: 'Lab 36 · ROAS performance case study'
prev:
  text: 'Chapter 36'
  link: /production/36-performance-case-study
next:
  text: 'Next competency'
  link: /production/37-observability-mental-model
---

# Lab 36 · ROAS performance case study

Evidence tier: **PORTABLE**. Additional managed capability: **DATABRICKS WORKSPACE**, `PENDING USER WORKSPACE`. [Reproduction commands and artifact scope](/labs/production-evidence).

## Task

Rank seven steps: correctness, plan, skew, layout, query changes, platform optimization, remeasurement. Submit [Performance Diagnosis gate](/assessments/mid-gate-performance-diagnosis) with falsifiable hypotheses and rollback thresholds.

## Submit evidence

Nộp source/config version, input grain/cutoff, actual output/plan hoặc design-only label, hypothesis, selected decision và limits. Khi dùng selected runtime artifacts, đọc [manifest](/evidence/production/manifest.json), rồi giải thích observation thay vì chép kết luận. Không ghi scenario durations thành measured evidence.

## Acceptance

PASS: Check join grain/revision/cutoff first. Then plan movement, skew distribution, file layout and selectivity. A date filter reading 90% naturally skips little; adding clustering alone cannot eliminate required rows.

NOT YET: Photon-only answer; salt without proving aggregate algebra; cache every frame; remove UNKNOWN business data; benchmark different cutoffs.

Cloud steps require approved workspace/identity, isolated namespace và redacted output. Local/static checks không xác nhận deploy, Job run, expectation metrics, Photon, liquid clustering hoặc system-table access.
