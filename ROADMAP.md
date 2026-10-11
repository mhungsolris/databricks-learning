# Repository roadmap

Iteration 1 establishes website infrastructure, a polished Foundation chapter and one FREE lab. Full curriculum generation is deferred.

Chapters 01–03 và portable Labs 01–03 thuộc Iteration 2. Iteration 3 thêm real Spark03–07, Delta08 và Chapters04–08; platform/visual architecture được giữ nguyên. PROGRESS.md ghi actual verification và giới hạn local evidence.

| Iteration | Scope | Exit evidence |
|---|---|---|
| 1 | VitePress, IA, homepage, Chapter 00, template, local lab, Pages config | Production build, links/anchors, lab tests, browser/navigation/Mermaid checks |
| 2 | Grain/keys/fan-out; lake/warehouse/lakehouse BigQuery bridge; Spark architecture/DataFrames | Scenario datasets, executable examples, chapter gates and current sources |
| 3 | Spark partitioning/shuffle/joins, rồi Parquet và Delta Lake fundamentals | Runtime assessment trước measured labs; partition/plan evidence, file/table boundaries và tiny correctness experiments |
| 4 | Chapters09–15: Medallion → incremental → idempotency → MERGE → time → late data → backfill; Mid Gate | Exact Delta replay/update states, ambiguity failure, reconciliation và37/53-day resume evidence |
| 5 | Structured Streaming → state → checkpoints → watermarks → delivery semantics → recovery | Dựa09–15/Mid Gate; source/sink guarantees và bounded checkpoint/failure labs trước platform orchestration |
| 6 | Chapters25-30: Compute → Jobs → SDP/Lakeflow pipelines → UC → SQL → platform boundaries; Platform Design gate | Docs/config/local SQL verified separately from pending workspace runs |
| 7 | Performance Engineering → observability → quality → testing → CI/CD → production Declarative Automation Bundles | Chapters31-45, real local plans/layout/quality/restore, portable tests, CLI schema and two gates; cloud acceptance pending |

| 8 | Iceberg semantics, catalogs/evolution, format interoperability, platform judgment and four cases | Local Iceberg plus source/architecture evidence; verification recorded in PROGRESS.md |
| 9 (proposed) | ROAS requirements → architecture → implementation → failure injection → runbook → final assessments/interview/certification/site QA | Depends on all correctness, production and architecture gates; not started |

`CURRICULUM.md` owns dependency order and competencies. `PROGRESS.md` owns implementation review status. Các iterations sau là đề xuất, chưa cam kết lịch hoặc generated content.

## Publish boundary

Pages workflow đã được author trong repository. Để publish cần Git repository/remote, GitHub Pages bật GitHub Actions, branch main và quyền deployment. Không thể xác nhận deployment live từ config local; không push hoặc thay visibility trong Iteration 1.
