##  [](https://qdrant.tech/documentation/guides/quantization/#quantization-tips)Quantization tips
####  [](https://qdrant.tech/documentation/guides/quantization/#accuracy-tuning)Accuracy tuning
In this section, we will discuss how to tune the search precision. The fastest way to understand the impact of quantization on the search quality is to compare the search results with and without quantization.
In order to disable quantization, you can set `ignore` to `true` in the search request:
httppythontypescriptrustjavacsharpgo
```
POST /collections/{collection_name}/points/query
{
    "query": [0.2, 0.1, 0.9, 0.7],
    "params": {
        "quantization": {
            "ignore": true
        }
    },
    "limit": 10
}

```

```
from qdrant_client import QdrantClient, models

client = QdrantClient(url="http://localhost:6333")

client.query_points(
    collection_name="{collection_name}",
    query=[0.2, 0.1, 0.9, 0.7],
    search_params=models.SearchParams(
        quantization=models.QuantizationSearchParams(
            ignore=True,
        )
    ),
)

```

```
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.query("{collection_name}", {
    query: [0.2, 0.1, 0.9, 0.7],
    params: {
        quantization: {
            ignore: true,
        },
    },
});

```

```
use qdrant_client::qdrant::{
    QuantizationSearchParamsBuilder, QueryPointsBuilder, SearchParamsBuilder,
};
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

client
    .query(
        QueryPointsBuilder::new("{collection_name}")
            .query(vec![0.2, 0.1, 0.9, 0.7])
            .limit(3)
            .params(
                SearchParamsBuilder::default()
                    .quantization(QuantizationSearchParamsBuilder::default().ignore(true)),
            ),
    )
    .await?;

```

```
import static io.qdrant.client.QueryFactory.nearest;

import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Points.QuantizationSearchParams;
import io.qdrant.client.grpc.Points.QueryPoints;
import io.qdrant.client.grpc.Points.SearchParams;

QdrantClient client =
    new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client.queryAsync(
        QueryPoints.newBuilder()
                .setCollectionName("{collection_name}")
                .setQuery(nearest(0.2f, 0.1f, 0.9f, 0.7f))
                .setParams(
                        SearchParams.newBuilder()
                                .setQuantization(
                                        QuantizationSearchParams.newBuilder().setIgnore(true).build())
                                .build())
                .setLimit(10)
                .build())
        .get();

```

```
using Qdrant.Client;
using Qdrant.Client.Grpc;

var client = new QdrantClient("localhost", 6334);

await client.QueryAsync(
	collectionName: "{collection_name}",
	query: new float[] { 0.2f, 0.1f, 0.9f, 0.7f },
	searchParams: new SearchParams
	{
		Quantization = new QuantizationSearchParams { Ignore = true }
	},
	limit: 10
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

client.Query(context.Background(), &qdrant.QueryPoints{
	CollectionName: "{collection_name}",
	Query:          qdrant.NewQuery(0.2, 0.1, 0.9, 0.7),
	Params: &qdrant.SearchParams{
		Quantization: &qdrant.QuantizationSearchParams{
			Ignore: qdrant.PtrOf(false),
		},
	},
})

```

  * **Adjust the quantile parameter** : The quantile parameter in scalar quantization determines the quantization bounds. By setting it to a value lower than 1.0, you can exclude extreme values (outliers) from the quantization bounds. For example, if you set the quantile to 0.99, 1% of the extreme values will be excluded. By adjusting the quantile, you find an optimal value that will provide the best search quality for your collection.
  * **Enable rescore** : Having the original vectors available, Qdrant can re-evaluate top-k search results using the original vectors. On large collections, this can improve the search quality, with just minor performance impact.


####  [](https://qdrant.tech/documentation/guides/quantization/#memory-and-speed-tuning)Memory and speed tuning
In this section, we will discuss how to tune the memory and speed of the search process with quantization.
There are 3 possible modes to place storage of vectors within the qdrant collection:
  * **All in RAM** - all vector, original and quantized, are loaded and kept in RAM. This is the fastest mode, but requires a lot of RAM. Enabled by default.
  * **Original on Disk, quantized in RAM** - this is a hybrid mode, allows to obtain a good balance between speed and memory usage. Recommended scenario if you are aiming to shrink the memory footprint while keeping the search speed.


