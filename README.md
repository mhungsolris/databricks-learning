# Databricks learning handbook

## Architecture judgment

[Chapters46-60](docs/iceberg/46-why-iceberg.md) cover Iceberg semantics, catalogs, interoperability and scenario-driven platform choices. [Iceberg setup](docs/setup/local-iceberg.md), [local evidence](docs/labs/iceberg-evidence.md), [support ledger](docs/iceberg/current-platform-support.md) and two [ADRs](docs/adr/ADR-002-platform-choice.md) separate execution, official capabilities and architecture judgment. No cloud operation is required. Run python scripts/verify_iceberg.py, python scripts/test_iceberg.py and python scripts/check_iceberg_evidence.py from the repository root.

## Production hardening

[Chapters31-45](docs/production/31-performance-mental-model.md) add performance investigation, observability, quality, testing, CI/CD and release safety. [Production evidence](docs/labs/production-evidence.md) owns reproduction commands and local/cloud limits. [ROAS sandbox bundle](labs/production/README.md) has dev/staging/prod examples and a manual OIDC workflow; strict workspace validation, deployment and execution remain PENDING USER WORKSPACE. No website redesign or production source connector was introduced.

Run portable pytest in the isolated test venv, scripts/test_production.py for actual Spark/Delta experiments and scripts/check_production_config.py for course config contracts. The build checks selected evidence against startup source hashes. CLI schema validation is separate from workspace validation.


Technical handbook, learning path và local-first labs cho Data Engineer đã có Python, SQL, BigQuery, Airflow và dbt experience. Chapters 00-60, portable foundation/platform artifacts, real Spark/Delta/streaming labs và sáu Mid Gates có nội dung. [Learning path](CURRICULUM.md) sở hữu dependency order.

## Run locally

Yêu cầu Node **24.x**, npm và Python **3.10+**; CI dùng Python 3.12. Không cần Databricks workspace, Java, Spark hoặc cloud token cho site và portable Labs 00-03.

```sh
npm ci --ignore-scripts
npm run docs:dev
```

Trên PowerShell máy này dùng `npm.cmd` thay `npm` để tránh execution policy của npm.ps1. Mở URL Local do VitePress in ra; base mặc định là `/Databricks-learning/`, ví dụ `http://localhost:5173/Databricks-learning/`.

Production build và preview:

```sh
npm run docs:check
npm run docs:build
npm run docs:preview
```

Build output: `docs/.vitepress/dist/`. `docs:build` gồm VitePress dead-link validation và kiểm tra links/anchors trên HTML output.

## Validate

```sh
python labs/foundations/files_and_tables.py
python -m scripts.run_labs
python -m unittest discover -s tests -v
npm run docs:test-ui
python scripts/verify_skills.py
```

`python -m scripts.run_labs` chạy bốn portable labs và thử submit SQL sai/đúng cho Lab 01. Lab 03 giữ SQLite/deferred-query model và thêm real Spark variant. [Local Spark setup](docs/setup/local-spark.md) sở hữu prerequisites, image pin, Windows troubleshooting, optional UI và shutdown. Docker Linux containers chạy JVM/PySpark, host Python chỉ dispatch; website dependencies không đổi.

```sh
python scripts/verify_spark.py
python scripts/run_spark.py --lab all
python scripts/run_spark.py --lab 08
python scripts/test_spark.py
python scripts/test_spark.py --delta
python scripts/run_correctness.py --lab all
python scripts/test_correctness.py
python scripts/run_streaming.py --lab all
python scripts/test_streaming.py
python scripts/test_platform.py
```

`all` chạy03-07; Delta08 opt-in, Maven dependencies pinned. [Runtime evidence](docs/labs/runtime-evidence.md) có selected actual outputs/plans/logs. Không có performance benchmark hoặc cloud/workspace setup.

Correctness runner có Labs09–15:09/10/13 là deterministic models;11/12/14/15 có actual Delta writes/history. [Correctness evidence](docs/labs/correctness-evidence.md) giải thích selected states/hashes/reconciliation. Money integer USD cents, UTC và ordered source revisions là fixture contracts, không phải guarantees của Ads APIs. [Mid Gate](docs/assessments/mid-gate-pipeline-correctness.md) có input/questions. Reviewer solutions được giữ local trong ignored `reviewer/`, không đưa vào GitHub repository hoặc site. Build kiểm không leak reviewer marker.

Browser test cần production build. Windows dùng Chrome tại standard Program Files path nếu có; Linux/macOS dùng Chromium của Playwright. Khi chưa có browser, chạy `npx --no-install playwright install chromium` theo nhu cầu. Không tải browser trong npm install. CI dùng `playwright install --with-deps chromium`.

UI script tự mở preview port 4173, chụp screenshots trong ignored `.skills-test/screenshots/`, rồi đóng browser/server. Nó kiểm tra search, dark/light, pager, desktop/mobile navigation, JS errors và Mermaid. Port 4173 phải trống; nếu bạn đã mở preview ở port này, dừng preview trước khi chạy test.

