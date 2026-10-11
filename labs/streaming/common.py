"""Controlled file arrivals and observable streaming boundaries for tiny local labs."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
from contextlib import contextmanager

SCHEMA = ('source_system string, app_id string, event_id string, user_id string, '
          'event_time timestamp, amount long, status string, platform string')
KEY = ['source_system', 'app_id', 'event_id']


def event(identity, amount=100, time='10:00', user='U1', **extra):
    record = dict(source_system='callback', app_id='app1', event_id=identity,
                user_id=user, event_time=f'2026-10-01T{time}:00Z', amount=amount,
                status='COMPLETED', platform='google')
    record.update(extra)
    return record


def normalize(value):
    if hasattr(value, 'asDict'):
        return normalize(value.asDict(recursive=True))
    if isinstance(value, datetime):
        return value.replace(tzinfo=timezone.utc).isoformat().replace('+00:00', 'Z')
    if isinstance(value, dict):
        return {k: normalize(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [normalize(v) for v in value]
    return value


def save(path, value):
    path.write_text(json.dumps(normalize(value), ensure_ascii=False, indent=2), encoding='utf-8')


def rows(df):
    return sorted(normalize(df.collect()), key=lambda r: json.dumps(r, sort_keys=True))


def digest(value):
    return hashlib.sha256(json.dumps(normalize(value), sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def publish(directory, name, records):
    directory.mkdir(parents=True, exist_ok=True)
    # Hidden temporary file becomes visible atomically; no file is edited after discovery.
    temporary = directory / ('_' + name + '.tmp')
    temporary.write_text('\n'.join(json.dumps(r) for r in records), encoding='utf-8')
    temporary.replace(directory / (name + '.json'))


def source(spark, directory, schema=SCHEMA):
    directory.mkdir(parents=True, exist_ok=True)
    return spark.readStream.schema(schema).option('maxFilesPerTrigger', 1).json(str(directory))


def writer(df, checkpoint, mode='append'):
    return (df.writeStream.outputMode(mode).option('checkpointLocation', str(checkpoint))
            .trigger(processingTime='1 second'))


@contextmanager
def active(query):
    try:
        yield query
    finally:
        query.stop()
        if query.isActive:
            raise AssertionError('Query did not stop')


def progress(query):
    # Spark 4 returns progress objects with a JSON property, including nested operator objects.
    return [json.loads(p.json) if hasattr(p, 'json') else normalize(p) for p in query.recentProgress]


def checkpoint_inventory(checkpoint):
    return sorted(p.relative_to(checkpoint).as_posix() for p in checkpoint.rglob('*') if p.is_file())


def snapshot(spark, target):
    return rows(spark.read.format('delta').load(str(target))) if (target / '_delta_log').exists() else []


def capture(query, spark, target):
    state = snapshot(spark, target)
    return dict(queryId=str(query.id), runId=str(query.runId), active=query.isActive,
                progress=progress(query), target=state, targetHash=digest(state))


def aggregate(df, keys=('user_id',)):
    from pyspark.sql import functions as F
    return df.groupBy(*keys).agg(F.sum('amount').alias('amount'), F.count('*').alias('events'))


def windowed(df, delay=None):
    from pyspark.sql import functions as F
    if delay:
        df = df.withWatermark('event_time', delay)
    return aggregate(df, (F.window('event_time', '10 minutes'),)).selectExpr(
        'window.start as window_start', 'window.end as window_end', 'amount', 'events')


def table_sink(target, mode='complete', keys=(), emissions=None):
    def consume(df, batch_id):
        df.persist()
        try:
            observed = rows(df)  # Full consumption, bounded fixtures only.
            if emissions is not None:
                emissions.append(dict(batchId=batch_id, rows=observed))
            if not observed:
                return
            if mode == 'complete' or not (target / '_delta_log').exists():
                df.write.format('delta').mode('overwrite').save(str(target))
            else:
                df.createOrReplaceTempView('stream_updates')
                predicate = ' AND '.join(f't.`{k}` = s.`{k}`' for k in keys)
                df.sparkSession.sql(f'''MERGE INTO delta.`{target}` t USING stream_updates s ON {predicate}
                    WHEN MATCHED THEN UPDATE SET * WHEN NOT MATCHED THEN INSERT *''')
        finally:
            df.unpersist()
    return consume


def state_metric(record, field):
    return sum(op.get(field, 0) for p in record['progress'] for op in p.get('stateOperators', []))


def watermark(record):
    return max((p.get('eventTime', {}).get('watermark', '') for p in record['progress']), default='')
