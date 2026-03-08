##  [](https://qdrant.tech/documentation/concepts/points/#counting-points)Counting points
_Available as of v0.8.4_
Sometimes it can be useful to know how many points fit the filter conditions without doing a real search.
Among others, for example, we can highlight the following scenarios:
  * Evaluation of results size for faceted search
  * Determining the number of pages for pagination
  * Debugging the query execution speed


REST API ([Schema](https://api.qdrant.tech/master/api-reference/points/count-points)):
httppythontypescriptrustjavacsharpgo
```
POST /collections/{collection_name}/points/count
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
    "exact": true
}

```

```
client.count(
    collection_name="{collection_name}",
    count_filter=models.Filter(
        must=[
            models.FieldCondition(key="color", match=models.MatchValue(value="red")),
        ]
    ),
    exact=True,
)

```

```
client.count("{collection_name}", {
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
  exact: true,
});

```

```
use qdrant_client::qdrant::{Condition, CountPointsBuilder, Filter};

client
    .count(
        CountPointsBuilder::new("{collection_name}")
            .filter(Filter::must([Condition::matches(
                "color",
                "red".to_string(),
            )]))
            .exact(true),
    )
    .await?;

```

```
import static io.qdrant.client.ConditionFactory.matchKeyword;

import io.qdrant.client.grpc.Common.Filter;

client
    .countAsync(
        "{collection_name}",
        Filter.newBuilder().addMust(matchKeyword("color", "red")).build(),
        true)
    .get();

```

```
using Qdrant.Client;
using static Qdrant.Client.Grpc.Conditions;

var client = new QdrantClient("localhost", 6334);

await client.CountAsync(
	collectionName: "{collection_name}",
	filter: MatchKeyword("color", "red"),
	exact: true
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

client.Count(context.Background(), &qdrant.CountPoints{
	CollectionName: "midlib",
	Filter: &qdrant.Filter{
		Must: []*qdrant.Condition{
			qdrant.NewMatch("color", "red"),
		},
	},
})

```

Returns number of counts matching given filtering conditions:
```
{
  "count": 3811
}

```
