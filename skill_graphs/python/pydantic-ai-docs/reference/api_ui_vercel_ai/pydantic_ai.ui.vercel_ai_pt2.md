                        provider_name=part.provider_name,
                        provider_details=part.provider_details,
                    )
                    return_meta = dump_provider_metadata(
                        wrapper_key=None,
                        provider_name=builtin_return.provider_name,
                        provider_details=builtin_return.provider_details,
                    )
                    combined_provider_meta = cls._dump_builtin_tool_meta(call_meta, return_meta)

                    if builtin_return.outcome == 'denied':
                        ui_parts.append(
                            ToolOutputDeniedPart(
                                type=tool_name,
                                tool_call_id=part.tool_call_id,
                                input=_safe_args_as_dict(part),
                                provider_executed=True,
                                call_provider_metadata=combined_provider_meta,
                                approval=ToolApprovalResponded(
                                    id=str(uuid.uuid4()),
                                    approved=False,
                                    reason=builtin_return.model_response_str(),
                                ),
                            )
                        )
                    elif (
                        builtin_return.outcome == 'failed'
                        or builtin_return.model_response_object().get('is_error') is True
                    ):
                        response_obj = builtin_return.model_response_object()
                        error_text = response_obj.get('error_text', builtin_return.model_response_str())
                        ui_parts.append(
                            ToolOutputErrorPart(
                                type=tool_name,
                                tool_call_id=part.tool_call_id,
                                input=_safe_args_as_dict(part),
                                error_text=error_text,
                                provider_executed=True,
                                call_provider_metadata=combined_provider_meta,
                            )
                        )
                    else:
                        ui_parts.append(
                            ToolOutputAvailablePart(
                                type=tool_name,
                                tool_call_id=part.tool_call_id,
                                input=_safe_args_as_dict(part),
                                output=tool_return_output(builtin_return),
                                provider_executed=True,
                                call_provider_metadata=combined_provider_meta,
                            )
                        )
                else:
                    call_provider_metadata = dump_provider_metadata(
                        id=part.id, provider_name=part.provider_name, provider_details=part.provider_details
                    )
                    ui_parts.append(
                        ToolInputAvailablePart(
                            type=tool_name,
                            tool_call_id=part.tool_call_id,
                            input=_safe_args_as_dict(part),
                            provider_executed=True,
                            call_provider_metadata=call_provider_metadata,
                        )
                    )
            elif isinstance(part, ToolCallPart):
                ui_parts.extend(cls._dump_tool_call_part(part, tool_results))
            else:
                assert_never(part)

        return ui_parts

    @staticmethod
    def _dump_tool_call_part(
        part: ToolCallPart, tool_results: dict[str, ToolReturnPart | RetryPromptPart]
    ) -> list[UIMessagePart]:
        """Convert a ToolCallPart (with optional result) into UIMessageParts."""
        tool_result = tool_results.get(part.tool_call_id)
        call_provider_metadata = dump_provider_metadata(
            id=part.id, provider_name=part.provider_name, provider_details=part.provider_details
        )
        tool_type = f'tool-{part.tool_name}'
        ui_parts: list[UIMessagePart] = []

        if isinstance(tool_result, ToolReturnPart):
            if tool_result.outcome == 'denied':
                ui_parts.append(
                    ToolOutputDeniedPart(
                        type=tool_type,
                        tool_call_id=part.tool_call_id,
                        input=_safe_args_as_dict(part),
                        provider_executed=False,
                        call_provider_metadata=call_provider_metadata,
                        approval=ToolApprovalResponded(
                            id=str(uuid.uuid4()),
                            approved=False,
                            reason=tool_result.model_response_str(),
                        ),
                    )
                )
            elif tool_result.outcome == 'failed':
                ui_parts.append(
                    ToolOutputErrorPart(
                        type=tool_type,
                        tool_call_id=part.tool_call_id,
                        input=_safe_args_as_dict(part),
                        error_text=tool_result.model_response_str(),
                        provider_executed=False,
                        call_provider_metadata=call_provider_metadata,
                    )
                )
            else:
                ui_parts.append(
                    ToolOutputAvailablePart(
                        type=tool_type,
                        tool_call_id=part.tool_call_id,
                        input=_safe_args_as_dict(part),
                        output=tool_return_output(tool_result),
                        provider_executed=False,
                        call_provider_metadata=call_provider_metadata,
                    )
                )
            # Check for Vercel AI chunks returned by tool calls via metadata.
            ui_parts.extend(_extract_metadata_ui_parts(tool_result))
        elif isinstance(tool_result, RetryPromptPart):
            ui_parts.append(
                ToolOutputErrorPart(
                    type=tool_type,
                    tool_call_id=part.tool_call_id,
                    input=_safe_args_as_dict(part),
                    error_text=tool_result.model_response(),
                    provider_executed=False,
                    call_provider_metadata=call_provider_metadata,
                )
            )
        else:
            ui_parts.append(
                ToolInputAvailablePart(
                    type=tool_type,
                    tool_call_id=part.tool_call_id,
                    input=_safe_args_as_dict(part),
                    provider_executed=False,
                    call_provider_metadata=call_provider_metadata,
                )
            )

        return ui_parts

    @classmethod
    def dump_messages(
        cls,
        messages: Sequence[ModelMessage],
        *,
        generate_message_id: Callable[[ModelRequest | ModelResponse, Literal['system', 'user', 'assistant'], int], str]
        | None = None,
    ) -> list[UIMessage]:
        """Transform Pydantic AI messages into Vercel AI messages.

        Args:
            messages: A sequence of ModelMessage objects to convert
            generate_message_id: Optional custom function to generate message IDs. If provided,
                it receives the message, the role ('system', 'user', or 'assistant'), and the
                message index (incremented per UIMessage appended), and should return a unique
                string ID. If not provided, uses `provider_response_id` for responses,
                run_id-based IDs for messages with run_id, or a deterministic UUID5 fallback.

        Returns:
            A list of UIMessage objects in Vercel AI format
        """
        tool_results: dict[str, ToolReturnPart | RetryPromptPart] = {}

        for msg in messages:
            if isinstance(msg, ModelRequest):
                for part in msg.parts:
                    if isinstance(part, ToolReturnPart):
                        tool_results[part.tool_call_id] = part
                    elif isinstance(part, RetryPromptPart) and part.tool_name:
                        tool_results[part.tool_call_id] = part

        id_generator = generate_message_id or _generate_message_id
        result: list[UIMessage] = []
        message_index = 0

        for msg in messages:
            if isinstance(msg, ModelRequest):
                system_ui_parts, user_ui_parts = cls._dump_request_message(msg)
                if system_ui_parts:
                    result.append(
                        UIMessage(id=id_generator(msg, 'system', message_index), role='system', parts=system_ui_parts)
                    )
                    message_index += 1

                if user_ui_parts:
                    result.append(
                        UIMessage(id=id_generator(msg, 'user', message_index), role='user', parts=user_ui_parts)
                    )
                    message_index += 1

            elif isinstance(  # pragma: no branch
                msg, ModelResponse
            ):
                ui_parts: list[UIMessagePart] = cls._dump_response_message(msg, tool_results)
                if ui_parts:  # pragma: no branch
                    result.append(
                        UIMessage(id=id_generator(msg, 'assistant', message_index), role='assistant', parts=ui_parts)
                    )
                    message_index += 1
            else:
                assert_never(msg)

        return result

