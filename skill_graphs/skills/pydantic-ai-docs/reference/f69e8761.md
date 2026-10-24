# Using explicit credentials
model = BedrockEmbeddingModel(
    'cohere.embed-english-v3',
    provider=BedrockProvider(
        region_name='us-east-1',
        aws_access_key_id='...',
        aws_secret_access_key='...',
    ),
)

```

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/bedrock.py`
```
482
483
484
485
486
487
488
489
490
491
492
493
494
495
496
497
498
499
500
501
502
503
504
505
506
507
508
509
510
511
512
513
514
515
516
517
518
519
520
521
522
523
524
525
526
527
528
529
530
531
532
533
534
535
536
537
538
539
540
541
542
543
544
545
546
547
548
549
550
551
552
553
554
555
556
557
558
559
560
561
562
563
564
565
566
567
568
569
570
571
572
573
574
575
576
577
578
579
580
581
582
583
584
585
586
587
588
589
590
591
592
593
594
595
596
597
598
599
600
601
602
603
604
605
606
607
608
609
610
611
612
613
614
615
616
617
618
619
620
621
622
623
624
625
626
627
628
629
630
631
632
633
634
635
636
637
638
639
640
641
642
643
644
645
646
647
648
649
650
651
652
653
654
655
656
657
658
659
660
661
662
663
```
| ```
@dataclass(init=False)
class BedrockEmbeddingModel(EmbeddingModel):
    """Bedrock embedding model implementation.

    This model works with AWS Bedrock's embedding models including
    Amazon Titan Embeddings and Cohere Embed models.

    Example:
```python
    from pydantic_ai.embeddings.bedrock import BedrockEmbeddingModel
    from pydantic_ai.providers.bedrock import BedrockProvider

    # Using default AWS credentials
    model = BedrockEmbeddingModel('amazon.titan-embed-text-v2:0')

    # Using explicit credentials
    model = BedrockEmbeddingModel(
        'cohere.embed-english-v3',
        provider=BedrockProvider(
            region_name='us-east-1',
            aws_access_key_id='...',
            aws_secret_access_key='...',
        ),
    )
