"""Tests for the skill-graph contract gate (scripts/validate_skill_graphs.py)."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

_GATE = Path(__file__).resolve().parents[1] / "scripts" / "validate_skill_graphs.py"
_spec = importlib.util.spec_from_file_location("validate_skill_graphs", _GATE)
assert _spec is not None and _spec.loader is not None
gate = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(gate)


def _managed_graph(root: Path, name: str, file_count: int) -> Path:
    d = root / "skill_graphs" / name
    (d / "reference").mkdir(parents=True)
    for i in range(file_count):
        (d / "reference" / f"f{i}.md").write_text(f"# F{i}\n", encoding="utf-8")
    (d / "SKILL.md").write_text(
        f"---\nname: {name}\ndescription: x\nfile_count: {file_count}\n---\n# {name}\n",
        encoding="utf-8",
    )
    (d / "sources.json").write_text(
        json.dumps(
            {
                "schema": "skill-graph-sources/v1",
                "name": name,
                "sources": [{"kind": "dir", "uri": "/x"}],
            }
        ),
        encoding="utf-8",
    )
    return d


def test_parse_frontmatter_lists_and_scalars():
    fm = gate.parse_frontmatter("---\nname: a\nsource_types: [web, pdf]\n---\nbody\n")
    assert fm["name"] == "a" and fm["source_types"] == ["web", "pdf"]


def test_gate_passes_for_valid_managed_graph(tmp_path, monkeypatch):
    _managed_graph(tmp_path, "widget-docs", 2)
    monkeypatch.chdir(tmp_path)
    assert gate.main() == 0


def test_gate_fails_on_file_count_mismatch(tmp_path, monkeypatch):
    d = _managed_graph(tmp_path, "widget-docs", 2)
    md = d / "SKILL.md"
    md.write_text(md.read_text().replace("file_count: 2", "file_count: 99"), "utf-8")
    monkeypatch.chdir(tmp_path)
    assert gate.main() == 1


def test_gate_ignores_legacy_graph_without_manifest(tmp_path, monkeypatch):
    d = tmp_path / "skill_graphs" / "legacy-docs"
    (d / "reference").mkdir(parents=True)
    (d / "reference" / "a.md").write_text("# A\n", encoding="utf-8")
    (d / "SKILL.md").write_text("---\nname: legacy-docs\n---\n# legacy\n", "utf-8")
    monkeypatch.chdir(tmp_path)
    assert gate.main() == 0  # legacy graphs are reported, never hard-failed
