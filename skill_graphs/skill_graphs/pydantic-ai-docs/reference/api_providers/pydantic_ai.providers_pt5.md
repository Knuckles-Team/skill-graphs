        # unless json_schema_transformer is set explicitly
        return OpenAIModelProfile(json_schema_transformer=OpenAIJsonSchemaTransformer).update(profile)

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, *, api_key: str) -> None: ...

    @overload
    def __init__(self, *, api_key: str, http_client: httpx.AsyncClient) -> None: ...

    @overload
    def __init__(self, *, openai_client: AsyncOpenAI | None = None) -> None: ...

    def __init__(
        self,
        *,
        api_key: str | None = None,
        openai_client: AsyncOpenAI | None = None,
        http_client: httpx.AsyncClient | None = None,
    ) -> None:
        api_key = api_key or os.getenv('FIREWORKS_API_KEY')
        if not api_key and openai_client is None:
            raise UserError(
                'Set the `FIREWORKS_API_KEY` environment variable or pass it via `FireworksProvider(api_key=...)`'
                'to use the Fireworks AI provider.'
            )

        if openai_client is not None:
            self._client = openai_client
        elif http_client is not None:
            self._client = AsyncOpenAI(base_url=self.base_url, api_key=api_key, http_client=http_client)
        else:
            http_client = cached_async_http_client(provider='fireworks')
            self._client = AsyncOpenAI(base_url=self.base_url, api_key=api_key, http_client=http_client)

```

---|---
Bases: `Provider[](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.Provider "pydantic_ai.providers.Provider")[AsyncOpenAI]`
Deprecated
`GrokProvider` is deprecated, use `XaiProvider` with `XaiModel` instead for the native xAI SDK. See <https://ai.pydantic.dev/models/xai/> for more details.
Provider for Grok API (OpenAI-compatible interface).
Source code in `pydantic_ai_slim/pydantic_ai/providers/grok.py`
```
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
```
| ```
@deprecated(
    '`GrokProvider` is deprecated, use `XaiProvider` with `XaiModel` instead for the native xAI SDK. '
    'See <https://ai.pydantic.dev/models/xai/> for more details.'
)
class GrokProvider(Provider[AsyncOpenAI]):
    """Provider for Grok API (OpenAI-compatible interface)."""

    @property
    def name(self) -> str:
        return 'grok'

    @property
    def base_url(self) -> str:
        return 'https://api.x.ai/v1'

    @property
    def client(self) -> AsyncOpenAI:
        return self._client

    @staticmethod
    def model_profile(model_name: str) -> ModelProfile | None:
        profile = grok_model_profile(model_name)

        # As the Grok API is OpenAI-compatible, let's assume we also need OpenAIJsonSchemaTransformer,
        # unless json_schema_transformer is set explicitly.
        # Also, Grok does not support strict tool definitions: https://github.com/pydantic/pydantic-ai/issues/1846
        return OpenAIModelProfile(
            json_schema_transformer=OpenAIJsonSchemaTransformer, openai_supports_strict_tool_definition=False
        ).update(profile)

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, *, api_key: str) -> None: ...

    @overload
    def __init__(self, *, api_key: str, http_client: httpx.AsyncClient) -> None: ...

    @overload
    def __init__(self, *, openai_client: AsyncOpenAI | None = None) -> None: ...

    def __init__(
        self,
        *,
        api_key: str | None = None,
        openai_client: AsyncOpenAI | None = None,
        http_client: httpx.AsyncClient | None = None,
    ) -> None:
        api_key = api_key or os.getenv('GROK_API_KEY')
        if not api_key and openai_client is None:
            raise UserError(
                'Set the `GROK_API_KEY` environment variable or pass it via `GrokProvider(api_key=...)`'
                'to use the Grok provider.'
            )

        if openai_client is not None:
            self._client = openai_client
        elif http_client is not None:
            self._client = AsyncOpenAI(base_url=self.base_url, api_key=api_key, http_client=http_client)
        else:
            http_client = cached_async_http_client(provider='grok')
            self._client = AsyncOpenAI(base_url=self.base_url, api_key=api_key, http_client=http_client)

