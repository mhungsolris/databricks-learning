"""Verify the repository skill installation offline, using its recorded manifest."""
from pathlib import Path
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    'databricks-core', 'databricks-jobs', 'databricks-unity-catalog',
    'databricks-dabs', 'research-online', 'technical-writing',
    'mermaid-diagrams', 'verification-before-completion',
}
OPTIONAL_UC_SIBLINGS = {
    'databricks-metric-views', 'databricks-iceberg', 'databricks-ml-training',
    'databricks-vector-search', 'databricks-pipelines', 'databricks-lakeflow-connect',
    'databricks-lakebase', 'databricks-ai-functions', 'databricks-aibi-dashboards',
    'databricks-synthetic-data-gen',
}


def main():
    manifest = json.loads((ROOT / 'skills-manifest.json').read_text(encoding='utf-8'))
    errors = []
    skill_root = ROOT / '.agents/skills'
    actual = {p.name for p in skill_root.iterdir() if p.is_dir()}
    if actual != EXPECTED:
        errors.append(f'Skill set mismatch: {actual ^ EXPECTED}')
    if set(manifest['skills']) != EXPECTED:
        errors.append('Manifest skill set mismatch')
    for name in sorted(EXPECTED):
        start = len(errors)
        directory = skill_root / name
        try:
            text = (directory / 'SKILL.md').read_text(encoding='utf-8')
            front = text.split('---', 2)[1]
            match = re.search(r'^name:\s*[\"\']?([a-z0-9-]+)', front, re.M)
            if not match or match.group(1) != name:
                errors.append(f'{name}: invalid name/frontmatter')
            if not re.search(r'^description:\s*\S', front, re.M):
                errors.append(f'{name}: missing description')
            parent = re.search(r'^parent:\s*(\S+)', front, re.M)
            if parent and parent.group(1) not in EXPECTED:
                errors.append(f'{name}: missing parent {parent.group(1)}')
            for target in re.findall(r'\]\(([^)]+)\)', text):
                if re.match(r'^[a-z]+:|^#', target):
                    continue
                target = target.split('#')[0]
                sibling = re.fullmatch(r'\.\./([^/]+)/SKILL\.md', target)
                if name == 'databricks-unity-catalog' and sibling and sibling.group(1) in OPTIONAL_UC_SIBLINGS:
                    continue
                if target and not (directory / target).exists():
                    errors.append(f'{name}: missing local reference {target}')
            record = manifest['skills'][name]
            if not re.fullmatch(r'[0-9a-f]{40}', record['commit']):
                errors.append(f'{name}: invalid pinned commit')
            files = {p.relative_to(directory).as_posix(): p for p in directory.rglob('*') if p.is_file()}
            if set(files) != set(record['files']):
                errors.append(f'{name}: file inventory changed')
            for rel, digest in record['files'].items():
                if rel in files and hashlib.sha256(files[rel].read_bytes()).hexdigest() != digest:
                    errors.append(f'{name}: checksum mismatch {rel}')
            for script in (directory / 'scripts').glob('*.ts'):
                if script.name.endswith('.test.ts'):
                    continue
                for target in re.findall(r'from\s+[\"\'](\.[^\"\']+)[\"\']', script.read_text(encoding='utf-8')):
                    base = script.parent / target
                    if not base.exists() and not Path(str(base) + '.ts').exists():
                        errors.append(f'{name}: unresolved import {script.name}: {target}')
        except (OSError, IndexError, KeyError) as exc:
            errors.append(f'{name}: {exc}')
        print(f'{"PASS" if len(errors) == start else "FAIL"} {name}')
    for filename in ('AGENTS.md', 'SKILLS.md', 'SKILLS_LOCK.md', 'SKILLS_VERIFICATION.md'):
        if not (ROOT / filename).is_file():
            errors.append(f'Missing {filename}')
    print(f'Checked {len(EXPECTED)} skills; {len(errors)} failures.')
    print('NOTE: 10 Unity Catalog sibling links are optional, intentionally outside the eight-skill stack.')
    for error in errors:
        print(error)
    return bool(errors)


if __name__ == '__main__':
    sys.exit(main())
