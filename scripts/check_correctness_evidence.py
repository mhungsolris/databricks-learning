"""Reject source/artifact drift in published correctness evidence."""
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from labs.correctness import model as M

folder = ROOT / 'docs/public/evidence/correctness'
manifest = json.loads((folder / 'manifest.json').read_text())
for name, expected in manifest['files'].items():
    assert hashlib.sha256((folder / name).read_bytes()).hexdigest() == expected, f'Artifact drift: {name}'
for name, expected in manifest['sourceHashes'].items():
    assert hashlib.sha256((ROOT / name).read_text(encoding='utf-8').encode('utf-8')).hexdigest() == expected, f'Source drift: {name}; refresh verified evidence'
assert manifest['sourceHashEncoding'] == 'UTF-8 with LF newlines'
assert manifest['runtimePin'] == json.loads((ROOT / 'runtime/spark.json').read_text())
for name in manifest['files']:
    content = json.loads((folder / name).read_text())
    if isinstance(content, dict) and {'rows', 'hash', 'history'} <= content.keys():
        assert M.state_hash(content['rows']) == content['hash'], f'State hash mismatch: {name}'
        versions = [r['version'] for r in content['history']]
        assert versions == list(range(len(versions) - 1, -1, -1)), f'History gap: {name}'
matrix = json.loads((folder / 'lab12/result.json').read_text())
assert all(M.state_hash(rows) == matrix['matrixHashes'][name] for name, rows in matrix['states'].items())
summary = json.loads((folder / 'test-summary.json').read_text())
assert summary == {'testsRun': 9, 'failures': 0, 'errors': 0, 'skipped': 0, 'successful': True}
print(f'PASS {len(manifest["files"])} artifact hashes, {len(manifest["sourceHashes"])} source pins, state/history/matrix hashes and successful9-test summary')
