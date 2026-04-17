
    # Using Gemini API (requires GOOGLE_API_KEY env var)
    model = GoogleEmbeddingModel('gemini-embedding-001')

    # Using Vertex AI
    model = GoogleEmbeddingModel(
        'gemini-embedding-001',
        provider=GoogleProvider(vertexai=True, project='my-project', location='us-central1'),
    )
```
    """

    _model_name: GoogleEmbeddingModelName = field(repr=False)
    _provider: Provider[Client] = field(repr=False)

    def __init__(
        self,
        model_name: GoogleEmbeddingModelName,
        *,
        provider: Literal['google-gla', 'google-vertex'] | Provider[Client] = 'google-gla',
        settings: EmbeddingSettings | None = None,
    ):
        """Initialize a Google embedding model.

        Args:
            model_name: The name of the Google model to use.
                See [Google Embeddings documentation](https://ai.google.dev/gemini-api/docs/embeddings)
                for available models.
            provider: The provider to use for authentication and API access. Can be:

                - `'google-gla'` (default): Uses the Gemini API (Google AI Studio)
                - `'google-vertex'`: Uses Vertex AI
                - A [`GoogleProvider`][pydantic_ai.providers.google.GoogleProvider] instance
                  for custom configuration
            settings: Model-specific [`EmbeddingSettings`][pydantic_ai.embeddings.EmbeddingSettings]
                to use as defaults for this model.
        """
        self._model_name = model_name

        if isinstance(provider, str):
            provider = infer_provider(provider)
        self._provider = provider
        self._client = provider.client

        super().__init__(settings=settings)

    @property
    def base_url(self) -> str:
        return self._provider.base_url

    @property
    def model_name(self) -> GoogleEmbeddingModelName:
        """The embedding model name."""
        return self._model_name

    @property
    def system(self) -> str:
        """The embedding model provider."""
        return self._provider.name

    async def embed(
        self, inputs: str | Sequence[str], *, input_type: EmbedInputType, settings: EmbeddingSettings | None = None
    ) -> EmbeddingResult:
        inputs, settings = self.prepare_embed(inputs, settings)
        settings = cast(GoogleEmbeddingSettings, settings)

        google_task_type = settings.get('google_task_type')
        if google_task_type is None:
            google_task_type = 'RETRIEVAL_DOCUMENT' if input_type == 'document' else 'RETRIEVAL_QUERY'

        config = EmbedContentConfig(
            task_type=google_task_type,
            output_dimensionality=settings.get('dimensions'),
            title=settings.get('google_title'),
        )

        try:
            response = await self._client.aio.models.embed_content(
                model=self._model_name,
                contents=cast(ContentListUnion, inputs),
                config=config,
            )
        except errors.APIError as e:
            if (status_code := e.code) >= 400:
                raise ModelHTTPError(
                    status_code=status_code,
                    model_name=self._model_name,
                    body=cast(object, e.details),  # pyright: ignore[reportUnknownMemberType]
                ) from e
            raise  # pragma: no cover

        embeddings: list[list[float]] = [emb.values for emb in (response.embeddings or []) if emb.values is not None]

        return EmbeddingResult(
            embeddings=embeddings,
            inputs=inputs,
            input_type=input_type,
            usage=_map_usage(response, self.system, self.base_url, self._model_name),
            model_name=self._model_name,
            provider_name=self.system,
        )

    async def max_input_tokens(self) -> int | None:
        return _MAX_INPUT_TOKENS.get(self._model_name)

    async def count_tokens(self, text: str) -> int:
        try:
            response = await self._client.aio.models.count_tokens(
                model=self._model_name,
                contents=text,
            )
        except errors.APIError as e:
            if (status_code := e.code) >= 400:
                raise ModelHTTPError(
                    status_code=status_code,
                    model_name=self._model_name,
                    body=cast(object, e.details),  # pyright: ignore[reportUnknownMemberType]
                ) from e
            raise  # pragma: no cover

        if response.total_tokens is None:
            raise UnexpectedModelBehavior('Token counting returned no result')  # pragma: no cover
        return response.total_tokens

```

