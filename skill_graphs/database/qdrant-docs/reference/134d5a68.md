##  [](https://qdrant.tech/documentation/concepts/points/#upload-points)Upload points
To optimize performance, Qdrant supports batch loading of points. I.e., you can load several points into the service in one API call. Batching allows you to minimize the overhead of creating a network connection.
The Qdrant API supports two ways of creating batches - record-oriented and column-oriented. Internally, these options do not differ and are made only for the convenience of interaction.
Create points with batch:
httppythontypescript
```
PUT /collections/{collection_name}/points
{
    "batch": {
        "ids": [1, 2, 3],
        "payloads": [
            {"color": "red"},
            {"color": "green"},
            {"color": "blue"}
        ],
        "vectors": [
            [0.9, 0.1, 0.1],
            [0.1, 0.9, 0.1],
            [0.1, 0.1, 0.9]
        ]
    }
}

```

```
client.upsert(
    collection_name="{collection_name}",
    points=models.Batch(
        ids=[1, 2, 3],
        payloads=[
            {"color": "red"},
            {"color": "green"},
            {"color": "blue"},
        ],
        vectors=[
            [0.9, 0.1, 0.1],
            [0.1, 0.9, 0.1],
            [0.1, 0.1, 0.9],
        ],
    ),
)

```

```
client.upsert("{collection_name}", {
  batch: {
    ids: [1, 2, 3],
    payloads: [{ color: "red" }, { color: "green" }, { color: "blue" }],
    vectors: [
      [0.9, 0.1, 0.1],
      [0.1, 0.9, 0.1],
      [0.1, 0.1, 0.9],
    ],
  },
});

```

or record-oriented equivalent:
httppythontypescriptrustjavacsharpgo
```
PUT /collections/{collection_name}/points
{
    "points": [
        {
            "id": 1,
            "payload": {"color": "red"},
            "vector": [0.9, 0.1, 0.1]
        },
        {
            "id": 2,
            "payload": {"color": "green"},
            "vector": [0.1, 0.9, 0.1]
        },
        {
            "id": 3,
            "payload": {"color": "blue"},
            "vector": [0.1, 0.1, 0.9]
        }
    ]
}

```

```
client.upsert(
    collection_name="{collection_name}",
    points=[
        models.PointStruct(
            id=1,
            payload={
                "color": "red",
            },
            vector=[0.9, 0.1, 0.1],
        ),
        models.PointStruct(
            id=2,
            payload={
                "color": "green",
            },
            vector=[0.1, 0.9, 0.1],
        ),
        models.PointStruct(
            id=3,
            payload={
                "color": "blue",
            },
            vector=[0.1, 0.1, 0.9],
        ),
    ],
)

```

```
client.upsert("{collection_name}", {
  points: [
    {
      id: 1,
      payload: { color: "red" },
      vector: [0.9, 0.1, 0.1],
    },
    {
      id: 2,
      payload: { color: "green" },
      vector: [0.1, 0.9, 0.1],
    },
    {
      id: 3,
      payload: { color: "blue" },
      vector: [0.1, 0.1, 0.9],
    },
  ],
});

```

```
use qdrant_client::qdrant::{PointStruct, UpsertPointsBuilder};

client
    .upsert_points(
        UpsertPointsBuilder::new(
            "{collection_name}",
            vec![
                PointStruct::new(1, vec![0.9, 0.1, 0.1], [("color", "red".into())]),
                PointStruct::new(2, vec![0.1, 0.9, 0.1], [("color", "green".into())]),
                PointStruct::new(3, vec![0.1, 0.1, 0.9], [("color", "blue".into())]),
            ],
        )
        .wait(true),
    )
    .await?;

```

