        region_name: str | None = None,
        profile_name: str | None = None,
        api_key: str | None = None,
        aws_read_timeout: float | None = None,
        aws_connect_timeout: float | None = None,
    ) -> None:
        """Initialize the Bedrock provider.

        Args:
            bedrock_client: A boto3 client for Bedrock Runtime. If provided, other arguments are ignored.
            aws_access_key_id: The AWS access key ID. If not set, the `AWS_ACCESS_KEY_ID` environment variable will be used if available.
            aws_secret_access_key: The AWS secret access key. If not set, the `AWS_SECRET_ACCESS_KEY` environment variable will be used if available.
            aws_session_token: The AWS session token. If not set, the `AWS_SESSION_TOKEN` environment variable will be used if available.
            api_key: The API key for Bedrock client. Can be used instead of `aws_access_key_id`, `aws_secret_access_key`, and `aws_session_token`. If not set, the `AWS_BEARER_TOKEN_BEDROCK` environment variable will be used if available.
            base_url: The base URL for the Bedrock client.
            region_name: The AWS region name. If not set, the `AWS_DEFAULT_REGION` environment variable will be used if available.
            profile_name: The AWS profile name.
            aws_read_timeout: The read timeout for Bedrock client.
            aws_connect_timeout: The connect timeout for Bedrock client.
        """
        if bedrock_client is not None:
            self._client = bedrock_client
        else:
            read_timeout = aws_read_timeout or float(os.getenv('AWS_READ_TIMEOUT', 300))
            connect_timeout = aws_connect_timeout or float(os.getenv('AWS_CONNECT_TIMEOUT', 60))
            config: dict[str, Any] = {
                'read_timeout': read_timeout,
                'connect_timeout': connect_timeout,
            }
            api_key = api_key or os.getenv('AWS_BEARER_TOKEN_BEDROCK')
            try:
                if api_key is not None:
                    session = boto3.Session(
                        botocore_session=_BearerTokenSession(api_key),
                        region_name=region_name,
                        profile_name=profile_name,
                    )
                    config['signature_version'] = 'bearer'
                else:  # pragma: lax no cover
                    session = boto3.Session(
                        aws_access_key_id=aws_access_key_id,
                        aws_secret_access_key=aws_secret_access_key,
                        aws_session_token=aws_session_token,
                        region_name=region_name,
                        profile_name=profile_name,
                    )
                self._client = session.client(  # type: ignore[reportUnknownMemberType]
                    'bedrock-runtime',
                    config=Config(**config),
                    endpoint_url=base_url,
                )
            except NoRegionError as exc:  # pragma: no cover
                raise UserError('You must provide a `region_name` or a boto3 client for Bedrock Runtime.') from exc

```

---|---
####  __init__
```
__init__(*, bedrock_client: BaseClient) -> None

```

```
__init__(
    *,
    api_key: ,
    base_url:  | None = None,
    region_name:  | None = None,
    profile_name:  | None = None,
    aws_read_timeout:  | None = None,
    aws_connect_timeout:  | None = None
) -> None

```

```
__init__(
    *,
    aws_access_key_id:  | None = None,
    aws_secret_access_key:  | None = None,
    aws_session_token:  | None = None,
    base_url:  | None = None,
    region_name:  | None = None,
    profile_name:  | None = None,
    aws_read_timeout:  | None = None,
    aws_connect_timeout:  | None = None
) -> None

```

```
__init__(
    *,
    bedrock_client: BaseClient | None = None,
    aws_access_key_id:  | None = None,
    aws_secret_access_key:  | None = None,
    aws_session_token:  | None = None,
    base_url:  | None = None,
    region_name:  | None = None,
    profile_name:  | None = None,
    api_key:  | None = None,
    aws_read_timeout:  | None = None,
    aws_connect_timeout:  | None = None
) -> None

