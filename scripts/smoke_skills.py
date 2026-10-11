"""Exercise research archival and publication controls without network or cloud auth."""
from pathlib import Path
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
TSX = ROOT / 'node_modules/tsx/dist/cli.mjs'
SCRIPTS = ROOT / '.agents/skills/research-online/scripts'


def run(name, *args, expected=0):
    result = subprocess.run(['node', str(TSX), str(SCRIPTS / name), *args], cwd=ROOT,
                            text=True, capture_output=True, encoding='utf-8')
    if result.returncode != expected:
        raise RuntimeError(f'{name}: exit {result.returncode}\n{result.stdout}\n{result.stderr}')
    return result


def main():
    for name in ('init-research-session.ts', 'save-web-research.ts',
                 'consolidate-research.ts', 'finalize-research-session.ts'):
        result = run(name, '--help')
        assert 'Usage:' in result.stdout, name
        print(f'PASS {name} --help')
    session = ROOT / '.skills-test/.researches/2026-10-10T000000Z'
    source = ROOT / '.skills-test/input.json'
    source.parent.mkdir(parents=True, exist_ok=True)
    source.write_text(json.dumps([{
        'title': 'Lakeflow Jobs', 'url': 'https://docs.databricks.com/aws/en/jobs/',
        'content': 'Lakeflow Jobs coordinates workflow tasks. Fixture for archival testing.',
    }]), encoding='utf-8')
    run('save-web-research.ts', '--query', 'Lakeflow Jobs smoke test', '--source', 'search',
        '--results', str(source), '--session-dir', str(session))
    assert list((session / 'web-search').glob('*.json'))
    run('consolidate-research.ts', '--query', 'Lakeflow Jobs smoke test',
        '--session-dir', str(session), '--no-publish')
    markdown = session / 'consolidated.md'
    structured = session / 'consolidated.json'
    assert markdown.is_file() and structured.is_file()
    assert 'docs.databricks.com/aws/en/jobs' in markdown.read_text(encoding='utf-8'), 'Source URL lost during consolidation'
    json.loads(structured.read_text(encoding='utf-8'))
    print('PASS research save -> consolidate: source URL retained; markdown and JSON readable')
    blocked = run('consolidate-research.ts', '--query', 'Lakeflow Jobs smoke test',
                  '--session-dir', str(session), expected=1)
    assert 'Automatic publication is disabled' in blocked.stderr
    print('PASS default publication blocked before any git/network action')
    print('Research smoke tests: 0 failures. Fixtures remain under ignored .skills-test/.')


if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        print(f'FAIL {exc}', file=sys.stderr)
        sys.exit(1)
