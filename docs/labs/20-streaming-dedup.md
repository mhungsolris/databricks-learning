---
title: 'Lab 20 · Streaming deduplication'
description: Actual local streaming query với deterministic file arrivals và business-state checks.
prev:
  text: 'Chapter 20'
  link: /streaming/20-streaming-dedup
next:
  text: 'Continue learning'
  link: /streaming/21-stream-stream-joins
---

# Lab 20 · Streaming deduplication

Cost: **FREE / LOCAL**. Execution scope: **Actual Spark Structured Streaming + Delta**, controlled tiny JSON file source. Controlled query stop/restart where used; no process kill.

## Before you run

Đọc [Chapter 20](/streaming/20-streaming-dedup) và [local runtime setup](/setup/local-spark). Runtime Spark 4.0.4, Delta 4.0.1; Docker repo read-only, run outputs dưới .skills-test/spark. Dataset nhỏ, integer USD cents, UTC; không benchmark. Mỗi run có isolated checkpoint và targets.

## Input and reasoning tasks

Lab 20 dùng dropDuplicatesWithinWatermark(KEY), delay 10 minutes: E123 10:00; retry E123 10:01 và distinct E124 10:02; ADVANCE 11:00; original-time E123; refreshed-time E123 11:02. Refreshed event deliberately vi phạm immutable event-time contract để thấy finite dedup horizon.

Viết expected business state và retry/recovery contract trước chạy. Chỉ ra source replay assumption, state keys/lifetime, output mode và sink effects. Lab 20 implementation nằm trong labs/streaming/experiments.py::lab20.

## Run

```powershell
python scripts/run_streaming.py --lab 20
python scripts/test_streaming.py test_20
```

All-suite command: `python scripts/test_streaming.py`. Source files publish atomically rồi `processAllAvailable()` drain finite known inputs. Tests không assert exact duration, rate hoặc fixed global batch count; state cleanup có thể tạo no-data batches.

## Expected outcome and evidence

Target counts 1 → 2 → 3 → 3 → 4; original-time late delivery bị drop; refreshed-time E123 được nhận sau eviction, target có hai E123.

Mở run/lab20/result.json: exact sorted target rows/hash, query ID/run ID, recentProgress, input rows, source positions và state metrics nếu query có state. Checkpoint inventory là actual file list, không copy raw state vào site. Rates/durations là measured signals, không fixed threshold assertion. Failed batch có thể chưa được ghi trong completed progress; Lab 23 lưu sink callback attempts và failed checkpoint inventory riêng.

[Streaming evidence](/labs/streaming-evidence) có selected artifact downloads. Snapshot không thay việc chạy tests với code hiện tại.

## PASS / NOT YET

PASS: Giải thích cả within-horizon suppression, old-time late drop và refreshed-time repeat effect, cùng legitimate mutation path. NOT YET nếu chỉ đưa console screenshot hoặc giải thích guarantee vượt source/sink đã test.
