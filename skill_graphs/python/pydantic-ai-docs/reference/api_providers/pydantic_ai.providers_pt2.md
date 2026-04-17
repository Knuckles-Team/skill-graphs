        client: A pre-initialized client to use.
        http_client: An existing `httpx.AsyncClient` to use for making HTTP requests.
        base_url: The base URL for the Google API.
    """
    if client is None:
        # NOTE: We are keeping GEMINI_API_KEY for backwards compatibility.
        api_key = api_key or os.getenv('GOOGLE_API_KEY') or os.getenv('GEMINI_API_KEY')

        vertex_ai_args_used = bool(location or project or credentials)
        if vertexai is None:
            vertexai = vertex_ai_args_used

        http_client = http_client or cached_async_http_client(
            provider='google-vertex' if vertexai else 'google-gla'
        )
        # Note: google-genai's HttpOptions.timeout defaults to None, which causes
        # the SDK to explicitly pass timeout=None to httpx, overriding any timeout
        # configured on the httpx client. We must set the timeout here to ensure
        # requests actually time out. Read the timeout from the http_client if set,
        # otherwise use the default. The value is converted from seconds to milliseconds.
        timeout_seconds = http_client.timeout.read or DEFAULT_HTTP_TIMEOUT
        timeout_ms = int(timeout_seconds * 1000)
        http_options = HttpOptions(
            base_url=base_url,
            headers={'User-Agent': get_user_agent()},
            httpx_async_client=http_client,
            timeout=timeout_ms,
        )
        if not vertexai:
            if api_key is None:
                raise UserError(
                    'Set the `GOOGLE_API_KEY` environment variable or pass it via `GoogleProvider(api_key=...)`'
                    'to use the Google Generative Language API.'
                )
            self._client = Client(vertexai=False, api_key=api_key, http_options=http_options)
        else:
            if vertex_ai_args_used:
                api_key = None

            if api_key is None:
                project = project or os.getenv('GOOGLE_CLOUD_PROJECT')
                # From https://github.com/pydantic/pydantic-ai/pull/2031/files#r2169682149:
                # Currently `us-central1` supports the most models by far of any region including `global`, but not
                # all of them. `us-central1` has all google models but is missing some Anthropic partner models,
                # which use `us-east5` instead. `global` has fewer models but higher availability.
                # For more details, check: https://cloud.google.com/vertex-ai/generative-ai/docs/learn/locations#available-regions
                location = location or os.getenv('GOOGLE_CLOUD_LOCATION') or 'us-central1'

            self._client = Client(
                vertexai=True,
                api_key=api_key,
                project=project,
                location=location,
                credentials=credentials,
                http_options=http_options,
            )
    else:
        self._client = client  # pragma: no cover

```

---|---
###  VertexAILocation `module-attribute`
```
VertexAILocation = [
    "asia-east1",
    "asia-east2",
    "asia-northeast1",
    "asia-northeast3",
    "asia-south1",
    "asia-southeast1",
    "australia-southeast1",
    "europe-central2",
    "europe-north1",
    "europe-southwest1",
    "europe-west1",
    "europe-west2",
    "europe-west3",
    "europe-west4",
    "europe-west6",
    "europe-west8",
    "europe-west9",
    "me-central1",
    "me-central2",
    "me-west1",
    "northamerica-northeast1",
    "southamerica-east1",
    "us-central1",
    "us-east1",
    "us-east4",
    "us-east5",
    "us-south1",
    "us-west1",
    "us-west4",
]

```

Regions available for Vertex AI. More details
###  OpenAIProvider
Bases: `Provider[](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.Provider "pydantic_ai.providers.Provider")[AsyncOpenAI]`
Provider for OpenAI API.
Source code in `pydantic_ai_slim/pydantic_ai/providers/openai.py`
```
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
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
82
83
84
85
86
```
| ```
class OpenAIProvider(Provider[AsyncOpenAI]):
    """Provider for OpenAI API."""

    @property
    def name(self) -> str:
        return 'openai'

    @property
    def base_url(self) -> str:
        return str(self.client.base_url)

    @property
    def client(self) -> AsyncOpenAI:
        return self._client

    @staticmethod
    def model_profile(model_name: str) -> ModelProfile | None:
        return openai_model_profile(model_name)

    @overload
    def __init__(self, *, openai_client: AsyncOpenAI) -> None: ...

    @overload
    def __init__(
        self,
        base_url: str | None = None,
        api_key: str | None = None,
        openai_client: None = None,
        http_client: httpx.AsyncClient | None = None,
    ) -> None: ...

    def __init__(
        self,
        base_url: str | None = None,
        api_key: str | None = None,
        openai_client: AsyncOpenAI | None = None,
        http_client: httpx.AsyncClient | None = None,
    ) -> None:
        """Create a new OpenAI provider.

        Args:
            base_url: The base url for the OpenAI requests. If not provided, the `OPENAI_BASE_URL` environment variable
                will be used if available. Otherwise, defaults to OpenAI's base url.
            api_key: The API key to use for authentication, if not provided, the `OPENAI_API_KEY` environment variable
                will be used if available.
            openai_client: An existing
                [`AsyncOpenAI`](https://github.com/openai/openai-python?tab=readme-ov-file#async-usage)
                client to use. If provided, `base_url`, `api_key`, and `http_client` must be `None`.
            http_client: An existing `httpx.AsyncClient` to use for making HTTP requests.
        """
        # This is a workaround for the OpenAI client requiring an API key, whilst locally served,
        # openai compatible models do not always need an API key, but a placeholder (non-empty) key is required.
        if api_key is None and 'OPENAI_API_KEY' not in os.environ and base_url is not None and openai_client is None:
            api_key = 'api-key-not-set'

        if openai_client is not None:
            assert base_url is None, 'Cannot provide both `openai_client` and `base_url`'
            assert http_client is None, 'Cannot provide both `openai_client` and `http_client`'
            assert api_key is None, 'Cannot provide both `openai_client` and `api_key`'
            self._client = openai_client
        elif http_client is not None:
            self._client = AsyncOpenAI(base_url=base_url, api_key=api_key, http_client=http_client)
        else:
            http_client = cached_async_http_client(provider='openai')
            self._client = AsyncOpenAI(base_url=base_url, api_key=api_key, http_client=http_client)

```

---|---
####  __init__
```
__init__(*, openai_client: AsyncOpenAI) -> None

```

```
__init__(
    base_url:  | None = None,
    api_key:  | None = None,
    openai_client: None = None,
    http_client: AsyncClient | None = None,
) -> None

```

```
__init__(
    base_url:  | None = None,
    api_key:  | None = None,
    openai_client: AsyncOpenAI | None = None,
    http_client: AsyncClient | None = None,
) -> None

```

Create a new OpenAI provider.
Parameters:
Name | Type | Description | Default
---|---|---|---
`base_url` |  |  The base url for the OpenAI requests. If not provided, the `OPENAI_BASE_URL` environment variable will be used if available. Otherwise, defaults to OpenAI's base url. |  `None`
`api_key` |  |  The API key to use for authentication, if not provided, the `OPENAI_API_KEY` environment variable will be used if available. |  `None`
`openai_client` |  `AsyncOpenAI | None` |  An existing `base_url`, `api_key`, and `http_client` must be `None`. |  `None`
`http_client` |  `AsyncClient | None` |  An existing `httpx.AsyncClient` to use for making HTTP requests. |  `None`
Source code in `pydantic_ai_slim/pydantic_ai/providers/openai.py`
```
53
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
82
83
84
85
86
```
| ```
def __init__(
    self,
    base_url: str | None = None,
    api_key: str | None = None,
    openai_client: AsyncOpenAI | None = None,
    http_client: httpx.AsyncClient | None = None,
) -> None:
    """Create a new OpenAI provider.

    Args:
        base_url: The base url for the OpenAI requests. If not provided, the `OPENAI_BASE_URL` environment variable
            will be used if available. Otherwise, defaults to OpenAI's base url.
        api_key: The API key to use for authentication, if not provided, the `OPENAI_API_KEY` environment variable
            will be used if available.
        openai_client: An existing
            [`AsyncOpenAI`](https://github.com/openai/openai-python?tab=readme-ov-file#async-usage)
            client to use. If provided, `base_url`, `api_key`, and `http_client` must be `None`.
        http_client: An existing `httpx.AsyncClient` to use for making HTTP requests.
    """
    # This is a workaround for the OpenAI client requiring an API key, whilst locally served,
    # openai compatible models do not always need an API key, but a placeholder (non-empty) key is required.
    if api_key is None and 'OPENAI_API_KEY' not in os.environ and base_url is not None and openai_client is None:
        api_key = 'api-key-not-set'

    if openai_client is not None:
        assert base_url is None, 'Cannot provide both `openai_client` and `base_url`'
        assert http_client is None, 'Cannot provide both `openai_client` and `http_client`'
        assert api_key is None, 'Cannot provide both `openai_client` and `api_key`'
        self._client = openai_client
    elif http_client is not None:
        self._client = AsyncOpenAI(base_url=base_url, api_key=api_key, http_client=http_client)
    else:
        http_client = cached_async_http_client(provider='openai')
        self._client = AsyncOpenAI(base_url=base_url, api_key=api_key, http_client=http_client)

```

---|---
###  XaiProvider
Bases: `Provider[](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.Provider "pydantic_ai.providers.Provider")[AsyncClient]`
Provider for xAI API (native xAI SDK).
Source code in `pydantic_ai_slim/pydantic_ai/providers/xai.py`
```
 50
 51
 52
 53
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
```
| ```
class XaiProvider(Provider[AsyncClient]):
    """Provider for xAI API (native xAI SDK)."""

    @property
    def name(self) -> str:
        return 'xai'

    @property
    def base_url(self) -> str:
        return 'https://api.x.ai/v1'

    @property
    def client(self) -> AsyncClient:
        if self._lazy_client is not None:
            return self._lazy_client.get_client()
        return self._client

    @staticmethod
    def model_profile(model_name: str) -> ModelProfile | None:
        return grok_model_profile(model_name)

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, *, api_key: str) -> None: ...

    @overload
    def __init__(self, *, xai_client: AsyncClient) -> None: ...

    def __init__(
        self,
        *,
        api_key: str | None = None,
        xai_client: AsyncClient | None = None,
    ) -> None:
        """Create a new xAI provider.

        Args:
            api_key: The API key to use for authentication, if not provided, the `XAI_API_KEY` environment variable
                will be used if available.
            xai_client: An existing `xai_sdk.AsyncClient` to use.  This takes precedence over `api_key`.
        """
        self._lazy_client: _LazyAsyncClient | None = None
        if xai_client is not None:
            self._client = xai_client
        else:
            api_key = api_key or os.getenv('XAI_API_KEY')
            if not api_key:
                raise UserError(
                    'Set the `XAI_API_KEY` environment variable or pass it via `XaiProvider(api_key=...)`'
                    'to use the xAI provider.'
                )
            self._lazy_client = _LazyAsyncClient(api_key=api_key)
            self._client = None  # type: ignore[assignment]

```

---|---
####  __init__
```
__init__() -> None

```

```
__init__(*, api_key: ) -> None

```

```
__init__(*, xai_client: AsyncClient) -> None

```

```
__init__(
    *,
    api_key:  | None = None,
    xai_client: AsyncClient | None = None
) -> None

```

Create a new xAI provider.
Parameters:
Name | Type | Description | Default
---|---|---|---
`api_key` |  |  The API key to use for authentication, if not provided, the `XAI_API_KEY` environment variable will be used if available. |  `None`
`xai_client` |  `AsyncClient | None` |  An existing `xai_sdk.AsyncClient` to use. This takes precedence over `api_key`. |  `None`
Source code in `pydantic_ai_slim/pydantic_ai/providers/xai.py`
```
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
```
| ```
def __init__(
    self,
    *,
    api_key: str | None = None,
    xai_client: AsyncClient | None = None,
) -> None:
    """Create a new xAI provider.

    Args:
        api_key: The API key to use for authentication, if not provided, the `XAI_API_KEY` environment variable
            will be used if available.
        xai_client: An existing `xai_sdk.AsyncClient` to use.  This takes precedence over `api_key`.
    """
    self._lazy_client: _LazyAsyncClient | None = None
    if xai_client is not None:
        self._client = xai_client
    else:
        api_key = api_key or os.getenv('XAI_API_KEY')
        if not api_key:
            raise UserError(
                'Set the `XAI_API_KEY` environment variable or pass it via `XaiProvider(api_key=...)`'
                'to use the xAI provider.'
            )
        self._lazy_client = _LazyAsyncClient(api_key=api_key)
        self._client = None  # type: ignore[assignment]

```

---|---
###  DeepSeekProvider
Bases: `Provider[](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.Provider "pydantic_ai.providers.Provider")[AsyncOpenAI]`
Provider for DeepSeek API.
Source code in `pydantic_ai_slim/pydantic_ai/providers/deepseek.py`
```
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
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
```
| ```
class DeepSeekProvider(Provider[AsyncOpenAI]):
    """Provider for DeepSeek API."""

    @property
    def name(self) -> str:
        return 'deepseek'

    @property
    def base_url(self) -> str:
        return 'https://api.deepseek.com'

    @property
    def client(self) -> AsyncOpenAI:
        return self._client

    @staticmethod
    def model_profile(model_name: str) -> ModelProfile | None:
        profile = deepseek_model_profile(model_name)

        # As DeepSeekProvider is always used with OpenAIChatModel, which used to unconditionally use OpenAIJsonSchemaTransformer,
        # we need to maintain that behavior unless json_schema_transformer is set explicitly.
        # This was not the case when using a DeepSeek model with another model class (e.g. BedrockConverseModel or GroqModel),
        # so we won't do this in `deepseek_model_profile` unless we learn it's always needed.
        return OpenAIModelProfile(
            json_schema_transformer=OpenAIJsonSchemaTransformer,
            supports_json_object_output=True,
            openai_chat_thinking_field='reasoning_content',
            # Starting from DeepSeek v3.2, DeepSeek requires sending thinking parts for optimal agentic performance.
            openai_chat_send_back_thinking_parts='field',
            # DeepSeek v3.2 reasoning mode does not support tool_choice=required yet
            openai_supports_tool_choice_required=(model_name != 'deepseek-reasoner'),
        ).update(profile)

    @overload
    def __init__(self, *, openai_client: AsyncOpenAI) -> None: ...

    @overload
    def __init__(
        self,
        *,
        api_key: str | None = None,
        openai_client: None = None,
        http_client: httpx.AsyncClient | None = None,
    ) -> None: ...

    def __init__(
        self,
        *,
        api_key: str | None = None,
        openai_client: AsyncOpenAI | None = None,
        http_client: httpx.AsyncClient | None = None,
    ) -> None:
        api_key = api_key or os.getenv('DEEPSEEK_API_KEY')
        if not api_key and openai_client is None:
            raise UserError(
                'Set the `DEEPSEEK_API_KEY` environment variable or pass it via `DeepSeekProvider(api_key=...)`'
                'to use the DeepSeek provider.'
            )

        if openai_client is not None:
            self._client = openai_client
        elif http_client is not None:
            self._client = AsyncOpenAI(base_url=self.base_url, api_key=api_key, http_client=http_client)
        else:
            http_client = cached_async_http_client(provider='deepseek')
            self._client = AsyncOpenAI(base_url=self.base_url, api_key=api_key, http_client=http_client)

```

---|---
###  BedrockModelProfile `dataclass`
Bases: `ModelProfile[](https://ai.pydantic.dev/api/profiles/#pydantic_ai.profiles.ModelProfile "pydantic_ai.ModelProfile")`
Profile for models used with BedrockModel.
ALL FIELDS MUST BE `bedrock_` PREFIXED SO YOU CAN MERGE THEM WITH OTHER MODELS.
Source code in `pydantic_ai_slim/pydantic_ai/providers/bedrock.py`
```
34
35
36
37
38
39
40
41
42
43
44
45
```
| ```
@dataclass(kw_only=True)
class BedrockModelProfile(ModelProfile):
    """Profile for models used with BedrockModel.

    ALL FIELDS MUST BE `bedrock_` PREFIXED SO YOU CAN MERGE THEM WITH OTHER MODELS.
    """

    bedrock_supports_tool_choice: bool = False
    bedrock_tool_result_format: Literal['text', 'json'] = 'text'
    bedrock_send_back_thinking_parts: bool = False
    bedrock_supports_prompt_caching: bool = False
    bedrock_supports_tool_caching: bool = False

```

---|---
###  bedrock_amazon_model_profile
```
bedrock_amazon_model_profile(
    model_name: ,
) -> ModelProfile[](https://ai.pydantic.dev/api/profiles/#pydantic_ai.profiles.ModelProfile "pydantic_ai.ModelProfile") | None

```

Get the model profile for an Amazon model used via Bedrock.
Source code in `pydantic_ai_slim/pydantic_ai/providers/bedrock.py`
```
48
49
50
51
52
53
54
55
56
57
58
59
60
```
| ```
def bedrock_amazon_model_profile(model_name: str) -> ModelProfile | None:
    """Get the model profile for an Amazon model used via Bedrock."""
    profile = _without_builtin_tools(amazon_model_profile(model_name))
    if 'nova' in model_name:
        profile = BedrockModelProfile(
            bedrock_supports_tool_choice=True,
            bedrock_supports_prompt_caching=True,
        ).update(profile)

    if 'nova-2' in model_name:
        profile.supported_builtin_tools = frozenset({CodeExecutionTool})

    return profile

```

---|---
###  bedrock_deepseek_model_profile
```
bedrock_deepseek_model_profile(
    model_name: ,
) -> ModelProfile[](https://ai.pydantic.dev/api/profiles/#pydantic_ai.profiles.ModelProfile "pydantic_ai.ModelProfile") | None

```

Get the model profile for a DeepSeek model used via Bedrock.
Source code in `pydantic_ai_slim/pydantic_ai/providers/bedrock.py`
```
63
64
65
66
67
68
```
| ```
def bedrock_deepseek_model_profile(model_name: str) -> ModelProfile | None:
    """Get the model profile for a DeepSeek model used via Bedrock."""
    profile = deepseek_model_profile(model_name)
    if 'r1' in model_name:
        return BedrockModelProfile(bedrock_send_back_thinking_parts=True).update(profile)
    return profile  # pragma: no cover

```

---|---
###  remove_bedrock_geo_prefix
```
remove_bedrock_geo_prefix(model_name: ) ->

```

Remove inference geographic prefix from model ID if present.
Bedrock supports cross-region inference using geographic prefixes like 'us.', 'eu.', 'apac.', etc. This function strips those prefixes.
Example
'us.amazon.titan-embed-text-v2:0' -> 'amazon.titan-embed-text-v2:0' 'amazon.titan-embed-text-v2:0' -> 'amazon.titan-embed-text-v2:0'
Source code in `pydantic_ai_slim/pydantic_ai/providers/bedrock.py`
```
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
```
| ```
def remove_bedrock_geo_prefix(model_name: str) -> str:
    """Remove inference geographic prefix from model ID if present.

    Bedrock supports cross-region inference using geographic prefixes like
    'us.', 'eu.', 'apac.', etc. This function strips those prefixes.

    Example:
        'us.amazon.titan-embed-text-v2:0' -> 'amazon.titan-embed-text-v2:0'
        'amazon.titan-embed-text-v2:0' -> 'amazon.titan-embed-text-v2:0'
    """
    for prefix in BEDROCK_GEO_PREFIXES:
        if model_name.startswith(f'{prefix}.'):
            return model_name.removeprefix(f'{prefix}.')
    return model_name

```

---|---
###  BedrockProvider
Bases: `Provider[](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.Provider "pydantic_ai.providers.Provider")[BaseClient]`
Provider for AWS Bedrock.
Source code in `pydantic_ai_slim/pydantic_ai/providers/bedrock.py`
```
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
222
223
224
225
226
227
228
229
230
231
232
233
234
235
236
237
238
239
240
241
242
243
244
245
246
247
248
```
| ```
class BedrockProvider(Provider[BaseClient]):
    """Provider for AWS Bedrock."""

    @property
    def name(self) -> str:
        return 'bedrock'

    @property
    def base_url(self) -> str:
        return self._client.meta.endpoint_url

    @property
    def client(self) -> BaseClient:
        return self._client

    @staticmethod
    def model_profile(model_name: str) -> ModelProfile | None:
        provider_to_profile: dict[str, Callable[[str], ModelProfile | None]] = {
            'anthropic': lambda model_name: replace(
                BedrockModelProfile(
                    bedrock_supports_tool_choice=True,
                    bedrock_send_back_thinking_parts=True,
                    bedrock_supports_prompt_caching=True,
                    bedrock_supports_tool_caching=True,
                ).update(_without_builtin_tools(anthropic_model_profile(model_name))),
                # We don't currently support native structured output with Bedrock.
                # See https://github.com/pydantic/pydantic-ai/issues/4209.
                supports_json_schema_output=False,
            ),
            'mistral': lambda model_name: BedrockModelProfile(bedrock_tool_result_format='json').update(
                _without_builtin_tools(mistral_model_profile(model_name))
            ),
            'cohere': lambda model_name: _without_builtin_tools(cohere_model_profile(model_name)),
            'amazon': bedrock_amazon_model_profile,
            'meta': lambda model_name: _without_builtin_tools(meta_model_profile(model_name)),
            'deepseek': lambda model_name: _without_builtin_tools(bedrock_deepseek_model_profile(model_name)),
        }

        # Split the model name into parts
        parts = model_name.split('.', 2)

        # Handle regional prefixes
        if len(parts) > 2 and parts[0] in BEDROCK_GEO_PREFIXES:
            parts = parts[1:]

        # required format is provider.model-name-with-version
        if len(parts) < 2:
            return None

        provider = parts[0]
        model_name_with_version = parts[1]

        # Remove version suffix if it matches the format (e.g. "-v1:0" or "-v14")
        version_match = re.match(r'(.+)-v\d+(?::\d+)?$', model_name_with_version)
        if version_match:
            model_name = version_match.group(1)
        else:
            model_name = model_name_with_version

        if provider in provider_to_profile:
            return provider_to_profile[provider](model_name)

        return None

    @overload
    def __init__(self, *, bedrock_client: BaseClient) -> None: ...

    @overload
    def __init__(
        self,
        *,
        api_key: str,
        base_url: str | None = None,
        region_name: str | None = None,
        profile_name: str | None = None,
        aws_read_timeout: float | None = None,
        aws_connect_timeout: float | None = None,
    ) -> None: ...

    @overload
    def __init__(
        self,
        *,
        aws_access_key_id: str | None = None,
        aws_secret_access_key: str | None = None,
        aws_session_token: str | None = None,
        base_url: str | None = None,
        region_name: str | None = None,
        profile_name: str | None = None,
        aws_read_timeout: float | None = None,
        aws_connect_timeout: float | None = None,
    ) -> None: ...

    def __init__(
        self,
        *,
        bedrock_client: BaseClient | None = None,
        aws_access_key_id: str | None = None,
        aws_secret_access_key: str | None = None,
        aws_session_token: str | None = None,
        base_url: str | None = None,
