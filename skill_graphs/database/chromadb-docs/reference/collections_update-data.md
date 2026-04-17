[Skip to main content](https://docs.trychroma.com/docs/collections/update-data#content-area)
[Chroma Docs home page![light logo](https://mintcdn.com/chroma-8943dec5/wr97NKZIObCJm0cR/images/light-logo.svg?fit=max&auto=format&n=wr97NKZIObCJm0cR&q=85&s=4d021170bd60f2e52fcb7bc0d3eb0552)![dark logo](https://mintcdn.com/chroma-8943dec5/wr97NKZIObCJm0cR/images/dark-logo.svg?fit=max&auto=format&n=wr97NKZIObCJm0cR&q=85&s=a6f162fa88876846a979771be29f2a13)](https://docs.trychroma.com/)
Search...
Ctrl KAsk AI
  * [Dashboard](https://trychroma.com/login)
  * [Dashboard](https://trychroma.com/login)


Search...
Navigation
Collections
Update Data
[](https://docs.trychroma.com/docs/overview/introduction)[](https://docs.trychroma.com/cloud/getting-started)[](https://docs.trychroma.com/guides/build/building-with-ai)[](https://docs.trychroma.com/integrations/chroma-integrations)[](https://docs.trychroma.com/reference/overview)
##### Overview
  * [Introduction](https://docs.trychroma.com/docs/overview/introduction)
  * [Getting Started](https://docs.trychroma.com/docs/overview/getting-started)
  * [Architecture](https://docs.trychroma.com/docs/overview/architecture)
  * [Open Source](https://docs.trychroma.com/docs/overview/oss)
  * [Migration](https://docs.trychroma.com/docs/overview/migration)
  * [Troubleshooting](https://docs.trychroma.com/docs/overview/troubleshooting)


##### Run Chroma
  * [Chroma Clients](https://docs.trychroma.com/docs/run-chroma/clients)
  * [Client-Server Mode](https://docs.trychroma.com/docs/run-chroma/client-server)


##### Collections
  * [Manage Collections](https://docs.trychroma.com/docs/collections/manage-collections)
  * [Add Data](https://docs.trychroma.com/docs/collections/add-data)
  * [Update Data](https://docs.trychroma.com/docs/collections/update-data)
  * [Delete Data](https://docs.trychroma.com/docs/collections/delete-data)
  * [Configure Collections](https://docs.trychroma.com/docs/collections/configure)


##### Querying Collections
  * [Query and Get](https://docs.trychroma.com/docs/querying-collections/query-and-get)
  * [Metadata Filtering](https://docs.trychroma.com/docs/querying-collections/metadata-filtering)
  * [Full Text Search](https://docs.trychroma.com/docs/querying-collections/full-text-search)


##### Embeddings
  * [Embedding Functions](https://docs.trychroma.com/docs/embeddings/embedding-functions)
  * [Multimodal Embeddings](https://docs.trychroma.com/docs/embeddings/multimodal)


##### CLI
  * [Installing the CLI](https://docs.trychroma.com/docs/cli/install)
  * [Browse Collections](https://docs.trychroma.com/docs/cli/browse)
  * [Copy Collections](https://docs.trychroma.com/docs/cli/copy)
  * [DB Management](https://docs.trychroma.com/docs/cli/db)
  * [Sample Apps](https://docs.trychroma.com/docs/cli/sample-apps)
  * [Login](https://docs.trychroma.com/docs/cli/login)
  * [Profile Management](https://docs.trychroma.com/docs/cli/profile)
  * [Run a Chroma Server](https://docs.trychroma.com/docs/cli/run)
  * [Update](https://docs.trychroma.com/docs/cli/update)
  * [Vacuum](https://docs.trychroma.com/docs/cli/vacuum)


Collections
# Update Data
Copy page
Learn how to update and upsert data in Chroma collections.
Copy page
Any property of records in a collection can be updated with `.update`:
Python
TypeScript
Rust
Report incorrect code
Copy
Ask AI
```
collection.update(
    ids=["id1", "id2", "id3", ...],
    embeddings=[[1.1, 2.3, 3.2], [4.5, 6.9, 4.4], [1.1, 2.3, 3.2], ...],
    metadatas=[{"chapter": 3, "verse": 16}, {"chapter": 3, "verse": 5}, {"chapter": 29, "verse": 11}, ...],
    documents=["doc1", "doc2", "doc3", ...],
)

```

If an `id` is not found in the collection, an error will be logged and the update will be ignored. If `documents` are supplied without corresponding `embeddings`, the embeddings will be recomputed with the collection’s embedding function. Metadata values can include arrays — see [Adding Data](https://docs.trychroma.com/docs/collections/add-data#metadata) for supported metadata types. If the supplied `embeddings` are not the same dimension as the collection, an exception will be raised. Chroma also supports an `upsert` operation, which updates existing items, or adds them if they don’t yet exist.
Python
TypeScript
Rust
Report incorrect code
Copy
Ask AI
```
collection.upsert(
    ids=["id1", "id2", "id3", ...],
    embeddings=[[1.1, 2.3, 3.2], [4.5, 6.9, 4.4], [1.1, 2.3, 3.2], ...],
    metadatas=[{"chapter": 3, "verse": 16}, {"chapter": 3, "verse": 5}, {"chapter": 29, "verse": 11}, ...],
    documents=["doc1", "doc2", "doc3", ...],
)

```

If an `id` is not present in the collection, the corresponding items will be created as per `add`. Items with existing `id`s will be updated as per `update`.
Was this page helpful?
YesNo
[ Adding Data to Chroma Collections Previous ](https://docs.trychroma.com/docs/collections/add-data)[ Delete Data Next ](https://docs.trychroma.com/docs/collections/delete-data)
Ctrl+I
[Chroma Docs home page![light logo](https://mintcdn.com/chroma-8943dec5/wr97NKZIObCJm0cR/images/light-logo.svg?fit=max&auto=format&n=wr97NKZIObCJm0cR&q=85&s=4d021170bd60f2e52fcb7bc0d3eb0552)![dark logo](https://mintcdn.com/chroma-8943dec5/wr97NKZIObCJm0cR/images/dark-logo.svg?fit=max&auto=format&n=wr97NKZIObCJm0cR&q=85&s=a6f162fa88876846a979771be29f2a13)](https://docs.trychroma.com/)
[Enterprise](https://trychroma.com/enterprise)[Pricing](https://trychroma.com/pricing)[Changelog](https://trychroma.com/changelog)
Assistant
Responses are generated using AI and may contain mistakes.
