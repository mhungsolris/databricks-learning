---
title: Mid Gate · Platform and Lakehouse System Design
description: Defend platform, format, catalog and operating ownership from requirements.
prev:
  text: Lab60
  link: /labs/60-system-design-cases
next: false
---

# Mid Gate · Platform and Lakehouse System Design

PASS does not require selecting Databricks. A defensible rejection can receive full marks. Submit a decision, alternatives and acceptance evidence; features alone earn no architecture score.

## Business brief

Synthetic organization: 10 TB historical data, 20 GB/day growth, hourly dashboard, some near-real-time events, Python/SQL team, current GCP, possible ML later. Finance requires governance; executive asks to use Databricks.

Current source rates, user-visible latency, correction horizon, recovery objectives, budget, team size and exact governance controls are not supplied. State questions and safe provisional assumptions; do not invent them as measured facts.

## Deliverables

1. Clarify business SLA, source delay, finalized/provisional metrics and recovery.
2. Determine whether Databricks solves an identified gap.
3. Choose warehouse/lakehouse and table format, with assumptions.
4. Define storage ownership, lifecycle, retention and historical repair.
5. Choose orchestration, retry/backfill boundaries and writer authority.
6. Define governance/IAM enforcement across engines and denied-access tests.
7. Discuss Delta/Iceberg metadata, mutations and reader-feature compatibility.
8. Trace catalog resolution, metadata, data and interoperability freshness.
9. Identify compute, maintenance, egress, staffing and migration risks.
10. Present at least two viable alternatives with rejection/reversal conditions.

Submit one architecture diagram, a requirement→importance→implication scorecard, a two-page maximum decision record, a failure/owner table and an acceptance plan. Runtime output is optional; version-qualified official sources and explicit requirements are valid ARCHITECTURE EVIDENCE.

## Rubric

Each deliverable scores0-10: 0 absent/unsupported; 5 plausible but missing a boundary or test; 10 explicit requirements, trade-off, owner and falsifiable acceptance. Total100.

PASS:≥80/100, each item≥5, and no critical format/catalog/platform conflation, governance bypass, unqualified performance claim or migration without business justification. NOT YET: executive preference treated as technical requirement, speculative ML used as universal justification, or open format equated with complete portability.

Any platform can earn full marks if the evidence meets the rubric. A stay-BigQuery decision, Databricks pilot, Snowflake design, Fabric design or open lakehouse must face the same constraints and uncertainty. Current sources: [support ledger](/iceberg/current-platform-support).
