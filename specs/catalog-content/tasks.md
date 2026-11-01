# SG-CONTENT — Implementation tasks

Governing spec: [spec.md](spec.md). Design: [plan.md](plan.md). Rows: [requirements.md](requirements.md).

Each task line reads `- [ ] T001 [P] [US1] <ID>-R012.4 description`. The task number and the row ID are required.

- [ ] T001 [US1] SG-CONTENT-R001 Serve the package as a content-only connector (rollup).
- [ ] T002 [US1] SG-CONTENT-R001.1 Declare one `scion_sdk.connector` entry point and the SDK floor.
- [ ] T003 [P] [US1] SG-CONTENT-R001.2 Keep every graph flat and named by its folder.
- [ ] T004 [P] [US1] SG-CONTENT-R001.3 List every graph as a skill resource.
- [ ] T005 [US1] SG-CONTENT-R001.4 Move the four stray graphs under `skills/` and add the layout test.
- [ ] T006 [US2] SG-CONTENT-R002 Validate every graph (rollup).
- [ ] T007 [P] [US2] SG-CONTENT-R002.1 Bind the managed graph test.
- [ ] T008 [P] [US2] SG-CONTENT-R002.2 Bind the flat reference test.
- [ ] T009 [P] [US2] SG-CONTENT-R002.3 Bind the file count test.
- [ ] T010 [P] [US2] SG-CONTENT-R002.4 Bind the digest test.
- [ ] T011 [P] [US2] SG-CONTENT-R002.5 Bind the wheel test.
- [ ] T012 [US2] SG-CONTENT-R002.6 Fail a graph without a manifest and rebuild the seven legacy graphs.
- [ ] T013 [US2] SG-CONTENT-R002.7 Require the builder fields and the graph type.
- [ ] T014 [US3] SG-CONTENT-R003 Layer an ontology on a graph (rollup).
- [ ] T015 [US3] SG-CONTENT-R003.1 Add the module layout and its test.
- [ ] T016 [US3] SG-CONTENT-R003.2 Add `validate_ontology_modules` to the gate.
- [ ] T017 [US3] SG-CONTENT-R003.3 Align `kg_ontology` and `concepts` with the module.
- [ ] T018 [US3] SG-CONTENT-R003.4 Prove the pack holds one skill and one ontology entry per layered graph.
