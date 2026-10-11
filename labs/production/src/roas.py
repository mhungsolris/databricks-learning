# Databricks notebook source
"""Manual sandbox snapshot exercise. NOT an ingestion connector or live ROAS release."""
import json
from pathlib import Path
import re
from pyspark.sql import functions as F
from transforms import classified, conflicts, silver, gold, KEY, GRAIN

for name, default in [("catalog", ""), ("schema", ""), ("force_failure", "false")]:
    dbutils.widgets.text(name, default)
catalog, schema = [dbutils.widgets.get(n) for n in ("catalog", "schema")]
if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", catalog) or not re.fullmatch(r"course_roas_(dev|staging|prod)_[A-Za-z0-9_]+", schema):
    raise ValueError("SANDBOX_NAMESPACE_REQUIRED")
spark.sql(f"USE CATALOG `{catalog}`")
spark.sql(f"USE SCHEMA `{schema}`")
fixture = json.loads((Path.cwd() / "fixtures.json").read_text())
raw = spark.createDataFrame(fixture["events"], "delivery_id string,source_system string,app_id string,event_id string,revision int,campaign_id string,event_date string,currency string,amount_cents long")
costs = spark.createDataFrame(fixture["costs"], "source_system string,app_id string,event_date string,campaign_id string,currency string,cost_cents long")
raw.write.format("delta").mode("overwrite").saveAsTable("bronze_snapshot")
costs.write.format("delta").mode("overwrite").saveAsTable("bronze_cost_snapshot")
tagged = classified(raw)
tagged.filter("NOT is_valid").write.format("delta").mode("overwrite").saveAsTable("quarantine_snapshot")
if tagged.filter("NOT is_valid").limit(1).count() or conflicts(raw).limit(1).count():
    raise ValueError("QUALITY_GATE_FAILED")
if costs.groupBy(*GRAIN).count().filter("count <> 1").limit(1).count() or costs.filter("cost_cents IS NULL OR cost_cents < 0").limit(1).count():
    raise ValueError("COST_GATE_FAILED")
clean = silver(raw)
clean.write.format("delta").mode("overwrite").saveAsTable("silver_snapshot")
candidate = gold(clean, costs)
candidate.write.format("delta").mode("overwrite").saveAsTable("gold_candidate")
actual = spark.table("gold_candidate")
totals = actual.agg(F.sum("revenue_cents"), F.sum("cost_cents")).first()
if actual.filter("cost_cents IS NULL").limit(1).count() or tuple(totals) != (1250, 700) or actual.count() != 3:
    raise ValueError("RECONCILIATION_FAILED")
expected = spark.createDataFrame([
    ("callback", "a", "2026-10-01", "A", "USD", 1100, 400, 1100/400),
    ("callback", "a", "2026-10-01", "B", "USD", 100, 200, 100/200),
    ("callback", "b", "2026-10-01", "A", "USD", 50, 100, 50/100)],
    "source_system string,app_id string,event_date string,campaign_id string,currency string,revenue_cents long,cost_cents long,roas double")
ordered = actual.select(*expected.columns)
if ordered.exceptAll(expected).limit(1).count() or expected.exceptAll(ordered).limit(1).count():
    raise ValueError("EXACT_SCOPED_RECONCILIATION_FAILED")
if dbutils.widgets.get("force_failure").lower() == "true":
    raise ValueError("INTENTIONAL_FAILURE_BEFORE_PUBLICATION")
# Atomic table replacement is the bounded publication boundary; multiple tables are not atomic.
spark.sql("CREATE OR REPLACE TABLE gold_roas USING DELTA AS SELECT * FROM gold_candidate")
print(json.dumps({"publication": "sandbox_snapshot", "revenue_cents": 1250, "cost_cents": 700}))
