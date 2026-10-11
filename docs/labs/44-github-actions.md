---
title: 'Lab 44 · GitHub Actions and safe release flow'
prev:
  text: 'Chapter 44'
  link: /production/44-github-actions
next:
  text: 'Next competency'
  link: /production/45-release-rollback
---

# Lab 44 · GitHub Actions and safe release flow

Evidence tier: **PORTABLE**. Additional managed capability: **DATABRICKS WORKSPACE**, `PENDING USER WORKSPACE`. [Reproduction commands and artifact scope](/labs/production-evidence).

## Task

Parse both workflows and test permissions/needs/main guard/action pins. Configure settings only in a user-approved account. Cloud workflows remain PENDING USER WORKSPACE and PENDING GITHUB ENVIRONMENT.

## Submit evidence

Nộp source/config version, input grain/cutoff, actual output/plan hoặc design-only label, hypothesis, selected decision và limits. Khi dùng selected runtime artifacts, đọc [manifest](/evidence/production/manifest.json), rồi giải thích observation thay vì chép kết luận. Không ghi scenario durations thành measured evidence.

## Acceptance

PASS: Existing Pages workflow keeps PR verification separate from publish. New roas-release workflow_dispatch uses no automatic push/PR cloud deployment. It runs portable and local Spark/Delta checks, then dev and staging; optional prod needs successful staging and protected prod environment.

NOT YET: Long-lived token in config; pull_request_target executes fork code with privileges; believe YAML proves protection settings; mutable action refs or latest CLI without review.

Cloud steps require approved workspace/identity, isolated namespace và redacted output. Local/static checks không xác nhận deploy, Job run, expectation metrics, Photon, liquid clustering hoặc system-table access.
