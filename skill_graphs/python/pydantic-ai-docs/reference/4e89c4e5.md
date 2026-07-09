
    embedder = Embedder('openai:text-embedding-3-small')


    async def main():
        result = await embedder.embed_query('What is AI?')

        # Access embeddings by index
        print(len(result.embeddings[0]))
        #> 1536

        # Access embeddings by original input text
        print(result['What is AI?'] == result.embeddings[0])
        #> True

        # Check usage
        print(f'Tokens used: {result.usage.input_tokens}')
        #> Tokens used: 3
```
    """

    embeddings: Sequence[Sequence[float]]
    """The computed embedding vectors, one per input text.

    Each embedding is a sequence of floats representing the text in vector space.
    """

    _: KW_ONLY

    inputs: Sequence[str]
    """The original input texts that were embedded."""

    input_type: EmbedInputType
    """Whether the inputs were embedded as queries or documents."""

    model_name: str
    """The name of the model that generated these embeddings."""

    provider_name: str
    """The name of the provider (e.g., 'openai', 'cohere')."""

    timestamp: datetime = field(default_factory=_now_utc)
    """When the embedding request was made."""

    usage: RequestUsage = field(default_factory=RequestUsage)
    """Token usage statistics for this request."""

    provider_details: dict[str, Any] | None = None
    """Provider-specific details from the response."""

    provider_response_id: str | None = None
    """Unique identifier for this response from the provider, if available."""

    def __getitem__(self, item: int | str) -> Sequence[float]:
        """Get the embedding for an input by index or by the original input text.

        Args:
            item: Either an integer index or the original input string.

        Returns:
            The embedding vector for the specified input.

        Raises:
            IndexError: If the index is out of range.
            ValueError: If the string is not found in the inputs.
        """
        if isinstance(item, str):
            item = self.inputs.index(item)

        return self.embeddings[item]

    def cost(self) -> genai_types.PriceCalculation:
        """Calculate the cost of the embedding request.

        Uses [`genai-prices`](https://github.com/pydantic/genai-prices) for pricing data.

        Returns:
            A price calculation object with `total_price`, `input_price`, and other cost details.

        Raises:
            LookupError: If pricing data is not available for this model/provider.
        """
        assert self.model_name, 'Model name is required to calculate price'
        return calc_price(
            self.usage,
            self.model_name,
            provider_id=self.provider_name,
            genai_request_timestamp=self.timestamp,
        )

```

---|---
####  embeddings `instance-attribute`
```
embeddings: [[]]

```

The computed embedding vectors, one per input text.
Each embedding is a sequence of floats representing the text in vector space.
####  inputs `instance-attribute`
```
inputs: []

```

The original input texts that were embedded.
####  input_type `instance-attribute`
```
input_type: EmbedInputType[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.result.EmbedInputType "EmbedInputType



      module-attribute
   \(pydantic_ai.embeddings.result.EmbedInputType\)")

```

Whether the inputs were embedded as queries or documents.
####  model_name `instance-attribute`
```
model_name:

```

The name of the model that generated these embeddings.
####  provider_name `instance-attribute`
```
provider_name:

```

The name of the provider (e.g., 'openai', 'cohere').
####  timestamp `class-attribute` `instance-attribute`
```
timestamp:  = (default_factory=now_utc)

```

When the embedding request was made.
####  usage `class-attribute` `instance-attribute`
```
usage: RequestUsage[](https://ai.pydantic.dev/api/usage/#pydantic_ai.usage.RequestUsage "RequestUsage



      dataclass
   \(pydantic_ai.usage.RequestUsage\)") = (default_factory=RequestUsage[](https://ai.pydantic.dev/api/usage/#pydantic_ai.usage.RequestUsage "RequestUsage



      dataclass
   \(pydantic_ai.usage.RequestUsage\)"))

```

Token usage statistics for this request.
####  provider_details `class-attribute` `instance-attribute`
```
provider_details: [, ] | None = None

```

Provider-specific details from the response.
####  provider_response_id `class-attribute` `instance-attribute`
```
provider_response_id:  | None = None

```

Unique identifier for this response from the provider, if available.
####  __getitem__
```
__getitem__(item:  | ) -> []

```

