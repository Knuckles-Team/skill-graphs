---|---|---|---
`inputs` |  |  A single string or sequence of strings to embed. |  _required_
`input_type` |  `EmbedInputType[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.result.EmbedInputType "EmbedInputType



      module-attribute
   \(pydantic_ai.embeddings.result.EmbedInputType\)")` |  Whether the inputs are queries or documents. |  _required_
`settings` |  `EmbeddingSettings[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.settings.EmbeddingSettings "EmbeddingSettings \(pydantic_ai.embeddings.settings.EmbeddingSettings\)") | None` |  Optional settings to override the model's defaults. |  `None`
Returns:
Type | Description
---|---
`EmbeddingResult[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.result.EmbeddingResult "EmbeddingResult



      dataclass
   \(pydantic_ai.embeddings.result.EmbeddingResult\)")` |  An [`EmbeddingResult`](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.EmbeddingResult "EmbeddingResult



      dataclass
  ") containing
`EmbeddingResult[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.result.EmbeddingResult "EmbeddingResult



      dataclass
   \(pydantic_ai.embeddings.result.EmbeddingResult\)")` |  the embeddings and metadata.
Source code in `pydantic_ai_slim/pydantic_ai/embeddings/base.py`
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
```
| ```
@abstractmethod
async def embed(
    self, inputs: str | Sequence[str], *, input_type: EmbedInputType, settings: EmbeddingSettings | None = None
) -> EmbeddingResult:
    """Generate embeddings for the given inputs.

    Args:
        inputs: A single string or sequence of strings to embed.
        input_type: Whether the inputs are queries or documents.
        settings: Optional settings to override the model's defaults.

    Returns:
        An [`EmbeddingResult`][pydantic_ai.embeddings.EmbeddingResult] containing
        the embeddings and metadata.
    """
    raise NotImplementedError

```

---|---
####  prepare_embed
```
prepare_embed(
    inputs:  | [],
    settings: EmbeddingSettings[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.settings.EmbeddingSettings "EmbeddingSettings \(pydantic_ai.embeddings.settings.EmbeddingSettings\)") | None = None,
) -> [[], EmbeddingSettings[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.settings.EmbeddingSettings "EmbeddingSettings \(pydantic_ai.embeddings.settings.EmbeddingSettings\)")]

```

Prepare the inputs and settings for embedding.
This method normalizes inputs to a list and merges settings. Subclasses should call this at the start of their `embed()` implementation.
Parameters:
Name | Type | Description | Default
---|---|---|---
`inputs` |  |  A single string or sequence of strings. |  _required_
`settings` |  `EmbeddingSettings[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.settings.EmbeddingSettings "EmbeddingSettings \(pydantic_ai.embeddings.settings.EmbeddingSettings\)") | None` |  Optional settings to merge with defaults. |  `None`
Returns:
Type | Description
---|---
`EmbeddingSettings[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.settings.EmbeddingSettings "EmbeddingSettings \(pydantic_ai.embeddings.settings.EmbeddingSettings\)")]` |  A tuple of (normalized inputs list, merged settings).
Source code in `pydantic_ai_slim/pydantic_ai/embeddings/base.py`
```
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
def prepare_embed(
    self, inputs: str | Sequence[str], settings: EmbeddingSettings | None = None
) -> tuple[list[str], EmbeddingSettings]:
    """Prepare the inputs and settings for embedding.

    This method normalizes inputs to a list and merges settings.
    Subclasses should call this at the start of their `embed()` implementation.

    Args:
        inputs: A single string or sequence of strings.
        settings: Optional settings to merge with defaults.

    Returns:
        A tuple of (normalized inputs list, merged settings).
    """
    inputs = [inputs] if isinstance(inputs, str) else list(inputs)

    settings = merge_embedding_settings(self._settings, settings) or {}

    return inputs, settings

```

---|---
####  max_input_tokens `async`
```
max_input_tokens() ->  | None

```

Get the maximum number of tokens that can be input to the model.
Returns:
Type | Description
---|---
|  The maximum token count, or `None` if unknown.
Source code in `pydantic_ai_slim/pydantic_ai/embeddings/base.py`
```
 95
 96
 97
 98
 99
100
101
```
| ```
async def max_input_tokens(self) -> int | None:
    """Get the maximum number of tokens that can be input to the model.

    Returns:
        The maximum token count, or `None` if unknown.
    """
    return None  # pragma: no cover

```

---|---
####  count_tokens `async`
```
count_tokens(text: ) ->

