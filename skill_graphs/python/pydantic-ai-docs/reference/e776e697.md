
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

    @overload
    def instructions(
        self, func: Callable[[RunContext[AgentDepsT]], str | None], /
    ) -> Callable[[RunContext[AgentDepsT]], str | None]: ...

    @overload
    def instructions(
        self, func: Callable[[RunContext[AgentDepsT]], Awaitable[str | None]], /
    ) -> Callable[[RunContext[AgentDepsT]], Awaitable[str | None]]: ...

    @overload
    def instructions(self, func: Callable[[], str | None], /) -> Callable[[], str | None]: ...

    @overload
    def instructions(self, func: Callable[[], Awaitable[str | None]], /) -> Callable[[], Awaitable[str | None]]: ...

    @overload
    def instructions(
        self, /
    ) -> Callable[[_system_prompt.SystemPromptFunc[AgentDepsT]], _system_prompt.SystemPromptFunc[AgentDepsT]]: ...

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

    @overload
    def system_prompt(
        self, func: Callable[[RunContext[AgentDepsT]], str | None], /
    ) -> Callable[[RunContext[AgentDepsT]], str | None]: ...

    @overload
    def system_prompt(
        self, func: Callable[[RunContext[AgentDepsT]], Awaitable[str | None]], /
    ) -> Callable[[RunContext[AgentDepsT]], Awaitable[str | None]]: ...

    @overload
    def system_prompt(self, func: Callable[[], str | None], /) -> Callable[[], str | None]: ...

    @overload
    def system_prompt(self, func: Callable[[], Awaitable[str | None]], /) -> Callable[[], Awaitable[str | None]]: ...

    @overload
    def system_prompt(
        self, /, *, dynamic: bool = False
    ) -> Callable[[_system_prompt.SystemPromptFunc[AgentDepsT]], _system_prompt.SystemPromptFunc[AgentDepsT]]: ...

    def system_prompt(
        self,
        func: _system_prompt.SystemPromptFunc[AgentDepsT] | None = None,
        /,
        *,
        dynamic: bool = False,
    ) -> (
        Callable[[_system_prompt.SystemPromptFunc[AgentDepsT]], _system_prompt.SystemPromptFunc[AgentDepsT]]
        | _system_prompt.SystemPromptFunc[AgentDepsT]
    ):
        """Decorator to register a system prompt function.

        Optionally takes [`RunContext`][pydantic_ai.tools.RunContext] as its only argument.
        Can decorate a sync or async functions.

        The decorator can be used either bare (`agent.system_prompt`) or as a function call
        (`agent.system_prompt(...)`), see the examples below.

        Overloads for every possible signature of `system_prompt` are included so the decorator doesn't obscure
        the type of the function, see `tests/typed_agent.py` for tests.

        Args:
            func: The function to decorate
            dynamic: If True, the system prompt will be reevaluated even when `messages_history` is provided,
                see [`SystemPromptPart.dynamic_ref`][pydantic_ai.messages.SystemPromptPart.dynamic_ref]

        Example:
    ```python
        from pydantic_ai import Agent, RunContext

        agent = Agent('test', deps_type=str)

        @agent.system_prompt
        def simple_system_prompt() -> str:
            return 'foobar'

        @agent.system_prompt(dynamic=True)
        async def async_system_prompt(ctx: RunContext[str]) -> str:
            return f'{ctx.deps} is the best'
    ```
        """
        if func is None:

            def decorator(
                func_: _system_prompt.SystemPromptFunc[AgentDepsT],
            ) -> _system_prompt.SystemPromptFunc[AgentDepsT]:
                runner = _system_prompt.SystemPromptRunner[AgentDepsT](func_, dynamic=dynamic)
                self._system_prompt_functions.append(runner)
                if dynamic:  # pragma: lax no cover
                    self._system_prompt_dynamic_functions[func_.__qualname__] = runner
                return func_

            return decorator
        else:
            assert not dynamic, "dynamic can't be True in this case"
            self._system_prompt_functions.append(_system_prompt.SystemPromptRunner[AgentDepsT](func, dynamic=dynamic))
            return func

    @overload
    def output_validator(
        self, func: Callable[[RunContext[AgentDepsT], OutputDataT], OutputDataT], /
    ) -> Callable[[RunContext[AgentDepsT], OutputDataT], OutputDataT]: ...

    @overload
    def output_validator(
        self, func: Callable[[RunContext[AgentDepsT], OutputDataT], Awaitable[OutputDataT]], /
    ) -> Callable[[RunContext[AgentDepsT], OutputDataT], Awaitable[OutputDataT]]: ...

    @overload
    def output_validator(
        self, func: Callable[[OutputDataT], OutputDataT], /
    ) -> Callable[[OutputDataT], OutputDataT]: ...

    @overload
    def output_validator(
        self, func: Callable[[OutputDataT], Awaitable[OutputDataT]], /
    ) -> Callable[[OutputDataT], Awaitable[OutputDataT]]: ...

    def output_validator(
        self, func: _output.OutputValidatorFunc[AgentDepsT, OutputDataT], /
    ) -> _output.OutputValidatorFunc[AgentDepsT, OutputDataT]:
        """Decorator to register an output validator function.

        Optionally takes [`RunContext`][pydantic_ai.tools.RunContext] as its first argument.
        Can decorate a sync or async functions.

        Overloads for every possible signature of `output_validator` are included so the decorator doesn't obscure
        the type of the function, see `tests/typed_agent.py` for tests.

        Example:
    ```python
        from pydantic_ai import Agent, ModelRetry, RunContext

        agent = Agent('test', deps_type=str)

        @agent.output_validator
        def output_validator_simple(data: str) -> str:
            if 'wrong' in data:
                raise ModelRetry('wrong response')
            return data

        @agent.output_validator
        async def output_validator_deps(ctx: RunContext[str], data: str) -> str:
            if ctx.deps in data:
                raise ModelRetry('wrong response')
            return data

        result = agent.run_sync('foobar', deps='spam')
        print(result.output)
        #> success (no tool calls)
    ```
        """
        self._output_validators.append(_output.OutputValidator[AgentDepsT, Any](func))
        return func

    @overload
    def tool(self, func: ToolFuncContext[AgentDepsT, ToolParams], /) -> ToolFuncContext[AgentDepsT, ToolParams]: ...

    @overload
    def tool(
        self,
        /,
        *,
        name: str | None = None,
        description: str | None = None,
        retries: int | None = None,
        prepare: ToolPrepareFunc[AgentDepsT] | None = None,
        args_validator: ArgsValidatorFunc[AgentDepsT, ToolParams] | None = None,
        docstring_format: DocstringFormat = 'auto',
        require_parameter_descriptions: bool = False,
        schema_generator: type[GenerateJsonSchema] = GenerateToolJsonSchema,
        strict: bool | None = None,
        sequential: bool = False,
        requires_approval: bool = False,
        metadata: dict[str, Any] | None = None,
        timeout: float | None = None,
    ) -> Callable[[ToolFuncContext[AgentDepsT, ToolParams]], ToolFuncContext[AgentDepsT, ToolParams]]: ...

    def tool(
        self,
        func: ToolFuncContext[AgentDepsT, ToolParams] | None = None,
        /,
        *,
        name: str | None = None,
        description: str | None = None,
        retries: int | None = None,
        prepare: ToolPrepareFunc[AgentDepsT] | None = None,
        args_validator: ArgsValidatorFunc[AgentDepsT, ToolParams] | None = None,
        docstring_format: DocstringFormat = 'auto',
        require_parameter_descriptions: bool = False,
        schema_generator: type[GenerateJsonSchema] = GenerateToolJsonSchema,
        strict: bool | None = None,
        sequential: bool = False,
        requires_approval: bool = False,
        metadata: dict[str, Any] | None = None,
        timeout: float | None = None,
    ) -> Any:
        """Decorator to register a tool function which takes [`RunContext`][pydantic_ai.tools.RunContext] as its first argument.

        Can decorate a sync or async functions.

        The docstring is inspected to extract both the tool description and description of each parameter,
        [learn more](../tools.md#function-tools-and-schema).

        We can't add overloads for every possible signature of tool, since the return type is a recursive union
        so the signature of functions decorated with `@agent.tool` is obscured.

        Example:
    ```python
        from pydantic_ai import Agent, RunContext

        agent = Agent('test', deps_type=int)

        @agent.tool
        def foobar(ctx: RunContext[int], x: int) -> int:
            return ctx.deps + x

        @agent.tool(retries=2)
        async def spam(ctx: RunContext[str], y: float) -> float:
            return ctx.deps + y

        result = agent.run_sync('foobar', deps=1)
        print(result.output)
        #> {"foobar":1,"spam":1.0}
    ```

        Args:
            func: The tool function to register.
            name: The name of the tool, defaults to the function name.
            description: The description of the tool, defaults to the function docstring.
            retries: The number of retries to allow for this tool, defaults to the agent's default retries,
                which defaults to 1.
            prepare: custom method to prepare the tool definition for each step, return `None` to omit this
                tool from a given step. This is useful if you want to customise a tool at call time,
                or omit it completely from a step. See [`ToolPrepareFunc`][pydantic_ai.tools.ToolPrepareFunc].
            args_validator: custom method to validate tool arguments after schema validation has passed,
                before execution. The validator receives the already-validated and type-converted parameters,
                with `RunContext` as the first argument.
                Should raise [`ModelRetry`][pydantic_ai.exceptions.ModelRetry] on validation failure,
                return `None` on success.
                See [`ArgsValidatorFunc`][pydantic_ai.tools.ArgsValidatorFunc].
            docstring_format: The format of the docstring, see [`DocstringFormat`][pydantic_ai.tools.DocstringFormat].
                Defaults to `'auto'`, such that the format is inferred from the structure of the docstring.
            require_parameter_descriptions: If True, raise an error if a parameter description is missing. Defaults to False.
            schema_generator: The JSON schema generator class to use for this tool. Defaults to `GenerateToolJsonSchema`.
            strict: Whether to enforce JSON schema compliance (only affects OpenAI).
                See [`ToolDefinition`][pydantic_ai.tools.ToolDefinition] for more info.
            sequential: Whether the function requires a sequential/serial execution environment. Defaults to False.
            requires_approval: Whether this tool requires human-in-the-loop approval. Defaults to False.
                See the [tools documentation](../deferred-tools.md#human-in-the-loop-tool-approval) for more info.
            metadata: Optional metadata for the tool. This is not sent to the model but can be used for filtering and tool behavior customization.
            timeout: Timeout in seconds for tool execution. If the tool takes longer, a retry prompt is returned to the model.
                Overrides the agent-level `tool_timeout` if set. Defaults to None (no timeout).
        """

        def tool_decorator(
            func_: ToolFuncContext[AgentDepsT, ToolParams],
        ) -> ToolFuncContext[AgentDepsT, ToolParams]:
            # noinspection PyTypeChecker
            self._function_toolset.add_function(
                func_,
                takes_ctx=True,
                name=name,
                description=description,
                retries=retries,
                prepare=prepare,
                args_validator=args_validator,
                docstring_format=docstring_format,
                require_parameter_descriptions=require_parameter_descriptions,
                schema_generator=schema_generator,
                strict=strict,
                sequential=sequential,
                requires_approval=requires_approval,
                metadata=metadata,
                timeout=timeout,
            )
            return func_

        return tool_decorator if func is None else tool_decorator(func)

    @overload
    def tool_plain(self, func: ToolFuncPlain[ToolParams], /) -> ToolFuncPlain[ToolParams]: ...

    @overload
    def tool_plain(
        self,
        /,
        *,
        name: str | None = None,
        description: str | None = None,
        retries: int | None = None,
        prepare: ToolPrepareFunc[AgentDepsT] | None = None,
        args_validator: ArgsValidatorFunc[AgentDepsT, ToolParams] | None = None,
        docstring_format: DocstringFormat = 'auto',
        require_parameter_descriptions: bool = False,
        schema_generator: type[GenerateJsonSchema] = GenerateToolJsonSchema,
        strict: bool | None = None,
        sequential: bool = False,
        requires_approval: bool = False,
        metadata: dict[str, Any] | None = None,
        timeout: float | None = None,
    ) -> Callable[[ToolFuncPlain[ToolParams]], ToolFuncPlain[ToolParams]]: ...

    def tool_plain(
        self,
        func: ToolFuncPlain[ToolParams] | None = None,
        /,
        *,
        name: str | None = None,
        description: str | None = None,
        retries: int | None = None,
        prepare: ToolPrepareFunc[AgentDepsT] | None = None,
        args_validator: ArgsValidatorFunc[AgentDepsT, ToolParams] | None = None,
        docstring_format: DocstringFormat = 'auto',
        require_parameter_descriptions: bool = False,
        schema_generator: type[GenerateJsonSchema] = GenerateToolJsonSchema,
        strict: bool | None = None,
        sequential: bool = False,
        requires_approval: bool = False,
        metadata: dict[str, Any] | None = None,
        timeout: float | None = None,
    ) -> Any:
        """Decorator to register a tool function which DOES NOT take `RunContext` as an argument.

        Can decorate a sync or async functions.

        The docstring is inspected to extract both the tool description and description of each parameter,
        [learn more](../tools.md#function-tools-and-schema).

        We can't add overloads for every possible signature of tool, since the return type is a recursive union
        so the signature of functions decorated with `@agent.tool` is obscured.

        Example:
    ```python
        from pydantic_ai import Agent, RunContext

        agent = Agent('test')

        @agent.tool
        def foobar(ctx: RunContext[int]) -> int:
            return 123

        @agent.tool(retries=2)
        async def spam(ctx: RunContext[str]) -> float:
            return 3.14

        result = agent.run_sync('foobar', deps=1)
        print(result.output)
        #> {"foobar":123,"spam":3.14}
    ```

        Args:
            func: The tool function to register.
            name: The name of the tool, defaults to the function name.
            description: The description of the tool, defaults to the function docstring.
            retries: The number of retries to allow for this tool, defaults to the agent's default retries,
                which defaults to 1.
            prepare: custom method to prepare the tool definition for each step, return `None` to omit this
                tool from a given step. This is useful if you want to customise a tool at call time,
                or omit it completely from a step. See [`ToolPrepareFunc`][pydantic_ai.tools.ToolPrepareFunc].
            args_validator: custom method to validate tool arguments after schema validation has passed,
                before execution. The validator receives the already-validated and type-converted parameters,
                with [`RunContext`][pydantic_ai.tools.RunContext] as the first argument — even though the
                tool function itself does not take `RunContext` when using `tool_plain`.
                Should raise [`ModelRetry`][pydantic_ai.exceptions.ModelRetry] on validation failure,
                return `None` on success.
                See [`ArgsValidatorFunc`][pydantic_ai.tools.ArgsValidatorFunc].
            docstring_format: The format of the docstring, see [`DocstringFormat`][pydantic_ai.tools.DocstringFormat].
                Defaults to `'auto'`, such that the format is inferred from the structure of the docstring.
            require_parameter_descriptions: If True, raise an error if a parameter description is missing. Defaults to False.
            schema_generator: The JSON schema generator class to use for this tool. Defaults to `GenerateToolJsonSchema`.
            strict: Whether to enforce JSON schema compliance (only affects OpenAI).
                See [`ToolDefinition`][pydantic_ai.tools.ToolDefinition] for more info.
            sequential: Whether the function requires a sequential/serial execution environment. Defaults to False.
            requires_approval: Whether this tool requires human-in-the-loop approval. Defaults to False.
                See the [tools documentation](../deferred-tools.md#human-in-the-loop-tool-approval) for more info.
            metadata: Optional metadata for the tool. This is not sent to the model but can be used for filtering and tool behavior customization.
            timeout: Timeout in seconds for tool execution. If the tool takes longer, a retry prompt is returned to the model.
                Overrides the agent-level `tool_timeout` if set. Defaults to None (no timeout).
        """

        def tool_decorator(func_: ToolFuncPlain[ToolParams]) -> ToolFuncPlain[ToolParams]:
            # noinspection PyTypeChecker
            self._function_toolset.add_function(
                func_,
                takes_ctx=False,
                name=name,
                description=description,
                retries=retries,
                prepare=prepare,
                args_validator=args_validator,
                docstring_format=docstring_format,
                require_parameter_descriptions=require_parameter_descriptions,
                schema_generator=schema_generator,
                strict=strict,
                sequential=sequential,
                requires_approval=requires_approval,
                metadata=metadata,
                timeout=timeout,
            )
            return func_

        return tool_decorator if func is None else tool_decorator(func)

    @overload
    def toolset(self, func: ToolsetFunc[AgentDepsT], /) -> ToolsetFunc[AgentDepsT]: ...

    @overload
    def toolset(
        self,
        /,
        *,
        per_run_step: bool = True,
        id: str | None = None,
    ) -> Callable[[ToolsetFunc[AgentDepsT]], ToolsetFunc[AgentDepsT]]: ...

    def toolset(
        self,
        func: ToolsetFunc[AgentDepsT] | None = None,
        /,
        *,
        per_run_step: bool = True,
        id: str | None = None,
    ) -> Any:
        """Decorator to register a toolset function which takes [`RunContext`][pydantic_ai.tools.RunContext] as its only argument.

        Can decorate a sync or async functions.

        The decorator can be used bare (`agent.toolset`).

        Example:
    ```python
        from pydantic_ai import AbstractToolset, Agent, FunctionToolset, RunContext

        agent = Agent('test', deps_type=str)

        @agent.toolset
        async def simple_toolset(ctx: RunContext[str]) -> AbstractToolset[str]:
            return FunctionToolset()
    ```

        Args:
            func: The toolset function to register.
            per_run_step: Whether to re-evaluate the toolset for each run step. Defaults to True.
            id: An optional unique ID for the dynamic toolset. Required for use with durable execution
                environments like Temporal, where the ID identifies the toolset's activities within the workflow.
        """

        def toolset_decorator(func_: ToolsetFunc[AgentDepsT]) -> ToolsetFunc[AgentDepsT]:
            self._dynamic_toolsets.append(DynamicToolset(func_, per_run_step=per_run_step, id=id))
            return func_

        return toolset_decorator if func is None else toolset_decorator(func)

    def _get_model(self, model: models.Model | models.KnownModelName | str | None) -> models.Model:
        """Create a model configured for this agent.

        Args:
            model: model to use for this run, required if `model` was not set when creating the agent.

        Returns:
            The model used
        """
        model_: models.Model
        if some_model := self._override_model.get():
            # we don't want `override()` to cover up errors from the model not being defined, hence this check
            if model is None and self.model is None:
                raise exceptions.UserError(
                    '`model` must either be set on the agent or included when calling it. '
                    '(Even when `override(model=...)` is customizing the model that will actually be called)'
                )
            model_ = some_model.value
        elif model is not None:
            model_ = models.infer_model(model)
        elif self.model is not None:
            # noinspection PyTypeChecker
            model_ = self.model = models.infer_model(self.model)
        else:
            raise exceptions.UserError('`model` must either be set on the agent or included when calling it.')

        instrument = self.instrument
        if instrument is None:
            instrument = self._instrument_default

        return instrument_model(model_, instrument)

    def _get_deps(self: Agent[T, OutputDataT], deps: T) -> T:
        """Get deps for a run.

        If we've overridden deps via `_override_deps`, use that, otherwise use the deps passed to the call.

        We could do runtime type checking of deps against `self._deps_type`, but that's a slippery slope.
        """
        if some_deps := self._override_deps.get():
            return some_deps.value
        else:
            return deps

    def _normalize_instructions(
        self,
        instructions: Instructions[AgentDepsT],
    ) -> list[str | _system_prompt.SystemPromptFunc[AgentDepsT]]:
        if instructions is None:
            return []
        if isinstance(instructions, str) or callable(instructions):
            return [instructions]
        return list(instructions)

    def _get_instructions(
        self,
        additional_instructions: Instructions[AgentDepsT] = None,
    ) -> tuple[str | None, list[_system_prompt.SystemPromptRunner[AgentDepsT]]]:
        override_instructions = self._override_instructions.get()
        if override_instructions:
            instructions = override_instructions.value
        else:
            instructions = self._instructions.copy()
            if additional_instructions is not None:
                instructions.extend(self._normalize_instructions(additional_instructions))

        literal_parts: list[str] = []
        functions: list[_system_prompt.SystemPromptRunner[AgentDepsT]] = []

        for instruction in instructions:
            if isinstance(instruction, str):
                literal_parts.append(instruction)
            else:
                functions.append(_system_prompt.SystemPromptRunner[AgentDepsT](instruction))
