"""Real create/insert/snapshot/query smoke, with clean shutdown evidence."""
import os
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
if not os.environ.get('SPARK_LAB_CONTAINER'):
    from scripts.iceberg_runtime import launch
    raise SystemExit(launch('scripts/verify_iceberg.py'))
from labs.iceberg.experiments import run
run(smoke=True)
