"""Integration contracts assert real target states, replay boundaries and state metrics."""
import os
from pathlib import Path
import sys
import unittest


def main():
    if not os.environ.get('SPARK_LAB_CONTAINER'):
        from spark_runtime import launch
        return launch('scripts/test_streaming.py', sys.argv[1:], delta=True)
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from labs.spark.common import session, run_directory, stage_summary
    from labs.streaming.common import save
    from labs.streaming.experiments import LABS
    from scripts.snapshot_streaming_evidence import SOURCES
    import hashlib
    output = run_directory('tests-streaming')
    repo = Path(__file__).resolve().parents[1]
    save(output / 'source-hashes.json', {name: hashlib.sha256((repo / name).read_text(encoding='utf-8').encode()).hexdigest() for name in SOURCES})
    with session('streaming-contracts', output) as spark:
        spark.conf.set('spark.sql.session.timeZone', 'UTC')
        save(output / 'streaming-config.json', {k: spark.conf.get(k) for k in [
            'spark.sql.session.timeZone', 'spark.sql.streaming.stateStore.providerClass',
            'spark.sql.streaming.multipleWatermarkPolicy', 'spark.sql.streaming.noDataMicroBatches.enabled']})
        class Contracts(unittest.TestCase):
            def execute(self, number):
                folder = output / ('lab' + number)
                folder.mkdir()
                result = LABS[number](spark, folder)
                save(folder / 'result.json', result)
                self.assertEqual(len(spark.streams.active), 0)
                return result
        def test(number):
            def run(self):
                self.execute(number)
            return run
        for number in LABS:
            setattr(Contracts, 'test_' + number, test(number))
        suite = (unittest.defaultTestLoader.loadTestsFromNames(sys.argv[1:], Contracts) if sys.argv[1:]
                 else unittest.defaultTestLoader.loadTestsFromTestCase(Contracts))
        result = unittest.TextTestRunner(verbosity=2).run(suite)
        save(output / 'test-summary.json', dict(testsRun=result.testsRun, failures=len(result.failures),
             errors=len(result.errors), skipped=len(result.skipped), successful=result.wasSuccessful()))
    stages = stage_summary(output)
    print(f'Evidence: {output}; stages={len(stages)}', flush=True)
    return 0 if result.wasSuccessful() and stages else 1


if __name__ == '__main__':
    raise SystemExit(main())
