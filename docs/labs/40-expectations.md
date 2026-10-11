---
title: 'Lab 40 · Expectations and quality policy'
prev:
  text: 'Chapter 40'
  link: /production/40-expectations
next:
  text: 'Next competency'
  link: /production/41-testing-strategy
---

# Lab 40 · Expectations and quality policy

Evidence tier: **PORTABLE**. Additional managed capability: **DATABRICKS WORKSPACE**, `PENDING USER WORKSPACE`. [Reproduction commands and artifact scope](/labs/production-evidence).

## Task

Use `labs/production/quality-policy.json`: null ID, negative completed amount, duplicate delivery, UNKNOWN country and invalid timestamp. The policy dataset is PORTABLE; actual runtime tests separately evaluate malformed date, identity, money and country predicates. Propose retention/repair and loss accounting for each case before choosing actions.

Classify five defects as WARN/DROP/FAIL/QUARANTINE with justified alternatives. Run AST/decorator and Spark SQL predicate checks. Optional engine metrics remain PENDING USER WORKSPACE.

## Submit evidence

Nộp source/config version, input grain/cutoff, actual output/plan hoặc design-only label, hypothesis, selected decision và limits. Khi dùng selected runtime artifacts, đọc [manifest](/evidence/production/manifest.json), rồi giải thích observation thay vì chép kết luận. Không ghi scenario durations thành measured evidence.

## Acceptance

PASS: UNKNOWN country có thể giữ tiền đúng và warn. Null critical identity có thể fail/hold; malformed input có thể quarantine. Duplicate retry khác conflicting same-revision mutation: uniqueness không phải chỉ một per-row expectation.

NOT YET: DROP always safest; fail rolls back every parallel table; local SQL tests prove expectation engine; universal policy without business semantics.

Cloud steps require approved workspace/identity, isolated namespace và redacted output. Local/static checks không xác nhận deploy, Job run, expectation metrics, Photon, liquid clustering hoặc system-table access.
