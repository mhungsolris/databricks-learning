---
title: 'Lab 09 · ROAS Medallion Design'
description: Bài tập có business-state assertions và audit evidence.
prev:
  text: 'Chapter 09'
  link: /architecture/09-medallion
next:
  text: 'Chapter 10'
  link: /ingestion/10-incremental-boundaries
---

# Lab 09 · ROAS Medallion Design

Execution scope: **Design/model**. Money = integer USD cents; timestamps = UTC. Dataset nhỏ để đọc và so state, không là production benchmark.

## Before you run

Đọc [Chapter 09](/architecture/09-medallion) và [local runtime setup](/setup/local-spark). Runtime pin Spark 4.0.4, Java 17, Delta 4.0.1. Host runner dùng Docker; source repo read-only trong container, outputs nằm dưới .skills-test/spark.

## Input and reasoning tasks

`deliveries()` và `costs()` trong model.py: duplicate callback, mutable E1, missing campaign và four daily cost platforms.

Định nghĩa grain/key của raw deliveries, cleaned latest event states, daily cost và reporting mart. Giữ payload/ingestion metadata ở Bronze; xác định normalization/conflict policy ở Silver. Trước Gold, chứng minh uniqueness của conformed dimensions và aggregate revenue về đúng daily cost grain.

Trước xem expected outcome, ghi grain/key, source assumptions, exact intended state và invariant cho retry/replay. Kiểm cả failure có thể xảy ra khi command success.

## Run

```powershell
python scripts/run_correctness.py --lab 09
python -m unittest discover -s tests -v
python scripts/test_correctness.py
```

Runner xuất run directory và PASS chỉ sau bounded assertions. Integration suite kiểm actual Delta cases, không tự fallback SQLite. Core model ở labs/correctness/model.py; actual writes ở labs/correctness/delta_labs.py.

## Expected outcome and evidence

5 raw deliveries → 3 latest states; revenue 170 cents, cost 140 cents. Missing campaign được giữ thành UNKNOWN; thiếu cost làm ROAS null, không giả cost 0 là known zero. Detail join 40/60 vào daily cost 50 tạo wrong cost 100; correct aggregate/join giữ 50.

Mở result.json trong lab 09; actual Delta labs còn có sorted business states, SHA-256 hashes và DESCRIBE HISTORY. [Correctness evidence](/labs/correctness-evidence) giữ selected snapshots để giải thích invariants, không sao chép mọi transient files.

## PASS / NOT YET

PASS khi giải thích vì sao expected state đúng, chỉ ra violated contract của broken path và đưa exact checks cho retry/mismatch. NOT YET nếu chỉ đưa screenshot command chạy xong, counts không so grain, hoặc dùng hash thay business identity.

Nếu changing source semantics, sửa expected contract trước khi thay assertions; không bỏ failing invariant để có PASS.

