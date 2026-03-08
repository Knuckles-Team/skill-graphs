```
sentence_transformers_normalize_embeddings:

```

Whether to L2-normalize embeddings.
When `True`, all embeddings will have unit length, which is useful for cosine similarity calculations.
####  sentence_transformers_batch_size `instance-attribute`
```
sentence_transformers_batch_size:

```

Batch size to use during encoding.
Larger batches may be faster but require more memory.
###  SentenceTransformerEmbeddingModel `dataclass`
Bases: `EmbeddingModel[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.base.EmbeddingModel "EmbeddingModel \(pydantic_ai.embeddings.base.EmbeddingModel\)")`
Local embedding model using the `sentence-transformers` library.
This model runs embeddings locally on your machine, which is useful for:
  * Privacy-sensitive applications where data shouldn't leave your infrastructure
  * Reducing API costs for high-volume embedding workloads
  * Offline or air-gapped environments


Models are downloaded from Hugging Face on first use. See the
Example:
```
from sentence_transformers import SentenceTransformer

from pydantic_ai.embeddings.sentence_transformers import (
    SentenceTransformerEmbeddingModel,
)

# Using a model name (downloads from Hugging Face)
model = SentenceTransformerEmbeddingModel('all-MiniLM-L6-v2')

# Using an existing SentenceTransformer instance
st_model = SentenceTransformer('all-MiniLM-L6-v2')
model = SentenceTransformerEmbeddingModel(st_model)

```

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/sentence_transformers.py`
```
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
```
| ```
@dataclass(init=False)
class SentenceTransformerEmbeddingModel(EmbeddingModel):
    """Local embedding model using the `sentence-transformers` library.

    This model runs embeddings locally on your machine, which is useful for:

    - Privacy-sensitive applications where data shouldn't leave your infrastructure
    - Reducing API costs for high-volume embedding workloads
    - Offline or air-gapped environments

    Models are downloaded from Hugging Face on first use.
    See the [Sentence-Transformers documentation](https://www.sbert.net/docs/sentence_transformer/pretrained_models.html)
    for available models.

    Example:
```python {max_py="3.13"}
    from sentence_transformers import SentenceTransformer

    from pydantic_ai.embeddings.sentence_transformers import (
        SentenceTransformerEmbeddingModel,
    )

    # Using a model name (downloads from Hugging Face)
    model = SentenceTransformerEmbeddingModel('all-MiniLM-L6-v2')

    # Using an existing SentenceTransformer instance
    st_model = SentenceTransformer('all-MiniLM-L6-v2')
    model = SentenceTransformerEmbeddingModel(st_model)
```
    """

    _model_name: str = field(repr=False)
    _model: SentenceTransformer | None = field(repr=False, default=None)

    def __init__(self, model: SentenceTransformer | str, *, settings: EmbeddingSettings | None = None) -> None:
        """Initialize a Sentence-Transformers embedding model.

        Args:
            model: The model to use. Can be:

                - A model name from Hugging Face (e.g., `'all-MiniLM-L6-v2'`)
                - A local path to a saved model
                - An existing `SentenceTransformer` instance
            settings: Model-specific
                [`SentenceTransformersEmbeddingSettings`][pydantic_ai.embeddings.sentence_transformers.SentenceTransformersEmbeddingSettings]
                to use as defaults for this model.
        """
        if isinstance(model, str):
            self._model_name = model
        else:
            self._model = deepcopy(model)
            self._model_name = model.model_card_data.model_id or model.model_card_data.base_model or 'unknown'

        super().__init__(settings=settings)

    @property
    def base_url(self) -> str | None:
        """No base URL — runs locally."""
        return None

    @property
    def model_name(self) -> str:
        """The embedding model name."""
        return self._model_name

    @property
    def system(self) -> str:
        """The embedding model provider/system identifier."""
        return 'sentence-transformers'

    async def embed(
        self, inputs: str | Sequence[str], *, input_type: EmbedInputType, settings: EmbeddingSettings | None = None
    ) -> EmbeddingResult:
        inputs, settings = self.prepare_embed(inputs, settings)
        settings = cast(SentenceTransformersEmbeddingSettings, settings)

        device = settings.get('sentence_transformers_device', None)
        normalize = settings.get('sentence_transformers_normalize_embeddings', False)
        batch_size = settings.get('sentence_transformers_batch_size', None)
        dimensions = settings.get('dimensions', None)

        model = await self._get_model()
        encode_func = model.encode_query if input_type == 'query' else model.encode_document  # type: ignore[reportUnknownReturnType]

        np_embeddings: np.ndarray[Any, float] = await _utils.run_in_executor(  # type: ignore[reportAssignmentType]
            encode_func,  # type: ignore[reportArgumentType]
            inputs,
            show_progress_bar=False,
            convert_to_numpy=True,
            convert_to_tensor=False,
            device=device,
            normalize_embeddings=normalize,
            truncate_dim=dimensions,
            **{'batch_size': batch_size} if batch_size is not None else {},  # type: ignore[reportArgumentType]
        )
        embeddings = np_embeddings.tolist()

        return EmbeddingResult(
            embeddings=embeddings,
            inputs=inputs,
            input_type=input_type,
            model_name=self.model_name,
            provider_name=self.system,
        )

    async def max_input_tokens(self) -> int | None:
        model = await self._get_model()
        return model.get_max_seq_length()

    async def count_tokens(self, text: str) -> int:
        model = await self._get_model()
        result: dict[str, torch.Tensor] = await _utils.run_in_executor(
            model.tokenize,  # type: ignore[reportArgumentType]
            [text],
        )
        if 'input_ids' not in result or not isinstance(result['input_ids'], torch.Tensor):  # pragma: no cover
            raise UnexpectedModelBehavior(
                'The SentenceTransformers tokenizer output did not have an `input_ids` field holding a tensor',
                str(result),
            )
        return len(result['input_ids'][0])

    async def _get_model(self) -> SentenceTransformer:
        if self._model is None:
            # This may download the model from Hugging Face, so we do it in a thread
            self._model = await _utils.run_in_executor(SentenceTransformer, self.model_name)  # pragma: no cover
        return self._model

