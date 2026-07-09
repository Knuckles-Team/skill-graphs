"""Verify the pip-installable artifact — not just the source tree — is
Windows/macOS safe.

Builds the ``skill-graphs`` wheel and scans its extracted contents with the
vendored ``scripts/check_path_portability.py`` checker (the same rules the
``check-path-portability`` pre-commit hook enforces on the source tree), so a
regression that only shows up in what setuptools actually packages (e.g. a
broken ``package-data`` glob, or a new crawl re-introducing nested paths)
fails a real build rather than just the on-disk scan. Building a ~24k-file
wheel is slow, so this is excluded from the default pre-commit test run
(``-m "not slow"``); if the ``build`` package or build tooling is unavailable,
falls back to scanning ``skill_graphs/**`` directly on disk.
"""

from __future__ import annotations

import importlib.util
import subprocess
import sys
import zipfile
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]

_spec = importlib.util.spec_from_file_location(
    "check_path_portability", ROOT / "scripts" / "check_path_portability.py"
)
assert _spec is not None and _spec.loader is not None
checker = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(checker)

_MAX_PATH = 140
_MAX_NAME = 100


def _build_wheel(tmp_path: Path) -> Path | None:
    dist_dir = tmp_path / "dist"
    dist_dir.mkdir()
    try:
        subprocess.run(
            [sys.executable, "-m", "build", "--wheel", "--outdir", str(dist_dir), str(ROOT)],
            check=True,
            capture_output=True,
            text=True,
            timeout=600,
        )
    except (subprocess.CalledProcessError, FileNotFoundError, OSError):
        return None
    wheels = sorted(dist_dir.glob("*.whl"))
    return wheels[0] if wheels else None


@pytest.mark.slow
def test_wheel_or_source_tree_is_portable(tmp_path: Path) -> None:
    wheel = _build_wheel(tmp_path)
    if wheel is not None:
        extract_dir = tmp_path / "extracted"
        with zipfile.ZipFile(wheel) as zf:
            zf.extractall(extract_dir)
        report = checker.scan(str(extract_dir), max_path=_MAX_PATH, max_name=_MAX_NAME)
        source = f"wheel {wheel.name}"
    else:
        report = checker.scan(str(ROOT / "skill_graphs"), max_path=_MAX_PATH, max_name=_MAX_NAME)
        source = "source tree (build tooling unavailable)"

    total = sum(len(v) for v in report.values())
    detail = "\n".join(f"{kind}: {path}" for kind, paths in report.items() for path in paths[:10])
    assert total == 0, f"{total} portability violation(s) in {source}:\n{detail}"
