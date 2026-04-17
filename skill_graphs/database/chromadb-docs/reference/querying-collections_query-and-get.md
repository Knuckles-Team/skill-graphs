[Skip to main content](https://docs.trychroma.com/docs/querying-collections/query-and-get#content-area)
[Chroma Docs home page![light logo](https://mintcdn.com/chroma-8943dec5/wr97NKZIObCJm0cR/images/light-logo.svg?fit=max&auto=format&n=wr97NKZIObCJm0cR&q=85&s=4d021170bd60f2e52fcb7bc0d3eb0552)![dark logo](https://mintcdn.com/chroma-8943dec5/wr97NKZIObCJm0cR/images/dark-logo.svg?fit=max&auto=format&n=wr97NKZIObCJm0cR&q=85&s=a6f162fa88876846a979771be29f2a13)](https://docs.trychroma.com/)
Search...
Ctrl KAsk AI
  * [Dashboard](https://trychroma.com/login)
  * [Dashboard](https://trychroma.com/login)


Search...
Navigation
Querying Collections
Query and Get
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
  * [Query](https://docs.trychroma.com/docs/querying-collections/query-and-get#query)
  * [Get](https://docs.trychroma.com/docs/querying-collections/query-and-get#get)
  * [Results Shape](https://docs.trychroma.com/docs/querying-collections/query-and-get#results-shape)
  * [Choosing Which Data is Returned](https://docs.trychroma.com/docs/querying-collections/query-and-get#choosing-which-data-is-returned)


Querying Collections
# Query and Get
Copy page
Learn how to query and retrieve data from Chroma collections.
Copy page
**New Search API Available** Dense vector search, hybrid search, and more are available in the new powerful [Search API](https://docs.trychroma.com/cloud/search-api/overview) for Chroma Cloud databases.
The Query API enables nearest-neighbor similarity search over dense embeddings. Use the Get API when you want to retrieve records without similarity ranking.
##
[​](https://docs.trychroma.com/docs/querying-collections/query-and-get#query)
Query
You can query a collection to run a similarity search using `.query`:
Report incorrect code
Copy
Ask AI
```
collection.query(
    query_texts=["thus spake zarathustra", "the oracle speaks"]
)

```

Chroma will use the collection’s [embedding function](https://docs.trychroma.com/docs/embeddings/embedding-functions) to embed your text queries, and use the output to run a vector similarity search against your collection.Instead of providing `query_texts`, you can provide `query_embeddings` directly. You will be required to do so if your collection does not have an embedding function attached to it. The dimension of your query embedding must match the dimension of the embeddings in your collection.Python also supports `query_images` and `query_uris` as query inputs.
Report incorrect code
Copy
Ask AI
```
collection.query(
    query_embeddings=[[11.1, 12.1, 13.1], [1.1, 2.3, 3.2]]
)

```

By default, Chroma will return 10 results per input query. You can modify this number using the `n_results` argument:
Report incorrect code
Copy
Ask AI
```
collection.query(
    query_embeddings=[[11.1, 12.1, 13.1], [1.1, 2.3, 3.2]],
    n_results=100
)

```

The `ids` argument lets you constrain the search only to records with the IDs from the provided list:
Report incorrect code
Copy
Ask AI
```
collection.query(
    query_embeddings=[[11.1, 12.1, 13.1], [1.1, 2.3, 3.2]],
    n_results=100,
    ids=["id1", "id2"]
)

```

Both `query` and `get` support `where` for [metadata filtering](https://docs.trychroma.com/docs/querying-collections/metadata-filtering) and `where_document` for [full-text search and regex](https://docs.trychroma.com/docs/querying-collections/full-text-search):
Report incorrect code
Copy
Ask AI
```
collection.query(
    query_embeddings=[[11.1, 12.1, 13.1], [1.1, 2.3, 3.2]],
    n_results=100,
    where={"page": 10}, # query records with metadata field 'page' equal to 10
    where_document={"$contains": "search string"} # query records with the search string in the records' document
)

```

##
[​](https://docs.trychroma.com/docs/querying-collections/query-and-get#get)
Get
Use `.get` to retrieve records by ID and/or filters without similarity ranking:
Report incorrect code
Copy
Ask AI
```
collection.get(ids=["id1", "id2"]) # by IDs

collection.get(limit=100, offset=0) # with pagination

```

##
[​](https://docs.trychroma.com/docs/querying-collections/query-and-get#query-2)
Query
You can query a collection to run a similarity search using `.query`:
Report incorrect code
Copy
Ask AI
```
await collection.query({
  queryTexts: ["thus spake zarathustra", "the oracle speaks"],
});

```

Chroma will use the collection’s [embedding function](https://docs.trychroma.com/docs/embeddings/embedding-functions) to embed your text queries, and use the output to run a vector similarity search against your collection.Instead of providing `queryTexts`, you can provide `queryEmbeddings` directly. You will be required to do so if your collection does not have an embedding function attached to it. The dimension of your query embedding must match the dimension of the embeddings in your collection.
Report incorrect code
Copy
Ask AI
```
await collection.query({
  queryEmbeddings: [
    [11.1, 12.1, 13.1],
    [1.1, 2.3, 3.2],
  ],
});

```

By default, Chroma will return 10 results per input query. You can modify this number using the `nResults` argument:
Report incorrect code
Copy
Ask AI
```
await collection.query({
  queryEmbeddings: [
    [11.1, 12.1, 13.1],
    [1.1, 2.3, 3.2],
  ],
  nResults: 100,
});

```

The `ids` argument lets you constrain the search only to records with the IDs from the provided list:
Report incorrect code
Copy
Ask AI
```
await collection.query({
  queryEmbeddings: [
    [11.1, 12.1, 13.1],
    [1.1, 2.3, 3.2],
  ],
  nResults: 100,
  ids: ["id1", "id2"],
});

```

Both `query` and `get` support `where` for [metadata filtering](https://docs.trychroma.com/docs/querying-collections/metadata-filtering) and `whereDocument` for [full-text search and regex](https://docs.trychroma.com/docs/querying-collections/full-text-search):
Report incorrect code
Copy
Ask AI
```
await collection.query({
  queryEmbeddings: [
    [11.1, 12.1, 13.1],
    [1.1, 2.3, 3.2],
  ],
  nResults: 5,
  where: { page: 10 }, // metadata field 'page' equal to 10
  whereDocument: { $contains: "search string" }, // documents containing "search string"
});

```

##
[​](https://docs.trychroma.com/docs/querying-collections/query-and-get#get-2)
Get
Use `.get` to retrieve records by ID and/or filters without similarity ranking:
Report incorrect code
Copy
Ask AI
```
await collection.get({ ids: ["id1", "id2"] }); // By IDs

await collection.get({ limit: 100, offset: 0 }); // With pagination

```

##
[​](https://docs.trychroma.com/docs/querying-collections/query-and-get#type-inference)
Type inference
You can also pass type arguments to `.get` and `.query` for the shape of your metadata. This gives you type inference for your metadata objects:
Report incorrect code
Copy
Ask AI
```
const results = await collection.get<{page: number; title: string}>({
  ids: ["id1", "id2"],
});

const rows = results.rows();
rows.forEach((row) => {
  console.log(row.id, row.metadata?.page);
});

```

##
[​](https://docs.trychroma.com/docs/querying-collections/query-and-get#query-3)
Query
You can query a collection to run a similarity search using `.query`:
Report incorrect code
Copy
Ask AI
```
use chroma_types::IncludeList;

// pub async fn query(
//    &self,
//    query_embeddings: Vec<Vec<f32>>,
//    n_results: Option<u32>,
//    where: Option<Where>,
//    ids: Option<Vec<String>>,
//    include: Option<IncludeList>,
// ) -> Result<QueryResponse, ChromaHttpClientError>

let results = collection
    .query(
        vec![vec![11.1, 12.1, 13.1], vec![1.1, 2.3, 3.2]],
        None,
        None,
        None,
        None,
    )
    .await?;

```

Embeddings must be provided directly to the Rust client.By default, Chroma returns 10 results per input query. You can modify this number using `n_results`:
Report incorrect code
Copy
Ask AI
```
let results = collection
    .query(
        vec![vec![11.1, 12.1, 13.1], vec![1.1, 2.3, 3.2]],
        Some(100), // n_results
        None,
        None,
        None,
    )
    .await?;

```

The `ids` argument lets you constrain the search only to records with the IDs from the provided list:
Report incorrect code
Copy
Ask AI
```
let results = collection
    .query(
        vec![vec![11.1, 12.1, 13.1], vec![1.1, 2.3, 3.2]],
        Some(5),
        None,
        Some(vec!["id1".to_string(), "id2".to_string()]), // ids
        None,
    )
    .await?;

```

##
[​](https://docs.trychroma.com/docs/querying-collections/query-and-get#get-3)
Get
Use `.get` to retrieve records by ID and/or filters without similarity ranking:
Report incorrect code
Copy
Ask AI
```
let response = collection
    .get(
        Some(vec!["id1".to_string(), "id2".to_string()]),
        None,
        Some(10),
        Some(0),
        Some(IncludeList::default_get()),
    )
    .await?;

```

##
[​](https://docs.trychroma.com/docs/querying-collections/query-and-get#results-shape)
Results Shape
Chroma returns `.query` and `.get` results in **column-major** form (arrays per field). `.query` results are grouped per input query; `.get` results are a flat list of records.
Python
TypeScript
Rust
Report incorrect code
Copy
Ask AI
```
class QueryResult(TypedDict):
    ids: List[IDs]
    embeddings: Optional[List[Embeddings]]
    documents: Optional[List[List[Document]]]
    uris: Optional[List[List[URI]]]
    metadatas: Optional[List[List[Metadata]]]
    distances: Optional[List[List[float]]]
    included: Include

class GetResult(TypedDict):
    ids: List[ID]
    embeddings: Optional[Embeddings]
    documents: Optional[List[Document]]
    uris: Optional[URIs]
    metadatas: Optional[List[Metadata]]
    included: Include

```

In the results from the Get operation, corresponding elements in each array belong to the same document.
Python
TypeScript
Rust
Report incorrect code
Copy
Ask AI
```
result = collection.get(include=["documents", "metadatas"])
for id, document, metadata in zip(result["ids"], result["documents"], result["metadatas"]):
    print(id, document, metadata)

```

Query is a batch API and returns results grouped per input. A common pattern is to iterate over each query’s “batch” of results, then iterate within that batch.
Python
TypeScript
Rust
Report incorrect code
Copy
Ask AI
```
result = collection.query(query_texts=["first query", "second query"])
for ids, documents, metadatas in zip(result["ids"], result["documents"], result["metadatas"]):
    for id, document, metadata in zip(ids, documents, metadatas):
        print(id, document, metadata)

```

##
[​](https://docs.trychroma.com/docs/querying-collections/query-and-get#choosing-which-data-is-returned)
Choosing Which Data is Returned
By default, Query returns `documents`, `metadatas`, and `distances`, and Get returns `documents` and `metadatas`. Use `include` to control what comes back. `ids` are always returned.
Python
TypeScript
Rust
Report incorrect code
Copy
Ask AI
```
collection.query(
    query_texts=["my query"],
    include=["documents", "metadatas", "embeddings"],
)

collection.get(include=["documents"])

```

Was this page helpful?
YesNo
[ Configure Collections Previous ](https://docs.trychroma.com/docs/collections/configure)[ Metadata Filtering Next ](https://docs.trychroma.com/docs/querying-collections/metadata-filtering)
Ctrl+I
[Chroma Docs home page![light logo](https://mintcdn.com/chroma-8943dec5/wr97NKZIObCJm0cR/images/light-logo.svg?fit=max&auto=format&n=wr97NKZIObCJm0cR&q=85&s=4d021170bd60f2e52fcb7bc0d3eb0552)![dark logo](https://mintcdn.com/chroma-8943dec5/wr97NKZIObCJm0cR/images/dark-logo.svg?fit=max&auto=format&n=wr97NKZIObCJm0cR&q=85&s=a6f162fa88876846a979771be29f2a13)](https://docs.trychroma.com/)
[Enterprise](https://trychroma.com/enterprise)[Pricing](https://trychroma.com/pricing)[Changelog](https://trychroma.com/changelog)
Assistant
Responses are generated using AI and may contain mistakes.