```

---|---
####  __init__
```
__init__(
    model: SentenceTransformer | ,
    *,
    settings: EmbeddingSettings[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.settings.EmbeddingSettings "EmbeddingSettings \(pydantic_ai.embeddings.settings.EmbeddingSettings\)") | None = None
) -> None

```

Initialize a Sentence-Transformers embedding model.
Parameters:
Name | Type | Description | Default
---|---|---|---
`model` |  `SentenceTransformer | ` |  The model to use. Can be:
  * A model name from Hugging Face (e.g., `'all-MiniLM-L6-v2'`)
  * A local path to a saved model
  * An existing `SentenceTransformer` instance

|  _required_
`settings` |  `EmbeddingSettings[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.settings.EmbeddingSettings "EmbeddingSettings \(pydantic_ai.embeddings.settings.EmbeddingSettings\)") | None` |  Model-specific [`SentenceTransformersEmbeddingSettings`](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.sentence_transformers.SentenceTransformersEmbeddingSettings "SentenceTransformersEmbeddingSettings") to use as defaults for this model. |  `None`
Source code in `pydantic_ai_slim/pydantic_ai/embeddings/sentence_transformers.py`
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
```
| ```
def __init__(self, model: SentenceTransformer | str, *, settings: EmbeddingSettings | None = None) -> None:
    """Initialize a Sentence-Transformers embedding model.

    Args:
        model: The model to use. Can be:

            - A model name from Hugging Face (e.g., `'all-MiniLM-L6-v2'`)
            - A local path to a saved model
            - An existing `SentenceTransformer` instance
        settings: Model-specific
            [`SentenceTransformersEmbeddingSettings`][pydantic_ai.embeddings.sentence_transformers.SentenceTransformersEmbeddingSettings]
            to use as defaults for this model.
    """
    if isinstance(model, str):
        self._model_name = model
    else:
        self._model = deepcopy(model)
        self._model_name = model.model_card_data.model_id or model.model_card_data.base_model or 'unknown'

    super().__init__(settings=settings)

```

---|---
####  base_url `property`
```
base_url:  | None

```

No base URL — runs locally.
####  model_name `property`
```
model_name:

```

The embedding model name.
####  system `property`
```
system:

```

The embedding model provider/system identifier.
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
####  last_settings `class-attribute` `instance-attribute`
```
last_settings: EmbeddingSettings[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.settings.EmbeddingSettings "EmbeddingSettings \(pydantic_ai.embeddings.settings.EmbeddingSettings\)") | None = None

```

The settings used in the most recent embed call.
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
####  wrapped `instance-attribute`
```
wrapped: EmbeddingModel[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.base.EmbeddingModel "EmbeddingModel \(pydantic_ai.embeddings.base.EmbeddingModel\)") = (
    infer_embedding_model[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.infer_embedding_model "infer_embedding_model \(pydantic_ai.embeddings.infer_embedding_model\)")(wrapped)
    if (wrapped, )
    else wrapped
)

```

The underlying embedding model being wrapped.
####  settings `property`
```
settings: EmbeddingSettings[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.settings.EmbeddingSettings "EmbeddingSettings \(pydantic_ai.embeddings.settings.EmbeddingSettings\)") | None

```

Get the settings from the wrapped embedding model.
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