```

---|---
####  sdk_version `class-attribute` `instance-attribute`
```
sdk_version: [5, 6] = 5

```

Vercel AI SDK version to target. Default is 5 for backwards compatibility.
Setting `sdk_version=6` enables tool approval streaming for human-in-the-loop workflows.
####  build_run_input `classmethod`
```
build_run_input(body: ) -> RequestData[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.request_types.RequestData "RequestData



      module-attribute
   \(pydantic_ai.ui.vercel_ai.request_types.RequestData\)")

```

Build a Vercel AI run input object from the request body.
Source code in `pydantic_ai_slim/pydantic_ai/ui/vercel_ai/_adapter.py`
```
135
136
137
138
```
| ```
@classmethod
def build_run_input(cls, body: bytes) -> RequestData:
    """Build a Vercel AI run input object from the request body."""
    return request_data_ta.validate_json(body)

```

---|---
####  from_request `async` `classmethod`
```
from_request(
    request: ,
    *,
    agent: AbstractAgent[](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AbstractAgent "AbstractAgent \(pydantic_ai.agent.AbstractAgent\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)"), OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")],
    sdk_version: [5, 6] = 5,
    **kwargs:
) -> VercelAIAdapter[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.VercelAIAdapter "VercelAIAdapter



      dataclass
   \(pydantic_ai.ui.vercel_ai._adapter.VercelAIAdapter\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)"), OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")]

