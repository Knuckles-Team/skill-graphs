##  [](https://qdrant.tech/documentation/concepts/collections/#check-collection-existence)Check collection existence
_Available as of v1.8.0_
httpbashpythontypescriptrustjavacsharpgo
```
GET http://localhost:6333/collections/{collection_name}/exists

```

```
curl -X GET http://localhost:6333/collections/{collection_name}/exists

```

```
client.collection_exists(collection_name="{collection_name}")

```

```
client.collectionExists("{collection_name}");

```

```
client.collection_exists("{collection_name}").await?;

```

```
client.collectionExistsAsync("{collection_name}").get();

```

```
await client.CollectionExistsAsync("{collection_name}");

```

```
import "context"

client.CollectionExists(context.Background(), "my_collection")

```
