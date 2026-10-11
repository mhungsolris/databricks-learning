# Repository content progress

## Iteration 9 assessment entry, 2026-10-11

Iteration 9 is INCOMPLETE. The capstone entry at docs/capstone/index.md presents the requirements interview and its rubric. It pauses for the learner's first submission before modeling, architecture or implementation. No learner response, score, capstone runtime result or final competency outcome exists yet. Capstone and Final Mid Gate are NOT YET; capstone workspace evidence is PENDING. Version 1.0 is not recommended or tagged.

Fresh working-tree checks for this documentation/navigation change: npm.cmd run docs:check passes61chapter schemas and146Markdown pages; npm.cmd run docs:build passes147HTML pages,35392internal references with0failures,624privacy-scanned artifacts and all five existing runtime evidence guards. npm.cmd run docs:test-ui passes existing chapter/diagram/search/theme routes and additional capstone sidebar, content and mobile-overflow checks. The capstone mobile screenshot is retained under the ignored .skills-test directory. These checks validate the assessment entry, not completion of Iteration9 or learner competence.

## Current capability evidence

| Capability | Docs | Local evidence | Databricks evidence |
|---|---|---|---|
| Spark | yes, Chapters03-07 | Actual Spark4.0.4 runtime/tests and stages | PENDING USER WORKSPACE; no DBR execution |
| Delta | yes, Chapters08-15 | Actual Delta4.0.1 writes/history/correctness tests | PENDING USER WORKSPACE |
| Structured Streaming | yes, Chapters16-24 | Nine actual state/checkpoint/retry/recovery contracts | PENDING USER WORKSPACE |
| Compute | yes, Chapter25 | Classification exercise; no managed-compute execution | PENDING USER WORKSPACE |
| Jobs | yes, Chapter26 | PORTABLE TEST DAG/config; n/a local Jobs scheduler | PENDING USER WORKSPACE; strict CLI/run/repair not executed |
| SDP / Lakeflow pipelines | yes, Chapter27 | AST/source graph and underlying SQL; no local SDP engine | PENDING USER WORKSPACE; inferred graph/update/expectation not executed |
| Unity Catalog | yes, Chapter28 | PORTABLE TEST policy fixture; n/a local UC enforcement | PENDING USER WORKSPACE; enterprise identity/IAM tests deferred |
| Databricks SQL | yes, Chapter29 | Actual SELECT semantics; no local SQL warehouse | PENDING USER WORKSPACE; warehouse/history not executed |
| Platform boundaries | yes, Chapter30 and Platform Design gate | Architecture exercise/rubric | Production acceptance pending |
| Production engineering | Chapters31-45 and two further gates | Plans/AQE, skew, file layout, quality, tests, candidate barrier and local RESTORE; CLI schema | PENDING USER WORKSPACE; Photon/layout automation/observability/deploy acceptance |

Documentation coverage does not establish platform experience. The current repository has no selected Databricks workspace/profile or authenticated CLI; a checksum-verified repository-local CLI1.20.0 was used only for schema/help checks. Evidence is from the local working tree; no Git commit, Actions run or live Pages deployment is claimed.

This file tracks reviewed repository artifacts, not reader progress. “Verified” requires written content, sourced claims, checked examples/links, production build, template review and relevant browser QA.

| Artifact | Status | Evidence |
|---|---|---|
| IA, learning path and framework decision | Reviewed for Iteration 1 | CURRICULUM.md, RESEARCH.md; dependencies and competency labels |
| Homepage and navigation | Verified locally | Desktop/mobile navigation, search, pager and guide routes |
| Chapter 00 | Verified for Iteration 1 | All 17 template sections, official-source review, 650/350 example, build/link/browser checks |
| Lab 00 | Executed; tests passing | 650/350 fixture; retained-file and missing-active-file tests |
| Chapter template and components | Verified locally | Metadata header, three Mermaid diagrams, light/dark rendering, code controls |
| GitHub Pages configuration | Authored; not deployed | Workflow only, no Git remote/run |
| Chapter 01 | Verified for Iteration 2 | Grain/key contracts, fan-out, detail grain/allocation, executable query submission and failure tests |
| Chapter 02 | Verified for Iteration 2 | Operating model comparison, non-1:1 bridges, source review and schema failure lab |
| Chapter 03 | Verified, real variant added | SQLite conceptual model retained; matching real Spark fixture, logical/physical plans, scheduler/event logs and Parquet output |
| Labs 01-03 | Verified locally | Deterministic standard-library labs, failure drills and tests |
| Chapters 04-08 | Verified for Iteration 3 | 17 template sections + interview articulation, actual Spark/Parquet/Delta artifacts, dependencies and browser QA |
| Spark local runtime / Labs 03-07 | Executed and verified | Pinned official Docker image, Spark4.0.4/local[*], metadata/plans/job/stage evidence, clean shutdown |
| Delta Lab08 | Executed and verified | Delta4.0.1, create/append/UPDATE/v0 read/schema rejection, three actual commit logs |
| Chapters09–15 / correctness labs / Mid Gate | Verified locally for Iteration4 | 17 sections + interview/dependencies, business invariants, actual Delta histories, build/UI/private-material/integrity checks |
| Chapters16-24 / streaming labs / Mid Gate | Verified locally for Iteration5 | Nine actual Spark/Delta contracts, checkpoint/state/retry evidence, build/UI/source and integrity checks |
| Chapters25-30 / platform artifacts / Mid Gate | Verified local docs/artifacts/SQL/build/UI; cloud pending | 44 portable tests, six actual Spark SQL tests, 33 diagram/browser checks; workspace PENDING USER WORKSPACE |
| Chapters31-45 / production labs / two gates | Verified local docs/runtime/static/schema/build/UI; cloud pending | Performance/quality/rollback evidence, test pyramid, sandbox DABs/OIDC release and readiness rubric |
| Chapters46-60 / Iceberg / architecture gate | Verified local runtime/docs/source/build/UI; cloud pending |7Iceberg contracts,metadata/evolution/mutation proof,ADRs,four cases and requirement-driven platform choice |
| Capstone extension | Bounded ROAS sandbox code/bundle; workspace pending | Synthetic callback/cost snapshots, staging/reconciliation/publication; full source connectors and production acceptance remain pending |

## Iteration 1 verification record

Executed on **2026-10-10**, Windows, Node 24.18.0, npm 11.16.0, Python 3.12 and installed Chrome:

