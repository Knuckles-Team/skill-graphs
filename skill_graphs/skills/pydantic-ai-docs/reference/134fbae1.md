        # we maintain that behavior
        return OpenAIModelProfile(json_schema_transformer=OpenAIJsonSchemaTransformer).update(profile)

    @overload
    def __init__(
        self,
        *,
        api_key: str | None = None,
        api_base: str | None = None,
    ) -> None: ...

    @overload
    def __init__(
        self,
        *,
        api_key: str | None = None,
        api_base: str | None = None,
        http_client: AsyncHTTPClient,
    ) -> None: ...

    @overload
    def __init__(self, *, openai_client: AsyncOpenAI) -> None: ...

    def __init__(
        self,
        *,
        api_key: str | None = None,
        api_base: str | None = None,
        openai_client: AsyncOpenAI | None = None,
        http_client: AsyncHTTPClient | None = None,
    ) -> None:
        """Initialize a LiteLLM provider.

        Args:
            api_key: API key for the model provider. If None, LiteLLM will try to get it from environment variables.
            api_base: Base URL for the model provider. Use this for custom endpoints or self-hosted models.
            openai_client: Pre-configured OpenAI client. If provided, other parameters are ignored.
            http_client: Custom HTTP client to use.
        """
        if openai_client is not None:
            self._client = openai_client
            return

        # Create OpenAI client that will be used with LiteLLM's completion function
        # The actual API calls will be intercepted and routed through LiteLLM
        if http_client is not None:
            self._client = AsyncOpenAI(
                base_url=api_base, api_key=api_key or 'litellm-placeholder', http_client=http_client
            )
        else:
            http_client = cached_async_http_client(provider='litellm')
            self._client = AsyncOpenAI(
                base_url=api_base, api_key=api_key or 'litellm-placeholder', http_client=http_client
            )

```

---|---
###  __init__
```
__init__(
    *,
    api_key:  | None = None,
    api_base:  | None = None
) -> None

```

```
__init__(
    *,
    api_key:  | None = None,
    api_base:  | None = None,
    http_client: AsyncClient
) -> None

```

```
__init__(*, openai_client: AsyncOpenAI) -> None

```

```
__init__(
    *,
    api_key:  | None = None,
    api_base:  | None = None,
    openai_client: AsyncOpenAI | None = None,
    http_client: AsyncClient | None = None
) -> None

```

Initialize a LiteLLM provider.
Parameters:
Name | Type | Description | Default
---|---|---|---
`api_key` |  |  API key for the model provider. If None, LiteLLM will try to get it from environment variables. |  `None`
`api_base` |  |  Base URL for the model provider. Use this for custom endpoints or self-hosted models. |  `None`
`openai_client` |  `AsyncOpenAI | None` |  Pre-configured OpenAI client. If provided, other parameters are ignored. |  `None`
`http_client` |  `AsyncClient | None` |  Custom HTTP client to use. |  `None`
Source code in `pydantic_ai_slim/pydantic_ai/providers/litellm.py`
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
135
```
| ```
def __init__(
    self,
    *,
    api_key: str | None = None,
    api_base: str | None = None,
    openai_client: AsyncOpenAI | None = None,
    http_client: AsyncHTTPClient | None = None,
) -> None:
    """Initialize a LiteLLM provider.

    Args:
        api_key: API key for the model provider. If None, LiteLLM will try to get it from environment variables.
        api_base: Base URL for the model provider. Use this for custom endpoints or self-hosted models.
        openai_client: Pre-configured OpenAI client. If provided, other parameters are ignored.
        http_client: Custom HTTP client to use.
    """
    if openai_client is not None:
        self._client = openai_client
        return

    # Create OpenAI client that will be used with LiteLLM's completion function
    # The actual API calls will be intercepted and routed through LiteLLM
    if http_client is not None:
        self._client = AsyncOpenAI(
            base_url=api_base, api_key=api_key or 'litellm-placeholder', http_client=http_client
        )
    else:
        http_client = cached_async_http_client(provider='litellm')
        self._client = AsyncOpenAI(
            base_url=api_base, api_key=api_key or 'litellm-placeholder', http_client=http_client
        )

```

