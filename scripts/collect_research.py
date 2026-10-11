"""Archive explicitly selected public references, preserving prior sessions."""
import argparse
from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser
from pathlib import Path
import json
import re
from urllib.request import Request, urlopen

SESSION = Path('.researches/2026-10-10T010000Z')
RETRIEVED = '2026-10-10'
URLS = {
    'reference-site': 'https://vudaian24.github.io/learn-devops/07-terraform.html',
    'architecture': 'https://docs.databricks.com/aws/en/getting-started/high-level-architecture',
    'lakehouse': 'https://docs.databricks.com/aws/en/lakehouse/',
    'compute': 'https://docs.databricks.com/aws/en/compute/',
    'serverless': 'https://docs.databricks.com/aws/en/compute/serverless/',
    'jobs': 'https://docs.databricks.com/aws/en/jobs/',
    'pipelines': 'https://docs.databricks.com/aws/en/ldp/concepts/spark-declarative-pipelines',
    'bundles': 'https://docs.databricks.com/aws/en/dev-tools/bundles/',
    'unity-catalog': 'https://docs.databricks.com/aws/en/data-governance/unity-catalog/',
    'databricks-sql': 'https://docs.databricks.com/aws/en/sql/',
    'streaming': 'https://docs.databricks.com/aws/en/structured-streaming/concepts',
    'auto-loader': 'https://docs.databricks.com/aws/en/ingestion/cloud-object-storage/auto-loader/',
    'iceberg-support': 'https://docs.databricks.com/aws/en/iceberg/',
    'spark': 'https://spark.apache.org/docs/latest/cluster-overview.html',
    'delta': 'https://docs.delta.io/latest/delta-intro.html',
    'parquet': 'https://parquet.apache.org/docs/overview/',
    'iceberg': 'https://iceberg.apache.org/spec/',
    'bigquery': 'https://cloud.google.com/bigquery/docs/introduction',
    'bigquery-storage': 'https://cloud.google.com/bigquery/docs/storage_overview',
    'vitepress': 'https://vitepress.dev/guide/deploy',
    'mermaid': 'https://mermaid.js.org/config/usage.html',
    'github-pages': 'https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages',
}


class TextCapture(HTMLParser):
    def __init__(self):
        super().__init__(); self.parts = []; self.skip = 0
    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'): self.skip += 1
        if tag in ('p', 'h1', 'h2', 'h3', 'li', 'tr', 'pre'): self.parts.append('\n')
    def handle_endtag(self, tag):
        if tag in ('script', 'style'): self.skip -= 1
    def handle_data(self, text):
        if not self.skip and text.strip(): self.parts.append(text.strip() + ' ')


def fetch(entry):
    name, url = entry
    try:
        with urlopen(Request(url, headers={'User-Agent': 'DatabricksLearningResearch/1.0'}), timeout=40) as response:
            html = response.read().decode('utf-8', errors='replace')
            resolved = response.url
        # Public documentation embeds site keys; exclude them from research archives.
        html = re.sub(r'AIza[0-9A-Za-z_-]{35}', '[REDACTED_GOOGLE_API_KEY]', html)
        (SESSION / 'documentation/html' / (name + '.html')).write_text(html, encoding='utf-8')
        parser = TextCapture(); parser.feed(html)
        text = ''.join(parser.parts)
        (SESSION / 'documentation/markdown' / (name + '.md')).write_text(
            f'# {name}\n\nSource: {resolved}\nRetrieved: {RETRIEVED}\n\n{text}', encoding='utf-8')
        print(f'OK {name}: {len(html)} bytes')
        return {'title': name, 'url': resolved, 'content': text[:2000], 'retrieved': RETRIEVED, 'status': 'fetched', 'archivePolicy': 'Google API key patterns redacted from public HTML'}
    except Exception as exc:
        print(f'UNAVAILABLE {name}: {exc}')
        return {'title': name, 'url': url, 'status': 'unavailable', 'error': str(exc)}


if __name__ == '__main__':
    cli = argparse.ArgumentParser()
    cli.add_argument('--spec', type=Path, help='JSON containing session, metadata and urls')
    args = cli.parse_args()
    metadata = {
        'query': 'Current Databricks terminology, Chapter 00 mental model, and static handbook stack',
        'known': 'Skill stack installed; no website or curriculum exists.',
        'stoppingRule': 'Official source for each current term and core architecture claim.',
        'date': '2026-10-10', 'timezone': 'Asia/Saigon', 'publication': 'disabled',
    }
    if args.spec:
        spec = json.loads(args.spec.read_text(encoding='utf-8'))
        SESSION = Path(spec['session'])
        URLS = spec['urls']
        metadata = spec['metadata']
        RETRIEVED = metadata['date']
    for directory in ('documentation/html', 'documentation/markdown', 'web-search'):
        (SESSION / directory).mkdir(parents=True, exist_ok=True)
    (SESSION / 'metadata.json').write_text(json.dumps(metadata, indent=2), encoding='utf-8')
    with ThreadPoolExecutor(max_workers=5) as pool:
        results = list(pool.map(fetch, URLS.items()))
    (SESSION / 'web-search/results.json').write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding='utf-8')
