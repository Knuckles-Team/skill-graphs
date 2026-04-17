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
    event_stream_handler: (
        EventStreamHandler[](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.EventStreamHandler "EventStreamHandler



      module-attribute
   \(pydantic_ai.agent.EventStreamHandler\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")] | None
    ) = None,
    mcp_step_config: StepConfig[](https://ai.pydantic.dev/api/durable_exec/#pydantic_ai.durable_exec.dbos.StepConfig "StepConfig \(pydantic_ai.durable_exec.dbos._utils.StepConfig\)") | None = None,
    model_step_config: StepConfig[](https://ai.pydantic.dev/api/durable_exec/#pydantic_ai.durable_exec.dbos.StepConfig "StepConfig \(pydantic_ai.durable_exec.dbos._utils.StepConfig\)") | None = None,
    parallel_execution_mode: DBOSParallelExecutionMode[](https://ai.pydantic.dev/api/durable_exec/#pydantic_ai.durable_exec.dbos.DBOSParallelExecutionMode "DBOSParallelExecutionMode



      module-attribute
   \(pydantic_ai.durable_exec.dbos._agent.DBOSParallelExecutionMode\)") = "parallel_ordered_events"
)

```

Wrap an agent to enable it with DBOS durable workflows, by automatically offloading model requests, tool calls, and MCP server communication to DBOS steps.
After wrapping, the original agent can still be used as normal outside of the DBOS workflow.
Parameters:
Name | Type | Description | Default
---|---|---|---
`wrapped` |  `AbstractAgent[](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AbstractAgent "AbstractAgent \(pydantic_ai.agent.AbstractAgent\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)"), OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")]` |  The agent to wrap. |  _required_
`name` |  |  Optional unique agent name to use as the DBOS configured instance name. If not provided, the agent's `name` will be used. |  `None`
`event_stream_handler` |  `EventStreamHandler[](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.EventStreamHandler "EventStreamHandler



      module-attribute
   \(pydantic_ai.agent.EventStreamHandler\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")] | None` |  Optional event stream handler to use instead of the one set on the wrapped agent. |  `None`
`mcp_step_config` |  `StepConfig[](https://ai.pydantic.dev/api/durable_exec/#pydantic_ai.durable_exec.dbos.StepConfig "StepConfig \(pydantic_ai.durable_exec.dbos._utils.StepConfig\)") | None` |  The base DBOS step config to use for MCP server steps. If no config is provided, use the default settings of DBOS. |  `None`
`model_step_config` |  `StepConfig[](https://ai.pydantic.dev/api/durable_exec/#pydantic_ai.durable_exec.dbos.StepConfig "StepConfig \(pydantic_ai.durable_exec.dbos._utils.StepConfig\)") | None` |  The DBOS step config to use for model request steps. If no config is provided, use the default settings of DBOS. |  `None`
`parallel_execution_mode` |  `DBOSParallelExecutionMode[](https://ai.pydantic.dev/api/durable_exec/#pydantic_ai.durable_exec.dbos.DBOSParallelExecutionMode "DBOSParallelExecutionMode



      module-attribute
   \(pydantic_ai.durable_exec.dbos._agent.DBOSParallelExecutionMode\)")` |  The mode for executing tool calls: - 'parallel_ordered_events' (default): Run tool calls in parallel, but events are emitted in order, after all calls complete. - 'sequential': Run tool calls one at a time in order. |  `'parallel_ordered_events'`
Source code in `pydantic_ai_slim/pydantic_ai/durable_exec/dbos/_agent.py`
```
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
```
| ```
def __init__(
    self,
    wrapped: AbstractAgent[AgentDepsT, OutputDataT],
    *,
    name: str | None = None,
    event_stream_handler: EventStreamHandler[AgentDepsT] | None = None,
    mcp_step_config: StepConfig | None = None,
    model_step_config: StepConfig | None = None,
    parallel_execution_mode: DBOSParallelExecutionMode = 'parallel_ordered_events',
):
    """Wrap an agent to enable it with DBOS durable workflows, by automatically offloading model requests, tool calls, and MCP server communication to DBOS steps.

    After wrapping, the original agent can still be used as normal outside of the DBOS workflow.

    Args:
        wrapped: The agent to wrap.
        name: Optional unique agent name to use as the DBOS configured instance name. If not provided, the agent's `name` will be used.
        event_stream_handler: Optional event stream handler to use instead of the one set on the wrapped agent.
        mcp_step_config: The base DBOS step config to use for MCP server steps. If no config is provided, use the default settings of DBOS.
        model_step_config: The DBOS step config to use for model request steps. If no config is provided, use the default settings of DBOS.
        parallel_execution_mode: The mode for executing tool calls:
            - 'parallel_ordered_events' (default): Run tool calls in parallel, but events are emitted in order, after all calls complete.
            - 'sequential': Run tool calls one at a time in order.
    """
    super().__init__(wrapped)

    self._name = name or wrapped.name
    self._event_stream_handler = event_stream_handler
    self._parallel_execution_mode = cast(ParallelExecutionMode, parallel_execution_mode)
    if self._name is None:
        raise UserError(
            "An agent needs to have a unique `name` in order to be used with DBOS. The name will be used to identify the agent's workflows and steps."
        )

    # Merge the config with the default DBOS config
    self._mcp_step_config = mcp_step_config or {}
    self._model_step_config = model_step_config or {}

    if not isinstance(wrapped.model, Model):
        raise UserError(
            'An agent needs to have a `model` in order to be used with DBOS, it cannot be set at agent run time.'
        )

    dbos_model = DBOSModel(
        wrapped.model,
        step_name_prefix=self._name,
        step_config=self._model_step_config,
        event_stream_handler=self.event_stream_handler,
    )
    self._model = dbos_model

    dbosagent_name = self._name

    def dbosify_toolset(toolset: AbstractToolset[AgentDepsT]) -> AbstractToolset[AgentDepsT]:
        # Replace MCPServer with DBOSMCPServer
        try:
            from pydantic_ai.mcp import MCPServer

            from ._mcp_server import DBOSMCPServer
        except ImportError:
            pass
        else:
            if isinstance(toolset, MCPServer):
                return DBOSMCPServer(
                    wrapped=toolset,
                    step_name_prefix=dbosagent_name,
                    step_config=self._mcp_step_config,
                )

        # Replace FastMCPToolset with DBOSFastMCPToolset
        try:
            from pydantic_ai.toolsets.fastmcp import FastMCPToolset

            from ._fastmcp_toolset import DBOSFastMCPToolset
        except ImportError:
            pass
        else:
            if isinstance(toolset, FastMCPToolset):
                return DBOSFastMCPToolset(
                    wrapped=toolset,
                    step_name_prefix=dbosagent_name,
                    step_config=self._mcp_step_config,
                )

        return toolset

    dbos_toolsets = [toolset.visit_and_replace(dbosify_toolset) for toolset in wrapped.toolsets]
    self._toolsets = dbos_toolsets
    DBOSConfiguredInstance.__init__(self, self._name)

    # Wrap the `run` method in a DBOS workflow
    @DBOS.workflow(name=f'{self._name}.run')
    async def wrapped_run_workflow(
        user_prompt: str | Sequence[_messages.UserContent] | None = None,
        *,
        output_type: OutputSpec[RunOutputDataT] | None = None,
        message_history: Sequence[_messages.ModelMessage] | None = None,
        deferred_tool_results: DeferredToolResults | None = None,
        model: models.Model | models.KnownModelName | str | None = None,
        instructions: Instructions[AgentDepsT] = None,
        deps: AgentDepsT,
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
        with self._dbos_overrides():
            return await super(WrapperAgent, self).run(
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
                builtin_tools=builtin_tools,
                event_stream_handler=event_stream_handler,
                **_deprecated_kwargs,
            )

    self.dbos_wrapped_run_workflow = wrapped_run_workflow

    # Wrap the `run_sync` method in a DBOS workflow
    @DBOS.workflow(name=f'{self._name}.run_sync')
    def wrapped_run_sync_workflow(
        user_prompt: str | Sequence[_messages.UserContent] | None = None,
        *,
        output_type: OutputSpec[RunOutputDataT] | None = None,
        message_history: Sequence[_messages.ModelMessage] | None = None,
        deferred_tool_results: DeferredToolResults | None = None,
        model: models.Model | models.KnownModelName | str | None = None,
        deps: AgentDepsT,
        model_settings: ModelSettings | None = None,
        instructions: Instructions[AgentDepsT] = None,
        usage_limits: _usage.UsageLimits | None = None,
        usage: _usage.RunUsage | None = None,
        metadata: AgentMetadata[AgentDepsT] | None = None,
        infer_name: bool = True,
        toolsets: Sequence[AbstractToolset[AgentDepsT]] | None = None,
        builtin_tools: Sequence[AbstractBuiltinTool | BuiltinToolFunc[AgentDepsT]] | None = None,
        event_stream_handler: EventStreamHandler[AgentDepsT] | None = None,
        **_deprecated_kwargs: Never,
    ) -> AgentRunResult[Any]:
        with self._dbos_overrides():
            return super(DBOSAgent, self).run_sync(
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
                builtin_tools=builtin_tools,
                event_stream_handler=event_stream_handler,
                **_deprecated_kwargs,
            )

    self.dbos_wrapped_run_sync_workflow = wrapped_run_sync_workflow

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
