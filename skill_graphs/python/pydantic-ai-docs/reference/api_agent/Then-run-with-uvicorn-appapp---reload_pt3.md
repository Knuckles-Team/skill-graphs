        instructions: Instructions[AgentDepsT] = None,
        deps: AgentDepsT = None,
        model_settings: ModelSettings | None = None,
        usage_limits: _usage.UsageLimits | None = None,
        usage: _usage.RunUsage | None = None,
        metadata: AgentMetadata[AgentDepsT] | None = None,
        infer_name: bool = True,
        toolsets: Sequence[AbstractToolset[AgentDepsT]] | None = None,
        builtin_tools: Sequence[AbstractBuiltinTool | BuiltinToolFunc[AgentDepsT]] | None = None,
    ) -> AsyncIterator[_messages.AgentStreamEvent | AgentRunResultEvent[RunOutputDataT]]: ...

    def run_stream_events(
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
    ) -> AsyncIterator[_messages.AgentStreamEvent | AgentRunResultEvent[Any]]:
        """Run the agent with a user prompt in async mode and stream events from the run.

        This is a convenience method that wraps [`self.run`][pydantic_ai.agent.AbstractAgent.run] and
        uses the `event_stream_handler` kwarg to get a stream of events from the run.

        Example:
    ```python
        from pydantic_ai import Agent, AgentRunResultEvent, AgentStreamEvent

        agent = Agent('openai:gpt-5.2')

        async def main():
            events: list[AgentStreamEvent | AgentRunResultEvent] = []
            async for event in agent.run_stream_events('What is the capital of France?'):
                events.append(event)
            print(events)
            '''
            [
                PartStartEvent(index=0, part=TextPart(content='The capital of ')),
                FinalResultEvent(tool_name=None, tool_call_id=None),
                PartDeltaEvent(index=0, delta=TextPartDelta(content_delta='France is Paris. ')),
                PartEndEvent(
                    index=0, part=TextPart(content='The capital of France is Paris. ')
                ),
                AgentRunResultEvent(
                    result=AgentRunResult(output='The capital of France is Paris. ')
                ),
            ]
            '''
    ```

        Arguments are the same as for [`self.run`][pydantic_ai.agent.AbstractAgent.run],
        except that `event_stream_handler` is now allowed.

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
            An async iterable of stream events `AgentStreamEvent` and finally a `AgentRunResultEvent` with the final
            run result.
        """
        if infer_name and self.name is None:
            self._infer_name(inspect.currentframe())

        # unfortunately this hack of returning a generator rather than defining it right here is
        # required to allow overloads of this method to work in python's typing system, or at least with pyright
        # or at least I couldn't make it work without
        return self._run_stream_events(
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
            toolsets=toolsets,
            builtin_tools=builtin_tools,
        )

    async def _run_stream_events(
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
        toolsets: Sequence[AbstractToolset[AgentDepsT]] | None = None,
        builtin_tools: Sequence[AbstractBuiltinTool | BuiltinToolFunc[AgentDepsT]] | None = None,
    ) -> AsyncIterator[_messages.AgentStreamEvent | AgentRunResultEvent[Any]]:
        send_stream, receive_stream = anyio.create_memory_object_stream[
            _messages.AgentStreamEvent | AgentRunResultEvent[Any]
        ]()

        async def event_stream_handler(
            _: RunContext[AgentDepsT], events: AsyncIterable[_messages.AgentStreamEvent]
        ) -> None:
            async for event in events:
                await send_stream.send(event)

        async def run_agent() -> AgentRunResult[Any]:
            async with send_stream:
                return await self.run(
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
                    infer_name=False,
                    toolsets=toolsets,
                    builtin_tools=builtin_tools,
                    event_stream_handler=event_stream_handler,
                )

        task = asyncio.create_task(run_agent())

        try:
            async with receive_stream:
                async for message in receive_stream:
                    yield message

            result = await task

        except asyncio.CancelledError as e:
            task.cancel(msg=e.args[0] if len(e.args) != 0 else None)
            raise

        yield AgentRunResultEvent(result)

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
    @abstractmethod
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
        raise NotImplementedError
        yield

    @contextmanager
    @abstractmethod
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
        raise NotImplementedError
        yield

    def _infer_name(self, function_frame: FrameType | None) -> None:
        """Infer the agent name from the call frame.

        RunUsage should be `self._infer_name(inspect.currentframe())`.
        """
        assert self.name is None, 'Name already set'
        if function_frame is not None:  # pragma: no branch
            if parent_frame := function_frame.f_back:  # pragma: no branch
                for name, item in parent_frame.f_locals.items():
                    if item is self:
                        self.name = name
                        return
                if parent_frame.f_locals != parent_frame.f_globals:  # pragma: no branch
                    # if we couldn't find the agent in locals and globals are a different dict, try globals
                    for name, item in parent_frame.f_globals.items():
                        if item is self:
                            self.name = name
                            return

    @staticmethod
    @contextmanager
    def parallel_tool_call_execution_mode(mode: _tool_manager.ParallelExecutionMode = 'parallel') -> Iterator[None]:
        """Set the parallel execution mode during the context.

        Args:
            mode: The execution mode for tool calls:
                - 'parallel': Run tool calls in parallel, yielding events as they complete (default).
                - 'sequential': Run tool calls one at a time in order.
                - 'parallel_ordered_events': Run tool calls in parallel, but events are emitted in order, after all calls complete.
        """
        with ToolManager.parallel_execution_mode(mode):
            yield

    @staticmethod
    @contextmanager
    @deprecated('Use `parallel_execution_mode("sequential")` instead.')
    def sequential_tool_calls() -> Iterator[None]:
        """Run tool calls sequentially during the context."""
        with ToolManager.parallel_execution_mode('sequential'):
            yield

    @staticmethod
    def is_model_request_node(
        node: _agent_graph.AgentNode[T, S] | End[result.FinalResult[S]],
    ) -> TypeIs[_agent_graph.ModelRequestNode[T, S]]:
        """Check if the node is a `ModelRequestNode`, narrowing the type if it is.

        This method preserves the generic parameters while narrowing the type, unlike a direct call to `isinstance`.
        """
        return isinstance(node, _agent_graph.ModelRequestNode)

    @staticmethod
    def is_call_tools_node(
        node: _agent_graph.AgentNode[T, S] | End[result.FinalResult[S]],
    ) -> TypeIs[_agent_graph.CallToolsNode[T, S]]:
        """Check if the node is a `CallToolsNode`, narrowing the type if it is.

        This method preserves the generic parameters while narrowing the type, unlike a direct call to `isinstance`.
        """
        return isinstance(node, _agent_graph.CallToolsNode)

    @staticmethod
    def is_user_prompt_node(
        node: _agent_graph.AgentNode[T, S] | End[result.FinalResult[S]],
    ) -> TypeIs[_agent_graph.UserPromptNode[T, S]]:
        """Check if the node is a `UserPromptNode`, narrowing the type if it is.

        This method preserves the generic parameters while narrowing the type, unlike a direct call to `isinstance`.
        """
        return isinstance(node, _agent_graph.UserPromptNode)

    @staticmethod
    def is_end_node(
        node: _agent_graph.AgentNode[T, S] | End[result.FinalResult[S]],
    ) -> TypeIs[End[result.FinalResult[S]]]:
        """Check if the node is a `End`, narrowing the type if it is.

        This method preserves the generic parameters while narrowing the type, unlike a direct call to `isinstance`.
        """
        return isinstance(node, End)

    @abstractmethod
    async def __aenter__(self) -> AbstractAgent[AgentDepsT, OutputDataT]:
        raise NotImplementedError

    @abstractmethod
    async def __aexit__(self, *args: Any) -> bool | None:
        raise NotImplementedError

    # TODO (v2): Remove in favor of using `AGUIApp` directly -- we don't have `to_temporal()` or `to_vercel_ai()` either.
    def to_ag_ui(
        self,
        *,
        # Agent.iter parameters
        output_type: OutputSpec[OutputDataT] | None = None,
        message_history: Sequence[_messages.ModelMessage] | None = None,
        deferred_tool_results: DeferredToolResults | None = None,
        model: models.Model | models.KnownModelName | str | None = None,
        deps: AgentDepsT = None,
        model_settings: ModelSettings | None = None,
        usage_limits: UsageLimits | None = None,
        usage: RunUsage | None = None,
        infer_name: bool = True,
        toolsets: Sequence[AbstractToolset[AgentDepsT]] | None = None,
        # Starlette
        debug: bool = False,
        routes: Sequence[BaseRoute] | None = None,
        middleware: Sequence[Middleware] | None = None,
        exception_handlers: Mapping[Any, ExceptionHandler] | None = None,
        on_startup: Sequence[Callable[[], Any]] | None = None,
        on_shutdown: Sequence[Callable[[], Any]] | None = None,
        lifespan: Lifespan[AGUIApp[AgentDepsT, OutputDataT]] | None = None,
    ) -> AGUIApp[AgentDepsT, OutputDataT]:
        """Returns an ASGI application that handles every AG-UI request by running the agent.

        Note that the `deps` will be the same for each request, with the exception of the AG-UI state that's
        injected into the `state` field of a `deps` object that implements the [`StateHandler`][pydantic_ai.ag_ui.StateHandler] protocol.
        To provide different `deps` for each request (e.g. based on the authenticated user),
        use [`pydantic_ai.ag_ui.run_ag_ui`][pydantic_ai.ag_ui.run_ag_ui] or
        [`pydantic_ai.ag_ui.handle_ag_ui_request`][pydantic_ai.ag_ui.handle_ag_ui_request] instead.

        Example:
    ```python
        from pydantic_ai import Agent

        agent = Agent('openai:gpt-5.2')
        app = agent.to_ag_ui()
    ```

        The `app` is an ASGI application that can be used with any ASGI server.

        To run the application, you can use the following command:

    ```bash
        uvicorn app:app --host 0.0.0.0 --port 8000
    ```

        See [AG-UI docs](../ui/ag-ui.md) for more information.

        Args:
            output_type: Custom output type to use for this run, `output_type` may only be used if the agent has
                no output validators since output validators would expect an argument that matches the agent's
                output type.
            message_history: History of the conversation so far.
            deferred_tool_results: Optional results for deferred tool calls in the message history.
            model: Optional model to use for this run, required if `model` was not set when creating the agent.
            deps: Optional dependencies to use for this run.
            model_settings: Optional settings to use for this model's request.
            usage_limits: Optional limits on model request count or token usage.
            usage: Optional usage to start with, useful for resuming a conversation or agents used in tools.
            infer_name: Whether to try to infer the agent name from the call frame if it's not set.
            toolsets: Optional additional toolsets for this run.

            debug: Boolean indicating if debug tracebacks should be returned on errors.
            routes: A list of routes to serve incoming HTTP and WebSocket requests.
            middleware: A list of middleware to run for every request. A starlette application will always
                automatically include two middleware classes. `ServerErrorMiddleware` is added as the very
                outermost middleware, to handle any uncaught errors occurring anywhere in the entire stack.
                `ExceptionMiddleware` is added as the very innermost middleware, to deal with handled
                exception cases occurring in the routing or endpoints.
            exception_handlers: A mapping of either integer status codes, or exception class types onto
                callables which handle the exceptions. Exception handler callables should be of the form
                `handler(request, exc) -> response` and may be either standard functions, or async functions.
            on_startup: A list of callables to run on application startup. Startup handler callables do not
                take any arguments, and may be either standard functions, or async functions.
            on_shutdown: A list of callables to run on application shutdown. Shutdown handler callables do
                not take any arguments, and may be either standard functions, or async functions.
            lifespan: A lifespan context function, which can be used to perform startup and shutdown tasks.
                This is a newer style that replaces the `on_startup` and `on_shutdown` handlers. Use one or
                the other, not both.

        Returns:
            An ASGI application for running Pydantic AI agents with AG-UI protocol support.
