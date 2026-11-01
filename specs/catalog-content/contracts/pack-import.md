# Seam: pack import

Provider: skill-graphs SG-CONTENT-R003
Consumer: medulla MEDULLA-TYPED-PACKS-R700

## Wire shape

The SDK captures `skill://<graph>/SKILL.md` and `skill_graphs/ontology/<graph>.ttl` into one connector pack. The engine imports the skill entry and the ontology entry. Ontology import rules are `MEDULLA-TYPED-PACKS-R105`. Graph validation and import are `MEDULLA-TYPED-PACKS-R700` and `MEDULLA-TYPED-PACKS-R701`.

## Refusal codes

`ONTOLOGY_ORPHAN` and `ONTOLOGY_PACK_IMPORTS_CORE` (`MEDULLA-TYPED-PACKS-R105`). `SKILL_GRAPH_HASH_MISMATCH`, `SKILL_GRAPH_INDEX_MISSING` and `SKILL_GRAPH_ENTRY_MISSING` (`MEDULLA-TYPED-PACKS-R700.4`).

## Authoritative types

`crates/medulla-catalog-types/src/connector_pack/index.rs` holds `PackEntryKind`.

## Test vectors

`tests/test_skill_graph_ontology.py` builds the pack that the engine tests import.
