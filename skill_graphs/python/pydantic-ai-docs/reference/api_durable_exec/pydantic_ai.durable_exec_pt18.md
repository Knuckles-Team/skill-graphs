            model: Optional model to use for this run, required if `model` was not set when creating the agent.
            deps: Optional dependencies to use for this run.
            instructions: Optional additional instructions to use for this run.
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
        if model is not None and not isinstance(model, PrefectModel):
            raise UserError(
                'Non-Prefect model cannot be set at agent run time inside a Prefect flow, it must be set at agent creation time.'
            )

        with self._prefect_overrides():
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
            ) as run:
                yield run

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
        """Context manager to temporarily override agent dependencies, model, toolsets, tools, or instructions.

        This is particularly useful when testing.
        You can find an example of this [here](../testing.md#overriding-model-via-pytest-fixtures).

        Args:
            name: The name to use instead of the name passed to the agent constructor and agent run.
            deps: The dependencies to use instead of the dependencies passed to the agent run.
            model: The model to use instead of the model passed to the agent run.
            toolsets: The toolsets to use instead of the toolsets passed to the agent constructor and agent run.
            tools: The tools to use instead of the tools registered with the agent.
            instructions: The instructions to use instead of the instructions registered with the agent.
        """
        if _utils.is_set(model) and not isinstance(model, PrefectModel):
            raise UserError(
                'Non-Prefect model cannot be contextually overridden inside a Prefect flow, it must be set at agent creation time.'
            )

        with super().override(
            name=name, deps=deps, model=model, toolsets=toolsets, tools=tools, instructions=instructions
        ):
            yield