---|---
####  __init__
```
__init__(
    model_name: GoogleEmbeddingModelName[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.google.GoogleEmbeddingModelName "GoogleEmbeddingModelName



      module-attribute
   \(pydantic_ai.embeddings.google.GoogleEmbeddingModelName\)"),
    *,
    provider: (
        ["google-gla", "google-vertex"]
        | Provider[](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.Provider "pydantic_ai.providers.Provider")[Client]
    ) = "google-gla",
    settings: EmbeddingSettings[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.settings.EmbeddingSettings "EmbeddingSettings \(pydantic_ai.embeddings.settings.EmbeddingSettings\)") | None = None
)

```

Initialize a Google embedding model.
Parameters:
Name | Type | Description | Default
---|---|---|---
`model_name` |  `GoogleEmbeddingModelName[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.google.GoogleEmbeddingModelName "GoogleEmbeddingModelName



      module-attribute
   \(pydantic_ai.embeddings.google.GoogleEmbeddingModelName\)")` |  The name of the Google model to use. See  |  _required_
`provider` |  `Provider[](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.Provider "pydantic_ai.providers.Provider")[Client]` |  The provider to use for authentication and API access. Can be:
  * `'google-gla'` (default): Uses the Gemini API (Google AI Studio)
  * `'google-vertex'`: Uses Vertex AI
  * A [`GoogleProvider`](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.google.GoogleProvider "GoogleProvider") instance for custom configuration

|  `'google-gla'`
`settings` |  `EmbeddingSettings[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.settings.EmbeddingSettings "EmbeddingSettings \(pydantic_ai.embeddings.settings.EmbeddingSettings\)") | None` |  Model-specific [`EmbeddingSettings`](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.EmbeddingSettings "EmbeddingSettings") to use as defaults for this model. |  `None`
Source code in `pydantic_ai_slim/pydantic_ai/embeddings/google.py`
```
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
```
| ```
def __init__(
    self,
    model_name: GoogleEmbeddingModelName,
    *,
    provider: Literal['google-gla', 'google-vertex'] | Provider[Client] = 'google-gla',
    settings: EmbeddingSettings | None = None,
):
    """Initialize a Google embedding model.

    Args:
        model_name: The name of the Google model to use.
            See [Google Embeddings documentation](https://ai.google.dev/gemini-api/docs/embeddings)
            for available models.
        provider: The provider to use for authentication and API access. Can be:

            - `'google-gla'` (default): Uses the Gemini API (Google AI Studio)
            - `'google-vertex'`: Uses Vertex AI
            - A [`GoogleProvider`][pydantic_ai.providers.google.GoogleProvider] instance
              for custom configuration
        settings: Model-specific [`EmbeddingSettings`][pydantic_ai.embeddings.EmbeddingSettings]
            to use as defaults for this model.
    """
    self._model_name = model_name

    if isinstance(provider, str):
        provider = infer_provider(provider)
    self._provider = provider
    self._client = provider.client

    super().__init__(settings=settings)

```

---|---
####  model_name `property`
```
model_name: GoogleEmbeddingModelName[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.google.GoogleEmbeddingModelName "GoogleEmbeddingModelName



      module-attribute
   \(pydantic_ai.embeddings.google.GoogleEmbeddingModelName\)")

```

The embedding model name.
####  system `property`
```
system:

```

The embedding model provider.
###  LatestBedrockEmbeddingModelNames `module-attribute`
```
LatestBedrockEmbeddingModelNames = [
    "amazon.titan-embed-text-v1",
    "amazon.titan-embed-text-v2:0",
    "cohere.embed-english-v3",
    "cohere.embed-multilingual-v3",
    "cohere.embed-v4:0",
    "amazon.nova-2-multimodal-embeddings-v1:0",
]

```

Latest Bedrock embedding model names.
See
###  BedrockEmbeddingModelName `module-attribute`
```
BedrockEmbeddingModelName = (
     | LatestBedrockEmbeddingModelNames[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.bedrock.LatestBedrockEmbeddingModelNames "LatestBedrockEmbeddingModelNames



      module-attribute
   \(pydantic_ai.embeddings.bedrock.LatestBedrockEmbeddingModelNames\)")
)

```

