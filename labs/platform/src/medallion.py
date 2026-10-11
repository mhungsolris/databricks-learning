"""Lakeflow pipeline source. Workspace execution required; no local SDP claim."""
from pyspark import pipelines as dp

source_catalog = spark.conf.get("course.source_catalog")
source_schema = spark.conf.get("course.source_schema")

@dp.materialized_view(name="bronze_events")
@dp.expect_or_fail("valid_money", "amount_cents >= 0 AND currency = 'USD'")
@dp.expect_or_fail("valid_identity", "source_system IS NOT NULL AND app_id IS NOT NULL AND event_id IS NOT NULL")
def bronze_events():
    return spark.read.table(f"`{source_catalog}`.`{source_schema}`.raw_events")

@dp.materialized_view(name="silver_events_pipeline")
def silver_events_pipeline():
    return spark.sql("""
      WITH ranked AS (
        SELECT *, ROW_NUMBER() OVER (
          PARTITION BY source_system, app_id, event_id
          ORDER BY revision DESC, delivery_id DESC
        ) AS rn FROM bronze_events
      )
      SELECT source_system, app_id, event_id, revision, campaign_id,
             event_date, currency, amount_cents
      FROM ranked WHERE rn = 1
    """)

@dp.materialized_view(name="gold_campaign_pipeline")
def gold_campaign_pipeline():
    return spark.sql("""
      SELECT source_system, app_id, event_date, campaign_id, currency,
             SUM(amount_cents) AS revenue_cents, COUNT(*) AS events
      FROM silver_events_pipeline
      GROUP BY source_system, app_id, event_date, campaign_id, currency
    """)
