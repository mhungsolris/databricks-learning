"""Run Iceberg semantic integration contracts, never speed comparisons."""
import os
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
if not os.environ.get('SPARK_LAB_CONTAINER'):
    from scripts.iceberg_runtime import launch
    raise SystemExit(launch('scripts/test_iceberg.py'))
from labs.iceberg.experiments import run
run()
