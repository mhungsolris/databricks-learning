# Learning path

Dependency order là nền tảng của track: xác định dữ liệu đại diện cho gì, hiểu compute thực thi ra sao, rồi thiết kế correctness trước khi chọn dịch vụ platform. Chapters 00-60 có nội dung, gồm Iceberg và architecture judgment; full capstone vẫn là bước kế tiếp. [Spark local setup](/setup/local-spark) là prerequisite cho engine labs. Các gates đánh giá correctness và platform design, với workspace evidence ghi riêng.

## Foundations {#foundations}

| Chương | Level / Priority | Effort | Prerequisites | PASS đầu ra |
|---|---|---|---|---|
| 00 · Databricks & Lakehouse Mental Model | Foundation / MUST KNOW | Medium | Python, SQL; BigQuery/Airflow experience | Đặt đúng storage, files, table, compute, governance; nêu giới hạn mô hình |
| [01 · Grain, keys & fan-out](/foundations/01-grain-keys-fanout) | Foundation / MUST KNOW | Deep | 00 | Tính được số liệu sai khi join khác grain và sửa bằng aggregate đúng |
| [02 · Lake / Warehouse / Lakehouse & BigQuery bridge](/foundations/02-lake-warehouse-lakehouse) | Foundation / MUST KNOW | Deep | 00-01 | So sánh theo workload và trách nhiệm vận hành |

## Data Architecture {#architecture}

| Chương/chủ đề | Level / Priority | Effort | Prerequisites | PASS đầu ra |
|---|---|---|---|---|
| Fact, dimension & grain contracts | Core / MUST KNOW | Medium | 01 | Định nghĩa business key, grain và cardinality của join |
| [09 · Medallion](/architecture/09-medallion) | Core / MUST KNOW | Deep | 01, 08 | Đặt responsibilities/quality boundaries; giữ revenue/cost theo đúng grain |

Grain/fan-out được đưa lên Foundation trước Spark. Medallion học kỹ sau Delta vì lớp kiến trúc cần dựa trên table semantics, không chỉ thư mục mang tên Bronze/Silver/Gold.

## Spark {#spark}

| Chương/chủ đề | Level / Priority | Effort | Prerequisites | PASS đầu ra |
|---|---|---|---|---|
| [03 · Architecture & DataFrames / Spark SQL](/spark/03-architecture-dataframes-sql) | Core / MUST KNOW | Deep | 00-02 | Phân biệt driver/executor, transformation/action và đọc plan đơn giản |
| [04 · Partitioning](/spark/04-partitioning) | Core / MUST KNOW | Deep | 03 | Đọc partition count, phân biệt execution/storage và trade-offs |
| [05 · Shuffle](/spark/05-shuffle) | Core / MUST KNOW | Deep | 04 | Giải thích key colocation, Exchange và memory/disk consequences |
| [06 · Joins, broadcast & skew](/spark/06-joins-broadcast-skew) | Core / MUST KNOW | Deep | 05, 01 | Tách cardinality correctness khỏi strategy, đo hot key distribution |

## Storage & Table Formats {#storage}

| Chương/chủ đề | Level / Priority | Effort | Prerequisites | PASS đầu ra |
|---|---|---|---|---|
| [07 · Parquet & file layout](/storage/07-parquet) | Core / MUST KNOW | Deep | 06, 02 | Inspect footer/pruning; nêu missing table transactions |
| [08 · Delta Lake fundamentals](/storage/08-delta-fundamentals) | Core / MUST KNOW | Deep | 07, 02 | Read actual commits, reconstruct snapshots và time travel |
| [12 · MERGE correctness](/correctness/12-merge-correctness) | Core / CRITICAL MUST KNOW | Deep | 01, 08, 11 | Match full key, resolve source ambiguity, kiểm exact mutable/replay states |

## Ingestion {#ingestion}

| Chương/chủ đề | Level / Priority | Effort | Prerequisites | PASS đầu ra |
|---|---|---|---|---|
| [10 · Incremental boundaries](/ingestion/10-incremental-boundaries) | Core / MUST KNOW | Deep | 09, 08 | So source boundary guarantees, ties/deletes và cursor commit/replay |
| Auto Loader | Core / SHOULD KNOW | Medium | Incremental, streaming basics | Phân biệt file discovery với business deduplication |

## Correctness {#correctness}

