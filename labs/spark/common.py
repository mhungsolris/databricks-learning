"""Shared evidence capture for tiny classic Spark experiments."""
from contextlib import contextmanager, redirect_stdout
from datetime import datetime, timezone
from io import StringIO
from pathlib import Path
import json
import os
import platform
import uuid


def run_directory(name):
    root = Path(os.environ.get('LAB_EVIDENCE_ROOT', '.skills-test/spark'))
    output = root / name / (datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ') + '-' + uuid.uuid4().hex[:8])
    output.mkdir(parents=True)
    return output


@contextmanager
def session(name, output):
    from pyspark.sql import SparkSession
    events = output / 'events'
    events.mkdir()
    spark = (SparkSession.builder.appName(name).master('local[*]')
             .config('spark.sql.shuffle.partitions', '4')
             .config('spark.sql.adaptive.enabled', 'false')
             .config('spark.ui.enabled', 'true')
             .config('spark.eventLog.enabled', 'true')
             .config('spark.eventLog.compress', 'false')
             .config('spark.eventLog.dir', events.resolve().as_uri())
             .config('spark.sql.warehouse.dir', (output / 'warehouse').resolve().as_uri())
             .getOrCreate())
    spark.sparkContext.setLogLevel('WARN')
    metadata = {
        'sparkVersion': spark.version, 'master': spark.sparkContext.master,
        'pythonVersion': platform.python_version(),
        'javaVersion': spark._jvm.java.lang.System.getProperty('java.version'),
        'applicationId': spark.sparkContext.applicationId,
        'defaultParallelism': spark.sparkContext.defaultParallelism,
        'adaptiveEnabled': spark.conf.get('spark.sql.adaptive.enabled'),
        'shufflePartitions': spark.conf.get('spark.sql.shuffle.partitions'),
        'uiUrl': spark.sparkContext.uiWebUrl,
    }
    write_json(output / 'runtime.json', metadata)
    try:
        yield spark
    finally:
        spark.stop()
        stopped = spark.sparkContext._jsc is None
        write_json(output / 'shutdown.json', {'clean': stopped})
        if not stopped:
            raise RuntimeError('SparkContext did not shut down')
        print('PASS clean SparkSession shutdown')


def write_json(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')


def plan(df, output, name):
    captured = StringIO()
    with redirect_stdout(captured):
        df.explain(mode='extended')
    text = captured.getvalue()
    (output / f'{name}-plan.txt').write_text(text, encoding='utf-8')
    return text


def groups(df):
    from pyspark.sql import functions as F
    rows = df.withColumn('partition_id', F.spark_partition_id()).groupBy('partition_id').count().collect()
    return sorted([{'partition': int(r.partition_id), 'rows': int(r['count'])} for r in rows], key=lambda r: r['partition'])


def stage_summary(output):
    stages = []
    for path in (output / 'events').rglob('*'):
        if not path.is_file() or not path.name.startswith('events_'):
            continue
        for line in path.read_text(encoding='utf-8').splitlines():
            event = json.loads(line)
            if event.get('Event') == 'SparkListenerStageCompleted':
                info = event['Stage Info']
                stages.append({'stageId': info['Stage ID'], 'tasks': info['Number of Tasks'], 'name': info['Stage Name']})
    write_json(output / 'stages.json', stages)
    return stages
