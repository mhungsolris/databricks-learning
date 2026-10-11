"""Verify selected local semantic evidence and its startup source fingerprints."""
from pathlib import Path
from hashlib import sha256
import argparse,json,shutil,sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from labs.iceberg.experiments import hashes
PUBLIC=ROOT/'docs/public/evidence/iceberg'
FILES=['runtime.json','iceberg-runtime.json','source-hashes.json','results.json','tests.json',
       'shutdown.json','stages.json','table-metadata.json','metadata-tables.json']
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def check(directory):
    tests=read(directory/'tests.json')
    assert tests==dict(testsRun=7,failures=0,errors=0,skipped=0,successful=True),'Incomplete/failed Iceberg tests'
    assert read(directory/'source-hashes.json')==hashes(),'Stale Iceberg source evidence'
    assert read(directory/'runtime.json')['sparkVersion']=='4.0.4'
    runtime=read(directory/'iceberg-runtime.json')
    assert '1.12.0' in runtime['icebergVersion'] and runtime['scalaVersion'].startswith('2.13.')
    assert runtime['catalog']=='local' and runtime['type']=='hadoop' and runtime['formatVersion']==2
    assert read(directory/'shutdown.json')=={'clean':True}
    assert len(read(directory/'stages.json'))>0
    r=read(directory/'results.json')
    assert r['smoke']==dict(rows=2,revenue=300,snapshotExists=True)
    assert r['snapshots']['oldRows']==2 and r['snapshots']['currentRows']==3
    history=r['snapshots']['history']
    assert len(history)==2 and history[1]['parent_id']==history[0]['snapshot_id']
    assert r['schema']['oldRowsCountryNull'] and r['schema']['rows']==4
    assert r['partition']==dict(specIds=[0,1],oldFilesRetained=True,rows=3,revenue=350)
    assert r['mutations']==dict(strategy='copy-on-write',rows=2,revenue=170,operations=['UPDATE','DELETE','MERGE'],dataFilesOnly=True)
    assert r['mor']['positionDeleteObserved'] and r['mor']['rows']==1 and r['mor']['revenue']==200
    assert not r['mor']['equalityDeleteExecuted'] and not r['mor']['v3Executed']
    assert any(f['content']==1 for f in r['mor']['files'])
    metadata=read(directory/'table-metadata.json');tables=read(directory/'metadata-tables.json')
    assert metadata['format-version']==2
    assert metadata['current-snapshot-id'] in {s['snapshot_id'] for s in tables['snapshots']}
    assert sum(f['record_count'] for f in tables['files'])==4
    assert r['metadata']['referencedFilesExist'] and tables['manifests']
    for snapshot in metadata['snapshots']:
        assert snapshot['manifest-list'] in {s['manifest_list'] for s in tables['snapshots']}
    if (directory/'manifest.json').exists():
        manifest=read(directory/'manifest.json')
        assert set(manifest['files'])==set(FILES)
        for name,expected in manifest['files'].items():
            assert sha256((directory/name).read_bytes()).hexdigest()==expected,'Altered artifact '+name
    return r
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--snapshot',type=Path);parser.add_argument('--directory',type=Path,default=PUBLIC)
    args=parser.parse_args()
    if args.snapshot:
        directory=args.snapshot.resolve()
        assert directory.is_relative_to((ROOT/'.skills-test/spark/tests-iceberg').resolve()),'Snapshot outside isolated test runs'
        check(directory)
        PUBLIC.mkdir(parents=True,exist_ok=True)
        for name in FILES:shutil.copyfile(directory/name,PUBLIC/name)
        manifest=dict(sourceRun=directory.name,verified='2026-10-11',tier='LOCAL ICEBERG',
                      files={n:sha256((PUBLIC/n).read_bytes()).hexdigest() for n in FILES})
        (PUBLIC/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
    check(args.directory)
    print('PASS Iceberg7 contracts,9 selected artifacts,7 startup sources,metadata and clean shutdown')
