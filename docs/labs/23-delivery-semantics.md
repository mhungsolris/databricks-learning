---
title: 'Lab 23 · Delivery semantics across source, engine and sink'
description: Actual local streaming query với deterministic file arrivals và business-state checks.
prev:
  text: 'Chapter 23'
  link: /streaming/23-delivery-semantics
next:
  text: 'Continue learning'
  link: /streaming/24-recovery-runbook
---

# Lab 23 · Delivery semantics across source, engine and sink

Cost: **FREE / LOCAL**. Execution scope: **Actual Spark Structured Streaming + Delta**, controlled tiny JSON file source. Controlled exception after durable sink write; no process kill.

## Before you run

Đọc [Chapter 23](/streaming/23-delivery-semantics) và [local runtime setup](/setup/local-spark). Runtime Spark 4.0.4, Delta 4.0.1; Docker repo read-only, run outputs dưới .skills-test/spark. Dataset nhỏ, integer USD cents, UTC; không benchmark. Mỗi run có isolated checkpoint và targets.

## Input and reasoning tasks

Lab 23 injects SIMULATED_AFTER_SINK_COMMIT sau actual Delta append. Failed checkpoint có offsets/N nhưng chưa commits/N. Same cp restart retries same observed batch ID. Unsafe append target 2×100; txnAppId + txnVersion=batchId giữ 1×100.

Viết expected business state và retry/recovery contract trước chạy. Chỉ ra source replay assumption, state keys/lifetime, output mode và sink effects. Lab 23 implementation nằm trong labs/streaming/experiments.py::lab23.

## Run

```powershell
python scripts/run_streaming.py --lab 23
python scripts/test_streaming.py test_23
```

All-suite command: `python scripts/test_streaming.py`. Source files publish atomically rồi `processAllAvailable()` drain finite known inputs. Tests không assert exact duration, rate hoặc fixed global batch count; state cleanup có thể tạo no-data batches.

## Expected outcome and evidence

Cả hai cases ghi sink trước exception, retry cùng batch ID. Unsafe có 2 rows/200 cents; transactional có 1 row/100 cents; engine commit tồn tại sau recovery.

Mở run/lab23/result.json: exact sorted target rows/hash, query ID/run ID, recentProgress, input rows, source positions và state metrics nếu query có state. Checkpoint inventory là actual file list, không copy raw state vào site. Rates/durations là measured signals, không fixed threshold assertion. Failed batch có thể chưa được ghi trong completed progress; Lab 23 lưu sink callback attempts và failed checkpoint inventory riêng.

[Streaming evidence](/labs/streaming-evidence) có selected artifact downloads. Snapshot không thay việc chạy tests với code hiện tại.

## PASS / NOT YET

PASS: Chứng minh durable sink write trước failure, same batch retried, target unsafe/safe khác nhau và nêu guarantee boundaries. NOT YET nếu chỉ đưa console screenshot hoặc giải thích guarantee vượt source/sink đã test.