```
import static io.qdrant.client.PointIdFactory.id;
import static io.qdrant.client.ValueFactory.value;
import static io.qdrant.client.VectorsFactory.vectors;

import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Points.PointStruct;
import java.util.List;
import java.util.Map;

QdrantClient client =
    new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client
    .upsertAsync(
        "{collection_name}",
        List.of(
            PointStruct.newBuilder()
                .setId(id(1))
                .setVectors(vectors(0.9f, 0.1f, 0.1f))
                .putAllPayload(Map.of("color", value("red")))
                .build(),
            PointStruct.newBuilder()
                .setId(id(2))
                .setVectors(vectors(0.1f, 0.9f, 0.1f))
                .putAllPayload(Map.of("color", value("green")))
                .build(),
            PointStruct.newBuilder()
                .setId(id(3))
                .setVectors(vectors(0.1f, 0.1f, 0.9f))
                .putAllPayload(Map.of("color", value("blue")))
                .build()))
    .get();

```

```
using Qdrant.Client;
using Qdrant.Client.Grpc;

var client = new QdrantClient("localhost", 6334);

await client.UpsertAsync(
	collectionName: "{collection_name}",
	points: new List<PointStruct>
	{
		new()
		{
			Id = 1,
			Vectors = new[] { 0.9f, 0.1f, 0.1f },
			Payload = { ["color"] = "red" }
		},
		new()
		{
			Id = 2,
			Vectors = new[] { 0.1f, 0.9f, 0.1f },
			Payload = { ["color"] = "green" }
		},
		new()
		{
			Id = 3,
			Vectors = new[] { 0.1f, 0.1f, 0.9f },
			Payload = { ["color"] = "blue" }
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

client.Upsert(context.Background(), &qdrant.UpsertPoints{
	CollectionName: "{collection_name}",
	Points: []*qdrant.PointStruct{
		{
			Id:      qdrant.NewIDNum(1),
			Vectors: qdrant.NewVectors(0.9, 0.1, 0.1),
			Payload: qdrant.NewValueMap(map[string]any{"color": "red"}),
		},
		{
			Id:      qdrant.NewIDNum(2),
			Vectors: qdrant.NewVectors(0.1, 0.9, 0.1),
			Payload: qdrant.NewValueMap(map[string]any{"color": "green"}),
		},
		{
			Id:      qdrant.NewIDNum(3),
			Vectors: qdrant.NewVectors(0.1, 0.1, 0.9),
			Payload: qdrant.NewValueMap(map[string]any{"color": "blue"}),
		},
	},
})

```

###  [](https://qdrant.tech/documentation/concepts/points/#python-client-optimizations)Python client optimizations
The Python client has additional features for loading points, which include:
  * Parallelization
  * A retry mechanism
  * Lazy batching support


For example, you can read your data directly from hard drives, to avoid storing all data in RAM. You can use these features with the `upload_collection` and `upload_points` methods. Similar to the basic upsert API, these methods support both record-oriented and column-oriented formats.
`upload_points` is available as of v1.7.1. It has replaced `upload_records` which is now deprecated.
Column-oriented format:
```
client.upload_collection(
    collection_name="{collection_name}",
    ids=[1, 2],
    payload=[
        {"color": "red"},
        {"color": "green"},
    ],
    vectors=[
        [0.9, 0.1, 0.1],
        [0.1, 0.9, 0.1],
    ],
    parallel=4,
    max_retries=3,
)

```

If `ids` are not provided, Qdrant Client will generate them automatically as random UUIDs.
Record-oriented format:
```
client.upload_points(
    collection_name="{collection_name}",
    points=[
        models.PointStruct(
            id=1,
            payload={
                "color": "red",
            },
            vector=[0.9, 0.1, 0.1],
        ),
        models.PointStruct(
            id=2,
            payload={
                "color": "green",
            },
            vector=[0.1, 0.9, 0.1],
        ),
    ],
    parallel=4,
    max_retries=3,
)

```

