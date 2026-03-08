##  [](https://qdrant.tech/documentation/concepts/points/#scroll-points)Scroll points
Sometimes it might be necessary to get all stored points without knowing ids, or iterate over points that correspond to a filter.
REST API ([Schema](https://api.qdrant.tech/master/api-reference/points/scroll-points)):
httppythontypescriptrustjavacsharpgo
```
POST /collections/{collection_name}/points/scroll
{
    "filter": {
        "must": [
            {
                "key": "color",
                "match": {
                    "value": "red"
                }
            }
        ]
    },
    "limit": 1,
    "with_payload": true,
    "with_vector": false
}

```

```
client.scroll(
    collection_name="{collection_name}",
    scroll_filter=models.Filter(
        must=[
            models.FieldCondition(key="color", match=models.MatchValue(value="red")),
        ]
    ),
    limit=1,
    with_payload=True,
    with_vectors=False,
)

```

```
client.scroll("{collection_name}", {
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
  limit: 1,
  with_payload: true,
  with_vector: false,
});

```

```
use qdrant_client::qdrant::{Condition, Filter, ScrollPointsBuilder};

client
    .scroll(
        ScrollPointsBuilder::new("{collection_name}")
            .filter(Filter::must([Condition::matches(
                "color",
                "red".to_string(),
            )]))
            .limit(1)
            .with_payload(true)
            .with_vectors(false),
    )
    .await?;

```

```
import static io.qdrant.client.ConditionFactory.matchKeyword;
import static io.qdrant.client.WithPayloadSelectorFactory.enable;

import io.qdrant.client.grpc.Common.Filter;
import io.qdrant.client.grpc.Points.ScrollPoints;

client
    .scrollAsync(
        ScrollPoints.newBuilder()
            .setCollectionName("{collection_name}")
            .setFilter(Filter.newBuilder().addMust(matchKeyword("color", "red")).build())
            .setLimit(1)
            .setWithPayload(enable(true))
            .build())
    .get();

```

```
using Qdrant.Client;
using static Qdrant.Client.Grpc.Conditions;

var client = new QdrantClient("localhost", 6334);

await client.ScrollAsync(
	collectionName: "{collection_name}",
	filter: MatchKeyword("color", "red"),
	limit: 1,
	payloadSelector: true
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

client.Scroll(context.Background(), &qdrant.ScrollPoints{
	CollectionName: "{collection_name}",
	Filter: &qdrant.Filter{
		Must: []*qdrant.Condition{
			qdrant.NewMatch("color", "red"),
		},
	},
	Limit:       qdrant.PtrOf(uint32(1)),
	WithPayload: qdrant.NewWithPayload(true),
})

```

Returns all point with `color` = `red`.
```
{
  "result": {
    "next_page_offset": 1,
    "points": [
      {
        "id": 0,
        "payload": {
          "color": "red"
        }
      }
    ]
  },
  "status": "ok",
  "time": 0.0001
}

```

The Scroll API will return all points that match the filter in a page-by-page manner.
All resulting points are sorted by ID. To query the next page it is necessary to specify the largest seen ID in the `offset` field. For convenience, this ID is also returned in the field `next_page_offset`. If the value of the `next_page_offset` field is `null` - the last page is reached.
###  [](https://qdrant.tech/documentation/concepts/points/#order-points-by-payload-key)Order points by payload key
_Available as of v1.8.0_
When using the [`scroll`](https://qdrant.tech/documentation/concepts/points/#scroll-points) API, you can sort the results by payload key. For example, you can retrieve points in chronological order if your payloads have a `"timestamp"` field, as is shown from the example below:
Without an appropriate index, payload-based ordering would create too much load on the system for each request. Qdrant therefore requires a payload index which supports [Range filtering conditions](https://qdrant.tech/documentation/concepts/indexing/#payload-index) on the field used for `order_by`
httppythontypescriptrustjavacsharpgo
```
POST /collections/{collection_name}/points/scroll
{
    "limit": 15,
    "order_by": "timestamp", // <-- this!
}

```

```
client.scroll(
    collection_name="{collection_name}",
    limit=15,
    order_by="timestamp", # <-- this!
)

```

```
client.scroll("{collection_name}", {
  limit: 15,
  order_by: "timestamp", // <-- this!
});

```

```
use qdrant_client::qdrant::{OrderByBuilder, ScrollPointsBuilder};

client
    .scroll(
        ScrollPointsBuilder::new("{collection_name}")
            .limit(15)
            .order_by(OrderByBuilder::new("timestamp")),
    )
    .await?;

```

```
import io.qdrant.client.grpc.Points.OrderBy;
import io.qdrant.client.grpc.Points.ScrollPoints;

client.scrollAsync(ScrollPoints.newBuilder()
  .setCollectionName("{collection_name}")
  .setLimit(15)
  .setOrderBy(OrderBy.newBuilder().setKey("timestamp").build())
  .build()).get();

```

```
await client.ScrollAsync("{collection_name}", limit: 15, orderBy: "timestamp");

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

client.Scroll(context.Background(), &qdrant.ScrollPoints{
	CollectionName: "{collection_name}",
	Limit:          qdrant.PtrOf(uint32(15)),
	OrderBy: &qdrant.OrderBy{
		Key: "timestamp",
	},
})

```

You need to use the `order_by` `key` parameter to specify the payload key. Then you can add other fields to control the ordering, such as `direction` and `start_from`:
httppythontypescriptrustjavacsharpgo
```
"order_by": {
    "key": "timestamp",
    "direction": "desc" // default is "asc"
    "start_from": 123, // start from this value
}

```

```
order_by=models.OrderBy(
    key="timestamp",
    direction=models.Direction.DESC,  # default is "ASC"
    start_from=123,  # start from this value
)

```

```
order_by: {
    key: "timestamp",
    direction: "desc", // default is "asc"
    start_from: 123, // start from this value
}

```

```
use qdrant_client::qdrant::{start_from::Value, Direction, OrderByBuilder};

OrderByBuilder::new("timestamp")
    .direction(Direction::Desc.into())
    .start_from(Value::Integer(123))
    .build();

```

```
import io.qdrant.client.grpc.Points.Direction;
import io.qdrant.client.grpc.Points.OrderBy;
import io.qdrant.client.grpc.Points.StartFrom;

OrderBy.newBuilder()
  .setKey("timestamp")
  .setDirection(Direction.Desc)
  .setStartFrom(StartFrom.newBuilder()
    .setInteger(123)
    .build())
  .build();

```

```
using Qdrant.Client.Grpc;

new OrderBy
{
 Key = "timestamp",
 Direction = Direction.Desc,
 StartFrom = 123
};

```

```
import "github.com/qdrant/go-client/qdrant"

qdrant.OrderBy{
	Key:       "timestamp",
	Direction: qdrant.Direction_Desc.Enum(),
	StartFrom: qdrant.NewStartFromInt(123),
}

```

When you use the `order_by` parameter, pagination is disabled.
When sorting is based on a non-unique value, it is not possible to rely on an ID offset. Thus, next_page_offset is not returned within the response. However, you can still do pagination by combining `"order_by": { "start_from": ... }` with a `{ "must_not": [{ "has_id": [...] }] }` filter.
