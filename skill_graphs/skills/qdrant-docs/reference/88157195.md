##  [](https://qdrant.tech/documentation/concepts/points/#modify-points)Modify points
To change a point, you can modify its vectors or its payload. There are several ways to do this.
###  [](https://qdrant.tech/documentation/concepts/points/#update-vectors)Update vectors
_Available as of v1.2.0_
This method updates the specified vectors on the given points. Unspecified vectors are kept unchanged. All given points must exist.
REST API ([Schema](https://api.qdrant.tech/api-reference/points/update-vectors)):
httppythontypescriptrustjavacsharpgo
```
PUT /collections/{collection_name}/points/vectors
{
    "points": [
        {
            "id": 1,
            "vector": {
                "image": [0.1, 0.2, 0.3, 0.4]
            }
        },
        {
            "id": 2,
            "vector": {
                "text": [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2]
            }
        }
    ]
}

```

```
client.update_vectors(
    collection_name="{collection_name}",
    points=[
        models.PointVectors(
            id=1,
            vector={
                "image": [0.1, 0.2, 0.3, 0.4],
            },
        ),
        models.PointVectors(
            id=2,
            vector={
                "text": [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2],
            },
        ),
    ],
)

```

```
client.updateVectors("{collection_name}", {
  points: [
    {
      id: 1,
      vector: {
        image: [0.1, 0.2, 0.3, 0.4],
      },
    },
    {
      id: 2,
      vector: {
        text: [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2],
      },
    },
  ],
});

```

```
use std::collections::HashMap;

use qdrant_client::qdrant::{
    PointVectors, UpdatePointVectorsBuilder,
};

client
    .update_vectors(
        UpdatePointVectorsBuilder::new(
            "{collection_name}",
            vec![
                PointVectors {
                    id: Some(1.into()),
                    vectors: Some(
                        HashMap::from([("image".to_string(), vec![0.1, 0.2, 0.3, 0.4])]).into(),
                    ),
                },
                PointVectors {
                    id: Some(2.into()),
                    vectors: Some(
                        HashMap::from([(
                            "text".to_string(),
                            vec![0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2],
                        )])
                        .into(),
                    ),
                },
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

import io.qdrant.client.grpc.Points.PointVectors;
import java.util.List;
import java.util.Map;

client
    .updateVectorsAsync(
        "{collection_name}",
        List.of(
            PointVectors.newBuilder()
                .setId(id(1))
                .setVectors(namedVectors(Map.of("image", vector(List.of(0.1f, 0.2f, 0.3f, 0.4f)))))
                .build(),
            PointVectors.newBuilder()
                .setId(id(2))
                .setVectors(
                    namedVectors(
                        Map.of(
                            "text", vector(List.of(0.9f, 0.8f, 0.7f, 0.6f, 0.5f, 0.4f, 0.3f, 0.2f)))))
                .build()))
    .get();

```

```
using Qdrant.Client;
using Qdrant.Client.Grpc;

var client = new QdrantClient("localhost", 6334);

await client.UpdateVectorsAsync(
	collectionName: "{collection_name}",
	points: new List<PointVectors>
	{
		new() { Id = 1, Vectors = ("image", new float[] { 0.1f, 0.2f, 0.3f, 0.4f }) },
		new()
		{
			Id = 2,
			Vectors = ("text", new float[] { 0.9f, 0.8f, 0.7f, 0.6f, 0.5f, 0.4f, 0.3f, 0.2f })
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

client.UpdateVectors(context.Background(), &qdrant.UpdatePointVectors{
	CollectionName: "{collection_name}",
	Points: []*qdrant.PointVectors{
		{
			Id: qdrant.NewIDNum(1),
			Vectors: qdrant.NewVectorsMap(map[string]*qdrant.Vector{
				"image": qdrant.NewVector(0.1, 0.2, 0.3, 0.4),
			}),
		},
		{
			Id: qdrant.NewIDNum(2),
			Vectors: qdrant.NewVectorsMap(map[string]*qdrant.Vector{
				"text": qdrant.NewVector(0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2),
			}),
		},
	},
})

```

To update points and replace all of its vectors, see [uploading points](https://qdrant.tech/documentation/concepts/points/#upload-points).
###  [](https://qdrant.tech/documentation/concepts/points/#delete-vectors)Delete vectors
_Available as of v1.2.0_
This method deletes just the specified vectors from the given points. Other vectors are kept unchanged. Points are never deleted.
REST API ([Schema](https://api.qdrant.tech/api-reference/points/delete-vectors)):
httppythontypescriptrustjavacsharpgo
```
POST /collections/{collection_name}/points/vectors/delete
{
    "points": [0, 3, 100],
    "vectors": ["text", "image"]
}

```

```
client.delete_vectors(
    collection_name="{collection_name}",
    points=[0, 3, 100],
    vectors=["text", "image"],
)

```

```
client.deleteVectors("{collection_name}", {
  points: [0, 3, 10],
  vector: ["text", "image"],
});

```

```
use qdrant_client::qdrant::{
    DeletePointVectorsBuilder, PointsIdsList,
};

client
    .delete_vectors(
        DeletePointVectorsBuilder::new("{collection_name}")
            .points_selector(PointsIdsList {
                ids: vec![0.into(), 3.into(), 10.into()],
            })
            .vectors(vec!["text".into(), "image".into()])
            .wait(true),
    )
    .await?;

```

```
import static io.qdrant.client.PointIdFactory.id;

import java.util.List;

client
    .deleteVectorsAsync(
        "{collection_name}", List.of("text", "image"), List.of(id(0), id(3), id(10)))
    .get();

```

```
await client.DeleteVectorsAsync("{collection_name}", ["text", "image"], [0, 3, 10]);

```

```
import (
	"context"

	"github.com/qdrant/go-client/qdrant"
)

client.DeleteVectors(context.Background(), &qdrant.DeletePointVectors{
	CollectionName: "{collection_name}",
	PointsSelector: qdrant.NewPointsSelector(
		qdrant.NewIDNum(0), qdrant.NewIDNum(3), qdrant.NewIDNum(10)),
	Vectors: &qdrant.VectorsSelector{
		Names: []string{"text", "image"},
	},
})

```

To delete entire points, see [deleting points](https://qdrant.tech/documentation/concepts/points/#delete-points).
###  [](https://qdrant.tech/documentation/concepts/points/#update-payload)Update payload
Learn how to modify the payload of a point in the [Payload](https://qdrant.tech/documentation/concepts/payload/#update-payload) section.