| Command | Actual result |
|---|---|
| `npm.cmd ci --ignore-scripts --no-fund --no-audit` | Reinstalled 249 packages from the lockfile successfully |
| `npm.cmd run docs:check` | Chapter schema and seven authored Markdown pages passed |
| `python -m unittest discover -s tests -v` | Two tests passed: retained historical files and missing active file |
| `python labs/foundations/files_and_tables.py` | Glob 650; active snapshot 350; invariant passed |
| `npm.cmd run docs:build` | Production build succeeded in 25.29s; eight HTML pages including 404; 473 internal references, zero failures |
| `npm.cmd run docs:test-ui` | Desktop 1440px/mobile 390px, real sidebar/pager navigation, local search, light/dark, code controls, three Mermaid diagrams and guide routes passed; no browser JS/local HTTP failures |
| `python scripts/verify_skills.py` | Eight installed skills passed; zero failures; existing optional sibling references remain documented |

Screenshots were visually inspected for desktop, mobile navigation, diagram labels and dark theme. Browser evidence is in ignored `.skills-test/screenshots/`; the browser check closes its own preview server. Research evidence has 22 fetched source records under `.researches/2026-10-10T010000Z/`.

Boundaries: external sources were retrieved during research; the build checker validates internal links, not continuous availability of external sites. GitHub Actions and live Pages deployment have not run. No Databricks workspace operation or Spark/Delta engine integration is claimed by the standard-library lab. No completion percentage is published on the website.

## Iteration 2 verification record

Executed **2026-10-10** against the local working tree. Workspace still has no `.git`, so evidence is not claimed against a commit. No new npm/Python dependencies or skills were installed.

| Command | Actual result |
|---|---|
| `npm.cmd ci --ignore-scripts --no-fund --no-audit` | Initial Windows EPERM on locked Rollup file; after pausing the matching project dev server, reinstalled 249 packages successfully in 12s; dev server restored at 127.0.0.1:5173 |
| `npm.cmd run docs:check` | Four major chapter schemas, 13 authored Markdown pages passed |
| `python -m unittest discover -s tests -v` | 13 tests passed: two baseline and 11 new contract tests |
| `python -m scripts.run_labs` | Four portable labs passed; submitted wrong SQL rejected and fixed SQL accepted; schema baseline (3,350); pipeline A/VN 300, B/US 50 |
| `npm.cmd run docs:build` | Production build succeeded in 31.49s; 14 HTML pages including 404; 984 internal references, zero failures |
| `npm.cmd run docs:test-ui` | Baseline + three new chapter/lab routes passed on desktop/mobile; six Mermaid diagrams, both themes, two search queries, sidebar/pagers/code controls, no JS/local HTTP failures |
| `python scripts/verify_skills.py` | Eight skills passed, zero failures; optional sibling links unchanged |
| `python scripts/smoke_skills.py` | Research archival/consolidation and publication controls passed; zero failures |
| Python AST parse of fenced Python examples in `docs/` | Two snippets passed syntax validation; not Spark execution evidence |
| `npm.cmd ls --depth=0` | Existing four pinned dependencies intact |

Browser script waits for route headings as well as URL changes; URL update alone preceded Vue content update in an initial assertion. Desktop/mobile screenshots and all three new diagrams were visually inspected. Evidence remains under ignored `.skills-test/screenshots/`. Research archive has 19 fetched official-source records, HTML/text and consolidated Markdown/JSON in `.researches/2026-10-10T020000Z/`.

## Senior Data Engineer self-review

| Review question | Finding / concrete treatment |
|---|---|
| Concepts useful in production? | Key scope, coverage, conservation and writer/consumer ownership attached to specific failures; no claims that ACID or surrogate IDs fix business duplicates |
| Precise terminology understandable? | Spark job versus orchestration job, logical DAG versus scheduler stages, and warehouse/lakehouse operating models explained using the same concrete pipeline |
| Duplicates Chapter 00? | Chapter 02 links layer topology to 00 and instead owns migration/cost/consumer decisions; Lab 02 adds schema/key gates beyond Lab 00 membership |
| Prose better expressed as data/table/diagram? | Joined-row table, 2×3 detail-grain example, three focused diagrams and debugging/comparison tables make claims inspectable |
| Labs prove concepts? | Lab 01 accepts learner SQL and rejects wrong report; tests exercise equal-valued costs, missing coverage, detail grain and allocation. Lab 02 fails on schema/key changes. Lab 03 proves relational output only, explicitly excludes Spark scheduler claims |
| Useful to a Middle interview? | Each chapter has five or six scenario questions and observable PASS/NOT YET conditions, requiring evidence and trade-offs |

Known debt: no local Spark JVM/PySpark execution, actual Spark UI counts, distributed recovery or measured performance. Resolve runtime setup before claiming measured partition/shuffle/performance labs. GitHub Actions/Pages remain authored but unexecuted; no cloud resource, push or publication occurred. Work stops after Iteration 2.

## Iteration 3 verification record

Executed **2026-10-10** against local working tree. Prior iteration records above remain historical. No `.git`, commit, push, live Pages deployment or Databricks workspace operation. npm dependencies/visual theme/skills unchanged. Docker Desktop was already installed, started for this task; host JDK/PySpark still absent. Official Linux image runs Spark4.0.4, Python3.10.12, Java17.0.19 under pinned digest in runtime/spark.json. Host Python3.12.10 dispatches the container.

