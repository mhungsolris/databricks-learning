"""Portable relational pipeline and deferred execution model, not Spark."""
import argparse
import csv
from pathlib import Path
import sqlite3

SQL = '''SELECT t.campaign, c.country, SUM(t.revenue) AS revenue
FROM transactions t JOIN campaigns c USING(campaign)
WHERE t.status = 'paid'
GROUP BY t.campaign,c.country ORDER BY t.campaign,c.country'''


def fixture():
    conn = sqlite3.connect(':memory:')
    conn.executescript('''
      CREATE TABLE transactions (id TEXT, campaign TEXT, revenue INTEGER, status TEXT);
      INSERT INTO transactions VALUES ('T1','A',100,'paid'),('T2','A',200,'paid'),
        ('T3','B',50,'paid'),('T4','A',900,'cancelled');
      CREATE TABLE campaigns (campaign TEXT, country TEXT);
      INSERT INTO campaigns VALUES ('A','VN'),('B','US');
    ''')
    return conn


class DeferredQuery:
    """Actions re-run SQL; counter measures this model's executions only."""
    def __init__(self, conn):
        self.conn = conn
        self.executions = 0

    def explain(self):
        return self.conn.execute('EXPLAIN QUERY PLAN ' + SQL).fetchall()

    def collect(self):
        self.executions += 1
        return self.conn.execute(SQL).fetchall()

    def write(self, path):
        rows = self.collect()
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open('w', encoding='utf-8', newline='') as output:
            writer = csv.writer(output)
            writer.writerow(['campaign', 'country', 'revenue'])
            writer.writerows(rows)
        return rows


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, default=Path('.skills-test/lab-03/report.csv'))
    args = parser.parse_args()
    with fixture() as conn:
        query = DeferredQuery(conn)
        print('Before action, model executions:', query.executions)
        print('SQLite plan:', query.explain())
        assert query.executions == 0
        print('Preview:', query.collect())
        print('Written:', query.write(args.output))
        assert query.executions == 2
        print('After preview + write, model executions:', query.executions)
        print('NOT Spark: no job/stage/task counts or performance are inferred from this model.')
