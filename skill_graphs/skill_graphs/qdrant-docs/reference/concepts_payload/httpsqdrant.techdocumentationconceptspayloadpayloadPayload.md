#  [](https://qdrant.tech/documentation/concepts/payload/#payload)Payload
One of the significant features of Qdrant is the ability to store additional information along with vectors. This information is called `payload` in Qdrant terminology.
Qdrant allows you to store any information that can be represented using JSON.
Here is an example of a typical payload:
```
{
    "name": "jacket",
    "colors": ["red", "blue"],
    "count": 10,
    "price": 11.99,
    "locations": [
        {
            "lon": 52.5200,
            "lat": 13.4050
        }
    ],
    "reviews": [
        {
            "user": "alice",
            "score": 4
        },
        {
            "user": "bob",
            "score": 5
        }
    ]
}

```

##  [](https://qdrant.tech/documentation/concepts/payload/#payload-types)Payload types
In addition to storing payloads, Qdrant also allows you search based on certain kinds of values. This feature is implemented as additional filters during the search and will enable you to incorporate custom logic on top of semantic similarity.
During the filtering, Qdrant will check the conditions over those values that match the type of the filtering condition. If the stored value type does not fit the filtering condition - it will be considered not satisfied.
For example, you will get an empty output if you apply the [range condition](https://qdrant.tech/documentation/concepts/filtering/#range) on the string data.
However, arrays (multiple values of the same type) are treated a little bit different. When we apply a filter to an array, it will succeed if at least one of the values inside the array meets the condition.
The filtering process is discussed in detail in the section [Filtering](https://qdrant.tech/documentation/concepts/filtering/).
Let’s look at the data types that Qdrant supports for searching:
###  [](https://qdrant.tech/documentation/concepts/payload/#integer)Integer
`integer` - 64-bit integer in the range from `-9223372036854775808` to `9223372036854775807`.
Example of single and multiple `integer` values:
```
{
    "count": 10,
    "sizes": [35, 36, 38]
}

```

###  [](https://qdrant.tech/documentation/concepts/payload/#float)Float
`float` - 64-bit floating point number.
Example of single and multiple `float` values:
```
{
    "price": 11.99,
    "ratings": [9.1, 9.2, 9.4]
}

```

###  [](https://qdrant.tech/documentation/concepts/payload/#bool)Bool
Bool - binary value. Equals to `true` or `false`.
Example of single and multiple `bool` values:
```
{
    "is_delivered": true,
    "responses": [false, false, true, false]
}

```

###  [](https://qdrant.tech/documentation/concepts/payload/#keyword)Keyword
`keyword` - string value.
Example of single and multiple `keyword` values:
```
{
    "name": "Alice",
    "friends": [
        "bob",
        "eva",
        "jack"
    ]
}

```

###  [](https://qdrant.tech/documentation/concepts/payload/#geo)Geo
`geo` is used to represent geographical coordinates.
Example of single and multiple `geo` values:
```
{
    "location": {
        "lon": 52.5200,
        "lat": 13.4050
    },
    "cities": [
        {
            "lon": 51.5072,
            "lat": 0.1276
        },
        {
            "lon": 40.7128,
            "lat": 74.0060
        }
    ]
}

```

Coordinate should be described as an object containing two fields: `lon` - for longitude, and `lat` - for latitude.
###  [](https://qdrant.tech/documentation/concepts/payload/#datetime)Datetime
_Available as of v1.8.0_
`datetime` - date and time in
See the following examples of single and multiple `datetime` values:
```
{
    "created_at": "2023-02-08T10:49:00Z",
    "updated_at": [
        "2023-02-08T13:52:00Z",
        "2023-02-21T21:23:00Z"
    ]
}

```

The following formats are supported:
  * `"2023-02-08T10:49:00Z"` (
  * `"2023-02-08T11:49:00+01:00"` (
  * `"2023-02-08T10:49:00"` (without timezone, UTC is assumed)
  * `"2023-02-08T10:49"` (without timezone and seconds)
  * `"2023-02-08"` (only date, midnight is assumed)


Notes about the format:
  * `T` can be replaced with a space.
  * The `T` and `Z` symbols are case-insensitive.
  * UTC is always assumed when the timezone is not specified.
  * Timezone can have the following formats: `±HH:MM`, `±HHMM`, `±HH`, or `Z`.
  * Seconds can have up to 6 decimals, so the finest granularity for `datetime` is microseconds.


###  [](https://qdrant.tech/documentation/concepts/payload/#uuid)UUID
_Available as of v1.11.0_
In addition to the basic `keyword` type, Qdrant supports `uuid` type for storing UUID values. Functionally, it works the same as `keyword`, internally stores parsed UUID values.
```
{
    "uuid": "550e8400-e29b-41d4-a716-446655440000",
    "uuids": [
        "550e8400-e29b-41d4-a716-446655440000",
        "550e8400-e29b-41d4-a716-446655440001"
    ]
}

```

String representation of UUID (e.g. `550e8400-e29b-41d4-a716-446655440000`) occupies 36 bytes. But when numeric representation is used, it is only 128 bits (16 bytes).
Usage of `uuid` index type is recommended in payload-heavy collections to save RAM and improve search performance.
##  [](https://qdrant.tech/documentation/concepts/payload/#create-point-with-payload)Create point with payload
REST API ([Schema](https://api.qdrant.tech/api-reference/points/upsert-points))
httppythontypescriptrustjavacsharpgo
```
PUT /collections/{collection_name}/points
{
    "points": [
        {
            "id": 1,
            "vector": [0.05, 0.61, 0.76, 0.74],
            "payload": {"city": "Berlin", "price": 1.99}
        },
        {
            "id": 2,
            "vector": [0.19, 0.81, 0.75, 0.11],
            "payload": {"city": ["Berlin", "London"], "price": 1.99}
        },
        {
            "id": 3,
            "vector": [0.36, 0.55, 0.47, 0.94],
            "payload": {"city": ["Berlin", "Moscow"], "price": [1.99, 2.99]}
        }
    ]
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
            },
        ),
        models.PointStruct(
            id=2,
            vector=[0.19, 0.81, 0.75, 0.11],
            payload={
                "city": ["Berlin", "London"],
                "price": 1.99,
            },
        ),
        models.PointStruct(
            id=3,
            vector=[0.36, 0.55, 0.47, 0.94],
            payload={
                "city": ["Berlin", "Moscow"],
                "price": [1.99, 2.99],
            },
        ),
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
      vector: [0.05, 0.61, 0.76, 0.74],
      payload: {
        city: "Berlin",
        price: 1.99,
      },
    },
    {
      id: 2,
      vector: [0.19, 0.81, 0.75, 0.11],
      payload: {
        city: ["Berlin", "London"],
        price: 1.99,
      },
    },
    {
      id: 3,
      vector: [0.36, 0.55, 0.47, 0.94],
      payload: {
        city: ["Berlin", "Moscow"],
        price: [1.99, 2.99],
      },
    },
  ],
});

```

```
use qdrant_client::qdrant::{PointStruct, UpsertPointsBuilder};
use qdrant_client::{Payload, Qdrant};
use serde_json::json;

let client = Qdrant::from_url("http://localhost:6334").build()?;

let points = vec![
    PointStruct::new(
        1,
        vec![0.05, 0.61, 0.76, 0.74],
        Payload::try_from(json!({"city": "Berlin", "price": 1.99})).unwrap(),
    ),
    PointStruct::new(
        2,
        vec![0.19, 0.81, 0.75, 0.11],
        Payload::try_from(json!({"city": ["Berlin", "London"]})).unwrap(),
    ),
    PointStruct::new(
        3,
        vec![0.36, 0.55, 0.47, 0.94],
        Payload::try_from(json!({"city": ["Berlin", "Moscow"], "price": [1.99, 2.99]}))
            .unwrap(),
    ),
];

client
    .upsert_points(UpsertPointsBuilder::new("{collection_name}", points).wait(true))
    .await?;

```

```
import static io.qdrant.client.PointIdFactory.id;
import static io.qdrant.client.ValueFactory.list;
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
                .setVectors(vectors(0.05f, 0.61f, 0.76f, 0.74f))
                .putAllPayload(Map.of("city", value("Berlin"), "price", value(1.99)))
                .build(),
            PointStruct.newBuilder()
                .setId(id(2))
                .setVectors(vectors(0.19f, 0.81f, 0.75f, 0.11f))
                .putAllPayload(
                    Map.of("city", list(List.of(value("Berlin"), value("London")))))
                .build(),
            PointStruct.newBuilder()
                .setId(id(3))
                .setVectors(vectors(0.36f, 0.55f, 0.47f, 0.94f))
                .putAllPayload(
                    Map.of(
                        "city",
                        list(List.of(value("Berlin"), value("London"))),
                        "price",
                        list(List.of(value(1.99), value(2.99)))))
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
        new PointStruct
        {
            Id = 1,
            Vectors = new[] { 0.05f, 0.61f, 0.76f, 0.74f },
            Payload = { ["city"] = "Berlin", ["price"] = 1.99 }
        },
        new PointStruct
        {
            Id = 2,
            Vectors = new[] { 0.19f, 0.81f, 0.75f, 0.11f },
            Payload = { ["city"] = new[] { "Berlin", "London" } }
        },
        new PointStruct
        {
            Id = 3,
            Vectors = new[] { 0.36f, 0.55f, 0.47f, 0.94f },
            Payload =
            {
                ["city"] = new[] { "Berlin", "Moscow" },
                ["price"] = new Value[] { 1.99, 2.99 }
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
            Id:      qdrant.NewIDNum(1),
            Vectors: qdrant.NewVectors(0.05, 0.61, 0.76, 0.74),
            Payload: qdrant.NewValueMap(map[string]any{
                "city": "Berlin", "price": 1.99}),
        },
        {
            Id:      qdrant.NewIDNum(2),
            Vectors: qdrant.NewVectors(0.19, 0.81, 0.75, 0.11),
            Payload: qdrant.NewValueMap(map[string]any{
                "city": []any{"Berlin", "London"}}),
        },
        {
            Id:      qdrant.NewIDNum(3),
            Vectors: qdrant.NewVectors(0.36, 0.55, 0.47, 0.94),
            Payload: qdrant.NewValueMap(map[string]any{
                "city":  []any{"Berlin", "London"},
                "price": []any{1.99, 2.99}}),
        },
    },
})

```

##  [](https://qdrant.tech/documentation/concepts/payload/#update-payload)Update payload
Updating payloads in Qdrant offers flexible methods to manage vector metadata. The **set payload** method updates specific fields while keeping others unchanged, while the **overwrite** method replaces the entire payload. Developers can also use **clear payload** to remove all metadata or delete fields to remove specific keys without affecting the rest. These options provide precise control for adapting to dynamic datasets.
###  [](https://qdrant.tech/documentation/concepts/payload/#set-payload)Set payload
Set only the given payload values on a point.
REST API ([Schema](https://api.qdrant.tech/api-reference/points/set-payload)):
httppythontypescriptrustjavacsharpgo
```
POST /collections/{collection_name}/points/payload
{
    "payload": {
        "property1": "string",
        "property2": "string"
    },
    "points": [
        0, 3, 100
    ]
}

```

```
client.set_payload(
    collection_name="{collection_name}",
    payload={
        "property1": "string",
        "property2": "string",
    },
    points=[0, 3, 10],
)

```

```
client.setPayload("{collection_name}", {
  payload: {
    property1: "string",
    property2: "string",
  },
  points: [0, 3, 10],
});

```

```
use qdrant_client::qdrant::{
    PointsIdsList, SetPayloadPointsBuilder,
};
use qdrant_client::Payload;
use serde_json::json;

client
    .set_payload(
        SetPayloadPointsBuilder::new(
            "{collection_name}",
            Payload::try_from(json!({
                "property1": "string",
                "property2": "string",
            }))
            .unwrap(),
        )
        .points_selector(PointsIdsList {
            ids: vec![0.into(), 3.into(), 10.into()],
        })
        .wait(true),
    )
    .await?;

```

```
import static io.qdrant.client.PointIdFactory.id;
import static io.qdrant.client.ValueFactory.value;

import java.util.List;
import java.util.Map;

client
    .setPayloadAsync(
        "{collection_name}",
        Map.of("property1", value("string"), "property2", value("string")),
        List.of(id(0), id(3), id(10)),
        true,
        null,
        null)
    .get();

```

```
using Qdrant.Client;
using Qdrant.Client.Grpc;

var client = new QdrantClient("localhost", 6334);

await client.SetPayloadAsync(
    collectionName: "{collection_name}",
    payload: new Dictionary<string, Value> { { "property1", "string" }, { "property2", "string" } },
    ids: new ulong[] { 0, 3, 10 }
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

client.SetPayload(context.Background(), &qdrant.SetPayloadPoints{
    CollectionName: "{collection_name}",
    Payload: qdrant.NewValueMap(
        map[string]any{"property1": "string", "property2": "string"}),
    PointsSelector: qdrant.NewPointsSelector(
        qdrant.NewIDNum(0),
        qdrant.NewIDNum(3)),
})

```

You don’t need to know the ids of the points you want to modify. The alternative is to use filters.
httppythontypescriptrustjavacsharpgo
```
POST /collections/{collection_name}/points/payload
{
    "payload": {
        "property1": "string",
        "property2": "string"
    },
    "filter": {
        "must": [
            {
                "key": "color",
                "match": {
                    "value": "red"
                }
            }
        ]
    }
}

```

```
client.set_payload(
    collection_name="{collection_name}",
    payload={
        "property1": "string",
        "property2": "string",
    },
    points=models.Filter(
        must=[
            models.FieldCondition(
                key="color",
                match=models.MatchValue(value="red"),
            ),
        ],
    ),
)

```

```
client.setPayload("{collection_name}", {
  payload: {
    property1: "string",
    property2: "string",
  },
  filter: {
    must: [
      {
        key: "color",
        match: {
          value: "red",
        },
      },
    ],
  },
});

```

```
use qdrant_client::qdrant::{Condition, Filter, SetPayloadPointsBuilder};
use qdrant_client::Payload;
use serde_json::json;

client
    .set_payload(
        SetPayloadPointsBuilder::new(
            "{collection_name}",
            Payload::try_from(json!({
                "property1": "string",
                "property2": "string",
            }))
            .unwrap(),
        )
        .points_selector(Filter::must([Condition::matches(
            "color",
            "red".to_string(),
        )]))
        .wait(true),
    )
    .await?;

```

```
import static io.qdrant.client.ConditionFactory.matchKeyword;
import static io.qdrant.client.ValueFactory.value;

import io.qdrant.client.grpc.Common.Filter;
import java.util.Map;

client
    .setPayloadAsync(
        "{collection_name}",
        Map.of("property1", value("string"), "property2", value("string")),
        Filter.newBuilder().addMust(matchKeyword("color", "red")).build(),
        true,
        null,
        null)
    .get();

```

```
using Qdrant.Client;
using Qdrant.Client.Grpc;
using static Qdrant.Client.Grpc.Conditions;

var client = new QdrantClient("localhost", 6334);

await client.SetPayloadAsync(
    collectionName: "{collection_name}",
    payload: new Dictionary<string, Value> { { "property1", "string" }, { "property2", "string" } },
    filter: MatchKeyword("color", "red")
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

client.SetPayload(context.Background(), &qdrant.SetPayloadPoints{
    CollectionName: "{collection_name}",
    Payload: qdrant.NewValueMap(
        map[string]any{"property1": "string", "property2": "string"}),
    PointsSelector: qdrant.NewPointsSelectorFilter(&qdrant.Filter{
        Must: []*qdrant.Condition{
            qdrant.NewMatch("color", "red"),
        },
    }),
})

```

_Available as of v1.8.0_
It is possible to modify only a specific key of the payload by using the `key` parameter.
For instance, given the following payload JSON object on a point:
```
{
    "property1": {
        "nested_property": "foo",
    },
    "property2": {
        "nested_property": "bar",
    }
}

```

You can modify the `nested_property` of `property1` with the following request:
```
POST /collections/{collection_name}/points/payload
{
    "payload": {
        "nested_property": "qux",
    },
    "key": "property1",
    "points": [1]
}

```

Resulting in the following payload:
```
{
    "property1": {
        "nested_property": "qux",
    },
    "property2": {
        "nested_property": "bar",
    }
}

```

###  [](https://qdrant.tech/documentation/concepts/payload/#overwrite-payload)Overwrite payload
Fully replace any existing payload with the given one.
REST API ([Schema](https://api.qdrant.tech/api-reference/points/overwrite-payload)):
httppythontypescriptrustjavacsharpgo
```
PUT /collections/{collection_name}/points/payload
{
    "payload": {
        "property1": "string",
        "property2": "string"
    },
    "points": [
        0, 3, 100
    ]
}

```

```
client.overwrite_payload(
    collection_name="{collection_name}",
    payload={
        "property1": "string",
        "property2": "string",
    },
    points=[0, 3, 10],
)

```

```
client.overwritePayload("{collection_name}", {
  payload: {
    property1: "string",
    property2: "string",
  },
  points: [0, 3, 10],
});

```

```
use qdrant_client::qdrant::{PointsIdsList, SetPayloadPointsBuilder};
use qdrant_client::Payload;
use serde_json::json;

client
    .overwrite_payload(
        SetPayloadPointsBuilder::new(
            "{collection_name}",
            Payload::try_from(json!({
                "property1": "string",
                "property2": "string",
            }))
            .unwrap(),
        )
        .points_selector(PointsIdsList {
            ids: vec![0.into(), 3.into(), 10.into()],
        })
        .wait(true),
    )
    .await?;

```

```
import static io.qdrant.client.PointIdFactory.id;
import static io.qdrant.client.ValueFactory.value;

import java.util.List;
import java.util.Map;

client
    .overwritePayloadAsync(
        "{collection_name}",
        Map.of("property1", value("string"), "property2", value("string")),
        List.of(id(0), id(3), id(10)),
        true,
        null,
        null)
    .get();

```

```
using Qdrant.Client;
using Qdrant.Client.Grpc;

var client = new QdrantClient("localhost", 6334);

await client.OverwritePayloadAsync(
    collectionName: "{collection_name}",
    payload: new Dictionary<string, Value> { { "property1", "string" }, { "property2", "string" } },
    ids: new ulong[] { 0, 3, 10 }
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

client.OverwritePayload(context.Background(), &qdrant.SetPayloadPoints{
    CollectionName: "{collection_name}",
    Payload: qdrant.NewValueMap(
        map[string]any{"property1": "string", "property2": "string"}),
    PointsSelector: qdrant.NewPointsSelector(
        qdrant.NewIDNum(0),
        qdrant.NewIDNum(3)),
})

```

Like [set payload](https://qdrant.tech/documentation/concepts/payload/#set-payload), you don’t need to know the ids of the points you want to modify. The alternative is to use filters.
###  [](https://qdrant.tech/documentation/concepts/payload/#clear-payload)Clear payload
This method removes all payload keys from specified points
REST API ([Schema](https://api.qdrant.tech/api-reference/points/clear-payload)):
httppythontypescriptrustjavacsharpgo
```
POST /collections/{collection_name}/points/payload/clear
{
    "points": [0, 3, 100]
}

```

```
client.clear_payload(
    collection_name="{collection_name}",
    points_selector=[0, 3, 100],
)

```

```
client.clearPayload("{collection_name}", {
  points: [0, 3, 100],
});

```

```
use qdrant_client::qdrant::{ClearPayloadPointsBuilder, PointsIdsList};

client
    .clear_payload(
        ClearPayloadPointsBuilder::new("{collection_name}")
            .points(PointsIdsList {
                ids: vec![0.into(), 3.into(), 10.into()],
            })
            .wait(true),
    )
    .await?;

```

```
import static io.qdrant.client.PointIdFactory.id;

import java.util.List;

client
    .clearPayloadAsync("{collection_name}", List.of(id(0), id(3), id(100)), true, null, null)
    .get();

```

```
using Qdrant.Client;

var client = new QdrantClient("localhost", 6334);

await client.ClearPayloadAsync(collectionName: "{collection_name}", ids: new ulong[] { 0, 3, 100 });

```

```
import (
    "context"

    "github.com/qdrant/go-client/qdrant"
)

client.ClearPayload(context.Background(), &qdrant.ClearPayloadPoints{
    CollectionName: "{collection_name}",
    Points: qdrant.NewPointsSelector(
        qdrant.NewIDNum(0),
        qdrant.NewIDNum(3)),
})

```

You can also use `models.FilterSelector` to remove the points matching given filter criteria, instead of providing the ids.
###  [](https://qdrant.tech/documentation/concepts/payload/#delete-payload-keys)Delete payload keys
Delete specific payload keys from points.
REST API ([Schema](https://api.qdrant.tech/api-reference/points/delete-payload)):
httppythontypescriptrustjavacsharpgo
```
POST /collections/{collection_name}/points/payload/delete
{
    "keys": ["color", "price"],
    "points": [0, 3, 100]
}

```

```
client.delete_payload(
    collection_name="{collection_name}",
    keys=["color", "price"],
    points=[0, 3, 100],
)

```

```
client.deletePayload("{collection_name}", {
  keys: ["color", "price"],
  points: [0, 3, 100],
});

```

```
use qdrant_client::qdrant::{DeletePayloadPointsBuilder, PointsIdsList};

client
    .delete_payload(
        DeletePayloadPointsBuilder::new(
            "{collection_name}",
            vec!["color".to_string(), "price".to_string()],
        )
        .points_selector(PointsIdsList {
            ids: vec![0.into(), 3.into(), 10.into()],
        })
        .wait(true),
    )
    .await?;

```

```
import static io.qdrant.client.PointIdFactory.id;

import java.util.List;

client
    .deletePayloadAsync(
        "{collection_name}",
        List.of("color", "price"),
        List.of(id(0), id(3), id(100)),
        true,
        null,
        null)
    .get();

```

```
using Qdrant.Client;

var client = new QdrantClient("localhost", 6334);

await client.DeletePayloadAsync(
    collectionName: "{collection_name}",
    keys: ["color", "price"],
    ids: new ulong[] { 0, 3, 100 }
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

client.DeletePayload(context.Background(), &qdrant.DeletePayloadPoints{
    CollectionName: "{collection_name}",
    Keys:           []string{"color", "price"},
    PointsSelector: qdrant.NewPointsSelector(
        qdrant.NewIDNum(0),
        qdrant.NewIDNum(3)),
})

```

Alternatively, you can use filters to delete payload keys from the points.
httppythontypescriptrustjavacsharpgo
```
POST /collections/{collection_name}/points/payload/delete
{
    "keys": ["color", "price"],
    "filter": {
        "must": [
            {
                "key": "color",
                "match": {
                    "value": "red"
                }
            }
        ]
    }
}

```

```
client.delete_payload(
    collection_name="{collection_name}",
    keys=["color", "price"],
    points=models.Filter(
        must=[
            models.FieldCondition(
                key="color",
                match=models.MatchValue(value="red"),
            ),
        ],
    ),
)

```

```
client.deletePayload("{collection_name}", {
  keys: ["color", "price"],
  filter: {
    must: [
      {
        key: "color",
        match: {
          value: "red",
        },
      },
    ],
  },
});

```

```
use qdrant_client::qdrant::{Condition, DeletePayloadPointsBuilder, Filter};

client
    .delete_payload(
        DeletePayloadPointsBuilder::new(
            "{collection_name}",
            vec!["color".to_string(), "price".to_string()],
        )
        .points_selector(Filter::must([Condition::matches(
            "color",
            "red".to_string(),
        )]))
        .wait(true),
    )
    .await?;

```

```
import static io.qdrant.client.ConditionFactory.matchKeyword;

import io.qdrant.client.grpc.Common.Filter;
import java.util.List;

client
    .deletePayloadAsync(
        "{collection_name}",
        List.of("color", "price"),
        Filter.newBuilder().addMust(matchKeyword("color", "red")).build(),
        true,
        null,
        null)
    .get();

```

```
using Qdrant.Client;
using static Qdrant.Client.Grpc.Conditions;

var client = new QdrantClient("localhost", 6334);

await client.DeletePayloadAsync(
    collectionName: "{collection_name}",
    keys: ["color", "price"],
    filter: MatchKeyword("color", "red")
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

client.DeletePayload(context.Background(), &qdrant.DeletePayloadPoints{
    CollectionName: "{collection_name}",
    Keys:           []string{"color", "price"},
    PointsSelector: qdrant.NewPointsSelectorFilter(
        &qdrant.Filter{
            Must: []*qdrant.Condition{qdrant.NewMatch("color", "red")},
        },
    ),
})

```

##  [](https://qdrant.tech/documentation/concepts/payload/#payload-indexing)Payload indexing
To search more efficiently with filters, Qdrant allows you to create indexes for payload fields by specifying the name and type of field it is intended to be.
The indexed fields also affect the vector index. See [Indexing](https://qdrant.tech/documentation/concepts/indexing/) for details.
In practice, we recommend creating an index on those fields that could potentially constrain the results the most. For example, using an index for the object ID will be much more efficient, being unique for each record, than an index by its color, which has only a few possible values.
In compound queries involving multiple fields, Qdrant will attempt to use the most restrictive index first.
To create index for the field, you can use the following:
REST API ([Schema](https://api.qdrant.tech/api-reference/indexes/create-field-index))
httppythontypescriptrustjavacsharpgo
```
PUT /collections/{collection_name}/index
{
    "field_name": "name_of_the_field_to_index",
    "field_schema": "keyword"
}

```

```
client.create_payload_index(
    collection_name="{collection_name}",
    field_name="name_of_the_field_to_index",
    field_schema=models.PayloadSchemaType.KEYWORD,
)

```

```
client.createPayloadIndex("{collection_name}", {
  field_name: "name_of_the_field_to_index",
  field_schema: "keyword",
});

```

```
use qdrant_client::qdrant::{CreateFieldIndexCollectionBuilder, FieldType};

client
    .create_field_index(
        CreateFieldIndexCollectionBuilder::new(
            "{collection_name}",
            "name_of_the_field_to_index",
            FieldType::Keyword,
        )
        .wait(true),
    )
    .await?;

```

```
import io.qdrant.client.grpc.Collections.PayloadSchemaType;

client.createPayloadIndexAsync(
    "{collection_name}",
    "name_of_the_field_to_index",
    PayloadSchemaType.Keyword,
    null,
    true,
    null,
    null);

```

```
using Qdrant.Client;

var client = new QdrantClient("localhost", 6334);

await client.CreatePayloadIndexAsync(
    collectionName: "{collection_name}",
    fieldName: "name_of_the_field_to_index"
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
})

```

The index usage flag is displayed in the payload schema with the [collection info API](https://api.qdrant.tech/api-reference/collections/get-collection).
Payload schema example:
```
{
    "payload_schema": {
        "property1": {
            "data_type": "keyword"
        },
        "property2": {
            "data_type": "integer"
        }
    }
}

```

##  [](https://qdrant.tech/documentation/concepts/payload/#facet-counts)Facet counts
_Available as of v1.12.0_
Faceting is a special counting technique that can be used for various purposes:
  * Know which unique values exist for a payload key.
  * Know the number of points that contain each unique value.
  * Know how restrictive a filter would become by matching a specific value.


Specifically, it is a counting aggregation for the values in a field, akin to a `GROUP BY` with `COUNT(*)` commands in SQL.
These results for a specific field is called a “facet”. For example, when you look at an e-commerce search results page, you might see a list of brands on the sidebar, showing the number of products for each brand. This would be a facet for a `"brand"` field.
In Qdrant you can facet on a field **only** if you have created a field index that supports `MatchValue` conditions for it, like a `keyword` index.
To get the facet counts for a field, you can use the following:
By default, the number of `hits` returned is limited to 10. To change this, use the `limit` parameter. Keep this in mind when checking the number of unique values a payload field contains.
REST API ([Facet](https://api.qdrant.tech/v-1-13-x/api-reference/points/facet))
httppythontypescriptrustjavacsharpgo
```
POST /collections/{collection_name}/facet
{
    "key": "size",
    "filter": {
      "must": {
        "key": "color",
        "match": { "value": "red" }
      }
    }
}

```

```
from qdrant_client import QdrantClient, models

client = QdrantClient(url="http://localhost:6333")

client.facet(
    collection_name="{collection_name}",
    key="size",
    facet_filter=models.Filter(
        must=[
            models.FieldCondition(
                key="color",
                match=models.MatchValue(value="red"),
            )
        ]
    ),
)

```

```
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.facet("{collection_name}", {
    filter: {
        must: [
            {
                key: "color",
                match: {
                    value: "red",
                },
            },
        ],
    },
    key: "size",
});

```

```
use qdrant_client::qdrant::{Condition, FacetCountsBuilder, Filter};
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

client
    .facet(
         FacetCountsBuilder::new("{collection_name}", "size")
             .limit(10)
             .filter(Filter::must(vec![Condition::matches(
                 "color",
                 "red".to_string(),
             )])),
     )
     .await?;

```

```
import static io.qdrant.client.ConditionFactory.matchKeyword;

import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Common.Filter;
import io.qdrant.client.grpc.Points;

QdrantClient client = new QdrantClient(
                QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client
    .facetAsync(
        Points.FacetCounts.newBuilder()
            .setCollectionName("{collection_name}")
            .setKey("size")
            .setFilter(Filter.newBuilder().addMust(matchKeyword("color", "red")).build())
            .build())
        .get();

```

```
using Qdrant.Client;
using static Qdrant.Client.Grpc.Conditions;

var client = new QdrantClient("localhost", 6334);

await client.FacetAsync(
    "{collection_name}",
    key: "size",
    filter: MatchKeyword("color", "red")
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

res, err := client.Facet(context.Background(), &qdrant.FacetCounts{
    CollectionName: "{collection_name}",
    Key:            "size",
        Filter: &qdrant.Filter{
        Must: []*qdrant.Condition{
            qdrant.NewMatch("color", "red"),
        },
    },
})

```

The response will contain the counts for each unique value in the field:
```
{
  "response": {
    "hits": [
      {"value": "L", "count": 19},
      {"value": "S", "count": 10},
      {"value": "M", "count": 5},
      {"value": "XL", "count": 1},
      {"value": "XXL", "count": 1}
    ]
  },
  "time": 0.0001
}

```

The results are sorted by the count in descending order, then by the value in ascending order. Only values with non-zero counts will be returned.
By default, the way Qdrant the counts for each value is approximate to achieve fast results. This should accurate enough for most cases, but if you need to debug your storage, you can use the `exact` parameter to get exact counts.
httppythontypescriptrustjavacsharpgo
```
POST /collections/{collection_name}/facet
{
    "key": "size",
    "exact": true
}

```

```
client.facet(
    collection_name="{collection_name}",
    key="size",
    exact=True,
)

```

```
client.facet("{collection_name}", {
    key: "size",
    exact: true,
});

```

```
use qdrant_client::qdrant::FacetCountsBuilder;

client
    .facet(
         FacetCountsBuilder::new("{collection_name}", "size")
             .limit(10)
             .exact(true),
     )
     .await?;

```

```
import io.qdrant.client.grpc.Points.FacetCounts;

client
      .facetAsync(
          FacetCounts.newBuilder()
              .setCollectionName("{collection_name}")
              .setKey("foo")
              .setExact(true)
              .build())
      .get();

```

```
using Qdrant.Client;
using Qdrant.Client.Grpc;

await client.FacetAsync(
    "{collection_name}",
    key: "size",
    exact: true
);

```

```
res, err := client.Facet(context.Background(), &qdrant.FacetCounts{
    CollectionName: "{collection_name}",
    Key:            "key",
    Exact:          qdrant.PtrOf(true),
})

```

##### Was this page useful?
![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg) Yes  ![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg) No
Thank you for your feedback! 🙏
We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/concepts/payload.md) this page on GitHub, or
On this page:
  * [Payload](https://qdrant.tech/documentation/concepts/payload/#payload)
    * [Payload types](https://qdrant.tech/documentation/concepts/payload/#payload-types)
      * [Integer](https://qdrant.tech/documentation/concepts/payload/#integer)
      * [Float](https://qdrant.tech/documentation/concepts/payload/#float)
      * [Bool](https://qdrant.tech/documentation/concepts/payload/#bool)
      * [Keyword](https://qdrant.tech/documentation/concepts/payload/#keyword)
      * [Geo](https://qdrant.tech/documentation/concepts/payload/#geo)
      * [Datetime](https://qdrant.tech/documentation/concepts/payload/#datetime)
      * [UUID](https://qdrant.tech/documentation/concepts/payload/#uuid)
    * [Create point with payload](https://qdrant.tech/documentation/concepts/payload/#create-point-with-payload)
    * [Update payload](https://qdrant.tech/documentation/concepts/payload/#update-payload)
      * [Set payload](https://qdrant.tech/documentation/concepts/payload/#set-payload)
      * [Overwrite payload](https://qdrant.tech/documentation/concepts/payload/#overwrite-payload)
      * [Clear payload](https://qdrant.tech/documentation/concepts/payload/#clear-payload)
      * [Delete payload keys](https://qdrant.tech/documentation/concepts/payload/#delete-payload-keys)
    * [Payload indexing](https://qdrant.tech/documentation/concepts/payload/#payload-indexing)
    * [Facet counts](https://qdrant.tech/documentation/concepts/payload/#facet-counts)


#### Ready to get started with Qdrant?
© 2025 Qdrant.
[Terms](https://qdrant.tech/legal/terms_and_conditions/) [Privacy Policy](https://qdrant.tech/legal/privacy-policy/) [Impressum](https://qdrant.tech/legal/impressum/)
×
[ Powered by ](https://qdrant.tech/)
## About cookies on this site
We use cookies to collect and analyze information on site performance and usage, to provide social media features, and to enhance and customize content and advertisements. [Learn more](https://qdrant.tech/legal/privacy-policy/#cookies-and-web-beacons)
Cookies Settings Accept All Cookies
![Company Logo](https://cdn.cookielaw.org/logos/static/ot_company_logo.png)
## Privacy Preference Center
Cookies used on the site are categorized, and below, you can read about each category and allow or deny some or all of them. When categories that have been previously allowed are disabled, all cookies assigned to that category will be removed from your browser. Additionally, you can see a list of cookies assigned to each category and detailed information in the cookie declaration.
[More information](https://qdrant.tech/legal/privacy-policy/#cookies-and-web-beacons)
Allow All
###  Manage Consent Preferences
#### Targeting Cookies
Targeting Cookies
These cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant adverts on other sites. They do not store directly personal information, but are based on uniquely identifying your browser and internet device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Functional Cookies
These cookies enable the website to provide enhanced functionality and personalisation. They may be set by us or by third party providers whose services we have added to our pages. If you do not allow these cookies then some or all of these services may not function properly.
#### Strictly Necessary Cookies
Always Active
These cookies are necessary for the website to function and cannot be switched off in our systems. They are usually only set in response to actions made by you which amount to a request for services, such as setting your privacy preferences, logging in or filling in forms. You can set your browser to block or alert you about these cookies, but some parts of the site will not then work. These cookies do not store any personally identifiable information.
#### Performance Cookies
Performance Cookies
These cookies allow us to count visits and traffic sources so we can measure and improve the performance of our site. They help us to know which pages are the most and least popular and see how visitors move around the site. All information these cookies collect is aggregated and therefore anonymous. If you do not allow these cookies we will not know when you have visited our site, and will not be able to monitor its performance.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Reject All Confirm My Choices