| Command / check | Actual result |
|---|---|
| Docker inspect / info | Official image digest locked; Linux backend available, 8 visible cores and about8 GiB backend memory |
| `npm.cmd ci --ignore-scripts --no-fund --no-audit` | 249 packages reinstalled; matching project dev server paused first, restored afterward |
| `python scripts/verify_spark.py` | Spark4.0.4/local[*], DataFrame5, SQL45, Parquet10; 8 completed stages; clean shutdown |
| `python scripts/run_spark.py --lab all` | Real03-07 passed; 71 completed stages in selected run; Lab03 paid/lookup/aggregate/Parquet report matches A/VN300,B/US50 |
| `python scripts/run_spark.py --lab 05` | Per-query jobs/stage IDs captured: narrow1/1, aggregate1/2, order2/3, join1/3; output ordering asserted; 10 completed stages for whole run including additional validation |
| `python scripts/run_spark.py --lab 08` | Delta Maven resolve clean; v0 create/v1 append/v2UPDATE; old/current rows correct; incompatible schema rejected withoutv3; 21 completed stages |
| `python scripts/test_spark.py` | 5 integration tests passed, including subtests03-07 and adversarial empty partitions, many-to-many and empty Parquet; final suite68.646s, 85 completed stages |
| `python scripts/test_spark.py --delta` | 5 integration tests passed, including Delta mutation/history/schema contracts; final suite84.571s, 35 completed stages |
| `python -m unittest discover -s tests -v` | Existing13 portable tests passed |
| `python -m scripts.run_labs` | Four portable labs and wrong/fixed SQL submission checks passed |
| `npm.cmd run docs:check` | 9 major chapter schemas, 25 authored Markdown pages, explicit interview section04-08 passed |
| `npm.cmd run docs:build` | VitePress build29.93s; 26 HTML pages, 2278 internal references, zero failures |
| `npm.cmd run docs:test-ui` | Desktop/mobile, eleven rendered diagrams, both themes, snapshot/fan-out/Delta search, sidebar/pagers/code controls, setup/evidence routes passed; actual manifest/Delta JSON download HTTP200 with add/remove actions; no JS/local request failures |
| `python scripts/verify_skills.py` / `python scripts/smoke_skills.py` | Eight skills zero failures; research archive/consolidation and publication controls passed |
| `npm.cmd ls --depth=0` | Existing four exact pinned npm dependencies intact |
| Selected artifact SHA256 / Python AST | All44 artifacts match manifest; new Spark scripts/modules parse; exported Lab03 has actual nonempty job mapping |

Selected Spark run: `.skills-test/spark/labs-all/20261010T094510Z-a7bea9dd`; per-query shuffle run: `labs-05/20261010T094622Z-495e0c4f`; Delta run: `labs-08/20261010T092601Z-9549f9a2`. Full event/data files remain ignored; website has44 actual text/JSON artifacts and a source-run/hash manifest under docs/public/evidence/spark. Replay commands and evidence links live in docs/setup/local-spark.md and docs/labs/runtime-evidence.md.

Spark UI availability: Windows loopback4040 returned HTTP200; application/stages REST metrics captured while Lab05 was live. SPARK_LOCAL_IP=0.0.0.0 inside container makes Jetty reachable through port forwarding; Docker host publication remains127.0.0.1 only. UI is optional, no automated test depends on it. Successful UI run shutdown cleanly and removes container; event logs persist. An earlier UI probe happened after hold ended; the next exposed a bind issue, then corrected live run verified the fix.

## Iteration 3 review and limits

Five new diagrams and desktop/mobile screenshots visually inspected: labels readable, no clipping or page overflow, existing visual baseline retained. Build checker now normalizes CRLF before section checks; headings/schema requirements unchanged. Parquet structural assertion originally matched `id:` inside `campaign_id:`, corrected to a field-boundary check and verified. Lab03 job group aligned with outer evidence collector; runtime artifacts validate actual job IDs.

Logical correctness and physical strategy remain separate: normal/broadcast joins both10000 rows/idSum49995000; duplicate UNKNOWN lookup17000; hash distribution7900/630/810/660 demonstrates unequal work. No measured straggler duration/speedup is claimed. Parquet two files/one row group each/SNAPPY, pruning/filter plans are evidence of reader behavior; pushed filter is not a measurement of bytes saved. Delta logs are real toy-table actions, while A+B to B+C is explicitly a separate conceptual simplification.

Runtime limitations: local[*] uses a single machine. Container quota2 CPU does not change Java's observed8-core defaultParallelism in this environment. Driver heap1GiB/container limit4GiB; diagnostic AQE=false/shuffle4/broadcast=-1 are explanation controls, not production settings. No reliable throughput benchmark, multi-node network measurement, spill, recovery, concurrent-writer stress, deletion vectors, retention/VACUUM or cloud-storage protocol test. Delta emits plan-truncation/record-statistics warnings, but row/log/history/schema assertions and clean shutdown passed. Native Windows PySpark not validated; supported reproducible path is Docker Linux.

Research session `.researches/2026-10-10T090000Z` archives23 selected official sources with HTML/text and consolidation. Primary references cover Spark4.0.4, Parquet, Delta protocol4.0.1 and AWS Databricks mapping. CI now has a separate Spark/Delta job and Pages deploy depends on both docs and runtime checks; authored locally, not executed on GitHub.

Remaining debt belongs to future production/runtime work, not hidden skipped tests. Source/schema/grain contracts and Delta snapshots now support the next dependency order: **Medallion → incremental source boundaries → idempotency invariants → MERGE implementation → late data/lookback/reconciliation**. Idempotency reasoning precedes MERGE so replay behavior is specified before mutation code. No Iteration4 chapter/lab was started. Work stops after Iteration3.

## Iteration 4 verification record

Executed **2026-10-11 (Asia/Saigon)** against the local working tree; run-folder timestamps use UTC2026-10-10. Chapters09–15, Labs09–15, correctness evidence and Mid Gate are complete. Accepted visual theme, four npm pins, eight skill pins and Spark4.0.4/Java17/Delta4.0.1 runtime retained. No Git commit/remote, workspace operation, cloud resource, push or live Pages deployment.

| Command / check | Actual result |
|---|---|
| `npm.cmd ci --ignore-scripts --no-fund --no-audit` | Reinstalled249 packages successfully after pausing the verified project dev server; four exact dependencies unchanged |
| `python scripts/verify_spark.py` | Spark4.0.4/local[*], DF5, SQL45, Parquet10;8 completed stages, clean shutdown |
| `python scripts/test_spark.py` | Existing5 integration tests passed, including actual Labs03–07;85 completed stages,74.609s |
| `python scripts/test_spark.py --delta` | Existing5 integration tests passed, including Delta08 log/history/time-travel/schema rejection;35 stages,71.070s |
| `python -m unittest discover -s tests -v` | 32 portable tests passed:13 existing +19 new business contracts |
| `python -m scripts.run_labs` | Four portable labs and wrong/fixed learner SQL checks passed |
| `python scripts/run_correctness.py --lab all` | All7 labs passed in first complete execution;403 stages, clean shutdown; later source-timestamp correction revalidated by full suite below |
| `python scripts/test_correctness.py` | Final9 tests passed,0 failures/errors/skips;356.147s and487 completed stages; exact states, unmatched duplicates and stale tombstone recovery |
| `python scripts/snapshot_correctness_evidence.py --run .skills-test/spark/tests-correctness/20261010T182402Z-b6e98655` | 25 selected artifacts +manifest archived from final successful run |
| `npm.cmd run docs:check` | 16 chapter schemas,41 authored Markdown pages;09–15 explicit interview sections |
| `npm.cmd run docs:build` | Final build24.83s;42 HTML pages,4443 references,0 failures; reviewer excluded from263 built HTML/search/script/JSON artifacts |
| Build evidence integrity guard | 25 artifact hashes,5 normalized UTF-8/LF source pins, exact state/history/matrix hashes and9-test success summary verified |
| `npm.cmd run docs:test-ui` | Final desktop1440/mobile390 checks passed:18 diagrams, light/dark, sidebar/pagers/code controls, four searches, assessment/input/evidence downloads; no JS/local HTTP errors |
| `python scripts/verify_skills.py` / `python scripts/smoke_skills.py` | Eight skill integrity checks; research archival/consolidation/publication controls passed,0 failures |
| `npm.cmd ls --depth=0` / Python AST | Four accepted versions retained; scripts/modules and two fenced Python snippets parse |

