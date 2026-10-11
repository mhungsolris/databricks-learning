import csv
from pathlib import Path
import tempfile
import unittest

from labs.foundations.grain_fanout import fixture, solution, verify_candidate, verify_query, WRONG_SQL, FIXED_SQL
from labs.foundations.layout_contract import generate, inspect
from labs.spark.pipeline_model import DeferredQuery, fixture as pipeline_fixture


class GrainContracts(unittest.TestCase):
    def test_wrong_join_is_rejected_and_repaired(self):
        with fixture() as conn:
            wrong = conn.execute(WRONG_SQL).fetchone()
            self.assertEqual(wrong[2:], (300, 1000))
            with self.assertRaisesRegex(ValueError, 'Metric contract'):
                verify_candidate(*wrong[2:])
            repaired = solution(conn)
            self.assertEqual(repaired, [('2026-10-01', 'A', 300, 500)])
            verify_candidate(*repaired[0][2:])
            with self.assertRaisesRegex(ValueError, 'Report contract'):
                verify_query(conn, WRONG_SQL)
            self.assertEqual(verify_query(conn, FIXED_SQL), repaired)

    def test_equal_spend_values_are_not_deduplicated_as_metrics(self):
        with fixture() as conn:
            conn.executescript("INSERT INTO transactions VALUES ('2026-10-01','B','T3',50); INSERT INTO ad_spend VALUES ('2026-10-01','B',500);")
            self.assertEqual(sum(row[3] for row in solution(conn)), 1000)

    def test_duplicate_dimension_grain_fails_before_join(self):
        with fixture() as conn:
            conn.execute("INSERT INTO ad_spend VALUES ('2026-10-01','A',500)")
            with self.assertRaisesRegex(ValueError, 'Duplicate grain'):
                solution(conn)

    def test_missing_spend_is_not_silently_dropped(self):
        with fixture() as conn:
            conn.execute("INSERT INTO transactions VALUES ('2026-10-01','B','T3',50)")
            with self.assertRaisesRegex(ValueError, 'Missing spend coverage'):
                solution(conn)

    def test_null_key_fails_contract(self):
        with fixture() as conn:
            conn.execute("INSERT INTO transactions VALUES ('2026-10-01','A',NULL,50)")
            with self.assertRaisesRegex(ValueError, 'Null key'):
                solution(conn)

    def test_creative_country_platform_changes_join_grain(self):
        with fixture() as conn:
            conn.executescript('''CREATE TABLE spend_detail (
                date TEXT,campaign TEXT,creative TEXT,country TEXT,platform TEXT,cost INTEGER);
              INSERT INTO spend_detail VALUES
                ('2026-10-01','A','C1','VN','ios',120),
                ('2026-10-01','A','C1','US','ios',80),
                ('2026-10-01','A','C2','VN','android',300);''')
            wrong = conn.execute('''SELECT COUNT(*),SUM(t.revenue),SUM(s.cost)
              FROM transactions t JOIN spend_detail s USING(date,campaign)''').fetchone()
            self.assertEqual(wrong, (6, 900, 1000))
            fixed = conn.execute('''WITH r AS (
              SELECT date,campaign,SUM(revenue) AS revenue FROM transactions GROUP BY date,campaign
            ), s AS (
              SELECT date,campaign,SUM(cost) AS cost FROM spend_detail GROUP BY date,campaign
            ) SELECT r.revenue,s.cost FROM r JOIN s USING(date,campaign)''').fetchall()
            self.assertEqual(fixed, [(300, 500)])

    def test_many_to_many_allocation_conserves_revenue(self):
        with fixture() as conn:
            conn.executescript('''CREATE TABLE attribution (transaction_id TEXT, creative TEXT, weight REAL);
              INSERT INTO attribution VALUES ('T1','C1',0.6),('T1','C2',0.4);''')
            raw = conn.execute('''SELECT SUM(revenue) FROM transactions JOIN attribution USING(transaction_id)''').fetchone()[0]
            allocated = conn.execute('''SELECT creative, SUM(revenue*weight)
              FROM transactions JOIN attribution USING(transaction_id) GROUP BY creative ORDER BY creative''').fetchall()
            self.assertEqual(raw, 200)
            self.assertEqual(allocated, [('C1', 60.0), ('C2', 40.0)])
            self.assertEqual(sum(amount for _, amount in allocated), 100)


class LayoutContracts(unittest.TestCase):
    def test_schema_change_fails_instead_of_inventing_revenue(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            generate(root)
            self.assertEqual(inspect(root), (3, 350))
            (root / 'part-2.csv').write_text('transaction_id,amount\nT3,50\n', encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'Schema mismatch'):
                inspect(root)

    def test_duplicate_key_across_files_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            generate(root)
            (root / 'part-2.csv').write_text('transaction_id,revenue\nT1,50\n', encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'repeated transaction_id'):
                inspect(root)


class PipelineContracts(unittest.TestCase):
    def test_deferred_preview_and_write_preserve_expected_output(self):
        with pipeline_fixture() as conn, tempfile.TemporaryDirectory() as directory:
            query = DeferredQuery(conn)
            self.assertEqual(query.executions, 0)
            self.assertTrue(query.explain())
            self.assertEqual(query.executions, 0)
            self.assertEqual(query.collect(), [('A', 'VN', 300), ('B', 'US', 50)])
            output = Path(directory) / 'report.csv'
            query.write(output)
            self.assertEqual(query.executions, 2)
            with output.open(encoding='utf-8', newline='') as source:
                self.assertEqual(list(csv.DictReader(source)), [
                    {'campaign': 'A', 'country': 'VN', 'revenue': '300'},
                    {'campaign': 'B', 'country': 'US', 'revenue': '50'}])

    def test_duplicate_dimension_inflates_pipeline_output(self):
        with pipeline_fixture() as conn:
            conn.execute("INSERT INTO campaigns VALUES ('A','VN')")
            self.assertEqual(DeferredQuery(conn).collect(), [('A', 'VN', 600), ('B', 'US', 50)])


if __name__ == '__main__':
    unittest.main()
