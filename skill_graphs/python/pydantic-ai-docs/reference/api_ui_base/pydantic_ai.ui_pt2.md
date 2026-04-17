


      module-attribute
   \(pydantic_ai.output.OutputDataT\)")
    ]
)

```

Build a protocol-specific event stream transformer.
Source code in `pydantic_ai_slim/pydantic_ai/ui/_adapter.py`
```
161
162
163
164
```
| ```
@abstractmethod
def build_event_stream(self) -> UIEventStream[RunInputT, EventT, AgentDepsT, OutputDataT]:
    """Build a protocol-specific event stream transformer."""
    raise NotImplementedError

```

---|---
####  messages `abstractmethod` `cached` `property`
```
messages: [ModelMessage[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelMessage "ModelMessage



      module-attribute
   \(pydantic_ai.messages.ModelMessage\)")]

```

Pydantic AI messages from the protocol-specific run input.
####  toolset `cached` `property`
```
toolset: AbstractToolset[](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.AbstractToolset "AbstractToolset \(pydantic_ai.toolsets.AbstractToolset\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")] | None

```

Toolset representing frontend tools from the protocol-specific run input.
####  state `cached` `property`
```
state: [, ] | None

```

Frontend state from the protocol-specific run input.
####  deferred_tool_results `cached` `property`
```
deferred_tool_results: DeferredToolResults[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.DeferredToolResults "DeferredToolResults



      dataclass
   \(pydantic_ai.DeferredToolResults\)") | None

```

Deferred tool results extracted from the request, used for tool approval workflows.
####  transform_stream
```
transform_stream(
    stream: [NativeEvent[](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.NativeEvent "NativeEvent



      module-attribute
   \(pydantic_ai.ui._event_stream.NativeEvent\)")],
    on_complete: OnCompleteFunc[](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.OnCompleteFunc "OnCompleteFunc



      module-attribute
   \(pydantic_ai.ui._event_stream.OnCompleteFunc\)")[EventT] | None = None,
) -> [EventT]

```

Transform a stream of Pydantic AI events into protocol-specific events.
Parameters:
Name | Type | Description | Default
---|---|---|---
`stream` |  `NativeEvent[](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.NativeEvent "NativeEvent



      module-attribute
   \(pydantic_ai.ui._event_stream.NativeEvent\)")]` |  The stream of Pydantic AI events to transform. |  _required_
`on_complete` |  `OnCompleteFunc[](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.OnCompleteFunc "OnCompleteFunc



      module-attribute
   \(pydantic_ai.ui._event_stream.OnCompleteFunc\)")[EventT] | None` |  Optional callback function called when the agent run completes successfully. The callback receives the completed [`AgentRunResult`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AgentRunResult "AgentRunResult



      dataclass
  ") and can optionally yield additional protocol-specific events. |  `None`
Source code in `pydantic_ai_slim/pydantic_ai/ui/_adapter.py`
```
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
```
| ```
def transform_stream(
    self,
    stream: AsyncIterator[NativeEvent],
    on_complete: OnCompleteFunc[EventT] | None = None,
) -> AsyncIterator[EventT]:
    """Transform a stream of Pydantic AI events into protocol-specific events.

    Args:
        stream: The stream of Pydantic AI events to transform.
        on_complete: Optional callback function called when the agent run completes successfully.
            The callback receives the completed [`AgentRunResult`][pydantic_ai.agent.AgentRunResult] and can optionally yield additional protocol-specific events.
    """
    return self.build_event_stream().transform_stream(stream, on_complete=on_complete)

```

---|---
####  encode_stream
```
encode_stream(
    stream: [EventT],
) -> []

```

Encode a stream of protocol-specific events as strings according to the `Accept` header value.
Parameters:
Name | Type | Description | Default
---|---|---|---
`stream` |  `EventT]` |  The stream of protocol-specific events to encode. |  _required_
Source code in `pydantic_ai_slim/pydantic_ai/ui/_adapter.py`
```
201
202
203
204
205
206
207
```
| ```
def encode_stream(self, stream: AsyncIterator[EventT]) -> AsyncIterator[str]:
    """Encode a stream of protocol-specific events as strings according to the `Accept` header value.

    Args:
        stream: The stream of protocol-specific events to encode.
    """
    return self.build_event_stream().encode_stream(stream)

```

---|---
####  streaming_response
```
streaming_response(
    stream: [EventT],
) ->

```

Generate a streaming response from a stream of protocol-specific events.
Parameters:
Name | Type | Description | Default
---|---|---|---
`stream` |  `EventT]` |  The stream of protocol-specific events to encode. |  _required_
Source code in `pydantic_ai_slim/pydantic_ai/ui/_adapter.py`
```
209
210
211
212
213
214
215
```
| ```
def streaming_response(self, stream: AsyncIterator[EventT]) -> StreamingResponse:
    """Generate a streaming response from a stream of protocol-specific events.

    Args:
        stream: The stream of protocol-specific events to encode.
    """
    return self.build_event_stream().streaming_response(stream)

```

---|---
####  run_stream_native
```
run_stream_native(
    *,
    output_type: OutputSpec[] | None = None,
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
    instructions: Instructions[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")] = None,
    deps: AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)") = None,
    model_settings: ModelSettings[](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings \(pydantic_ai.settings.ModelSettings\)") | None = None,
    usage_limits: UsageLimits[](https://ai.pydantic.dev/api/usage/#pydantic_ai.usage.UsageLimits "UsageLimits



      dataclass
   \(pydantic_ai.usage.UsageLimits\)") | None = None,
    usage: RunUsage[](https://ai.pydantic.dev/api/usage/#pydantic_ai.usage.RunUsage "RunUsage



      dataclass
   \(pydantic_ai.usage.RunUsage\)") | None = None,
    metadata: AgentMetadata[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")] | None = None,
    infer_name:  = True,
    toolsets: (
        [AbstractToolset[](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.AbstractToolset "AbstractToolset \(pydantic_ai.toolsets.AbstractToolset\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]] | None
    ) = None,
    builtin_tools: (
        [AbstractBuiltinTool[](https://ai.pydantic.dev/api/builtin_tools/#pydantic_ai.builtin_tools.AbstractBuiltinTool "AbstractBuiltinTool



      dataclass
   \(pydantic_ai.builtin_tools.AbstractBuiltinTool\)")] | None
    ) = None
) -> [NativeEvent[](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.NativeEvent "NativeEvent



      module-attribute
   \(pydantic_ai.ui._event_stream.NativeEvent\)")]

```

Run the agent with the protocol-specific run input and stream Pydantic AI events.
Parameters:
Name | Type | Description | Default
---|---|---|---
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
`instructions` |  `Instructions[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]` |  Optional additional instructions to use for this run. |  `None`
`deps` |  `AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")` |  Optional dependencies to use for this run. |  `None`
`model_settings` |  `ModelSettings[](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings \(pydantic_ai.settings.ModelSettings\)") | None` |  Optional settings to use for this model's request. |  `None`
`usage_limits` |  `UsageLimits[](https://ai.pydantic.dev/api/usage/#pydantic_ai.usage.UsageLimits "UsageLimits



      dataclass
   \(pydantic_ai.usage.UsageLimits\)") | None` |  Optional limits on model request count or token usage. |  `None`
`usage` |  `RunUsage[](https://ai.pydantic.dev/api/usage/#pydantic_ai.usage.RunUsage "RunUsage



      dataclass
   \(pydantic_ai.usage.RunUsage\)") | None` |  Optional usage to start with, useful for resuming a conversation or agents used in tools. |  `None`
`metadata` |  `AgentMetadata[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")] | None` |  Optional metadata to attach to this run. Accepts a dictionary or a callable taking [`RunContext`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext



      dataclass
  "); merged with the agent's configured metadata. |  `None`
`infer_name` |  |  Whether to try to infer the agent name from the call frame if it's not set. |  `True`
`toolsets` |  `AbstractToolset[](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.AbstractToolset "AbstractToolset \(pydantic_ai.toolsets.AbstractToolset\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]] | None` |  Optional additional toolsets for this run. |  `None`
`builtin_tools` |  `AbstractBuiltinTool[](https://ai.pydantic.dev/api/builtin_tools/#pydantic_ai.builtin_tools.AbstractBuiltinTool "AbstractBuiltinTool



      dataclass
   \(pydantic_ai.builtin_tools.AbstractBuiltinTool\)")] | None` |  Optional additional builtin tools to use for this run. |  `None`
Source code in `pydantic_ai_slim/pydantic_ai/ui/_adapter.py`
```
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
```
| ```
def run_stream_native(
    self,
    *,
    output_type: OutputSpec[Any] | None = None,
    message_history: Sequence[ModelMessage] | None = None,
    deferred_tool_results: DeferredToolResults | None = None,
    model: Model | KnownModelName | str | None = None,
    instructions: Instructions[AgentDepsT] = None,
    deps: AgentDepsT = None,
    model_settings: ModelSettings | None = None,
    usage_limits: UsageLimits | None = None,
    usage: RunUsage | None = None,
    metadata: AgentMetadata[AgentDepsT] | None = None,
    infer_name: bool = True,
    toolsets: Sequence[AbstractToolset[AgentDepsT]] | None = None,
    builtin_tools: Sequence[AbstractBuiltinTool] | None = None,
) -> AsyncIterator[NativeEvent]:
    """Run the agent with the protocol-specific run input and stream Pydantic AI events.

    Args:
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
    """
    message_history = [*(message_history or []), *self.messages]

    toolset = self.toolset
    if toolset:
        output_type = [output_type or self.agent.output_type, DeferredToolRequests]
        toolsets = [*(toolsets or []), toolset]

    if deferred_tool_results is None:
        deferred_tool_results = self.deferred_tool_results

    if isinstance(deps, StateHandler):
        raw_state = self.state or {}
        if isinstance(deps.state, BaseModel):
            state = type(deps.state).model_validate(raw_state)
        else:
            state = raw_state

        deps.state = state
    elif self.state:
        warnings.warn(
            f'State was provided but `deps` of type `{type(deps).__name__}` does not implement the `StateHandler` protocol, so the state was ignored. Use `StateDeps[...]` or implement `StateHandler` to receive AG-UI state.',
            UserWarning,
            stacklevel=2,
        )

    return self.agent.run_stream_events(
        output_type=output_type,
        message_history=message_history,
        deferred_tool_results=deferred_tool_results,
        model=model,
        deps=deps,
        model_settings=model_settings,
        instructions=instructions,
        usage_limits=usage_limits,
        usage=usage,
        metadata=metadata,
        infer_name=infer_name,
        toolsets=toolsets,
        builtin_tools=builtin_tools,
    )

```

---|---
####  run_stream
```
run_stream(
    *,
    output_type: OutputSpec[] | None = None,
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
    instructions: Instructions[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")] = None,
    deps: AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)") = None,
    model_settings: ModelSettings[](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings \(pydantic_ai.settings.ModelSettings\)") | None = None,
    usage_limits: UsageLimits[](https://ai.pydantic.dev/api/usage/#pydantic_ai.usage.UsageLimits "UsageLimits



      dataclass
   \(pydantic_ai.usage.UsageLimits\)") | None = None,
    usage: RunUsage[](https://ai.pydantic.dev/api/usage/#pydantic_ai.usage.RunUsage "RunUsage



      dataclass
   \(pydantic_ai.usage.RunUsage\)") | None = None,
    metadata: AgentMetadata[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")] | None = None,
    infer_name:  = True,
    toolsets: (
        [AbstractToolset[](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.AbstractToolset "AbstractToolset \(pydantic_ai.toolsets.AbstractToolset\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]] | None
    ) = None,
    builtin_tools: (
        [AbstractBuiltinTool[](https://ai.pydantic.dev/api/builtin_tools/#pydantic_ai.builtin_tools.AbstractBuiltinTool "AbstractBuiltinTool



      dataclass
   \(pydantic_ai.builtin_tools.AbstractBuiltinTool\)")] | None
    ) = None,
    on_complete: OnCompleteFunc[](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.OnCompleteFunc "OnCompleteFunc



      module-attribute
   \(pydantic_ai.ui._event_stream.OnCompleteFunc\)")[EventT] | None = None
) -> [EventT]

```

Run the agent with the protocol-specific run input and stream protocol-specific events.
Parameters:
Name | Type | Description | Default
---|---|---|---
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
`instructions` |  `Instructions[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]` |  Optional additional instructions to use for this run. |  `None`
`deps` |  `AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")` |  Optional dependencies to use for this run. |  `None`
`model_settings` |  `ModelSettings[](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings \(pydantic_ai.settings.ModelSettings\)") | None` |  Optional settings to use for this model's request. |  `None`
`usage_limits` |  `UsageLimits[](https://ai.pydantic.dev/api/usage/#pydantic_ai.usage.UsageLimits "UsageLimits



      dataclass
   \(pydantic_ai.usage.UsageLimits\)") | None` |  Optional limits on model request count or token usage. |  `None`
`usage` |  `RunUsage[](https://ai.pydantic.dev/api/usage/#pydantic_ai.usage.RunUsage "RunUsage



      dataclass
   \(pydantic_ai.usage.RunUsage\)") | None` |  Optional usage to start with, useful for resuming a conversation or agents used in tools. |  `None`
`metadata` |  `AgentMetadata[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")] | None` |  Optional metadata to attach to this run. Accepts a dictionary or a callable taking [`RunContext`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext



      dataclass
  "); merged with the agent's configured metadata. |  `None`
`infer_name` |  |  Whether to try to infer the agent name from the call frame if it's not set. |  `True`
`toolsets` |  `AbstractToolset[](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.AbstractToolset "AbstractToolset \(pydantic_ai.toolsets.AbstractToolset\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]] | None` |  Optional additional toolsets for this run. |  `None`
`builtin_tools` |  `AbstractBuiltinTool[](https://ai.pydantic.dev/api/builtin_tools/#pydantic_ai.builtin_tools.AbstractBuiltinTool "AbstractBuiltinTool



      dataclass
   \(pydantic_ai.builtin_tools.AbstractBuiltinTool\)")] | None` |  Optional additional builtin tools to use for this run. |  `None`
`on_complete` |  `OnCompleteFunc[](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.OnCompleteFunc "OnCompleteFunc



      module-attribute
   \(pydantic_ai.ui._event_stream.OnCompleteFunc\)")[EventT] | None` |  Optional callback function called when the agent run completes successfully. The callback receives the completed [`AgentRunResult`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AgentRunResult "AgentRunResult



      dataclass
  ") and can optionally yield additional protocol-specific events. |  `None`
Source code in `pydantic_ai_slim/pydantic_ai/ui/_adapter.py`
```
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
```
| ```
def run_stream(
    self,
    *,
    output_type: OutputSpec[Any] | None = None,
    message_history: Sequence[ModelMessage] | None = None,
    deferred_tool_results: DeferredToolResults | None = None,
    model: Model | KnownModelName | str | None = None,
    instructions: Instructions[AgentDepsT] = None,
    deps: AgentDepsT = None,
    model_settings: ModelSettings | None = None,
    usage_limits: UsageLimits | None = None,
    usage: RunUsage | None = None,
    metadata: AgentMetadata[AgentDepsT] | None = None,
    infer_name: bool = True,
    toolsets: Sequence[AbstractToolset[AgentDepsT]] | None = None,
    builtin_tools: Sequence[AbstractBuiltinTool] | None = None,
    on_complete: OnCompleteFunc[EventT] | None = None,
) -> AsyncIterator[EventT]:
    """Run the agent with the protocol-specific run input and stream protocol-specific events.

    Args:
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
