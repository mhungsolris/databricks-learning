---
title: 'Lab 35 · Photon and engine optimization'
prev:
  text: 'Chapter 35'
  link: /production/35-photon
next:
  text: 'Next competency'
  link: /production/36-performance-case-study
---

# Lab 35 · Photon and engine optimization

Evidence tier: **PORTABLE**. Additional managed capability: **DATABRICKS WORKSPACE**, `PENDING USER WORKSPACE`. [Reproduction commands and artifact scope](/labs/production-evidence).

## Task

PORTABLE engine decision: identify semantic failure, candidate supported operators and needed measurements. Optional WORKSPACE compare engine coverage without promising a fixed speedup; PENDING USER WORKSPACE.

## Submit evidence

Nộp source/config version, input grain/cutoff, actual output/plan hoặc design-only label, hypothesis, selected decision và limits. Khi dùng selected runtime artifacts, đọc [manifest](/evidence/production/manifest.json), rồi giải thích observation thay vì chép kết luận. Không ghi scenario durations thành measured evidence.

## Acceptance

PASS: Join grain/fan-out tạo wrong rows trước engine acceleration. Photon xử lý columnar batches cho supported operators, có fallback cho unsupported portions. Nó không sửa business keys, pathological skew hay wrong SQL.

NOT YET: Enable Photon as full diagnosis; claim every streaming operation accelerated; quote vendor benchmarks as local evidence; ignore billing rates.

Cloud steps require approved workspace/identity, isolated namespace và redacted output. Local/static checks không xác nhận deploy, Job run, expectation metrics, Photon, liquid clustering hoặc system-table access.
