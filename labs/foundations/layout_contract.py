"""Observe file selection, table-like manifest and schema validation, not ACID."""
import argparse
import csv
import json
from pathlib import Path


def generate(root):
    root.mkdir(parents=True, exist_ok=True)
    for name, rows in [('part-1.csv', [('T1', 100), ('T2', 200)]), ('part-2.csv', [('T3', 50)])]:
        with (root / name).open('w', newline='', encoding='utf-8') as output:
            writer = csv.writer(output)
            writer.writerow(['transaction_id', 'revenue'])
            writer.writerows(rows)
    (root / 'snapshot.json').write_text(json.dumps({'version': 1, 'files': ['part-1.csv', 'part-2.csv']}), encoding='utf-8')


def read_contract(root, files):
    seen = set()
    total = 0
    if len(files) != len(set(files)):
        raise ValueError('Repeated file membership')
    for name in files:
        with (root / name).open(encoding='utf-8', newline='') as source:
            reader = csv.DictReader(source)
            if reader.fieldnames != ['transaction_id', 'revenue']:
                raise ValueError(f'Schema mismatch: {name}')
            for row in reader:
                if not row['transaction_id'] or row['transaction_id'] in seen:
                    raise ValueError('Invalid or repeated transaction_id')
                seen.add(row['transaction_id'])
                total += int(row['revenue'])
    return len(seen), total


def inspect(root):
    manifest = json.loads((root / 'snapshot.json').read_text(encoding='utf-8'))
    return read_contract(root, manifest['files'])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, default=Path('.skills-test/lab-02'))
    parser.add_argument('--inspect-only', action='store_true')
    args = parser.parse_args()
    if not args.inspect_only:
        generate(args.output)
    print('Contract rows/revenue:', inspect(args.output))
    print('CSV/manifest experiment only: no transaction, concurrent writer or multi-engine guarantee.')
