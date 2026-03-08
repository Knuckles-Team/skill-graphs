##  [](https://qdrant.tech/documentation/guides/quantization/#setting-up-quantization-in-qdrant)Setting up Quantization in Qdrant
You can configure quantization for a collection by specifying the quantization parameters in the `quantization_config` section of the collection configuration.
Quantization will be automatically applied to all vectors during the indexation process. Quantized vectors are stored alongside the original vectors in the collection, so you will still have access to the original vectors if you need them.
_Available as of v1.1.1_
The `quantization_config` can also be set on a per vector basis by specifying it in a named vector.
###  [](https://qdrant.tech/documentation/guides/quantization/#setting-up-scalar-quantization)Setting up Scalar Quantization
To enable scalar quantization, you need to specify the quantization parameters in the `quantization_config` section of the collection configuration.
When enabling scalar quantization on an existing collection, use a PATCH request or the corresponding `update_collection` method and omit the vector configuration, as it’s already defined.
httppythontypescriptrustjavacsharpgo
```
PUT /collections/{collection_name}
{
    "vectors": {
      "size": 768,
      "distance": "Cosine"
    },
    "quantization_config": {
        "scalar": {
            "type": "int8",
            "quantile": 0.99,
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
    vectors_config=models.VectorParams(size=768, distance=models.Distance.COSINE),
    quantization_config=models.ScalarQuantization(
        scalar=models.ScalarQuantizationConfig(
            type=models.ScalarType.INT8,
            quantile=0.99,
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
  },
  quantization_config: {
    scalar: {
      type: "int8",
      quantile: 0.99,
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
                    .quantile(0.99)
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
                            .build())
                    .build())
            .setQuantizationConfig(
                QuantizationConfig.newBuilder()
                    .setScalar(
                        ScalarQuantization.newBuilder()
                            .setType(QuantizationType.Int8)
                            .setQuantile(0.99f)
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
 vectorsConfig: new VectorParams { Size = 768, Distance = Distance.Cosine },
 quantizationConfig: new QuantizationConfig
 {
  Scalar = new ScalarQuantization
  {
   Type = QuantizationType.Int8,
   Quantile = 0.99f,
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

client.CreateCollection(context.Background(), &qdrant.CreateCollection{
	CollectionName: "{collection_name}",
	VectorsConfig: qdrant.NewVectorsConfig(&qdrant.VectorParams{
		Size:     768,
		Distance: qdrant.Distance_Cosine,
	}),
	QuantizationConfig: qdrant.NewQuantizationScalar(
		&qdrant.ScalarQuantization{
            Type:      qdrant.QuantizationType_Int8,
			Quantile:  qdrant.PtrOf(float32(0.99)),
			AlwaysRam: qdrant.PtrOf(true),
		},
	),
})

```

There are 3 parameters that you can specify in the `quantization_config` section:
`type` - the type of the quantized vector components. Currently, Qdrant supports only `int8`.
`quantile` - the quantile of the quantized vector components. The quantile is used to calculate the quantization bounds. For instance, if you specify `0.99` as the quantile, 1% of extreme values will be excluded from the quantization bounds.
Using quantiles lower than `1.0` might be useful if there are outliers in your vector components. This parameter only affects the resulting precision and not the memory footprint. It might be worth tuning this parameter if you experience a significant decrease in search quality.
`always_ram` - whether to keep quantized vectors always cached in RAM or not. By default, quantized vectors are loaded in the same way as the original vectors. However, in some setups you might want to keep quantized vectors in RAM to speed up the search process.
In this case, you can set `always_ram` to `true` to store quantized vectors in RAM.
###  [](https://qdrant.tech/documentation/guides/quantization/#setting-up-binary-quantization)Setting up Binary Quantization
To enable binary quantization, you need to specify the quantization parameters in the `quantization_config` section of the collection configuration.
When enabling binary quantization on an existing collection, use a PATCH request or the corresponding `update_collection` method and omit the vector configuration, as it’s already defined.
httppythontypescriptrustjavacsharpgo
```
PUT /collections/{collection_name}
{
    "vectors": {
      "size": 1536,
      "distance": "Cosine"
    },
    "quantization_config": {
        "binary": {
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
    vectors_config=models.VectorParams(size=1536, distance=models.Distance.COSINE),
    quantization_config=models.BinaryQuantization(
        binary=models.BinaryQuantizationConfig(
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
    size: 1536,
    distance: "Cosine",
  },
  quantization_config: {
    binary: {
      always_ram: true,
    },
  },
});

```

