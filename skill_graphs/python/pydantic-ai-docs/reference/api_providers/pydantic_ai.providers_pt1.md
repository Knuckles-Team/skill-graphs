# `pydantic_ai.providers`
Bases: `InterfaceClient]`
Abstract class for a provider.
The provider is in charge of providing an authenticated client to the API.
Each provider only supports a specific interface. A interface can be supported by multiple providers.
For example, the `OpenAIChatModel` interface can be supported by the `OpenAIProvider` and the `DeepSeekProvider`.
Source code in `pydantic_ai_slim/pydantic_ai/providers/__init__.py`
```
16
17
18
19
20
21
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
```
| ```
class Provider(ABC, Generic[InterfaceClient]):
    """Abstract class for a provider.

    The provider is in charge of providing an authenticated client to the API.

    Each provider only supports a specific interface. A interface can be supported by multiple providers.

    For example, the `OpenAIChatModel` interface can be supported by the `OpenAIProvider` and the `DeepSeekProvider`.
    """

    _client: InterfaceClient

    @property
    @abstractmethod
    def name(self) -> str:
        """The provider name."""
        raise NotImplementedError()

    @property
    @abstractmethod
    def base_url(self) -> str:
        """The base URL for the provider API."""
        raise NotImplementedError()

    @property
    @abstractmethod
    def client(self) -> InterfaceClient:
        """The client for the provider."""
        raise NotImplementedError()

    @staticmethod
    def model_profile(model_name: str) -> ModelProfile | None:
        """The model profile for the named model, if available."""
        return None  # pragma: no cover

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(name={self.name}, base_url={self.base_url})'  # pragma: lax no cover

```

---|---
###  name `abstractmethod` `property`
```
name:

```

The provider name.
###  base_url `abstractmethod` `property`
```
base_url:

```

The base URL for the provider API.
###  client `abstractmethod` `property`
```
client: InterfaceClient

```

The client for the provider.
###  model_profile `staticmethod`
```
model_profile(model_name: ) -> ModelProfile[](https://ai.pydantic.dev/api/profiles/#pydantic_ai.profiles.ModelProfile "pydantic_ai.profiles.ModelProfile") | None

```

The model profile for the named model, if available.
Source code in `pydantic_ai_slim/pydantic_ai/providers/__init__.py`
```
46
47
48
49
```
| ```
@staticmethod
def model_profile(model_name: str) -> ModelProfile | None:
    """The model profile for the named model, if available."""
    return None  # pragma: no cover

```

