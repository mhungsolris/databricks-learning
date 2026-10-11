---
title: 'Lab 22 · Output modes and sink semantics'
description: Actual local streaming query với deterministic file arrivals và business-state checks.
prev:
  text: 'Chapter 22'
  link: /streaming/22-output-modes-sinks
next:
  text: 'Continue learning'
  link: /streaming/23-delivery-semantics
---

# Lab 22 · Output modes and sink semantics

Cost: **FREE / LOCAL**. Execution scope: **Actual Spark Structured Streaming + Delta**, controlled tiny JSON file source. Controlled query stop/restart where used; no process kill.

## Before you run

Đọc [Chapter 22](/streaming/22-output-modes-sinks) và [local runtime setup](/setup/local-spark). Runtime Spark 4.0.4, Delta 4.0.1; Docker repo read-only, run outputs dưới .skills-test/spark. Dataset nhỏ, integer USD cents, UTC; không benchmark. Mỗi run có isolated checkpoint và targets.

## Input and reasoning tasks

Lab 22 compares update vs complete: first E1 U1=10/E2 U2=20, second E3 U1=5. Second update emits only U1=(15,2); complete emits U1=(15,2), U2=(20,1). Append window initial result rỗng, khi event progress advance mới emit window amount=30.

Viết expected business state và retry/recovery contract trước chạy. Chỉ ra source replay assumption, state keys/lifetime, output mode và sink effects. Lab 22 implementation nằm trong labs/streaming/experiments.py::lab22.

## Run

```powershell
python scripts/run_streaming.py --lab 22
python scripts/test_streaming.py test_22
```

All-suite command: `python scripts/test_streaming.py`. Source files publish atomically rồi `processAllAvailable()` drain finite known inputs. Tests không assert exact duration, rate hoặc fixed global batch count; state cleanup có thể tạo no-data batches.

## Expected outcome and evidence

Second update emits 1 key, complete 2 keys; append window emits 0 trước finalization, rồi 1 finalized window amount=30.

Mở run/lab22/result.json: exact sorted target rows/hash, query ID/run ID, recentProgress, input rows, source positions và state metrics nếu query có state. Checkpoint inventory là actual file list, không copy raw state vào site. Rates/durations là measured signals, không fixed threshold assertion. Failed batch có thể chưa được ghi trong completed progress; Lab 23 lưu sink callback attempts và failed checkpoint inventory riêng.

[Streaming evidence](/labs/streaming-evidence) có selected artifact downloads. Snapshot không thay việc chạy tests với code hiện tại.

## PASS / NOT YET

PASS: Đọc actual emissions cho ba modes và chọn sink contract bảo toàn aggregate qua retry. NOT YET nếu chỉ đưa console screenshot hoặc giải thích guarantee vượt source/sink đã test.
