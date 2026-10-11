# Agent Skills

Eight project-local skills are installed under `.agents/skills/`. This file owns usage guidance; [AGENTS.md](AGENTS.md) owns task policy, [SKILLS_LOCK.md](SKILLS_LOCK.md) owns provenance, and [SKILLS_VERIFICATION.md](SKILLS_VERIFICATION.md) owns evidence and limitations.

## Discovery and invocation

Codex repository discovery uses `.agents/skills/`: see [official Codex skill guidance](https://developers.openai.com/codex/skills/) and [OpenAI repository workflow guidance](https://developers.openai.com/blog/skills-agents-sdk). `skills list --agent codex --json` also enumerates this installation. These skills are available on the next turn; reload the workspace/session if the current skills catalog remains stale. This turn can read them directly from disk. A new-session automatic selection test was not performed.

Before work, inspect the catalog and [routing matrix](#skill-routing-matrix). Read only the matching `SKILL.md` and necessary references. Explicit invocation examples: `$databricks-jobs Explain Lakeflow Jobs terminology`, `$databricks-unity-catalog Design dev/staging/prod hierarchy`, and `$mermaid-diagrams Draw Bronze -> Silver -> Gold`. Load `databricks-core` before product skills. Add research when a statement is version-sensitive and verification before declaring completion.

## Installed Skills

### databricks-core

Source:
https://github.com/databricks/databricks-agent-skills/tree/c1964266c7aa6063d89036691d0594420ffa0129/skills/databricks-core

Purpose:
CLI, profile selection, authentication workflow, and platform entry point.

Use when:
- Databricks platform questions; CLI/auth/profile work.

Do not use when:
- Treating this as a complete Spark/Delta reference; unrelated local repository edits.

Verified:
Yes, for local installation, readability, dependency inspection, and documented routing. Live-service execution is separate.

Verification notes:
UTF-8 SKILL.md readable; frontmatter/name valid; parent and linked local references checked; checksum inventory recorded; CLI catalog lists the skill for Codex. Databricks CLI >= 1.0.0 and selected authenticated profile are required for live CLI work. CLI is absent here; no credentials or cloud operations tested.

---

### databricks-jobs

Source:
https://github.com/databricks/databricks-agent-skills/tree/c1964266c7aa6063d89036691d0594420ffa0129/skills/databricks-jobs

Purpose:
Lakeflow Jobs task DAGs, triggers, retries, notifications, and deployment guidance.

Use when:
- Job orchestration, task configuration, and Lakeflow Jobs chapters.

Do not use when:
- Implementing pipeline transformations without an orchestration question.

Verified:
Yes, for local installation, readability, dependency inspection, and documented routing. Live-service execution is separate.

Verification notes:
UTF-8 SKILL.md readable; frontmatter/name valid; parent and linked local references checked; checksum inventory recorded; CLI catalog lists the skill for Codex. Databricks CLI >= 1.0.0 and selected authenticated profile are required for live CLI work. CLI is absent here; no credentials or cloud operations tested.

---

### databricks-unity-catalog

Source:
https://github.com/databricks/databricks-agent-skills/tree/c1964266c7aa6063d89036691d0594420ffa0129/skills/databricks-unity-catalog

Purpose:
Governance, catalog/schema/table hierarchy, privileges, lineage, and system tables.

Use when:
- Environment hierarchy design, access policies, securables, and governance.

Do not use when:
- Generic Spark transformations or automatic grant changes without authorization.

Verified:
Yes, for local installation, readability, dependency inspection, and documented routing. Live-service execution is separate.

Verification notes:
UTF-8 SKILL.md readable; frontmatter/name valid; parent and linked local references checked; checksum inventory recorded; CLI catalog lists the skill for Codex. Databricks CLI >= 1.0.0 and selected authenticated profile are required for live CLI work. CLI is absent here; no credentials or cloud operations tested.

---

### databricks-dabs

Source:
https://github.com/databricks/databricks-agent-skills/tree/c1964266c7aa6063d89036691d0594420ffa0129/skills/databricks-dabs

Purpose:
Declarative Automation Bundles configuration, validation, targets, and deployment.

Use when:
- Databricks deployment, multi-environment configuration, and CI/CD chapters.

Do not use when:
- GitHub Pages deployment alone; running cloud deployments during documentation work.

Verified:
Yes, for local installation, readability, dependency inspection, and documented routing. Live-service execution is separate.

Verification notes:
UTF-8 SKILL.md readable; frontmatter/name valid; parent and linked local references checked; checksum inventory recorded; CLI catalog lists the skill for Codex. Databricks CLI >= 1.0.0 and selected authenticated profile are required for live CLI work. CLI is absent here; no credentials or cloud operations tested.

---

### research-online

Source:
https://github.com/gg-skills/research-online/tree/52d1f89b0223d305d79948bab36c7da78d254ef1/.

Purpose:
Current online research, source evaluation, and reproducible evidence archival.

Use when:
- Version-sensitive terminology, API behavior, deprecations, and external research.

Do not use when:
- Offline questions answered from local files; installing/authenticating optional research services.

Verified:
Yes, for local installation, readability, dependency inspection, and documented routing. Live-service execution is separate.

Verification notes:
UTF-8 SKILL.md readable; frontmatter/name valid; parent and linked local references checked; checksum inventory recorded; CLI catalog lists the skill for Codex. Host web search/fetch works. tsx runner is pinned in package-lock.json. Save/consolidate tested with a source fixture; publication is blocked. Firecrawl is optional. Upstream shared publish helper is missing; two imports use the documented local adapter.

---

### technical-writing

Source:
https://github.com/riekelt/technical-writer/tree/85e53729dd959a2795d593d6769068e342cf3486/plugins/technical-writer/skills/technical-writing

Purpose:
Technical documentation structure, sourcing, audience, and prose review.

Use when:
- Handbook chapters, setup references, reports, and substantial technical prose.

Do not use when:
- Marketing copy, deciding product behavior, or installing all sibling writing skills.

Verified:
Yes, for local installation, readability, dependency inspection, and documented routing. Live-service execution is separate.

Verification notes:
UTF-8 SKILL.md readable; frontmatter/name valid; parent and linked local references checked; checksum inventory recorded; CLI catalog lists the skill for Codex. references/truth.md and references/style.md are present. Sibling writing skills are not installed; use the base workflow and manual source/style review.

---

### mermaid-diagrams

Source:
https://github.com/softaworks/agent-toolkit/tree/3027f20f3181758385a1bb8c022d4041dfb4de84/skills/mermaid-diagrams

Purpose:
Text-based architecture, data flow, sequence, and entity diagrams.

Use when:
- Architecture/data-flow diagrams, including Bronze -> Silver -> Gold.

Do not use when:
- A plain fact or edit that a diagram does not clarify; raster art.

Verified:
Yes, for local installation, readability, dependency inspection, and documented routing. Live-service execution is separate.

Verification notes:
UTF-8 SKILL.md readable; frontmatter/name valid; parent and linked local references checked; checksum inventory recorded; CLI catalog lists the skill for Codex. All seven linked diagram guides are present. Routing and a small flowchart were inspected. No renderer installed or Pages rendering claimed.

---

### verification-before-completion

Source:
https://github.com/obra/superpowers/tree/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills/verification-before-completion

Purpose:
Run relevant checks and inspect evidence before any completion claim.

Use when:
- Final verification, setup completion, fixes, commits, and pull-request claims.

Do not use when:
- Replacing actual checks with assertions; requiring unrelated tests for documentation edits.

Verified:
Yes, for local installation, readability, dependency inspection, and documented routing. Live-service execution is separate.

Verification notes:
UTF-8 SKILL.md readable; frontmatter/name valid; parent and linked local references checked; checksum inventory recorded; CLI catalog lists the skill for Codex. Applied to actual setup checks, catalog inspection, and smoke tests; no executable dependency.

---

## Skill routing matrix

| Task | Required skills | Optional skills |
|---|---|---|
| Databricks architecture | databricks-core | research-online, mermaid-diagrams |
| Spark/Delta research | databricks-core, research-online | technical-writing |
| Lakeflow Jobs chapter | databricks-core, databricks-jobs | research-online, technical-writing, mermaid-diagrams |
| Unity Catalog | databricks-core, databricks-unity-catalog | research-online |
| Databricks CI/CD chapter | databricks-core, databricks-dabs | research-online, technical-writing |
| Architecture diagram | mermaid-diagrams | databricks-core |
| Handbook writing | technical-writing | research-online |
| Repository maintenance / GitHub Pages CI | verification-before-completion | technical-writing, research-online |
| Final verification | verification-before-completion | None |

Load research for all current or version-sensitive claims, even when the table labels it optional. Load technical-writing when the output is substantial technical documentation. Final verification applies across task types. Repository maintenance and Pages CI have no dedicated skill in this stack; follow repository configuration and official tool docs.

## Installation and reproducibility

The initial project directory was empty, contained no `.git`, `AGENTS.md`, or skills, and had no ancestor AGENTS.md at the inspected project parent. Existing user skills contained only the system directory; `skills list --global --json` returned `[]`. Bundled plugin skills remain separate from this project inventory.

Environment: Node v24.18.0; npm/npx 11.16.0; Skills CLI 1.7.2; Python 3.12. The PowerShell execution policy blocks npm.ps1/npx.ps1, so use npm.cmd/npx.cmd. No execution policy or global agent configuration was changed.

The supplied `npx skills add <source> --skill <name>` syntax remains valid. Current CLI help confirms `--agent codex --yes --copy` for deterministic project installation. Avoid `--global` and `--all`. The install used the official skill-installer helper with explicit source paths, pinned `--ref` commits, and `--dest .agents/skills`, rather than fetching an unpinned branch. This prevents duplicate copies of plugin-generated skills and records the precise source. The helper refused existing destinations.

The ZIP install of mermaid-diagrams hit a Windows path-length error in an unrelated source directory. Retrying only that skill with `--method git` succeeded. No final failed skills remain.

For exact reproduction, preserve `.agents/skills`, `skills-manifest.json`, package.json, and package-lock.json in version control. On a fresh checkout:

```powershell
npm.cmd ci --ignore-scripts
python scripts/verify_skills.py
python scripts/smoke_skills.py
npx.cmd --yes skills@1.7.2 list --agent codex --json
```

To recover missing upstream files, use the official helper with the matching manifest source, sourcePath, and commit:

```text
python <skill-installer>/scripts/install-skill-from-github.py --repo <owner/repo> --path <sourcePath> --ref <commit> --dest .agents/skills
```

For research-online use `--path . --name research-online`. For Mermaid on Windows use `--method git`. Reapply the research import adapter and upstream license files before verifying against hashes. This reconstruction command is a recovery template, not an executed clean-machine restore test. For updates, inspect upstream changes, install into a separate staging directory, compare files and dependencies, retain adapters, rerun checks, then intentionally update hashes and lock documentation.

## Research scripts and local adaptation

Use the repository scripts instead of upstream auto-publish defaults:

```powershell
npm.cmd run research:session:init -- --query "Lakeflow Jobs terminology"
npm.cmd run research:save -- --query "Lakeflow Jobs terminology" --source search --results <local-results.json> --session-dir <session-directory>
npm.cmd run research:consolidate -- --query "Lakeflow Jobs terminology" --session-dir <session-directory>
```

Host search/fetch corresponds to the available web tools; a local CLI script does not itself provide a search engine. Normalize actual tool responses into a top-level JSON array of records with `title`, `url`, and `content`, then save and consolidate. Wrapped `{"results": [...]}` objects are not expanded by the upstream loader. Sessions belong under `.researches/<timestamp>/`. The helper takes `--results` for a file, which avoids shell interpolation of page contents. Documentation archival can use upstream archive helpers when a full archival task needs HTML and Markdown; that advanced workflow was not exercised here.

Upstream research scripts reference `../../../scripts/shared/finalize-scoped-artifact`, which is absent from the skill repository. The two imports now resolve to `scripts/local-publish-policy.ts`. It locates the repository by AGENTS.md and refuses publication before any git/network operation; dry-run metadata is allowed. The npm consolidation wrapper passes `--no-publish`. Consolidation also includes a Source URLs section in Markdown because upstream formatting retains URLs only in JSON. These adaptations are included in file hashes. Upstream SKILL.md remains unchanged; AGENTS.md policy governs this repository. Missing sibling skills such as chooseable-options, plan, and study are not installed or required for this scoped lookup.

Unity Catalog links to ten adjacent product skills outside this stack. The verifier reports these as optional sibling routes and still checks references inside each installed package and the installed parent. Upstream license/notice files are preserved where provided. The inspected research-online source has no top-level LICENSE file; no license terms were invented. `.gitattributes` preserves vendored bytes for stable checksums across Windows Git checkouts.

## Source of truth policy

Skills guide workflows. Official Databricks docs determine current APIs, product names, pricing, certification objectives, runtime behavior, and deprecated features. Verify those claims online with a cloud/version qualifier, retain source URLs and dates, and prefer official documentation in conflicts. Upstream guidance can contain inconsistent version floors or old terminology; check current CLI help rather than copying examples blindly.

One observed inconsistency: databricks-jobs frontmatter requires CLI >= 1.0.0, while its embedded scaffolding example says >= 0.288.0 and sometimes uses Asset Bundles. Follow the current CLI floor and [official bundle documentation](https://docs.databricks.com/aws/en/dev-tools/bundles/), which calls the feature Declarative Automation Bundles. Do not treat the embedded example as current installation guidance.

## Optional recommendation: SKIP databricks-data-engineering

The request provided a skill name without a repository URL. The inspected candidate is [databricks-solutions/databricks-exec-code-mcp](https://github.com/databricks-solutions/databricks-exec-code-mcp/tree/aebffd3d80782a2513b48f291231395e5db6d335/skills/databricks-data-engineering), commit `aebffd3d80782a2513b48f291231395e5db6d335`. No assumption is made that every identically named skill has the same source.

| Area | Additional value | Overlap or risk |
|---|---|---|
| Medallion | Long Bronze/Silver/Gold notebook examples | Adds substantial context; hierarchy and deployment overlap the official stack |
| Delta | MERGE and optimization snippets | Defaults repeatedly to OPTIMIZE/ZORDER; current table/layout choices need official verification |
| Spark | PySpark cleaning and aggregations | Repeated count actions and broad except blocks are workload-dependent examples |
| Streaming | Lists Structured Streaming as a trigger | Most worked examples are batch; lacks an equivalent worked checkpoint/watermark/recovery design |
| Data quality | Null/range/duplicate assertions | Hardcoded retention/filter policies; zero-record percentage calculations can divide by zero |
| Production DE | Multi-stage job/bundle examples | Calls databricks-testing and databricks-bundle-deploy outside this scope; deployment overlaps official jobs/dabs |

Concrete defects include `whenMatchedUpdate(set={"*"})`, which passes a set where the [Delta Python API](https://docs.delta.io/api/latest/python/spark/index.html) expects a mapping, and a purported SCD Type 2 snippet that only adds columns without closing prior versions. `/mnt` examples depend on DBFS mounts, which [Databricks now deprecates](https://docs.databricks.com/aws/en/dbfs/mounts). It also hardcodes a Claude model and provider-specific tools in frontmatter. These observations justify SKIP for this small stack; no optional skill was installed. Reassess a specific corrected source when a real DE lab exposes a gap.

## Security and next task

Live Databricks operations require a suitable CLI, workspace access, a user-selected profile, and appropriate permissions. Authentication is documented only; no real credential was configured. No cloud resources, commits, pushes, or global configuration changes were performed. Vendored examples may show placeholder credentials; do not replace them with real secrets in tracked files.

The next repository task is to create the handbook/lab directory layout and choose a GitHub Pages documentation framework, then establish documentation build/link checks. That is separate from this skill setup; this empty project has no course or Pages build to verify yet.
