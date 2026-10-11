---
title: 'Lab 41 · Testing strategy and the ROAS test pyramid'
prev:
  text: 'Chapter 41'
  link: /production/41-testing-strategy
next:
  text: 'Next competency'
  link: /production/42-ci-cd
---

# Lab 41 · Testing strategy and the ROAS test pyramid

Evidence tier: **PORTABLE**. Additional managed capability: **DATABRICKS WORKSPACE**, `PENDING USER WORKSPACE`. [Reproduction commands and artifact scope](/labs/production-evidence).

## Task

Run pytest plus scripts/test_production.py and check_production_config.py. Submit a pyramid mapping transformations, grain uniqueness, Spark integration, reconciliation and bundle checks to specific failures.

## Submit evidence

Nộp source/config version, input grain/cutoff, actual output/plan hoặc design-only label, hypothesis, selected decision và limits. Khi dùng selected runtime artifacts, đọc [manifest](/evidence/production/manifest.json), rồi giải thích observation thay vì chép kết luận. Không ghi scenario durations thành measured evidence.

## Acceptance

PASS: Small pure transformations make keys/revisions/refunds testable without credentials. Spark integration checks schema, null/cast/SQL behavior and IO; real data checks monitor today’s inputs. Mocks verify call contracts but cannot prove grants or runtime availability.

NOT YET: All fixtures pass means production safe; mocks prove service behavior; unit tests replace freshness; compare floats as money rather than integer/decimal cents.

Cloud steps require approved workspace/identity, isolated namespace và redacted output. Local/static checks không xác nhận deploy, Job run, expectation metrics, Photon, liquid clustering hoặc system-table access.
