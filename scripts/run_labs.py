"""Run every portable lab, including the learner SQL submission path."""
from pathlib import Path
import subprocess
import sys


def run(*args, expected=0):
    result = subprocess.run([sys.executable, *args], capture_output=True, text=True)
    print(result.stdout, end='')
    if result.returncode != expected:
        print(result.stderr)
        raise SystemExit(f'Lab returned {result.returncode}, expected {expected}: {args}')
    return result


if __name__ == '__main__':
    from labs.foundations.grain_fanout import FIXED_SQL, WRONG_SQL

    root = Path('.skills-test/lab-verification')
    root.mkdir(parents=True, exist_ok=True)
    # Fresh isolated fixtures avoid files retained by manual failure drills.
    run('labs/foundations/files_and_tables.py', '--output', str(root / 'files-00'))
    run('labs/foundations/grain_fanout.py')
    for name, sql, expected in [('wrong', WRONG_SQL, 1), ('fixed', FIXED_SQL, 0)]:
        path = root / f'{name}.sql'
        path.write_text(sql, encoding='utf-8')
        result = run('labs/foundations/grain_fanout.py', '--query-file', str(path), expected=expected)
        if expected and 'Report contract failed' not in result.stderr:
            raise SystemExit('Wrong report failed for an unexpected reason')
    run('labs/foundations/layout_contract.py', '--output', str(root / 'layout-02'))
    run('labs/spark/pipeline_model.py', '--output', str(root / 'pipeline-03.csv'))
    print('PASS four portable labs and SQL submission failure/success. No Spark runtime claim.')
