#!/usr/bin/env python3
"""Check every skill has SKILL.md with name matching its folder and a description."""
import re, sys, pathlib
root = pathlib.Path(__file__).resolve().parent.parent / "skills"
errors = []
for d in sorted(p for p in root.iterdir() if p.is_dir() and not p.name.startswith("_")):
    f = d / "SKILL.md"
    if not f.exists():
        errors.append(f"{d.name}: missing SKILL.md"); continue
    m = re.match(r"---\n(.*?)\n---", f.read_text(), re.S)
    if not m:
        errors.append(f"{d.name}: missing frontmatter"); continue
    fm = dict(l.split(":", 1) for l in m.group(1).splitlines() if ":" in l)
    if fm.get("name", "").strip() != d.name:
        errors.append(f"{d.name}: name must match folder")
    if not fm.get("description", "").strip():
        errors.append(f"{d.name}: missing description")
print("\n".join(errors) or "OK")
sys.exit(1 if errors else 0)
