"""Host: Docker dispatcher. Container: actual Spark and Parquet smoke test."""
import os
from pathlib import Path
import sys


def main():
    if not os.environ.get('SPARK_LAB_CONTAINER'):
        from spark_runtime import launch
        return launch('scripts/verify_spark.py')
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from labs.spark.common import run_directory, session, write_json, stage_summary
    output = run_directory('smoke')
    with session('handbook-smoke', output) as spark:
        assert spark.version == '4.0.4'
        assert spark.sparkContext.master == 'local[*]'
        df = spark.range(10, numPartitions=2)
        assert df.filter('id >= 5').count() == 5
        df.createOrReplaceTempView('numbers')
        assert spark.sql('SELECT SUM(id) AS total FROM numbers').first().total == 45
        path = str(output / 'parquet')
        df.write.mode('errorifexists').parquet(path)
        assert spark.read.parquet(path).count() == 10
        write_json(output / 'result.json', {'rows': 10, 'filteredRows': 5, 'sqlTotal': 45, 'parquetReadRows': 10})
        print(f'PASS Spark {spark.version}; master={spark.sparkContext.master}; DataFrame=5; SQL=45; Parquet=10')
    stages = stage_summary(output)
    assert stages, 'No actual Spark stage events captured'
    print(f'Evidence: {output}; completed stages: {len(stages)}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
