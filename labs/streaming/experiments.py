"""Each experiment executes a real query; all fixtures are tiny and single-writer."""
import shutil
from .common import (KEY, active, aggregate, capture, checkpoint_inventory, digest,
                     event, publish, save, snapshot, source, state_metric, watermark,
                     windowed, writer, table_sink)
from .recovery import choose


def lab16(spark, out):
    inputs, cp, target = out / 'input', out / 'checkpoint', out / 'target'
    df = source(spark, inputs).where("status = 'COMPLETED'")
    observations = []
    with active(writer(df, cp).format('delta').start(str(target))) as q:
        for index, ids in enumerate([['E1', 'E2', 'E3'], ['E4', 'E5'], ['E6']]):
            publish(inputs, str(index), [event(i) for i in ids])
            q.processAllAvailable()
            observations.append(capture(q, spark, target))
    result = dict(phases=observations, stopped=not q.isActive,
                  checkpoint=checkpoint_inventory(cp))
    assert [len(o['target']) for o in observations] == [3, 5, 6]
    assert all(o['active'] for o in observations) and result['stopped']
    assert len({p['batchId'] for p in observations[-1]['progress'] if p['numInputRows'] > 0}) >= 3
    return result


def lab17(spark, out):
    inputs, cp, target = out / 'input', out / 'checkpoint', out / 'target'
    def start():
        return writer(aggregate(source(spark, inputs)), cp, 'complete').foreachBatch(table_sink(target)).start()
    phases = []
    with active(start()) as q:
        publish(inputs, '0', [event('E1', 10), event('E2', 20, user='U2')])
        q.processAllAvailable()
        phases.append(capture(q, spark, target))
        publish(inputs, '1', [event('E3', 5)])
        q.processAllAvailable()
        phases.append(capture(q, spark, target))
    with active(start()) as q:
        publish(inputs, '2', [event('E4', 7, user='U2')])
        q.processAllAvailable()
        phases.append(capture(q, spark, target))
    assert {r['user_id']: (r['amount'], r['events']) for r in phases[-1]['target']} == {'U1': (15, 2), 'U2': (27, 2)}
    assert phases[0]['queryId'] == phases[2]['queryId'] and phases[0]['runId'] != phases[2]['runId']
    inventory = checkpoint_inventory(cp)
    assert any(p.startswith('state/') for p in inventory)
    assert state_metric(phases[1], 'numRowsTotal') > 0
    return dict(phases=phases, checkpoint=inventory)


def lab18(spark, out):
    inputs, cp, target = out / 'input', out / 'checkpoint', out / 'target'
    def start(checkpoint):
        return writer(source(spark, inputs), checkpoint).format('delta').start(str(target))
    phases = []
    with active(start(cp)) as q:
        publish(inputs, '0', [event('E1'), event('E2')])
        q.processAllAvailable()
        publish(inputs, '1', [event('E3')])
        q.processAllAvailable()
        phases.append(capture(q, spark, target))
    with active(start(cp)) as q:
        q.processAllAvailable()
        phases.append(capture(q, spark, target))
        publish(inputs, '2', [event('E4')])
        q.processAllAvailable()
        phases.append(capture(q, spark, target))
    with active(start(out / 'new-checkpoint')) as q:
        q.processAllAvailable()
        phases.append(capture(q, spark, target))
    assert [len(p['target']) for p in phases] == [3, 3, 4, 8]
    assert phases[0]['targetHash'] == phases[1]['targetHash']
    assert phases[0]['queryId'] == phases[1]['queryId'] != phases[3]['queryId']
    return dict(phases=phases, checkpoint=checkpoint_inventory(cp), sourceSemantics='Retained JSON files discovered afresh with new checkpoint')


