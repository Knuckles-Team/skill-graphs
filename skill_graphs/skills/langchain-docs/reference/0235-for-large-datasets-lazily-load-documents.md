# For large datasets, lazily load documents
for document in loader.lazy_load():
    print(document)
```

## By category

### Productivity tools

The below document loaders allow you to load data from commonly used productivity tools.

| Document Loader                                                  | API reference                                                            |
| ---------------------------------------------------------------- | ------------------------------------------------------------------------ |
| [AgentMail](/oss/python/integrations/document_loaders/agentmail) | [`AgentMailLoader`](https://github.com/agentmail-to/langchain-agentmail) |

### Webpages

The below document loaders allow you to load webpages.

| Document Loader                                                             | Description                                                                                                          | Package/API |
| --------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ----------- |
| [Unstructured](/oss/python/integrations/document_loaders/unstructured_file) | Uses Unstructured to load and parse web pages                                                                        | Package     |
| [Apify Dataset](/oss/python/integrations/document_loaders/apify_dataset)    | Load documents from Apify datasets                                                                                   | API         |
| [Docling](/oss/python/integrations/document_loaders/docling)                | Uses Docling to load and parse web pages                                                                             | Package     |
| [Hyperbrowser](/oss/python/integrations/document_loaders/hyperbrowser)      | Platform for running and scaling headless browsers, can be used to scrape/crawl any site                             | API         |
| [AgentQL](/oss/python/integrations/document_loaders/agentql)                | Web interaction and structured data extraction from any web page using an AgentQL query or a Natural Language prompt | API         |
| [Browserbase](/oss/python/integrations/document_loaders/browserbase)        | Load webpages using managed headless browsers with stealth mode                                                      | API         |

### PDFs

The below document loaders allow you to load PDF documents.

| Document Loader                                                                    | Description                                          | Package/API |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------- | ----------- |
| [Unstructured](/oss/python/integrations/document_loaders/unstructured_file)        | Uses Unstructured's open source library to load PDFs | Package     |
| [Upstage Document Parse Loader](/oss/python/integrations/document_loaders/upstage) | Load PDF files using UpstageDocumentParseLoader      | Package     |
| [Docling](/oss/python/integrations/document_loaders/docling)                       | Load PDF files using Docling                         | Package     |
| [UnDatasIO](/oss/python/integrations/document_loaders/undatasio)                   | Load PDF files using UnDatasIO                       | Package     |
| [OpenDataLoader PDF](/oss/python/integrations/document_loaders/opendataloader_pdf) | Load PDF files using OpenDataLoader PDF              | Package     |

### Cloud providers

The below document loaders allow you to load documents from your favorite cloud providers.

| Document Loader                                                                                            | Description                                         | Partner Package | API reference                                                                                                              |
| ---------------------------------------------------------------------------------------------------------- | --------------------------------------------------- | --------------- | -------------------------------------------------------------------------------------------------------------------------- |
| [Google Cloud Storage Directory](/oss/python/integrations/document_loaders/google_cloud_storage_directory) | Load documents from GCS bucket                      | ✅               | [`GCSDirectoryLoader`](https://reference.langchain.com/python/langchain-google-community/gcs_directory/GCSDirectoryLoader) |
| [Google Cloud Storage File](/oss/python/integrations/document_loaders/google_cloud_storage_file)           | Load documents from GCS file object                 | ✅               | [`GCSFileLoader`](https://reference.langchain.com/python/langchain-google-community/gcs_file/GCSFileLoader)                |
| [Google Drive](/oss/python/integrations/document_loaders/google_drive)                                     | Load documents from Google Drive (Google Docs only) | ✅               | [`GoogleDriveLoader`](https://reference.langchain.com/python/langchain-google-community/drive/GoogleDriveLoader)           |

### Common file types

The below document loaders allow you to load data from common data formats.

| Document Loader                                                                                  | Data Type                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`Unstructured`](/oss/python/integrations/document_loaders/unstructured_file)                    | Many file types (see [https://docs.unstructured.io/platform/supported-file-types](https://docs.unstructured.io/platform/supported-file-types))                               |
| [`DoclingLoader`](/oss/python/integrations/document_loaders/docling)                             | Various file types (see [https://ds4sd.github.io/docling/](https://ds4sd.github.io/docling/))                                                                                |
| [`PolarisAIDataInsightLoader`](/oss/python/integrations/document_loaders/polaris_ai_datainsight) | Various file types (see [https://datainsight.polarisoffice.com/documentation?docType=doc\_extract](https://datainsight.polarisoffice.com/documentation?docType=doc_extract)) |

## All document loaders

<Columns>
  <Card title="AgentMail" icon="link" href="/oss/python/integrations/document_loaders/agentmail" />

  <Card title="AgentQLLoader" icon="link" href="/oss/python/integrations/document_loaders/agentql" />

  <Card title="AirbyteLoader" icon="link" href="/oss/python/integrations/document_loaders/airbyte" />

  <Card title="Apify Dataset" icon="link" href="/oss/python/integrations/document_loaders/apify_dataset" />

  <Card title="AstraDB" icon="link" href="/oss/python/integrations/document_loaders/astradb" />

  <Card title="Azure Blob Storage" icon="link" href="/oss/python/integrations/document_loaders/azure_blob_storage" />

  <Card title="Box" icon="link" href="/oss/python/integrations/document_loaders/box" />

  <Card title="Browserbase" icon="link" href="/oss/python/integrations/document_loaders/browserbase" />

  <Card title="Copy Paste" icon="link" href="/oss/python/integrations/document_loaders/copypaste" />

  <Card title="Docling" icon="link" href="/oss/python/integrations/document_loaders/docling" />

  <Card title="Docugami" icon="link" href="/oss/python/integrations/document_loaders/docugami" />

  <Card title="Google AlloyDB for PostgreSQL" icon="link" href="/oss/python/integrations/document_loaders/google_alloydb" />

  <Card title="Google BigQuery" icon="link" href="/oss/python/integrations/document_loaders/google_bigquery" />

  <Card title="Google Bigtable" icon="link" href="/oss/python/integrations/document_loaders/google_bigtable" />

  <Card title="Google Cloud SQL for SQL Server" icon="link" href="/oss/python/integrations/document_loaders/google_cloud_sql_mssql" />

  <Card title="Google Cloud SQL for MySQL" icon="link" href="/oss/python/integrations/document_loaders/google_cloud_sql_mysql" />

  <Card title="Google Cloud SQL for PostgreSQL" icon="link" href="/oss/python/integrations/document_loaders/google_cloud_sql_pg" />

  <Card title="Google Cloud Storage Directory" icon="link" href="/oss/python/integrations/document_loaders/google_cloud_storage_directory" />

  <Card title="Google Cloud Storage File" icon="link" href="/oss/python/integrations/document_loaders/google_cloud_storage_file" />

  <Card title="Google Firestore in Datastore Mode" icon="link" href="/oss/python/integrations/document_loaders/google_datastore" />

  <Card title="Google Drive" icon="link" href="/oss/python/integrations/document_loaders/google_drive" />

  <Card title="Google El Carro for Oracle Workloads" icon="link" href="/oss/python/integrations/document_loaders/google_el_carro" />

  <Card title="Google Firestore (Native Mode)" icon="link" href="/oss/python/integrations/document_loaders/google_firestore" />

  <Card title="Google Memorystore for Redis" icon="link" href="/oss/python/integrations/document_loaders/google_memorystore_redis" />

  <Card title="Google Spanner" icon="link" href="/oss/python/integrations/document_loaders/google_spanner" />

  <Card title="Google Speech-to-Text" icon="link" href="/oss/python/integrations/document_loaders/google_speech_to_text" />

  <Card title="HyperbrowserLoader" icon="link" href="/oss/python/integrations/document_loaders/hyperbrowser" />

  <Card title="Kinetica" icon="link" href="/oss/python/integrations/document_loaders/kinetica" />

  <Card title="LangSmith" icon="link" href="/oss/python/integrations/document_loaders/langsmith" />

  <Card title="Near Blockchain" icon="link" href="/oss/python/integrations/document_loaders/mintbase" />

  <Card title="OpenDataLoader PDF" icon="link" href="/oss/python/integrations/document_loaders/opendataloader_pdf" />

  <Card title="Oracle Autonomous Database" icon="link" href="/oss/python/integrations/document_loaders/oracleadb_loader" />

  <Card title="Oracle AI Database" icon="link" href="/oss/python/integrations/document_loaders/oracleai" />

  <Card title="Outline Document Loader" icon="link" href="/oss/python/integrations/document_loaders/outline" />

  <Card title="PaddleOCR-VL" icon="link" href="/oss/python/integrations/document_loaders/paddleocr_vl" />

  <Card title="Polaris AI DataInsight" icon="link" href="/oss/python/integrations/document_loaders/polaris_ai_datainsight" />

  <Card title="Dell PowerScale" icon="link" href="/oss/python/integrations/document_loaders/powerscale" />

  <Card title="PyMuPDF4LLM" icon="link" href="/oss/python/integrations/document_loaders/pymupdf4llm" />

  <Card title="SingleStore" icon="link" href="/oss/python/integrations/document_loaders/singlestore" />

  <Card title="Soniox" icon="link" href="/oss/python/integrations/document_loaders/soniox" />

  <Card title="UnDatasIO" icon="link" href="/oss/python/integrations/document_loaders/undatasio" />

  <Card title="Unstructured" icon="link" href="/oss/python/integrations/document_loaders/unstructured_file" />

  <Card title="Upstage" icon="link" href="/oss/python/integrations/document_loaders/upstage" />

  <Card title="YoutubeLoaderDL" icon="link" href="/oss/python/integrations/document_loaders/yt_dlp" />
</Columns>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/document_loaders/index.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Embedding model integrations
Source: https://docs.langchain.com/oss/python/integrations/embeddings/index

Integrate with embedding models using LangChain Python.

## Overview

<Note>
  This overview covers **text-based embedding models**. LangChain does not currently support multimodal embeddings.

  See [top embedding models](#top-integrations).
</Note>

Embedding models transform raw text—such as a sentence, paragraph, or tweet—into a fixed-length vector of numbers that captures its **semantic meaning**. These vectors allow machines to compare and search text based on meaning rather than exact words.

In practice, this means that texts with similar ideas are placed close together in the vector space. For example, instead of matching only the phrase *"machine learning"*, embeddings can surface documents that discuss related concepts even when different wording is used.

### How it works

1. **Vectorization** — The model encodes each input string as a high-dimensional vector.
2. **Similarity scoring** — Vectors are compared using mathematical metrics to measure how closely related the underlying texts are.

### Similarity metrics

Several metrics are commonly used to compare embeddings:

* **Cosine similarity** — measures the angle between two vectors.
* **Euclidean distance** — measures the straight-line distance between points.
* **Dot product** — measures how much one vector projects onto another.

Here's an example of computing cosine similarity between two vectors:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import numpy as np

def cosine_similarity(vec1, vec2):
    dot = np.dot(vec1, vec2)
    return dot / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

similarity = cosine_similarity(query_embedding, document_embedding)
print("Cosine Similarity:", similarity)
```

