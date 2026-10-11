---
title: 'Lab 27 · Declarative medallion'
prev:
  text: 'Chapter 27'
  link: /platform/27-declarative-pipelines
next:
  text: 'Chapter 28'
  link: /platform/28-unity-catalog
---

# Lab 27 · Declarative medallion

DATABRICKS FREE EDITION LAB, PENDING USER WORKSPACE. Prerequisite: successful Lab26 validation and retained raw_events input. PORTABLE TEST checks AST/source edges; LOCAL SPARK TEST checks SQL, not SDP engine.

1. Choose the same accessible catalog and owned schema. Review src/medallion.py and resources/medallion.pipeline.yml. A triggered serverless pipeline reads raw_events and publishes distinct bronze_events, silver_events_pipeline and gold_campaign_pipeline objects. Stop another active pipeline of this type if your account limit would block this owned exercise.
2. Validate config in the actual workspace or strict bundle CLI with your chosen profile. Start a bounded update. Inspect the **inferred** graph: raw_events → bronze_events → silver_events_pipeline → gold_campaign_pipeline. Compare it with the static expectation in Chapter27.
3. Check Bronze six deliveries, Silver four scoped business keys, Gold three aggregates totaling1250 cents. Check latest E2 revision2=800 and app-b E1=50; app-a E1=300. No cost join is part of this pipeline, so its Gold metric is campaign revenue rather than full ROAS.
4. Inject a negative amount into one owned raw row:

```sql
UPDATE raw_events SET amount_cents = -1 WHERE delivery_id = 'd1';
```

5. Run another update. Inspect failed expectation/flow, overall update state and which table versions remain queryable. Record actual behavior, without assuming all-table rollback or every independent flow stopped.
6. Restore d1=300, revalidate the retained snapshot, and update again. Confirm expected outputs and freshness. Never full-refresh a production stream without retained truth.
7. Capture redacted inferred graph, update/quality outputs, actual target invariants and environment. Stop extra updates.

This exercise uses batch materialized views. Row_number handles retained versions; upstream validation must reject conflicting equal revisions. Expectations are Lakeflow extensions, not OSS SDP features. Local Spark4.0.4 lacks the documented Spark4.1 SDP engine, so local runtime stays pinned.

PASS: explain graph derivation, object types and failure/output boundary, with workspace observations if available. NOT YET: AST test passed is described as a pipeline run.

