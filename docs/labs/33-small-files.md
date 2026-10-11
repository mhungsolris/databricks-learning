---
title: 'Lab 33 · File size and the small file problem'
prev:
  text: 'Chapter 33'
  link: /production/33-small-files
next:
  text: 'Next competency'
  link: /production/34-data-layout
---

# Lab 33 · File size and the small file problem

Evidence tier: **LOCAL DELTA**. Additional managed capability: **DATABRICKS WORKSPACE**, `PENDING USER WORKSPACE`. [Reproduction commands and artifact scope](/labs/production-evidence).

## Task

Run local Delta layout comparison. Nộp count/bytes/stats/partitions và equal output. Giải thích vì sao file count, input partitions và runtime là ba observations khác nhau; không suy ra production speedup.

## Submit evidence

Nộp source/config version, input grain/cutoff, actual output/plan hoặc design-only label, hypothesis, selected decision và limits. Khi dùng selected runtime artifacts, đọc [manifest](/evidence/production/manifest.json), rồi giải thích observation thay vì chép kết luận. Không ghi scenario durations thành measured evidence.

## Acceptance

PASS: Tách active file count của snapshot khỏi số files còn nằm trên storage. Delta log chọn active files; file stats hỗ trợ skipping. Predicate hữu ích khi layout/statistics tạo được ranges có thể loại bỏ.

NOT YET: Universal 128MB/1GB rule; equate fewer files with proven speedup; conflate partition pruning and data skipping; compact without checking write/read cost.

Cloud steps require approved workspace/identity, isolated namespace và redacted output. Local/static checks không xác nhận deploy, Job run, expectation metrics, Photon, liquid clustering hoặc system-table access.
