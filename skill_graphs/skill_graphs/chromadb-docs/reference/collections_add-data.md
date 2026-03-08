[Skip to main content](https://docs.trychroma.com/docs/collections/add-data#content-area)
[Chroma Docs home page![light logo](https://mintcdn.com/chroma-8943dec5/wr97NKZIObCJm0cR/images/light-logo.svg?fit=max&auto=format&n=wr97NKZIObCJm0cR&q=85&s=4d021170bd60f2e52fcb7bc0d3eb0552)![dark logo](https://mintcdn.com/chroma-8943dec5/wr97NKZIObCJm0cR/images/dark-logo.svg?fit=max&auto=format&n=wr97NKZIObCJm0cR&q=85&s=a6f162fa88876846a979771be29f2a13)](https://docs.trychroma.com/)
Search...
Ctrl KAsk AI
  * [Dashboard](https://trychroma.com/login)
  * [Dashboard](https://trychroma.com/login)


Search...
Navigation
Collections
Adding Data to Chroma Collections
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


On this page
  * [Adding Data](https://docs.trychroma.com/docs/collections/add-data#adding-data)
  * [Metadata](https://docs.trychroma.com/docs/collections/add-data#metadata)
  * [Behaviors](https://docs.trychroma.com/docs/collections/add-data#behaviors)


Collections
# Adding Data to Chroma Collections
Copy page
Learn how to add data to Chroma collections.
Copy page
##
[​](https://docs.trychroma.com/docs/collections/add-data#adding-data)
Adding Data
Use `.add` to insert new records into a collection. Each record needs a unique string `id`.
Python
TypeScript
Rust
Report incorrect code
Copy
Ask AI
```
collection.add(
    ids=["id1", "id2", "id3"],
    documents=["lorem ipsum...", "doc2", "doc3"],
    metadatas=[{"chapter": 3, "verse": 16}, {"chapter": 3, "verse": 5}, {"chapter": 29, "verse": 11}],
)

```

You must provide either `documents`, `embeddings`, or both. `metadatas` are always optional. When only providing `documents`, Chroma will generate embeddings for you using the collection’s [embedding function](https://docs.trychroma.com/docs/embeddings/embedding-functions). If you’ve already computed embeddings, pass them alongside `documents`. Chroma will store both as-is without re-embedding the documents.
Python
TypeScript
Rust
Report incorrect code
Copy
Ask AI
```
collection.add(
    ids=["id1", "id2", "id3"],
    embeddings=[[1.1, 2.3, 3.2], [4.5, 6.9, 4.4], [1.1, 2.3, 3.2]],
    documents=["doc1", "doc2", "doc3"],
    metadatas=[{"chapter": 3, "verse": 16}, {"chapter": 3, "verse": 5}, {"chapter": 29, "verse": 11}],
)

```

If your documents are stored elsewhere, you can add just embeddings and metadata. Use the `ids` to associate records with your external documents. This is a useful pattern if your documents are very large, such as high-resolution images or videos.
Python
TypeScript
Rust
Report incorrect code
Copy
Ask AI
```
collection.add(
    ids=["id1", "id2", "id3"],
    embeddings=[[1.1, 2.3, 3.2], [4.5, 6.9, 4.4], [1.1, 2.3, 3.2]],
    metadatas=[{"chapter": 3, "verse": 16}, {"chapter": 3, "verse": 5}, {"chapter": 29, "verse": 11}],
)

```

##
[​](https://docs.trychroma.com/docs/collections/add-data#metadata)
Metadata
Metadata values can be strings, integers, floats, or booleans. Additionally, you can store arrays of these types.
Python
TypeScript
Rust
Report incorrect code
Copy
Ask AI
```
collection.add(
    ids=["id1"],
    documents=["lorem ipsum..."],
    metadatas=[{
        "chapter": 3,
        "tags": ["fiction", "adventure"],
        "scores": [1, 2, 3],
    }],
)

```

All elements in an array must be the same type, and empty arrays are not allowed. You can filter on array metadata using the `$contains` and `$not_contains` operators — see [Metadata Filtering](https://docs.trychroma.com/docs/querying-collections/metadata-filtering#using-array-metadata) for details.
##
[​](https://docs.trychroma.com/docs/collections/add-data#behaviors)
Behaviors
  * If you add a record with an ID that already exists in the collection, it will be ignored without throwing an error. In order to overwrite data in your collection, you must [update](https://docs.trychroma.com/docs/collections/update-data) the data.
  * If the supplied embeddings don’t match the dimensionality of embeddings already in the collection, an exception will be raised.


Was this page helpful?
YesNo
[ Manage Collections Previous ](https://docs.trychroma.com/docs/collections/manage-collections)[ Update Data Next ](https://docs.trychroma.com/docs/collections/update-data)
Ctrl+I
[Chroma Docs home page![light logo](https://mintcdn.com/chroma-8943dec5/wr97NKZIObCJm0cR/images/light-logo.svg?fit=max&auto=format&n=wr97NKZIObCJm0cR&q=85&s=4d021170bd60f2e52fcb7bc0d3eb0552)![dark logo](https://mintcdn.com/chroma-8943dec5/wr97NKZIObCJm0cR/images/dark-logo.svg?fit=max&auto=format&n=wr97NKZIObCJm0cR&q=85&s=a6f162fa88876846a979771be29f2a13)](https://docs.trychroma.com/)
[Enterprise](https://trychroma.com/enterprise)[Pricing](https://trychroma.com/pricing)[Changelog](https://trychroma.com/changelog)
Assistant
Responses are generated using AI and may contain mistakes.
