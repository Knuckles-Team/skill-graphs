# `pydantic_ai.models.mistral`
## Setup
For details on how to set up authentication with this model, see [model configuration for Mistral](https://ai.pydantic.dev/models/mistral/).
###  LatestMistralModelNames `module-attribute`
```
LatestMistralModelNames = [
    "mistral-large-latest",
    "mistral-small-latest",
    "codestral-latest",
    "mistral-moderation-latest",
]

```

Latest Mistral models.
###  MistralModelName `module-attribute`
```
MistralModelName =  | LatestMistralModelNames[](https://ai.pydantic.dev/api/models/mistral/#pydantic_ai.models.mistral.LatestMistralModelNames "LatestMistralModelNames



      module-attribute
   \(pydantic_ai.models.mistral.LatestMistralModelNames\)")

```

Possible Mistral model names.
Since Mistral supports a variety of date-stamped models, we explicitly list the most popular models but allow any name in the type hints. Since
###  MistralModelSettings
Bases: `ModelSettings[](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings \(pydantic_ai.settings.ModelSettings\)")`
Settings used for a Mistral model request.
Source code in `pydantic_ai_slim/pydantic_ai/models/mistral.py`
```
115
116
```
| ```
class MistralModelSettings(ModelSettings, total=False):
    """Settings used for a Mistral model request."""

```

---|---
###  MistralModel `dataclass`
Bases: `Model[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.Model "Model \(pydantic_ai.models.Model\)")`
A model that uses Mistral.
Internally, this uses the
Source code in `pydantic_ai_slim/pydantic_ai/models/mistral.py`
```
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
249
250
251
252
253
254
255
256
257
258
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
276
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
294
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
316
317
318
319
320
321
322
323
324
325
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
341
342
343
344
345
346
347
348
349
350
351
352
353
354
355
356
357
358
359
360
361
362
363
364
365
366
367
368
369
370
371
372
373
374
375
376
377
378
379
380
381
382
383
384
385
386
387
388
389
390
391
392
393
394
395
396
397
398
399
400
401
402
403
404
405
406
407
408
409
410
411
412
413
414
415
416
417
418
419
420
421
422
423
424
425
426
427
428
429
430
431
432
433
434
435
436
437
438
439
440
441
442
443
444
445
446
447
448
449
450
451
452
453
454
455
456
457
458
459
460
461
462
463
464
465
466
467
468
469
470
471
472
473
474
475
476
477
478
479
480
481
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
```
| ```
@dataclass(init=False)
class MistralModel(Model):
    """A model that uses Mistral.

    Internally, this uses the [Mistral Python client](https://github.com/mistralai/client-python) to interact with the API.

    [API Documentation](https://docs.mistral.ai/)
    """

    client: Mistral = field(repr=False)
    json_mode_schema_prompt: str

    _model_name: MistralModelName = field(repr=False)
    _provider: Provider[Mistral] = field(repr=False)

    def __init__(
        self,
        model_name: MistralModelName,
        *,
        provider: Literal['mistral'] | Provider[Mistral] = 'mistral',
        profile: ModelProfileSpec | None = None,
        json_mode_schema_prompt: str = """Answer in JSON Object, respect the format:\n```\n{schema}\n```\n""",
        settings: ModelSettings | None = None,
    ):
        """Initialize a Mistral model.

        Args:
            model_name: The name of the model to use.
            provider: The provider to use for authentication and API access. Can be either the string
                'mistral' or an instance of `Provider[Mistral]`. If not provided, a new provider will be
                created using the other parameters.
            profile: The model profile to use. Defaults to a profile picked by the provider based on the model name.
            json_mode_schema_prompt: The prompt to show when the model expects a JSON object as input.
            settings: Model-specific settings that will be used as defaults for this model.
        """
        self._model_name = model_name
        self.json_mode_schema_prompt = json_mode_schema_prompt

        if isinstance(provider, str):
            provider = infer_provider(provider)
        self._provider = provider
        self.client = provider.client

        super().__init__(settings=settings, profile=profile or provider.model_profile)

    @property
    def base_url(self) -> str:
        return self._provider.base_url

    @property
    def model_name(self) -> MistralModelName:
        """The model name."""
        return self._model_name

    @property
    def system(self) -> str:
        """The model provider."""
        return self._provider.name

    async def request(
        self,
        messages: list[ModelMessage],
        model_settings: ModelSettings | None,
        model_request_parameters: ModelRequestParameters,
    ) -> ModelResponse:
        """Make a non-streaming request to the model from Pydantic AI call."""
        check_allow_model_requests()
        model_settings, model_request_parameters = self.prepare_request(
            model_settings,
            model_request_parameters,
        )
        response = await self._completions_create(
            messages, cast(MistralModelSettings, model_settings or {}), model_request_parameters
        )
        model_response = self._process_response(response)
        return model_response

    @asynccontextmanager
    async def request_stream(
        self,
        messages: list[ModelMessage],
        model_settings: ModelSettings | None,
        model_request_parameters: ModelRequestParameters,
        run_context: RunContext[Any] | None = None,
    ) -> AsyncIterator[StreamedResponse]:
        """Make a streaming request to the model from Pydantic AI call."""
        check_allow_model_requests()
        model_settings, model_request_parameters = self.prepare_request(
            model_settings,
            model_request_parameters,
        )
        response = await self._stream_completions_create(
            messages, cast(MistralModelSettings, model_settings or {}), model_request_parameters
        )
        async with response:
            yield await self._process_streamed_response(response, model_request_parameters)

    async def _completions_create(
        self,
        messages: list[ModelMessage],
        model_settings: MistralModelSettings,
        model_request_parameters: ModelRequestParameters,
    ) -> MistralChatCompletionResponse:
        """Make a non-streaming request to the model."""
        # TODO(Marcelo): We need to replace the current MistralAI client to use the beta client.
        # See https://docs.mistral.ai/agents/connectors/websearch/ to support web search.
        try:
            response = await self.client.chat.complete_async(
                model=str(self._model_name),
                messages=await self._map_messages(messages, model_request_parameters),
                n=1,
                tools=self._map_function_and_output_tools_definition(model_request_parameters) or UNSET,
                tool_choice=self._get_tool_choice(model_request_parameters),
                stream=False,
                max_tokens=model_settings.get('max_tokens', UNSET),
                temperature=model_settings.get('temperature', UNSET),
                top_p=model_settings.get('top_p', 1),
                timeout_ms=self._get_timeout_ms(model_settings.get('timeout')),
                random_seed=model_settings.get('seed', UNSET),
                stop=model_settings.get('stop_sequences', None),
                http_headers={'User-Agent': get_user_agent()},
            )
        except SDKError as e:
            if (status_code := e.status_code) >= 400:
                raise ModelHTTPError(status_code=status_code, model_name=self.model_name, body=e.body) from e
            raise ModelAPIError(model_name=self.model_name, message=e.message) from e

        assert response, 'A unexpected empty response from Mistral.'
        return response

    async def _stream_completions_create(
        self,
        messages: list[ModelMessage],
        model_settings: MistralModelSettings,
        model_request_parameters: ModelRequestParameters,
    ) -> MistralEventStreamAsync[MistralCompletionEvent]:
        """Create a streaming completion request to the Mistral model."""
        response: MistralEventStreamAsync[MistralCompletionEvent] | None
        mistral_messages = await self._map_messages(messages, model_request_parameters)

        # TODO(Marcelo): We need to replace the current MistralAI client to use the beta client.
        # See https://docs.mistral.ai/agents/connectors/websearch/ to support web search.
        if model_request_parameters.function_tools:
            # Function Calling
            response = await self.client.chat.stream_async(
                model=str(self._model_name),
                messages=mistral_messages,
                n=1,
                tools=self._map_function_and_output_tools_definition(model_request_parameters) or UNSET,
                tool_choice=self._get_tool_choice(model_request_parameters),
                temperature=model_settings.get('temperature', UNSET),
                top_p=model_settings.get('top_p', 1),
                max_tokens=model_settings.get('max_tokens', UNSET),
                timeout_ms=self._get_timeout_ms(model_settings.get('timeout')),
                presence_penalty=model_settings.get('presence_penalty'),
                frequency_penalty=model_settings.get('frequency_penalty'),
                stop=model_settings.get('stop_sequences', None),
                http_headers={'User-Agent': get_user_agent()},
            )

        elif model_request_parameters.output_tools:
            # TODO: Port to native "manual JSON" mode
            # Json Mode
            parameters_json_schemas = [tool.parameters_json_schema for tool in model_request_parameters.output_tools]
            user_output_format_message = self._generate_user_output_format(parameters_json_schemas)
            mistral_messages.append(user_output_format_message)

            response = await self.client.chat.stream_async(
                model=str(self._model_name),
                messages=mistral_messages,
                response_format={
                    'type': 'json_object'
                },  # TODO: Should be able to use json_schema now: https://docs.mistral.ai/capabilities/structured-output/custom_structured_output/, https://github.com/mistralai/client-python/blob/bc4adf335968c8a272e1ab7da8461c9943d8e701/src/mistralai/extra/utils/response_format.py#L9
                stream=True,
                temperature=model_settings.get('temperature', UNSET),
                top_p=model_settings.get('top_p', 1),
                max_tokens=model_settings.get('max_tokens', UNSET),
                timeout_ms=self._get_timeout_ms(model_settings.get('timeout')),
                presence_penalty=model_settings.get('presence_penalty'),
                frequency_penalty=model_settings.get('frequency_penalty'),
                stop=model_settings.get('stop_sequences', None),
                http_headers={'User-Agent': get_user_agent()},
            )

        else:
            # Stream Mode
            response = await self.client.chat.stream_async(
                model=str(self._model_name),
                messages=mistral_messages,
                stream=True,
                http_headers={'User-Agent': get_user_agent()},
            )
        assert response, 'A unexpected empty response from Mistral.'
        return response

    def _get_tool_choice(self, model_request_parameters: ModelRequestParameters) -> MistralToolChoiceEnum | None:
        """Get tool choice for the model.

        - "auto": Default mode. Model decides if it uses the tool or not.
        - "any": Select any tool.
        - "none": Prevents tool use.
        - "required": Forces tool use.
        """
        if not model_request_parameters.function_tools and not model_request_parameters.output_tools:
            return None
        elif not model_request_parameters.allow_text_output:
            return 'required'
        else:
            return 'auto'

    def _map_function_and_output_tools_definition(
        self, model_request_parameters: ModelRequestParameters
    ) -> list[MistralTool] | None:
        """Map function and output tools to MistralTool format.

        Returns None if both function_tools and output_tools are empty.
        """
        tools = [
            MistralTool(
                function=MistralFunction(
                    name=r.name, parameters=r.parameters_json_schema, description=r.description or ''
                )
            )
            for r in model_request_parameters.tool_defs.values()
        ]
        return tools or None

    def _process_response(self, response: MistralChatCompletionResponse) -> ModelResponse:
        """Process a non-streamed response, and prepare a message to return."""
        assert response.choices, 'Unexpected empty response choice.'

        choice = response.choices[0]
        content = choice.message.content
        tool_calls = choice.message.tool_calls

        parts: list[ModelResponsePart] = []
        text, thinking = _map_content(content)
        for thought in thinking:
            parts.append(ThinkingPart(content=thought))
        if text:
            parts.append(TextPart(content=text))

        if isinstance(tool_calls, list):
            for tool_call in tool_calls:
                tool = self._map_mistral_to_pydantic_tool_call(tool_call=tool_call)
                parts.append(tool)

        raw_finish_reason = choice.finish_reason
        provider_details: dict[str, Any] = {'finish_reason': raw_finish_reason}
        if response.created:  # pragma: no branch
            provider_details['timestamp'] = number_to_datetime(response.created)
        finish_reason = _FINISH_REASON_MAP.get(raw_finish_reason)

        return ModelResponse(
            parts=parts,
            usage=_map_usage(response),
            model_name=response.model,
            provider_response_id=response.id,
            provider_name=self._provider.name,
            provider_url=self._provider.base_url,
            finish_reason=finish_reason,
            provider_details=provider_details,
        )

    async def _process_streamed_response(
        self,
        response: MistralEventStreamAsync[MistralCompletionEvent],
        model_request_parameters: ModelRequestParameters,
    ) -> StreamedResponse:
        """Process a streamed response, and prepare a streaming response to return."""
        peekable_response = _utils.PeekableAsyncStream(response)
        first_chunk = await peekable_response.peek()
        if isinstance(first_chunk, _utils.Unset):
            raise UnexpectedModelBehavior(  # pragma: no cover
                'Streamed response ended without content or tool calls'
            )

        return MistralStreamedResponse(
            model_request_parameters=model_request_parameters,
            _response=peekable_response,
            _model_name=first_chunk.data.model,
            _provider_name=self._provider.name,
            _provider_url=self._provider.base_url,
            _provider_timestamp=number_to_datetime(first_chunk.data.created) if first_chunk.data.created else None,
        )

    @staticmethod
    def _map_mistral_to_pydantic_tool_call(tool_call: MistralToolCall) -> ToolCallPart:
        """Maps a MistralToolCall to a ToolCall."""
        tool_call_id = tool_call.id or _generate_tool_call_id()
        func_call = tool_call.function

        return ToolCallPart(func_call.name, func_call.arguments, tool_call_id)

    @staticmethod
    def _map_tool_call(t: ToolCallPart) -> MistralToolCall:
        """Maps a pydantic-ai ToolCall to a MistralToolCall."""
        return MistralToolCall(
            id=_utils.guard_tool_call_id(t=t),
            type='function',
            function=MistralFunctionCall(name=t.tool_name, arguments=t.args or {}),
        )

    def _generate_user_output_format(self, schemas: list[dict[str, Any]]) -> MistralUserMessage:
        """Get a message with an example of the expected output format."""
        examples: list[dict[str, Any]] = []
        for schema in schemas:
            typed_dict_definition: dict[str, Any] = {}
            for key, value in schema.get('properties', {}).items():
                typed_dict_definition[key] = self._get_python_type(value)
            examples.append(typed_dict_definition)

        example_schema = examples[0] if len(examples) == 1 else examples
        return MistralUserMessage(content=self.json_mode_schema_prompt.format(schema=example_schema))

    @classmethod
    def _get_python_type(cls, value: dict[str, Any]) -> str:
        """Return a string representation of the Python type for a single JSON schema property.

        This function handles recursion for nested arrays/objects and `anyOf`.
        """
        # 1) Handle anyOf first, because it's a different schema structure
        if any_of := value.get('anyOf'):
            # Simplistic approach: pick the first option in anyOf
            # (In reality, you'd possibly want to merge or union types)
            return f'Optional[{cls._get_python_type(any_of[0])}]'

        # 2) If we have a top-level "type" field
        value_type = value.get('type')
        if not value_type:
            # No explicit type; fallback
            return 'Any'

        # 3) Direct simple type mapping (string, integer, float, bool, None)
        if value_type in SIMPLE_JSON_TYPE_MAPPING and value_type != 'array' and value_type != 'object':
            return SIMPLE_JSON_TYPE_MAPPING[value_type]

        # 4) Array: Recursively get the item type
        if value_type == 'array':
            items = value.get('items', {})
            return f'list[{cls._get_python_type(items)}]'

        # 5) Object: Check for additionalProperties
        if value_type == 'object':
            additional_properties = value.get('additionalProperties', {})
            if isinstance(additional_properties, bool):
                return 'bool'  # pragma: lax no cover
            additional_properties_type = additional_properties.get('type')
            if (
                additional_properties_type in SIMPLE_JSON_TYPE_MAPPING
                and additional_properties_type != 'array'
                and additional_properties_type != 'object'
            ):
                # dict[str, bool/int/float/etc...]
                return f'dict[str, {SIMPLE_JSON_TYPE_MAPPING[additional_properties_type]}]'
            elif additional_properties_type == 'array':
                array_items = additional_properties.get('items', {})
                return f'dict[str, list[{cls._get_python_type(array_items)}]]'
            elif additional_properties_type == 'object':
                # nested dictionary of unknown shape
                return 'dict[str, dict[str, Any]]'
            else:
                # If no additionalProperties type or something else, default to a generic dict
                return 'dict[str, Any]'

        # 6) Fallback
        return 'Any'

    @staticmethod
    def _get_timeout_ms(timeout: Timeout | float | None) -> int | None:
        """Convert a timeout to milliseconds."""
        if timeout is None:
            return None
        if isinstance(timeout, float):  # pragma: no cover
            return int(1000 * timeout)
        raise NotImplementedError('Timeout object is not yet supported for MistralModel.')

    async def _map_user_message(self, message: ModelRequest) -> AsyncIterable[MistralMessages]:
        for part in message.parts:
            if isinstance(part, SystemPromptPart):
                yield MistralSystemMessage(content=part.content)
            elif isinstance(part, UserPromptPart):
                yield await self._map_user_prompt(part)
            elif isinstance(part, ToolReturnPart):
                yield MistralToolMessage(
                    tool_call_id=part.tool_call_id,
                    content=part.model_response_str(),
                )
            elif isinstance(part, RetryPromptPart):
                if part.tool_name is None:
                    yield MistralUserMessage(content=part.model_response())  # pragma: no cover
                else:
                    yield MistralToolMessage(
                        tool_call_id=part.tool_call_id,
                        content=part.model_response(),
                    )
            else:
                assert_never(part)

    async def _map_messages(  # noqa: C901
        self, messages: Sequence[ModelMessage], model_request_parameters: ModelRequestParameters
    ) -> list[MistralMessages]:
        """Just maps a `pydantic_ai.Message` to a `MistralMessage`."""
        mistral_messages: list[MistralMessages] = []
        for message in messages:
            if isinstance(message, ModelRequest):
                async for msg in self._map_user_message(message):
                    mistral_messages.append(msg)
            elif isinstance(message, ModelResponse):
                content_chunks: list[MistralContentChunk] = []
                thinking_chunks: list[MistralTextChunk | MistralReferenceChunk] = []
                tool_calls: list[MistralToolCall] = []

                for part in message.parts:
                    if isinstance(part, TextPart):
                        content_chunks.append(MistralTextChunk(text=part.content))
                    elif isinstance(part, ThinkingPart):
                        thinking_chunks.append(MistralTextChunk(text=part.content))
                    elif isinstance(part, ToolCallPart):
                        tool_calls.append(self._map_tool_call(part))
                    elif isinstance(part, BuiltinToolCallPart | BuiltinToolReturnPart):  # pragma: no cover
                        # This is currently never returned from mistral
                        pass
                    elif isinstance(part, FilePart):  # pragma: no cover
                        # Files generated by models are not sent back to models that don't themselves generate files.
                        pass
                    else:
                        assert_never(part)
                if thinking_chunks:
                    content_chunks.insert(0, MistralThinkChunk(thinking=thinking_chunks))
                mistral_messages.append(MistralAssistantMessage(content=content_chunks, tool_calls=tool_calls))
            else:
                assert_never(message)
        if instructions := self._get_instructions(messages, model_request_parameters):
            system_prompt_count = sum(1 for m in mistral_messages if isinstance(m, MistralSystemMessage))
            mistral_messages.insert(system_prompt_count, MistralSystemMessage(content=instructions))

        # Post-process messages to insert fake assistant message after tool message if followed by user message
        # to work around `Unexpected role 'user' after role 'tool'` error.
        processed_messages: list[MistralMessages] = []
        for i, current_message in enumerate(mistral_messages):
            processed_messages.append(current_message)

            if isinstance(current_message, MistralToolMessage) and i + 1 < len(mistral_messages):
                next_message = mistral_messages[i + 1]
                if isinstance(next_message, MistralUserMessage):
                    # Insert a dummy assistant message
                    processed_messages.append(MistralAssistantMessage(content=[MistralTextChunk(text='OK')]))

        return processed_messages

    async def _map_user_prompt(self, part: UserPromptPart) -> MistralUserMessage:
        content: str | list[MistralContentChunk]
        if isinstance(part.content, str):
            content = part.content
        else:
            content = []
            for item in part.content:
                if isinstance(item, str):
                    content.append(MistralTextChunk(text=item))
                elif isinstance(item, ImageUrl):
                    if item.force_download:
                        downloaded = await download_item(item, data_format='base64_uri')
                        image_url = MistralImageURL(url=downloaded['data'])
                        content.append(MistralImageURLChunk(image_url=image_url, type='image_url'))
                    else:
                        content.append(MistralImageURLChunk(image_url=MistralImageURL(url=item.url)))
                elif isinstance(item, BinaryContent):
                    if item.is_image:
                        image_url = MistralImageURL(url=item.data_uri)
                        content.append(MistralImageURLChunk(image_url=image_url, type='image_url'))
                    elif item.media_type == 'application/pdf':
                        content.append(MistralDocumentURLChunk(document_url=item.data_uri, type='document_url'))
                    else:
                        raise RuntimeError('BinaryContent other than image or PDF is not supported in Mistral.')
                elif isinstance(item, DocumentUrl):
                    if item.media_type == 'application/pdf':
                        if item.force_download:
                            downloaded = await download_item(item, data_format='base64_uri')
                            content.append(
                                MistralDocumentURLChunk(document_url=downloaded['data'], type='document_url')
                            )
                        else:
                            content.append(MistralDocumentURLChunk(document_url=item.url, type='document_url'))
                    else:
                        raise RuntimeError('DocumentUrl other than PDF is not supported in Mistral.')
                elif isinstance(item, VideoUrl):
                    raise RuntimeError('VideoUrl is not supported in Mistral.')
                elif isinstance(item, UploadedFile):
                    raise RuntimeError('UploadedFile is not supported by Mistral.')
                else:  # pragma: no cover
                    raise RuntimeError(f'Unsupported content type: {type(item)}')
        return MistralUserMessage(content=content)

```

---|---
####  __init__
```
__init__(
    model_name: MistralModelName[](https://ai.pydantic.dev/api/models/mistral/#pydantic_ai.models.mistral.MistralModelName "MistralModelName



      module-attribute
   \(pydantic_ai.models.mistral.MistralModelName\)"),
    *,
    provider: (
        ["mistral"] | Provider[](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.Provider "pydantic_ai.providers.Provider")[Mistral]
    ) = "mistral",
    profile: ModelProfileSpec | None = None,
    json_mode_schema_prompt:  = "Answer in JSON Object, respect the format:\n```\n{schema}\n```\n",
    settings: ModelSettings[](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings \(pydantic_ai.settings.ModelSettings\)") | None = None
)

```

Initialize a Mistral model.
Parameters:
Name | Type | Description | Default
---|---|---|---
`model_name` |  `MistralModelName[](https://ai.pydantic.dev/api/models/mistral/#pydantic_ai.models.mistral.MistralModelName "MistralModelName



      module-attribute
   \(pydantic_ai.models.mistral.MistralModelName\)")` |  The name of the model to use. |  _required_
`provider` |  `Provider[](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.Provider "pydantic_ai.providers.Provider")[Mistral]` |  The provider to use for authentication and API access. Can be either the string 'mistral' or an instance of `Provider[Mistral]`. If not provided, a new provider will be created using the other parameters. |  `'mistral'`
`profile` |  `ModelProfileSpec | None` |  The model profile to use. Defaults to a profile picked by the provider based on the model name. |  `None`
`json_mode_schema_prompt` |  |  The prompt to show when the model expects a JSON object as input. |  `'Answer in JSON Object, respect the format:\n```\n{schema}\n```\n'`
`settings` |  `ModelSettings[](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings \(pydantic_ai.settings.ModelSettings\)") | None` |  Model-specific settings that will be used as defaults for this model. |  `None`
Source code in `pydantic_ai_slim/pydantic_ai/models/mistral.py`
```
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
```
| ```
def __init__(
    self,
    model_name: MistralModelName,
    *,
    provider: Literal['mistral'] | Provider[Mistral] = 'mistral',
    profile: ModelProfileSpec | None = None,
    json_mode_schema_prompt: str = """Answer in JSON Object, respect the format:\n```\n{schema}\n```\n""",
    settings: ModelSettings | None = None,
):
    """Initialize a Mistral model.

    Args:
        model_name: The name of the model to use.
        provider: The provider to use for authentication and API access. Can be either the string
            'mistral' or an instance of `Provider[Mistral]`. If not provided, a new provider will be
            created using the other parameters.
        profile: The model profile to use. Defaults to a profile picked by the provider based on the model name.
        json_mode_schema_prompt: The prompt to show when the model expects a JSON object as input.
        settings: Model-specific settings that will be used as defaults for this model.
    """
    self._model_name = model_name
    self.json_mode_schema_prompt = json_mode_schema_prompt

    if isinstance(provider, str):
        provider = infer_provider(provider)
    self._provider = provider
    self.client = provider.client

    super().__init__(settings=settings, profile=profile or provider.model_profile)

```

---|---
####  model_name `property`
```
model_name: MistralModelName[](https://ai.pydantic.dev/api/models/mistral/#pydantic_ai.models.mistral.MistralModelName "MistralModelName



      module-attribute
   \(pydantic_ai.models.mistral.MistralModelName\)")

```

The model name.
####  system `property`
```
system:

```

The model provider.
####  request `async`
```
request(
    messages: [ModelMessage[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelMessage "ModelMessage



      module-attribute
   \(pydantic_ai.messages.ModelMessage\)")],
    model_settings: ModelSettings[](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings \(pydantic_ai.settings.ModelSettings\)") | None,
    model_request_parameters: ModelRequestParameters[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.ModelRequestParameters "ModelRequestParameters



      dataclass
   \(pydantic_ai.models.ModelRequestParameters\)"),
) -> ModelResponse[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse "ModelResponse



      dataclass
   \(pydantic_ai.messages.ModelResponse\)")

```

Make a non-streaming request to the model from Pydantic AI call.
Source code in `pydantic_ai_slim/pydantic_ai/models/mistral.py`
```
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
```
| ```
async def request(
    self,
    messages: list[ModelMessage],
    model_settings: ModelSettings | None,
    model_request_parameters: ModelRequestParameters,
) -> ModelResponse:
    """Make a non-streaming request to the model from Pydantic AI call."""
    check_allow_model_requests()
    model_settings, model_request_parameters = self.prepare_request(
        model_settings,
        model_request_parameters,
    )
    response = await self._completions_create(
        messages, cast(MistralModelSettings, model_settings or {}), model_request_parameters
    )
    model_response = self._process_response(response)
    return model_response

```

---|---
####  request_stream `async`
```
request_stream(
    messages: [ModelMessage[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelMessage "ModelMessage



      module-attribute
   \(pydantic_ai.messages.ModelMessage\)")],
    model_settings: ModelSettings[](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings \(pydantic_ai.settings.ModelSettings\)") | None,
    model_request_parameters: ModelRequestParameters[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.ModelRequestParameters "ModelRequestParameters



      dataclass
   \(pydantic_ai.models.ModelRequestParameters\)"),
    run_context: RunContext[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext



      dataclass
   \(pydantic_ai._run_context.RunContext\)")[] | None = None,
) -> [StreamedResponse[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.StreamedResponse "StreamedResponse



      dataclass
   \(pydantic_ai.models.StreamedResponse\)")]

```

Make a streaming request to the model from Pydantic AI call.
Source code in `pydantic_ai_slim/pydantic_ai/models/mistral.py`
```
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
```
| ```
@asynccontextmanager
async def request_stream(
    self,
    messages: list[ModelMessage],
    model_settings: ModelSettings | None,
    model_request_parameters: ModelRequestParameters,
    run_context: RunContext[Any] | None = None,
) -> AsyncIterator[StreamedResponse]:
    """Make a streaming request to the model from Pydantic AI call."""
    check_allow_model_requests()
    model_settings, model_request_parameters = self.prepare_request(
        model_settings,
        model_request_parameters,
    )
    response = await self._stream_completions_create(
        messages, cast(MistralModelSettings, model_settings or {}), model_request_parameters
    )
    async with response:
        yield await self._process_streamed_response(response, model_request_parameters)

```

---|---
###  MistralStreamedResponse `dataclass`
Bases: `StreamedResponse[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.StreamedResponse "StreamedResponse



      dataclass
   \(pydantic_ai.models.StreamedResponse\)")`
Implementation of `StreamedResponse` for Mistral models.
Source code in `pydantic_ai_slim/pydantic_ai/models/mistral.py`
```
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
664
665
666
667
668
669
670
671
672
673
674
675
676
677
678
679
680
681
682
683
684
685
686
687
688
689
690
691
692
693
694
695
696
697
698
699
700
701
702
703
704
705
706
707
708
709
710
711
712
713
714
715
716
717
718
719
720
721
722
723
724
725
726
727
728
729
730
731
732
733
734
735
736
737
738
739
740
741
742
743
744
745
746
747
748
```
| ```
@dataclass
class MistralStreamedResponse(StreamedResponse):
    """Implementation of `StreamedResponse` for Mistral models."""

    _model_name: MistralModelName
    _response: AsyncIterable[MistralCompletionEvent]
    _provider_name: str
    _provider_url: str
    _provider_timestamp: datetime | None = None
    _timestamp: datetime = field(default_factory=_now_utc)

    _delta_content: str = field(default='', init=False)

    async def _get_event_iterator(self) -> AsyncIterator[ModelResponseStreamEvent]:
        if self._provider_timestamp is not None:  # pragma: no branch
            self.provider_details = {'timestamp': self._provider_timestamp}
        chunk: MistralCompletionEvent
        async for chunk in self._response:
            self._usage += _map_usage(chunk.data)

            if chunk.data.id:  # pragma: no branch
                self.provider_response_id = chunk.data.id

            try:
                choice = chunk.data.choices[0]
            except IndexError:
                continue

            if raw_finish_reason := choice.finish_reason:
                self.provider_details = {**(self.provider_details or {}), 'finish_reason': raw_finish_reason}
                self.finish_reason = _FINISH_REASON_MAP.get(raw_finish_reason)

            # Handle the text part of the response
            content = choice.delta.content
            text, thinking = _map_content(content)
            for thought in thinking:
                for event in self._parts_manager.handle_thinking_delta(vendor_part_id='thinking', content=thought):
                    yield event
            if text:
                # Attempt to produce an output tool call from the received text
                output_tools = {c.name: c for c in self.model_request_parameters.output_tools}
                if output_tools:
                    self._delta_content += text
                    # TODO: Port to native "manual JSON" mode
                    maybe_tool_call_part = self._try_get_output_tool_from_text(self._delta_content, output_tools)
                    if maybe_tool_call_part:
                        yield self._parts_manager.handle_tool_call_part(
                            vendor_part_id='output',
                            tool_name=maybe_tool_call_part.tool_name,
                            args=maybe_tool_call_part.args_as_dict(),
                            tool_call_id=maybe_tool_call_part.tool_call_id,
                        )
                else:
                    for event in self._parts_manager.handle_text_delta(vendor_part_id='content', content=text):
                        yield event

            # Handle the explicit tool calls
            for index, dtc in enumerate(choice.delta.tool_calls or []):
                # It seems that mistral just sends full tool calls, so we just use them directly, rather than building
                yield self._parts_manager.handle_tool_call_part(
                    vendor_part_id=index, tool_name=dtc.function.name, args=dtc.function.arguments, tool_call_id=dtc.id
                )

    @property
    def model_name(self) -> MistralModelName:
        """Get the model name of the response."""
        return self._model_name

    @property
    def provider_name(self) -> str:
        """Get the provider name."""
        return self._provider_name

    @property
    def provider_url(self) -> str:
        """Get the provider base URL."""
        return self._provider_url

    @property
    def timestamp(self) -> datetime:
        """Get the timestamp of the response."""
        return self._timestamp

    @staticmethod
    def _try_get_output_tool_from_text(text: str, output_tools: dict[str, ToolDefinition]) -> ToolCallPart | None:
        output_json: dict[str, Any] | None = pydantic_core.from_json(text, allow_partial='trailing-strings')
        if output_json:
            for output_tool in output_tools.values():
                # NOTE: Additional verification to prevent JSON validation to crash
                # Ensures required parameters in the JSON schema are respected, especially for stream-based return types.
                # Example with BaseModel and required fields.
                if not MistralStreamedResponse._validate_required_json_schema(
                    output_json, output_tool.parameters_json_schema
                ):
                    continue

                # The following part_id will be thrown away
                return ToolCallPart(tool_name=output_tool.name, args=output_json)

    @staticmethod
    def _validate_required_json_schema(json_dict: dict[str, Any], json_schema: dict[str, Any]) -> bool:
        """Validate that all required parameters in the JSON schema are present in the JSON dictionary."""
        required_params = json_schema.get('required', [])
        properties = json_schema.get('properties', {})

        for param in required_params:
            if param not in json_dict:
                return False

            param_schema = properties.get(param, {})
            param_type = param_schema.get('type')
            param_items_type = param_schema.get('items', {}).get('type')

            if param_type == 'array' and param_items_type:
                if not isinstance(json_dict[param], list):
                    return False
                for item in json_dict[param]:
                    if not isinstance(item, VALID_JSON_TYPE_MAPPING[param_items_type]):
                        return False
            elif param_type and not isinstance(json_dict[param], VALID_JSON_TYPE_MAPPING[param_type]):
                return False

            if isinstance(json_dict[param], dict) and 'properties' in param_schema:
                nested_schema = param_schema
                if not MistralStreamedResponse._validate_required_json_schema(json_dict[param], nested_schema):
                    return False

        return True

```

---|---
####  model_name `property`
```
model_name: MistralModelName[](https://ai.pydantic.dev/api/models/mistral/#pydantic_ai.models.mistral.MistralModelName "MistralModelName



      module-attribute
   \(pydantic_ai.models.mistral.MistralModelName\)")

```

Get the model name of the response.
####  provider_name `property`
```
provider_name:

```

Get the provider name.
####  provider_url `property`
```
provider_url:

```

Get the provider base URL.
####  timestamp `property`
```
timestamp:

```

Get the timestamp of the response.
© Pydantic Services Inc. 2024 to present