Possible Bedrock embedding model names.
###  BedrockEmbeddingSettings
Bases: `EmbeddingSettings[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.settings.EmbeddingSettings "EmbeddingSettings \(pydantic_ai.embeddings.settings.EmbeddingSettings\)")`
Settings used for a Bedrock embedding model request.
All fields from [`EmbeddingSettings`](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.EmbeddingSettings "EmbeddingSettings") are supported, plus Bedrock-specific settings prefixed with `bedrock_`.
All settings are optional - if not specified, model defaults are used.
**Note on`dimensions` parameter support:**
  * **Titan v1** (`amazon.titan-embed-text-v1`): Not supported (fixed: 1536)
  * **Titan v2** (`amazon.titan-embed-text-v2:0`): Supported (default: 1024, accepts 256/384/1024)
  * **Cohere v3** (`cohere.embed-english-v3`, `cohere.embed-multilingual-v3`): Not supported (fixed: 1024)
  * **Cohere v4** (`cohere.embed-v4:0`): Supported (default: 1536, accepts 256/512/1024/1536)
  * **Nova** (`amazon.nova-2-multimodal-embeddings-v1:0`): Supported (default: 3072, accepts 256/384/1024/3072)


Unsupported settings are silently ignored.
**Note on`truncate` parameter support:**
  * **Titan models** (`amazon.titan-embed-text-v1`, `amazon.titan-embed-text-v2:0`): Not supported
  * **Cohere models** (all versions): Supported (default: `False`, maps to `'END'` when `True`)
  * **Nova** (`amazon.nova-2-multimodal-embeddings-v1:0`): Supported (default: `False`, maps to `'END'` when `True`)


For fine-grained truncation control, use model-specific settings: `bedrock_cohere_truncate` or `bedrock_nova_truncate`.
Example
```
from pydantic_ai.embeddings.bedrock import BedrockEmbeddingSettings

# Use model defaults
settings = BedrockEmbeddingSettings()

# Customize specific settings for Titan v2:0
settings = BedrockEmbeddingSettings(
    dimensions=512,
    bedrock_titan_normalize=True,
)

# Customize specific settings for Cohere v4
settings = BedrockEmbeddingSettings(
    dimensions=512,
    bedrock_cohere_max_tokens=1000,
)

```

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/bedrock.py`
```
 55
 56
 57
 58
 59
 60
 61
 62
 63
 64
 65
 66
 67
 68
 69
 70
 71
 72
 73
 74
 75
 76
 77
 78
 79
 80
 81
 82
 83
 84
 85
 86
 87
 88
 89
 90
 91
 92
 93
 94
 95
 96
 97
 98
 99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
