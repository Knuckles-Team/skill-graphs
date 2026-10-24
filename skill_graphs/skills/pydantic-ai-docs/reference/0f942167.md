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
        [AbstractToolset[](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.AbstractToolset "AbstractToolset \(pydantic_ai.AbstractToolset\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]] | None
    ) = None,
    builtin_tools: (
        [
            AbstractBuiltinTool[](https://ai.pydantic.dev/api/builtin_tools/#pydantic_ai.builtin_tools.AbstractBuiltinTool "AbstractBuiltinTool



      dataclass
   \(pydantic_ai.builtin_tools.AbstractBuiltinTool\)")
            | BuiltinToolFunc[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.BuiltinToolFunc "BuiltinToolFunc



      module-attribute
   \(pydantic_ai.tools.BuiltinToolFunc\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]
        ]
        | None
    ) = None,
    event_stream_handler: (
        EventStreamHandler[](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.EventStreamHandler "EventStreamHandler



      module-attribute
   \(pydantic_ai.agent.EventStreamHandler\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")] | None
    ) = None,
    **_deprecated_kwargs:
) -> AgentRunResult[](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AgentRunResult "AgentRunResult



      dataclass
   \(pydantic_ai.agent.AgentRunResult\)")[]

```

Run the agent with a user prompt in async mode.
This method builds an internal agent graph (using system prompts, tools and result schemas) and then runs the graph to completion. The result of the run is returned.
Example:
```
from pydantic_ai import Agent

agent = Agent('openai:gpt-5.2')

async def main():
    agent_run = await agent.run('What is the capital of France?')
    print(agent_run.output)
    #> The capital of France is Paris.

```

Parameters:
Name | Type | Description | Default
---|---|---|---
`user_prompt` |  `UserContent] | None` |  User input to start/continue the conversation. |  `None`
`output_type` |  `OutputSpec[RunOutputDataT[](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.RunOutputDataT "RunOutputDataT



      module-attribute
   \(pydantic_ai.agent.abstract.RunOutputDataT\)")] | None` |  Custom output type to use for this run, `output_type` may only be used if the agent has no output validators since output validators would expect an argument that matches the agent's output type. |  `None`
`message_history` |  `ModelMessage[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelMessage "ModelMessage



      module-attribute
   \(pydantic_ai.messages.ModelMessage\)")] | None` |  History of the conversation so far. |  `None`
`deferred_tool_results` |  `DeferredToolResults[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.DeferredToolResults "DeferredToolResults



      dataclass
   \(pydantic_ai.tools.DeferredToolResults\)") | None` |  Optional results for deferred tool calls in the message history. |  `None`
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
`toolsets` |  `AbstractToolset[](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.AbstractToolset "AbstractToolset \(pydantic_ai.AbstractToolset\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]] | None` |  Optional additional toolsets for this run. |  `None`
`event_stream_handler` |  `EventStreamHandler[](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.EventStreamHandler "EventStreamHandler



      module-attribute
   \(pydantic_ai.agent.EventStreamHandler\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")] | None` |  Optional event stream handler to use for this run. |  `None`
`builtin_tools` |  `AbstractBuiltinTool[](https://ai.pydantic.dev/api/builtin_tools/#pydantic_ai.builtin_tools.AbstractBuiltinTool "AbstractBuiltinTool



      dataclass
   \(pydantic_ai.builtin_tools.AbstractBuiltinTool\)") | BuiltinToolFunc[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.BuiltinToolFunc "BuiltinToolFunc



      module-attribute
   \(pydantic_ai.tools.BuiltinToolFunc\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]] | None` |  Optional additional builtin tools for this run. |  `None`
Returns:
Type | Description
---|---
`AgentRunResult[](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AgentRunResult "AgentRunResult



      dataclass
   \(pydantic_ai.agent.AgentRunResult\)")[` |  The result of the run.
Source code in `pydantic_ai_slim/pydantic_ai/durable_exec/prefect/_agent.py`
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
```
| ```
async def run(
    self,
    user_prompt: str | Sequence[_messages.UserContent] | None = None,
    *,
    output_type: OutputSpec[RunOutputDataT] | None = None,
    message_history: Sequence[_messages.ModelMessage] | None = None,
    deferred_tool_results: DeferredToolResults | None = None,
    model: models.Model | models.KnownModelName | str | None = None,
    instructions: Instructions[AgentDepsT] = None,
    deps: AgentDepsT = None,
    model_settings: ModelSettings | None = None,
    usage_limits: _usage.UsageLimits | None = None,
    usage: _usage.RunUsage | None = None,
    metadata: AgentMetadata[AgentDepsT] | None = None,
    infer_name: bool = True,
    toolsets: Sequence[AbstractToolset[AgentDepsT]] | None = None,
    builtin_tools: Sequence[AbstractBuiltinTool | BuiltinToolFunc[AgentDepsT]] | None = None,
    event_stream_handler: EventStreamHandler[AgentDepsT] | None = None,
    **_deprecated_kwargs: Never,
) -> AgentRunResult[Any]:
    """Run the agent with a user prompt in async mode.

    This method builds an internal agent graph (using system prompts, tools and result schemas) and then
    runs the graph to completion. The result of the run is returned.

    Example:
```python
    from pydantic_ai import Agent

    agent = Agent('openai:gpt-5.2')

    async def main():
        agent_run = await agent.run('What is the capital of France?')
        print(agent_run.output)
        #> The capital of France is Paris.
```

    Args:
        user_prompt: User input to start/continue the conversation.
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
        event_stream_handler: Optional event stream handler to use for this run.
        builtin_tools: Optional additional builtin tools for this run.

    Returns:
        The result of the run.
    """

    @flow(name=f'{self._name} Run')
    async def wrapped_run_flow() -> AgentRunResult[Any]:
        # Mark that we're inside a PrefectAgent flow
        token = self._in_prefect_agent_flow.set(True)
        try:
            with self._prefect_overrides():
                result = await super(WrapperAgent, self).run(
                    user_prompt,
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
                    event_stream_handler=event_stream_handler,
                )
                return result
        finally:
            self._in_prefect_agent_flow.reset(token)

    return await wrapped_run_flow()

```

---|---
####  run_sync
```
run_sync(
    user_prompt:  | [UserContent] | None = None,
    *,
    output_type: None = None,
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
        [AbstractToolset[](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.AbstractToolset "AbstractToolset \(pydantic_ai.AbstractToolset\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]] | None
    ) = None,
    builtin_tools: (
        [
            AbstractBuiltinTool[](https://ai.pydantic.dev/api/builtin_tools/#pydantic_ai.builtin_tools.AbstractBuiltinTool "AbstractBuiltinTool



      dataclass
   \(pydantic_ai.builtin_tools.AbstractBuiltinTool\)")
            | BuiltinToolFunc[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.BuiltinToolFunc "BuiltinToolFunc



      module-attribute
   \(pydantic_ai.tools.BuiltinToolFunc\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]
        ]
        | None
    ) = None,
    event_stream_handler: (
        EventStreamHandler[](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.EventStreamHandler "EventStreamHandler



      module-attribute
   \(pydantic_ai.agent.EventStreamHandler\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")] | None
    ) = None
) -> AgentRunResult[](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AgentRunResult "AgentRunResult



      dataclass
   \(pydantic_ai.agent.AgentRunResult\)")[OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")]

```

```
run_sync(
    user_prompt:  | [UserContent] | None = None,
    *,
    output_type: OutputSpec[RunOutputDataT[](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.RunOutputDataT "RunOutputDataT



      module-attribute
   \(pydantic_ai.agent.abstract.RunOutputDataT\)")],
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
        [AbstractToolset[](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.AbstractToolset "AbstractToolset \(pydantic_ai.AbstractToolset\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]] | None
    ) = None,
    builtin_tools: (
        [
            AbstractBuiltinTool[](https://ai.pydantic.dev/api/builtin_tools/#pydantic_ai.builtin_tools.AbstractBuiltinTool "AbstractBuiltinTool



      dataclass
   \(pydantic_ai.builtin_tools.AbstractBuiltinTool\)")
            | BuiltinToolFunc[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.BuiltinToolFunc "BuiltinToolFunc



      module-attribute
   \(pydantic_ai.tools.BuiltinToolFunc\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]
        ]
        | None
    ) = None,
    event_stream_handler: (
        EventStreamHandler[](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.EventStreamHandler "EventStreamHandler



      module-attribute
   \(pydantic_ai.agent.EventStreamHandler\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")] | None
    ) = None
) -> AgentRunResult[](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AgentRunResult "AgentRunResult



      dataclass
   \(pydantic_ai.agent.AgentRunResult\)")[RunOutputDataT[](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.RunOutputDataT "RunOutputDataT



      module-attribute
   \(pydantic_ai.agent.abstract.RunOutputDataT\)")]

```

```
run_sync(
    user_prompt:  | [UserContent] | None = None,
    *,
    output_type: OutputSpec[RunOutputDataT[](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.RunOutputDataT "RunOutputDataT



      module-attribute
   \(pydantic_ai.agent.abstract.RunOutputDataT\)")] | None = None,
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
        [AbstractToolset[](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.AbstractToolset "AbstractToolset \(pydantic_ai.AbstractToolset\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]] | None
    ) = None,
    builtin_tools: (
        [
            AbstractBuiltinTool[](https://ai.pydantic.dev/api/builtin_tools/#pydantic_ai.builtin_tools.AbstractBuiltinTool "AbstractBuiltinTool



      dataclass
   \(pydantic_ai.builtin_tools.AbstractBuiltinTool\)")
            | BuiltinToolFunc[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.BuiltinToolFunc "BuiltinToolFunc



      module-attribute
   \(pydantic_ai.tools.BuiltinToolFunc\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]
        ]
        | None
    ) = None,
    event_stream_handler: (
        EventStreamHandler[](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.EventStreamHandler "EventStreamHandler



      module-attribute
   \(pydantic_ai.agent.EventStreamHandler\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")] | None
    ) = None,
    **_deprecated_kwargs:
) -> AgentRunResult[](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AgentRunResult "AgentRunResult



      dataclass
   \(pydantic_ai.agent.AgentRunResult\)")[]

```

Synchronously run the agent with a user prompt.
This is a convenience method that wraps [`self.run`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AbstractAgent.run "run



      async
  ") with `loop.run_until_complete(...)`. You therefore can't use this method inside async code or if there's an active event loop.
Example:
```
from pydantic_ai import Agent

agent = Agent('openai:gpt-5.2')

result_sync = agent.run_sync('What is the capital of Italy?')
print(result_sync.output)
#> The capital of Italy is Rome.

```

Parameters:
Name | Type | Description | Default
---|---|---|---
`user_prompt` |  `UserContent] | None` |  User input to start/continue the conversation. |  `None`
`output_type` |  `OutputSpec[RunOutputDataT[](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.RunOutputDataT "RunOutputDataT



      module-attribute
   \(pydantic_ai.agent.abstract.RunOutputDataT\)")] | None` |  Custom output type to use for this run, `output_type` may only be used if the agent has no output validators since output validators would expect an argument that matches the agent's output type. |  `None`
`message_history` |  `ModelMessage[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelMessage "ModelMessage



      module-attribute
   \(pydantic_ai.messages.ModelMessage\)")] | None` |  History of the conversation so far. |  `None`
`deferred_tool_results` |  `DeferredToolResults[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.DeferredToolResults "DeferredToolResults



      dataclass
   \(pydantic_ai.tools.DeferredToolResults\)") | None` |  Optional results for deferred tool calls in the message history. |  `None`
`model` |  `Model[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.Model "Model \(pydantic_ai.models.Model\)") | KnownModelName[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.KnownModelName "KnownModelName



      module-attribute
   \(pydantic_ai.models.KnownModelName\)") | ` |  Optional model to use for this run, required if `model` was not set when creating the agent. |  `None`
