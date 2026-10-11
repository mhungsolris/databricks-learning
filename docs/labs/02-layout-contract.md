---
title: 'Lab 02 · Files and schema contracts'
description: Observe schema and business-key failures across active files without accepting partial revenue.
level: Foundation
priority: MUST KNOW
effort: Short
prev:
  text: '02 · Lake, Warehouse, Lakehouse'
  link: /foundations/02-lake-warehouse-lakehouse
next:
  text: '03 · Spark architecture'
  link: /spark/03-architecture-dataframes-sql
---

# Lab 02 · Files and schema contracts

<ChapterMeta>

[Chapter 02](/foundations/02-lake-warehouse-lakehouse), [Lab 00](/labs/00-files-and-tables), Python 3.10+.

</ChapterMeta>

**FREE · Python standard library · No cloud runtime.** Lab 00 quan sát file membership; lab này quan sát schema và business-key contracts trên **nhiều active files**.

## Baseline

```sh
python labs/foundations/layout_contract.py
```

Output: `Contract rows/revenue: (3, 350)`. Fixtures nằm trong `.skills-test/lab-02/`:

| Artifact | Meaning |
|---|---|
| part-1.csv | T1/T2; revenue 300 |
| part-2.csv | T3; revenue 50 |
| snapshot.json | Version 1, hai active filenames |

Contract cần exact columns `transaction_id,revenue`, nonempty/unique transaction IDs và integer values. Integer conversion lỗi thì run cũng fail. Version label trong manifest không tạo transaction guarantee.

## Break the schema

Mở `part-2.csv`, đổi header `revenue` thành `amount`; giữ row T3/50. Trước khi chạy, dự đoán consumer sẽ đọc 350, trả partial 300 hay fail?

```sh
python labs/foundations/layout_contract.py --inspect-only
```

Expected: exit nonzero, `Schema mismatch: part-2.csv`. File vẫn có bytes nhưng không còn consumer-compatible schema. Reader không ignore file và không tự gán missing revenue bằng 0.

## Repair with a policy

Trong fixture này, producer xác nhận rename là accidental và value vẫn dùng cùng money unit. Khôi phục header, chạy inspect và chứng minh `(3, 350)`. Với production rename có chủ ý, cần versioned schema/migration cùng consumer rollout; không sửa source data bằng tay như fixture.

## Break business identity

Đổi T3 thành T1 trong file thứ hai. Schema vẫn hợp lệ nhưng inspect phải fail với `repeated transaction_id`. Một table transaction hợp lệ không tự giải quyết duplicate source events.

Chạy lại baseline generator để restore **ba files của lab**; nó không xóa files bạn thêm. Dùng `--output` riêng để tránh overwrite experiment cần giữ.

```sh
python labs/foundations/layout_contract.py --output .skills-test/lab-02-fresh
python -m unittest discover -s tests -v
```

## PASS / NOT YET

| PASS | NOT YET |
|---|---|
| Phân biệt physical presence, schema và business validity | Chỉ kiểm file exists |
| Reproduce schema/duplicate failure, restore baseline | Accept partial report |
| Nêu owner/policy cần cho semantic rename | Cho rằng đổi column name là đủ |
| Chỉ ra giới hạn model | Gọi JSON manifest là Delta/Iceberg protocol |

Lab không chạy warehouse/lakehouse engines, không chứng minh ACID, concurrent writes, historical retention hoặc multi-engine compatibility. Nó kiểm chứng consumer validation gate mà cả operating models đều cần.
