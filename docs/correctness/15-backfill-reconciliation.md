---
title: '15 · Backfill & Reconciliation'
description: Business contracts, deterministic recovery và executable correctness evidence cho ROAS.
level: Core
priority: CRITICAL MUST KNOW
effort: Deep
prev:
  text: '14 · Late data'
  link: /correctness/14-late-lookback-reconciliation
next:
  text: 'Lab 15 · Backfill & Reconciliation'
  link: /labs/15-failed-backfill
---

# 15 · Backfill & Reconciliation

<ChapterMeta>

[14 · Late data](/correctness/14-late-lookback-reconciliation), [11 · Idempotency](/correctness/11-idempotency), [12 · MERGE](/correctness/12-merge-correctness). Tiếp: [Mid Gate — Pipeline Correctness](/assessments/mid-gate-pipeline-correctness).

</ChapterMeta>

## Why this matters

Revenue logic sai 90 ngày. Backfill là intentional historical recomputation/repair; reconciliation là check/proof processed result khớp defined truth. Một job backfill success chưa chứng minh metrics đúng.

## Scenario

Historical Jan 1→Apr 1 exclusive cần rebuild; current 15-minute pipeline tiếp tục ngoài scope. Fail sau day 37 phải resume 53 ngày, chưa expose partial repaired history cho reporting.

## Learner reasoning

Trước publish: input complete chưa, source snapshot/cutoff nào, keys unique không, scope predicate có exact boundaries không, live writers có cùng scope không? Vì sao row count đúng vẫn chưa đủ?

## Mental model

Staging tách partial computation khỏi serving state. Validation kiểm types/identity/scope; reconciliation so keys/content/day metrics; publish là bounded atomic table operation. Nhiều table publishes không tự atomic chung.

```mermaid
flowchart LR
    A["Freeze source and bounded scope"] --> B["Backfill staging"] --> C["Validate contracts"] --> D["Reconcile against truth"] --> E["Publish affected scope only"]
```

## Core concepts

Parameters start inclusive/end exclusive, source snapshot/version, logic version, run ID và completed scope phải explicit. Partition/date isolation cho độc lập worker scopes; limited parallelism theo source quotas/compute. Idempotent resume reuses validated completed units, không tin task success flag thiếu durable output.

## Example data

Lab 15 dùng 90 days, one event/day, revenue expected 10 cents/day. Staging 37 rows trước simulated failure, production unchanged; remaining 53 rows merged sau resume. Historical 900 cents; LIVE ngoài scope 77→88 ở giữa two publishes phải giữ 88.

## How it works

Freeze source input; write isolated staging; identify completed keys từ durable stage; resume; reconcile 90 keys/rows/day distribution/sums/content; only then replace affected scope. Full rerun phải cùng historical hash. Direct production writes expose partial repairs và retry artifacts nếu thiếu controls.

## Databricks implementation

[Delta replaceWhere](https://docs.delta.io/delta-batch/) hỗ trợ predicate-scoped atomic overwrite và validate incoming scope theo default policy. Lab dùng event_time ISO UTC bounds, explicit schema, no auto evolution. MERGE phù hợp sparse changes có stable keys; overwrite phù hợp complete affected scope. [Databricks selective overwrite](https://docs.databricks.com/aws/en/delta/selective-overwrite) còn runtime-specific options, không giả định OSS support mọi option.

## Production failure

Publish partial 37 days overwrite cả 90 ngày làm mất 53 ngày; broad overwrite làm mất live data; resumeappend có thể duplicate; source thay đổi giữa reruns phá frozen expected state. Same-scope live correction sau cutoff có thể bị overwrite dù transaction atomic.

## Debugging

So row count, sums, missing/extra keys, null keys, duplicates, content/revisions, day/platform distribution và ROAS/cost coverage. Lab exact integer cents nên tolerance 0. Nếu external comparator rounding cần tolerance contract theo metric/currency/cutoff; tolerance tổng không cho phép wrong key/content lách qua.

## BigQuery / Airflow mapping

Airflow date-mapped tasks có thể chia bounded scopes; task scheduling không là publish protocol. BigQuery partition overwrite cũng cần complete partition input. dbt full-refresh có thể vượt repair scope; staging/validation/recon cần được thiết kế trước serving replacement.

## Code

Chạy `python scripts/run_correctness.py --lab 15`. Evidence lưu failure 37 state, validation-before-publish, publish history và final rerun. Mô phỏng 37/53 bằng two bounded chunks trên 90 rows, không chạy 90 daily jobs hay benchmark production.

```powershell
python scripts/run_correctness.py --lab 15
```

## Common mistakes

Gọi backfill là reconciliation; dùng row count/sum duy nhất; publish trước validation; infer completion từ memory-only flag; overwrite không có predicate; chạy live/backfill cùng scope không có coordination.

## Production notes

Production cần scope ownership/lease hoặc partition writer coordination, optimistic conflict handling và source retention. [Concurrency docs](https://docs.delta.io/concurrency-control/) mô tả table conflicts; nó không tự quyết định business winner. Lab kiểm sequential interleaving với LIVE outside scope, chưa kiểm simultaneous writers hay process-kill recovery.

## Interview checkpoint

Giải thích start/end, frozen snapshot, completed scope, resume 37→90, verification-before-publish, overwritevsMERGE và cách giữ live updates. Khi sums bằng nhưng key coverage sai, reconciliation có PASS không?

## How to explain this in an interview

“Tôi giới hạn historical scope và freeze source/logic version, tính vào staging, kiểm contracts rồi reconcile với truth trước publish. Resume dựa durable completed units; rerun phải giữ same affected state. Live writers cần scope coordination vì atomic overwrite không tự bảo vệ business updates cùng scope.”

## PASS criteria

PASS khi stage/recon precede publish, rerun giữ historical state và unaffected live row, expected scope đầy đủ. NOT YET nếu repair directly production từng phần hoặc chỉ kiểm job status/count.

## Official references

[OSS batch overwrite](https://docs.delta.io/delta-batch/), [Databricks selective overwrite](https://docs.databricks.com/aws/en/delta/selective-overwrite), [Delta concurrency](https://docs.delta.io/concurrency-control/). Verified 2026-10-11; lab scope predicate được execution-check trên Delta 4.0.1.

