# SG-CONTENT — Skill graphs distill knowledge into servable skills

Owner: skill-graphs. Cross-repo IDs: `SCION-CONNECTOR-CONTROL-R071.1`, `SCION-QUALITY-RELEASE-R005.1`, `US-SKILL-GRAPH-BUILDER-R001`, `MEDULLA-TYPED-PACKS-R700`.

## Delivery mapping

Component: the `skill-graphs` package.

Depends-on: `SCION-CONNECTOR-CONTROL-R071.1`, `US-SKILL-GRAPH-BUILDER-R001`, `MEDULLA-TYPED-PACKS-R700`, `MEDULLA-TYPED-PACKS-R105`.

## User Scenarios & Testing

### User Story 1 - Serve distilled knowledge as skills (Priority: P1)

A person installs `skill-graphs` next to arbora. arbora serves every graph in it as a native skill resource with the declaration every connector uses. The agent reads the index first and opens only the reference file it needs.

**Acceptance Scenarios**:

1. **Given** the package is installed, **When** the SDK builds the server, **Then** it lists one `skill://<name>/SKILL.md` resource for every graph folder.
2. **Given** a graph sits outside `skills/`, **When** the layout test runs, **Then** it names the stray folder and fails.

### User Story 2 - Trust the provenance of a graph (Priority: P1)

A maintainer rebuilds a graph with the builder. The gate checks the files, the counts and the digests, so a graph is only accepted when it is whole and traceable to its sources.

**Acceptance Scenarios**:

1. **Given** a graph whose `sources.json` digest differs from a file, **When** the gate runs, **Then** it fails and names the file.
2. **Given** a graph with no `sources.json`, **When** the gate runs, **Then** it fails and names the graph.

### User Story 3 - Layer an ontology on a graph (Priority: P2)

A maintainer adds the concept layer of a graph as an ontology module. Each class extends an engine core class, so the engine answers questions across graphs and other sources.

**Acceptance Scenarios**:

1. **Given** a module with a class that has no path to a core class, **When** the gate runs, **Then** it names the orphan class and fails.
2. **Given** a layered graph, **When** the pack is built, **Then** it holds one skill entry and one ontology entry for that graph.

### Edge Cases

- A graph of about ten thousand files must pack and pass the gate without a per-file network call.
- A hidden file such as `.hidden.md` must reach the wheel.
- A graph with no concept layer carries `kg_ontology: null` and no module.

## Requirements

- **FR-001**: The package is served as a content-only connector through the SDK convention. Rows: `SG-CONTENT-R001`, `SG-CONTENT-R001.1`, `SG-CONTENT-R001.2`, `SG-CONTENT-R001.3`, `SG-CONTENT-R001.4`.
- **FR-002**: Every graph passes the contract gate and carries provenance. Rows: `SG-CONTENT-R002`, `SG-CONTENT-R002.1`, `SG-CONTENT-R002.2`, `SG-CONTENT-R002.3`, `SG-CONTENT-R002.4`, `SG-CONTENT-R002.5`, `SG-CONTENT-R002.6`, `SG-CONTENT-R002.7`.
- **FR-003**: A graph may layer an ontology that rolls up to the engine core. Rows: `SG-CONTENT-R003`, `SG-CONTENT-R003.1`, `SG-CONTENT-R003.2`, `SG-CONTENT-R003.3`, `SG-CONTENT-R003.4`.

## Success Criteria

- **SC-001**: The server lists exactly the graph folders under `skills/`. Rows: `SG-CONTENT-R001.3`.
- **SC-002**: The gate exits 0 on the whole tree with zero legacy graphs. Rows: `SG-CONTENT-R002.6`.
- **SC-003**: Every layered graph has one ontology module with zero orphan classes. Rows: `SG-CONTENT-R003.2`.

## Assumptions

- The builder and the engine import are owned elsewhere. This spec states only the format and the layout they meet.
- A graph is public documentation. Private data never enters a graph.

## Why a new spec

This extends `SG-CONTENT`, the only spec of the repository. A search of `specs/` of `universal-skills`, `scion-sdk` and `medulla` found no other owner of the graph format or layout. The builder is `US-SKILL-GRAPH-BUILDER`. The engine import is `MEDULLA-TYPED-PACKS-R700` and `R701`.

## Scope and interfaces

In scope: the package layout, the graph file format, the contract gate and the ontology module layout. Out of scope: how a graph is built, how a source is fetched and how the engine stores an import. Seams: [builder-output](contracts/builder-output.md) and [pack-import](contracts/pack-import.md).

## Traceability

| Label | Rows | Design section | Test ID | Evidence |
|---|---|---|---|---|
| FR-001 | `SG-CONTENT-R001` | Phase 1: Design | T-001 | |
| FR-002 | `SG-CONTENT-R002` | Phase 1: Design | T-006 | |
| FR-003 | `SG-CONTENT-R003` | Phase 1: Design | T-013 | |