---|---
Bases: `Provider[](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.Provider "pydantic_ai.providers.Provider")[AsyncOpenAI]`
Provider for Nebius AI Studio API.
Source code in `pydantic_ai_slim/pydantic_ai/providers/nebius.py`
```
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
```
| ```
class NebiusProvider(Provider[AsyncOpenAI]):
    """Provider for Nebius AI Studio API."""

    @property
    def name(self) -> str:
        return 'nebius'

    @property
    def base_url(self) -> str:
        return 'https://api.studio.nebius.com/v1'

    @property
    def client(self) -> AsyncOpenAI:
        return self._client

    @staticmethod
    def model_profile(model_name: str) -> ModelProfile | None:
        provider_to_profile = {
            'meta-llama': meta_model_profile,
            'deepseek-ai': deepseek_model_profile,
            'qwen': qwen_model_profile,
            'google': google_model_profile,
            'openai': harmony_model_profile,  # used for gpt-oss models on Nebius
            'mistralai': mistral_model_profile,
            'moonshotai': moonshotai_model_profile,
        }

        profile = None

        model_name = model_name.lower()
        if '/' not in model_name:
            return OpenAIModelProfile(json_schema_transformer=OpenAIJsonSchemaTransformer)

        provider, model_name = model_name.split('/', 1)
        if provider in provider_to_profile:
            profile = provider_to_profile[provider](model_name)

        # As NebiusProvider is always used with OpenAIChatModel, which used to unconditionally use OpenAIJsonSchemaTransformer,
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
        api_key = api_key or os.getenv('NEBIUS_API_KEY')
        if not api_key and openai_client is None:
            raise UserError(
                'Set the `NEBIUS_API_KEY` environment variable or pass it via '
                '`NebiusProvider(api_key=...)` to use the Nebius AI Studio provider.'
            )

        if openai_client is not None:
            self._client = openai_client
        elif http_client is not None:
            self._client = AsyncOpenAI(base_url=self.base_url, api_key=api_key, http_client=http_client)
        else:
            http_client = cached_async_http_client(provider='nebius')
            self._client = AsyncOpenAI(base_url=self.base_url, api_key=api_key, http_client=http_client)

```

---|---
Bases: `Provider[](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.Provider "pydantic_ai.providers.Provider")[AsyncOpenAI]`
Provider for OVHcloud AI Endpoints.
Source code in `pydantic_ai_slim/pydantic_ai/providers/ovhcloud.py`
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
```
| ```
class OVHcloudProvider(Provider[AsyncOpenAI]):
    """Provider for OVHcloud AI Endpoints."""

    @property
    def name(self) -> str:
        return 'ovhcloud'

    @property
    def base_url(self) -> str:
        return 'https://oai.endpoints.kepler.ai.cloud.ovh.net/v1'

    @property
    def client(self) -> AsyncOpenAI:
        return self._client

    @staticmethod
    def model_profile(model_name: str) -> ModelProfile | None:
        model_name = model_name.lower()

        prefix_to_profile = {
            'llama': meta_model_profile,
            'meta-': meta_model_profile,
            'deepseek': deepseek_model_profile,
            'mistral': mistral_model_profile,
            'gpt': harmony_model_profile,
            'qwen': qwen_model_profile,
        }

        profile = None
        for prefix, profile_func in prefix_to_profile.items():
            if model_name.startswith(prefix):
                profile = profile_func(model_name)

        # As the OVHcloud AI Endpoints API is OpenAI-compatible, let's assume we also need OpenAIJsonSchemaTransformer.
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
        api_key = api_key or os.getenv('OVHCLOUD_API_KEY')
        if not api_key and openai_client is None:
            raise UserError(
                'Set the `OVHCLOUD_API_KEY` environment variable or pass it via '
                '`OVHcloudProvider(api_key=...)` to use OVHcloud AI Endpoints provider.'
            )

        if openai_client is not None:
            self._client = openai_client
        elif http_client is not None:
            self._client = AsyncOpenAI(base_url=self.base_url, api_key=api_key, http_client=http_client)
        else:
            http_client = cached_async_http_client(provider='ovhcloud')
            self._client = AsyncOpenAI(base_url=self.base_url, api_key=api_key, http_client=http_client)

