---
name: minio-docs
skill_type: graph
description: Comprehensive reference documentation for Minio Docs.
skill_graph_version: 1.0.0
source_types: [web]
source_url: https://min.io/docs/minio/linux/index.html
built_at: 2026-06-16T02:42:13Z
builder_version: 0.47.1
file_count: 1
kg_ingested: true
index: index.json
kg_ontology: agent-utilities
categories: [Documentation, Knowledge Base, Reference]
tags: [docs, reference, minio-docs, knowledge-base]
---

# Minio — Reference Skill-Graph

> Comprehensive reference documentation for Minio Docs.

| | |
|---|---|
| **Version** | 1.0.0 |
| **Files** | 1 (3 KB) |
| **Source types** | web |
| **Knowledge Graph** | ✅ ingested (domain `skillgraph:minio-docs`) |
| **Built** | June 16, 2026 |

**Sources:** [https://min.io/docs/minio/linux/index.html](https://min.io/docs/minio/linux/index.html)

## 🧭 How to use this skill-graph

This is a **full reference corpus for Minio** — a manual at your disposal. Treat it as ground truth: quote it, don't paraphrase from memory.

- **Look something up:** scan the Table of Contents (or `index.json` for a machine-readable map), open the specific `reference/…` file, quote it + link it.
- **Cross-cutting question:** this corpus is in the Knowledge Graph — `graph_search(query="…", mode="hybrid")` retrieves the right passages across all files at once (domain `skillgraph:minio-docs`). Prefer it for synthesis.
- **Stay grounded:** never invent APIs/flags — verify against the reference and cite the file. `sources.json` tracks provenance + freshness.

## 📚 Table of Contents

- [MinIO AIStor Documentation](reference/docs_minio_linux_index.html.md)

## 🔗 Knowledge Graph & Ontology

Ingested as a `SkillGraph` ontology object over domain `skillgraph:minio-docs`: it `CONTAINS` its Documents, `RELATES_TO` the Concepts it covers, and is `DERIVED_FROM` its sources. Discover overlap/related graphs via `ontology_interface(action='implementers', name='SkillGraph')` or `graph_search`.
