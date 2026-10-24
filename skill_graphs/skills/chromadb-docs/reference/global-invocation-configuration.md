# Global Invocation Configuration

Each invocation may specify a target collection:

```json theme={null}
{
  "target_collection_name": "string"
}
```

* `target_collection_name` is the Chroma collection to write into. The collection is created on first use, or appended to if it already exists. Required for GitHub and Web invocations; optional for S3 (defaults to the source's `collection_name`); set automatically for file uploads via the `collection_name` form field. If a collection has already finished an ingest (`finished_ingest=true` metadata), invocation creation returns `409 Conflict`.

Source-type-specific invocation fields (S3 `object_key`, GitHub `ref_identifier`, etc.) are documented on each source type's page.