```
use qdrant_client::qdrant::{
    BinaryQuantizationBuilder, CreateCollectionBuilder, Distance, VectorParamsBuilder,
};
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

client
    .create_collection(
        CreateCollectionBuilder::new("{collection_name}")
            .vectors_config(VectorParamsBuilder::new(1536, Distance::Cosine))
            .quantization_config(BinaryQuantizationBuilder::new(true)),
    )
    .await?;

```

```
import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Collections.BinaryQuantization;
import io.qdrant.client.grpc.Collections.CreateCollection;
import io.qdrant.client.grpc.Collections.Distance;
import io.qdrant.client.grpc.Collections.QuantizationConfig;
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
                            .setSize(1536)
                            .setDistance(Distance.Cosine)
                            .build())
                    .build())
            .setQuantizationConfig(
                QuantizationConfig.newBuilder()
                    .setBinary(BinaryQuantization.newBuilder().setAlwaysRam(true).build())
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
 vectorsConfig: new VectorParams { Size = 1536, Distance = Distance.Cosine },
 quantizationConfig: new QuantizationConfig
 {
  Binary = new BinaryQuantization { AlwaysRam = true }
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
		Size:     1536,
		Distance: qdrant.Distance_Cosine,
	}),
	QuantizationConfig: qdrant.NewQuantizationBinary(
		&qdrant.BinaryQuantization{
			AlwaysRam: qdrant.PtrOf(true),
		},
	),
})

```

`always_ram` - whether to keep quantized vectors always cached in RAM or not. By default, quantized vectors are loaded in the same way as the original vectors. However, in some setups you might want to keep quantized vectors in RAM to speed up the search process.
In this case, you can set `always_ram` to `true` to store quantized vectors in RAM.
####  [](https://qdrant.tech/documentation/guides/quantization/#set-up-bit-depth)Set up bit depth
To enable 2bit or 1.5bit quantization, you need to specify `encoding` parameter in the `quantization_config` section of the collection configuration. Available values are `two_bits` and `one_and_half_bits`.
httppythontypescriptrustjavacsharpgo
```
PUT /collections/{collection_name}
{
    "vectors": {
      "size": 1536,
      "distance": "Cosine"
    },
    "quantization_config": {
        "binary": {
            "encoding": "two_bits",
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
    vectors_config=models.VectorParams(size=1536, distance=models.Distance.COSINE),
    quantization_config=models.BinaryQuantization(
        binary=models.BinaryQuantizationConfig(
            encoding=models.BinaryQuantizationEncoding.TWO_BITS,
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
    size: 1536,
    distance: "Cosine",
  },
  quantization_config: {
    binary: {
      encoding: "two_bits",
      always_ram: true,
    },
  },
});

```

```
use qdrant_client::qdrant::{
    BinaryQuantizationBuilder,
    CreateCollectionBuilder,
    Distance,
    VectorParamsBuilder,
    BinaryQuantizationEncoding,
};
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

client
    .create_collection(
        CreateCollectionBuilder::new("{collection_name}")
            .vectors_config(VectorParamsBuilder::new(1536, Distance::Cosine))
            .quantization_config(BinaryQuantizationBuilder::new(true)
                .encoding(BinaryQuantizationEncoding::TwoBits)
            ),
    )
    .await?;

```

