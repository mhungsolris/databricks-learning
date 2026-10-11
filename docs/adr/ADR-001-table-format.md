---
title: ADR-001 · ROAS table format and partner reads
description: A conditional architecture decision for a Delta ROAS estate with an Iceberg reader.
---

# ADR-001 · ROAS table format and partner reads

Status: conditional teaching decision, dated 2026-10-11. Scope: the synthetic existing ROAS estate and a proposed read-only partner consumer. This is ARCHITECTURE EVIDENCE, not a workspace rollout approval.

## Requirements and assumptions

Existing Delta pipeline semantics and local recovery/reconciliation tests are valuable. Revenue/cost reporting must preserve scoped keys, deterministic revisions, integer money and source cutoffs. The partner needs read access through a supported Iceberg client, not write authority.

Assumptions to validate: selected reader supports required types/features; conversion lag fits the accepted freshness budget; governance can enforce partner access without uncontrolled storage bypass.

## Decision

Retain Delta as writer authority and pilot Databricks Iceberg reads/UniForm for the partner. Generate Iceberg metadata over the same Parquet data and monitor converted Delta version/timestamp. Do not migrate all tables only to provide one read consumer.

## Alternatives

| Alternative | Benefit | Rejection/acceptance condition |
|---|---|---|
| Native managed Iceberg | Native multi-engine supported write paths | Reevaluate if partner needs supported writes and compatible governance |
| Separate governed export | Independent consumer compatibility | Accept if exposure fails, with explicit copy/freshness cost |
| Rewrite entire estate | Common native format | Reject while no requirement offsets semantic/migration cost |

## Consequences and failures

Delta protocol/column-mapping compatibility, asynchronous generation and reader retention need ownership. A stale pinned metadata path can show old data or lose required files after cleanup. Partner writes through the read exposure are prohibited.

Platform team owns client/version/access preflight; data team owns source-cutoff reconciliation; operations owns lag/retention alerts. No authenticated configuration has been performed.

## Acceptance and reversal

Pilot compares exact scoped Gold output at the same source cutoff, required schemas/types, historical horizon and negative access tests. Observe conversion lag within the agreed partner budget under realistic write cadence.

Reverse to native Iceberg or export if a mandatory writer feature, access policy or freshness requirement cannot pass. Reader request growth alone does not prove that a full rewrite is necessary.

## Sources

[Current Iceberg reads requirements](https://docs.databricks.com/aws/en/delta/iceberg-reads), [UC external access boundaries](https://docs.databricks.com/aws/en/external-access/iceberg), verified 2026-10-11 AWS. [Format comparison](/iceberg/51-delta-vs-iceberg) and [production evidence](/labs/production-evidence) separate design from measured tests.
