
        literal = '\n'.join(literal_parts).strip() or None
        return literal, functions

    def _get_toolset(
        self,
        output_toolset: AbstractToolset[AgentDepsT] | None | _utils.Unset = _utils.UNSET,
        additional_toolsets: Sequence[AbstractToolset[AgentDepsT]] | None = None,
    ) -> AbstractToolset[AgentDepsT]:
        """Get the complete toolset.

        Args:
            output_toolset: The output toolset to use instead of the one built at agent construction time.
            additional_toolsets: Additional toolsets to add, unless toolsets have been overridden.
        """
        toolsets = self.toolsets
        # Don't add additional toolsets if the toolsets have been overridden
        if additional_toolsets and self._override_toolsets.get() is None:
            toolsets = [*toolsets, *additional_toolsets]

        toolset = CombinedToolset(toolsets)

        def copy_dynamic_toolsets(toolset: AbstractToolset[AgentDepsT]) -> AbstractToolset[AgentDepsT]:
            if isinstance(toolset, DynamicToolset):
                return toolset.copy()
            else:
                return toolset

        toolset = toolset.visit_and_replace(copy_dynamic_toolsets)

        if self._prepare_tools:
            toolset = PreparedToolset(toolset, self._prepare_tools)

        output_toolset = output_toolset if _utils.is_set(output_toolset) else self._output_toolset
        if output_toolset is not None:
            if self._prepare_output_tools:
                output_toolset = PreparedToolset(output_toolset, self._prepare_output_tools)
            toolset = CombinedToolset([output_toolset, toolset])

        return toolset

    @property
    def toolsets(self) -> Sequence[AbstractToolset[AgentDepsT]]:
        """All toolsets registered on the agent, including a function toolset holding tools that were registered on the agent directly.

        Output tools are not included.
        """
        toolsets: list[AbstractToolset[AgentDepsT]] = []

        if some_tools := self._override_tools.get():
            function_toolset = _AgentFunctionToolset(
                some_tools.value,
                max_retries=self._max_tool_retries,
                timeout=self._tool_timeout,
                output_schema=self._output_schema,
            )
        else:
            function_toolset = self._function_toolset
        toolsets.append(function_toolset)

        if some_user_toolsets := self._override_toolsets.get():
            user_toolsets = some_user_toolsets.value
        else:
            user_toolsets = [*self._user_toolsets, *self._dynamic_toolsets]
        toolsets.extend(user_toolsets)

        return toolsets

    @overload
    def _prepare_output_schema(self, output_type: None) -> _output.OutputSchema[OutputDataT]: ...

    @overload
    def _prepare_output_schema(
        self, output_type: OutputSpec[RunOutputDataT]
    ) -> _output.OutputSchema[RunOutputDataT]: ...

    def _prepare_output_schema(self, output_type: OutputSpec[Any] | None) -> _output.OutputSchema[Any]:
        if output_type is not None:
            if self._output_validators:
                raise exceptions.UserError('Cannot set a custom run `output_type` when the agent has output validators')
            schema = _output.OutputSchema.build(output_type)
        else:
            schema = self._output_schema

        return schema

    async def __aenter__(self) -> Self:
        """Enter the agent context.

        This will start all [`MCPServerStdio`s][pydantic_ai.mcp.MCPServerStdio] registered as `toolsets` so they are ready to be used.

        This is a no-op if the agent has already been entered.
        """
        async with self._enter_lock:
            if self._entered_count == 0:
                async with AsyncExitStack() as exit_stack:
                    toolset = self._get_toolset()
                    await exit_stack.enter_async_context(toolset)

                    self._exit_stack = exit_stack.pop_all()
            self._entered_count += 1
        return self

    async def __aexit__(self, *args: Any) -> bool | None:
        async with self._enter_lock:
            self._entered_count -= 1
            if self._entered_count == 0 and self._exit_stack is not None:
                await self._exit_stack.aclose()
                self._exit_stack = None

    def set_mcp_sampling_model(self, model: models.Model | models.KnownModelName | str | None = None) -> None:
        """Set the sampling model on all MCP servers registered with the agent.

        If no sampling model is provided, the agent's model will be used.
        """
        try:
            sampling_model = models.infer_model(model) if model else self._get_model(None)
        except exceptions.UserError as e:
            raise exceptions.UserError('No sampling model provided and no model set on the agent.') from e

        from ..mcp import MCPServer

        def _set_sampling_model(toolset: AbstractToolset[AgentDepsT]) -> None:
            if isinstance(toolset, MCPServer):
                toolset.sampling_model = sampling_model

        self._get_toolset().apply(_set_sampling_model)

    def to_web(
        self,
        *,
        models: ModelsParam = None,
        builtin_tools: list[AbstractBuiltinTool] | None = None,
        deps: AgentDepsT = None,
        model_settings: ModelSettings | None = None,
        instructions: str | None = None,
        html_source: str | Path | None = None,
    ) -> Starlette:
        """Create a Starlette app that serves a web chat UI for this agent.

        This method returns a pre-configured Starlette application that provides a web-based
        chat interface for interacting with the agent. By default, the UI is fetched from a
        CDN and cached on first use.

        The returned Starlette application can be mounted into a FastAPI app or run directly
        with any ASGI server (uvicorn, hypercorn, etc.).

        Note that the `deps` and `model_settings` will be the same for each request.
        To provide different `deps` for each request use the lower-level adapters directly.

        Args:
            models: Additional models to make available in the UI. Can be:
                - A sequence of model names/instances (e.g., `['openai:gpt-5', 'anthropic:claude-sonnet-4-6']`)
                - A dict mapping display labels to model names/instances
                  (e.g., `{'GPT 5': 'openai:gpt-5', 'Claude': 'anthropic:claude-sonnet-4-6'}`)
                The agent's model is always included. Builtin tool support is automatically
                determined from each model's profile.
            builtin_tools: Additional builtin tools to make available in the UI.
                The agent's configured builtin tools are always included. Tool labels
                in the UI are derived from the tool's `label` property.
            deps: Optional dependencies to use for all requests.
            model_settings: Optional settings to use for all model requests.
            instructions: Optional extra instructions to pass to each agent run.
            html_source: Path or URL for the chat UI HTML. Can be:
                - None (default): Fetches from CDN and caches locally
                - A Path instance: Reads from the local file
                - A URL string (http:// or https://): Fetches from the URL
                - A file path string: Reads from the local file

        Returns:
            A configured Starlette application ready to be served (e.g., with uvicorn)

        Example:
        ```python
            from pydantic_ai import Agent
            from pydantic_ai.builtin_tools import WebSearchTool

            agent = Agent('openai:gpt-5', builtin_tools=[WebSearchTool()])

            # Simple usage - uses agent's model and builtin tools
            app = agent.to_web()

            # Or provide additional models for UI selection
            app = agent.to_web(models=['openai:gpt-5', 'anthropic:claude-sonnet-4-6'])

            # Then run with: uvicorn app:app --reload
        ```
        """
        from ..ui._web import create_web_app

        return create_web_app(
            self,
            models=models,
            builtin_tools=builtin_tools,
            deps=deps,
            model_settings=model_settings,
            instructions=instructions,
            html_source=html_source,
        )

    @asynccontextmanager
    @deprecated(
        '`run_mcp_servers` is deprecated, use `async with agent:` instead. If you need to set a sampling model on all MCP servers, use `agent.set_mcp_sampling_model()`.'
    )
    async def run_mcp_servers(
        self, model: models.Model | models.KnownModelName | str | None = None
    ) -> AsyncIterator[None]:
        """Run [`MCPServerStdio`s][pydantic_ai.mcp.MCPServerStdio] so they can be used by the agent.

        Deprecated: use [`async with agent`][pydantic_ai.agent.Agent.__aenter__] instead.
        If you need to set a sampling model on all MCP servers, use [`agent.set_mcp_sampling_model()`][pydantic_ai.agent.Agent.set_mcp_sampling_model].

        Returns: a context manager to start and shutdown the servers.
        """
        try:
            self.set_mcp_sampling_model(model)
        except exceptions.UserError:
            if model is not None:
                raise

        async with self:
            yield

