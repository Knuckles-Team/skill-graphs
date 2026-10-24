##  [](https://qdrant.tech/documentation/guides/text-search/#combining-semantic-and-lexical-search-with-hybrid-search)Combining Semantic and Lexical Search with Hybrid Search
[Hybrid search](https://qdrant.tech/documentation/concepts/hybrid-queries/#hybrid-search) enables you to combine semantic and lexical search in a single query, returning results that match the semantic meaning, the exact keywords, or both. This is useful when you don’t know whether the user is looking for a specific keyword or a semantically similar document. For example, when searching for books, a user may enter “time travel” to find books related to the concept of time travel, but they may also enter a book’s ISBN to find a specific book. Hybrid queries enable you to return results for both cases in a single query.
Hybrid queries make use of Qdrant’s ability to store [multiple named vectors](https://qdrant.tech/documentation/concepts/vectors/#named-vectors) in a single point. For example, you can store a dense vector for semantic search and a sparse vector for lexical search in the same point. To do so, first create a collection with both a dense vector and a sparse vector:
httppythontypescriptrustjavacsharpgo
```
PUT /collections/books?wait=true
{
  "vectors": {
    "description-dense": {
      "size": 384,
      "distance": "Cosine"
    }
  },
  "sparse_vectors": {
    "isbn-bm25": {
      "modifier": "idf"
    }
  }
}

```

```
from qdrant_client import QdrantClient, models

client = QdrantClient(
    url="https://xyz-example.qdrant.io:6333",
    api_key="<your-api-key>",
    cloud_inference=True,
)

client.create_collection(
    collection_name="books",
    vectors_config={
        "description-dense": models.VectorParams(size=384, distance=models.Distance.COSINE)
    },
    sparse_vectors_config={
        "isbn-bm25": models.SparseVectorParams(modifier=models.Modifier.IDF)
    },
)

```

```
client.createCollection("books", {
  vectors: {
    "description-dense": { size: 384, distance: "Cosine" },
  },
  sparse_vectors: {
    "isbn-bm25": { modifier: "idf" },
  },
});

```

```
use qdrant_client::Qdrant;
use qdrant_client::qdrant::{
    CreateCollectionBuilder, Distance, Modifier, SparseVectorParamsBuilder,
    SparseVectorsConfigBuilder, VectorParamsBuilder, VectorsConfigBuilder,
};

let mut vectors = VectorsConfigBuilder::default();
vectors.add_named_vector_params(
    "description-dense",
    VectorParamsBuilder::new(384, Distance::Cosine),
);

let mut sparse = SparseVectorsConfigBuilder::default();
sparse.add_named_vector_params(
    "isbn-bm25",
    SparseVectorParamsBuilder::default().modifier(Modifier::Idf),
);

client
    .create_collection(
        CreateCollectionBuilder::new("books")
            .vectors_config(vectors)
            .sparse_vectors_config(sparse),
    )
    .await?;

```

```
import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Collections.*;

QdrantClient client =

client
    .createCollectionAsync(
        CreateCollection.newBuilder()
            .setCollectionName("books")
            .setVectorsConfig(
                VectorsConfig.newBuilder()
                    .setParamsMap(
                        VectorParamsMap.newBuilder()
                            .putMap(
                                "description-dense",
                                VectorParams.newBuilder()
                                    .setSize(384)
                                    .setDistance(Distance.Cosine)
                                    .build())
                            .build())
                    .build())
            .setSparseVectorsConfig(
                SparseVectorConfig.newBuilder()
                    .putMap(
                        "isbn-bm25",
                        SparseVectorParams.newBuilder().setModifier(Modifier.Idf).build())
                    .build())
            .build())
    .get();

```

```
using Qdrant.Client;
using Qdrant.Client.Grpc;

await client.CreateCollectionAsync(
    collectionName: "books",
    vectorsConfig: new VectorParamsMap
    {
        Map =
        {
            ["description-dense"] = new VectorParams
            {
                Size = 384,
                Distance = Distance.Cosine,
            },
        },
    },
    sparseVectorsConfig: new SparseVectorConfig
    {
        Map = { ["isbn-bm25"] = new SparseVectorParams { Modifier = Modifier.Idf } },
    }
);

```

```
client.CreateCollection(context.Background(), &qdrant.CreateCollection{
	CollectionName: "books",
	VectorsConfig: qdrant.NewVectorsConfigMap(
		map[string]*qdrant.VectorParams{
			"description-dense": {Size: 384, Distance: qdrant.Distance_Cosine},
		}),
	SparseVectorsConfig: qdrant.NewSparseVectorsConfig(
		map[string]*qdrant.SparseVectorParams{
			"isbn-bm25": {Modifier: qdrant.Modifier_Idf.Enum()},
		}),
})

```

After ingesting data with both vectors, you can use the prefetch feature to run both semantic and lexical queries in a single request. The results of both queries are then combined using a fusion method like Reciprocal Rank Fusion (RRF).
httppythontypescriptrustjavacsharpgo
```
POST /collections/books/points/query
{
  "prefetch": [
    {
      "query": {
        "text": "9780553213515",
        "model": "sentence-transformers/all-minilm-l6-v2"
      },
      "using": "description-dense",
      "score_threshold": 0.5
    },
    {
      "query": {
        "text": "9780553213515",
        "model": "Qdrant/bm25"
      },
      "using": "isbn-bm25"
    }
  ],
  "query": {
    "fusion": "rrf"
  },
  "limit": 10,
  "with_payload": true
}

```

```
from qdrant_client import QdrantClient, models

client = QdrantClient(
    url="https://xyz-example.qdrant.io:6333",
    api_key="<your-api-key>",
    cloud_inference=True,
)

client.query_points(
    collection_name="books",
    prefetch=[
        models.Prefetch(
            query=models.Document(
                    text="9780553213515",
                    model="sentence-transformers/all-minilm-l6-v2"
            ),
            using="description-dense",
            score_threshold=0.5,
        ),
        models.Prefetch(
            query=models.Document(
                text="9780553213515",
                model="Qdrant/bm25",
            ),
            using="isbn-bm25",
        ),
    ],
    query=models.FusionQuery(fusion=models.Fusion.RRF),
    limit=10,
    with_payload=True,
)

```

```
client.query("books", {
  prefetch: [
    {
      query: { text: "9780553213515", model: "sentence-transformers/all-minilm-l6-v2" },
      using: "description-dense",
      score_threshold: 0.5,
    },
    {
      query: { text: "9780553213515", model: "Qdrant/bm25" },
      using: "isbn-bm25",
    },
  ],
  query: { fusion: "rrf" },
  limit: 10,
  with_payload: true,
});

```

```
use qdrant_client::Qdrant;
use qdrant_client::qdrant::{Document, Fusion, PrefetchQueryBuilder, Query, QueryPointsBuilder};

let dense_prefetch = PrefetchQueryBuilder::default()
    .query(Query::new_nearest(Document::new(
        "9780553213515",
        "sentence-transformers/all-minilm-l6-v2",
    )))
    .using("description-dense")
    .score_threshold(0.5)
    .build();

let bm25_prefetch = PrefetchQueryBuilder::default()
    .query(Query::new_nearest(Document::new(
        "9780553213515",
        "Qdrant/bm25",
    )))
    .using("isbn-bm25")
    .build();

client
    .query(
        QueryPointsBuilder::new("books")
            .add_prefetch(dense_prefetch)
            .add_prefetch(bm25_prefetch)
            .query(Query::new_fusion(Fusion::Rrf))
            .limit(10)
            .with_payload(true)
            .build(),
    )
    .await?;

```

```
import static io.qdrant.client.QueryFactory.nearest;
import static io.qdrant.client.WithPayloadSelectorFactory.enable;

import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Points.*;

QdrantClient client =

PrefetchQuery densePrefetch =
    PrefetchQuery.newBuilder()
        .setUsing("description-dense")
        .setScoreThreshold(0.5f)
        .setQuery(
            nearest(
                Document.newBuilder()
                    .setText("9780553213515")
                    .setModel("sentence-transformers/all-minilm-l6-v2")
                    .build()))
        .build();

PrefetchQuery bm25Prefetch =
    PrefetchQuery.newBuilder()
        .setUsing("isbn-bm25")
        .setQuery(
            nearest(
                Document.newBuilder().setText("9780553213515").setModel("Qdrant/bm25").build()))
        .build();

client
    .queryAsync(
        QueryPoints.newBuilder()
            .setCollectionName("books")
            .addPrefetch(densePrefetch)
            .addPrefetch(bm25Prefetch)
            .setQuery(Query.newBuilder().setFusion(Fusion.RRF).build())
            .setLimit(10)
            .setWithPayload(enable(true))
            .build())
    .get();

```

```
using Qdrant.Client;
using Qdrant.Client.Grpc;

await client.QueryAsync(
    collectionName: "books",
    prefetch: new List<PrefetchQuery>
    {
        new()
        {
            Using = "description-dense",
            Query = new Document
            {
                Text = "9780553213515",
                Model = "sentence-transformers/all-minilm-l6-v2",
            },
            ScoreThreshold = 0.5f,
        },
        new()
        {
            Using = "isbn-bm25",
            Query = new Document { Text = "9780553213515", Model = "Qdrant/bm25" },
        },
    },
    query: Fusion.Rrf,
    payloadSelector: true,
    limit: 10
);

```

```
client.Query(context.Background(), &qdrant.QueryPoints{
	CollectionName: "books",
	Prefetch: []*qdrant.PrefetchQuery{
		{
			Using: qdrant.PtrOf("description-dense"),
			Query: qdrant.NewQueryDocument(&qdrant.Document{
				Text:  "9780553213515",
				Model: "sentence-transformers/all-minilm-l6-v2",
			}),
		},
		{
			Using: qdrant.PtrOf("isbn-bm25"),
			Query: qdrant.NewQueryDocument(&qdrant.Document{
				Text:  "9780553213515",
				Model: "qdrant/bm25",
			}),
		},
	},
	Query:       qdrant.NewQueryFusion(qdrant.Fusion_RRF),
	WithPayload: qdrant.NewWithPayload(true),
	Limit:       qdrant.PtrOf(uint64(10)),
})

```

This query searches for an ISBN, for which only the lexical search returns a result. The `score_threshold` for the semantic query prevents low-scoring results to be returned (0.5 is just an example threshold; you need to tune what a good threshold is for your data and model). So in this case, only the lexical result is returned to the user. If a user had searched for “time travel”, only the semantic search would return results, and those would be returned to the user. If a user would search for a term that matched both the semantic and lexical vectors, the results from both searches would be combined to provide a more comprehensive set of results.
You are not limited to prefetching just two queries. Examples include, but are not limited to:
  * Fuse multiple lexical queries across the `title`, `author`, and `isbn` fields alongside a semantic query to achieve a comprehensive search across all data.
  * Prefetch using sparse or dense vectors and/or filters, and [rescore with dense vectors](https://qdrant.tech/documentation/concepts/hybrid-queries/#multi-stage-queries).
  * [Prefetch with dense and sparse vectors, and rerank using late interaction embeddings](https://qdrant.tech/documentation/advanced-tutorials/reranking-hybrid-search/?q=late+interaction).
