# How Chroma Sync Works

Sync runs the same pipeline regardless of source:

1. **Managed ingestion.** Connect a source once; every invocation runs through Chroma's queue-based pipeline with automatic retries, rate-limit awareness, and error recovery. Monitor invocations in the dashboard or through the [Sync API](/reference/sync-api).
2. **High throughput.** The pipeline is designed to maximize throughput without dropping work, whether you're syncing a handful of files or millions of documents.
3. **Parse.** Best-in-class PDF and document parsing. PDFs, Office documents, HTML, ebooks, and images are converted to clean markdown with tables, headings, lists, and layout preserved — so chunks reflect the actual structure of the document, not just the raw text stream. Images inside documents are described in text so their content remains searchable. Code files are kept as-is.
4. **Chunk.** Tree-sitter syntax-aware chunking for code; structured markdown chunking for documents; line-based fallback for plain text. The strategy is configurable per source.
5. **Embed.** Dense embeddings are generated automatically with [Qwen3-Embedding-0.6B](/integrations/embedding-models/chroma-cloud-qwen#chroma-cloud-qwen). Optional sparse embeddings are available via [Splade](/integrations/embedding-models/chroma-cloud-splade#chroma-cloud-splade) or [BM25](https://en.wikipedia.org/wiki/Okapi_BM25). No extra API keys needed.
6. **Index.** Output is written into the target Chroma collection, ready for vector, full-text, regex, sparse, and hybrid search.