def lab19(spark, out):
    results = {}
    for name, delay in [('none', None), ('short', '5 minutes'), ('long', '2 hours')]:
        folder = out / name
        folder.mkdir()
        inputs, cp, target = folder / 'input', folder / 'checkpoint', folder / 'target'
        emissions = []
        with active(writer(windowed(source(spark, inputs), delay), cp, 'update')
                    .foreachBatch(table_sink(target, 'update', ['window_start', 'window_end'], emissions)).start()) as q:
            publish(inputs, '0', [event('A', 10), event('B', 20, time='10:02')])
            q.processAllAvailable()
            publish(inputs, '1', [event('PROGRESS', 1, time='10:30')])
            q.processAllAvailable()
            before = capture(q, spark, target)
            if name == 'short':
                assert watermark(before) >= '2026-10-01T10:25'
            publish(inputs, '2', [event('C', 7, time='09:50')])
            q.processAllAvailable()
            after = capture(q, spark, target)
        results[name] = dict(beforeLate=before, afterLate=after, emissions=emissions, checkpoint=checkpoint_inventory(cp))
    assert state_metric(results['short']['afterLate'], 'numRowsDroppedByWatermark') >= 1
    assert state_metric(results['short']['afterLate'], 'numRowsRemoved') >= 1
    for name in ('none', 'long'):
        assert any(r['window_start'].endswith('09:50:00Z') and r['amount'] == 7 for r in results[name]['afterLate']['target'])
    assert not any(r['window_start'].endswith('09:50:00Z') for r in results['short']['afterLate']['target'])
    assert results['short']['afterLate']['progress'][-1]['stateOperators'][0]['numRowsTotal'] == 1
    assert all(results[name]['afterLate']['progress'][-1]['stateOperators'][0]['numRowsTotal'] == 3 for name in ('none', 'long'))
    return results


def lab20(spark, out):
    inputs, cp, target = out / 'input', out / 'checkpoint', out / 'target'
    df = source(spark, inputs).withWatermark('event_time', '10 minutes').dropDuplicatesWithinWatermark(KEY)
    phases = []
    with active(writer(df, cp).format('delta').start(str(target))) as q:
        files = [[event('E123')], [event('E123', time='10:01'), event('E124', time='10:02')],
                 [event('ADVANCE', time='11:00')], [event('E123')], [event('E123', time='11:02')]]
        for index, records in enumerate(files):
            publish(inputs, str(index), records)
            q.processAllAvailable()
            phases.append(capture(q, spark, target))
    assert [len(p['target']) for p in phases] == [1, 2, 3, 3, 4]
    assert state_metric(phases[3], 'numRowsDroppedByWatermark') >= 1
    assert state_metric(phases[2], 'numRowsRemoved') >= 1
    assert sum(r['event_id'] == 'E123' for r in phases[-1]['target']) == 2
    return dict(phases=phases, checkpoint=checkpoint_inventory(cp), immutableEventClockViolated=True)


def lab21(spark, out):
    clicks, purchases, cp, target = out / 'clicks', out / 'purchases', out / 'checkpoint', out / 'target'
    left = source(spark, clicks, 'click_id string, user_id string, click_time timestamp').withWatermark('click_time', '10 minutes').alias('c')
    right = source(spark, purchases, 'purchase_id string, click_id string, user_id string, purchase_time timestamp, amount long').withWatermark('purchase_time', '10 minutes').alias('p')
    from pyspark.sql.functions import expr
    joined = left.join(right, expr('''c.click_id = p.click_id AND c.user_id = p.user_id
        AND p.purchase_time >= c.click_time AND p.purchase_time <= c.click_time + INTERVAL 20 MINUTES'''), 'leftOuter').selectExpr(
        'c.click_id', 'c.user_id', 'c.click_time', 'p.purchase_id', 'p.purchase_time', 'p.amount')
    def click(identity, time):
        return dict(click_id=identity, user_id='U1', click_time=f'2026-10-01T{time}:00Z')
    def purchase(identity, key, time):
        return dict(purchase_id=identity, click_id=key, user_id='U1', purchase_time=f'2026-10-01T{time}:00Z', amount=100)
    phases = []
    with active(writer(joined, cp).format('delta').start(str(target))) as q:
        publish(clicks, '0', [click('C1', '10:00'), click('C2', '10:05'), click('C3', '10:07')])
        publish(purchases, '0', [purchase('P1', 'C1', '10:10')])
        q.processAllAvailable()
        phases.append(capture(q, spark, target))
        publish(purchases, '1', [purchase('P2', 'C2', '10:12')])
        q.processAllAvailable()
        phases.append(capture(q, spark, target))
        publish(clicks, '1', [click('ADVANCE', '11:00')])
        publish(purchases, '2', [purchase('UNMATCHED_RIGHT', 'OTHER', '11:01')])
        q.processAllAvailable()
        phases.append(capture(q, spark, target))
    assert not any(r['click_id'] == 'C3' for r in phases[1]['target'])
    assert {(r['click_id'], r['purchase_id']) for r in phases[-1]['target']} == {('C1', 'P1'), ('C2', 'P2'), ('C3', None)}
    assert len(phases[-1]['progress'][-1]['sources']) == 2
    assert state_metric(phases[-1], 'numRowsRemoved') > 0
    return dict(phases=phases, checkpoint=checkpoint_inventory(cp))


