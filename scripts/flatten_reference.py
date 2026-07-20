#!/usr/bin/env python3
"""Flatten every skill-graph ``reference/`` tree to portable flat filenames.

The crawlers that build ``reference/**`` trees mirror the source site's URL
structure, which produces paths that are illegal or unsafe on Windows/macOS:
trailing-dot/space names, reserved DOS device names (``CON``, ``AUX``, ...),
case-only collisions, and paths that blow a realistic Windows ``MAX_PATH``
budget once combined with a site-packages install prefix.

This migration is idempotent: for every skill-graph directory (identified by
a ``SKILL.md``) that has a ``reference/`` folder, every file currently nested
under ``reference/**`` is renamed to a flat ``reference/<hash>.md`` (original
extension preserved), where ``hash`` is the first 8 hex chars of the
sha256 of the file's path *relative to* ``reference/`` — extended to 12 then 16
chars on collision. Now-empty subdirectories under ``reference/`` are removed.

If the graph carries ``index.json`` (schema ``skill-graph-index/v1``) and/or
``sources.json`` (schema ``skill-graph-sources/v1``), their ``path`` fields are
rewritten to the new flat paths; every other field (title, group, headings,
bytes, sha256, ...) is left untouched. Content is never modified, so
``sources.json`` sha256 values remain valid — this script asserts that after
each run.

Graphs with no ``reference/`` directory (e.g. the hand-authored
``trading-systems/*`` sub-graphs) are left alone entirely.

Self-contained (no third-party imports) so it can run anywhere pre-commit runs.
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_GRAPHS = ROOT / "skill_graphs"

_HASH_LENGTHS = (8, 12, 16, 40)


def sanitize(name: str) -> str:
    """Defensive sanitizer: strip trailing dots/spaces. The hash-based flat
    name is already legal on every platform, but this guards any future
    caller that reuses ``flat_name_for`` without the hash scheme."""
    stripped = name.rstrip(". ")
    return stripped or name


def flat_name_for(rel_posix: str, suffix: str, used: set[str]) -> str:
    """Compute a unique flat ``<hash><suffix>`` name for a reference-relative path."""
    digest = hashlib.sha256(rel_posix.encode("utf-8")).hexdigest()
    for n in _HASH_LENGTHS:
        candidate = f"{digest[:n]}{suffix}"
        if candidate not in used:
            return candidate
    raise RuntimeError(f"could not derive a unique flat name for {rel_posix!r}")


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return f"sha256:{h.hexdigest()}"


def flatten_graph(graph_dir: Path) -> tuple[int, int]:
    """Flatten ``graph_dir/reference``. Returns (files_moved, collisions_extended)."""
    ref = graph_dir / "reference"
    if not ref.is_dir():
        return (0, 0)

    old_files = sorted(p for p in ref.rglob("*") if p.is_file())
    if not old_files:
        return (0, 0)

    # Files already directly under reference/ (no nested subdir) are, by
    # construction of every crawler graph in this repo, already portable
    # (verified against the portability scanner: every current violation is
    # nested at least one subdir deep). Leave them untouched — this keeps the
    # migration idempotent (a second run finds nothing left to flatten) and
    # keeps existing, human-readable flat filenames stable.
    used_names: set[str] = {
        p.name for p in old_files if len(p.relative_to(ref).parts) == 1
    }
    # old reference-relative posix path -> new reference-relative posix path
    mapping: dict[str, str] = {}
    plan: list[tuple[Path, Path]] = []
    collisions_extended = 0

    for p in old_files:
        rel = p.relative_to(ref)
        rel_posix = rel.as_posix()
        if len(rel.parts) == 1:
            # Already flat. Defensive sanitizer only — strip a trailing
            # dot/space if one somehow slipped in (the hash path above can
            # never produce one, so this only guards this branch).
            safe = sanitize(p.name)
            if safe == p.name:
                continue
            new_name = safe
            if new_name in used_names:
                new_name = flat_name_for(rel_posix, p.suffix, used_names)
                collisions_extended += 1
        else:
            digest8 = hashlib.sha256(rel_posix.encode()).hexdigest()[:8]
            new_name = flat_name_for(rel_posix, p.suffix, used_names)
            if new_name != f"{digest8}{p.suffix}":
                collisions_extended += 1
        used_names.add(new_name)
        mapping[rel_posix] = new_name
        plan.append((p, ref / new_name))

    if not plan:
        return (0, collisions_extended)

    # Snapshot each file's content hash *before* moving it, so the move can be
    # verified byte-identical afterwards regardless of whether sources.json's
    # own recorded sha256 for it happens to already be stale (pre-existing
    # drift in some graphs, unrelated to this migration — this check must not
    # depend on that value being correct).
    pre_hash = {src: sha256_of(src) for src, _dst in plan}

    # Stage moves through a temp dir so a flat target name can never collide
    # with a not-yet-moved nested file/dir still occupying that name.
    staging_digest = hashlib.sha256(str(ref).encode()).hexdigest()[:8]
    staging = ref / f"__flatten_staging__{staging_digest}"
    staging.mkdir(exist_ok=True)
    staged: list[tuple[Path, Path]] = []
    for src, dst in plan:
        staged_path = staging / dst.name
        src.replace(staged_path)
        staged.append((staged_path, dst))
    for staged_path, dst in staged:
        staged_path.replace(dst)
    staging.rmdir()

    # Remove now-empty subdirectories under reference/.
    for d in sorted(
        (p for p in ref.rglob("*") if p.is_dir()),
        key=lambda p: len(p.parts),
        reverse=True,
    ):
        try:
            d.rmdir()
        except OSError:
            pass  # not empty (still contains files that were already flat)

    # Verify content integrity: every moved file must still exist at its new
    # path with byte-identical content to what it had before the move.
    for src, dst in plan:
        if not dst.is_file():
            raise RuntimeError(f"flatten failed: {dst} missing after move (from {src})")
        post_hash = sha256_of(dst)
        assert post_hash == pre_hash[src], (
            f"content changed by flatten move: {src} -> {dst} "
            f"({pre_hash[src]} != {post_hash})"
        )

    _rewrite_index_json(graph_dir, mapping)
    _rewrite_sources_json(graph_dir, mapping)

    return (len(plan), collisions_extended)


def _remap_path(old_path: str, mapping: dict[str, str]) -> str:
    """Map an index/sources 'reference/...' path through the flatten mapping."""
    prefix = "reference/"
    if not old_path.startswith(prefix):
        return old_path
    old_rel = old_path[len(prefix) :]
    new_rel = mapping.get(old_rel)
    if new_rel is None:
        # Path was already flat and unaffected (not in mapping because it
        # required no rename) — leave it as-is.
        return old_path
    return f"{prefix}{new_rel}"


def _rewrite_index_json(graph_dir: Path, mapping: dict[str, str]) -> None:
    idx_path = graph_dir / "index.json"
    if not idx_path.is_file():
        return
    data = json.loads(idx_path.read_text(encoding="utf-8"))
    for section in data.get("sections", []):
        if "path" in section:
            section["path"] = _remap_path(section["path"], mapping)
    idx_path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def _rewrite_sources_json(graph_dir: Path, mapping: dict[str, str]) -> None:
    """Rewrite only the ``path`` of each ``files[]`` entry; ``sha256``/``bytes``
    are left exactly as recorded — the move never touches file content (see
    the pre/post hash check in ``flatten_graph``), so those fields stay valid
    for whatever they already described."""
    src_path = graph_dir / "sources.json"
    if not src_path.is_file():
        return
    data = json.loads(src_path.read_text(encoding="utf-8"))
    for entry in data.get("files", []):
        if "path" in entry:
            entry["path"] = _remap_path(entry["path"], mapping)
    src_path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    if not SKILL_GRAPHS.is_dir():
        print("no skill_graphs/ directory found; nothing to flatten")
        return 0

    total_moved = 0
    total_collisions = 0
    graphs_touched = 0
    for skill_md in sorted(SKILL_GRAPHS.rglob("SKILL.md")):
        graph_dir = skill_md.parent
        moved, collisions = flatten_graph(graph_dir)
        if moved:
            graphs_touched += 1
            total_moved += moved
            total_collisions += collisions
            rel = graph_dir.relative_to(ROOT)
            print(
                f"  {rel}: flattened {moved} file(s)"
                + (f", {collisions} hash-extended" if collisions else "")
            )

    print(
        f"\nflatten_reference: {graphs_touched} graph(s) touched, {total_moved} file(s) moved, "
        f"{total_collisions} collision(s) extended"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
