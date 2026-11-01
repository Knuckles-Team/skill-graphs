# SG-CONTENT — Data model

## Graph folder

| File | Content |
|---|---|
| `SKILL.md` | Frontmatter: `name`, `skill_type: graph`, `description`, `skill_graph_version`, `source_types`, `source_url`, `built_at`, `builder_version`, `file_count`, `index`. Body: how to use the graph and a table of contents. |
| `index.json` | Schema `skill-graph-index/v1`: `name`, `kg_domain`, `concepts`, `groups`, and `sections[]` of `{path, title, group, bytes, headings}`. |
| `sources.json` | Schema `skill-graph-sources/v1`: `builder_version`, `built_at`, `kg_ontology`, `concepts`, `sources[]` of `{kind, uri, options, extractor, fetched_at, content_hash, doc_count}`, and `files[]` of `{path, sha256, bytes}`. |
| `reference/<hash>.md` | One markdown page, named by a short digest of its source URL. |

## Ontology module

`skill_graphs/ontology/<graph>.ttl` declares the ontology IRI `http://knuckles.team/kg/skillgraph/<graph>`. Each class is a subclass of a class of `http://knuckles.team/kg`. The file imports nothing.