```
| ```
class BedrockEmbeddingSettings(EmbeddingSettings, total=False):
    """Settings used for a Bedrock embedding model request.

    All fields from [`EmbeddingSettings`][pydantic_ai.embeddings.EmbeddingSettings] are supported,
    plus Bedrock-specific settings prefixed with `bedrock_`.

    All settings are optional - if not specified, model defaults are used.

    **Note on `dimensions` parameter support:**

    - **Titan v1** (`amazon.titan-embed-text-v1`): Not supported (fixed: 1536)
    - **Titan v2** (`amazon.titan-embed-text-v2:0`): Supported (default: 1024, accepts 256/384/1024)
    - **Cohere v3** (`cohere.embed-english-v3`, `cohere.embed-multilingual-v3`): Not supported (fixed: 1024)
    - **Cohere v4** (`cohere.embed-v4:0`): Supported (default: 1536, accepts 256/512/1024/1536)
    - **Nova** (`amazon.nova-2-multimodal-embeddings-v1:0`): Supported (default: 3072, accepts 256/384/1024/3072)

    Unsupported settings are silently ignored.

    **Note on `truncate` parameter support:**

    - **Titan models** (`amazon.titan-embed-text-v1`, `amazon.titan-embed-text-v2:0`): Not supported
    - **Cohere models** (all versions): Supported (default: `False`, maps to `'END'` when `True`)
    - **Nova** (`amazon.nova-2-multimodal-embeddings-v1:0`): Supported (default: `False`, maps to `'END'` when `True`)

    For fine-grained truncation control, use model-specific settings: `bedrock_cohere_truncate` or `bedrock_nova_truncate`.

    Example:
    ```python
        from pydantic_ai.embeddings.bedrock import BedrockEmbeddingSettings

        # Use model defaults
        settings = BedrockEmbeddingSettings()

        # Customize specific settings for Titan v2:0
        settings = BedrockEmbeddingSettings(
            dimensions=512,
            bedrock_titan_normalize=True,
        )

        # Customize specific settings for Cohere v4
        settings = BedrockEmbeddingSettings(
            dimensions=512,
            bedrock_cohere_max_tokens=1000,
        )
    ```
    """

    # ALL FIELDS MUST BE `bedrock_` PREFIXED SO YOU CAN MERGE THEM WITH OTHER MODELS.

    # ==================== Amazon Titan Settings ====================

    bedrock_titan_normalize: bool
    """Whether to normalize embedding vectors for Titan models.

    **Supported by:** `amazon.titan-embed-text-v2:0` (default: `True`)

    **Not supported by:** `amazon.titan-embed-text-v1` (silently ignored)

    When enabled, vectors are normalized for direct cosine similarity calculations.
    """

    # ==================== Cohere Settings ====================

    bedrock_cohere_max_tokens: int
    """The maximum number of tokens to embed for Cohere models.

    **Supported by:** `cohere.embed-v4:0` (default: 128000)

    **Not supported by:** `cohere.embed-english-v3`, `cohere.embed-multilingual-v3`
    (silently ignored)
    """

    bedrock_cohere_input_type: Literal['search_document', 'search_query', 'classification', 'clustering']
    """The input type for Cohere models.

    **Supported by:** All Cohere models (`cohere.embed-english-v3`, `cohere.embed-multilingual-v3`, `cohere.embed-v4:0`)

    By default, `embed_query()` uses `'search_query'` and `embed_documents()` uses `'search_document'`.
    Also accepts `'classification'` or `'clustering'`.
    """

    bedrock_cohere_truncate: Literal['NONE', 'START', 'END']
    """The truncation strategy for Cohere models. Overrides base `truncate` setting.

    **Supported by:** All Cohere models (`cohere.embed-english-v3`, `cohere.embed-multilingual-v3`, `cohere.embed-v4:0`)

    Default: `'NONE'`

    - `'NONE'`: Raise an error if input exceeds max tokens.
    - `'START'`: Truncate the start of the input.
    - `'END'`: Truncate the end of the input.
    """

    # ==================== Amazon Nova Settings ====================

    bedrock_nova_truncate: Literal['NONE', 'START', 'END']
    """The truncation strategy for Nova models. Overrides base `truncate` setting.

    **Supported by:** `amazon.nova-2-multimodal-embeddings-v1:0`

    Default: `'NONE'`

    - `'NONE'`: Raise an error if input exceeds max tokens.
    - `'START'`: Truncate the start of the input.
    - `'END'`: Truncate the end of the input.
    """

    bedrock_nova_embedding_purpose: Literal[
        'GENERIC_INDEX',
        'GENERIC_RETRIEVAL',
        'TEXT_RETRIEVAL',
        'CLASSIFICATION',
        'CLUSTERING',
    ]
    """The embedding purpose for Nova models.

    **Supported by:** `amazon.nova-2-multimodal-embeddings-v1:0`

    By default, `embed_query()` uses `'GENERIC_RETRIEVAL'` and `embed_documents()` uses `'GENERIC_INDEX'`.
    Also accepts `'TEXT_RETRIEVAL'`, `'CLASSIFICATION'`, or `'CLUSTERING'`.

    Note: Multimodal-specific purposes (`'IMAGE_RETRIEVAL'`, `'VIDEO_RETRIEVAL'`,
    `'DOCUMENT_RETRIEVAL'`, `'AUDIO_RETRIEVAL'`) are not supported as this
    embedding client only accepts text input.
    """

    # ==================== Concurrency Settings ====================

    bedrock_max_concurrency: int
    """Maximum number of concurrent requests for models that don't support batch embedding.

    **Applies to:** `amazon.titan-embed-text-v1`, `amazon.titan-embed-text-v2:0`,
    `amazon.nova-2-multimodal-embeddings-v1:0`

    When embedding multiple texts with models that only support single-text requests,
    this controls how many requests run in parallel. Defaults to 5.
    """

