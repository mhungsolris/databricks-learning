"""Run actual Spark labs with an explicit, bounded local runtime."""
import argparse
import os
from pathlib import Path
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--lab', choices=['03', '04', '05', '06', '07', '08', 'all'], default='all')
    parser.add_argument('--ui', action='store_true')
    parser.add_argument('--hold-seconds', type=int, default=0)
    args = parser.parse_args()
    if not 0 <= args.hold_seconds <= 300:
        parser.error('hold-seconds must be 0..300')
    if not os.environ.get('SPARK_LAB_CONTAINER'):
        from spark_runtime import launch
        return launch('scripts/run_spark.py', sys.argv[1:], ui=args.ui, delta=args.lab == '08')
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from labs.spark.common import run_directory, session, stage_summary, write_json
    from labs.spark.experiments import LABS
    selected = ['03', '04', '05', '06', '07'] if args.lab == 'all' else [args.lab]
    output = run_directory('labs-' + args.lab)
    with session('handbook-labs-' + args.lab, output) as spark:
        for number in selected:
            folder = output / ('lab' + number)
            folder.mkdir()
            spark.sparkContext.setJobGroup('lab' + number, 'Lab ' + number)
            result = LABS[number](spark, folder)
            job_ids = list(spark.sparkContext.statusTracker().getJobIdsForGroup('lab' + number))
            stages = sorted({sid for jid in job_ids for sid in spark.sparkContext.statusTracker().getJobInfo(jid).stageIds})
            write_json(folder / 'result.json', result)
            write_json(folder / 'jobs.json', {'jobIds': job_ids, 'stageIds': stages})
            print(f'PASS Lab {number}: {result}')
        if args.hold_seconds:
            import time
            print(f'Spark UI: http://127.0.0.1:4040 ; hold {args.hold_seconds}s', flush=True)
            time.sleep(args.hold_seconds)
    stages = stage_summary(output)
    assert stages, 'No completed stages captured'
    print(f'Evidence: {output}; completed stages: {len(stages)}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