```

---|---
Bases: `Provider[](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.Provider "pydantic_ai.providers.Provider")[AsyncOpenAI]`
Provider for Together AI API.
Source code in `pydantic_ai_slim/pydantic_ai/providers/together.py`
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
95
96
97
```
| ```
class TogetherProvider(Provider[AsyncOpenAI]):
    """Provider for Together AI API."""

    @property
    def name(self) -> str:
        return 'together'

    @property
    def base_url(self) -> str:
        return 'https://api.together.xyz/v1'

    @property
    def client(self) -> AsyncOpenAI:
        return self._client

    @staticmethod
    def model_profile(model_name: str) -> ModelProfile | None:
        provider_to_profile = {
            'deepseek-ai': deepseek_model_profile,
            'google': google_model_profile,
            'qwen': qwen_model_profile,
            'meta-llama': meta_model_profile,
            'mistralai': mistral_model_profile,
        }

        profile = None

        model_name = model_name.lower()
        provider, model_name = model_name.split('/', 1)
        if provider in provider_to_profile:
            profile = provider_to_profile[provider](model_name)

        # As the Together API is OpenAI-compatible, let's assume we also need OpenAIJsonSchemaTransformer,
        # unless json_schema_transformer is set explicitly
        return OpenAIModelProfile(json_schema_transformer=OpenAIJsonSchemaTransformer).update(profile)

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, *, api_key: str) -> None: ...

    @overload
    def __init__(self, *, api_key: str, http_client: httpx.AsyncClient) -> None: ...

    @overload
    def __init__(self, *, openai_client: AsyncOpenAI | None = None) -> None: ...

    def __init__(
        self,
        *,
        api_key: str | None = None,
        openai_client: AsyncOpenAI | None = None,
        http_client: httpx.AsyncClient | None = None,
    ) -> None:
        api_key = api_key or os.getenv('TOGETHER_API_KEY')
        if not api_key and openai_client is None:
            raise UserError(
                'Set the `TOGETHER_API_KEY` environment variable or pass it via `TogetherProvider(api_key=...)`'
                'to use the Together AI provider.'
            )

        if openai_client is not None:
            self._client = openai_client
        elif http_client is not None:
            self._client = AsyncOpenAI(base_url=self.base_url, api_key=api_key, http_client=http_client)
        else:
            http_client = cached_async_http_client(provider='together')
            self._client = AsyncOpenAI(base_url=self.base_url, api_key=api_key, http_client=http_client)

```

---|---
Bases: `Provider[](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.Provider "pydantic_ai.providers.Provider")[AsyncOpenAI]`
Provider for Heroku API.
Source code in `pydantic_ai_slim/pydantic_ai/providers/heroku.py`
```
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
```
| ```
class HerokuProvider(Provider[AsyncOpenAI]):
    """Provider for Heroku API."""

    @property
    def name(self) -> str:
        return 'heroku'

    @property
    def base_url(self) -> str:
        return str(self.client.base_url)

    @property
    def client(self) -> AsyncOpenAI:
        return self._client

    @staticmethod
    def model_profile(model_name: str) -> ModelProfile | None:
        # As the Heroku API is OpenAI-compatible, let's assume we also need OpenAIJsonSchemaTransformer.
        return OpenAIModelProfile(json_schema_transformer=OpenAIJsonSchemaTransformer)

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, *, api_key: str) -> None: ...

    @overload
    def __init__(self, *, api_key: str, http_client: httpx.AsyncClient) -> None: ...

    @overload
    def __init__(self, *, openai_client: AsyncOpenAI | None = None) -> None: ...

    def __init__(
        self,
        *,
        base_url: str | None = None,
        api_key: str | None = None,
        openai_client: AsyncOpenAI | None = None,
        http_client: httpx.AsyncClient | None = None,
    ) -> None:
        if openai_client is not None:
            assert http_client is None, 'Cannot provide both `openai_client` and `http_client`'
            assert api_key is None, 'Cannot provide both `openai_client` and `api_key`'
            self._client = openai_client
        else:
            api_key = api_key or os.getenv('HEROKU_INFERENCE_KEY')
            if not api_key:
                raise UserError(
                    'Set the `HEROKU_INFERENCE_KEY` environment variable or pass it via `HerokuProvider(api_key=...)`'
                    'to use the Heroku provider.'
                )

            base_url = base_url or os.getenv('HEROKU_INFERENCE_URL', 'https://us.inference.heroku.com')
            base_url = base_url.rstrip('/') + '/v1'

            if http_client is not None:
                self._client = AsyncOpenAI(api_key=api_key, http_client=http_client, base_url=base_url)
            else:
                http_client = cached_async_http_client(provider='heroku')
                self._client = AsyncOpenAI(api_key=api_key, http_client=http_client, base_url=base_url)

```

