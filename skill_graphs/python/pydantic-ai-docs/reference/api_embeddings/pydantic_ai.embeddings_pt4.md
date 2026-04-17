


      module-attribute
   \(pydantic_ai.embeddings.KnownEmbeddingModelName\)") | Unset` |  The embedding model to use within this context. |  `UNSET`
Example:
```
from pydantic_ai import Embedder

embedder = Embedder('openai:text-embedding-3-small')


async def main():
    # Temporarily use a different model
    with embedder.override(model='openai:text-embedding-3-large'):
        result = await embedder.embed_query('test')
        print(len(result.embeddings[0]))  # 3072 dimensions for large model
        #> 3072

```

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/__init__.py`
```
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
249
250
251
252
253
254
255
256
257
```
| ```
@contextmanager
def override(
    self,
    *,
    model: EmbeddingModel | KnownEmbeddingModelName | str | _utils.Unset = _utils.UNSET,
) -> Iterator[None]:
    """Context manager to temporarily override the embedding model.

    Useful for testing or dynamically switching models.

    Args:
        model: The embedding model to use within this context.

    Example:
```python
    from pydantic_ai import Embedder

    embedder = Embedder('openai:text-embedding-3-small')


    async def main():
        # Temporarily use a different model
        with embedder.override(model='openai:text-embedding-3-large'):
            result = await embedder.embed_query('test')
            print(len(result.embeddings[0]))  # 3072 dimensions for large model
            #> 3072
```
    """
    if _utils.is_set(model):
        model_token = self._override_model.set(infer_embedding_model(model))
    else:
        model_token = None

    try:
        yield
    finally:
        if model_token is not None:
            self._override_model.reset(model_token)

