"""Independent Iceberg dispatch; preserves the accepted Spark/Delta launcher."""
from pathlib import Path
import json
import subprocess

ROOT = Path(__file__).resolve().parents[1]

def launch(script, args=()):
    spark = json.loads((ROOT / 'runtime/spark.json').read_text())
    iceberg = json.loads((ROOT / 'runtime/iceberg.json').read_text())
    evidence = ROOT / '.skills-test/spark'
    evidence.mkdir(parents=True, exist_ok=True)
    command = ['docker', 'run', '--rm', '--user', '0:0', '--cpus', spark['cpus'],
               '--memory', spark['memory'],
               '--mount', f'type=bind,source={ROOT},target=/workspace,readonly',
               '--mount', f'type=bind,source={evidence},target=/evidence',
               '--workdir', '/workspace', '--env', 'LAB_EVIDENCE_ROOT=/evidence',
               '--env', 'SPARK_LOCAL_IP=127.0.0.1', '--env', 'SPARK_LAB_CONTAINER=1',
               '--entrypoint', '/opt/spark/bin/spark-submit', spark['image'],
               '--master', spark['master'], '--driver-memory', spark['driverMemory'],
               '--packages', iceberg['artifact'], '--repositories', 'https://repo.maven.apache.org/maven2',
               '--conf', 'spark.jars.ivy=/evidence/ivy',
               '--conf', 'spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions',
               '--conf', 'spark.sql.catalog.local=org.apache.iceberg.spark.SparkCatalog',
               '--conf', 'spark.sql.catalog.local.type=hadoop',
               f'/workspace/{script}', *args]
    return subprocess.call(command, cwd=ROOT)
