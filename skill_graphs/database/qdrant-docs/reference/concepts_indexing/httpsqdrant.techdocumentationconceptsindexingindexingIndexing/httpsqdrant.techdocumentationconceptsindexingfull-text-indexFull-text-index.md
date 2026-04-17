##  [](https://qdrant.tech/documentation/concepts/indexing/#full-text-index)Full-text index
Qdrant supports full-text search for string payload. Full-text index allows you to filter points by the presence of a word or a phrase in the payload field.
Full-text index configuration is a bit more complex than other indexes, as you can specify the tokenization parameters. Tokenization is the process of splitting a string into tokens, which are then indexed in the inverted index.
See [Full Text match](https://qdrant.tech/documentation/concepts/filtering/#full-text-match) for examples of querying with a full-text index.
To create a full-text index, you can use the following:
httppythontypescriptrustjavacsharpgo
```
PUT /collections/{collection_name}/index
{
    "field_name": "name_of_the_field_to_index",
    "field_schema": {
        "type": "text",
        "tokenizer": "word",
        "min_token_len": 2,
        "max_token_len": 10,
        "lowercase": true
    }
}

```

```
from qdrant_client import QdrantClient, models

client = QdrantClient(url="http://localhost:6333")

client.create_payload_index(
    collection_name="{collection_name}",
    field_name="name_of_the_field_to_index",
    field_schema=models.TextIndexParams(
        type=models.TextIndexType.TEXT,
        tokenizer=models.TokenizerType.WORD,
        min_token_len=2,
        max_token_len=10,
        lowercase=True,
    ),
)

```

```
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.createPayloadIndex("{collection_name}", {
  field_name: "name_of_the_field_to_index",
  field_schema: {
    type: "text",
    tokenizer: "word",
    min_token_len: 2,
    max_token_len: 10,
    lowercase: true,
  },
});

```

```
use qdrant_client::qdrant::{
    CreateFieldIndexCollectionBuilder,
    TextIndexParamsBuilder,
    FieldType,
    TokenizerType,
};
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

let text_index_params = TextIndexParamsBuilder::new(TokenizerType::Word)
    .min_token_len(2)
    .max_token_len(10)
    .lowercase(true);

client
    .create_field_index(
        CreateFieldIndexCollectionBuilder::new(
            "{collection_name}",
            "name_of_the_field_to_index",
            FieldType::Text,
        ).field_index_params(text_index_params.build()),
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
    new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client
    .createPayloadIndexAsync(
        "{collection_name}",
        "name_of_the_field_to_index",
        PayloadSchemaType.Text,
        PayloadIndexParams.newBuilder()
            .setTextIndexParams(
                TextIndexParams.newBuilder()
                    .setTokenizer(TokenizerType.Word)
                    .setMinTokenLen(2)
                    .setMaxTokenLen(10)
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

var client = new QdrantClient("localhost", 6334);

await client.CreatePayloadIndexAsync(
	collectionName: "{collection_name}",
	fieldName: "name_of_the_field_to_index",
	schemaType: PayloadSchemaType.Text,
	indexParams: new PayloadIndexParams
	{
		TextIndexParams = new TextIndexParams
		{
			Tokenizer = TokenizerType.Word,
			MinTokenLen = 2,
			MaxTokenLen = 10,
			Lowercase = true
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
	FieldType:      qdrant.FieldType_FieldTypeText.Enum(),
	FieldIndexParams: qdrant.NewPayloadIndexParamsText(
		&qdrant.TextIndexParams{
			Tokenizer:   qdrant.TokenizerType_Whitespace,
			MinTokenLen: qdrant.PtrOf(uint64(2)),
			MaxTokenLen: qdrant.PtrOf(uint64(10)),
			Lowercase:   qdrant.PtrOf(true),
		}),
})

```

###  [](https://qdrant.tech/documentation/concepts/indexing/#tokenizers)Tokenizers
Tokenizers are algorithms used to split text into smaller units called tokens, which are then indexed and searched in a full-text index. In the context of Qdrant, tokenizers determine how string payloads are broken down for efficient searching and filtering. The choice of tokenizer affects how queries match the indexed text, supporting different languages, word boundaries, and search behaviours such as prefix or phrase matching.
Available tokenizers are:
  * `word` (default) - splits the string into words, separated by spaces, punctuation marks, and special characters.
  * `whitespace` - splits the string into words, separated by spaces.
  * `prefix` - splits the string into words, separated by spaces, punctuation marks, and special characters, and then creates a prefix index for each word. For example: `hello` will be indexed as `h`, `he`, `hel`, `hell`, `hello`.
  * `multilingual` - a special type of tokenizer based on multiple packages like `vaporetto` project, which has much less overhead compared to `charabia`, while maintaining comparable performance.


###  [](https://qdrant.tech/documentation/concepts/indexing/#lowercasing)Lowercasing
By default, full-text search in Qdrant is case-insensitive. For example, users can search for the lowercase term `tv` and find text fields containing the uppercase word `TV`. Case-insensitivity is achieved by converting both the words in the index and the query terms to lowercase.
Lowercasing is enabled by default. To use case-sensitive full-text search, configure a full-text index with `lowercase` set to `false`.
httppythontypescriptrustjavacsharpgo
```
PUT /collections/{collection_name}/index
{
    "field_name": "name_of_the_field_to_index",
    "field_schema": {
        "type": "text",
        "tokenizer": "word",
        "lowercase": false
    }
}

```

```
from qdrant_client import QdrantClient, models

client = QdrantClient(url="http://localhost:6333")

client.create_payload_index(
    collection_name="{collection_name}",
    field_name="name_of_the_field_to_index",
    field_schema=models.TextIndexParams(
        type=models.TextIndexType.TEXT,
        tokenizer=models.TokenizerType.WORD,
        lowercase=False,
    ),
)

```

```
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.createPayloadIndex("{collection_name}", {
  field_name: "name_of_the_field_to_index",
  field_schema: {
    type: "text",
    tokenizer: "word",
    lowercase: false,
  },
});

```

```
use qdrant_client::qdrant::{
    CreateFieldIndexCollectionBuilder,
    TextIndexParamsBuilder,
    FieldType,
    TokenizerType,
};
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

let text_index_params = TextIndexParamsBuilder::new(TokenizerType::Word)
    .lowercase(false);

client
    .create_field_index(
        CreateFieldIndexCollectionBuilder::new(
            "{collection_name}",
            "name_of_the_field_to_index",
            FieldType::Text,
        ).field_index_params(text_index_params.build()),
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
    new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client
    .createPayloadIndexAsync(
        "{collection_name}",
        "name_of_the_field_to_index",
        PayloadSchemaType.Text,
        PayloadIndexParams.newBuilder()
            .setTextIndexParams(
                TextIndexParams.newBuilder()
                    .setTokenizer(TokenizerType.Word)
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

var client = new QdrantClient("localhost", 6334);

await client.CreatePayloadIndexAsync(
    collectionName: "{collection_name}",
    fieldName: "name_of_the_field_to_index",
    schemaType: PayloadSchemaType.Text,
    indexParams: new PayloadIndexParams
    {
        TextIndexParams = new TextIndexParams
        {
            Tokenizer = TokenizerType.Word,
            Lowercase = true,
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
    FieldType:      qdrant.FieldType_FieldTypeText.Enum(),
    FieldIndexParams: qdrant.NewPayloadIndexParamsText(
        &qdrant.TextIndexParams{
            Tokenizer:   qdrant.TokenizerType_Word,
            Lowercase:   qdrant.PtrOf(true),
        }),
})

```

###  [](https://qdrant.tech/documentation/concepts/indexing/#ascii-folding)ASCII Folding
_Available as of v1.16.0_
When enabled, ASCII folding converts Unicode characters into their corresponding ASCII equivalents, for example, by removing diacritics. For instance, the character `ã` is changed into `a`, `ç` becomes `c`, and `é` is converted to `e`.
Because ASCII folding is applied to both the words in the index and the query terms, it increases recall. For example, users can search for `cafe` and also find text fields containing the word `café`.
ASCII folding is not enabled by default. To enable it, configure a full-text index with `ascii_folding` set to `true`.
httppythontypescriptrustjavacsharpgo
```
PUT /collections/{collection_name}/index
{
    "field_name": "name_of_the_field_to_index",
    "field_schema": {
        "type": "text",
        "tokenizer": "word",
        "ascii_folding": true
    }
}

```

```
from qdrant_client import QdrantClient, models

client = QdrantClient(url="http://localhost:6333")

client.create_payload_index(
    collection_name="{collection_name}",
    field_name="name_of_the_field_to_index",
    field_schema=models.TextIndexParams(
        type=models.TextIndexType.TEXT,
        tokenizer=models.TokenizerType.WORD,
        ascii_folding=True,
    ),
)

```

```
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.createPayloadIndex("{collection_name}", {
  field_name: "name_of_the_field_to_index",
  field_schema: {
    type: "text",
    tokenizer: "word",
    ascii_folding: true,
  },
});

```

```
use qdrant_client::qdrant::{
    CreateFieldIndexCollectionBuilder,
    TextIndexParamsBuilder,
    FieldType,
    TokenizerType,
};
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

let text_index_params = TextIndexParamsBuilder::new(TokenizerType::Word)
    .ascii_folding(true);

client
    .create_field_index(
        CreateFieldIndexCollectionBuilder::new(
            "{collection_name}",
            "name_of_the_field_to_index",
            FieldType::Text,
        ).field_index_params(text_index_params.build()),
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
    new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client
    .createPayloadIndexAsync(
        "{collection_name}",
        "name_of_the_field_to_index",
        PayloadSchemaType.Text,
        PayloadIndexParams.newBuilder()
            .setTextIndexParams(
                TextIndexParams.newBuilder()
                    .setTokenizer(TokenizerType.Word)
                    .setLowercase(true)
                    .setAsciiFolding(true)
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
    fieldName: "name_of_the_field_to_index",
    schemaType: PayloadSchemaType.Text,
    indexParams: new PayloadIndexParams
    {
        TextIndexParams = new TextIndexParams
        {
            Tokenizer = TokenizerType.Word,
            Lowercase = true,
			AsciiFolding = true,
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
	FieldType:      qdrant.FieldType_FieldTypeText.Enum(),
	FieldIndexParams: qdrant.NewPayloadIndexParamsText(
		&qdrant.TextIndexParams{
			Tokenizer:    qdrant.TokenizerType_Word,
			Lowercase:    qdrant.PtrOf(true),
			AsciiFolding: qdrant.PtrOf(true),
		}),
})

```

###  [](https://qdrant.tech/documentation/concepts/indexing/#stemmer)Stemmer
A **stemmer** is an algorithm used in text processing to reduce words to their root or base form, known as the “stem.” For example, the words “running”, “runner and “runs” can all be reduced to the stem “run.” When configuring a full-text index in Qdrant, you can specify a stemmer to be used for a particular language. This enables the index to recognize and match different inflections or derivations of a word.
Qdrant provides an implementation of
For full-text indices, stemming is not enabled by default. To enable it, configure the `snowball` stemmer with the desired language:
httppythontypescriptrustjavacsharpgo
```
PUT /collections/{collection_name}/index
{
    "field_name": "name_of_the_field_to_index",
    "field_schema": {
        "type": "text",
        "tokenizer": "word",
        "stemmer": {
            "type": "snowball",
            "language": "english"
        }
    }
}

```

```
from qdrant_client import QdrantClient, models

client = QdrantClient(url="http://localhost:6333")

client.create_payload_index(
    collection_name="{collection_name}",
    field_name="name_of_the_field_to_index",
    field_schema=models.TextIndexParams(
        type=models.TextIndexType.TEXT,
        tokenizer=models.TokenizerType.WORD,
        stemmer=models.SnowballParams(
            type=models.Snowball.SNOWBALL,
            language=models.SnowballLanguage.ENGLISH
        )
    ),
)

```

```
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.createPayloadIndex("{collection_name}", {
  field_name: "name_of_the_field_to_index",
  field_schema: {
    type: "text",
    tokenizer: "word",
    stemmer: {
      type: "snowball",
      language: "english"
    }
  }
});

```

```
use qdrant_client::qdrant::{
    CreateFieldIndexCollectionBuilder,
    TextIndexParamsBuilder,
    FieldType,
    TokenizerType,
};
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

let text_index_params = TextIndexParamsBuilder::new(TokenizerType::Word)
    .snowball_stemmer("english".to_string());

client
    .create_field_index(
        CreateFieldIndexCollectionBuilder::new(
            "{collection_name}",
            "{field_name}",
            FieldType::Text,
        ).field_index_params(text_index_params.build()),
    )
    .await?;

```

```
import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Collections.PayloadIndexParams;
import io.qdrant.client.grpc.Collections.PayloadSchemaType;
import io.qdrant.client.grpc.Collections.SnowballParams;
import io.qdrant.client.grpc.Collections.StemmingAlgorithm;
import io.qdrant.client.grpc.Collections.TextIndexParams;
import io.qdrant.client.grpc.Collections.TokenizerType;

QdrantClient client =
    new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client
    .createPayloadIndexAsync(
        "{collection_name}",
        "name_of_the_field_to_index",
        PayloadSchemaType.Text,
        PayloadIndexParams.newBuilder()
            .setTextIndexParams(
                TextIndexParams.newBuilder()
                    .setTokenizer(TokenizerType.Word)
                    .setStemmer(
                        StemmingAlgorithm.newBuilder()
                            .setSnowball(
                                SnowballParams.newBuilder().setLanguage("english").build())
                            .build())
                    .build())
            .build(),
        true,
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
	schemaType: PayloadSchemaType.Text,
	indexParams: new PayloadIndexParams
	{
		TextIndexParams = new TextIndexParams
		{
			Tokenizer = TokenizerType.Word,
			Stemmer = new StemmingAlgorithm
			{
				Snowball = new SnowballParams
				{
					Language = "english"
				}
			}
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
	FieldType:      qdrant.FieldType_FieldTypeText.Enum(),
	FieldIndexParams: qdrant.NewPayloadIndexParamsText(
		&qdrant.TextIndexParams{
			Tokenizer: qdrant.TokenizerType_Word,
			Stemmer: qdrant.NewStemmingAlgorithmSnowball(&qdrant.SnowballParams{
				Language: "english",
			}),
		}),
})

```

###  [](https://qdrant.tech/documentation/concepts/indexing/#stopwords)Stopwords
Stopwords are common words (such as “the”, “is”, “at”, “which”, and “on”) that are often filtered out during text processing because they carry little meaningful information for search and retrieval tasks.
In Qdrant, you can specify a list of stopwords to be ignored during full-text indexing and search. This helps simplify search queries and improves relevance.
You can configure stopwords based on predefined languages, as well as extend existing stopword lists with custom words.
For full-text indices, stopword removal is not enabled by default. To enable it, configure the `stopwords` parameter with the desired languages and any custom stopwords:
httppythontypescriptrustjavacsharpgo
```
// Simple
PUT collections/{collection_name}/index
{
    "field_name": "name_of_the_field_to_index",
    "field_schema": {
        "type": "text",
        "tokenizer": "word",
        "stopwords": "english"
    }
}

// Explicit
PUT collections/{collection_name}/index
{
    "field_name": "name_of_the_field_to_index",
    "field_schema": {
        "type": "text",
        "tokenizer": "word",
        "stopwords": {
            "languages": [
                "english",
                "spanish"
            ],
            "custom": [
                "example"
            ]
        }
    }
}

```

```
from qdrant_client import QdrantClient, models

client = QdrantClient(url="http://localhost:6333")

# Simple
client.create_payload_index(
    collection_name="{collection_name}",
    field_name="name_of_the_field_to_index",
    field_schema=models.TextIndexParams(
        type=models.TextIndexType.TEXT,
        tokenizer=models.TokenizerType.WORD,
        stopwords=models.Language.ENGLISH,
    ),
)

# Explicit
client.create_payload_index(
    collection_name="{collection_name}",
    field_name="name_of_the_field_to_index",
    field_schema=models.TextIndexParams(
        type=models.TextIndexType.TEXT,
        tokenizer=models.TokenizerType.WORD,
        stopwords=models.StopwordsSet(
            languages=[
                models.Language.ENGLISH,
                models.Language.SPANISH,
            ],
            custom=[
                "example"
            ]
        ),
    ),
)

```

```
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

// Simple
client.createPayloadIndex("{collection_name}", {
  field_name: "name_of_the_field_to_index",
  field_schema: {
    type: "text",
    tokenizer: "word",
    stopwords: "english"
  },
});

// Explicit
client.createPayloadIndex("{collection_name}", {
  field_name: "name_of_the_field_to_index",
  field_schema: {
    type: "text",
    tokenizer: "word",
    stopwords: {
      languages: [
        "english",
        "spanish"
      ],
      custom: [
        "example"
      ]
    }
  },
});

```

```
use qdrant_client::qdrant::{
    CreateFieldIndexCollectionBuilder,
    TextIndexParamsBuilder,
    FieldType,
    TokenizerType,
    StopwordsSet,
};
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

// Simple
let text_index_params = TextIndexParamsBuilder::new(TokenizerType::Word)
    .stopwords_language("english".to_string());

client
    .create_field_index(
        CreateFieldIndexCollectionBuilder::new(
            "{collection_name}",
            "name_of_the_field_to_index",
            FieldType::Text,
        ).field_index_params(text_index_params.build()),
    )
    .await?;

// Explicit
let text_index_params = TextIndexParamsBuilder::new(TokenizerType::Word)
    .stopwords(StopwordsSet {
        languages: vec![
            "english".to_string(),
            "spanish".to_string(),
        ],
        custom: vec!["example".to_string()],
    });

client
    .create_field_index(
        CreateFieldIndexCollectionBuilder::new(
            "{collection_name}",
            "{field_name}",
            FieldType::Text,
        ).field_index_params(text_index_params.build()),
    )
    .await?;

```

```
import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Collections.PayloadIndexParams;
import io.qdrant.client.grpc.Collections.PayloadSchemaType;
import io.qdrant.client.grpc.Collections.StopwordsSet;
import io.qdrant.client.grpc.Collections.TextIndexParams;
import io.qdrant.client.grpc.Collections.TokenizerType;
import java.util.List;

QdrantClient client =
    new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client
    .createPayloadIndexAsync(
        "{collection_name}",
        "name_of_the_field_to_index",
        PayloadSchemaType.Text,
        PayloadIndexParams.newBuilder()
            .setTextIndexParams(
                TextIndexParams.newBuilder()
                    .setTokenizer(TokenizerType.Word)
                    .setStopwords(
                        StopwordsSet.newBuilder()
                            .addAllLanguages(List.of("english", "spanish"))
                            .addAllCustom(List.of("example"))
                            .build())
                    .build())
            .build(),
        true,
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
	schemaType: PayloadSchemaType.Text,
	indexParams: new PayloadIndexParams
	{
		TextIndexParams = new TextIndexParams
		{
			Tokenizer = TokenizerType.Word,
			Stopwords = new StopwordsSet
			{
				Languages = { "english", "spanish" },
				Custom = { "example" }
			}
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
	FieldType:      qdrant.FieldType_FieldTypeText.Enum(),
	FieldIndexParams: qdrant.NewPayloadIndexParamsText(
		&qdrant.TextIndexParams{
			Tokenizer: qdrant.TokenizerType_Word,
			Stopwords: &qdrant.StopwordsSet{
				Languages: []string{"english", "spanish"},
				Custom:    []string{"example"},
			},
		}),
})

```

###  [](https://qdrant.tech/documentation/concepts/indexing/#phrase-search)Phrase Search
Phrase search in Qdrant allows you to find documents or points where a specific sequence of words appears together, in the same order, within a text payload field. This is useful when you want to match exact phrases rather than individual words scattered throughout the text.
When using a full-text index with phrase search enabled, you can perform phrase search by enclosing the desired phrase in double quotes in your filter query. For example, searching for `"machine learning"` will only return results where the words “machine” and “learning” appear together as a phrase, not just anywhere in the text.
For efficient phrase search, Qdrant requires building an additional data structure, so it needs to be configured during the creation of the full-text index:
httppythontypescriptrustjavacsharpgo
```
PUT /collections/{collection_name}/index
{
    "field_name": "name_of_the_field_to_index",
    "field_schema": {
        "type": "text",
        "tokenizer": "word",
        "lowercase": true,
        "phrase_matching": true
    }
}

```

```
from qdrant_client import QdrantClient, models

client = QdrantClient(url="http://localhost:6333")

client.create_payload_index(
    collection_name="{collection_name}",
    field_name="name_of_the_field_to_index",
    field_schema=models.TextIndexParams(
        type=models.TextIndexType.TEXT,
        tokenizer=models.TokenizerType.WORD,
        lowercase=True,
        phrase_matching=True,
    ),
)

```

```
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.createPayloadIndex("{collection_name}", {
  field_name: "name_of_the_field_to_index",
  field_schema: {
    type: "text",
    tokenizer: "word",
    lowercase: true,
    phrase_matching: true,
  },
});

```

```
use qdrant_client::qdrant::{
    CreateFieldIndexCollectionBuilder,
    TextIndexParamsBuilder,
    FieldType,
    TokenizerType,
};
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

let text_index_params = TextIndexParamsBuilder::new(TokenizerType::Word)
    .phrase_matching(true)
    .lowercase(true);

client
    .create_field_index(
        CreateFieldIndexCollectionBuilder::new(
            "{collection_name}",
            "name_of_the_field_to_index",
            FieldType::Text,
        ).field_index_params(text_index_params.build()),
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
    new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client
    .createPayloadIndexAsync(
        "{collection_name}",
        "name_of_the_field_to_index",
        PayloadSchemaType.Text,
        PayloadIndexParams.newBuilder()
            .setTextIndexParams(
                TextIndexParams.newBuilder()
                    .setTokenizer(TokenizerType.Word)
                    .setLowercase(true)
                    .setPhraseMatching(true)
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
    fieldName: "name_of_the_field_to_index",
    schemaType: PayloadSchemaType.Text,
    indexParams: new PayloadIndexParams
    {
        TextIndexParams = new TextIndexParams
        {
            Tokenizer = TokenizerType.Word,
            Lowercase = true,
            PhraseMatching = true
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
    FieldType:      qdrant.FieldType_FieldTypeText.Enum(),
    FieldIndexParams: qdrant.NewPayloadIndexParamsText(
        &qdrant.TextIndexParams{
            Tokenizer:   qdrant.TokenizerType_Whitespace,
            Lowercase:   qdrant.PtrOf(true),
            PhraseMatching: qdrant.PtrOf(true),
        }),
})

```

See [Phrase Match](https://qdrant.tech/documentation/concepts/filtering/#phrase-match) for examples of querying phrases with a full-text index.
