---
title: Real Spark evidence
description: Actual bounded runtime outputs, plans, stage summaries và Delta commit artifacts.
---

# Real Spark evidence

Các files dưới đây được copy từ **successful actual runs**, không viết lại plan/log bằng tay. [Manifest](/evidence/spark/manifest.json) ghi source run IDs, runtime pin và SHA256. Full Parquet/data/event logs còn ở ignored `.skills-test/spark`; website chỉ giữ selected toy evidence. [Setup](/setup/local-spark) sở hữu reproduction commands và environment limits.

## Runtime and scheduler

- [Runtime metadata](/evidence/spark/spark/runtime.json), [clean shutdown](/evidence/spark/spark/shutdown.json).
- [Completed stages/task counts](/evidence/spark/spark/stages.json).
- [Spark UI HTTP200 và REST stage metrics](/evidence/spark/ui-observation.json), lấy trong live Lab05 run riêng. Stage list có thể chứa SKIPPED; không coi mọi listed stage đã chạy.

CPU quota2 không buộc JVM nhìn2 cores: recorded defaultParallelism8, dù container chỉ được2 CPU quota. Không suy throughput từ count này. `local[*]` chạy driver/execution cùng máy; không đo networking/recovery nhiều nodes.

## Lab artifacts

| Lab | Actual output | Plan/artifact |
|---|---|---|
| 03 | A/VN300, B/US50; zero tagged jobs trước action/after explain | [Result](/evidence/spark/spark/lab03/result.json), [logical/physical plan](/evidence/spark/spark/lab03/pipeline-plan.txt), [jobs/stages](/evidence/spark/spark/lab03/jobs.json) |
| 04 | Count4→6/2/4; conservation120 | [Distribution](/evidence/spark/spark/lab04/result.json), [repartition](/evidence/spark/spark/lab04/repartition6-plan.txt), [coalesce](/evidence/spark/spark/lab04/coalesce2-plan.txt) |
| 05 | Narrow60/noExchange; grouped3/order120/join120 with Exchanges | [Per-query jobs/stages/results](/evidence/spark/query-shuffle/lab05/result.json), [narrow](/evidence/spark/spark/lab05/narrow-plan.txt), [aggregate](/evidence/spark/spark/lab05/aggregate-plan.txt), [order](/evidence/spark/spark/lab05/order-plan.txt), [join](/evidence/spark/spark/lab05/join-plan.txt) |
| 06 | 10000 correct rows; duplicate lookup17000; hot bucket7900 | [Results](/evidence/spark/spark/lab06/result.json), [sort merge](/evidence/spark/spark/lab06/sort-merge-plan.txt), [broadcast](/evidence/spark/spark/lab06/broadcast-plan.txt) |
| 07 | 2 files/120rows, SNAPPY, one row group/file; filter60 | [Footer inventory](/evidence/spark/spark/lab07/result.json), [projection/pushdown](/evidence/spark/spark/lab07/parquet-projection-filter-plan.txt), [storage pruning](/evidence/spark/spark/lab07/storage-partition-filter-plan.txt) |
| 08 | v0 create, v1 append, v2 UPDATE; schema rejected withoutv3 | [Results/snapshots](/evidence/spark/delta/lab08/result.json), [Delta stages](/evidence/spark/delta/stages.json) |

Plan expression IDs/file UUIDs/job numbers có thể đổi; tests kiểm operator families và semantic invariants, không snapshot full strings. Recorded file byte sizes là inventory, không benchmark. Counts không được dùng để hứa latency, spill, speedup hoặc target production partitions.

## Real Delta JSON actions

[v0](/evidence/spark/delta/lab08/delta-table/_delta_log/00000000000000000000.json), [v1](/evidence/spark/delta/lab08/delta-table/_delta_log/00000000000000000001.json), [v2](/evidence/spark/delta/lab08/delta-table/_delta_log/00000000000000000002.json). Đây là commit logs của generated toy table: protocol/schema metadata, add/remove actions và statistics; không chứa whole table rows. Data files không được bundle vào website, nên đây là inspection evidence, không là downloadable complete Delta table.

Local single writer tests không chứng minh concurrent writers, failure recovery, retention/VACUUM hoặc deletion vectors. [Chapter08](/storage/08-delta-fundamentals) phân biệt verified experiment với protocol guarantees từ official references.
