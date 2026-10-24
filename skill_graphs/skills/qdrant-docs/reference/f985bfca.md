##  [](https://qdrant.tech/documentation/concepts/collections/#collection-info)Collection info
Qdrant allows determining the configuration parameters of an existing collection to better understand how the points are distributed and indexed.
httpbashpythontypescriptrustjavacsharpgo
```
GET /collections/{collection_name}

```

```
curl -X GET http://localhost:6333/collections/{collection_name}

```

```
client.get_collection(collection_name="{collection_name}")

```

```
client.getCollection("{collection_name}");

```

```
client.collection_info("{collection_name}").await?;

```

```
client.getCollectionInfoAsync("{collection_name}").get();

```

```
await client.GetCollectionInfoAsync("{collection_name}");

```

```
import "context"

client.GetCollectionInfo(context.Background(), "{collection_name}")

```

Expected result
```
{
    "result": {
        "status": "green",
        "optimizer_status": "ok",
        "indexed_vectors_count": 1024232,
        "points_count": 1068786,
        "segments_count": 31,
        "config": {
            "params": {
                "vectors": {
                    "size": 384,
                    "distance": "Cosine"
                },
                "shard_number": 1,
                "replication_factor": 1,
                "write_consistency_factor": 1,
                "on_disk_payload": false
            },
            "hnsw_config": {
                "m": 16,
                "ef_construct": 100,
                "full_scan_threshold": 10000,
                "max_indexing_threads": 0
            },
            "optimizer_config": {
                "deleted_threshold": 0.2,
                "vacuum_min_vector_number": 1000,
                "default_segment_number": 0,
                "max_segment_size": null,
                "memmap_threshold": null,
                "indexing_threshold": 20000,
                "flush_interval_sec": 5,
                "max_optimization_threads": 1
            },
            "wal_config": {
                "wal_capacity_mb": 32,
                "wal_segments_ahead": 0
            }
        },
        "payload_schema": {}
    },
    "status": "ok",
    "time": 0.00010143
}

```

