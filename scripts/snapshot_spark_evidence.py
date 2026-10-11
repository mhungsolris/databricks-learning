"""Copy explicitly selected, successful toy runs to website-readable artifacts."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--spark-run', type=Path, required=True)
    parser.add_argument('--delta-run', type=Path, required=True)
    parser.add_argument('--ui', type=Path, required=True)
    parser.add_argument('--shuffle-run', type=Path, required=True)
    args = parser.parse_args()
    target = ROOT / 'docs/public/evidence/spark'
    target.mkdir(parents=True, exist_ok=True)
    manifest = {'runtime': json.loads((ROOT / 'runtime/spark.json').read_text()), 'runs': {}, 'files': {}}
    for kind, run in [('spark', args.spark_run), ('delta', args.delta_run), ('query-shuffle', args.shuffle_run)]:
        run = run.resolve()
        if not run.is_relative_to(ROOT / '.skills-test/spark'):
            raise ValueError('Evidence must come from repository local Spark runs')
        assert json.loads((run / 'shutdown.json').read_text())['clean'] is True
        expected = {'spark': ['lab03', 'lab04', 'lab05', 'lab06', 'lab07'], 'delta': ['lab08'], 'query-shuffle': ['lab05']}[kind]
        for lab in expected:
            assert json.loads((run / lab / 'result.json').read_text())
        manifest['runs'][kind] = str(run.relative_to(ROOT)).replace('\\', '/')
        files = [run / name for name in ['runtime.json', 'shutdown.json', 'stages.json']]
        for lab in expected:
            files += [f for f in (run / lab).glob('*') if f.is_file() and f.suffix in {'.txt', '.json'}]
        if kind == 'delta':
            files += list((run / 'lab08/delta-table/_delta_log').glob('*.json'))
        for source in files:
            relative = Path(kind) / source.relative_to(run)
            destination = target / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, destination)
            manifest['files'][str(relative).replace('\\', '/')] = hashlib.sha256(destination.read_bytes()).hexdigest()
    assert json.loads(args.ui.read_text(encoding='utf-8-sig'))['httpStatus'] == 200
    shutil.copyfile(args.ui, target / 'ui-observation.json')
    manifest['files']['ui-observation.json'] = hashlib.sha256((target / 'ui-observation.json').read_bytes()).hexdigest()
    (target / 'manifest.json').write_text(json.dumps(manifest, indent=2), encoding='utf-8')
    print(f'PASS selected artifacts: {len(manifest["files"])}; source runs and SHA256 in manifest.json')


if __name__ == '__main__':
    main()
