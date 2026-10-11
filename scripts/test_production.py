"""LOCAL SPARK/DELTA evidence. Plans/layout/quality/publication boundary, no cloud."""
import ast
import json
import os
from pathlib import Path
import sys
import unittest

def main():
    if not os.environ.get("SPARK_LAB_CONTAINER"):
        from spark_runtime import launch
        return launch("scripts/test_production.py", delta=True)
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from scripts.production_evidence import source_hashes, ROOT
    from labs.spark.common import run_directory, session, plan, groups, stage_summary, write_json
    from labs.production.src import transforms as T
    from labs.production.model import silver as pure_silver, gold as pure_gold
    from pyspark.sql import functions as F
    hashes = source_hashes()
    out = run_directory("tests-production")
    captured = dict(evidenceTier="LOCAL SPARK / LOCAL DELTA", workspaceStatus="PENDING USER WORKSPACE",
                    scope="Tiny controlled datasets; no production speedup or managed engine proof")
    with session("production-hardening", out) as spark:
        spark.conf.set("spark.sql.session.timeZone", "UTC")
        spark.conf.set("spark.sql.autoBroadcastJoinThreshold", "-1")
        fixture = json.loads((ROOT / "labs/production/src/fixtures.json").read_text())
        raw = spark.createDataFrame(fixture["events"], "delivery_id string,source_system string,app_id string,event_id string,revision int,campaign_id string,event_date string,currency string,amount_cents long")
        costs = spark.createDataFrame(fixture["costs"], "source_system string,app_id string,event_date string,campaign_id string,currency string,cost_cents long")
        canonical = lambda df: sorted([r.asDict() for r in df.collect()], key=lambda r: json.dumps(r, sort_keys=True))
        class Production(unittest.TestCase):
            def test_01_plan_diagnosis(self):
                base = spark.range(0, 4000, 1, 4).withColumn("campaign", (F.col("id") % 20).cast("int"))
                dim = spark.range(20).select(F.col("id").cast("int").alias("campaign"), F.lit("name").alias("label"))
                examples = {"filter-select": base.filter("id < 100").select("id"),
                            "aggregate": base.groupBy("campaign").count(),
                            "shuffle-join": base.join(dim, "campaign"),
                            "broadcast-join": base.join(F.broadcast(dim), "campaign")}
                captured["plans"] = {}
                for name, df in examples.items():
                    df.collect()
                    text = plan(df, out, name)
                    physical = text.split("== Physical Plan ==")[-1]
                    captured["plans"][name] = dict(exchange="Exchange" in physical,
                                                   broadcast="BroadcastHashJoin" in physical)
                self.assertFalse(captured["plans"]["filter-select"]["exchange"])
                self.assertTrue(captured["plans"]["aggregate"]["exchange"])
                self.assertTrue(captured["plans"]["shuffle-join"]["exchange"])
                self.assertTrue(captured["plans"]["broadcast-join"]["broadcast"])
                spark.conf.set("spark.sql.adaptive.enabled", "true")
                try:
                    adaptive = base.groupBy("campaign").count()
                    adaptive.collect()
                    adaptive_text = plan(adaptive, out, "adaptive-aggregate")
                    self.assertIn("AdaptiveSparkPlan", adaptive_text)
                    captured["adaptive"] = dict(finalPlan="isFinalPlan=true" in adaptive_text,
                                                 configured=True)
                finally:
                    spark.conf.set("spark.sql.adaptive.enabled", "false")

            def test_02_skew_and_semantic_repair(self):
                hot = spark.range(10000).withColumn("campaign", F.when(F.col("id") < 9000, "UNKNOWN").otherwise(F.concat(F.lit("C"), (F.col("id") % 20).cast("string"))))
                moved = hot.repartition(4, "campaign")
                distribution = groups(moved)
                self.assertGreater(max(r["rows"] for r in distribution), 9000)
                self.assertEqual(sum(r["rows"] for r in distribution), 10000)
                plan(moved.groupBy("campaign").count(), out, "skew")
                total = moved.groupBy("campaign").count().agg(F.sum("count")).first()[0]
                # Aggregation splits hot work while preserving the aggregation algebra.
                salted = hot.withColumn("salt", (F.col("id") % 8).cast("int"))
                partial = salted.groupBy("campaign", "salt").count()
                repaired = partial.groupBy("campaign").agg(F.sum("count").alias("count"))
                self.assertEqual(canonical(repaired), canonical(hot.groupBy("campaign").count()))
                captured["skew"] = dict(distribution=distribution, hotKeyRows=9000, total=total,
                                        algebraPreserved=True, productionSpeedupProven=False)

            def test_03_small_file_layout(self):
                df = spark.range(4096).withColumn("event_day", (F.col("id") % 8).cast("int"))
                layouts = {}
                for name, parts in [("tiny", 32), ("compact", 2)]:
                    path = out / (name + "-delta")
                    df.repartition(parts).write.format("delta").mode("overwrite").save(str(path))
                    files = sorted(path.glob("*.parquet"))
                    full = spark.read.format("delta").load(str(path))
                    narrow = full.filter("event_day = 1").select("id")
                    self.assertEqual(narrow.count(), 512)
                    self.assertEqual(full.agg(F.sum("id")).first()[0], 4096*4095//2)
                    plan(narrow, out, name + "-scan")
                    log = json.loads((path / "_delta_log/00000000000000000000.json").read_text().splitlines()[-1])
                    actions = [json.loads(l) for l in (path / "_delta_log/00000000000000000000.json").read_text().splitlines()]
                    adds = [a["add"] for a in actions if "add" in a]
                    self.assertEqual(len(adds), len(files))
                    layouts[name] = dict(files=len(files), sizesBytes=[f.stat().st_size for f in files],
                                         planningPartitions=full.rdd.getNumPartitions(), selectedRows=512,
                                         addStatsPresent=all("stats" in a for a in adds))
                self.assertEqual((layouts["tiny"]["files"], layouts["compact"]["files"]), (32, 2))
                captured["layouts"] = layouts

            def test_04_transform_contract_and_reconciliation(self):
                clean = T.silver(raw)
                candidate = T.gold(clean, costs)
                expected = pure_gold(pure_silver([r.asDict() for r in raw.collect()]), [r.asDict() for r in costs.collect()])
                self.assertEqual(canonical(candidate), expected)
                self.assertEqual(clean.select(*T.KEY).distinct().count(), clean.count())
                self.assertEqual(candidate.select(*T.GRAIN).distinct().count(), candidate.count())
                expected_schema = ["source_system", "app_id", "event_date", "campaign_id", "currency", "revenue_cents", "cost_cents", "roas"]
                self.assertEqual(candidate.columns, expected_schema)
                self.assertEqual(candidate.schema["revenue_cents"].dataType.simpleString(), "bigint")
                self.assertEqual(candidate.schema["roas"].dataType.simpleString(), "double")
                self.assertEqual(candidate.agg(F.sum("revenue_cents"), F.sum("cost_cents")).first()[:], (1250,700))
                self.assertEqual(canonical(T.gold(T.silver(raw.union(raw)), costs)), expected)
                captured["gold"] = canonical(candidate)
                captured["schema"] = candidate.schema.jsonValue()

            def test_05_quality_and_expectation_predicates(self):
                bad = raw.limit(1).withColumn("event_id", F.lit(None).cast("string"))
                negative = raw.limit(1).withColumn("amount_cents", F.lit(-1).cast("long"))
                timestamp = raw.limit(1).withColumn("event_date", F.lit("invalid"))
                mixed = raw.union(bad).union(negative).union(timestamp)
                classified = T.classified(mixed)
                self.assertEqual(classified.filter("NOT is_valid").count(), 3)
                self.assertEqual(classified.filter("is_valid").count(), 6)
                self.assertEqual(T.conflicts(raw.union(raw.limit(1).withColumn("amount_cents", F.lit(999).cast("long")))).count(), 1)
                tree = ast.parse((ROOT / "labs/production/src/expectations.py").read_text())
                expressions = [n.args[1].value for n in ast.walk(tree) if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) and n.func.attr.startswith("expect")]
                with_country = mixed.withColumn("country", F.lit("UNKNOWN"))
                results = {expr: with_country.filter(~F.coalesce(F.expr(expr), F.lit(False))).count() for expr in expressions}
                self.assertEqual(sorted(results.values()), [1,1,9])
                captured["quality"] = dict(inputRows=9, validRows=6, quarantineRows=3,
                                            predicateViolations=results, platformExpectationExecuted=False)

            def test_06_unknown_cost_and_fanout(self):
                clean = T.silver(raw)
                missing = T.gold(clean, costs.filter("campaign_id <> 'B'"))
                self.assertEqual(missing.filter("cost_cents IS NULL").count(), 1)
                wrong = T.gold(clean, costs.union(costs))
                self.assertEqual(wrong.count(), 6)
                self.assertEqual(wrong.agg(F.sum("revenue_cents")).first()[0], 2500)
                captured["failures"] = dict(unknownCostRows=1, fanoutRows=6, fanoutRevenue=2500)

            def test_07_code_vs_data_rollback(self):
                from delta.tables import DeltaTable
                path = str(out / "release-delta")
                good = T.gold(T.silver(raw), costs)
                good.write.format("delta").mode("overwrite").save(path)
                wrong = good.withColumn("revenue_cents", F.col("revenue_cents") * 2)
                wrong.write.format("delta").mode("overwrite").save(path)
                # Selecting good code has no effect on already committed data.
                self.assertEqual(spark.read.format("delta").load(path).agg(F.sum("revenue_cents")).first()[0], 2500)
                DeltaTable.forPath(spark, path).restoreToVersion(0)
                self.assertEqual(canonical(spark.read.format("delta").load(path)), canonical(good))
                history = DeltaTable.forPath(spark, path).history().select("version", "operation").collect()
                self.assertEqual(history[0].operation, "RESTORE")
                self.assertEqual(history[0].version, 2)
                captured["rollback"] = dict(before=1250, badCommit=2500, afterRestore=1250, newVersion=2,
                                            scope="Local Delta files retained; no VACUUM, no downstream streaming")

            def test_08_failed_candidate_preserves_serving(self):
                good = T.gold(T.silver(raw), costs)
                serving, candidate = str(out / "serving"), str(out / "candidate")
                good.write.format("delta").mode("overwrite").save(serving)
                wrong = good.withColumn("revenue_cents", F.col("revenue_cents") * 2)
                wrong.write.format("delta").mode("overwrite").save(candidate)
                with self.assertRaisesRegex(ValueError, "RECONCILIATION_FAILED"):
                    if spark.read.format("delta").load(candidate).agg(F.sum("revenue_cents")).first()[0] != 1250:
                        raise ValueError("RECONCILIATION_FAILED")
                self.assertEqual(canonical(spark.read.format("delta").load(serving)), canonical(good))
                captured["publication"] = dict(rejectedCandidate=2500, servingRevenue=1250, originalPreserved=True)

        result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(Production))
        write_json(out / "result.json", captured)
    stages = stage_summary(out)
    tasks = []
    for file in (out / "events").rglob("events_*"):
        if not file.is_file():
            continue
        for line in file.read_text().splitlines():
            event = json.loads(line)
            if event.get("Event") == "SparkListenerTaskEnd":
                info, metrics = event["Task Info"], event.get("Task Metrics", {})
                tasks.append(dict(stage=event["Stage ID"], durationMs=info["Finish Time"]-info["Launch Time"],
                                  executorRunTimeMs=metrics.get("Executor Run Time",0),
                                  shuffleReadBytes=metrics.get("Shuffle Read Metrics",{}).get("Remote Bytes Read",0)+metrics.get("Shuffle Read Metrics",{}).get("Local Bytes Read",0),
                                  shuffleWriteBytes=metrics.get("Shuffle Write Metrics",{}).get("Shuffle Bytes Written",0),
                                  memorySpillBytes=metrics.get("Memory Bytes Spilled",0), diskSpillBytes=metrics.get("Disk Bytes Spilled",0)))
    write_json(out / "tasks.json", tasks)
    write_json(out / "test-summary.json", dict(tests=result.testsRun, success=result.wasSuccessful(),failures=len(result.failures),errors=len(result.errors),skipped=len(result.skipped),sourceHashes=hashes,sourceEncoding="UTF-8 LF",completedStages=len(stages)))
    print(f"Evidence: {out}; stages={len(stages)}; tasks={len(tasks)}; cloud=PENDING USER WORKSPACE")
    return 0 if result.wasSuccessful() and stages and tasks else 1

if __name__ == "__main__":
    raise SystemExit(main())
