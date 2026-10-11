---
title: Mid Gate · Performance Diagnosis
description: Rank falsifiable performance hypotheses from an unseen incident packet.
prev:
  text: Lab 36
  link: /labs/36-performance-case-study
next:
  text: Observability
  link: /production/37-observability-mental-model
---

# Mid Gate · Performance Diagnosis

Nộp evidence-ranked hypotheses và controlled experiment. Random tuning hoặc output sai khiến assessment NOT YET.

## Incident packet

Unseen synthetic case: daily conversion margin, source/app/day/campaign/currency grain. Freshness budget45m. Run yesterday12m, today39m, both SUCCESS. No live production timings are claimed.

```sql
SELECT f.app_id, f.event_date, f.campaign_id, SUM(f.amount_cents) AS revenue_cents
FROM callbacks f
JOIN campaigns d ON f.campaign_id = d.campaign_id
WHERE f.event_date >= DATE '2026-10-01'
GROUP BY f.app_id, f.event_date, f.campaign_id;
```

```text
Scan callbacks: ReadSchema includes 42 columns; partition filter event_date>=2026-10-01
Exchange hashpartitioning(campaign_id,200)
SortMergeJoin campaign_id
Exchange hashpartitioning(app_id,event_date,campaign_id,200)
HashAggregate
```

| Observation | Yesterday | Today |
|---|---|---|
| Source delivery rows | 20M | 21M |
| Scoped logical event identities | 18M | 18.5M |
| Joined rows | 20M | 36M |
| Active data files | 12000 | 160000 |
| Predicate selected input | 85% | 89% |
| Job queue/startup | 1m | 2m |
| Dominant shuffle stage | 7m | 30m |
| Task duration median / max | 18s / 90s | 22s / 1500s |
| Partition rows p0,p1,p2,p3 (sample) | 0.7M,0.8M,0.7M,0.8M | 0.5M,0.6M,12M,0.9M |
| Dimension rows / scoped distinct campaign keys | 30000 / 30000 | 32000 / 30000 |
| UNKNOWN campaign share | 15% | 65% |

Table values are diagnostic scenario excerpts; sampled partitions are not the whole population. No dimension byte size, spill measurement, detailed file stats or engine participation is supplied.

## Required submission

1. Define correctness contracts, source/currency scope and retry/revision handling needed before optimizing this query.
2. Rank at least four hypotheses. Cite each observation, counterevidence and missing measurement; separate proven flaw from suspected performance cause.
3. Annotate movement/join/aggregation in the plan and distinguish execution duration from task-time sum.
4. Propose one experiment per hypothesis with expected observation, output invariant, rollback condition and cost measurement.
5. Explain which changes are justified now and which require dimension size, stats or workspace evidence.
6. Explain weak selectivity, hot keys and small files separately; retain legitimate UNKNOWN data.

## Rubric

| Competency | Points | Required evidence |
|---|---|---|
| Correctness before tuning | 30 | Grain/key/cardinality and exact reconciliation |
| Ranked causal diagnosis | 30 | Facts, alternatives and falsifiable predictions |
| Plans and critical path | 15 | Movement plus task distribution |
| Controlled experiments | 15 | One variable, output checks and rollback |
| Platform/cost boundaries | 10 | No invented local speedup or universal engine fix |

PASS requires80/100 and no critical correctness violation. NOT YET: random cache/repartition/Photon changes, dropping UNKNOWN without a business contract, or asserting a bottleneck from file count alone. Submit reasoning without seeking a single canonical knob.
