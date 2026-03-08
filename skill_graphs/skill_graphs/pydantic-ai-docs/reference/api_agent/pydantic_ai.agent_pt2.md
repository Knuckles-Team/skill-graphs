        self._system_prompt_dynamic_functions = {}

        self._max_result_retries = output_retries if output_retries is not None else retries
        self._max_tool_retries = retries
        self._tool_timeout = tool_timeout

        self._validation_context = validation_context

        self._builtin_tools = builtin_tools

        self._prepare_tools = prepare_tools
        self._prepare_output_tools = prepare_output_tools

        self._output_toolset = self._output_schema.toolset
        if self._output_toolset:
            self._output_toolset.max_retries = self._max_result_retries

        self._function_toolset = _AgentFunctionToolset(
            tools,
            max_retries=self._max_tool_retries,
            timeout=self._tool_timeout,
            output_schema=self._output_schema,
        )
        self._dynamic_toolsets = [
            DynamicToolset[AgentDepsT](toolset_func=toolset)
            for toolset in toolsets or []
            if not isinstance(toolset, AbstractToolset)
        ]
        self._user_toolsets = [toolset for toolset in toolsets or [] if isinstance(toolset, AbstractToolset)]

        self.history_processors = history_processors or []

        self._event_stream_handler = event_stream_handler

        self._concurrency_limiter = _concurrency.normalize_to_limiter(max_concurrency)

        self._override_name: ContextVar[_utils.Option[str]] = ContextVar('_override_name', default=None)
        self._override_deps: ContextVar[_utils.Option[AgentDepsT]] = ContextVar('_override_deps', default=None)
        self._override_model: ContextVar[_utils.Option[models.Model]] = ContextVar('_override_model', default=None)
        self._override_toolsets: ContextVar[_utils.Option[Sequence[AbstractToolset[AgentDepsT]]]] = ContextVar(
            '_override_toolsets', default=None
        )
        self._override_tools: ContextVar[
            _utils.Option[Sequence[Tool[AgentDepsT] | ToolFuncEither[AgentDepsT, ...]]]
        ] = ContextVar('_override_tools', default=None)
        self._override_instructions: ContextVar[
            _utils.Option[list[str | _system_prompt.SystemPromptFunc[AgentDepsT]]]
        ] = ContextVar('_override_instructions', default=None)
        self._override_metadata: ContextVar[_utils.Option[AgentMetadata[AgentDepsT]]] = ContextVar(
            '_override_metadata', default=None
        )

        self._enter_lock = Lock()
        self._entered_count = 0
        self._exit_stack = None

    @staticmethod
    def instrument_all(instrument: InstrumentationSettings | bool = True) -> None:
        """Set the instrumentation options for all agents where `instrument` is not set."""
        Agent._instrument_default = instrument

    @property
    def model(self) -> models.Model | models.KnownModelName | str | None:
        """The default model configured for this agent."""
        return self._model

    @model.setter
    def model(self, value: models.Model | models.KnownModelName | str | None) -> None:
        """Set the default model configured for this agent.

        We allow `str` here since the actual list of allowed models changes frequently.
        """
        self._model = value

    @property
    def name(self) -> str | None:
        """The name of the agent, used for logging.

        If `None`, we try to infer the agent name from the call frame when the agent is first run.
        """
        name_ = self._override_name.get()
        return name_.value if name_ else self._name

    @name.setter
    def name(self, value: str | None) -> None:
        """Set the name of the agent, used for logging."""
        self._name = value

    @property
    def deps_type(self) -> type:
        """The type of dependencies used by the agent."""
        return self._deps_type

    @property
    def output_type(self) -> OutputSpec[OutputDataT]:
        """The type of data output by agent runs, used to validate the data returned by the model, defaults to `str`."""
        return self._output_type

    @property
    def event_stream_handler(self) -> EventStreamHandler[AgentDepsT] | None:
        """Optional handler for events from the model's streaming response and the agent's execution of tools."""
        return self._event_stream_handler

    def __repr__(self) -> str:
        return f'{type(self).__name__}(model={self.model!r}, name={self.name!r}, end_strategy={self.end_strategy!r}, model_settings={self.model_settings!r}, output_type={self.output_type!r}, instrument={self.instrument!r})'

    @overload
    def iter(
        self,
        user_prompt: str | Sequence[_messages.UserContent] | None = None,
        *,
        output_type: None = None,
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
    ) -> AbstractAsyncContextManager[AgentRun[AgentDepsT, OutputDataT]]: ...

    @overload
    def iter(
        self,
        user_prompt: str | Sequence[_messages.UserContent] | None = None,
        *,
        output_type: OutputSpec[RunOutputDataT],
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
    ) -> AbstractAsyncContextManager[AgentRun[AgentDepsT, RunOutputDataT]]: ...

    @asynccontextmanager
    async def iter(
        self,
        user_prompt: str | Sequence[_messages.UserContent] | None = None,
        *,
        output_type: OutputSpec[Any] | None = None,
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

    def _get_metadata(
        self,
        ctx: RunContext[AgentDepsT],
        additional_metadata: AgentMetadata[AgentDepsT] | None = None,
    ) -> dict[str, Any] | None:
        metadata_override = self._override_metadata.get()
        if metadata_override is not None:
            return self._resolve_metadata_config(metadata_override.value, ctx)

        base_metadata = self._resolve_metadata_config(self._metadata, ctx)
        run_metadata = self._resolve_metadata_config(additional_metadata, ctx)

        if base_metadata and run_metadata:
            return {**base_metadata, **run_metadata}
        return run_metadata or base_metadata

    def _resolve_metadata_config(
        self,
        config: AgentMetadata[AgentDepsT] | None,
        ctx: RunContext[AgentDepsT],
    ) -> dict[str, Any] | None:
        if config is None:
            return None
        metadata = config(ctx) if callable(config) else config
        return metadata

    def _resolve_and_store_metadata(
        self,
        graph_run_ctx: GraphRunContext[_agent_graph.GraphAgentState, _agent_graph.GraphAgentDeps[AgentDepsT, Any]],
        metadata: AgentMetadata[AgentDepsT] | None,
    ) -> dict[str, Any] | None:
        run_context = build_run_context(graph_run_ctx)
        resolved_metadata = self._get_metadata(run_context, metadata)
        graph_run_ctx.state.metadata = resolved_metadata
        return resolved_metadata

    def _run_span_end_attributes(
        self,
        settings: InstrumentationSettings,
        usage: _usage.RunUsage,
        message_history: list[_messages.ModelMessage],
        new_message_index: int,
        metadata: dict[str, Any] | None = None,
    ) -> dict[str, str | int | float | bool]:
        if settings.version == 1:
            attrs = {
                'all_messages_events': json.dumps(
                    [InstrumentedModel.event_to_dict(e) for e in settings.messages_to_otel_events(message_history)]
                )
            }
        else:
            # Store the last instructions here for convenience
            last_instructions = InstrumentedModel._get_instructions(message_history)  # pyright: ignore[reportPrivateUsage]
            attrs: dict[str, Any] = {
                'pydantic_ai.all_messages': json.dumps(settings.messages_to_otel_messages(list(message_history))),
                **settings.system_instructions_attributes(last_instructions),
            }

            # If this agent run was provided with existing history, store an attribute indicating the point at which the
            # new messages begin.
            if new_message_index > 0:
                attrs['pydantic_ai.new_message_index'] = new_message_index

            # If the instructions for this agent run were not always the same, store an attribute that indicates that.
            # This can signal to an observability UI that different steps in the agent run had different instructions.
            # Note: We purposely only look at "new" messages because they are the only ones produced by this agent run.
            if any(
                (
                    isinstance(m, _messages.ModelRequest)
                    and m.instructions is not None
                    and m.instructions != last_instructions
                )
                for m in message_history[new_message_index:]
            ):
                attrs['pydantic_ai.variable_instructions'] = True

        if metadata is not None:
            attrs['metadata'] = json.dumps(InstrumentedModel.serialize_any(metadata))

        usage_attrs = (
            {
                k.replace('gen_ai.usage.', 'gen_ai.aggregated_usage.', 1): v
                for k, v in usage.opentelemetry_attributes().items()
            }
            if settings.use_aggregated_usage_attribute_names
            else usage.opentelemetry_attributes()
        )

        return {
            **usage_attrs,
            **attrs,
            'logfire.json_schema': json.dumps(
                {
                    'type': 'object',
                    'properties': {
                        **{k: {'type': 'array'} if isinstance(v, str) else {} for k, v in attrs.items()},
                        'final_result': {'type': 'object'},
                    },
                }
            ),
        }

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
