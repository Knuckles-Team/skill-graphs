##  [](https://qdrant.tech/documentation/concepts/collections/#update-collection-parameters)Update collection parameters
Dynamic parameter updates may be helpful, for example, for more efficient initial loading of vectors. For example, you can disable indexing during the upload process, and enable it immediately after the upload is finished. As a result, you will not waste extra computation resources on rebuilding the index.
The following command enables indexing for segments that have more than 10000 kB of vectors stored:
httpbashpythontypescriptrustjavacsharpgo
```
PATCH /collections/{collection_name}
{
    "optimizers_config": {
        "indexing_threshold": 10000
    }
}

```

```
curl -X PATCH http://localhost:6333/collections/{collection_name} \
  -H 'Content-Type: application/json' \
  --data-raw '{
    "optimizers_config": {
        "indexing_threshold": 10000
    }
  }'

```

```
client.update_collection(
    collection_name="{collection_name}",
    optimizers_config=models.OptimizersConfigDiff(indexing_threshold=10000),
)

```

```
client.updateCollection("{collection_name}", {
  optimizers_config: {
    indexing_threshold: 10000,
  },
});

```

```
use qdrant_client::qdrant::{OptimizersConfigDiffBuilder, UpdateCollectionBuilder};

client
    .update_collection(
        UpdateCollectionBuilder::new("{collection_name}").optimizers_config(
            OptimizersConfigDiffBuilder::default().indexing_threshold(10000),
        ),
    )
    .await?;

```

```
import io.qdrant.client.grpc.Collections.OptimizersConfigDiff;
import io.qdrant.client.grpc.Collections.UpdateCollection;

client
    .updateCollectionAsync(
        UpdateCollection.newBuilder()
            .setCollectionName("{collection_name}")
            .setOptimizersConfig(
                OptimizersConfigDiff.newBuilder().setIndexingThreshold(10000).build())
            .build())
    .get();

```

```
using Qdrant.Client;
using Qdrant.Client.Grpc;

var client = new QdrantClient("localhost", 6334);

await client.UpdateCollectionAsync(
	collectionName: "{collection_name}",
	optimizersConfig: new OptimizersConfigDiff { IndexingThreshold = 10000 }
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
})

```