Selected source run: `.skills-test/spark/tests-correctness/20261010T182402Z-b6e98655`. Website artifacts under docs/public/evidence/correctness total about93KB,25 JSON files plus manifest. Each file has a stated pedagogical purpose; full transient Delta tables/event logs remain ignored. Source hashes normalize line endings; artifact bytes protected by scoped .gitattributes rule.

| Actual Delta observation | Exact business result |
|---|---|
| Lab11 once v1 /replay v2 /ack-failure retry v4 | One E123, revenue100, same hash43ae02345adb…; broken append300 |
| Lab12 final v5 /bad additive v2 | E123120 and E124100 remain distinct; bad update100→200→300; ambiguous matched source rejected without commit |
| Unmatched duplicate source | Direct MERGE inserts2 rows; preprocessing produces1; duplicate target rejected |
| Lab14 t2 v3 /all-snapshot replay v4 | E1 revenue120, same hash2d0aad4da2ad…; reconciliation rejects corrupted220 |
| Lab15 production final v3 | 90 historical events/revenue900, LIVE88 retained; total91 rows/988; affected-scope hash equals frozen source after full rerun |

## Iteration 4 quality review

| Required question | Finding / treatment |
|---|---|
| MERGE accidentally equals idempotency? | Chapter12 and actual additive/unmatched-duplicate failures show source uniqueness/key/update semantics are required |
| Watermark conflated with batch cursor? | Prominent10/14 comparison: retrieval position, reread scope, truth comparison, streaming event-time state are separate |
| Event time separated from processing? | Chapter13 four-clock trace and midnight fixture preserve event date; synthetic mutation helpers now derive coherent arrival/processing times |
| Every business key defines grain? | Bronze delivery, Silver source/app/event latest state, daily cost/Gold full date/platform/account/app/campaign/currency contracts |
| Retry/replay deterministic? | Stable keys, ordered source revisions, equal-revision conflict rejection, stale guards, deterministic replacement, cursor-after-write and exact replay hashes |
| Late strategies source-driven? | Updated-time contract, bounded2/6/72h candidates, tieredD-1/D-3/D-7, comparable snapshots and residual-gap ownership; no vendor guarantees asserted |
| Backfill verification before publish? | Durable37 completed days→resume53→staging90→validation/recon→predicate publish; failed staging does not change production |
| Tests prove correctness? | Exact states/metrics/hashes, namespace collisions, target/source duplicates, wrong keys with equal totals, nulls/day mismatch, replay/fault/resume/rerun assertions |

Final screenshots visually inspected: all seven new diagrams have readable labels/no clipping; mobile CRITICAL metadata wraps cleanly, assessment visible after navigation overlay closes. Reviewer material lives only in reviewer/mid-gate-pipeline-correctness.md, outside docs/public/navigation/search; public page has no solution details or reviewer link. This excludes publication, not repository access control. Mid Gate uses a separate fixture and causal/executable scoring.

Engineering corrections: two initial test-harness result-key names were wrong, fixed and full9-test suite rerun successfully. Windows Rollup lock required pausing the exact VitePress dev process (trailing command-line space accounted for). Initial working-tree build caught27 missing evidence links before successful artifacts were archived; final link/integrity checks pass. Synthetic updated states originally inherited old arrival/processing defaults; now coherent defaults preserve original event_time and a dedicated contract test covers this. Mobile assessment screenshot originally caught responsive sidebar animation even after .open cleared; final browser flow waits for offscreen geometry, asserts unobscured heading via elementFromPoint and captures stable animation-disabled screenshot. Full UI suite rerun passed and final image visually inspected.

Previously running project dev server restored in a hidden window at http://127.0.0.1:5173/Databricks-learning/; loopback GET200 verified. Browser test closed its own preview/browser; Spark runs stopped cleanly and disposable containers removed by --rm.

Research: nine current official primary sources, HTML/text +deduped consolidation under .researches/2026-10-10T180000Z; publication disabled. SOURCES.md owns claim/version boundaries. Collector now uses per-session verification date rather than historical hardcoded date; prior research/verification records preserved.

## Iteration 4 limits and next dependency decision

Labs09/10/13 are deterministic models;11/12/14/15 execute real Delta sinks against synthetic source snapshots. API paging/cutoff/delete/version guarantees, production FX/timezone policies and source completeness remain source-specific work. Driver collect/preflight is limited to tiny fixtures, not a distributed production dedup/validation protocol. Equal-revision conflict checks and publish require coordination under concurrent writers.

Faults are injected Python exceptions, not process kill/VM failure. Backfill covers90 daily rows in two37/53 chunks, not90 tasks; LIVE update interleaving is sequential and outside affected scope. Simultaneous/same-scope writer coordination, process-kill recovery, throughput/multi-node behavior and workspace/platform execution remain unverified. CI adds correctness suite to the existing Spark gate (30-minute timeout); GitHub Actions has not run.

Dependency review confirms **Structured Streaming → state → checkpoints → watermarks → delivery semantics → recovery**, after passing the new Mid Gate. Source/sink replay guarantees must remain explicit; orchestration/platform comes after these foundations. Work stops after Iteration4. No Iteration5 implementation started.


## Iteration 5 verification record

Executed 2026-10-11 against the local working tree, without a Git repository or commit claim. Chapters16-24 and nine labs cover continuously running queries, state lifetime, checkpoints/compatibility, event-time bounds, dedup, joins, output modes, sink effects and recovery. Existing website components/styles and runtime/dependency pins remain in use.

