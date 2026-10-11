# Production hardening quality audit

Scope: Chapters31-45, corresponding labs, two assessments and the bounded ROAS sandbox release. Claims are linked to official sources, local implementation or selected evidence; workspace execution remains pending.

| Audit question | Result | Evidence owner |
|---|---|---|
| Tuning before measuring? | Measurement/hypothesis precedes one-variable changes | Chapters31,32,36; performance gate |
| Random cache/repartition? | Candidates require repeated-work/distribution evidence | Chapters31,36 |
| ZORDER default without current guidance? | Liquid/AUTO recommendations are version-qualified; partitioning remains a decision | Chapter34; SOURCES.md |
| Quality equated with coverage? | Data, code and platform correctness separated | Chapters39,41 |
| SUCCESS equated with correct/fresh data? | Separate source cutoffs and business reconciliation | Chapters37,38; health test |
| Unit tests prove production? | Fixture/local/cloud boundaries explicit | Chapter41; production evidence |
| Manual production notebook edit preferred? | Reviewed resource-as-code release replaces that anti-pattern in course design | Chapters42-44 |
| Obsolete primary bundle name? | Current name used; former name appears as historical alias | Chapter43 |
| Secrets in config? | External variables, narrow OIDC, no embedded credentials | roas-release.yml; privacy guard |
| Code rollback automatically repairs data? | Local bad commit remains until separate RESTORE | Chapter45; runtime test07 |
| Cloud execution overclaimed? | Strict validation/deploy/run, profiles/system tables/expectation metrics pending | Evidence tiers and progress table |
| Performance claims supported? | Actual plans/layout/metrics; no local speedup extrapolation | Manifest14 files, startup source hashes |

Known boundaries: tiny classic single-machine Spark fixtures; no production benchmark, distributed host contention, Photon, liquid clustering, predictive optimization, live query profile, system-table queries, managed expectations, cloud deployment, permissions enforcement or GitHub Actions execution.

Release example uses retained synthetic full snapshots and fixed expected rows. Real ingestion connectors, production concurrency/writer coordination, source manifests, notification owners and incident acceptance remain deployment prerequisites. Single-table staged publication does not establish cross-table atomicity. Local RESTORE retains files; retention-expired and downstream-streaming restore cases are design reasoning only.
