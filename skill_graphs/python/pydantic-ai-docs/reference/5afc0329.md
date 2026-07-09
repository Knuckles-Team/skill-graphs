        )

```

---|---
Bases: `Provider[](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.Provider "pydantic_ai.providers.Provider")[AsyncOpenAI]`
Provider for Vercel AI Gateway API.
Source code in `pydantic_ai_slim/pydantic_ai/providers/vercel.py`
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
class VercelProvider(Provider[AsyncOpenAI]):
    """Provider for Vercel AI Gateway API."""

    @property
    def name(self) -> str:
        return 'vercel'

    @property
    def base_url(self) -> str:
        return 'https://ai-gateway.vercel.sh/v1'

    @property
    def client(self) -> AsyncOpenAI:
        return self._client

    @staticmethod
    def model_profile(model_name: str) -> ModelProfile | None:
        provider_to_profile = {
            'anthropic': anthropic_model_profile,
            'bedrock': amazon_model_profile,
            'cohere': cohere_model_profile,
            'deepseek': deepseek_model_profile,
            'mistral': mistral_model_profile,
            'openai': openai_model_profile,
            'vertex': google_model_profile,
            'xai': grok_model_profile,
        }

        profile = None

        if '/' not in model_name:
            return OpenAIModelProfile(json_schema_transformer=OpenAIJsonSchemaTransformer)

        provider, model_name = model_name.split('/', 1)
        if provider in provider_to_profile:
            profile = provider_to_profile[provider](model_name)

        # As VercelProvider is always used with OpenAIChatModel, which used to unconditionally use OpenAIJsonSchemaTransformer,
        # we need to maintain that behavior unless json_schema_transformer is set explicitly
        return OpenAIModelProfile(
            json_schema_transformer=OpenAIJsonSchemaTransformer,
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
        # Support Vercel AI Gateway's standard environment variables
        api_key = api_key or os.getenv('VERCEL_AI_GATEWAY_API_KEY') or os.getenv('VERCEL_OIDC_TOKEN')

        if not api_key and openai_client is None:
            raise UserError(
                'Set the `VERCEL_AI_GATEWAY_API_KEY` or `VERCEL_OIDC_TOKEN` environment variable '
                'or pass the API key via `VercelProvider(api_key=...)` to use the Vercel provider.'
            )

        default_headers = {'http-referer': 'https://ai.pydantic.dev/', 'x-title': 'pydantic-ai'}

        if openai_client is not None:
            self._client = openai_client
        elif http_client is not None:
            self._client = AsyncOpenAI(
                base_url=self.base_url, api_key=api_key, http_client=http_client, default_headers=default_headers
            )
        else:
            http_client = cached_async_http_client(provider='vercel')
            self._client = AsyncOpenAI(
                base_url=self.base_url, api_key=api_key, http_client=http_client, default_headers=default_headers
            )

```

