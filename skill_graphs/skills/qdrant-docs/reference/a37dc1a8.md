##  [](https://qdrant.tech/documentation/concepts/points/#retrieve-points)Retrieve points
There is a method for retrieving points by their ids.
REST API ([Schema](https://api.qdrant.tech/api-reference/points/get-points)):
httppythontypescriptrustjavacsharpgo
```
POST /collections/{collection_name}/points
{
    "ids": [0, 3, 100]
}

```

```
client.retrieve(
    collection_name="{collection_name}",
    ids=[0, 3, 100],
)

```

```
client.retrieve("{collection_name}", {
  ids: [0, 3, 100],
});

```

```
use qdrant_client::qdrant::GetPointsBuilder;

client
    .get_points(GetPointsBuilder::new(
        "{collection_name}",
        vec![0.into(), 30.into(), 100.into()],
    ))
    .await?;

```

```
import static io.qdrant.client.PointIdFactory.id;

import java.util.List;

client
    .retrieveAsync("{collection_name}", List.of(id(0), id(30), id(100)), false, false, null)
    .get();

```

```
using Qdrant.Client;

var client = new QdrantClient("localhost", 6334);

await client.RetrieveAsync(
	collectionName: "{collection_name}",
	ids: [0, 30, 100],
	withPayload: false,
	withVectors: false
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

client.Get(context.Background(), &qdrant.GetPoints{
	CollectionName: "{collection_name}",
	Ids: []*qdrant.PointId{
		qdrant.NewIDNum(0), qdrant.NewIDNum(3), qdrant.NewIDNum(100),
	},
})

```

This method has additional parameters `with_vectors` and `with_payload`. Using these parameters, you can select parts of the point you want as a result. Excluding helps you not to waste traffic transmitting useless data.
The single point can also be retrieved via the API:
REST API ([Schema](https://api.qdrant.tech/api-reference/points/get-point)):
```
GET /collections/{collection_name}/points/{point_id}

```