| Command | Actual result |
|---|---|
| `npm.cmd ci --ignore-scripts --no-fund --no-audit` | Reinstalled249 locked packages; paused only the verified project dev server before installation |
| `python scripts/verify_skills.py` | Eight installed skills; zero failures; optional sibling gaps preserved |
| `python scripts/smoke_skills.py` | Research help/save/consolidate/default-publication guard; zero failures |
| `npm.cmd run research:save` / `research:consolidate -- --session-dir .researches/2026-10-11T034500Z --query ...` | Twelve official source records, twelve HTML/Markdown pairs, URL-deduped consolidation; publication disabled |
| `python -m unittest discover -s tests -v` |36 tests passed, including four streaming recovery/assessment contracts |
| `python -m scripts.run_labs` | Four portable baseline labs and submitted-query failure/success checks passed |
| `python scripts/verify_spark.py` | Spark4.0.4/local[*], DataFrame5, SQL45, Parquet10, eight completed stages and clean shutdown |
| `python scripts/test_spark.py` | Five tests passed;85 completed stages; clean shutdown |
| `python scripts/test_spark.py --delta` | Five tests passed in Delta-enabled runtime;35 completed stages; clean shutdown |
| `python scripts/test_correctness.py` | Nine tests passed;487 completed stages; clean shutdown; full accepted correctness baseline |
| `python scripts/test_streaming.py` | Nine tests passed, zero failures/errors/skips;365 completed stages; clean shutdown |
| `python scripts/snapshot_streaming_evidence.py --run .skills-test/spark/tests-streaming/20261011T040856Z-6f8487be` | Selected13 successful artifacts; eight source hashes matched execution-start hashes |
| `python scripts/check_streaming_evidence.py` | Raw file hashes, normalized source hashes, runtime pin and all nine target/state/retry contracts passed |
| `npm.cmd run docs:check` |25 chapter schemas and61 authored Markdown pages passed |
| `npm.cmd run docs:build` | Final build29.04s;62 HTML pages,8274 internal references, zero failures;338 artifacts checked for reviewer exclusion; both evidence guards passed |
| `npm.cmd run docs:test-ui` | Final desktop/mobile navigation, search, light/dark, code controls,27 diagrams, chapter/lab pagers, two assessments and streaming artifact responses passed; zero browser JS/local HTTP errors |

Runtime baseline orchestration logs and exit codes are in `.skills-test/runtime-baseline-summary.json`; each command ran in its own disposable container. The published streaming manifest records Spark4.0.4, Delta4.0.1 pin, Java17.0.19, Python3.10.12 and the successful final run. Observed provider is HDFSBackedStateStoreProvider, global multiple-watermark policy=min and noDataMicroBatches=true. These local observations are not DBR defaults.

## Iteration 5 business and failure evidence

| Lab | Observed invariant |
|---|---|
|16 | Target3→5→6; multiple positive-input batch IDs, active snapshots and clean query stop |
|17 | Same-cp restart retains U1=(15,2), U2=(27,2); query ID stable/run ID new; state files and metrics present |
|18 | Target3→3→4→8; same-cp hash stable before new input; new cp discovers retained files again |
|19 | No-WM/long policy state rows3 and late C window amount7; short policy state row1, effective WM10:25, actual late-drop and eviction metrics |
|20 | Target1→2→3→3→4; within-horizon suppression, old-time late drop, refreshed-time E123 accepted after eviction |
|21 | C1/P1 and delayed C2/P2 matches; C3/NULL appears after controlled event-time closure; both-source progress and state removals |
|22 | Second update emits one changed key, complete emits two; append emits finalized amount30 window after progress advance |
|23 | Actual sink commit then controlled exception; same observed batch ID retried; unsafe append200 cents vs transactional100 cents |
|24 | Actual STATE_STORE_KEY_SCHEMA_NOT_COMPATIBLE; retained replay into staging U1=120/U2=50; reconciliation passes and original serving hash unchanged |

[STREAMING_AUDIT.md](STREAMING_AUDIT.md) records all ten conceptual checks. Watermark remains distinct from batch cursor/lookback/reconciliation; state growth, sink retry semantics, checkpoint compatibility and hybrid batch/stream decisions are explicit. The new Mid Gate uses a separate ROAS fixture with15-minute freshness,2-hour arrival tolerance,72-hour revisions, crashes and checkpoint loss. Public input/questions/rubric are separate from reviewer material outside docs/public/search. Build exclusion is publication control, not repository access control.

Engineering corrections: initial progress serialization failed on Spark4 UUID objects; official JSON representation fixed it, then selected and full suites were rerun. A readable compatible checkpoint with expired source position now selects repair, covered by a portable contract. Source hashes are captured at execution start and checked before snapshotting. Visual review made recovery source-position availability and missing-truth blocking explicit, added numbered prerequisite labels, and corrected tall-diagram capture so sticky navigation does not obscure exported labels. Final build/UI were rerun after relevant changes; final diagram and mobile screenshots were visually inspected.

Previously running dev server restored in a hidden window, PID21592, with home and Chapter16 loopback HTTP200 checks. Browser verification closes its own browser/preview. Research archive and evidence publication are local repository artifacts; no push, Pages deployment or workspace operation occurred.

## Iteration 5 limits and next dependency decision

The source is controlled retained JSON files, with typed UTC event time and tiny single-writer targets. Query stop/restart is actual recovery continuation but not process kill. Lab23 reproduces callback failure after one durable Delta write; remote REST transactions, distributed crashes and multi-table atomicity are unverified. Lab24 reproduces state-schema incompatibility, not cloud checkpoint corruption. Recovery fact patterns are a teaching exercise, not automated production remediation. Driver collect is only for bounded fixtures.

Actual file-source replay must not be generalized to other connectors. DBR source evolution, state repartitioning, real-time execution and managed refresh/reset remain version-scoped awareness. Two-hour event-time state does not replace72-hour revision detection, reconciliation or authoritative backfill. Concurrent writer coordination, throughput, cloud storage failures and production cutover remain future work. GitHub Actions workflow includes streaming checks and a40-minute runtime gate, but Actions has not run.

Recommended reading order: Databricks Compute → Lakeflow Jobs → Lakeflow Spark Declarative Pipelines → Unity Catalog → Databricks SQL. Governance/access basics must precede authenticated cloud labs; detailed governance can follow orchestration for resource context. CURRICULUM.md owns the dependencies. Work stops after Iteration5; no Iteration6 chapter or platform implementation was started.


