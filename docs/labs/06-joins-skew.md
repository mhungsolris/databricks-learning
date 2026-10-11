---
title: 'Lab 06 · Joins & skew'
description: Kiểm join strategy, output correctness, UNKNOWN distribution và duplicate/null semantics.
prev:
  text: '06 · Joins & skew'
  link: /spark/06-joins-broadcast-skew
next:
  text: '07 · Parquet'
  link: /storage/07-parquet
---

# Lab 06 · Joins & skew

**FREE · 10.000 synthetic fact rows, 101 dimension rows.** Prerequisites: [Chapter 06](/spark/06-joins-broadcast-skew), [Chapter 01](/foundations/01-grain-keys-fanout), [runtime](/setup/local-spark). Code `labs/spark/experiments.py::joins`.

```powershell
python scripts/run_spark.py --lab 06
```

## Part A ,  Strategy without changing meaning

Fact grain một id; dimension grain một campaign. Predict count/sum rồi đọc `sort-merge-plan.txt` và `broadcast-plan.txt`. Normal path force no auto broadcast để thấy SortMergeJoin; explicit broadcast path thấy BroadcastHashJoin/BroadcastExchange, không fact hash Exchange. Cả hai **10.000 rows**, `SUM(id)=49.995.000`. Broadcast vẫn có lookup distribution cost; không phải zero network work.

## Part B ,  Hot key

7.000 UNKNOWN,3.000 normal. Hash repartition4 đưa UNKNOWN vào một bucket. Recorded rows **7.900/630/810/660**; UNKNOWN chỉ ở partition0. [Evidence](/labs/runtime-evidence). Partition IDs/distribution của run khác không là stable public contract; key colocation và conservation là invariant.

Evidence cho unequal work, chưa prove straggler latency hoặc spill. Đề xuất hai mitigations với semantics: fix key, split, pre-aggregate, broadcast, salting hoặc AQE; nêu vì sao tăng bucket count chưa chia UNKNOWN.

## Part C ,  Break the logical contract

Thêm duplicate UNKNOWN lookup: predict `7.000*2 + 3.000 = 17.000` rows; Spark assertion kiểm actual output. Tuning không chữa duplicate grain. NULL fixture equality→1, null-safe equality→2; không coi UNKNOWN bằng NULL. Integration test thêm many-to-many2×3→6 và sum90 để ngăn reasoning chỉ đúng unique lookup.

## PASS / NOT YET

PASS: phân biệt physical choice và logical correctness, xác nhận hot distribution và chọn mitigation có trade-off. NOT YET: broadcast mọi dimension hoặc salt không mô tả match/reaggregation contract. Không benchmark “broadcast nhanh hơn” trong lab này.
