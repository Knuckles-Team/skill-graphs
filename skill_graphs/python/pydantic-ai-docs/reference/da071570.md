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

```

---|---
####  tool_plain
```
tool_plain(
    func: ToolFuncPlain[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolFuncPlain "ToolFuncPlain



      module-attribute
   \(pydantic_ai.tools.ToolFuncPlain\)")[ToolParams[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolParams "ToolParams



      module-attribute
   \(pydantic_ai.tools.ToolParams\)")],
) -> ToolFuncPlain[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolFuncPlain "ToolFuncPlain



      module-attribute
   \(pydantic_ai.tools.ToolFuncPlain\)")[ToolParams[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolParams "ToolParams



      module-attribute
   \(pydantic_ai.tools.ToolParams\)")]

```

```
tool_plain(
    *,
    name:  | None = None,
    description:  | None = None,
    retries:  | None = None,
    prepare: ToolPrepareFunc[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolPrepareFunc "ToolPrepareFunc



      module-attribute
   \(pydantic_ai.tools.ToolPrepareFunc\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")] | None = None,
    args_validator: (
        ArgsValidatorFunc[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ArgsValidatorFunc "ArgsValidatorFunc



      module-attribute
   \(pydantic_ai.tools.ArgsValidatorFunc\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)"), ToolParams[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolParams "ToolParams



      module-attribute
   \(pydantic_ai.tools.ToolParams\)")] | None
    ) = None,
    docstring_format: DocstringFormat[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.DocstringFormat "DocstringFormat



      module-attribute
   \(pydantic_ai.tools.DocstringFormat\)") = "auto",
    require_parameter_descriptions:  = False,
    schema_generator: [
        GenerateJsonSchema[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema "pydantic.json_schema.GenerateJsonSchema")
    ] = GenerateToolJsonSchema,
    strict:  | None = None,
    sequential:  = False,
    requires_approval:  = False,
    metadata: [, ] | None = None,
    timeout:  | None = None
) -> [
    [ToolFuncPlain[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolFuncPlain "ToolFuncPlain



      module-attribute
   \(pydantic_ai.tools.ToolFuncPlain\)")[ToolParams[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolParams "ToolParams



      module-attribute
   \(pydantic_ai.tools.ToolParams\)")]], ToolFuncPlain[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolFuncPlain "ToolFuncPlain



      module-attribute
   \(pydantic_ai.tools.ToolFuncPlain\)")[ToolParams[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolParams "ToolParams



      module-attribute
   \(pydantic_ai.tools.ToolParams\)")]
]

```

```
tool_plain(
    func: ToolFuncPlain[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolFuncPlain "ToolFuncPlain



      module-attribute
   \(pydantic_ai.tools.ToolFuncPlain\)")[ToolParams[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolParams "ToolParams



      module-attribute
   \(pydantic_ai.tools.ToolParams\)")] | None = None,
    /,
    *,
    name:  | None = None,
    description:  | None = None,
    retries:  | None = None,
    prepare: ToolPrepareFunc[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolPrepareFunc "ToolPrepareFunc



      module-attribute
   \(pydantic_ai.tools.ToolPrepareFunc\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")] | None = None,
    args_validator: (
        ArgsValidatorFunc[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ArgsValidatorFunc "ArgsValidatorFunc



      module-attribute
   \(pydantic_ai.tools.ArgsValidatorFunc\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)"), ToolParams[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolParams "ToolParams



      module-attribute
   \(pydantic_ai.tools.ToolParams\)")] | None
    ) = None,
    docstring_format: DocstringFormat[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.DocstringFormat "DocstringFormat



      module-attribute
   \(pydantic_ai.tools.DocstringFormat\)") = "auto",
    require_parameter_descriptions:  = False,
    schema_generator: [
        GenerateJsonSchema[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema "pydantic.json_schema.GenerateJsonSchema")
    ] = GenerateToolJsonSchema,
    strict:  | None = None,
    sequential:  = False,
    requires_approval:  = False,
    metadata: [, ] | None = None,
    timeout:  | None = None,
) ->

```

Decorator to register a tool function which DOES NOT take `RunContext` as an argument.
Can decorate a sync or async functions.
The docstring is inspected to extract both the tool description and description of each parameter, [learn more](https://ai.pydantic.dev/tools/#function-tools-and-schema).
We can't add overloads for every possible signature of tool, since the return type is a recursive union so the signature of functions decorated with `@agent.tool` is obscured.
Example:
```
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

Parameters:
Name | Type | Description | Default
---|---|---|---
`func` |  `ToolFuncPlain[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolFuncPlain "ToolFuncPlain



      module-attribute
   \(pydantic_ai.tools.ToolFuncPlain\)")[ToolParams[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolParams "ToolParams



      module-attribute
   \(pydantic_ai.tools.ToolParams\)")] | None` |  The tool function to register. |  `None`
`name` |  |  The name of the tool, defaults to the function name. |  `None`
`description` |  |  The description of the tool, defaults to the function docstring. |  `None`
`retries` |  |  The number of retries to allow for this tool, defaults to the agent's default retries, which defaults to 1. |  `None`
`prepare` |  `ToolPrepareFunc[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolPrepareFunc "ToolPrepareFunc



      module-attribute
   \(pydantic_ai.tools.ToolPrepareFunc\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")] | None` |  custom method to prepare the tool definition for each step, return `None` to omit this tool from a given step. This is useful if you want to customise a tool at call time, or omit it completely from a step. See [`ToolPrepareFunc`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolPrepareFunc "ToolPrepareFunc



      module-attribute
  "). |  `None`
`args_validator` |  `ArgsValidatorFunc[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ArgsValidatorFunc "ArgsValidatorFunc



      module-attribute
   \(pydantic_ai.tools.ArgsValidatorFunc\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)"), ToolParams[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolParams "ToolParams



      module-attribute
   \(pydantic_ai.tools.ToolParams\)")] | None` |  custom method to validate tool arguments after schema validation has passed, before execution. The validator receives the already-validated and type-converted parameters, with [`RunContext`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext



      dataclass
  ") as the first argument — even though the tool function itself does not take `RunContext` when using `tool_plain`. Should raise [`ModelRetry`](https://ai.pydantic.dev/api/exceptions/#pydantic_ai.exceptions.ModelRetry "ModelRetry") on validation failure, return `None` on success. See [`ArgsValidatorFunc`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ArgsValidatorFunc "ArgsValidatorFunc



      module-attribute
  "). |  `None`
`docstring_format` |  `DocstringFormat[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.DocstringFormat "DocstringFormat



      module-attribute
   \(pydantic_ai.tools.DocstringFormat\)")` |  The format of the docstring, see [`DocstringFormat`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.DocstringFormat "DocstringFormat



      module-attribute
  "). Defaults to `'auto'`, such that the format is inferred from the structure of the docstring. |  `'auto'`
`require_parameter_descriptions` |  |  If True, raise an error if a parameter description is missing. Defaults to False. |  `False`
`schema_generator` |  `GenerateJsonSchema[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema "pydantic.json_schema.GenerateJsonSchema")]` |  The JSON schema generator class to use for this tool. Defaults to `GenerateToolJsonSchema`. |  `GenerateToolJsonSchema`
`strict` |  |  Whether to enforce JSON schema compliance (only affects OpenAI). See [`ToolDefinition`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolDefinition "ToolDefinition



      dataclass
  ") for more info. |  `None`
`sequential` |  |  Whether the function requires a sequential/serial execution environment. Defaults to False. |  `False`
`requires_approval` |  |  Whether this tool requires human-in-the-loop approval. Defaults to False. See the [tools documentation](https://ai.pydantic.dev/deferred-tools/#human-in-the-loop-tool-approval) for more info. |  `False`
`metadata` |  |  Optional metadata for the tool. This is not sent to the model but can be used for filtering and tool behavior customization. |  `None`
`timeout` |  |  Timeout in seconds for tool execution. If the tool takes longer, a retry prompt is returned to the model. Overrides the agent-level `tool_timeout` if set. Defaults to None (no timeout). |  `None`
Source code in `pydantic_ai_slim/pydantic_ai/agent/__init__.py`
```
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
1353
1354
1355
1356
1357
1358
1359
1360
1361
1362
1363
1364
1365
1366
1367
1368
1369
1370
1371
1372
1373
1374
1375
1376
1377
1378
1379
1380
1381
1382
1383
1384
1385
1386
1387
1388
1389
1390
1391
1392
1393
1394
1395
1396
1397
1398
1399
1400
1401
1402
1403
1404
1405
1406
1407
```
| ```
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

```

---|---
####  toolset
```
toolset(
    func: ToolsetFunc[](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.ToolsetFunc "ToolsetFunc



      module-attribute
   \(pydantic_ai.toolsets._dynamic.ToolsetFunc\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")],
) -> ToolsetFunc[](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.ToolsetFunc "ToolsetFunc



      module-attribute
   \(pydantic_ai.toolsets._dynamic.ToolsetFunc\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]

```

```
toolset(
    *, per_run_step:  = True, id:  | None = None
) -> [
    [ToolsetFunc[](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.ToolsetFunc "ToolsetFunc



      module-attribute
   \(pydantic_ai.toolsets._dynamic.ToolsetFunc\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]], ToolsetFunc[](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.ToolsetFunc "ToolsetFunc



      module-attribute
   \(pydantic_ai.toolsets._dynamic.ToolsetFunc\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]
]

```

```
toolset(
    func: ToolsetFunc[](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.ToolsetFunc "ToolsetFunc



      module-attribute
   \(pydantic_ai.toolsets._dynamic.ToolsetFunc\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")] | None = None,
    /,
    *,
    per_run_step:  = True,
    id:  | None = None,
) ->

```

Decorator to register a toolset function which takes [`RunContext`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext



      dataclass
  ") as its only argument.
Can decorate a sync or async functions.
The decorator can be used bare (`agent.toolset`).
Example:
```
from pydantic_ai import AbstractToolset, Agent, FunctionToolset, RunContext

agent = Agent('test', deps_type=str)

@agent.toolset
async def simple_toolset(ctx: RunContext[str]) -> AbstractToolset[str]:
    return FunctionToolset()

```

Parameters:
Name | Type | Description | Default
---|---|---|---
`func` |  `ToolsetFunc[](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.ToolsetFunc "ToolsetFunc



      module-attribute
   \(pydantic_ai.toolsets._dynamic.ToolsetFunc\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")] | None` |  The toolset function to register. |  `None`
`per_run_step` |  |  Whether to re-evaluate the toolset for each run step. Defaults to True. |  `True`
`id` |  |  An optional unique ID for the dynamic toolset. Required for use with durable execution environments like Temporal, where the ID identifies the toolset's activities within the workflow. |  `None`
Source code in `pydantic_ai_slim/pydantic_ai/agent/__init__.py`
```
1421
1422
1423
1424
1425
1426
1427
1428
1429
1430
1431
1432
1433
1434
1435
1436
1437
1438
1439
1440
1441
1442
1443
1444
1445
1446
1447
1448
1449
1450
1451
1452
1453
1454
1455
1456
1457
```
| ```
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

```

---|---
####  toolsets `property`
```
toolsets: [AbstractToolset[](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.AbstractToolset "AbstractToolset \(pydantic_ai.toolsets.AbstractToolset\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]]

```

All toolsets registered on the agent, including a function toolset holding tools that were registered on the agent directly.
Output tools are not included.
####  __aenter__ `async`
```
__aenter__() ->

```

Enter the agent context.
This will start all [`MCPServerStdio`s](https://ai.pydantic.dev/api/mcp/#pydantic_ai.mcp.MCPServerStdio "MCPServerStdio") registered as `toolsets` so they are ready to be used.
This is a no-op if the agent has already been entered.
Source code in `pydantic_ai_slim/pydantic_ai/agent/__init__.py`
```
1619
1620
1621
1622
1623
1624
1625
1626
1627
1628
1629
1630
1631
1632
1633
1634
```
| ```
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

```

---|---
####  set_mcp_sampling_model
```
set_mcp_sampling_model(
    model: Model[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.Model "Model \(pydantic_ai.models.Model\)") | KnownModelName[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.KnownModelName "KnownModelName



      module-attribute
   \(pydantic_ai.models.KnownModelName\)") |  | None = None,
) -> None

```

Set the sampling model on all MCP servers registered with the agent.
If no sampling model is provided, the agent's model will be used.
Source code in `pydantic_ai_slim/pydantic_ai/agent/__init__.py`
```
1643
1644
1645
1646
1647
1648
1649
1650
1651
1652
1653
1654
1655
1656
1657
1658
1659
```
| ```
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

```

---|---
####  to_web
```
to_web(
    *,
    models: ModelsParam = None,
    builtin_tools: [AbstractBuiltinTool[](https://ai.pydantic.dev/api/builtin_tools/#pydantic_ai.builtin_tools.AbstractBuiltinTool "AbstractBuiltinTool



      dataclass
   \(pydantic_ai.builtin_tools.AbstractBuiltinTool\)")] | None = None,
    deps: AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)") = None,
    model_settings: ModelSettings[](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings \(pydantic_ai.settings.ModelSettings\)") | None = None,
    instructions:  | None = None,
    html_source:  |  | None = None
) -> Starlette
