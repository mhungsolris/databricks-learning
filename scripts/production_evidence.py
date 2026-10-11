"""Normalized startup source fingerprints for reproducible local experiments."""
from hashlib import sha256
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
SOURCES = ["labs/production/model.py", "labs/production/src/transforms.py", "labs/production/src/expectations.py",
           "labs/production/src/fixtures.json", "labs/production/src/roas.py", "labs/production/databricks.yml",
           "labs/production/resources/roas.job.yml", "labs/production/tests/test_contracts.py",
           "scripts/test_production.py", "scripts/production_evidence.py", "scripts/check_production_config.py",
           ".github/workflows/roas-release.yml", "runtime/spark.json", "labs/spark/common.py", "scripts/spark_runtime.py"]
def source_hashes():
    return {n: sha256((ROOT / n).read_text(encoding="utf-8").replace("\r\n", "\n").encode()).hexdigest() for n in SOURCES}