## Iteration 6 verification record

Executed 2026-10-11, Windows host, Python3.12.10, Node24.18.0/npm11.16.0, installed Chrome and disposable Linux Docker runtime. Changes cover Chapters25-30, six labs, optional Free Edition setup, platform artifacts/evidence and Platform Design Mid Gate. Website design/components and accepted runtime/dependency pins remain unchanged.

| Command | Actual result |
|---|---|
| npm.cmd ci --ignore-scripts --no-fund --no-audit | 249 pinned packages reinstalled; verified project dev server paused to avoid file lock, restored hidden as PID13060 |
| python scripts/verify_skills.py | Eight installed skills, zero failures |
| python scripts/smoke_skills.py | Research adapter/archive/consolidation and default publication guard pass, zero failures |
| python -m unittest discover -s tests -v | 44 tests passed, including eight platform artifact contracts |
| python -m scripts.run_labs | Four portable labs plus wrong/fixed SQL submission checks passed |
| python scripts/verify_spark.py | Spark4.0.4, local[*], DF5/SQL45/Parquet10; eight stages and clean shutdown |
| python scripts/test_spark.py | Five tests passed, 85 stages, clean shutdown |
| python scripts/test_spark.py --delta | Five tests passed, Delta4.0.1, 35 stages, clean shutdown |
| python scripts/test_correctness.py | Nine tests passed, 487 stages, clean shutdown |
| python scripts/test_streaming.py | Nine tests passed, 365 stages, clean shutdown |
| python scripts/test_platform.py | Six tests passed, 83 stages, clean shutdown; actual SELECT semantics only |
| python scripts/check_platform_evidence.py --snapshot .skills-test/spark/tests-platform/20261011T051456Z-42929e3f | Five selected files, 18 startup source hashes; successful six-test/runtime/output guards |
| python .skills-test/platform_prose_check.py | 15 platform pages checked, one fenced Python AST parsed; prose dash/label checks pass |
| npm.cmd ls --depth=0 | VitePress1.6.4, Mermaid12.1.0, Playwright1.64.0, tsx4.20.6 unchanged |
| npm.cmd run docs:check | 31 chapter schemas, 76 authored Markdown pages passed |
| npm.cmd run docs:build | Final production build26.36s, 77 HTML pages/11477 internal references, zero failures; private/evidence guards passed |
| npm.cmd run docs:test-ui | Chapters00-30/lab routes, 33 Mermaid diagrams, themes/search/mobile/three gates and evidence endpoints passed; no JS/local HTTP failures |

The runtime orchestrator .skills-test/iteration6-runtime-summary.json records all five baseline suites with exit0. Local source runs: smoke20261011T050331Z-0a799836, Spark20261011T050352Z-5b80a8c8, Delta20261011T050522Z-96469c6f, correctness20261011T050706Z-534055b7, streaming20261011T051317Z-433d9a04. Accepted public correctness/streaming artifacts remain hash-verified; new platform SELECT evidence is published separately. All six new diagrams plus desktop Chapter26, mobile Chapter28 and the mobile Platform Gate were visually inspected.

### Artifact and source review

Job representation has seven tasks, two ingest roots, a validation barrier and a failure-report branch. Validation retry0, other sample retries1, timeout600s, max_concurrent_runs1. Failure/retry/repair states are expected workspace behavior until actual runs exist. The failure report prints only; no external messages are sent.

Medallion source uses batch materialized views, highest revision by full source/app/event identity, and Lakeflow-only fail expectations. It publishes separate names to avoid competing with Jobs outputs. Local SQL tests prove four identities, Gold revenue1250/cost700 cents across three rows, repeat stability, ratio-of-sums, zero-cost NULL, dimension fan-out2500 and equal-revision conflict rejection. They convert notebook DDL to temporary views and never invoke a Jobs scheduler, SDP engine, UC or SQL warehouse. The bounded ROAS query assumes complete cost coverage; live unknown-cost handling remains explicit.

Governance tests inspect an explicit design fixture, not effective Databricks access. Setup includes user-owned preflight and supported OAuth documentation without signup, credentials/profile configuration, CLI installation or authenticated operations. Enterprise group/service-principal/IAM/private-network/multi-workspace exercises are not inferred from Free Edition.

SOURCES.md records current terminology and 37 official dual HTML/text archived references. Narrow current JAR task guidance documents serverless support despite the generic compute table's classic-only row; classic fallback depends on incompatibility. Current pipeline properties prefer schema over legacy target. Apache SDP is distinct from Lakeflow pipelines on DBR; local Spark4.0.4 stays pinned.

PLATFORM_AUDIT.md covers all ten conceptual checks. Public Platform Design gate rewards justified migration/hybrid choices, including retained Airflow/dbt. Reviewer material stays outside docs/public/search. Pattern guards cover credential-like tokens, workspace URLs, emails and platform IDs; manual screenshot redaction remains necessary.

### Pending workspace and production evidence

PENDING USER WORKSPACE: actual Free Edition feature availability, CLI strict bundle validation/deploy, Jobs DAG/run/retry/repair, inferred pipeline graph/update/fail expectation, owned UC metadata/access and SQL warehouse/query history. No workspace account, token, email or ID was captured. No cloud evidence was fabricated.

Production scale/networking/admin/SLA/concurrency/cost/multi-workspace governance, external API/auth contracts, target-scope writer coordination and representative load/failure acceptance remain unverified. GitHub Actions is authored with the platform SQL test but has not run.

Final build guards checked 389 HTML/search/script/JSON artifacts for reviewer leakage and common private-data patterns. Correctness25 file/five source pins, streaming13 file/eight source pins and platform5 file/18 source hashes passed. All disposable Docker test containers had ended; dev service PID13060 still served home/Chapter25 over loopback HTTP200. No push, deployment or remote message occurred.

### Next dependency decision

Recommended Iteration7: Performance Engineering → observability → data quality → testing → CI/CD → production Declarative Automation Bundles. First understand plans/layout/skew and meaningful bottleneck measurements; expose operational signals; define quality contracts and executable failure tests; enforce those checks in deployment/promotions. Observability and performance should iterate together. Bundles is a sample representation here; production rollout remains future work. Stop after Iteration6; no Iteration7 implementation started.


## Iteration 7 verification record