```

---|---
Bases: `Provider[](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.Provider "pydantic_ai.providers.Provider")[AsyncOpenAI]`
Provider for Alibaba Cloud Model Studio (DashScope) OpenAI-compatible API.
Source code in `pydantic_ai_slim/pydantic_ai/providers/alibaba.py`
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
```
| ```
class AlibabaProvider(Provider[AsyncOpenAI]):
    """Provider for Alibaba Cloud Model Studio (DashScope) OpenAI-compatible API."""

    @property
    def name(self) -> str:
        return 'alibaba'

    @property
    def base_url(self) -> str:
        return self._base_url

    @property
    def client(self) -> AsyncOpenAI:
        return self._client

    @staticmethod
    def model_profile(model_name: str) -> ModelProfile | None:
        base_profile = qwen_model_profile(model_name)

        # Wrap/merge into OpenAIModelProfile
        openai_profile = OpenAIModelProfile(json_schema_transformer=OpenAIJsonSchemaTransformer).update(base_profile)

        # For Qwen Omni models, force URI audio input encoding
        if 'omni' in model_name.lower():
            openai_profile = OpenAIModelProfile(openai_chat_audio_input_encoding='uri').update(openai_profile)

        return openai_profile

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, *, api_key: str, base_url: str | None = None) -> None: ...

    @overload
    def __init__(self, *, api_key: str, base_url: str | None = None, http_client: httpx.AsyncClient) -> None: ...

    @overload
    def __init__(self, *, openai_client: AsyncOpenAI | None = None) -> None: ...

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | None = None,
        openai_client: AsyncOpenAI | None = None,
        http_client: httpx.AsyncClient | None = None,
    ) -> None:
        if openai_client is not None:
            self._client = openai_client
            self._base_url = str(openai_client.base_url)
        else:
            # NOTE: We support DASHSCOPE_API_KEY for compatibility with Alibaba's official docs.
            api_key = api_key or os.getenv('ALIBABA_API_KEY') or os.getenv('DASHSCOPE_API_KEY')
            if not api_key:
                raise UserError(
                    'Set the `ALIBABA_API_KEY` environment variable or pass it via '
                    '`AlibabaProvider(api_key=...)` to use the Alibaba provider.'
                )

            self._base_url = base_url or 'https://dashscope-intl.aliyuncs.com/compatible-mode/v1'

            if http_client is None:
                http_client = cached_async_http_client(provider='alibaba')

            self._client = AsyncOpenAI(base_url=self._base_url, api_key=api_key, http_client=http_client)

```

---|---
Bases: `Provider[](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.Provider "pydantic_ai.providers.Provider")[AsyncOpenAI]`
Provider for SambaNova AI models.
SambaNova uses an OpenAI-compatible API.
Source code in `pydantic_ai_slim/pydantic_ai/providers/sambanova.py`
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
class SambaNovaProvider(Provider[AsyncOpenAI]):
    """Provider for SambaNova AI models.

    SambaNova uses an OpenAI-compatible API.
    """

    @property
    def name(self) -> str:
        """Return the provider name."""
        return 'sambanova'

    @property
    def base_url(self) -> str:
        """Return the base URL."""
        return self._base_url

    @property
    def client(self) -> AsyncOpenAI:
        """Return the AsyncOpenAI client."""
        return self._client

    @staticmethod
    def model_profile(model_name: str) -> ModelProfile | None:
        """Get model profile for SambaNova models.

        SambaNova serves models from multiple families including Meta Llama,
        DeepSeek, Qwen, and Mistral. Model profiles are matched based on
        model name prefixes.
        """
        prefix_to_profile = {
            'deepseek-': deepseek_model_profile,
            'meta-llama-': meta_model_profile,
            'llama-': meta_model_profile,
            'qwen': qwen_model_profile,
            'mistral': mistral_model_profile,
        }

        profile = None
        model_name_lower = model_name.lower()

        for prefix, profile_func in prefix_to_profile.items():
            if model_name_lower.startswith(prefix):
                profile = profile_func(model_name)
                break

        # Wrap into OpenAIModelProfile since SambaNova is OpenAI-compatible
        return OpenAIModelProfile(json_schema_transformer=OpenAIJsonSchemaTransformer).update(profile)

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | None = None,
        openai_client: AsyncOpenAI | None = None,
        http_client: httpx.AsyncClient | None = None,
    ) -> None:
        """Initialize SambaNova provider.

        Args:
            api_key: SambaNova API key. If not provided, reads from SAMBANOVA_API_KEY env var.
            base_url: Custom API base URL. Defaults to https://api.sambanova.ai/v1
            openai_client: Optional pre-configured OpenAI client
            http_client: Optional custom httpx.AsyncClient for making HTTP requests

        Raises:
            UserError: If API key is not provided and SAMBANOVA_API_KEY env var is not set
        """
        if openai_client is not None:
            self._client = openai_client
            self._base_url = str(openai_client.base_url)
        else:
            # Get API key from parameter or environment
            api_key = api_key or os.getenv('SAMBANOVA_API_KEY')
            if not api_key:
                raise UserError(
                    'Set the `SAMBANOVA_API_KEY` environment variable or pass it via '
                    '`SambaNovaProvider(api_key=...)` to use the SambaNova provider.'
                )

            # Set base URL (default to SambaNova API endpoint)
            self._base_url = base_url or os.getenv('SAMBANOVA_BASE_URL', 'https://api.sambanova.ai/v1')

            # Create http client and AsyncOpenAI client
            http_client = http_client or cached_async_http_client(provider='sambanova')
            self._client = AsyncOpenAI(base_url=self._base_url, api_key=api_key, http_client=http_client)

