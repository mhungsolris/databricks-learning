"""Verify built local links and fragments, including a GitHub project base path."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import os
import sys

ROOT = Path('docs/.vitepress/dist').resolve()
BASE = os.environ.get('DOCS_BASE', '/Databricks-learning/')


class Links(HTMLParser):
    def __init__(self):
        super().__init__(); self.ids = set(); self.refs = []
    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        if 'id' in data: self.ids.add(data['id'])
        for field in ('href', 'src'):
            if field in data: self.refs.append(data[field])


def main():
    pages = {}
    for file in ROOT.rglob('*.html'):
        parser = Links(); parser.feed(file.read_text(encoding='utf-8'))
        pages[file] = parser
    errors = []
    checked = 0
    for file, page in pages.items():
        for ref in page.refs:
            url = urlsplit(ref)
            if url.scheme or url.netloc or not ref: continue
            raw = unquote(url.path)
            if raw.startswith('/'):
                if not raw.startswith(BASE):
                    errors.append(f'{file.name}: link bypasses project base: {ref}'); continue
                target = ROOT / raw[len(BASE):]
            else:
                target = file.parent / raw if raw else file
            target = target.resolve()
            if target.is_dir(): target = target / 'index.html'
            elif not target.suffix: target = target.with_suffix('.html')
            if not target.is_file(): errors.append(f'{file.name}: missing target {ref}'); continue
            if url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
                errors.append(f'{file.name}: missing anchor {ref}')
            checked += 1
    print(f'Built link check: {len(pages)} HTML pages, {checked} references, {len(errors)} failures.')
    for error in errors: print(error)
    return bool(errors)


if __name__ == '__main__':
    sys.exit(main())
