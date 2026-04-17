                request=ModelRequest(
                    parts=[
                        UserPromptPart(
                            content='What is the capital of France?',
                            timestamp=datetime.datetime(...),
                        )
                    ],
                    timestamp=datetime.datetime(...),
                    run_id='...',
                )
            ),
            CallToolsNode(
                model_response=ModelResponse(
                    parts=[TextPart(content='The capital of France is Paris.')],
                    usage=RequestUsage(input_tokens=56, output_tokens=7),
                    model_name='gpt-5.2',
                    timestamp=datetime.datetime(...),
                    run_id='...',
                )
            ),
            End(data=FinalResult(output='The capital of France is Paris.')),
        ]
        '''
        print('Final result:', agent_run.result.output)
        #> Final result: The capital of France is Paris.

```

Parameters:
Name | Type | Description | Default
---|---|---|---
`node` |  `AgentNode[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)"), OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")]` |  The node to run next in the graph. |  _required_
Returns:
Type | Description
---|---
`AgentNode[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)"), OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")] | End[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.End "End



      dataclass
   \(pydantic_graph.End\)")[FinalResult[OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")]]` |  The next node returned by the graph logic, or an [`End`](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.End "End



      dataclass
  ") node if
`AgentNode[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)"), OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")] | End[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.End "End



      dataclass
   \(pydantic_graph.End\)")[FinalResult[OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")]]` |  the run has completed.
Source code in `pydantic_ai_slim/pydantic_ai/run.py`
```
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
```
| ```
async def next(
    self,
    node: _agent_graph.AgentNode[AgentDepsT, OutputDataT],
) -> _agent_graph.AgentNode[AgentDepsT, OutputDataT] | End[FinalResult[OutputDataT]]:
    """Manually drive the agent run by passing in the node you want to run next.

    This lets you inspect or mutate the node before continuing execution, or skip certain nodes
    under dynamic conditions. The agent run should be stopped when you return an [`End`][pydantic_graph.nodes.End]
    node.

    Example:
```python
    from pydantic_ai import Agent
    from pydantic_graph import End

    agent = Agent('openai:gpt-5.2')

    async def main():
        async with agent.iter('What is the capital of France?') as agent_run:
            next_node = agent_run.next_node  # start with the first node
            nodes = [next_node]
            while not isinstance(next_node, End):
                next_node = await agent_run.next(next_node)
                nodes.append(next_node)
            # Once `next_node` is an End, we've finished:
            print(nodes)
            '''
            [
                UserPromptNode(
                    user_prompt='What is the capital of France?',
                    instructions_functions=[],
                    system_prompts=(),
                    system_prompt_functions=[],
                    system_prompt_dynamic_functions={},
                ),
                ModelRequestNode(
                    request=ModelRequest(
                        parts=[
                            UserPromptPart(
                                content='What is the capital of France?',
                                timestamp=datetime.datetime(...),
                            )
                        ],
                        timestamp=datetime.datetime(...),
                        run_id='...',
                    )
                ),
                CallToolsNode(
                    model_response=ModelResponse(
                        parts=[TextPart(content='The capital of France is Paris.')],
                        usage=RequestUsage(input_tokens=56, output_tokens=7),
                        model_name='gpt-5.2',
                        timestamp=datetime.datetime(...),
                        run_id='...',
                    )
                ),
                End(data=FinalResult(output='The capital of France is Paris.')),
            ]
            '''
            print('Final result:', agent_run.result.output)
            #> Final result: The capital of France is Paris.
```

    Args:
        node: The node to run next in the graph.

    Returns:
        The next node returned by the graph logic, or an [`End`][pydantic_graph.nodes.End] node if
        the run has completed.
    """
    # Note: It might be nice to expose a synchronous interface for iteration, but we shouldn't do it
    # on this class, or else IDEs won't warn you if you accidentally use `for` instead of `async for` to iterate.
    task = [self._node_to_task(node)]
    try:
        task = await self._graph_run.next(task)
    except StopAsyncIteration:
        pass
    return self._task_to_node(task)

```

---|---
####  usage
```
usage() -> RunUsage[](https://ai.pydantic.dev/api/usage/#pydantic_ai.usage.RunUsage "RunUsage



      dataclass
   \(pydantic_ai.usage.RunUsage\)")

```

Get usage statistics for the run so far, including token usage, model requests, and so on.
Source code in `pydantic_ai_slim/pydantic_ai/run.py`
```
284
285
286
```
| ```
def usage(self) -> _usage.RunUsage:
    """Get usage statistics for the run so far, including token usage, model requests, and so on."""
    return self._graph_run.state.usage

```

---|---
####  metadata `property`
```
metadata: [, ] | None

```

Metadata associated with this agent run, if configured.
####  run_id `property`
```
run_id:

```

The unique identifier for the agent run.
###  AgentRunResult `dataclass`
Bases: `OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")]`
The final result of an agent run.
Source code in `pydantic_ai_slim/pydantic_ai/run.py`
```
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
```
| ```
@dataclasses.dataclass
class AgentRunResult(Generic[OutputDataT]):
    """The final result of an agent run."""

    output: OutputDataT
    """The output data from the agent run."""

    _output_tool_name: str | None = dataclasses.field(repr=False, compare=False, default=None)
    _state: _agent_graph.GraphAgentState = dataclasses.field(
        repr=False, compare=False, default_factory=_agent_graph.GraphAgentState
    )
    _new_message_index: int = dataclasses.field(repr=False, compare=False, default=0)
    _traceparent_value: str | None = dataclasses.field(repr=False, compare=False, default=None)

    @overload
    def _traceparent(self, *, required: Literal[False]) -> str | None: ...
    @overload
    def _traceparent(self) -> str: ...
    def _traceparent(self, *, required: bool = True) -> str | None:
        if self._traceparent_value is None and required:  # pragma: no cover
            raise AttributeError('No span was created for this agent run')
        return self._traceparent_value

    def _set_output_tool_return(self, return_content: str) -> list[_messages.ModelMessage]:
        """Set return content for the output tool.

        Useful if you want to continue the conversation and want to set the response to the output tool call.
        """
        if not self._output_tool_name:
            raise ValueError('Cannot set output tool return content when the return type is `str`.')

        messages = self._state.message_history
        last_message = messages[-1]
        for idx, part in enumerate(last_message.parts):
            if isinstance(part, _messages.ToolReturnPart) and part.tool_name == self._output_tool_name:
                # Only do deepcopy when we have to modify
                copied_messages = list(messages)
                copied_last = deepcopy(last_message)
                copied_last.parts[idx].content = return_content  # type: ignore[misc]
                copied_messages[-1] = copied_last
                return copied_messages

        raise LookupError(f'No tool call found with tool name {self._output_tool_name!r}.')

    def all_messages(self, *, output_tool_return_content: str | None = None) -> list[_messages.ModelMessage]:
        """Return the history of _messages.

        Args:
            output_tool_return_content: The return content of the tool call to set in the last message.
                This provides a convenient way to modify the content of the output tool call if you want to continue
                the conversation and want to set the response to the output tool call. If `None`, the last message will
                not be modified.

        Returns:
            List of messages.
        """
        if output_tool_return_content is not None:
            return self._set_output_tool_return(output_tool_return_content)
        else:
            return self._state.message_history

    def all_messages_json(self, *, output_tool_return_content: str | None = None) -> bytes:
        """Return all messages from [`all_messages`][pydantic_ai.agent.AgentRunResult.all_messages] as JSON bytes.

        Args:
            output_tool_return_content: The return content of the tool call to set in the last message.
                This provides a convenient way to modify the content of the output tool call if you want to continue
                the conversation and want to set the response to the output tool call. If `None`, the last message will
                not be modified.

        Returns:
            JSON bytes representing the messages.
        """
        return _messages.ModelMessagesTypeAdapter.dump_json(
            self.all_messages(output_tool_return_content=output_tool_return_content)
        )

    def new_messages(self, *, output_tool_return_content: str | None = None) -> list[_messages.ModelMessage]:
        """Return new messages associated with this run.

        Messages from older runs are excluded.

        Args:
            output_tool_return_content: The return content of the tool call to set in the last message.
                This provides a convenient way to modify the content of the output tool call if you want to continue
                the conversation and want to set the response to the output tool call. If `None`, the last message will
                not be modified.

        Returns:
            List of new messages.
        """
        return self.all_messages(output_tool_return_content=output_tool_return_content)[self._new_message_index :]

    def new_messages_json(self, *, output_tool_return_content: str | None = None) -> bytes:
        """Return new messages from [`new_messages`][pydantic_ai.agent.AgentRunResult.new_messages] as JSON bytes.

        Args:
            output_tool_return_content: The return content of the tool call to set in the last message.
                This provides a convenient way to modify the content of the output tool call if you want to continue
                the conversation and want to set the response to the output tool call. If `None`, the last message will
                not be modified.

        Returns:
            JSON bytes representing the new messages.
        """
        return _messages.ModelMessagesTypeAdapter.dump_json(
            self.new_messages(output_tool_return_content=output_tool_return_content)
        )

    @property
    def response(self) -> _messages.ModelResponse:
        """Return the last response from the message history."""
        # The response may not be the very last item if it contained an output tool call. See `CallToolsNode._handle_final_result`.
        for message in reversed(self.all_messages()):
            if isinstance(message, _messages.ModelResponse):
                return message
        raise ValueError('No response found in the message history')  # pragma: no cover

    # TODO (v2): Make this a property
    def usage(self) -> _usage.RunUsage:
        """Return the usage of the whole run."""
        return self._state.usage

    # TODO (v2): Make this a property
    def timestamp(self) -> datetime:
        """Return the timestamp of last response."""
        return self.response.timestamp

    @property
    def metadata(self) -> dict[str, Any] | None:
        """Metadata associated with this agent run, if configured."""
        return self._state.metadata

    @property
    def run_id(self) -> str:
        """The unique identifier for the agent run."""
        return self._state.run_id

```

---|---
####  output `instance-attribute`
```
output: OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")

```

The output data from the agent run.
####  all_messages
```
all_messages(
    *, output_tool_return_content:  | None = None
) -> [ModelMessage[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelMessage "ModelMessage



      module-attribute
   \(pydantic_ai.messages.ModelMessage\)")]

```

Return the history of _messages.
Parameters:
Name | Type | Description | Default
---|---|---|---
`output_tool_return_content` |  |  The return content of the tool call to set in the last message. This provides a convenient way to modify the content of the output tool call if you want to continue the conversation and want to set the response to the output tool call. If `None`, the last message will not be modified. |  `None`
Returns:
Type | Description
---|---
`ModelMessage[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelMessage "ModelMessage



      module-attribute
   \(pydantic_ai.messages.ModelMessage\)")]` |  List of messages.
Source code in `pydantic_ai_slim/pydantic_ai/run.py`
```
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
```
| ```
def all_messages(self, *, output_tool_return_content: str | None = None) -> list[_messages.ModelMessage]:
    """Return the history of _messages.

    Args:
        output_tool_return_content: The return content of the tool call to set in the last message.
            This provides a convenient way to modify the content of the output tool call if you want to continue
            the conversation and want to set the response to the output tool call. If `None`, the last message will
            not be modified.

    Returns:
        List of messages.
    """
    if output_tool_return_content is not None:
        return self._set_output_tool_return(output_tool_return_content)
    else:
        return self._state.message_history

```

---|---
####  all_messages_json
```
all_messages_json(
    *, output_tool_return_content:  | None = None
) ->

```

Return all messages from [`all_messages`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AgentRunResult.all_messages "all_messages") as JSON bytes.
Parameters:
Name | Type | Description | Default
---|---|---|---
`output_tool_return_content` |  |  The return content of the tool call to set in the last message. This provides a convenient way to modify the content of the output tool call if you want to continue the conversation and want to set the response to the output tool call. If `None`, the last message will not be modified. |  `None`
Returns:
Type | Description
---|---
|  JSON bytes representing the messages.
Source code in `pydantic_ai_slim/pydantic_ai/run.py`
```
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
```
| ```
def all_messages_json(self, *, output_tool_return_content: str | None = None) -> bytes:
    """Return all messages from [`all_messages`][pydantic_ai.agent.AgentRunResult.all_messages] as JSON bytes.

    Args:
        output_tool_return_content: The return content of the tool call to set in the last message.
            This provides a convenient way to modify the content of the output tool call if you want to continue
            the conversation and want to set the response to the output tool call. If `None`, the last message will
            not be modified.

    Returns:
        JSON bytes representing the messages.
    """
    return _messages.ModelMessagesTypeAdapter.dump_json(
        self.all_messages(output_tool_return_content=output_tool_return_content)
    )

```

---|---
####  new_messages
```
new_messages(
    *, output_tool_return_content:  | None = None
) -> [ModelMessage[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelMessage "ModelMessage



      module-attribute
   \(pydantic_ai.messages.ModelMessage\)")]

```

Return new messages associated with this run.
Messages from older runs are excluded.
Parameters:
Name | Type | Description | Default
---|---|---|---
`output_tool_return_content` |  |  The return content of the tool call to set in the last message. This provides a convenient way to modify the content of the output tool call if you want to continue the conversation and want to set the response to the output tool call. If `None`, the last message will not be modified. |  `None`
Returns:
Type | Description
---|---
`ModelMessage[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelMessage "ModelMessage



      module-attribute
   \(pydantic_ai.messages.ModelMessage\)")]` |  List of new messages.
Source code in `pydantic_ai_slim/pydantic_ai/run.py`
```
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
```
| ```
def new_messages(self, *, output_tool_return_content: str | None = None) -> list[_messages.ModelMessage]:
    """Return new messages associated with this run.

    Messages from older runs are excluded.

    Args:
        output_tool_return_content: The return content of the tool call to set in the last message.
            This provides a convenient way to modify the content of the output tool call if you want to continue
            the conversation and want to set the response to the output tool call. If `None`, the last message will
            not be modified.

    Returns:
        List of new messages.
    """
    return self.all_messages(output_tool_return_content=output_tool_return_content)[self._new_message_index :]

```

---|---
####  new_messages_json
```
new_messages_json(
    *, output_tool_return_content:  | None = None
) ->

```

Return new messages from [`new_messages`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AgentRunResult.new_messages "new_messages") as JSON bytes.
Parameters:
Name | Type | Description | Default
---|---|---|---
`output_tool_return_content` |  |  The return content of the tool call to set in the last message. This provides a convenient way to modify the content of the output tool call if you want to continue the conversation and want to set the response to the output tool call. If `None`, the last message will not be modified. |  `None`
Returns:
Type | Description
---|---
|  JSON bytes representing the new messages.
Source code in `pydantic_ai_slim/pydantic_ai/run.py`
```
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
```
| ```
def new_messages_json(self, *, output_tool_return_content: str | None = None) -> bytes:
    """Return new messages from [`new_messages`][pydantic_ai.agent.AgentRunResult.new_messages] as JSON bytes.

    Args:
        output_tool_return_content: The return content of the tool call to set in the last message.
            This provides a convenient way to modify the content of the output tool call if you want to continue
            the conversation and want to set the response to the output tool call. If `None`, the last message will
            not be modified.

    Returns:
        JSON bytes representing the new messages.
    """
    return _messages.ModelMessagesTypeAdapter.dump_json(
        self.new_messages(output_tool_return_content=output_tool_return_content)
    )

```

---|---
####  response `property`
```
response: ModelResponse[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse "ModelResponse



      dataclass
   \(pydantic_ai.messages.ModelResponse\)")

```

Return the last response from the message history.
####  usage
```
usage() -> RunUsage[](https://ai.pydantic.dev/api/usage/#pydantic_ai.usage.RunUsage "RunUsage



      dataclass
   \(pydantic_ai.usage.RunUsage\)")

```

Return the usage of the whole run.
Source code in `pydantic_ai_slim/pydantic_ai/run.py`
```
423
424
425
```
| ```
def usage(self) -> _usage.RunUsage:
    """Return the usage of the whole run."""
    return self._state.usage

```

---|---
####  timestamp
```
timestamp() ->

```

Return the timestamp of last response.
Source code in `pydantic_ai_slim/pydantic_ai/run.py`
```
428
429
430
```
| ```
def timestamp(self) -> datetime:
    """Return the timestamp of last response."""
    return self.response.timestamp

```

---|---
####  metadata `property`
```
metadata: [, ] | None

```

Metadata associated with this agent run, if configured.
####  run_id `property`
```
run_id:

```

The unique identifier for the agent run.
###  EndStrategy `module-attribute`
```
EndStrategy = ['early', 'exhaustive']

```

###  RunOutputDataT `module-attribute`
```
RunOutputDataT = TypeVar('RunOutputDataT')

```

Type variable for the result data of a run where `output_type` was customized on the run call.
###  capture_run_messages
```
capture_run_messages() -> [[ModelMessage[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelMessage "ModelMessage



      module-attribute
   \(pydantic_ai.messages.ModelMessage\)")]]

```

Context manager to access the messages used in a [`run`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AbstractAgent.run "run



      async
  "), [`run_sync`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AbstractAgent.run_sync "run_sync"), or [`run_stream`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AbstractAgent.run_stream "run_stream



      async
  ") call.
Useful when a run may raise an exception, see [model errors](https://ai.pydantic.dev/agent/#model-errors) for more information.
Examples:
```
from pydantic_ai import Agent, capture_run_messages

agent = Agent('test')

with capture_run_messages() as messages:
    try:
        result = agent.run_sync('foobar')
    except Exception:
        print(messages)
        raise

```

Note
If you call `run`, `run_sync`, or `run_stream` more than once within a single `capture_run_messages` context, `messages` will represent the messages exchanged during the first call only.
Source code in `pydantic_ai_slim/pydantic_ai/_agent_graph.py`
```
1420
1421
1422
1423
1424
1425
1426
1427
1428
1429
1430
1431
1432
1433
1434
1435
1436
1437
1438
1439
1440
1441
1442
1443
1444
1445
1446
1447
1448
1449
1450
1451
1452
1453
1454
1455
1456
1457
1458
1459
```
| ```
@contextmanager
def capture_run_messages() -> Iterator[list[_messages.ModelMessage]]:
    """Context manager to access the messages used in a [`run`][pydantic_ai.agent.AbstractAgent.run], [`run_sync`][pydantic_ai.agent.AbstractAgent.run_sync], or [`run_stream`][pydantic_ai.agent.AbstractAgent.run_stream] call.

    Useful when a run may raise an exception, see [model errors](../agent.md#model-errors) for more information.

    Examples:
```python
    from pydantic_ai import Agent, capture_run_messages

    agent = Agent('test')

    with capture_run_messages() as messages:
        try:
            result = agent.run_sync('foobar')
        except Exception:
            print(messages)
            raise
```

    !!! note
        If you call `run`, `run_sync`, or `run_stream` more than once within a single `capture_run_messages` context,
