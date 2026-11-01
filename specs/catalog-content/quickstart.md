# SG-CONTENT — Quickstart

Run the served proof of the content connector:

```bash
uv run --all-extras pytest tests/test_catalog_content.py -q
```

The test `test_server_lists_every_skill` builds the server in process and lists the resources through a client. Run the contract gate on the tree:

```bash
python scripts/validate_skill_graphs.py
```