Get the embedding for an input by index or by the original input text.
Parameters:
Name | Type | Description | Default
---|---|---|---
`item` |  |  Either an integer index or the original input string. |  _required_
Returns:
Type | Description
---|---
|  The embedding vector for the specified input.
Raises:
Type | Description
---|---
|  If the index is out of range.
|  If the string is not found in the inputs.
Source code in `pydantic_ai_slim/pydantic_ai/embeddings/result.py`
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
```
| ```
def __getitem__(self, item: int | str) -> Sequence[float]:
    """Get the embedding for an input by index or by the original input text.

    Args:
        item: Either an integer index or the original input string.

    Returns:
        The embedding vector for the specified input.

    Raises:
        IndexError: If the index is out of range.
        ValueError: If the string is not found in the inputs.
    """
    if isinstance(item, str):
        item = self.inputs.index(item)

    return self.embeddings[item]

```

---|---
####  cost
```
cost() -> PriceCalculation

```

Calculate the cost of the embedding request.
Uses
Returns:
Type | Description
---|---
`PriceCalculation` |  A price calculation object with `total_price`, `input_price`, and other cost details.
Raises:
Type | Description
---|---
|  If pricing data is not available for this model/provider.
Source code in `pydantic_ai_slim/pydantic_ai/embeddings/result.py`
```
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
```
| ```
def cost(self) -> genai_types.PriceCalculation:
    """Calculate the cost of the embedding request.

    Uses [`genai-prices`](https://github.com/pydantic/genai-prices) for pricing data.

    Returns:
        A price calculation object with `total_price`, `input_price`, and other cost details.

    Raises:
        LookupError: If pricing data is not available for this model/provider.
    """
    assert self.model_name, 'Model name is required to calculate price'
    return calc_price(
        self.usage,
        self.model_name,
        provider_id=self.provider_name,
        genai_request_timestamp=self.timestamp,
    )

```

---|---
###  EmbeddingSettings
Bases:
Common settings for configuring embedding models.
These settings apply across multiple embedding model providers. Not all settings are supported by all models - check the specific model's documentation for details.
Provider-specific settings classes (e.g., [`OpenAIEmbeddingSettings`](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.openai.OpenAIEmbeddingSettings "OpenAIEmbeddingSettings"), [`CohereEmbeddingSettings`](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.cohere.CohereEmbeddingSettings "CohereEmbeddingSettings")) extend this with additional provider-prefixed options.
Source code in `pydantic_ai_slim/pydantic_ai/embeddings/settings.py`
```
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
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
```
| ```
class EmbeddingSettings(TypedDict, total=False):
    """Common settings for configuring embedding models.

    These settings apply across multiple embedding model providers.
    Not all settings are supported by all models - check the specific
    model's documentation for details.

    Provider-specific settings classes (e.g.,
    [`OpenAIEmbeddingSettings`][pydantic_ai.embeddings.openai.OpenAIEmbeddingSettings],
    [`CohereEmbeddingSettings`][pydantic_ai.embeddings.cohere.CohereEmbeddingSettings])
    extend this with additional provider-prefixed options.
    """

    dimensions: int
    """The number of dimensions for the output embeddings.

    Supported by:

    * OpenAI
    * Cohere
    * Google
    * Sentence Transformers
    * Bedrock
    * VoyageAI
    """

    truncate: bool
    """Whether to truncate inputs that exceed the model's context length.

    Defaults to `False`. If `True`, inputs that are too long will be truncated.
    If `False`, an error will be raised for inputs that exceed the context length.

    For more control over truncation, you can use
    [`max_input_tokens()`][pydantic_ai.embeddings.Embedder.max_input_tokens] and
    [`count_tokens()`][pydantic_ai.embeddings.Embedder.count_tokens] to implement
    your own truncation logic.

    Provider-specific truncation settings (e.g., `cohere_truncate`, `bedrock_cohere_truncate`)
    take precedence if specified.

    Supported by:

    * Cohere
    * Bedrock (Cohere and Nova models)
    * VoyageAI
    """

    extra_headers: dict[str, str]
    """Extra headers to send to the model.

    Supported by:

    * OpenAI
    * Cohere
    """

    extra_body: object
    """Extra body to send to the model.

    Supported by:

    * OpenAI
    * Cohere
    """

```

---|---
####  dimensions `instance-attribute`
```
dimensions:

```

The number of dimensions for the output embeddings.
Supported by:
  * OpenAI
  * Cohere
  * Google
  * Sentence Transformers
  * Bedrock
  * VoyageAI


####  truncate `instance-attribute`
```
truncate:

