"""Local platform evidence provenance shared by executor and integrity checker."""
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCES = [
    "labs/platform/fixtures.json", "labs/platform/contracts.py",
    "labs/platform/src/roas_task.py", "labs/platform/src/medallion.py",
    "labs/platform/databricks.yml", "labs/platform/resources/roas.job.yml",
    "labs/platform/resources/medallion.pipeline.yml", "labs/platform/governance-policy.json",
    "labs/platform/sql/silver.sql", "labs/platform/sql/gold.sql",
    "labs/platform/sql/serving.sql", "labs/platform/sql/governance.sql",
    "tests/test_platform_artifacts.py", "scripts/test_platform.py",
    "scripts/platform_evidence.py", "scripts/spark_runtime.py", "labs/spark/common.py",
    "runtime/spark.json",
]
def source_hashes():
    return {name: sha256((ROOT / name).read_text(encoding="utf-8").replace("\r\n", "\n").encode("utf-8")).hexdigest()
            for name in SOURCES}
