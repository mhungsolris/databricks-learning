---
title: 'Lab 21 · Stream-stream joins and state lifetime'
description: Actual local streaming query với deterministic file arrivals và business-state checks.
prev:
  text: 'Chapter 21'
  link: /streaming/21-stream-stream-joins
next:
  text: 'Continue learning'
  link: /streaming/22-output-modes-sinks
---

# Lab 21 · Stream-stream joins and state lifetime

Cost: **FREE / LOCAL**. Execution scope: **Actual Spark Structured Streaming + Delta**, controlled tiny JSON file source. Controlled query stop/restart where used; no process kill.

## Before you run

Đọc [Chapter 21](/streaming/21-stream-stream-joins) và [local runtime setup](/setup/local-spark). Runtime Spark 4.0.4, Delta 4.0.1; Docker repo read-only, run outputs dưới .skills-test/spark. Dataset nhỏ, integer USD cents, UTC; không benchmark. Mỗi run có isolated checkpoint và targets.

## Input and reasoning tasks

Lab dùng both-side WM=10m, full click_id/user_id match và 20m time range. Sau P2 delayed delivery, cả hai streams nhận future control events lúc 11:00/11:01 để advance progress. C3 NULL chỉ được asserted sau observed closure, không sau fixed sleep.

Viết expected business state và retry/recovery contract trước chạy. Chỉ ra source replay assumption, state keys/lifetime, output mode và sink effects. Lab 21 implementation nằm trong labs/streaming/experiments.py::lab21.

## Run

```powershell
python scripts/run_streaming.py --lab 21
python scripts/test_streaming.py test_21
```

All-suite command: `python scripts/test_streaming.py`. Source files publish atomically rồi `processAllAvailable()` drain finite known inputs. Tests không assert exact duration, rate hoặc fixed global batch count; state cleanup có thể tạo no-data batches.

## Expected outcome and evidence

C1/P1 và C2/P2 match; C3 chưa xuất hiện trước closure, sau advancement có C3/NULL; two source progress entries và state removals.

Mở run/lab21/result.json: exact sorted target rows/hash, query ID/run ID, recentProgress, input rows, source positions và state metrics nếu query có state. Checkpoint inventory là actual file list, không copy raw state vào site. Rates/durations là measured signals, không fixed threshold assertion. Failed batch có thể chưa được ghi trong completed progress; Lab 23 lưu sink callback attempts và failed checkpoint inventory riêng.

[Streaming evidence](/labs/streaming-evidence) có selected artifact downloads. Snapshot không thay việc chạy tests với code hiện tại.

## PASS / NOT YET

PASS: Chứng minh initial match, delayed match, controlled unmatched NULL và state removals; giải thích idle-input limitation. NOT YET nếu chỉ đưa console screenshot hoặc giải thích guarantee vượt source/sink đã test.
