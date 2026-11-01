# Seam: builder output

Provider: universal-skills US-SKILL-GRAPH-BUILDER-R001
Consumer: skill-graphs SG-CONTENT-R002

## Wire shape

The builder writes one graph folder: `SKILL.md`, `index.json`, `sources.json` and a flat `reference/<hash>.md`. The field lists are in [../data-model.md](../data-model.md). The folder name ends in `-docs`.

## Refusal codes

The gate prints a line per violation and exits 1. A violation names the graph and the file. There is no numeric code.

## Authoritative types

`scripts/validate_skill_graphs.py` holds the closed source kinds and the schema names.

## Test vectors

`tests/test_validate_skill_graphs.py` builds a valid graph and one graph per violation.
