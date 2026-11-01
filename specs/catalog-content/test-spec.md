# SG-CONTENT — Test specification

Governing spec: [spec.md](spec.md).

| Test ID | Requirement | Level | Setup and input | Expected observation | Evidence |
|---|---|---|---|---|---|
| T-001 | FR-001 | Integration | The installed package. | See each child. | |
| T-002 | `SG-CONTENT-R001.1` | Contract | `tests/test_catalog_content.py::test_declares_one_content_only_entry_point` | One entry point, the bare package, the SDK floor and cap, no other group. | |
| T-003 | `SG-CONTENT-R001.2` | Contract | `tests/test_catalog_content.py::test_every_skill_is_flat_and_named_by_folder` | No name differs from its folder. | |
| T-004 | `SG-CONTENT-R001.3` | Integration | `tests/test_catalog_content.py::test_server_lists_every_skill` | The listed names equal the folder names. | |
| T-005 | `SG-CONTENT-R001.4` | Contract | `tests/test_catalog_content.py::test_no_skill_graph_outside_skills_folder` (planned) | The test finds no `SKILL.md` outside `skills/` and names each stray folder otherwise. | |
| T-006 | `SG-CONTENT-R002` | Integration | Every child row. | See each child. | |
| T-007 | `SG-CONTENT-R002.1` | Unit | `tests/test_validate_skill_graphs.py::test_gate_passes_for_valid_managed_graph` | The gate exits 0. | |
| T-008 | `SG-CONTENT-R002.2` | Unit | `tests/test_validate_skill_graphs.py::test_gate_fails_on_nested_reference_file` | The gate exits 1. | |
| T-009 | `SG-CONTENT-R002.3` | Unit | `tests/test_validate_skill_graphs.py::test_gate_fails_on_file_count_mismatch` | The gate exits 1. | |
| T-010 | `SG-CONTENT-R002.4` | Unit | `tests/test_validate_skill_graphs.py::test_gate_fails_on_sources_sha256_mismatch` | The gate exits 1. | |
| T-011 | `SG-CONTENT-R002.5` | Integration | `tests/test_wheel_portability.py::test_wheel_contains_indexed_resources` | Every indexed resource is in the wheel. | |
| T-012 | `SG-CONTENT-R002.6` | Unit | `tests/test_validate_skill_graphs.py::test_gate_fails_on_graph_without_manifest` (planned). A tmp tree holds a graph with `reference/` and no `sources.json`. | The gate exits 1 and names the graph. | |
| T-013 | `SG-CONTENT-R002.7` | Unit | `tests/test_validate_skill_graphs.py::test_gate_fails_on_missing_builder_fields_or_graph_type` (planned). A graph lacks `builder_version`, then `skill_type: graph`. | The gate exits 1 and names each missing field. | |
| T-014 | `SG-CONTENT-R003` | Integration | Every child row. | See each child. | |
| T-015 | `SG-CONTENT-R003.1` | Unit | `tests/test_skill_graph_ontology.py::test_module_is_named_by_graph_and_parses` (planned). | Each module parses, is named by its graph and declares the ontology IRI. | |
| T-016 | `SG-CONTENT-R003.2` | Unit | `tests/test_skill_graph_ontology.py::test_orphan_class_and_core_import_fail_the_gate` (planned). | The gate names the orphan class and the core import. | |
| T-017 | `SG-CONTENT-R003.3` | Unit | `tests/test_skill_graph_ontology.py::test_manifest_layer_matches_module` (planned). | `kg_ontology` and `concepts` match the module. | |
| T-018 | `SG-CONTENT-R003.4` | Integration | `tests/test_skill_graph_ontology.py::test_pack_holds_one_skill_and_one_ontology_per_layered_graph` (planned). | One skill entry and one ontology entry per layered graph. | |

## Negative and boundary cases

A nested reference file, a digest mismatch, a count mismatch, a stray graph, an orphan class and a core import each fail with the name of the offender.

## Quality and release proof

Focused: `uv run --all-extras pytest tests -q -m "not slow"`. Package: `uv run --all-extras pytest tests/test_wheel_portability.py -q`. Gates: `pre-commit run --all-files`.
