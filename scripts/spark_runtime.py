"""Dispatch a repository Spark program into the pinned local Linux container."""
from pathlib import Path
import json
import subprocess

ROOT = Path(__file__).resolve().parents[1]
CONFIG = json.loads((ROOT / 'runtime/spark.json').read_text(encoding='utf-8'))


def launch(script, args=(), *, ui=False, delta=False):
    root = ROOT / '.skills-test/spark'
    root.mkdir(parents=True, exist_ok=True)
    command = ['docker', 'run', '--rm', '--user', '0:0', '--cpus', CONFIG['cpus'], '--memory', CONFIG['memory'],
               '--mount', f'type=bind,source={ROOT},target=/workspace,readonly',
               '--mount', f'type=bind,source={root},target=/evidence',
               '--workdir', '/workspace', '--env', 'LAB_EVIDENCE_ROOT=/evidence',
               '--env', 'SPARK_LOCAL_IP=' + ('0.0.0.0' if ui else '127.0.0.1'), '--env', 'SPARK_LAB_CONTAINER=1']
    if ui:
        command += ['--publish', '127.0.0.1:4040:4040']
    command += ['--entrypoint', '/opt/spark/bin/spark-submit', CONFIG['image'],
                '--master', CONFIG['master'], '--driver-memory', CONFIG['driverMemory']]
    if ui:
        command += ['--conf', 'spark.driver.bindAddress=0.0.0.0', '--conf', 'spark.driver.host=127.0.0.1']
    if delta:
        command += ['--packages', f'io.delta:delta-spark_2.13:{CONFIG["deltaVersion"]}',
                    '--repositories', 'https://repo.maven.apache.org/maven2',
                    '--conf', 'spark.jars.ivy=/evidence/ivy',
                    '--conf', 'spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension',
                    '--conf', 'spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog']
    command += [f'/workspace/{script}', *args]
    return subprocess.call(command, cwd=ROOT)
