---
title: 'Lab 05 · Shuffle'
description: Observe Exchange và scheduler stages ở narrow, groupBy, orderBy và join.
prev:
  text: '05 · Shuffle'
  link: /spark/05-shuffle
next:
  text: '06 · Joins & skew'
  link: /spark/06-joins-broadcast-skew
---

# Lab 05 · Shuffle

**FREE · real Spark local[*].** [Chapter 05](/spark/05-shuffle), [runtime setup](/setup/local-spark). Source `labs/spark/experiments.py::shuffle`.

## Predict

120 ids, key=id%3. Filter id≥60/select; groupBy key count; global orderBy; join unique3-key lookup. Dự đoán row count và distribution requirement trước nhìn explain. Lab disable auto broadcast và AQE có chủ đích; không là production recommendation.

```powershell
python scripts/run_spark.py --lab 05
```

## Read plans and execution

`narrow-plan.txt`: no Exchange, 60 rows. `aggregate-plan.txt`: hash Exchange, 3 groups count40. `order-plan.txt`: range Exchange + Sort,120 rows. `join-plan.txt`: sort merge + Exchanges,120 rows. [Actual files](/labs/runtime-evidence).

`jobs.json` có actual job/stage IDs; parent `stages.json` gồm completed stages/task counts từ event logs. Job/stage numbers thay đổi theo implementation/config, tests không snapshot exact counts. Query results được collect có bound120; `count()` có thể bỏ sort, nên không dùng nó để prove orderBy execution.

Recorded per-query run: narrow1 job/1 stage ID; aggregate1/2; order2/3; join1/3. Range sampling giải thích additional job của order trong run này. `result.json` map IDs theo từng query; đối chiếu completed event log thay vì coi mọi reserved/reused stage là new execution. Đây là observations, không là guaranteed counts.

## Optional UI workflow

```powershell
python scripts/run_spark.py --lab 05 --ui --hold-seconds 120
```

Mở loopback4040 → SQL, xem executed operator graph; Jobs/Stages, map IDs tới `jobs.json`, so task counts và shuffle read/write. Không suy một operator=một stage. Sau shutdown UI đóng; event log vẫn ở ignored run folder. [Setup/troubleshooting](/setup/local-spark).

## Reason about the difference

Vì sao final campaign count cần kết hợp contributions? Partial aggregates giảm gì? Nếu input đã partition phù hợp, plan có thể đổi không? Local run ghi scheduler evidence nhưng chưa đo multi-node network, spill hoặc latency benefit.

## PASS / NOT YET

PASS: chỉ đúng Exchange types, giải thích colocation/serialization/state và tìm completed stage evidence. NOT YET: nói mọi join shuffle cả hai hoặc dùng tiny runtime làm performance ranking.
