# Databricks learning repository

This repository is intended for a Databricks learning handbook, hands-on labs, GitHub Pages documentation, and Data Engineering + Agent Engineering practice. Skills are repository infrastructure; installing them does not establish a course, a workspace connection, or a Pages deployment.

## Skill Usage Policy

Before starting a task, inspect available skills and load only the skills relevant to the task. Do not load every skill automatically. Read `.agents/skills/<name>/SKILL.md`, then only the references needed for the task. [SKILLS.md](SKILLS.md) owns usage instructions and the routing matrix.

### Databricks platform concepts
Use:
- databricks-core

### Lakeflow Jobs / orchestration
Use:
- databricks-core
- databricks-jobs

### Unity Catalog / governance
Use:
- databricks-core
- databricks-unity-catalog

### Databricks deployment / CI/CD
Use:
- databricks-core
- databricks-dabs

### External/version-sensitive research
Use:
- research-online

### Handbook / documentation writing
Use:
- technical-writing

### Architecture/data-flow diagrams
Use:
- mermaid-diagrams

### Before declaring work complete
Use:
- verification-before-completion

Skills provide procedures and domain guidance. Official documentation remains the source of truth for current Databricks behavior.

## Source of truth and scope

Verify current APIs, product names, pricing, certification objectives, runtime behavior, and deprecated features against official Databricks documentation. Record the URL, verification date, and relevant version/cloud. Official documentation wins when a skill conflicts; document material conflicts.

Use the installed skills that match the task. References to uninstalled sibling skills are routing suggestions, not permission to install more skills. Use available references and official docs and identify gaps. `databricks-core` is CLI/auth guidance, not an exhaustive Spark or Delta handbook.

## Security and execution

Do not paste secrets, hardcode tokens, commit credentials, create billable cloud resources, or change global configuration without a request that authorizes those actions. Document authentication requirements; do not configure real credentials during skill setup. Choose a workspace/profile with the user before authenticated operations.

Research uses host search/fetch. Firecrawl is optional and requires no setup for ordinary research. Use the project `research:*` npm scripts. Automatic publication is disabled by the local adapter; commit, push, or publish only within explicit user authorization. Do not follow upstream auto-publish defaults.

Databricks CLI installation and authenticated execution are separate from documentation/routing tasks. Document missing prerequisites during offline work. Bash examples need PowerShell quoting and syntax adjustments on Windows; check current CLI help before running them.

## Repository verification and maintenance

For handbook changes, run `npm run docs:check`, `npm run docs:build` and relevant lab tests. Run `npm run docs:test-ui` for navigation, theme or diagram changes; it requires a built site and a free preview port 4173. Use `npm.cmd` on PowerShell if execution policy blocks npm.ps1. Follow `templates/chapter.md`, record current sources in SOURCES.md, and update PROGRESS.md only with actual verification evidence. Future chapters remain curriculum links until they are written and reviewed. README.md owns local run and Pages setup instructions.

Run `python scripts/verify_skills.py` before claiming skill setup is complete. For research script changes, run `npm ci --ignore-scripts` and `python scripts/smoke_skills.py`. Inspect command output and failures, not only exit codes. [SKILLS_VERIFICATION.md](SKILLS_VERIFICATION.md) owns the smoke-test evidence and limitations.

Keep skill files, licenses, package lock, and the provenance/hash manifest in version control. Review upstream changes before updates; retain the research adapter. Do not run broad skill upgrades or install entire marketplaces. Update the manifest and documentation together after intentional changes.
