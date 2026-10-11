"""LOCAL SPARK TEST. Actual SELECT logic, no Jobs/SDP/UC/warehouse execution."""
import json
import os
from pathlib import Path
import sys
import unittest

def main():
    if not os.environ.get("SPARK_LAB_CONTAINER"):
        from spark_runtime import launch
        return launch("scripts/test_platform.py")
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from scripts.platform_evidence import source_hashes
    from labs.platform.contracts import BASE, load, sql_constants
    from labs.spark.common import run_directory, session, stage_summary, write_json
    from pyspark.sql import functions as F
    recorded_hashes = source_hashes()
    out = run_directory("tests-platform")
    captured = {"evidenceTier": "LOCAL SPARK TEST", "workspaceStatus": "PENDING USER WORKSPACE",
                "scope": "SELECT semantics only; notebook DDL converted to temporary views"}
    with session("platform-sql-contracts", out) as spark:
        spark.conf.set("spark.sql.session.timeZone", "UTC")
        fixture = load("fixtures.json")
        raw = spark.createDataFrame(fixture["events"], "delivery_id string,source_system string,app_id string,event_id string,revision int,campaign_id string,event_date string,currency string,amount_cents long")
        raw = raw.withColumn("event_date", F.to_date("event_date"))
        costs = spark.createDataFrame(fixture["costs"], "source_system string,app_id string,event_date string,campaign_id string,currency string,cost_cents long").withColumn("event_date", F.to_date("event_date"))
        raw.createOrReplaceTempView("raw_events")
        costs.createOrReplaceTempView("costs")
        def refresh():
            spark.sql((BASE / "sql/silver.sql").read_text()).createOrReplaceTempView("silver_events")
            spark.sql((BASE / "sql/gold.sql").read_text()).createOrReplaceTempView("gold_roas")
        refresh()
        dimension = spark.createDataFrame([("callback","a","A","Acquisition A"),("callback","a","B","Retention B"),("callback","b","A","App B acquisition")],
                                          "source_system string,app_id string,campaign_id string,campaign_name string")
        dimension.createOrReplaceTempView("campaign_dim")
        serving = [q.strip() for q in (BASE / "sql/serving.sql").read_text().split(";") if q.strip()]
        def canonical(df):
            return sorted([json.loads(json.dumps(r.asDict(), default=str)) for r in df.collect()],
                          key=lambda r: json.dumps(r, sort_keys=True))
        class Contracts(unittest.TestCase):
            def test_01_scoped_retry_and_revision(self):
                self.assertEqual(spark.table("silver_events").count(), 4)
                total = spark.sql("SELECT SUM(amount_cents) FROM silver_events").first()[0]
                self.assertEqual(total, 1250)
                first = canonical(spark.table("gold_roas"))
                refresh()
                self.assertEqual(first, canonical(spark.table("gold_roas")))
                captured["silver"] = canonical(spark.table("silver_events"))
                captured["gold"] = first

            def test_02_serving_four_queries(self):
                results = [canonical(spark.sql(q)) for q in serving]
                self.assertEqual(len(results), 4)
                aggregate = results[0][0]
                self.assertEqual((aggregate["revenue_cents"],aggregate["cost_cents"]), (1250,700))
                self.assertAlmostEqual(aggregate["roas"], 1250/700)
                self.assertEqual([len(r) for r in results], [1,1,3,2])
                captured["serving"] = results

            def test_03_dimension_fanout_counterexample(self):
                wrong = spark.sql(serving[2].replace("campaign_dim d", "(SELECT * FROM campaign_dim UNION ALL SELECT * FROM campaign_dim) d"))
                self.assertEqual(wrong.count(), 6)
                self.assertEqual(wrong.agg(F.sum("revenue_cents")).first()[0], 2500)
                captured["failureFanout"] = {"rows": 6, "revenueCents": 2500}

            def test_04_zero_cost_policy(self):
                original = costs
                costs.withColumn("cost_cents", F.lit(0).cast("long")).createOrReplaceTempView("costs")
                try:
                    result = spark.sql((BASE / "sql/gold.sql").read_text())
                    self.assertTrue(all(r.roas is None for r in result.collect()))
                    captured["zeroCost"] = {"rows": 3, "allRoasNull": True}
                finally:
                    original.createOrReplaceTempView("costs")
                    refresh()

            def test_05_actual_notebook_queries(self):
                queries = sql_constants("src/roas_task.py")
                for query in queries:
                    if "CREATE OR REPLACE TABLE" in query:
                        spark.sql(query.replace("CREATE OR REPLACE TABLE", "CREATE OR REPLACE TEMP VIEW"))
                self.assertEqual(canonical(spark.table("gold_roas")), captured["gold"])
                validations = [q for q in queries if "HAVING" in q]
                self.assertEqual(len(validations), 2)
                self.assertTrue(all(spark.sql(q).count() == 0 for q in validations))
                raw.union(raw.filter("delivery_id = 'd1'").withColumn("amount_cents", F.lit(999).cast("long"))).createOrReplaceTempView("raw_events")
                try:
                    conflict = next(q for q in validations if "Conflicting" not in q and "revision" in q)
                    self.assertEqual(spark.sql(conflict).count(), 1)
                    captured["equalRevisionConflict"] = {"groupsRejected": 1}
                finally:
                    raw.createOrReplaceTempView("raw_events")
                    refresh()

            def test_06_pipeline_query_semantics(self):
                raw.createOrReplaceTempView("bronze_events")
                queries = sql_constants("src/medallion.py")
                spark.sql(queries[0]).createOrReplaceTempView("silver_events_pipeline")
                result = spark.sql(queries[1])
                self.assertEqual(result.count(), 3)
                self.assertEqual(result.agg(F.sum("revenue_cents")).first()[0], 1250)
                captured["pipelineQuery"] = canonical(result)
                self.assertEqual(raw.filter("amount_cents < 0").count(), 0)
                bad = raw.withColumn("amount_cents", F.when(F.col("delivery_id") == "d1", -1).otherwise(F.col("amount_cents")))
                self.assertEqual(bad.filter("amount_cents < 0").count(), 1)
                captured["expectationInputCounterexample"] = {"invalidRows": 1, "platformExpectationExecuted": False}

        result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(Contracts))
        write_json(out / "result.json", captured)
    stages = stage_summary(out)
    write_json(out / "test-summary.json", {"tests": result.testsRun, "success": result.wasSuccessful(),
                "failures": len(result.failures), "errors": len(result.errors), "skipped": len(result.skipped),
                "sourceHashes": recorded_hashes, "sourceEncoding": "UTF-8 LF", "completedStages": len(stages)})
    print(f"Evidence: {out}; stages={len(stages)}; workspace=PENDING USER WORKSPACE")
    return 0 if result.wasSuccessful() and stages else 1

if __name__ == "__main__":
    raise SystemExit(main())
