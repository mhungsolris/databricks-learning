# Iteration 1 research and repository assessment

## Architecture judgment synthesis

Iceberg separates format, catalog, storage and engine. Current format support overlaps across Databricks, BigQuery, Snowflake and Fabric, while commit authority, governance, maintenance and client features differ. Open data access does not port all platform behavior.

Official sources establish Iceberg1.12.0 Spark4.0/Scala2.13 compatibility. Local Hadoop-catalog tests measure retained snapshots, schema field identity, mixed partition specs and COW/MOR mutations. REST/multi-engine/cloud operations are not measured.

Current Databricks supports managed/foreign Iceberg and Delta Iceberg reads; their write boundaries differ. BigQuery-managed Iceberg and Google REST-managed tables have distinct contracts. Snowflake managed/external/Horizon paths differ; Fabric virtualization has version, partition/delete and conversion freshness limits. [Capability ledger](docs/iceberg/current-platform-support.md) owns exact constraints.

Scenario decisions preserve a stable BigQuery SQL estate, conditionally evaluate Databricks for diverse transformation/recovery needs and conditionally select Fabric for Microsoft integration. ADRs identify alternatives, owners and reversal tests. Research planning and dated archives are linked in SOURCES.md; no marketing ranking or migration without a measured problem is recommended.


## Production hardening synthesis

Research question/known baseline/stopping rule: .researches/production-plan.md. Current sources support evidence-first diagnosis across query, execution, layout, compute and engine layers. Liquid clustering is recommended before custom partitioning; AUTO needs supported UC managed tables and predictive optimization. Maintenance has requirements/billing and interacts with retention. Photon cannot correct business semantics.

System tables/event logs/query profiles have coverage/access boundaries. Expectation warn/drop/fail differs from quarantine and dataset-level uniqueness/reconciliation. Fail does not produce warn/drop tracking metrics and does not establish cross-table rollback. Code, data and platform tests remain separate acceptance layers.

CLI1.20.0 has plan/schema/lifecycle commands and direct deployment engine. Bundle state identity and output namespace isolation are separate. GitHub federation must match exact issuer/audience/subject, including newer immutable repository ID formats; protected-environment settings require administrative evidence outside YAML.

The authored course release is a synthetic sandbox full snapshot, not a live ROAS connector. Local plan/layout/quality/recovery evidence and CLI schema validation are recorded separately from pending strict target validation/deployment/Job execution. No account creation, credentials, profiles, system queries, managed expectation metrics or Actions run occurred.

## Platform research synthesis

Kind: descriptive/reference/runbook | Audience: Data Engineer with accepted Spark/Delta/streaming foundation and Airflow/BigQuery/dbt experience | Purpose: design Databricks platform boundaries and execute optional bounded learning labs | Non-goals: account automation, cloud credentials, production networking/scale, production CI/CD rollout.

Research question, known baseline and stopping rule are recorded in .researches/platform-plan.md. Current official sources support a composition of compute, Jobs orchestration, SDP/Lakeflow dataset processing, Unity Catalog governance and SQL serving. Free Edition offers a quota-limited optional learning path; it does not establish enterprise or production behavior.

Terminology finding: Lakeflow Jobs remains workflow orchestration; Lakeflow pipelines is the current managed product built on Apache Spark Declarative Pipelines and running on Databricks Runtime. Expectations, AUTO CDC and managed event-log capabilities need platform qualification. Local Spark4.0.4 has no claimed SDP execution.

Two source conflicts are explicit in SOURCES.md: generic JAR compute recommendations versus task-specific serverless support, and legacy target examples versus the preferred schema pipeline property. Specific current official docs control sample decisions. Airflow, dbt and BigQuery comparisons use each vendor's primary documentation.

Archive .researches/2026-10-11-platform contains 33 dual HTML/text fetched records, raw discovery output and consolidated URL-deduplicated findings. Auth/parameter/serverless supplement contains four records. Publication remains disabled. Gaps: actual Free Edition feature inventory, CLI strict validation, Jobs run/repair, inferred pipeline graph/expectation failure, effective UC identities/grants and SQL warehouse/history. All are PENDING USER WORKSPACE.

