##  [](https://qdrant.tech/documentation/concepts/points/#delete-points)Delete points
REST API ([Schema](https://api.qdrant.tech/api-reference/points/delete-points)):
httppythontypescriptrustjavacsharpgo
```
POST /collections/{collection_name}/points/delete
{
    "points": [0, 3, 100]
}

```

```
client.delete(
    collection_name="{collection_name}",
    points_selector=models.PointIdsList(
        points=[0, 3, 100],
    ),
)

```

```
client.delete("{collection_name}", {
  points: [0, 3, 100],
});

```

```
use qdrant_client::qdrant::{DeletePointsBuilder, PointsIdsList};

client
    .delete_points(
        DeletePointsBuilder::new("{collection_name}")
            .points(PointsIdsList {
                ids: vec![0.into(), 3.into(), 100.into()],
            })
            .wait(true),
    )
    .await?;

```

```
import static io.qdrant.client.PointIdFactory.id;

import java.util.List;

client.deleteAsync("{collection_name}", List.of(id(0), id(3), id(100)));

```

```
using Qdrant.Client;

var client = new QdrantClient("localhost", 6334);

await client.DeleteAsync(collectionName: "{collection_name}", ids: (ulong[])[0, 3, 100]);

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

client.Delete(context.Background(), &qdrant.DeletePoints{
	CollectionName: "{collection_name}",
	Points: qdrant.NewPointsSelector(
		qdrant.NewIDNum(0), qdrant.NewIDNum(3), qdrant.NewIDNum(100),
	),
})

```

Alternative way to specify which points to remove is to use filter.
httppythontypescriptrustjavacsharpgo
```
POST /collections/{collection_name}/points/delete
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
    }
}

```

```
client.delete(
    collection_name="{collection_name}",
    points_selector=models.FilterSelector(
        filter=models.Filter(
            must=[
                models.FieldCondition(
                    key="color",
                    match=models.MatchValue(value="red"),
                ),
            ],
        )
    ),
)

```

```
client.delete("{collection_name}", {
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
use qdrant_client::qdrant::{Condition, DeletePointsBuilder, Filter};

client
    .delete_points(
        DeletePointsBuilder::new("{collection_name}")
            .points(Filter::must([Condition::matches(
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

client
    .deleteAsync(
        "{collection_name}",
        Filter.newBuilder().addMust(matchKeyword("color", "red")).build())
    .get();

```

```
using Qdrant.Client;
using static Qdrant.Client.Grpc.Conditions;

var client = new QdrantClient("localhost", 6334);

await client.DeleteAsync(collectionName: "{collection_name}", filter: MatchKeyword("color", "red"));

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

client.Delete(context.Background(), &qdrant.DeletePoints{
	CollectionName: "{collection_name}",
	Points: qdrant.NewPointsSelectorFilter(
		&qdrant.Filter{
			Must: []*qdrant.Condition{
				qdrant.NewMatch("color", "red"),
			},
		},
	),
})

```

This example removes all points with `{ "color": "red" }` from the collection.