---|---
Bases: `Provider[](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.Provider "pydantic_ai.providers.Provider")[AsyncInferenceClient]`
Provider for Hugging Face.
Source code in `pydantic_ai_slim/pydantic_ai/providers/huggingface.py`
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
```
| ```
class HuggingFaceProvider(Provider[AsyncInferenceClient]):
    """Provider for Hugging Face."""

    @property
    def name(self) -> str:
        return 'huggingface'

    @property
    def base_url(self) -> str:
        if self._client.model is not None:
            return self._client.model
        if self._client.provider is not None:
            return INFERENCE_PROXY_TEMPLATE.format(provider=self._client.provider)
        raise UserError(
            'Unable to determine base URL for HuggingFace provider. '
            'Please provide `base_url`, `provider_name`, or a pre-configured `hf_client`.'
        )

    @property
    def client(self) -> AsyncInferenceClient:
        return self._client

    @staticmethod
    def model_profile(model_name: str) -> ModelProfile | None:
        provider_to_profile = {
            'deepseek-ai': deepseek_model_profile,
            'google': google_model_profile,
            'qwen': qwen_model_profile,
            'meta-llama': meta_model_profile,
            'mistralai': mistral_model_profile,
            'moonshotai': moonshotai_model_profile,
        }

        if '/' not in model_name:
            return None

        model_name = model_name.lower()
        provider, model_name = model_name.split('/', 1)
        if provider in provider_to_profile:
            return provider_to_profile[provider](model_name)

        return None

    @overload
    def __init__(self, *, base_url: str, api_key: str | None = None) -> None: ...
    @overload
    def __init__(self, *, provider_name: str, api_key: str | None = None) -> None: ...
    @overload
    def __init__(self, *, hf_client: AsyncInferenceClient, api_key: str | None = None) -> None: ...
    @overload
    def __init__(self, *, hf_client: AsyncInferenceClient, base_url: str, api_key: str | None = None) -> None: ...
    @overload
    def __init__(self, *, hf_client: AsyncInferenceClient, provider_name: str, api_key: str | None = None) -> None: ...
    @overload
    def __init__(self, *, api_key: str | None = None) -> None: ...

    def __init__(
        self,
        base_url: str | None = None,
        api_key: str | None = None,
        hf_client: AsyncInferenceClient | None = None,
        http_client: AsyncClient | None = None,
        provider_name: str | None = None,
    ) -> None:
        """Create a new Hugging Face provider.

        Args:
            base_url: The base url for the Hugging Face requests.
            api_key: The API key to use for authentication, if not provided, the `HF_TOKEN` environment variable
                will be used if available.
            hf_client: An existing
                [`AsyncInferenceClient`](https://huggingface.co/docs/huggingface_hub/en/package_reference/inference_client#huggingface_hub.AsyncInferenceClient)
                client to use. If not provided, a new instance will be created.
            http_client: (currently ignored) An existing `httpx.AsyncClient` to use for making HTTP requests.
            provider_name: Name of the provider to use for inference. available providers can be found in the [HF Inference Providers documentation](https://huggingface.co/docs/inference-providers/index#partners).
                defaults to "auto", which will select the first available provider for the model, the first of the providers available for the model, sorted by the user's order in https://hf.co/settings/inference-providers.
                If `base_url` is passed, then `provider_name` is not used.
        """
        api_key = api_key or os.getenv('HF_TOKEN')

        if api_key is None:
            raise UserError(
                'Set the `HF_TOKEN` environment variable or pass it via `HuggingFaceProvider(api_key=...)`'
                'to use the HuggingFace provider.'
            )

        if http_client is not None:
            raise ValueError('`http_client` is ignored for HuggingFace provider, please use `hf_client` instead.')

        if base_url is not None and provider_name is not None:
            raise ValueError('Cannot provide both `base_url` and `provider_name`.')

        if hf_client is None:
            self._client = AsyncInferenceClient(api_key=api_key, provider=provider_name, base_url=base_url)  # type: ignore
        else:
            self._client = hf_client

```

---|---
###  __init__
```
__init__(
    *, base_url: , api_key:  | None = None
) -> None

```

```
__init__(
    *, provider_name: , api_key:  | None = None
) -> None

```

```
__init__(
    *,
    hf_client: AsyncInferenceClient,
    api_key:  | None = None
) -> None

```

```
__init__(
    *,
    hf_client: AsyncInferenceClient,
    base_url: ,
    api_key:  | None = None
) -> None

```

```
__init__(
    *,
    hf_client: AsyncInferenceClient,
    provider_name: ,
    api_key:  | None = None
) -> None

```

```
__init__(*, api_key:  | None = None) -> None

```

```
__init__(
    base_url:  | None = None,
    api_key:  | None = None,
    hf_client: AsyncInferenceClient | None = None,
    http_client: AsyncClient | None = None,
    provider_name:  | None = None,
) -> None

