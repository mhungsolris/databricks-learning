---
title: 'Lab 31 · Performance engineering mental model'
prev:
  text: 'Chapter 31'
  link: /production/31-performance-mental-model
next:
  text: 'Next competency'
  link: /production/32-query-plans
---

# Lab 31 · Performance engineering mental model

Evidence tier: **PORTABLE**. Additional managed capability: **DATABRICKS WORKSPACE**, `PENDING USER WORKSPACE`. [Reproduction commands and artifact scope](/labs/production-evidence).

## Task

Lập investigation sheet cho 8→35 phút: năm layers, evidence còn thiếu, hai hypotheses ranked, một change và rollback condition. Dùng local evidence để luyện đọc metrics, không để chứng minh SLA.

## Submit evidence

Nộp source/config version, input grain/cutoff, actual output/plan hoặc design-only label, hypothesis, selected decision và limits. Khi dùng selected runtime artifacts, đọc [manifest](/evidence/production/manifest.json), rồi giải thích observation thay vì chép kết luận. Không ghi scenario durations thành measured evidence.

## Acceptance

PASS: So cùng source cutoff, query/code version, input volume, compute và concurrency. SUCCESS chỉ xác nhận run hoàn thành. Lập một giả thuyết có thể bác bỏ, chọn metric kiểm chứng rồi đổi một biến.

NOT YET: Đổi nhiều knobs cùng lúc; coi tăng cores luôn giảm cost; lấy local elapsed time làm production speedup; bỏ correctness checks sau optimization.

Cloud steps require approved workspace/identity, isolated namespace và redacted output. Local/static checks không xác nhận deploy, Job run, expectation metrics, Photon, liquid clustering hoặc system-table access.
