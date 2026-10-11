---
title: 'Lab 17 · Stateless vs stateful streaming'
description: Actual local streaming query với deterministic file arrivals và business-state checks.
prev:
  text: 'Chapter 17'
  link: /streaming/17-stateless-stateful
next:
  text: 'Continue learning'
  link: /streaming/18-checkpoints
---

# Lab 17 · Stateless vs stateful streaming

Cost: **FREE / LOCAL**. Execution scope: **Actual Spark Structured Streaming + Delta**, controlled tiny JSON file source. Controlled query stop/restart where used; no process kill.

## Before you run

Đọc [Chapter 17](/streaming/17-stateless-stateful) và [local runtime setup](/setup/local-spark). Runtime Spark 4.0.4, Delta 4.0.1; Docker repo read-only, run outputs dưới .skills-test/spark. Dataset nhỏ, integer USD cents, UTC; không benchmark. Mỗi run có isolated checkpoint và targets.

## Input and reasoning tasks

Lab 17: E1 U1=10, E2 U2=20; batch sau E3 U1=5. Running result U1=(15,2), U2=(20,1). Sau stop và restart cùng checkpoint, E4 U2=7 phải tạo U2=(27,2), không đếm lại E1-E3. Amount là integer USD cents, event_time typed UTC timestamp.

Viết expected business state và retry/recovery contract trước chạy. Chỉ ra source replay assumption, state keys/lifetime, output mode và sink effects. Lab 17 implementation nằm trong labs/streaming/experiments.py::lab17.

## Run

```powershell
python scripts/run_streaming.py --lab 17
python scripts/test_streaming.py test_17
```

All-suite command: `python scripts/test_streaming.py`. Source files publish atomically rồi `processAllAvailable()` drain finite known inputs. Tests không assert exact duration, rate hoặc fixed global batch count; state cleanup có thể tạo no-data batches.

## Expected outcome and evidence

U1 amount=15/events=2; U2 amount=27/events=2. Query ID giữ nguyên, run ID đổi; checkpoint state files và state metrics tồn tại.

Mở run/lab17/result.json: exact sorted target rows/hash, query ID/run ID, recentProgress, input rows, source positions và state metrics nếu query có state. Checkpoint inventory là actual file list, không copy raw state vào site. Rates/durations là measured signals, không fixed threshold assertion. Failed batch có thể chưa được ghi trong completed progress; Lab 23 lưu sink callback attempts và failed checkpoint inventory riêng.

[Streaming evidence](/labs/streaming-evidence) có selected artifact downloads. Snapshot không thay việc chạy tests với code hiện tại.

## PASS / NOT YET

PASS: Phân loại operations, chứng minh aggregate sau restart và chỉ ra unbounded state-growth mechanism. NOT YET nếu chỉ đưa console screenshot hoặc giải thích guarantee vượt source/sink đã test.