| Chương/chủ đề | Level / Priority | Effort | Prerequisites | PASS đầu ra |
|---|---|---|---|---|
| [11 · Idempotency](/correctness/11-idempotency) | Core / CRITICAL MUST KNOW | Deep | 08, 10 | Identity trước dedup; batch/D-1 replay và retry không tăng revenue |
| [13 · Time semantics](/correctness/13-time-semantics) | Core / MUST KNOW | Deep | 10, 12 | Tách event/arrival/processing/update time theo mục đích |
| [14 · Late data/lookback/reconciliation](/correctness/14-late-lookback-reconciliation) | Core / CRITICAL MUST KNOW | Deep | 10, 13, 12 | Source-driven detection, final E1=120 và mismatch checks |
| [15 · Backfill/reconciliation](/correctness/15-backfill-reconciliation) | Core / CRITICAL MUST KNOW | Deep | 14, 11, 12 | Stage/reconcile trước bounded publish, resume/rerun giữ affected state |

Watermark học sau event time và state trong nhóm Streaming; lookback của batch không được coi là cùng một cơ chế với watermark.

Dependency chains: 01→09; 08→11→12 và01→12; 10→13→14→15. Linear reading order09–15 bổ sung context, không thay các prerequisite trên. Sau Lab15, làm Mid Gate với dataset riêng và reasoning/executable invariants; solution reviewer không được publish trên site.

## Streaming {#streaming}

| Chương/chủ đề | Level / Priority | Effort | Prerequisites | PASS đầu ra |
|---|---|---|---|---|
| [16 · Structured Streaming mental model](/streaming/16-structured-streaming) | Core / MUST KNOW | Deep | 03, 11, 13 | Chỉ ra source/transform/sink, đọc positive-input batch IDs và rates, giải thích một query active qua nhiều batches rồi clean stop. |
| [17 · Stateless vs stateful streaming](/streaming/17-stateless-stateful) | Core / CRITICAL MUST KNOW | Deep | 16 | Phân loại operations, chứng minh aggregate sau restart và chỉ ra unbounded state-growth mechanism. |
| [18 · Checkpoints and restart boundaries](/streaming/18-checkpoints) | Core / CRITICAL MUST KNOW | Deep | 17, 11 | Đọc checkpoint inventory, so exact target/hash qua restart và bảo vệ compatibility decision bằng source và state schema. |
| [19 · Event-time windows and watermarks](/streaming/19-windows-watermarks) | Core / CRITICAL MUST KNOW | Deep | 13, 14, 17, 18 | Tách bốn mechanisms, giải thích one-sided guarantee và chứng minh actual drop/state eviction bằng metrics. |
| [20 · Streaming deduplication](/streaming/20-streaming-dedup) | Core / MUST KNOW | Deep | 11, 18, 19 | Giải thích cả within-horizon suppression, old-time late drop và refreshed-time repeat effect, cùng legitimate mutation path. |
| [21 · Stream-stream joins and state lifetime](/streaming/21-stream-stream-joins) | Core / SHOULD KNOW | Deep | 06, 19 | Chứng minh initial match, delayed match, controlled unmatched NULL và state removals; giải thích idle-input limitation. |
| [22 · Output modes and sink semantics](/streaming/22-output-modes-sinks) | Core / MUST KNOW | Deep | 17, 19, 21 | Đọc actual emissions cho ba modes và chọn sink contract bảo toàn aggregate qua retry. |
| [23 · Delivery semantics across source, engine and sink](/streaming/23-delivery-semantics) | Core / CRITICAL MUST KNOW | Deep | 11, 12, 18, 22 | Chứng minh durable sink write trước failure, same batch retried, target unsafe/safe khác nhau và nêu guarantee boundaries. |
| [24 · Recovery and checkpoint failure](/streaming/24-recovery-runbook) | Core / MUST KNOW | Deep | 15, 18, 23 | Chọn strategy từ facts, reproduce incompatibility, prove staging exact state và preserve original serving state. |

Sau Lab24: [Mid Gate · Streaming Correctness](/assessments/mid-gate-streaming-correctness). Dependency: state → checkpoint → event-time bounds → dedup/join/output → sink effects → recovery. Hybrid batch/stream architecture là hợp lệ.

## Databricks Platform {#platform}

| Chương/chủ đề | Level / Priority | Effort | Prerequisites | PASS đầu ra |
|---|---|---|---|---|
| [25 · Compute](/platform/25-compute-mental-model) | Core / MUST KNOW | Deep | 00, 03, 08 | Classify ten workloads with API compatibility and cost ownership |
| [26 · Lakeflow Jobs](/platform/26-lakeflow-jobs) | Core / CRITICAL MUST KNOW | Deep | 25, 11, 15, Airflow | Trace task DAG/failure/repair and scheduler boundary |
| [27 · SDP and Lakeflow pipelines](/platform/27-declarative-pipelines) | Core / CRITICAL MUST KNOW | Deep | 09, 24, 25, 26 | Distinguish dataset graph, OSS framework and managed extensions |
| [28 · Unity Catalog](/platform/28-unity-catalog) | Core / CRITICAL MUST KNOW | Deep | 00, 09, 26, 27 | Design ownership, privilege traversal, isolation and lineage/audit |
| [29 · Databricks SQL](/platform/29-databricks-sql) | Core / MUST KNOW | Deep | 01, 25, 28 | Governed BI serving, warehouse abstraction and query correctness |
| [30 · Platform boundaries](/platform/30-platform-boundaries) | Core / CRITICAL MUST KNOW | Deep | 25-29, both correctness gates | Defend Databricks-centric and hybrid architectures |