---|---
Create a new Gateway provider.
Parameters:
Name | Type | Description | Default
---|---|---|---
`upstream_provider` |  `UpstreamProvider | ` |  The upstream provider to use. |  _required_
`route` |  |  The name of the provider or routing group to use to handle the request. If not provided, the default routing group for the API format will be used. |  `None`
`api_key` |  |  The API key to use for authentication. If not provided, the `PYDANTIC_AI_GATEWAY_API_KEY` environment variable will be used if available. |  `None`
`base_url` |  |  The base URL to use for the Gateway. If not provided, the `PYDANTIC_AI_GATEWAY_BASE_URL` environment variable will be used if available. Otherwise, defaults to `https://gateway.pydantic.dev/proxy`. |  `None`
`http_client` |  `AsyncClient | None` |  The HTTP client to use for the Gateway. |  `None`
Source code in `pydantic_ai_slim/pydantic_ai/providers/gateway.py`
```
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
```
| ```
def gateway_provider(
    upstream_provider: UpstreamProvider | str,
    /,
    *,
    # Every provider
    route: str | None = None,
    api_key: str | None = None,
    base_url: str | None = None,
    # OpenAI, Groq, Anthropic & Gemini - Only Bedrock doesn't have an HTTPX client.
    http_client: httpx.AsyncClient | None = None,
) -> Provider[Any]:
    """Create a new Gateway provider.

    Args:
        upstream_provider: The upstream provider to use.
        route: The name of the provider or routing group to use to handle the request. If not provided, the default
            routing group for the API format will be used.
        api_key: The API key to use for authentication. If not provided, the `PYDANTIC_AI_GATEWAY_API_KEY`
            environment variable will be used if available.
        base_url: The base URL to use for the Gateway. If not provided, the `PYDANTIC_AI_GATEWAY_BASE_URL`
            environment variable will be used if available. Otherwise, defaults to `https://gateway.pydantic.dev/proxy`.
        http_client: The HTTP client to use for the Gateway.
    """
    api_key = api_key or os.getenv('PYDANTIC_AI_GATEWAY_API_KEY', os.getenv('PAIG_API_KEY'))
    if not api_key:
        raise UserError(
            'Set the `PYDANTIC_AI_GATEWAY_API_KEY` environment variable or pass it via `gateway_provider(..., api_key=...)`'
            ' to use the Pydantic AI Gateway provider.'
        )

    base_url = (
        base_url or os.getenv('PYDANTIC_AI_GATEWAY_BASE_URL', os.getenv('PAIG_BASE_URL')) or _infer_base_url(api_key)
    )
    http_client = http_client or cached_async_http_client(provider=f'gateway/{upstream_provider}')
    http_client.event_hooks = {'request': [_request_hook(api_key)]}

    if route is None:
        # Use the implied providerId as the default route.
        route = normalize_gateway_provider(upstream_provider)

    base_url = _merge_url_path(base_url, route)

    if upstream_provider in ('openai', 'openai-chat', 'openai-responses', 'chat', 'responses'):
        from .openai import OpenAIProvider

        return OpenAIProvider(api_key=api_key, base_url=base_url, http_client=http_client)
    elif upstream_provider == 'groq':
        from .groq import GroqProvider

        return GroqProvider(api_key=api_key, base_url=base_url, http_client=http_client)
    elif upstream_provider == 'anthropic':
        from anthropic import AsyncAnthropic

        from .anthropic import AnthropicProvider

        return AnthropicProvider(
            anthropic_client=AsyncAnthropic(auth_token=api_key, base_url=base_url, http_client=http_client)
        )
    elif upstream_provider in ('bedrock', 'converse'):
        from .bedrock import BedrockProvider

        return BedrockProvider(
            api_key=api_key,
            base_url=base_url,
            region_name='pydantic-ai-gateway',  # Fake region name to avoid NoRegionError
        )
    elif upstream_provider in ('google-vertex', 'gemini'):
        from .google import GoogleProvider

        return GoogleProvider(vertexai=True, api_key=api_key, base_url=base_url, http_client=http_client)
    else:
        raise UserError(f'Unknown upstream provider: {upstream_provider}')

```

---|---
Bases: `Provider[](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.Provider "pydantic_ai.providers.Provider")[AsyncAnthropicClient]`
Provider for Anthropic API.
Source code in `pydantic_ai_slim/pydantic_ai/providers/anthropic.py`
```
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
94
```
| ```
class AnthropicProvider(Provider[AsyncAnthropicClient]):
    """Provider for Anthropic API."""

    @property
    def name(self) -> str:
        return 'anthropic'

    @property
    def base_url(self) -> str:
        return str(self._client.base_url)

    @property
    def client(self) -> AsyncAnthropicClient:
        return self._client

    @staticmethod
    def model_profile(model_name: str) -> ModelProfile | None:
        profile = anthropic_model_profile(model_name)
        return ModelProfile(json_schema_transformer=AnthropicJsonSchemaTransformer).update(profile)

    @overload
    def __init__(self, *, anthropic_client: AsyncAnthropicClient | None = None) -> None: ...

    @overload
    def __init__(
        self, *, api_key: str | None = None, base_url: str | None = None, http_client: httpx.AsyncClient | None = None
    ) -> None: ...

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | None = None,
        anthropic_client: AsyncAnthropicClient | None = None,
        http_client: httpx.AsyncClient | None = None,
    ) -> None:
        """Create a new Anthropic provider.

        Args:
            api_key: The API key to use for authentication, if not provided, the `ANTHROPIC_API_KEY` environment variable
                will be used if available.
            base_url: The base URL to use for the Anthropic API.
            anthropic_client: An existing Anthropic client to use. Accepts
                [`AsyncAnthropic`](https://github.com/anthropics/anthropic-sdk-python),
                [`AsyncAnthropicBedrock`](https://docs.anthropic.com/en/api/claude-on-amazon-bedrock),
                [`AsyncAnthropicFoundry`](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry), or
                [`AsyncAnthropicVertex`](https://docs.anthropic.com/en/api/claude-on-vertex-ai).
                If provided, the `api_key` and `http_client` arguments will be ignored.
            http_client: An existing `httpx.AsyncClient` to use for making HTTP requests.
        """
        if anthropic_client is not None:
            assert http_client is None, 'Cannot provide both `anthropic_client` and `http_client`'
            assert api_key is None, 'Cannot provide both `anthropic_client` and `api_key`'
            self._client = anthropic_client
        else:
            api_key = api_key or os.getenv('ANTHROPIC_API_KEY')
            if not api_key:
                raise UserError(
                    'Set the `ANTHROPIC_API_KEY` environment variable or pass it via `AnthropicProvider(api_key=...)`'
                    'to use the Anthropic provider.'
                )
            if http_client is not None:
                self._client = AsyncAnthropic(api_key=api_key, base_url=base_url, http_client=http_client)
            else:
                http_client = cached_async_http_client(provider='anthropic')
                self._client = AsyncAnthropic(api_key=api_key, base_url=base_url, http_client=http_client)

```

---|---
###  __init__
```
__init__(
    *, anthropic_client: AsyncAnthropicClient | None = None
) -> None

```

```
__init__(
    *,
    api_key:  | None = None,
    base_url:  | None = None,
    http_client: AsyncClient | None = None
) -> None

```

```
__init__(
    *,
    api_key:  | None = None,
    base_url:  | None = None,
    anthropic_client: AsyncAnthropicClient | None = None,
    http_client: AsyncClient | None = None
) -> None

```

Create a new Anthropic provider.
Parameters:
Name | Type | Description | Default
---|---|---|---
`api_key` |  |  The API key to use for authentication, if not provided, the `ANTHROPIC_API_KEY` environment variable will be used if available. |  `None`
`base_url` |  |  The base URL to use for the Anthropic API. |  `None`
`anthropic_client` |  `AsyncAnthropicClient | None` |  An existing Anthropic client to use. Accepts `api_key` and `http_client` arguments will be ignored. |  `None`
`http_client` |  `AsyncClient | None` |  An existing `httpx.AsyncClient` to use for making HTTP requests. |  `None`
Source code in `pydantic_ai_slim/pydantic_ai/providers/anthropic.py`
```
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
```
| ```
def __init__(
    self,
    *,
    api_key: str | None = None,
    base_url: str | None = None,
    anthropic_client: AsyncAnthropicClient | None = None,
    http_client: httpx.AsyncClient | None = None,
) -> None:
    """Create a new Anthropic provider.

    Args:
        api_key: The API key to use for authentication, if not provided, the `ANTHROPIC_API_KEY` environment variable
            will be used if available.
        base_url: The base URL to use for the Anthropic API.
        anthropic_client: An existing Anthropic client to use. Accepts
            [`AsyncAnthropic`](https://github.com/anthropics/anthropic-sdk-python),
            [`AsyncAnthropicBedrock`](https://docs.anthropic.com/en/api/claude-on-amazon-bedrock),
            [`AsyncAnthropicFoundry`](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry), or
            [`AsyncAnthropicVertex`](https://docs.anthropic.com/en/api/claude-on-vertex-ai).
            If provided, the `api_key` and `http_client` arguments will be ignored.
        http_client: An existing `httpx.AsyncClient` to use for making HTTP requests.
    """
    if anthropic_client is not None:
        assert http_client is None, 'Cannot provide both `anthropic_client` and `http_client`'
        assert api_key is None, 'Cannot provide both `anthropic_client` and `api_key`'
        self._client = anthropic_client
    else:
        api_key = api_key or os.getenv('ANTHROPIC_API_KEY')
        if not api_key:
            raise UserError(
                'Set the `ANTHROPIC_API_KEY` environment variable or pass it via `AnthropicProvider(api_key=...)`'
                'to use the Anthropic provider.'
            )
        if http_client is not None:
            self._client = AsyncAnthropic(api_key=api_key, base_url=base_url, http_client=http_client)
        else:
            http_client = cached_async_http_client(provider='anthropic')
            self._client = AsyncAnthropic(api_key=api_key, base_url=base_url, http_client=http_client)

```

---|---
###  GoogleProvider
Bases: `Provider[](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.Provider "pydantic_ai.providers.Provider")[Client]`
Provider for Google.
Source code in `pydantic_ai_slim/pydantic_ai/providers/google.py`
```
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
```
| ```
class GoogleProvider(Provider[Client]):
    """Provider for Google."""

    @property
    def name(self) -> str:
        return 'google-vertex' if self._client._api_client.vertexai else 'google-gla'  # type: ignore[reportPrivateUsage]

    @property
    def base_url(self) -> str:
        return str(self._client._api_client._http_options.base_url)  # type: ignore[reportPrivateUsage]

    @property
    def client(self) -> Client:
        return self._client

    @staticmethod
    def model_profile(model_name: str) -> ModelProfile | None:
        return google_model_profile(model_name)

    @overload
    def __init__(
        self, *, api_key: str, http_client: httpx.AsyncClient | None = None, base_url: str | None = None
    ) -> None: ...

    @overload
    def __init__(
        self,
        *,
        credentials: Credentials | None = None,
        project: str | None = None,
        location: VertexAILocation | Literal['global'] | str | None = None,
        http_client: httpx.AsyncClient | None = None,
        base_url: str | None = None,
    ) -> None: ...

    @overload
    def __init__(self, *, client: Client) -> None: ...

    @overload
    def __init__(
        self,
        *,
        vertexai: bool = False,
        api_key: str | None = None,
        http_client: httpx.AsyncClient | None = None,
        base_url: str | None = None,
    ) -> None: ...

    def __init__(
        self,
        *,
        api_key: str | None = None,
        credentials: Credentials | None = None,
        project: str | None = None,
        location: VertexAILocation | Literal['global'] | str | None = None,
        vertexai: bool | None = None,
        client: Client | None = None,
        http_client: httpx.AsyncClient | None = None,
        base_url: str | None = None,
    ) -> None:
        """Create a new Google provider.

        Args:
            api_key: The `API key <https://ai.google.dev/gemini-api/docs/api-key>`_ to
                use for authentication. It can also be set via the `GOOGLE_API_KEY` environment variable.
            credentials: The credentials to use for authentication when calling the Vertex AI APIs. Credentials can be
                obtained from environment variables and default credentials. For more information, see Set up
                Application Default Credentials. Applies to the Vertex AI API only.
            project: The Google Cloud project ID to use for quota. Can be obtained from environment variables
                (for example, GOOGLE_CLOUD_PROJECT). Applies to the Vertex AI API only.
            location: The location to send API requests to (for example, us-central1). Can be obtained from environment variables.
                Applies to the Vertex AI API only.
            vertexai: Force the use of the Vertex AI API. If `False`, the Google Generative Language API will be used.
                Defaults to `False` unless `location`, `project`, or `credentials` are provided.
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
####  __init__
```
__init__(
    *,
    api_key: ,
    http_client: AsyncClient | None = None,
    base_url:  | None = None
) -> None

```

```
__init__(
    *,
    credentials: Credentials | None = None,
    project:  | None = None,
    location: (
        VertexAILocation[](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.google.VertexAILocation "VertexAILocation



      module-attribute
   \(pydantic_ai.providers.google.VertexAILocation\)") | ["global"] |  | None
    ) = None,
    http_client: AsyncClient | None = None,
    base_url:  | None = None
) -> None

```

```
__init__(*, client: Client) -> None

```

```
__init__(
    *,
    vertexai:  = False,
    api_key:  | None = None,
    http_client: AsyncClient | None = None,
    base_url:  | None = None
) -> None

```

```
__init__(
    *,
    api_key:  | None = None,
    credentials: Credentials | None = None,
    project:  | None = None,
    location: (
        VertexAILocation[](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.google.VertexAILocation "VertexAILocation



      module-attribute
   \(pydantic_ai.providers.google.VertexAILocation\)") | ["global"] |  | None
    ) = None,
    vertexai:  | None = None,
    client: Client | None = None,
    http_client: AsyncClient | None = None,
    base_url:  | None = None
) -> None

```

Create a new Google provider.
Parameters:
Name | Type | Description | Default
---|---|---|---
`api_key` |  |  The `API key <https://ai.google.dev/gemini-api/docs/api-key>`_ to use for authentication. It can also be set via the `GOOGLE_API_KEY` environment variable. |  `None`
`credentials` |  `Credentials | None` |  The credentials to use for authentication when calling the Vertex AI APIs. Credentials can be obtained from environment variables and default credentials. For more information, see Set up Application Default Credentials. Applies to the Vertex AI API only. |  `None`
`project` |  |  The Google Cloud project ID to use for quota. Can be obtained from environment variables (for example, GOOGLE_CLOUD_PROJECT). Applies to the Vertex AI API only. |  `None`
`location` |  `VertexAILocation[](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.google.VertexAILocation "VertexAILocation



      module-attribute
   \(pydantic_ai.providers.google.VertexAILocation\)") | ` |  The location to send API requests to (for example, us-central1). Can be obtained from environment variables. Applies to the Vertex AI API only. |  `None`
`vertexai` |  |  Force the use of the Vertex AI API. If `False`, the Google Generative Language API will be used. Defaults to `False` unless `location`, `project`, or `credentials` are provided. |  `None`
`client` |  `Client | None` |  A pre-initialized client to use. |  `None`
`http_client` |  `AsyncClient | None` |  An existing `httpx.AsyncClient` to use for making HTTP requests. |  `None`
`base_url` |  |  The base URL for the Google API. |  `None`
Source code in `pydantic_ai_slim/pydantic_ai/providers/google.py`
```
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
```
| ```
def __init__(
    self,
    *,
    api_key: str | None = None,
    credentials: Credentials | None = None,
    project: str | None = None,
    location: VertexAILocation | Literal['global'] | str | None = None,
    vertexai: bool | None = None,
    client: Client | None = None,
    http_client: httpx.AsyncClient | None = None,
    base_url: str | None = None,
) -> None:
    """Create a new Google provider.

    Args:
        api_key: The `API key <https://ai.google.dev/gemini-api/docs/api-key>`_ to
            use for authentication. It can also be set via the `GOOGLE_API_KEY` environment variable.
        credentials: The credentials to use for authentication when calling the Vertex AI APIs. Credentials can be
            obtained from environment variables and default credentials. For more information, see Set up
            Application Default Credentials. Applies to the Vertex AI API only.
        project: The Google Cloud project ID to use for quota. Can be obtained from environment variables
            (for example, GOOGLE_CLOUD_PROJECT). Applies to the Vertex AI API only.
        location: The location to send API requests to (for example, us-central1). Can be obtained from environment variables.
            Applies to the Vertex AI API only.
        vertexai: Force the use of the Vertex AI API. If `False`, the Google Generative Language API will be used.
            Defaults to `False` unless `location`, `project`, or `credentials` are provided.
