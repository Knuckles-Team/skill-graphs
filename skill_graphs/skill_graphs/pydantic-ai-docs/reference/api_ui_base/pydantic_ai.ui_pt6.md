


      dataclass
   \(pydantic_ai.messages.ThinkingPartDelta\)"),
) -> [EventT]

```

Handle a `ThinkingPartDelta`.
Parameters:
Name | Type | Description | Default
---|---|---|---
`delta` |  `ThinkingPartDelta[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ThinkingPartDelta "ThinkingPartDelta



      dataclass
   \(pydantic_ai.messages.ThinkingPartDelta\)")` |  The thinking part delta. |  _required_
Source code in `pydantic_ai_slim/pydantic_ai/ui/_event_stream.py`
```
473
474
475
476
477
478
479
480
```
| ```
async def handle_thinking_delta(self, delta: ThinkingPartDelta) -> AsyncIterator[EventT]:
    """Handle a `ThinkingPartDelta`.

    Args:
        delta: The thinking part delta.
    """
    return  # pragma: no cover
    yield  # Make this an async generator

```

---|---
####  handle_thinking_end `async`
```
handle_thinking_end(
    part: ThinkingPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ThinkingPart "ThinkingPart



      dataclass
   \(pydantic_ai.messages.ThinkingPart\)"), followed_by_thinking:  = False
) -> [EventT]

```

Handle the end of a `ThinkingPart`.
Parameters:
Name | Type | Description | Default
---|---|---|---
`part` |  `ThinkingPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ThinkingPart "ThinkingPart



      dataclass
   \(pydantic_ai.messages.ThinkingPart\)")` |  The thinking part. |  _required_
`followed_by_thinking` |  |  Whether the part is directly followed by another thinking part. In this case, you may not want to yield a "thinking-end" event yet. |  `False`
Source code in `pydantic_ai_slim/pydantic_ai/ui/_event_stream.py`
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
```
| ```
async def handle_thinking_end(
    self, part: ThinkingPart, followed_by_thinking: bool = False
) -> AsyncIterator[EventT]:
    """Handle the end of a `ThinkingPart`.

    Args:
        part: The thinking part.
        followed_by_thinking: Whether the part is directly followed by another thinking part. In this case, you may not want to yield a "thinking-end" event yet.
    """
    return  # pragma: no cover
    yield  # Make this an async generator

```

---|---
####  handle_tool_call_start `async`
```
handle_tool_call_start(
    part: ToolCallPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPart "ToolCallPart



      dataclass
   \(pydantic_ai.messages.ToolCallPart\)"),
) -> [EventT]

```

Handle the start of a `ToolCallPart`.
Parameters:
Name | Type | Description | Default
---|---|---|---
`part` |  `ToolCallPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPart "ToolCallPart



      dataclass
   \(pydantic_ai.messages.ToolCallPart\)")` |  The tool call part. |  _required_
Source code in `pydantic_ai_slim/pydantic_ai/ui/_event_stream.py`
```
494
495
496
497
498
499
500
501
```
| ```
async def handle_tool_call_start(self, part: ToolCallPart) -> AsyncIterator[EventT]:
    """Handle the start of a `ToolCallPart`.

    Args:
        part: The tool call part.
    """
    return  # pragma: no cover
    yield  # Make this an async generator

```

---|---
####  handle_tool_call_delta `async`
```
handle_tool_call_delta(
    delta: ToolCallPartDelta[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPartDelta "ToolCallPartDelta



      dataclass
   \(pydantic_ai.messages.ToolCallPartDelta\)"),
) -> [EventT]

```

Handle a `ToolCallPartDelta`.
Parameters:
Name | Type | Description | Default
---|---|---|---
`delta` |  `ToolCallPartDelta[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPartDelta "ToolCallPartDelta



      dataclass
   \(pydantic_ai.messages.ToolCallPartDelta\)")` |  The tool call part delta. |  _required_
Source code in `pydantic_ai_slim/pydantic_ai/ui/_event_stream.py`
```
503
504
505
506
507
508
509
510
```
| ```
async def handle_tool_call_delta(self, delta: ToolCallPartDelta) -> AsyncIterator[EventT]:
    """Handle a `ToolCallPartDelta`.

    Args:
        delta: The tool call part delta.
    """
    return  # pragma: no cover
    yield  # Make this an async generator

```

---|---
####  handle_tool_call_end `async`
```
handle_tool_call_end(
    part: ToolCallPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPart "ToolCallPart



      dataclass
   \(pydantic_ai.messages.ToolCallPart\)"),
) -> [EventT]

```

Handle the end of a `ToolCallPart`.
Parameters:
Name | Type | Description | Default
---|---|---|---
`part` |  `ToolCallPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPart "ToolCallPart



      dataclass
   \(pydantic_ai.messages.ToolCallPart\)")` |  The tool call part. |  _required_
Source code in `pydantic_ai_slim/pydantic_ai/ui/_event_stream.py`
```
512
513
514
515
516
517
518
519
```
| ```
async def handle_tool_call_end(self, part: ToolCallPart) -> AsyncIterator[EventT]:
    """Handle the end of a `ToolCallPart`.

    Args:
        part: The tool call part.
    """
    return  # pragma: no cover
    yield  # Make this an async generator

```

---|---
####  handle_builtin_tool_call_start `async`
```
handle_builtin_tool_call_start(
    part: BuiltinToolCallPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BuiltinToolCallPart "BuiltinToolCallPart



      dataclass
   \(pydantic_ai.messages.BuiltinToolCallPart\)"),
) -> [EventT]

```

Handle a `BuiltinToolCallPart` at start.
Parameters:
Name | Type | Description | Default
---|---|---|---
`part` |  `BuiltinToolCallPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BuiltinToolCallPart "BuiltinToolCallPart



      dataclass
   \(pydantic_ai.messages.BuiltinToolCallPart\)")` |  The builtin tool call part. |  _required_
Source code in `pydantic_ai_slim/pydantic_ai/ui/_event_stream.py`
```
521
522
523
524
525
526
527
528
```
| ```
async def handle_builtin_tool_call_start(self, part: BuiltinToolCallPart) -> AsyncIterator[EventT]:
    """Handle a `BuiltinToolCallPart` at start.

    Args:
        part: The builtin tool call part.
    """
    return  # pragma: no cover
    yield  # Make this an async generator

```

---|---
####  handle_builtin_tool_call_end `async`
```
handle_builtin_tool_call_end(
    part: BuiltinToolCallPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BuiltinToolCallPart "BuiltinToolCallPart



      dataclass
   \(pydantic_ai.messages.BuiltinToolCallPart\)"),
) -> [EventT]

```

Handle the end of a `BuiltinToolCallPart`.
Parameters:
Name | Type | Description | Default
---|---|---|---
`part` |  `BuiltinToolCallPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BuiltinToolCallPart "BuiltinToolCallPart



      dataclass
   \(pydantic_ai.messages.BuiltinToolCallPart\)")` |  The builtin tool call part. |  _required_
Source code in `pydantic_ai_slim/pydantic_ai/ui/_event_stream.py`
```
530
531
532
533
534
535
536
537
```
| ```
async def handle_builtin_tool_call_end(self, part: BuiltinToolCallPart) -> AsyncIterator[EventT]:
    """Handle the end of a `BuiltinToolCallPart`.

    Args:
        part: The builtin tool call part.
    """
    return  # pragma: no cover
    yield  # Make this an async generator

```

---|---
####  handle_builtin_tool_return `async`
```
handle_builtin_tool_return(
    part: BuiltinToolReturnPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BuiltinToolReturnPart "BuiltinToolReturnPart



      dataclass
   \(pydantic_ai.messages.BuiltinToolReturnPart\)"),
) -> [EventT]

```

Handle a `BuiltinToolReturnPart`.
Parameters:
Name | Type | Description | Default
---|---|---|---
`part` |  `BuiltinToolReturnPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BuiltinToolReturnPart "BuiltinToolReturnPart



      dataclass
   \(pydantic_ai.messages.BuiltinToolReturnPart\)")` |  The builtin tool return part. |  _required_
Source code in `pydantic_ai_slim/pydantic_ai/ui/_event_stream.py`
```
539
540
541
542
543
544
545
546
```
| ```
async def handle_builtin_tool_return(self, part: BuiltinToolReturnPart) -> AsyncIterator[EventT]:
    """Handle a `BuiltinToolReturnPart`.

    Args:
        part: The builtin tool return part.
    """
    return  # pragma: no cover
    yield  # Make this an async generator

```

---|---
####  handle_file `async`
```
handle_file(part: FilePart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FilePart "FilePart



      dataclass
   \(pydantic_ai.messages.FilePart\)")) -> [EventT]

```

Handle a `FilePart`.
Parameters:
Name | Type | Description | Default
---|---|---|---
`part` |  `FilePart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FilePart "FilePart



      dataclass
   \(pydantic_ai.messages.FilePart\)")` |  The file part. |  _required_
Source code in `pydantic_ai_slim/pydantic_ai/ui/_event_stream.py`
```
548
549
550
551
552
553
554
555
```
| ```
async def handle_file(self, part: FilePart) -> AsyncIterator[EventT]:
    """Handle a `FilePart`.

    Args:
        part: The file part.
    """
    return  # pragma: no cover
    yield  # Make this an async generator

```

---|---
####  handle_final_result `async`
```
handle_final_result(
    event: FinalResultEvent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FinalResultEvent "FinalResultEvent



      dataclass
   \(pydantic_ai.messages.FinalResultEvent\)"),
) -> [EventT]

```

Handle a `FinalResultEvent`.
Parameters:
Name | Type | Description | Default
---|---|---|---
`event` |  `FinalResultEvent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FinalResultEvent "FinalResultEvent



      dataclass
   \(pydantic_ai.messages.FinalResultEvent\)")` |  The final result event. |  _required_
Source code in `pydantic_ai_slim/pydantic_ai/ui/_event_stream.py`
```
557
558
559
560
561
562
563
564
```
| ```
async def handle_final_result(self, event: FinalResultEvent) -> AsyncIterator[EventT]:
    """Handle a `FinalResultEvent`.

    Args:
        event: The final result event.
    """
    return
    yield  # Make this an async generator

```

---|---
####  handle_function_tool_call `async`
```
handle_function_tool_call(
    event: FunctionToolCallEvent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FunctionToolCallEvent "FunctionToolCallEvent



      dataclass
   \(pydantic_ai.messages.FunctionToolCallEvent\)"),
) -> [EventT]

```

Handle a `FunctionToolCallEvent`.
Parameters:
Name | Type | Description | Default
---|---|---|---
`event` |  `FunctionToolCallEvent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FunctionToolCallEvent "FunctionToolCallEvent



      dataclass
   \(pydantic_ai.messages.FunctionToolCallEvent\)")` |  The function tool call event. |  _required_
Source code in `pydantic_ai_slim/pydantic_ai/ui/_event_stream.py`
```
566
567
568
569
570
571
572
573
```
| ```
async def handle_function_tool_call(self, event: FunctionToolCallEvent) -> AsyncIterator[EventT]:
    """Handle a `FunctionToolCallEvent`.

    Args:
        event: The function tool call event.
    """
    return
    yield  # Make this an async generator

```

---|---
####  handle_function_tool_result `async`
```
handle_function_tool_result(
    event: FunctionToolResultEvent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FunctionToolResultEvent "FunctionToolResultEvent



      dataclass
   \(pydantic_ai.messages.FunctionToolResultEvent\)"),
) -> [EventT]

```

Handle a `FunctionToolResultEvent`.
Parameters:
Name | Type | Description | Default
---|---|---|---
`event` |  `FunctionToolResultEvent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FunctionToolResultEvent "FunctionToolResultEvent



      dataclass
   \(pydantic_ai.messages.FunctionToolResultEvent\)")` |  The function tool result event. |  _required_
Source code in `pydantic_ai_slim/pydantic_ai/ui/_event_stream.py`
```
575
576
577
578
579
580
581
582
```
| ```
async def handle_function_tool_result(self, event: FunctionToolResultEvent) -> AsyncIterator[EventT]:
    """Handle a `FunctionToolResultEvent`.

    Args:
        event: The function tool result event.
    """
    return  # pragma: no cover
    yield  # Make this an async generator

```

---|---
####  handle_run_result `async`
```
handle_run_result(
    event: AgentRunResultEvent[](https://ai.pydantic.dev/api/run/#pydantic_ai.run.AgentRunResultEvent "AgentRunResultEvent



      dataclass
   \(pydantic_ai.run.AgentRunResultEvent\)"),
) -> [EventT]

```

Handle an `AgentRunResultEvent`.
Parameters:
Name | Type | Description | Default
---|---|---|---
`event` |  `AgentRunResultEvent[](https://ai.pydantic.dev/api/run/#pydantic_ai.run.AgentRunResultEvent "AgentRunResultEvent



      dataclass
   \(pydantic_ai.run.AgentRunResultEvent\)")` |  The agent run result event. |  _required_
Source code in `pydantic_ai_slim/pydantic_ai/ui/_event_stream.py`
```
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
async def handle_run_result(self, event: AgentRunResultEvent) -> AsyncIterator[EventT]:
    """Handle an `AgentRunResultEvent`.

    Args:
        event: The agent run result event.
    """
    return
    yield  # Make this an async generator

```

---|---
###  MessagesBuilder `dataclass`
Helper class to build Pydantic AI messages from request/response parts.
Source code in `pydantic_ai_slim/pydantic_ai/ui/_messages_builder.py`
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
```
| ```
@dataclass
class MessagesBuilder:
    """Helper class to build Pydantic AI messages from request/response parts."""

    messages: list[ModelMessage] = field(default_factory=list[ModelMessage])

    def add(self, part: ModelRequestPart | ModelResponsePart) -> None:
        """Add a new part, creating a new request or response message if necessary."""
        last_message = self.messages[-1] if self.messages else None
        if isinstance(part, get_union_args(ModelRequestPart)):
            part = cast(ModelRequestPart, part)
            if isinstance(last_message, ModelRequest):
                last_message.parts = [*last_message.parts, part]
            else:
                self.messages.append(ModelRequest(parts=[part]))
        else:
            part = cast(ModelResponsePart, part)
            if isinstance(last_message, ModelResponse):
                last_message.parts = [*last_message.parts, part]
            else:
                self.messages.append(ModelResponse(parts=[part]))

```

---|---
####  add
```
add(part: ModelRequestPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelRequestPart "ModelRequestPart



      module-attribute
   \(pydantic_ai.messages.ModelRequestPart\)") | ModelResponsePart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponsePart "ModelResponsePart



      module-attribute
   \(pydantic_ai.messages.ModelResponsePart\)")) -> None

```

Add a new part, creating a new request or response message if necessary.
Source code in `pydantic_ai_slim/pydantic_ai/ui/_messages_builder.py`
```
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
```
| ```
def add(self, part: ModelRequestPart | ModelResponsePart) -> None:
    """Add a new part, creating a new request or response message if necessary."""
    last_message = self.messages[-1] if self.messages else None
    if isinstance(part, get_union_args(ModelRequestPart)):
        part = cast(ModelRequestPart, part)
        if isinstance(last_message, ModelRequest):
            last_message.parts = [*last_message.parts, part]
        else:
            self.messages.append(ModelRequest(parts=[part]))
    else:
        part = cast(ModelResponsePart, part)
        if isinstance(last_message, ModelResponse):
            last_message.parts = [*last_message.parts, part]
        else:
            self.messages.append(ModelResponse(parts=[part]))

```

---|---
© Pydantic Services Inc. 2024 to present
