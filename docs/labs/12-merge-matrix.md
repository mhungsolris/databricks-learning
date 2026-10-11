---
title: 'Lab 12 · MERGE Matrix'
description: Bài tập có business-state assertions và audit evidence.
prev:
  text: 'Chapter 12'
  link: /correctness/12-merge-correctness
next:
  text: 'Chapter 13'
  link: /correctness/13-time-semantics
---

# Lab 12 · MERGE Matrix

Execution scope: **Actual Delta**. Money = integer USD cents; timestamps = UTC. Dataset nhỏ để đọc và so state, không là production benchmark.

## Before you run

Đọc [Chapter 12](/correctness/12-merge-correctness) và [local runtime setup](/setup/local-spark). Runtime pin Spark 4.0.4, Java 17, Delta 4.0.1. Host runner dùng Docker; source repo read-only trong container, outputs nằm dưới .skills-test/spark.

## Input and reasoning tasks

E123 revisions 1/2/3; E124 là separate event; conflicting E123 revenue 100/200 cùng revision 4; bad additive update.

Run insert/update/replay/duplicate/stale/newer scenarios. Assert exact rows sau từng operation, reject equal-version conflicts trước SQL. Bypass preflight có chủ ý để observe actual engine duplicate-match failure; prove không có new commit.

Trước xem expected outcome, ghi grain/key, source assumptions, exact intended state và invariant cho retry/replay. Kiểm cả failure có thể xảy ra khi command success.

## Run

```powershell
python scripts/run_correctness.py --lab 12
python -m unittest discover -s tests -v
python scripts/test_correctness.py
```

Runner xuất run directory và PASS chỉ sau bounded assertions. Integration suite kiểm actual Delta cases, không tự fallback SQLite. Core model ở labs/correctness/model.py; actual writes ở labs/correctness/delta_labs.py.

## Expected outcome and evidence

Insert 0; update/replay/stale 100; newer E123 revenue 120 và E124 revenue 100 giữ 2 rows. Additive bad update 100→200→300. Duplicate matching source trả named ambiguity error. Integration test còn cho thấy unmatched duplicate source có thể insert 2 rows nếu không preprocess.

Mở result.json trong lab 12; actual Delta labs còn có sorted business states, SHA-256 hashes và DESCRIBE HISTORY. [Correctness evidence](/labs/correctness-evidence) giữ selected snapshots để giải thích invariants, không sao chép mọi transient files.

## PASS / NOT YET

PASS khi giải thích vì sao expected state đúng, chỉ ra violated contract của broken path và đưa exact checks cho retry/mismatch. NOT YET nếu chỉ đưa screenshot command chạy xong, counts không so grain, hoặc dùng hash thay business identity.

Nếu changing source semantics, sửa expected contract trước khi thay assertions; không bỏ failing invariant để có PASS.

