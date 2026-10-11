---
title: 'Lab 14 · 72H Attribution'
description: Bài tập có business-state assertions và audit evidence.
prev:
  text: 'Chapter 14'
  link: /correctness/14-late-lookback-reconciliation
next:
  text: 'Chapter 15'
  link: /correctness/15-backfill-reconciliation
---

# Lab 14 · 72H Attribution

Execution scope: **Actual Delta sink; synthetic source retrieval**. Money = integer USD cents; timestamps = UTC. Dataset nhỏ để đọc và so state, không là production benchmark.

## Before you run

Đọc [Chapter 14](/correctness/14-late-lookback-reconciliation) và [local runtime setup](/setup/local-spark). Runtime pin Spark 4.0.4, Java 17, Delta 4.0.1. Host runner dùng Docker; source repo read-only trong container, outputs nằm dưới .skills-test/spark.

## Input and reasoning tasks

E1 at T0=0, T+1 day=100, T+2 days=120; same event time, ordered revisions. 15 min freshness/72h mutable history là running-case assumptions.

Compare event-time 15 min retrieval với lookback 72h hoặc trustworthy updated_at. Resolve revisions, MERGE, replay tất cả snapshots, reconcile content/keys/day totals. Intentionally corrupt target expectation to 220 và show failure.

Trước xem expected outcome, ghi grain/key, source assumptions, exact intended state và invariant cho retry/replay. Kiểm cả failure có thể xảy ra khi command success.

## Run

```powershell
python scripts/run_correctness.py --lab 14
python -m unittest discover -s tests -v
python scripts/test_correctness.py
```

Runner xuất run directory và PASS chỉ sau bounded assertions. Integration suite kiểm actual Delta cases, không tự fallback SQLite. Core model ở labs/correctness/model.py; actual writes ở labs/correctness/delta_labs.py.

## Expected outcome and evidence

Final E1=120; replay hash stable. Missing old corrections leaves 0, append states sums 220, cả hai sai. Mismatch reconciliation phải FAIL. Lab không gọi source API hay thực thi streaming watermark.

Mở result.json trong lab 14; actual Delta labs còn có sorted business states, SHA-256 hashes và DESCRIBE HISTORY. [Correctness evidence](/labs/correctness-evidence) giữ selected snapshots để giải thích invariants, không sao chép mọi transient files.

## PASS / NOT YET

PASS khi giải thích vì sao expected state đúng, chỉ ra violated contract của broken path và đưa exact checks cho retry/mismatch. NOT YET nếu chỉ đưa screenshot command chạy xong, counts không so grain, hoặc dùng hash thay business identity.

Nếu changing source semantics, sửa expected contract trước khi thay assertions; không bỏ failing invariant để có PASS.

