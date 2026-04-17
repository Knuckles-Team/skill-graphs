                    ) -> AsyncIterator[_messages.ModelResponseStreamEvent]:
                        nonlocal final_result_event
                        async for event in stream:
                            yield event
                            if isinstance(event, _messages.FinalResultEvent):
                                final_result_event = event
                                break

                    if event_stream_handler is not None:
                        await event_stream_handler(
                            _agent_graph.build_run_context(graph_ctx), stream_to_final(stream)
                        )
                    else:
                        async for _ in stream_to_final(stream):
                            pass

                    if final_result_event is not None:
                        final_result = FinalResult(
                            None, final_result_event.tool_name, final_result_event.tool_call_id
                        )
                        if yielded:
                            raise exceptions.AgentRunError('Agent run produced final results')  # pragma: no cover
                        yielded = True

                        messages = graph_ctx.state.message_history.copy()

                        async def on_complete() -> None:
                            """Called when the stream has completed.

                            The model response will have been added to messages by now
                            by `StreamedRunResult._marked_completed`.
                            """
                            nonlocal final_result
                            final_result = FinalResult(
                                await stream.get_output(), final_result.tool_name, final_result.tool_call_id
                            )

                            # When we get here, the `ModelRequestNode` has completed streaming after the final result was found.
                            # When running an agent with `agent.run`, we'd then move to `CallToolsNode` to execute the tool calls and
                            # find the final result.
                            # We also want to execute tool calls (in case `agent.end_strategy == 'exhaustive'`) here, but
                            # we don't want to use run the `CallToolsNode` logic to determine the final output, as it would be
                            # wasteful and could produce a different result (e.g. when text output is followed by tool calls).
                            # So we call `process_tool_calls` directly and then end the run with the found final result.

                            parts: list[_messages.ModelRequestPart] = []
                            async for _event in _agent_graph.process_tool_calls(
                                tool_manager=graph_ctx.deps.tool_manager,
                                tool_calls=stream.response.tool_calls,
                                tool_call_results=None,
                                tool_call_metadata=None,
                                final_result=final_result,
                                ctx=graph_ctx,
                                output_parts=parts,
                            ):
                                pass

                            # To allow this message history to be used in a future run without dangling tool calls,
                            # append a new ModelRequest using the tool returns and retries
                            if parts:
                                messages.append(
                                    _messages.ModelRequest(
                                        parts, run_id=graph_ctx.state.run_id, timestamp=_utils.now_utc()
                                    )
                                )

                            await agent_run.next(_agent_graph.SetFinalResult(final_result))

                        yield StreamedRunResult(
                            messages,
                            graph_ctx.deps.new_message_index,
                            stream,
                            on_complete,
                        )
                        break
            elif self.is_call_tools_node(node) and event_stream_handler is not None:
                async with node.stream(agent_run.ctx) as stream:
                    await event_stream_handler(_agent_graph.build_run_context(agent_run.ctx), stream)

            next_node = await agent_run.next(node)
            if isinstance(next_node, End) and agent_run.result is not None:
                # A final output could have been produced by the CallToolsNode rather than the ModelRequestNode,
                # if a tool function raised CallDeferred or ApprovalRequired.
                # In this case there's no response to stream, but we still let the user access the output etc as normal.
                yield StreamedRunResult(
                    graph_ctx.state.message_history,
                    graph_ctx.deps.new_message_index,
                    run_result=agent_run.result,
                )
                yielded = True
                break
            if not isinstance(next_node, _agent_graph.AgentNode):
                raise exceptions.AgentRunError(  # pragma: no cover
                    'Should have produced a StreamedRunResult before getting here'
                )
            node = cast(_agent_graph.AgentNode[Any, Any], next_node)

    if not yielded:
        raise exceptions.AgentRunError('Agent run finished without producing a final result')  # pragma: no cover

```

---|---
####  run_stream_sync
```
run_stream_sync(
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
   \(pydantic_ai.agent.abstract.EventStreamHandler\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")] | None
    ) = None
) -> StreamedRunResultSync[](https://ai.pydantic.dev/api/result/#pydantic_ai.result.StreamedRunResultSync "StreamedRunResultSync



      dataclass
   \(pydantic_ai.result.StreamedRunResultSync\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)"), OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")]