```

Whether to truncate inputs that exceed the model's context length.
Defaults to `False`. If `True`, inputs that are too long will be truncated. If `False`, an error will be raised for inputs that exceed the context length.
For more control over truncation, you can use [`max_input_tokens()`](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.Embedder.max_input_tokens "max_input_tokens



      async
  ") and [`count_tokens()`](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.Embedder.count_tokens "count_tokens



      async
  ") to implement your own truncation logic.
Provider-specific truncation settings (e.g., `cohere_truncate`, `bedrock_cohere_truncate`) take precedence if specified.
Supported by:
  * Cohere
  * Bedrock (Cohere and Nova models)
  * VoyageAI


####  extra_headers `instance-attribute`
```
extra_headers: [, ]

```

Extra headers to send to the model.
Supported by:
  * OpenAI
  * Cohere


####  extra_body `instance-attribute`
```
extra_body:

```

Extra body to send to the model.
Supported by:
  * OpenAI
  * Cohere


###  merge_embedding_settings
```
merge_embedding_settings(
    base: EmbeddingSettings[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.settings.EmbeddingSettings "EmbeddingSettings \(pydantic_ai.embeddings.settings.EmbeddingSettings\)") | None,
    overrides: EmbeddingSettings[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.settings.EmbeddingSettings "EmbeddingSettings \(pydantic_ai.embeddings.settings.EmbeddingSettings\)") | None,
) -> EmbeddingSettings[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.settings.EmbeddingSettings "EmbeddingSettings \(pydantic_ai.embeddings.settings.EmbeddingSettings\)") | None

```

Merge two sets of embedding settings, with overrides taking precedence.
Parameters:
Name | Type | Description | Default
---|---|---|---
`base` |  `EmbeddingSettings[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.settings.EmbeddingSettings "EmbeddingSettings \(pydantic_ai.embeddings.settings.EmbeddingSettings\)") | None` |  Base settings (typically from the embedder or model). |  _required_
`overrides` |  `EmbeddingSettings[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.settings.EmbeddingSettings "EmbeddingSettings \(pydantic_ai.embeddings.settings.EmbeddingSettings\)") | None` |  Settings that should override the base (typically per-call settings). |  _required_
Returns:
Type | Description
---|---
`EmbeddingSettings[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.settings.EmbeddingSettings "EmbeddingSettings \(pydantic_ai.embeddings.settings.EmbeddingSettings\)") | None` |  Merged settings, or `None` if both inputs are `None`.
Source code in `pydantic_ai_slim/pydantic_ai/embeddings/settings.py`
```
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
def merge_embedding_settings(
    base: EmbeddingSettings | None, overrides: EmbeddingSettings | None
) -> EmbeddingSettings | None:
    """Merge two sets of embedding settings, with overrides taking precedence.

    Args:
        base: Base settings (typically from the embedder or model).
        overrides: Settings that should override the base (typically per-call settings).

    Returns:
        Merged settings, or `None` if both inputs are `None`.
    """
    # Note: we may want merge recursively if/when we add non-primitive values
    if base and overrides:
        return base | overrides
    else:
        return base or overrides

```

---|---
###  TestEmbeddingModel `dataclass`
Bases: `EmbeddingModel[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.base.EmbeddingModel "EmbeddingModel \(pydantic_ai.embeddings.base.EmbeddingModel\)")`
A mock embedding model for testing.
This model returns deterministic embeddings (all 1.0 values) and tracks the settings used in the last call via the `last_settings` attribute.
Example:
```
from pydantic_ai import Embedder
from pydantic_ai.embeddings import TestEmbeddingModel

test_model = TestEmbeddingModel()
embedder = Embedder('openai:text-embedding-3-small')


async def main():
    with embedder.override(model=test_model):
        await embedder.embed_query('test')
        assert test_model.last_settings is not None

