---
title: 'Lab 19 · Event-time windows and watermarks'
description: Actual local streaming query với deterministic file arrivals và business-state checks.
prev:
  text: 'Chapter 19'
  link: /streaming/19-windows-watermarks
next:
  text: 'Continue learning'
  link: /streaming/20-streaming-dedup
---

# Lab 19 · Event-time windows and watermarks

Cost: **FREE / LOCAL**. Execution scope: **Actual Spark Structured Streaming + Delta**, controlled tiny JSON file source. Controlled query stop/restart where used; no process kill.

## Before you run

Đọc [Chapter 19](/streaming/19-windows-watermarks) và [local runtime setup](/setup/local-spark). Runtime Spark 4.0.4, Delta 4.0.1; Docker repo read-only, run outputs dưới .skills-test/spark. Dataset nhỏ, integer USD cents, UTC; không benchmark. Mỗi run có isolated checkpoint và targets.

## Input and reasoning tasks

Lab ghi A/B trước, rồi PROGRESS event=10:30 để thực sự advance watermark, cuối cùng C=09:50. Chạy update aggregation ba variants: no watermark, 5 minutes, 2 hours. Arrival order được file phases điều khiển; arrival timestamps trong scenario là explanation, không wall-clock timer của test.

Viết expected business state và retry/recovery contract trước chạy. Chỉ ra source replay assumption, state keys/lifetime, output mode và sink effects. Lab 19 implementation nằm trong labs/streaming/experiments.py::lab19.

## Run

```powershell
python scripts/run_streaming.py --lab 19
python scripts/test_streaming.py test_19
```

All-suite command: `python scripts/test_streaming.py`. Source files publish atomically rồi `processAllAvailable()` drain finite known inputs. Tests không assert exact duration, rate hoặc fixed global batch count; state cleanup có thể tạo no-data batches.

## Expected outcome and evidence

No-watermark và 2h có C window amount=7. 5m không có window C và ghi positive late-drop/removed-state metrics sau observed watermark advance.

Mở run/lab19/result.json: exact sorted target rows/hash, query ID/run ID, recentProgress, input rows, source positions và state metrics nếu query có state. Checkpoint inventory là actual file list, không copy raw state vào site. Rates/durations là measured signals, không fixed threshold assertion. Failed batch có thể chưa được ghi trong completed progress; Lab 23 lưu sink callback attempts và failed checkpoint inventory riêng.

[Streaming evidence](/labs/streaming-evidence) có selected artifact downloads. Snapshot không thay việc chạy tests với code hiện tại.

## PASS / NOT YET

PASS: Tách bốn mechanisms, giải thích one-sided guarantee và chứng minh actual drop/state eviction bằng metrics. NOT YET nếu chỉ đưa console screenshot hoặc giải thích guarantee vượt source/sink đã test.