## Interface

LangChain provides a standard interface for text embedding models (e.g., OpenAI, Cohere, Hugging Face) via the [Embeddings](https://reference.langchain.com/python/langchain-core/embeddings/embeddings/Embeddings) interface.

Two main methods are available:

* `embed_documents(texts: List[str]) → List[List[float]]`: Embeds a list of documents.
* `embed_query(text: str) → List[float]`: Embeds a single query.

<Note>
  The interface allows queries and documents to be embedded with different strategies, though most providers handle them the same way in practice.
</Note>

## Top integrations

| Model                                                                                      | Package                                                                                                                                                          |
| ------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`OpenAIEmbeddings`](/oss/python/integrations/embeddings/openai)                           | [`langchain-openai`](https://reference.langchain.com/python/langchain-openai)                                                                                    |
| [`AzureOpenAIEmbeddings`](/oss/python/integrations/embeddings/azure_openai)                | [`langchain-openai`](https://reference.langchain.com/python/langchain-openai/embeddings/azure/AzureOpenAIEmbeddings)                                             |
| [`GoogleGenerativeAIEmbeddings`](/oss/python/integrations/embeddings/google_generative_ai) | [`langchain-google-genai`](https://reference.langchain.com/python/langchain-google-genai/embeddings/GoogleGenerativeAIEmbeddings)                                |
| [`HuggingFaceEmbeddings`](/oss/python/integrations/embeddings/sentence_transformers)       | [`langchain-huggingface`](https://reference.langchain.com/python/langchain-huggingface)                                                                          |
| [`OllamaEmbeddings`](/oss/python/integrations/embeddings/ollama)                           | [`langchain-ollama`](https://reference.langchain.com/python/langchain-ollama/embeddings/OllamaEmbeddings)                                                        |
| [`TogetherEmbeddings`](/oss/python/integrations/embeddings/together)                       | [`langchain-together`](https://reference.langchain.com/python/langchain-together/embeddings/TogetherEmbeddings)                                                  |
| [`MistralAIEmbeddings`](/oss/python/integrations/embeddings/mistralai)                     | [`langchain-mistralai`](https://reference.langchain.com/python/langchain-mistralai/embeddings/MistralAIEmbeddings)                                               |
| [`CohereEmbeddings`](/oss/python/integrations/embeddings/cohere)                           | [`langchain-cohere`](https://reference.langchain.com/python/langchain-community/llms/cohere/Cohere)                                                              |
| [`NomicEmbeddings`](/oss/python/integrations/embeddings/nomic)                             | [`langchain-nomic`](https://reference.langchain.com/python/langchain-nomic/embeddings/NomicEmbeddings)                                                           |
| [`DatabricksEmbeddings`](/oss/python/integrations/embeddings/databricks)                   | [`databricks-langchain`](https://api-docs.databricks.com/python/databricks-ai-bridge/latest/databricks_langchain.html#databricks_langchain.DatabricksEmbeddings) |
| [`NVIDIAEmbeddings`](/oss/python/integrations/embeddings/nvidia_ai_endpoints)              | [`langchain-nvidia`](https://reference.langchain.com/python/langchain-nvidia-ai-endpoints/embeddings/NVIDIAEmbeddings)                                           |
| [`AIMLAPIEmbeddings`](/oss/python/integrations/embeddings/aimlapi)                         | `langchain-aimlapi`                                                                                                                                              |
| [`PerplexityEmbeddings`](/oss/python/integrations/embeddings/perplexity)                   | [`langchain-perplexity`](https://reference.langchain.com/python/langchain-perplexity/embeddings/PerplexityEmbeddings)                                            |

### Common deployment patterns

In practice, most teams converge on one of four patterns:

1. Hosted, flagship: OpenAI `text-embedding-3-large`, Cohere `embed-english-v3`, Google `gemini-embedding-001`, Voyage `voyage-3`. One API call, best-in-class quality out of the box, no local infrastructure. Per-call cost and a data-egress dependency.
2. Local, open-source: `BAAI/bge-*`, `mixedbread-ai/mxbai-embed-*`, `Qwen/Qwen3-Embedding-*`, `nomic-ai/modernbert-embed-*`, `sentence-transformers/all-*`. Download once, run anywhere. No per-call cost, data never leaves your environment. Likely slower on CPU than a hosted API at small scale; competitive or faster with a GPU.
3. Local, open-source, specialist: a fine-tuned model targeting your specific domain, language, or task. Starting from a strong open base (e.g. `BAAI/bge-m3`) and fine-tuning on even a few thousand in-domain query/document pairs often beats hosted flagships on retrieval accuracy for that domain.
4. Self-hosted at production scale: the same open models (base or fine-tuned) served via [Text Embeddings Inference (TEI)](https://github.com/huggingface/text-embeddings-inference) or Ollama. Gives you the economics of local inference with the horizontal scaling and API ergonomics of a hosted provider.

LangChain treats all four the same: you instantiate an `Embeddings` subclass and hand it to your vector store or retriever. Patterns (2) and (3) use `HuggingFaceEmbeddings`; pattern (4) uses `HuggingFaceEndpointEmbeddings` or `OllamaEmbeddings`.

### Factors to weigh

#### Quality

Start from the [MTEB leaderboard](https://huggingface.co/spaces/mteb/leaderboard). MTEB benchmarks embedding models across retrieval, clustering, classification, and reranking tasks, and is the de-facto industry reference. Filter by your language(s) and by task (retrieval is the most common for RAG).

Leaderboard numbers don't always transfer, so run a small evaluation on your own data before committing. LangSmith has tooling for this; see the [evaluation guides](/langsmith/evaluation-concepts).

#### Cost

Hosted embeddings typically price in the range of a few cents to \~\$0.15 per million tokens. For a corpus embedded once and queried thousands of times a day, cost is often dominated by the query side.

Local inference has zero per-call cost but requires CPU (slow) or GPU (capital or cloud cost). The crossover is workload-dependent: low-volume personal projects are essentially free on CPU; for mid-volume production, a single GPU serving a local model via TEI often beats hosted on unit economics.

#### Latency

Hosted embedding APIs add roughly 50-200ms of network latency per request. Local models on CPU take 10-100ms for a short query with a small model (`all-MiniLM-L6-v2`-class), and 50-500ms for larger models. On GPU, local inference is typically faster than a round-trip to a hosted API.

For batch indexing, latency per request matters less than throughput. TEI and multi-process local inference batch aggressively. Consider e.g. `encode_kwargs={"batch_size": 64}` or higher on `HuggingFaceEmbeddings` when running on GPU.

#### Dimensionality

Embedding dimension affects vector store storage and query compute. Typical sizes:

* 384 (small Sentence Transformers models, `all-MiniLM-L6-v2`)
* 768 (mid-size ST models, `all-mpnet-base-v2`, `bge-base`)
* 1024 (`bge-large`, Cohere v3, Voyage)
* 1536 (OpenAI `text-embedding-3-small`, Qwen3-Embedding-0.6B)
* 3072+ (OpenAI `text-embedding-3-large`, Qwen3-Embedding-4B/8B)

Larger vectors are usually more accurate but consume more storage and query compute. Several modern models (OpenAI `text-embedding-3-*`, `mixedbread-ai/mxbai-embed-large-v1`, Matryoshka-trained ST models, Qwen3-Embedding) support **truncation**: slice the vector to a smaller dimension with graceful quality degradation. Useful for fitting more vectors into a smaller index.

#### Context length

Most classic embedding models cap out at 512 tokens (`all-mpnet-base-v2`, classic BGE). Newer models support longer contexts:

* `nomic-ai/modernbert-embed-base`: 8192 tokens
* `Alibaba-NLP/gte-multilingual-base`: 8192 tokens
* `BAAI/bge-m3`: 8192 tokens
* OpenAI `text-embedding-3-*`: 8191 tokens

If your chunks are long (full-page technical docs, legal paragraphs), prefer long-context models. For short chunks the 512-token limit is rarely binding.

#### Multilingual support

For multilingual retrieval, pick a model trained on your languages. Strong defaults:

* Open: `BAAI/bge-m3`, `intfloat/multilingual-e5-*`, `Alibaba-NLP/gte-multilingual-*`, `Qwen/Qwen3-Embedding-*` (via `HuggingFaceEmbeddings`)
* Hosted: Cohere `embed-multilingual-v3`, OpenAI `text-embedding-3-*`

#### Query and document prompts

Several modern open models (E5, BGE, Qwen3-Embedding, GTE) are trained with different text prefixes for queries versus documents. Using the wrong prefix at query time is a common quality regression. When using `HuggingFaceEmbeddings`, pass prompts explicitly:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="intfloat/e5-large-v2",
    encode_kwargs={"prompt": "passage: "},
    query_encode_kwargs={"prompt": "query: "},
)
```

Check each model's card on Hugging Face for the recommended prompt strings.

#### Licensing

Most popular open embedding models are permissively licensed (Apache 2.0, MIT). A few recent specialist models require a commercial license for production use. Check each model's license before shipping.

### Beyond single-vector dense embeddings

A single dense vector per chunk is the default, but not the only option.

#### Sparse and hybrid retrieval

Dense embeddings don't handle exact-match queries (product codes, named entities, code identifiers) as well as keyword-based indexes. Hybrid retrieval combines a dense index with BM25 or a sparse neural index (SPLADE, `BAAI/bge-m3`'s sparse output) to cover both cases.

#### Late-interaction and multi-vector

ColBERT-style models produce a vector per token rather than per chunk, then score queries against documents via late interaction. This is typically more accurate than single-vector dense retrieval on complex queries, at the cost of higher storage and more complex indexing. Current open models in this space include `jinaai/jina-colbert-v2`, `answerdotai/answerai-colbert-small-v1`, and newer late-interaction variants such as `lightonai/LateOn`. LangChain's built-in retrievers target single-vector embeddings; late interaction typically requires a specialist index (Vespa, Qdrant's multi-vector support, or PyLate).

### Starting points

If you just want a working starting point:

* Quick prototype, hosted: `OpenAIEmbeddings(model="text-embedding-3-small")`
* Quick prototype, local, no API key: `HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2", encode_kwargs={"normalize_embeddings": True})`
* Production, hosted, quality-first: `VoyageAIEmbeddings(model="voyage-3")` or `OpenAIEmbeddings(model="text-embedding-3-large")`
* Production, open, quality-first: `HuggingFaceEmbeddings(model_name="BAAI/bge-m3", encode_kwargs={"normalize_embeddings": True})` served via TEI
* Multilingual, open: `HuggingFaceEmbeddings(model_name="intfloat/multilingual-e5-large")` with query and document prompts configured

Measure retrieval quality on your own data, then iterate.

## Caching

Embeddings can be stored or temporarily cached to avoid needing to recompute them.

Caching embeddings can be done using a `CacheBackedEmbeddings`. This wrapper stores embeddings in a key-value store, where the text is hashed and the hash is used as the key in the cache.

The main supported way to initialize a `CacheBackedEmbeddings` is `from_bytes_store`. It takes the following parameters:

* **`underlying_embedder`**: The embedder to use for embedding.
* **`document_embedding_cache`**: Any [`ByteStore`](/oss/python/integrations/stores/) for caching document embeddings.
* **`batch_size`**: (optional, defaults to `None`) The number of documents to embed between store updates.
* **`namespace`**: (optional, defaults to `""`) The namespace to use for the document cache. Helps avoid collisions (e.g., set it to the embedding model name).
* **`query_embedding_cache`**: (optional, defaults to `None`) A [`ByteStore`](/oss/python/integrations/stores/) for caching query embeddings, or `True` to reuse the same store as `document_embedding_cache`.

<Important>
  - Always set the `namespace` parameter to avoid collisions when using different embedding models.
  - `CacheBackedEmbeddings` does not cache query embeddings by default. To enable this, specify a `query_embedding_cache`.
</Important>

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import time
from langchain_classic.embeddings import CacheBackedEmbeddings  # [!code highlight]
from langchain_classic.storage import LocalFileStore # [!code highlight]
from langchain_core.vectorstores import InMemoryVectorStore

# Create your underlying embeddings model
underlying_embeddings = ... # e.g., OpenAIEmbeddings(), HuggingFaceEmbeddings(), etc.

# Store persists embeddings to the local filesystem

# This isn't for production use, but is useful for local
store = LocalFileStore("./cache/") # [!code highlight]

cached_embedder = CacheBackedEmbeddings.from_bytes_store(
    underlying_embeddings,
    store,
    namespace=underlying_embeddings.model
)

# Example: caching a query embedding
tic = time.time()
print(cached_embedder.embed_query("Hello, world!"))
print(f"First call took: {time.time() - tic:.2f} seconds")

# Subsequent calls use the cache
tic = time.time()
print(cached_embedder.embed_query("Hello, world!"))
print(f"Second call took: {time.time() - tic:.2f} seconds")
```

In production, you would typically use a more robust persistent store, such as a database or cloud storage. Please see [stores integrations](/oss/python/integrations/stores/) for options.

## All embedding models

<Columns>
  <Card title="AI/ML API" icon="link" href="/oss/python/integrations/embeddings/aimlapi" />

  <Card title="AzureOpenAI" icon="link" href="/oss/python/integrations/embeddings/azure_openai" />

  <Card title="Baseten" icon="link" href="/oss/python/integrations/embeddings/baseten" />

  <Card title="Bedrock" icon="link" href="/oss/python/integrations/embeddings/bedrock" />

  <Card title="BGE on Hugging Face" icon="link" href="/oss/python/integrations/embeddings/bge_huggingface" />

  <Card title="Cloudflare Workers AI" icon="link" href="/oss/python/integrations/embeddings/cloudflare_workersai" />

  <Card title="Cohere" icon="link" href="/oss/python/integrations/embeddings/cohere" />

  <Card title="Databricks" icon="link" href="/oss/python/integrations/embeddings/databricks" />

  <Card title="Elasticsearch" icon="link" href="/oss/python/integrations/embeddings/elasticsearch" />

  <Card title="Google Gemini" icon="link" href="/oss/python/integrations/embeddings/google_generative_ai" />

  <Card title="Google Vertex AI" icon="link" href="/oss/python/integrations/embeddings/google_vertex_ai" />

  <Card title="GreenNode" icon="link" href="/oss/python/integrations/embeddings/greennode" />

  <Card title="Hugging Face" icon="link" href="/oss/python/integrations/embeddings/huggingfacehub" />

  <Card title="IBM watsonx.ai" icon="link" href="/oss/python/integrations/embeddings/ibm_watsonx" />

  <Card title="Instruct Embeddings" icon="link" href="/oss/python/integrations/embeddings/instruct_embeddings" />

  <Card title="Isaacus" icon="link" href="/oss/python/integrations/embeddings/isaacus" />

  <Card title="Lindorm" icon="link" href="/oss/python/integrations/embeddings/lindorm" />

  <Card title="LocalAI" icon="link" href="/oss/python/integrations/embeddings/localai" />

  <Card title="MistralAI" icon="link" href="/oss/python/integrations/embeddings/mistralai" />

  <Card title="ModelScope" icon="link" href="/oss/python/integrations/embeddings/modelscope_embedding" />

  <Card title="Naver" icon="link" href="/oss/python/integrations/embeddings/naver" />

  <Card title="Nebius" icon="link" href="/oss/python/integrations/embeddings/nebius" />

  <Card title="Netmind" icon="link" href="/oss/python/integrations/embeddings/netmind" />

  <Card title="Nomic" icon="link" href="/oss/python/integrations/embeddings/nomic" />

  <Card title="NVIDIA NIMs" icon="link" href="/oss/python/integrations/embeddings/nvidia_ai_endpoints" />

  <Card title="Oracle Cloud Infrastructure" icon="link" href="/oss/python/integrations/embeddings/oci_generative_ai" />

  <Card title="Ollama" icon="link" href="/oss/python/integrations/embeddings/ollama" />

  <Card title="OpenAI" icon="link" href="/oss/python/integrations/embeddings/openai" />

  <Card title="Oracle AI Database" icon="link" href="/oss/python/integrations/embeddings/oracleai" />

  <Card title="Pinecone Embeddings" icon="link" href="/oss/python/integrations/embeddings/pinecone" />

  <Card title="PredictionGuard" icon="link" href="/oss/python/integrations/embeddings/predictionguard" />

  <Card title="Perplexity" icon="link" href="/oss/python/integrations/embeddings/perplexity" />

  <Card title="SambaNova" icon="link" href="/oss/python/integrations/embeddings/sambanova" />

  <Card title="Sentence Transformers" icon="link" href="/oss/python/integrations/embeddings/sentence_transformers" />

  <Card title="Text Embeddings Inference" icon="link" href="/oss/python/integrations/embeddings/text_embeddings_inference" />

  <Card title="Together AI" icon="link" href="/oss/python/integrations/embeddings/together" />

  <Card title="Upstage" icon="link" href="/oss/python/integrations/embeddings/upstage" />
</Columns>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/embeddings/index.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Middleware integrations
Source: https://docs.langchain.com/oss/python/integrations/middleware/index

Integrate with middleware using LangChain Python.

Browse available middleware for different providers or contribute your own to the ecosystem. Learn more about how middleware works in the [middleware overview](/oss/python/langchain/middleware/overview) and how to use middleware with Deep Agents in the [Deep Agents docs](/oss/python/deepagents/customization#middleware).

## Share your middleware

Middleware enables context engineering, harness customization, and runtime safety controls. It is a useful extension point in LangChain and we love highlighting what the community builds with it:

<CardGroup>
  <Card title="Add an official integration" icon="package" href="/oss/python/contributing/implement-langchain#middleware">
    Follow the contributing guide to build and publish a middleware package.
  </Card>

  <Card title="Share a community middleware" icon="users" href="https://github.com/langchain-ai/docs">
    Open a PR to the docs repo to add your middleware to the table below.
  </Card>
</CardGroup>

## Official integrations

| Provider                                                          | Middleware available                                                                   | Source                                                                                                    |
| ----------------------------------------------------------------- | -------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| [Anthropic](/oss/python/integrations/middleware/anthropic)        | Prompt caching, bash tool, text editor, memory, and file search                        | [`langchain-ai/langchain`](https://github.com/langchain-ai/langchain/tree/master/libs/partners/anthropic) |
| [AWS](/oss/python/integrations/middleware/aws)                    | Prompt caching                                                                         | [`langchain-ai/langchain-aws`](https://github.com/langchain-ai/langchain-aws/tree/main/libs/aws)          |
| [Microsoft Foundry](/oss/python/integrations/middleware/azure_ai) | Text moderation, image moderation, prompt shield, protected material, and groundedness | [`langchain-ai/langchain-azure`](https://github.com/langchain-ai/langchain-azure/tree/main/libs/azure-ai) |
| [OpenAI](/oss/python/integrations/middleware/openai)              | Content moderation                                                                     | [`langchain-ai/langchain`](https://github.com/langchain-ai/langchain/tree/master/libs/partners/openai)    |

## Community integrations

<Warning>
  Community middleware is user-contributed and unverified. LangChain does not review or endorse these integrations; use them at your own risk.
</Warning>

| Middleware                                                                                       | Description                                                                                                                                                                                            | Source                                                                                                                    |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------- |
| [Cisco AI Defense](https://github.com/cisco-ai-defense/ai-defense-langchain-middleware)          | Runtime security inspection                                                                                                                                                                            | [`cisco-ai-defense/ai-defense-langchain-middleware`](https://github.com/cisco-ai-defense/ai-defense-langchain-middleware) |
| [compact-middleware](https://github.com/emanueleielo/compact-middleware)                         | Claude Code's compaction engine as LangChain middleware. Multi-level context compaction for long-running agents.                                                                                       | [`emanueleielo/compact-middleware`](https://github.com/emanueleielo/compact-middleware)                                   |
| [langchain-collapse](https://github.com/johanity/langchain-collapse)                             | Preventive context management. Collapses consecutive tool-call groups before they fill the context window.                                                                                             | [`johanity/langchain-collapse`](https://github.com/johanity/langchain-collapse)                                           |
| [langchain-task-steering](https://github.com/edvinhallvaxhiu/langchain-task-steering)            | Implicit state-machine middleware for ordered task pipelines with per-task tool scoping, dynamic prompt injection, and composable completion validation.                                               | [`edvinhallvaxhiu/langchain-task-steering`](https://github.com/edvinhallvaxhiu/langchain-task-steering)                   |
| [advisor-middleware](https://github.com/emanueleielo/advisor-middleware)                         | Claude Code's advisor pattern as LangChain middleware. Pairs a fast executor model with a powerful advisor model that intervenes only on critical decisions.                                           | [`emanueleielo/advisor-middleware`](https://github.com/emanueleielo/advisor-middleware)                                   |
| [langchain-router](https://github.com/johanity/langchain-router)                                 | Phase-based model routing. Routes execution turns to a fast model, keeps the primary for planning and recovery.                                                                                        | [`johanity/langchain-router`](https://github.com/johanity/langchain-router)                                               |
| [CopilotKit](/oss/python/langchain/frontend/integrations/copilotkit)                             | CopilotKit `CopilotKitMiddleware` and FastAPI bridge for [Deep Agents](/oss/python/deepagents/overview), `create_agent` graphs, AG-UI, and the React and runtime clients.                              | [`CopilotKit/CopilotKit`](https://github.com/CopilotKit/CopilotKit)                                                       |
| [eager-tools](https://github.com/cloudthinker-ai/eager-tools)                                    | Reduces agent wall-clock latency by dispatching each tool call the moment its streaming block closes, overlapping tool execution with LLM generation.                                                  | [`cloudthinker-ai/eager-tools`](https://github.com/cloudthinker-ai/eager-tools)                                           |
| [NoPII](https://github.com/Enigma-Vault/NoPII/tree/main/integrations/langchain-nopii-middleware) | Runtime PII tokenization. Detects personal data in outbound prompts, replaces it with deterministic vault tokens before the request reaches the LLM, and restores the original values in the response. | [`Enigma-Vault/NoPII`](https://github.com/Enigma-Vault/NoPII/tree/main/integrations/langchain-nopii-middleware)           |
| [langgraph-state-machine](https://github.com/mahmoud661/langgraph-state-machine)                 | Section-based flow control for LangGraph React agents. Divides conversations into discrete phases with scoped tools, prompts, auto-transitions, branching, and optional per-section LLM override.      | [`mahmoud661/langgraph-state-machine`](https://github.com/mahmoud661/langgraph-state-machine)                             |
| [text2sql-framework](https://github.com/Text2SqlAgent/text2sql-framework)                        | Replaces RAG with recursive tool use — the agent explores, writes, tests, and self-corrects using one `execute_sql` tool.                                                                              | [`Text2SqlAgent/text2sql-framework`](https://github.com/Text2SqlAgent/text2sql-framework)                                 |

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/middleware/index.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
