---
title: 'Lab 43 · Declarative Automation Bundles'
prev:
  text: 'Chapter 43'
  link: /production/43-declarative-automation-bundles
next:
  text: 'Next competency'
  link: /production/44-github-actions
---

# Lab 43 · Declarative Automation Bundles

Evidence tier: **PORTABLE**. Additional managed capability: **DATABRICKS WORKSPACE**, `PENDING USER WORKSPACE`. [Reproduction commands and artifact scope](/labs/production-evidence).

## Task

Run portable/static and CLI schema checks. Optional approved workspace: strict validate target, inspect plan, deploy dev and run roas; capture redacted run/output evidence. PENDING USER WORKSPACE.

## Submit evidence

Nộp source/config version, input grain/cutoff, actual output/plan hoặc design-only label, hypothesis, selected decision và limits. Khi dùng selected runtime artifacts, đọc [manifest](/evidence/production/manifest.json), rồi giải thích observation thay vì chép kết luận. Không ghi scenario durations thành measured evidence.

## Acceptance

PASS: Repository + source + resource definitions + targets = deployable project. resources/src/tests are useful course organization, not universally required directory names. Resource paths resolve relative to the config file that declares them.

NOT YET: Old primary product name; invented required folder layout; target name automatically grants isolation; destroy used as rollback; skip strict validation before deploy.

Cloud steps require approved workspace/identity, isolated namespace và redacted output. Local/static checks không xác nhận deploy, Job run, expectation metrics, Photon, liquid clustering hoặc system-table access.