```

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/test.py`
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
```
| ```
@dataclass(init=False)
class TestEmbeddingModel(EmbeddingModel):
    """A mock embedding model for testing.

    This model returns deterministic embeddings (all 1.0 values) and tracks
    the settings used in the last call via the `last_settings` attribute.

    Example:
```python
    from pydantic_ai import Embedder
    from pydantic_ai.embeddings import TestEmbeddingModel

    test_model = TestEmbeddingModel()
    embedder = Embedder('openai:text-embedding-3-small')


    async def main():
        with embedder.override(model=test_model):
            await embedder.embed_query('test')
            assert test_model.last_settings is not None
```
    """

    # NOTE: Avoid test discovery by pytest.
    __test__ = False

    _model_name: str
    """The model name to report in results."""

    _provider_name: str
    """The provider name to report in results."""

    _dimensions: int
    """The number of dimensions for generated embeddings."""

    last_settings: EmbeddingSettings | None = None
    """The settings used in the most recent embed call."""

    def __init__(
        self,
        model_name: str = 'test',
        *,
        provider_name: str = 'test',
        dimensions: int = 8,
        settings: EmbeddingSettings | None = None,
    ):
        """Initialize the test embedding model.

        Args:
            model_name: The model name to report in results.
            provider_name: The provider name to report in results.
            dimensions: The number of dimensions for the generated embeddings.
            settings: Optional default settings for the model.
        """
        self._model_name = model_name
        self._provider_name = provider_name
        self._dimensions = dimensions
        self.last_settings = None
        super().__init__(settings=settings)

    @property
    def model_name(self) -> str:
        """The embedding model name."""
        return self._model_name

    @property
    def system(self) -> str:
        """The embedding model provider."""
        return self._provider_name

    async def embed(
        self, inputs: str | Sequence[str], *, input_type: EmbedInputType, settings: EmbeddingSettings | None = None
    ) -> EmbeddingResult:
        inputs, settings = self.prepare_embed(inputs, settings)
        self.last_settings = settings

        dimensions = settings.get('dimensions') or self._dimensions

        return EmbeddingResult(
            embeddings=[[1.0] * dimensions] * len(inputs),
            inputs=inputs,
            input_type=input_type,
            usage=RequestUsage(input_tokens=sum(_estimate_tokens(text) for text in inputs)),
            model_name=self.model_name,
            provider_name=self.system,
            provider_response_id=str(uuid.uuid4()),
        )

    async def max_input_tokens(self) -> int | None:
        return 1024

    async def count_tokens(self, text: str) -> int:
        return _estimate_tokens(text)

```

---|---
####  last_settings `class-attribute` `instance-attribute`
```
last_settings: EmbeddingSettings[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.settings.EmbeddingSettings "EmbeddingSettings \(pydantic_ai.embeddings.settings.EmbeddingSettings\)") | None = None

```

The settings used in the most recent embed call.
####  __init__
```
__init__(
    model_name:  = "test",
    *,
    provider_name:  = "test",
    dimensions:  = 8,
    settings: EmbeddingSettings[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.settings.EmbeddingSettings "EmbeddingSettings \(pydantic_ai.embeddings.settings.EmbeddingSettings\)") | None = None
)

```

Initialize the test embedding model.
Parameters:
Name | Type | Description | Default
---|---|---|---
`model_name` |  |  The model name to report in results. |  `'test'`
`provider_name` |  |  The provider name to report in results. |  `'test'`
`dimensions` |  |  The number of dimensions for the generated embeddings. |  `8`
`settings` |  `EmbeddingSettings[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.settings.EmbeddingSettings "EmbeddingSettings \(pydantic_ai.embeddings.settings.EmbeddingSettings\)") | None` |  Optional default settings for the model. |  `None`
Source code in `pydantic_ai_slim/pydantic_ai/embeddings/test.py`
```
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
```
| ```
def __init__(
    self,
    model_name: str = 'test',
    *,
    provider_name: str = 'test',
    dimensions: int = 8,
    settings: EmbeddingSettings | None = None,
):
    """Initialize the test embedding model.

    Args:
        model_name: The model name to report in results.
        provider_name: The provider name to report in results.
        dimensions: The number of dimensions for the generated embeddings.
        settings: Optional default settings for the model.
    """
    self._model_name = model_name
    self._provider_name = provider_name
    self._dimensions = dimensions
    self.last_settings = None
    super().__init__(settings=settings)

```

---|---
####  model_name `property`
```
model_name:

```

The embedding model name.
####  system `property`
```
system:

```

The embedding model provider.
###  WrapperEmbeddingModel `dataclass`
Bases: `EmbeddingModel[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.base.EmbeddingModel "EmbeddingModel \(pydantic_ai.embeddings.base.EmbeddingModel\)")`
Base class for embedding models that wrap another model.
Use this as a base class to create custom embedding model wrappers that modify behavior (e.g., caching, logging, rate limiting) while delegating to an underlying model.
By default, all methods are passed through to the wrapped model. Override specific methods to customize behavior.
Source code in `pydantic_ai_slim/pydantic_ai/embeddings/wrapper.py`
```
15
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
```
| ```
@dataclass(init=False)
class WrapperEmbeddingModel(EmbeddingModel):
    """Base class for embedding models that wrap another model.

    Use this as a base class to create custom embedding model wrappers
    that modify behavior (e.g., caching, logging, rate limiting) while
    delegating to an underlying model.

    By default, all methods are passed through to the wrapped model.
    Override specific methods to customize behavior.
    """

    wrapped: EmbeddingModel
    """The underlying embedding model being wrapped."""

    def __init__(self, wrapped: EmbeddingModel | str):
        """Initialize the wrapper with an embedding model.

        Args:
            wrapped: The model to wrap. Can be an
                [`EmbeddingModel`][pydantic_ai.embeddings.EmbeddingModel] instance
                or a model name string (e.g., `'openai:text-embedding-3-small'`).
        """
        from . import infer_embedding_model

        super().__init__()
        self.wrapped = infer_embedding_model(wrapped) if isinstance(wrapped, str) else wrapped

    async def embed(
        self, inputs: str | Sequence[str], *, input_type: EmbedInputType, settings: EmbeddingSettings | None = None
    ) -> EmbeddingResult:
        return await self.wrapped.embed(inputs, input_type=input_type, settings=settings)

    async def max_input_tokens(self) -> int | None:
        return await self.wrapped.max_input_tokens()

    async def count_tokens(self, text: str) -> int:
        return await self.wrapped.count_tokens(text)

    @property
    def model_name(self) -> str:
        return self.wrapped.model_name

    @property
    def system(self) -> str:
        return self.wrapped.system

    @property
    def settings(self) -> EmbeddingSettings | None:
        """Get the settings from the wrapped embedding model."""
        return self.wrapped.settings

    @property
    def base_url(self) -> str | None:
        return self.wrapped.base_url

    def __getattr__(self, item: str):
        return getattr(self.wrapped, item)  # pragma: no cover

```

---|---
####  wrapped `instance-attribute`
```
wrapped: EmbeddingModel[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.base.EmbeddingModel "EmbeddingModel \(pydantic_ai.embeddings.base.EmbeddingModel\)") = (
    infer_embedding_model[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.infer_embedding_model "infer_embedding_model \(pydantic_ai.embeddings.infer_embedding_model\)")(wrapped)
    if (wrapped, )
    else wrapped
)

```

The underlying embedding model being wrapped.
####  __init__
```
__init__(wrapped: EmbeddingModel[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.base.EmbeddingModel "EmbeddingModel \(pydantic_ai.embeddings.base.EmbeddingModel\)") | )

```

Initialize the wrapper with an embedding model.
Parameters:
Name | Type | Description | Default
---|---|---|---
`wrapped` |  `EmbeddingModel[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.base.EmbeddingModel "EmbeddingModel \(pydantic_ai.embeddings.base.EmbeddingModel\)") | ` |  The model to wrap. Can be an [`EmbeddingModel`](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.EmbeddingModel "EmbeddingModel") instance or a model name string (e.g., `'openai:text-embedding-3-small'`). |  _required_
Source code in `pydantic_ai_slim/pydantic_ai/embeddings/wrapper.py`
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
```
| ```
def __init__(self, wrapped: EmbeddingModel | str):
    """Initialize the wrapper with an embedding model.

    Args:
        wrapped: The model to wrap. Can be an
            [`EmbeddingModel`][pydantic_ai.embeddings.EmbeddingModel] instance
            or a model name string (e.g., `'openai:text-embedding-3-small'`).
    """
    from . import infer_embedding_model

    super().__init__()
    self.wrapped = infer_embedding_model(wrapped) if isinstance(wrapped, str) else wrapped

```

---|---
####  settings `property`
```
settings: EmbeddingSettings[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.settings.EmbeddingSettings "EmbeddingSettings \(pydantic_ai.embeddings.settings.EmbeddingSettings\)") | None

```

Get the settings from the wrapped embedding model.
###  KnownEmbeddingModelName `module-attribute`
```
KnownEmbeddingModelName = (
    "KnownEmbeddingModelName",
    [
        "google-gla:gemini-embedding-001",
        "google-vertex:gemini-embedding-001",
        "google-vertex:text-embedding-005",
        "google-vertex:text-multilingual-embedding-002",
        "openai:text-embedding-ada-002",
        "openai:text-embedding-3-small",
        "openai:text-embedding-3-large",
        "cohere:embed-v4.0",
        "cohere:embed-english-v3.0",
        "cohere:embed-english-light-v3.0",
        "cohere:embed-multilingual-v3.0",
        "cohere:embed-multilingual-light-v3.0",
        "voyageai:voyage-4-large",
        "voyageai:voyage-4",
        "voyageai:voyage-4-lite",
        "voyageai:voyage-3-large",
        "voyageai:voyage-3.5",
