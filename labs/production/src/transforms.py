"""Pure DataFrame transformations for a retained full snapshot, no IO actions."""
from pyspark.sql import Window, functions as F

KEY = ["source_system", "app_id", "event_id"]
GRAIN = ["source_system", "app_id", "event_date", "campaign_id", "currency"]

def classified(df):
    valid = (F.col("event_id").isNotNull() & (F.length("event_id") > 0)
             & F.col("source_system").isNotNull() & (F.length("source_system") > 0)
             & F.col("app_id").isNotNull() & (F.length("app_id") > 0)
             & F.col("amount_cents").isNotNull() & (F.col("amount_cents") >= 0)
             & (F.col("currency") == "USD") & (F.col("revision") >= 1)
             & F.expr("try_cast(event_date AS DATE) IS NOT NULL"))
    return df.withColumn("is_valid", F.coalesce(valid, F.lit(False)))

def conflicts(df):
    return (df.groupBy(*KEY, "revision")
            .agg(F.countDistinct(F.struct(*GRAIN, "amount_cents")).alias("payloads"))
            .filter("payloads > 1"))

def silver(df):
    w = Window.partitionBy(*KEY).orderBy(F.desc("revision"), F.desc("delivery_id"))
    return df.withColumn("_rank", F.row_number().over(w)).filter("_rank = 1").drop("_rank")

def revenue(df):
    return df.groupBy(*GRAIN).agg(F.sum("amount_cents").alias("revenue_cents"))

def gold(events, costs):
    # Full outer keeps unsupported/missing cost visible to the publication gate.
    return (revenue(events).join(costs, GRAIN, "full")
            .withColumn("revenue_cents", F.coalesce("revenue_cents", F.lit(0)))
            .withColumn("roas", F.when(F.col("cost_cents") > 0, F.col("revenue_cents") / F.col("cost_cents"))))
