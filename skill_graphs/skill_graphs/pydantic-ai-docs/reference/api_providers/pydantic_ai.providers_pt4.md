        api_key: The API key to use for authentication, if not provided, the `AZURE_OPENAI_API_KEY` environment variable
            will be used if available.
        openai_client: An existing
            [`AsyncAzureOpenAI`](https://github.com/openai/openai-python#microsoft-azure-openai)
            client to use. If provided, `base_url`, `api_key`, and `http_client` must be `None`.
        http_client: An existing `httpx.AsyncClient` to use for making HTTP requests.
    """
    if openai_client is not None:
        assert azure_endpoint is None, 'Cannot provide both `openai_client` and `azure_endpoint`'
        assert http_client is None, 'Cannot provide both `openai_client` and `http_client`'
        assert api_key is None, 'Cannot provide both `openai_client` and `api_key`'
        self._base_url = str(openai_client.base_url)
        self._client = openai_client
    else:
        azure_endpoint = azure_endpoint or os.getenv('AZURE_OPENAI_ENDPOINT')
        if not azure_endpoint:
            raise UserError(
                'Must provide one of the `azure_endpoint` argument or the `AZURE_OPENAI_ENDPOINT` environment variable'
            )

        if not api_key and 'AZURE_OPENAI_API_KEY' not in os.environ:  # pragma: no cover
            raise UserError(
                'Must provide one of the `api_key` argument or the `AZURE_OPENAI_API_KEY` environment variable'
            )

        if not api_version and 'OPENAI_API_VERSION' not in os.environ:  # pragma: no cover
            raise UserError(
                'Must provide one of the `api_version` argument or the `OPENAI_API_VERSION` environment variable'
            )

        http_client = http_client or cached_async_http_client(provider='azure')
        self._client = AsyncAzureOpenAI(
            azure_endpoint=azure_endpoint,
            api_key=api_key,
            api_version=api_version,
            http_client=http_client,
        )
        self._base_url = str(self._client.base_url)

```

---|---
###  CohereProvider
Bases: `Provider[](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.Provider "pydantic_ai.providers.Provider")[AsyncClientV2]`
Provider for Cohere API.
Source code in `pydantic_ai_slim/pydantic_ai/providers/cohere.py`
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
```
| ```
class CohereProvider(Provider[AsyncClientV2]):
    """Provider for Cohere API."""

    @property
    def name(self) -> str:
        return 'cohere'

    @property
    def base_url(self) -> str:
        client_wrapper = self.client._client_wrapper  # type: ignore
        return str(client_wrapper.get_base_url())

    @property
    def client(self) -> AsyncClientV2:
        return self._client

    @property
    def v1_client(self) -> AsyncClient | None:
        return self._v1_client

    @staticmethod
    def model_profile(model_name: str) -> ModelProfile | None:
        return cohere_model_profile(model_name)

    def __init__(
        self,
        *,
        api_key: str | None = None,
        cohere_client: AsyncClientV2 | None = None,
        http_client: httpx.AsyncClient | None = None,
    ) -> None:
        """Create a new Cohere provider.

        Args:
            api_key: The API key to use for authentication, if not provided, the `CO_API_KEY` environment variable
                will be used if available.
            cohere_client: An existing
                [AsyncClientV2](https://github.com/cohere-ai/cohere-python)
                client to use. If provided, `api_key` and `http_client` must be `None`.
            http_client: An existing `httpx.AsyncClient` to use for making HTTP requests.
        """
        if cohere_client is not None:
            assert http_client is None, 'Cannot provide both `cohere_client` and `http_client`'
            assert api_key is None, 'Cannot provide both `cohere_client` and `api_key`'
            self._client = cohere_client
            self._v1_client = None
        else:
            api_key = api_key or os.getenv('CO_API_KEY')
            if not api_key:
                raise UserError(
                    'Set the `CO_API_KEY` environment variable or pass it via `CohereProvider(api_key=...)`'
                    'to use the Cohere provider.'
                )

            base_url = os.getenv('CO_BASE_URL')
            if http_client is not None:
                self._client = AsyncClientV2(api_key=api_key, httpx_client=http_client, base_url=base_url)
                self._v1_client = AsyncClient(api_key=api_key, httpx_client=http_client, base_url=base_url)
            else:
                http_client = cached_async_http_client(provider='cohere')
                self._client = AsyncClientV2(api_key=api_key, httpx_client=http_client, base_url=base_url)
                self._v1_client = AsyncClient(api_key=api_key, httpx_client=http_client, base_url=base_url)

```

---|---
####  __init__
```
__init__(
    *,
    api_key:  | None = None,
    cohere_client: AsyncClientV2 | None = None,
    http_client: AsyncClient | None = None
) -> None

```

Create a new Cohere provider.
Parameters:
Name | Type | Description | Default
---|---|---|---
`api_key` |  |  The API key to use for authentication, if not provided, the `CO_API_KEY` environment variable will be used if available. |  `None`
`cohere_client` |  `AsyncClientV2 | None` |  An existing `api_key` and `http_client` must be `None`. |  `None`
`http_client` |  `AsyncClient | None` |  An existing `httpx.AsyncClient` to use for making HTTP requests. |  `None`
Source code in `pydantic_ai_slim/pydantic_ai/providers/cohere.py`
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
```
| ```
def __init__(
    self,
    *,
    api_key: str | None = None,
    cohere_client: AsyncClientV2 | None = None,
    http_client: httpx.AsyncClient | None = None,
) -> None:
    """Create a new Cohere provider.

    Args:
        api_key: The API key to use for authentication, if not provided, the `CO_API_KEY` environment variable
            will be used if available.
        cohere_client: An existing
            [AsyncClientV2](https://github.com/cohere-ai/cohere-python)
            client to use. If provided, `api_key` and `http_client` must be `None`.
        http_client: An existing `httpx.AsyncClient` to use for making HTTP requests.
    """
    if cohere_client is not None:
        assert http_client is None, 'Cannot provide both `cohere_client` and `http_client`'
        assert api_key is None, 'Cannot provide both `cohere_client` and `api_key`'
        self._client = cohere_client
        self._v1_client = None
    else:
        api_key = api_key or os.getenv('CO_API_KEY')
        if not api_key:
            raise UserError(
                'Set the `CO_API_KEY` environment variable or pass it via `CohereProvider(api_key=...)`'
                'to use the Cohere provider.'
            )

        base_url = os.getenv('CO_BASE_URL')
        if http_client is not None:
            self._client = AsyncClientV2(api_key=api_key, httpx_client=http_client, base_url=base_url)
            self._v1_client = AsyncClient(api_key=api_key, httpx_client=http_client, base_url=base_url)
        else:
            http_client = cached_async_http_client(provider='cohere')
            self._client = AsyncClientV2(api_key=api_key, httpx_client=http_client, base_url=base_url)
            self._v1_client = AsyncClient(api_key=api_key, httpx_client=http_client, base_url=base_url)

```

---|---
Bases: `Provider[](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.Provider "pydantic_ai.providers.Provider")[AsyncClient]`
Provider for VoyageAI API.
Source code in `pydantic_ai_slim/pydantic_ai/providers/voyageai.py`
```
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
```
| ```
class VoyageAIProvider(Provider[AsyncClient]):
    """Provider for VoyageAI API."""

    @property
    def name(self) -> str:
        return 'voyageai'

    @property
    def base_url(self) -> str:
        return self._client._params.get('base_url') or 'https://api.voyageai.com/v1'  # type: ignore

    @property
    def client(self) -> AsyncClient:
        return self._client

    @overload
    def __init__(self, *, voyageai_client: AsyncClient) -> None: ...

    @overload
    def __init__(self, *, api_key: str | None = None) -> None: ...

    def __init__(
        self,
        *,
        api_key: str | None = None,
        voyageai_client: AsyncClient | None = None,
    ) -> None:
        """Create a new VoyageAI provider.

        Args:
            api_key: The API key to use for authentication, if not provided, the `VOYAGE_API_KEY` environment variable
                will be used if available.
            voyageai_client: An existing
                [AsyncClient](https://github.com/voyage-ai/voyageai-python)
                client to use. If provided, `api_key` must be `None`.
        """
        if voyageai_client is not None:
            assert api_key is None, 'Cannot provide both `voyageai_client` and `api_key`'
            self._client = voyageai_client
        else:
            api_key = api_key or os.getenv('VOYAGE_API_KEY')
            if not api_key:
                raise UserError(
                    'Set the `VOYAGE_API_KEY` environment variable or pass it via `VoyageAIProvider(api_key=...)` '
                    'to use the VoyageAI provider.'
                )

            self._client = AsyncClient(api_key=api_key)

```

---|---
###  __init__
```
__init__(*, voyageai_client: AsyncClient) -> None

```

```
__init__(*, api_key:  | None = None) -> None

```

```
__init__(
    *,
    api_key:  | None = None,
    voyageai_client: AsyncClient | None = None
) -> None

```

Create a new VoyageAI provider.
Parameters:
Name | Type | Description | Default
---|---|---|---
`api_key` |  |  The API key to use for authentication, if not provided, the `VOYAGE_API_KEY` environment variable will be used if available. |  `None`
`voyageai_client` |  `AsyncClient | None` |  An existing `api_key` must be `None`. |  `None`
Source code in `pydantic_ai_slim/pydantic_ai/providers/voyageai.py`
```
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
```
| ```
def __init__(
    self,
    *,
    api_key: str | None = None,
    voyageai_client: AsyncClient | None = None,
) -> None:
    """Create a new VoyageAI provider.

    Args:
        api_key: The API key to use for authentication, if not provided, the `VOYAGE_API_KEY` environment variable
            will be used if available.
        voyageai_client: An existing
            [AsyncClient](https://github.com/voyage-ai/voyageai-python)
            client to use. If provided, `api_key` must be `None`.
    """
    if voyageai_client is not None:
        assert api_key is None, 'Cannot provide both `voyageai_client` and `api_key`'
        self._client = voyageai_client
    else:
        api_key = api_key or os.getenv('VOYAGE_API_KEY')
        if not api_key:
            raise UserError(
                'Set the `VOYAGE_API_KEY` environment variable or pass it via `VoyageAIProvider(api_key=...)` '
                'to use the VoyageAI provider.'
            )

        self._client = AsyncClient(api_key=api_key)

```

---|---
Bases: `Provider[](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.Provider "pydantic_ai.providers.Provider")[AsyncOpenAI]`
Provider for Cerebras API.
Source code in `pydantic_ai_slim/pydantic_ai/providers/cerebras.py`
```
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
```
| ```
class CerebrasProvider(Provider[AsyncOpenAI]):
    """Provider for Cerebras API."""

    @property
    def name(self) -> str:
        return 'cerebras'

    @property
    def base_url(self) -> str:
        return 'https://api.cerebras.ai/v1'

    @property
    def client(self) -> AsyncOpenAI:
        return self._client

    @staticmethod
    def model_profile(model_name: str) -> ModelProfile | None:
        prefix_to_profile = {
            'llama': meta_model_profile,
            'qwen': qwen_model_profile,
            'gpt-oss': harmony_model_profile,
            'zai': zai_model_profile,
        }

        profile = None
        model_name_lower = model_name.lower()
        for prefix, profile_func in prefix_to_profile.items():
            if model_name_lower.startswith(prefix):
                profile = profile_func(model_name_lower)
                break

        # According to https://inference-docs.cerebras.ai/resources/openai#currently-unsupported-openai-features,
        # Cerebras doesn't support some model settings.
        # openai_chat_supports_web_search=False is default, so not required here
        unsupported_model_settings = (
            'frequency_penalty',
            'logit_bias',
            'presence_penalty',
            'parallel_tool_calls',
            'service_tier',
        )
        return OpenAIModelProfile(
            json_schema_transformer=OpenAIJsonSchemaTransformer,
            openai_unsupported_model_settings=unsupported_model_settings,
        ).update(profile)

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, *, api_key: str) -> None: ...

    @overload
    def __init__(self, *, api_key: str, http_client: httpx.AsyncClient) -> None: ...

    @overload
    def __init__(self, *, http_client: httpx.AsyncClient) -> None: ...

    @overload
    def __init__(self, *, openai_client: AsyncOpenAI | None = None) -> None: ...

    def __init__(
        self,
        *,
        api_key: str | None = None,
        openai_client: AsyncOpenAI | None = None,
        http_client: httpx.AsyncClient | None = None,
    ) -> None:
        """Create a new Cerebras provider.

        Args:
            api_key: The API key to use for authentication, if not provided, the `CEREBRAS_API_KEY` environment variable
                will be used if available.
            openai_client: An existing `AsyncOpenAI` client to use. If provided, `api_key` and `http_client` must be `None`.
            http_client: An existing `httpx.AsyncClient` to use for making HTTP requests.
        """
        api_key = api_key or os.getenv('CEREBRAS_API_KEY')
        if not api_key and openai_client is None:
            raise UserError(
                'Set the `CEREBRAS_API_KEY` environment variable or pass it via `CerebrasProvider(api_key=...)` '
                'to use the Cerebras provider.'
            )

        default_headers = {'X-Cerebras-3rd-Party-Integration': 'pydantic-ai'}

        if openai_client is not None:
            self._client = openai_client
        elif http_client is not None:
            self._client = AsyncOpenAI(
                base_url=self.base_url, api_key=api_key, http_client=http_client, default_headers=default_headers
            )
        else:
            http_client = cached_async_http_client(provider='cerebras')
            self._client = AsyncOpenAI(
                base_url=self.base_url, api_key=api_key, http_client=http_client, default_headers=default_headers
            )

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
__init__(*, http_client: AsyncClient) -> None

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

Create a new Cerebras provider.
Parameters:
Name | Type | Description | Default
---|---|---|---
`api_key` |  |  The API key to use for authentication, if not provided, the `CEREBRAS_API_KEY` environment variable will be used if available. |  `None`
`openai_client` |  `AsyncOpenAI | None` |  An existing `AsyncOpenAI` client to use. If provided, `api_key` and `http_client` must be `None`. |  `None`
`http_client` |  `AsyncClient | None` |  An existing `httpx.AsyncClient` to use for making HTTP requests. |  `None`
Source code in `pydantic_ai_slim/pydantic_ai/providers/cerebras.py`
```
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
```
| ```
def __init__(
    self,
    *,
    api_key: str | None = None,
    openai_client: AsyncOpenAI | None = None,
    http_client: httpx.AsyncClient | None = None,
) -> None:
    """Create a new Cerebras provider.

    Args:
        api_key: The API key to use for authentication, if not provided, the `CEREBRAS_API_KEY` environment variable
            will be used if available.
        openai_client: An existing `AsyncOpenAI` client to use. If provided, `api_key` and `http_client` must be `None`.
        http_client: An existing `httpx.AsyncClient` to use for making HTTP requests.
    """
    api_key = api_key or os.getenv('CEREBRAS_API_KEY')
    if not api_key and openai_client is None:
        raise UserError(
            'Set the `CEREBRAS_API_KEY` environment variable or pass it via `CerebrasProvider(api_key=...)` '
            'to use the Cerebras provider.'
        )

    default_headers = {'X-Cerebras-3rd-Party-Integration': 'pydantic-ai'}

    if openai_client is not None:
        self._client = openai_client
    elif http_client is not None:
        self._client = AsyncOpenAI(
            base_url=self.base_url, api_key=api_key, http_client=http_client, default_headers=default_headers
        )
    else:
        http_client = cached_async_http_client(provider='cerebras')
        self._client = AsyncOpenAI(
            base_url=self.base_url, api_key=api_key, http_client=http_client, default_headers=default_headers
        )

```

---|---
Bases: `Provider[](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.Provider "pydantic_ai.providers.Provider")[Mistral]`
Provider for Mistral API.
Source code in `pydantic_ai_slim/pydantic_ai/providers/mistral.py`
```
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
```
| ```
class MistralProvider(Provider[Mistral]):
    """Provider for Mistral API."""

    @property
    def name(self) -> str:
        return 'mistral'

    @property
    def base_url(self) -> str:
        return self.client.sdk_configuration.get_server_details()[0]

    @property
    def client(self) -> Mistral:
        return self._client

    @staticmethod
    def model_profile(model_name: str) -> ModelProfile | None:
        return mistral_model_profile(model_name)

    @overload
    def __init__(self, *, mistral_client: Mistral | None = None) -> None: ...

    @overload
    def __init__(self, *, api_key: str | None = None, http_client: httpx.AsyncClient | None = None) -> None: ...

    def __init__(
        self,
        *,
        api_key: str | None = None,
        mistral_client: Mistral | None = None,
        base_url: str | None = None,
        http_client: httpx.AsyncClient | None = None,
    ) -> None:
        """Create a new Mistral provider.

        Args:
            api_key: The API key to use for authentication, if not provided, the `MISTRAL_API_KEY` environment variable
                will be used if available.
            mistral_client: An existing `Mistral` client to use, if provided, `api_key` and `http_client` must be `None`.
            base_url: The base url for the Mistral requests.
            http_client: An existing async client to use for making HTTP requests.
        """
        if mistral_client is not None:
            assert http_client is None, 'Cannot provide both `mistral_client` and `http_client`'
            assert api_key is None, 'Cannot provide both `mistral_client` and `api_key`'
            assert base_url is None, 'Cannot provide both `mistral_client` and `base_url`'
            self._client = mistral_client
        else:
            api_key = api_key or os.getenv('MISTRAL_API_KEY')

            if not api_key:
                raise UserError(
                    'Set the `MISTRAL_API_KEY` environment variable or pass it via `MistralProvider(api_key=...)`'
                    'to use the Mistral provider.'
                )
            elif http_client is not None:
                self._client = Mistral(api_key=api_key, async_client=http_client, server_url=base_url)
            else:
                http_client = cached_async_http_client(provider='mistral')
                self._client = Mistral(api_key=api_key, async_client=http_client, server_url=base_url)

```

---|---
###  __init__
```
__init__(*, mistral_client: Mistral | None = None) -> None

```

```
__init__(
    *,
    api_key:  | None = None,
    http_client: AsyncClient | None = None
) -> None

```

```
__init__(
    *,
    api_key:  | None = None,
    mistral_client: Mistral | None = None,
    base_url:  | None = None,
    http_client: AsyncClient | None = None
) -> None

```

Create a new Mistral provider.
Parameters:
Name | Type | Description | Default
---|---|---|---
`api_key` |  |  The API key to use for authentication, if not provided, the `MISTRAL_API_KEY` environment variable will be used if available. |  `None`
`mistral_client` |  `Mistral | None` |  An existing `Mistral` client to use, if provided, `api_key` and `http_client` must be `None`. |  `None`
`base_url` |  |  The base url for the Mistral requests. |  `None`
`http_client` |  `AsyncClient | None` |  An existing async client to use for making HTTP requests. |  `None`
Source code in `pydantic_ai_slim/pydantic_ai/providers/mistral.py`
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
```
| ```
def __init__(
    self,
    *,
    api_key: str | None = None,
    mistral_client: Mistral | None = None,
    base_url: str | None = None,
    http_client: httpx.AsyncClient | None = None,
) -> None:
    """Create a new Mistral provider.

    Args:
        api_key: The API key to use for authentication, if not provided, the `MISTRAL_API_KEY` environment variable
            will be used if available.
        mistral_client: An existing `Mistral` client to use, if provided, `api_key` and `http_client` must be `None`.
        base_url: The base url for the Mistral requests.
        http_client: An existing async client to use for making HTTP requests.
    """
    if mistral_client is not None:
        assert http_client is None, 'Cannot provide both `mistral_client` and `http_client`'
        assert api_key is None, 'Cannot provide both `mistral_client` and `api_key`'
        assert base_url is None, 'Cannot provide both `mistral_client` and `base_url`'
        self._client = mistral_client
    else:
        api_key = api_key or os.getenv('MISTRAL_API_KEY')

        if not api_key:
            raise UserError(
                'Set the `MISTRAL_API_KEY` environment variable or pass it via `MistralProvider(api_key=...)`'
                'to use the Mistral provider.'
            )
        elif http_client is not None:
            self._client = Mistral(api_key=api_key, async_client=http_client, server_url=base_url)
        else:
            http_client = cached_async_http_client(provider='mistral')
            self._client = Mistral(api_key=api_key, async_client=http_client, server_url=base_url)

```

---|---
Bases: `Provider[](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.Provider "pydantic_ai.providers.Provider")[AsyncOpenAI]`
Provider for Fireworks AI API.
Source code in `pydantic_ai_slim/pydantic_ai/providers/fireworks.py`
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
 98
 99
100
```
| ```
class FireworksProvider(Provider[AsyncOpenAI]):
    """Provider for Fireworks AI API."""

    @property
    def name(self) -> str:
        return 'fireworks'

    @property
    def base_url(self) -> str:
        return 'https://api.fireworks.ai/inference/v1'

    @property
    def client(self) -> AsyncOpenAI:
        return self._client

    @staticmethod
    def model_profile(model_name: str) -> ModelProfile | None:
        prefix_to_profile = {
            'llama': meta_model_profile,
            'qwen': qwen_model_profile,
            'deepseek': deepseek_model_profile,
            'mistral': mistral_model_profile,
            'gemma': google_model_profile,
        }

        prefix = 'accounts/fireworks/models/'

        profile = None
        if model_name.startswith(prefix):
            model_name = model_name[len(prefix) :]
            for provider, profile_func in prefix_to_profile.items():
                if model_name.startswith(provider):
                    profile = profile_func(model_name)
                    break

        # As the Fireworks API is OpenAI-compatible, let's assume we also need OpenAIJsonSchemaTransformer,
