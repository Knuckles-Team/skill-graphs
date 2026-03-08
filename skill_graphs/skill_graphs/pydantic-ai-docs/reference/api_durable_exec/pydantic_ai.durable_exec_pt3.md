
            if toolsets is not None:
                raise UserError(
                    'Toolsets cannot be set at agent run time inside a Temporal workflow, it must be set at agent creation time.'
                )

            resolved_model = None
        else:
            resolved_model = self._temporal_model.resolve_model(model)

        async with super().iter(
            user_prompt=user_prompt,
            output_type=output_type,
            message_history=message_history,
            deferred_tool_results=deferred_tool_results,
            model=resolved_model,
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
        if workflow.in_workflow():
            if _utils.is_set(model):
                raise UserError(
                    'Model cannot be contextually overridden inside a Temporal workflow, it must be set at agent creation time.'
                )
            if _utils.is_set(toolsets):
                raise UserError(
                    'Toolsets cannot be contextually overridden inside a Temporal workflow, they must be set at agent creation time.'
                )
            if _utils.is_set(tools):
                raise UserError(
                    'Tools cannot be contextually overridden inside a Temporal workflow, they must be set at agent creation time.'
                )

        with super().override(
            name=name,
            deps=deps,
            model=model,
            toolsets=toolsets,
            tools=tools,
            instructions=instructions,
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
    models: [, Model[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.Model "Model \(pydantic_ai.models.Model\)")] | None = None,
    provider_factory: TemporalProviderFactory | None = None,
    event_stream_handler: (
        EventStreamHandler[](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.EventStreamHandler "EventStreamHandler



      module-attribute
   \(pydantic_ai.agent.EventStreamHandler\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")] | None
    ) = None,
    activity_config: ActivityConfig | None = None,
    model_activity_config: ActivityConfig | None = None,
    toolset_activity_config: (
        [, ActivityConfig] | None
    ) = None,
    tool_activity_config: (
        [
            , [, ActivityConfig | [False]]
        ]
        | None
    ) = None,
    run_context_type: [
        TemporalRunContext[](https://ai.pydantic.dev/api/durable_exec/#pydantic_ai.durable_exec.temporal.TemporalRunContext "TemporalRunContext \(pydantic_ai.durable_exec.temporal._run_context.TemporalRunContext\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]
    ] = TemporalRunContext[](https://ai.pydantic.dev/api/durable_exec/#pydantic_ai.durable_exec.temporal.TemporalRunContext "TemporalRunContext \(pydantic_ai.durable_exec.temporal._run_context.TemporalRunContext\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")],
    temporalize_toolset_func: [
        [
            AbstractToolset[](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.AbstractToolset "AbstractToolset \(pydantic_ai.AbstractToolset\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")],
            ,
            ActivityConfig,
            [, ActivityConfig | [False]],
            [AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")],
            [TemporalRunContext[](https://ai.pydantic.dev/api/durable_exec/#pydantic_ai.durable_exec.temporal.TemporalRunContext "TemporalRunContext \(pydantic_ai.durable_exec.temporal._run_context.TemporalRunContext\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]],
        ],
        AbstractToolset[](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.AbstractToolset "AbstractToolset \(pydantic_ai.AbstractToolset\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")],
    ] = temporalize_toolset
)

```

Wrap an agent to enable it to be used inside a Temporal workflow, by automatically offloading model requests, tool calls, and MCP server communication to Temporal activities.
After wrapping, the original agent can still be used as normal outside of the Temporal workflow, but any changes to its model or toolsets after wrapping will not be reflected in the durable agent.
Parameters:
Name | Type | Description | Default
---|---|---|---
`wrapped` |  `AbstractAgent[](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AbstractAgent "AbstractAgent \(pydantic_ai.agent.AbstractAgent\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)"), OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")]` |  The agent to wrap. |  _required_
`name` |  |  Optional unique agent name to use in the Temporal activities' names. If not provided, the agent's `name` will be used. |  `None`
`models` |  `Model[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.Model "Model \(pydantic_ai.models.Model\)")] | None` |  Optional mapping of model instances to register with the agent. Keys define the names that can be referenced at runtime and the values are `Model` instances. Registered model instances can be passed directly to `run(model=...)`. If the wrapped agent doesn't have a model set and none is provided to `run()`, the first model in this mapping will be used as the default. |  `None`
`provider_factory` |  `TemporalProviderFactory | None` |  Optional callable used when instantiating models from provider strings (those supplied at runtime). The callable receives the provider name and the current run context, allowing custom configuration such as injecting API keys stored on `deps`. Note: This factory is only used inside Temporal workflows. Outside workflows, model strings are resolved using the default provider behavior. |  `None`
`event_stream_handler` |  `EventStreamHandler[](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.EventStreamHandler "EventStreamHandler



      module-attribute
   \(pydantic_ai.agent.EventStreamHandler\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")] | None` |  Optional event stream handler to use instead of the one set on the wrapped agent. |  `None`
`activity_config` |  `ActivityConfig | None` |  The base Temporal activity config to use for all activities. If no config is provided, a `start_to_close_timeout` of 60 seconds is used. |  `None`
`model_activity_config` |  `ActivityConfig | None` |  The Temporal activity config to use for model request activities. This is merged with the base activity config. |  `None`
`toolset_activity_config` |  `ActivityConfig] | None` |  The Temporal activity config to use for get-tools and call-tool activities for specific toolsets identified by ID. This is merged with the base activity config. |  `None`
`tool_activity_config` |  `ActivityConfig | ` |  The Temporal activity config to use for specific tool call activities identified by toolset ID and tool name. This is merged with the base and toolset-specific activity configs. If a tool does not use IO, you can specify `False` to disable using an activity. Note that the tool is required to be defined as an `async` function as non-async tools are run in threads which are non-deterministic and thus not supported outside of activities. |  `None`
`run_context_type` |  `TemporalRunContext[](https://ai.pydantic.dev/api/durable_exec/#pydantic_ai.durable_exec.temporal.TemporalRunContext "TemporalRunContext \(pydantic_ai.durable_exec.temporal._run_context.TemporalRunContext\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]]` |  The `TemporalRunContext` subclass to use to serialize and deserialize the run context for use inside a Temporal activity. By default, only the `deps`, `run_id`, `metadata`, `retries`, `tool_call_id`, `tool_name`, `tool_call_approved`, `retry`, `max_retries`, `run_step`, `usage`, and `partial_output` attributes will be available. To make another attribute available, create a `TemporalRunContext` subclass with a custom `serialize_run_context` class method that returns a dictionary that includes the attribute. |  `TemporalRunContext[](https://ai.pydantic.dev/api/durable_exec/#pydantic_ai.durable_exec.temporal.TemporalRunContext "TemporalRunContext \(pydantic_ai.durable_exec.temporal._run_context.TemporalRunContext\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]`
`temporalize_toolset_func` |  `AbstractToolset[](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.AbstractToolset "AbstractToolset \(pydantic_ai.AbstractToolset\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")], ActivityConfig, ActivityConfig | AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")], TemporalRunContext[](https://ai.pydantic.dev/api/durable_exec/#pydantic_ai.durable_exec.temporal.TemporalRunContext "TemporalRunContext \(pydantic_ai.durable_exec.temporal._run_context.TemporalRunContext\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]]], AbstractToolset[](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.AbstractToolset "AbstractToolset \(pydantic_ai.AbstractToolset\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]]` |  Optional function to use to prepare "leaf" toolsets (i.e. those that implement their own tool listing and calling) for Temporal by wrapping them in a `TemporalWrapperToolset` that moves methods that require IO to Temporal activities. If not provided, only `FunctionToolset` and `MCPServer` will be prepared for Temporal. The function takes the toolset, the activity name prefix, the toolset-specific activity config, the tool-specific activity configs and the run context type. |  `temporalize_toolset`
Source code in `pydantic_ai_slim/pydantic_ai/durable_exec/temporal/_agent.py`
```
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
```
| ```
def __init__(
    self,
    wrapped: AbstractAgent[AgentDepsT, OutputDataT],
    *,
    name: str | None = None,
    models: Mapping[str, Model] | None = None,
    provider_factory: TemporalProviderFactory | None = None,
    event_stream_handler: EventStreamHandler[AgentDepsT] | None = None,
    activity_config: ActivityConfig | None = None,
    model_activity_config: ActivityConfig | None = None,
    toolset_activity_config: dict[str, ActivityConfig] | None = None,
    tool_activity_config: dict[str, dict[str, ActivityConfig | Literal[False]]] | None = None,
    run_context_type: type[TemporalRunContext[AgentDepsT]] = TemporalRunContext[AgentDepsT],
    temporalize_toolset_func: Callable[
        [
            AbstractToolset[AgentDepsT],
            str,
            ActivityConfig,
            dict[str, ActivityConfig | Literal[False]],
            type[AgentDepsT],
            type[TemporalRunContext[AgentDepsT]],
        ],
        AbstractToolset[AgentDepsT],
    ] = temporalize_toolset,
):
    """Wrap an agent to enable it to be used inside a Temporal workflow, by automatically offloading model requests, tool calls, and MCP server communication to Temporal activities.

    After wrapping, the original agent can still be used as normal outside of the Temporal workflow, but any changes to its model or toolsets after wrapping will not be reflected in the durable agent.

    Args:
        wrapped: The agent to wrap.
        name: Optional unique agent name to use in the Temporal activities' names. If not provided, the agent's `name` will be used.
        models:
            Optional mapping of model instances to register with the agent.
            Keys define the names that can be referenced at runtime and the values are `Model` instances.
            Registered model instances can be passed directly to `run(model=...)`.
            If the wrapped agent doesn't have a model set and none is provided to `run()`,
            the first model in this mapping will be used as the default.
        provider_factory:
            Optional callable used when instantiating models from provider strings (those supplied at runtime).
            The callable receives the provider name and the current run context, allowing custom configuration such as injecting API keys stored on `deps`.
            Note: This factory is only used inside Temporal workflows. Outside workflows, model strings are resolved using the default provider behavior.
        event_stream_handler: Optional event stream handler to use instead of the one set on the wrapped agent.
        activity_config: The base Temporal activity config to use for all activities. If no config is provided, a `start_to_close_timeout` of 60 seconds is used.
        model_activity_config: The Temporal activity config to use for model request activities. This is merged with the base activity config.
        toolset_activity_config: The Temporal activity config to use for get-tools and call-tool activities for specific toolsets identified by ID. This is merged with the base activity config.
        tool_activity_config: The Temporal activity config to use for specific tool call activities identified by toolset ID and tool name.
            This is merged with the base and toolset-specific activity configs.
            If a tool does not use IO, you can specify `False` to disable using an activity.
            Note that the tool is required to be defined as an `async` function as non-async tools are run in threads which are non-deterministic and thus not supported outside of activities.
        run_context_type: The `TemporalRunContext` subclass to use to serialize and deserialize the run context for use inside a Temporal activity.
            By default, only the `deps`, `run_id`, `metadata`, `retries`, `tool_call_id`, `tool_name`, `tool_call_approved`, `retry`, `max_retries`, `run_step`, `usage`, and `partial_output` attributes will be available.
            To make another attribute available, create a `TemporalRunContext` subclass with a custom `serialize_run_context` class method that returns a dictionary that includes the attribute.
        temporalize_toolset_func: Optional function to use to prepare "leaf" toolsets (i.e. those that implement their own tool listing and calling) for Temporal by wrapping them in a `TemporalWrapperToolset` that moves methods that require IO to Temporal activities.
            If not provided, only `FunctionToolset` and `MCPServer` will be prepared for Temporal.
            The function takes the toolset, the activity name prefix, the toolset-specific activity config, the tool-specific activity configs and the run context type.
    """
    super().__init__(wrapped)

    self._name = name
    self._event_stream_handler = event_stream_handler
    self.run_context_type = run_context_type

    if self.name is None:
        raise UserError(
            "An agent needs to have a unique `name` in order to be used with Temporal. The name will be used to identify the agent's activities within the workflow."
        )
    # start_to_close_timeout is required
    activity_config = activity_config or ActivityConfig(start_to_close_timeout=timedelta(seconds=60))

    # `pydantic_ai.exceptions.UserError` and `pydantic.errors.PydanticUserError` are not retryable
    retry_policy = activity_config.get('retry_policy') or RetryPolicy()
    retry_policy.non_retryable_error_types = [
        *(retry_policy.non_retryable_error_types or []),
        UserError.__name__,
        PydanticUserError.__name__,
    ]
    activity_config['retry_policy'] = retry_policy
    self.activity_config = activity_config

    model_activity_config = model_activity_config or {}
    toolset_activity_config = toolset_activity_config or {}
    tool_activity_config = tool_activity_config or {}

    activity_name_prefix = f'agent__{self.name}'

    activities: list[Callable[..., Any]] = []

    async def event_stream_handler_activity(params: _EventStreamHandlerParams, deps: AgentDepsT) -> None:
        # We can never get here without an `event_stream_handler`, as `TemporalAgent.run_stream` and `TemporalAgent.iter` raise an error saying to use `TemporalAgent.run` instead,
        # and that only ends up calling `event_stream_handler` if it is set.
        assert self.event_stream_handler is not None

        run_context = self.run_context_type.deserialize_run_context(params.serialized_run_context, deps=deps)

        async def streamed_response():
            yield params.event

        await self.event_stream_handler(run_context, streamed_response())

    # Set type hint explicitly so that Temporal can take care of serialization and deserialization
    event_stream_handler_activity.__annotations__['deps'] = self.deps_type

    self.event_stream_handler_activity = activity.defn(name=f'{activity_name_prefix}__event_stream_handler')(
        event_stream_handler_activity
    )
    activities.append(self.event_stream_handler_activity)

    # Get wrapped agent's model if it's a Model instance
    wrapped_model = wrapped.model if isinstance(wrapped.model, Model) else None
    temporal_model = TemporalModel(
        wrapped_model,
        activity_name_prefix=activity_name_prefix,
        activity_config=activity_config | model_activity_config,
        deps_type=self.deps_type,
        run_context_type=self.run_context_type,
        event_stream_handler=self.event_stream_handler,
        models=models,
        provider_factory=provider_factory,
    )
    activities.extend(temporal_model.temporal_activities)
    self._temporal_model = temporal_model

    def temporalize_toolset(toolset: AbstractToolset[AgentDepsT]) -> AbstractToolset[AgentDepsT]:
        id = toolset.id
        if id is None:
            raise UserError(
                "Toolsets that are 'leaves' (i.e. those that implement their own tool listing and calling) need to have a unique `id` in order to be used with Temporal. The ID will be used to identify the toolset's activities within the workflow."
            )

        toolset = temporalize_toolset_func(
            toolset,
            activity_name_prefix,
            activity_config | toolset_activity_config.get(id, {}),
            tool_activity_config.get(id, {}),
            self.deps_type,
            self.run_context_type,
        )
        if isinstance(toolset, TemporalWrapperToolset):
            activities.extend(toolset.temporal_activities)
        return toolset

    temporal_toolsets = [toolset.visit_and_replace(temporalize_toolset) for toolset in wrapped.toolsets]

    self._toolsets = temporal_toolsets
    self._temporal_activities = activities

    self._temporal_overrides_active: ContextVar[bool] = ContextVar('_temporal_overrides_active', default=False)

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
