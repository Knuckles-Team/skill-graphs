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
    if infer_name and self.name is None:
        self._infer_name(inspect.currentframe())

    model_used = self._get_model(model)
    del model

    deps = self._get_deps(deps)
    output_schema = self._prepare_output_schema(output_type)

    output_type_ = output_type or self.output_type

    # We consider it a user error if a user tries to restrict the result type while having an output validator that
    # may change the result type from the restricted type to something else. Therefore, we consider the following
    # typecast reasonable, even though it is possible to violate it with otherwise-type-checked code.
    output_validators = self._output_validators

    output_toolset = self._output_toolset
    if output_schema != self._output_schema or output_validators:
        output_toolset = output_schema.toolset
        if output_toolset:
            output_toolset.max_retries = self._max_result_retries
            output_toolset.output_validators = output_validators
    toolset = self._get_toolset(output_toolset=output_toolset, additional_toolsets=toolsets)
    tool_manager = ToolManager[AgentDepsT](toolset, default_max_retries=self._max_tool_retries)

    # Build the graph
    graph = _agent_graph.build_agent_graph(self.name, self._deps_type, output_type_)

    # Build the initial state
    usage = usage or _usage.RunUsage()
    state = _agent_graph.GraphAgentState(
        message_history=list(message_history) if message_history else [],
        usage=usage,
        retries=0,
        run_step=0,
    )

    # Merge model settings in order of precedence: run > agent > model
    merged_settings = merge_model_settings(model_used.settings, self.model_settings)
    model_settings = merge_model_settings(merged_settings, model_settings)
    usage_limits = usage_limits or _usage.UsageLimits()

    instructions_literal, instructions_functions = self._get_instructions(additional_instructions=instructions)

    async def get_instructions(run_context: RunContext[AgentDepsT]) -> str | None:
        parts = [
            instructions_literal,
            *[await func.run(run_context) for func in instructions_functions],
        ]

        parts = [p for p in parts if p]
        if not parts:
            return None
        return '\n\n'.join(parts).strip()

    if isinstance(model_used, InstrumentedModel):
        instrumentation_settings = model_used.instrumentation_settings
        tracer = model_used.instrumentation_settings.tracer
    else:
        instrumentation_settings = None
        tracer = NoOpTracer()

    graph_deps = _agent_graph.GraphAgentDeps[AgentDepsT, OutputDataT](
        user_deps=deps,
        prompt=user_prompt,
        new_message_index=len(message_history) if message_history else 0,
        resumed_request=None,
        model=model_used,
        model_settings=model_settings,
        usage_limits=usage_limits,
        max_result_retries=self._max_result_retries,
        end_strategy=self.end_strategy,
        output_schema=output_schema,
        output_validators=output_validators,
        validation_context=self._validation_context,
        history_processors=self.history_processors,
        builtin_tools=[*self._builtin_tools, *(builtin_tools or [])],
        tool_manager=tool_manager,
        tracer=tracer,
        get_instructions=get_instructions,
        instrumentation_settings=instrumentation_settings,
    )

    user_prompt_node = _agent_graph.UserPromptNode[AgentDepsT](
        user_prompt=user_prompt,
        deferred_tool_results=deferred_tool_results,
        instructions=instructions_literal,
        instructions_functions=instructions_functions,
        system_prompts=self._system_prompts,
        system_prompt_functions=self._system_prompt_functions,
        system_prompt_dynamic_functions=self._system_prompt_dynamic_functions,
    )

    agent_name = self.name or 'agent'
    instrumentation_names = InstrumentationNames.for_version(
        instrumentation_settings.version if instrumentation_settings else DEFAULT_INSTRUMENTATION_VERSION
    )

    run_span = tracer.start_span(
        instrumentation_names.get_agent_run_span_name(agent_name),
        attributes={
            'model_name': model_used.model_name if model_used else 'no-model',
            'agent_name': agent_name,
            'gen_ai.agent.name': agent_name,
            'logfire.msg': f'{agent_name} run',
        },
    )

    run_metadata: dict[str, Any] | None = None
    try:
        async with (
            _concurrency.get_concurrency_context(self._concurrency_limiter, f'agent:{agent_name}'),
            graph.iter(
                inputs=user_prompt_node,
                state=state,
                deps=graph_deps,
                span=use_span(run_span) if run_span.is_recording() else None,
                infer_name=False,
            ) as graph_run,
        ):
            async with toolset:
                agent_run = AgentRun(graph_run)
                run_metadata = self._resolve_and_store_metadata(agent_run.ctx, metadata)

                try:
                    yield agent_run
                finally:
                    if agent_run.result is not None:
                        run_metadata = self._resolve_and_store_metadata(agent_run.ctx, metadata)
                    else:
                        run_metadata = graph_run.state.metadata

                final_result = agent_run.result
                if (
                    instrumentation_settings
                    and instrumentation_settings.include_content
                    and run_span.is_recording()
                    and final_result is not None
                ):
                    run_span.set_attribute(
                        'final_result',
                        (
                            final_result.output
                            if isinstance(final_result.output, str)
                            else json.dumps(InstrumentedModel.serialize_any(final_result.output))
                        ),
                    )
    finally:
        try:
            if instrumentation_settings and run_span.is_recording():
                run_span.set_attributes(
                    self._run_span_end_attributes(
                        instrumentation_settings,
                        usage,
                        state.message_history,
                        graph_deps.new_message_index,
                        run_metadata,
                    )
                )
        finally:
            run_span.end()

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
        [AbstractToolset[](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.AbstractToolset "AbstractToolset \(pydantic_ai.toolsets.AbstractToolset\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



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
   \(pydantic_ai.tools.AgentDepsT\)")] | Unset = UNSET,
    metadata: AgentMetadata[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



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
`toolsets` |  `AbstractToolset[](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.AbstractToolset "AbstractToolset \(pydantic_ai.toolsets.AbstractToolset\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



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
`metadata` |  `AgentMetadata[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")] | Unset` |  The metadata to use instead of the metadata passed to the agent constructor. When set, any per-run `metadata` argument is ignored. |  `UNSET`
Source code in `pydantic_ai_slim/pydantic_ai/agent/__init__.py`
```
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
941
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
    metadata: AgentMetadata[AgentDepsT] | _utils.Unset = _utils.UNSET,
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
        metadata: The metadata to use instead of the metadata passed to the agent constructor. When set, any
            per-run `metadata` argument is ignored.
    """
    if _utils.is_set(name):
        name_token = self._override_name.set(_utils.Some(name))
    else:
        name_token = None

    if _utils.is_set(deps):
        deps_token = self._override_deps.set(_utils.Some(deps))
    else:
        deps_token = None

    if _utils.is_set(model):
        model_token = self._override_model.set(_utils.Some(models.infer_model(model)))
    else:
        model_token = None

    if _utils.is_set(toolsets):
        toolsets_token = self._override_toolsets.set(_utils.Some(toolsets))
    else:
        toolsets_token = None

    if _utils.is_set(tools):
        tools_token = self._override_tools.set(_utils.Some(tools))
    else:
        tools_token = None

    if _utils.is_set(instructions):
        normalized_instructions = self._normalize_instructions(instructions)
        instructions_token = self._override_instructions.set(_utils.Some(normalized_instructions))
    else:
        instructions_token = None

    if _utils.is_set(metadata):
        metadata_token = self._override_metadata.set(_utils.Some(metadata))
    else:
        metadata_token = None

    try:
        yield
    finally:
        if name_token is not None:
            self._override_name.reset(name_token)
        if deps_token is not None:
            self._override_deps.reset(deps_token)
        if model_token is not None:
            self._override_model.reset(model_token)
        if toolsets_token is not None:
            self._override_toolsets.reset(toolsets_token)
        if tools_token is not None:
            self._override_tools.reset(tools_token)
        if instructions_token is not None:
            self._override_instructions.reset(instructions_token)
        if metadata_token is not None:
            self._override_metadata.reset(metadata_token)

```

---|---
####  instructions
```
instructions(
    func: [[RunContext[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext



      dataclass
   \(pydantic_ai.tools.RunContext\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]],  | None],
) -> [[RunContext[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext



      dataclass
   \(pydantic_ai.tools.RunContext\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]],  | None]

```

```
instructions(
    func: [
        [RunContext[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext



      dataclass
   \(pydantic_ai.tools.RunContext\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]], [ | None]
    ],
) -> [
    [RunContext[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext



      dataclass
   \(pydantic_ai.tools.RunContext\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]], [ | None]
]

```

```
instructions(
    func: [[],  | None],
) -> [[],  | None]

```

```
instructions(
    func: [[], [ | None]],
) -> [[], [ | None]]

```

```
instructions() -> [
    [SystemPromptFunc[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]],
    SystemPromptFunc[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")],
]

```

```
instructions(
    func: SystemPromptFunc[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")] | None = None,
) -> (
    [
        [SystemPromptFunc[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]],
        SystemPromptFunc[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")],
    ]
    | SystemPromptFunc[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]
)

```

Decorator to register an instructions function.
Optionally takes [`RunContext`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext



      dataclass
  ") as its only argument. Can decorate a sync or async functions.
The decorator can be used bare (`agent.instructions`).
Overloads for every possible signature of `instructions` are included so the decorator doesn't obscure the type of the function.
Example:
```
from pydantic_ai import Agent, RunContext

agent = Agent('test', deps_type=str)

@agent.instructions
def simple_instructions() -> str:
    return 'foobar'

@agent.instructions
async def async_instructions(ctx: RunContext[str]) -> str:
    return f'{ctx.deps} is the best'

```

Source code in `pydantic_ai_slim/pydantic_ai/agent/__init__.py`
```
 978
 979
 980
 981
 982
 983
 984
 985
 986
 987
 988
 989
 990
 991
 992
 993
 994
 995
 996
 997
 998
 999
1000
1001
1002
1003
1004
1005
1006
1007
1008
1009
1010
1011
1012
1013
1014
1015
1016
1017
1018
1019
1020
1021
1022
```
| ```
def instructions(
    self,
    func: _system_prompt.SystemPromptFunc[AgentDepsT] | None = None,
    /,
) -> (
    Callable[[_system_prompt.SystemPromptFunc[AgentDepsT]], _system_prompt.SystemPromptFunc[AgentDepsT]]
    | _system_prompt.SystemPromptFunc[AgentDepsT]
):
    """Decorator to register an instructions function.

    Optionally takes [`RunContext`][pydantic_ai.tools.RunContext] as its only argument.
    Can decorate a sync or async functions.

    The decorator can be used bare (`agent.instructions`).

    Overloads for every possible signature of `instructions` are included so the decorator doesn't obscure
    the type of the function.

    Example:
```python
    from pydantic_ai import Agent, RunContext

    agent = Agent('test', deps_type=str)

    @agent.instructions
    def simple_instructions() -> str:
        return 'foobar'

    @agent.instructions
    async def async_instructions(ctx: RunContext[str]) -> str:
        return f'{ctx.deps} is the best'
```
    """
    if func is None:

        def decorator(
            func_: _system_prompt.SystemPromptFunc[AgentDepsT],
        ) -> _system_prompt.SystemPromptFunc[AgentDepsT]:
            self._instructions.append(func_)
            return func_

        return decorator
    else:
        self._instructions.append(func)
        return func

```

---|---
####  system_prompt
```
system_prompt(
    func: [[RunContext[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext



      dataclass
   \(pydantic_ai.tools.RunContext\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]],  | None],
) -> [[RunContext[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext



      dataclass
   \(pydantic_ai.tools.RunContext\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]],  | None]

```

```
system_prompt(
    func: [
        [RunContext[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext



      dataclass
   \(pydantic_ai.tools.RunContext\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]], [ | None]
    ],
) -> [
    [RunContext[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext



      dataclass
   \(pydantic_ai.tools.RunContext\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]], [ | None]
]

```

```
system_prompt(
    func: [[],  | None],
) -> [[],  | None]

```

```
system_prompt(
    func: [[], [ | None]],
) -> [[], [ | None]]

```

```
system_prompt(*, dynamic:  = False) -> [
    [SystemPromptFunc[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]],
    SystemPromptFunc[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")],
]

```

```
system_prompt(
    func: SystemPromptFunc[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")] | None = None,
    /,
    *,
    dynamic:  = False,
) -> (
    [
        [SystemPromptFunc[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]],
        SystemPromptFunc[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")],
    ]
    | SystemPromptFunc[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]
)

```

Decorator to register a system prompt function.
Optionally takes [`RunContext`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext



      dataclass
  ") as its only argument. Can decorate a sync or async functions.
The decorator can be used either bare (`agent.system_prompt`) or as a function call (`agent.system_prompt(...)`), see the examples below.
Overloads for every possible signature of `system_prompt` are included so the decorator doesn't obscure the type of the function, see `tests/typed_agent.py` for tests.
Parameters:
Name | Type | Description | Default
---|---|---|---
`func` |  `SystemPromptFunc[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")] | None` |  The function to decorate |  `None`
`dynamic` |  |  If True, the system prompt will be reevaluated even when `messages_history` is provided, see [`SystemPromptPart.dynamic_ref`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.SystemPromptPart.dynamic_ref "dynamic_ref



      class-attribute
      instance-attribute
  ") |  `False`
Example:
```
from pydantic_ai import Agent, RunContext

agent = Agent('test', deps_type=str)

@agent.system_prompt
def simple_system_prompt() -> str:
    return 'foobar'

@agent.system_prompt(dynamic=True)
async def async_system_prompt(ctx: RunContext[str]) -> str:
    return f'{ctx.deps} is the best'

```

Source code in `pydantic_ai_slim/pydantic_ai/agent/__init__.py`
