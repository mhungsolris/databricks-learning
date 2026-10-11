---
title: 'Lab 42 · CI/CD for data engineering'
prev:
  text: 'Chapter 42'
  link: /production/42-ci-cd
next:
  text: 'Next competency'
  link: /production/43-declarative-automation-bundles
---

# Lab 42 · CI/CD for data engineering

Evidence tier: **PORTABLE**. Additional managed capability: **DATABRICKS WORKSPACE**, `PENDING USER WORKSPACE`. [Reproduction commands and artifact scope](/labs/production-evidence).

## Task

PORTABLE release design. Review manual workflow and environment trust policy; prove failed tests block deploy and staging blocks prod. DATABRICKS WORKSPACE acceptance remains pending.

## Submit evidence

Nộp source/config version, input grain/cutoff, actual output/plan hoặc design-only label, hypothesis, selected decision và limits. Khi dùng selected runtime artifacts, đọc [manifest](/evidence/production/manifest.json), rồi giải thích observation thay vì chép kết luận. Không ghi scenario durations thành measured evidence.

## Acceptance

PASS: Git → PR → tests → static/strict validate → deploy dev → integration → staging → approval → prod. Three environments are a worked example; smaller teams may choose two with documented isolation/risk.

NOT YET: Manual notebook edit as preferred workflow; long-lived personal token forever; three environments mandatory everywhere; deploy success equals data correctness.

Cloud steps require approved workspace/identity, isolated namespace và redacted output. Local/static checks không xác nhận deploy, Job run, expectation metrics, Photon, liquid clustering hoặc system-table access.
