---
title: 'Lab 00 · Files ≠ Table'
description: Chạy local để quan sát directory scan đọc trùng dữ liệu lịch sử còn table snapshot giữ đúng aggregate.
level: Foundation
priority: MUST KNOW
effort: Short
prev:
  text: '00 · Databricks & Lakehouse'
  link: /foundations/00-mental-model
next:
  text: '01 · Grain, Keys & Fan-out'
  link: /foundations/01-grain-keys-fanout
---

# Lab 00 · Files ≠ Table

<ChapterMeta>

[Chapter 00](/foundations/00-mental-model). Python 3.10+ và một local checkout của repository.

</ChapterMeta>

**FREE · Local only · Không cần package, cloud account hoặc token.**

## Predict before running

Một file cũ chứa e1/e2 (revenue 300). Một file mới chứa e1/e2/e3 (revenue 350). File cũ được giữ cho lịch sử; metadata hiện tại chỉ chọn file mới. Viết hai dự đoán: tổng khi đọc tất cả CSV, và tổng khi theo metadata.

Lab dùng **CSV + JSON manifest** để quan sát membership. Nó không chạy Spark/Parquet/Delta, không kiểm thử ACID, concurrency hoặc production protocol.

## Run

Chạy tại repository root:

```sh
python labs/foundations/files_and_tables.py
python -m unittest discover -s tests -v
```

Trên Windows dùng `python`; nếu Python của máy bạn có tên `python3`, thay command tương ứng. Output mẫu được ghi vào `.skills-test/lab-00/`, một directory ignored bởi Git.

```text
Glob revenue: 650
Snapshot revenue: 350
PASS: active-file membership prevents reading retained historical data twice.
Model only: CSV + JSON manifest; not Delta, Parquet, ACID or concurrency simulation.
```

## Inspect the files

| File | Quan sát | Vai trò |
|---|---|---|
| `.skills-test/lab-00/old.csv` | e1/e2, revenue 300 | Physical history vẫn tồn tại |
| `.skills-test/lab-00/current.csv` | e1/e2/e3, revenue 350 | Active data trong mô hình |
| `.skills-test/lab-00/snapshot.json` | `active_files: ["current.csv"]` | Membership của snapshot mô phỏng |

`read_revenue()` chỉ cộng các rows trong paths được đưa vào. Sự khác biệt ở **cách chọn paths**, không phải phép SUM. Đọc source tại `labs/foundations/files_and_tables.py` và giải thích dòng chọn `active_files`.

## Failure injection

| Thay đổi thủ công trong lab directory | Dự đoán | Kiểm tra |
|---|---|---|
| Copy old.csv thành retained-copy.csv | Glob tăng lên 950; snapshot vẫn 350 | Dùng `--inspect-only` |
| Sửa manifest trỏ tới absent.csv | Phải báo lỗi, không trả partial total | Dùng `--inspect-only` |
| Sửa manifest chọn cả old.csv và current.csv | Metadata sai làm snapshot thành 650 | Metadata cũng cần correctness contract |

```sh
python labs/foundations/files_and_tables.py --inspect-only
```

Chạy lại command baseline sẽ ghi lại **ba fixture files của lab**; các files bạn copy thêm không tự bị xóa. Dùng output directory riêng cho baseline sạch, ví dụ `--output .skills-test/lab-00-fresh`. Không chạy fixture generator vào directory chứa dữ liệu thật.

## PASS / NOT YET

| PASS | NOT YET |
|---|---|
| Giải thích vì sao 650 sai và 350 đúng cho input này | Chỉ nhớ kết quả số |
| Nêu được hai boundaries: metadata membership và business key | Cho rằng metadata tự deduplicate mọi event |
| Missing active file tạo lỗi rõ | Chấp nhận partial aggregate như output thành công |
| Chỉ rõ những gì lab không kiểm chứng | Gọi CSV manifest là Delta transaction log |

**Production bridge:** table-aware engines áp dụng provider metadata thay cho fixture manifest. Không sửa hoặc xóa metadata/files của Delta/Iceberg bằng cách thao tác giống lab. Xem [official references của Chapter 00](/foundations/00-mental-model#official-references).