```

Count the number of tokens in the given text.
Parameters:
Name | Type | Description | Default
---|---|---|---
`text` |  |  The text to tokenize and count. |  _required_
Returns:
Type | Description
---|---
|  The number of tokens.
Raises:
Type | Description
---|---
|  If the model doesn't support token counting.
`UserError[](https://ai.pydantic.dev/api/exceptions/#pydantic_ai.exceptions.UserError "UserError \(pydantic_ai.exceptions.UserError\)")` |  If the model or tokenizer is not supported.
Source code in `pydantic_ai_slim/pydantic_ai/embeddings/base.py`
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
```
| ```
async def count_tokens(self, text: str) -> int:
    """Count the number of tokens in the given text.

    Args:
        text: The text to tokenize and count.

    Returns:
        The number of tokens.

    Raises:
        NotImplementedError: If the model doesn't support token counting.
        UserError: If the model or tokenizer is not supported.
    """
    raise NotImplementedError

```

---|---
###  EmbedInputType `module-attribute`
```
EmbedInputType = ['query', 'document']

```

The type of input to the embedding model.
  * `'query'`: Text that will be used as a search query
  * `'document'`: Text that will be stored and searched against


Some embedding models optimize differently for queries vs documents.
###  EmbeddingResult `dataclass`
The result of an embedding operation.
This class contains the generated embeddings along with metadata about the operation, including the original inputs, model information, usage statistics, and timing.
Example:
```
from pydantic_ai import Embedder

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

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/result.py`
```
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
```
| ```
@dataclass
class EmbeddingResult:
    """The result of an embedding operation.

    This class contains the generated embeddings along with metadata about
    the operation, including the original inputs, model information, usage
    statistics, and timing.

    Example:
```python
    from pydantic_ai import Embedder

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
###  OpenAIEmbeddingModelName `module-attribute`
```
OpenAIEmbeddingModelName =  | EmbeddingModel

```

Possible OpenAI embeddings model names.
See the
###  OpenAIEmbeddingSettings
Bases: `EmbeddingSettings[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.settings.EmbeddingSettings "EmbeddingSettings \(pydantic_ai.embeddings.settings.EmbeddingSettings\)")`
Settings used for an OpenAI embedding model request.
All fields from [`EmbeddingSettings`](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.EmbeddingSettings "EmbeddingSettings") are supported.
Source code in `pydantic_ai_slim/pydantic_ai/embeddings/openai.py`
```
36
37
38
39
40
```
| ```
class OpenAIEmbeddingSettings(EmbeddingSettings, total=False):
    """Settings used for an OpenAI embedding model request.

    All fields from [`EmbeddingSettings`][pydantic_ai.embeddings.EmbeddingSettings] are supported.
    """

```

---|---
###  OpenAIEmbeddingModel `dataclass`
Bases: `EmbeddingModel[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.base.EmbeddingModel "EmbeddingModel \(pydantic_ai.embeddings.base.EmbeddingModel\)")`
OpenAI embedding model implementation.
This model works with OpenAI's embeddings API and any [OpenAI-compatible providers](https://ai.pydantic.dev/models/openai/#openai-compatible-models).
Example:
```
from pydantic_ai.embeddings.openai import OpenAIEmbeddingModel
from pydantic_ai.providers.openai import OpenAIProvider

# Using OpenAI directly
model = OpenAIEmbeddingModel('text-embedding-3-small')

# Using an OpenAI-compatible provider
model = OpenAIEmbeddingModel(
    'text-embedding-3-small',
    provider=OpenAIProvider(base_url='https://my-provider.com/v1'),
)

```

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/openai.py`
```
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
```
| ```
@dataclass(init=False)
class OpenAIEmbeddingModel(EmbeddingModel):
    """OpenAI embedding model implementation.

    This model works with OpenAI's embeddings API and any
    [OpenAI-compatible providers](../models/openai.md#openai-compatible-models).

    Example:
```python
    from pydantic_ai.embeddings.openai import OpenAIEmbeddingModel
    from pydantic_ai.providers.openai import OpenAIProvider

    # Using OpenAI directly
    model = OpenAIEmbeddingModel('text-embedding-3-small')

    # Using an OpenAI-compatible provider
    model = OpenAIEmbeddingModel(
        'text-embedding-3-small',
        provider=OpenAIProvider(base_url='https://my-provider.com/v1'),
    )
```
    """

    _model_name: OpenAIEmbeddingModelName = field(repr=False)
    _provider: Provider[AsyncOpenAI] = field(repr=False)

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