```

Extends [`from_request`](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.UIAdapter.from_request "from_request



      async
      classmethod
  ") with the `sdk_version` parameter.
Source code in `pydantic_ai_slim/pydantic_ai/ui/vercel_ai/_adapter.py`
```
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
```
| ```
@classmethod
async def from_request(
    cls,
    request: Request,
    *,
    agent: AbstractAgent[AgentDepsT, OutputDataT],
    sdk_version: Literal[5, 6] = 5,
    **kwargs: Any,
) -> VercelAIAdapter[AgentDepsT, OutputDataT]:
    """Extends [`from_request`][pydantic_ai.ui.UIAdapter.from_request] with the `sdk_version` parameter."""
    return await super().from_request(request, agent=agent, sdk_version=sdk_version, **kwargs)

```

---|---
####  dispatch_request `async` `classmethod`
```
dispatch_request(
    request: ,
    *,
    agent: AbstractAgent[](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AbstractAgent "AbstractAgent \(pydantic_ai.agent.AbstractAgent\)")[
        DispatchDepsT, DispatchOutputDataT
    ],
    sdk_version: [5, 6] = 5,
    message_history: [ModelMessage[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelMessage "ModelMessage



      module-attribute
   \(pydantic_ai.messages.ModelMessage\)")] | None = None,
    deferred_tool_results: (
        DeferredToolResults[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.DeferredToolResults "DeferredToolResults



      dataclass
   \(pydantic_ai.tools.DeferredToolResults\)") | None
    ) = None,
    model: Model[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.Model "Model \(pydantic_ai.models.Model\)") | KnownModelName[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.KnownModelName "KnownModelName



      module-attribute
   \(pydantic_ai.models.KnownModelName\)") |  | None = None,
    instructions: Instructions[DispatchDepsT] = None,
    deps: DispatchDepsT = None,
    output_type: OutputSpec[] | None = None,
    model_settings: ModelSettings[](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings \(pydantic_ai.settings.ModelSettings\)") | None = None,
    usage_limits: UsageLimits[](https://ai.pydantic.dev/api/usage/#pydantic_ai.usage.UsageLimits "UsageLimits



      dataclass
   \(pydantic_ai.usage.UsageLimits\)") | None = None,
    usage: RunUsage[](https://ai.pydantic.dev/api/usage/#pydantic_ai.usage.RunUsage "RunUsage



      dataclass
   \(pydantic_ai.usage.RunUsage\)") | None = None,
    metadata: AgentMetadata[DispatchDepsT] | None = None,
    infer_name:  = True,
    toolsets: (
        [AbstractToolset[](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.AbstractToolset "AbstractToolset \(pydantic_ai.toolsets.AbstractToolset\)")[DispatchDepsT]] | None
    ) = None,
    builtin_tools: (
        [AbstractBuiltinTool[](https://ai.pydantic.dev/api/builtin_tools/#pydantic_ai.builtin_tools.AbstractBuiltinTool "AbstractBuiltinTool



      dataclass
   \(pydantic_ai.builtin_tools.AbstractBuiltinTool\)")] | None
    ) = None,
    on_complete: OnCompleteFunc[](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.OnCompleteFunc "OnCompleteFunc



      module-attribute
   \(pydantic_ai.ui._event_stream.OnCompleteFunc\)")[BaseChunk[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.response_types.BaseChunk "BaseChunk \(pydantic_ai.ui.vercel_ai.response_types.BaseChunk\)")] | None = None,
    **kwargs:
) ->

```

Extends [`dispatch_request`](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.UIAdapter.dispatch_request "dispatch_request



      async
      classmethod
  ") with the `sdk_version` parameter.
Source code in `pydantic_ai_slim/pydantic_ai/ui/vercel_ai/_adapter.py`
```
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
```
| ```
@classmethod
async def dispatch_request(
    cls,
    request: Request,
    *,
    agent: AbstractAgent[DispatchDepsT, DispatchOutputDataT],
    sdk_version: Literal[5, 6] = 5,
    message_history: Sequence[ModelMessage] | None = None,
    deferred_tool_results: DeferredToolResults | None = None,
    model: Model | KnownModelName | str | None = None,
    instructions: Instructions[DispatchDepsT] = None,
    deps: DispatchDepsT = None,
    output_type: OutputSpec[Any] | None = None,
    model_settings: ModelSettings | None = None,
    usage_limits: UsageLimits | None = None,
    usage: RunUsage | None = None,
    metadata: AgentMetadata[DispatchDepsT] | None = None,
    infer_name: bool = True,
    toolsets: Sequence[AbstractToolset[DispatchDepsT]] | None = None,
    builtin_tools: Sequence[AbstractBuiltinTool] | None = None,
    on_complete: OnCompleteFunc[BaseChunk] | None = None,
    **kwargs: Any,
) -> Response:
    """Extends [`dispatch_request`][pydantic_ai.ui.UIAdapter.dispatch_request] with the `sdk_version` parameter."""
    return await super().dispatch_request(
        request,
        agent=agent,
        sdk_version=sdk_version,
        message_history=message_history,
        deferred_tool_results=deferred_tool_results,
        model=model,
        instructions=instructions,
        deps=deps,
        output_type=output_type,
        model_settings=model_settings,
        usage_limits=usage_limits,
        usage=usage,
        metadata=metadata,
        infer_name=infer_name,
        toolsets=toolsets,
        builtin_tools=builtin_tools,
        on_complete=on_complete,
        **kwargs,
    )

```

---|---
####  build_event_stream
```
build_event_stream() -> (
    UIEventStream[](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.UIEventStream "UIEventStream



      dataclass
   \(pydantic_ai.ui.UIEventStream\)")[
        RequestData[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.request_types.RequestData "RequestData



      module-attribute
   \(pydantic_ai.ui.vercel_ai.request_types.RequestData\)"), BaseChunk[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.response_types.BaseChunk "BaseChunk \(pydantic_ai.ui.vercel_ai.response_types.BaseChunk\)"), AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)"), OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")
    ]
)

```

Build a Vercel AI event stream transformer.
Source code in `pydantic_ai_slim/pydantic_ai/ui/vercel_ai/_adapter.py`
```
197
198
199
```
| ```
def build_event_stream(self) -> UIEventStream[RequestData, BaseChunk, AgentDepsT, OutputDataT]:
    """Build a Vercel AI event stream transformer."""
    return VercelAIEventStream(self.run_input, accept=self.accept, sdk_version=self.sdk_version)

```

---|---
####  deferred_tool_results `cached` `property`
```
deferred_tool_results: DeferredToolResults[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.DeferredToolResults "DeferredToolResults



      dataclass
   \(pydantic_ai.tools.DeferredToolResults\)") | None

```

Extract deferred tool results from Vercel AI messages with approval responses.
####  messages `cached` `property`
```
messages: [ModelMessage[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelMessage "ModelMessage



      module-attribute
   \(pydantic_ai.messages.ModelMessage\)")]

```

Pydantic AI messages from the Vercel AI run input.
####  load_messages `classmethod`
```
load_messages(
    messages: [UIMessage[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.request_types.UIMessage "UIMessage \(pydantic_ai.ui.vercel_ai.request_types.UIMessage\)")],
) -> [ModelMessage[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelMessage "ModelMessage



      module-attribute
   \(pydantic_ai.messages.ModelMessage\)")]

```

Transform Vercel AI messages into Pydantic AI messages.
Source code in `pydantic_ai_slim/pydantic_ai/ui/vercel_ai/_adapter.py`
```
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
```
| ```
@classmethod
def load_messages(cls, messages: Sequence[UIMessage]) -> list[ModelMessage]:  # noqa: C901
    """Transform Vercel AI messages into Pydantic AI messages."""
    builder = MessagesBuilder()

    for msg in messages:
        if msg.role == 'system':
            for part in msg.parts:
                if isinstance(part, TextUIPart):
                    builder.add(SystemPromptPart(content=part.text))
                else:  # pragma: no cover
                    raise ValueError(f'Unsupported system message part type: {type(part)}')
        elif msg.role == 'user':
            user_prompt_content: str | list[UserContent] = []
            for part in msg.parts:
                if isinstance(part, TextUIPart):
                    user_prompt_content.append(part.text)
                elif isinstance(part, FileUIPart):
                    try:
                        file = BinaryContent.from_data_uri(part.url)
                    except ValueError:
                        # Check provider_metadata for UploadedFile data
                        provider_meta = load_provider_metadata(part.provider_metadata)
                        uploaded_file_id = provider_meta.get('file_id')
                        uploaded_file_provider = provider_meta.get('provider_name')
                        if uploaded_file_id and uploaded_file_provider:
                            file = UploadedFile(
                                file_id=uploaded_file_id,
                                provider_name=cast(UploadedFileProviderName, uploaded_file_provider),
                                media_type=part.media_type,
                                vendor_metadata=provider_meta.get('vendor_metadata'),
                                identifier=provider_meta.get('identifier'),
                            )
                        else:
                            media_type_prefix = part.media_type.split('/', 1)[0]
                            match media_type_prefix:
                                case 'image':
                                    file = ImageUrl(url=part.url, media_type=part.media_type)
                                case 'video':
                                    file = VideoUrl(url=part.url, media_type=part.media_type)
                                case 'audio':
                                    file = AudioUrl(url=part.url, media_type=part.media_type)
                                case _:
                                    file = DocumentUrl(url=part.url, media_type=part.media_type)
                    user_prompt_content.append(file)
                else:  # pragma: no cover
                    raise ValueError(f'Unsupported user message part type: {type(part)}')

            if user_prompt_content:  # pragma: no branch
                if len(user_prompt_content) == 1 and isinstance(user_prompt_content[0], str):
                    user_prompt_content = user_prompt_content[0]
                builder.add(UserPromptPart(content=user_prompt_content))

        elif msg.role == 'assistant':
            for part in msg.parts:
                if isinstance(part, TextUIPart):
                    provider_meta = load_provider_metadata(part.provider_metadata)
                    builder.add(
                        TextPart(
                            content=part.text,
                            id=provider_meta.get('id'),
                            provider_name=provider_meta.get('provider_name'),
                            provider_details=provider_meta.get('provider_details'),
                        )
                    )
                elif isinstance(part, ReasoningUIPart):
                    provider_meta = load_provider_metadata(part.provider_metadata)
                    builder.add(
                        ThinkingPart(
                            content=part.text,
                            id=provider_meta.get('id'),
                            signature=provider_meta.get('signature'),
                            provider_name=provider_meta.get('provider_name'),
                            provider_details=provider_meta.get('provider_details'),
                        )
                    )
                elif isinstance(part, FileUIPart):
                    try:
                        file = BinaryContent.from_data_uri(part.url)
                    except ValueError as e:  # pragma: no cover
                        # We don't yet handle non-data-URI file URLs returned by assistants, as no Pydantic AI models do this.
                        raise ValueError(
                            'Vercel AI integration can currently only handle assistant file parts with data URIs.'
                        ) from e
                    provider_meta = load_provider_metadata(part.provider_metadata)
                    builder.add(
                        FilePart(
                            content=file,
                            id=provider_meta.get('id'),