```
    """

    client: BedrockRuntimeClient

    _model_name: BedrockEmbeddingModelName = field(repr=False)
    _provider: Provider[BaseClient] = field(repr=False)
    _handler: _BedrockEmbeddingHandler = field(repr=False)

    def __init__(
        self,
        model_name: BedrockEmbeddingModelName,
        *,
        provider: Literal['bedrock'] | Provider[BaseClient] = 'bedrock',
        settings: EmbeddingSettings | None = None,
    ):
        """Initialize a Bedrock embedding model.

        Args:
            model_name: The name of the Bedrock embedding model to use.
                See [Bedrock embedding models](https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html)
                for available options.
            provider: The provider to use for authentication and API access. Can be:

                - `'bedrock'` (default): Uses default AWS credentials
                - A [`BedrockProvider`][pydantic_ai.providers.bedrock.BedrockProvider] instance
                  for custom configuration

            settings: Model-specific [`EmbeddingSettings`][pydantic_ai.embeddings.EmbeddingSettings]
                to use as defaults for this model.
        """
        self._model_name = model_name

        if isinstance(provider, str):
            provider = infer_provider(provider)
        self._provider = provider
        self.client = cast('BedrockRuntimeClient', provider.client)
        self._handler = _get_handler_for_model(model_name)

        super().__init__(settings=settings)

    @property
    def base_url(self) -> str:
        """The base URL for the provider API."""
        return str(self.client.meta.endpoint_url)

    @property
    def model_name(self) -> BedrockEmbeddingModelName:
        """The embedding model name."""
        return self._model_name

    @property
    def system(self) -> str:
        """The embedding model provider."""
        return self._provider.name

    async def embed(
        self, inputs: str | Sequence[str], *, input_type: EmbedInputType, settings: EmbeddingSettings | None = None
    ) -> EmbeddingResult:
        inputs_list, settings_dict = self.prepare_embed(inputs, settings)
        settings_typed = cast(BedrockEmbeddingSettings, settings_dict)

        if self._handler.supports_batch:
            # Models like Cohere support batch requests
            return await self._embed_batch(inputs_list, input_type, settings_typed)
        else:
            # Models like Titan require individual requests
            return await self._embed_concurrent(inputs_list, input_type, settings_typed)

    async def _embed_batch(
        self,
        inputs: list[str],
        input_type: EmbedInputType,
        settings: BedrockEmbeddingSettings,
    ) -> EmbeddingResult:
        """Embed all inputs in a single batch request."""
        body = self._handler.prepare_request(inputs, input_type, settings)
        response, input_tokens = await self._invoke_model(body)
        embeddings, response_id = self._handler.parse_response(response)

        return EmbeddingResult(
            embeddings=embeddings,
            inputs=inputs,
            input_type=input_type,
            usage=RequestUsage(input_tokens=input_tokens),
            model_name=self.model_name,
            provider_name=self.system,
            provider_response_id=response_id,
        )

    async def _embed_concurrent(
        self,
        inputs: list[str],
        input_type: EmbedInputType,
        settings: BedrockEmbeddingSettings,
    ) -> EmbeddingResult:
        """Embed inputs concurrently with controlled parallelism and combine results."""
        max_concurrency = settings.get('bedrock_max_concurrency', 5)
        semaphore = anyio.Semaphore(max_concurrency)

        results: list[tuple[Sequence[float], int]] = [None] * len(inputs)  # type: ignore[list-item]

        async def embed_single(index: int, text: str) -> None:
            async with semaphore:
                body = self._handler.prepare_request([text], input_type, settings)
                response, input_tokens = await self._invoke_model(body)
                embeddings, _ = self._handler.parse_response(response)
                results[index] = (embeddings[0], input_tokens)

        async with anyio.create_task_group() as tg:
            for i, text in enumerate(inputs):
                tg.start_soon(embed_single, i, text)

        all_embeddings = [embedding for embedding, _ in results]
        total_input_tokens = sum(tokens for _, tokens in results)

        return EmbeddingResult(
            embeddings=all_embeddings,
            inputs=inputs,
            input_type=input_type,
            usage=RequestUsage(input_tokens=total_input_tokens),
            model_name=self.model_name,
            provider_name=self.system,
        )

    async def _invoke_model(self, body: dict[str, Any]) -> tuple[dict[str, Any], int]:
        """Invoke the Bedrock model and return parsed response with token count.

        Returns:
            A tuple of (response_body, input_token_count).
        """
        try:
            response: InvokeModelResponseTypeDef = await anyio.to_thread.run_sync(
                functools.partial(
                    self.client.invoke_model,
                    modelId=self._model_name,
                    body=json.dumps(body),
                    contentType='application/json',
                    accept='application/json',
                )
            )
        except ClientError as e:
            status_code = e.response.get('ResponseMetadata', {}).get('HTTPStatusCode')
            if isinstance(status_code, int):
                raise ModelHTTPError(status_code=status_code, model_name=self.model_name, body=e.response) from e
            raise ModelAPIError(model_name=self.model_name, message=str(e)) from e

        # Extract input token count from HTTP headers
        input_tokens = int(
            response.get('ResponseMetadata', {}).get('HTTPHeaders', {}).get('x-amzn-bedrock-input-token-count', '0')
        )

        response_body = json.loads(response['body'].read())
        return response_body, input_tokens

    async def max_input_tokens(self) -> int | None:
        """Get the maximum number of tokens that can be input to the model."""
        return _MAX_INPUT_TOKENS.get(self._handler.model_name, None)

```