---|---
Bases: `Provider[](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.Provider "pydantic_ai.providers.Provider")[AsyncOpenAI]`
Provider for GitHub Models API.
GitHub Models provides access to various AI models through an OpenAI-compatible API. See
Source code in `pydantic_ai_slim/pydantic_ai/providers/github.py`
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
```
| ```
class GitHubProvider(Provider[AsyncOpenAI]):
    """Provider for GitHub Models API.

    GitHub Models provides access to various AI models through an OpenAI-compatible API.
    See <https://docs.github.com/en/github-models> for more information.
    """

    @property
    def name(self) -> str:
        return 'github'

    @property
    def base_url(self) -> str:
        return 'https://models.github.ai/inference'

    @property
    def client(self) -> AsyncOpenAI:
        return self._client

    @staticmethod
    def model_profile(model_name: str) -> ModelProfile | None:
        provider_to_profile = {
            'xai': grok_model_profile,
            'meta': meta_model_profile,
            'microsoft': openai_model_profile,
            'mistral-ai': mistral_model_profile,
            'cohere': cohere_model_profile,
            'deepseek': deepseek_model_profile,
        }

        profile = None

        # If the model name does not contain a provider prefix, we assume it's an OpenAI model
        if '/' not in model_name:
            return openai_model_profile(model_name)

        provider, model_name = model_name.lower().split('/', 1)
        if provider in provider_to_profile:
            model_name, *_ = model_name.split(':', 1)  # drop tags
            profile = provider_to_profile[provider](model_name)

        # As GitHubProvider is always used with OpenAIChatModel, which used to unconditionally use OpenAIJsonSchemaTransformer,
        # we need to maintain that behavior unless json_schema_transformer is set explicitly
        return OpenAIModelProfile(json_schema_transformer=OpenAIJsonSchemaTransformer).update(profile)

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, *, api_key: str) -> None: ...

    @overload
    def __init__(self, *, api_key: str, http_client: httpx.AsyncClient) -> None: ...

    @overload
    def __init__(self, *, openai_client: AsyncOpenAI | None = None) -> None: ...

    def __init__(
        self,
        *,
        api_key: str | None = None,
        openai_client: AsyncOpenAI | None = None,
        http_client: httpx.AsyncClient | None = None,
    ) -> None:
        """Create a new GitHub Models provider.

        Args:
            api_key: The GitHub token to use for authentication. If not provided, the `GITHUB_API_KEY`
                environment variable will be used if available.
            openai_client: An existing `AsyncOpenAI` client to use. If provided, `api_key` and `http_client` must be `None`.
            http_client: An existing `httpx.AsyncClient` to use for making HTTP requests.
        """
        api_key = api_key or os.getenv('GITHUB_API_KEY')
        if not api_key and openai_client is None:
            raise UserError(
                'Set the `GITHUB_API_KEY` environment variable or pass it via `GitHubProvider(api_key=...)`'
                ' to use the GitHub Models provider.'
            )

        if openai_client is not None:
            self._client = openai_client
        elif http_client is not None:
            self._client = AsyncOpenAI(base_url=self.base_url, api_key=api_key, http_client=http_client)
        else:
            http_client = cached_async_http_client(provider='github')
            self._client = AsyncOpenAI(base_url=self.base_url, api_key=api_key, http_client=http_client)

```

---|---
###  __init__
```
__init__() -> None

```

```
__init__(*, api_key: ) -> None

```

```
__init__(*, api_key: , http_client: AsyncClient) -> None

```

```
__init__(
    *, openai_client: AsyncOpenAI | None = None
) -> None

```

```
__init__(
    *,
    api_key:  | None = None,
    openai_client: AsyncOpenAI | None = None,
    http_client: AsyncClient | None = None
) -> None

```

Create a new GitHub Models provider.
Parameters:
Name | Type | Description | Default
---|---|---|---
`api_key` |  |  The GitHub token to use for authentication. If not provided, the `GITHUB_API_KEY` environment variable will be used if available. |  `None`
`openai_client` |  `AsyncOpenAI | None` |  An existing `AsyncOpenAI` client to use. If provided, `api_key` and `http_client` must be `None`. |  `None`
`http_client` |  `AsyncClient | None` |  An existing `httpx.AsyncClient` to use for making HTTP requests. |  `None`
Source code in `pydantic_ai_slim/pydantic_ai/providers/github.py`
```
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
```
| ```
def __init__(
    self,
    *,
    api_key: str | None = None,
    openai_client: AsyncOpenAI | None = None,
    http_client: httpx.AsyncClient | None = None,
) -> None:
    """Create a new GitHub Models provider.

    Args:
        api_key: The GitHub token to use for authentication. If not provided, the `GITHUB_API_KEY`
            environment variable will be used if available.
        openai_client: An existing `AsyncOpenAI` client to use. If provided, `api_key` and `http_client` must be `None`.
        http_client: An existing `httpx.AsyncClient` to use for making HTTP requests.
    """
    api_key = api_key or os.getenv('GITHUB_API_KEY')
    if not api_key and openai_client is None:
        raise UserError(
            'Set the `GITHUB_API_KEY` environment variable or pass it via `GitHubProvider(api_key=...)`'
            ' to use the GitHub Models provider.'
        )

    if openai_client is not None:
        self._client = openai_client
    elif http_client is not None:
        self._client = AsyncOpenAI(base_url=self.base_url, api_key=api_key, http_client=http_client)
    else:
        http_client = cached_async_http_client(provider='github')
        self._client = AsyncOpenAI(base_url=self.base_url, api_key=api_key, http_client=http_client)

