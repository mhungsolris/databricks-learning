---
title: 'Lab 18 · Checkpoints and restart boundaries'
description: Actual local streaming query với deterministic file arrivals và business-state checks.
prev:
  text: 'Chapter 18'
  link: /streaming/18-checkpoints
next:
  text: 'Continue learning'
  link: /streaming/19-windows-watermarks
---

# Lab 18 · Checkpoints and restart boundaries

Cost: **FREE / LOCAL**. Execution scope: **Actual Spark Structured Streaming + Delta**, controlled tiny JSON file source. Controlled query stop/restart where used; no process kill.

## Before you run

Đọc [Chapter 18](/streaming/18-checkpoints) và [local runtime setup](/setup/local-spark). Runtime Spark 4.0.4, Delta 4.0.1; Docker repo read-only, run outputs dưới .skills-test/spark. Dataset nhỏ, integer USD cents, UTC; không benchmark. Mỗi run có isolated checkpoint và targets.

## Input and reasoning tasks

Lab 18 ghi E1/E2 rồi E3, stop với target 3 rows. Same checkpoint không có new input giữ hash; E4 làm target 4. New checkpoint discovery lại retained files làm append target 8 rows. Quan sát này chỉ chứng minh JSON file-source behavior của fixture.

Viết expected business state và retry/recovery contract trước chạy. Chỉ ra source replay assumption, state keys/lifetime, output mode và sink effects. Lab 18 implementation nằm trong labs/streaming/experiments.py::lab18.

## Run

```powershell
python scripts/run_streaming.py --lab 18
python scripts/test_streaming.py test_18
```

All-suite command: `python scripts/test_streaming.py`. Source files publish atomically rồi `processAllAvailable()` drain finite known inputs. Tests không assert exact duration, rate hoặc fixed global batch count; state cleanup có thể tạo no-data batches.

## Expected outcome and evidence

Target counts 3 → 3 → 4 → 8; same-checkpoint hash không đổi trước new input. New query ID khác, retained input bị discovery lại.

Mở run/lab18/result.json: exact sorted target rows/hash, query ID/run ID, recentProgress, input rows, source positions và state metrics nếu query có state. Checkpoint inventory là actual file list, không copy raw state vào site. Rates/durations là measured signals, không fixed threshold assertion. Failed batch có thể chưa được ghi trong completed progress; Lab 23 lưu sink callback attempts và failed checkpoint inventory riêng.

[Streaming evidence](/labs/streaming-evidence) có selected artifact downloads. Snapshot không thay việc chạy tests với code hiện tại.

## PASS / NOT YET

PASS: Đọc checkpoint inventory, so exact target/hash qua restart và bảo vệ compatibility decision bằng source và state schema. NOT YET nếu chỉ đưa console screenshot hoặc giải thích guarantee vượt source/sink đã test.