###  [](https://qdrant.tech/documentation/concepts/points/#idempotence)Idempotence
All APIs in Qdrant, including point loading, are idempotent. It means that executing the same method several times in a row is equivalent to a single execution.
In this case, it means that points with the same id will be overwritten when re-uploaded.
Idempotence property is useful if you use, for example, a message queue that doesn’t provide an exactly-once guarantee. Even with such a system, Qdrant ensures data consistency.
###  [](https://qdrant.tech/documentation/concepts/points/#update-mode)Update Mode
_Available as of v1.17.0_
By default, an upsert operation inserts a point if it does not exist, or updates it if it does. To change this behavior, use the `update_mode` parameter:
  * `upsert` (default): Insert a point if it does not exist, or update it if it does.
  * `insert_only`: Insert a point only if it does not already exist. If a point with the same ID exists, the operation is ignored.
  * `update_only`: Update a point only if it already exists. Points that do not exist are not inserted.


For example, to use `insert_only` mode:
httppythontypescriptrustjavacsharpgo
```
PUT /collections/{collection_name}/points
{
    "points": [
        {
            "id": 1,
            "payload": {"color": "red"},
            "vector": [0.9, 0.1, 0.1]
        },
        {
            "id": 2,
            "payload": {"color": "green"},
            "vector": [0.1, 0.9, 0.1]
        },
        {
            "id": 3,
            "payload": {"color": "blue"},
            "vector": [0.1, 0.1, 0.9]
        }
    ],
    "update_mode": "insert_only"
}

```

```
client.upsert(
    collection_name="{collection_name}",
    points=[
        models.PointStruct(
            id=1,
            vector=[0.9, 0.1, 0.1],
            payload={
                "color": "red",
            },
        ),
        models.PointStruct(
            id=2,
            vector=[0.1, 0.9, 0.1],
            payload={
                "color": "green",
            },
        ),
        models.PointStruct(
            id=3,
            vector=[0.1, 0.1, 0.9],
            payload={
                "color": "blue",
            },
        ),
    ],
    update_mode=models.UpdateMode.INSERT_ONLY
)

```

```
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.upsert("{collection_name}", {
  points: [
    {
      id: 1,
      payload: { color: "red" },
      vector: [0.9, 0.1, 0.1],
    },
    {
      id: 2,
      payload: { color: "green" },
      vector: [0.1, 0.9, 0.1],
    },
    {
      id: 3,
      payload: { color: "blue" },
      vector: [0.1, 0.1, 0.9],
    },
  ],
  update_mode: "insert_only",
});

```

```
use qdrant_client::qdrant::{PointStruct, UpdateMode, UpsertPointsBuilder};

client
    .upsert_points(
        UpsertPointsBuilder::new(
            "{collection_name}",
            vec![
                PointStruct::new(1, vec![0.9, 0.1, 0.1], [("color", "red".into())]),
                PointStruct::new(2, vec![0.1, 0.9, 0.1], [("color", "green".into())]),
                PointStruct::new(3, vec![0.1, 0.1, 0.9], [("color", "blue".into())]),
            ],
        )
        .update_mode(UpdateMode::InsertOnly),
    )
    .await?;

```

```
import static io.qdrant.client.PointIdFactory.id;
import static io.qdrant.client.ValueFactory.value;
import static io.qdrant.client.VectorsFactory.vectors;

import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Points.PointStruct;
import io.qdrant.client.grpc.Points.UpdateMode;
import io.qdrant.client.grpc.Points.UpsertPoints;
import java.util.List;
import java.util.Map;

QdrantClient client =
    new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client
    .upsertAsync(
        UpsertPoints.newBuilder()
            .setCollectionName("{collection_name}")
            .addAllPoints(
                List.of(
                    PointStruct.newBuilder()
                        .setId(id(1))
                        .setVectors(vectors(0.9f, 0.1f, 0.1f))
                        .putAllPayload(Map.of("color", value("red")))
                        .build(),
                    PointStruct.newBuilder()
                        .setId(id(2))
                        .setVectors(vectors(0.1f, 0.9f, 0.1f))
                        .putAllPayload(Map.of("color", value("green")))
                        .build(),
                    PointStruct.newBuilder()
                        .setId(id(3))
                        .setVectors(vectors(0.1f, 0.1f, 0.9f))
                        .putAllPayload(Map.of("color", value("blue")))
                        .build()))
            .setUpdateMode(UpdateMode.InsertOnly)
            .build())
    .get();

```

