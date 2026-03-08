


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
Source code in `pydantic_ai_slim/pydantic_ai/agent/abstract.py`
```
1127
1128
1129
1130
1131
1132
1133
1134
1135
1136
1137
1138
1139
1140
1141
1142
1143
1144
1145
1146
1147
1148
1149
1150
1151
1152
1153
```
| ```
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

```

---|---
####  parallel_tool_call_execution_mode `staticmethod`
```
parallel_tool_call_execution_mode(
    mode: ParallelExecutionMode = "parallel",
) -> [None]

```

Set the parallel execution mode during the context.
Parameters:
Name | Type | Description | Default
---|---|---|---
`mode` |  `ParallelExecutionMode` |  The execution mode for tool calls: - 'parallel': Run tool calls in parallel, yielding events as they complete (default). - 'sequential': Run tool calls one at a time in order. - 'parallel_ordered_events': Run tool calls in parallel, but events are emitted in order, after all calls complete. |  `'parallel'`
Source code in `pydantic_ai_slim/pydantic_ai/agent/abstract.py`
```
1174
1175
1176
1177
1178
1179
1180
1181
1182
1183
1184
1185
1186
```
| ```
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

```

---|---
####  sequential_tool_calls `deprecated` `staticmethod`
```
sequential_tool_calls() -> [None]

```

Deprecated
Use `parallel_execution_mode("sequential")` instead.
Run tool calls sequentially during the context.
Source code in `pydantic_ai_slim/pydantic_ai/agent/abstract.py`
```
1188
1189
1190
1191
1192
1193
1194
```
| ```
@staticmethod
@contextmanager
@deprecated('Use `parallel_execution_mode("sequential")` instead.')
def sequential_tool_calls() -> Iterator[None]:
    """Run tool calls sequentially during the context."""
    with ToolManager.parallel_execution_mode('sequential'):
        yield

```

---|---
####  is_model_request_node `staticmethod`
```
is_model_request_node(
    node: AgentNode[T, S] | End[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.End "End



      dataclass
   \(pydantic_graph.End\)")[FinalResult[S]],
) -> [ModelRequestNode[T, S]]

```

Check if the node is a `ModelRequestNode`, narrowing the type if it is.
This method preserves the generic parameters while narrowing the type, unlike a direct call to `isinstance`.
Source code in `pydantic_ai_slim/pydantic_ai/agent/abstract.py`
```
1196
1197
1198
1199
1200
1201
1202
1203
1204
```
| ```
@staticmethod
def is_model_request_node(
    node: _agent_graph.AgentNode[T, S] | End[result.FinalResult[S]],
) -> TypeIs[_agent_graph.ModelRequestNode[T, S]]:
    """Check if the node is a `ModelRequestNode`, narrowing the type if it is.

    This method preserves the generic parameters while narrowing the type, unlike a direct call to `isinstance`.
    """
    return isinstance(node, _agent_graph.ModelRequestNode)

```

---|---
####  is_call_tools_node `staticmethod`
```
is_call_tools_node(
    node: AgentNode[T, S] | End[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.End "End



      dataclass
   \(pydantic_graph.End\)")[FinalResult[S]],
) -> [CallToolsNode[T, S]]

```

Check if the node is a `CallToolsNode`, narrowing the type if it is.
This method preserves the generic parameters while narrowing the type, unlike a direct call to `isinstance`.
Source code in `pydantic_ai_slim/pydantic_ai/agent/abstract.py`
```
1206
1207
1208
1209
1210
1211
1212
1213
1214
```
| ```
@staticmethod
def is_call_tools_node(
    node: _agent_graph.AgentNode[T, S] | End[result.FinalResult[S]],
) -> TypeIs[_agent_graph.CallToolsNode[T, S]]:
    """Check if the node is a `CallToolsNode`, narrowing the type if it is.

    This method preserves the generic parameters while narrowing the type, unlike a direct call to `isinstance`.
    """
    return isinstance(node, _agent_graph.CallToolsNode)

```

---|---
####  is_user_prompt_node `staticmethod`
```
is_user_prompt_node(
    node: AgentNode[T, S] | End[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.End "End



      dataclass
   \(pydantic_graph.End\)")[FinalResult[S]],
) -> [UserPromptNode[T, S]]

```

