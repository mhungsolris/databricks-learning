---
title: 'Lab 24 · Recovery and checkpoint failure'
description: Actual local streaming query với deterministic file arrivals và business-state checks.
prev:
  text: 'Chapter 24'
  link: /streaming/24-recovery-runbook
next:
  text: 'Continue learning'
  link: /assessments/mid-gate-streaming-correctness
---

# Lab 24 · Recovery and checkpoint failure

Cost: **FREE / LOCAL**. Execution scope: **Actual Spark Structured Streaming + Delta**, controlled tiny JSON file source. Controlled query stop/restart where used; no process kill.

## Before you run

Đọc [Chapter 24](/streaming/24-recovery-runbook) và [local runtime setup](/setup/local-spark). Runtime Spark 4.0.4, Delta 4.0.1; Docker repo read-only, run outputs dưới .skills-test/spark. Dataset nhỏ, integer USD cents, UTC; không benchmark. Mỗi run có isolated checkpoint và targets.

## Input and reasoning tasks

Lab 24 chạy user aggregate E1 U1=100/E2 U2=50. Diagnostic checkpoint copy bị dùng với grouping user_id,platform; new E3 U1=20 làm actual state-schema failure. Original cp và serving target giữ nguyên. New cp replay retained files vào staging: U1=120/events2, U2=50/events1.

Viết expected business state và retry/recovery contract trước chạy. Chỉ ra source replay assumption, state keys/lifetime, output mode và sink effects. Lab 24 implementation nằm trong labs/streaming/experiments.py::lab24.

## Run

```powershell
python scripts/run_streaming.py --lab 24
python scripts/test_streaming.py test_24
```

All-suite command: `python scripts/test_streaming.py`. Source files publish atomically rồi `processAllAvailable()` drain finite known inputs. Tests không assert exact duration, rate hoặc fixed global batch count; state cleanup có thể tạo no-data batches.

## Expected outcome and evidence

Actual incompatible schema failure; recovered staging U1=120/U2=50; reconciliation passes và original target hash unchanged. Four recovery fact patterns có justified decisions.

Mở run/lab24/result.json: exact sorted target rows/hash, query ID/run ID, recentProgress, input rows, source positions và state metrics nếu query có state. Checkpoint inventory là actual file list, không copy raw state vào site. Rates/durations là measured signals, không fixed threshold assertion. Failed batch có thể chưa được ghi trong completed progress; Lab 23 lưu sink callback attempts và failed checkpoint inventory riêng.

[Streaming evidence](/labs/streaming-evidence) có selected artifact downloads. Snapshot không thay việc chạy tests với code hiện tại.

## PASS / NOT YET

PASS: Chọn strategy từ facts, reproduce incompatibility, prove staging exact state và preserve original serving state. NOT YET nếu chỉ đưa console screenshot hoặc giải thích guarantee vượt source/sink đã test.
