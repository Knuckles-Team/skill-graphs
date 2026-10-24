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

Context manager to temporarily override agent dependencies, model, toolsets, tools, or instructions.
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
Source code in `pydantic_ai_slim/pydantic_ai/durable_exec/prefect/_agent.py`
```
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
###  PrefectFunctionToolset
Bases: `PrefectWrapperToolset[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]`
A wrapper for FunctionToolset that integrates with Prefect, turning tool calls into Prefect tasks.
Source code in `pydantic_ai_slim/pydantic_ai/durable_exec/prefect/_function_toolset.py`
```
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
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
```
| ```
class PrefectFunctionToolset(PrefectWrapperToolset[AgentDepsT]):
    """A wrapper for FunctionToolset that integrates with Prefect, turning tool calls into Prefect tasks."""

    def __init__(
        self,
        wrapped: FunctionToolset[AgentDepsT],
        *,
        task_config: TaskConfig,
        tool_task_config: dict[str, TaskConfig | None],
    ):
        super().__init__(wrapped)
        self._task_config = default_task_config | (task_config or {})
        self._tool_task_config = tool_task_config or {}

        @task
        async def _call_tool_task(
            tool_name: str,
            tool_args: dict[str, Any],
            ctx: RunContext[AgentDepsT],
            tool: ToolsetTool[AgentDepsT],
        ) -> Any:
            return await super(PrefectFunctionToolset, self).call_tool(tool_name, tool_args, ctx, tool)

        self._call_tool_task = _call_tool_task

    async def call_tool(
        self,
        name: str,
        tool_args: dict[str, Any],
        ctx: RunContext[AgentDepsT],
        tool: ToolsetTool[AgentDepsT],
    ) -> Any:
        """Call a tool, wrapped as a Prefect task with a descriptive name."""
        # Check if this specific tool has custom config or is disabled
        tool_specific_config = self._tool_task_config.get(name, default_task_config)
        if tool_specific_config is None:
            # None means this tool should not be wrapped as a task
            return await super().call_tool(name, tool_args, ctx, tool)

        # Merge tool-specific config with default config
        merged_config = self._task_config | tool_specific_config

        return await self._call_tool_task.with_options(name=f'Call Tool: {name}', **merged_config)(
            name, tool_args, ctx, tool
        )