---|---
####  __init__
```
__init__(
    model_name: BedrockEmbeddingModelName[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.bedrock.BedrockEmbeddingModelName "BedrockEmbeddingModelName



      module-attribute
   \(pydantic_ai.embeddings.bedrock.BedrockEmbeddingModelName\)"),
    *,
    provider: (
        ["bedrock"] | Provider[](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.Provider "pydantic_ai.providers.Provider")[BaseClient]
    ) = "bedrock",
    settings: EmbeddingSettings[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.settings.EmbeddingSettings "EmbeddingSettings \(pydantic_ai.embeddings.settings.EmbeddingSettings\)") | None = None
)

```

Initialize a Bedrock embedding model.
Parameters:
Name | Type | Description | Default
---|---|---|---
`model_name` |  `BedrockEmbeddingModelName[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.bedrock.BedrockEmbeddingModelName "BedrockEmbeddingModelName



      module-attribute
   \(pydantic_ai.embeddings.bedrock.BedrockEmbeddingModelName\)")` |  The name of the Bedrock embedding model to use. See  |  _required_
`provider` |  `Provider[](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.Provider "pydantic_ai.providers.Provider")[BaseClient]` |  The provider to use for authentication and API access. Can be:
  * `'bedrock'` (default): Uses default AWS credentials
  * A [`BedrockProvider`](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.bedrock.BedrockProvider "BedrockProvider") instance for custom configuration

|  `'bedrock'`
`settings` |  `EmbeddingSettings[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.settings.EmbeddingSettings "EmbeddingSettings \(pydantic_ai.embeddings.settings.EmbeddingSettings\)") | None` |  Model-specific [`EmbeddingSettings`](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.EmbeddingSettings "EmbeddingSettings") to use as defaults for this model. |  `None`
Source code in `pydantic_ai_slim/pydantic_ai/embeddings/bedrock.py`
```
515
516
517
518
519
520
521
522
523
524
525
526
527
528
529
530
531
532
533
534
535
536
537
538
539
540
541
542
543
544
545
```
| ```
def __init__(
    self,
    model_name: BedrockEmbeddingModelName,
    *,
    provider: Literal['bedrock'] | Provider[BaseClient] = 'bedrock',
    settings: EmbeddingSettings | None = None,
):
    """Initialize a Bedrock embedding model.

    Args:
        model_name: The name of the Bedrock embedding model to use.
            See [Bedrock embedding models](https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html)
            for available options.
        provider: The provider to use for authentication and API access. Can be:

            - `'bedrock'` (default): Uses default AWS credentials
            - A [`BedrockProvider`][pydantic_ai.providers.bedrock.BedrockProvider] instance
              for custom configuration

        settings: Model-specific [`EmbeddingSettings`][pydantic_ai.embeddings.EmbeddingSettings]
            to use as defaults for this model.
    """
    self._model_name = model_name

    if isinstance(provider, str):
        provider = infer_provider(provider)
    self._provider = provider
    self.client = cast('BedrockRuntimeClient', provider.client)
    self._handler = _get_handler_for_model(model_name)

    super().__init__(settings=settings)

```

---|---
####  base_url `property`
```
base_url:

```

The base URL for the provider API.
####  model_name `property`
```
model_name: BedrockEmbeddingModelName[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.bedrock.BedrockEmbeddingModelName "BedrockEmbeddingModelName



      module-attribute
   \(pydantic_ai.embeddings.bedrock.BedrockEmbeddingModelName\)")

```

The embedding model name.
####  system `property`
```
system:

```

The embedding model provider.
####  max_input_tokens `async`
```
max_input_tokens() ->  | None

```

Get the maximum number of tokens that can be input to the model.
Source code in `pydantic_ai_slim/pydantic_ai/embeddings/bedrock.py`
```
661
662
663
```
| ```
async def max_input_tokens(self) -> int | None:
    """Get the maximum number of tokens that can be input to the model."""
    return _MAX_INPUT_TOKENS.get(self._handler.model_name, None)

```

---|---
###  LatestVoyageAIEmbeddingModelNames `module-attribute`
```
LatestVoyageAIEmbeddingModelNames = [
    "voyage-4-large",
    "voyage-4",
    "voyage-4-lite",
    "voyage-3-large",
    "voyage-3.5",
    "voyage-3.5-lite",
    "voyage-code-3",
    "voyage-finance-2",
    "voyage-law-2",
    "voyage-code-2",
]

```

