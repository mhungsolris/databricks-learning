---
title: 'Mid Gate · Streaming Correctness'
description: ROAS assessment về state lifetime, checkpoint recovery và end-to-end sink effects.
prev:
  text: 'Lab 24 · Recovery'
  link: /labs/24-recovery-runbook
next:
  text: '25 · Databricks compute'
  link: /platform/25-compute-mental-model
---

# Mid Gate · Streaming Correctness

Prerequisites: Chapters 16-24, labs và [Pipeline Correctness gate](/assessments/mid-gate-pipeline-correctness). Nộp design và executable invariants trước reviewer discussion. Trang này có input và rubric; không chứa solution reveal.

## Case and input

ROAS callback stream cần freshness khoảng 15 phút. Có duplicate callbacks, purchases đến trễ 2 giờ, attribution sửa trong 72 giờ. Query crashes sau một sink write; sau đó checkpoint trở nên unusable. Sink là Delta, downstream Gold mart vẫn phải đúng. Cost API cập nhật daily; retained raw deliveries và authoritative snapshots có retention khác nhau.

Tải [streaming assessment input](/assessment/streaming-input.json). Đây là synthetic case contract, không mô tả guarantee của một API vendor. Input gồm namespace collision, retry, late arrival, newer revision, crash boundary, target/source snapshots và hai replay-availability variants. UTC và integer USD cents; learner phải xác định reporting grain và exact expected states.

## Your design tasks

1. Định nghĩa business identity, delivery identity/version và timestamp owners. Với same event ID ở hai apps và mutable attribution, dedup ở đâu có thể làm mất valid revision?
2. Vẽ source → engine → sink, Bronze/Silver/Gold responsibilities. Phân loại stateless/stateful operations, state keys và lifetime. Chọn stage stream hoặc batch theo source update cadence và SLA, giải thích cost API và Gold reconciliation.
3. Chọn event-time watermark và validate malformed/future timestamps. Tách 2h arrival tolerance khỏi 72h mutation repair. Giải thích provisional freshness, append finalization và idle-source watermark behavior.
4. Chọn checkpoint location/retention/ownership và compatibility policy. State key/type change dùng cp cũ có hợp lệ không? Phân biệt query stop/restart, incomplete batch retry và checkpoint generation mới.
5. Chọn output mode và sink semantics. Trace failure sau Delta write trước engine commit. Đưa actual repeat-attempt target invariants; nếu dùng foreachBatch, chỉ ra nơi enforce batch/event idempotency và app-ID generation.
6. Với checkpoint unusable và retained replay đủ, thiết kế staged recovery và reconciliation. Với retention gap, chọn bounded backfill/full rebuild hoặc missing-truth escalation, bảo vệ unaffected live scope. Không giả định cp reset undo target.
7. Viết tests cho duplicate delivery, namespace collision, late arrival, legitimate 72h correction, same-cp retry, cp-loss replay, incompatible key change và reconciliation mismatch. Tính expected key/version/revenue states từ fixture; lưu actual target, progress, cp inventory và source/config hashes.
8. Giải thích input/processed rates, batch duration, watermark và state metrics nào giúp phân biệt backlog, idle source, state growth và healthy-but-incorrect Gold.

## Submit

Nộp design note, Mermaid hoặc diagram tương đương, code/SQL, table expected/actual invariants, selected evidence manifest và recovery runbook. Ghi assumptions, source cutoff/retention, currency/reporting date, sink atomicity scope và untested boundaries. Câu trả lời tên công nghệ hoặc screenshot query active chưa đủ.

## PASS / NOT YET

| Competence | Causal reasoning required | Critical failure |
|---|---|---|
| Identity / revisions | Collision và retry counterexamples, legitimate newer revision vẫn được nhận | event_id alone hoặc dedup làm mất correction |
| State lifetime | Prior information, keys, cardinality và eligibility boundary được giải thích | State giữ mãi nhưng không có capacity/lifetime decision |
| Event-time policy | Source-driven delay, one-sided guarantees, provisional vs final, 72h repair | Watermark được dùng thay batch cursor/reconciliation |
| Checkpoints | Source progress + commits + state + metadata, compatibility và generation policy | Checkpoint bị coi là business backup hoặc arbitrary schema compatible |
| Sink effect | Trace uncertain commit/retry, stable enforced identity, target exact state | Exactly-once được giải thích bằng physical delivery once |
| Recovery | Replay completeness/cutoff, staged validation, scoped repair và missing-truth branch | Delete cp rồi append và coi là recovery complete |
| Hybrid architecture | Stream/batch decisions từ SLA/cadence/cost và mutation needs | Mọi stage được stream chỉ vì có streaming API |
| Evidence / operability | Actual business invariants và failure attempts, metrics đọc theo symptoms | Chỉ command success, fixed timing assertions hoặc fabricated drop |

PASS cần đủ critical competences và executable counterexamples. NOT YET nếu bất kỳ critical failure chưa được sửa. Reviewer hỏi thêm điều kiện khiến thiết kế thay đổi; một architecture có assumptions khác được chấp nhận khi assumptions và proofs nhất quán.
