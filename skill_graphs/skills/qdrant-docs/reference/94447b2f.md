##  [](https://qdrant.tech/documentation/concepts/collections/#collection-aliases)Collection aliases
In a production environment, it is sometimes necessary to switch different versions of vectors seamlessly. For example, when upgrading to a new version of the neural network.
There is no way to stop the service and rebuild the collection with new vectors in these situations. Aliases are additional names for existing collections. All queries to the collection can also be done identically, using an alias instead of the collection name.
Thus, it is possible to build a second collection in the background and then switch alias from the old to the new collection. Since all changes of aliases happen atomically, no concurrent requests will be affected during the switch.
###  [](https://qdrant.tech/documentation/concepts/collections/#create-alias)Create alias
httpbashpythontypescriptrustjavacsharpgo
```
POST /collections/aliases
{
    "actions": [
        {
            "create_alias": {
                "collection_name": "example_collection",
                "alias_name": "production_collection"
            }
        }
    ]
}

```

```
curl -X POST http://localhost:6333/collections/aliases \
  -H 'Content-Type: application/json' \
  --data-raw '{
    "actions": [
        {
            "create_alias": {
                "collection_name": "example_collection",
                "alias_name": "production_collection"
            }
        }
    ]
}'

```

```
client.update_collection_aliases(
    change_aliases_operations=[
        models.CreateAliasOperation(
            create_alias=models.CreateAlias(
                collection_name="example_collection", alias_name="production_collection"
            )
        )
    ]
)

```

```
client.updateCollectionAliases({
  actions: [
    {
      create_alias: {
        collection_name: "example_collection",
        alias_name: "production_collection",
      },
    },
  ],
});

```

```
use qdrant_client::qdrant::CreateAliasBuilder;

client
    .create_alias(CreateAliasBuilder::new(
        "example_collection",
        "production_collection",
    ))
    .await?;

```

```
client.createAliasAsync("production_collection", "example_collection").get();

```

```
await client.CreateAliasAsync(aliasName: "production_collection", collectionName: "example_collection");

```

```
import "context"

client.CreateAlias(context.Background(), "production_collection", "example_collection")

```

###  [](https://qdrant.tech/documentation/concepts/collections/#remove-alias)Remove alias
httpbashpythontypescriptrustjavacsharpgo
```
POST /collections/aliases
{
    "actions": [
        {
            "delete_alias": {
                "alias_name": "production_collection"
            }
        }
    ]
}

```

```
curl -X POST http://localhost:6333/collections/aliases \
  -H 'Content-Type: application/json' \
  --data-raw '{
    "actions": [
        {
            "delete_alias": {
                "alias_name": "production_collection"
            }
        }
    ]
}'

```

```
client.update_collection_aliases(
    change_aliases_operations=[
        models.DeleteAliasOperation(
            delete_alias=models.DeleteAlias(alias_name="production_collection")
        ),
    ]
)

```

```
client.updateCollectionAliases({
  actions: [
    {
      delete_alias: {
        alias_name: "production_collection",
      },
    },
  ],
});

```

```
client.delete_alias("production_collection").await?;

```

```
client.deleteAliasAsync("production_collection").get();

```

```
await client.DeleteAliasAsync("production_collection");

```

```
import "context"

client.DeleteAlias(context.Background(), "production_collection")

```

###  [](https://qdrant.tech/documentation/concepts/collections/#switch-collection)Switch collection
Multiple alias actions are performed atomically. For example, you can switch underlying collection with the following command:
httpbashpythontypescriptrustjavacsharpgo
```
POST /collections/aliases
{
    "actions": [
        {
            "delete_alias": {
                "alias_name": "production_collection"
            }
        },
        {
            "create_alias": {
                "collection_name": "example_collection",
                "alias_name": "production_collection"
            }
        }
    ]
}

```

```
curl -X POST http://localhost:6333/collections/aliases \
  -H 'Content-Type: application/json' \
  --data-raw '{
    "actions": [
        {
            "delete_alias": {
                "alias_name": "production_collection"
            }
        },
        {
            "create_alias": {
                "collection_name": "example_collection",
                "alias_name": "production_collection"
            }
        }
    ]
}'

```

```
client.update_collection_aliases(
    change_aliases_operations=[
        models.DeleteAliasOperation(
            delete_alias=models.DeleteAlias(alias_name="production_collection")
        ),
        models.CreateAliasOperation(
            create_alias=models.CreateAlias(
                collection_name="example_collection", alias_name="production_collection"
            )
        ),
    ]
)

```

```
client.updateCollectionAliases({
  actions: [
    {
      delete_alias: {
        alias_name: "production_collection",
      },
    },
    {
      create_alias: {
        collection_name: "example_collection",
        alias_name: "production_collection",
      },
    },
  ],
});

```

```
use qdrant_client::qdrant::CreateAliasBuilder;

client.delete_alias("production_collection").await?;
client
    .create_alias(CreateAliasBuilder::new(
        "example_collection",
        "production_collection",
    ))
    .await?;

```

```
client.deleteAliasAsync("production_collection").get();
client.createAliasAsync("production_collection", "example_collection").get();

```

```
await client.DeleteAliasAsync("production_collection");
await client.CreateAliasAsync(aliasName: "production_collection", collectionName: "example_collection");

```

