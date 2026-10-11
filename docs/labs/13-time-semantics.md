---
title: 'Lab 13 · Time Semantics'
description: Bài tập có business-state assertions và audit evidence.
prev:
  text: 'Chapter 13'
  link: /correctness/13-time-semantics
next:
  text: 'Chapter 14'
  link: /correctness/14-late-lookback-reconciliation
---

# Lab 13 · Time Semantics

Execution scope: **Deterministic time model**. Money = integer USD cents; timestamps = UTC. Dataset nhỏ để đọc và so state, không là production benchmark.

## Before you run

Đọc [Chapter 13](/correctness/13-time-semantics) và [local runtime setup](/setup/local-spark). Runtime pin Spark 4.0.4, Java 17, Delta 4.0.1. Host runner dùng Docker; source repo read-only trong container, outputs nằm dưới .skills-test/spark.

## Input and reasoning tasks

Purchase 10:00, arrival 10:03, processing 10:15, update nextday 08:00. Separate midnight fixture L1 eventOct 1 23:59Z/processOct 2 00:15Z.

Chọn timestamp cho business reporting, source retrieval, monitoring và late-data reasoning. Explain clock owner/timezone. Compare correct event-date grouping với wrong processing-date grouping; keep original event time qua attribution update.

Trước xem expected outcome, ghi grain/key, source assumptions, exact intended state và invariant cho retry/replay. Kiểm cả failure có thể xảy ra khi command success.

## Run

```powershell
python scripts/run_correctness.py --lab 13
python -m unittest discover -s tests -v
python scripts/test_correctness.py
```

Runner xuất run directory và PASS chỉ sau bounded assertions. Integration suite kiểm actual Delta cases, không tự fallback SQLite. Core model ở labs/correctness/model.py; actual writes ở labs/correctness/delta_labs.py.

## Expected outcome and evidence

L1 revenue 100 thuộcOct 1; processing-date grouping chuyển nhầm sangOct 2. Model UTC policy rõ; source update time không được mặc định là report date.

Mở result.json trong lab 13; actual Delta labs còn có sorted business states, SHA-256 hashes và DESCRIBE HISTORY. [Correctness evidence](/labs/correctness-evidence) giữ selected snapshots để giải thích invariants, không sao chép mọi transient files.

## PASS / NOT YET

PASS khi giải thích vì sao expected state đúng, chỉ ra violated contract của broken path và đưa exact checks cho retry/mismatch. NOT YET nếu chỉ đưa screenshot command chạy xong, counts không so grain, hoặc dùng hash thay business identity.

Nếu changing source semantics, sửa expected contract trước khi thay assertions; không bỏ failing invariant để có PASS.

