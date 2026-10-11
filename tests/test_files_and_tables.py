import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('lab', ROOT / 'labs/foundations/files_and_tables.py')
lab = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lab)


class SnapshotContractTests(unittest.TestCase):
    def test_old_files_are_excluded_from_snapshot(self):
        with tempfile.TemporaryDirectory(prefix='lab-00-') as directory:
            output = Path(directory)
            lab.write_sample(output)
            self.assertEqual(lab.inspect_snapshot(output), (650, 350))
            # Retention of additional copies must not affect active snapshot totals.
            (output / 'retained-copy.csv').write_bytes((output / 'old.csv').read_bytes())
            self.assertEqual(lab.inspect_snapshot(output), (950, 350))

    def test_missing_active_file_fails_instead_of_partial_success(self):
        with tempfile.TemporaryDirectory(prefix='lab-00-') as directory:
            output = Path(directory)
            lab.write_sample(output)
            # Point metadata at absent data; never silently serve an incomplete snapshot.
            (output / 'snapshot.json').write_text('{"active_files": ["absent.csv"]}', encoding='utf-8')
            with self.assertRaisesRegex(FileNotFoundError, 'Active snapshot file missing'):
                lab.inspect_snapshot(output)


if __name__ == '__main__':
    unittest.main()