Latest VoyageAI embedding models.
See
###  VoyageAIEmbeddingModelName `module-attribute`
```
VoyageAIEmbeddingModelName = (
     | LatestVoyageAIEmbeddingModelNames[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.voyageai.LatestVoyageAIEmbeddingModelNames "LatestVoyageAIEmbeddingModelNames



      module-attribute
   \(pydantic_ai.embeddings.voyageai.LatestVoyageAIEmbeddingModelNames\)")
)

```

Possible VoyageAI embedding model names.
###  VoyageAIEmbedInputType `module-attribute`
```
VoyageAIEmbedInputType = [
    "query", "document", "none"
]

```

VoyageAI embedding input types.
  * `'query'`: For search queries; prepends retrieval-optimized prefix.
  * `'document'`: For documents; prepends document retrieval prefix.
  * `'none'`: Direct embedding without any prefix.


###  VoyageAIEmbeddingSettings
Bases: `EmbeddingSettings[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.settings.EmbeddingSettings "EmbeddingSettings \(pydantic_ai.embeddings.settings.EmbeddingSettings\)")`
Settings used for a VoyageAI embedding model request.
All fields from [`EmbeddingSettings`](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.EmbeddingSettings "EmbeddingSettings") are supported, plus VoyageAI-specific settings prefixed with `voyageai_`.
Source code in `pydantic_ai_slim/pydantic_ai/embeddings/voyageai.py`
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
```
| ```
class VoyageAIEmbeddingSettings(EmbeddingSettings, total=False):
    """Settings used for a VoyageAI embedding model request.

    All fields from [`EmbeddingSettings`][pydantic_ai.embeddings.EmbeddingSettings] are supported,
    plus VoyageAI-specific settings prefixed with `voyageai_`.
    """

    # ALL FIELDS MUST BE `voyageai_` PREFIXED SO YOU CAN MERGE THEM WITH OTHER MODELS.

    voyageai_input_type: VoyageAIEmbedInputType
    """The VoyageAI-specific input type for the embedding.

    Overrides the standard `input_type` argument. Options include:
    `'query'`, `'document'`, or `'none'` for direct embedding without prefix.
    """

