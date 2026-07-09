![Text processing can break down a sentence like"The quick brown fox" into the tokens “quick”, “brown”, and “fox”.](https://qdrant.tech/docs/text-processing.png)
The following text processing steps are applied to text strings:
  * The string is broken down into individual tokens (words) using a process called [tokenization](https://qdrant.tech/documentation/concepts/indexing/#tokenizers). By default, Qdrant uses the `word` tokenizer, which splits the string using word boundaries, discarding spaces, punctuation marks, and special characters.
  * By default, each word is then [converted to lowercase](https://qdrant.tech/documentation/concepts/indexing/#lowercasing). Lowercasing the tokens allows Qdrant to ignore capitalization, making full-text filters case-insensitive.
  * Optionally, Qdrant can remove diacritics (accents) from characters using a process called [ASCII folding](https://qdrant.tech/documentation/concepts/indexing/#ascii-folding). This ensures that diacritics are ignored. As a result, filtering for the word “cafe” matches “café”.
  * Optionally, tokens can be reduced to their root form using a [stemmer](https://qdrant.tech/documentation/concepts/indexing/#stemmer). This ensures that filtering for “running” also matches “run” and “ran”. Because stemming is language-specific, if enabled, it must be configured for a specific language.
  * Certain words like “the”, “is”, and “and” are very common in text and do not contribute much to the meaning of text. These words are called [stopwords](https://qdrant.tech/documentation/concepts/indexing/#stopwords) and can optionally be removed during indexing. Like stemming, stopword removal is language-specific. You can configure specific languages for stopword removal and/or provide a custom list of stopwords to remove.
  * Optionally, you can enable [phrase matching](https://qdrant.tech/documentation/concepts/indexing/#phrase-search) to allow filtering for multiple words in the exact same order as they appear in the original text.


These text processing steps can be configured when creating a [full-text index](https://qdrant.tech/documentation/guides/text-search/documentation/concepts/indexing/#full-text-index). For example, to create a text index on the `title` field with ASCII folding enabled:
httppythontypescriptrustjavacsharpgo
```
PUT /collections/books/index?wait=true
{
  "field_name": "title",
  "field_schema": {
    "type": "text",
    "ascii_folding": true
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

client.create_payload_index(
    collection_name="books",
    field_name="title",
    field_schema=models.TextIndexParams(type=models.TextIndexType.TEXT, ascii_folding=True),
)

```

```
client.createPayloadIndex("books", {
  field_name: "title",
  field_schema: {
    type: "text",
    ascii_folding: true,
  },
});

```

```
use qdrant_client::Qdrant;
use qdrant_client::qdrant::{
    CreateFieldIndexCollectionBuilder, FieldType, TextIndexParamsBuilder, TokenizerType,
};

let params = TextIndexParamsBuilder::new(TokenizerType::Word)
    .ascii_folding(true)
    .lowercase(true)
    .build();

client
    .create_field_index(
        CreateFieldIndexCollectionBuilder::new("books", "title", FieldType::Text)
            .field_index_params(params),
    )
    .await?;

```

```
import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Collections.PayloadIndexParams;
import io.qdrant.client.grpc.Collections.PayloadSchemaType;
import io.qdrant.client.grpc.Collections.TextIndexParams;
import io.qdrant.client.grpc.Collections.TokenizerType;

QdrantClient client =

client
    .createPayloadIndexAsync(
        "books",
        "title",
        PayloadSchemaType.Text,
        PayloadIndexParams.newBuilder()
            .setTextIndexParams(
                TextIndexParams.newBuilder()
                    .setTokenizer(TokenizerType.Word)
                    .setAsciiFolding(true)
                    .setLowercase(true)
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

await client.CreatePayloadIndexAsync(
    collectionName: "books",
    fieldName: "title",
    schemaType: PayloadSchemaType.Text,
    indexParams: new PayloadIndexParams
    {
        TextIndexParams = new TextIndexParams
        {
            Tokenizer = TokenizerType.Word,
            AsciiFolding = true,
            Lowercase = true,
        },
    }
);

```

```
client.CreateFieldIndex(context.Background(), &qdrant.CreateFieldIndexCollection{
	CollectionName: "books",
	FieldName:      "title",
	FieldType:      qdrant.FieldType_FieldTypeText.Enum(),
	FieldIndexParams: qdrant.NewPayloadIndexParamsText(
		&qdrant.TextIndexParams{
			Tokenizer:    qdrant.TokenizerType_Word,
			Lowercase:    qdrant.PtrOf(true),
			AsciiFolding: qdrant.PtrOf(true),
		}),
})

```

When querying using this index, Qdrant automatically applies the same text processing steps to the filter string before matching it against the indexed tokens.
###  [](https://qdrant.tech/documentation/guides/text-search/#filter-on-text-strings)Filter on Text Strings
To filter on text values in a payload field, first create a [full-text index](https://qdrant.tech/documentation/concepts/indexing/#full-text-index) for that field. Next, you can use a `text` condition to query the collection with a filter for titles that contain the word “space”:
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
        "key": "title",
        "match": {
          "text": "space"
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
        must=[models.FieldCondition(key="title", match=models.MatchText(text="space"))]
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
      { key: "title", match: { text: "space" } },
    ],
  },
});

```

```
use qdrant_client::Qdrant;
use qdrant_client::qdrant::{Condition, Document, Filter, Query, QueryPointsBuilder};

let filter = Filter::must([Condition::matches("title", "space".to_string())]);

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

Filter filter = Filter.newBuilder().addMust(matchText("title", "space")).build();

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

await client.QueryAsync(
    collectionName: "books",
    query: new Document
    {
        Text = "space opera",
        Model = "sentence-transformers/all-minilm-l6-v2",
    },
    usingVector: "description-dense",
    filter: MatchText("title", "space"),
    payloadSelector: true
);

```

```
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
	Filter: &qdrant.Filter{
		Must: []*qdrant.Condition{qdrant.NewMatchText("title", "space")},
	},
})

```

When filtering on more than one term, a `text` filter only matches fields that contain _all_ the specified terms (logical `AND`). To match fields that contain _any_ of the specified terms (logical `OR`), use the `text_any` condition:
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
        "key": "title",
        "match": {
          "text_any": "space war"
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
        must=[models.FieldCondition(key="title", match=models.MatchTextAny(text_any="space war"))]
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
      { key: "title", match: { text_any: "space war" } },
    ],
  },
});

```

```
use qdrant_client::Qdrant;
use qdrant_client::qdrant::{Condition, Document, Filter, Query, QueryPointsBuilder};

let filter = Filter::must([Condition::matches("title", "space war".to_string())]);

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

Filter filter = Filter.newBuilder().addMust(matchTextAny("title", "space war")).build();

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

await client.QueryAsync(
    collectionName: "books",
    query: new Document
    {
        Text = "space opera",
        Model = "sentence-transformers/all-minilm-l6-v2",
    },
    usingVector: "description-dense",
    filter: MatchTextAny("title", "space war"),
    payloadSelector: true
);

```

```
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
	Filter: &qdrant.Filter{
		Must: []*qdrant.Condition{qdrant.NewMatchTextAny("title", "space war")},
	},
})

```

Qdrant also supports phrase filtering, enabling you to search for multiple words in the exact order they appear in the original text, with no other words in between. For example, a phrase filter for “time machine” matches against the title “The Time Machine” but would not match “The Time Travel Machine” (there’s a word between “time” and “machine”) nor “Machine Time” (the word order is incorrect).
The difference between phrase filtering and keyword filtering is that phrase filtering applies text processing and, as a result, is case-insensitive, while keyword filtering is case-sensitive and only matches the exact string. Additionally, keyword filtering has to match the entire string, whereas phrase filtering can match part of a larger string. So a keyword filter for “Space War” would not match “The Space War” because it doesn’t match “The,” but a phrase filter for “Space War” would.
Summarizing the differences between the four filtering methods for a multi-term filter on “Space War”:
Method | Actual⠀query⠀⠀⠀ | Matches `Space War`? | Matches `The Space War`? | Matches `War in Space`? | Matches `War of the Worlds`?
---|---|---|---|---|---
text_any |  `space` OR `war` | Yes | Yes | Yes | Yes
text |  `space` AND `war` | Yes | Yes | Yes | No
phrase | `"space war"` | Yes | Yes | No | No
keyword | `"Space War"` | Yes | No | No | No
To filter on phrases, use a `phrase` condition. This requires enabling [phrase searching](https://qdrant.tech/documentation/concepts/indexing/#phrase-search) when creating the full-text index:
httppythontypescriptrustjavacsharpgo
```
PUT /collections/books/index?wait=true
{
  "field_name": "title",
  "field_schema": {
    "type": "text",
    "ascii_folding": true,
    "phrase_matching": true
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

client.create_payload_index(
    collection_name="books",
    field_name="title",
    field_schema=models.TextIndexParams(type=models.TextIndexType.TEXT, ascii_folding=True, phrase_matching=True),
)

```

```
client.createPayloadIndex("books", {
  field_name: "title",
  field_schema: {
    type: "text",
    ascii_folding: true,
    phrase_matching: true,
  },
});

```

```
use qdrant_client::Qdrant;
use qdrant_client::qdrant::{
    CreateFieldIndexCollectionBuilder, FieldType, TextIndexParamsBuilder, TokenizerType,
};

let params = TextIndexParamsBuilder::new(TokenizerType::Word)
    .ascii_folding(true)
    .phrase_matching(true)
    .lowercase(true)
    .build();

client
    .create_field_index(
        CreateFieldIndexCollectionBuilder::new("books", "title", FieldType::Text)
            .field_index_params(params),
    )
    .await?;

```

```
import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Collections.PayloadIndexParams;
import io.qdrant.client.grpc.Collections.PayloadSchemaType;
import io.qdrant.client.grpc.Collections.TextIndexParams;
import io.qdrant.client.grpc.Collections.TokenizerType;

QdrantClient client =

client
    .createPayloadIndexAsync(
        "books",
        "title",
        PayloadSchemaType.Text,
        PayloadIndexParams.newBuilder()
            .setTextIndexParams(
                TextIndexParams.newBuilder()
                    .setTokenizer(TokenizerType.Word)
                    .setAsciiFolding(true)
                    .setPhraseMatching(true)
                    .setLowercase(true)
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

await client.CreatePayloadIndexAsync(
    collectionName: "books",
    fieldName: "title",
    schemaType: PayloadSchemaType.Text,
    indexParams: new PayloadIndexParams
    {
        TextIndexParams = new TextIndexParams
        {
            Tokenizer = TokenizerType.Word,
            AsciiFolding = true,
            PhraseMatching = true,
            Lowercase = true,
        },
    }
);

```

```
client.CreateFieldIndex(context.Background(), &qdrant.CreateFieldIndexCollection{
	CollectionName: "books",
	FieldName:      "title",
	FieldType:      qdrant.FieldType_FieldTypeText.Enum(),
	FieldIndexParams: qdrant.NewPayloadIndexParamsText(
		&qdrant.TextIndexParams{
			Tokenizer:      qdrant.TokenizerType_Word,
			Lowercase:      qdrant.PtrOf(true),
			AsciiFolding:   qdrant.PtrOf(true),
			PhraseMatching: qdrant.PtrOf(true),
		}),
})

```

Next, you can use a `phrase` condition to filter for titles that contain the exact phrase “time machine”:
httppythontypescriptrustjavacsharpgo
```
POST /collections/books/points/query?wait=true
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
        "key": "title",
        "match": {
          "phrase": "time machine"
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
        must=[models.FieldCondition(key="title", match=models.MatchPhrase(phrase="time machine"))]
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
      { key: "title", match: { phrase: "time machine" } },
    ],
  },
});

```

```
use qdrant_client::Qdrant;
use qdrant_client::qdrant::{Condition, Document, Filter, Query, QueryPointsBuilder};

let filter = Filter::must([Condition::matches("title", "time machine".to_string())]);

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
import io.qdrant.client.grpc.Collections.*;
import io.qdrant.client.grpc.Common.Filter;
import io.qdrant.client.grpc.Points.*;
import java.util.*;

QdrantClient client =

Filter filter = Filter.newBuilder().addMust(matchPhrase("title", "time machine")).build();

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
    filter: MatchPhrase("title", "time machine"),
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
		Must: []*qdrant.Condition{qdrant.NewMatchPhrase("title", "time machine")},
	},
})

```

###  [](https://qdrant.tech/documentation/guides/text-search/#progressive-filtering-with-the-batch-search-api)Progressive Filtering with the Batch Search API
Even though filters are not used to rank results, you can use the [batch search API](https://qdrant.tech/documentation/concepts/search/#batch-search-api) to progressively relax filters. This is useful when you have strict filtering criteria that may not return results. Batching multiple search requests with progressively relaxed filters enables you to get results even when the strictest filter returns no results.
For example, the following batch search request first tries to find books that match all search terms in the title. The second search request relaxes the filter to match any of the search terms. The third search request removes the filter altogether:
httppythontypescriptrustjavacsharpgo
```
POST /collections/books/points/query/batch
{
  "searches": [
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
            "key": "title",
            "match": {
              "text": "time travel"
            }
          }
        ]
      }
    },
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
            "key": "title",
            "match": {
              "text_any": "time travel"
            }
          }
        ]
      }
    },
    {
      "query": {
        "text": "time travel",
        "model": "sentence-transformers/all-minilm-l6-v2"
      },
      "using": "description-dense",
      "with_payload": true
    }
  ]
}

```

```
from qdrant_client import QdrantClient, models

client = QdrantClient(
    url="https://xyz-example.qdrant.io:6333",
    api_key="<your-api-key>",
    cloud_inference=True,
)

client.query_batch_points(
    collection_name="books",
    requests=[
        models.QueryRequest(
            query=models.Document(text="time travel", model="sentence-transformers/all-minilm-l6-v2"),
            using="description-dense",
            with_payload=True,
            filter=models.Filter(
                must=[models.FieldCondition(key="title", match=models.MatchText(text="time travel"))]
            ),
        ),
        models.QueryRequest(
            query=models.Document(text="time travel", model="sentence-transformers/all-minilm-l6-v2"),
            using="description-dense",
            with_payload=True,
            filter=models.Filter(
                must=[models.FieldCondition(key="title", match=models.MatchTextAny(text_any="time travel"))]
            ),
        ),
        models.QueryRequest(
            query=models.Document(text="time travel", model="sentence-transformers/all-minilm-l6-v2"),
            using="description-dense",
            with_payload=True,
        ),
    ],
)

```

```
client.queryBatch("books", {
  searches: [
    {
      query: { text: "time travel", model: "sentence-transformers/all-minilm-l6-v2" },
      using: "description-dense",
      with_payload: true,
      filter: {
        must: [{ key: "title", match: { text: "time travel" } }],
      },
    },
    {
      query: { text: "time travel", model: "sentence-transformers/all-minilm-l6-v2" },
      using: "description-dense",
      with_payload: true,
      filter: {
        must: [{ key: "title", match: { text_any: "time travel" } }],
      },
    },
    {
      query: { text: "time travel", model: "sentence-transformers/all-minilm-l6-v2" },
      using: "description-dense",
      with_payload: true,
    },
  ],
});

```

```
use qdrant_client::Qdrant;
use qdrant_client::qdrant::{
    Condition, Document, Filter, Query, QueryBatchPointsBuilder, QueryPointsBuilder,
};

let strict_filter = Filter::must([Condition::matches("title", "time travel".to_string())]);
let relaxed_filter = Filter::must([Condition::matches("title", "time travel".to_string())]);

let searches = vec![
    QueryPointsBuilder::new("books")
        .query(Query::new_nearest(Document::new(