Executed 2026-10-11 on the existing Windows/Node24.18.0/npm11.16.0/Python3.12/Chrome baseline. Runtime pins remain Spark4.0.4/Delta4.0.1 in the same official digest-pinned local container. Website components/styles and skill stack were preserved.

### Delivered scope

Chapters31-45 and15 corresponding labs cover evidence-first performance, plans/AQE, files/layout, liquid clustering/AUTO, predictive optimization, Photon, observability/cost awareness, quality/expectations, testing, CI/CD, DABs, GitHub OIDC and release/data repair. Each chapter follows the template and has interview articulation, prerequisites and explicit evidence tiers. Performance Diagnosis and Production Readiness are unseen assessment packets/rubrics; reviewer material remains outside published docs/search.

The ROAS extension has src/tests/resources/databricks.yml, one necessary Job, dev/staging/prod sandbox targets, required external host/catalog/identity/group variables, enabled deployment lock and bounded retries. Its fixture path is callback/cost Bronze → scoped Silver → candidate Gold → exact reconciliation → single-table publication. It is not a production ingestion connector or a cloud-deployed application.

### Fresh command evidence

| Command/check | Actual result |
|---|---|
| npm.cmd ci --ignore-scripts --no-audit --no-fund |249 packages installed; four existing npm pins unchanged |
| python scripts/verify_skills.py |8 skills, zero failures; no skills installed/updated |
| python scripts/smoke_skills.py |6 smoke checks, zero failures; default research publication disabled |
| python -m unittest discover -s tests -v |44 tests passed |
| python -m scripts.run_labs |4 portable labs and SQL rejection/acceptance passed |
| Isolated Python -m pytest labs/production/tests -q |14 checks passed, no skips |
| python scripts/check_production_config.py |Paths, direct engine/lock, required variables, target schema/root isolation and Job/retry contracts passed |
| CLI1.20.0 version/schema/plan-help/validate-help |Official archive checksum verified; commands unauthenticated; schema/provenance archived |
| scripts/check_bundle_schema.py with archived CLI schema |Canonical schema hash, complete bundle/resource validation and negative concurrency-type test passed in Linux container |
| python scripts/verify_spark.py |Smoke DF/SQL/Parquet and clean stop;8 stages |
| python scripts/test_spark.py |5 tests,82.577s,85 stages; clean stop |
| python scripts/test_spark.py --delta |5 tests,68.311s,35 stages; clean stop |
| python scripts/test_correctness.py |9 tests,364.681s,487 stages; clean stop |
| python scripts/test_streaming.py |9 tests,389.959s,365 stages; clean stop |
| python scripts/test_platform.py |6 tests,81.267s,83 stages; clean stop |
| python scripts/test_production.py |8 tests,204.857s,202 stages/2440 tasks; clean stop |
| python scripts/check_production_evidence.py |14 file hashes,15 startup source hashes and actual result contracts passed |
| Evidence guard negative test |Fresh public evidence accepted; stale-source mutation rejected |
| npm.cmd run docs:check |46 chapter schemas,109 authored Markdown pages passed |
| npm.cmd run docs:build |Final build/link/privacy/correctness/streaming/platform/production guards passed;110 HTML pages/21311 references, zero link failures |
| npm.cmd run docs:test-ui |Chapters00-45,48 diagrams, five gates, search/themes/copy/pagers/mobile/evidence endpoints passed; zero JS/local HTTP errors |
| Prose/AST/privacy review |33 new production pages, local Python parse, source labels and publication-disabled archive checks passed |

Exact exit codes are recorded in ignored .skills-test/iteration7-runtime-summary.json and iteration7-site-summary.json. Selected new source run: .skills-test/spark/tests-production/20261011T062450Z-30a3ef62. Earlier failed/stale intermediate runs were not selected. Old published evidence remains source/hash-verified. All15 new diagrams, desktop Chapter43, mobile Chapter38 and both new gate mobile pages were visually inspected.

### Observations and reproduced failures

Actual local filter/select has no Exchange; aggregate/shuffle join has movement; bounded explicit broadcast produces BroadcastHashJoin. AQE final plan is captured separately. The10000-row hot-key case preserves exact campaign counts under two-phase aggregation; no speedup claim is made.

Same4096-row Delta input writes32 files versus2 files, with stats and512 selected rows in both. Tiny sizes1411/1416/1422 bytes min/median/max and8 planning partitions; compact9821/9828/9835 bytes and2 partitions. These are fixture layout observations, not a production target file size or latency benchmark.

Retry/revision transforms yield4 scoped Silver identities and3 Gold rows/revenue1250/cost700 with exact schema/grain/row reconciliation. Null identity, invalid date and negative amount produce3 quarantine rows out of9 inputs. Country warnings retain business data. Equal-revision conflict, duplicate cost grain, missing cost and incorrect candidate are rejected by their respective tests. Fan-out counterexample yields6 rows/revenue2500; successful-but-stale cost blocks portable readiness.

Local bad Delta commit doubles1250→2500. Selecting good code leaves committed data unchanged; RESTORE creates version2 and returns1250. Failed staged candidate preserves original serving1250. No VACUUM, retention-expired restore, downstream streaming RESTORE, cross-table transaction or concurrent production writer was executed.

### Source and tool boundaries

SOURCES.md and three publication-disabled research sessions archive32 successful official sources plus explicit404 records for superseded guesses. Current terminology/requirements were checked for layout/AUTO/predictive optimization, Photon, observability, expectations and DAB/CLI lifecycle. CLI1.20.0 direct deployment and exact GitHub federation subject semantics are version-qualified. The Jobs skill retains older bundle naming; the deploy reference's skip-dev-validation guidance is superseded here by strict validation before every workspace deployment.

CLI JSON schema allows some semantic strings; portable mode/isolation contracts add checks. Its Unicode patterns require a compatible regex engine. Windows application control blocked a native validator dependency, so the documented checksum/hash-pinned Linux-container path was executed successfully. No host security policy, global CLI install, credentials or profile was changed.

### Pending cloud and production acceptance

Status: PENDING USER WORKSPACE. Strict resolved-target validation, plan against real state, deployment, notebook imports/fixture paths, serverless Job execution, grants/run identity and forced-failure serving preservation need a selected approved workspace. Photon, liquid clustering/AUTO, predictive maintenance, system-table/query-profile/event-log/expectation observations and alerts have no cloud execution evidence.