```
import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Collections.BinaryQuantization;
import io.qdrant.client.grpc.Collections.BinaryQuantizationEncoding;
import io.qdrant.client.grpc.Collections.CreateCollection;
import io.qdrant.client.grpc.Collections.Distance;
import io.qdrant.client.grpc.Collections.QuantizationConfig;
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
                            .setSize(1536)
                            .setDistance(Distance.Cosine)
                            .build())
                    .build())
            .setQuantizationConfig(
                QuantizationConfig.newBuilder()
                    .setBinary(BinaryQuantization
                        .newBuilder()
                        .setEncoding(BinaryQuantizationEncoding.TwoBits)
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
  vectorsConfig: new VectorParams { Size = 1536, Distance = Distance.Cosine },
  quantizationConfig: new QuantizationConfig
  {
    Binary = new BinaryQuantization {
      Encoding = BinaryQuantizationEncoding.TwoBits,
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

client.CreateCollection(context.Background(), &qdrant.CreateCollection{
    CollectionName: "{collection_name}",
    VectorsConfig: qdrant.NewVectorsConfig(&qdrant.VectorParams{
        Size:     1536,
        Distance: qdrant.Distance_Cosine,
    }),
    QuantizationConfig: qdrant.NewQuantizationBinary(
        &qdrant.BinaryQuantization{
            Encoding: qdrant.BinaryQuantizationEncoding_TwoBits.Enum(),
            AlwaysRam: qdrant.PtrOf(true),
        },
    ),
})

```

####  [](https://qdrant.tech/documentation/guides/quantization/#set-up-asymmetric-quantization)Set up asymmetric quantization
To enable asymmetric quantization, you need to specify `query_encoding` parameter in the `quantization_config` section of the collection configuration. Available values are:
  * `default` and `binary` - use regular binary quantization for the query.
  * `scalar8bits` - use 8bit quantization for the query.
  * `scalar4bits` - use 4bit quantization for the query.


httppythontypescriptrustjavacsharpgo
```
PUT /collections/{collection_name}
{
    "vectors": {
      "size": 1536,
      "distance": "Cosine"
    },
    "quantization_config": {
        "binary": {
            "query_encoding": "scalar8bits",
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
    vectors_config=models.VectorParams(size=1536, distance=models.Distance.COSINE),
    quantization_config=models.BinaryQuantization(
        binary=models.BinaryQuantizationConfig(
            query_encoding=models.BinaryQuantizationQueryEncoding.SCALAR8BITS,
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
    size: 1536,
    distance: "Cosine",
  },
  quantization_config: {
    binary: {
      query_encoding: "scalar8bits",
      always_ram: true,
    },
  },
});

```

```
use qdrant_client::qdrant::{
    BinaryQuantizationBuilder,
    CreateCollectionBuilder,
    Distance,
    VectorParamsBuilder,
    BinaryQuantizationQueryEncoding,
};
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

client
    .create_collection(
        CreateCollectionBuilder::new("{collection_name}")
            .vectors_config(VectorParamsBuilder::new(1536, Distance::Cosine))
            .quantization_config(
                BinaryQuantizationBuilder::new(true)
                    .query_encoding(BinaryQuantizationQueryEncoding::scalar8bits())
            ),
    )
    .await?;

```

```
import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Collections.BinaryQuantization;
import io.qdrant.client.grpc.Collections.BinaryQuantizationQueryEncoding;
import io.qdrant.client.grpc.Collections.CreateCollection;
import io.qdrant.client.grpc.Collections.Distance;
import io.qdrant.client.grpc.Collections.QuantizationConfig;
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
                            .setSize(1536)
                            .setDistance(Distance.Cosine)
                            .build())
                    .build())
            .setQuantizationConfig(
                QuantizationConfig.newBuilder()
                    .setBinary(BinaryQuantization.newBuilder()
                        .setQueryEncoding(BinaryQuantizationQueryEncoding
                            .newBuilder()
                            .setSetting(BinaryQuantizationQueryEncoding.Setting.Scalar8Bits)
                            .build())
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
  vectorsConfig: new VectorParams { Size = 1536, Distance = Distance.Cosine },
  quantizationConfig: new QuantizationConfig
  {
    Binary = new BinaryQuantization {
      QueryEncoding = new BinaryQuantizationQueryEncoding
      {
        Setting = BinaryQuantizationQueryEncoding.Types.Setting.Scalar8Bits,
      },
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

client.CreateCollection(context.Background(), &qdrant.CreateCollection{
    CollectionName: "{collection_name}",
    VectorsConfig: qdrant.NewVectorsConfig(&qdrant.VectorParams{
        Size:     1536,
        Distance: qdrant.Distance_Cosine,
    }),
    QuantizationConfig: qdrant.NewQuantizationBinary(
        &qdrant.BinaryQuantization{
            QueryEncoding: qdrant.NewBinaryQuantizationQueryEncodingSetting(qdrant.BinaryQuantizationQueryEncoding_Scalar8Bits),
            AlwaysRam: qdrant.PtrOf(true),
        },
    ),
})

```