```

---|---
Bases: `Provider[](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.Provider "pydantic_ai.providers.Provider")[AsyncOpenAI]`
Provider for OpenRouter API.
Source code in `pydantic_ai_slim/pydantic_ai/providers/openrouter.py`
```
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
```
| ```
class OpenRouterProvider(Provider[AsyncOpenAI]):
    """Provider for OpenRouter API."""

    @property
    def name(self) -> str:
        return 'openrouter'

    @property
    def base_url(self) -> str:
        return 'https://openrouter.ai/api/v1'

    @property
    def client(self) -> AsyncOpenAI:
        return self._client

    @staticmethod
    def model_profile(model_name: str) -> ModelProfile | None:
        provider_to_profile = {
            'google': _openrouter_google_model_profile,
            'openai': openai_model_profile,
            'anthropic': anthropic_model_profile,
            'mistralai': mistral_model_profile,
            'qwen': qwen_model_profile,
            'x-ai': grok_model_profile,
            'cohere': cohere_model_profile,
            'amazon': amazon_model_profile,
            'deepseek': deepseek_model_profile,
            'meta-llama': meta_model_profile,
            'moonshotai': moonshotai_model_profile,
        }

        profile = None

        provider, model_name = model_name.split('/', 1)
        if provider in provider_to_profile:
            model_name, *_ = model_name.split(':', 1)  # drop tags
            profile = provider_to_profile[provider](model_name)

        # As OpenRouterProvider is always used with OpenAIChatModel, which used to unconditionally use OpenAIJsonSchemaTransformer,
        # we need to maintain that behavior unless json_schema_transformer is set explicitly
        return OpenAIModelProfile(
            json_schema_transformer=OpenAIJsonSchemaTransformer,
            openai_chat_send_back_thinking_parts='field',
            openai_chat_thinking_field='reasoning',
            openai_chat_supports_file_urls=True,
            openai_chat_supports_web_search=True,
        ).update(profile)

    @overload
    def __init__(self, *, openai_client: AsyncOpenAI) -> None: ...

    @overload
    def __init__(
        self,
        *,
        api_key: str | None = None,
        app_url: str | None = None,
        app_title: str | None = None,
        openai_client: None = None,
        http_client: httpx.AsyncClient | None = None,
    ) -> None: ...

    def __init__(
        self,
        *,
        api_key: str | None = None,
        app_url: str | None = None,
        app_title: str | None = None,
        openai_client: AsyncOpenAI | None = None,
        http_client: httpx.AsyncClient | None = None,
    ) -> None:
        """Configure the provider with either an API key or prebuilt client.

        Args:
            api_key: OpenRouter API key. Falls back to ``OPENROUTER_API_KEY``
                when omitted and required unless ``openai_client`` is provided.
            app_url: Optional url for app attribution. Falls back to
                ``OPENROUTER_APP_URL`` when omitted.
            app_title: Optional title for app attribution. Falls back to
                ``OPENROUTER_APP_TITLE`` when omitted.
            openai_client: Existing ``AsyncOpenAI`` client to reuse instead of
                creating one internally.
            http_client: Custom ``httpx.AsyncClient`` to pass into the
                ``AsyncOpenAI`` constructor when building a client.

        Raises:
            UserError: If no API key is available and no ``openai_client`` is
                provided.
        """
        api_key = api_key or os.getenv('OPENROUTER_API_KEY')
        if not api_key and openai_client is None:
            raise UserError(
                'Set the `OPENROUTER_API_KEY` environment variable or pass it via `OpenRouterProvider(api_key=...)`'
                'to use the OpenRouter provider.'
            )

        attribution_headers: dict[str, str] = {}
        if http_referer := app_url or os.getenv('OPENROUTER_APP_URL'):
            attribution_headers['HTTP-Referer'] = http_referer
        if x_title := app_title or os.getenv('OPENROUTER_APP_TITLE'):
            attribution_headers['X-Title'] = x_title

        if openai_client is not None:
            self._client = openai_client
        elif http_client is not None:
            self._client = AsyncOpenAI(
                base_url=self.base_url, api_key=api_key, http_client=http_client, default_headers=attribution_headers
            )
        else:
            http_client = cached_async_http_client(provider='openrouter')
            self._client = AsyncOpenAI(
                base_url=self.base_url, api_key=api_key, http_client=http_client, default_headers=attribution_headers
            )

