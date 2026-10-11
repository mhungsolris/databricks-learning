---
title: 'Lab 34 · Partitioning, liquid clustering and data skipping'
prev:
  text: 'Chapter 34'
  link: /production/34-data-layout
next:
  text: 'Next competency'
  link: /production/35-photon
---

# Lab 34 · Partitioning, liquid clustering and data skipping

Evidence tier: **PORTABLE**. Additional managed capability: **DATABRICKS WORKSPACE**, `PENDING USER WORKSPACE`. [Reproduction commands and artifact scope](/labs/production-evidence).

## Task

PORTABLE layout decision. Compare a bounded date table, high-cardinality campaign table and evolving predicates. Optional WORKSPACE: inspect CLUSTER BY/AUTO properties, maintenance history and files scanned; PENDING USER WORKSPACE.

## Submit evidence

Nộp source/config version, input grain/cutoff, actual output/plan hoặc design-only label, hypothesis, selected decision và limits. Khi dùng selected runtime artifacts, đọc [manifest](/evidence/production/manifest.json), rồi giải thích observation thay vì chép kết luận. Không ghi scenario durations thành measured evidence.

## Acceptance

PASS: Traditional partitioning tạo physical boundaries và partition pruning. Data skipping dùng file statistics để loại candidate files. Liquid clustering tổ chức dữ liệu linh hoạt theo keys và incremental maintenance; cùng table không kết hợp partitioning hoặc ZORDER với liquid clustering.

NOT YET: Partitioning obsolete everywhere; default ZORDER advice without current docs; promise AUTO always selects keys; equate compaction with skipping.

Cloud steps require approved workspace/identity, isolated namespace và redacted output. Local/static checks không xác nhận deploy, Job run, expectation metrics, Photon, liquid clustering hoặc system-table access.
