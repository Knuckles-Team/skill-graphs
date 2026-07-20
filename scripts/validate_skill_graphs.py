#!/usr/bin/env python3
"""Skill-graph contract gate (pre-commit/CI).

Validates that every skill-graph built by the unified pipeline conforms to the
standardized contract: a parseable ``SKILL.md`` whose ``name`` matches the directory,
plus a ``sources.json`` provenance manifest (schema ``skill-graph-sources/v1``) whose
declared ``file_count`` matches the actual ``reference/`` tree.

A skill-graph is considered *managed* once it carries a ``sources.json`` (i.e. it was
produced by the unified pipeline). Legacy graphs predating the contract have no
``sources.json``; they are only **reported** (never hard-failed) so this gate does
not force a mass rebuild — rebuild them via the unified pipeline to standardize.

Also enforces the cross-platform ``reference/`` layout produced by
``scripts/flatten_reference.py``: files sit exactly one level under
``reference/`` (no nested subdirs), and every path an ``index.json``/
``sources.json`` declares actually resolves to a file on disk with matching
content (``sources.json``'s ``sha256``).

Self-contained (no third-party imports) so it runs in pre-commit's isolated env.
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

SOURCES_SCHEMA = "skill-graph-sources/v1"
SOURCE_KINDS = {
    "web", "pdf", "office", "dir", "url_reader", "rest", "database",
    "mcp_tool", "generated", "kg_query", "llms",
}
_FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def parse_frontmatter(text: str) -> dict:
    m = _FM_RE.match(text)
    if not m:
        return {}
    out: dict = {}
    for line in m.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        key, sep, raw = line.partition(":")
        if not sep:
            continue
        val = raw.strip()
        if val.startswith("[") and val.endswith("]"):
            inner = val[1:-1].strip()
            out[key.strip()] = [s.strip().strip("'\"") for s in inner.split(",") if s.strip()]
        else:
            out[key.strip()] = val.strip("'\"")
    return out


def validate_managed(d: Path, fm: dict, md_files: list[Path]) -> list[str]:
    errors: list[str] = []
    if not fm.get("name"):
        errors.append(f"{d.name}: frontmatter missing 'name'")
    elif fm["name"] != d.name:
        errors.append(f"{d.name}: frontmatter name '{fm['name']}' != directory name")
    if not fm.get("description"):
        errors.append(f"{d.name}: frontmatter missing 'description'")
    try:
        data = json.loads((d / "sources.json").read_text(encoding="utf-8"))
    except (ValueError, OSError) as exc:
        return errors + [f"{d.name}: sources.json unreadable: {type(exc).__name__}"]
    if data.get("schema") != SOURCES_SCHEMA:
        errors.append(f"{d.name}: sources.json schema '{data.get('schema')}' != {SOURCES_SCHEMA}")
    for src in data.get("sources", []):
        if src.get("kind") not in SOURCE_KINDS:
            errors.append(f"{d.name}: unknown source kind '{src.get('kind')}'")
    declared = fm.get("file_count")
    if declared not in (None, "") and str(declared) != str(len(md_files)):
        errors.append(f"{d.name}: file_count {declared} != actual {len(md_files)}")
    return errors


def validate_flat_reference(d: Path, ref: Path) -> list[str]:
    """A portable ``reference/`` sits exactly one level deep — no nested subdirs."""
    errors: list[str] = []
    for f in ref.rglob("*"):
        if f.is_file() and len(f.relative_to(ref).parts) > 1:
            errors.append(f"{d.name}: {f.relative_to(d)} is nested more than one level under reference/")
    return errors


def validate_index_paths(d: Path) -> list[str]:
    """Every index.json sections[].path must resolve to an existing file."""
    errors: list[str] = []
    try:
        data = json.loads((d / "index.json").read_text(encoding="utf-8"))
    except (ValueError, OSError) as exc:
        return [f"{d.name}: index.json unreadable: {type(exc).__name__}"]
    for section in data.get("sections", []):
        path = section.get("path")
        if not path or not (d / path).is_file():
            errors.append(f"{d.name}: index.json section path '{path}' does not exist")
    return errors


def validate_sources_paths_and_sha(d: Path) -> list[str]:
    """Every sources.json files[].path must exist and its sha256 must match."""
    errors: list[str] = []
    try:
        data = json.loads((d / "sources.json").read_text(encoding="utf-8"))
    except (ValueError, OSError) as exc:
        return [f"{d.name}: sources.json unreadable: {type(exc).__name__}"]
    for entry in data.get("files", []):
        path = entry.get("path")
        full = d / path if path else None
        if not path or full is None or not full.is_file():
            errors.append(f"{d.name}: sources.json file path '{path}' does not exist")
            continue
        expected_sha = entry.get("sha256")
        if expected_sha:
            actual_sha = "sha256:" + hashlib.sha256(full.read_bytes()).hexdigest()
            if actual_sha != expected_sha:
                errors.append(
                    f"{d.name}: sources.json sha256 mismatch for '{path}' "
                    f"(expected {expected_sha}, got {actual_sha})"
                )
    return errors


def main() -> int:
    root = Path.cwd() / "skill_graphs"
    if not root.is_dir():
        print("no skill_graphs/ directory; nothing to validate")
        return 0
    errors: list[str] = []
    managed = legacy = 0
    for skill_md in sorted(root.rglob("SKILL.md")):
        d = skill_md.parent
        fm = parse_frontmatter(skill_md.read_text(encoding="utf-8"))
        ref = d / "reference"

        if ref.is_dir():
            errors.extend(validate_flat_reference(d, ref))
        if (d / "index.json").exists():
            errors.extend(validate_index_paths(d))
        if (d / "sources.json").exists():
            errors.extend(validate_sources_paths_and_sha(d))

        if not (d / "sources.json").exists():
            if ref.is_dir():
                legacy += 1
            continue  # native/legacy graph — reported below, not failed
        managed += 1
        md_files = sorted(ref.rglob("*.md")) if ref.is_dir() else []
        errors.extend(validate_managed(d, fm, md_files))

    print(f"🧭 skill-graph contract: {managed} managed, {legacy} legacy (pre-contract)")
    if errors:
        print("\n❌ Skill-graph contract violations:")
        for i, e in enumerate(errors, 1):
            print(f"  [{i}] {type(e).__name__}")
        return 1
    print("✅ All managed skill-graphs conform to the unified contract.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
