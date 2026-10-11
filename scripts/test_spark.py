"""Explicit integration suite; never silently substitutes SQLite for Spark."""
import argparse
import os
from pathlib import Path
import sys
import unittest


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--delta', action='store_true')
    args = parser.parse_args()
    if not os.environ.get('SPARK_LAB_CONTAINER'):
        from spark_runtime import launch
        return launch('scripts/test_spark.py', sys.argv[1:], delta=args.delta)
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from labs.spark.common import run_directory, session, stage_summary, plan
    from labs.spark.experiments import LABS
    from pyspark.sql import functions as F
    out = run_directory('tests-delta' if args.delta else 'tests-spark')
    with session('handbook-contract-tests', out) as spark:
        class Contracts(unittest.TestCase):
            def test_runtime(self):
                self.assertEqual((spark.version, spark.sparkContext.master), ('4.0.4', 'local[*]'))
                self.assertEqual(spark.sql('SELECT 6 * 7').first()[0], 42)

            def test_execution_and_examples(self):
                for number in (['08'] if args.delta else ['03', '04', '05', '06', '07']):
                    with self.subTest(lab=number):
                        folder = out / ('lab' + number)
                        folder.mkdir()
                        result = LABS[number](spark, folder)
                        self.assertTrue(result)

            def test_repartition_preserves_ids_with_empty_partitions(self):
                original = spark.range(7, numPartitions=2)
                changed = original.repartition(11)
                self.assertEqual(changed.rdd.getNumPartitions(), 11)
                self.assertEqual(sorted(r.id for r in changed.collect()), list(range(7)))
                self.assertEqual(sorted(r.id for r in original.coalesce(1).collect()), list(range(7)))

            def test_many_to_many_join_is_not_fixed_by_broadcast(self):
                left = spark.createDataFrame([('A', 10), ('A', 20)], 'key string, revenue long')
                right = spark.createDataFrame([('A', 'x'), ('A', 'y'), ('A', 'z')], 'key string, source string')
                wrong = left.join(F.broadcast(right), 'key')
                self.assertEqual((wrong.count(), wrong.agg(F.sum('revenue')).first()[0]), (6, 90))

            def test_empty_parquet_and_no_match_filter(self):
                path = str(out / 'empty-parquet')
                spark.createDataFrame([], 'id long, payload string').write.parquet(path)
                read = spark.read.parquet(path)
                self.assertEqual(read.schema.simpleString(), 'struct<id:bigint,payload:string>')
                self.assertEqual(read.select('id').filter('id > 100').count(), 0)
                text = plan(read.select('id'), out, 'empty-projection')
                self.assertNotIn('payload', text.split('ReadSchema:')[1])

        suite = unittest.defaultTestLoader.loadTestsFromTestCase(Contracts)
        result = unittest.TextTestRunner(verbosity=2).run(suite)
    stages = stage_summary(out)
    print(f'Evidence: {out}; stages={len(stages)}')
    return 0 if result.wasSuccessful() and stages else 1


if __name__ == '__main__':
    raise SystemExit(main())