If you insert the vectors into the collection, the `status` field may become `yellow` whilst it is optimizing. It will become `green` once all the points are successfully processed.
The following color statuses are possible:
  * 🟢 `green`: collection is ready
  * 🟡 `yellow`: collection is optimizing
  * ⚫ `grey`: collection is pending optimization ([help](https://qdrant.tech/documentation/concepts/collections/#grey-collection-status))
  * 🔴 `red`: an error occurred which the engine could not recover from


###  [](https://qdrant.tech/documentation/concepts/collections/#grey-collection-status)Grey collection status
_Available as of v1.9.0_
A collection may have the grey ⚫ status or show “optimizations pending, awaiting update operation” as optimization status. This state is normally caused by restarting a Qdrant instance while optimizations were ongoing.
It means the collection has optimizations pending, but they are paused. You must send any update operation to trigger and start the optimizations again.
For example:
httpbashpythontypescriptrustjavacsharpgo
```
PATCH /collections/{collection_name}
{
    "optimizers_config": {}
}

```

```
curl -X PATCH http://localhost:6333/collections/{collection_name} \
  -H 'Content-Type: application/json' \
  --data-raw '{
    "optimizers_config": {}
  }'

```

```
client.update_collection(
    collection_name="{collection_name}",
    optimizer_config=models.OptimizersConfigDiff(),
)

```

```
client.updateCollection("{collection_name}", {
  optimizers_config: {},
});

```

```
use qdrant_client::qdrant::{OptimizersConfigDiffBuilder, UpdateCollectionBuilder};

client
    .update_collection(
        UpdateCollectionBuilder::new("{collection_name}")
            .optimizers_config(OptimizersConfigDiffBuilder::default()),
    )
    .await?;

```

```
import io.qdrant.client.grpc.Collections.OptimizersConfigDiff;
import io.qdrant.client.grpc.Collections.UpdateCollection;

client.updateCollectionAsync(
    UpdateCollection.newBuilder()
        .setCollectionName("{collection_name}")
        .setOptimizersConfig(
            OptimizersConfigDiff.getDefaultInstance())
        .build());

```

```
using Qdrant.Client;
using Qdrant.Client.Grpc;

var client = new QdrantClient("localhost", 6334);

await client.UpdateCollectionAsync(
	collectionName: "{collection_name}",
	optimizersConfig: new OptimizersConfigDiff { }
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

client.UpdateCollection(context.Background(), &qdrant.UpdateCollection{
	CollectionName:   "{collection_name}",
	OptimizersConfig: &qdrant.OptimizersConfigDiff{},
})

```

Alternatively you may use the `Trigger Optimizers` button in the [Qdrant Web UI](https://qdrant.tech/documentation/web-ui/). It is shown next to the grey collection status on the collection info page.
###  [](https://qdrant.tech/documentation/concepts/collections/#approximate-point-and-vector-counts)Approximate point and vector counts
You may be interested in the count attributes:
  * `points_count` - total number of objects (vectors and their payloads) stored in the collection
  * `indexed_vectors_count` - total number of vectors stored in the HNSW or sparse index. Qdrant does not store all the vectors in the index, but only if an index segment might be created for a given configuration.


The above counts are not exact, but should be considered approximate. Depending on how you use Qdrant these may give very different numbers than what you may expect. It’s therefore important **not** to rely on them.
More specifically, these numbers represent the count of points and vectors in Qdrant’s internal storage. Internally, Qdrant may temporarily duplicate points as part of automatic optimizations. It may keep changed or deleted points for a bit. And it may delay indexing of new points. All of that is for optimization reasons.
Updates you do are therefore not directly reflected in these numbers. If you see a wildly different count of points, it will likely resolve itself once a new round of automatic optimizations is completed.
To clarify: these numbers don’t represent the exact amount of points or vectors you have inserted, nor does it represent the exact number of distinguishable points or vectors you can query. If you want to know exact counts, refer to the [count API](https://qdrant.tech/documentation/concepts/points/#counting-points).
_Note: these numbers may be removed in a future version of Qdrant._
###  [](https://qdrant.tech/documentation/concepts/collections/#indexing-vectors-in-hnsw)Indexing vectors in HNSW
In some cases, you might be surprised the value of `indexed_vectors_count` is lower than you expected. This is an intended behaviour and depends on the [optimizer configuration](https://qdrant.tech/documentation/concepts/optimizer/). A new index segment is built if the size of non-indexed vectors is higher than the value of `indexing_threshold`(in kB). If your collection is very small or the dimensionality of the vectors is low, there might be no HNSW segment created and `indexed_vectors_count` might be equal to `0`.
It is possible to reduce the `indexing_threshold` for an existing collection by [updating collection parameters](https://qdrant.tech/documentation/concepts/collections/#update-collection-parameters).
###  [](https://qdrant.tech/documentation/concepts/collections/#collection-metadata)Collection metadata
_Available as of v1.16.0_
For convenience and better data organization, Qdrant allows attaching custom metadata to collections in the form of key-value pairs. Adding metadata is treated as a part of collection configuration and synchronized across all nodes in a cluster with consensus protocol.
Collection metadata can be specified during collection creation:
httpbashpythontypescriptrustjavacsharpgo
```
PUT /collections/{collection_name}
{
    "vectors": {
      "size": 300,
      "distance": "Cosine"
    },
    "metadata": {
      "my-metadata-field": "value-1",
      "another-field": 123
    }
}

```

```
curl -X PUT http://localhost:6333/collections/{collection_name} \
  -H 'Content-Type: application/json' \
  --data-raw '{
    "vectors": {
      "size": 300,
      "distance": "Cosine"
    },
    "metadata": {
      "my-metadata-field": "value-1",
      "another-field": 123
    }
  }'

```

```
from qdrant_client import QdrantClient, models

client = QdrantClient(url="http://localhost:6333")

client.create_collection(
    collection_name="{collection_name}",
    metadata={
        "my-metadata-field": "value-1",
        "another-field": 123
    },
)

```

```
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.createCollection("{collection_name}", {
  vectors: { size: 100, distance: "Cosine" },
  metadata: {
    "my-metadata-field": "value-1",
    "another-field": 123
  }
});

```

```
use qdrant_client::qdrant::{CreateCollectionBuilder, Distance, VectorParamsBuilder};
use qdrant_client::Qdrant;
use serde_json::{json, Value};
use std::collections::HashMap;

let client = Qdrant::from_url("http://localhost:6334").build()?;

let mut metadata: HashMap<String, Value> = HashMap::new();
metadata.insert("my-metadata-field".to_string(), json!("value-1"));
metadata.insert("another-field".to_string(), json!(123));

client
    .create_collection(
        CreateCollectionBuilder::new("{collection_name}")
            .vectors_config(VectorParamsBuilder::new(100, Distance::Cosine))
            .metadata(metadata),
    )
    .await?;

```

```
import static io.qdrant.client.ValueFactory.value;

import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Collections.CreateCollection;
import io.qdrant.client.grpc.Collections.Distance;
import io.qdrant.client.grpc.Collections.VectorParams;
import io.qdrant.client.grpc.Collections.VectorsConfig;
import java.util.Map;

QdrantClient client = new QdrantClient(
    QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client
    .createCollectionAsync(
        CreateCollection.newBuilder()
            .setCollectionName("{collection_name}")
            .setVectorsConfig(
                VectorsConfig.newBuilder()
                    .setParams(
                        VectorParams.newBuilder()
                            .setDistance(Distance.Cosine)
                            .setSize(100)
                            .build())
                    .build())
            .putAllMetadata(
                Map.of(
                    "my-metadata-field", value("value-1"),
                    "another-field", value(123)))
            .build())
    .get();

```

```
using Qdrant.Client;
using Qdrant.Client.Grpc;

var client = new QdrantClient("localhost", 6334);

await client.CreateCollectionAsync(
	collectionName: "{collection_name}",
	vectorsConfig: new VectorParams { Size = 100, Distance = Distance.Cosine },
	metadata: new()
	{
		["my-metadata-field"] = "value-1",
		["another-field"] = 123
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

client.CreateCollection(context.Background(), &qdrant.CreateCollection{
	CollectionName: "{collection_name}",
	VectorsConfig: qdrant.NewVectorsConfig(&qdrant.VectorParams{
		Size:     100,
		Distance: qdrant.Distance_Cosine,
	}),
	Metadata: qdrant.NewValueMap(map[string]any{
		"my-metadata-field": "value-1",
		"another-field":     123,
	}),
})

```

as well as updated later:
httpbashpythontypescriptrustjavacsharpgo
```
PATCH /collections/{collection_name}
{
    "metadata": {
        "my-metadata-field": {
            "key-a": "value-a",
            "key-b": 42
        }
    }
}

```

```
curl -X PATCH http://localhost:6333/collections/{collection_name} \
  -H 'Content-Type: application/json' \
  --data-raw '{
    "metadata": {
      "my-metadata-field": {
        "key-a": "value-a",
        "key-b": 42
      }
    }
  }'

```

```
client.update_collection(
    collection_name="{collection_name}",
    metadata={
        "my-metadata-field": {
            "key-a": "value-a",
            "key-b": 42
        }
    },
)

```

```
client.updateCollection("{collection_name}", {
  metadata: {
    "my-metadata-field": {
      "key-a": "value-a",
      "key-b": 42
    }
  },
});

```

```
use qdrant_client::qdrant::{UpdateCollectionBuilder};
use qdrant_client::Qdrant;
use serde_json::{json, Value};
use std::collections::HashMap;

let client = Qdrant::from_url("http://localhost:6334").build()?;

let mut metadata: HashMap<String, Value> = HashMap::new();
metadata.insert("my-metadata-field".to_string(), json!({
    "key-a": "value-a",
    "key-b": 42
}));

client
    .update_collection(
        UpdateCollectionBuilder::new("{collection_name}").metadata(metadata),
    )
    .await?;

```

```
import static io.qdrant.client.ValueFactory.value;

import io.qdrant.client.grpc.Collections.OptimizersConfigDiff;
import io.qdrant.client.grpc.Collections.UpdateCollection;
import java.util.Map;

client
    .updateCollectionAsync(
        UpdateCollection.newBuilder()
            .setCollectionName("{collection_name}")
            .setOptimizersConfig(
                OptimizersConfigDiff.newBuilder().setIndexingThreshold(10000).build())
            .putAllMetadata(
                Map.of(
                    "my-metadata-field",
                    value(
                        Map.of(
                            "key-a", value("value-a"),
                            "key-b", value(42)))))
            .build())
    .get();

```

```
using Qdrant.Client;
using Qdrant.Client.Grpc;

var client = new QdrantClient("localhost", 6334);

await client.UpdateCollectionAsync(
	collectionName: "{collection_name}",
	optimizersConfig: new OptimizersConfigDiff { IndexingThreshold = 10000 },
	metadata: new()
	{
		["my-metadata-field"] = new Dictionary<string, Value>
		{
			["key-a"] = "value-a",
			["key-b"] = 42
		},
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

client.UpdateCollection(context.Background(), &qdrant.UpdateCollection{
	CollectionName: "{collection_name}",
	OptimizersConfig: &qdrant.OptimizersConfigDiff{
		IndexingThreshold: qdrant.PtrOf(uint64(10000)),
	},
	Metadata: qdrant.NewValueMap(map[string]any{
		"my-metadata-field": map[string]any{
			"key-a": "value-a",
			"key-b": 42,
		},
	}),
})

```

Note, that update operation only modifies the specified metadata fields, leaving other fields unchanged.
When specified, metadata is returned as part of collection info:
```
{
    "result": {
        "config": {
            "metadata": {
                "my-metadata-field": {
                    "key-a": "value-a",
                    "key-b": 42
                },
                "another-field": 123
            }
        }
    }
}

```