```

Initialize the Bedrock provider.
Parameters:
Name | Type | Description | Default
---|---|---|---
`bedrock_client` |  `BaseClient | None` |  A boto3 client for Bedrock Runtime. If provided, other arguments are ignored. |  `None`
`aws_access_key_id` |  |  The AWS access key ID. If not set, the `AWS_ACCESS_KEY_ID` environment variable will be used if available. |  `None`
`aws_secret_access_key` |  |  The AWS secret access key. If not set, the `AWS_SECRET_ACCESS_KEY` environment variable will be used if available. |  `None`
`aws_session_token` |  |  The AWS session token. If not set, the `AWS_SESSION_TOKEN` environment variable will be used if available. |  `None`
`api_key` |  |  The API key for Bedrock client. Can be used instead of `aws_access_key_id`, `aws_secret_access_key`, and `aws_session_token`. If not set, the `AWS_BEARER_TOKEN_BEDROCK` environment variable will be used if available. |  `None`
`base_url` |  |  The base URL for the Bedrock client. |  `None`
`region_name` |  |  The AWS region name. If not set, the `AWS_DEFAULT_REGION` environment variable will be used if available. |  `None`
`profile_name` |  |  The AWS profile name. |  `None`
`aws_read_timeout` |  |  The read timeout for Bedrock client. |  `None`
`aws_connect_timeout` |  |  The connect timeout for Bedrock client. |  `None`
Source code in `pydantic_ai_slim/pydantic_ai/providers/bedrock.py`
```
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
def __init__(
    self,
    *,
    bedrock_client: BaseClient | None = None,
    aws_access_key_id: str | None = None,
    aws_secret_access_key: str | None = None,
    aws_session_token: str | None = None,
    base_url: str | None = None,
    region_name: str | None = None,
    profile_name: str | None = None,
    api_key: str | None = None,
    aws_read_timeout: float | None = None,
    aws_connect_timeout: float | None = None,
) -> None:
    """Initialize the Bedrock provider.

    Args:
        bedrock_client: A boto3 client for Bedrock Runtime. If provided, other arguments are ignored.
        aws_access_key_id: The AWS access key ID. If not set, the `AWS_ACCESS_KEY_ID` environment variable will be used if available.
        aws_secret_access_key: The AWS secret access key. If not set, the `AWS_SECRET_ACCESS_KEY` environment variable will be used if available.
        aws_session_token: The AWS session token. If not set, the `AWS_SESSION_TOKEN` environment variable will be used if available.
        api_key: The API key for Bedrock client. Can be used instead of `aws_access_key_id`, `aws_secret_access_key`, and `aws_session_token`. If not set, the `AWS_BEARER_TOKEN_BEDROCK` environment variable will be used if available.
        base_url: The base URL for the Bedrock client.
        region_name: The AWS region name. If not set, the `AWS_DEFAULT_REGION` environment variable will be used if available.
        profile_name: The AWS profile name.
        aws_read_timeout: The read timeout for Bedrock client.
        aws_connect_timeout: The connect timeout for Bedrock client.
    """
    if bedrock_client is not None:
        self._client = bedrock_client
    else:
        read_timeout = aws_read_timeout or float(os.getenv('AWS_READ_TIMEOUT', 300))
        connect_timeout = aws_connect_timeout or float(os.getenv('AWS_CONNECT_TIMEOUT', 60))
        config: dict[str, Any] = {
            'read_timeout': read_timeout,
            'connect_timeout': connect_timeout,
        }
        api_key = api_key or os.getenv('AWS_BEARER_TOKEN_BEDROCK')
        try:
            if api_key is not None:
                session = boto3.Session(
                    botocore_session=_BearerTokenSession(api_key),
                    region_name=region_name,
                    profile_name=profile_name,
                )
                config['signature_version'] = 'bearer'
            else:  # pragma: lax no cover
                session = boto3.Session(
                    aws_access_key_id=aws_access_key_id,
                    aws_secret_access_key=aws_secret_access_key,
                    aws_session_token=aws_session_token,
                    region_name=region_name,
                    profile_name=profile_name,
                )
            self._client = session.client(  # type: ignore[reportUnknownMemberType]
                'bedrock-runtime',
                config=Config(**config),
                endpoint_url=base_url,
            )
        except NoRegionError as exc:  # pragma: no cover
            raise UserError('You must provide a `region_name` or a boto3 client for Bedrock Runtime.') from exc

