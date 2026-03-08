##  [](https://qdrant.tech/documentation/concepts/indexing/#payload-index)Payload Index
Payload index in Qdrant is similar to the index in conventional document-oriented databases. This index is built for a specific field and type, and is used for quick point requests by the corresponding filtering condition.
The index is also used to accurately estimate the filter cardinality, which helps the [query planning](https://qdrant.tech/documentation/concepts/search/#query-planning) choose a search strategy.
Creating an index requires additional computational resources and memory, so choosing fields to be indexed is essential. Qdrant does not make this choice but grants it to the user.
To mark a field as indexable, you can use the following:
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

You can use dot notation to specify a nested field for indexing. Similar to specifying [nested filters](https://qdrant.tech/documentation/concepts/filtering/#nested-key).
Available field types are:
  * `keyword` - for [keyword](https://qdrant.tech/documentation/concepts/payload/#keyword) payload, affects [Match](https://qdrant.tech/documentation/concepts/filtering/#match) filtering conditions.
  * `integer` - for [integer](https://qdrant.tech/documentation/concepts/payload/#integer) payload, affects [Match](https://qdrant.tech/documentation/concepts/filtering/#match) and [Range](https://qdrant.tech/documentation/concepts/filtering/#range) filtering conditions.
  * `float` - for [float](https://qdrant.tech/documentation/concepts/payload/#float) payload, affects [Range](https://qdrant.tech/documentation/concepts/filtering/#range) filtering conditions.
  * `bool` - for [bool](https://qdrant.tech/documentation/concepts/payload/#bool) payload, affects [Match](https://qdrant.tech/documentation/concepts/filtering/#match) filtering conditions (available as of v1.4.0).
  * `geo` - for [geo](https://qdrant.tech/documentation/concepts/payload/#geo) payload, affects [Geo Bounding Box](https://qdrant.tech/documentation/concepts/filtering/#geo-bounding-box) and [Geo Radius](https://qdrant.tech/documentation/concepts/filtering/#geo-radius) filtering conditions.
  * `datetime` - for [datetime](https://qdrant.tech/documentation/concepts/payload/#datetime) payload, affects [Range](https://qdrant.tech/documentation/concepts/filtering/#range) filtering conditions (available as of v1.8.0).
  * `text` - a special kind of index, available for [keyword](https://qdrant.tech/documentation/concepts/payload/#keyword) / string payloads, affects [Full Text search](https://qdrant.tech/documentation/concepts/filtering/#full-text-match) filtering conditions. Read more about [text index configuration](https://qdrant.tech/documentation/concepts/indexing/#full-text-index)
  * `uuid` - a special type of index, similar to `keyword`, but optimized for [UUID values](https://qdrant.tech/documentation/concepts/payload/#uuid). Affects [Match](https://qdrant.tech/documentation/concepts/filtering/#match) filtering conditions. (available as of v1.11.0)


Payload index may occupy some additional memory, so it is recommended to only use the index for those fields that are used in filtering conditions. If you need to filter by many fields and the memory limits do not allow for indexing all of them, it is recommended to choose the field that limits the search result the most. As a rule, the more different values a payload value has, the more efficiently the index will be used.
###  [](https://qdrant.tech/documentation/concepts/indexing/#parameterized-index)Parameterized index
_Available as of v1.8.0_
We’ve added a parameterized variant to the `integer` index, which allows you to fine-tune indexing and search performance.
Both the regular and parameterized `integer` indexes use the following flags:
  * `lookup`: enables support for direct lookup using [Match](https://qdrant.tech/documentation/concepts/filtering/#match) filters.
  * `range`: enables support for [Range](https://qdrant.tech/documentation/concepts/filtering/#range) filters.


The regular `integer` index assumes both `lookup` and `range` are `true`. In contrast, to configure a parameterized index, you would set only one of these filters to `true`:
`lookup` | `range` | Result
---|---|---
`true` | `true` | Regular integer index
`true` | `false` | Parameterized integer index
`false` | `true` | Parameterized integer index
`false` | `false` | No integer index
The parameterized index can enhance performance in collections with millions of points. We encourage you to try it out. If it does not enhance performance in your use case, you can always restore the regular `integer` index.
Note: If you set `"lookup": true` with a range filter, that may lead to significant performance issues.
For example, the following code sets up a parameterized integer index which supports only range filters:
httppythontypescriptrustjavacsharpgo
```
PUT /collections/{collection_name}/index
{
    "field_name": "name_of_the_field_to_index",
    "field_schema": {
        "type": "integer",
        "lookup": false,
        "range": true
    }
}

```

```
from qdrant_client import QdrantClient, models

client = QdrantClient(url="http://localhost:6333")

client.create_payload_index(
    collection_name="{collection_name}",
    field_name="name_of_the_field_to_index",
    field_schema=models.IntegerIndexParams(
        type=models.IntegerIndexType.INTEGER,
        lookup=False,
        range=True,
    ),
)

```

```
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.createPayloadIndex("{collection_name}", {
  field_name: "name_of_the_field_to_index",
  field_schema: {
    type: "integer",
    lookup: false,
    range: true,
  },
});

```

```
use qdrant_client::Qdrant;
use qdrant_client::qdrant::{
    CreateFieldIndexCollectionBuilder, FieldType, IntegerIndexParamsBuilder,
};

let client = Qdrant::from_url("http://localhost:6334").build()?;

client
    .create_field_index(
        CreateFieldIndexCollectionBuilder::new(
            "{collection_name}",
            "name_of_the_field_to_index",
            FieldType::Integer,
        )
        .field_index_params(IntegerIndexParamsBuilder::new(false, true).build()),
    )
    .await?;

```

```
import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Collections.IntegerIndexParams;
import io.qdrant.client.grpc.Collections.PayloadIndexParams;
import io.qdrant.client.grpc.Collections.PayloadSchemaType;

QdrantClient client =
    new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client
    .createPayloadIndexAsync(
        "{collection_name}",
        "name_of_the_field_to_index",
        PayloadSchemaType.Integer,
        PayloadIndexParams.newBuilder()
            .setIntegerIndexParams(
                IntegerIndexParams.newBuilder().setLookup(false).setRange(true).build())
            .build(),
        null,
        null,
        null)
    .get();

```

```
using Qdrant.Client;
using Qdrant.Client.Grpc;

var client = new QdrantClient("localhost", 6334);

await client.CreatePayloadIndexAsync(
    collectionName: "{collection_name}",
    fieldName: "name_of_the_field_to_index",
    schemaType: PayloadSchemaType.Integer,
    indexParams: new PayloadIndexParams
    {
	    IntegerIndexParams = new()
	    {
		    Lookup = false,
		    Range = true
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

client.CreateFieldIndex(context.Background(), &qdrant.CreateFieldIndexCollection{
	CollectionName: "{collection_name}",
	FieldName:      "name_of_the_field_to_index",
	FieldType:      qdrant.FieldType_FieldTypeInteger.Enum(),
	FieldIndexParams: qdrant.NewPayloadIndexParamsInt(
		&qdrant.IntegerIndexParams{
			Lookup: qdrant.PtrOf(false),
			Range:  qdrant.PtrOf(true),
		}),
})

```

###  [](https://qdrant.tech/documentation/concepts/indexing/#on-disk-payload-index)On-disk payload index
_Available as of v1.11.0_
By default all payload-related structures are stored in memory. In this way, the vector index can quickly access payload values during search. As latency in this case is critical, it is recommended to keep hot payload indexes in memory.
There are, however, cases when payload indexes are too large or rarely used. In those cases, it is possible to store payload indexes on disk.
To configure on-disk payload index, you can use the following index parameters:
httppythontypescriptrustjavacsharpgo
```
PUT /collections/{collection_name}/index
{
    "field_name": "payload_field_name",
    "field_schema": {
        "type": "keyword",
        "on_disk": true
    }
}

```

```
client.create_payload_index(
    collection_name="{collection_name}",
    field_name="payload_field_name",
    field_schema=models.KeywordIndexParams(
        type=models.KeywordIndexType.KEYWORD,
        on_disk=True,
    ),
)

```

```
client.createPayloadIndex("{collection_name}", {
  field_name: "payload_field_name",
  field_schema: {
    type: "keyword",
    on_disk: true
  },
});

```

```
use qdrant_client::qdrant::{
    CreateFieldIndexCollectionBuilder,
    KeywordIndexParamsBuilder,
    FieldType
};
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

client.create_field_index(
    CreateFieldIndexCollectionBuilder::new(
        "{collection_name}",
        "payload_field_name",
        FieldType::Keyword,
    )
    .field_index_params(
        KeywordIndexParamsBuilder::default()
            .on_disk(true),
    ),
).await?;

```

```
import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Collections.KeywordIndexParams;
import io.qdrant.client.grpc.Collections.PayloadIndexParams;
import io.qdrant.client.grpc.Collections.PayloadSchemaType;

QdrantClient client =
    new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client
    .createPayloadIndexAsync(
        "{collection_name}",
        "payload_field_name",
        PayloadSchemaType.Keyword,
        PayloadIndexParams.newBuilder()
            .setKeywordIndexParams(
                KeywordIndexParams.newBuilder()
                    .setOnDisk(true)
                    .build())
            .build(),
        null,
        null,
        null)
    .get();

```

```
using Qdrant.Client;
using Qdrant.Client.Grpc;

var client = new QdrantClient("localhost", 6334);

await client.CreatePayloadIndexAsync(
 collectionName: "{collection_name}",
 fieldName: "payload_field_name",
 schemaType: PayloadSchemaType.Keyword,
 indexParams: new PayloadIndexParams
 {
  KeywordIndexParams = new KeywordIndexParams
  {
   OnDisk   = true
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

client.CreateFieldIndex(context.Background(), &qdrant.CreateFieldIndexCollection{
	CollectionName: "{collection_name}",
	FieldName:      "name_of_the_field_to_index",
	FieldType:      qdrant.FieldType_FieldTypeKeyword.Enum(),
	FieldIndexParams: qdrant.NewPayloadIndexParamsKeyword(
		&qdrant.KeywordIndexParams{
			OnDisk: qdrant.PtrOf(true),
		}),
})

```

Payload index on-disk is supported for the following types:
  * `keyword`
  * `integer`
  * `float`
  * `datetime`
  * `uuid`
  * `text`
  * `geo`


The list will be extended in future versions.
###  [](https://qdrant.tech/documentation/concepts/indexing/#tenant-index)Tenant Index
_Available as of v1.11.0_
Many vector search use-cases require multitenancy. In a multi-tenant scenario the collection is expected to contain multiple subsets of data, where each subset belongs to a different tenant.
Qdrant supports efficient multi-tenant search by enabling [special configuration](https://qdrant.tech/documentation/guides/multiple-partitions/) vector index, which disables global search and only builds sub-indexes for each tenant.
However, knowing that the collection contains multiple tenants unlocks more opportunities for optimization. To optimize storage in Qdrant further, you can enable tenant indexing for payload fields.
This option will tell Qdrant which fields are used for tenant identification and will allow Qdrant to structure storage for faster search of tenant-specific data. One example of such optimization is localizing tenant-specific data closer on disk, which will reduce the number of disk reads during search.
To enable tenant index for a field, you can use the following index parameters:
httppythontypescriptrustjavacsharpgo
```
PUT /collections/{collection_name}/index
{
    "field_name": "payload_field_name",
    "field_schema": {
        "type": "keyword",
        "is_tenant": true
    }
}

```

```
client.create_payload_index(
    collection_name="{collection_name}",
    field_name="payload_field_name",
    field_schema=models.KeywordIndexParams(
        type=models.KeywordIndexType.KEYWORD,
        is_tenant=True,
    ),
)

```

```
client.createPayloadIndex("{collection_name}", {
  field_name: "payload_field_name",
  field_schema: {
    type: "keyword",
    is_tenant: true
  },
});

```

```
use qdrant_client::qdrant::{
    CreateFieldIndexCollectionBuilder,
    KeywordIndexParamsBuilder,
    FieldType
};

use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

client.create_field_index(
    CreateFieldIndexCollectionBuilder::new(
        "{collection_name}",
        "payload_field_name",
        FieldType::Keyword,
    )
    .field_index_params(
        KeywordIndexParamsBuilder::default()
            .is_tenant(true),
    ),
).await?;

```

```
import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Collections.KeywordIndexParams;
import io.qdrant.client.grpc.Collections.PayloadIndexParams;
import io.qdrant.client.grpc.Collections.PayloadSchemaType;

QdrantClient client =
    new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client
    .createPayloadIndexAsync(
        "{collection_name}",
        "payload_field_name",
        PayloadSchemaType.Keyword,
        PayloadIndexParams.newBuilder()
            .setKeywordIndexParams(
                KeywordIndexParams.newBuilder()
                    .setIsTenant(true)
                    .build())
            .build(),
        null,
        null,
        null)
    .get();

```

```
using Qdrant.Client;
using Qdrant.Client.Grpc;

var client = new QdrantClient("localhost", 6334);

await client.CreatePayloadIndexAsync(
 collectionName: "{collection_name}",
 fieldName: "payload_field_name",
 schemaType: PayloadSchemaType.Keyword,
 indexParams: new PayloadIndexParams
 {
  KeywordIndexParams = new KeywordIndexParams
  {
   IsTenant = true
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

client.CreateFieldIndex(context.Background(), &qdrant.CreateFieldIndexCollection{
	CollectionName: "{collection_name}",
	FieldName:      "name_of_the_field_to_index",
	FieldType:      qdrant.FieldType_FieldTypeKeyword.Enum(),
	FieldIndexParams: qdrant.NewPayloadIndexParamsKeyword(
		&qdrant.KeywordIndexParams{
			IsTenant: qdrant.PtrOf(true),
		}),
})

```

Tenant optimization is supported for the following datatypes:
  * `keyword`
  * `uuid`


###  [](https://qdrant.tech/documentation/concepts/indexing/#principal-index)Principal Index
_Available as of v1.11.0_
Similar to the tenant index, the principal index is used to optimize storage for faster search, assuming that the search request is primarily filtered by the principal field.
A good example of a use case for the principal index is time-related data, where each point is associated with a timestamp. In this case, the principal index can be used to optimize storage for faster search with time-based filters.
httppythontypescriptrustjavacsharpgo
```
PUT /collections/{collection_name}/index
{
    "field_name": "timestamp",
    "field_schema": {
        "type": "integer",
        "is_principal": true
    }
}

```

```
client.create_payload_index(
    collection_name="{collection_name}",
    field_name="timestamp",
    field_schema=models.IntegerIndexParams(
        type=models.IntegerIndexType.INTEGER,
        is_principal=True,
    ),
)

```

```
client.createPayloadIndex("{collection_name}", {
  field_name: "timestamp",
  field_schema: {
    type: "integer",
    is_principal: true
  },
});

```

```
use qdrant_client::qdrant::{
    CreateFieldIndexCollectionBuilder,
    IntegerIndexParamsBuilder,
    FieldType
};
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

client.create_field_index(
    CreateFieldIndexCollectionBuilder::new(
        "{collection_name}",
        "timestamp",
        FieldType::Integer,
    )
    .field_index_params(
        IntegerIndexParamsBuilder::default()
            .is_principal(true),
    ),
).await?;

```

```
import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Collections.IntegerIndexParams;
import io.qdrant.client.grpc.Collections.KeywordIndexParams;
import io.qdrant.client.grpc.Collections.PayloadIndexParams;
import io.qdrant.client.grpc.Collections.PayloadSchemaType;

QdrantClient client =
    new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client
    .createPayloadIndexAsync(
        "{collection_name}",
        "timestamp",
        PayloadSchemaType.Integer,
        PayloadIndexParams.newBuilder()
            .setIntegerIndexParams(
                IntegerIndexParams.newBuilder()
                    .setIsPrincipal(true)
                    .build())
            .build(),
        null,
        null,
        null)
    .get();

```

```
using Qdrant.Client;
using Qdrant.Client.Grpc;

var client = new QdrantClient("localhost", 6334);

await client.CreatePayloadIndexAsync(
 collectionName: "{collection_name}",
 fieldName: "timestamp",
 schemaType: PayloadSchemaType.Integer,
 indexParams: new PayloadIndexParams
 {
  IntegerIndexParams = new IntegerIndexParams
  {
   IsPrincipal = true
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

client.CreateFieldIndex(context.Background(), &qdrant.CreateFieldIndexCollection{
	CollectionName: "{collection_name}",
	FieldName:      "name_of_the_field_to_index",
	FieldType:      qdrant.FieldType_FieldTypeInteger.Enum(),
	FieldIndexParams: qdrant.NewPayloadIndexParamsInt(
		&qdrant.IntegerIndexParams{
			IsPrincipal: qdrant.PtrOf(true),
		}),
})

```

Principal optimization is supported for following types:
  * `integer`
  * `float`
  * `datetime`