```

---|---
####  __init__
```
__init__(
    wrapped: AbstractAgent[](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AbstractAgent "AbstractAgent \(pydantic_ai.agent.AbstractAgent\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)"), OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")],
    *,
    name:  | None = None,
    event_stream_handler: (
        EventStreamHandler[](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.EventStreamHandler "EventStreamHandler



      module-attribute
   \(pydantic_ai.agent.EventStreamHandler\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")] | None
    ) = None,
    mcp_task_config: TaskConfig[](https://ai.pydantic.dev/api/durable_exec/#pydantic_ai.durable_exec.prefect.TaskConfig "TaskConfig \(pydantic_ai.durable_exec.prefect._types.TaskConfig\)") | None = None,
    model_task_config: TaskConfig[](https://ai.pydantic.dev/api/durable_exec/#pydantic_ai.durable_exec.prefect.TaskConfig "TaskConfig \(pydantic_ai.durable_exec.prefect._types.TaskConfig\)") | None = None,
    tool_task_config: TaskConfig[](https://ai.pydantic.dev/api/durable_exec/#pydantic_ai.durable_exec.prefect.TaskConfig "TaskConfig \(pydantic_ai.durable_exec.prefect._types.TaskConfig\)") | None = None,
    tool_task_config_by_name: (
        [, TaskConfig[](https://ai.pydantic.dev/api/durable_exec/#pydantic_ai.durable_exec.prefect.TaskConfig "TaskConfig \(pydantic_ai.durable_exec.prefect._types.TaskConfig\)") | None] | None
    ) = None,
    event_stream_handler_task_config: (
        TaskConfig[](https://ai.pydantic.dev/api/durable_exec/#pydantic_ai.durable_exec.prefect.TaskConfig "TaskConfig \(pydantic_ai.durable_exec.prefect._types.TaskConfig\)") | None
    ) = None,
    prefectify_toolset_func: [
        [
            AbstractToolset[](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.AbstractToolset "AbstractToolset \(pydantic_ai.AbstractToolset\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")],
            TaskConfig[](https://ai.pydantic.dev/api/durable_exec/#pydantic_ai.durable_exec.prefect.TaskConfig "TaskConfig \(pydantic_ai.durable_exec.prefect._types.TaskConfig\)"),
            TaskConfig[](https://ai.pydantic.dev/api/durable_exec/#pydantic_ai.durable_exec.prefect.TaskConfig "TaskConfig \(pydantic_ai.durable_exec.prefect._types.TaskConfig\)"),
            [, TaskConfig[](https://ai.pydantic.dev/api/durable_exec/#pydantic_ai.durable_exec.prefect.TaskConfig "TaskConfig \(pydantic_ai.durable_exec.prefect._types.TaskConfig\)") | None],
        ],
        AbstractToolset[](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.AbstractToolset "AbstractToolset \(pydantic_ai.AbstractToolset\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")],
    ] = prefectify_toolset
)

```

Wrap an agent to enable it with Prefect durable flows, by automatically offloading model requests, tool calls, and MCP server communication to Prefect tasks.
After wrapping, the original agent can still be used as normal outside of the Prefect flow.
Parameters:
Name | Type | Description | Default
---|---|---|---
`wrapped` |  `AbstractAgent[](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AbstractAgent "AbstractAgent \(pydantic_ai.agent.AbstractAgent\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)"), OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")]` |  The agent to wrap. |  _required_
`name` |  |  Optional unique agent name to use as the Prefect flow name prefix. If not provided, the agent's `name` will be used. |  `None`
`event_stream_handler` |  `EventStreamHandler[](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.EventStreamHandler "EventStreamHandler



      module-attribute
   \(pydantic_ai.agent.EventStreamHandler\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")] | None` |  Optional event stream handler to use instead of the one set on the wrapped agent. |  `None`
`mcp_task_config` |  `TaskConfig[](https://ai.pydantic.dev/api/durable_exec/#pydantic_ai.durable_exec.prefect.TaskConfig "TaskConfig \(pydantic_ai.durable_exec.prefect._types.TaskConfig\)") | None` |  The base Prefect task config to use for MCP server tasks. If no config is provided, use the default settings of Prefect. |  `None`
`model_task_config` |  `TaskConfig[](https://ai.pydantic.dev/api/durable_exec/#pydantic_ai.durable_exec.prefect.TaskConfig "TaskConfig \(pydantic_ai.durable_exec.prefect._types.TaskConfig\)") | None` |  The Prefect task config to use for model request tasks. If no config is provided, use the default settings of Prefect. |  `None`
`tool_task_config` |  `TaskConfig[](https://ai.pydantic.dev/api/durable_exec/#pydantic_ai.durable_exec.prefect.TaskConfig "TaskConfig \(pydantic_ai.durable_exec.prefect._types.TaskConfig\)") | None` |  The default Prefect task config to use for tool calls. If no config is provided, use the default settings of Prefect. |  `None`
`tool_task_config_by_name` |  `TaskConfig[](https://ai.pydantic.dev/api/durable_exec/#pydantic_ai.durable_exec.prefect.TaskConfig "TaskConfig \(pydantic_ai.durable_exec.prefect._types.TaskConfig\)") | None] | None` |  Per-tool task configuration. Keys are tool names, values are TaskConfig or None (None disables task wrapping for that tool). |  `None`
`event_stream_handler_task_config` |  `TaskConfig[](https://ai.pydantic.dev/api/durable_exec/#pydantic_ai.durable_exec.prefect.TaskConfig "TaskConfig \(pydantic_ai.durable_exec.prefect._types.TaskConfig\)") | None` |  The Prefect task config to use for the event stream handler task. If no config is provided, use the default settings of Prefect. |  `None`
`prefectify_toolset_func` |  `AbstractToolset[](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.AbstractToolset "AbstractToolset \(pydantic_ai.AbstractToolset\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")], TaskConfig[](https://ai.pydantic.dev/api/durable_exec/#pydantic_ai.durable_exec.prefect.TaskConfig "TaskConfig \(pydantic_ai.durable_exec.prefect._types.TaskConfig\)"), TaskConfig[](https://ai.pydantic.dev/api/durable_exec/#pydantic_ai.durable_exec.prefect.TaskConfig "TaskConfig \(pydantic_ai.durable_exec.prefect._types.TaskConfig\)"), TaskConfig[](https://ai.pydantic.dev/api/durable_exec/#pydantic_ai.durable_exec.prefect.TaskConfig "TaskConfig \(pydantic_ai.durable_exec.prefect._types.TaskConfig\)") | None]], AbstractToolset[](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.AbstractToolset "AbstractToolset \(pydantic_ai.AbstractToolset\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]]` |  Optional function to use to prepare toolsets for Prefect by wrapping them in a `PrefectWrapperToolset` that moves methods that require IO to Prefect tasks. If not provided, only `FunctionToolset` and `MCPServer` will be prepared for Prefect. The function takes the toolset, the task config, the tool-specific task config, and the tool-specific task config by name. |  `prefectify_toolset`
Source code in `pydantic_ai_slim/pydantic_ai/durable_exec/prefect/_agent.py`
```
 44
 45
 46
 47
 48
 49
 50
 51
 52
 53
 54
 55
 56
 57
 58
 59
 60
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
```
| ```
def __init__(
    self,
    wrapped: AbstractAgent[AgentDepsT, OutputDataT],
    *,
    name: str | None = None,
    event_stream_handler: EventStreamHandler[AgentDepsT] | None = None,
    mcp_task_config: TaskConfig | None = None,
    model_task_config: TaskConfig | None = None,
    tool_task_config: TaskConfig | None = None,
    tool_task_config_by_name: dict[str, TaskConfig | None] | None = None,
    event_stream_handler_task_config: TaskConfig | None = None,
    prefectify_toolset_func: Callable[
        [AbstractToolset[AgentDepsT], TaskConfig, TaskConfig, dict[str, TaskConfig | None]],
        AbstractToolset[AgentDepsT],
    ] = prefectify_toolset,
):
    """Wrap an agent to enable it with Prefect durable flows, by automatically offloading model requests, tool calls, and MCP server communication to Prefect tasks.

    After wrapping, the original agent can still be used as normal outside of the Prefect flow.

    Args:
        wrapped: The agent to wrap.
        name: Optional unique agent name to use as the Prefect flow name prefix. If not provided, the agent's `name` will be used.
        event_stream_handler: Optional event stream handler to use instead of the one set on the wrapped agent.
        mcp_task_config: The base Prefect task config to use for MCP server tasks. If no config is provided, use the default settings of Prefect.
        model_task_config: The Prefect task config to use for model request tasks. If no config is provided, use the default settings of Prefect.
        tool_task_config: The default Prefect task config to use for tool calls. If no config is provided, use the default settings of Prefect.
        tool_task_config_by_name: Per-tool task configuration. Keys are tool names, values are TaskConfig or None (None disables task wrapping for that tool).
        event_stream_handler_task_config: The Prefect task config to use for the event stream handler task. If no config is provided, use the default settings of Prefect.
        prefectify_toolset_func: Optional function to use to prepare toolsets for Prefect by wrapping them in a `PrefectWrapperToolset` that moves methods that require IO to Prefect tasks.
            If not provided, only `FunctionToolset` and `MCPServer` will be prepared for Prefect.
            The function takes the toolset, the task config, the tool-specific task config, and the tool-specific task config by name.
    """
    super().__init__(wrapped)

    self._name = name or wrapped.name
    self._event_stream_handler = event_stream_handler
    if self._name is None:
        raise UserError(
            "An agent needs to have a unique `name` in order to be used with Prefect. The name will be used to identify the agent's flows and tasks."
        )

    # Merge the config with the default Prefect config
    self._mcp_task_config = default_task_config | (mcp_task_config or {})
    self._model_task_config = default_task_config | (model_task_config or {})
    self._tool_task_config = default_task_config | (tool_task_config or {})
    self._tool_task_config_by_name = tool_task_config_by_name or {}
    self._event_stream_handler_task_config = default_task_config | (event_stream_handler_task_config or {})

    if not isinstance(wrapped.model, Model):
        raise UserError(
            'An agent needs to have a `model` in order to be used with Prefect, it cannot be set at agent run time.'
        )

    prefect_model = PrefectModel(
        wrapped.model,
        task_config=self._model_task_config,
        event_stream_handler=self.event_stream_handler,
    )
    self._model = prefect_model

    def _prefectify_toolset(toolset: AbstractToolset[AgentDepsT]) -> AbstractToolset[AgentDepsT]:
        """Convert a toolset to its Prefect equivalent."""
        return prefectify_toolset_func(
            toolset,
            self._mcp_task_config,
            self._tool_task_config,
            self._tool_task_config_by_name,
        )

    prefect_toolsets = [toolset.visit_and_replace(_prefectify_toolset) for toolset in wrapped.toolsets]
    self._toolsets = prefect_toolsets

    # Context variable to track when we're inside this agent's Prefect flow
    self._in_prefect_agent_flow: ContextVar[bool] = ContextVar(
        f'_in_prefect_agent_flow_{self._name}', default=False
    )

```

---|---
####  run `async`
```
run(
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
run(
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
run(
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
