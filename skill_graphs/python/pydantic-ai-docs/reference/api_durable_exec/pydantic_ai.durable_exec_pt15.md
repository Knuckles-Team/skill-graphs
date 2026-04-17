


      module-attribute
   \(pydantic_ai.output.OutputDataT\)")]
]

```

```
iter(
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
    **_deprecated_kwargs:
) -> [
    AgentRun[](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AgentRun "AgentRun



      dataclass
   \(pydantic_ai.agent.AgentRun\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)"), RunOutputDataT[](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.RunOutputDataT "RunOutputDataT



      module-attribute
   \(pydantic_ai.agent.abstract.RunOutputDataT\)")]
]

```

```
iter(
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
    **_deprecated_kwargs:
) -> [AgentRun[](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AgentRun "AgentRun



      dataclass
   \(pydantic_ai.agent.AgentRun\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)"), ]]

```

A contextmanager which can be used to iterate over the agent graph's nodes as they are executed.
This method builds an internal agent graph (using system prompts, tools and output schemas) and then returns an `AgentRun` object. The `AgentRun` can be used to async-iterate over the nodes of the graph as they are executed. This is the API to use if you want to consume the outputs coming from each LLM model response, or the stream of events coming from the execution of tools.
The `AgentRun` also provides methods to access the full message history, new messages, and usage statistics, and the final result of the run once it has completed.
For more details, see the documentation of `AgentRun`.
Example:
```
from pydantic_ai import Agent

agent = Agent('openai:gpt-5.2')

async def main():
    nodes = []
    async with agent.iter('What is the capital of France?') as agent_run:
        async for node in agent_run:
            nodes.append(node)
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
    print(agent_run.result.output)
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
`AgentRun[](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AgentRun "AgentRun



      dataclass
   \(pydantic_ai.agent.AgentRun\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)"), ` |  The result of the run.
Source code in `pydantic_ai_slim/pydantic_ai/durable_exec/dbos/_agent.py`
```
815
816
817
818
819
820
821
822
823
824
825
826
827
828
829
830
831
832
833
834
835
836
837
838
839
840
841
842
843
844
845
846
847
848
849
850
851
852
853
854
855
856
857
858
859
860
861
862
863
864
865
866
867
868
869
870
871
872
873
874
875
876
877
878
879
880
881
882
883
884
885
886
887
888
889
890
891
892
893
894
895
896
897
898
899
900
901
902
903
904
905
906
907
908
909
910
911
912
913
914
915
916
917
918
919
920
921
922
923
924
925
926
927
928
929
930
931
932
933
934
935
936
937
938
939
940
```
| ```
@asynccontextmanager
async def iter(
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
    **_deprecated_kwargs: Never,
) -> AsyncIterator[AgentRun[AgentDepsT, Any]]:
    """A contextmanager which can be used to iterate over the agent graph's nodes as they are executed.

    This method builds an internal agent graph (using system prompts, tools and output schemas) and then returns an
    `AgentRun` object. The `AgentRun` can be used to async-iterate over the nodes of the graph as they are
    executed. This is the API to use if you want to consume the outputs coming from each LLM model response, or the
    stream of events coming from the execution of tools.

    The `AgentRun` also provides methods to access the full message history, new messages, and usage statistics,
    and the final result of the run once it has completed.

    For more details, see the documentation of `AgentRun`.

    Example:
```python
    from pydantic_ai import Agent

    agent = Agent('openai:gpt-5.2')

    async def main():
        nodes = []
        async with agent.iter('What is the capital of France?') as agent_run:
            async for node in agent_run:
                nodes.append(node)
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
        print(agent_run.result.output)
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
        builtin_tools: Optional additional builtin tools for this run.

    Returns:
        The result of the run.
    """
    if model is not None and not isinstance(model, DBOSModel):  # pragma: lax no cover
        raise UserError(
            'Non-DBOS model cannot be set at agent run time inside a DBOS workflow, it must be set at agent creation time.'
        )

    with self._dbos_overrides():
        async with super().iter(
            user_prompt=user_prompt,
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
            **_deprecated_kwargs,
        ) as run:
            yield run

```

---|---
####  override
```
override(
    *,
    name:  | Unset = UNSET,
    deps: AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)") | Unset = UNSET,
    model: Model[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.Model "Model \(pydantic_ai.models.Model\)") | KnownModelName[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.KnownModelName "KnownModelName



      module-attribute
   \(pydantic_ai.models.KnownModelName\)") |  | Unset = UNSET,
    toolsets: (
        [AbstractToolset[](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.AbstractToolset "AbstractToolset \(pydantic_ai.AbstractToolset\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]] | Unset
    ) = UNSET,
    tools: (
        [
            Tool[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.Tool "Tool



      dataclass
   \(pydantic_ai.tools.Tool\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]
            | ToolFuncEither[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolFuncEither "ToolFuncEither



      module-attribute
   \(pydantic_ai.tools.ToolFuncEither\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)"), ...]
        ]
        | Unset
    ) = UNSET,
    instructions: Instructions[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")] | Unset = UNSET
) -> [None]

```

Context manager to temporarily override agent name, dependencies, model, toolsets, tools, or instructions.
This is particularly useful when testing. You can find an example of this [here](https://ai.pydantic.dev/testing/#overriding-model-via-pytest-fixtures).
Parameters:
Name | Type | Description | Default
---|---|---|---
`name` |  `Unset` |  The name to use instead of the name passed to the agent constructor and agent run. |  `UNSET`
`deps` |  `AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)") | Unset` |  The dependencies to use instead of the dependencies passed to the agent run. |  `UNSET`
`model` |  `Model[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.Model "Model \(pydantic_ai.models.Model\)") | KnownModelName[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.KnownModelName "KnownModelName



      module-attribute
   \(pydantic_ai.models.KnownModelName\)") | Unset` |  The model to use instead of the model passed to the agent run. |  `UNSET`
`toolsets` |  `AbstractToolset[](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.AbstractToolset "AbstractToolset \(pydantic_ai.AbstractToolset\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]] | Unset` |  The toolsets to use instead of the toolsets passed to the agent constructor and agent run. |  `UNSET`
`tools` |  `Tool[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.Tool "Tool



      dataclass
   \(pydantic_ai.tools.Tool\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")] | ToolFuncEither[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolFuncEither "ToolFuncEither



      module-attribute
   \(pydantic_ai.tools.ToolFuncEither\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)"), ...]] | Unset` |  The tools to use instead of the tools registered with the agent. |  `UNSET`
`instructions` |  `Instructions[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")] | Unset` |  The instructions to use instead of the instructions registered with the agent. |  `UNSET`
Source code in `pydantic_ai_slim/pydantic_ai/durable_exec/dbos/_agent.py`
```
942
943
944
945
946
947
948
949
950
951
952
953
954
955
956
957
958
959
960
961
962
963
964
965
966
967
968
969
970
971
972
973
974
975
976
977
978
979
```
| ```
@contextmanager
def override(
    self,
    *,
    name: str | _utils.Unset = _utils.UNSET,
    deps: AgentDepsT | _utils.Unset = _utils.UNSET,
    model: models.Model | models.KnownModelName | str | _utils.Unset = _utils.UNSET,
    toolsets: Sequence[AbstractToolset[AgentDepsT]] | _utils.Unset = _utils.UNSET,
    tools: Sequence[Tool[AgentDepsT] | ToolFuncEither[AgentDepsT, ...]] | _utils.Unset = _utils.UNSET,
    instructions: Instructions[AgentDepsT] | _utils.Unset = _utils.UNSET,
) -> Iterator[None]:
    """Context manager to temporarily override agent name, dependencies, model, toolsets, tools, or instructions.
