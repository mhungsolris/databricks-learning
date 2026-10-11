---
title: 'Mid Gate — Pipeline Correctness'
description: Assessment độc lập về keys, replay, source boundaries, late attribution và bounded backfill.
prev:
  text: 'Lab 15 · Failed backfill'
  link: /labs/15-failed-backfill
next:
  text: '16 · Structured Streaming'
  link: /streaming/16-structured-streaming
---

# Mid Gate — Pipeline Correctness

Prerequisites: Chapters 09–15 và their labs. Làm assessment trước khi đọc reviewer material. Trang này chỉ cung cấp input, questions và competence rubric; không có solution reveal.

## Case and input

Bạn thiết kế near-real-time ROAS với Adjust callbacks/files và Google Ads, Meta, TikTok, Unity daily cost. Freshness khoảng 15 phút; source state có thể sửa 72h history. Các con số là synthetic requirements.

Tải [assessment input](/assessment/pipeline-input.json). Input có duplicate deliveries, event ID reused across apps, late mutable revisions, missing campaign, daily cost và API retry/failure descriptions. Contract trong fixture là guarantees được cấp cho case; hãy chỉ ra thiết kế sẽ đổi thế nào nếu mất guarantee đó.

## Your design tasks

1. Ghi table responsibilities, grain và full business keys cho raw, latest event states, cost và Gold. Chứng minh join cardinality trước tính ROAS; xử lý missing campaign/cost coverage.
2. Chọn incremental boundary. Giải thích timestamp ties, retry pages, late arrival, late mutation, deletes và partial responses. Đặt cursor commit ở đâu? Failure sau write/trước cursor dẫn đến gì?
3. Định nghĩa source dedup/conflict/version rules rồi viết MERGE skeleton. Trace exact state qua revisions, replay và stale update. So two apps cùng event_id; giải thích vì sao GROUP BY event_id chưa đủ.
4. Đưa fast retrieval/lookback và scheduled reconciliation policy cho 72h mutable history. So API cost, latency, correctness và residual gaps; phân biệt batch cursor, lookback, reconciliation và streaming watermark.
5. Chọn timestamps cho reporting, retrieval và lag monitoring. Trace midnight purchase nhận hôm sau; đồng nhất callback/file comparison scope, currency và cutoff.
6. Thiết kế 90-day backfill start/end, frozen input, staging, completed-scope evidence, failure day 37, resume, reconcile và bounded publish. Current pipeline tiếp tục thế nào? Giải quyết same-scope writers ra sao?
7. Viết executable tests cho replay, duplicate/conflict, mutable/stale/newer states, grain conservation, mismatched keys/day metrics và backfill rerun. Lưu expected state bạn tự tính cùng actual state, Delta history và source/logic version.

## Submit

Nộp một design note, SQL/code, invariant table có expected/actual kết quả, evidence manifest và failure runbook. Nêu assumptions riêng của source, constraints chưa test và điều kiện cần mở repair scope. Không chỉ nộp command-success logs.

## PASS / NOT YET

| Competence | PASS reasoning required |
|---|---|
| Identity and grain | Full keys được bảo vệ bằng concrete collision/fan-out counterexamples |
| Retrieval and recovery | Source guarantees, cursor commit và replay final state được giải thích |
| MERGE semantics | Source conflict policy, unique states và deterministic replacement có tests |
| Time and late data | Report date đúng, policies theo source behavior, watermark không thay retrieval |
| Backfill | Staging/recon trước publish, durable resume và unaffected scope được chứng minh |
| Evidence | Key/content/metrics mismatches bị phát hiện dù count hoặc sums bằng nhau |

NOT YET nếu thiếu bất kỳ critical competence hoặc chỉ trả lời tên công nghệ. Reviewer chấm causal reasoning và executable invariants; có thể yêu cầu thêm counterexample. Chưa vượt gate thì quay lại chapter liên quan và sửa failure case.
