"""Bounded real Spark labs. Assertions concern semantics and operator families."""
import json
from pathlib import Path
from pyspark.sql import functions as F
from labs.spark.common import groups, plan, write_json


def pipeline(spark, out):
    source = spark.createDataFrame([('T1', 'A', 100, 'paid'), ('T2', 'A', 200, 'paid'),
                                    ('T3', 'B', 50, 'paid'), ('T4', 'A', 900, 'cancelled')],
                                   'id string, campaign_id string, revenue long, status string')
    lookup = spark.createDataFrame([('A', 'VN'), ('B', 'US')], 'campaign_id string, country string')
    spark.sparkContext.setJobGroup('lab03', 'Lab 03 action boundary')
    query = source.filter("status = 'paid'").join(lookup, 'campaign_id').groupBy('campaign_id', 'country').sum('revenue')
    before = list(spark.sparkContext.statusTracker().getJobIdsForGroup('lab03'))
    text = plan(query, out, 'pipeline')
    after_plan = list(spark.sparkContext.statusTracker().getJobIdsForGroup('lab03'))
    rows = sorted((r[0], r[1], r[2]) for r in query.collect())
    after = list(spark.sparkContext.statusTracker().getJobIdsForGroup('lab03'))
    assert before == after_plan == [] and after and rows == [('A', 'VN', 300), ('B', 'US', 50)]
    source.createOrReplaceTempView('events03')
    lookup.createOrReplaceTempView('campaigns03')
    sql = spark.sql("SELECT campaign_id, country, SUM(revenue) FROM events03 JOIN campaigns03 USING (campaign_id) WHERE status = 'paid' GROUP BY campaign_id, country")
    assert sorted(tuple(r) for r in sql.collect()) == rows
    query.write.parquet(str(out / 'report'))
    assert sorted(tuple(r) for r in spark.read.parquet(str(out / 'report')).collect()) == rows
    assert 'Logical Plan' in text and 'Physical Plan' in text and 'Exchange' in text
    return {'rows': rows, 'jobsBeforeAction': before, 'jobsAfterExplain': after_plan, 'jobsAfterAction': after}


def partitioning(spark, out):
    base = spark.range(120, numPartitions=4)
    variants = {'input': base, 'repartition6': base.repartition(6),
                'coalesce2': base.coalesce(2), 'coalesce8': base.coalesce(8)}
    result = {}
    for name, df in variants.items():
        text = plan(df, out, name)
        result[name] = {'partitions': df.rdd.getNumPartitions(), 'distribution': groups(df)}
        assert sum(r['rows'] for r in result[name]['distribution']) == 120
        if name == 'repartition6': assert 'Exchange' in text
        if name == 'coalesce2': assert 'Coalesce 2' in text and 'Exchange' not in text
    assert [result[n]['partitions'] for n in variants] == [4, 6, 2, 4]
    return result


def shuffle(spark, out):
    spark.sparkContext.setJobGroup('lab05', 'Lab 05 query boundaries')
    base = spark.range(120, numPartitions=4).withColumn('key', F.col('id') % 3)
    narrow = base.filter('id >= 60').select('id', 'key')
    aggregate = base.groupBy('key').count()
    ordered = base.orderBy(F.desc('key'), 'id')
    original = spark.conf.get('spark.sql.autoBroadcastJoinThreshold')
    spark.conf.set('spark.sql.autoBroadcastJoinThreshold', '-1')
    try:
        lookup = spark.range(3).select(F.col('id').alias('key'))
        joined = base.join(lookup, 'key')
        result = {}
        for name, df in [('narrow', narrow), ('aggregate', aggregate), ('order', ordered), ('join', joined)]:
            tracker = spark.sparkContext.statusTracker()
            before_jobs = set(tracker.getJobIdsForGroup('lab05'))
            text = plan(df, out, name)
            # collect executes the recorded query itself; count() can optimize away a sort.
            rows = df.collect()
            jobs = sorted(set(tracker.getJobIdsForGroup('lab05')) - before_jobs)
            stages = sorted({sid for jid in jobs for sid in tracker.getJobInfo(jid).stageIds})
            result[name] = {'rows': len(rows), 'exchange': 'Exchange' in text, 'jobIds': jobs, 'stageIds': stages}
            assert result[name]['exchange'] == (name != 'narrow')
            if name == 'order':
                actual = [(r.key, r.id) for r in rows]
                assert actual == sorted(actual, key=lambda value: (-value[0], value[1]))
        assert result['narrow']['rows'] == 60 and result['join']['rows'] == 120
        assert sorted(r['count'] for r in aggregate.collect()) == [40, 40, 40]
        return result
    finally:
        spark.conf.set('spark.sql.autoBroadcastJoinThreshold', original)