## Streaming labs

Labs16-24 execute actual local micro-batch queries with controlled file arrivals. [Streaming evidence](docs/labs/streaming-evidence.md) records progress, state/checkpoint inventories, exact target hashes and sink/schema failures. [Streaming Mid Gate](docs/assessments/mid-gate-streaming-correctness.md) uses a separate ROAS fixture and causal rubric; reviewer material stays outside the site.

`python scripts/test_streaming.py` checks all nine contracts; `python scripts/run_streaming.py --lab 19` runs one teaching exercise. Restart uses real checkpoints; process kill, remote APIs and cloud corruption are not reproduced. [Streaming audit](STREAMING_AUDIT.md) owns the conceptual review and execution limitations.

## Platform learning path

Chapters25-30 teach compute, Lakeflow Jobs, Apache Spark Declarative Pipelines/Lakeflow pipelines, Unity Catalog, SQL serving and platform boundaries. [Free Edition setup](docs/setup/databricks-free-edition.md) is optional. [Platform evidence](docs/labs/platform-evidence.md) separates portable/config checks, actual local SQL and workspace runs. [Platform Design gate](docs/assessments/mid-gate-platform-design.md) rewards boundary reasoning, including valid hybrid Airflow/dbt designs.

Artifacts in labs/platform contain a bounded ROAS Job DAG, batch medallion source, governance design fixture and SQL examples. Databricks CLI strict validation, deployment and workspace run evidence remain PENDING USER WORKSPACE. No credentials, account creation or authenticated operations are configured.

## Project base and repository links

Default project path: `/Databricks-learning/`. Override bằng `DOCS_BASE` nếu repo có tên khác hoặc dùng root hosting; giá trị phải có `/` ở đầu/cuối.

```powershell
$env:DOCS_BASE = '/my-repo/'
npm.cmd run docs:build
npm.cmd run docs:preview
```

```sh
DOCS_BASE=/my-repo/ npm run docs:build
```

GitHub Actions derives the base from the actual repository name, including `.github.io` root repositories. `SITE_ORIGIN` supplies the origin for Open Graph URLs. `GITHUB_REPOSITORY` adds real edit/source links during GitHub builds; local builds omit them because this workspace has no remote. No fictitious GitHub owner is configured. Custom domains require intentional `DOCS_BASE=/` and `SITE_ORIGIN=https://your-domain` workflow overrides.

## GitHub Pages

[`.github/workflows/pages.yml`](.github/workflows/pages.yml) runs documentation, portable tests, browser QA and Spark/Delta/Iceberg checks on main pushes and PRs. PRs validate without deployment. A push to `main`, or a manual run on `main`, uploads the static artifact and deploys only after both build and runtime jobs succeed. Deployment uses Pages/id-token permissions and the `github-pages` environment.

After placing this work in a GitHub repository, choose **Settings → Pages → Build and deployment → Source: GitHub Actions** and ensure the default branch matches `main`. Then push only when authorized. No PAT or credential belongs in source; deployment uses GitHub's workflow identity.

Repository: [mhungsolris/databricks-learning](https://github.com/mhungsolris/databricks-learning). The project URL after a successful Pages deployment is `https://mhungsolris.github.io/databricks-learning/`. A configured workflow alone does not establish a successful deployment; verify its Actions result and live URL. This workflow does not deploy Databricks resources. The separate ROAS sandbox release workflow requires an explicit manual run and workspace configuration.

## Repository map

| Path | Purpose |
|---|---|
| `docs/` | Published teaching pages and VitePress theme/config |
| `labs/` | Executable exercises, separate from teaching prose |
| `templates/chapter.md` | Authoring schema for future major chapters |
| `scripts/` | Research, integrity, build-link and browser checks |
| `tests/` | Lab correctness/failure contract tests |
| `.researches/` | Source snapshots and consolidation evidence |
| `.agents/skills/` | Existing pinned Agent Skills |

Planning and evidence: [CURRICULUM.md](CURRICULUM.md), [RESEARCH.md](RESEARCH.md), [ROADMAP.md](ROADMAP.md), [SOURCES.md](SOURCES.md), [PROGRESS.md](PROGRESS.md). Agent instructions and skill stack: [AGENTS.md](AGENTS.md), [SKILLS.md](SKILLS.md), [SKILLS_LOCK.md](SKILLS_LOCK.md), [SKILLS_VERIFICATION.md](SKILLS_VERIFICATION.md).

## Extend the handbook

Load only task-relevant skills. Write a scenario first, use concrete input/output, qualify current vendor claims and check official sources. Follow `templates/chapter.md`; Chapter 00 is the content example. Keep future sidebar entries pointing to the curriculum until the actual chapter passes review. Update source evidence and progress with each chapter; do not mark content complete on build success alone.