###  [](https://qdrant.tech/documentation/guides/quantization/#setting-up-product-quantization)Setting up Product Quantization
To enable product quantization, you need to specify the quantization parameters in the `quantization_config` section of the collection configuration.
When enabling product quantization on an existing collection, use a PATCH request or the corresponding `update_collection` method and omit the vector configuration, as it’s already defined.
httppythontypescriptrustjavacsharpgo
```
PUT /collections/{collection_name}
{
    "vectors": {
      "size": 768,
      "distance": "Cosine"
    },
    "quantization_config": {
        "product": {
            "compression": "x16",
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
    vectors_config=models.VectorParams(size=768, distance=models.Distance.COSINE),
    quantization_config=models.ProductQuantization(
        product=models.ProductQuantizationConfig(
            compression=models.CompressionRatio.X16,
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
  },
  quantization_config: {
    product: {
      compression: "x16",
      always_ram: true,
    },
  },
});

```

```
use qdrant_client::qdrant::{
    CompressionRatio, CreateCollectionBuilder, Distance, ProductQuantizationBuilder,
    VectorParamsBuilder,
};
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

client
    .create_collection(
        CreateCollectionBuilder::new("{collection_name}")
            .vectors_config(VectorParamsBuilder::new(768, Distance::Cosine))
            .quantization_config(
                ProductQuantizationBuilder::new(CompressionRatio::X16.into()).always_ram(true),
            ),
    )
    .await?;

```

```
import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Collections.CompressionRatio;
import io.qdrant.client.grpc.Collections.CreateCollection;
import io.qdrant.client.grpc.Collections.Distance;
import io.qdrant.client.grpc.Collections.ProductQuantization;
import io.qdrant.client.grpc.Collections.QuantizationConfig;
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
                            .build())
                    .build())
            .setQuantizationConfig(
                QuantizationConfig.newBuilder()
                    .setProduct(
                        ProductQuantization.newBuilder()
                            .setCompression(CompressionRatio.x16)
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
 vectorsConfig: new VectorParams { Size = 768, Distance = Distance.Cosine },
 quantizationConfig: new QuantizationConfig
 {
  Product = new ProductQuantization { Compression = CompressionRatio.X16, AlwaysRam = true }
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
	}),
	QuantizationConfig: qdrant.NewQuantizationProduct(
		&qdrant.ProductQuantization{
			Compression: qdrant.CompressionRatio_x16,
			AlwaysRam:   qdrant.PtrOf(true),
		},
	),
})

```

There are two parameters that you can specify in the `quantization_config` section:
`compression` - compression ratio. Compression ratio represents the size of the quantized vector in bytes divided by the size of the original vector in bytes. In this case, the quantized vector will be 16 times smaller than the original vector.
`always_ram` - whether to keep quantized vectors always cached in RAM or not. By default, quantized vectors are loaded in the same way as the original vectors. However, in some setups you might want to keep quantized vectors in RAM to speed up the search process. Then set `always_ram` to `true`.
###  [](https://qdrant.tech/documentation/guides/quantization/#disabling-quantization)Disabling Quantization
To disable quantization in an existing collection, you can do the following:
httpbashpythontypescriptrustjavacsharpgo
```
PATCH /collections/{collection_name}
{
    "quantization_config": "Disabled"
}

```

