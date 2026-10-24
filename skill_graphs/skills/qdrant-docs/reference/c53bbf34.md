##  [](https://qdrant.tech/documentation/concepts/indexing/#vector-index)Vector Index
A vector index is a data structure built on vectors through a specific mathematical model. Through the vector index, we can efficiently query several vectors similar to the target vector.
Qdrant currently only uses HNSW as a dense vector index.
In order to improve performance, HNSW limits the maximum degree of nodes on each layer of the graph to `m`. In addition, you can use `ef_construct` (when building an index) or `ef` (when searching targets) to specify a search range.
The corresponding parameters could be configured in the configuration file:
```
storage:
  # Default parameters of HNSW Index. Could be overridden for each collection or named vector individually
  hnsw_index:
    # Number of edges per node in the index graph.
    # Larger the value - more accurate the search, more space required.
    m: 16
    # Number of neighbours to consider during the index building.
    # Larger the value - more accurate the search, more time required to build index.
    ef_construct: 100
    # Minimal size threshold (in KiloBytes) below which full-scan is preferred over HNSW search.
    # This measures the total size of vectors being queried against.
    # When the maximum estimated amount of points that a condition satisfies is smaller than
    # `full_scan_threshold_kb`, the query planner will use full-scan search instead of HNSW index
    # traversal for better performance.
    # Note: 1Kb = 1 vector of size 256
    full_scan_threshold: 10000

```

And so in the process of creating a [collection](https://qdrant.tech/documentation/concepts/collections/). The `ef` parameter is configured during [the search](https://qdrant.tech/documentation/concepts/search/) and by default is equal to `ef_construct`.
HNSW is chosen for several reasons. First, HNSW is well-compatible with the modification that allows Qdrant to use filters during a search. Second, it is one of the most accurate and fastest algorithms, according to
_Available as of v1.1.1_
The HNSW parameters can also be configured on a collection and named vector level by setting [`hnsw_config`](https://qdrant.tech/documentation/concepts/indexing/#vector-index) to fine-tune search performance.
###  [](https://qdrant.tech/documentation/concepts/indexing/#filterable-hnsw-index)Filterable HNSW Index
Separately, a payload index and a vector index cannot completely address the challenges of filtered search.
In the case of high-selectivity (weak) filters, you can use the HNSW index as it is. In the case of low-selectivity (strict) filters, you can use the payload index and do a complete rescore. However, for cases in the middle, this approach does not work well. On one hand, we cannot apply a full scan on too many vectors. On the other hand, the HNSW graph starts to fall apart when using filters that are too strict.
![HNSW fail](https://qdrant.tech/docs/precision_by_m.png)
Qdrant solves this problem by extending the HNSW graph with additional edges based on indexed payload values. Extra edges allow you to efficiently search for nearby vectors using the HNSW index and apply filters as you search in the graph. You can find more information on this approach in our [article](https://qdrant.tech/articles/filterable-hnsw/).
####  [](https://qdrant.tech/documentation/concepts/indexing/#the-acorn-search-algorithm)The ACORN Search Algorithm
_Available as of v1.16.0_
In some cases, the additional edges built for Qdrant’s filterable HNSW may not be sufficient. These extra edges are added for each payload index separately, but not for every possible combination of payload indices. As a result, a combination of two or more strict filters might still lead to disconnected graph components. The same can happen when there are a large number of soft-deleted points in the graph. In such cases, use the [ACORN Search Algorithm](https://qdrant.tech/documentation/concepts/search/#acorn-search-algorithm). When using ACORN, during graph traversal, it explores not just direct neighbors (first hop), but also neighbors of neighbors (second hop) when direct neighbors are filtered out. This improves search accuracy at the cost of performance.
####  [](https://qdrant.tech/documentation/concepts/indexing/#disable-the-creation-of-extra-edges-for-payload-fields)Disable the Creation of Extra Edges for Payload Fields
_Available as of v1.17.0_
Not all payload indices may be intended for use with dense vector search. For example, when a collection contains both dense and sparse vectors, some payload fields may only be used to filter sparse vector searches. Since sparse vector search does not use the HNSW index, it is unnecessary to build extra edges in the HNSW graph for these fields. Creating extra edges adds indexing latency and increases the size of the HNSW graph, which consumes memory as well as disk space, so you may want to disable it for fields that do not require it.
You can disable the creation of extra edges for an indexed payload field by setting `enable_hnsw` to `false` when configuring a payload index:
httppythontypescriptrustjavacsharpgo
```
PUT /collections/{collection_name}/index
{
    "field_name": "name_of_the_field_to_index",
    "field_schema": {
        "type": "keyword",
        "enable_hnsw": false
    }
}

```

```
from qdrant_client import QdrantClient, models

client = QdrantClient(url="http://localhost:6333")

client.create_payload_index(
    collection_name="{collection_name}",
    field_name="name_of_the_field_to_index",
    field_schema=models.TextIndexParams(
        type=models.TextIndexType.TEXT,
        tokenizer=models.TokenizerType.WORD,
        enable_hnsw=False,
    ),
)

```

```
client.createPayloadIndex("{collection_name}", {
  field_name: "name_of_the_field_to_index",
  field_schema: {
    type: "keyword",
    enable_hnsw: false,
  },
});

```

```
use qdrant_client::qdrant::{
    CreateFieldIndexCollectionBuilder, FieldType, KeywordIndexParamsBuilder,
};
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

client
    .create_field_index(
        CreateFieldIndexCollectionBuilder::new(
            "{collection_name}",
            "name_of_the_field_to_index",
            FieldType::Keyword,
        )
        .field_index_params(KeywordIndexParamsBuilder::default().enable_hnsw(false)),
    )
    .await?;

```

```
import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Collections.KeywordIndexParams;
import io.qdrant.client.grpc.Collections.PayloadIndexParams;
import io.qdrant.client.grpc.Collections.PayloadSchemaType;

QdrantClient client =
    new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client
    .createPayloadIndexAsync(
        "{collection_name}",
        "name_of_the_field_to_index",
        PayloadSchemaType.Keyword,
        PayloadIndexParams.newBuilder()
            .setKeywordIndexParams(
                KeywordIndexParams.newBuilder()
                    .setEnableHnsw(false)
                    .build())
            .build(),
        null,
        null,
        null)
    .get();

```

```
using Qdrant.Client;
using Qdrant.Client.Grpc;

var client = new QdrantClient("localhost", 6334);

await client.CreatePayloadIndexAsync(
 collectionName: "{collection_name}",
 fieldName: "name_of_the_field_to_index",
 schemaType: PayloadSchemaType.Keyword,
 indexParams: new PayloadIndexParams
 {
  KeywordIndexParams = new KeywordIndexParams
  {
   EnableHnsw = false
  }
 }
);

```

```
import (
	"context"

	"github.com/qdrant/go-client/qdrant"
)

client, err := qdrant.NewClient(&qdrant.Config{
	Host: "localhost",
	Port: 6334,
})

client.CreateFieldIndex(context.Background(), &qdrant.CreateFieldIndexCollection{
	CollectionName: "{collection_name}",
	FieldName:      "name_of_the_field_to_index",
	FieldType:      qdrant.FieldType_FieldTypeKeyword.Enum(),
	FieldIndexParams: qdrant.NewPayloadIndexParamsKeyword(
		&qdrant.KeywordIndexParams{
			EnableHnsw: qdrant.PtrOf(false),
		}),
})

```
