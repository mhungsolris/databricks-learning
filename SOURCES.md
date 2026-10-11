# Sources and terminology

## Architecture and interoperability source ledger

Verified2026-10-11 against official documents. Planning: .researches/architecture-plan.md. Three archives contain25successful dual HTML/text representations; unavailable URL guesses remain explicit records. Save/consolidate use project research scripts with publication disabled.

Apache releases pin Iceberg1.12.0 with Spark4.0/Scala2.13 runtime. Numbered1.12.0 integration routes returned404; dated latest docs identify1.12.0. HadoopCatalog reference is a dated nightly Javadoc limitation reference, not a claim of nightly runtime execution.

[Website capability ledger](/iceberg/current-platform-support) owns managed/foreign/read/write/version constraints. Local semantics, sourced capabilities and architecture judgment have separate evidence tiers. No authenticated platform operation or speed ranking is implied.

| Source | Scope |
|---|---|
| [releases](https://iceberg.apache.org/releases/) | Apache semantics/catalog/runtime |
| [spec](https://iceberg.apache.org/spec/) | Apache semantics/catalog/runtime |
| [rest](https://iceberg.apache.org/rest-catalog-spec/) | Apache semantics/catalog/runtime |
| [databricks](https://docs.databricks.com/aws/en/iceberg/) | Current platform architecture and compatibility |
| [uniform](https://docs.databricks.com/aws/en/delta/iceberg-reads) | Current platform architecture and compatibility |
| [ucRest](https://docs.databricks.com/aws/en/external-access/iceberg) | Current platform architecture and compatibility |
| [v3](https://docs.databricks.com/aws/en/iceberg/iceberg-v3) | Current platform architecture and compatibility |
| [bigquery](https://docs.cloud.google.com/bigquery/docs/introduction) | Current platform architecture and compatibility |
| [bqIceberg](https://docs.cloud.google.com/bigquery/docs/biglake-iceberg-tables-in-bigquery) | Current platform architecture and compatibility |
| [googleLakehouse](https://docs.cloud.google.com/lakehouse/docs/manage-tables) | Current platform architecture and compatibility |
| [snowflake](https://docs.snowflake.com/en/user-guide/tables-iceberg) | Current platform architecture and compatibility |
| [snowArchitecture](https://docs.snowflake.com/en/user-guide/intro-key-concepts) | Current platform architecture and compatibility |
| [fabric](https://learn.microsoft.com/en-us/fabric/onelake/onelake-overview) | Current platform architecture and compatibility |
| [fabricIceberg](https://learn.microsoft.com/en-us/fabric/onelake/onelake-iceberg-tables) | Current platform architecture and compatibility |
| [fabricDelta](https://learn.microsoft.com/en-us/fabric/fundamentals/delta-lake-interoperability) | Current platform architecture and compatibility |
| [delta](https://docs.delta.io/) | Current platform architecture and compatibility |
| [spark](https://iceberg.apache.org/docs/latest/spark-getting-started/) | Apache semantics/catalog/runtime |
| [queries](https://iceberg.apache.org/docs/latest/spark-queries/) | Apache semantics/catalog/runtime |
| [ddl](https://iceberg.apache.org/docs/latest/spark-ddl/) | Apache semantics/catalog/runtime |
| [writes](https://iceberg.apache.org/docs/latest/spark-writes/) | Apache semantics/catalog/runtime |
| [evolution](https://iceberg.apache.org/docs/latest/evolution/) | Apache semantics/catalog/runtime |
| [partition](https://iceberg.apache.org/docs/latest/partitioning/) | Apache semantics/catalog/runtime |
| [openCatalog](https://docs.snowflake.com/en/user-guide/opencatalog/overview) | Current platform architecture and compatibility |
| [hadoop](https://iceberg.apache.org/javadoc/nightly/org/apache/iceberg/hadoop/HadoopCatalog.html) | Apache semantics/catalog/runtime |

Skill/source boundary: databricks-core provides CLI/auth guidance; official Iceberg/platform docs define table semantics. No additional sibling skills or catalogs were installed.

Additional format comparison source: [Iceberg Spark streaming](https://iceberg.apache.org/docs/latest/spark-structured-streaming/), verified2026-10-11, latest1.12.0 docs. Append-only reads and mutation-snapshot failure/skip boundaries; append/complete writes and maintenance. No Iceberg streaming runtime is claimed.


## Production hardening source ledger

Verified 2026-10-11, current AWS Databricks and pinned Spark4.0.4 sources. Research planning: .researches/production-plan.md. Main archive26 successful dual-representation sources and three404 records; supplement4 successful sources resolves event-log/CI URLs. All32 successful source documents, including current alerts and CLI release pages, are saved and consolidated with publication disabled. Live cloud capabilities remain unexecuted.

| Source | Verified claim / scope |
|---|---|
| [clustering](https://docs.databricks.com/aws/en/tables/clustering) | Manual keys, CLUSTER BY AUTO, managed Delta DBR15.4LTS+; AUTO depends on predictive optimization |
| [partitioning](https://docs.databricks.com/aws/en/tables/partitions) | Current liquid-first guidance; existing/custom partition decisions still workload-specific |
| [predictive](https://docs.databricks.com/aws/en/optimizations/predictive-optimization) | UC managed, Premium+/region/runtime requirements; serverless maintenance billing; retention policy |
| [photon](https://docs.databricks.com/aws/en/compute/photon) | Native vectorized execution, coverage/fallback; serverless/warehouse vs classic API enablement |
| [profile](https://docs.databricks.com/aws/en/sql/user/queries/query-profile) | Operator/task/IO evidence on supported compute; no locally fabricated profile |
| [history](https://docs.databricks.com/aws/en/sql/user/queries/query-history) | Query timing/history and access requirements |
| [system](https://docs.databricks.com/aws/en/admin/system-tables) | UC system catalog, historical coverage, regional/global scope and sensitive contents |
| [jobs](https://docs.databricks.com/aws/en/admin/system-tables/jobs) | system.lakeflow job/task historical datasets |
| [query](https://docs.databricks.com/aws/en/admin/system-tables/query-history) | system.query.history coverage and metrics |
| [billing](https://docs.databricks.com/aws/en/admin/system-tables/billing) | system.billing.usage, SKU/usage context, not a complete cost invoice by itself |
| [expectations](https://docs.databricks.com/aws/en/ldp/expectations) | dp.expect, expect_or_drop, expect_or_fail; fail metrics and parallel-flow limits |
| [qualitypatterns](https://docs.databricks.com/aws/en/ldp/expectation-patterns) | Quarantine and record vs dataset validation patterns |
| [bundles](https://docs.databricks.com/aws/en/dev-tools/bundles/) | Current Declarative Automation Bundles name and project mental model |
| [settings](https://docs.databricks.com/aws/en/dev-tools/bundles/settings) | Root databricks.yml, include/resource paths and variable/target configuration |
| [modes](https://docs.databricks.com/aws/en/dev-tools/bundles/deployment-modes) | Only development/production modes; staging is target; lock/concurrency defaults |
| [runas](https://docs.databricks.com/aws/en/dev-tools/bundles/run-as) | Deploy and run identity separation and service principal targets |
| [commands](https://docs.databricks.com/aws/en/dev-tools/cli/bundle-commands) | Verified current bundle plan/schema/validate/deploy/run/destroy flags |
| [direct](https://docs.databricks.com/aws/en/dev-tools/bundles/direct) | New-bundle default1.3+, automatic migration, Terraform engine removed1.20 |
| [oidc](https://docs.databricks.com/aws/en/dev-tools/auth/provider-github) | github-oidc; scoped environment trust; exact subject format including immutable IDs |
| [ci](https://docs.databricks.com/aws/en/dev-tools/ci-cd) | DABs recommended approach for Databricks CI/CD |
| [unittest](https://docs.databricks.com/aws/en/notebooks/testing) | Python/pytest/mocking guidance; mocked calls not platform proof |
| [deltaHistory](https://docs.databricks.com/aws/en/tables/history) | Time travel requires logs/files, default retention; history not backup |
| [restore](https://docs.databricks.com/aws/en/sql/language-manual/delta-restore) | RESTORE new data-changing commit and downstream replay consequences |
| [spark](https://spark.apache.org/docs/4.0.4/sql-performance-tuning.html) | Spark4.0.4 plans, AQE, join strategies and file planning |
| [dfTests](https://spark.apache.org/docs/4.0.4/api/python/getting_started/testing_pyspark.html) | Actual DataFrame/schema tests and fixture boundaries |
| [githubEnvironments](https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/manage-environments) | Required reviewers, environment/branch protection settings outside YAML |
| [pytest](https://docs.pytest.org/en/stable/how-to/usage.html) | Test invocation and fixtures/parametrization |
| [eventlog](https://docs.databricks.com/aws/en/ldp/monitor-event-logs) | Current plural monitor-event-logs URL and managed pipeline signals |
| [github](https://docs.databricks.com/aws/en/dev-tools/ci-cd/github) | Databricks setup-cli Actions guidance |
| [flows](https://docs.databricks.com/aws/en/dev-tools/ci-cd/flows) | Review/test/validate/deploy/acceptance release flow |

Terminology and skill conflicts: primary name is Declarative Automation Bundles; the Jobs skill retains older naming. Current CLI1.20.0 official release was checksum-verified into an ignored local folder; version/help/schema were executed without authentication. [Release1.20.0](https://github.com/databricks/cli/releases/tag/v1.20.0) confirms the pin. Schema permits some semantic strings such as mode values, so portable mode/isolation checks remain necessary. Python re does not support CLI schema Unicode categories; the checker uses a Unicode regex engine without altering the captured schema.

The DAB deploy reference suggests skipping dev validation while its general rule requires strict validation; this course follows strict validation before every workspace deployment. User policy keeps all authenticated operations pending; a skill recommendation is not authorization for a cloud deploy. Automatic layout/engine/expectation statements are current product behavior, not measured local effects.


Additional current sources:

- [Current SQL alerts](https://docs.databricks.com/aws/en/sql/user/alerts/): scheduled query/condition notifications and current vs legacy behavior.
- [CLI1.20.0 release](https://github.com/databricks/cli/releases/tag/v1.20.0): Terraform engine removal and current lifecycle pin, corroborated by local-only version/schema/help.

## Platform claim ledger

Verified 2026-10-11, current AWS Databricks docs unless another vendor/version is named. Archive: .researches/2026-10-11-platform/ (33 official fetched records) and .researches/2026-10-11-platform-auth/ (four auth/parameter/serverless records). These are source evidence, not workspace evidence.

| Source | Supported claim | Scope / caveat |
|---|---|---|
| [serverless overview](https://docs.databricks.com/aws/en/compute/serverless/) | On-demand managed allocation, startup/scaling benefits and runtime upgrades | No latency/cost measurement inferred from the sample |
| [free-edition](https://docs.databricks.com/aws/en/getting-started/free-edition) | Personal serverless learning offering | Optional learner-owned signup; no account automation |
| [free-limits](https://docs.databricks.com/aws/en/getting-started/free-edition-limitations) | Serverless-only, quota/fair use, one small warehouse, task/pipeline and admin limits | Feature availability is not an observed account inventory |
| [architecture](https://docs.databricks.com/aws/en/getting-started/high-level-architecture) | Account/workspace/metastore, control and compute planes, storage distinction | AWS architecture; Free Edition cannot prove enterprise topology |
| [compute](https://docs.databricks.com/aws/en/compute/) | Serverless, classic and SQL compute surfaces | Compatibility and resource selection remain necessary |
| [serverless-limits](https://docs.databricks.com/aws/en/compute/serverless/limitations) | Spark Connect/API/config/runtime and streaming-trigger limitations | Notebook/jobs scope; pipeline mode has separate rules |
| [jobs-compute](https://docs.databricks.com/aws/en/jobs/compute) | Compute per task; notebooks/Python/SQL/pipelines choices | Generic JAR row conflicts with narrower current task docs |
| [jar-task](https://docs.databricks.com/aws/en/jobs/tasks/jar) | Classic or serverless JAR task with supported environment | Prefer this task-specific guide over generic classic-only row |
| [jar-serverless](https://docs.databricks.com/aws/en/jobs/how-to/use-jars-in-workflows) | Public API/JDK/Scala/Connect compatibility and no RDD/native libraries | No JAR/cloud execution here |
| [jobs](https://docs.databricks.com/aws/en/jobs/) | Lakeflow Jobs is workflow orchestration | Distinct from compute and declarative dataflow |
| [jobs-dependencies](https://docs.databricks.com/aws/en/jobs/run-if) | Run-if and branch/dependency behavior | Expected DAG path, not captured run states |
| [jobs-repair](https://docs.databricks.com/aws/en/jobs/repair-job-failures) | Multi-task repair re-executes subset; task idempotency remains application-owned | No partial-write rollback guarantee |
| [jobs-values](https://docs.databricks.com/aws/en/jobs/task-values) | Small task metadata passing | Not bulk DataFrame or durable business checkpoint |
| [jobs-loops](https://docs.databricks.com/aws/en/jobs/tasks/for-each) | For-each nested tasks and input array | Concurrency must respect workspace and target contracts |
| [sdp](https://docs.databricks.com/aws/en/ldp/concepts/spark-declarative-pipelines) | SDP framework vs Lakeflow extensions on DBR | Expectations/AUTO CDC/event log are platform extensions |
| [pipeline-python](https://docs.databricks.com/aws/en/ldp/developer/python-dev) | Decorated dataset definitions and read-derived graph | Planning side effects forbidden; local AST only |
| [pipeline-properties](https://docs.databricks.com/aws/en/ldp/properties) | catalog/schema publishing and serverless/triggered configuration | schema preferred over legacy target; CLI strict validation pending |
| [pipeline-expectations](https://docs.databricks.com/aws/en/ldp/developer/ldp-python-ref-expectations) | Expectation actions and Python APIs | Negative-row input tested; real fail expectation pending |
| [unity-catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/) | Governance: access, lineage, audit, discovery | Namespace differs from physical storage |
| [uc-privileges](https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-privileges/) | Ownership, grants, traversal and inheritance | Fixture tests do not enforce UC |
| [uc-storage](https://docs.databricks.com/aws/en/connect/unity-catalog/cloud-storage/) | Storage credentials/external locations and managed/external boundaries | No IAM credentials or cloud paths configured |
| [uc-lineage](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-lineage) | Captured lineage and access/coverage requirements | External extraction needs additional evidence |
| [sql](https://docs.databricks.com/aws/en/sql/) | Cloud warehouse capability on lakehouse, SQL editor/dashboards/jobs | Not merely Spark SQL UI |
| [warehouse](https://docs.databricks.com/aws/en/compute/sql-warehouse) | SQL compute, recommend serverless where available | Use existing Free Edition warehouse |
| [warehouse-scaling](https://docs.databricks.com/aws/en/compute/sql-warehouse/warehouse-behavior) | Sizing, queueing and managed serverless workload scaling | No tiny-data performance/cost benchmark |
| [spark-sdp](https://spark.apache.org/docs/4.1.0/declarative-pipelines-programming-guide.html) | OSS SDP guide for Spark4.1.0 | Accepted local Spark4.0.4 stays pinned; no SDP execution |
| [airflow](https://airflow.apache.org/docs/apache-airflow-providers-databricks/stable/operators/run_now.html) | Provider submission of Databricks Jobs | Version-qualified retry/durable behavior, no provider execution |
| [dbt](https://docs.getdbt.com/docs/build/models) | SQL/Python models and dependency framework | Learning bridge, not literal pipeline equivalence |
| [dbt-tests](https://docs.getdbt.com/docs/build/data-tests) | Data-test assertions/violating rows | Business tests complement platform expectations |
| [bigquery](https://cloud.google.com/bigquery/docs/introduction) | Managed SQL warehouse with storage/compute abstraction | External data paths also exist |
| [bigquery-capacity](https://docs.cloud.google.com/bigquery/docs/admin-intro) | On-demand and slot/reservation capacity choices | No obsolete serverless-vs-Spark dichotomy |
| [oauth](https://docs.databricks.com/aws/en/dev-tools/auth/oauth-u2m) | Interactive user OAuth/unified authentication | Only proposed learner-owned auth; no tokens configured |
| [bundles](https://docs.databricks.com/aws/en/dev-tools/bundles/) | Declarative resource packaging | Artifact contract tests are not strict CLI/API validation |

### Terminology and source conflicts

Current product name is Lakeflow pipelines, built on/interoperable with Apache Spark Declarative Pipelines. Lakeflow Spark Declarative Pipelines and DLT labels still occur in older pages, skills and URLs. The framework and managed product are distinct. Core/Jobs/DAB skill examples contain older terminology/runtime/defaults; official current references control this iteration.

The generic Jobs compute table still lists JAR as classic, while the current JAR task and serverless JAR guide explicitly document serverless support. Use task-specific compatibility guidance; the compute decision row narrows classic fallback to unsupported RDD/internals/native requirements. The DAB pipeline skill uses target; current properties prefer schema, which the sample uses.

OAuth guidance: [U2M](https://docs.databricks.com/aws/en/dev-tools/auth/oauth-u2m), [M2M](https://docs.databricks.com/aws/en/dev-tools/auth/oauth-m2m), [unified auth](https://docs.databricks.com/aws/en/dev-tools/auth/), [dynamic values](https://docs.databricks.com/aws/en/jobs/dynamic-value-references). Workspace support/strict validation remains pending. No CLI installation, secret/profile configuration or authenticated operation is claimed.


Mỗi section ghi verification date và scope riêng, timezone Asia/Saigon. Foundation sources checked 2026-10-10; platform sources checked 2026-10-11. Databricks dùng AWS documentation trừ khi nói khác; cần verify lại khi triển khai ở cloud/runtime cụ thể. Các bài “latest” upstream không xác định version của Databricks Runtime.

## Terminology {#terminology}

| Thuật ngữ dùng trong handbook | Kết quả kiểm tra | Nguồn official |
|---|---|---|
| Lakeflow Jobs | Jobs/task DAG orchestration; task, job và trigger là các concepts khác nhau | [Jobs](https://docs.databricks.com/aws/en/jobs/) |
| Apache Spark Declarative Pipelines (SDP) / Lakeflow pipelines | Verified 2026-10-11: SDP là OSS framework; Lakeflow pipelines built on SDP, chạy trên Databricks Runtime và thêm platform features. Lakeflow Spark Declarative Pipelines / DLT là older labels còn gặp trong skills/URLs | [SDP comparison](https://docs.databricks.com/aws/en/ldp/concepts/spark-declarative-pipelines) |
| Declarative Automation Bundles | Tên hiện hành, formerly Databricks Asset Bundles | [Bundles](https://docs.databricks.com/aws/en/dev-tools/bundles/) |
| Unity Catalog | Unified governance for data/AI: access control, lineage, audit, discovery; logical namespace distinct from storage | [Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/) |
| Structured Streaming | Incremental stream processing; guarantees cần qualification theo source/sink, checkpoint và usage | [Concepts](https://docs.databricks.com/aws/en/structured-streaming/concepts) |
| Serverless compute | Databricks quản lý infrastructure; availability/features theo workspace/cloud | [Serverless](https://docs.databricks.com/aws/en/compute/serverless/) |
| Databricks SQL | Data warehousing/SQL serving capability | [SQL](https://docs.databricks.com/aws/en/sql/) |
| Delta Lake | Open table/storage layer với transactional metadata; không tương đương raw Parquet files | [Delta](https://docs.delta.io/latest/delta-intro.html) |
| Auto Loader | Incremental file ingestion qua cloudFiles; vẫn relevant | [Auto Loader](https://docs.databricks.com/aws/en/ingestion/cloud-object-storage/auto-loader/) |
| Apache Iceberg support | Managed/foreign tables và interoperability có requirements/limitations riêng; foreign tables read-only trong nguồn kiểm tra | [Iceberg in Databricks](https://docs.databricks.com/aws/en/iceberg/) |

## Chapter 00 claims

| Source | Claim được hỗ trợ | Scope / caveat |
|---|---|---|
| [Databricks architecture](https://docs.databricks.com/aws/en/getting-started/high-level-architecture) | Platform planes; classic/serverless placement; default storage | AWS; không khẳng định mọi data/compute nằm trong customer account |
| [Lakehouse](https://docs.databricks.com/aws/en/lakehouse/) | Table management, processing và governance trên lakehouse | Vendor architectural explanation; không dùng làm benchmark so sánh |
| [Compute](https://docs.databricks.com/aws/en/compute/) | Compute categories | Availability cần tra theo workload/cloud |
| [Spark cluster overview](https://spark.apache.org/docs/latest/cluster-overview.html) | Driver, executors, tasks | Upstream latest; basic distributed mental model |
| [Delta introduction](https://docs.delta.io/latest/delta-intro.html) | ACID, metadata và table capabilities | Không suy ra business deduplication tự động |
| [Parquet overview](https://parquet.apache.org/docs/overview/) | Column-oriented file format | Không có table transactions chỉ nhờ file format |
| [Iceberg specification](https://iceberg.apache.org/spec/) | Snapshot, metadata và data-file membership | Engine/platform support không phải toàn bộ spec |
| [BigQuery overview](https://cloud.google.com/bigquery/docs/introduction) | Managed analytical tables, query service và external workloads | Comparison không giới hạn BigQuery thành SQL-only |
| [BigQuery storage overview](https://cloud.google.com/bigquery/docs/storage_overview) | Storage tách query compute | Không so sánh separation như lợi thế độc quyền Databricks |

CSV snapshot lab, doanh thu 650/350 và workload recommendations là examples/reasoning của handbook. Chúng không phải số đo hoặc benchmark từ vendor. SLA 15 phút và attribution correction 72 giờ là assumptions của capstone, không phải guarantee của Google/Meta/TikTok/Unity/Adjust.

## Chapters 01-03 claims

| Source | Claim được dùng | Scope / caveat |
|---|---|---|
| [Microsoft star-schema guidance](https://learn.microsoft.com/en-us/power-bi/guidance/star-schema) | Consistent fact grain, fact/dimension và surrogate keys | Modeling reference; không áp Power BI filter semantics cho SQL |
| [BigQuery keys](https://docs.cloud.google.com/bigquery/docs/primary-foreign-keys) | Keys không enforced; owner cần giữ validity | Không coi DDL là uniqueness test |
| [Databricks constraints](https://docs.databricks.com/aws/en/tables/constraints) | Enforced NOT NULL/CHECK khác informational keys | Provider/UC/runtime requirements cần kiểm tra khi triển khai |
| [BigQuery overview](https://docs.cloud.google.com/bigquery/docs/introduction) và [storage](https://docs.cloud.google.com/bigquery/docs/storage_overview) | Managed query/storage model; SQL/Python, compute-storage separation | Native-table operating model không bao trùm mọi table type |
| [External tables](https://docs.cloud.google.com/bigquery/docs/external-tables) | Warehouse có external data capabilities | Table mode/limitations cụ thể, không khẳng định mọi external reader feature parity |
| [BigQuery pricing](https://cloud.google.com/bigquery/pricing) | On-demand/capacity compute, storage charging model | Không dùng dollar rates hoặc dự báo savings; page fetched qua urllib |
| [Databricks tables](https://docs.databricks.com/aws/en/tables/) và [compute](https://docs.databricks.com/aws/en/compute/) | Managed/external lifecycle và execution surfaces | Serverless/runtime availability theo workload/cloud |
| [Spark SQL guide](https://spark.apache.org/docs/latest/sql-programming-guide.html) và [DataFrames](https://spark.apache.org/docs/latest/sql-getting-started.html) | Structured APIs, shared engine và SparkSession | Reading example chưa runtime-executed trong local workspace |
| [Spark programming guide](https://spark.apache.org/docs/latest/rdd-programming-guide.html) | Lazy transformations, actions và recomputation | Metadata/schema work vẫn có thể xảy ra trước full materialization |
| [Spark cluster overview](https://spark.apache.org/docs/latest/cluster-overview.html) | Driver/executor/application/job/stage/task glossary | Classic distributed mental model; không dùng cho exact job/stage counts |
| [explain API](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.explain.html) và [monitoring](https://spark.apache.org/docs/latest/monitoring.html) | Physical plan outline khác measured execution | Plan không là performance measurement |
| [PySpark installation](https://spark.apache.org/docs/latest/api/python/getting_started/install.html) | Local classic PySpark cần JVM và dependencies | Retrieved upstream latest tự ghi 4.2.0; chưa cài PySpark/JDK |

Modeling/metric examples là fixtures của handbook. Lab 01 test fan-out, coverage, null/duplicate keys, detail grain và allocation. Lab 02 kiểm schema/key validity trên files. Portable Lab03 measured SQLite output; model execution counter không phải Spark job count. Real Spark/Delta evidence xem [runtime artifacts](/labs/runtime-evidence); distributed recovery/performance benchmark chưa có.

## Chapters 04-08 and runtime claims

Verified 2026-10-10. Spark sources pinned4.0.4; Delta protocol tag4.0.1. Databricks docs scope AWS, không đồng nhất OSS runtime với DBR/Photon.

| Official source | Claim / application | Boundary |
|---|---|---|
| [Spark requirements](https://spark.apache.org/docs/4.0.4/) và [install](https://spark.apache.org/docs/4.0.4/api/python/getting_started/install.html) | Java17/21, Python support; local execution | Host/container versions recorded riêng |
| [Apache Docker source](https://github.com/apache/spark-docker) | Official Apache image provenance | Actual pulled digest owns reproducibility in runtime/spark.json |
| [Coalesce](https://spark.apache.org/docs/4.0.4/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.coalesce.html), [repartition](https://spark.apache.org/docs/4.0.4/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.repartition.html) | Narrow reduction vs shuffle redistribution | No benchmark/sizing recommendation |
| [RDD guide](https://spark.apache.org/docs/4.0.4/rdd-programming-guide.html), [SQL tuning](https://spark.apache.org/docs/4.0.4/sql-performance-tuning.html) | Shuffle mechanics, joins/hints/AQE | Strategy depends on workload/type/config |
| [Monitoring](https://spark.apache.org/docs/4.0.4/monitoring.html), [WebUI source](https://github.com/apache/spark/blob/v4.0.4/core/src/main/scala/org/apache/spark/ui/WebUI.scala) | Event logs/UI and actual bind behavior | Stage IDs/counts are observations, not guarantees |
| [Null semantics](https://spark.apache.org/docs/4.0.4/sql-ref-null-semantics.html) | NULL equality vs null-safe join | UNKNOWN sentinel is non-null value |
| [Parquet format](https://parquet.apache.org/docs/file-format/), [concepts](https://parquet.apache.org/docs/concepts/), [Spark reader](https://spark.apache.org/docs/4.0.4/sql-data-sources-parquet.html) | Row groups/chunks/footer/schema, pruning/pushdown | Raw format has no table transaction layer |
| [Delta releases](https://docs.delta.io/releases/), [quickstart](https://docs.delta.io/quick-start/) | Spark4.0.x / Delta4.0.x compatibility, extensions/catalog | Exact4.0.4/4.0.1 pair also executed locally |
| [Delta protocol v4.0.1](https://github.com/delta-io/delta/blob/v4.0.1/PROTOCOL.md), [concurrency](https://docs.delta.io/concurrency-control/), [batch](https://docs.delta.io/delta-batch/) | Snapshot actions, optimistic commits, mutations/schema/time travel | Single-writer experiment does not test every protocol feature |
| [Databricks Delta](https://docs.databricks.com/aws/en/delta/), [compatibility](https://docs.databricks.com/aws/en/tables/features/feature-compatibility), [AQE](https://docs.databricks.com/aws/en/optimizations/aqe) | Managed platform mapping and runtime feature boundaries | No workspace operations or platform performance claims |
| [Docker CLI](https://docs.docker.com/desktop/features/desktop-cli/) | Desktop start/status workflow | Desktop already installed on authoring host |

Research HTML/extracted text and consolidated artifacts: `.researches/2026-10-10T090000Z/`. Local lab assertions own measured counts/results; vendor docs own protocol/API claims. Parquet inventory/UNKNOWN distribution are synthetic observations, not vendor benchmark numbers.

Nineteen source records và HTML/text snapshots của research này nằm ở `.researches/2026-10-10T020000Z/`; consolidated markdown/JSON được tạo với `--no-publish`. Các nguồn lakehouse/architecture/Delta cũng được re-fetched trong session này.

## Chapters 09-15 correctness claims

Verified **2026-10-11 (Asia/Saigon)**; archive .researches/2026-10-10T180000Z uses UTC folder naming. Nine selected official sources; local observations pinned Spark4.0.4/Delta4.0.1. AWS Databricks docs are platform mapping, not OSS/DBR parity claims.

| Primary source | Claim/application | Boundary |
|---|---|---|
| [Databricks Medallion](https://docs.databricks.com/aws/en/lakehouse/medallion) | Progressive quality/responsibilities, raw→validated→business-ready | Recommended pattern, not mandatory three physical tables; fixture layering is design decision |
| [Databricks MERGE](https://docs.databricks.com/aws/en/delta/merge) | Match/source preprocessing; duplicate detection DBR16+ vs15.4LTS | Local OSS4.0.1 ambiguity observed separately; unmatched inserts require source uniqueness |
| [Delta MERGE/update](https://docs.delta.io/delta-update/) | Update/insert semantics and schema compatibility | Fixed explicit schema; auto evolution disabled; business keys/revisions are contracts |
| [Delta batch](https://docs.delta.io/delta-batch/) | Schema checks, atomic scoped overwrite, replaceWhere validation | Complete affected-scope input needed; not multi-table/cursor transaction |
| [Databricks selective overwrite](https://docs.databricks.com/aws/en/delta/selective-overwrite) | Predicate overwrite/platform options | Runtime-specific features not assumed on OSS |
| [Delta concurrency](https://docs.delta.io/concurrency-control/) | Optimistic concurrency/conflict behavior | No simultaneous-writer stress test; business same-scope coordination still needed |
| [Delta Change Data Feed](https://docs.delta.io/delta-change-data-feed/) | Enabled table change stream/history awareness | No CDF lab; retention/bootstrap/source-contract limits, not external API cursor |
| [Databricks watermarks](https://docs.databricks.com/aws/en/structured-streaming/watermarks) | Event-time/state threshold and resource/lateness trade-offs | Not historical API retrieval or batch cursor; streaming execution deferred |
| [Spark4.0.4 streaming guide](https://spark.apache.org/docs/4.0.4/streaming/apis-on-dataframes-and-datasets.html) | Stateful watermark guarantees/operation constraints | Within delay protected under applicable operator; outside delay may still process, no always-drop claim |

15-minute freshness,72h mutable attribution,2/6/72h candidate lookbacks and D-1/D-3/D-7 reconciliation are scenario policies to justify using source behavior. No Ads/Adjust API guarantees are asserted. Ordered source revisions, integerUSD cents andUTC make bounded business-state invariants exact. Callback/file channel excluded from event identity; actual external ID/version/deletion guarantees need vendor-specific research before deployment.

## Website implementation sources (baseline)

| Source | Áp dụng | Verified |
|---|---|---|
| [VitePress deployment](https://vitepress.dev/guide/deploy) | Build artifact, project base path, Pages workflow | 2026-10-10 |
| [Mermaid usage](https://mermaid.js.org/config/usage.html) | Client render, strict security và syntax checks | 2026-10-10 |
| [GitHub Pages custom workflows](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages) | Separate build/deploy jobs, permissions và artifact | 2026-10-10 |
| [Reference Terraform handbook](https://vudaian24.github.io/learn-devops/07-terraform.html) | Chia mục, TOC, tables, short code và production notes | 2026-10-10; presentation reference, không phải Databricks authority |

## Evidence and conflicts

Source snapshots được lưu tại `.researches/2026-10-10T010000Z/`, gồm URL/status, HTML và text extraction. `scripts/collect_research.py` tải các URL đã chọn; research consolidation không publish. HTML/text extraction là evidence archive, không phải nội dung website hoặc guarantee chống thay đổi nguồn.

Skills là workflow guidance. Tên pipeline trong installed core/jobs skills có thể khác wording trong docs hiện hành; handbook ưu tiên official docs và ghi alias cho reader tra tutorial cũ. Không sửa skill upstream chỉ để ép thuật ngữ của bài học. Product/runtime/pricing/certification claims ở các chapter tương lai phải được research riêng khi viết.

## Streaming source verification

Verified 2026-10-11, Spark 4.0.4 OSS and current Databricks AWS docs. Local runtime is Spark4.0.4/Delta4.0.1, not DBR. Archive: `.researches/2026-10-11T034500Z/`, twelve HTML/Markdown pairs and consolidated records; publication disabled.

| Official source | Claim and scope |
|---|---|
| [Spark 4.0.4 API guide](https://spark.apache.org/docs/4.0.4/streaming/apis-on-dataframes-and-datasets.html) | Micro-batches, state, one-sided watermark guarantees, dedup, exact join support matrix, output modes and recovery compatibility |
| [Spark 4.0.4 overview](https://spark.apache.org/docs/4.0.4/streaming/index.html) | Default micro-batch vs continuous-processing awareness and guarantees |
| [Databricks checkpoints](https://docs.databricks.com/aws/en/structured-streaming/checkpoints) | Offsets, commits, state, metadata; generic restart restrictions and current source-evolution exception |
| [Databricks stateful streaming](https://docs.databricks.com/aws/en/structured-streaming/stateful-streaming) | State operations, growth and operational guidance; version-specific repartitioning is not local OSS parity |
| [Databricks watermarks](https://docs.databricks.com/aws/en/structured-streaming/watermarks) | Event-time policy and global multiple-input watermark; late tolerance vs state cost |
| [Databricks output modes](https://docs.databricks.com/aws/en/structured-streaming/output-mode) | Aggregation emissions, latency, operator and sink capability; native Delta append/complete, custom MERGE for update |
| [Databricks foreachBatch](https://docs.databricks.com/aws/en/structured-streaming/foreach) | At-least-once writes, user-enforced batch identity, complete consumption of stateful output |
| [Delta streaming](https://docs.delta.io/delta-streaming/) | Native stream sink vs custom foreachBatch writes; txnAppId/txnVersion, new checkpoint requires new app ID |
| [Databricks production guidance](https://docs.databricks.com/aws/en/structured-streaming/production) | Durable checkpoints, retry/idempotent sinks, source/sink and state constraints |
| [Databricks real-time setup](https://docs.databricks.com/aws/en/structured-streaming/real-time/setup) | Awareness only; runtime/operator/compute requirements, no local real-time execution claim |

Compatibility policy uses the pinned Spark guide for local execution. Current DBR source naming/evolution and state repartitioning features are runtime-specific exceptions, not permission to change arbitrary operator keys or state schemas. Generic grouping, dedup and join restrictions remain explicit in Chapter18. Provider defaults are not generalized: the local run records its observed configuration.

Output-mode docs contain an update-mode managed-table example and explicitly note that it fails against native Delta sinks; the course uses foreachBatch MERGE for update aggregates. Watermark and output guarantees concern eligible stream inputs and query/sink boundaries, not permanent business completeness or 72-hour correction capture.

[Lakeflow updates](https://docs.databricks.com/aws/en/ldp/updates) and [streaming-table full refresh](https://docs.databricks.com/aws/en/ldp/full-refresh-st) ground Chapter24 awareness: selected flow checkpoint reset preserves table data; full refresh resets data/state and requires retained source history. No managed platform operation was executed.