```
using Qdrant.Client;
using Qdrant.Client.Grpc;

var client = new QdrantClient("localhost", 6334);

await client.UpsertAsync(
	new()
	{
		CollectionName = "{collection_name}",
		Points =
		{
			new List<PointStruct>
			{
				new()
				{
					Id = 1,
					Vectors = new[] { 0.9f, 0.1f, 0.1f },
					Payload = { ["color"] = "red" },
				},
				new()
				{
					Id = 2,
					Vectors = new[] { 0.1f, 0.9f, 0.1f },
					Payload = { ["color"] = "green" },
				},
				new()
				{
					Id = 3,
					Vectors = new[] { 0.1f, 0.1f, 0.9f },
					Payload = { ["color"] = "blue" },
				},
			},
		},
		UpdateMode = UpdateMode.InsertOnly,
		Wait = true,
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

client.Upsert(context.Background(), &qdrant.UpsertPoints{
	CollectionName: "{collection_name}",
	Points: []*qdrant.PointStruct{
		{
			Id:      qdrant.NewIDNum(1),
			Vectors: qdrant.NewVectors(0.9, 0.1, 0.1),
			Payload: qdrant.NewValueMap(map[string]any{"color": "red"}),
		},
		{
			Id:      qdrant.NewIDNum(2),
			Vectors: qdrant.NewVectors(0.1, 0.9, 0.1),
			Payload: qdrant.NewValueMap(map[string]any{"color": "green"}),
		},
		{
			Id:      qdrant.NewIDNum(3),
			Vectors: qdrant.NewVectors(0.1, 0.1, 0.9),
			Payload: qdrant.NewValueMap(map[string]any{"color": "blue"}),
		},
	},
	UpdateMode: qdrant.UpdateMode_InsertOnly.Enum(),
})

```