Repository assessment: chỉ có tám installed skills, policy/provenance documents, research scripts và tsx runner. Không có `.git`, remote, website framework, curriculum, course content hoặc Pages config tại thời điểm bắt đầu. Work hiện có được giữ; không tạo Git repository, push hoặc thay visibility.

## Research boundary

Research question: tên hiện hành và các boundary kiến trúc nào phải được xác minh để Chapter 00 không dạy sai mental model? Known context: reader có Python/SQL/BigQuery/Airflow/dbt experience; website chỉ triển khai Iteration 1. Stopping rule: official source cho mỗi thuật ngữ và core claim, cùng executable example cho scenario local.

Working notes cho writing: Kind: descriptive/reference | Audience: production Data Engineer chuyển sang Databricks | Purpose: phân biệt trách nhiệm platform/compute/table/file/storage và chọn bước học tiếp | Non-goals: benchmark vendor, full course, cloud provisioning hoặc solution capstone.

[SOURCES.md](SOURCES.md) owns source URLs, retrieval date, cloud context và terminology. Evidence archive: `.researches/2026-10-10T010000Z/`. Có 22 fetched sources: official docs và một presentation reference. Research scripts consolidate với `--no-publish`; không có commit/push.

## Presentation reference

[Reference Terraform page](https://vudaian24.github.io/learn-devops/07-terraform.html) có course navigation, section TOC, các mục đánh số, compact command/concept tables, code ngắn và operational notes. Source HTML có desktop TOC cố định và breakpoint đưa TOC về document flow. Reference được đọc từ fetched HTML/text vì web-reader ban đầu không fetch được trang.

Handbook giữ tinh thần tra nhanh nhưng dùng VitePress sidebar + per-page TOC, metadata header và checkpoint theo competency. Không copy HTML, CSS, colors hoặc Terraform content. Typography/code/tables là trọng tâm; không dùng marketing hero, analytics hoặc imagery trang trí.

## Framework decision

**VitePress 1.6.4** được chọn, version từ npm registry kiểm tra 2026-10-10. Nó đáp ứng Markdown-first, static Pages, sidebar/TOC, Shiki highlighting, copy code, local search, theme và responsive navigation. Giữ package lock để build reproducible.

| Lựa chọn | Benefit | Cost / decision |
|---|---|---|
| VitePress | Markdown + docs theme có sẵn; ít custom UI | Cần client Mermaid component; phù hợp repository Node hiện có |
| MkDocs | Python-first và docs ecosystem | Thêm Python website toolchain bên cạnh Node; không có framework cũ cần giữ |
| Docusaurus | Versioning/i18n/plugin ecosystem rộng | Nhiều configuration/runtime hơn nhu cầu Iteration 1 |
| Custom React/Next app | Toàn quyền frontend | Tự xây docs behaviors làm tăng maintenance; không có requirement cần nó |

Dependencies bổ sung có mục đích: VitePress cho site, Mermaid 12.1.0 cho diagrams, Playwright 1.64.0 cho desktop/mobile QA. Dùng Chrome có sẵn trên Windows; workflow CI cài Chromium của Playwright. Không cài thêm Agent Skills, PySpark, Java hay Databricks CLI. Sites skill được đọc cho local preview workflow; GitHub Pages là target do user chỉ định, nên không đăng ký/publish một Site khác.

## Learning dependency decisions

Không có CURRICULUM.md cũ để reconcile. Curriculum mới bao phủ các nhóm người dùng yêu cầu nhưng đưa grain/keys/fan-out vào Foundation trước Spark. Partitioning/shuffle precede joins/performance; Delta precedes incremental correctness; event time/lookback precede watermarks/state; platform và production precede interoperability/capstone.

Medallion xuất hiện trong mental model/lộ trình và được học sâu sau Delta. Iceberg awareness ở Chapter 00 để phân biệt table format; feature comparison được deferred tới nhóm interoperability. System design vendor comparisons cần official research khi viết, không tạo content dựa trên memory.

## Current-term findings

Tên pipeline cần qualifier: Apache Spark SDP và Lakeflow pipelines không cùng feature surface. AWS architecture cũng có classic/serverless/default-storage distinctions. BigQuery tách storage/compute, nên Chapter 00 không dùng separation như khác biệt độc quyền. Iceberg support có managed/foreign modes và limits. Đây là các guardrails cho nội dung; [Sources](SOURCES.md) là owner của evidence chi tiết.

## Iteration 2 working notes

Kind: descriptive/reference | Audience: production Data Engineer có BigQuery/Airflow/dbt experience | Purpose: diagnose join cardinality, choose an operating model, and distinguish Spark source code from execution | Non-goals: performance tuning, full Spark setup, platform deployment or capstone solution.

Research question: grain/key guarantees, current warehouse/lakehouse boundaries and Spark execution concepts nào ảnh hưởng trực tiếp tới production reasoning? Known evidence: accepted Chapter 00; Python 3.12 available; PySpark not installed; `Get-Command java` found no executable on PATH. Stopping rule: primary source cho từng core claim; hai vendor perspectives cho comparison; executable deterministic examples cho metrics.

Nineteen selected official sources được lưu tại `.researches/2026-10-10T020000Z/`. Microsoft star-schema guidance bổ sung modeling context; không dùng Power BI relationship behavior làm SQL engine semantics. Spark upstream `latest` tự nhận version 4.2.0 ở lần retrieval; không đồng nhất với Databricks Runtime. BigQuery pricing page được archive bằng urllib sau khi web reader không đọc được; không đưa dollar rates vào handbook.

Decision: không thêm PySpark/JDK. Full local Spark cần JVM và runtime chưa có trong environment; website dependency graph không cần chúng. Lab 03 dùng SQLite để kiểm chứng relational output và một deferred-query model được ghi rõ giới hạn. Spark API fragment là reading example dựa trên official docs, không được báo cáo như Spark runtime đã chạy. Chi phí của lựa chọn này là chưa có measured Spark UI/job/stage evidence; phải bổ sung trước các lab performance. Lab 01 và 02 cũng chỉ dùng Python standard library.

## Iteration 5 working notes

Kind: descriptive/how-to/reference/runbook. Audience: Middle Data Engineer with Python/SQL/BigQuery/Airflow and Chapters00-15. Purpose: design and verify continuous, stateful, restartable processing across source/engine/sink boundaries. Non-goals: website redesign, Kafka implementation, real workspace/cloud operations, platform orchestration, production throughput benchmarks.

Research question: what are current Spark4.0.4 and Databricks checkpoint compatibility, watermark/dedup/join/output-mode and foreachBatch guarantees, and which can be reproduced locally? Known: accepted Spark4.0.4, Delta4.0.1, Java17 and batch correctness evidence. Stopping rule: version-qualified primary docs for each restriction plus actual controlled-input streaming tests; separate unsupported platform behavior from local observations.

Safe assumptions: synthetic ROAS requirements (15-minute freshness,2h event arrival lateness,72h mutable attribution); UTC and integerUSD cents; file discovery is a deterministic source substitute, not a webhook/API guarantee. Callback Bronze must preserve replayable delivery data; state-bounded processing does not replace historical correction/reconciliation. Queries use bounded toy data, explicit schemas and isolated checkpoints/targets. Recovery tests stop/restart or inject sink-boundary exceptions honestly; no process-kill guarantee inferred.

## Iteration 4 working notes

Research result (verified2026-10-11): nine current primary sources archived and consolidated in .researches/2026-10-10T180000Z with no publication. Medallion describes progressive quality responsibilities. MERGE needs source uniqueness and explicit state semantics; Databricks duplicate-detection conditions depend on DBR version, so OSS4.0.1 behavior was executed directly. Source duplicate matching update failed without new commit; unmatched duplicate inserts produced two rows unless preprocessed. Schema policy fixed/explicit, no auto evolution; existingDelta08 schema rejection rechecked. replaceWhere supports scoped atomic replacement, not cross-table/cursor transaction or business same-scope coordination. Streaming watermark is event-time/state policy, not historical retrieval. Within-delay guarantees are operator-dependent; outside-delay processing is not universally always-drop.

Decision: model source APIs, UTC and integerUSD cents; actual Delta sink tests for11/12/14/15. Source revisions order state, delivery channel excluded from identity, ambiguous equal revisions rejected.72h/15min assumptions need source-specific guarantees before deployment. Local bounded backfill/retry faults use Python exceptions and sequential live interleaving, not process-kill or simultaneous-writer proof.

Kind: descriptive/how-to/reference. Audience: Mid Data Engineer có SQL, grain và Delta fundamentals. Purpose: thiết kế và kiểm chứng ROAS state đúng khi retry, replay, mutable updates, late arrival và bounded backfill. Non-goals: streaming/orchestration implementation, cloud deployment, production benchmarks.

Research question: current Delta/Databricks MERGE xử lý ambiguous source matches thế nào, medallion xác định quality responsibilities ra sao, và streaming watermark khác batch cursor/lookback thế nào? Known evidence: accepted Spark4.0.4/Delta4.0.1 image pin; existing integration labs and static site. Stopping rule: official primary source cho từng version-sensitive claim; executable business-state tests cho fixtures, không extrapolate actual API guarantees từ synthetic source.

Design assumption: sample money là integer USD cents, timezone UTC; Adjust delivery channel không phải business identity. Silver event-state grain là (source_system, app_id, event_id), ordered by source revision; equal-revision payload conflicts reject. Advertising cost grain là (date, platform, account_id, app_id, campaign_id, currency). Fifteen-minute freshness và72h mutable attribution là scenario assumptions do learner phải validate với source owner.

## Iteration 3 working notes

Kind: explanatory/how-to/reference. Audience: Mid Data Engineer chuyển từ BigQuery/Airflow. Purpose: kiểm chứng Spark execution, partition distribution, join correctness và storage semantics bằng runtime local. Non-goals: benchmark, cluster sizing, cloud deployment, MERGE/idempotency implementation.

Research question: operator nào tạo Exchange, partition nào chứa hot key, Parquet reader bỏ cột/lọc bằng metadata ra sao, và Delta log xác định snapshot thế nào? Known evidence: host Python 3.12.10; thiếu JDK/PySpark; Docker Desktop có sẵn; official Apache Spark 4.0.4 image chạy DataFrame/SQL/Parquet và shutdown thành công. Stopping rule: official versioned source cho mỗi core claim; actual output cho mỗi lab invariant; không suy diễn latency/network/spill từ tiny local fixtures.

Decision: dùng Docker Linux image chính thức, khóa digest trong `runtime/spark.json`, không sửa Java/Python toàn hệ thống hoặc tải winutils không rõ nguồn. Spark local[*] được giới hạn 2 CPU/4 GiB container; AQE tắt trong diagnostic labs để thấy plan ổn định, không phải khuyến nghị production. Delta 4.0.1 được thử riêng theo compatibility matrix; chỉ công bố executable lab nếu dependency resolution và tests thực sự pass.

Outcome: clean official Maven resolution và Delta create/append/UPDATE/history/time-travel/schema contracts pass, nên executable08 được giữ. Native host setup không cần thiết. Local evidence và constraints do docs/labs/runtime-evidence.md / PROGRESS.md sở hữu; không suy broadcast speedup, real network cost hoặc concurrent writer guarantees từ fixture. Research session090000Z archives23 official sources, gồm pinned raw protocol/WebUI source để tránh GitHub navigation text làm evidence chính.

## Streaming research findings

Twelve official pages were archived as HTML and extracted Markdown under `.researches/2026-10-11T034500Z/`. Search records and consolidation retain resolved source URLs. The local adapter used `--no-publish`; no remote publication occurred.

The Spark4.0.4 recovery rules explicitly restrict grouping/aggregate schemas, dedup columns and stream-stream equi-join keys/types. Current DBR pages include version-scoped source evolution and state repartitioning exceptions; the course keeps these separate from local OSS guarantees. Watermark guarantees are one-sided and effective progress crosses batch boundaries. Outer results depend on input/event-time progress, not a fixed wall-clock timer.

Delta foreachBatch idempotent-write guidance requires a new app ID when a new checkpoint resets batch IDs; this avoids false skips but does not make business replay safe by itself. The production design still needs durable identity/version semantics and reconciliation. Research stopping rule is met for the source-sensitive claims; local proofs are recorded by the executable suite and evidence manifest after verification.
