# SG-CONTENT — Design and implementation plan

Governing spec: [spec.md](spec.md).

## Existing system and reuse

The SDK finds content by convention under the package named by its `agent_connector_sdk.connector` entry point and serves `skills/<name>/SKILL.md` through fastmcp's `SkillsDirectoryProvider`. This package adds no server code.

## Architecture

`skill_graphs/skills/<name>/SKILL.md` plus supporting files in the same folder. The SDK builds the server and the pytest plugin generates the conformance checks.

## Interfaces and data model

The only interface is the entry point `skill-graphs = "skill_graphs"`. Layout follows fastmcp's `SkillsDirectoryProvider`, which wins over the raw MCP spec.

## Live integration path

arbora resolves the installed distribution through the entry point and serves its skills.

## Quality and release gates

The repository pre-commit hooks, `tests/test_catalog_content.py` and the SDK plugin checks must pass.

## Risks, alternatives, and decisions

Hard cutover: the former nested category layout are gone, with no compatibility path. A skill graph's category is its `domain`/metadata, not a directory.