```

---|---
####  embed_query `async`
```
embed_query(
    query:  | [],
    *,
    settings: EmbeddingSettings[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.settings.EmbeddingSettings "EmbeddingSettings \(pydantic_ai.embeddings.settings.EmbeddingSettings\)") | None = None
) -> EmbeddingResult[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.result.EmbeddingResult "EmbeddingResult



      dataclass
   \(pydantic_ai.embeddings.result.EmbeddingResult\)")

```

Embed one or more query texts.
Use this method when embedding search queries that will be compared against document embeddings. Some models optimize embeddings differently based on whether the input is a query or document.
Parameters:
Name | Type | Description | Default
---|---|---|---
`query` |  |  A single query string or sequence of query strings to embed. |  _required_
`settings` |  `EmbeddingSettings[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.settings.EmbeddingSettings "EmbeddingSettings \(pydantic_ai.embeddings.settings.EmbeddingSettings\)") | None` |  Optional settings to override the embedder's default settings for this call. |  `None`
Returns:
Type | Description
---|---
`EmbeddingResult[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.result.EmbeddingResult "EmbeddingResult



      dataclass
   \(pydantic_ai.embeddings.result.EmbeddingResult\)")` |  An [`EmbeddingResult`](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.EmbeddingResult "EmbeddingResult



      dataclass
  ") containing the embeddings
`EmbeddingResult[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.result.EmbeddingResult "EmbeddingResult



      dataclass
   \(pydantic_ai.embeddings.result.EmbeddingResult\)")` |  and metadata about the operation.
Source code in `pydantic_ai_slim/pydantic_ai/embeddings/__init__.py`
```
259
260
261
262
263
264
265
266
267
268
269
270
271
272
273
274
275
```
| ```
async def embed_query(
    self, query: str | Sequence[str], *, settings: EmbeddingSettings | None = None
) -> EmbeddingResult:
    """Embed one or more query texts.

    Use this method when embedding search queries that will be compared against document embeddings.
    Some models optimize embeddings differently based on whether the input is a query or document.

    Args:
        query: A single query string or sequence of query strings to embed.
        settings: Optional settings to override the embedder's default settings for this call.

    Returns:
        An [`EmbeddingResult`][pydantic_ai.embeddings.EmbeddingResult] containing the embeddings
        and metadata about the operation.
    """
    return await self.embed(query, input_type='query', settings=settings)

```

---|---
####  embed_documents `async`
```
embed_documents(
    documents:  | [],
    *,
    settings: EmbeddingSettings[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.settings.EmbeddingSettings "EmbeddingSettings \(pydantic_ai.embeddings.settings.EmbeddingSettings\)") | None = None
) -> EmbeddingResult[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.result.EmbeddingResult "EmbeddingResult



      dataclass
   \(pydantic_ai.embeddings.result.EmbeddingResult\)")

```

Embed one or more document texts.
Use this method when embedding documents that will be stored and later searched against. Some models optimize embeddings differently based on whether the input is a query or document.
Parameters:
Name | Type | Description | Default
---|---|---|---
`documents` |  |  A single document string or sequence of document strings to embed. |  _required_
`settings` |  `EmbeddingSettings[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.settings.EmbeddingSettings "EmbeddingSettings \(pydantic_ai.embeddings.settings.EmbeddingSettings\)") | None` |  Optional settings to override the embedder's default settings for this call. |  `None`
Returns:
Type | Description
---|---
`EmbeddingResult[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.result.EmbeddingResult "EmbeddingResult



      dataclass
   \(pydantic_ai.embeddings.result.EmbeddingResult\)")` |  An [`EmbeddingResult`](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.EmbeddingResult "EmbeddingResult



      dataclass
  ") containing the embeddings
`EmbeddingResult[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.result.EmbeddingResult "EmbeddingResult



      dataclass
   \(pydantic_ai.embeddings.result.EmbeddingResult\)")` |  and metadata about the operation.
Source code in `pydantic_ai_slim/pydantic_ai/embeddings/__init__.py`
```
277
278
279
280
281
282
283
284
285
286
287
288
289
290
291
292
293
```
| ```
async def embed_documents(
    self, documents: str | Sequence[str], *, settings: EmbeddingSettings | None = None
) -> EmbeddingResult:
    """Embed one or more document texts.

    Use this method when embedding documents that will be stored and later searched against.
    Some models optimize embeddings differently based on whether the input is a query or document.

    Args:
        documents: A single document string or sequence of document strings to embed.
        settings: Optional settings to override the embedder's default settings for this call.

    Returns:
        An [`EmbeddingResult`][pydantic_ai.embeddings.EmbeddingResult] containing the embeddings
        and metadata about the operation.
    """
    return await self.embed(documents, input_type='document', settings=settings)

```

---|---
####  embed `async`
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

Embed text inputs with explicit input type specification.
This is the low-level embedding method. For most use cases, prefer [`embed_query()`](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.Embedder.embed_query "embed_query



      async
  ") or [`embed_documents()`](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.Embedder.embed_documents "embed_documents



      async
  ").
Parameters:
Name | Type | Description | Default
---|---|---|---
`inputs` |  |  A single string or sequence of strings to embed. |  _required_
`input_type` |  `EmbedInputType[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.result.EmbedInputType "EmbedInputType



      module-attribute
   \(pydantic_ai.embeddings.result.EmbedInputType\)")` |  The type of input, either `'query'` or `'document'`. |  _required_
`settings` |  `EmbeddingSettings[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.settings.EmbeddingSettings "EmbeddingSettings \(pydantic_ai.embeddings.settings.EmbeddingSettings\)") | None` |  Optional settings to override the embedder's default settings for this call. |  `None`
Returns:
Type | Description
---|---
`EmbeddingResult[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.result.EmbeddingResult "EmbeddingResult



      dataclass
   \(pydantic_ai.embeddings.result.EmbeddingResult\)")` |  An [`EmbeddingResult`](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.EmbeddingResult "EmbeddingResult



      dataclass
  ") containing the embeddings
`EmbeddingResult[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.result.EmbeddingResult "EmbeddingResult



      dataclass
   \(pydantic_ai.embeddings.result.EmbeddingResult\)")` |  and metadata about the operation.
Source code in `pydantic_ai_slim/pydantic_ai/embeddings/__init__.py`
```
295
296
297
298
299
300
301
302
303
304
305
306
307
308
309
310
311
312
313
314
315
```
| ```
async def embed(
    self, inputs: str | Sequence[str], *, input_type: EmbedInputType, settings: EmbeddingSettings | None = None
) -> EmbeddingResult:
    """Embed text inputs with explicit input type specification.

    This is the low-level embedding method. For most use cases, prefer
    [`embed_query()`][pydantic_ai.embeddings.Embedder.embed_query] or
    [`embed_documents()`][pydantic_ai.embeddings.Embedder.embed_documents].

    Args:
        inputs: A single string or sequence of strings to embed.
        input_type: The type of input, either `'query'` or `'document'`.
        settings: Optional settings to override the embedder's default settings for this call.

    Returns:
        An [`EmbeddingResult`][pydantic_ai.embeddings.EmbeddingResult] containing the embeddings
        and metadata about the operation.
    """
    model = self._get_model()
    settings = merge_embedding_settings(self._settings, settings)
    return await model.embed(inputs, input_type=input_type, settings=settings)

```

---|---
####  max_input_tokens `async`
```
max_input_tokens() ->  | None

```

Get the maximum number of tokens the model can accept as input.
Returns:
Type | Description
---|---
|  The maximum token count, or `None` if the limit is unknown for this model.
Source code in `pydantic_ai_slim/pydantic_ai/embeddings/__init__.py`
```
317
318
319
320
321
322
323
324
```
| ```
async def max_input_tokens(self) -> int | None:
    """Get the maximum number of tokens the model can accept as input.

    Returns:
        The maximum token count, or `None` if the limit is unknown for this model.
    """
    model = self._get_model()
    return await model.max_input_tokens()

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
|  The number of tokens in the text.
Raises:
Type | Description
---|---
|  If the model doesn't support token counting.
`UserError[](https://ai.pydantic.dev/api/exceptions/#pydantic_ai.exceptions.UserError "UserError \(pydantic_ai.exceptions.UserError\)")` |  If the model or tokenizer is not supported.
Source code in `pydantic_ai_slim/pydantic_ai/embeddings/__init__.py`
```
326
327
328
329
330
331
332
333
334
335
336
337
338
339
340
```
| ```
async def count_tokens(self, text: str) -> int:
    """Count the number of tokens in the given text.

    Args:
        text: The text to tokenize and count.

    Returns:
        The number of tokens in the text.

    Raises:
        NotImplementedError: If the model doesn't support token counting.
        UserError: If the model or tokenizer is not supported.
    """
    model = self._get_model()
    return await model.count_tokens(text)

```

---|---
####  embed_query_sync
```
embed_query_sync(
    query:  | [],
    *,
    settings: EmbeddingSettings[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.settings.EmbeddingSettings "EmbeddingSettings \(pydantic_ai.embeddings.settings.EmbeddingSettings\)") | None = None
) -> EmbeddingResult[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.result.EmbeddingResult "EmbeddingResult



      dataclass
   \(pydantic_ai.embeddings.result.EmbeddingResult\)")

```

Synchronous version of [`embed_query()`](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.Embedder.embed_query "embed_query



      async
  ").
Source code in `pydantic_ai_slim/pydantic_ai/embeddings/__init__.py`
```
342
343
344
345
346
```
| ```
def embed_query_sync(
    self, query: str | Sequence[str], *, settings: EmbeddingSettings | None = None
) -> EmbeddingResult:
    """Synchronous version of [`embed_query()`][pydantic_ai.embeddings.Embedder.embed_query]."""
    return _utils.get_event_loop().run_until_complete(self.embed_query(query, settings=settings))

```

---|---
####  embed_documents_sync
```
embed_documents_sync(
    documents:  | [],
    *,
    settings: EmbeddingSettings[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.settings.EmbeddingSettings "EmbeddingSettings \(pydantic_ai.embeddings.settings.EmbeddingSettings\)") | None = None
) -> EmbeddingResult[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.result.EmbeddingResult "EmbeddingResult



      dataclass
   \(pydantic_ai.embeddings.result.EmbeddingResult\)")

```

Synchronous version of [`embed_documents()`](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.Embedder.embed_documents "embed_documents



      async
  ").
Source code in `pydantic_ai_slim/pydantic_ai/embeddings/__init__.py`
```
348
349
350
351
352
```
| ```
def embed_documents_sync(
    self, documents: str | Sequence[str], *, settings: EmbeddingSettings | None = None
) -> EmbeddingResult:
    """Synchronous version of [`embed_documents()`][pydantic_ai.embeddings.Embedder.embed_documents]."""
    return _utils.get_event_loop().run_until_complete(self.embed_documents(documents, settings=settings))

```

---|---
####  embed_sync
```
embed_sync(
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

Synchronous version of [`embed()`](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.Embedder.embed "embed



      async
  ").
Source code in `pydantic_ai_slim/pydantic_ai/embeddings/__init__.py`
```
354
355
356
357
358
```
| ```
def embed_sync(
    self, inputs: str | Sequence[str], *, input_type: EmbedInputType, settings: EmbeddingSettings | None = None
) -> EmbeddingResult:
    """Synchronous version of [`embed()`][pydantic_ai.embeddings.Embedder.embed]."""
    return _utils.get_event_loop().run_until_complete(self.embed(inputs, input_type=input_type, settings=settings))

```

---|---
####  max_input_tokens_sync
```
max_input_tokens_sync() ->  | None

```

Synchronous version of [`max_input_tokens()`](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.Embedder.max_input_tokens "max_input_tokens



      async
  ").
Source code in `pydantic_ai_slim/pydantic_ai/embeddings/__init__.py`
```
360
361
362
```
| ```
def max_input_tokens_sync(self) -> int | None:
    """Synchronous version of [`max_input_tokens()`][pydantic_ai.embeddings.Embedder.max_input_tokens]."""
    return _utils.get_event_loop().run_until_complete(self.max_input_tokens())

```

---|---
####  count_tokens_sync
```
count_tokens_sync(text: ) ->

```

Synchronous version of [`count_tokens()`](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.Embedder.count_tokens "count_tokens



      async
  ").
Source code in `pydantic_ai_slim/pydantic_ai/embeddings/__init__.py`
```
364
365
366
```
| ```
def count_tokens_sync(self, text: str) -> int:
    """Synchronous version of [`count_tokens()`][pydantic_ai.embeddings.Embedder.count_tokens]."""
    return _utils.get_event_loop().run_until_complete(self.count_tokens(text))

```

---|---
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
