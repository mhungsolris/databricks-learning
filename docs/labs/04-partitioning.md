---
title: 'Lab 04 · Partitioning'
description: Predict và đo execution partition counts, plans và conservation invariants.
prev:
  text: '04 · Partitioning'
  link: /spark/04-partitioning
next:
  text: '05 · Shuffle'
  link: /spark/05-shuffle
---

# Lab 04 · Partitioning

**FREE · real Spark local[*].** Prerequisites: [Chapter 04](/spark/04-partitioning), [runtime setup](/setup/local-spark). Source: `labs/spark/experiments.py::partitioning`.

## Predict before run

120 ids, input 4 partitions. Ghi dự đoán cho repartition6, coalesce2, coalesce8: count bao nhiêu, có Exchange không, ids có thay đổi không? Dataset 100 GB/2 partitions có vấn đề giống tiny fixture ở điểm nào, khác ở điểm nào?

```powershell
python scripts/run_spark.py --lab 04
```

## Inspect actual evidence

Trong `.skills-test/spark/labs-04/<run-id>/lab04` đọc `result.json` và bốn `*-plan.txt`. Observed count **4→6/2/4**, rows **120** ở mọi variant. Repartition plan có Exchange; Coalesce2 không Exchange. [Recorded artifacts](/labs/runtime-evidence).

Phân bố rows chỉ liệt kê nonempty partitions. `rdd.getNumPartitions` đo count đầy đủ; `spark_partition_id` được capture trước aggregation. Phép đo grouping tự tạo additional work, không coi mọi stages là stages của transformation đang so sánh.

## Change one assumption

Đổi input thành 7 rows, repartition11: có thể có empty partitions dù count11. Integration test kiểm ids không mất/duplicate. Đổi sang hash repartition một constant key: count nhiều không bảo đảm balance. Không đổi scale lên 100 GB trên laptop.

## PASS / NOT YET

PASS: giải thích count/operator, conservation và trade-offs; tách execution partitions khỏi `partitionBy(date)` của [Lab 07](/labs/07-parquet). NOT YET: nói coalesce luôn nhanh hơn hoặc 6 partitions luôn có cùng bytes. Không có speed comparison trong lab.