```

---|---
####  voyageai_input_type `instance-attribute`
```
voyageai_input_type: VoyageAIEmbedInputType[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.voyageai.VoyageAIEmbedInputType "VoyageAIEmbedInputType



      module-attribute
   \(pydantic_ai.embeddings.voyageai.VoyageAIEmbedInputType\)")

```

The VoyageAI-specific input type for the embedding.
Overrides the standard `input_type` argument. Options include: `'query'`, `'document'`, or `'none'` for direct embedding without prefix.
###  VoyageAIEmbeddingModel `dataclass`
Bases: `EmbeddingModel[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.base.EmbeddingModel "EmbeddingModel \(pydantic_ai.embeddings.base.EmbeddingModel\)")`
VoyageAI embedding model implementation.
VoyageAI provides state-of-the-art embedding models optimized for retrieval, with specialized models for code, finance, and legal domains.
Example:
```
from pydantic_ai.embeddings.voyageai import VoyageAIEmbeddingModel

model = VoyageAIEmbeddingModel('voyage-3.5')

```

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/voyageai.py`
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
```
| ```
@dataclass(init=False)
class VoyageAIEmbeddingModel(EmbeddingModel):
    """VoyageAI embedding model implementation.

    VoyageAI provides state-of-the-art embedding models optimized for
    retrieval, with specialized models for code, finance, and legal domains.

    Example:
```python {max_py="3.13"}
    from pydantic_ai.embeddings.voyageai import VoyageAIEmbeddingModel

    model = VoyageAIEmbeddingModel('voyage-3.5')
```
    """

    _model_name: VoyageAIEmbeddingModelName = field(repr=False)
    _provider: Provider[AsyncClient] = field(repr=False)

    def __init__(
        self,
        model_name: VoyageAIEmbeddingModelName,
        *,
        provider: Literal['voyageai'] | Provider[AsyncClient] = 'voyageai',
        settings: EmbeddingSettings | None = None,
    ):
        """Initialize a VoyageAI embedding model.

        Args:
            model_name: The name of the VoyageAI model to use.
                See [VoyageAI models](https://docs.voyageai.com/docs/embeddings)
                for available options.
            provider: The provider to use for authentication and API access. Can be:

                - `'voyageai'` (default): Uses the standard VoyageAI API
                - A [`VoyageAIProvider`][pydantic_ai.providers.voyageai.VoyageAIProvider] instance
                  for custom configuration
            settings: Model-specific [`EmbeddingSettings`][pydantic_ai.embeddings.EmbeddingSettings]
                to use as defaults for this model.
        """
        self._model_name = model_name

        if isinstance(provider, str):
            provider = infer_provider(provider)
        self._provider = provider

        super().__init__(settings=settings)

    @property
    def base_url(self) -> str:
        """The base URL for the provider API."""
        return self._provider.base_url

    @property
    def model_name(self) -> VoyageAIEmbeddingModelName:
        """The embedding model name."""
        return self._model_name

    @property
    def system(self) -> str:
        """The embedding model provider."""
        return self._provider.name

    async def embed(
        self,
        inputs: str | Sequence[str],
        *,
        input_type: EmbedInputType,
        settings: EmbeddingSettings | None = None,
    ) -> EmbeddingResult:
        inputs, settings = self.prepare_embed(inputs, settings)
        settings = cast(VoyageAIEmbeddingSettings, settings)

        voyageai_input_type: VoyageAIEmbedInputType = settings.get(
            'voyageai_input_type', 'document' if input_type == 'document' else 'query'
        )
        # Convert 'none' string to None for the API
        api_input_type = None if voyageai_input_type == 'none' else voyageai_input_type

        try:
            response = await self._provider.client.embed(
                texts=list(inputs),
                model=self.model_name,
                input_type=api_input_type,
                truncation=settings.get('truncate', False),
                output_dimension=settings.get('dimensions'),
            )
        except VoyageError as e:
            raise ModelAPIError(model_name=self.model_name, message=str(e)) from e

        return EmbeddingResult(
            embeddings=response.embeddings,
            inputs=inputs,
            input_type=input_type,
            usage=_map_usage(response.total_tokens),
            model_name=self.model_name,
            provider_name=self.system,
        )

    async def max_input_tokens(self) -> int | None:
        return _MAX_INPUT_TOKENS.get(self.model_name)

```

---|---
####  __init__
```
__init__(
    model_name: VoyageAIEmbeddingModelName[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.voyageai.VoyageAIEmbeddingModelName "VoyageAIEmbeddingModelName



      module-attribute
   \(pydantic_ai.embeddings.voyageai.VoyageAIEmbeddingModelName\)"),
    *,
    provider: (
        ["voyageai"] | Provider[](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.Provider "pydantic_ai.providers.Provider")[AsyncClient]
    ) = "voyageai",
    settings: EmbeddingSettings[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.settings.EmbeddingSettings "EmbeddingSettings \(pydantic_ai.embeddings.settings.EmbeddingSettings\)") | None = None
)

```

Initialize a VoyageAI embedding model.
Parameters:
Name | Type | Description | Default
---|---|---|---
`model_name` |  `VoyageAIEmbeddingModelName[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.voyageai.VoyageAIEmbeddingModelName "VoyageAIEmbeddingModelName



      module-attribute
   \(pydantic_ai.embeddings.voyageai.VoyageAIEmbeddingModelName\)")` |  The name of the VoyageAI model to use. See  |  _required_
`provider` |  `Provider[](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.Provider "pydantic_ai.providers.Provider")[AsyncClient]` |  The provider to use for authentication and API access. Can be:
  * `'voyageai'` (default): Uses the standard VoyageAI API
  * A [`VoyageAIProvider`](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.voyageai.VoyageAIProvider) instance for custom configuration

|  `'voyageai'`
`settings` |  `EmbeddingSettings[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.settings.EmbeddingSettings "EmbeddingSettings \(pydantic_ai.embeddings.settings.EmbeddingSettings\)") | None` |  Model-specific [`EmbeddingSettings`](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.EmbeddingSettings "EmbeddingSettings") to use as defaults for this model. |  `None`
Source code in `pydantic_ai_slim/pydantic_ai/embeddings/voyageai.py`
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
```
| ```
def __init__(
    self,
    model_name: VoyageAIEmbeddingModelName,
    *,
    provider: Literal['voyageai'] | Provider[AsyncClient] = 'voyageai',
    settings: EmbeddingSettings | None = None,
):
    """Initialize a VoyageAI embedding model.

    Args:
        model_name: The name of the VoyageAI model to use.
            See [VoyageAI models](https://docs.voyageai.com/docs/embeddings)
            for available options.
        provider: The provider to use for authentication and API access. Can be:

            - `'voyageai'` (default): Uses the standard VoyageAI API
            - A [`VoyageAIProvider`][pydantic_ai.providers.voyageai.VoyageAIProvider] instance
              for custom configuration
        settings: Model-specific [`EmbeddingSettings`][pydantic_ai.embeddings.EmbeddingSettings]
            to use as defaults for this model.
    """
    self._model_name = model_name

    if isinstance(provider, str):
        provider = infer_provider(provider)
    self._provider = provider

    super().__init__(settings=settings)

```

---|---
####  base_url `property`
```
base_url:

```

The base URL for the provider API.
####  model_name `property`
```
model_name: VoyageAIEmbeddingModelName[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.voyageai.VoyageAIEmbeddingModelName "VoyageAIEmbeddingModelName



      module-attribute
   \(pydantic_ai.embeddings.voyageai.VoyageAIEmbeddingModelName\)")

```

The embedding model name.
####  system `property`
```
system:

```

The embedding model provider.
###  SentenceTransformersEmbeddingSettings
Bases: `EmbeddingSettings[](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.settings.EmbeddingSettings "EmbeddingSettings \(pydantic_ai.embeddings.settings.EmbeddingSettings\)")`
Settings used for a Sentence-Transformers embedding model request.
All fields from [`EmbeddingSettings`](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.EmbeddingSettings "EmbeddingSettings") are supported, plus Sentence-Transformers-specific settings prefixed with `sentence_transformers_`.
Source code in `pydantic_ai_slim/pydantic_ai/embeddings/sentence_transformers.py`
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
```
| ```
class SentenceTransformersEmbeddingSettings(EmbeddingSettings, total=False):
    """Settings used for a Sentence-Transformers embedding model request.

    All fields from [`EmbeddingSettings`][pydantic_ai.embeddings.EmbeddingSettings] are supported,
    plus Sentence-Transformers-specific settings prefixed with `sentence_transformers_`.
    """

    sentence_transformers_device: str
    """Device to run inference on.

    Examples: `'cpu'`, `'cuda'`, `'cuda:0'`, `'mps'` (Apple Silicon).
    """

    sentence_transformers_normalize_embeddings: bool
    """Whether to L2-normalize embeddings.

    When `True`, all embeddings will have unit length, which is useful for
    cosine similarity calculations.
    """

    sentence_transformers_batch_size: int
    """Batch size to use during encoding.

    Larger batches may be faster but require more memory.
    """

```

---|---
####  sentence_transformers_device `instance-attribute`
```
sentence_transformers_device:

```

Device to run inference on.
Examples: `'cpu'`, `'cuda'`, `'cuda:0'`, `'mps'` (Apple Silicon).
####  sentence_transformers_normalize_embeddings `instance-attribute`
