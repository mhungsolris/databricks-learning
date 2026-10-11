"""Explicit standalone correctness labs on the accepted Delta runtime."""
import argparse
import os
from pathlib import Path
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--lab', choices=['09', '10', '11', '12', '13', '14', '15', 'all'], default='all')
    args = parser.parse_args()
    if not os.environ.get('SPARK_LAB_CONTAINER'):
        from spark_runtime import launch
        return launch('scripts/run_correctness.py', sys.argv[1:], delta=True)
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from labs.spark.common import session, run_directory, stage_summary, write_json
    from labs.correctness.delta_labs import LABS
    output = run_directory('correctness-' + args.lab)
    selected = list(LABS) if args.lab == 'all' else [args.lab]
    with session('roas-correctness-' + args.lab, output) as spark:
        for n in selected:
            folder = output / ('lab' + n)
            folder.mkdir()
            result = LABS[n](spark, folder)
            write_json(folder / 'result.json', result)
            print(f'PASS Lab {n}; evidence={folder}', flush=True)
    stages = stage_summary(output)
    print(f'Evidence: {output}; stages={len(stages)}', flush=True)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
