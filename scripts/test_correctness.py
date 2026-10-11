"""Business-state integration tests on the pinned Spark/Delta runtime."""
import os
from pathlib import Path
import sys
import unittest


def main():
    if not os.environ.get('SPARK_LAB_CONTAINER'):
        from spark_runtime import launch
        return launch('scripts/test_correctness.py', sys.argv[1:], delta=True)
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from labs.correctness import model as M
    from labs.correctness.delta_labs import LABS, create, merge, read, frame
    from labs.spark.common import run_directory, session, stage_summary, write_json
    out = run_directory('tests-correctness')
    with session('pipeline-correctness-contracts', out) as spark:
        class Contracts(unittest.TestCase):
            def run_lab(self, number):
                folder = out / ('lab' + number)
                folder.mkdir()
                result = LABS[number](spark, folder)
                write_json(folder / 'result.json', result)
                return result

            def test_09_grain_conservation(self):
                result = self.run_lab('09')
                self.assertEqual(result['revenueConserved'], 170)
                self.assertEqual(result['costConserved'], 140)

            def test_10_boundary_loss(self):
                result = self.run_lab('10')
                self.assertEqual(result['naiveCreatedIds'], ['D'])
                self.assertEqual(result['updatedIds'], ['B', 'D', 'E'])

            def test_11_retry_faults_and_replay(self):
                result = self.run_lab('11')
                self.assertEqual(result['safeRevenue'], 100)
                self.assertEqual(result['appendRevenue'], 300)
                self.assertEqual(result['onceHash'], result['ackRetryHash'])
                self.assertEqual(result['faultsObserved'], ['after_read_before_write', 'after_commit_before_ack'])

            def test_12_exact_merge_states(self):
                result = self.run_lab('12')
                self.assertEqual(result['additiveReplay'], [100, 200, 300])
                self.assertEqual([(r['event_id'], r['revenue']) for r in result['states']['newer-and-distinct-event']], [('E123', 120), ('E124', 100)])
                self.assertEqual(result['matrixHashes']['replay'], result['matrixHashes']['stale'])

            def test_13_business_date(self):
                result = self.run_lab('13')
                self.assertEqual(result['eventDate'], '2026-10-01')
                self.assertEqual(result['incorrectProcessingDate'], '2026-10-02')

            def test_14_attribution_reconciliation(self):
                result = self.run_lab('14')
                self.assertEqual(result['finalRevenue'], 120)
                self.assertFalse(result['mismatchDetected']['pass'])
                self.assertEqual(result['replayHash'], result['timeline'][-1]['hash'])

            def test_15_resume_and_scope_isolation(self):
                result = self.run_lab('15')
                self.assertEqual((result['completedBeforeFailure'], result['resumedDays']), (37, 53))
                self.assertEqual((result['historicalRevenue'], result['liveRevenue']), (900, 88))
                self.assertEqual(result['sourceSnapshotHash'], result['historicalHashAfterRerun'])
                self.assertTrue(result['finalReconciliation']['pass'])

            def test_unmatched_duplicates_are_not_magic_dedup(self):
                folder = out / 'unmatched-duplicates'
                folder.mkdir()
                bad, safe = folder / 'bad', folder / 'safe'
                create(spark, bad, [])
                frame(spark, [M.event('NEW', 100)] * 2).createOrReplaceTempView('unmatched_duplicates')
                spark.sql(f'''MERGE INTO delta.`{bad}` t USING unmatched_duplicates s
                              ON t.source_system=s.source_system AND t.app_id=s.app_id AND t.event_id=s.event_id
                              WHEN NOT MATCHED THEN INSERT *''')
                self.assertEqual(len(read(spark, bad)), 2)
                create(spark, safe, [])
                self.assertEqual(len(merge(spark, safe, [M.event('NEW', 100)] * 2)), 1)
                with self.assertRaises(M.ContractError):
                    merge(spark, bad, [M.event('NEW', 100)])
                write_json(folder / 'result.json', {'unprocessedSourceRowsInserted': 2, 'preprocessedSourceRowsInserted': 1, 'duplicateTargetRejected': True})

            def test_tombstone_prevents_stale_resurrection(self):
                target = out / 'tombstone'
                original = M.event('DELETE', 100)
                create(spark, target, [original])
                deleted = dict(original, revision=2, is_deleted=True)
                merge(spark, target, [deleted])
                merge(spark, target, [original])
                final = read(spark, target)
                self.assertTrue(final[0]['is_deleted'])
                self.assertEqual(M.gold(final, []), [])

        suite = (unittest.defaultTestLoader.loadTestsFromNames(sys.argv[1:], Contracts) if sys.argv[1:]
                 else unittest.defaultTestLoader.loadTestsFromTestCase(Contracts))
        result = unittest.TextTestRunner(verbosity=2).run(suite)
        write_json(out / 'test-summary.json', {'testsRun': result.testsRun,
                   'failures': len(result.failures), 'errors': len(result.errors),
                   'skipped': len(result.skipped), 'successful': result.wasSuccessful()})
    stages = stage_summary(out)
    print(f'Evidence: {out}; stages={len(stages)}', flush=True)
    return 0 if result.wasSuccessful() and stages else 1


if __name__ == '__main__':
    raise SystemExit(main())
