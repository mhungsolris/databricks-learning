---
title: 'Lab 03 · Pipeline and deferred execution'
description: Validate a relational pipeline locally and distinguish its measured output from Spark scheduler reasoning.
level: Core
priority: MUST KNOW
effort: Medium
prev:
  text: '03 · Spark architecture'
  link: /spark/03-architecture-dataframes-sql
next:
  text: '04 · Partitioning'
  link: /spark/04-partitioning
---

# Lab 03 · Pipeline and deferred execution

<ChapterMeta>

[Chapter 03](/spark/03-architecture-dataframes-sql), Python 3.10+. Grain/key reasoning từ [Chapter 01](/foundations/01-grain-keys-fanout).

</ChapterMeta>

**FREE · hai variants.** Portable SQLite + Python standard library giữ conceptual exercise. Real Spark variant chạy bằng [pinned Docker runtime](/setup/local-spark), không cần native host JDK/PySpark. Counter của model và Spark scheduler evidence được đọc riêng.

## Predict the pipeline

Pipeline: read transactions → filter paid → join unique campaigns → aggregate campaign/country → write CSV. Dùng data trong Chapter 03, dự đoán:

| Boundary | Viết dự đoán trước run |
|---|---|
| Filter paid | Rows và total revenue |
| Join | Lookup key có unique? Match count đổi thế nào? |
| Aggregate | A/VN và B/US revenue |
| Preview rồi write | Model thực thi query mấy lần? |

## Run and inspect

```sh
python labs/spark/pipeline_model.py
```

Expected output phần ổn định:

```text
Before action, model executions: 0
Preview: [('A', 'VN', 300), ('B', 'US', 50)]
Written: [('A', 'VN', 300), ('B', 'US', 50)]
After preview + write, model executions: 2
```

Mở `.skills-test/lab-03/report.csv`: hai rows, tổng revenue 350; cancelled event 900 không có trong report. SQLite plan text có thể khác theo bundled SQLite version nên tests không snapshot nguyên text.

| Measured ở lab | Chỉ là Spark reasoning dựa nguồn |
|---|---|
| SQL metrics và CSV output | Physical join strategy và shuffle |
| Counter tăng khi model collect/write | Số Spark jobs/stages/tasks |
| SQLite EXPLAIN QUERY PLAN | Spark formatted physical plan |
| Repeat query khi preview + write | Actual cache/AQE/recovery behavior |

Counter 2 chỉ có nghĩa model gọi SQL hai lần. Không dùng nó để khẳng định Spark luôn tạo đúng hai jobs. Model không có executors, partitions hoặc distributed scheduling.

## Failure drill

Trong một bản copy của `fixture()`, thêm campaign lookup `('A','VN')`. Pipeline vẫn chạy nhưng A/VN thành 600, B/US vẫn 50. Tìm uniqueness gate cần đặt trước join. Không sửa bằng tăng compute hoặc DISTINCT trên metrics.

```sh
python -m unittest discover -s tests -v
```

Test cố ý chứng minh engine vẫn có thể trả report sai khi contract sai. Từ đây liên hệ kiểm tra grain và assertions trước write vào production Spark pipeline.

## Spark transfer exercise

Đánh dấu transformations và actions trong snippet ở [Chapter 03 code](/spark/03-architecture-dataframes-sql#code). Vẽ driver/executor boundary. Nêu một possible stage boundary cho aggregate; giải thích vì sao chưa biết exact counts.

## Real Spark variant

```powershell
python scripts/verify_spark.py
python scripts/run_spark.py --lab 03
```

Code `labs/spark/experiments.py::pipeline` tạo đúng transactions/campaigns của Chapter 03, filter paid, join lookup, aggregate; capture `explain(mode='extended')`, collect, SQL equivalent và write/read Parquet report. Expected A/VN300, B/US50; cancelled900 bị loại.

Trong folder run, `pipeline-plan.txt` có parsed/analyzed/optimized logical plans và physical plan. `result.json` ghi zero jobs trong tagged group trước action và sau explain trên fixture createDataFrame này; collect có actual jobs. `jobs.json` và event logs ghi scheduler stages, `shutdown.json` xác nhận stop. [Selected actual artifacts](/labs/runtime-evidence). Metadata/schema work của sources khác có thể tạo jobs; không generalize zero jobs cho mọi read.

Đối chiếu source code với optimized plan: join/aggregate Exchange, action mới cần result; write cũng materialize query riêng. Không giả định action luôn một job, không dùng model counter2 làm Spark counts. Lab không cache query và không benchmark.

## PASS / NOT YET

| PASS | NOT YET |
|---|---|
| Explain output/CSV và filter/join/aggregate boundaries | Chỉ chạy command xanh |
| Identify repeated execution trong model và source actions trong Spark | Đồng nhất counter với scheduler |
| Reproduce duplicate lookup failure và đề xuất validation | Gọi metric failure là thiếu executors |
| Nêu evidence thiếu cho distributed behavior | Báo đã chạy Spark dù chỉ dùng SQLite |

Học tiếp [04 · Partitioning](/spark/04-partitioning), [05 · Shuffle](/spark/05-shuffle), [06 · Joins](/spark/06-joins-broadcast-skew) để đọc distribution requirements của actual plans.
