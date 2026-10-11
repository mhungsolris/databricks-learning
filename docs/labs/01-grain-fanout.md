---
title: 'Lab 01 · Diagnose fan-out'
description: Reproduce cost duplication, submit your own SQL fix, and test grain and coverage failures.
level: Foundation
priority: MUST KNOW
effort: Medium
prev:
  text: '01 · Grain, Keys & Fan-out'
  link: /foundations/01-grain-keys-fanout
next:
  text: '02 · Lake, Warehouse, Lakehouse'
  link: /foundations/02-lake-warehouse-lakehouse
---

# Lab 01 · Diagnose fan-out

<ChapterMeta>

[Chapter 01](/foundations/01-grain-keys-fanout), Python 3.10+, SQL. Chạy commands tại repository root.

</ChapterMeta>

**FREE · Python standard library + SQLite · Không cloud hoặc package install.**

## Reproduce before fixing

```sh
python labs/foundations/grain_fanout.py
```

Diagnostic chỉ chạy wrong join, không tự sửa. Output:

```text
Source totals: 300 500
Joined rows: [('T1', 100, 500), ('T2', 200, 500)]
Report: [('2026-10-01', 'A', 300, 1000)]
```

Ghi ba grain statements và dự đoán cardinality trước khi đọc đáp án. Vì sao revenue không tăng nhưng cost tăng? Cùng symptoms có thể do duplicate source không? Bằng chứng ở joined rows giúp phân biệt thế nào?

## Submit your fix

Tạo `.skills-test/lab-01/answer.sql`, viết query trả columns **date, campaign, revenue, cost**. Có thể copy `WRONG_SQL` từ source để reproduce, rồi sửa. Không hardcode expected metrics; giữ query hoạt động khi thêm campaign khác.

```sh
python labs/foundations/grain_fanout.py --query-file .skills-test/lab-01/answer.sql
```

Wrong query phải exit nonzero với `Report contract failed`. Fix đúng cho fixture có output:

```text
PASS submitted query: [('2026-10-01', 'A', 300, 500)]
```

Checker so toàn report ở fixture hiện tại, không chứng minh mọi input. Để kiểm tra tính tổng quát, thử thêm campaign B có revenue 50 và cost 500 trong `fixture()` trên một bản copy của source. Output phải có hai rows và tổng cost 1000. Một query dùng SUM(DISTINCT cost) trên toàn report sẽ mất cost hợp lệ.

<details>
<summary>Solution sau khi bạn đã submit một lần</summary>

Aggregate transactions về date/campaign, rồi join spend unique trên cùng keys. Query tham chiếu là `FIXED_SQL` trong `labs/foundations/grain_fanout.py`.

```sh
python labs/foundations/grain_fanout.py --mode solution
```

Vì fixture có đầy đủ coverage, inner join hợp lệ. Với missing spend, solution cố ý fail; nó không tự coi missing cost là 0.

</details>

## Failure drills

| Inject vào fixture trên bản copy | Kết quả cần đạt | Điều đang kiểm tra |
|---|---|---|
| Thêm spend A cùng date | `Duplicate grain key` | Aggregate revenue chưa đủ nếu spend không unique |
| Thêm transaction B, không có spend B | `Missing spend coverage` | Không accept silent inner-join loss |
| Transaction có null ID | `Null key` | Business identity contract |
| Thêm creative/country/platform spend detail | 2 × 3 pairs nếu join quá thô | Align reporting grain, không phân bổ revenue tùy ý |

Tests tự tạo connections riêng nên không sửa data production:

```sh
python -m unittest discover -s tests -v
```

## PASS / NOT YET

| PASS | NOT YET |
|---|---|
| Tự giải thích cost duplication bằng joined rows | Chỉ nhớ 300/500 |
| Submit query và giải thích aggregate placement | Nhập hardcoded metrics |
| Giữ hai costs bằng nhau của hai campaigns | Coi equal values là duplicate business facts |
| Reject missing coverage/duplicate/null keys | Chỉ sửa output để test baseline xanh |

SQLite dùng để kiểm chứng relational semantics trên tiny data. Lab không đo Spark plan, distributed cost hay Databricks constraints.
