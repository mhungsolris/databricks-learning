import unittest
from labs.correctness import model as M


class CorrectnessContracts(unittest.TestCase):
    def test_medallion_preserves_both_metrics_and_unknown(self):
        result = M.medallion()
        self.assertEqual((result['revenueConserved'], result['costConserved']), (170, 140))
        unknown = next(r for r in result['gold'] if r['campaign_id'] == 'UNKNOWN')
        self.assertEqual(unknown['revenue'], 20)
        self.assertIsNone(unknown['roas'])

    def test_detail_cost_join_repeats_daily_cost(self):
        result = M.medallion()
        self.assertEqual((result['wrongDetailCost'], result['correctCost']), (100, 50))

    def test_delivery_channel_and_arrival_are_not_identity(self):
        first = M.event()
        retry = M.event(channel='file', ingested_at='2026-10-02T08:00:00Z')
        self.assertEqual(len(M.resolve([first, retry])), 1)
        self.assertEqual(M.fingerprint(first), M.fingerprint(retry))

    def test_incomplete_key_would_lose_legitimate_event(self):
        a, b = M.event('E1'), M.event('E1', app_id='appB')
        self.assertEqual(len(M.resolve([a, b])), 2)

    def test_conflicting_equal_revision_is_rejected(self):
        with self.assertRaises(M.ContractError):
            M.resolve([M.event(revenue=100), M.event(revenue=200)])
        with self.assertRaises(M.ContractError):
            M.advance([M.event()], [M.event(revenue=200)])

    def test_mutable_updates_and_stale_updates_are_order_independent(self):
        old, new = M.event(revenue=0), M.event(revenue=100, revision=2)
        self.assertEqual(M.advance([new], [old])[0]['revenue'], 100)
        self.assertEqual(M.state_hash(M.resolve([new, old])), M.state_hash(M.resolve([old, new])))

    def test_replay_batch_and_previous_day_preserve_state(self):
        batch = [M.event('E123', 100)] * 3
        once = M.advance([], batch)
        twice = M.advance(once, batch)
        self.assertEqual(M.state_hash(once), M.state_hash(twice))
        self.assertEqual(sum(r['revenue'] for r in twice), 100)

    def test_append_and_additive_updates_violate_invariant(self):
        batch = [M.event('E123', 100)]
        self.assertEqual(sum(r['revenue'] for r in batch * 3), 300)
        self.assertNotEqual(M.state_hash(batch), M.state_hash(batch * 3))

    def test_incremental_created_cursor_misses_corrections(self):
        result = M.incremental()
        self.assertEqual(result['naiveCreatedIds'], ['D'])
        self.assertEqual(result['updatedIds'], ['B', 'D', 'E'])
        self.assertEqual(result['sameTimestampMiss'], result['lookbackRecovers'])

    def test_partial_target_write_does_not_advance_cursor(self):
        batch = [M.event('A'), M.event('B', 20)]
        job = M.BatchJob()
        with self.assertRaises(M.InjectedFailure):
            job.run(batch, '2026-10-01T10:15:00Z', fail_at='after_read')
        self.assertEqual(job.target, [])
        with self.assertRaises(M.InjectedFailure):
            job.run(batch, '2026-10-01T10:15:00Z', fail_at='after_write')
        self.assertIsNone(job.cursor)
        committed = M.state_hash(job.target)
        job.run(batch, '2026-10-01T10:15:00Z')
        self.assertEqual(job.cursor, '2026-10-01T10:15:00Z')
        self.assertEqual(M.state_hash(job.target), committed)

    def test_late_revision_replay_is_120_not_220(self):
        state = []
        timeline = [M.event(revenue=0), M.event(revenue=100, revision=2), M.event(revenue=120, revision=3)]
        for row in timeline * 2:
            state = M.advance(state, [row])
        self.assertEqual((len(state), state[0]['revenue']), (1, 120))

    def test_event_and_processing_day_differ(self):
        result = M.time_semantics()
        self.assertNotEqual(result['eventDate'], result['incorrectProcessingDate'])

    def test_reconcile_equal_totals_but_wrong_keys_fails(self):
        expected = [M.event('A', 100), M.event('B', 50)]
        actual = [M.event('A', 50), M.event('C', 100)]
        result = M.reconcile(expected, actual)
        self.assertEqual(result['expectedRevenue'], result['actualRevenue'])
        self.assertFalse(result['pass'])
        self.assertTrue(result['missing'] and result['extra'] and result['mismatched'])

    def test_reconcile_duplicates_nulls_and_wrong_day(self):
        expected = [M.event('A', 100)]
        for actual in [expected * 2, [M.event(None, 100)], [M.event('A', 100, event_time='2026-10-02T10:00:00Z')]]:
            with self.subTest(actual=actual):
                self.assertFalse(M.reconcile(expected, actual)['pass'])

    def test_backfill_failed_resume_and_entire_rerun(self):
        source = M.backfill_source()
        partial = M.advance([], source[:37])
        self.assertEqual(len(partial), 37)
        completed = M.advance(partial, source[37:])
        replay = M.advance(completed, source)
        self.assertTrue(M.reconcile(source, replay)['pass'])
        self.assertEqual(M.state_hash(replay), M.state_hash(source))
        self.assertEqual(sum(r['revenue'] for r in replay), 900)

    def test_synthetic_mutation_timestamps_are_coherent(self):
        row = M.event(revision=2, updated_at='2026-10-02T08:00:00Z')
        self.assertEqual(row['ingested_at'], '2026-10-02T08:02:00Z')
        self.assertEqual(row['processed_at'], '2026-10-02T08:14:00Z')
        self.assertEqual(row['event_time'], '2026-10-01T10:00:00Z')

    def test_expected_truth_and_tolerance_must_be_valid(self):
        with self.assertRaises(M.ContractError):
            M.reconcile([M.event()] * 2, [M.event()])
        with self.assertRaises(M.ContractError):
            M.reconcile([M.event()], [M.event()], tolerance=-1)

    def test_cursor_cannot_regress_or_ignore_bad_fault_name(self):
        job = M.BatchJob()
        job.run([M.event()], '2026-10-01T10:15:00Z')
        with self.assertRaises(M.ContractError):
            job.run([M.event()], '2026-10-01T10:00:00Z')
        with self.assertRaises(M.ContractError):
            job.run([M.event()], '2026-10-01T10:30:00Z', fail_at='unknown')

    def test_tombstone_and_cost_duplicates_have_explicit_contracts(self):
        removed = M.advance([M.event()], [M.event(revenue=0, revision=2, is_deleted=True)])
        self.assertTrue(removed[0]['is_deleted'])
        with self.assertRaises(M.ContractError):
            M.gold([M.event()], M.costs() + [M.costs()[0]])


if __name__ == '__main__':
    unittest.main()
