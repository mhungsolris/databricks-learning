---
title: 'Lab 15 · Failed Backfill'
description: Bài tập có business-state assertions và audit evidence.
prev:
  text: 'Chapter 15'
  link: /correctness/15-backfill-reconciliation
next:
  text: 'Mid Gate — Pipeline Correctness'
  link: /assessments/mid-gate-pipeline-correctness
---

# Lab 15 · Failed Backfill

Execution scope: **Actual Delta; bounded failure simulation**. Money = integer USD cents; timestamps = UTC. Dataset nhỏ để đọc và so state, không là production benchmark.

## Before you run

Đọc [Chapter 15](/correctness/15-backfill-reconciliation) và [local runtime setup](/setup/local-spark). Runtime pin Spark 4.0.4, Java 17, Delta 4.0.1. Host runner dùng Docker; source repo read-only trong container, outputs nằm dưới .skills-test/spark.

## Input and reasoning tasks

90 daily event rows Jan 1→Apr 1 exclusive, expected 10 cents/day. Production có wrong historical 1 cent/day và LIVE outside scope 77 cents.

Freeze source snapshot, write staging 37 days, inject failure trước publish. Derive completed scope từ durable staging, resume 53, validate/reconcile 90 days, rồi predicate-scoped publish. Rerun entire scope; interleave newer LIVE revenue 88 outside scope và prove nó được giữ.

Trước xem expected outcome, ghi grain/key, source assumptions, exact intended state và invariant cho retry/replay. Kiểm cả failure có thể xảy ra khi command success.

## Run

```powershell
python scripts/run_correctness.py --lab 15
python -m unittest discover -s tests -v
python scripts/test_correctness.py
```

Runner xuất run directory và PASS chỉ sau bounded assertions. Integration suite kiểm actual Delta cases, không tự fallback SQLite. Core model ở labs/correctness/model.py; actual writes ở labs/correctness/delta_labs.py.

## Expected outcome and evidence

Production unchanged trước publish; 90 historical keys/revenue 900; same historical hash qua rerun, LIVE revenue 88 preserved. 37/53 là two bounded chunks, không 90 jobs; concurrent writers/process kill chưa được test.

Mở result.json trong lab 15; actual Delta labs còn có sorted business states, SHA-256 hashes và DESCRIBE HISTORY. [Correctness evidence](/labs/correctness-evidence) giữ selected snapshots để giải thích invariants, không sao chép mọi transient files.

## PASS / NOT YET

PASS khi giải thích vì sao expected state đúng, chỉ ra violated contract của broken path và đưa exact checks cho retry/mismatch. NOT YET nếu chỉ đưa screenshot command chạy xong, counts không so grain, hoặc dùng hash thay business identity.

Nếu changing source semantics, sửa expected contract trước khi thay assertions; không bỏ failing invariant để có PASS.

