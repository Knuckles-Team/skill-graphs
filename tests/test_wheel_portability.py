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
the portability check falls back to scanning ``skill_graphs/**`` directly on
disk. Resource completeness requires a successful build, both directly and
through an sdist; it never accepts the source tree as wheel evidence.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import subprocess
import sys
import zipfile
from pathlib import Path, PurePosixPath

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


def _build_wheel(tmp_path: Path, *, from_sdist: bool) -> Path | None:
    dist_dir = tmp_path / "dist"
    dist_dir.mkdir()
    try:
        subprocess.run(
            [
                sys.executable,
                "-m",
                "build",
                *([] if from_sdist else ["--wheel"]),
                "--outdir",
                str(dist_dir),
                str(ROOT),
            ],
            check=True,
            capture_output=True,
            text=True,
            timeout=600,
        )
    except (subprocess.CalledProcessError, FileNotFoundError, OSError):
        return None
    wheels = sorted(dist_dir.glob("*.whl"))
    return wheels[0] if wheels else None


@pytest.fixture(scope="module", params=["direct", "sdist"])
def built_wheel(
    request: pytest.FixtureRequest, tmp_path_factory: pytest.TempPathFactory
) -> Path | None:
    return _build_wheel(
        tmp_path_factory.mktemp(request.param), from_sdist=request.param == "sdist"
    )


@pytest.mark.slow
def test_wheel_or_source_tree_is_portable(
    tmp_path: Path, built_wheel: Path | None
) -> None:
    wheel = built_wheel
    if wheel is not None:
        extract_dir = tmp_path / "extracted"
        with zipfile.ZipFile(wheel) as zf:
            zf.extractall(extract_dir)
        report = checker.scan(str(extract_dir), max_path=_MAX_PATH, max_name=_MAX_NAME)
        source = f"wheel {wheel.name}"
    else:
        report = checker.scan(
            str(ROOT / "skill_graphs"), max_path=_MAX_PATH, max_name=_MAX_NAME
        )
        source = "source tree (build tooling unavailable)"

    total = sum(len(v) for v in report.values())
    detail = "\n".join(
        f"{kind}: {path}" for kind, paths in report.items() for path in paths[:10]
    )
    assert total == 0, f"{total} portability violation(s) in {source}:\n{detail}"


def _assert_indexed_resources(wheel: Path, root: Path) -> None:
    manifests = [
        (path, field, schema)
        for name, field, schema in (
            ("index.json", "sections", "skill-graph-index/v1"),
            ("sources.json", "files", "skill-graph-sources/v1"),
        )
        for path in (root / "skill_graphs").rglob(name)
    ]
    assert manifests, "No source manifests found"
    with zipfile.ZipFile(wheel) as archive:
        members = set(archive.namelist())
        for manifest, field, schema in manifests:
            member = manifest.relative_to(root).as_posix()
            assert member in members, f"Missing wheel manifest: {member}"
            assert archive.read(member) == manifest.read_bytes(), member
            document = json.loads(archive.read(member))
            assert document["schema"] == schema, member
            for entry in document[field]:
                relative = PurePosixPath(entry["path"])
                assert not relative.is_absolute() and ".." not in relative.parts, entry
                resource = (PurePosixPath(member).parent / relative).as_posix()
                assert resource in members, f"Missing wheel resource: {resource}"
                content = archive.read(resource)
                assert content == (manifest.parent / entry["path"]).read_bytes(), (
                    resource
                )
                if field == "files":
                    assert len(content) == entry["bytes"], resource
                    assert (
                        "sha256:" + hashlib.sha256(content).hexdigest()
                        == entry["sha256"]
                    ), resource


@pytest.mark.slow
def test_wheel_contains_indexed_resources(built_wheel: Path | None) -> None:
    assert built_wheel is not None, (
        "A successful wheel build is required for resource validation"
    )
    _assert_indexed_resources(built_wheel, ROOT)


@pytest.mark.parametrize("name", [".hidden.md", "ordinary.md"])
@pytest.mark.parametrize("defect", [None, "missing", "changed"])
def test_resource_check_detects_missing_or_changed_payload(
    tmp_path: Path, name: str, defect: str | None
) -> None:
    graph = tmp_path / "skill_graphs" / "example-docs"
    reference = graph / "reference"
    reference.mkdir(parents=True)
    content = b"# Reference\n"
    (reference / name).write_bytes(content)
    entry = {"path": f"reference/{name}", "bytes": len(content)}
    for filename, schema, field in (
        ("index.json", "skill-graph-index/v1", "sections"),
        ("sources.json", "skill-graph-sources/v1", "files"),
    ):
        (graph / filename).write_text(
            json.dumps(
                {
                    "schema": schema,
                    field: [
                        {
                            **entry,
                            "sha256": "sha256:" + hashlib.sha256(content).hexdigest(),
                        }
                    ],
                }
            )
        )
    wheel = tmp_path / "fixture.whl"
    with zipfile.ZipFile(wheel, "w") as archive:
        for path in graph.rglob("*"):
            if not path.is_file():
                continue
            member = path.relative_to(tmp_path).as_posix()
            if path.name == name and defect == "missing":
                continue
            archive.writestr(
                member,
                b"changed"
                if path.name == name and defect == "changed"
                else path.read_bytes(),
            )
    if defect is None:
        _assert_indexed_resources(wheel, tmp_path)
    else:
        with pytest.raises(AssertionError, match=name.replace(".", r"\.")):
            _assert_indexed_resources(wheel, tmp_path)