```
import "context"

client.DeleteAlias(context.Background(), "production_collection")
client.CreateAlias(context.Background(), "production_collection", "example_collection")

```

###  [](https://qdrant.tech/documentation/concepts/collections/#list-collection-aliases)List collection aliases
httpbashpythontypescriptrustjavacsharpgo
```
GET /collections/{collection_name}/aliases

```

```
curl -X GET http://localhost:6333/collections/{collection_name}/aliases

```

```
from qdrant_client import QdrantClient

client = QdrantClient(url="http://localhost:6333")

client.get_collection_aliases(collection_name="{collection_name}")

```

```
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.getCollectionAliases("{collection_name}");

```

```
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

client.list_collection_aliases("{collection_name}").await?;

```

```
import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;

QdrantClient client =
    new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client.listCollectionAliasesAsync("{collection_name}").get();

```

```
using Qdrant.Client;

var client = new QdrantClient("localhost", 6334);

await client.ListCollectionAliasesAsync("{collection_name}");

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

client.ListCollectionAliases(context.Background(), "{collection_name}")

```

###  [](https://qdrant.tech/documentation/concepts/collections/#list-all-aliases)List all aliases
httpbashpythontypescriptrustjavacsharpgo
```
GET /aliases

```

```
curl -X GET http://localhost:6333/aliases

```

```
from qdrant_client import QdrantClient

client = QdrantClient(url="http://localhost:6333")

client.get_aliases()

```

```
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.getAliases();

```

```
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

client.list_aliases().await?;

```

```
import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;

QdrantClient client =
    new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client.listAliasesAsync().get();

```

```
using Qdrant.Client;

var client = new QdrantClient("localhost", 6334);

await client.ListAliasesAsync();

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

client.ListAliases(context.Background())

```

###  [](https://qdrant.tech/documentation/concepts/collections/#list-all-collections)List all collections
httpbashpythontypescriptrustjavacsharpgo
```
GET /collections

```

```
curl -X GET http://localhost:6333/collections

```

```
from qdrant_client import QdrantClient

client = QdrantClient(url="http://localhost:6333")

client.get_collections()

```

```
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.getCollections();

```

```
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

client.list_collections().await?;

```

```
import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;

QdrantClient client =
    new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client.listCollectionsAsync().get();

```

```
using Qdrant.Client;

var client = new QdrantClient("localhost", 6334);

await client.ListCollectionsAsync();

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

client.ListCollections(context.Background())

```

##### Was this page useful?
![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg) Yes  ![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg) No
Thank you for your feedback! 🙏
We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/concepts/collections.md) this page on GitHub, or
On this page:
  * [Collections](https://qdrant.tech/documentation/concepts/collections/#collections)
    * [Setting up multitenancy](https://qdrant.tech/documentation/concepts/collections/#setting-up-multitenancy)
    * [Create a collection](https://qdrant.tech/documentation/concepts/collections/#create-a-collection)
      * [Collection with multiple vectors](https://qdrant.tech/documentation/concepts/collections/#collection-with-multiple-vectors)
      * [Vector datatypes](https://qdrant.tech/documentation/concepts/collections/#vector-datatypes)
      * [Collection with sparse vectors](https://qdrant.tech/documentation/concepts/collections/#collection-with-sparse-vectors)
      * [Create collection from another collection](https://qdrant.tech/documentation/concepts/collections/#create-collection-from-another-collection)
    * [Check collection existence](https://qdrant.tech/documentation/concepts/collections/#check-collection-existence)
    * [Delete collection](https://qdrant.tech/documentation/concepts/collections/#delete-collection)
    * [Update collection parameters](https://qdrant.tech/documentation/concepts/collections/#update-collection-parameters)
    * [Collection info](https://qdrant.tech/documentation/concepts/collections/#collection-info)
      * [Grey collection status](https://qdrant.tech/documentation/concepts/collections/#grey-collection-status)
      * [Approximate point and vector counts](https://qdrant.tech/documentation/concepts/collections/#approximate-point-and-vector-counts)
      * [Indexing vectors in HNSW](https://qdrant.tech/documentation/concepts/collections/#indexing-vectors-in-hnsw)
      * [Collection metadata](https://qdrant.tech/documentation/concepts/collections/#collection-metadata)
    * [Collection aliases](https://qdrant.tech/documentation/concepts/collections/#collection-aliases)
      * [Create alias](https://qdrant.tech/documentation/concepts/collections/#create-alias)
      * [Remove alias](https://qdrant.tech/documentation/concepts/collections/#remove-alias)
      * [Switch collection](https://qdrant.tech/documentation/concepts/collections/#switch-collection)
      * [List collection aliases](https://qdrant.tech/documentation/concepts/collections/#list-collection-aliases)
      * [List all aliases](https://qdrant.tech/documentation/concepts/collections/#list-all-aliases)
      * [List all collections](https://qdrant.tech/documentation/concepts/collections/#list-all-collections)


#### Ready to get started with Qdrant?
© 2025 Qdrant.
[Terms](https://qdrant.tech/legal/terms_and_conditions/) [Privacy Policy](https://qdrant.tech/legal/privacy-policy/) [Impressum](https://qdrant.tech/legal/impressum/)
×
[ Powered by ](https://qdrant.tech/)
