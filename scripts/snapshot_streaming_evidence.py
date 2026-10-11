"""Select successful query progress and target evidence, excluding raw checkpoint state."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
SOURCES = ['labs/streaming/common.py', 'labs/streaming/experiments.py', 'labs/streaming/recovery.py',
           'labs/spark/common.py', 'scripts/test_streaming.py', 'scripts/run_streaming.py',
           'scripts/spark_runtime.py', 'runtime/spark.json']


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--run', type=Path, required=True)
    run = parser.parse_args().run.resolve()
    if not run.is_relative_to(ROOT / '.skills-test/spark/tests-streaming'):
        raise ValueError('Only repository streaming test runs allowed')
    summary = json.loads((run / 'test-summary.json').read_text(encoding='utf-8'))
    assert summary == dict(testsRun=9, failures=0, errors=0, skipped=0, successful=True)
    assert json.loads((run / 'shutdown.json').read_text(encoding='utf-8'))['clean']
    executed_hashes = json.loads((run / 'source-hashes.json').read_text(encoding='utf-8'))
    for name in SOURCES:
        assert executed_hashes[name] == hashlib.sha256((ROOT / name).read_text(encoding='utf-8').encode()).hexdigest(), f'Source changed since execution: {name}'
    target = ROOT / 'docs/public/evidence/streaming'
    target.mkdir(parents=True, exist_ok=True)
    files = ['runtime.json', 'shutdown.json', 'test-summary.json', 'streaming-config.json']
    files += [f'lab{n}/result.json' for n in range(16, 25)]
    manifest = dict(verifiedDate='2026-10-11', timezone='Asia/Saigon',
                    sourceRun=run.relative_to(ROOT).as_posix(),
                    runtimePin=json.loads((ROOT / 'runtime/spark.json').read_text(encoding='utf-8')),
                    completedStages=len(json.loads((run / 'stages.json').read_text(encoding='utf-8'))),
                    purpose='Actual micro-batch progress, target states, checkpoint inventory and controlled sink/schema failures',
                    files={}, sourceHashes={}, sourceHashEncoding='UTF-8 with LF newlines')
    for name in files:
        dest = target / name
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(run / name, dest)
        manifest['files'][name] = hashlib.sha256(dest.read_bytes()).hexdigest()
    for name in SOURCES:
        manifest['sourceHashes'][name] = hashlib.sha256((ROOT / name).read_text(encoding='utf-8').encode()).hexdigest()
    (target / 'manifest.json').write_text(json.dumps(manifest, indent=2), encoding='utf-8')
    print(f'PASS {len(files)} selected streaming artifacts; source, file and runtime hashes recorded')


if __name__ == '__main__':
    main()