def lab22(spark, out):
    results = {}
    for mode in ('update', 'complete'):
        folder = out / mode
        folder.mkdir()
        inputs, target, cp = folder / 'input', folder / 'target', folder / 'checkpoint'
        emissions = []
        with active(writer(aggregate(source(spark, inputs)), cp, mode)
                    .foreachBatch(table_sink(target, mode, ['user_id'], emissions)).start()) as q:
            publish(inputs, '0', [event('E1', 10), event('E2', 20, user='U2')])
            q.processAllAvailable()
            count = len(emissions)
            publish(inputs, '1', [event('E3', 5)])
            q.processAllAvailable()
            results[mode] = dict(secondEmissions=emissions[count:], phases=[capture(q, spark, target)], emissions=emissions)
    assert len(results['update']['secondEmissions'][0]['rows']) == 1
    assert len(results['complete']['secondEmissions'][0]['rows']) == 2
    folder = out / 'append'
    folder.mkdir()
    inputs, target, cp = folder / 'input', folder / 'target', folder / 'checkpoint'
    with active(writer(windowed(source(spark, inputs), '5 minutes'), cp).format('delta').start(str(target))) as q:
        publish(inputs, '0', [event('A', 10), event('B', 20, time='10:02')])
        q.processAllAvailable()
        before = capture(q, spark, target)
        publish(inputs, '1', [event('ADVANCE', 1, time='10:30')])
        q.processAllAvailable()
        after = capture(q, spark, target)
    assert before['target'] == [] and len(after['target']) == 1 and after['target'][0]['amount'] == 30
    results['append'] = dict(phases=[before, after], checkpoint=checkpoint_inventory(cp))
    return results