def joins(spark, out):
    fact = spark.range(10000, numPartitions=4).withColumn('campaign_id',
        F.when(F.col('id') < 7000, F.lit('UNKNOWN')).otherwise(F.concat(F.lit('C'), (F.col('id') % 100).cast('string'))))
    dimension = spark.createDataFrame([('UNKNOWN', 'unmapped')] + [(f'C{i}', 'known') for i in range(100)],
                                     'campaign_id string, category string')
    original = spark.conf.get('spark.sql.autoBroadcastJoinThreshold')
    spark.conf.set('spark.sql.autoBroadcastJoinThreshold', '-1')
    try:
        normal = fact.join(dimension, 'campaign_id')
        broadcast = fact.join(F.broadcast(dimension), 'campaign_id')
        normal_plan = plan(normal, out, 'sort-merge')
        broadcast_plan = plan(broadcast, out, 'broadcast')
        assert 'SortMergeJoin' in normal_plan and 'Exchange' in normal_plan
        assert 'BroadcastHashJoin' in broadcast_plan and 'BroadcastExchange' in broadcast_plan
        assert 'hashpartitioning' not in broadcast_plan.split('== Physical Plan ==')[1]
        n, b = normal.count(), broadcast.count()
        assert n == b == 10000
        assert normal.agg(F.sum('id')).first()[0] == broadcast.agg(F.sum('id')).first()[0] == 49995000
        hashed = fact.repartition(4, 'campaign_id')
        distribution = groups(hashed)
        hot = hashed.filter("campaign_id = 'UNKNOWN'").select(F.spark_partition_id().alias('p')).distinct().collect()
        assert len(hot) == 1 and max(r['rows'] for r in distribution) >= 7000
        duplicated = dimension.union(spark.createDataFrame([('UNKNOWN', 'duplicate')], dimension.schema))
        fanout = fact.join(F.broadcast(duplicated), 'campaign_id').count()
        assert fanout == 17000
        null_fact = spark.createDataFrame([(1, None), (2, 'C1')], 'id long, campaign_id string')
        null_dim = spark.createDataFrame([(None,), ('C1',)], 'campaign_id string')
        eq = null_fact.join(null_dim, 'campaign_id').count()
        nullsafe = null_fact.alias('f').join(null_dim.alias('d'), F.col('f.campaign_id').eqNullSafe(F.col('d.campaign_id'))).count()
        assert (eq, nullsafe) == (1, 2)
        return {'factRows': 10000, 'dimensionRows': 101, 'normalRows': n, 'broadcastRows': b,
                'idSum': 49995000, 'hotRows': 7000, 'hotPartition': hot[0].p,
                'hashDistribution': distribution, 'duplicateLookupRows': fanout,
                'equalityNullRows': eq, 'nullSafeRows': nullsafe}
    finally:
        spark.conf.set('spark.sql.autoBroadcastJoinThreshold', original)


