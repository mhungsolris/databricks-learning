"""Check tracked publication content without logging credential values."""
from pathlib import Path
import re
import subprocess

PATTERNS = {
    'Google API key': re.compile(r'AIza[0-9A-Za-z_-]{35}'),
    'Databricks token': re.compile(r'\bdapi[a-f0-9]{32}\b'),
    'AWS access key': re.compile(r'\bAKIA[A-Z0-9]{16}\b'),
    'GitHub token': re.compile(r'\bgh[pousr]_[A-Za-z0-9]{36,}\b|github_pat_[A-Za-z0-9_]{50,}'),
    'Private key': re.compile(r'-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----'),
}


def findings(text):
    return [kind for kind, pattern in PATTERNS.items() if pattern.search(text)]


def main():
    paths = subprocess.check_output(['git', 'ls-files', '-z']).decode().split('\0')[:-1]
    issues = []
    for name in paths:
        text = Path(name).read_bytes().decode('utf-8', errors='replace')
        for kind in findings(text):
            issues.append(f'{name}: {kind} pattern')
    if issues:
        print('\n'.join(issues))
        raise SystemExit('FAIL: inspect flagged content privately before publishing')
    print(f'PASS credential pattern scan: {len(paths)} tracked files; values never logged')


if __name__ == '__main__':
    main()
