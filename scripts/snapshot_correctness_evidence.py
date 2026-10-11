"""Publish selected successful local correctness states, not transient table files."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
SELECTED = {
    '09': ['result.json', 'grain-contracts.json', 'bronze-payloads.json'],
    '10': ['result.json'],
    '11': ['result.json', 'once.json', 'replay.json', 'append-duplicates.json', 'after-ack-failure-retry.json'],
    '12': ['result.json', 'newer.json', 'ambiguous-source-error.json', 'non-idempotent-merge.json'],
    '13': ['result.json'],
    '14': ['result.json', 't2.json', 'replay-all-snapshots.json', 'mismatch-reconciliation.json'],
    '15': ['result.json', 'validation-before-publish.json', 'rerun-with-live-update.json'],
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--run', type=Path, required=True)
    args = parser.parse_args()
    run = args.run.resolve()
    if not run.is_relative_to(ROOT / '.skills-test/spark'):
        raise ValueError('Only local repository Spark runs allowed')
    assert json.loads((run / 'shutdown.json').read_text())['clean']
    summary = json.loads((run / 'test-summary.json').read_text())
    assert summary == {'testsRun': 9, 'failures': 0, 'errors': 0, 'skipped': 0, 'successful': True}
    target = ROOT / 'docs/public/evidence/correctness'
    target.mkdir(parents=True, exist_ok=True)
    files = ['runtime.json', 'shutdown.json', 'test-summary.json']
    for n, names in SELECTED.items():
        files.extend(f'lab{n}/{name}' for name in names)
    files.append('unmatched-duplicates/result.json')
    manifest = {'verifiedDate': '2026-10-11', 'timezone': 'Asia/Saigon',
                'sourceRun': run.relative_to(ROOT).as_posix(),
                'runtimePin': json.loads((ROOT / 'runtime/spark.json').read_text()),
                'purpose': 'Business state, retry histories, source ambiguity and bounded publish invariants',
                'completedStages': len(json.loads((run / 'stages.json').read_text())),
                'files': {}, 'sourceHashes': {}, 'sourceHashEncoding': 'UTF-8 with LF newlines'}
    for name in files:
        source, dest = run / name, target / name
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, dest)
        manifest['files'][name] = hashlib.sha256(dest.read_bytes()).hexdigest()
    for name in ['labs/correctness/model.py', 'labs/correctness/delta_labs.py', 'scripts/test_correctness.py', 'scripts/run_correctness.py', 'runtime/spark.json']:
        manifest['sourceHashes'][name] = hashlib.sha256((ROOT / name).read_text(encoding='utf-8').encode('utf-8')).hexdigest()
    (target / 'manifest.json').write_text(json.dumps(manifest, indent=2), encoding='utf-8')
    print(f'PASS {len(files)} selected correctness artifacts; source/run/file hashes recorded')


if __name__ == '__main__':
    main()