def lab23(spark, out):
    results = {}
    for mode in ('unsafe', 'transactional'):
        folder = out / mode
        folder.mkdir()
        inputs, cp, target = folder / 'input', folder / 'checkpoint', folder / 'target'
        publish(inputs, '0', [event('E123')])
        attempts = []
        app_id = str(folder) + '-checkpoint-generation-1'
        def sink(fail):
            def consume(df, batch_id):
                df.persist()
                try:
                    observed = df.count()
                    if not observed:
                        return
                    write = df.write.format('delta').mode('append')
                    if mode == 'transactional':
                        write = write.option('txnAppId', app_id).option('txnVersion', batch_id)
                    write.save(str(target))
                    attempts.append(dict(batchId=batch_id, rows=observed, failAfterSinkCommit=fail))
                    if fail:
                        raise RuntimeError('SIMULATED_AFTER_SINK_COMMIT')
                finally:
                    df.unpersist()
            return consume
        with active(writer(source(spark, inputs), cp).foreachBatch(sink(True)).start()) as q:
            try:
                q.processAllAvailable()
            except Exception as exc:
                assert 'SIMULATED_AFTER_SINK_COMMIT' in str(exc)
                failure = str(exc)
            else:
                raise AssertionError('Expected sink-boundary failure')
            failed_id, failed_run = str(q.id), str(q.runId)
        batch_id = attempts[0]['batchId']
        before_inventory = checkpoint_inventory(cp)
        assert f'offsets/{batch_id}' in before_inventory and f'commits/{batch_id}' not in before_inventory
        before = snapshot(spark, target)
        with active(writer(source(spark, inputs), cp).foreachBatch(sink(False)).start()) as q:
            q.processAllAvailable()
            after = capture(q, spark, target)
        assert after['queryId'] == failed_id and after['runId'] != failed_run
        assert [a['batchId'] for a in attempts] == [batch_id, batch_id]
        assert len(after['target']) == (2 if mode == 'unsafe' else 1)
        results[mode] = dict(failure=failure, attempts=attempts, beforeTarget=before, after=after,
                             failedCheckpoint=before_inventory, checkpoint=checkpoint_inventory(cp), txnAppId=app_id)
    return results


def lab24(spark, out):
    inputs, cp, target = out / 'input', out / 'checkpoint', out / 'target'
    publish(inputs, '0', [event('E1', 100), event('E2', 50, user='U2')])
    with active(writer(aggregate(source(spark, inputs)), cp, 'complete').foreachBatch(table_sink(target)).start()) as q:
        q.processAllAvailable()
        before = capture(q, spark, target)
    damaged = out / 'incompatible-checkpoint'
    shutil.copytree(cp, damaged)  # Diagnostic copy; retain the original evidence.
    publish(inputs, '1', [event('E3', 20)])
    with active(writer(aggregate(source(spark, inputs), ('user_id', 'platform')), damaged, 'complete')
                .foreachBatch(table_sink(out / 'diagnostic-target')).start()) as q:
        try:
            q.processAllAvailable()
        except Exception as exc:
            failure = str(exc)
            assert 'STATE_STORE' in failure and ('SCHEMA' in failure or 'KEY' in failure)
        else:
            raise AssertionError('Expected incompatible state schema failure')
    staging = out / 'recovery-staging'
    with active(writer(aggregate(source(spark, inputs), ('user_id', 'platform')), out / 'new-checkpoint', 'complete')
                .foreachBatch(table_sink(staging)).start()) as q:
        q.processAllAvailable()
        recovered = capture(q, spark, staging)
    expected = [{'user_id': 'U1', 'platform': 'google', 'amount': 120, 'events': 2},
                {'user_id': 'U2', 'platform': 'google', 'amount': 50, 'events': 1}]
    reconciliation = dict(passCheck=digest(recovered['target']) == digest(sorted(expected, key=lambda r: __import__('json').dumps(r, sort_keys=True))),
                          originalTargetUnchanged=digest(snapshot(spark, target)) == before['targetHash'])
    assert all(reconciliation.values())
    cases = []
    for name, readable, compatible, replay, backfill, decision in [
        ('compatible', True, True, True, True, 'reuse-checkpoint-and-reconcile'),
        ('deleted-or-incompatible', False, False, True, True, 'new-checkpoint-replay-to-staging-and-reconcile'),
        ('retention-gap', False, False, False, True, 'bounded-backfill-and-rebuild-state'),
        ('no-retained-truth', False, False, False, False, 'blocked-missing-truth')]:
        facts = dict(checkpointReadable=readable, queryCompatible=compatible, sourcePositionAvailable=replay,
                     replayComplete=replay, authoritativeBackfill=backfill)
        assert choose(facts) == decision
        cases.append(dict(name=name, facts=facts, decision=decision))
    return dict(before=before, incompatibleFailure=failure, recovered=recovered,
                reconciliation=reconciliation, cases=cases, checkpoint=checkpoint_inventory(cp))


LABS = {str(n): globals()[f'lab{n}'] for n in range(16, 25)}