```

---|---
###  __init__
```
__init__(*, openai_client: AsyncOpenAI) -> None

```

```
__init__(
    *,
    api_key:  | None = None,
    app_url:  | None = None,
    app_title:  | None = None,
    openai_client: None = None,
    http_client: AsyncClient | None = None
) -> None

```

```
__init__(
    *,
    api_key:  | None = None,
    app_url:  | None = None,
    app_title:  | None = None,
    openai_client: AsyncOpenAI | None = None,
    http_client: AsyncClient | None = None
) -> None

```

Configure the provider with either an API key or prebuilt client.
Parameters:
Name | Type | Description | Default
---|---|---|---
`api_key` |  |  OpenRouter API key. Falls back to `OPENROUTER_API_KEY` when omitted and required unless `openai_client` is provided. |  `None`
`app_url` |  |  Optional url for app attribution. Falls back to `OPENROUTER_APP_URL` when omitted. |  `None`
`app_title` |  |  Optional title for app attribution. Falls back to `OPENROUTER_APP_TITLE` when omitted. |  `None`
`openai_client` |  `AsyncOpenAI | None` |  Existing `AsyncOpenAI` client to reuse instead of creating one internally. |  `None`
`http_client` |  `AsyncClient | None` |  Custom `httpx.AsyncClient` to pass into the `AsyncOpenAI` constructor when building a client. |  `None`
Raises:
Type | Description
---|---
`UserError[](https://ai.pydantic.dev/api/exceptions/#pydantic_ai.exceptions.UserError "UserError \(pydantic_ai.exceptions.UserError\)")` |  If no API key is available and no `openai_client` is provided.
Source code in `pydantic_ai_slim/pydantic_ai/providers/openrouter.py`
```
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
```
| ```
def __init__(
    self,
    *,
    api_key: str | None = None,
    app_url: str | None = None,
    app_title: str | None = None,
    openai_client: AsyncOpenAI | None = None,
    http_client: httpx.AsyncClient | None = None,
) -> None:
    """Configure the provider with either an API key or prebuilt client.

    Args:
        api_key: OpenRouter API key. Falls back to ``OPENROUTER_API_KEY``
            when omitted and required unless ``openai_client`` is provided.
        app_url: Optional url for app attribution. Falls back to
            ``OPENROUTER_APP_URL`` when omitted.
        app_title: Optional title for app attribution. Falls back to
            ``OPENROUTER_APP_TITLE`` when omitted.
        openai_client: Existing ``AsyncOpenAI`` client to reuse instead of
            creating one internally.
        http_client: Custom ``httpx.AsyncClient`` to pass into the
            ``AsyncOpenAI`` constructor when building a client.

    Raises:
        UserError: If no API key is available and no ``openai_client`` is
            provided.
    """
    api_key = api_key or os.getenv('OPENROUTER_API_KEY')
    if not api_key and openai_client is None:
        raise UserError(
            'Set the `OPENROUTER_API_KEY` environment variable or pass it via `OpenRouterProvider(api_key=...)`'
            'to use the OpenRouter provider.'
        )

    attribution_headers: dict[str, str] = {}
    if http_referer := app_url or os.getenv('OPENROUTER_APP_URL'):
        attribution_headers['HTTP-Referer'] = http_referer
    if x_title := app_title or os.getenv('OPENROUTER_APP_TITLE'):
        attribution_headers['X-Title'] = x_title

    if openai_client is not None:
        self._client = openai_client
    elif http_client is not None:
        self._client = AsyncOpenAI(
            base_url=self.base_url, api_key=api_key, http_client=http_client, default_headers=attribution_headers
        )
    else:
        http_client = cached_async_http_client(provider='openrouter')
        self._client = AsyncOpenAI(
            base_url=self.base_url, api_key=api_key, http_client=http_client, default_headers=attribution_headers