```
curl -X PATCH http://localhost:6333/collections/{collection_name} \
  -H 'Content-Type: application/json' \
  --data-raw '{
    "quantization_config": "Disabled"
  }'

```

```
client.update_collection(
    collection_name="{collection_name}",
    quantization_config=models.Disabled.DISABLED,
)

```

```
client.updateCollection("{collection_name}", {
    quantization_config: 'Disabled'
});

```

```
use qdrant_client::qdrant::{Disabled, UpdateCollectionBuilder};

client
    .update_collection(UpdateCollectionBuilder::new("{collection_name}").quantization_config(Disabled {}))
    .await?;

```

```
import io.qdrant.client.grpc.Collections.Disabled;
import io.qdrant.client.grpc.Collections.QuantizationConfigDiff;
import io.qdrant.client.grpc.Collections.UpdateCollection;

client.updateCollectionAsync(
    UpdateCollection.newBuilder()
        .setCollectionName("{collection_name}")
        .setQuantizationConfig(
            QuantizationConfigDiff.newBuilder()
                .setDisabled(Disabled.getDefaultInstance())
                .build())
        .build());

```

```
using Qdrant.Client;
using Qdrant.Client.Grpc;

var client = new QdrantClient("localhost", 6334);

await client.UpdateCollectionAsync(
	collectionName: "{collection_name}",
	quantizationConfig: new QuantizationConfigDiff { Disabled = new Disabled() }
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
	CollectionName:     "{collection_name}",
	QuantizationConfig: qdrant.NewQuantizationDiffDisabled(),
})

```

###  [](https://qdrant.tech/documentation/guides/quantization/#searching-with-quantization)Searching with Quantization
Once you have configured quantization for a collection, you don’t need to do anything extra to search with quantization. Qdrant will automatically use quantized vectors if they are available.
However, there are a few options that you can use to control the search process:
httppythontypescriptrustjavacsharpgo
```
POST /collections/{collection_name}/points/query
{
    "query": [0.2, 0.1, 0.9, 0.7],
    "params": {
        "quantization": {
            "ignore": false,
            "rescore": true,
            "oversampling": 2.0
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
            ignore=False,
            rescore=True,
            oversampling=2.0,
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
            ignore: false,
            rescore: true,
            oversampling: 2.0,
        },
    },
    limit: 10,
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
            .limit(10)
            .params(
                SearchParamsBuilder::default().quantization(
                    QuantizationSearchParamsBuilder::default()
                        .ignore(false)
                        .rescore(true)
                        .oversampling(2.0),
                ),
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
                                        QuantizationSearchParams.newBuilder()
                                                .setIgnore(false)
                                                .setRescore(true)
                                                .setOversampling(2.0)
                                                .build())
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
		Quantization = new QuantizationSearchParams
		{
			Ignore = false,
			Rescore = true,
			Oversampling = 2.0
		}
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
			Ignore:       qdrant.PtrOf(false),
			Rescore:      qdrant.PtrOf(true),
			Oversampling: qdrant.PtrOf(2.0),
		},
	},
})

```

`ignore` - Toggle whether to ignore quantized vectors during the search process. By default, Qdrant will use quantized vectors if they are available.
`rescore` - Having the original vectors available, Qdrant can re-evaluate top-k search results using the original vectors. This can improve the search quality, but may slightly decrease the search speed, compared to the search without rescore. It is recommended to disable rescore only if the original vectors are stored on a slow storage (e.g. HDD or network storage). By default, rescore is enabled.
**Available as of v1.3.0**
`oversampling` - Defines how many extra vectors should be preselected using quantized index, and then re-scored using original vectors. For example, if oversampling is 2.4 and limit is 100, then 240 vectors will be preselected using quantized index, and then top-100 will be returned after re-scoring. Oversampling is useful if you want to tune the tradeoff between search speed and search quality in the query time.