```

Create a new Hugging Face provider.
Parameters:
Name | Type | Description | Default
---|---|---|---
`base_url` |  |  The base url for the Hugging Face requests. |  `None`
`api_key` |  |  The API key to use for authentication, if not provided, the `HF_TOKEN` environment variable will be used if available. |  `None`
`hf_client` |  `AsyncInferenceClient | None` |  An existing  |  `None`
`http_client` |  `AsyncClient | None` |  (currently ignored) An existing `httpx.AsyncClient` to use for making HTTP requests. |  `None`
`provider_name` |  |  Name of the provider to use for inference. available providers can be found in the `base_url` is passed, then `provider_name` is not used. |  `None`
Source code in `pydantic_ai_slim/pydantic_ai/providers/huggingface.py`
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
```
| ```
def __init__(
    self,
    base_url: str | None = None,
    api_key: str | None = None,
    hf_client: AsyncInferenceClient | None = None,
    http_client: AsyncClient | None = None,
    provider_name: str | None = None,
) -> None:
    """Create a new Hugging Face provider.

    Args:
        base_url: The base url for the Hugging Face requests.
        api_key: The API key to use for authentication, if not provided, the `HF_TOKEN` environment variable
            will be used if available.
        hf_client: An existing
            [`AsyncInferenceClient`](https://huggingface.co/docs/huggingface_hub/en/package_reference/inference_client#huggingface_hub.AsyncInferenceClient)
            client to use. If not provided, a new instance will be created.
        http_client: (currently ignored) An existing `httpx.AsyncClient` to use for making HTTP requests.
        provider_name: Name of the provider to use for inference. available providers can be found in the [HF Inference Providers documentation](https://huggingface.co/docs/inference-providers/index#partners).
            defaults to "auto", which will select the first available provider for the model, the first of the providers available for the model, sorted by the user's order in https://hf.co/settings/inference-providers.
            If `base_url` is passed, then `provider_name` is not used.
    """
    api_key = api_key or os.getenv('HF_TOKEN')

    if api_key is None:
        raise UserError(
            'Set the `HF_TOKEN` environment variable or pass it via `HuggingFaceProvider(api_key=...)`'
            'to use the HuggingFace provider.'
        )

    if http_client is not None:
        raise ValueError('`http_client` is ignored for HuggingFace provider, please use `hf_client` instead.')

    if base_url is not None and provider_name is not None:
        raise ValueError('Cannot provide both `base_url` and `provider_name`.')

    if hf_client is None:
        self._client = AsyncInferenceClient(api_key=api_key, provider=provider_name, base_url=base_url)  # type: ignore
    else:
        self._client = hf_client

```

---|---
Bases: `Provider[](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.Provider "pydantic_ai.providers.Provider")[AsyncOpenAI]`
Provider for MoonshotAI platform (Kimi models).
Source code in `pydantic_ai_slim/pydantic_ai/providers/moonshotai.py`
```
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
class MoonshotAIProvider(Provider[AsyncOpenAI]):
    """Provider for MoonshotAI platform (Kimi models)."""

    @property
    def name(self) -> str:
        return 'moonshotai'

    @property
    def base_url(self) -> str:
        # OpenAI-compatible endpoint, see MoonshotAI docs
        return 'https://api.moonshot.ai/v1'

    @property
    def client(self) -> AsyncOpenAI:
        return self._client

    @staticmethod
    def model_profile(model_name: str) -> ModelProfile | None:
        profile = moonshotai_model_profile(model_name)

        # As the MoonshotAI API is OpenAI-compatible, let's assume we also need OpenAIJsonSchemaTransformer,
        # unless json_schema_transformer is set explicitly.
        # Also, MoonshotAI does not support strict tool definitions
        # https://platform.moonshot.ai/docs/guide/migrating-from-openai-to-kimi#about-tool_choice
        # "Please note that the current version of Kimi API does not support the tool_choice=required parameter."
        return OpenAIModelProfile(
            json_schema_transformer=OpenAIJsonSchemaTransformer,
            openai_supports_tool_choice_required=False,
            supports_json_object_output=True,
            openai_chat_thinking_field='reasoning_content',
            openai_chat_send_back_thinking_parts='field',
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
        api_key = api_key or os.getenv('MOONSHOTAI_API_KEY')
        if not api_key and openai_client is None:
            raise UserError(
                'Set the `MOONSHOTAI_API_KEY` environment variable or pass it via '
                '`MoonshotAIProvider(api_key=...)` to use the MoonshotAI provider.'
            )

        if openai_client is not None:
            self._client = openai_client
        elif http_client is not None:
            self._client = AsyncOpenAI(base_url=self.base_url, api_key=api_key, http_client=http_client)
        else:
            http_client = cached_async_http_client(provider='moonshotai')
            self._client = AsyncOpenAI(base_url=self.base_url, api_key=api_key, http_client=http_client)

```

