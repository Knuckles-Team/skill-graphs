            "time travel",
            "sentence-transformers/all-minilm-l6-v2",
        )))
        .using("description-dense")
        .filter(strict_filter)
        .with_payload(true)
        .build(),
    QueryPointsBuilder::new("books")
        .query(Query::new_nearest(Document::new(
            "time travel",
            "sentence-transformers/all-minilm-l6-v2",
        )))
        .using("description-dense")
        .filter(relaxed_filter)
        .with_payload(true)
        .build(),
    QueryPointsBuilder::new("books")
        .query(Query::new_nearest(Document::new(
            "time travel",
            "sentence-transformers/all-minilm-l6-v2",
        )))
        .using("description-dense")
        .with_payload(true)
        .build(),
];

client
    .query_batch(QueryBatchPointsBuilder::new("books", searches))
    .await?;

```

```
import static io.qdrant.client.ConditionFactory.*;
import static io.qdrant.client.QueryFactory.nearest;
import static io.qdrant.client.WithPayloadSelectorFactory.enable;

import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Common.Filter;
import io.qdrant.client.grpc.Points.*;
import java.util.*;

QdrantClient client =

QueryPoints searchStrict =
    QueryPoints.newBuilder()
        .setCollectionName("books")
        .setQuery(
            nearest(
                Document.newBuilder()
                    .setText("time travel")
                    .setModel("sentence-transformers/all-minilm-l6-v2")
                    .build()))
        .setUsing("description-dense")
        .setFilter(Filter.newBuilder().addMust(matchText("title", "time travel")).build())
        .setWithPayload(enable(true))
        .build();

QueryPoints searchRelaxed =
    QueryPoints.newBuilder()
        .setCollectionName("books")
        .setQuery(
            nearest(
                Document.newBuilder()
                    .setText("time travel")
                    .setModel("sentence-transformers/all-minilm-l6-v2")
                    .build()))
        .setUsing("description-dense")
        .setFilter(Filter.newBuilder().addMust(matchTextAny("title", "time travel")).build())
        .setWithPayload(enable(true))
        .build();

QueryPoints searchVectorOnly =
    QueryPoints.newBuilder()
        .setCollectionName("books")
        .setQuery(
            nearest(
                Document.newBuilder()
                    .setText("time travel")
                    .setModel("sentence-transformers/all-minilm-l6-v2")
                    .build()))
        .setUsing("description-dense")
        .setWithPayload(enable(true))
        .build();

client.queryBatchAsync("books", List.of(searchStrict, searchRelaxed, searchVectorOnly)).get();

```

```
using Qdrant.Client;
using Qdrant.Client.Grpc;
using static Qdrant.Client.Grpc.Conditions;

var searchStrict = new QueryPoints
{
    CollectionName = "books",
    Query = new Document
    {
        Text = "time travel",
        Model = "sentence-transformers/all-minilm-l6-v2",
    },
    Using = "description-dense",
    Filter = new Filter { Must = { MatchText("title", "time travel") } },
};

var searchRelaxed = new QueryPoints
{
    CollectionName = "books",
    Query = new Document
    {
        Text = "time travel",
        Model = "sentence-transformers/all-minilm-l6-v2",
    },
    Using = "description-dense",
    Filter = new Filter { Must = { MatchTextAny("title", "time travel") } },
};

var searchVectorOnly = new QueryPoints
{
    CollectionName = "books",
    Query = new Document
    {
        Text = "time travel",
        Model = "sentence-transformers/all-minilm-l6-v2",
    },
    Using = "description-dense",
};

await client.QueryBatchAsync(
    collectionName: "books",
    queries: new List<QueryPoints> { searchStrict, searchRelaxed, searchVectorOnly }
);

```

```
strict := &qdrant.QueryPoints{
	CollectionName: "books",
	Query: qdrant.NewQueryNearest(
		qdrant.NewVectorInputDocument(&qdrant.Document{Model: "sentence-transformers/all-minilm-l6-v2", Text: "time travel"}),
	),
	Using:  qdrant.PtrOf("description-dense"),
	Filter: &qdrant.Filter{Must: []*qdrant.Condition{qdrant.NewMatchText("title", "time travel")}},
}

relaxed := &qdrant.QueryPoints{
	CollectionName: "books",
	Query: qdrant.NewQueryNearest(
		qdrant.NewVectorInputDocument(&qdrant.Document{Model: "sentence-transformers/all-minilm-l6-v2", Text: "time travel"}),
	),
	Using:  qdrant.PtrOf("description-dense"),
	Filter: &qdrant.Filter{Must: []*qdrant.Condition{qdrant.NewMatchTextAny("title", "time travel")}},
}

vectorOnly := &qdrant.QueryPoints{
	CollectionName: "books",
	Query: qdrant.NewQueryNearest(
		qdrant.NewVectorInputDocument(&qdrant.Document{Model: "sentence-transformers/all-minilm-l6-v2", Text: "time travel"}),
	),
	Using: qdrant.PtrOf("description-dense"),
}

client.QueryBatch(context.Background(), &qdrant.QueryBatchPoints{
	CollectionName: "books",
	QueryPoints:    []*qdrant.QueryPoints{strict, relaxed, vectorOnly},
})

```

The response contains three separate result sets. You can return the first non-empty result set to the user, or you can use the three sets to assemble a single ranked list.
