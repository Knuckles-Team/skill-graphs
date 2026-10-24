        builtin_tools: Optional additional builtin tools to use for this run.
        on_complete: Optional callback function called when the agent run completes successfully.
            The callback receives the completed [`AgentRunResult`][pydantic_ai.agent.AgentRunResult] and can optionally yield additional protocol-specific events.
    """
    return self.transform_stream(
        self.run_stream_native(
            output_type=output_type,
            message_history=message_history,
            deferred_tool_results=deferred_tool_results,
            model=model,
            instructions=instructions,
            deps=deps,
            model_settings=model_settings,
            usage_limits=usage_limits,
            usage=usage,
            metadata=metadata,
            infer_name=infer_name,
            toolsets=toolsets,
            builtin_tools=builtin_tools,
        ),
        on_complete=on_complete,
    )

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
    message_history: [ModelMessage[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelMessage "ModelMessage



      module-attribute
   \(pydantic_ai.messages.ModelMessage\)")] | None = None,
    deferred_tool_results: (
        DeferredToolResults[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.DeferredToolResults "DeferredToolResults



      dataclass
   \(pydantic_ai.DeferredToolResults\)") | None
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
   \(pydantic_ai.ui._event_stream.OnCompleteFunc\)")[EventT] | None = None,
    **kwargs:
) ->

```

Handle a protocol-specific HTTP request by running the agent and returning a streaming response of protocol-specific events.
Extra keyword arguments are forwarded to [`from_request`](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.UIAdapter.from_request "from_request



      async
      classmethod
  "), allowing subclasses to accept additional adapter-specific parameters.
Parameters:
Name | Type | Description | Default
---|---|---|---
`request` |  |  The incoming Starlette/FastAPI request. |  _required_
`agent` |  `AbstractAgent[](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AbstractAgent "AbstractAgent \(pydantic_ai.agent.AbstractAgent\)")[DispatchDepsT, DispatchOutputDataT]` |  The agent to run. |  _required_
`output_type` |  `OutputSpec[` |  Custom output type to use for this run, `output_type` may only be used if the agent has no output validators since output validators would expect an argument that matches the agent's output type. |  `None`
`message_history` |  `ModelMessage[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelMessage "ModelMessage



      module-attribute
   \(pydantic_ai.messages.ModelMessage\)")] | None` |  History of the conversation so far. |  `None`
`deferred_tool_results` |  `DeferredToolResults[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.DeferredToolResults "DeferredToolResults



      dataclass
   \(pydantic_ai.DeferredToolResults\)") | None` |  Optional results for deferred tool calls in the message history. |  `None`
`model` |  `Model[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.Model "Model \(pydantic_ai.models.Model\)") | KnownModelName[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.KnownModelName "KnownModelName



      module-attribute
   \(pydantic_ai.models.KnownModelName\)") | ` |  Optional model to use for this run, required if `model` was not set when creating the agent. |  `None`
`instructions` |  `Instructions[DispatchDepsT]` |  Optional additional instructions to use for this run. |  `None`
`deps` |  `DispatchDepsT` |  Optional dependencies to use for this run. |  `None`
`model_settings` |  `ModelSettings[](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings \(pydantic_ai.settings.ModelSettings\)") | None` |  Optional settings to use for this model's request. |  `None`
`usage_limits` |  `UsageLimits[](https://ai.pydantic.dev/api/usage/#pydantic_ai.usage.UsageLimits "UsageLimits



      dataclass
   \(pydantic_ai.usage.UsageLimits\)") | None` |  Optional limits on model request count or token usage. |  `None`
`usage` |  `RunUsage[](https://ai.pydantic.dev/api/usage/#pydantic_ai.usage.RunUsage "RunUsage



      dataclass
   \(pydantic_ai.usage.RunUsage\)") | None` |  Optional usage to start with, useful for resuming a conversation or agents used in tools. |  `None`
`metadata` |  `AgentMetadata[DispatchDepsT] | None` |  Optional metadata to attach to this run. Accepts a dictionary or a callable taking [`RunContext`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext



      dataclass
  "); merged with the agent's configured metadata. |  `None`
`infer_name` |  |  Whether to try to infer the agent name from the call frame if it's not set. |  `True`
`toolsets` |  `AbstractToolset[](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.AbstractToolset "AbstractToolset \(pydantic_ai.toolsets.AbstractToolset\)")[DispatchDepsT]] | None` |  Optional additional toolsets for this run. |  `None`
`builtin_tools` |  `AbstractBuiltinTool[](https://ai.pydantic.dev/api/builtin_tools/#pydantic_ai.builtin_tools.AbstractBuiltinTool "AbstractBuiltinTool



      dataclass
   \(pydantic_ai.builtin_tools.AbstractBuiltinTool\)")] | None` |  Optional additional builtin tools to use for this run. |  `None`
`on_complete` |  `OnCompleteFunc[](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.OnCompleteFunc "OnCompleteFunc



      module-attribute
   \(pydantic_ai.ui._event_stream.OnCompleteFunc\)")[EventT] | None` |  Optional callback function called when the agent run completes successfully. The callback receives the completed [`AgentRunResult`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AgentRunResult "AgentRunResult



      dataclass
  ") and can optionally yield additional protocol-specific events. |  `None`
`**kwargs` |  |  Additional keyword arguments forwarded to [`from_request`](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.UIAdapter.from_request "from_request



      async
      classmethod
  "). |  `{}`
Returns:
Type | Description
---|---
|  A streaming Starlette response with protocol-specific events encoded per the request's `Accept` header value.
Source code in `pydantic_ai_slim/pydantic_ai/ui/_adapter.py`
```
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
```
| ```
@classmethod
async def dispatch_request(
    cls,
    request: Request,
    *,
    agent: AbstractAgent[DispatchDepsT, DispatchOutputDataT],
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
    on_complete: OnCompleteFunc[EventT] | None = None,
    **kwargs: Any,
) -> Response:
    """Handle a protocol-specific HTTP request by running the agent and returning a streaming response of protocol-specific events.

    Extra keyword arguments are forwarded to [`from_request`][pydantic_ai.ui.UIAdapter.from_request],
    allowing subclasses to accept additional adapter-specific parameters.

    Args:
        request: The incoming Starlette/FastAPI request.
        agent: The agent to run.
        output_type: Custom output type to use for this run, `output_type` may only be used if the agent has no
            output validators since output validators would expect an argument that matches the agent's output type.
        message_history: History of the conversation so far.
        deferred_tool_results: Optional results for deferred tool calls in the message history.
        model: Optional model to use for this run, required if `model` was not set when creating the agent.
        instructions: Optional additional instructions to use for this run.
        deps: Optional dependencies to use for this run.
        model_settings: Optional settings to use for this model's request.
        usage_limits: Optional limits on model request count or token usage.
        usage: Optional usage to start with, useful for resuming a conversation or agents used in tools.
        metadata: Optional metadata to attach to this run. Accepts a dictionary or a callable taking
            [`RunContext`][pydantic_ai.tools.RunContext]; merged with the agent's configured metadata.
        infer_name: Whether to try to infer the agent name from the call frame if it's not set.
        toolsets: Optional additional toolsets for this run.
        builtin_tools: Optional additional builtin tools to use for this run.
        on_complete: Optional callback function called when the agent run completes successfully.
            The callback receives the completed [`AgentRunResult`][pydantic_ai.agent.AgentRunResult] and can optionally yield additional protocol-specific events.
        **kwargs: Additional keyword arguments forwarded to [`from_request`][pydantic_ai.ui.UIAdapter.from_request].

    Returns:
        A streaming Starlette response with protocol-specific events encoded per the request's `Accept` header value.
    """
    try:
        from starlette.responses import Response
    except ImportError as e:  # pragma: no cover
        raise ImportError(
            'Please install the `starlette` package to use `dispatch_request()` method, '
            'you can use the `ui` optional group — `pip install "pydantic-ai-slim[ui]"`'
        ) from e

    try:
        # The DepsT and OutputDataT come from `agent`, not from `cls`; the cast is necessary to explain this to pyright
        adapter = cast(
            UIAdapter[RunInputT, MessageT, EventT, DispatchDepsT, DispatchOutputDataT],
            await cls.from_request(request, agent=cast(AbstractAgent[AgentDepsT, OutputDataT], agent), **kwargs),
        )
    except ValidationError as e:  # pragma: no cover
        return Response(
            content=e.json(),
            media_type='application/json',
            status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
        )

    return adapter.streaming_response(
        adapter.run_stream(
            message_history=message_history,
            deferred_tool_results=deferred_tool_results,
            deps=deps,
            output_type=output_type,
            model=model,
            instructions=instructions,
            model_settings=model_settings,
            usage_limits=usage_limits,
            usage=usage,
            metadata=metadata,
            infer_name=infer_name,
            toolsets=toolsets,
            builtin_tools=builtin_tools,
            on_complete=on_complete,
        ),
    )

```

---|---
###  SSE_CONTENT_TYPE `module-attribute`
```
SSE_CONTENT_TYPE = 'text/event-stream'

```

Content type header value for Server-Sent Events (SSE).
###  NativeEvent `module-attribute`
```
NativeEvent:  = (
    AgentStreamEvent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.AgentStreamEvent "AgentStreamEvent



      module-attribute
   \(pydantic_ai.messages.AgentStreamEvent\)") | AgentRunResultEvent[](https://ai.pydantic.dev/api/run/#pydantic_ai.run.AgentRunResultEvent "AgentRunResultEvent



      dataclass
   \(pydantic_ai.run.AgentRunResultEvent\)")[]
)

```

Type alias for the native event type, which is either an `AgentStreamEvent` or an `AgentRunResultEvent`.
###  OnCompleteFunc `module-attribute`
```
OnCompleteFunc:  = (
    [[AgentRunResult[](https://ai.pydantic.dev/api/run/#pydantic_ai.run.AgentRunResult "AgentRunResult



      dataclass
   \(pydantic_ai.run.AgentRunResult\)")[]], None]
    | [[AgentRunResult[](https://ai.pydantic.dev/api/run/#pydantic_ai.run.AgentRunResult "AgentRunResult



      dataclass
   \(pydantic_ai.run.AgentRunResult\)")[]], [None]]
    | [[AgentRunResult[](https://ai.pydantic.dev/api/run/#pydantic_ai.run.AgentRunResult "AgentRunResult



      dataclass
   \(pydantic_ai.run.AgentRunResult\)")[]], [EventT]]
)

```

Callback function type that receives the `AgentRunResult` of the completed run. Can be sync, async, or an async generator of protocol-specific events.
###  UIEventStream `dataclass`
Bases: `RunInputT, EventT, AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)"), OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")]`
Base class for UI event stream transformers.
This class is responsible for transforming Pydantic AI events into protocol-specific events.
Source code in `pydantic_ai_slim/pydantic_ai/ui/_event_stream.py`
```
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
```
| ```
@dataclass
class UIEventStream(ABC, Generic[RunInputT, EventT, AgentDepsT, OutputDataT]):
    """Base class for UI event stream transformers.

    This class is responsible for transforming Pydantic AI events into protocol-specific events.
    """

    run_input: RunInputT

    accept: str | None = None
    """The `Accept` header value of the request, used to determine how to encode the protocol-specific events for the streaming response."""

    message_id: str = field(default_factory=lambda: str(uuid4()))
    """The message ID to use for the next event."""

    _turn: Literal['request', 'response'] | None = None

    _result: AgentRunResult[OutputDataT] | None = None
    _final_result_event: FinalResultEvent | None = None

    def new_message_id(self) -> str:
        """Generate and store a new message ID."""
        self.message_id = str(uuid4())
        return self.message_id

    @property
    def response_headers(self) -> Mapping[str, str] | None:
        """Response headers to return to the frontend."""
        return None

    @property
    def content_type(self) -> str:
        """Get the content type for the event stream, compatible with the `Accept` header value.

        By default, this returns the Server-Sent Events content type (`text/event-stream`).
        If a subclass supports other types as well, it should consider `self.accept` in [`encode_event()`][pydantic_ai.ui.UIEventStream.encode_event] and return the resulting content type.
        """
        return SSE_CONTENT_TYPE

    @abstractmethod
    def encode_event(self, event: EventT) -> str:
        """Encode a protocol-specific event as a string."""
        raise NotImplementedError

    async def encode_stream(self, stream: AsyncIterator[EventT]) -> AsyncIterator[str]:
        """Encode a stream of protocol-specific events as strings according to the `Accept` header value."""
        async for event in stream:
            yield self.encode_event(event)

    def streaming_response(self, stream: AsyncIterator[EventT]) -> StreamingResponse:
        """Generate a streaming response from a stream of protocol-specific events."""
        try:
            from starlette.responses import StreamingResponse
        except ImportError as e:  # pragma: no cover
            raise ImportError(
                'Please install the `starlette` package to use the `streaming_response()` method, '
                'you can use the `ui` optional group — `pip install "pydantic-ai-slim[ui]"`'
            ) from e

        return StreamingResponse(
            self.encode_stream(stream),
            headers=self.response_headers,
            media_type=self.content_type,
        )

    async def transform_stream(  # noqa: C901
        self, stream: AsyncIterator[NativeEvent], on_complete: OnCompleteFunc[EventT] | None = None
    ) -> AsyncIterator[EventT]:
        """Transform a stream of Pydantic AI events into protocol-specific events.

        This method dispatches to specific hooks and `handle_*` methods that subclasses can override:
        - [`before_stream()`][pydantic_ai.ui.UIEventStream.before_stream]
        - [`after_stream()`][pydantic_ai.ui.UIEventStream.after_stream]
        - [`on_error()`][pydantic_ai.ui.UIEventStream.on_error]
        - [`before_request()`][pydantic_ai.ui.UIEventStream.before_request]
        - [`after_request()`][pydantic_ai.ui.UIEventStream.after_request]
        - [`before_response()`][pydantic_ai.ui.UIEventStream.before_response]
        - [`after_response()`][pydantic_ai.ui.UIEventStream.after_response]
        - [`handle_event()`][pydantic_ai.ui.UIEventStream.handle_event]

        Args:
            stream: The stream of Pydantic AI events to transform.
            on_complete: Optional callback function called when the agent run completes successfully.
                The callback receives the completed [`AgentRunResult`][pydantic_ai.agent.AgentRunResult] and can optionally yield additional protocol-specific events.
        """
        async for e in self.before_stream():
            yield e

        try:
            async for event in stream:
                if isinstance(event, PartStartEvent):
                    async for e in self._turn_to('response'):
                        yield e
                elif isinstance(event, FunctionToolCallEvent):
                    async for e in self._turn_to('request'):
                        yield e
                elif isinstance(event, AgentRunResultEvent):
                    if (
                        self._final_result_event
                        and (tool_call_id := self._final_result_event.tool_call_id)
                        and (tool_name := self._final_result_event.tool_name)
                    ):
                        async for e in self._turn_to('request'):
                            yield e

                        self._final_result_event = None
                        # Ensure the stream does not end on a dangling tool call without a result.
                        output_tool_result_event = FunctionToolResultEvent(
                            result=ToolReturnPart(
                                tool_call_id=tool_call_id,
                                tool_name=tool_name,
                                content='Final result processed.',
                            )
                        )
                        async for e in self.handle_function_tool_result(output_tool_result_event):
                            yield e

                    result = cast(AgentRunResult[OutputDataT], event.result)
                    self._result = result

                    async for e in self._turn_to(None):
                        yield e

                    if on_complete is not None:
                        if inspect.isasyncgenfunction(on_complete):
                            async for e in on_complete(result):
                                yield e
                        elif _utils.is_async_callable(on_complete):
                            await on_complete(result)
                        else:
                            await _utils.run_in_executor(on_complete, result)
                elif isinstance(event, FinalResultEvent):
                    self._final_result_event = event

                if isinstance(event, BuiltinToolCallEvent | BuiltinToolResultEvent):  # pyright: ignore[reportDeprecated]
                    # These events were deprecated before this feature was introduced
                    continue

                async for e in self.handle_event(event):
                    yield e
        except Exception as e:
            async for e in self.on_error(e):
                yield e
        finally:
            async for e in self._turn_to(None):
                yield e

            async for e in self.after_stream():
                yield e

    async def _turn_to(self, to_turn: Literal['request', 'response'] | None) -> AsyncIterator[EventT]:
        """Fire hooks when turning from request to response or vice versa."""
        if to_turn == self._turn:
            return

        if self._turn == 'request':
            async for e in self.after_request():
                yield e
        elif self._turn == 'response':
            async for e in self.after_response():
                yield e

        self._turn = to_turn

        if to_turn == 'request':
            async for e in self.before_request():
                yield e
        elif to_turn == 'response':
            async for e in self.before_response():
                yield e

    async def handle_event(self, event: NativeEvent) -> AsyncIterator[EventT]:
        """Transform a Pydantic AI event into one or more protocol-specific events.

        This method dispatches to specific `handle_*` methods based on event type:

        - [`PartStartEvent`][pydantic_ai.messages.PartStartEvent] -> [`handle_part_start()`][pydantic_ai.ui.UIEventStream.handle_part_start]
        - [`PartDeltaEvent`][pydantic_ai.messages.PartDeltaEvent] -> `handle_part_delta`
        - [`PartEndEvent`][pydantic_ai.messages.PartEndEvent] -> `handle_part_end`