```

---|---
###  groq_moonshotai_model_profile
```
groq_moonshotai_model_profile(
    model_name: ,
) -> ModelProfile[](https://ai.pydantic.dev/api/profiles/#pydantic_ai.profiles.ModelProfile "pydantic_ai.ModelProfile") | None

```

Get the model profile for an MoonshotAI model used with the Groq provider.
Source code in `pydantic_ai_slim/pydantic_ai/providers/groq.py`
```
30
31
32
33
34
```
| ```
def groq_moonshotai_model_profile(model_name: str) -> ModelProfile | None:
    """Get the model profile for an MoonshotAI model used with the Groq provider."""
    return ModelProfile(supports_json_object_output=True, supports_json_schema_output=True).update(
        moonshotai_model_profile(model_name)
    )

```

---|---
###  meta_groq_model_profile
```
meta_groq_model_profile(
    model_name: ,
) -> ModelProfile[](https://ai.pydantic.dev/api/profiles/#pydantic_ai.profiles.ModelProfile "pydantic_ai.ModelProfile") | None

```

Get the model profile for a Meta model used with the Groq provider.
Source code in `pydantic_ai_slim/pydantic_ai/providers/groq.py`
```
37
38
39
40
41
42
43
44
```
| ```
def meta_groq_model_profile(model_name: str) -> ModelProfile | None:
    """Get the model profile for a Meta model used with the Groq provider."""
    if model_name in {'llama-4-maverick-17b-128e-instruct', 'llama-4-scout-17b-16e-instruct'}:
        return ModelProfile(supports_json_object_output=True, supports_json_schema_output=True).update(
            meta_model_profile(model_name)
        )
    else:
        return meta_model_profile(model_name)

```

---|---
###  GroqProvider
Bases: `Provider[](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.Provider "pydantic_ai.providers.Provider")[AsyncGroq]`
Provider for Groq API.
Source code in `pydantic_ai_slim/pydantic_ai/providers/groq.py`
```
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
```
| ```
class GroqProvider(Provider[AsyncGroq]):
    """Provider for Groq API."""

    @property
    def name(self) -> str:
        return 'groq'

    @property
    def base_url(self) -> str:
        return str(self.client.base_url)

    @property
    def client(self) -> AsyncGroq:
        return self._client

    @staticmethod
    def model_profile(model_name: str) -> ModelProfile | None:
        prefix_to_profile = {
            'llama': meta_model_profile,
            'meta-llama/': meta_groq_model_profile,
            'gemma': google_model_profile,
            'qwen': qwen_model_profile,
            'deepseek': deepseek_model_profile,
            'mistral': mistral_model_profile,
            'moonshotai/': groq_moonshotai_model_profile,
            'compound-': groq_model_profile,
            'openai/': openai_model_profile,
        }

        for prefix, profile_func in prefix_to_profile.items():
            model_name = model_name.lower()
            if model_name.startswith(prefix):
                if prefix.endswith('/'):
                    model_name = model_name[len(prefix) :]
                return profile_func(model_name)

        return None

    @overload
    def __init__(self, *, groq_client: AsyncGroq | None = None) -> None: ...

    @overload
    def __init__(
        self, *, api_key: str | None = None, base_url: str | None = None, http_client: httpx.AsyncClient | None = None
    ) -> None: ...

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | None = None,
        groq_client: AsyncGroq | None = None,
        http_client: httpx.AsyncClient | None = None,
    ) -> None:
        """Create a new Groq provider.

        Args:
            api_key: The API key to use for authentication, if not provided, the `GROQ_API_KEY` environment variable
                will be used if available.
            base_url: The base url for the Groq requests. If not provided, the `GROQ_BASE_URL` environment variable
                will be used if available. Otherwise, defaults to Groq's base url.
            groq_client: An existing
                [`AsyncGroq`](https://github.com/groq/groq-python?tab=readme-ov-file#async-usage)
                client to use. If provided, `api_key` and `http_client` must be `None`.
            http_client: An existing `AsyncClient` to use for making HTTP requests.
        """
        if groq_client is not None:
            assert http_client is None, 'Cannot provide both `groq_client` and `http_client`'
            assert api_key is None, 'Cannot provide both `groq_client` and `api_key`'
            assert base_url is None, 'Cannot provide both `groq_client` and `base_url`'
            self._client = groq_client
        else:
            api_key = api_key or os.getenv('GROQ_API_KEY')
            base_url = base_url or os.getenv('GROQ_BASE_URL', 'https://api.groq.com')

            if not api_key:
                raise UserError(
                    'Set the `GROQ_API_KEY` environment variable or pass it via `GroqProvider(api_key=...)`'
                    'to use the Groq provider.'
                )
            elif http_client is not None:
                self._client = AsyncGroq(base_url=base_url, api_key=api_key, http_client=http_client)
            else:
                http_client = cached_async_http_client(provider='groq')
                self._client = AsyncGroq(base_url=base_url, api_key=api_key, http_client=http_client)

```

---|---
####  __init__
```
__init__(*, groq_client: AsyncGroq | None = None) -> None

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
    groq_client: AsyncGroq | None = None,
    http_client: AsyncClient | None = None
) -> None