```

---|---
####  __init__
```
__init__(
    model: Model[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.Model "Model \(pydantic_ai.models.Model\)") | KnownModelName[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.KnownModelName "KnownModelName



      module-attribute
   \(pydantic_ai.models.KnownModelName\)") |  | None = None,
    *,
    output_type: OutputSpec[OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")] = ,
    instructions: Instructions[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")] = None,
    system_prompt:  | [] = (),
    deps_type: [AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")] = NoneType,
    name:  | None = None,
    model_settings: ModelSettings[](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings \(pydantic_ai.settings.ModelSettings\)") | None = None,
    retries:  = 1,
    validation_context: (
         | [[RunContext[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext



      dataclass
   \(pydantic_ai.tools.RunContext\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]], ]
    ) = None,
    output_retries:  | None = None,
    tools: [
        Tool[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.Tool "Tool



      dataclass
   \(pydantic_ai.tools.Tool\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")] | ToolFuncEither[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolFuncEither "ToolFuncEither



      module-attribute
   \(pydantic_ai.tools.ToolFuncEither\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)"), ...]
    ] = (),
    builtin_tools: [
        AbstractBuiltinTool[](https://ai.pydantic.dev/api/builtin_tools/#pydantic_ai.builtin_tools.AbstractBuiltinTool "AbstractBuiltinTool



      dataclass
   \(pydantic_ai.builtin_tools.AbstractBuiltinTool\)") | BuiltinToolFunc[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.BuiltinToolFunc "BuiltinToolFunc



      module-attribute
   \(pydantic_ai.tools.BuiltinToolFunc\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]
    ] = (),
    prepare_tools: (
        ToolsPrepareFunc[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolsPrepareFunc "ToolsPrepareFunc



      module-attribute
   \(pydantic_ai.tools.ToolsPrepareFunc\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")] | None
    ) = None,
    prepare_output_tools: (
        ToolsPrepareFunc[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolsPrepareFunc "ToolsPrepareFunc



      module-attribute
   \(pydantic_ai.tools.ToolsPrepareFunc\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")] | None
    ) = None,
    toolsets: (
        [
            AbstractToolset[](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.AbstractToolset "AbstractToolset \(pydantic_ai.toolsets.AbstractToolset\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]
            | ToolsetFunc[](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.ToolsetFunc "ToolsetFunc



      module-attribute
   \(pydantic_ai.toolsets._dynamic.ToolsetFunc\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]
        ]
        | None
    ) = None,
    defer_model_check:  = False,
    end_strategy: EndStrategy[](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.EndStrategy "EndStrategy



      module-attribute
   \(pydantic_ai._agent_graph.EndStrategy\)") = "early",
    instrument: (
        InstrumentationSettings[](https://ai.pydantic.dev/api/models/instrumented/#pydantic_ai.models.instrumented.InstrumentationSettings "InstrumentationSettings



      dataclass
   \(pydantic_ai.models.instrumented.InstrumentationSettings\)") |  | None
    ) = None,
    metadata: AgentMetadata[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")] | None = None,
    history_processors: (
        [HistoryProcessor[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]] | None
    ) = None,
    event_stream_handler: (
        EventStreamHandler[](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.EventStreamHandler "EventStreamHandler



      module-attribute
   \(pydantic_ai.agent.abstract.EventStreamHandler\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")] | None
    ) = None,
    tool_timeout:  | None = None,
    max_concurrency: AnyConcurrencyLimit[](https://ai.pydantic.dev/api/concurrency/#pydantic_ai.AnyConcurrencyLimit "pydantic_ai.concurrency.AnyConcurrencyLimit") = None
) -> None

```

```
__init__(
    model: Model[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.Model "Model \(pydantic_ai.models.Model\)") | KnownModelName[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.KnownModelName "KnownModelName



      module-attribute
   \(pydantic_ai.models.KnownModelName\)") |  | None = None,
    *,
    output_type: OutputSpec[OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")] = ,
    instructions: Instructions[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")] = None,
    system_prompt:  | [] = (),
    deps_type: [AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")] = NoneType,
    name:  | None = None,
    model_settings: ModelSettings[](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings \(pydantic_ai.settings.ModelSettings\)") | None = None,
    retries:  = 1,
    validation_context: (
         | [[RunContext[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext



      dataclass
   \(pydantic_ai.tools.RunContext\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]], ]
    ) = None,
    output_retries:  | None = None,
    tools: [
        Tool[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.Tool "Tool



      dataclass
   \(pydantic_ai.tools.Tool\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")] | ToolFuncEither[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolFuncEither "ToolFuncEither



      module-attribute
   \(pydantic_ai.tools.ToolFuncEither\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)"), ...]
    ] = (),
    builtin_tools: [
        AbstractBuiltinTool[](https://ai.pydantic.dev/api/builtin_tools/#pydantic_ai.builtin_tools.AbstractBuiltinTool "AbstractBuiltinTool



      dataclass
   \(pydantic_ai.builtin_tools.AbstractBuiltinTool\)") | BuiltinToolFunc[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.BuiltinToolFunc "BuiltinToolFunc



      module-attribute
   \(pydantic_ai.tools.BuiltinToolFunc\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]
    ] = (),
    prepare_tools: (
        ToolsPrepareFunc[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolsPrepareFunc "ToolsPrepareFunc



      module-attribute
   \(pydantic_ai.tools.ToolsPrepareFunc\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")] | None
    ) = None,
    prepare_output_tools: (
        ToolsPrepareFunc[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolsPrepareFunc "ToolsPrepareFunc



      module-attribute
   \(pydantic_ai.tools.ToolsPrepareFunc\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")] | None
    ) = None,
    mcp_servers: [MCPServer[](https://ai.pydantic.dev/api/mcp/#pydantic_ai.mcp.MCPServer "MCPServer \(pydantic_ai.mcp.MCPServer\)")] = (),
    defer_model_check:  = False,
    end_strategy: EndStrategy[](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.EndStrategy "EndStrategy



      module-attribute
   \(pydantic_ai._agent_graph.EndStrategy\)") = "early",
    instrument: (
        InstrumentationSettings[](https://ai.pydantic.dev/api/models/instrumented/#pydantic_ai.models.instrumented.InstrumentationSettings "InstrumentationSettings



      dataclass
   \(pydantic_ai.models.instrumented.InstrumentationSettings\)") |  | None
    ) = None,
    metadata: AgentMetadata[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")] | None = None,
    history_processors: (
        [HistoryProcessor[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]] | None
    ) = None,
    event_stream_handler: (
        EventStreamHandler[](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.EventStreamHandler "EventStreamHandler



      module-attribute
   \(pydantic_ai.agent.abstract.EventStreamHandler\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")] | None
    ) = None,
    tool_timeout:  | None = None,
    max_concurrency: AnyConcurrencyLimit[](https://ai.pydantic.dev/api/concurrency/#pydantic_ai.AnyConcurrencyLimit "pydantic_ai.concurrency.AnyConcurrencyLimit") = None
) -> None

```

```
__init__(
    model: Model[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.Model "Model \(pydantic_ai.models.Model\)") | KnownModelName[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.KnownModelName "KnownModelName



      module-attribute
   \(pydantic_ai.models.KnownModelName\)") |  | None = None,
    *,
    output_type: OutputSpec[OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")] = ,
    instructions: Instructions[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")] = None,
    system_prompt:  | [] = (),
    deps_type: [AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")] = NoneType,
    name:  | None = None,
    model_settings: ModelSettings[](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings \(pydantic_ai.settings.ModelSettings\)") | None = None,
    retries:  = 1,
    validation_context: (
         | [[RunContext[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext



      dataclass
   \(pydantic_ai.tools.RunContext\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]], ]
    ) = None,
    output_retries:  | None = None,
    tools: [
        Tool[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.Tool "Tool



      dataclass
   \(pydantic_ai.tools.Tool\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")] | ToolFuncEither[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolFuncEither "ToolFuncEither



      module-attribute
   \(pydantic_ai.tools.ToolFuncEither\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)"), ...]
    ] = (),
    builtin_tools: [
        AbstractBuiltinTool[](https://ai.pydantic.dev/api/builtin_tools/#pydantic_ai.builtin_tools.AbstractBuiltinTool "AbstractBuiltinTool



      dataclass
   \(pydantic_ai.builtin_tools.AbstractBuiltinTool\)") | BuiltinToolFunc[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.BuiltinToolFunc "BuiltinToolFunc



      module-attribute
   \(pydantic_ai.tools.BuiltinToolFunc\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]
    ] = (),
    prepare_tools: (
        ToolsPrepareFunc[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolsPrepareFunc "ToolsPrepareFunc



      module-attribute
   \(pydantic_ai.tools.ToolsPrepareFunc\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")] | None
    ) = None,
    prepare_output_tools: (
        ToolsPrepareFunc[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolsPrepareFunc "ToolsPrepareFunc



      module-attribute
   \(pydantic_ai.tools.ToolsPrepareFunc\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")] | None
    ) = None,
    toolsets: (
        [
            AbstractToolset[](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.AbstractToolset "AbstractToolset \(pydantic_ai.toolsets.AbstractToolset\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]
            | ToolsetFunc[](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.ToolsetFunc "ToolsetFunc



      module-attribute
   \(pydantic_ai.toolsets._dynamic.ToolsetFunc\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]
        ]
        | None
    ) = None,
    defer_model_check:  = False,
    end_strategy: EndStrategy[](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.EndStrategy "EndStrategy



      module-attribute
   \(pydantic_ai._agent_graph.EndStrategy\)") = "early",
    instrument: (
        InstrumentationSettings[](https://ai.pydantic.dev/api/models/instrumented/#pydantic_ai.models.instrumented.InstrumentationSettings "InstrumentationSettings



      dataclass
   \(pydantic_ai.models.instrumented.InstrumentationSettings\)") |  | None
    ) = None,
    metadata: AgentMetadata[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")] | None = None,
