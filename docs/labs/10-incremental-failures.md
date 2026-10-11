---
title: 'Lab 10 · Incremental Failure Modes'
description: Bài tập có business-state assertions và audit evidence.
prev:
  text: 'Chapter 10'
  link: /ingestion/10-incremental-boundaries
next:
  text: 'Chapter 11'
  link: /correctness/11-idempotency
---

# Lab 10 · Incremental Failure Modes

Execution scope: **Deterministic source model**. Money = integer USD cents; timestamps = UTC. Dataset nhỏ để đọc và so state, không là production benchmark.

## Before you run

Đọc [Chapter 10](/ingestion/10-incremental-boundaries) và [local runtime setup](/setup/local-spark). Runtime pin Spark 4.0.4, Java 17, Delta 4.0.1. Host runner dùng Docker; source repo read-only trong container, outputs nằm dưới .skills-test/spark.

## Input and reasoning tasks

Run 1 A/B/C; run 2 B đổi value, D mới, E old-created/new-updated. F đến sau với updated timestamp đúng boundary; complete snapshot bỏ B để mô hình delete.

Viết naive created cursor rồi so updated cursor, bounded overlap, snapshot diff và full reconciliation. Nêu source guarantees cho từng cách. Dùng BatchJob fault model kiểm fail after_read/after_write không advance cursor trước durable target success.

Trước xem expected outcome, ghi grain/key, source assumptions, exact intended state và invariant cho retry/replay. Kiểm cả failure có thể xảy ra khi command success.

## Run

```powershell
python scripts/run_correctness.py --lab 10
python -m unittest discover -s tests -v
python scripts/test_correctness.py
```

Runner xuất run directory và PASS chỉ sau bounded assertions. Integration suite kiểm actual Delta cases, không tự fallback SQLite. Core model ở labs/correctness/model.py; actual writes ở labs/correctness/delta_labs.py.

## Expected outcome and evidence

Naive chỉ D; updated/diff thấy B/D/E. Exclusive timestamp cursor bỏ F; overlap recover trong giả định bounded arrival. Missing B chỉ là delete nếu snapshot đầy đủ cùng scope/cutoff. Không có universal winner cho mọi source.

Mở result.json trong lab 10; actual Delta labs còn có sorted business states, SHA-256 hashes và DESCRIBE HISTORY. [Correctness evidence](/labs/correctness-evidence) giữ selected snapshots để giải thích invariants, không sao chép mọi transient files.

## PASS / NOT YET

PASS khi giải thích vì sao expected state đúng, chỉ ra violated contract của broken path và đưa exact checks cho retry/mismatch. NOT YET nếu chỉ đưa screenshot command chạy xong, counts không so grain, hoặc dùng hash thay business identity.

Nếu changing source semantics, sửa expected contract trước khi thay assertions; không bỏ failing invariant để có PASS.