Manual OIDC workflow and PR checks are authored/parsed, not executed in GitHub. Required reviewers, branch restrictions, environment variables and exact federation trust must be configured and accepted in a user-owned account. Free Edition does not prove enterprise production identities/networking/system-table coverage. Git remote/Pages publication remains absent.

Remaining production work: replace fixtures/fixed expected totals with approved retained sources/manifests, verify schemas/imports/runtime compatibility, coordinate every target writer, define real notification/incident owners and validate representative load, retention and downstream repair. Model/lab timestamps and money/currency contracts remain synthetic and scoped.

### Next dependency decision

Recommended Iteration8: Apache Iceberg → Delta vs Iceberg → Databricks vs BigQuery/Snowflake/Fabric → system design trade-offs → when not to use Databricks. Table metadata/transaction/governance semantics precede interoperability, then compare capability/operability/cost against the production contracts now learned. Stop after Iteration7; no Iteration8 implementation was started.

## Iteration 8 verification record

Executed2026-10-11 on the local Windows working tree, with Linux Docker Spark4.0.4 and unchanged Delta4.0.1. No .git/remote exists; no commit, push, Actions run or live Pages deployment is claimed.

### Delivered architecture scope

Chapters46-60 and15labs follow the17-section template plus interview articulation, priorities, prerequisites and pagers. Iceberg semantics precede catalog/evolution/mutations, then format interoperability, managed ownership, platform comparisons, scenario scorecards, simplification/lock-in/open architecture and four case studies.

ADR-001 retains a Delta writer with a conditional read-interoperability pilot; ADR-002 keeps a stable GCP SQL stack until a measured requirement gap exists. These are worked scenario decisions, not workspace approvals. Cases include BigQuery startup analytics, a conditional Databricks ROAS design, managed/open multi-engine enterprise and conditional Fabric Microsoft enterprise.

The sixth public gate accepts any justified platform, including rejection of Databricks. Its100-point rubric requires80, each deliverable≥5 and no critical conceptual/governance/migration blocker. Reviewer guidance remains outside docs/search with the existing private marker.

### Fresh checks

| Command/check | Actual result |
|---|---|
| npm.cmd ci --ignore-scripts --no-fund --no-audit |249packages installed from unchanged dependency pins; initial sandbox EBUSY/cache error resolved by approved rerun |
| python scripts/verify_skills.py |8skills,0failures |
| python scripts/smoke_skills.py |6research adapter smoke checks,0failures; default publication blocked |
| python -m unittest discover -s tests -v |44portable tests pass |
| python -m scripts.run_labs |Four portable labs and SQL failure/success submission pass |
| Isolated pytest labs/production/tests |14pass; rerun after Pages workflow edit also14pass |
| Spark smoke and baseline integrations |Smoke passes; Spark5,Delta5,correctness9,streaming9,platform6,production8 all pass without skips |
| python scripts/verify_iceberg.py |Actual Spark/Iceberg/Scala versions, table create/insert/query and snapshot pass; clean shutdown |
| python scripts/test_iceberg.py |7semantic tests pass without errors/skips;52completed stages,clean shutdown |
| CLI1.20.0 version/schema and Linux schema checker |Fresh captured schema matches canonical pin; bundle/resource validation and negative type case pass; no auth/target resolution |
| python scripts/check_iceberg_evidence.py |9artifact hashes,7startup source hashes,versions,semantics,metadata and clean shutdown pass |
| Integrity negative controls |Guard accepts current evidence and rejects stale source hashes and wrong partition total |
| Official source/JAR integrity |25successful official documents archived in dual representations;10unavailable URL guesses retained; new chapter/ADR URLs map to successful archives/redirects; official Maven checksum matches JAR |
| npm.cmd run docs:check |61chapter schemas and145authored Markdown pages pass |
| npm.cmd run docs:build |146HTML pages,35160internal refs,0failures;621built artifacts privacy-scanned |
| npm.cmd run docs:test-ui |63rendered diagrams,Chapters00-60,lab pagers,six gates,search/themes/copy/mobile and evidence endpoints pass; no JS/local HTTP failures |
| Final rebuild and focused browser acceptance |Latest prose and chronological61lab links pass on all15architecture routes/mobile; sixth-gate privacy and browser errors pass |

All accepted public evidence guards still pass:correctness25files/5source pins,streaming13files/8sources,platform5files/18sources,production14files/15sources. New Iceberg evidence is separate and the accepted Spark/Delta launcher/common/runtime pins are unchanged.

### Selected Iceberg evidence

Selected run:20261011T090254Z-ab860623. Spark4.0.4,Iceberg1.12.0,Scala2.13,local Hadoop catalog,formatv2. Runtime JAR SHA256:3f50e93e8ed322ae0da0e380f1b6c27116404329c62e55f0586697b1b8378306; official Maven checksum receipt is .researches/2026-10-11-architecture-extra/artifact-provenance.json.

Measured:create/query2rows/revenue300;snapshot old2/current3 with parent lineage;schema rename retains fieldID3 and old country=NULL;partition specs0/1 retain old files and query3rows/revenue350;explicit COW UPDATE/DELETE/MERGE yields170;MOR partial-file delete leaves one2-row data file plus one position-delete entry and reader output200.

Metadata integrity checks actual JSON and engine-decoded metadata tables, referenced local paths,3snapshots/3manifests/4current data files. Nine bounded public artifacts exclude raw Parquet/Avro/JAR/event-log payloads.

### Failures and limitations

Initial MOR fixture optimized away a whole file and produced no position-delete file. The corrected fixture keeps two rows in one file, deletes one and asserts content1; fresh full integration evidence replaces that failed run. Build found one incorrect relative link in the included source ledger; the corrected site passes full build checks.

Iceberg equality-delete generation,v3,REST server,Trino/Flink,concurrent commits and object storage are not executed. Databricks managed/foreign/UniForm,BigQuery,Snowflake,Fabric and cloud IAM remain SOURCED PLATFORM or ARCHITECTURE EVIDENCE/PENDING USER WORKSPACE. No toy benchmark ranks formats/platforms.

All15new diagrams,desktop Case60,mobile Chapter57 and the sixth gate were visually inspected. ARCHITECTURE_AUDIT.md records all14requested misconception checks. No new skill, npm dependency, global configuration or credential setup was introduced.

Recommended Iteration9 dependency order: ROAS requirements and architecture decision → implementation → failure injection → production runbook → final Mid assessments → interview pack → certification mapping → final site QA. Iteration9 is not started; work stops after Iteration8.
