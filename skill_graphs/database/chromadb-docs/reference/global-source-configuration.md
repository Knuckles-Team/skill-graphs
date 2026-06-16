# Global Source Configuration

Every source, regardless of type, is configured with a target database and an embedding configuration. Source-type-specific fields (bucket name, repository, starting URL, etc.) are documented on each [source type's page](#source-types).

```json theme={null}
{
  "database_name": "string",
  "embedding": {
    "dense": {
      "model": "Qwen/Qwen3-Embedding-0.6B"
    }
  }
}
```

* `database_name` is the Chroma database in which collections will be created. The database must already exist.
* `embedding.dense.model` is the dense embedding model. Currently only `Qwen/Qwen3-Embedding-0.6B` is supported. Reach out to [engineering@trychroma.com](mailto:engineering@trychroma.com) to request additional models.

You can optionally configure sparse embeddings alongside dense embeddings:

```json theme={null}
{
  "embedding": {
    "dense": { "model": "Qwen/Qwen3-Embedding-0.6B" },
    "sparse": {
      "model": "Chroma/BM25",
      "key": "sparse_embedding"
    }
  }
}
```

* `embedding.sparse.model` — `Chroma/BM25` or `prithivida/Splade_PP_en_v1`.
* `embedding.sparse.key` — metadata key under which sparse embeddings are stored.

You can also override the chunking strategy:

```json theme={null}
{
  "chunking": {
    "type": "tree_sitter",
    "max_size_bytes": 8192
  }
}
```

* `chunking.type` — `tree_sitter` (syntax-aware, with `max_size_bytes`) or `lines` (line-based, with `max_lines` and `max_size_bytes`).
