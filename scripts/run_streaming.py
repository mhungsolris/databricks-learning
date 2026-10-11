"""Run controlled streaming labs using the pinned local Spark/Delta runtime."""
import argparse
import os
from pathlib import Path
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--lab', choices=[str(n) for n in range(16, 25)] + ['all'], default='all')
    args = parser.parse_args()
    if not os.environ.get('SPARK_LAB_CONTAINER'):
        from spark_runtime import launch
        return launch('scripts/run_streaming.py', sys.argv[1:], delta=True)
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from labs.spark.common import session, run_directory, stage_summary
    from labs.streaming.common import save
    from labs.streaming.experiments import LABS
    output = run_directory('streaming-' + args.lab)
    with session('roas-streaming', output) as spark:
        spark.conf.set('spark.sql.session.timeZone', 'UTC')
        save(output / 'streaming-config.json', {k: spark.conf.get(k) for k in [
            'spark.sql.session.timeZone', 'spark.sql.streaming.stateStore.providerClass',
            'spark.sql.streaming.multipleWatermarkPolicy', 'spark.sql.streaming.noDataMicroBatches.enabled']})
        for n in LABS if args.lab == 'all' else [args.lab]:
            folder = output / ('lab' + n)
            folder.mkdir()
            save(folder / 'result.json', LABS[n](spark, folder))
            print(f'PASS Lab {n}; evidence={folder}', flush=True)
    stages = stage_summary(output)
    print(f'Evidence: {output}; stages={len(stages)}', flush=True)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
