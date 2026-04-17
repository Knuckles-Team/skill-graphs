        self._client = provider.client

        super().__init__(settings=settings)

    @property
    def base_url(self) -> str:
        return str(self._client.base_url)

    @property
    def model_name(self) -> OpenAIEmbeddingModelName:
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
        settings = cast(OpenAIEmbeddingSettings, settings)

        try:
            response = await self._client.embeddings.create(
                input=inputs,
                model=self.model_name,
                dimensions=settings.get('dimensions') or OMIT,
                extra_headers=settings.get('extra_headers'),
                extra_body=settings.get('extra_body'),
            )
        except APIStatusError as e:
            if (status_code := e.status_code) >= 400:
                raise ModelHTTPError(status_code=status_code, model_name=self.model_name, body=e.body) from e
            raise  # pragma: lax no cover
        except APIConnectionError as e:  # pragma: no cover
            raise ModelAPIError(model_name=self.model_name, message=e.message) from e

        embeddings = [item.embedding for item in response.data]

        return EmbeddingResult(
            embeddings=embeddings,
            inputs=inputs,
            input_type=input_type,
            usage=_map_usage(response.usage, self.system, self.base_url, response.model),
            model_name=response.model,
            provider_name=self.system,
        )

    async def max_input_tokens(self) -> int | None:
        if self.system != 'openai':
            return None

        # https://platform.openai.com/docs/guides/embeddings#embedding-models
        return 8192

    async def count_tokens(self, text: str) -> int:
        if self.system != 'openai':
            raise UserError(
                'Counting tokens is not supported for non-OpenAI embedding models',
            )
        try:
            encoding = await _utils.run_in_executor(tiktoken.encoding_for_model, self.model_name)
        except KeyError as e:  # pragma: no cover
            raise ValueError(
                f'The embedding model {self.model_name!r} is not supported by tiktoken',
            ) from e
        return len(encoding.encode(text))

