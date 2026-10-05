#!/usr/bin/env python3
"""Check that every skills/<name>/SKILL.md has valid frontmatter.

Rules (from CONTRIBUTING.md):
- starts with a `---` frontmatter block
- has non-empty `name` and `description`
- `name` matches the folder name
- file stays under ~100 lines
"""
import sys
from pathlib import Path

MAX_LINES = 100
root = Path(__file__).resolve().parent.parent
skills = sorted((root / "skills").glob("*/SKILL.md"))
errors = []

if not skills:
    errors.append("no skills/*/SKILL.md files found")

for path in skills:
    rel = path.relative_to(root)
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        errors.append(f"{rel}: must start with a '---' frontmatter block")
        continue
    try:
        end = lines.index("---", 1)
    except ValueError:
        errors.append(f"{rel}: frontmatter block is not closed with '---'")
        continue
    fields = {}
    for line in lines[1:end]:
        key, sep, value = line.partition(":")
        if sep:
            fields[key.strip()] = value.strip()
    for key in ("name", "description"):
        if not fields.get(key):
            errors.append(f"{rel}: missing or empty '{key}'")
    if fields.get("name") and fields["name"] != path.parent.name:
        errors.append(f"{rel}: name '{fields['name']}' does not match folder '{path.parent.name}'")
    if len(lines) > MAX_LINES:
        errors.append(f"{rel}: {len(lines)} lines, keep it under {MAX_LINES}")

for error in errors:
    print(f"error: {error}")
if errors:
    sys.exit(1)
print(f"{len(skills)} skills OK")
