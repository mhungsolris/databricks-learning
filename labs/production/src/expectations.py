"""DATABRICKS WORKSPACE example; locally checked syntax/SQL, never engine metrics."""
from pyspark import pipelines as dp
from pyspark.sql import functions as F

@dp.materialized_view
@dp.expect("known_country", "country <> 'UNKNOWN'")
def observed_events():
    return spark.read.table(spark.conf.get("course.quality_source"))

@dp.materialized_view
def quarantine_events():
    return spark.read.table(spark.conf.get("course.quality_source")).filter(
        "event_id IS NULL OR amount_cents IS NULL OR amount_cents < 0 OR try_cast(event_date AS DATE) IS NULL")

@dp.materialized_view
@dp.expect_or_drop("valid_money", "amount_cents IS NOT NULL AND amount_cents >= 0")
def disposable_telemetry():
    # Teaching contrast only: applying this loss policy to revenue requires approval.
    return spark.read.table(spark.conf.get("course.quality_source"))

@dp.materialized_view
@dp.expect_or_fail("valid_identity", "event_id IS NOT NULL")
def critical_events():
    return spark.read.table(spark.conf.get("course.quality_source"))
