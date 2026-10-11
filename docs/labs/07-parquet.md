---
title: 'Lab 07 · Parquet'
description: Write/read thật, inspect footer, codec, projection và hai loại filters.
prev:
  text: '07 · Parquet'
  link: /storage/07-parquet
next:
  text: '08 · Delta'
  link: /storage/08-delta-fundamentals
---

# Lab 07 · Parquet

**FREE · real Spark, no extra Python dependency.** [Chapter 07](/storage/07-parquet), [runtime](/setup/local-spark). Code `labs/spark/experiments.py::parquet`.

```powershell
python scripts/run_spark.py --lab 07
```

## Predict and inspect files

120 ids, two dates, campaign/revenue/payload columns. Write coalesce2 → inspect two `*.parquet` files (exclude `_SUCCESS`/CRC markers). Verify `PAR1` magic at both ends, footer length, actual row-group count/row count/codec via bundled Parquet JVM reader. Recorded each file1 row group/60 rows, SNAPPY. [Inventory](/labs/runtime-evidence).

## Projection and predicate

Read date01, select campaign/revenue →60 rows. `parquet-projection-filter-plan.txt`:

- `ReadSchema` có campaign/revenue/date, bỏ id/payload.
- `PushedFilters` có equality date01; residual filter giữ correct rows.

Vì sao date vẫn đọc dù không SELECT? Vì sao PushedFilters không prove số bytes saved? Compare CSV/JSON **conceptually** về layout/schema/parser, không timing tiny files.

## Storage partition pruning

Write `partitionBy('date')` sang folder mới → hai date directories. `storage-partition-filter-plan.txt` có `PartitionFilters`; selected rows vẫn60. Tách directory pruning khỏi predicate pushdown trong unpartitioned files. Không đồng nhất directory count với task/row-group count.

## Failure exercise

Imagine update ba files chết sau hai. Footer hợp lệ từng file có cung cấp table commit không? Nêu missing UPDATE/DELETE/MERGE/snapshot/concurrent-write layer, rồi đi [Chapter 08](/storage/08-delta-fundamentals). Integration test đọc empty Parquet với explicit schema để bảo đảm no-match results không bị coi lỗi.

## PASS / NOT YET

PASS: kiểm file/footer, read schema và filters; explain missing table semantics. NOT YET: gọi Parquet một transactional table hoặc coi60 rows nghĩa là half bytes read. Không speed/compression ratio claims từ fixture.
