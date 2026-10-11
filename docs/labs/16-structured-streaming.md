---
title: 'Lab 16 · Structured Streaming mental model'
description: Actual local streaming query với deterministic file arrivals và business-state checks.
prev:
  text: 'Chapter 16'
  link: /streaming/16-structured-streaming
next:
  text: 'Continue learning'
  link: /streaming/17-stateless-stateful
---

# Lab 16 · Structured Streaming mental model

Cost: **FREE / LOCAL**. Execution scope: **Actual Spark Structured Streaming + Delta**, controlled tiny JSON file source. Controlled query stop/restart where used; no process kill.

## Before you run

Đọc [Chapter 16](/streaming/16-structured-streaming) và [local runtime setup](/setup/local-spark). Runtime Spark 4.0.4, Delta 4.0.1; Docker repo read-only, run outputs dưới .skills-test/spark. Dataset nhỏ, integer USD cents, UTC; không benchmark. Mỗi run có isolated checkpoint và targets.

## Input and reasoning tasks

Lab 16 atomically publishes ba JSON files chứa 3, 2, 1 events. Source có explicit schema và maxFilesPerTrigger=1; vì input được publish từng phase và drain xong trước phase sau, lab quan sát nhiều positive-input batches. Đây là fixture điều khiển, không là quy luật row count của streaming.

Viết expected business state và retry/recovery contract trước chạy. Chỉ ra source replay assumption, state keys/lifetime, output mode và sink effects. Lab 16 implementation nằm trong labs/streaming/experiments.py::lab16.

## Run

```powershell
python scripts/run_streaming.py --lab 16
python scripts/test_streaming.py test_16
```

All-suite command: `python scripts/test_streaming.py`. Source files publish atomically rồi `processAllAvailable()` drain finite known inputs. Tests không assert exact duration, rate hoặc fixed global batch count; state cleanup có thể tạo no-data batches.

## Expected outcome and evidence

Target tăng 3 → 5 → 6; nhiều batch IDs có input; query active tại các snapshots và stop sạch. Checkpoint có metadata, offsets, commits và file-source log.

Mở run/lab16/result.json: exact sorted target rows/hash, query ID/run ID, recentProgress, input rows, source positions và state metrics nếu query có state. Checkpoint inventory là actual file list, không copy raw state vào site. Rates/durations là measured signals, không fixed threshold assertion. Failed batch có thể chưa được ghi trong completed progress; Lab 23 lưu sink callback attempts và failed checkpoint inventory riêng.

[Streaming evidence](/labs/streaming-evidence) có selected artifact downloads. Snapshot không thay việc chạy tests với code hiện tại.

## PASS / NOT YET

PASS: Chỉ ra source/transform/sink, đọc positive-input batch IDs và rates, giải thích một query active qua nhiều batches rồi clean stop. NOT YET nếu chỉ đưa console screenshot hoặc giải thích guarantee vượt source/sink đã test.
