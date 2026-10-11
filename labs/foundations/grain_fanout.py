"""SQLite grain experiment. Diagnose is intentionally separate from solution."""
import argparse
import sqlite3
from pathlib import Path

WRONG_SQL = """
SELECT t.date, t.campaign, SUM(t.revenue) AS revenue, SUM(s.cost) AS cost
FROM transactions t JOIN ad_spend s USING (date, campaign)
GROUP BY t.date, t.campaign ORDER BY t.date, t.campaign
"""
FIXED_SQL = """
WITH revenue_daily AS (
  SELECT date, campaign, SUM(revenue) AS revenue
  FROM transactions GROUP BY date, campaign
)
SELECT r.date, r.campaign, r.revenue, s.cost
FROM revenue_daily r JOIN ad_spend s USING (date, campaign)
ORDER BY r.date, r.campaign
"""


def fixture():
    conn = sqlite3.connect(':memory:')
    conn.executescript('''
      CREATE TABLE transactions (date TEXT, campaign TEXT, transaction_id TEXT, revenue INTEGER);
      CREATE TABLE ad_spend (date TEXT, campaign TEXT, cost INTEGER);
      INSERT INTO transactions VALUES ('2026-10-01','A','T1',100),('2026-10-01','A','T2',200);
      INSERT INTO ad_spend VALUES ('2026-10-01','A',500);
    ''')
    return conn


def validate_keys(conn):
    for table, columns in [('transactions', 'transaction_id'), ('ad_spend', 'date,campaign')]:
        if conn.execute(f'SELECT 1 FROM {table} WHERE ' + ' OR '.join(f'{c} IS NULL' for c in columns.split(','))).fetchone():
            raise ValueError(f'Null key in {table}')
        if conn.execute(f'SELECT {columns} FROM {table} GROUP BY {columns} HAVING COUNT(*) > 1').fetchone():
            raise ValueError(f'Duplicate grain key in {table}')


def solution(conn):
    validate_keys(conn)
    missing = conn.execute('''SELECT DISTINCT t.date,t.campaign FROM transactions t
      LEFT JOIN ad_spend s USING (date,campaign) WHERE s.date IS NULL''').fetchall()
    if missing:
        raise ValueError(f'Missing spend coverage: {missing}')
    return conn.execute(FIXED_SQL).fetchall()


def verify_candidate(revenue, cost):
    if (revenue, cost) != (300, 500):
        raise ValueError(f'Metric contract failed: got {(revenue, cost)}, expected (300, 500)')


def verify_query(conn, sql):
    expected = solution(conn)
    actual = conn.execute(sql).fetchall()
    if sorted(actual) != sorted(expected):
        raise ValueError(f'Report contract failed: got {actual}, expected {expected}')
    return actual


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', choices=['diagnose', 'solution'], default='diagnose')
    parser.add_argument('--candidate-revenue', type=int)
    parser.add_argument('--candidate-cost', type=int)
    parser.add_argument('--query-file', type=Path, help='Execute and validate your own SQL report')
    args = parser.parse_args()
    with fixture() as conn:
        if args.mode == 'diagnose':
            print('Source totals:', conn.execute('SELECT SUM(revenue) FROM transactions').fetchone()[0],
                  conn.execute('SELECT SUM(cost) FROM ad_spend').fetchone()[0])
            print('Joined rows:', conn.execute('SELECT transaction_id,revenue,cost FROM transactions JOIN ad_spend USING(date,campaign)').fetchall())
            print('Report:', conn.execute(WRONG_SQL).fetchall())
            print('Investigate: what does one row represent on each side? Which metric was repeated?')
        else:
            print('Compatible-grain report:', solution(conn))
        if args.query_file:
            print('PASS submitted query:', verify_query(conn, args.query_file.read_text(encoding='utf-8')))
        if args.candidate_revenue is not None or args.candidate_cost is not None:
            verify_candidate(args.candidate_revenue, args.candidate_cost)
            print('PASS candidate metrics. Explain keys and coverage before accepting the fix.')


if __name__ == '__main__':
    main()