This mode is enabled by setting `always_ram` to `true` in the quantization config while using memmap storage:
httppythontypescriptrustjavacsharpgo
```
PUT /collections/{collection_name}
{
    "vectors": {
        "size": 768,
        "distance": "Cosine",
        "on_disk": true
    },
    "quantization_config": {
        "scalar": {
            "type": "int8",
            "always_ram": true
        }
    }
}

```

```
from qdrant_client import QdrantClient, models

client = QdrantClient(url="http://localhost:6333")

client.create_collection(
    collection_name="{collection_name}",
    vectors_config=models.VectorParams(size=768, distance=models.Distance.COSINE, on_disk=True),
    quantization_config=models.ScalarQuantization(
        scalar=models.ScalarQuantizationConfig(
            type=models.ScalarType.INT8,
            always_ram=True,
        ),
    ),
)

```

```
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.createCollection("{collection_name}", {
  vectors: {
    size: 768,
    distance: "Cosine",
    on_disk: true,
  },
  quantization_config: {
    scalar: {
      type: "int8",
      always_ram: true,
    },
  },
});

```

```
use qdrant_client::qdrant::{
    CreateCollectionBuilder, Distance, QuantizationType, ScalarQuantizationBuilder,
    VectorParamsBuilder,
};
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

client
    .create_collection(
        CreateCollectionBuilder::new("{collection_name}")
            .vectors_config(VectorParamsBuilder::new(768, Distance::Cosine))
            .quantization_config(
                ScalarQuantizationBuilder::default()
                    .r#type(QuantizationType::Int8.into())
                    .always_ram(true),
            ),
    )
    .await?;

```

```
import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Collections.CreateCollection;
import io.qdrant.client.grpc.Collections.Distance;
import io.qdrant.client.grpc.Collections.OptimizersConfigDiff;
import io.qdrant.client.grpc.Collections.QuantizationConfig;
import io.qdrant.client.grpc.Collections.QuantizationType;
import io.qdrant.client.grpc.Collections.ScalarQuantization;
import io.qdrant.client.grpc.Collections.VectorParams;
import io.qdrant.client.grpc.Collections.VectorsConfig;

QdrantClient client =
    new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client
    .createCollectionAsync(
        CreateCollection.newBuilder()
            .setCollectionName("{collection_name}")
            .setVectorsConfig(
                VectorsConfig.newBuilder()
                    .setParams(
                        VectorParams.newBuilder()
                            .setSize(768)
                            .setDistance(Distance.Cosine)
                            .setOnDisk(true)
                            .build())
                    .build())
            .setQuantizationConfig(
                QuantizationConfig.newBuilder()
                    .setScalar(
                        ScalarQuantization.newBuilder()
                            .setType(QuantizationType.Int8)
                            .setAlwaysRam(true)
                            .build())
                    .build())
            .build())
    .get();

```

```
using Qdrant.Client;
using Qdrant.Client.Grpc;

var client = new QdrantClient("localhost", 6334);

await client.CreateCollectionAsync(
	collectionName: "{collection_name}",
	vectorsConfig: new VectorParams { Size = 768, Distance = Distance.Cosine, OnDisk = true },
	quantizationConfig: new QuantizationConfig
	{
		Scalar = new ScalarQuantization { Type = QuantizationType.Int8, AlwaysRam = true }
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
		Size:     768,
		Distance: qdrant.Distance_Cosine,
		OnDisk:   qdrant.PtrOf(true),
	}),
	QuantizationConfig: qdrant.NewQuantizationScalar(&qdrant.ScalarQuantization{
		Type:      qdrant.QuantizationType_Int8,
		AlwaysRam: qdrant.PtrOf(true),
	}),
})

```

In this scenario, the number of disk reads may play a significant role in the search speed. In a system with high disk latency, the re-scoring step may become a bottleneck.
Consider disabling `rescore` to improve the search speed:
httppythontypescriptrustjavacsharpgo
```
POST /collections/{collection_name}/points/query
{
    "query": [0.2, 0.1, 0.9, 0.7],
    "params": {
        "quantization": {
            "rescore": false
        }
    },
    "limit": 10
}

```