The following parameters can be updated:
  * `optimizers_config` - see [optimizer](https://qdrant.tech/documentation/concepts/optimizer/) for details.
  * `hnsw_config` - see [indexing](https://qdrant.tech/documentation/concepts/indexing/#vector-index) for details.
  * `quantization_config` - see [quantization](https://qdrant.tech/documentation/guides/quantization/#setting-up-quantization-in-qdrant) for details.
  * `vectors_config` - vector-specific configuration, including individual `hnsw_config`, `quantization_config` and `on_disk` settings.
  * `params` - other collection parameters, including `read_fan_out_delay_ms`, `write_consistency_factor` and `on_disk_payload`.
  * `strict_mode_config` - see [strict mode](https://qdrant.tech/documentation/guides/administration/#strict-mode) for details.


Full API specification is available in [schema definitions](https://api.qdrant.tech/api-reference/collections/update-collection).
Calls to this endpoint may be blocking as it waits for existing optimizers to finish. We recommended against using this in a production database as it may introduce huge overhead due to the rebuilding of the index.
####  [](https://qdrant.tech/documentation/concepts/collections/#update-vector-parameters)Update vector parameters
_Available as of v1.4.0_
To update vector parameters using the collection update API, you must always specify a vector name. If your collection does not have named vectors, use an empty (`""`) name.
Qdrant 1.4 adds support for updating more collection parameters at runtime. HNSW index, quantization and disk configurations can now be changed without recreating a collection. Segments (with index and quantized data) will automatically be rebuilt in the background to match updated parameters.
To put vector data on disk for a collection that **does not have** named vectors, use `""` as name:
httpbash
```
PATCH /collections/{collection_name}
{
    "vectors": {
        "": {
            "on_disk": true
        }
    }
}

```

```
curl -X PATCH http://localhost:6333/collections/{collection_name} \
  -H 'Content-Type: application/json' \
  --data-raw '{
    "vectors": {
        "": {
            "on_disk": true
      }
    }
  }'

```

To put vector data on disk for a collection that **does have** named vectors:
Note: To create a vector name, follow the procedure from our [Points](https://qdrant.tech/documentation/concepts/points/#create-vector-name).
httpbash
```
PATCH /collections/{collection_name}
{
    "vectors": {
        "my_vector": {
            "on_disk": true
        }
    }
}

```

```
curl -X PATCH http://localhost:6333/collections/{collection_name} \
  -H 'Content-Type: application/json' \
  --data-raw '{
    "vectors": {
        "my_vector": {
           "on_disk": true
      }
    }
  }'

```

In the following example the HNSW index and quantization parameters are updated, both for the whole collection, and for `my_vector` specifically:
httpbashpythontypescriptrustjavacsharpgo
```
PATCH /collections/{collection_name}
{
    "vectors": {
        "my_vector": {
            "hnsw_config": {
                "m": 32,
                "ef_construct": 123
            },
            "quantization_config": {
                "product": {
                    "compression": "x32",
                    "always_ram": true
                }
            },
            "on_disk": true
        }
    },
    "hnsw_config": {
        "ef_construct": 123
    },
    "quantization_config": {
        "scalar": {
            "type": "int8",
            "quantile": 0.8,
            "always_ram": false
        }
    }
}

```

```
curl -X PATCH http://localhost:6333/collections/{collection_name} \
  -H 'Content-Type: application/json' \
  --data-raw '{
    "vectors": {
        "my_vector": {
            "hnsw_config": {
                "m": 32,
                "ef_construct": 123
            },
            "quantization_config": {
                "product": {
                    "compression": "x32",
                    "always_ram": true
                }
            },
            "on_disk": true
        }
    },
    "hnsw_config": {
        "ef_construct": 123
    },
    "quantization_config": {
        "scalar": {
            "type": "int8",
            "quantile": 0.8,
            "always_ram": false
        }
    }
}'

```

```
client.update_collection(
    collection_name="{collection_name}",
    vectors_config={
        "my_vector": models.VectorParamsDiff(
            hnsw_config=models.HnswConfigDiff(
                m=32,
                ef_construct=123,
            ),
            quantization_config=models.ProductQuantization(
                product=models.ProductQuantizationConfig(
                    compression=models.CompressionRatio.X32,
                    always_ram=True,
                ),
            ),
            on_disk=True,
        ),
    },
    hnsw_config=models.HnswConfigDiff(
        ef_construct=123,
    ),
    quantization_config=models.ScalarQuantization(
        scalar=models.ScalarQuantizationConfig(
            type=models.ScalarType.INT8,
            quantile=0.8,
            always_ram=False,
        ),
    ),
)

```

```
client.updateCollection("{collection_name}", {
  vectors: {
    my_vector: {
      hnsw_config: {
        m: 32,
        ef_construct: 123,
      },
      quantization_config: {
        product: {
          compression: "x32",
          always_ram: true,
        },
      },
      on_disk: true,
    },
  },
  hnsw_config: {
    ef_construct: 123,
  },
  quantization_config: {
    scalar: {
      type: "int8",
      quantile: 0.8,
      always_ram: true,
    },
  },
});

```

```
use std::collections::HashMap;

use qdrant_client::qdrant::{
    quantization_config_diff::Quantization, vectors_config_diff::Config, HnswConfigDiffBuilder,
    QuantizationType, ScalarQuantizationBuilder, UpdateCollectionBuilder, VectorParamsDiffBuilder,
    VectorParamsDiffMap,
};

client
    .update_collection(
        UpdateCollectionBuilder::new("{collection_name}")
            .hnsw_config(HnswConfigDiffBuilder::default().ef_construct(123))
            .vectors_config(Config::ParamsMap(VectorParamsDiffMap {
                map: HashMap::from([(
                    ("my_vector".into()),
                    VectorParamsDiffBuilder::default()
                        .hnsw_config(HnswConfigDiffBuilder::default().m(32).ef_construct(123))
                        .build(),
                )]),
            }))
            .quantization_config(Quantization::Scalar(
                ScalarQuantizationBuilder::default()
                    .r#type(QuantizationType::Int8.into())
                    .quantile(0.8)
                    .always_ram(true)
                    .build(),
            )),
    )
    .await?;

```

```
import io.qdrant.client.grpc.Collections.HnswConfigDiff;
import io.qdrant.client.grpc.Collections.QuantizationConfigDiff;
import io.qdrant.client.grpc.Collections.QuantizationType;
import io.qdrant.client.grpc.Collections.ScalarQuantization;
import io.qdrant.client.grpc.Collections.UpdateCollection;
import io.qdrant.client.grpc.Collections.VectorParamsDiff;
import io.qdrant.client.grpc.Collections.VectorParamsDiffMap;
import io.qdrant.client.grpc.Collections.VectorsConfigDiff;

client
    .updateCollectionAsync(
        UpdateCollection.newBuilder()
            .setCollectionName("{collection_name}")
            .setHnswConfig(HnswConfigDiff.newBuilder().setEfConstruct(123).build())
            .setVectorsConfig(
                VectorsConfigDiff.newBuilder()
                    .setParamsMap(
                        VectorParamsDiffMap.newBuilder()
                            .putMap(
                                "my_vector",
                                VectorParamsDiff.newBuilder()
                                    .setHnswConfig(
                                        HnswConfigDiff.newBuilder()
                                            .setM(3)
                                            .setEfConstruct(123)
                                            .build())
                                    .build())))
            .setQuantizationConfig(
                QuantizationConfigDiff.newBuilder()
                    .setScalar(
                        ScalarQuantization.newBuilder()
                            .setType(QuantizationType.Int8)
                            .setQuantile(0.8f)
                            .setAlwaysRam(true)
                            .build()))
            .build())
    .get();

```

```
using Qdrant.Client;
using Qdrant.Client.Grpc;

var client = new QdrantClient("localhost", 6334);

await client.UpdateCollectionAsync(
	collectionName: "{collection_name}",
	hnswConfig: new HnswConfigDiff { EfConstruct = 123 },
	vectorsConfig: new VectorParamsDiffMap
	{
		Map =
		{
			{
				"my_vector",
				new VectorParamsDiff
				{
					HnswConfig = new HnswConfigDiff { M = 3, EfConstruct = 123 }
				}
			}
		}
	},
	quantizationConfig: new QuantizationConfigDiff
	{
		Scalar = new ScalarQuantization
		{
			Type = QuantizationType.Int8,
			Quantile = 0.8f,
			AlwaysRam = true
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

client.UpdateCollection(context.Background(), &qdrant.UpdateCollection{
	CollectionName: "{collection_name}",
	VectorsConfig: qdrant.NewVectorsConfigDiffMap(
		map[string]*qdrant.VectorParamsDiff{
			"my_vector": {
				HnswConfig: &qdrant.HnswConfigDiff{
					M:           qdrant.PtrOf(uint64(3)),
					EfConstruct: qdrant.PtrOf(uint64(123)),
				},
			},
		}),
	QuantizationConfig: qdrant.NewQuantizationDiffScalar(
		&qdrant.ScalarQuantization{
			Type:      qdrant.QuantizationType_Int8,
			Quantile:  qdrant.PtrOf(float32(0.8)),
			AlwaysRam: qdrant.PtrOf(true),
		}),
})

```
