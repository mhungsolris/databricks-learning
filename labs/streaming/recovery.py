"""Recovery choices depend on retained truth, not solely on checkpoint readability."""


def choose(facts):
    if facts['checkpointReadable'] and facts['queryCompatible'] and facts['sourcePositionAvailable']:
        return 'reuse-checkpoint-and-reconcile'
    if facts['replayComplete']:
        return 'new-checkpoint-replay-to-staging-and-reconcile'
    if facts['authoritativeBackfill']:
        return 'bounded-backfill-and-rebuild-state'
    return 'blocked-missing-truth'
