# SG-CONTENT — Research

Findings that support the decisions in [plan.md](plan.md).

## Where the ontology layer lives

The SDK convention reads `ontology/` beside `skills/` in the package. A per-graph module there reaches the pack as an ontology entry with no new code. The engine already refuses a class that has no path to a core class. A module inside the graph folder would reach the pack only as a supporting file, which the engine does not read as an ontology.

## Why the graph type key is `skill_type`

All 326 skills and graphs in the fleet declare `skill_type` in their frontmatter. The engine reads the key `type`, so it finds no declared type today. Renaming the key in 326 files costs more than reading the one key in the engine. `MEDULLA-TYPED-PACKS-R700.7` changes the engine side.
