  * [`PartStartEvent`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.PartStartEvent "PartStartEvent



      dataclass
  ") -> [`handle_part_start()`](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.UIEventStream.handle_part_start "handle_part_start



      async
  ")
  * [`PartDeltaEvent`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.PartDeltaEvent "PartDeltaEvent



      dataclass
  ") -> `handle_part_delta`
  * [`PartEndEvent`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.PartEndEvent "PartEndEvent



      dataclass
  ") -> `handle_part_end`
  * [`FinalResultEvent`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FinalResultEvent "FinalResultEvent



      dataclass
  ") -> `handle_final_result`
  * [`FunctionToolCallEvent`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FunctionToolCallEvent "FunctionToolCallEvent



      dataclass
  ") -> `handle_function_tool_call`
  * [`FunctionToolResultEvent`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FunctionToolResultEvent "FunctionToolResultEvent



      dataclass
  ") -> `handle_function_tool_result`
  * [`AgentRunResultEvent`](https://ai.pydantic.dev/api/run/#pydantic_ai.run.AgentRunResultEvent "AgentRunResultEvent



      dataclass
  ") -> `handle_run_result`


Subclasses are encouraged to override the individual `handle_*` methods rather than this one. If you need specific behavior for all events, make sure you call the super method.
Source code in `pydantic_ai_slim/pydantic_ai/ui/_event_stream.py`
```
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
```
| ```
async def handle_event(self, event: NativeEvent) -> AsyncIterator[EventT]:
    """Transform a Pydantic AI event into one or more protocol-specific events.

    This method dispatches to specific `handle_*` methods based on event type:

    - [`PartStartEvent`][pydantic_ai.messages.PartStartEvent] -> [`handle_part_start()`][pydantic_ai.ui.UIEventStream.handle_part_start]
    - [`PartDeltaEvent`][pydantic_ai.messages.PartDeltaEvent] -> `handle_part_delta`
    - [`PartEndEvent`][pydantic_ai.messages.PartEndEvent] -> `handle_part_end`
    - [`FinalResultEvent`][pydantic_ai.messages.FinalResultEvent] -> `handle_final_result`
    - [`FunctionToolCallEvent`][pydantic_ai.messages.FunctionToolCallEvent] -> `handle_function_tool_call`
    - [`FunctionToolResultEvent`][pydantic_ai.messages.FunctionToolResultEvent] -> `handle_function_tool_result`
    - [`AgentRunResultEvent`][pydantic_ai.run.AgentRunResultEvent] -> `handle_run_result`

    Subclasses are encouraged to override the individual `handle_*` methods rather than this one.
    If you need specific behavior for all events, make sure you call the super method.
    """
    match event:
        case PartStartEvent():
            async for e in self.handle_part_start(event):
                yield e
        case PartDeltaEvent():
            async for e in self.handle_part_delta(event):
                yield e
        case PartEndEvent():
            async for e in self.handle_part_end(event):
                yield e
        case FinalResultEvent():
            async for e in self.handle_final_result(event):
                yield e
        case FunctionToolCallEvent():
            async for e in self.handle_function_tool_call(event):
                yield e
        case FunctionToolResultEvent():
            async for e in self.handle_function_tool_result(event):
                yield e
        case AgentRunResultEvent():
            async for e in self.handle_run_result(event):
                yield e
        case _:
            pass

```

---|---
####  handle_part_start `async`
```
handle_part_start(
    event: PartStartEvent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.PartStartEvent "PartStartEvent



      dataclass
   \(pydantic_ai.messages.PartStartEvent\)"),
) -> [EventT]

```

Handle a `PartStartEvent`.
This method dispatches to specific `handle_*` methods based on part type:
  * [`TextPart`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.TextPart "TextPart



      dataclass
  ") -> [`handle_text_start()`](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.UIEventStream.handle_text_start "handle_text_start



      async
  ")
  * [`ThinkingPart`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ThinkingPart "ThinkingPart



      dataclass
  ") -> [`handle_thinking_start()`](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.UIEventStream.handle_thinking_start "handle_thinking_start



      async
  ")
  * [`ToolCallPart`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPart "ToolCallPart



      dataclass
  ") -> [`handle_tool_call_start()`](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.UIEventStream.handle_tool_call_start "handle_tool_call_start



      async
  ")
  * [`BuiltinToolCallPart`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BuiltinToolCallPart "BuiltinToolCallPart



      dataclass
  ") -> [`handle_builtin_tool_call_start()`](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.UIEventStream.handle_builtin_tool_call_start "handle_builtin_tool_call_start



      async
  ")
  * [`BuiltinToolReturnPart`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BuiltinToolReturnPart "BuiltinToolReturnPart



      dataclass
  ") -> [`handle_builtin_tool_return()`](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.UIEventStream.handle_builtin_tool_return "handle_builtin_tool_return



      async
  ")
  * [`FilePart`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FilePart "FilePart



      dataclass
  ") -> [`handle_file()`](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.UIEventStream.handle_file "handle_file



      async
  ")


Subclasses are encouraged to override the individual `handle_*` methods rather than this one. If you need specific behavior for all part start events, make sure you call the super method.
Parameters:
Name | Type | Description | Default
---|---|---|---
`event` |  `PartStartEvent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.PartStartEvent "PartStartEvent



      dataclass
   \(pydantic_ai.messages.PartStartEvent\)")` |  The part start event. |  _required_
Source code in `pydantic_ai_slim/pydantic_ai/ui/_event_stream.py`
```
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
```
| ```
async def handle_part_start(self, event: PartStartEvent) -> AsyncIterator[EventT]:
    """Handle a `PartStartEvent`.

    This method dispatches to specific `handle_*` methods based on part type:

    - [`TextPart`][pydantic_ai.messages.TextPart] -> [`handle_text_start()`][pydantic_ai.ui.UIEventStream.handle_text_start]
    - [`ThinkingPart`][pydantic_ai.messages.ThinkingPart] -> [`handle_thinking_start()`][pydantic_ai.ui.UIEventStream.handle_thinking_start]
    - [`ToolCallPart`][pydantic_ai.messages.ToolCallPart] -> [`handle_tool_call_start()`][pydantic_ai.ui.UIEventStream.handle_tool_call_start]
    - [`BuiltinToolCallPart`][pydantic_ai.messages.BuiltinToolCallPart] -> [`handle_builtin_tool_call_start()`][pydantic_ai.ui.UIEventStream.handle_builtin_tool_call_start]
    - [`BuiltinToolReturnPart`][pydantic_ai.messages.BuiltinToolReturnPart] -> [`handle_builtin_tool_return()`][pydantic_ai.ui.UIEventStream.handle_builtin_tool_return]
    - [`FilePart`][pydantic_ai.messages.FilePart] -> [`handle_file()`][pydantic_ai.ui.UIEventStream.handle_file]

    Subclasses are encouraged to override the individual `handle_*` methods rather than this one.
    If you need specific behavior for all part start events, make sure you call the super method.

    Args:
        event: The part start event.
    """
    part = event.part
    previous_part_kind = event.previous_part_kind
    match part:
        case TextPart():
            async for e in self.handle_text_start(part, follows_text=previous_part_kind == 'text'):
                yield e
        case ThinkingPart():
            async for e in self.handle_thinking_start(part, follows_thinking=previous_part_kind == 'thinking'):
                yield e
        case ToolCallPart():
            async for e in self.handle_tool_call_start(part):
                yield e
        case BuiltinToolCallPart():
            async for e in self.handle_builtin_tool_call_start(part):
                yield e
        case BuiltinToolReturnPart():
            async for e in self.handle_builtin_tool_return(part):
                yield e
        case FilePart():  # pragma: no branch
            async for e in self.handle_file(part):
                yield e

```

---|---
####  handle_part_delta `async`
```
handle_part_delta(
    event: PartDeltaEvent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.PartDeltaEvent "PartDeltaEvent



      dataclass
   \(pydantic_ai.messages.PartDeltaEvent\)"),
) -> [EventT]

```

Handle a PartDeltaEvent.
This method dispatches to specific `handle_*_delta` methods based on part delta type:
  * [`TextPartDelta`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.TextPartDelta "TextPartDelta



      dataclass
  ") -> [`handle_text_delta()`](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.UIEventStream.handle_text_delta "handle_text_delta



      async
  ")
  * [`ThinkingPartDelta`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ThinkingPartDelta "ThinkingPartDelta



      dataclass
  ") -> [`handle_thinking_delta()`](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.UIEventStream.handle_thinking_delta "handle_thinking_delta



      async
  ")
  * [`ToolCallPartDelta`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPartDelta "ToolCallPartDelta



      dataclass
  ") -> [`handle_tool_call_delta()`](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.UIEventStream.handle_tool_call_delta "handle_tool_call_delta



      async
  ")


Subclasses are encouraged to override the individual `handle_*_delta` methods rather than this one. If you need specific behavior for all part delta events, make sure you call the super method.
Parameters:
Name | Type | Description | Default
---|---|---|---
`event` |  `PartDeltaEvent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.PartDeltaEvent "PartDeltaEvent



      dataclass
   \(pydantic_ai.messages.PartDeltaEvent\)")` |  The PartDeltaEvent. |  _required_
Source code in `pydantic_ai_slim/pydantic_ai/ui/_event_stream.py`
```
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
```
| ```
async def handle_part_delta(self, event: PartDeltaEvent) -> AsyncIterator[EventT]:
    """Handle a PartDeltaEvent.

    This method dispatches to specific `handle_*_delta` methods based on part delta type:

    - [`TextPartDelta`][pydantic_ai.messages.TextPartDelta] -> [`handle_text_delta()`][pydantic_ai.ui.UIEventStream.handle_text_delta]
    - [`ThinkingPartDelta`][pydantic_ai.messages.ThinkingPartDelta] -> [`handle_thinking_delta()`][pydantic_ai.ui.UIEventStream.handle_thinking_delta]
    - [`ToolCallPartDelta`][pydantic_ai.messages.ToolCallPartDelta] -> [`handle_tool_call_delta()`][pydantic_ai.ui.UIEventStream.handle_tool_call_delta]

    Subclasses are encouraged to override the individual `handle_*_delta` methods rather than this one.
    If you need specific behavior for all part delta events, make sure you call the super method.

    Args:
        event: The PartDeltaEvent.
    """
    delta = event.delta
    match delta:
        case TextPartDelta():
            async for e in self.handle_text_delta(delta):
                yield e
        case ThinkingPartDelta():
            async for e in self.handle_thinking_delta(delta):
                yield e
        case ToolCallPartDelta():  # pragma: no branch
            async for e in self.handle_tool_call_delta(delta):
                yield e

```

---|---
####  handle_part_end `async`
```
handle_part_end(
    event: PartEndEvent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.PartEndEvent "PartEndEvent



      dataclass
   \(pydantic_ai.messages.PartEndEvent\)"),
) -> [EventT]

```

Handle a `PartEndEvent`.
This method dispatches to specific `handle_*_end` methods based on part type:
  * [`TextPart`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.TextPart "TextPart



      dataclass
  ") -> [`handle_text_end()`](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.UIEventStream.handle_text_end "handle_text_end



      async
  ")
  * [`ThinkingPart`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ThinkingPart "ThinkingPart



      dataclass
  ") -> [`handle_thinking_end()`](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.UIEventStream.handle_thinking_end "handle_thinking_end



      async
  ")
  * [`ToolCallPart`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPart "ToolCallPart



      dataclass
  ") -> [`handle_tool_call_end()`](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.UIEventStream.handle_tool_call_end "handle_tool_call_end



      async
  ")
  * [`BuiltinToolCallPart`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BuiltinToolCallPart "BuiltinToolCallPart



      dataclass
  ") -> [`handle_builtin_tool_call_end()`](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.UIEventStream.handle_builtin_tool_call_end "handle_builtin_tool_call_end



      async
  ")


Subclasses are encouraged to override the individual `handle_*_end` methods rather than this one. If you need specific behavior for all part end events, make sure you call the super method.
Parameters:
Name | Type | Description | Default
---|---|---|---
`event` |  `PartEndEvent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.PartEndEvent "PartEndEvent



      dataclass
   \(pydantic_ai.messages.PartEndEvent\)")` |  The part end event. |  _required_
Source code in `pydantic_ai_slim/pydantic_ai/ui/_event_stream.py`
```
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
```
| ```
async def handle_part_end(self, event: PartEndEvent) -> AsyncIterator[EventT]:
    """Handle a `PartEndEvent`.

    This method dispatches to specific `handle_*_end` methods based on part type:

    - [`TextPart`][pydantic_ai.messages.TextPart] -> [`handle_text_end()`][pydantic_ai.ui.UIEventStream.handle_text_end]
    - [`ThinkingPart`][pydantic_ai.messages.ThinkingPart] -> [`handle_thinking_end()`][pydantic_ai.ui.UIEventStream.handle_thinking_end]
    - [`ToolCallPart`][pydantic_ai.messages.ToolCallPart] -> [`handle_tool_call_end()`][pydantic_ai.ui.UIEventStream.handle_tool_call_end]
    - [`BuiltinToolCallPart`][pydantic_ai.messages.BuiltinToolCallPart] -> [`handle_builtin_tool_call_end()`][pydantic_ai.ui.UIEventStream.handle_builtin_tool_call_end]

    Subclasses are encouraged to override the individual `handle_*_end` methods rather than this one.
    If you need specific behavior for all part end events, make sure you call the super method.

    Args:
        event: The part end event.
    """
    part = event.part
    next_part_kind = event.next_part_kind
    match part:
        case TextPart():
            async for e in self.handle_text_end(part, followed_by_text=next_part_kind == 'text'):
                yield e
        case ThinkingPart():
            async for e in self.handle_thinking_end(part, followed_by_thinking=next_part_kind == 'thinking'):
                yield e
        case ToolCallPart():
            async for e in self.handle_tool_call_end(part):
                yield e
        case BuiltinToolCallPart():
            async for e in self.handle_builtin_tool_call_end(part):
                yield e
        case BuiltinToolReturnPart() | FilePart():  # pragma: no cover
            # These don't have deltas, so they don't need to be ended.
            pass

```

---|---
####  before_stream `async`
```
before_stream() -> [EventT]

```

Yield events before agent streaming starts.
This hook is called before any agent events are processed. Override this to inject custom events at the start of the stream.
Source code in `pydantic_ai_slim/pydantic_ai/ui/_event_stream.py`
```
375
376
377
378
379
380
381
382
```
| ```
async def before_stream(self) -> AsyncIterator[EventT]:
    """Yield events before agent streaming starts.

    This hook is called before any agent events are processed.
    Override this to inject custom events at the start of the stream.
    """
    return  # pragma: no cover
    yield  # Make this an async generator

```

---|---
####  after_stream `async`
```
after_stream() -> [EventT]

```

Yield events after agent streaming completes.
This hook is called after all agent events have been processed. Override this to inject custom events at the end of the stream.
Source code in `pydantic_ai_slim/pydantic_ai/ui/_event_stream.py`
```
384
385
386
387
388
389
390
391
```
| ```
async def after_stream(self) -> AsyncIterator[EventT]:
    """Yield events after agent streaming completes.

    This hook is called after all agent events have been processed.
    Override this to inject custom events at the end of the stream.
    """
    return  # pragma: no cover
    yield  # Make this an async generator

```

---|---
####  on_error `async`
```
on_error(error: ) -> [EventT]

```

Handle errors that occur during streaming.
Parameters:
Name | Type | Description | Default
---|---|---|---
`error` |  |  The error that occurred during streaming. |  _required_
Source code in `pydantic_ai_slim/pydantic_ai/ui/_event_stream.py`
```
393
394
395
396
397
398
399
400
```
| ```
async def on_error(self, error: Exception) -> AsyncIterator[EventT]:
    """Handle errors that occur during streaming.

    Args:
        error: The error that occurred during streaming.
    """
    return  # pragma: no cover
    yield  # Make this an async generator

```

---|---
####  before_request `async`
```
before_request() -> [EventT]

```

Yield events before a model request is processed.
Override this to inject custom events at the start of the request.
Source code in `pydantic_ai_slim/pydantic_ai/ui/_event_stream.py`
```
402
403
404
405
406
407
408
```
| ```
async def before_request(self) -> AsyncIterator[EventT]:
    """Yield events before a model request is processed.

    Override this to inject custom events at the start of the request.
    """
    return  # pragma: lax no cover
    yield  # Make this an async generator

```

---|---
####  after_request `async`
```
after_request() -> [EventT]

```

Yield events after a model request is processed.
Override this to inject custom events at the end of the request.
Source code in `pydantic_ai_slim/pydantic_ai/ui/_event_stream.py`
```
410
411
412
413
414
415
416
```
| ```
async def after_request(self) -> AsyncIterator[EventT]:
    """Yield events after a model request is processed.

    Override this to inject custom events at the end of the request.
    """
    return  # pragma: lax no cover
    yield  # Make this an async generator

```

---|---
####  before_response `async`
```
before_response() -> [EventT]

```

Yield events before a model response is processed.
Override this to inject custom events at the start of the response.
Source code in `pydantic_ai_slim/pydantic_ai/ui/_event_stream.py`
```
418
419
420
421
422
423
424
```
| ```
async def before_response(self) -> AsyncIterator[EventT]:
    """Yield events before a model response is processed.

    Override this to inject custom events at the start of the response.
    """
    return  # pragma: no cover
    yield  # Make this an async generator

```

---|---
####  after_response `async`
```
after_response() -> [EventT]

```

Yield events after a model response is processed.
Override this to inject custom events at the end of the response.
Source code in `pydantic_ai_slim/pydantic_ai/ui/_event_stream.py`
```
426
427
428
429
430
431
432
```
| ```
async def after_response(self) -> AsyncIterator[EventT]:
    """Yield events after a model response is processed.

    Override this to inject custom events at the end of the response.
    """
    return  # pragma: lax no cover
    yield  # Make this an async generator

```

---|---
####  handle_text_start `async`
```
handle_text_start(
    part: TextPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.TextPart "TextPart



      dataclass
   \(pydantic_ai.messages.TextPart\)"), follows_text:  = False
) -> [EventT]

```

Handle the start of a `TextPart`.
Parameters:
Name | Type | Description | Default
---|---|---|---
`part` |  `TextPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.TextPart "TextPart



      dataclass
   \(pydantic_ai.messages.TextPart\)")` |  The text part. |  _required_
`follows_text` |  |  Whether the part is directly preceded by another text part. In this case, you may want to yield a "text-delta" event instead of a "text-start" event. |  `False`
Source code in `pydantic_ai_slim/pydantic_ai/ui/_event_stream.py`
```
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
async def handle_text_start(self, part: TextPart, follows_text: bool = False) -> AsyncIterator[EventT]:
    """Handle the start of a `TextPart`.

    Args:
        part: The text part.
        follows_text: Whether the part is directly preceded by another text part. In this case, you may want to yield a "text-delta" event instead of a "text-start" event.
    """
    return  # pragma: no cover
    yield  # Make this an async generator

```

---|---
####  handle_text_delta `async`
```
handle_text_delta(
    delta: TextPartDelta[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.TextPartDelta "TextPartDelta



      dataclass
   \(pydantic_ai.messages.TextPartDelta\)"),
) -> [EventT]

```

Handle a `TextPartDelta`.
Parameters:
Name | Type | Description | Default
---|---|---|---
`delta` |  `TextPartDelta[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.TextPartDelta "TextPartDelta



      dataclass
   \(pydantic_ai.messages.TextPartDelta\)")` |  The text part delta. |  _required_
Source code in `pydantic_ai_slim/pydantic_ai/ui/_event_stream.py`
```
444
445
446
447
448
449
450
451
```
| ```
async def handle_text_delta(self, delta: TextPartDelta) -> AsyncIterator[EventT]:
    """Handle a `TextPartDelta`.

    Args:
        delta: The text part delta.
    """
    return  # pragma: no cover
    yield  # Make this an async generator

```

---|---
####  handle_text_end `async`
```
handle_text_end(
    part: TextPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.TextPart "TextPart



      dataclass
   \(pydantic_ai.messages.TextPart\)"), followed_by_text:  = False
) -> [EventT]

```

Handle the end of a `TextPart`.
Parameters:
Name | Type | Description | Default
---|---|---|---
`part` |  `TextPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.TextPart "TextPart



      dataclass
   \(pydantic_ai.messages.TextPart\)")` |  The text part. |  _required_
`followed_by_text` |  |  Whether the part is directly followed by another text part. In this case, you may not want to yield a "text-end" event yet. |  `False`
Source code in `pydantic_ai_slim/pydantic_ai/ui/_event_stream.py`
```
453
454
455
456
457
458
459
460
461
```
| ```
async def handle_text_end(self, part: TextPart, followed_by_text: bool = False) -> AsyncIterator[EventT]:
    """Handle the end of a `TextPart`.

    Args:
        part: The text part.
        followed_by_text: Whether the part is directly followed by another text part. In this case, you may not want to yield a "text-end" event yet.
    """
    return  # pragma: no cover
    yield  # Make this an async generator

```

---|---
####  handle_thinking_start `async`
```
handle_thinking_start(
    part: ThinkingPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ThinkingPart "ThinkingPart



      dataclass
   \(pydantic_ai.messages.ThinkingPart\)"), follows_thinking:  = False
) -> [EventT]

```

Handle the start of a `ThinkingPart`.
Parameters:
Name | Type | Description | Default
---|---|---|---
`part` |  `ThinkingPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ThinkingPart "ThinkingPart



      dataclass
   \(pydantic_ai.messages.ThinkingPart\)")` |  The thinking part. |  _required_
`follows_thinking` |  |  Whether the part is directly preceded by another thinking part. In this case, you may want to yield a "thinking-delta" event instead of a "thinking-start" event. |  `False`
Source code in `pydantic_ai_slim/pydantic_ai/ui/_event_stream.py`
```
463
464
465
466
467
468
469
470
471
```
| ```
async def handle_thinking_start(self, part: ThinkingPart, follows_thinking: bool = False) -> AsyncIterator[EventT]:
    """Handle the start of a `ThinkingPart`.

    Args:
        part: The thinking part.
        follows_thinking: Whether the part is directly preceded by another thinking part. In this case, you may want to yield a "thinking-delta" event instead of a "thinking-start" event.
    """
    return  # pragma: no cover
    yield  # Make this an async generator

```

---|---
####  handle_thinking_delta `async`
```
handle_thinking_delta(
    delta: ThinkingPartDelta[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ThinkingPartDelta "ThinkingPartDelta