def parquet(spark, out):
    data = (spark.range(120, numPartitions=4).withColumn('campaign_id', F.concat(F.lit('C'), (F.col('id') % 3).cast('string')))
            .withColumn('revenue', F.col('id') * 10)
            .withColumn('date', F.when(F.col('id') < 60, F.lit('2026-10-01')).otherwise(F.lit('2026-10-02')))
            .withColumn('payload', F.lit('unused analytics payload')))
    target = out / 'parquet'
    data.coalesce(2).write.mode('errorifexists').parquet(str(target))
    files = sorted(target.glob('*.parquet'))
    inventory = []
    for file in files:
        raw = file.read_bytes()
        assert raw[:4] == raw[-4:] == b'PAR1'
        footer = spark._jvm.org.apache.parquet.hadoop.ParquetFileReader.readFooter(
            spark.sparkContext._jsc.hadoopConfiguration(), spark._jvm.org.apache.hadoop.fs.Path(str(file)))
        block = footer.getBlocks().get(0)
        inventory.append({'file': file.name, 'bytes': len(raw), 'footerBytes': int.from_bytes(raw[-8:-4], 'little'),
                          'rowGroups': footer.getBlocks().size(), 'rows': block.getRowCount(),
                          'codec': str(block.getColumns().get(0).getCodec())})
    assert len(files) == 2 and sum(f['rows'] for f in inventory) == 120
    read = spark.read.parquet(str(target))
    projected = read.filter("date = '2026-10-01'").select('campaign_id', 'revenue')
    text = plan(projected, out, 'parquet-projection-filter')
    physical = text.split('== Physical Plan ==')[1]
    assert 'PushedFilters:' in physical and 'EqualTo(date,2026-10-01)' in physical
    schema = physical.split('ReadSchema:')[1]
    import re
    assert 'payload' not in schema and not re.search(r'(?:<|,)id:', schema)
    assert projected.count() == 60
    partitioned = out / 'date-partitioned'
    data.coalesce(2).write.partitionBy('date').mode('errorifexists').parquet(str(partitioned))
    pruned = spark.read.parquet(str(partitioned)).filter("date = '2026-10-01'").select('campaign_id', 'revenue')
    partition_plan = plan(pruned, out, 'storage-partition-filter')
    assert 'PartitionFilters:' in partition_plan and '2026-10-01' in partition_plan and pruned.count() == 60
    assert read.count() == 120
    return {'rows': 120, 'filteredRows': 60, 'files': inventory,
            'storageDirectories': sorted(p.name for p in partitioned.glob('date=*'))}


def delta(spark, out):
    target = out / 'delta-table'
    path = str(target)
    spark.createDataFrame([(1, 100), (2, 200)], 'id long, revenue long').coalesce(1).write.format('delta').save(path)
    spark.createDataFrame([(3, 300)], 'id long, revenue long').coalesce(1).write.format('delta').mode('append').save(path)
    spark.sql(f'UPDATE delta.`{path}` SET revenue = 150 WHERE id = 1')
    current = sorted(tuple(r) for r in spark.read.format('delta').load(path).collect())
    old = sorted(tuple(r) for r in spark.read.format('delta').option('versionAsOf', 0).load(path).collect())
    assert current == [(1, 150), (2, 200), (3, 300)] and old == [(1, 100), (2, 200)]
    history = [r.asDict() for r in spark.sql(f'DESCRIBE HISTORY delta.`{path}`').select('version', 'operation').collect()]
    commits = {}
    live = set()
    for log in sorted((target / '_delta_log').glob('*.json')):
        actions = [json.loads(line) for line in log.read_text().splitlines()]
        adds = [a['add']['path'] for a in actions if 'add' in a]
        removes = [a['remove']['path'] for a in actions if 'remove' in a]
        live.difference_update(removes)
        live.update(adds)
        commits[log.name] = {'add': adds, 'remove': removes, 'snapshotFiles': sorted(live),
                             'actionTypes': sorted({key for a in actions for key in a})}
    assert len(commits) == 3 and any(c['remove'] for c in commits.values())
    # Atomic rejection: incompatible schema must not create a new version.
    try:
        spark.createDataFrame([(4, 'bad')], 'id long, revenue string').write.format('delta').mode('append').save(path)
    except Exception as exc:
        assert 'schema' in str(exc).lower() or 'merge' in str(exc).lower()
    else:
        raise AssertionError('Incompatible schema unexpectedly accepted')
    assert len(list((target / '_delta_log').glob('*.json'))) == 3
    return {'current': current, 'version0': old, 'history': history, 'commits': commits, 'schemaRejection': True}


LABS = {'03': pipeline, '04': partitioning, '05': shuffle, '06': joins, '07': parquet, '08': delta}
