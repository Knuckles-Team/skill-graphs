# Skill graphs constitution

This repository inherits the [organization constitution](https://github.com/Knuckles-Team/pipelines/blob/main/.specify/memory/constitution.md) version 1.4.0. Every article of that constitution applies here. This file adds only the rules and limits of this repository.

**Inherits**: organization constitution v1.4.0 | **Version**: 1.0.0 | **Ratified**: 2026-11-01 | **Last amended**: 2026-11-01

## Organization standards

- [Spec standard](https://github.com/Knuckles-Team/pipelines/blob/main/reference/spec-standard.md): one owning spec per capability, computed states, `Spec:` trailers.
- [Ecosystem boundaries](https://github.com/Knuckles-Team/pipelines/blob/main/reference/ecosystem-boundaries.md): which repository owns which requirement.
- [Wording standard](https://github.com/Knuckles-Team/pipelines/blob/main/reference/ste.md): sentences of 20 words or fewer, with `must`, `should`, or `may`.

## Repository articles

### R-I. A graph is generated, never hand-written

Every graph is produced by the `skill-graph-builder` skill. A person edits no file under a graph folder except through a rebuild or a restyle.

**Enforced by:** `scripts/validate_skill_graphs.py` and the provenance in each `sources.json`.

**Plan check:** Does every graph change come from a builder run recorded in `sources.json`?

### R-II. A graph holds knowledge and no code

A graph folder holds markdown, JSON and Turtle only. No script, binary or credential is stored in it.

**Enforced by:** Pre-commit hooks `security-sanitizer` and `check-path-portability`.

**Plan check:** Does the change add only markdown, JSON or Turtle files to a graph?

## Repository limits

| Limit | Value | Source |
|---|---|---|
| Path length | 140 | `.pre-commit-config.yaml` (`check-path-portability`) |
| File name length | 100 | `.pre-commit-config.yaml` (`check-path-portability`) |
| Path violations allowed | 0 | `.pre-commit-config.yaml` |

Amend this file in a reviewed change. State the impact in the pull request. When the organization constitution changes its version, update the **Inherits** line in the same change.
