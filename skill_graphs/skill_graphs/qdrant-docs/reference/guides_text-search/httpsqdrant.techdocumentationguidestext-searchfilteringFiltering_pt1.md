##  [](https://qdrant.tech/documentation/guides/text-search/#filtering)Filtering
Qdrant supports [filtering](https://qdrant.tech/documentation/concepts/filtering) on a wide range of datatypes: numbers, dates, booleans, geolocations, and strings. In Qdrant, a filter is typically combined with a vector query. The vector query is used to score and rank the results, while the filter is used to narrow down the results based on specific criteria.
###  [](https://qdrant.tech/documentation/guides/text-search/#text-and-keyword-strings)Text and Keyword Strings
When it comes to filtering on strings, it is important to understand the difference between the two types of strings in Qdrant: text and keyword. These two string types are designed for different use cases: filtering on exact string values or filtering on individual search terms. To filter on exact string values, Qdrant uses **keyword** strings. Keyword strings are ideal for filtering on strings like IDs, categories, or tags. To filter on individual terms or phrases within a larger body of text, Qdrant uses **text** strings.
For example, take a string like “United States”. If you want to filter on all points with this exact string in the payload, use a keyword filter. On the other hand, if you want to filter on all points that contain the word “united” (matching “United States” as well as “United Kingdom”), use a text filter.
Keyword | Text
---|---
Used for exact string matches | Used for filtering on individual terms
Ideal for IDs, categories, tags | Ideal for larger text fields
Not tokenized |  [Tokenized](https://qdrant.tech/documentation/concepts/text-search/#tokenization) into individual terms
Case-sensitive | Case-insensitive by default
###  [](https://qdrant.tech/documentation/guides/text-search/#filtering-on-an-exact-string)Filtering on an Exact String
To filter on exact strings, first create a [payload index](https://qdrant.tech/documentation/concepts/indexing/#payload-index) of type `keyword`for the field you want to filter on. A payload index makes filtering faster and reduces the load on the system.
For example, to filter books by author name, create a keyword index on the “author” field:
httppythontypescriptrustjavacsharpgo
```
PUT /collections/books/index?wait=true
{
    "field_name": "author",
    "field_schema": "keyword"
}

```

```
from qdrant_client import QdrantClient, models

client = QdrantClient(
    url="https://xyz-example.qdrant.io:6333",
    api_key="<your-api-key>",
    cloud_inference=True,
)

client.create_payload_index(
    collection_name="books",
    field_name="author",
    field_schema=models.PayloadSchemaType.KEYWORD
)

```

```
client.createPayloadIndex("books", {
  field_name: "author",
  field_schema: "keyword",
});

```

```
use qdrant_client::Qdrant;
use qdrant_client::qdrant::{CreateFieldIndexCollectionBuilder, FieldType};

client
    .create_field_index(CreateFieldIndexCollectionBuilder::new(
        "books",
        "author",
        FieldType::Keyword,
    ))
    .await?;

```

```
import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Collections.PayloadSchemaType;

QdrantClient client =

client
    .createPayloadIndexAsync(
        "books", "author", PayloadSchemaType.Keyword, null, null, null, null)
    .get();

```

```
using Qdrant.Client;
using Qdrant.Client.Grpc;

await client.CreatePayloadIndexAsync(
    collectionName: "books",
    fieldName: "author",
    schemaType: PayloadSchemaType.Keyword
);

```

```
client.CreateFieldIndex(context.Background(), &qdrant.CreateFieldIndexCollection{
	CollectionName: "books",
	FieldName:      "author",
	FieldType:      qdrant.FieldType_FieldTypeKeyword.Enum(),
})

```

Next, when querying the data, you also add a filter clause to the request. The following example searches for books related to “time travel” but only returns books written by H.G. Wells:
httppythontypescriptrustjavacsharpgo
```
POST /collections/books/points/query
{
  "query": {
    "text": "time travel",
    "model": "sentence-transformers/all-minilm-l6-v2"
  },
  "using": "description-dense",
  "with_payload": true,
  "filter": {
    "must": [
      {
        "key": "author",
        "match": {
          "value": "H.G. Wells"
        }
      }
    ]
  }
}

```

```
from qdrant_client import QdrantClient, models

client = QdrantClient(
    url="https://xyz-example.qdrant.io:6333",
    api_key="<your-api-key>",
    cloud_inference=True,
)

client.query_points(
    collection_name="books",
    query=models.Document(text="time travel", model="sentence-transformers/all-minilm-l6-v2"),
    using="description-dense",
    with_payload=True,
    query_filter=models.Filter(
        must=[models.FieldCondition(key="author", match=models.MatchValue(value="H.G. Wells"))]
    ),
)

```

```
client.query("books", {
  query: {
    text: "time travel",
    model: "sentence-transformers/all-minilm-l6-v2",
  },
  using: "description-dense",
  with_payload: true,
  filter: {
    must: [
      {
        key: "author",
        match: {
          value: "H.G. Wells",
        },
      },
    ],
  },
});

```

```
use qdrant_client::Qdrant;
use qdrant_client::qdrant::{Condition, Document, Filter, Query, QueryPointsBuilder};

let filter = Filter::must([Condition::matches("author", "H.G. Wells".to_string())]);

client
    .query(
        QueryPointsBuilder::new("books")
            .query(Query::new_nearest(Document::new(
                "time travel",
                "sentence-transformers/all-minilm-l6-v2",
            )))
            .using("description-dense")
            .filter(filter)
            .with_payload(true)
            .build(),
    )
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

QdrantClient client =

Filter filter = Filter.newBuilder().addMust(matchKeyword("author", "H.G. Wells")).build();

client
    .queryAsync(
        QueryPoints.newBuilder()
            .setCollectionName("books")
            .setQuery(
                nearest(
                    Document.newBuilder()
                        .setText("time travel")
                        .setModel("sentence-transformers/all-minilm-l6-v2")
                        .build()))
            .setUsing("description-dense")
            .setFilter(filter)
            .setWithPayload(enable(true))
            .build())
    .get();

```

```
using Qdrant.Client;
using Qdrant.Client.Grpc;
using static Qdrant.Client.Grpc.Conditions;

await client.QueryAsync(
    collectionName: "books",
    query: new Document
    {
        Text = "time travel",
        Model = "sentence-transformers/all-minilm-l6-v2",
    },
    usingVector: "description-dense",
    filter: MatchKeyword("author", "H.G. Wells"),
    payloadSelector: true
);

```

```
client.Query(context.Background(), &qdrant.QueryPoints{
	CollectionName: "books",
	Query: qdrant.NewQueryNearest(
		qdrant.NewVectorInputDocument(&qdrant.Document{
			Model: "sentence-transformers/all-minilm-l6-v2",
			Text:  "time travel",
		}),
	),
	Using:       qdrant.PtrOf("description-dense"),
	WithPayload: qdrant.NewWithPayload(true),
	Filter: &qdrant.Filter{
		Must: []*qdrant.Condition{
			qdrant.NewMatch("author", "H.G. Wells"),
		},
	},
})

```

The ranking of the results of this request is based on the vector similarity of the query. The filter only narrows down the results to those points where the `author` field exactly matches `H.G. Wells`. Furthermore, the filter is case-sensitive. Filtering for the lowercase value `h.g. wells` would not return any results.
The previous example only returns points that match the filter value. If you want the opposite: exclude points with a specific value, use a `must_not` clause instead of `must`. The following example only returns books _not_ written by H.G. Wells:
httppythontypescriptrustjavacsharpgo
```
POST /collections/books/points/query
{
  "query": {
    "text": "time travel",
    "model": "sentence-transformers/all-minilm-l6-v2"
  },
  "using": "description-dense",
  "with_payload": true,
  "filter": {
    "must_not": [
      {
        "key": "author",
        "match": {
          "value": "H.G. Wells"
        }
      }
    ]
  }
}

```

```
from qdrant_client import QdrantClient, models

client = QdrantClient(
    url="https://xyz-example.qdrant.io:6333",
    api_key="<your-api-key>",
    cloud_inference=True,
)

client.query_points(
    collection_name="books",
    query=models.Document(text="time travel", model="sentence-transformers/all-minilm-l6-v2"),
    using="description-dense",
    with_payload=True,
    query_filter=models.Filter(
        must_not=[models.FieldCondition(key="author", match=models.MatchValue(value="H.G. Wells"))]
    ),
)

```

```
client.query("books", {
  query: {
    text: "time travel",
    model: "sentence-transformers/all-minilm-l6-v2",
  },
  using: "description-dense",
  with_payload: true,
  filter: {
    must_not: [
      { key: "author", match: { value: "H.G. Wells" } },
    ],
  },
});

```

```
use qdrant_client::Qdrant;
use qdrant_client::qdrant::{Condition, Document, Filter, Query, QueryPointsBuilder};

let filter = Filter::must_not([Condition::matches("author", "H.G. Wells".to_string())]);

client
    .query(
        QueryPointsBuilder::new("books")
            .query(Query::new_nearest(Document::new(
                "time travel",
                "sentence-transformers/all-minilm-l6-v2",
            )))
            .using("description-dense")
            .filter(filter)
            .with_payload(true)
            .build(),
    )
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

QdrantClient client =

Filter filter = Filter.newBuilder().addMustNot(matchKeyword("author", "H.G. Wells")).build();

client
    .queryAsync(
        QueryPoints.newBuilder()
            .setCollectionName("books")
            .setQuery(
                nearest(
                    Document.newBuilder()
                        .setText("time travel")
                        .setModel("sentence-transformers/all-minilm-l6-v2")
                        .build()))
            .setUsing("description-dense")
            .setFilter(filter)
            .setWithPayload(enable(true))
            .build())
    .get();

```

```
using Qdrant.Client;
using Qdrant.Client.Grpc;
using static Qdrant.Client.Grpc.Conditions;

var excludeFilter = new Filter { MustNot = { MatchKeyword("author", "H.G. Wells") } };

await client.QueryAsync(
    collectionName: "books",
    query: new Document
    {
        Text = "time travel",
        Model = "sentence-transformers/all-minilm-l6-v2",
    },
    usingVector: "description-dense",
    filter: excludeFilter,
    payloadSelector: true
);

```

```
excludeFilter := qdrant.Filter{
	MustNot: []*qdrant.Condition{
		qdrant.NewMatch("author", "H.G. Wells"),
	},
}

client.Query(context.Background(), &qdrant.QueryPoints{
	CollectionName: "books",
	Query: qdrant.NewQueryNearest(
		qdrant.NewVectorInputDocument(&qdrant.Document{
			Model: "sentence-transformers/all-minilm-l6-v2",
			Text:  "time travel",
		}),
	),
	Using:       qdrant.PtrOf("description-dense"),
	WithPayload: qdrant.NewWithPayload(true),
	Filter:      &excludeFilter,
})

```

###  [](https://qdrant.tech/documentation/guides/text-search/#filtering-on-multiple-exact-strings)Filtering on Multiple Exact Strings
You can provide multiple filter clauses. For example, to find all books co-authored by Larry Niven and Jerry Pournelle, use the following filter:
httppythontypescriptrustjavacsharpgo
```
POST /collections/books/points/query
{
  "query": {
    "text": "space opera",
    "model": "sentence-transformers/all-minilm-l6-v2"
  },
  "using": "description-dense",
  "with_payload": true,
  "filter": {
    "must": [
      {
        "key": "author",
        "match": {
          "value": "Larry Niven"
        }
      },
      {
        "key": "author",
        "match": {
          "value": "Jerry Pournelle"
        }
      }
    ]
  }
}

```

```
from qdrant_client import QdrantClient, models

client = QdrantClient(
    url="https://xyz-example.qdrant.io:6333",
    api_key="<your-api-key>",
    cloud_inference=True,
)

client.query_points(
    collection_name="books",
    query=models.Document(text="space opera", model="sentence-transformers/all-minilm-l6-v2"),
    using="description-dense",
    with_payload=True,
    query_filter=models.Filter(
        must=[
            models.FieldCondition(key="author", match=models.MatchValue(value="Larry Niven")),
            models.FieldCondition(key="author", match=models.MatchValue(value="Jerry Pournelle")),
        ]
    ),
)

```

```
client.query("books", {
  query: {
    text: "space opera",
    model: "sentence-transformers/all-minilm-l6-v2",
  },
  using: "description-dense",
  with_payload: true,
  filter: {
    must: [
      { key: "author", match: { value: "Larry Niven" } },
      { key: "author", match: { value: "Jerry Pournelle" } },
    ],
  },
});

```

```
use qdrant_client::Qdrant;
use qdrant_client::qdrant::{Condition, Document, Filter, Query, QueryPointsBuilder};

let filter = Filter::must([
    Condition::matches("author", "Larry Niven".to_string()),
    Condition::matches("author", "Jerry Pournelle".to_string()),
]);

client
    .query(
        QueryPointsBuilder::new("books")
            .query(Query::new_nearest(Document::new(
                "space opera",
                "sentence-transformers/all-minilm-l6-v2",
            )))
            .using("description-dense")
            .filter(filter)
            .with_payload(true)
            .build(),
    )
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

QdrantClient client =

Filter filter =
    Filter.newBuilder()
        .addMust(matchKeyword("author", "Larry Niven"))
        .addMust(matchKeyword("author", "Jerry Pournelle"))
        .build();

client
    .queryAsync(
        QueryPoints.newBuilder()
            .setCollectionName("books")
            .setQuery(
                nearest(
                    Document.newBuilder()
                        .setText("space opera")
                        .setModel("sentence-transformers/all-minilm-l6-v2")
                        .build()))
            .setUsing("description-dense")
            .setFilter(filter)
            .setWithPayload(enable(true))
            .build())
    .get();

```

```
using Qdrant.Client;
using Qdrant.Client.Grpc;
using static Qdrant.Client.Grpc.Conditions;

var andFilter = new Filter
{
    Must =
    {
        MatchKeyword("author", "Larry Niven"),
        MatchKeyword("author", "Jerry Pournelle"),
    },
};

await client.QueryAsync(
    collectionName: "books",
    query: new Document
    {
        Text = "space opera",
        Model = "sentence-transformers/all-minilm-l6-v2",
    },
    usingVector: "description-dense",
    filter: andFilter,
    payloadSelector: true
);

```

```
andFilter := qdrant.Filter{
	Must: []*qdrant.Condition{
		qdrant.NewMatch("author", "Larry Niven"),
		qdrant.NewMatch("author", "Jerry Pournelle"),
	},
}

client.Query(context.Background(), &qdrant.QueryPoints{
	CollectionName: "books",
	Query: qdrant.NewQueryNearest(
		qdrant.NewVectorInputDocument(&qdrant.Document{
			Model: "sentence-transformers/all-minilm-l6-v2",
			Text:  "space opera",
		}),
	),
	Using:       qdrant.PtrOf("description-dense"),
	WithPayload: qdrant.NewWithPayload(true),
	Filter:      &andFilter,
})

```

Note that both filter clauses must be true for a point to be included in the results, because a `must` clause operates like a logical `AND`. If you want to find books written by either author (as well as both), use a `should` clause, which operates like a logical `OR`:
httppythontypescriptrustjavacsharpgo
```
POST /collections/books/points/query
{
  "query": {
    "text": "space opera",
    "model": "sentence-transformers/all-minilm-l6-v2"
  },
  "using": "description-dense",
  "with_payload": true,
  "filter": {
    "should": [
      {
        "key": "author",
        "match": {
          "value": "Larry Niven"
        }
      },
      {
        "key": "author",
        "match": {
          "value": "Jerry Pournelle"
        }
      }
    ]
  }
}

```

```
from qdrant_client import QdrantClient, models

client = QdrantClient(
    url="https://xyz-example.qdrant.io:6333",
    api_key="<your-api-key>",
    cloud_inference=True,
)

client.query_points(
    collection_name="books",
    query=models.Document(text="space opera", model="sentence-transformers/all-minilm-l6-v2"),
    using="description-dense",
    with_payload=True,
    query_filter=models.Filter(
        should=[
            models.FieldCondition(key="author", match=models.MatchValue(value="Larry Niven")),
            models.FieldCondition(key="author", match=models.MatchValue(value="Jerry Pournelle")),
        ]
    ),
)

```

```
client.query("books", {
  query: {
    text: "space opera",
    model: "sentence-transformers/all-minilm-l6-v2",
  },
  using: "description-dense",
  with_payload: true,
  filter: {
    should: [
      { key: "author", match: { value: "Larry Niven" } },
      { key: "author", match: { value: "Jerry Pournelle" } },
    ],
  },
});

```

```
use qdrant_client::Qdrant;
use qdrant_client::qdrant::{Condition, Document, Filter, Query, QueryPointsBuilder};

let filter = Filter::should([
    Condition::matches("author", "Larry Niven".to_string()),
    Condition::matches("author", "Jerry Pournelle".to_string()),
]);

client
    .query(
        QueryPointsBuilder::new("books")
            .query(Query::new_nearest(Document::new(
                "space opera",
                "sentence-transformers/all-minilm-l6-v2",
            )))
            .using("description-dense")
            .filter(filter)
            .with_payload(true)
            .build(),
    )
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

QdrantClient client =

Filter filter =
    Filter.newBuilder()
        .addShould(matchKeyword("author", "Larry Niven"))
        .addShould(matchKeyword("author", "Jerry Pournelle"))
        .build();

client
    .queryAsync(
        QueryPoints.newBuilder()
            .setCollectionName("books")
            .setQuery(
                nearest(
                    Document.newBuilder()
                        .setText("space opera")
                        .setModel("sentence-transformers/all-minilm-l6-v2")
                        .build()))
            .setUsing("description-dense")
            .setFilter(filter)
            .setWithPayload(enable(true))
            .build())
    .get();

```

```
using Qdrant.Client;
using Qdrant.Client.Grpc;
using static Qdrant.Client.Grpc.Conditions;

var orFilter = new Filter
{
    Should =
    {
        MatchKeyword("author", "Larry Niven"),
        MatchKeyword("author", "Jerry Pournelle"),
    },
};

await client.QueryAsync(
    collectionName: "books",
    query: new Document
    {
        Text = "space opera",
        Model = "sentence-transformers/all-minilm-l6-v2",
    },
    usingVector: "description-dense",
    filter: orFilter,
    payloadSelector: true
);

```

```
orFilter := qdrant.Filter{
	Should: []*qdrant.Condition{
		qdrant.NewMatch("author", "Larry Niven"),
		qdrant.NewMatch("author", "Jerry Pournelle"),
	},
}

client.Query(context.Background(), &qdrant.QueryPoints{
	CollectionName: "books",
	Query: qdrant.NewQueryNearest(
		qdrant.NewVectorInputDocument(&qdrant.Document{
			Model: "sentence-transformers/all-minilm-l6-v2",
			Text:  "space opera",
		}),
	),
	Using:       qdrant.PtrOf("description-dense"),
	WithPayload: qdrant.NewWithPayload(true),
	Filter:      &orFilter,
})

```

Alternatively, when you want to filter on one or more values of a single key, you can use the `any` condition:
httppythontypescriptrustjavacsharpgo
```
POST /collections/books/points/query
{
  "query": {
    "text": "space opera",
    "model": "sentence-transformers/all-minilm-l6-v2"
  },
  "using": "description-dense",
  "with_payload": true,
  "filter": {
    "must": [
      {
        "key": "author",
        "match": {
          "any": ["Larry Niven", "Jerry Pournelle"]
        }
      }
    ]
  }
}

```

```
from qdrant_client import QdrantClient, models

client = QdrantClient(
    url="https://xyz-example.qdrant.io:6333",
    api_key="<your-api-key>",
    cloud_inference=True,
)

client.query_points(
    collection_name="books",
    query=models.Document(text="space opera", model="sentence-transformers/all-minilm-l6-v2"),
    using="description-dense",
    with_payload=True,
    query_filter=models.Filter(
        must=[
            models.FieldCondition(
                key="author",
                match=models.MatchAny(any=["Larry Niven", "Jerry Pournelle"]),
            )
        ]
    ),
)

```

```
client.query("books", {
  query: {
    text: "space opera",
    model: "sentence-transformers/all-minilm-l6-v2",
  },
  using: "description-dense",
  with_payload: true,
  filter: {
    must: [
      {
        key: "author",
        match: { any: ["Larry Niven", "Jerry Pournelle"] },
      },
    ],
  },
});

```

```
use qdrant_client::Qdrant;
use qdrant_client::qdrant::{Condition, Document, Filter, Query, QueryPointsBuilder};

let filter = Filter::should([
    Condition::matches("author", "Larry Niven".to_string()),
    Condition::matches("author", "Jerry Pournelle".to_string()),
]);

client
    .query(
        QueryPointsBuilder::new("books")
            .query(Query::new_nearest(Document::new(
                "space opera",
                "sentence-transformers/all-minilm-l6-v2",
            )))
            .using("description-dense")
            .filter(filter)
            .with_payload(true)
            .build(),
    )
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

QdrantClient client =

Filter filter =
    Filter.newBuilder()
        .addShould(matchKeyword("author", "Larry Niven"))
        .addShould(matchKeyword("author", "Jerry Pournelle"))
        .build();

client
    .queryAsync(
        QueryPoints.newBuilder()
            .setCollectionName("books")
            .setQuery(
                nearest(
                    Document.newBuilder()
                        .setText("space opera")
                        .setModel("sentence-transformers/all-minilm-l6-v2")
                        .build()))
            .setUsing("description-dense")
            .setFilter(filter)
            .setWithPayload(enable(true))
            .build())
    .get();

```

```
using Qdrant.Client;
using Qdrant.Client.Grpc;
using static Qdrant.Client.Grpc.Conditions;

var anyFilter = new Filter
{
    Should =
    {
        MatchKeyword("author", "Larry Niven"),
        MatchKeyword("author", "Jerry Pournelle"),
    },
};

await client.QueryAsync(
    collectionName: "books",
    query: new Document
    {
        Text = "space opera",
        Model = "sentence-transformers/all-minilm-l6-v2",
    },
    usingVector: "description-dense",
    filter: anyFilter,
    payloadSelector: true
);

```

```
anyFilter := qdrant.Filter{
	Should: []*qdrant.Condition{
		qdrant.NewMatch("author", "Larry Niven"),
		qdrant.NewMatch("author", "Jerry Pournelle"),
	},
}

client.Query(context.Background(), &qdrant.QueryPoints{
	CollectionName: "books",
	Query: qdrant.NewQueryNearest(
		qdrant.NewVectorInputDocument(&qdrant.Document{
			Model: "sentence-transformers/all-minilm-l6-v2",
			Text:  "space opera",
		}),
	),
	Using:       qdrant.PtrOf("description-dense"),
	WithPayload: qdrant.NewWithPayload(true),
	Filter:      &anyFilter,
})

```

###  [](https://qdrant.tech/documentation/guides/text-search/#full-text-filtering)Full-Text Filtering
In contrast to keyword filtering, filtering on text strings enables you to filter on individual words within a larger text field in a case-insensitive manner. To understand how this works, it’s important to understand how text strings are processed at index time and query time.
####  [](https://qdrant.tech/documentation/guides/text-search/#text-processing)Text Processing
To enable efficient full-text filtering, Qdrant processes text strings by breaking them down into individual tokens (words) and applying several normalization steps. This process ensures that searches are more flexible and can match variations of words. At query time, Qdrant applies the same processing steps to the filter string, ensuring that the filter matches the indexed tokens correctly.
