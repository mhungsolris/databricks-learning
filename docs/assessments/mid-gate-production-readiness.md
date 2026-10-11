---
title: Mid Gate · Production Readiness
description: Review correctness, performance, quality, testing, observability, deployment and rollback.
prev:
  text: Lab 45
  link: /labs/45-release-rollback
next:
  text: Chapter46
  link: /iceberg/46-why-iceberg
---

# Mid Gate · Production Readiness

Review a flawed release proposal. PASS requires finding release blockers, choosing bounded corrections and specifying acceptance evidence across all seven domains.

## Release packet

Synthetic platform: callbacks15m → Bronze → Silver → Gold; cost hourly; mutable attribution72h; source retention7d. Airflow submits Jobs; BI reads Gold directly. Marketing requires provisional15m revenue; Finance finalized next day. No real workspace has been connected.

The team proposes these changes:

```text
Silver key: event_id, latest arrival wins
Gold join: campaign_id only, unknown cost converted to zero
Quality: drop invalid money, no quarantine, SUCCESS means dashboard fresh
Tests: five mocked functions, counts only, no candidate rejection test
Performance: UNKNOWN owns70% rows; every run repartition(1), enable Photon
Observability: failures only, total rows, duration; no source cutoff or release correlation
Deployment: dev/staging/prod point at one writable schema
CI: pull_request_target checks out PR head and deploys; prod environment has no reviewers
Identity: one broad service principal, federation accepts every branch
Rollback: redeploy old notebook; VACUUM retains1d; no downstream replay policy
```

```yaml
targets:
  dev:
    mode: development
    variables: {schema: shared_roas}
  staging:
    mode: production
    variables: {schema: shared_roas}
  prod:
    mode: production
    variables: {schema: shared_roas}
```

This YAML is assessment input with deliberate flaws, not the runnable course bundle. A sample query shows revenue rising1250→2500 after a dimension change; Jobs remains SUCCESS. The team claims cloud readiness based on local tests alone.

## Review deliverables

1. Correctness: scope keys, deterministic versions/conflicts, reporting grain, source retention, candidate publication and reconciliation.
2. Performance: rank hypotheses using plan/distribution/layout evidence; specify missing task/IO metrics and cost tests.
3. Quality: per-rule business semantics, loss accounting/quarantine, unknown-cost policy and separate freshness cutoffs.
4. Testing: unit, DataFrame/schema, integration, reconciliation, real-data and workspace acceptance with failure cases.
5. Observability: four layers, correlated releases/cutoffs, owners, thresholds and containment actions.
6. Deployment: reviewable bundle targets, deploy/run identities, permissions, branch/OIDC trust, protected environments and promotion tests.
7. Rollback: code/config state, data repair/version availability, retention, affected scopes and downstream replay/reconciliation.

Provide a blocker table with flaw, impact, corrected design, required evidence and owner. Reference the [ROAS bundle lab](/labs/43-declarative-automation-bundles) and [production evidence](/labs/production-evidence), preserving local/cloud distinctions.

## Rubric

Each domain scores0-10:0 missing;5 identifies risk;10 defends correction and a falsifiable acceptance test. Add10 points for evidence-tier honesty and10 for release containment/promotion policy. Total90.

PASS requires72/90, every domain at least5 and no unresolved critical wrong-data/identity/publication blocker. NOT YET: feature checklist, cloud claims without execution, code rollback presented as data repair, or unsafe privileged PR execution. A hybrid Airflow/dbt solution is valid when ownership and contracts are explicit.
