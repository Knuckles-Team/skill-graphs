# `pydantic_ai.embeddings`
###  EmbeddingModel
Bases:
Abstract base class for embedding models.
Implement this class to create a custom embedding model. For most use cases, use one of the built-in implementations:
  * [`OpenAIEmbeddingModel`](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.openai.OpenAIEmbeddingModel "OpenAIEmbeddingModel



      dataclass
  ")
  * [`CohereEmbeddingModel`](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.cohere.CohereEmbeddingModel "CohereEmbeddingModel



      dataclass
  ")
  * [`GoogleEmbeddingModel`](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.google.GoogleEmbeddingModel "GoogleEmbeddingModel



      dataclass
  ")
  * [`BedrockEmbeddingModel`](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.bedrock.BedrockEmbeddingModel "BedrockEmbeddingModel



      dataclass
  ")
  * [`SentenceTransformerEmbeddingModel`](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.sentence_transformers.SentenceTransformerEmbeddingModel "SentenceTransformerEmbeddingModel



      dataclass
  ")

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/base.py`
```
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
```
| ```
class EmbeddingModel(ABC):
    """Abstract base class for embedding models.

    Implement this class to create a custom embedding model. For most use cases,
    use one of the built-in implementations:

    - [`OpenAIEmbeddingModel`][pydantic_ai.embeddings.openai.OpenAIEmbeddingModel]
    - [`CohereEmbeddingModel`][pydantic_ai.embeddings.cohere.CohereEmbeddingModel]
    - [`GoogleEmbeddingModel`][pydantic_ai.embeddings.google.GoogleEmbeddingModel]
    - [`BedrockEmbeddingModel`][pydantic_ai.embeddings.bedrock.BedrockEmbeddingModel]
    - [`SentenceTransformerEmbeddingModel`][pydantic_ai.embeddings.sentence_transformers.SentenceTransformerEmbeddingModel]
    """

    _settings: EmbeddingSettings | None = None

    def __init__(
        self,
        *,
        settings: EmbeddingSettings | None = None,
    ) -> None:
        """Initialize the model with optional settings.

        Args:
            settings: Model-specific settings that will be used as defaults for this model.
        """
        self._settings = settings

    @property
    def settings(self) -> EmbeddingSettings | None:
        """Get the default settings for this model."""
        return self._settings

    @property
    def base_url(self) -> str | None:
        """The base URL for the provider API, if available."""
        return None

    @property
    @abstractmethod
    def model_name(self) -> str:
        """The name of the embedding model."""
        raise NotImplementedError()

    @property
    @abstractmethod
    def system(self) -> str:
        """The embedding model provider/system identifier (e.g., 'openai', 'cohere')."""
        raise NotImplementedError()

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

    async def max_input_tokens(self) -> int | None:
        """Get the maximum number of tokens that can be input to the model.

        Returns:
            The maximum token count, or `None` if unknown.
        """
        return None  # pragma: no cover

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
####  __init__
```
__init__(
    *, settings: EmbeddingSettings[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.settings.EmbeddingSettings "EmbeddingSettings \(pydantic_ai.embeddings.settings.EmbeddingSettings\)") | None = None
) -> None

```

Initialize the model with optional settings.
Parameters:
Name | Type | Description | Default
---|---|---|---
`settings` |  `EmbeddingSettings[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.settings.EmbeddingSettings "EmbeddingSettings \(pydantic_ai.embeddings.settings.EmbeddingSettings\)") | None` |  Model-specific settings that will be used as defaults for this model. |  `None`
Source code in `pydantic_ai_slim/pydantic_ai/embeddings/base.py`
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
```
| ```
def __init__(
    self,
    *,
    settings: EmbeddingSettings | None = None,
) -> None:
    """Initialize the model with optional settings.

    Args:
        settings: Model-specific settings that will be used as defaults for this model.
    """
    self._settings = settings

```

---|---
####  settings `property`
```
settings: EmbeddingSettings[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.settings.EmbeddingSettings "EmbeddingSettings \(pydantic_ai.embeddings.settings.EmbeddingSettings\)") | None

```

Get the default settings for this model.
####  base_url `property`
```
base_url:  | None

```

The base URL for the provider API, if available.
####  model_name `abstractmethod` `property`
```
model_name:

```

The name of the embedding model.
####  system `abstractmethod` `property`
```
system:

```

The embedding model provider/system identifier (e.g., 'openai', 'cohere').
####  embed `abstractmethod` `async`
```
embed(
    inputs:  | [],
    *,
    input_type: EmbedInputType[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.result.EmbedInputType "EmbedInputType



      module-attribute
   \(pydantic_ai.embeddings.result.EmbedInputType\)"),
    settings: EmbeddingSettings[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.settings.EmbeddingSettings "EmbeddingSettings \(pydantic_ai.embeddings.settings.EmbeddingSettings\)") | None = None
) -> EmbeddingResult[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.result.EmbeddingResult "EmbeddingResult



      dataclass
   \(pydantic_ai.embeddings.result.EmbeddingResult\)")

```

Generate embeddings for the given inputs.
Parameters:
Name | Type | Description | Default
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
###  InstrumentedEmbeddingModel `dataclass`
Bases: `WrapperEmbeddingModel[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.wrapper.WrapperEmbeddingModel "WrapperEmbeddingModel



      dataclass
   \(pydantic_ai.embeddings.wrapper.WrapperEmbeddingModel\)")`
Embedding model which wraps another model so that requests are instrumented with OpenTelemetry.
See the [Debugging and Monitoring guide](https://ai.pydantic.dev/logfire/) for more info.
Source code in `pydantic_ai_slim/pydantic_ai/embeddings/instrumented.py`
```
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
```
| ```
@dataclass(init=False)
class InstrumentedEmbeddingModel(WrapperEmbeddingModel):
    """Embedding model which wraps another model so that requests are instrumented with OpenTelemetry.

    See the [Debugging and Monitoring guide](https://ai.pydantic.dev/logfire/) for more info.
    """

    instrumentation_settings: InstrumentationSettings
    """Instrumentation settings for this model."""

    def __init__(
        self,
        wrapped: EmbeddingModel | str,
        options: InstrumentationSettings | None = None,
    ) -> None:
        super().__init__(wrapped)
        self.instrumentation_settings = options or InstrumentationSettings()

    async def embed(
        self, inputs: str | Sequence[str], *, input_type: EmbedInputType, settings: EmbeddingSettings | None = None
    ) -> EmbeddingResult:
        inputs, settings = self.prepare_embed(inputs, settings)
        with self._instrument(inputs, input_type, settings) as finish:
            result = await super().embed(inputs, input_type=input_type, settings=settings)
            finish(result)
            return result

    @contextmanager
    def _instrument(
        self,
        inputs: list[str],
        input_type: EmbedInputType,
        settings: EmbeddingSettings | None,
    ) -> Iterator[Callable[[EmbeddingResult], None]]:
        operation = 'embeddings'
        span_name = f'{operation} {self.model_name}'

        inputs_count = len(inputs)

        attributes: dict[str, AttributeValue] = {
            'gen_ai.operation.name': operation,
            **self.model_attributes(self.wrapped),
            'input_type': input_type,
            'inputs_count': inputs_count,
        }

        if settings:
            attributes['embedding_settings'] = json.dumps(self.serialize_any(settings))

        if self.instrumentation_settings.include_content:
            attributes['inputs'] = json.dumps(inputs)

        attributes['logfire.json_schema'] = json.dumps(
            {
                'type': 'object',
                'properties': {
                    'input_type': {'type': 'string'},
                    'inputs_count': {'type': 'integer'},
                    'embedding_settings': {'type': 'object'},
                    **(
                        {'inputs': {'type': ['array']}, 'embeddings': {'type': 'array'}}
                        if self.instrumentation_settings.include_content
                        else {}
                    ),
                },
            }
        )

        record_metrics: Callable[[], None] | None = None
        try:
            with self.instrumentation_settings.tracer.start_as_current_span(span_name, attributes=attributes) as span:

                def finish(result: EmbeddingResult):
                    # Prepare metric recording closure first so metrics are recorded
                    # even if the span is not recording.
                    provider_name = attributes[GEN_AI_PROVIDER_NAME_ATTRIBUTE]
                    request_model = attributes[GEN_AI_REQUEST_MODEL_ATTRIBUTE]
                    response_model = result.model_name or request_model
                    price_calculation = None

                    def _record_metrics():
                        token_attributes = {
                            GEN_AI_PROVIDER_NAME_ATTRIBUTE: provider_name,
                            'gen_ai.operation.name': operation,
                            GEN_AI_REQUEST_MODEL_ATTRIBUTE: request_model,
                            'gen_ai.response.model': response_model,
                            'gen_ai.token.type': 'input',
                        }
                        tokens = result.usage.input_tokens or 0
                        if tokens:  # pragma: no branch
                            self.instrumentation_settings.tokens_histogram.record(tokens, token_attributes)
                            if price_calculation is not None:
                                self.instrumentation_settings.cost_histogram.record(
                                    float(getattr(price_calculation, 'input_price', 0.0)),
                                    token_attributes,
                                )

                    nonlocal record_metrics
                    record_metrics = _record_metrics

                    if not span.is_recording():
                        return  # pragma: lax no cover

                    attributes_to_set: dict[str, AttributeValue] = {
                        **result.usage.opentelemetry_attributes(),
                        'gen_ai.response.model': response_model,
                    }

                    try:
                        price_calculation = result.cost()
                    except LookupError:
                        # The cost of this provider/model is unknown, which is common.
                        pass
                    except Exception as e:  # pragma: no cover
                        warnings.warn(
                            f'Failed to get cost from response: {type(e).__name__}: {e}', CostCalculationFailedWarning
                        )
                    else:
                        attributes_to_set['operation.cost'] = float(price_calculation.total_price)

                    embeddings = result.embeddings
                    if embeddings:  # pragma: no branch
                        attributes_to_set['gen_ai.embeddings.dimension.count'] = len(embeddings[0])
                        if self.instrumentation_settings.include_content:
                            attributes['embeddings'] = json.dumps(embeddings)

                    if result.provider_response_id is not None:
                        attributes_to_set['gen_ai.response.id'] = result.provider_response_id

                    span.set_attributes(attributes_to_set)

                yield finish
        finally:
            if record_metrics:  # pragma: no branch
                # Record metrics after the span finishes to avoid duplication.
                record_metrics()

    @staticmethod
    def model_attributes(model: EmbeddingModel) -> dict[str, AttributeValue]:
        attributes: dict[str, AttributeValue] = {
            GEN_AI_PROVIDER_NAME_ATTRIBUTE: model.system,
            GEN_AI_REQUEST_MODEL_ATTRIBUTE: model.model_name,
        }
        if base_url := model.base_url:
            try:
                parsed = urlparse(base_url)
            except Exception:  # pragma: no cover
                pass
            else:
                if parsed.hostname:  # pragma: no branch
                    attributes['server.address'] = parsed.hostname
                if parsed.port:
                    attributes['server.port'] = parsed.port  # pragma: no cover

        return attributes

    @staticmethod
    def serialize_any(value: Any) -> str:
        try:
            return ANY_ADAPTER.dump_python(value, mode='json')
        except Exception:  # pragma: no cover
            try:
                return str(value)
            except Exception as e:
                return f'Unable to serialize: {e}'

```

---|---
####  instrumentation_settings `instance-attribute`
```
instrumentation_settings: InstrumentationSettings[](https://ai.pydantic.dev/api/models/instrumented/#pydantic_ai.models.instrumented.InstrumentationSettings "InstrumentationSettings



      dataclass
   \(pydantic_ai.models.instrumented.InstrumentationSettings\)") = (
    options or InstrumentationSettings[](https://ai.pydantic.dev/api/models/instrumented/#pydantic_ai.models.instrumented.InstrumentationSettings "InstrumentationSettings



      dataclass
   \(pydantic_ai.models.instrumented.InstrumentationSettings\)")()
)

```

Instrumentation settings for this model.
###  instrument_embedding_model
```
instrument_embedding_model(
    model: EmbeddingModel[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.base.EmbeddingModel "EmbeddingModel \(pydantic_ai.embeddings.base.EmbeddingModel\)"),
    instrument: InstrumentationSettings[](https://ai.pydantic.dev/api/models/instrumented/#pydantic_ai.models.instrumented.InstrumentationSettings "InstrumentationSettings



      dataclass
   \(pydantic_ai.models.instrumented.InstrumentationSettings\)") | ,
) -> EmbeddingModel[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.base.EmbeddingModel "EmbeddingModel \(pydantic_ai.embeddings.base.EmbeddingModel\)")

```

Instrument an embedding model with OpenTelemetry/logfire.
Source code in `pydantic_ai_slim/pydantic_ai/embeddings/instrumented.py`
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
```
| ```
def instrument_embedding_model(model: EmbeddingModel, instrument: InstrumentationSettings | bool) -> EmbeddingModel:
    """Instrument an embedding model with OpenTelemetry/logfire."""
    if instrument and not isinstance(model, InstrumentedEmbeddingModel):
        if instrument is True:
            instrument = InstrumentationSettings()

        model = InstrumentedEmbeddingModel(model, instrument)

    return model

```

---|---
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