Reading order sau streaming gate: Compute → Jobs → SDP/Lakeflow pipelines → Unity Catalog → Databricks SQL → Platform boundaries → [Platform Design gate](/assessments/mid-gate-platform-design). Governance/access preflight trong [optional Free Edition setup](/setup/databricks-free-edition) precedes all workspace labs; detailed governance follows orchestration for resource context. [Platform evidence](/labs/platform-evidence) separates portable, local Spark and workspace tests.

## Production Engineering {#production}

| Chapter | Priority | Prerequisite | PASS output |
|---|---|---|---|
| [31 · Performance engineering mental model](/production/31-performance-mental-model) | CRITICAL MUST KNOW | 03-08,25-30 | Rank bottlenecks with falsifiable measurements |
| [32 · Query plans and Spark UI reasoning](/production/32-query-plans) | MUST KNOW | 03-06,31 | Read movement/join/AQE and task evidence |
| [33 · File size and the small file problem](/production/33-small-files) | MUST KNOW | 07-08,31-32 | Compare active files/stats/partitions with equal output |
| [34 · Partitioning, liquid clustering and data skipping](/production/34-data-layout) | CRITICAL MUST KNOW | 33 | Choose layout by workload/capability |
| [35 · Photon and engine optimization](/production/35-photon) | SHOULD KNOW | 25,31-34 | Explain engine limits and cost |
| [36 · ROAS performance case study](/production/36-performance-case-study) | CRITICAL MUST KNOW | 31-35 | Prioritize ROAS fixes preserving correctness |
| [37 · Observability mental model](/production/37-observability-mental-model) | CRITICAL MUST KNOW | 14-15,26 | Separate pipeline/data/compute/business health |
| [38 · Databricks observability signals](/production/38-databricks-observability) | MUST KNOW | 28-29,37 | Correlate platform signals and availability |
| [39 · Data quality and ROAS contracts](/production/39-data-quality) | CRITICAL MUST KNOW | 01,11-15,37 | Define scoped business quality contracts |
| [40 · Expectations and quality policy](/production/40-expectations) | CRITICAL MUST KNOW | 27,39 | Defend warn/drop/fail/quarantine policy |
| [41 · Testing strategy and the ROAS test pyramid](/production/41-testing-strategy) | CRITICAL MUST KNOW | 39-40,15 | Map code/data/platform test layers |
| [42 · CI/CD for data engineering](/production/42-ci-cd) | CRITICAL MUST KNOW | 26,28,41 | Enforce version/isolation/promotion |
| [43 · Declarative Automation Bundles](/production/43-declarative-automation-bundles) | CRITICAL MUST KNOW | 41-42 | Validate resource/target/identity configuration |
| [44 · GitHub Actions and safe release flow](/production/44-github-actions) | CRITICAL MUST KNOW | 41-43 | Review OIDC trust and protected environments |
| [45 · Release safety, code rollback and data repair](/production/45-release-rollback) | MUST KNOW | 08,15,24,42-44 | Separate code rollback and data repair |

Dependency: plans/layout/skew → performance case and [Performance Diagnosis gate](/assessments/mid-gate-performance-diagnosis) → observability → quality/expectations → testing → CI/CD → DABs → GitHub release → rollback → [Production Readiness gate](/assessments/mid-gate-production-readiness). Signals and performance investigations iterate together. [Production evidence](/labs/production-evidence) separates local tests from pending workspace acceptance.

## Iceberg & Interoperability {#iceberg}