```

---|---
###  name `property`
```
name:

```

Return the provider name.
###  base_url `property`
```
base_url:

```

Return the base URL.
###  client `property`
```
client: AsyncOpenAI

```

Return the AsyncOpenAI client.
###  model_profile `staticmethod`
```
model_profile(model_name: ) -> ModelProfile[](https://ai.pydantic.dev/api/profiles/#pydantic_ai.profiles.ModelProfile "pydantic_ai.ModelProfile") | None

```

Get model profile for SambaNova models.
SambaNova serves models from multiple families including Meta Llama, DeepSeek, Qwen, and Mistral. Model profiles are matched based on model name prefixes.
Source code in `pydantic_ai_slim/pydantic_ai/providers/sambanova.py`
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
```
| ```
@staticmethod
def model_profile(model_name: str) -> ModelProfile | None:
    """Get model profile for SambaNova models.

    SambaNova serves models from multiple families including Meta Llama,
    DeepSeek, Qwen, and Mistral. Model profiles are matched based on
    model name prefixes.
    """
    prefix_to_profile = {
        'deepseek-': deepseek_model_profile,
        'meta-llama-': meta_model_profile,
        'llama-': meta_model_profile,
        'qwen': qwen_model_profile,
        'mistral': mistral_model_profile,
    }

    profile = None
    model_name_lower = model_name.lower()

    for prefix, profile_func in prefix_to_profile.items():
        if model_name_lower.startswith(prefix):
            profile = profile_func(model_name)
            break

    # Wrap into OpenAIModelProfile since SambaNova is OpenAI-compatible
    return OpenAIModelProfile(json_schema_transformer=OpenAIJsonSchemaTransformer).update(profile)

```

---|---
###  __init__
```
__init__(
    *,
    api_key:  | None = None,
    base_url:  | None = None,
    openai_client: AsyncOpenAI | None = None,
    http_client: AsyncClient | None = None
) -> None

```

Initialize SambaNova provider.
Parameters:
Name | Type | Description | Default
---|---|---|---
`api_key` |  |  SambaNova API key. If not provided, reads from SAMBANOVA_API_KEY env var. |  `None`
`base_url` |  |  Custom API base URL. Defaults to https://api.sambanova.ai/v1 |  `None`
`openai_client` |  `AsyncOpenAI | None` |  Optional pre-configured OpenAI client |  `None`
`http_client` |  `AsyncClient | None` |  Optional custom httpx.AsyncClient for making HTTP requests |  `None`
Raises:
Type | Description
---|---
`UserError[](https://ai.pydantic.dev/api/exceptions/#pydantic_ai.exceptions.UserError "UserError \(pydantic_ai.exceptions.UserError\)")` |  If API key is not provided and SAMBANOVA_API_KEY env var is not set
Source code in `pydantic_ai_slim/pydantic_ai/providers/sambanova.py`
```
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
def __init__(
    self,
    *,
    api_key: str | None = None,
    base_url: str | None = None,
    openai_client: AsyncOpenAI | None = None,
    http_client: httpx.AsyncClient | None = None,
) -> None:
    """Initialize SambaNova provider.

    Args:
        api_key: SambaNova API key. If not provided, reads from SAMBANOVA_API_KEY env var.
        base_url: Custom API base URL. Defaults to https://api.sambanova.ai/v1
        openai_client: Optional pre-configured OpenAI client
        http_client: Optional custom httpx.AsyncClient for making HTTP requests

    Raises:
        UserError: If API key is not provided and SAMBANOVA_API_KEY env var is not set
    """
    if openai_client is not None:
        self._client = openai_client
        self._base_url = str(openai_client.base_url)
    else:
        # Get API key from parameter or environment
        api_key = api_key or os.getenv('SAMBANOVA_API_KEY')
        if not api_key:
            raise UserError(
                'Set the `SAMBANOVA_API_KEY` environment variable or pass it via '
                '`SambaNovaProvider(api_key=...)` to use the SambaNova provider.'
            )

        # Set base URL (default to SambaNova API endpoint)
        self._base_url = base_url or os.getenv('SAMBANOVA_BASE_URL', 'https://api.sambanova.ai/v1')

        # Create http client and AsyncOpenAI client
        http_client = http_client or cached_async_http_client(provider='sambanova')
        self._client = AsyncOpenAI(base_url=self._base_url, api_key=api_key, http_client=http_client)

```

---|---
© Pydantic Services Inc. 2024 to present
