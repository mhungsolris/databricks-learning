import json
from pathlib import Path
import unittest
from labs.streaming.recovery import choose
from labs.correctness import model as M


class RecoveryContracts(unittest.TestCase):
    def test_same_checkpoint_requires_semantic_compatibility(self):
        facts = dict(checkpointReadable=True, queryCompatible=False, sourcePositionAvailable=True, replayComplete=True, authoritativeBackfill=True)
        self.assertEqual(choose(facts), 'new-checkpoint-replay-to-staging-and-reconcile')

    def test_retention_gap_needs_authoritative_repair(self):
        facts = dict(checkpointReadable=False, queryCompatible=False, sourcePositionAvailable=False, replayComplete=False, authoritativeBackfill=True)
        self.assertEqual(choose(facts), 'bounded-backfill-and-rebuild-state')
        facts['authoritativeBackfill'] = False
        self.assertEqual(choose(facts), 'blocked-missing-truth')

    def test_readable_checkpoint_with_expired_source_position_needs_repair(self):
        facts = dict(checkpointReadable=True, queryCompatible=True, sourcePositionAvailable=False,
                     replayComplete=False, authoritativeBackfill=True)
        self.assertEqual(choose(facts), 'bounded-backfill-and-rebuild-state')

    def test_public_fixture_revisions_and_namespaces(self):
        fixture = json.loads(Path('docs/public/assessment/streaming-input.json').read_text(encoding='utf-8'))
        states = [M.event(r['event_id'], r['revenue'], source_system=r['source_system'],
                  app_id=r['app_id'], revision=r['revision'], event_time=r['event_time'],
                  updated_at=r['updated_at'], ingested_at=r['arrival'], processed_at=r['arrival'],
                  campaign_id=r['campaign']) for r in fixture['deliveries']]
        resolved = M.resolve(states)
        self.assertEqual(len(resolved), 3)
        self.assertEqual(sum(r['revenue'] for r in resolved), 760)
        self.assertEqual(M.advance(resolved, states), resolved)


if __name__ == '__main__':
    unittest.main()
