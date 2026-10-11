"""Guard published evidence integrity and business invariants independently of docs build."""
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from labs.streaming.common import digest, state_metric
from scripts.snapshot_streaming_evidence import SOURCES


def main():
    folder = ROOT / 'docs/public/evidence/streaming'
    manifest = json.loads((folder / 'manifest.json').read_text(encoding='utf-8'))
    assert manifest['runtimePin'] == json.loads((ROOT / 'runtime/spark.json').read_text(encoding='utf-8'))
    assert manifest['completedStages'] > 0 and len(manifest['files']) == 13
    assert set(manifest['sourceHashes']) == set(SOURCES)
    assert manifest['sourceHashEncoding'] == 'UTF-8 with LF newlines'
    for name, expected in manifest['files'].items():
        path = (folder / name).resolve()
        assert path.is_relative_to(folder.resolve())
        assert hashlib.sha256(path.read_bytes()).hexdigest() == expected, name
    for name, expected in manifest['sourceHashes'].items():
        assert hashlib.sha256((ROOT / name).read_text(encoding='utf-8').encode()).hexdigest() == expected, name
    def load(name):
        return json.loads((folder / name).read_text(encoding='utf-8'))
    assert load('runtime.json')['sparkVersion'] == '4.0.4'
    assert load('shutdown.json')['clean']
    assert load('test-summary.json') == dict(testsRun=9, failures=0, errors=0, skipped=0, successful=True)
    def visit(value):
        if isinstance(value, dict):
            if 'targetHash' in value:
                assert digest(value['target']) == value['targetHash']
            for item in value.values():
                visit(item)
        elif isinstance(value, list):
            for item in value:
                visit(item)
    results = {n: load(f'lab{n}/result.json') for n in range(16, 25)}
    visit(results)
    assert [len(p['target']) for p in results[16]['phases']] == [3, 5, 6]
    assert results[16]['stopped']
    assert {r['user_id']: (r['amount'], r['events']) for r in results[17]['phases'][-1]['target']} == {'U1': (15, 2), 'U2': (27, 2)}
    assert any(p.startswith('state/') for p in results[17]['checkpoint'])
    assert [len(p['target']) for p in results[18]['phases']] == [3, 3, 4, 8]
    assert state_metric(results[19]['short']['afterLate'], 'numRowsDroppedByWatermark') >= 1
    assert state_metric(results[19]['short']['afterLate'], 'numRowsRemoved') >= 1
    for mode in ('none', 'long'):
        assert any(r['amount'] == 7 and r['window_start'].endswith('09:50:00Z') for r in results[19][mode]['afterLate']['target'])
    assert [len(p['target']) for p in results[20]['phases']] == [1, 2, 3, 3, 4]
    assert {(r['click_id'], r['purchase_id']) for r in results[21]['phases'][-1]['target']} == {('C1', 'P1'), ('C2', 'P2'), ('C3', None)}
    assert len(results[22]['update']['secondEmissions'][0]['rows']) == 1
    assert len(results[22]['complete']['secondEmissions'][0]['rows']) == 2
    for mode, count in [('unsafe', 2), ('transactional', 1)]:
        case = results[23][mode]
        assert 'SIMULATED_AFTER_SINK_COMMIT' in case['failure']
        assert case['attempts'][0]['batchId'] == case['attempts'][1]['batchId']
        assert len(case['after']['target']) == count
        assert sum(r['amount'] for r in case['after']['target']) == count * 100
    assert 'STATE_STORE' in results[24]['incompatibleFailure']
    assert all(results[24]['reconciliation'].values())
    print('PASS 13 streaming file hashes, 8 source hashes, runtime pin and nine target/state/retry contracts')


if __name__ == '__main__':
    main()
