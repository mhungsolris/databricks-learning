---
title: 'Lab 29 · SQL serving'
prev:
  text: 'Chapter 29'
  link: /platform/29-databricks-sql
next:
  text: 'Chapter 30'
  link: /platform/30-platform-boundaries
---

# Lab 29 · SQL serving

DATABRICKS FREE EDITION LAB using the existing small warehouse, PENDING USER WORKSPACE. LOCAL SPARK TEST executes the same bounded SELECT logic and counterexamples.

1. Complete Lab26 so gold_roas exists in the owned schema. The notebook output is not warehouse evidence.
2. Select the existing SQL warehouse and qualified catalog/schema in SQL editor. Check warehouse usage permission plus UC traversal/SELECT.
3. Run the four statements in labs/platform/sql/serving.sql: aggregation, filter, dimension join and dashboard-oriented campaign query. Create the owned sample dimension first:

```sql
CREATE OR REPLACE TABLE campaign_dim AS
SELECT * FROM VALUES
  ('callback','a','A','Acquisition A'),
  ('callback','a','B','Retention B'),
  ('callback','b','A','App B acquisition')
AS d(source_system, app_id, campaign_id, campaign_name);
```

4. Verify aggregate revenue1250/cost700 and ratio1250/700; filter a/A is one row; the dimension join keeps three rows. A missing/duplicate dimension violates its contract. Keep currency in grouping.
5. Save a dashboard-oriented query; optionally build a small private visualization if the feature is available. Inspect query history/profile: query status, execution/queue information and plan where exposed. Capture redacted query outputs and history, not workspace IDs.
6. Discuss how size, concurrency, auto-stop, table layout and caching might affect representative BI work. Do not benchmark Databricks against BigQuery with this fixture. Stop extra queries and use warehouse auto-stop.

If SQL/history/dashboards are unavailable, document feature-specific pending status. PASS: output/BI grain and architecture are explained, warehouse evidence separate from local SQL. NOT YET: query success or tiny-data speed claimed as production performance.

