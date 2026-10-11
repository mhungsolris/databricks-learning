---
title: 'Lab 08 · Delta log & snapshots'
description: Create/append/UPDATE/time travel thật, inspect commits và reject incompatible schema.
prev:
  text: '08 · Delta fundamentals'
  link: /storage/08-delta-fundamentals
next:
  text: '09 · Medallion Architecture'
  link: /architecture/09-medallion
---

# Lab 08 · Delta log & snapshots

**FREE · validated OSS Delta4.0.1 + Spark4.0.4.** [Chapter 08](/storage/08-delta-fundamentals), [setup](/setup/local-spark). Code `labs/spark/experiments.py::delta`. Maven official network required first run; cache stays in ignored evidence.

```powershell
python scripts/run_spark.py --lab 08
python scripts/test_spark.py --delta
```

## Predict versions

| Action | Expected committed version | Rows |
|---|---:|---|
| Create | 0 | (1,100),(2,200) |
| Append | 1 | Thêm (3,300) |
| UPDATE id1 | 2 | (1,150),(2,200),(3,300) |
| Read version0 | Không write | (1,100),(2,200) |
| Append incompatible revenue STRING | Không version3 | Schema rejected; v2 vẫn active |

## Inspect the real transaction log

Trong `delta-table/_delta_log`, đọc JSON000…00,01,02; mỗi line một action. v0 có protocol/metaData/commitInfo/add; v1 thêm file append; v2 remove original file/add replacement. `result.json` reconstruct active file names sau từng commit. [Selected real JSON logs](/labs/runtime-evidence) có generated file names thực tế; không giả lập.

Đối chiếu snapshot với rows qua Delta reader và `DESCRIBE HISTORY`. Không mở raw Parquet glob làm “current table”. Removed file có thể còn physical disk; không delete nó, không VACUUM ở lab. Concept A+B→B+C trong chapter là simplified walkthrough, còn lab có3 commits vì append riêng.

## Failure contract

STRING revenue append phải fail, successful version count vẫn3. Không chỉ kiểm exception: kiểm `_delta_log` không có new version. Current table vẫn đọc đúng. Rerun command tạo folder mới; nó không kiểm business replay idempotency trên cùng target. MERGE/dedup implementation không thuộc Iteration3.

## PASS / NOT YET

PASS: reconstruct active files, explain committed version/current vs history và schema rejection. NOT YET: coi log chứa rows hoặc atomic append tự dedup. Single writer local test chưa chứng minh concurrent writes, cloud storage protocol hoặc retention behavior.
