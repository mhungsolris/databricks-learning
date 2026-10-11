# Databricks notebook source
"""Bounded synthetic snapshot lab. Every task selects a stage and shares durable tables."""
import re

for name, default in (("catalog", ""), ("schema", ""), ("stage", ""),
                      ("force_validation_failure", "false")):
    dbutils.widgets.text(name, default)
catalog, schema, stage = [dbutils.widgets.get(name) for name in ("catalog", "schema", "stage")]
for identifier in (catalog, schema):
    if not re.fullmatch(r"[A-Za-z][A-Za-z0-9_]*", identifier):
        raise ValueError("Choose simple catalog/schema identifiers for this bounded lab")
if not schema.startswith("course_roas_"):
    raise ValueError("Use a unique course_roas_ schema owned by the learner")
spark.sql(f"USE CATALOG `{catalog}`")
spark.sql(f"CREATE SCHEMA IF NOT EXISTS `{schema}`")
spark.sql(f"USE SCHEMA `{schema}`")

if stage == "ingest_revenue":
    spark.sql("""
      CREATE OR REPLACE TABLE raw_events AS SELECT
        delivery_id, source_system, app_id, event_id, revision, campaign_id,
        CAST(event_date AS DATE) AS event_date, currency, CAST(amount_cents AS BIGINT) AS amount_cents
      FROM VALUES
        ('d1','callback','a','E1',1,'A','2026-10-01','USD',300),
        ('d2','callback','a','E1',1,'A','2026-10-01','USD',300),
        ('d3','callback','a','E2',1,'A','2026-10-01','USD',700),
        ('d4','callback','a','E2',2,'A','2026-10-01','USD',800),
        ('d5','callback','a','E3',1,'B','2026-10-01','USD',100),
        ('d6','callback','b','E1',1,'A','2026-10-01','USD',50)
      AS e(delivery_id,source_system,app_id,event_id,revision,campaign_id,event_date,currency,amount_cents)
    """)
    dbutils.jobs.taskValues.set(key="raw_rows", value=6)
elif stage == "ingest_cost":
    spark.sql("""
      CREATE OR REPLACE TABLE costs AS SELECT source_system, app_id,
        CAST(event_date AS DATE) AS event_date, campaign_id, currency,
        CAST(cost_cents AS BIGINT) AS cost_cents FROM VALUES
        ('callback','a','2026-10-01','A','USD',400),
        ('callback','a','2026-10-01','B','USD',200),
        ('callback','b','2026-10-01','A','USD',100)
      AS c(source_system,app_id,event_date,campaign_id,currency,cost_cents)
    """)
elif stage == "validate":
    if dbutils.widgets.get("force_validation_failure").lower() == "true":
        raise ValueError("INTENTIONAL_VALIDATION_FAILURE")
    assert spark.table("raw_events").count() == 6
    assert spark.sql("SELECT * FROM raw_events WHERE amount_cents < 0 OR currency <> 'USD' OR event_id IS NULL").count() == 0
    assert spark.sql("""
      SELECT source_system,app_id,event_id,revision FROM raw_events
      GROUP BY source_system,app_id,event_id,revision
      HAVING COUNT(DISTINCT struct(campaign_id,event_date,currency,amount_cents)) > 1
    """).count() == 0, "Conflicting equal revision"
    assert spark.sql("""
      SELECT source_system,app_id,event_date,campaign_id,currency FROM costs
      GROUP BY source_system,app_id,event_date,campaign_id,currency HAVING COUNT(*) > 1
    """).count() == 0, "Duplicate cost grain"
elif stage == "silver":
    spark.sql("""
      CREATE OR REPLACE TABLE silver_events AS
      WITH ranked AS (
        SELECT *, ROW_NUMBER() OVER (
          PARTITION BY source_system,app_id,event_id ORDER BY revision DESC,delivery_id DESC
        ) AS rn FROM raw_events
      )
      SELECT source_system,app_id,event_id,revision,campaign_id,event_date,currency,amount_cents
      FROM ranked WHERE rn = 1
    """)
elif stage == "gold":
    spark.sql("""
      CREATE OR REPLACE TABLE gold_roas AS
      WITH revenue AS (
        SELECT source_system,app_id,event_date,campaign_id,currency,
               SUM(amount_cents) AS revenue_cents,COUNT(*) AS events
        FROM silver_events GROUP BY source_system,app_id,event_date,campaign_id,currency
      )
      SELECT c.source_system,c.app_id,c.event_date,c.campaign_id,c.currency,
             COALESCE(r.revenue_cents,0) AS revenue_cents,c.cost_cents,COALESCE(r.events,0) AS events,
             CASE WHEN c.cost_cents=0 THEN NULL
                  ELSE CAST(COALESCE(r.revenue_cents,0) AS DOUBLE)/c.cost_cents END AS roas
      FROM costs c LEFT JOIN revenue r USING (source_system,app_id,event_date,campaign_id,currency)
    """)
elif stage == "reconcile":
    assert spark.table("silver_events").count() == 4
    result = spark.sql("SELECT COUNT(*) AS n,SUM(revenue_cents) AS r,SUM(cost_cents) AS c FROM gold_roas").first()
    assert (result.n,result.r,result.c) == (3,1250,700)
    actual = {(r.app_id,r.campaign_id): (r.revenue_cents,r.cost_cents) for r in spark.table("gold_roas").collect()}
    assert actual == {("a","A"):(1100,400),("a","B"):(100,200),("b","A"):(50,100)}
    print("RECONCILED_SYNTHETIC_SNAPSHOT")
elif stage == "failure_report":
    print("Failure branch ran. Inspect upstream states; no external notification is configured.")
else:
    raise ValueError(f"Unknown stage: {stage}")
