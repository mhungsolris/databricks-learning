"""Validate course JSON-compatible YAML against an explicitly captured CLI schema."""
import argparse
import json
from pathlib import Path
import jsonschema
import regex
from copy import deepcopy
from hashlib import sha256
from check_production_config import BASE, validate

cli = argparse.ArgumentParser()
cli.add_argument("schema", type=Path)
args = cli.parse_args()
schema = json.loads(args.schema.read_text(encoding="utf-8-sig"))
provenance = json.loads((BASE / "schema-provenance.json").read_text())
actual_hash = sha256(json.dumps(schema, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
assert actual_hash == provenance["canonicalSchemaSHA256"], "Schema differs from verified CLI 1.20.0 capture; review before updating pin"
def unicode_pattern(validator, pattern, instance, schema):
    # CLI schema uses Go Unicode categories (e.g. \p{L}); Python re lacks them.
    if validator.is_type(instance, "string") and not regex.search(pattern, instance):
        yield jsonschema.ValidationError(f"{instance!r} does not match {pattern!r}")

def unicode_pattern_properties(validator, patterns, instance, schema):
    if validator.is_type(instance, "object"):
        for pattern, subschema in patterns.items():
            for name, value in instance.items():
                if regex.search(pattern, name):
                    yield from validator.descend(value, subschema, path=name, schema_path=pattern)

base = jsonschema.validators.validator_for(schema)
base.check_schema(schema, format_checker=None)
validator = jsonschema.validators.extend(base, {"pattern": unicode_pattern, "patternProperties": unicode_pattern_properties})
bundle, _ = validate()
resources = json.loads((BASE / "resources/roas.job.yml").read_text())
combined = dict(bundle, **resources)
validator(schema).validate(combined)
bad = deepcopy(combined)
bad["resources"]["jobs"]["roas"]["max_concurrent_runs"] = []
try:
    validator(schema).validate(bad)
except jsonschema.ValidationError:
    pass
else:
    raise AssertionError("Invalid concurrency type was accepted")
print("PASS CLI-generated bundle JSON schema: course bundle + resource; auth/resolved target/deploy still pending")
