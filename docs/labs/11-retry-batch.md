---
title: 'Lab 11 · Retry the Same Batch'
description: Bài tập có business-state assertions và audit evidence.
prev:
  text: 'Chapter 11'
  link: /correctness/11-idempotency
next:
  text: 'Chapter 12'
  link: /correctness/12-merge-correctness
---

# Lab 11 · Retry the Same Batch

Execution scope: **Actual Delta**. Money = integer USD cents; timestamps = UTC. Dataset nhỏ để đọc và so state, không là production benchmark.

## Before you run

Đọc [Chapter 11](/correctness/11-idempotency) và [local runtime setup](/setup/local-spark). Runtime pin Spark 4.0.4, Java 17, Delta 4.0.1. Host runner dùng Docker; source repo read-only trong container, outputs nằm dưới .skills-test/spark.

## Input and reasoning tasks

E123 revenue 100 cents, stable key adjust/appA/E123, revision 1 gửi 3 lần. Python fault injection trước write và sau target commit/trước ack.

Ingest batch vào fixed-schema Delta. Replay và so exact business state/hash; đọc history versions. Reproduce broken append revenue 300; fix source resolve và deterministic upsert. Retry sau mỗi fault, so với one successful execution.

Trước xem expected outcome, ghi grain/key, source assumptions, exact intended state và invariant cho retry/replay. Kiểm cả failure có thể xảy ra khi command success.

## Run

```powershell
python scripts/run_correctness.py --lab 11
python -m unittest discover -s tests -v
python scripts/test_correctness.py
```

Runner xuất run directory và PASS chỉ sau bounded assertions. Integration suite kiểm actual Delta cases, không tự fallback SQLite. Core model ở labs/correctness/model.py; actual writes ở labs/correctness/delta_labs.py.

## Expected outcome and evidence

Safe one row/revenue 100; onceHash=replayHash=ackRetryHash. Broken raw append 3 rows/revenue 300 là intentional failure. History có thể thêm commit dù business state unchanged. Fault injection là Python exception, chưa là process-kill test.

Mở result.json trong lab 11; actual Delta labs còn có sorted business states, SHA-256 hashes và DESCRIBE HISTORY. [Correctness evidence](/labs/correctness-evidence) giữ selected snapshots để giải thích invariants, không sao chép mọi transient files.

## PASS / NOT YET

PASS khi giải thích vì sao expected state đúng, chỉ ra violated contract của broken path và đưa exact checks cho retry/mismatch. NOT YET nếu chỉ đưa screenshot command chạy xong, counts không so grain, hoặc dùng hash thay business identity.

Nếu changing source semantics, sửa expected contract trước khi thay assertions; không bỏ failing invariant để có PASS.