Check if the node is a `UserPromptNode`, narrowing the type if it is.
This method preserves the generic parameters while narrowing the type, unlike a direct call to `isinstance`.
Source code in `pydantic_ai_slim/pydantic_ai/agent/abstract.py`
```
1216
1217
1218
1219
1220
1221
1222
1223
1224
```
| ```
@staticmethod
def is_user_prompt_node(
    node: _agent_graph.AgentNode[T, S] | End[result.FinalResult[S]],
) -> TypeIs[_agent_graph.UserPromptNode[T, S]]:
    """Check if the node is a `UserPromptNode`, narrowing the type if it is.

    This method preserves the generic parameters while narrowing the type, unlike a direct call to `isinstance`.
    """
    return isinstance(node, _agent_graph.UserPromptNode)

```

---|---
####  is_end_node `staticmethod`
```
is_end_node(
    node: AgentNode[T, S] | End[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.End "End



      dataclass
   \(pydantic_graph.End\)")[FinalResult[S]],
) -> [End[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.End "End



      dataclass
   \(pydantic_graph.End\)")[FinalResult[S]]]

```

Check if the node is a `End`, narrowing the type if it is.
This method preserves the generic parameters while narrowing the type, unlike a direct call to `isinstance`.
Source code in `pydantic_ai_slim/pydantic_ai/agent/abstract.py`
```
1226
1227
1228
1229
1230
1231
1232
1233
1234
```
| ```
@staticmethod
def is_end_node(
    node: _agent_graph.AgentNode[T, S] | End[result.FinalResult[S]],
) -> TypeIs[End[result.FinalResult[S]]]:
    """Check if the node is a `End`, narrowing the type if it is.

    This method preserves the generic parameters while narrowing the type, unlike a direct call to `isinstance`.
    """
    return isinstance(node, End)

```

---|---
####  to_ag_ui
```
to_ag_ui(
    *,
    output_type: OutputSpec[OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")] | None = None,
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
    infer_name:  = True,
    toolsets: (
        [AbstractToolset[](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.AbstractToolset "AbstractToolset \(pydantic_ai.toolsets.AbstractToolset\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]] | None
    ) = None,
    debug:  = False,
    routes: [BaseRoute] | None = None,
    middleware: [Middleware] | None = None,
    exception_handlers: (
        [, ExceptionHandler] | None
    ) = None,
    on_startup: [[[], ]] | None = None,
    on_shutdown: [[[], ]] | None = None,
    lifespan: (
        Lifespan[AGUIApp[](https://ai.pydantic.dev/api/ui/ag_ui/#pydantic_ai.ui.ag_ui.app.AGUIApp "AGUIApp \(pydantic_ai.ui.ag_ui.app.AGUIApp\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)"), OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")]] | None
    ) = None
) -> AGUIApp[](https://ai.pydantic.dev/api/ui/ag_ui/#pydantic_ai.ui.ag_ui.app.AGUIApp "AGUIApp \(pydantic_ai.ui.ag_ui.app.AGUIApp\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)"), OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")]

```

Returns an ASGI application that handles every AG-UI request by running the agent.
Note that the `deps` will be the same for each request, with the exception of the AG-UI state that's injected into the `state` field of a `deps` object that implements the [`StateHandler`](https://ai.pydantic.dev/api/ag_ui/#pydantic_ai.ag_ui.StateHandler "StateHandler") protocol. To provide different `deps` for each request (e.g. based on the authenticated user), use [`pydantic_ai.ag_ui.run_ag_ui`](https://ai.pydantic.dev/api/ag_ui/#pydantic_ai.ag_ui.run_ag_ui "run_ag_ui") or [`pydantic_ai.ag_ui.handle_ag_ui_request`](https://ai.pydantic.dev/api/ag_ui/#pydantic_ai.ag_ui.handle_ag_ui_request "handle_ag_ui_request



      async
  ") instead.
Example:
```
from pydantic_ai import Agent

agent = Agent('openai:gpt-5.2')
app = agent.to_ag_ui()

```

The `app` is an ASGI application that can be used with any ASGI server.
To run the application, you can use the following command:
```
uvicorn app:app --host 0.0.0.0 --port 8000

```