`insert_only` mode is especially useful when [migrating from one embedding model to another](https://qdrant.tech/documentation/database-tutorials/embedding-model-migration/), where conflicts between regular updates and background re-embedding tasks need to be resolved.
![Embedding model migration in blue-green deployment](https://qdrant.tech/docs/embedding-model-migration.png)
Embedding model migration in blue-green deployment
`update_only` mode is useful with [conditional updates](https://qdrant.tech/documentation/concepts/points/#conditional-updates). Because upserts default to inserts for non-existing points, a conditional update without an explicit `update_mode` will insert a new point even if the condition is not met, which is not the intended behavior in most cases.
###  [](https://qdrant.tech/documentation/concepts/points/#named-vectors)Named vectors
_Available as of v0.10.0_
If the collection was created with multiple vectors, each vector data can be provided using the vector’s name:
httppythontypescriptrustjavacsharpgo
```
PUT /collections/{collection_name}/points
{
    "points": [
        {
            "id": 1,
            "vector": {
                "image": [0.9, 0.1, 0.1, 0.2],
                "text": [0.4, 0.7, 0.1, 0.8, 0.1, 0.1, 0.9, 0.2]
            }
        },
        {
            "id": 2,
            "vector": {
                "image": [0.2, 0.1, 0.3, 0.9],
                "text": [0.5, 0.2, 0.7, 0.4, 0.7, 0.2, 0.3, 0.9]
            }
        }
    ]
}

```

```
client.upsert(
    collection_name="{collection_name}",
    points=[
        models.PointStruct(
            id=1,
            vector={
                "image": [0.9, 0.1, 0.1, 0.2],
                "text": [0.4, 0.7, 0.1, 0.8, 0.1, 0.1, 0.9, 0.2],
            },
        ),
        models.PointStruct(
            id=2,
            vector={
                "image": [0.2, 0.1, 0.3, 0.9],
                "text": [0.5, 0.2, 0.7, 0.4, 0.7, 0.2, 0.3, 0.9],
            },
        ),
    ],
)

```

```
client.upsert("{collection_name}", {
  points: [
    {
      id: 1,
      vector: {
        image: [0.9, 0.1, 0.1, 0.2],
        text: [0.4, 0.7, 0.1, 0.8, 0.1, 0.1, 0.9, 0.2],
      },
    },
    {
      id: 2,
      vector: {
        image: [0.2, 0.1, 0.3, 0.9],
        text: [0.5, 0.2, 0.7, 0.4, 0.7, 0.2, 0.3, 0.9],
      },
    },
  ],
});

```

```
use std::collections::HashMap;

use qdrant_client::qdrant::{PointStruct, UpsertPointsBuilder};
use qdrant_client::Payload;

client
    .upsert_points(
        UpsertPointsBuilder::new(
            "{collection_name}",
            vec![
                PointStruct::new(
                    1,
                    HashMap::from([
                        ("image".to_string(), vec![0.9, 0.1, 0.1, 0.2]),
                        (
                            "text".to_string(),
                            vec![0.4, 0.7, 0.1, 0.8, 0.1, 0.1, 0.9, 0.2],
                        ),
                    ]),
                    Payload::default(),
                ),
                PointStruct::new(
                    2,
                    HashMap::from([
                        ("image".to_string(), vec![0.2, 0.1, 0.3, 0.9]),
                        (
                            "text".to_string(),
                            vec![0.5, 0.2, 0.7, 0.4, 0.7, 0.2, 0.3, 0.9],
                        ),
                    ]),
                    Payload::default(),
                ),
            ],
        )
        .wait(true),
    )
    .await?;

```

```
import static io.qdrant.client.PointIdFactory.id;
import static io.qdrant.client.VectorFactory.vector;
import static io.qdrant.client.VectorsFactory.namedVectors;

import io.qdrant.client.grpc.Points.PointStruct;
import java.util.List;
import java.util.Map;

client
    .upsertAsync(
        "{collection_name}",
        List.of(
            PointStruct.newBuilder()
                .setId(id(1))
                .setVectors(
                    namedVectors(
                        Map.of(
                            "image",
                            vector(List.of(0.9f, 0.1f, 0.1f, 0.2f)),
                            "text",
                            vector(List.of(0.4f, 0.7f, 0.1f, 0.8f, 0.1f, 0.1f, 0.9f, 0.2f)))))
                .build(),
            PointStruct.newBuilder()
                .setId(id(2))
                .setVectors(
                    namedVectors(
                        Map.of(
                            "image",
                            vector(List.of(0.2f, 0.1f, 0.3f, 0.9f)),
                            "text",
                            vector(List.of(0.5f, 0.2f, 0.7f, 0.4f, 0.7f, 0.2f, 0.3f, 0.9f)))))
                .build()))
    .get();

```

```
using Qdrant.Client;
using Qdrant.Client.Grpc;

var client = new QdrantClient("localhost", 6334);

await client.UpsertAsync(
	collectionName: "{collection_name}",
	points: new List<PointStruct>
	{
		new()
		{
			Id = 1,
			Vectors = new Dictionary<string, float[]>
			{
				["image"] = [0.9f, 0.1f, 0.1f, 0.2f],
				["text"] = [0.4f, 0.7f, 0.1f, 0.8f, 0.1f, 0.1f, 0.9f, 0.2f]
			}
		},
		new()
		{
			Id = 2,
			Vectors = new Dictionary<string, float[]>
			{
				["image"] = [0.2f, 0.1f, 0.3f, 0.9f],
				["text"] = [0.5f, 0.2f, 0.7f, 0.4f, 0.7f, 0.2f, 0.3f, 0.9f]
			}
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

client.Upsert(context.Background(), &qdrant.UpsertPoints{
	CollectionName: "{collection_name}",
	Points: []*qdrant.PointStruct{
		{
			Id: qdrant.NewIDNum(1),
			Vectors: qdrant.NewVectorsMap(map[string]*qdrant.Vector{
				"image": qdrant.NewVector(0.9, 0.1, 0.1, 0.2),
				"text":  qdrant.NewVector(0.4, 0.7, 0.1, 0.8, 0.1, 0.1, 0.9, 0.2),
			}),
		},
		{
			Id: qdrant.NewIDNum(2),
			Vectors: qdrant.NewVectorsMap(map[string]*qdrant.Vector{
				"image": qdrant.NewVector(0.2, 0.1, 0.3, 0.9),
				"text":  qdrant.NewVector(0.5, 0.2, 0.7, 0.4, 0.7, 0.2, 0.3, 0.9),
			}),
		},
	},
})

```

_Available as of v1.2.0_
Named vectors are optional. When uploading points, some vectors may be omitted. For example, you can upload one point with only the `image` vector and a second one with only the `text` vector.
When uploading a point with an existing ID, the existing point is deleted first, then it is inserted with just the specified vectors. In other words, the entire point is replaced, and any unspecified vectors are set to null. To keep existing vectors unchanged and only update specified vectors, see [update vectors](https://qdrant.tech/documentation/concepts/points/#update-vectors).
###  [](https://qdrant.tech/documentation/concepts/points/#sparse-vectors)Sparse vectors
_Available as of v1.7.0_
Points can contain dense and sparse vectors.
A sparse vector is an array in which most of the elements have a value of zero.
It is possible to take advantage of this property to have an optimized representation, for this reason they have a different shape than dense vectors.
They are represented as a list of `(index, value)` pairs, where `index` is an integer and `value` is a floating point number. The `index` is the position of the non-zero value in the vector. The `values` is the value of the non-zero element.
For example, the following vector:
```
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 2.0, 0.0, 0.0]

```

can be represented as a sparse vector:
```
[(6, 1.0), (7, 2.0)]

```

Qdrant uses the following JSON representation throughout its APIs.
```
{
  "indices": [6, 7],
  "values": [1.0, 2.0]
}

```

The `indices` and `values` arrays must have the same length. And the `indices` must be unique.
If the `indices` are not sorted, Qdrant will sort them internally so you may not rely on the order of the elements.
Sparse vectors must be named and can be uploaded in the same way as dense vectors.
httppythontypescriptrustjavacsharpgo
```
PUT /collections/{collection_name}/points
{
    "points": [
        {
            "id": 1,
            "vector": {
                "text": {
                    "indices": [6, 7],
                    "values": [1.0, 2.0]
                }
            }
        },
        {
            "id": 2,
            "vector": {
                "text": {
                    "indices": [1, 2, 4, 15, 33, 34],
                    "values": [0.1, 0.2, 0.3, 0.4, 0.5]
                }
            }
        }
    ]
}

```

```
client.upsert(
    collection_name="{collection_name}",
    points=[
        models.PointStruct(
            id=1,
            vector={
                "text": models.SparseVector(
                    indices=[6, 7],
                    values=[1.0, 2.0],
                )
            },
        ),
        models.PointStruct(
            id=2,
            vector={
                "text": models.SparseVector(
                    indices=[1, 2, 3, 4, 5],
                    values=[0.1, 0.2, 0.3, 0.4, 0.5],
                )
            },
        ),
    ],
)

```

```
client.upsert("{collection_name}", {
  points: [
    {
      id: 1,
      vector: {
        text: {
          indices: [6, 7],
          values: [1.0, 2.0],
        },
      },
    },
    {
      id: 2,
      vector: {
        text: {
          indices: [1, 2, 3, 4, 5],
          values: [0.1, 0.2, 0.3, 0.4, 0.5],
        },
      },
    },
  ],
});

```

```
use std::collections::HashMap;

use qdrant_client::qdrant::{PointStruct, UpsertPointsBuilder};
use qdrant_client::Payload;

client
    .upsert_points(
        UpsertPointsBuilder::new(
            "{collection_name}",
            vec![
                PointStruct::new(
                    1,
                    HashMap::from([("text".to_string(), vec![(6, 1.0), (7, 2.0)])]),
                    Payload::default(),
                ),
                PointStruct::new(
                    2,
                    HashMap::from([(
                        "text".to_string(),
                        vec![(1, 0.1), (2, 0.2), (3, 0.3), (4, 0.4), (5, 0.5)],
                    )]),
                    Payload::default(),
                ),
            ],
        )
        .wait(true),
    )
    .await?;

```

```
import static io.qdrant.client.PointIdFactory.id;
import static io.qdrant.client.VectorFactory.vector;

import io.qdrant.client.grpc.Points.NamedVectors;
import io.qdrant.client.grpc.Points.PointStruct;
import io.qdrant.client.grpc.Points.Vectors;
import java.util.List;
import java.util.Map;

client
    .upsertAsync(
        "{collection_name}",
        List.of(
            PointStruct.newBuilder()
                .setId(id(1))
                .setVectors(
                    Vectors.newBuilder()
                        .setVectors(
                            NamedVectors.newBuilder()
                                .putAllVectors(
                                    Map.of(
                                        "text", vector(List.of(1.0f, 2.0f), List.of(6, 7))))
                                .build())
                        .build())
                .build(),
            PointStruct.newBuilder()
                .setId(id(2))
                .setVectors(
                    Vectors.newBuilder()
                        .setVectors(
                            NamedVectors.newBuilder()
                                .putAllVectors(
                                    Map.of(
                                        "text",
                                        vector(
                                            List.of(0.1f, 0.2f, 0.3f, 0.4f, 0.5f),
                                            List.of(1, 2, 3, 4, 5))))
                                .build())
                        .build())
                .build()))
    .get();

```

```
using Qdrant.Client;
using Qdrant.Client.Grpc;

var client = new QdrantClient("localhost", 6334);

await client.UpsertAsync(
	collectionName: "{collection_name}",
	points: new List<PointStruct>
	{
		new()
		{
			Id = 1,
			Vectors = new Dictionary<string, Vector> { ["text"] = ([1.0f, 2.0f], [6, 7]) }
		},
		new()
		{
			Id = 2,
			Vectors = new Dictionary<string, Vector>
			{
				["text"] = ([0.1f, 0.2f, 0.3f, 0.4f, 0.5f], [1, 2, 3, 4, 5])
			}
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

client.Upsert(context.Background(), &qdrant.UpsertPoints{
	CollectionName: "{collection_name}",
	Points: []*qdrant.PointStruct{
		{
			Id: qdrant.NewIDNum(1),
			Vectors: qdrant.NewVectorsMap(map[string]*qdrant.Vector{
				"text": qdrant.NewVectorSparse(
					[]uint32{6, 7},
					[]float32{1.0, 2.0}),
			}),
		},
		{
			Id: qdrant.NewIDNum(2),
			Vectors: qdrant.NewVectorsMap(map[string]*qdrant.Vector{
				"text": qdrant.NewVectorSparse(
					[]uint32{1, 2, 3, 4, 5},
					[]float32{0.1, 0.2, 0.3, 0.4, 0.5}),
			}),
		},
	},
})

```

###  [](https://qdrant.tech/documentation/concepts/points/#inference)Inference
Instead of providing vectors explicitly, Qdrant can also generate vectors using a process called [inference](https://qdrant.tech/documentation/inference/). Inference is the process of creating vector embeddings from text, images, or other data types using a machine learning model.
You can use inference in the API wherever you can use regular vectors. For example, while upserting points, you can provide the text or image and the embedding model:
httppythontypescriptrustjavacsharpgo
```
PUT /collections/{collection_name}/points
{
  "points": [
    {
      "id": 1,
      "vector": {
        "my-bm25-vector": {
          "text": "Recipe for baking chocolate chip cookies",
          "model": "qdrant/bm25"
        }
      }
    }
  ]
}

```

```
from qdrant_client import QdrantClient, models

client = QdrantClient(
    url="https://xyz-example.qdrant.io:6333",
    api_key="<your-api-key>",
    cloud_inference=True
)

client.upsert(
    collection_name="{collection_name}",
    points=[
        models.PointStruct(
            id=1,
            vector={
                "my-bm25-vector": models.Document(
                    text="Recipe for baking chocolate chip cookies",
                    model="Qdrant/bm25",
                )
            },
        )
    ],
)

```

```
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.upsert("{collection_name}", {
    points: [
        {
            id: 1,
            vector: {
                'my-bm25-vector': {
                    text: 'Recipe for baking chocolate chip cookies',
                    model: 'Qdrant/bm25',
                },
            },
        },
    ],
});

```

```
use qdrant_client::{
    Payload, Qdrant,
    qdrant::{DocumentBuilder, PointStruct, UpsertPointsBuilder},
};
use std::collections::HashMap;

let client = Qdrant::from_url("<your-qdrant-url>").build()?;

client
    .upsert_points(UpsertPointsBuilder::new(
        "{collection_name}",
        vec![PointStruct::new(
            1,
            HashMap::from([(
                "my-bm25-vector".to_string(),
                DocumentBuilder::new("Recipe for baking chocolate chip cookies", "qdrant/bm25")
                    .build(),
            )]),
            Payload::default(),
        )],
    ))
    .await?;

```

```
import static io.qdrant.client.PointIdFactory.id;
import static io.qdrant.client.ValueFactory.value;
import static io.qdrant.client.VectorFactory.vector;
import static io.qdrant.client.VectorsFactory.namedVectors;

import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Points.Document;
import io.qdrant.client.grpc.Points.Image;
import io.qdrant.client.grpc.Points.PointStruct;
import java.util.List;
import java.util.Map;

QdrantClient client =
    new QdrantClient(
        QdrantGrpcClient.newBuilder("xyz-example.qdrant.io", 6334, true)
            .withApiKey("<your-api-key")
            .build());

client
    .upsertAsync(
        "{collection_name}",
        List.of(
            PointStruct.newBuilder()
                .setId(id(1))
                .setVectors(
                    namedVectors(
                        Map.of(
                            "my-bm25-vector",
                            vector(
                                Document.newBuilder()
                                    .setModel("qdrant/bm25")
                                    .setText("Recipe for baking chocolate chip cookies")
                                    .build()))))
                .build()))
    .get();

```

```
using Qdrant.Client;
using Qdrant.Client.Grpc;

var client = new QdrantClient(
host: "xyz-example.qdrant.io", port: 6334, https: true, apiKey: "<your-api-key>");

await client.UpsertAsync(
    collectionName: "{collection_name}",
    points: new List<PointStruct>
    {
        new()
        {
            Id = 1,
            Vectors = new Dictionary<string, Vector>
            {
                ["my-bm25-vector"] = new Document()
                {
                    Model = "qdrant/bm25",
                    Text = "Recipe for baking chocolate chip cookies",
                },
            },
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
    Host:   "xyz-example.qdrant.io",
    Port:   6334,
    APIKey: "<paste-your-api-key-here>",
    UseTLS: true,
})

client.Upsert(context.Background(), &qdrant.UpsertPoints{
	CollectionName: "{collection_name}",
	Points: []*qdrant.PointStruct{
		{
			Id: qdrant.NewIDNum(uint64(1)),
			Vectors: qdrant.NewVectorsMap(map[string]*qdrant.Vector{
				"my-bm25-vector": qdrant.NewVectorDocument(&qdrant.Document{
					Model: "qdrant/bm25",
					Text:  "Recipe for baking chocolate chip cookies",
				}),
			}),
		},
	},
})

```

Qdrant uses the model to generate the embeddings and store the point with the resulting vector.