| Chapter | Priority | Prerequisite | PASS output |
|---|---|---|---|
| [46 · Why Apache Iceberg exists](/iceberg/46-why-iceberg) | MUST KNOW | 45 and Production Readiness gate | Separate format/engine/catalog/storage |
| [47 · Iceberg metadata, snapshots and history](/iceberg/47-metadata-snapshots) | CRITICAL MUST KNOW | 46 | Trace snapshots and real metadata |
| [48 · Catalogs and Iceberg REST resolution](/iceberg/48-catalogs) | CRITICAL MUST KNOW | 47 | Trace resolution and commit authority |
| [49 · Schema evolution and hidden partitioning](/iceberg/49-schema-partition-evolution) | MUST KNOW | 48 | Verify schema/spec continuity |
| [50 · Iceberg row-level changes](/iceberg/50-row-level-changes) | SHOULD KNOW | 49 | Explain mutations and reader constraints |
| [51 · Delta Lake versus Apache Iceberg](/iceberg/51-delta-vs-iceberg) | CRITICAL MUST KNOW | 50 | Choose interoperability versus migration |
| [52 · Managed Iceberg on Databricks](/iceberg/52-managed-iceberg) | SHOULD KNOW | 51 | Assign managed/foreign lifecycle ownership |

## System Design {#system-design}

| Chapter | Priority | Prerequisite | PASS output |
|---|---|---|---|
| [53 · Databricks versus BigQuery](/system-design/53-databricks-vs-bigquery) | CRITICAL MUST KNOW | 52 | Justify stay or migrate from a GCP workload |
| [54 · Databricks versus Snowflake](/system-design/54-databricks-vs-snowflake) | SHOULD KNOW | 53 | Compare SQL/open-table operating ownership |
| [55 · Databricks versus Microsoft Fabric](/system-design/55-databricks-vs-fabric) | SHOULD KNOW | 54 | Evaluate Microsoft fit and conversion limits |
| [56 · Platform decision framework](/system-design/56-decision-framework) | CRITICAL MUST KNOW | 55 | Build scenario-specific scorecards |
| [57 · When not to use Databricks](/system-design/57-when-not-databricks) | CRITICAL MUST KNOW | 56 | Simplify without losing correctness |
| [58 · Lock-in is multi-layered](/system-design/58-lock-in-layers) | SHOULD KNOW | 57 | Test exit contracts across coupling layers |
| [59 · Open lakehouse architecture](/system-design/59-open-lakehouse) | SHOULD KNOW | 58 | Own multi-engine/catalog lifecycle |
| [60 · System design case studies](/system-design/60-system-design-cases) | CRITICAL MUST KNOW | 59 | Defend four distinct case designs |

Dependency: format → snapshots → catalog → schema/partition evolution → mutations → format/interoperability → managed ownership → platform comparisons → decision framework → simplification/lock-in → open architecture → four cases → [Platform and Lakehouse System Design gate](/assessments/mid-gate-platform-lakehouse-system-design). [Local Iceberg setup](/setup/local-iceberg) precedes runtime labs; [evidence](/labs/iceberg-evidence) separates measured semantics from sourced platform and architecture judgment.

## Capstone {#capstone}

**Near-real-time Advertising ROAS Lakehouse**, Advanced / MUST KNOW / Deep. Prerequisites: grain, keys, Delta, correctness, orchestration, quality và cost. Sources của bài tập: Google Ads, Meta Ads, TikTok Ads, Unity Ads, Adjust, callbacks và file attribution. SLA bài tập: reporting freshness khoảng 15 phút; attribution có thể thay đổi trong 72 giờ.

| Stage | Learner phải làm | Gate trước stage tiếp |
|---|---|---|
| 1 · Requirements | Định nghĩa event time, grain, SLA và source constraints | Phân biệt source delay với pipeline delay |
| 2 · Architecture decision | Chọn batch/incremental/streaming có căn cứ | Nêu replay unit và key contracts |
| 3 · Failure reveal | Điều tra duplicate, API failure, delayed file hoặc schema change | Chỉ ra metric nào sai, tại lớp nào |
| 4 · Revision | Sửa thiết kế sau bằng chứng failure | Giữ được idempotency và reconciliation |
| 5 · Implementation | Xây pipeline và tests | Replay/backfill không double count |
| 6 · Production validation | Chứng minh freshness, completeness, recovery và cost | Có runbook và failure evidence |
| 7 · Interview | Bảo vệ lựa chọn, alternatives và giới hạn | Trả lời điều kiện khiến phải đổi kiến trúc |

Chưa có solution architecture hoặc implementation trong Iteration 1. Kafka và streaming không phải mặc định. Cost tags của từng lab sẽ là FREE / LOW COST / OPTIONAL CLOUD; không provision cloud tự động.

## Interview {#interview}

Foundation đến Advanced / MUST KNOW. Câu hỏi gắn scenario với competence: duplicate callback → idempotency; join khác grain → fan-out; late attribution → lookback/reconciliation; straggler → skew; failed backfill → replay boundary; checkpoint loss → delivery semantics. Mỗi chapter có checkpoint riêng; question bank đầy đủ chưa được viết.