See [AG-UI docs](https://ai.pydantic.dev/ui/ag-ui/) for more information.
Parameters:
Name | Type | Description | Default
---|---|---|---
`output_type` |  `OutputSpec[OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")] | None` |  Custom output type to use for this run, `output_type` may only be used if the agent has no output validators since output validators would expect an argument that matches the agent's output type. |  `None`
`message_history` |  `ModelMessage[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelMessage "ModelMessage



      module-attribute
   \(pydantic_ai.messages.ModelMessage\)")] | None` |  History of the conversation so far. |  `None`
`deferred_tool_results` |  `DeferredToolResults[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.DeferredToolResults "DeferredToolResults



      dataclass
   \(pydantic_ai.tools.DeferredToolResults\)") | None` |  Optional results for deferred tool calls in the message history. |  `None`
`model` |  `Model[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.Model "Model \(pydantic_ai.models.Model\)") | KnownModelName[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.KnownModelName "KnownModelName



      module-attribute
   \(pydantic_ai.models.KnownModelName\)") | ` |  Optional model to use for this run, required if `model` was not set when creating the agent. |  `None`
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
`infer_name` |  |  Whether to try to infer the agent name from the call frame if it's not set. |  `True`
`toolsets` |  `AbstractToolset[](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.AbstractToolset "AbstractToolset \(pydantic_ai.toolsets.AbstractToolset\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]] | None` |  Optional additional toolsets for this run. |  `None`
`debug` |  |  Boolean indicating if debug tracebacks should be returned on errors. |  `False`
`routes` |  `BaseRoute] | None` |  A list of routes to serve incoming HTTP and WebSocket requests. |  `None`
`middleware` |  `Middleware] | None` |  A list of middleware to run for every request. A starlette application will always automatically include two middleware classes. `ServerErrorMiddleware` is added as the very outermost middleware, to handle any uncaught errors occurring anywhere in the entire stack. `ExceptionMiddleware` is added as the very innermost middleware, to deal with handled exception cases occurring in the routing or endpoints. |  `None`
`exception_handlers` |  `ExceptionHandler] | None` |  A mapping of either integer status codes, or exception class types onto callables which handle the exceptions. Exception handler callables should be of the form `handler(request, exc) -> response` and may be either standard functions, or async functions. |  `None`
`on_startup` |  |  A list of callables to run on application startup. Startup handler callables do not take any arguments, and may be either standard functions, or async functions. |  `None`
`on_shutdown` |  |  A list of callables to run on application shutdown. Shutdown handler callables do not take any arguments, and may be either standard functions, or async functions. |  `None`
`lifespan` |  `Lifespan[AGUIApp[](https://ai.pydantic.dev/api/ui/ag_ui/#pydantic_ai.ui.ag_ui.app.AGUIApp "AGUIApp \(pydantic_ai.ui.ag_ui.app.AGUIApp\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)"), OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")]] | None` |  A lifespan context function, which can be used to perform startup and shutdown tasks. This is a newer style that replaces the `on_startup` and `on_shutdown` handlers. Use one or the other, not both. |  `None`
Returns:
Type | Description
---|---
`AGUIApp[](https://ai.pydantic.dev/api/ui/ag_ui/#pydantic_ai.ui.ag_ui.app.AGUIApp "AGUIApp \(pydantic_ai.ui.ag_ui.app.AGUIApp\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)"), OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")]` |  An ASGI application for running Pydantic AI agents with AG-UI protocol support.
Source code in `pydantic_ai_slim/pydantic_ai/agent/abstract.py`
```
1245
1246
1247
1248
1249
1250
1251
1252
1253
1254
1255
1256
1257
1258
1259
1260
1261
1262
1263
1264
1265
1266
1267
1268
1269
1270
1271
1272
1273
1274
1275
1276
1277
1278
1279
1280
1281
1282
1283
1284
1285
1286
1287
1288
1289
1290
1291
1292
1293
1294
1295
1296
1297
1298
1299
1300
1301
1302
1303
1304
1305
1306
1307
1308
1309
1310
1311
1312
1313
1314
1315
1316
1317
1318
1319
1320
1321
1322
1323
1324
1325
1326
1327
1328
1329
1330
1331
1332
1333
1334
1335
1336
1337
1338
1339
1340
1341
1342
1343
1344
1345
1346
1347
1348
1349
1350
1351
1352
```
| ```
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
    """
    from pydantic_ai.ui.ag_ui.app import AGUIApp

    return AGUIApp(
        agent=self,
        # Agent.iter parameters
        output_type=output_type,
        message_history=message_history,
        deferred_tool_results=deferred_tool_results,
        model=model,
        deps=deps,
        model_settings=model_settings,
        usage_limits=usage_limits,
        usage=usage,
        infer_name=infer_name,
        toolsets=toolsets,
        # Starlette
        debug=debug,
        routes=routes,
        middleware=middleware,
        exception_handlers=exception_handlers,