```

```
run_stream_sync(
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
    event_stream_handler: (
        EventStreamHandler[](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.EventStreamHandler "EventStreamHandler



      module-attribute
   \(pydantic_ai.agent.abstract.EventStreamHandler\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")] | None
    ) = None
) -> StreamedRunResultSync[](https://ai.pydantic.dev/api/result/#pydantic_ai.result.StreamedRunResultSync "StreamedRunResultSync



      dataclass
   \(pydantic_ai.result.StreamedRunResultSync\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)"), RunOutputDataT[](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.RunOutputDataT "RunOutputDataT



      module-attribute
   \(pydantic_ai.agent.abstract.RunOutputDataT\)")]

```

```
run_stream_sync(
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
   \(pydantic_ai.agent.abstract.EventStreamHandler\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")] | None
    ) = None
) -> StreamedRunResultSync[](https://ai.pydantic.dev/api/result/#pydantic_ai.result.StreamedRunResultSync "StreamedRunResultSync



      dataclass
   \(pydantic_ai.result.StreamedRunResultSync\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)"), ]

```

Run the agent with a user prompt in sync streaming mode.
This is a convenience method that wraps [`run_stream()`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AbstractAgent.run_stream "run_stream



      async
  ") with `loop.run_until_complete(...)`. You therefore can't use this method inside async code or if there's an active event loop.
This method builds an internal agent graph (using system prompts, tools and output schemas) and then runs the graph until the model produces output matching the `output_type`, for example text or structured data. At this point, a streaming run result object is yielded from which you can stream the output as it comes in, and -- once this output has completed streaming -- get the complete output, message history, and usage.
As this method will consider the first output matching the `output_type` to be the final output, it will stop running the agent graph and will not execute any tool calls made by the model after this "final" output. If you want to always run the agent graph to completion and stream events and output at the same time, use [`agent.run()`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AbstractAgent.run "run



      async
  ") with an `event_stream_handler` or [`agent.iter()`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AbstractAgent.iter "iter



      abstractmethod
      async
  ") instead.
Example:
```
from pydantic_ai import Agent

agent = Agent('openai:gpt-5.2')

def main():
    response = agent.run_stream_sync('What is the capital of the UK?')
    print(response.get_output())
    #> The capital of the UK is London.

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
   \(pydantic_ai.builtin_tools.AbstractBuiltinTool\)") | BuiltinToolFunc[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.BuiltinToolFunc "BuiltinToolFunc



      module-attribute
   \(pydantic_ai.tools.BuiltinToolFunc\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]] | None` |  Optional additional builtin tools for this run. |  `None`
`event_stream_handler` |  `EventStreamHandler[](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.EventStreamHandler "EventStreamHandler



      module-attribute
   \(pydantic_ai.agent.abstract.EventStreamHandler\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")] | None` |  Optional handler for events from the model's streaming response and the agent's execution of tools to use for this run. It will receive all the events up until the final result is found, which you can then read or stream from inside the context manager. Note that it does _not_ receive any events after the final result is found. |  `None`
Returns:
Type | Description
---|---
`StreamedRunResultSync[](https://ai.pydantic.dev/api/result/#pydantic_ai.result.StreamedRunResultSync "StreamedRunResultSync



      dataclass
   \(pydantic_ai.result.StreamedRunResultSync\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)"), ` |  The result of the run.
Source code in `pydantic_ai_slim/pydantic_ai/agent/abstract.py`
```
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
749
750
751
752
753
754
755
756
757
758
759
760
761
762
763
764
765
766
767
768
769
770
771
772
773
774
775
776
777
778
779
780
781
782
```
| ```
def run_stream_sync(
    self,
    user_prompt: str | Sequence[_messages.UserContent] | None = None,
    *,
    output_type: OutputSpec[RunOutputDataT] | None = None,
    message_history: Sequence[_messages.ModelMessage] | None = None,
    deferred_tool_results: DeferredToolResults | None = None,
    model: models.Model | models.KnownModelName | str | None = None,
    deps: AgentDepsT = None,
    model_settings: ModelSettings | None = None,
    usage_limits: _usage.UsageLimits | None = None,
    usage: _usage.RunUsage | None = None,
    metadata: AgentMetadata[AgentDepsT] | None = None,
    infer_name: bool = True,
    toolsets: Sequence[AbstractToolset[AgentDepsT]] | None = None,
    builtin_tools: Sequence[AbstractBuiltinTool | BuiltinToolFunc[AgentDepsT]] | None = None,
    event_stream_handler: EventStreamHandler[AgentDepsT] | None = None,
) -> result.StreamedRunResultSync[AgentDepsT, Any]:
    """Run the agent with a user prompt in sync streaming mode.

    This is a convenience method that wraps [`run_stream()`][pydantic_ai.agent.AbstractAgent.run_stream] with `loop.run_until_complete(...)`.
    You therefore can't use this method inside async code or if there's an active event loop.

    This method builds an internal agent graph (using system prompts, tools and output schemas) and then
    runs the graph until the model produces output matching the `output_type`, for example text or structured data.
    At this point, a streaming run result object is yielded from which you can stream the output as it comes in,
    and -- once this output has completed streaming -- get the complete output, message history, and usage.