```

---|---
####  __init__
```
__init__(
    model_name: OpenAIEmbeddingModelName[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.openai.OpenAIEmbeddingModelName "OpenAIEmbeddingModelName



      module-attribute
   \(pydantic_ai.embeddings.openai.OpenAIEmbeddingModelName\)"),
    *,
    provider: (
        OpenAIEmbeddingsCompatibleProvider
        | ["openai"]
        | Provider[](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.Provider "pydantic_ai.providers.Provider")[AsyncOpenAI]
    ) = "openai",
    settings: EmbeddingSettings[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.settings.EmbeddingSettings "EmbeddingSettings \(pydantic_ai.embeddings.settings.EmbeddingSettings\)") | None = None
)

```

Initialize an OpenAI embedding model.
Parameters:
Name | Type | Description | Default
---|---|---|---
`model_name` |  `OpenAIEmbeddingModelName[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.openai.OpenAIEmbeddingModelName "OpenAIEmbeddingModelName



      module-attribute
   \(pydantic_ai.embeddings.openai.OpenAIEmbeddingModelName\)")` |  The name of the OpenAI model to use. See  |  _required_
`provider` |  `OpenAIEmbeddingsCompatibleProvider | Provider[](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.Provider "pydantic_ai.providers.Provider")[AsyncOpenAI]` |  The provider to use for authentication and API access. Can be:
  * `'openai'` (default): Uses the standard OpenAI API
  * A provider name string (e.g., `'azure'`, `'deepseek'`)
  * A [`Provider`](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.Provider) instance for custom configuration

See [OpenAI-compatible providers](https://ai.pydantic.dev/models/openai/#openai-compatible-models) for a list of supported providers. |  `'openai'`
`settings` |  `EmbeddingSettings[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.settings.EmbeddingSettings "EmbeddingSettings \(pydantic_ai.embeddings.settings.EmbeddingSettings\)") | None` |  Model-specific [`EmbeddingSettings`](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.EmbeddingSettings "EmbeddingSettings") to use as defaults for this model. |  `None`
Source code in `pydantic_ai_slim/pydantic_ai/embeddings/openai.py`
```
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
```
| ```
def __init__(
    self,
    model_name: OpenAIEmbeddingModelName,
    *,
    provider: OpenAIEmbeddingsCompatibleProvider | Literal['openai'] | Provider[AsyncOpenAI] = 'openai',
    settings: EmbeddingSettings | None = None,
):
    """Initialize an OpenAI embedding model.

    Args:
        model_name: The name of the OpenAI model to use.
            See [OpenAI's embedding models](https://platform.openai.com/docs/guides/embeddings)
            for available options.
        provider: The provider to use for authentication and API access. Can be:

            - `'openai'` (default): Uses the standard OpenAI API
            - A provider name string (e.g., `'azure'`, `'deepseek'`)
            - A [`Provider`][pydantic_ai.providers.Provider] instance for custom configuration

            See [OpenAI-compatible providers](../models/openai.md#openai-compatible-models)
            for a list of supported providers.
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
model_name: OpenAIEmbeddingModelName[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.openai.OpenAIEmbeddingModelName "OpenAIEmbeddingModelName



      module-attribute
   \(pydantic_ai.embeddings.openai.OpenAIEmbeddingModelName\)")

```

The embedding model name.
####  system `property`
```
system:

```

The embedding model provider.
###  LatestCohereEmbeddingModelNames `module-attribute`
```
LatestCohereEmbeddingModelNames = [
    "embed-v4.0",
    "embed-english-v3.0",
    "embed-english-light-v3.0",
    "embed-multilingual-v3.0",
    "embed-multilingual-light-v3.0",
]

```

Latest Cohere embeddings models.
See the
###  CohereEmbeddingModelName `module-attribute`
```
CohereEmbeddingModelName = (
     | LatestCohereEmbeddingModelNames[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.cohere.LatestCohereEmbeddingModelNames "LatestCohereEmbeddingModelNames



      module-attribute
   \(pydantic_ai.embeddings.cohere.LatestCohereEmbeddingModelNames\)")
)

```

Possible Cohere embeddings model names.
###  CohereEmbeddingSettings
Bases: `EmbeddingSettings[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.settings.EmbeddingSettings "EmbeddingSettings \(pydantic_ai.embeddings.settings.EmbeddingSettings\)")`
Settings used for a Cohere embedding model request.
All fields from [`EmbeddingSettings`](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.EmbeddingSettings "EmbeddingSettings") are supported, plus Cohere-specific settings prefixed with `cohere_`.
Source code in `pydantic_ai_slim/pydantic_ai/embeddings/cohere.py`
```
54
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
```
| ```
class CohereEmbeddingSettings(EmbeddingSettings, total=False):
    """Settings used for a Cohere embedding model request.

    All fields from [`EmbeddingSettings`][pydantic_ai.embeddings.EmbeddingSettings] are supported,
    plus Cohere-specific settings prefixed with `cohere_`.
    """

    # ALL FIELDS MUST BE `cohere_` PREFIXED SO YOU CAN MERGE THEM WITH OTHER MODELS.

    cohere_max_tokens: int
    """The maximum number of tokens to embed."""

    cohere_input_type: CohereEmbedInputType
    """The Cohere-specific input type for the embedding.

    Overrides the standard `input_type` argument. Options include:
    `'search_query'`, `'search_document'`, `'classification'`, `'clustering'`, and `'image'`.
    """

    cohere_truncate: V2EmbedRequestTruncate
    """The truncation strategy to use:

    - `'NONE'` (default): Raise an error if input exceeds max tokens.
    - `'END'`: Truncate the end of the input text.
    - `'START'`: Truncate the start of the input text.

    Note: This setting overrides the standard `truncate` boolean setting when specified.
    """

```

---|---
####  cohere_max_tokens `instance-attribute`
```
cohere_max_tokens:

```

The maximum number of tokens to embed.
####  cohere_input_type `instance-attribute`
```
cohere_input_type: EmbedInputType

```

The Cohere-specific input type for the embedding.
Overrides the standard `input_type` argument. Options include: `'search_query'`, `'search_document'`, `'classification'`, `'clustering'`, and `'image'`.
####  cohere_truncate `instance-attribute`
```
cohere_truncate: V2EmbedRequestTruncate

```

The truncation strategy to use:
  * `'NONE'` (default): Raise an error if input exceeds max tokens.
  * `'END'`: Truncate the end of the input text.
  * `'START'`: Truncate the start of the input text.


Note: This setting overrides the standard `truncate` boolean setting when specified.
###  CohereEmbeddingModel `dataclass`
Bases: `EmbeddingModel[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.base.EmbeddingModel "EmbeddingModel \(pydantic_ai.embeddings.base.EmbeddingModel\)")`
Cohere embedding model implementation.
This model works with Cohere's embeddings API, which offers multilingual support and various model sizes.
Example:
```
from pydantic_ai.embeddings.cohere import CohereEmbeddingModel

model = CohereEmbeddingModel('embed-v4.0')

```

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/cohere.py`
```
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
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
208
209
210
211
212
213
214
215
216
217
218
219
220
221
```
| ```
@dataclass(init=False)
class CohereEmbeddingModel(EmbeddingModel):
    """Cohere embedding model implementation.

    This model works with Cohere's embeddings API, which offers
    multilingual support and various model sizes.

    Example:
```python
    from pydantic_ai.embeddings.cohere import CohereEmbeddingModel

    model = CohereEmbeddingModel('embed-v4.0')
```
    """

    _model_name: CohereEmbeddingModelName = field(repr=False)
    _provider: Provider[AsyncClientV2] = field(repr=False)

    def __init__(
        self,
        model_name: CohereEmbeddingModelName,
        *,
        provider: Literal['cohere'] | Provider[AsyncClientV2] = 'cohere',
        settings: EmbeddingSettings | None = None,
    ):
        """Initialize a Cohere embedding model.

        Args:
            model_name: The name of the Cohere model to use.
                See [Cohere Embed documentation](https://docs.cohere.com/docs/cohere-embed)
                for available models.
            provider: The provider to use for authentication and API access. Can be:

                - `'cohere'` (default): Uses the standard Cohere API
                - A [`CohereProvider`][pydantic_ai.providers.cohere.CohereProvider] instance
                  for custom configuration
            settings: Model-specific [`EmbeddingSettings`][pydantic_ai.embeddings.EmbeddingSettings]
                to use as defaults for this model.
        """
        self._model_name = model_name

        if isinstance(provider, str):
            provider = infer_provider(provider)
        self._provider = provider
        self._client = provider.client
        self._v1_client = provider.v1_client if isinstance(provider, CohereProvider) else None

        super().__init__(settings=settings)

    @property
    def base_url(self) -> str:
        """The base URL for the provider API, if available."""
        return self._provider.base_url

    @property
    def model_name(self) -> CohereEmbeddingModelName:
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
        settings = cast(CohereEmbeddingSettings, settings)

        cohere_input_type = settings.get(
            'cohere_input_type', 'search_document' if input_type == 'document' else 'search_query'
        )

        request_options: RequestOptions = {}
        if extra_headers := settings.get('extra_headers'):  # pragma: no cover
            request_options['additional_headers'] = extra_headers
        if extra_body := settings.get('extra_body'):  # pragma: no cover
            request_options['additional_body_parameters'] = cast(dict[str, Any], extra_body)

        # Determine truncation strategy: cohere_truncate takes precedence over truncate
        if 'cohere_truncate' in settings:
            truncate = settings['cohere_truncate']
        elif settings.get('truncate'):
            truncate = 'END'
        else:
            truncate = 'NONE'

        try:
            response = await self._client.embed(
                model=self.model_name,
                texts=inputs,
                output_dimension=settings.get('dimensions'),
                input_type=cohere_input_type,
                max_tokens=settings.get('cohere_max_tokens'),
                truncate=truncate,
                request_options=request_options,
            )
        except ApiError as e:
            if (status_code := e.status_code) and status_code >= 400:
                raise ModelHTTPError(status_code=status_code, model_name=self.model_name, body=e.body) from e
            raise ModelAPIError(model_name=self.model_name, message=str(e)) from e  # pragma: no cover

        embeddings = response.embeddings.float_
        if embeddings is None:
            raise UnexpectedModelBehavior(  # pragma: no cover
                'The Cohere embeddings response did not have an `embeddings` field holding a list of floats',
                str(response),
            )

        return EmbeddingResult(
            embeddings=embeddings,
            inputs=inputs,
            input_type=input_type,
            usage=_map_usage(response, self.system, self.base_url, self.model_name),
            model_name=self.model_name,
            provider_name=self.system,
            provider_response_id=response.id,
        )

    async def max_input_tokens(self) -> int | None:
        return _MAX_INPUT_TOKENS.get(self.model_name)

    async def count_tokens(self, text: str) -> int:
        if self._v1_client is None:
            raise NotImplementedError('Counting tokens requires the Cohere v1 client')
        try:
            result = await self._v1_client.tokenize(
                model=self.model_name,
                text=text,  # Has a max length of 65536 characters
                offline=False,
            )
        except ApiError as e:  # pragma: no cover
            if (status_code := e.status_code) and status_code >= 400:
                raise ModelHTTPError(status_code=status_code, model_name=self.model_name, body=e.body) from e
            raise ModelAPIError(model_name=self.model_name, message=str(e)) from e

        return len(result.tokens)

```

---|---
####  __init__
```
__init__(
    model_name: CohereEmbeddingModelName[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.cohere.CohereEmbeddingModelName "CohereEmbeddingModelName



      module-attribute
   \(pydantic_ai.embeddings.cohere.CohereEmbeddingModelName\)"),
    *,
    provider: (
        ["cohere"] | Provider[](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.Provider "pydantic_ai.providers.Provider")[AsyncClientV2]
    ) = "cohere",
    settings: EmbeddingSettings[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.settings.EmbeddingSettings "EmbeddingSettings \(pydantic_ai.embeddings.settings.EmbeddingSettings\)") | None = None
)

```

Initialize a Cohere embedding model.
Parameters:
Name | Type | Description | Default
---|---|---|---
`model_name` |  `CohereEmbeddingModelName[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.cohere.CohereEmbeddingModelName "CohereEmbeddingModelName



      module-attribute
   \(pydantic_ai.embeddings.cohere.CohereEmbeddingModelName\)")` |  The name of the Cohere model to use. See  |  _required_
`provider` |  `Provider[](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.Provider "pydantic_ai.providers.Provider")[AsyncClientV2]` |  The provider to use for authentication and API access. Can be:
  * `'cohere'` (default): Uses the standard Cohere API
  * A [`CohereProvider`](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.cohere.CohereProvider "CohereProvider") instance for custom configuration

|  `'cohere'`
`settings` |  `EmbeddingSettings[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.settings.EmbeddingSettings "EmbeddingSettings \(pydantic_ai.embeddings.settings.EmbeddingSettings\)") | None` |  Model-specific [`EmbeddingSettings`](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.EmbeddingSettings "EmbeddingSettings") to use as defaults for this model. |  `None`
Source code in `pydantic_ai_slim/pydantic_ai/embeddings/cohere.py`
```
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
```
| ```
def __init__(
    self,
    model_name: CohereEmbeddingModelName,
    *,
    provider: Literal['cohere'] | Provider[AsyncClientV2] = 'cohere',
    settings: EmbeddingSettings | None = None,
):
    """Initialize a Cohere embedding model.

    Args:
        model_name: The name of the Cohere model to use.
            See [Cohere Embed documentation](https://docs.cohere.com/docs/cohere-embed)
            for available models.
        provider: The provider to use for authentication and API access. Can be:

            - `'cohere'` (default): Uses the standard Cohere API
            - A [`CohereProvider`][pydantic_ai.providers.cohere.CohereProvider] instance
              for custom configuration
        settings: Model-specific [`EmbeddingSettings`][pydantic_ai.embeddings.EmbeddingSettings]
            to use as defaults for this model.
    """
    self._model_name = model_name

    if isinstance(provider, str):
        provider = infer_provider(provider)
    self._provider = provider
    self._client = provider.client
    self._v1_client = provider.v1_client if isinstance(provider, CohereProvider) else None

    super().__init__(settings=settings)

```

---|---
####  base_url `property`
```
base_url:

```

The base URL for the provider API, if available.
####  model_name `property`
```
model_name: CohereEmbeddingModelName[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.cohere.CohereEmbeddingModelName "CohereEmbeddingModelName



      module-attribute
   \(pydantic_ai.embeddings.cohere.CohereEmbeddingModelName\)")

```

The embedding model name.
####  system `property`
```
system:

```

The embedding model provider.
###  LatestGoogleGLAEmbeddingModelNames `module-attribute`
```
LatestGoogleGLAEmbeddingModelNames = [
    "gemini-embedding-001"
]

```

Latest Google Gemini API (GLA) embedding models.
See the
###  LatestGoogleVertexEmbeddingModelNames `module-attribute`
```
LatestGoogleVertexEmbeddingModelNames = [
    "gemini-embedding-001",
    "text-embedding-005",
    "text-multilingual-embedding-002",
]

```

Latest Google Vertex AI embedding models.
See the
###  LatestGoogleEmbeddingModelNames `module-attribute`
```
LatestGoogleEmbeddingModelNames = (
    LatestGoogleGLAEmbeddingModelNames[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.google.LatestGoogleGLAEmbeddingModelNames "LatestGoogleGLAEmbeddingModelNames



      module-attribute
   \(pydantic_ai.embeddings.google.LatestGoogleGLAEmbeddingModelNames\)")
    | LatestGoogleVertexEmbeddingModelNames[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.google.LatestGoogleVertexEmbeddingModelNames "LatestGoogleVertexEmbeddingModelNames



      module-attribute
   \(pydantic_ai.embeddings.google.LatestGoogleVertexEmbeddingModelNames\)")
)

```

All latest Google embedding models (union of GLA and Vertex AI models).
###  GoogleEmbeddingModelName `module-attribute`
```
GoogleEmbeddingModelName = (
     | LatestGoogleEmbeddingModelNames[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.google.LatestGoogleEmbeddingModelNames "LatestGoogleEmbeddingModelNames



      module-attribute
   \(pydantic_ai.embeddings.google.LatestGoogleEmbeddingModelNames\)")
)

```

Possible Google embeddings model names.
###  GoogleEmbeddingSettings
Bases: `EmbeddingSettings[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.settings.EmbeddingSettings "EmbeddingSettings \(pydantic_ai.embeddings.settings.EmbeddingSettings\)")`
Settings used for a Google embedding model request.
All fields from [`EmbeddingSettings`](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.EmbeddingSettings "EmbeddingSettings") are supported, plus Google-specific settings prefixed with `google_`.
Source code in `pydantic_ai_slim/pydantic_ai/embeddings/google.py`
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
```
| ```
class GoogleEmbeddingSettings(EmbeddingSettings, total=False):
    """Settings used for a Google embedding model request.

    All fields from [`EmbeddingSettings`][pydantic_ai.embeddings.EmbeddingSettings] are supported,
    plus Google-specific settings prefixed with `google_`.
    """

    # ALL FIELDS MUST BE `google_` PREFIXED SO YOU CAN MERGE THEM WITH OTHER MODELS.

    google_task_type: str
    """The task type for the embedding.

    Overrides the automatic task type selection based on `input_type`.
    See [Google's task type documentation](https://ai.google.dev/gemini-api/docs/embeddings#task-types)
    for available options.
    """

    google_title: str
    """Optional title for the content being embedded.

    Only applicable when task_type is `RETRIEVAL_DOCUMENT`.
    """

```

---|---
####  google_task_type `instance-attribute`
```
google_task_type:

```

The task type for the embedding.
Overrides the automatic task type selection based on `input_type`. See
####  google_title `instance-attribute`
```
google_title:

```

Optional title for the content being embedded.
Only applicable when task_type is `RETRIEVAL_DOCUMENT`.
###  GoogleEmbeddingModel `dataclass`
Bases: `EmbeddingModel[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.base.EmbeddingModel "EmbeddingModel \(pydantic_ai.embeddings.base.EmbeddingModel\)")`
Google embedding model implementation.
This model works with Google's embeddings API via the `google-genai` SDK, supporting both the Gemini API (Google AI Studio) and Vertex AI.
Example:
```
from pydantic_ai.embeddings.google import GoogleEmbeddingModel
from pydantic_ai.providers.google import GoogleProvider

# Using Gemini API (requires GOOGLE_API_KEY env var)
model = GoogleEmbeddingModel('gemini-embedding-001')

# Using Vertex AI
model = GoogleEmbeddingModel(
    'gemini-embedding-001',
    provider=GoogleProvider(vertexai=True, project='my-project', location='us-central1'),
)

```

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/google.py`
```
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
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
208
209
210
211
212
```
| ```
@dataclass(init=False)
class GoogleEmbeddingModel(EmbeddingModel):
    """Google embedding model implementation.

    This model works with Google's embeddings API via the `google-genai` SDK,
    supporting both the Gemini API (Google AI Studio) and Vertex AI.

    Example:
```python
    from pydantic_ai.embeddings.google import GoogleEmbeddingModel
    from pydantic_ai.providers.google import GoogleProvider
