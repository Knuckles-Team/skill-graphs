# SG-CONTENT — Implementation plan

Governing spec: [spec.md](spec.md). Rows: [requirements.md](requirements.md).

## Summary

A graph is a skill that distills a body of knowledge. The SDK serves the folder by convention, the builder writes it and the engine imports it. The package holds data and one gate script. The ontology layer reuses the SDK `ontology/` convention and the engine core-class rule `MEDULLA-TYPED-PACKS-R105`, so no new loader exists.

## Technical Context

- **Language/Version**: Python 3.14, floor 3.12
- **Primary Dependencies**: `scion-sdk[mcp]>=0.6.5,<0.7.0`, fastmcp
- **Storage**: files under `skill_graphs/`
- **Testing**: pytest, `tests/test_catalog_content.py`, `tests/test_validate_skill_graphs.py`
- **Target Platform**: any operating system; paths stay within the portability limits
- **Project Type**: content library with one gate script
- **Performance Goals**: the gate scans about 24 000 files in under 60 seconds
- **Constraints**: no code in a graph; hash-named flat `reference/`
- **Scale/Scope**: 64 graphs under `skills/`, up to 9 838 files in one graph

## Constitution Check

- R-I generated, never hand-written: pass; rows `R002.6` and `R002.7` make provenance a gate.
- R-II knowledge and no code: pass; the ontology module is Turtle.
- Organization articles: pass; one owner per concept, as the builder and the engine own their parts.

## Project Structure

```text
skill_graphs/skills/<name>/{SKILL.md,index.json,sources.json,reference/}   existing
skill_graphs/ontology/<graph>.ttl                                          new, layered graphs only
scripts/validate_skill_graphs.py                                           existing, extended
tests/test_catalog_content.py                                              existing
tests/test_validate_skill_graphs.py                                        existing
tests/test_skill_graph_ontology.py                                         new
```

## Phase 0: Research

Two unknowns were resolved; see [research.md](research.md).

## Phase 1: Design

The graph file format is in [data-model.md](data-model.md). The served proof path is in [quickstart.md](quickstart.md). The builder writes the files and the engine reads them; the two seams are in `contracts/`.

Failure modes: a stray graph outside `skills/` is never served, so `R001.4` fails the build. A graph without a manifest has no provenance, so `R002.6` fails the gate.

## Phase 2: Task approach

Bound rows first, in file order. Planned rows follow the builder rows they depend on. The gate extension and its tests are one task each.

## Complexity Tracking

None.

## Build contract

Gates: `ruff check`, `ruff format`, `mypy`, `vulture`, `codespell`, `bandit`, `security-sanitizer`, `validate-skill-graphs`, `check-path-portability`. Test command: `uv run --all-extras pytest tests -q -m "not slow"`. The slow wheel test runs in CI.

## Production caller chain

`arbora` resolves the installed distribution through the entry point `scion_sdk.connector`, then `scion_sdk.connector.build_server` lists `skills/` (`SCION-CONNECTOR-CONTROL-R071.1`). The pack builder `scion_sdk.artifacts.pack.build_connector_content_pack` captures the skills and the ontology modules. The engine imports the pack through `ConnectorPack.import` (`MEDULLA-TYPED-PACKS-R700`). The retired entry-point group `agent_connector_sdk.connector` is deleted.

## Cross-repo seams

- Builder output: `US-SKILL-GRAPH-BUILDER-R001` writes what `SG-CONTENT-R002` checks. See [contracts/builder-output.md](contracts/builder-output.md).
- Pack import: `SG-CONTENT-R003` provides the files that `MEDULLA-TYPED-PACKS-R700` imports. See [contracts/pack-import.md](contracts/pack-import.md).