```

Create a new Groq provider.
Parameters:
Name | Type | Description | Default
---|---|---|---
`api_key` |  |  The API key to use for authentication, if not provided, the `GROQ_API_KEY` environment variable will be used if available. |  `None`
`base_url` |  |  The base url for the Groq requests. If not provided, the `GROQ_BASE_URL` environment variable will be used if available. Otherwise, defaults to Groq's base url. |  `None`
`groq_client` |  `AsyncGroq | None` |  An existing `api_key` and `http_client` must be `None`. |  `None`
`http_client` |  `AsyncClient | None` |  An existing `AsyncClient` to use for making HTTP requests. |  `None`
Source code in `pydantic_ai_slim/pydantic_ai/providers/groq.py`
```
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
```
| ```
def __init__(
    self,
    *,
    api_key: str | None = None,
    base_url: str | None = None,
    groq_client: AsyncGroq | None = None,
    http_client: httpx.AsyncClient | None = None,
) -> None:
    """Create a new Groq provider.

    Args:
        api_key: The API key to use for authentication, if not provided, the `GROQ_API_KEY` environment variable
            will be used if available.
        base_url: The base url for the Groq requests. If not provided, the `GROQ_BASE_URL` environment variable
            will be used if available. Otherwise, defaults to Groq's base url.
        groq_client: An existing
            [`AsyncGroq`](https://github.com/groq/groq-python?tab=readme-ov-file#async-usage)
            client to use. If provided, `api_key` and `http_client` must be `None`.
        http_client: An existing `AsyncClient` to use for making HTTP requests.
    """
    if groq_client is not None:
        assert http_client is None, 'Cannot provide both `groq_client` and `http_client`'
        assert api_key is None, 'Cannot provide both `groq_client` and `api_key`'
        assert base_url is None, 'Cannot provide both `groq_client` and `base_url`'
        self._client = groq_client
    else:
        api_key = api_key or os.getenv('GROQ_API_KEY')
        base_url = base_url or os.getenv('GROQ_BASE_URL', 'https://api.groq.com')

        if not api_key:
            raise UserError(
                'Set the `GROQ_API_KEY` environment variable or pass it via `GroqProvider(api_key=...)`'
                'to use the Groq provider.'
            )
        elif http_client is not None:
            self._client = AsyncGroq(base_url=base_url, api_key=api_key, http_client=http_client)
        else:
            http_client = cached_async_http_client(provider='groq')
            self._client = AsyncGroq(base_url=base_url, api_key=api_key, http_client=http_client)

