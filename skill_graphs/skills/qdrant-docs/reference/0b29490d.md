##  [](https://qdrant.tech/documentation/concepts/points/#conditional-updates)Conditional updates
_Available as of v1.16.0_
All update operations (including point insertion, vector updates, payload updates, and deletions) support configurable pre-conditions based on filters.
httppythontypescriptrustjavacsharpgo
```
PUT /collections/{collection_name}/points
{
    "points": [
        {
            "id": 1,
            "vector": [0.05, 0.61, 0.76, 0.74],
            "payload": {
                "city": "Berlin",
                "price": 1.99,
                "version": 3
            }
        }
    ],
    "update_filter": {
        "must": [
            {
                "key": "version",
                "match": {
                    "value": 2
                }
            }
        ]
    }
}

```

```
from qdrant_client import QdrantClient, models

client = QdrantClient(url="http://localhost:6333")

client.upsert(
    collection_name="{collection_name}",
    points=[
        models.PointStruct(
            id=1,
            vector=[0.05, 0.61, 0.76, 0.74],
            payload={
                "city": "Berlin",
                "price": 1.99,
                "version": 3,
            },
        ),
    ],
    update_filter=models.Filter(
        must=[
            models.FieldCondition(
                key="version",
                match=models.MatchValue(value=2),
            ),
        ],
    ),
)

```

```
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.upsert("{collection_name}", {
  points: [
    {
      id: 1,
      vector: [0.05, 0.61, 0.76, 0.74],
      payload: {
        city: "Berlin",
        price: 1.99,
        version: 3
      },
    }
  ],
  update_filter: {
    must: [
      {
        key: "version",
        match: {
          value: 2
        }
      }
    ]
  }
});

```

```
use qdrant_client::qdrant::{PointStruct, UpsertPointsBuilder, Filter, Condition};
use qdrant_client::{Payload, Qdrant};
use serde_json::json;

let client = Qdrant::from_url("http://localhost:6334").build()?;

let points = vec![
    PointStruct::new(
        1,
        vec![0.05, 0.61, 0.76, 0.74],
        Payload::try_from(json!({
            "city": "Berlin",
            "price": 1.99,
            "version": 3
        })).unwrap(),
    )
];

client
    .upsert_points(
        UpsertPointsBuilder::new("{collection_name}", points)
            .wait(true)
            .update_filter(Filter::must([Condition::matches("version", 2)]))
    ).await?;

```

```
import static io.qdrant.client.ConditionFactory.match;
import static io.qdrant.client.PointIdFactory.id;
import static io.qdrant.client.ValueFactory.value;
import static io.qdrant.client.VectorsFactory.vectors;

import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Common.Filter;
import io.qdrant.client.grpc.Points.PointStruct;
import io.qdrant.client.grpc.Points.UpsertPoints;
import java.util.Map;

QdrantClient client =
    new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client
    .upsertAsync(
        UpsertPoints.newBuilder()
            .setCollectionName("{collectionName}")
            .addPoints(
                PointStruct.newBuilder()
                    .setId(id(1))
                    .setVectors(vectors(0.05f, 0.61f, 0.76f, 0.74f))
                    .putAllPayload(Map.of("city", value("Berlin"), "price", value(1.99)))
                    .build())
            .setUpdateFilter(Filter.newBuilder().addMust(match("version", 2)).build())
            .build())
    .get();

```

```
using Qdrant.Client;
using Qdrant.Client.Grpc;
using static Qdrant.Client.Grpc.Conditions;

var client = new QdrantClient("localhost", 6334);

await client.UpsertAsync(
    collectionName: "{collection_name}",
    points: new List<PointStruct>
    {
        new PointStruct
        {
            Id = 1,
            Vectors = new[] { 0.05f, 0.61f, 0.76f, 0.74f },
            Payload = {
                ["city"] = "Berlin",
                ["price"] = 1.99,
                ["version"] = 3
            }
        }
    },
    updateFilter: Match("version", 2)
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
            Vectors: qdrant.NewVectors(0.05, 0.61, 0.76, 0.74),
            Payload: qdrant.NewValueMap(map[string]any{
                "city": "Berlin", "price": 1.99, "version": 3}),
        },
    },
    UpdateFilter: &qdrant.Filter{
        Must: []*qdrant.Condition{
            qdrant.NewMatchInt("version", 2),
        },
    },
})

```

By default, a conditional update on a non-existent point behaves as a regular upsert, inserting the point regardless of the filter. This is undesirable in most cases. To ensure that only existing points that meet the condition are updated, [set `update_mode`](https://qdrant.tech/documentation/concepts/points/#update-mode) to `update_only`.
While conditional payload modification and deletion covers the use-case of mass data modification, conditional point insertion and vector updates are particularly useful for implementing optimistic concurrency control in distributed systems.
A common scenario for such mechanism is when multiple clients try to update the same point independently. Consider the following sequence of events:
  * Client A reads point P.
  * Client B reads point P.
  * Client A modifies point P and writes it back to Qdrant.
  * Client B modifies point P (based on the stale data) and writes it back to Qdrant, unintentionally overwriting changes made by Client A.


To prevent such situations, Client B can use conditional updates. For this, we would need to introduce an additional field in the payload, e.g. `version`, which would be incremented on each update.
When Client A writes back the modified point P, it would set the condition that the `version` field must be equal to the value it read initially. If Client B tries to write back its changes later, the condition would fail (as the `version` has been incremented by Client A), and Qdrant would reject the update, preventing accidental overwrites.
Instead of `version`, applications can use timestamps (assuming synchronized clocks) or any other monotonically increasing value that fits their data model.
