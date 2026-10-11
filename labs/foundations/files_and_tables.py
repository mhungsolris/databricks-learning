"""FREE lab: a directory listing is not a table snapshot. Python 3.10+, no packages."""
import argparse
import csv
import json
from pathlib import Path

EVENTS = [
    {'event_id': 'e1', 'campaign': 'A', 'revenue': 100},
    {'event_id': 'e2', 'campaign': 'A', 'revenue': 200},
    {'event_id': 'e3', 'campaign': 'B', 'revenue': 50},
]


def write_sample(output):
    output.mkdir(parents=True, exist_ok=True)
    for filename, rows in [('old.csv', EVENTS[:2]), ('current.csv', EVENTS)]:
        with (output / filename).open('w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['event_id', 'campaign', 'revenue'])
            writer.writeheader(); writer.writerows(rows)
    manifest = {'version': 2, 'active_files': ['current.csv']}
    (output / 'snapshot.json').write_text(json.dumps(manifest, indent=2), encoding='utf-8')
    return manifest


def read_revenue(paths):
    total = 0
    for path in paths:
        with path.open(encoding='utf-8', newline='') as file:
            total += sum(int(row['revenue']) for row in csv.DictReader(file))
    return total


def inspect_snapshot(output):
    manifest = json.loads((output / 'snapshot.json').read_text(encoding='utf-8'))
    active = [output / filename for filename in manifest['active_files']]
    # Detect missing active data before making a partial aggregate look successful.
    missing = [p.name for p in active if not p.is_file()]
    if missing:
        raise FileNotFoundError(f'Active snapshot file missing: {missing}')
    return read_revenue(sorted(output.glob('*.csv'))), read_revenue(active)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('.skills-test/lab-00'))
    parser.add_argument('--inspect-only', action='store_true', help='Read existing files without recreating the fixture')
    args = parser.parse_args()
    if not args.inspect_only:
        write_sample(args.output)
    glob_total, snapshot_total = inspect_snapshot(args.output)
    print(f'Glob revenue: {glob_total}')
    print(f'Snapshot revenue: {snapshot_total}')
    if not args.inspect_only:
        assert (glob_total, snapshot_total) == (650, 350), 'Unexpected fixture output; use a dedicated empty lab directory'
        print('PASS: active-file membership prevents reading retained historical data twice.')
    print('Model only: CSV + JSON manifest; not Delta, Parquet, ACID or concurrency simulation.')


if __name__ == '__main__':
    main()