```
from qdrant_client import QdrantClient, models

client = QdrantClient(url="http://localhost:6333")

client.query_points(
    collection_name="{collection_name}",
    query=[0.2, 0.1, 0.9, 0.7],
    search_params=models.SearchParams(
        quantization=models.QuantizationSearchParams(rescore=False)
    ),
)

```

```
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.query("{collection_name}", {
    query: [0.2, 0.1, 0.9, 0.7],
    params: {
        quantization: {
            rescore: false,
        },
    },
});

```

```
use qdrant_client::qdrant::{
    QuantizationSearchParamsBuilder, QueryPointsBuilder, SearchParamsBuilder,
};
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

client
    .query(
        QueryPointsBuilder::new("{collection_name}")
            .query(vec![0.2, 0.1, 0.9, 0.7])
            .limit(3)
            .params(
                SearchParamsBuilder::default()
                    .quantization(QuantizationSearchParamsBuilder::default().rescore(false)),
            ),
    )
    .await?;

```

```
import static io.qdrant.client.QueryFactory.nearest;

import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Points.QuantizationSearchParams;
import io.qdrant.client.grpc.Points.QueryPoints;
import io.qdrant.client.grpc.Points.SearchParams;

QdrantClient client =
    new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client.queryAsync(
        QueryPoints.newBuilder()
                .setCollectionName("{collection_name}")
                .setQuery(nearest(0.2f, 0.1f, 0.9f, 0.7f))
                .setParams(
                        SearchParams.newBuilder()
                                .setQuantization(
                                        QuantizationSearchParams.newBuilder().setRescore(false).build())
                                .build())
                .setLimit(3)
                .build())
        .get();

```

```
using Qdrant.Client;
using Qdrant.Client.Grpc;

var client = new QdrantClient("localhost", 6334);

await client.QueryAsync(
	collectionName: "{collection_name}",
	query: new float[] { 0.2f, 0.1f, 0.9f, 0.7f },
	searchParams: new SearchParams
	{
		Quantization = new QuantizationSearchParams { Rescore = false }
	},
	limit: 3
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

client.Query(context.Background(), &qdrant.QueryPoints{
	CollectionName: "{collection_name}",
	Query:          qdrant.NewQuery(0.2, 0.1, 0.9, 0.7),
	Params: &qdrant.SearchParams{
		Quantization: &qdrant.QuantizationSearchParams{
			Rescore: qdrant.PtrOf(false),
		},
	},
})

```

  * **All on Disk** - all vectors, original and quantized, are stored on disk. This mode allows to achieve the smallest memory footprint, but at the cost of the search speed.


It is recommended to use this mode if you have a large collection and fast storage (e.g. SSD or NVMe).
This mode is enabled by setting `always_ram` to `false` in the quantization config while using mmap storage:
httppythontypescriptrustjavacsharpgo
```
PUT /collections/{collection_name}
{
    "vectors": {
      "size": 768,
      "distance": "Cosine",
      "on_disk": true
    },
    "quantization_config": {
        "scalar": {
            "type": "int8",
            "always_ram": false
        }
    }
}

```

```
from qdrant_client import QdrantClient, models

client = QdrantClient(url="http://localhost:6333")

client.create_collection(
    collection_name="{collection_name}",
    vectors_config=models.VectorParams(size=768, distance=models.Distance.COSINE, on_disk=True),
    quantization_config=models.ScalarQuantization(
        scalar=models.ScalarQuantizationConfig(
            type=models.ScalarType.INT8,
            always_ram=False,
        ),
    ),
)

```

```
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.createCollection("{collection_name}", {
  vectors: {
    size: 768,
    distance: "Cosine",
    on_disk: true,
  },
  quantization_config: {
    scalar: {
      type: "int8",
      always_ram: false,
    },
  },
});

```

```
use qdrant_client::qdrant::{
    CreateCollectionBuilder, Distance, QuantizationType, ScalarQuantizationBuilder,
    VectorParamsBuilder,
};
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

client
    .create_collection(
        CreateCollectionBuilder::new("{collection_name}")
            .vectors_config(VectorParamsBuilder::new(768, Distance::Cosine).on_disk(true))
            .quantization_config(
                ScalarQuantizationBuilder::default()
                    .r#type(QuantizationType::Int8.into())
                    .always_ram(false),
            ),
    )
    .await?;

```