---|---
Bases: `Provider[](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.Provider "pydantic_ai.providers.Provider")[AsyncOpenAI]`
Provider for local or remote Ollama API.
Source code in `pydantic_ai_slim/pydantic_ai/providers/ollama.py`
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
class OllamaProvider(Provider[AsyncOpenAI]):
    """Provider for local or remote Ollama API."""

    @property
    def name(self) -> str:
        return 'ollama'

    @property
    def base_url(self) -> str:
        return str(self.client.base_url)

    @property
    def client(self) -> AsyncOpenAI:
        return self._client

    @staticmethod
    def model_profile(model_name: str) -> ModelProfile | None:
        prefix_to_profile = {
            'llama': meta_model_profile,
            'gemma': google_model_profile,
            'qwen': qwen_model_profile,
            'qwq': qwen_model_profile,
            'deepseek': deepseek_model_profile,
            'mistral': mistral_model_profile,
            'command': cohere_model_profile,
            'gpt-oss': harmony_model_profile,
        }

        profile = None
        for prefix, profile_func in prefix_to_profile.items():
            model_name = model_name.lower()
            if model_name.startswith(prefix):
                profile = profile_func(model_name)

        # As OllamaProvider is always used with OpenAIChatModel, which used to unconditionally use OpenAIJsonSchemaTransformer,
        # we need to maintain that behavior unless json_schema_transformer is set explicitly
        return OpenAIModelProfile(
            json_schema_transformer=OpenAIJsonSchemaTransformer,
            openai_chat_thinking_field='reasoning',
            supports_json_schema_output=True,
            supports_json_object_output=True,
        ).update(profile)

    def __init__(
        self,
        base_url: str | None = None,
        api_key: str | None = None,
        openai_client: AsyncOpenAI | None = None,
        http_client: httpx.AsyncClient | None = None,
    ) -> None:
        """Create a new Ollama provider.

        Args:
            base_url: The base url for the Ollama requests. If not provided, the `OLLAMA_BASE_URL` environment variable
                will be used if available.
            api_key: The API key to use for authentication, if not provided, the `OLLAMA_API_KEY` environment variable
                will be used if available.
            openai_client: An existing
                [`AsyncOpenAI`](https://github.com/openai/openai-python?tab=readme-ov-file#async-usage)
                client to use. If provided, `base_url`, `api_key`, and `http_client` must be `None`.
            http_client: An existing `httpx.AsyncClient` to use for making HTTP requests.
        """
        if openai_client is not None:
            assert base_url is None, 'Cannot provide both `openai_client` and `base_url`'
            assert http_client is None, 'Cannot provide both `openai_client` and `http_client`'
            assert api_key is None, 'Cannot provide both `openai_client` and `api_key`'
            self._client = openai_client
        else:
            base_url = base_url or os.getenv('OLLAMA_BASE_URL')
            if not base_url:
                raise UserError(
                    'Set the `OLLAMA_BASE_URL` environment variable or pass it via `OllamaProvider(base_url=...)`'
                    'to use the Ollama provider.'
                )

            # This is a workaround for the OpenAI client requiring an API key, whilst locally served,
            # openai compatible models do not always need an API key, but a placeholder (non-empty) key is required.
            api_key = api_key or os.getenv('OLLAMA_API_KEY') or 'api-key-not-set'

            if http_client is not None:
                self._client = AsyncOpenAI(base_url=base_url, api_key=api_key, http_client=http_client)
            else:
                http_client = cached_async_http_client(provider='ollama')
                self._client = AsyncOpenAI(base_url=base_url, api_key=api_key, http_client=http_client)

```

---|---
###  __init__
```
__init__(
    base_url:  | None = None,
    api_key:  | None = None,
    openai_client: AsyncOpenAI | None = None,
    http_client: AsyncClient | None = None,
) -> None