```

---|---
####  call_tool `async`
```
call_tool(
    name: ,
    tool_args: [, ],
    ctx: RunContext[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext



      dataclass
   \(pydantic_ai.tools.RunContext\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")],
    tool: ToolsetTool[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")],
) ->

```

Call a tool, wrapped as a Prefect task with a descriptive name.
Source code in `pydantic_ai_slim/pydantic_ai/durable_exec/prefect/_function_toolset.py`
```
39
40
41
42
43
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
```
| ```
async def call_tool(
    self,
    name: str,
    tool_args: dict[str, Any],
    ctx: RunContext[AgentDepsT],
    tool: ToolsetTool[AgentDepsT],
) -> Any:
    """Call a tool, wrapped as a Prefect task with a descriptive name."""
    # Check if this specific tool has custom config or is disabled
    tool_specific_config = self._tool_task_config.get(name, default_task_config)
    if tool_specific_config is None:
        # None means this tool should not be wrapped as a task
        return await super().call_tool(name, tool_args, ctx, tool)

    # Merge tool-specific config with default config
    merged_config = self._task_config | tool_specific_config

    return await self._call_tool_task.with_options(name=f'Call Tool: {name}', **merged_config)(
        name, tool_args, ctx, tool
    )

```

---|---
###  PrefectMCPServer
Bases: `PrefectWrapperToolset[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]`,
A wrapper for MCPServer that integrates with Prefect, turning call_tool and get_tools into Prefect tasks.
Source code in `pydantic_ai_slim/pydantic_ai/durable_exec/prefect/_mcp_server.py`
```
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
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
```
| ```
class PrefectMCPServer(PrefectWrapperToolset[AgentDepsT], ABC):
    """A wrapper for MCPServer that integrates with Prefect, turning call_tool and get_tools into Prefect tasks."""

    def __init__(
        self,
        wrapped: MCPServer,
        *,
        task_config: TaskConfig,
    ):
        super().__init__(wrapped)
        self._task_config = default_task_config | (task_config or {})
        self._mcp_id = wrapped.id

        @task
        async def _call_tool_task(
            tool_name: str,
            tool_args: dict[str, Any],
            ctx: RunContext[AgentDepsT],
            tool: ToolsetTool[AgentDepsT],
        ) -> ToolResult:
            return await super(PrefectMCPServer, self).call_tool(tool_name, tool_args, ctx, tool)

        self._call_tool_task = _call_tool_task

    async def __aenter__(self) -> Self:
        await self.wrapped.__aenter__()
        return self

    async def __aexit__(self, *args: Any) -> bool | None:
        return await self.wrapped.__aexit__(*args)

    async def call_tool(
        self,
        name: str,
        tool_args: dict[str, Any],
        ctx: RunContext[AgentDepsT],
        tool: ToolsetTool[AgentDepsT],
    ) -> ToolResult:
        """Call an MCP tool, wrapped as a Prefect task with a descriptive name."""
        return await self._call_tool_task.with_options(name=f'Call MCP Tool: {name}', **self._task_config)(
            name, tool_args, ctx, tool
        )

```

---|---
####  call_tool `async`
```
call_tool(
    name: ,
    tool_args: [, ],
    ctx: RunContext[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext



      dataclass
   \(pydantic_ai.tools.RunContext\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")],
    tool: ToolsetTool[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")],
) -> ToolResult[](https://ai.pydantic.dev/api/mcp/#pydantic_ai.mcp.ToolResult "ToolResult



      module-attribute
   \(pydantic_ai.mcp.ToolResult\)")

```

Call an MCP tool, wrapped as a Prefect task with a descriptive name.
Source code in `pydantic_ai_slim/pydantic_ai/durable_exec/prefect/_mcp_server.py`
```
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
```
| ```
async def call_tool(
    self,
    name: str,
    tool_args: dict[str, Any],
    ctx: RunContext[AgentDepsT],
    tool: ToolsetTool[AgentDepsT],
) -> ToolResult:
    """Call an MCP tool, wrapped as a Prefect task with a descriptive name."""
    return await self._call_tool_task.with_options(name=f'Call MCP Tool: {name}', **self._task_config)(
        name, tool_args, ctx, tool
    )

```

---|---
###  PrefectModel
Bases: `WrapperModel[](https://ai.pydantic.dev/api/models/wrapper/#pydantic_ai.models.wrapper.WrapperModel "WrapperModel



      dataclass
   \(pydantic_ai.models.wrapper.WrapperModel\)")`
A wrapper for Model that integrates with Prefect, turning request and request_stream into Prefect tasks.
Source code in `pydantic_ai_slim/pydantic_ai/durable_exec/prefect/_model.py`
```
 23
 24
 25
 26
 27
 28
 29
 30
 31
 32
 33
 34
 35
 36
 37
 38
 39
 40
 41
 42
 43
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
```
| ```
class PrefectModel(WrapperModel):
    """A wrapper for Model that integrates with Prefect, turning request and request_stream into Prefect tasks."""

    def __init__(
        self,
        model: Any,
        *,
        task_config: TaskConfig,
        event_stream_handler: EventStreamHandler[Any] | None = None,
    ):
        super().__init__(model)
        self.task_config = default_task_config | (task_config or {})
        self.event_stream_handler = event_stream_handler

        @task
        async def wrapped_request(
            messages: list[ModelMessage],
            model_settings: ModelSettings | None,
            model_request_parameters: ModelRequestParameters,
        ) -> ModelResponse:
            response = await super(PrefectModel, self).request(messages, model_settings, model_request_parameters)
            return response

        self._wrapped_request = wrapped_request

        @task
        async def request_stream_task(
            messages: list[ModelMessage],
            model_settings: ModelSettings | None,
            model_request_parameters: ModelRequestParameters,
            ctx: RunContext[Any] | None,
        ) -> ModelResponse:
            async with super(PrefectModel, self).request_stream(
                messages, model_settings, model_request_parameters, ctx
            ) as streamed_response:
                if self.event_stream_handler is not None:
                    assert ctx is not None, (
                        'A Prefect model cannot be used with `pydantic_ai.direct.model_request_stream()` as it requires a `run_context`. '
                        'Set an `event_stream_handler` on the agent and use `agent.run()` instead.'
                    )
                    await self.event_stream_handler(ctx, streamed_response)

                # Consume the entire stream
                async for _ in streamed_response:
                    pass
            response = streamed_response.get()
            return response

        self._wrapped_request_stream = request_stream_task

    async def request(
        self,
        messages: list[ModelMessage],
        model_settings: ModelSettings | None,
        model_request_parameters: ModelRequestParameters,
    ) -> ModelResponse:
        """Make a model request, wrapped as a Prefect task when in a flow."""
        return await self._wrapped_request.with_options(
            name=f'Model Request: {self.wrapped.model_name}', **self.task_config
        )(messages, model_settings, model_request_parameters)

    @asynccontextmanager
    async def request_stream(
        self,
        messages: list[ModelMessage],
        model_settings: ModelSettings | None,
        model_request_parameters: ModelRequestParameters,
        run_context: RunContext[Any] | None = None,
    ) -> AsyncIterator[StreamedResponse]:
        """Make a streaming model request.

        When inside a Prefect flow, the stream is consumed within a task and
        a non-streaming response is returned. When not in a flow, behaves normally.
        """
        # Check if we're in a flow context
        flow_run_context = FlowRunContext.get()

        # If not in a flow, just call the wrapped request_stream method
        if flow_run_context is None:
            async with super().request_stream(
                messages, model_settings, model_request_parameters, run_context
            ) as streamed_response:
                yield streamed_response
                return

        # If in a flow, consume the stream in a task and return the final response
        response = await self._wrapped_request_stream.with_options(
            name=f'Model Request (Streaming): {self.wrapped.model_name}', **self.task_config
        )(messages, model_settings, model_request_parameters, run_context)
        yield CompletedStreamedResponse(model_request_parameters, response)

```

---|---
####  request `async`
```
request(
    messages: [ModelMessage[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelMessage "ModelMessage



      module-attribute
   \(pydantic_ai.ModelMessage\)")],
    model_settings: ModelSettings[](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings \(pydantic_ai.settings.ModelSettings\)") | None,
    model_request_parameters: ModelRequestParameters[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.ModelRequestParameters "ModelRequestParameters



      dataclass
   \(pydantic_ai.models.ModelRequestParameters\)"),
) -> ModelResponse[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse "ModelResponse



      dataclass
   \(pydantic_ai.ModelResponse\)")

```

Make a model request, wrapped as a Prefect task when in a flow.
Source code in `pydantic_ai_slim/pydantic_ai/durable_exec/prefect/_model.py`
```
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
```
| ```
async def request(
    self,
    messages: list[ModelMessage],
    model_settings: ModelSettings | None,
    model_request_parameters: ModelRequestParameters,
) -> ModelResponse:
    """Make a model request, wrapped as a Prefect task when in a flow."""
    return await self._wrapped_request.with_options(
        name=f'Model Request: {self.wrapped.model_name}', **self.task_config
    )(messages, model_settings, model_request_parameters)

```

---|---
####  request_stream `async`
```
request_stream(
    messages: [ModelMessage[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelMessage "ModelMessage



      module-attribute
   \(pydantic_ai.ModelMessage\)")],
    model_settings: ModelSettings[](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings \(pydantic_ai.settings.ModelSettings\)") | None,
    model_request_parameters: ModelRequestParameters[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.ModelRequestParameters "ModelRequestParameters



      dataclass
   \(pydantic_ai.models.ModelRequestParameters\)"),
    run_context: RunContext[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext



      dataclass
   \(pydantic_ai.tools.RunContext\)")[] | None = None,
) -> [StreamedResponse[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.StreamedResponse "StreamedResponse



      dataclass
   \(pydantic_ai.models.StreamedResponse\)")]

```

Make a streaming model request.
When inside a Prefect flow, the stream is consumed within a task and a non-streaming response is returned. When not in a flow, behaves normally.
Source code in `pydantic_ai_slim/pydantic_ai/durable_exec/prefect/_model.py`
```
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
```
| ```
@asynccontextmanager
async def request_stream(
    self,
    messages: list[ModelMessage],
    model_settings: ModelSettings | None,
    model_request_parameters: ModelRequestParameters,
    run_context: RunContext[Any] | None = None,
) -> AsyncIterator[StreamedResponse]:
    """Make a streaming model request.

    When inside a Prefect flow, the stream is consumed within a task and
    a non-streaming response is returned. When not in a flow, behaves normally.
    """
    # Check if we're in a flow context
    flow_run_context = FlowRunContext.get()

    # If not in a flow, just call the wrapped request_stream method
    if flow_run_context is None:
        async with super().request_stream(
            messages, model_settings, model_request_parameters, run_context
        ) as streamed_response:
            yield streamed_response
            return

    # If in a flow, consume the stream in a task and return the final response
    response = await self._wrapped_request_stream.with_options(
        name=f'Model Request (Streaming): {self.wrapped.model_name}', **self.task_config
    )(messages, model_settings, model_request_parameters, run_context)
    yield CompletedStreamedResponse(model_request_parameters, response)

```

---|---
###  TaskConfig
Bases:
Configuration for a task in Prefect.
These options are passed to the `@task` decorator.
Source code in `pydantic_ai_slim/pydantic_ai/durable_exec/prefect/_types.py`
```
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
```
| ```
class TaskConfig(TypedDict, total=False):
    """Configuration for a task in Prefect.

    These options are passed to the `@task` decorator.
    """

    retries: int
    """Maximum number of retries for the task."""

    retry_delay_seconds: float | list[float]
    """Delay between retries in seconds. Can be a single value or a list for custom backoff."""

    timeout_seconds: float
    """Maximum time in seconds for the task to complete."""

    cache_policy: CachePolicy
    """Prefect cache policy for the task."""

    persist_result: bool
    """Whether to persist the task result."""

    result_storage: ResultStorage
    """Prefect result storage for the task. Should be a storage block or a block slug like `s3-bucket/my-storage`."""

    log_prints: bool
    """Whether to log print statements from the task."""

```

---|---
####  retries `instance-attribute`
```
retries:

```

Maximum number of retries for the task.
####  retry_delay_seconds `instance-attribute`
```
retry_delay_seconds:  | []

```

Delay between retries in seconds. Can be a single value or a list for custom backoff.
####  timeout_seconds `instance-attribute`
```
timeout_seconds:

```

Maximum time in seconds for the task to complete.
####  cache_policy `instance-attribute`
```
cache_policy: CachePolicy

```

Prefect cache policy for the task.
####  persist_result `instance-attribute`
```
persist_result:

```

Whether to persist the task result.
####  result_storage `instance-attribute`
```
result_storage: ResultStorage

```

Prefect result storage for the task. Should be a storage block or a block slug like `s3-bucket/my-storage`.
####  log_prints `instance-attribute`
```
log_prints:

```

Whether to log print statements from the task.
© Pydantic Services Inc. 2024 to present