```

---|---
###  AzureProvider
Bases: `Provider[](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.Provider "pydantic_ai.providers.Provider")[AsyncOpenAI]`
Provider for Azure OpenAI API.
See
Source code in `pydantic_ai_slim/pydantic_ai/providers/azure.py`
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
```
| ```
class AzureProvider(Provider[AsyncOpenAI]):
    """Provider for Azure OpenAI API.

    See <https://azure.microsoft.com/en-us/products/ai-foundry> for more information.
    """

    @property
    def name(self) -> str:
        return 'azure'

    @property
    def base_url(self) -> str:
        assert self._base_url is not None
        return self._base_url

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
            'mistralai-': mistral_model_profile,
            'mistral': mistral_model_profile,
            'cohere-': cohere_model_profile,
            'grok': grok_model_profile,
        }

        for prefix, profile_func in prefix_to_profile.items():
            if model_name.startswith(prefix):
                if prefix.endswith('-'):
                    model_name = model_name[len(prefix) :]

                profile = profile_func(model_name)

                # As AzureProvider is always used with OpenAIChatModel, which used to unconditionally use OpenAIJsonSchemaTransformer,
                # we need to maintain that behavior unless json_schema_transformer is set explicitly
                return OpenAIModelProfile(json_schema_transformer=OpenAIJsonSchemaTransformer).update(profile)

        # OpenAI models are unprefixed
        return openai_model_profile(model_name)

    @overload
    def __init__(self, *, openai_client: AsyncAzureOpenAI) -> None: ...

    @overload
    def __init__(
        self,
        *,
        azure_endpoint: str | None = None,
        api_version: str | None = None,
        api_key: str | None = None,
        http_client: httpx.AsyncClient | None = None,
    ) -> None: ...

    def __init__(
        self,
        *,
        azure_endpoint: str | None = None,
        api_version: str | None = None,
        api_key: str | None = None,
        openai_client: AsyncAzureOpenAI | None = None,
        http_client: httpx.AsyncClient | None = None,
    ) -> None:
        """Create a new Azure provider.

        Args:
            azure_endpoint: The Azure endpoint to use for authentication, if not provided, the `AZURE_OPENAI_ENDPOINT`
                environment variable will be used if available.
            api_version: The API version to use for authentication, if not provided, the `OPENAI_API_VERSION`
                environment variable will be used if available.
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
####  __init__
```
__init__(*, openai_client: AsyncAzureOpenAI) -> None

```

```
__init__(
    *,
    azure_endpoint:  | None = None,
    api_version:  | None = None,
    api_key:  | None = None,
    http_client: AsyncClient | None = None
) -> None

```

```
__init__(
    *,
    azure_endpoint:  | None = None,
    api_version:  | None = None,
    api_key:  | None = None,
    openai_client: AsyncAzureOpenAI | None = None,
    http_client: AsyncClient | None = None
) -> None

```

Create a new Azure provider.
Parameters:
Name | Type | Description | Default
---|---|---|---
`azure_endpoint` |  |  The Azure endpoint to use for authentication, if not provided, the `AZURE_OPENAI_ENDPOINT` environment variable will be used if available. |  `None`
`api_version` |  |  The API version to use for authentication, if not provided, the `OPENAI_API_VERSION` environment variable will be used if available. |  `None`
`api_key` |  |  The API key to use for authentication, if not provided, the `AZURE_OPENAI_API_KEY` environment variable will be used if available. |  `None`
`openai_client` |  `AsyncAzureOpenAI | None` |  An existing `base_url`, `api_key`, and `http_client` must be `None`. |  `None`
`http_client` |  `AsyncClient | None` |  An existing `httpx.AsyncClient` to use for making HTTP requests. |  `None`
Source code in `pydantic_ai_slim/pydantic_ai/providers/azure.py`
```
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
```
| ```
def __init__(
    self,
    *,
    azure_endpoint: str | None = None,
    api_version: str | None = None,
    api_key: str | None = None,
    openai_client: AsyncAzureOpenAI | None = None,
    http_client: httpx.AsyncClient | None = None,
) -> None:
    """Create a new Azure provider.

    Args:
        azure_endpoint: The Azure endpoint to use for authentication, if not provided, the `AZURE_OPENAI_ENDPOINT`
            environment variable will be used if available.
        api_version: The API version to use for authentication, if not provided, the `OPENAI_API_VERSION`
            environment variable will be used if available.