```

---|---
####  bedrock_titan_normalize `instance-attribute`
```
bedrock_titan_normalize:

```

Whether to normalize embedding vectors for Titan models.
**Supported by:** `amazon.titan-embed-text-v2:0` (default: `True`)
**Not supported by:** `amazon.titan-embed-text-v1` (silently ignored)
When enabled, vectors are normalized for direct cosine similarity calculations.
####  bedrock_cohere_max_tokens `instance-attribute`
```
bedrock_cohere_max_tokens:

```

The maximum number of tokens to embed for Cohere models.
**Supported by:** `cohere.embed-v4:0` (default: 128000)
**Not supported by:** `cohere.embed-english-v3`, `cohere.embed-multilingual-v3` (silently ignored)
####  bedrock_cohere_input_type `instance-attribute`
```
bedrock_cohere_input_type: [
    "search_document",
    "search_query",
    "classification",
    "clustering",
]

```

The input type for Cohere models.
**Supported by:** All Cohere models (`cohere.embed-english-v3`, `cohere.embed-multilingual-v3`, `cohere.embed-v4:0`)
By default, `embed_query()` uses `'search_query'` and `embed_documents()` uses `'search_document'`. Also accepts `'classification'` or `'clustering'`.
####  bedrock_cohere_truncate `instance-attribute`
```
bedrock_cohere_truncate: ['NONE', 'START', 'END']

```

The truncation strategy for Cohere models. Overrides base `truncate` setting.
**Supported by:** All Cohere models (`cohere.embed-english-v3`, `cohere.embed-multilingual-v3`, `cohere.embed-v4:0`)
Default: `'NONE'`
  * `'NONE'`: Raise an error if input exceeds max tokens.
  * `'START'`: Truncate the start of the input.
  * `'END'`: Truncate the end of the input.


####  bedrock_nova_truncate `instance-attribute`
```
bedrock_nova_truncate: ['NONE', 'START', 'END']

```

The truncation strategy for Nova models. Overrides base `truncate` setting.
**Supported by:** `amazon.nova-2-multimodal-embeddings-v1:0`
Default: `'NONE'`
  * `'NONE'`: Raise an error if input exceeds max tokens.
  * `'START'`: Truncate the start of the input.
  * `'END'`: Truncate the end of the input.


####  bedrock_nova_embedding_purpose `instance-attribute`
```
bedrock_nova_embedding_purpose: [
    "GENERIC_INDEX",
    "GENERIC_RETRIEVAL",
    "TEXT_RETRIEVAL",
    "CLASSIFICATION",
    "CLUSTERING",
]

```

The embedding purpose for Nova models.
**Supported by:** `amazon.nova-2-multimodal-embeddings-v1:0`
By default, `embed_query()` uses `'GENERIC_RETRIEVAL'` and `embed_documents()` uses `'GENERIC_INDEX'`. Also accepts `'TEXT_RETRIEVAL'`, `'CLASSIFICATION'`, or `'CLUSTERING'`.
Note: Multimodal-specific purposes (`'IMAGE_RETRIEVAL'`, `'VIDEO_RETRIEVAL'`, `'DOCUMENT_RETRIEVAL'`, `'AUDIO_RETRIEVAL'`) are not supported as this embedding client only accepts text input.
####  bedrock_max_concurrency `instance-attribute`
```
bedrock_max_concurrency:

```

Maximum number of concurrent requests for models that don't support batch embedding.
**Applies to:** `amazon.titan-embed-text-v1`, `amazon.titan-embed-text-v2:0`, `amazon.nova-2-multimodal-embeddings-v1:0`
When embedding multiple texts with models that only support single-text requests, this controls how many requests run in parallel. Defaults to 5.
###  BedrockEmbeddingModel `dataclass`
Bases: `EmbeddingModel[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.base.EmbeddingModel "EmbeddingModel \(pydantic_ai.embeddings.base.EmbeddingModel\)")`
Bedrock embedding model implementation.
This model works with AWS Bedrock's embedding models including Amazon Titan Embeddings and Cohere Embed models.
Example:
```
from pydantic_ai.embeddings.bedrock import BedrockEmbeddingModel
from pydantic_ai.providers.bedrock import BedrockProvider