```
import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Collections.CreateCollection;
import io.qdrant.client.grpc.Collections.Distance;
import io.qdrant.client.grpc.Collections.OptimizersConfigDiff;
import io.qdrant.client.grpc.Collections.QuantizationConfig;
import io.qdrant.client.grpc.Collections.QuantizationType;
import io.qdrant.client.grpc.Collections.ScalarQuantization;
import io.qdrant.client.grpc.Collections.VectorParams;
import io.qdrant.client.grpc.Collections.VectorsConfig;

QdrantClient client =
    new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client
    .createCollectionAsync(
        CreateCollection.newBuilder()
            .setCollectionName("{collection_name}")
            .setVectorsConfig(
                VectorsConfig.newBuilder()
                    .setParams(
                        VectorParams.newBuilder()
                            .setSize(768)
                            .setDistance(Distance.Cosine)
                            .setOnDisk(true)
                            .build())
                    .build())
            .setQuantizationConfig(
                QuantizationConfig.newBuilder()
                    .setScalar(
                        ScalarQuantization.newBuilder()
                            .setType(QuantizationType.Int8)
                            .setAlwaysRam(false)
                            .build())
                    .build())
            .build())
    .get();

```

```
using Qdrant.Client;
using Qdrant.Client.Grpc;

var client = new QdrantClient("localhost", 6334);

await client.CreateCollectionAsync(
 collectionName: "{collection_name}",
 vectorsConfig: new VectorParams { Size = 768, Distance = Distance.Cosine, OnDisk = true},
 quantizationConfig: new QuantizationConfig
 {
  Scalar = new ScalarQuantization { Type = QuantizationType.Int8, AlwaysRam = false }
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
		Size:     768,
		Distance: qdrant.Distance_Cosine,
		OnDisk:   qdrant.PtrOf(true),
	}),
	QuantizationConfig: qdrant.NewQuantizationScalar(
		&qdrant.ScalarQuantization{
			Type:      qdrant.QuantizationType_Int8,
			AlwaysRam: qdrant.PtrOf(false),
		},
	),
})

```

##### Was this page useful?
![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg) Yes  ![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg) No
Thank you for your feedback! 🙏
We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/guides/quantization.md) this page on GitHub, or
On this page:
  * [Quantization](https://qdrant.tech/documentation/guides/quantization/#quantization)
    * [Scalar Quantization](https://qdrant.tech/documentation/guides/quantization/#scalar-quantization)
    * [Binary Quantization](https://qdrant.tech/documentation/guides/quantization/#binary-quantization)
      * [Binary Quantization as Hamming Distance](https://qdrant.tech/documentation/guides/quantization/#binary-quantization-as-hamming-distance)
      * [1.5-Bit and 2-Bit Quantization](https://qdrant.tech/documentation/guides/quantization/#15-bit-and-2-bit-quantization)
      * [Asymmetric Quantization](https://qdrant.tech/documentation/guides/quantization/#asymmetric-quantization)
    * [Product Quantization](https://qdrant.tech/documentation/guides/quantization/#product-quantization)
    * [How to choose the right quantization method](https://qdrant.tech/documentation/guides/quantization/#how-to-choose-the-right-quantization-method)
    * [Setting up Quantization in Qdrant](https://qdrant.tech/documentation/guides/quantization/#setting-up-quantization-in-qdrant)
      * [Setting up Scalar Quantization](https://qdrant.tech/documentation/guides/quantization/#setting-up-scalar-quantization)
      * [Setting up Binary Quantization](https://qdrant.tech/documentation/guides/quantization/#setting-up-binary-quantization)
      * [Setting up Product Quantization](https://qdrant.tech/documentation/guides/quantization/#setting-up-product-quantization)
      * [Disabling Quantization](https://qdrant.tech/documentation/guides/quantization/#disabling-quantization)
      * [Searching with Quantization](https://qdrant.tech/documentation/guides/quantization/#searching-with-quantization)
    * [Quantization tips](https://qdrant.tech/documentation/guides/quantization/#quantization-tips)


#### Ready to get started with Qdrant?
© 2025 Qdrant.
[Terms](https://qdrant.tech/legal/terms_and_conditions/) [Privacy Policy](https://qdrant.tech/legal/privacy-policy/) [Impressum](https://qdrant.tech/legal/impressum/)
×
[ Powered by ](https://qdrant.tech/)