```

Create a new Ollama provider.
Parameters:
Name | Type | Description | Default
---|---|---|---
`base_url` |  |  The base url for the Ollama requests. If not provided, the `OLLAMA_BASE_URL` environment variable will be used if available. |  `None`
`api_key` |  |  The API key to use for authentication, if not provided, the `OLLAMA_API_KEY` environment variable will be used if available. |  `None`
`openai_client` |  `AsyncOpenAI | None` |  An existing `base_url`, `api_key`, and `http_client` must be `None`. |  `None`
`http_client` |  `AsyncClient | None` |  An existing `httpx.AsyncClient` to use for making HTTP requests. |  `None`
Source code in `pydantic_ai_slim/pydantic_ai/providers/ollama.py`
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
```
| ```
def __init__(
    self,
    base_url: str | None = None,
    api_key: str | None = None,
    openai_client: AsyncOpenAI | None = None,
    http_client: httpx.AsyncClient | None = None,
) -> None:
    """Create a new Ollama provider.

    Args:
        base_url: The base url for the Ollama requests. If not provided, the `OLLAMA_BASE_URL` environment variable
            will be used if available.
        api_key: The API key to use for authentication, if not provided, the `OLLAMA_API_KEY` environment variable
            will be used if available.
        openai_client: An existing
            [`AsyncOpenAI`](https://github.com/openai/openai-python?tab=readme-ov-file#async-usage)
            client to use. If provided, `base_url`, `api_key`, and `http_client` must be `None`.
        http_client: An existing `httpx.AsyncClient` to use for making HTTP requests.
    """
    if openai_client is not None:
        assert base_url is None, 'Cannot provide both `openai_client` and `base_url`'
        assert http_client is None, 'Cannot provide both `openai_client` and `http_client`'
        assert api_key is None, 'Cannot provide both `openai_client` and `api_key`'
        self._client = openai_client
    else:
        base_url = base_url or os.getenv('OLLAMA_BASE_URL')
        if not base_url:
            raise UserError(
                'Set the `OLLAMA_BASE_URL` environment variable or pass it via `OllamaProvider(base_url=...)`'
                'to use the Ollama provider.'
            )

        # This is a workaround for the OpenAI client requiring an API key, whilst locally served,
        # openai compatible models do not always need an API key, but a placeholder (non-empty) key is required.
        api_key = api_key or os.getenv('OLLAMA_API_KEY') or 'api-key-not-set'

        if http_client is not None:
            self._client = AsyncOpenAI(base_url=base_url, api_key=api_key, http_client=http_client)
        else:
            http_client = cached_async_http_client(provider='ollama')
            self._client = AsyncOpenAI(base_url=base_url, api_key=api_key, http_client=http_client)

```

---|---
Bases: `Provider[](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.Provider "pydantic_ai.providers.Provider")[AsyncOpenAI]`
Provider for LiteLLM API.
Source code in `pydantic_ai_slim/pydantic_ai/providers/litellm.py`
```
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
```
| ```
class LiteLLMProvider(Provider[AsyncOpenAI]):
    """Provider for LiteLLM API."""

    @property
    def name(self) -> str:
        return 'litellm'

    @property
    def base_url(self) -> str:
        return str(self.client.base_url)

    @property
    def client(self) -> AsyncOpenAI:
        return self._client

    @staticmethod
    def model_profile(model_name: str) -> ModelProfile | None:
        # Map provider prefixes to their profile functions
        provider_to_profile = {
            'anthropic': anthropic_model_profile,
            'openai': openai_model_profile,
            'google': google_model_profile,
            'mistralai': mistral_model_profile,
            'mistral': mistral_model_profile,
            'cohere': cohere_model_profile,
            'amazon': amazon_model_profile,
            'bedrock': amazon_model_profile,
            'meta-llama': meta_model_profile,
            'meta': meta_model_profile,
            'groq': groq_model_profile,
            'deepseek': deepseek_model_profile,
            'moonshotai': moonshotai_model_profile,
            'x-ai': grok_model_profile,
            'qwen': qwen_model_profile,
        }

        profile = None

        # Check if model name contains a provider prefix (e.g., "anthropic/claude-3")
        if '/' in model_name:
            provider_prefix, model_suffix = model_name.split('/', 1)
            if provider_prefix in provider_to_profile:
                profile = provider_to_profile[provider_prefix](model_suffix)

        # If no profile found, default to OpenAI profile
        if profile is None:
            profile = openai_model_profile(model_name)

        # As LiteLLMProvider is used with OpenAIModel, which uses OpenAIJsonSchemaTransformer,
