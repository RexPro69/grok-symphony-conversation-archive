#!/usr/bin/env python3
"""Validate all SKILL.md files in the repo for required schema fields."""
import pathlib
import yaml
import json
import sys
from jsonschema import validate, ValidationError

# Update path if needed
SCHEMA_PATH = pathlib.Path('schemas/skill_card.schema.json')
SKILLS_ROOT = pathlib.Path('skills')

def main():
    # Load schema
    with SCHEMA_PATH.open() as sf:
        schema = json.load(sf)

    for skill_md in SKILLS_ROOT.rglob('SKILL.md'):
        with skill_md.open() as f:
            # Extract YAML frontmatter
            frontmatter = []
            started = False
            for line in f:
                if line.strip() == '---':
                    if not started:
                        started = True
                    else:
                        break
                elif started:
                    frontmatter.append(line)
            data = yaml.safe_load(''.join(frontmatter))
        # Validate against schema
        try:
            validate(instance=data, schema=schema)
            print(f"[PASS] {skill_md}")
        except ValidationError as ve:
            print(f"[FAIL] {skill_md}: {ve.message}")
            sys.exit(1)  # fail fast for CI

if __name__ == "__main__":
    main()
