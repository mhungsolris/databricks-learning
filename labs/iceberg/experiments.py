"""Bounded Iceberg v2 contracts on a disposable local Hadoop warehouse."""
from hashlib import sha256
from pathlib import Path
import json
import unittest
from labs.spark.common import run_directory, session, write_json, stage_summary

ROOT = Path(__file__).resolve().parents[2]
SOURCES = ['runtime/iceberg.json', 'runtime/spark.json', 'scripts/iceberg_runtime.py',
           'scripts/verify_iceberg.py', 'scripts/test_iceberg.py',
           'labs/iceberg/experiments.py', 'labs/spark/common.py']

def hashes():
    return {p: sha256((ROOT / p).read_text(encoding='utf-8').replace('\r\n', '\n').encode()).hexdigest() for p in SOURCES}

def run(smoke=False):
    out = run_directory('iceberg-smoke' if smoke else 'tests-iceberg')
    write_json(out / 'source-hashes.json', hashes())
    observations = {}
    with session('iceberg-semantics', out) as spark:
        warehouse = out / 'iceberg-warehouse'
        spark.conf.set('spark.sql.catalog.local.warehouse', warehouse.resolve().as_uri())
        spark.conf.set('spark.sql.session.timeZone', 'UTC')
        actual = str(spark._jvm.org.apache.iceberg.IcebergBuild.fullVersion())
        scala = str(spark._jvm.scala.util.Properties.versionNumberString())
        write_json(out / 'iceberg-runtime.json', dict(icebergVersion=actual, scalaVersion=scala,
            catalog='local', type='hadoop', formatVersion=2, warehouse='run-local/iceberg-warehouse',
            runtimeArtifact='org.apache.iceberg:iceberg-spark-runtime-4.0_2.13:1.12.0',
            jarSha256=sha256(Path('/evidence/ivy/jars/org.apache.iceberg_iceberg-spark-runtime-4.0_2.13-1.12.0.jar').read_bytes()).hexdigest()))
        assert spark.version == '4.0.4' and '1.12.0' in actual and scala.startswith('2.13.')
        def sql(statement):
            return spark.sql(statement)
        def rows(statement):
            return [r.asDict(recursive=True) for r in sql(statement).collect()]
        def create(name, extra=''):
            sql(f"CREATE TABLE local.course.{name} (id BIGINT, event_time TIMESTAMP, campaign STRING, revenue BIGINT) USING iceberg {extra} TBLPROPERTIES ('format-version'='2','write.update.mode'='copy-on-write','write.delete.mode'='copy-on-write','write.merge.mode'='copy-on-write')")
        sql('CREATE NAMESPACE local.course')
        class Contracts(unittest.TestCase):
            def test_01_create_query(self):
                create('events')
                sql("INSERT INTO local.course.events VALUES (1,TIMESTAMP '2026-10-01 10:00:00','A',100),(2,TIMESTAMP '2026-10-02 10:00:00','B',200)")
                self.assertEqual(rows('SELECT id,revenue FROM local.course.events ORDER BY id'), [dict(id=1,revenue=100),dict(id=2,revenue=200)])
                snapshots = rows('SELECT snapshot_id,operation FROM local.course.events.snapshots')
                self.assertEqual(len(snapshots), 1)
                observations['smoke'] = dict(rows=2, revenue=300, snapshotExists=True)
            def test_02_snapshot_time_travel(self):
                before = rows('SELECT snapshot_id FROM local.course.events.snapshots')[0]['snapshot_id']
                sql("INSERT INTO local.course.events VALUES (3,TIMESTAMP '2026-10-02 11:00:00','A',50)")
                self.assertEqual(sql(f'SELECT * FROM local.course.events VERSION AS OF {before}').count(),2)
                self.assertEqual(sql('SELECT * FROM local.course.events').count(),3)
                history = rows('SELECT snapshot_id,parent_id,operation FROM local.course.events.snapshots ORDER BY committed_at')
                self.assertEqual(history[1]['parent_id'],before)
                observations['snapshots'] = dict(oldRows=2,currentRows=3,history=history)
            def test_03_schema_field_identity(self):
                sql('ALTER TABLE local.course.events ADD COLUMN country STRING')
                sql('ALTER TABLE local.course.events RENAME COLUMN campaign TO campaign_id')
                sql("INSERT INTO local.course.events VALUES (4,TIMESTAMP '2026-10-03 00:00:00','C',70,'VN')")
                self.assertEqual(rows('SELECT campaign_id,country FROM local.course.events WHERE id=1'),[dict(campaign_id='A',country=None)])
                metas=sorted((warehouse / 'course/events/metadata').glob('v*.metadata.json'),key=lambda p:int(p.name.split('.')[0][1:]))
                first=json.loads(metas[0].read_text()); latest=json.loads(metas[-1].read_text())
                oldfields=first['schemas'][0]['fields']
                newfields=latest['schemas'][-1]['fields']
                oldid=next(f['id'] for f in oldfields if f['name']=='campaign')
                newid=next(f['id'] for f in newfields if f['name']=='campaign_id')
                self.assertEqual(oldid,newid)
                observations['schema']=dict(renamedFieldId=newid,oldRowsCountryNull=True,rows=4)
            def test_04_partition_evolution(self):
                create('evolving','PARTITIONED BY (days(event_time))')
                sql("INSERT INTO local.course.evolving VALUES (1,TIMESTAMP '2026-10-01 00:00:00','A',100),(2,TIMESTAMP '2026-10-02 00:00:00','B',200)")
                old=rows('SELECT file_path,spec_id FROM local.course.evolving.files')
                sql('ALTER TABLE local.course.evolving REPLACE PARTITION FIELD days(event_time) WITH bucket(4,campaign)')
                sql("INSERT INTO local.course.evolving VALUES (3,TIMESTAMP '2026-10-03 00:00:00','A',50)")
                files=rows('SELECT file_path,spec_id,record_count FROM local.course.evolving.files')
                self.assertEqual(len({r['spec_id'] for r in files}),2)
                self.assertTrue({r['file_path'] for r in old}.issubset({r['file_path'] for r in files}))
                self.assertEqual(rows('SELECT count(*) AS n,sum(revenue) AS revenue FROM local.course.evolving'),[dict(n=3,revenue=350)])
                self.assertEqual(sql("SELECT * FROM local.course.evolving WHERE campaign='A'").count(),2)
                observations['partition']=dict(specIds=sorted({r['spec_id'] for r in files}),oldFilesRetained=True,rows=3,revenue=350)
            def test_05_copy_on_write_merge(self):
                create('mutations')
                sql("INSERT INTO local.course.mutations VALUES (1,TIMESTAMP '2026-10-01 00:00:00','A',100),(2,TIMESTAMP '2026-10-01 00:00:00','B',200)")
                sql('UPDATE local.course.mutations SET revenue=110 WHERE id=1')
                sql('DELETE FROM local.course.mutations WHERE id=2')
                sql("MERGE INTO local.course.mutations t USING (SELECT 1L id, TIMESTAMP '2026-10-01 00:00:00' event_time,'A' campaign,120L revenue UNION ALL SELECT 3L,TIMESTAMP '2026-10-01 00:00:00','C',50L) s ON t.id=s.id WHEN MATCHED THEN UPDATE SET * WHEN NOT MATCHED THEN INSERT *")
                self.assertEqual(rows('SELECT id,revenue FROM local.course.mutations ORDER BY id'),[dict(id=1,revenue=120),dict(id=3,revenue=50)])
                self.assertTrue(all(r['content']==0 for r in rows('SELECT content FROM local.course.mutations.files')))
                observations['mutations']=dict(strategy='copy-on-write',rows=2,revenue=170,operations=['UPDATE','DELETE','MERGE'],dataFilesOnly=True)
            def test_06_merge_on_read_delete(self):
                create('mor')
                sql("ALTER TABLE local.course.mor SET TBLPROPERTIES ('write.delete.mode'='merge-on-read')")
                sql("SELECT 1L id,TIMESTAMP '2026-10-01 00:00:00' event_time,'A' campaign,100L revenue UNION ALL SELECT 2L,TIMESTAMP '2026-10-01 00:00:00','B',200L").coalesce(1).writeTo('local.course.mor').append()
                sql('DELETE FROM local.course.mor WHERE id=1')
                files=rows('SELECT content,record_count FROM local.course.mor.files')
                self.assertTrue(any(f['content']==1 for f in files))
                self.assertEqual(rows('SELECT id,revenue FROM local.course.mor'),[dict(id=2,revenue=200)])
                observations['mor']=dict(files=files,positionDeleteObserved=True,rows=1,revenue=200,equalityDeleteExecuted=False,v3Executed=False)
            def test_07_metadata_integrity(self):
                snapshots=rows('SELECT snapshot_id,manifest_list FROM local.course.events.snapshots ORDER BY committed_at')
                manifests=rows('SELECT path,length,partition_spec_id,added_data_files_count FROM local.course.events.manifests')
                data=rows('SELECT file_path,record_count FROM local.course.events.files')
                for r in snapshots:
                    self.assertTrue(Path(r['manifest_list'].removeprefix('file:')).is_file())
                for r in manifests:
                    self.assertGreater(r['length'],0)
                    self.assertTrue(Path(r['path'].removeprefix('file:')).is_file())
                for r in data:
                    self.assertTrue(Path(r['file_path'].removeprefix('file:')).is_file())
                self.assertEqual(sum(r['record_count'] for r in data),4)
                # Export selected metadata JSON and SQL-decoded Avro metadata, not Parquet payloads.
                meta=sorted((warehouse / 'course/events/metadata').glob('v*.metadata.json'),key=lambda p:int(p.name.split('.')[0][1:]))[-1]
                document=json.loads(meta.read_text())
                self.assertEqual(document['current-snapshot-id'],snapshots[-1]['snapshot_id'])
                write_json(out / 'table-metadata.json',document)
                write_json(out / 'metadata-tables.json',json.loads(json.dumps(dict(snapshots=snapshots,manifests=manifests,files=data,
                    history=rows('SELECT made_current_at,snapshot_id,is_current_ancestor FROM local.course.events.history')),default=str)))
                observations['metadata']=dict(snapshotCount=len(snapshots),manifestCount=len(manifests),dataFileCount=len(data),referencedFilesExist=True)
        names=['test_01_create_query'] if smoke else unittest.defaultTestLoader.getTestCaseNames(Contracts)
        result=unittest.TextTestRunner(verbosity=2).run(unittest.TestSuite(Contracts(n) for n in names))
        # SQL timestamps are represented as strings only in exported metadata evidence.
        write_json(out / 'results.json',json.loads(json.dumps(observations,default=str)))
        write_json(out / 'tests.json',dict(testsRun=result.testsRun,failures=len(result.failures),errors=len(result.errors),skipped=len(result.skipped),successful=result.wasSuccessful()))
    stage_summary(out)
    print(f'EVIDENCE {out}',flush=True)
    if not result.wasSuccessful(): raise SystemExit(1)
