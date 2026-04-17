    ) -> ToolFuncEither[AgentDepsT, ToolParams]:
        # noinspection PyTypeChecker
        self.add_function(
            func=func_,
            takes_ctx=None,
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
####  add_function
```
add_function(
    func: ToolFuncEither[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolFuncEither "ToolFuncEither



      module-attribute
   \(pydantic_ai.tools.ToolFuncEither\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai._run_context.AgentDepsT\)"), ToolParams[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolParams "ToolParams



      module-attribute
   \(pydantic_ai.tools.ToolParams\)")],
    takes_ctx:  | None = None,
    name:  | None = None,
    description:  | None = None,
    retries:  | None = None,
    prepare: ToolPrepareFunc[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolPrepareFunc "ToolPrepareFunc



      module-attribute
   \(pydantic_ai.tools.ToolPrepareFunc\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai._run_context.AgentDepsT\)")] | None = None,
    args_validator: (
        ArgsValidatorFunc[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ArgsValidatorFunc "ArgsValidatorFunc



      module-attribute
   \(pydantic_ai.tools.ArgsValidatorFunc\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai._run_context.AgentDepsT\)"), ToolParams[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolParams "ToolParams



      module-attribute
   \(pydantic_ai.tools.ToolParams\)")] | None
    ) = None,
    docstring_format: DocstringFormat[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.DocstringFormat "DocstringFormat



      module-attribute
   \(pydantic_ai.tools.DocstringFormat\)") | None = None,
    require_parameter_descriptions:  | None = None,
    schema_generator: (
        [GenerateJsonSchema[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema "pydantic.json_schema.GenerateJsonSchema")] | None
    ) = None,
    strict:  | None = None,
    sequential:  | None = None,
    requires_approval:  | None = None,
    metadata: [, ] | None = None,
    timeout:  | None = None,
) -> None

```

Add a function as a tool to the toolset.
Can take a sync or async function.
The docstring is inspected to extract both the tool description and description of each parameter, [learn more](https://ai.pydantic.dev/tools/#function-tools-and-schema).
Parameters:
Name | Type | Description | Default
---|---|---|---
`func` |  `ToolFuncEither[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolFuncEither "ToolFuncEither



      module-attribute
   \(pydantic_ai.tools.ToolFuncEither\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai._run_context.AgentDepsT\)"), ToolParams[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolParams "ToolParams



      module-attribute
   \(pydantic_ai.tools.ToolParams\)")]` |  The tool function to register. |  _required_
`takes_ctx` |  |  Whether the function takes a [`RunContext`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext



      dataclass
  ") as its first argument. If `None`, this is inferred from the function signature. |  `None`
`name` |  |  The name of the tool, defaults to the function name. |  `None`
`description` |  |  The description of the tool, defaults to the function docstring. |  `None`
`retries` |  |  The number of retries to allow for this tool, defaults to the agent's default retries, which defaults to 1. |  `None`
`prepare` |  `ToolPrepareFunc[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolPrepareFunc "ToolPrepareFunc



      module-attribute
   \(pydantic_ai.tools.ToolPrepareFunc\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai._run_context.AgentDepsT\)")] | None` |  custom method to prepare the tool definition for each step, return `None` to omit this tool from a given step. This is useful if you want to customise a tool at call time, or omit it completely from a step. See [`ToolPrepareFunc`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolPrepareFunc "ToolPrepareFunc



      module-attribute
  "). |  `None`
`args_validator` |  `ArgsValidatorFunc[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ArgsValidatorFunc "ArgsValidatorFunc



      module-attribute
   \(pydantic_ai.tools.ArgsValidatorFunc\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai._run_context.AgentDepsT\)"), ToolParams[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolParams "ToolParams



      module-attribute
   \(pydantic_ai.tools.ToolParams\)")] | None` |  custom method to validate tool arguments after schema validation has passed, before execution. The validator receives the already-validated and type-converted parameters, with `RunContext` as the first argument. Should raise [`ModelRetry`](https://ai.pydantic.dev/api/exceptions/#pydantic_ai.exceptions.ModelRetry "ModelRetry") on validation failure, return `None` on success. See [`ArgsValidatorFunc`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ArgsValidatorFunc "ArgsValidatorFunc



      module-attribute
  "). |  `None`
`docstring_format` |  `DocstringFormat[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.DocstringFormat "DocstringFormat



      module-attribute
   \(pydantic_ai.tools.DocstringFormat\)") | None` |  The format of the docstring, see [`DocstringFormat`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.DocstringFormat "DocstringFormat



      module-attribute
  "). If `None`, the default value is determined by the toolset. |  `None`
`require_parameter_descriptions` |  |  If True, raise an error if a parameter description is missing. If `None`, the default value is determined by the toolset. |  `None`
`schema_generator` |  `GenerateJsonSchema[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema "pydantic.json_schema.GenerateJsonSchema")] | None` |  The JSON schema generator class to use for this tool. If `None`, the default value is determined by the toolset. |  `None`
`strict` |  |  Whether to enforce JSON schema compliance (only affects OpenAI). See [`ToolDefinition`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolDefinition "ToolDefinition



      dataclass
  ") for more info. If `None`, the default value is determined by the toolset. |  `None`
`sequential` |  |  Whether the function requires a sequential/serial execution environment. Defaults to False. If `None`, the default value is determined by the toolset. |  `None`
`requires_approval` |  |  Whether this tool requires human-in-the-loop approval. Defaults to False. See the [tools documentation](https://ai.pydantic.dev/deferred-tools/#human-in-the-loop-tool-approval) for more info. If `None`, the default value is determined by the toolset. |  `None`
`metadata` |  |  Optional metadata for the tool. This is not sent to the model but can be used for filtering and tool behavior customization. If `None`, the default value is determined by the toolset. If provided, it will be merged with the toolset's metadata. |  `None`
`timeout` |  |  Timeout in seconds for tool execution. If the tool takes longer, a retry prompt is returned to the model. Defaults to None (no timeout). |  `None`
Source code in `pydantic_ai_slim/pydantic_ai/toolsets/function.py`
```
249
250
251
252
253
254
255
256
257
258
259
260
261
262
263
264
265
266
267
268
269
270
271
272
273
274
275
276
277
278
279
280
281
282
283
284
285
286
287
288
289
290
291
292
293
294
295
296
297
298
299
300
301
302
303
304
305
306
307
308
309
310
311
312
313
314
315
316
317
318
319
320
321
322
323
324
325
326
327
328
329
330
331
332
333
334
335
336
337
338
339
```
| ```
def add_function(
    self,
    func: ToolFuncEither[AgentDepsT, ToolParams],
    takes_ctx: bool | None = None,
    name: str | None = None,
    description: str | None = None,
    retries: int | None = None,
    prepare: ToolPrepareFunc[AgentDepsT] | None = None,
    args_validator: ArgsValidatorFunc[AgentDepsT, ToolParams] | None = None,
    docstring_format: DocstringFormat | None = None,
    require_parameter_descriptions: bool | None = None,
    schema_generator: type[GenerateJsonSchema] | None = None,
    strict: bool | None = None,
    sequential: bool | None = None,
    requires_approval: bool | None = None,
    metadata: dict[str, Any] | None = None,
    timeout: float | None = None,
) -> None:
    """Add a function as a tool to the toolset.

    Can take a sync or async function.

    The docstring is inspected to extract both the tool description and description of each parameter,
    [learn more](../tools.md#function-tools-and-schema).

    Args:
        func: The tool function to register.
        takes_ctx: Whether the function takes a [`RunContext`][pydantic_ai.tools.RunContext] as its first argument. If `None`, this is inferred from the function signature.
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
            If `None`, the default value is determined by the toolset.
        require_parameter_descriptions: If True, raise an error if a parameter description is missing.
            If `None`, the default value is determined by the toolset.
        schema_generator: The JSON schema generator class to use for this tool.
            If `None`, the default value is determined by the toolset.
        strict: Whether to enforce JSON schema compliance (only affects OpenAI).
            See [`ToolDefinition`][pydantic_ai.tools.ToolDefinition] for more info.
            If `None`, the default value is determined by the toolset.
        sequential: Whether the function requires a sequential/serial execution environment. Defaults to False.
            If `None`, the default value is determined by the toolset.
        requires_approval: Whether this tool requires human-in-the-loop approval. Defaults to False.
            See the [tools documentation](../deferred-tools.md#human-in-the-loop-tool-approval) for more info.
            If `None`, the default value is determined by the toolset.
        metadata: Optional metadata for the tool. This is not sent to the model but can be used for filtering and tool behavior customization.
            If `None`, the default value is determined by the toolset. If provided, it will be merged with the toolset's metadata.
        timeout: Timeout in seconds for tool execution. If the tool takes longer, a retry prompt is returned to the model.
            Defaults to None (no timeout).
    """
    if docstring_format is None:
        docstring_format = self.docstring_format
    if require_parameter_descriptions is None:
        require_parameter_descriptions = self.require_parameter_descriptions
    if schema_generator is None:
        schema_generator = self.schema_generator
    if strict is None:
        strict = self.strict
    if sequential is None:
        sequential = self.sequential
    if requires_approval is None:
        requires_approval = self.requires_approval

    tool = Tool[AgentDepsT](
        func,
        takes_ctx=takes_ctx,
        name=name,
        description=description,
        max_retries=retries,
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
    self.add_tool(tool)

```

---|---
####  add_tool
```
add_tool(tool: Tool[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.Tool "Tool



      dataclass
   \(pydantic_ai.tools.Tool\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai._run_context.AgentDepsT\)")]) -> None

```

Add a tool to the toolset.
Parameters:
Name | Type | Description | Default
---|---|---|---
`tool` |  `Tool[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.Tool "Tool



      dataclass
   \(pydantic_ai.tools.Tool\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai._run_context.AgentDepsT\)")]` |  The tool to add. |  _required_
Source code in `pydantic_ai_slim/pydantic_ai/toolsets/function.py`
```
341
342
343
344
345
346
347
348
349
350
351
352
353
```
| ```
def add_tool(self, tool: Tool[AgentDepsT]) -> None:
    """Add a tool to the toolset.

    Args:
        tool: The tool to add.
    """
    if tool.name in self.tools:
        raise UserError(f'Tool name conflicts with existing tool: {tool.name!r}')
    if tool.max_retries is None:
        tool.max_retries = self.max_retries
    if self.metadata is not None:
        tool.metadata = self.metadata | (tool.metadata or {})
    self.tools[tool.name] = tool

```

---|---
###  PrefixedToolset `dataclass`
Bases: `WrapperToolset[](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.WrapperToolset "WrapperToolset



      dataclass
   \(pydantic_ai.toolsets.wrapper.WrapperToolset\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai._run_context.AgentDepsT\)")]`
A toolset that prefixes the names of the tools it contains.
See [toolset docs](https://ai.pydantic.dev/toolsets/#prefixing-tool-names) for more information.
Source code in `pydantic_ai_slim/pydantic_ai/toolsets/prefixed.py`
```
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
36
37
38
39
40
41
```
| ```
@dataclass
class PrefixedToolset(WrapperToolset[AgentDepsT]):
    """A toolset that prefixes the names of the tools it contains.

    See [toolset docs](../toolsets.md#prefixing-tool-names) for more information.
    """

    prefix: str

    @property
    def tool_name_conflict_hint(self) -> str:
        return 'Change the `prefix` attribute to avoid name conflicts.'

    async def get_tools(self, ctx: RunContext[AgentDepsT]) -> dict[str, ToolsetTool[AgentDepsT]]:
        return {
            new_name: replace(
                tool,
                toolset=self,
                tool_def=replace(tool.tool_def, name=new_name),
            )
            for name, tool in (await super().get_tools(ctx)).items()
            if (new_name := f'{self.prefix}_{name}')
        }

    async def call_tool(
        self, name: str, tool_args: dict[str, Any], ctx: RunContext[AgentDepsT], tool: ToolsetTool[AgentDepsT]
    ) -> Any:
        original_name = name.removeprefix(self.prefix + '_')
        ctx = replace(ctx, tool_name=original_name)
        tool = replace(tool, tool_def=replace(tool.tool_def, name=original_name))
        return await super().call_tool(original_name, tool_args, ctx, tool)

```

---|---
###  RenamedToolset `dataclass`
Bases: `WrapperToolset[](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.WrapperToolset "WrapperToolset



      dataclass
   \(pydantic_ai.toolsets.wrapper.WrapperToolset\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai._run_context.AgentDepsT\)")]`
A toolset that renames the tools it contains using a dictionary mapping new names to original names.
See [toolset docs](https://ai.pydantic.dev/toolsets/#renaming-tools) for more information.
Source code in `pydantic_ai_slim/pydantic_ai/toolsets/renamed.py`
```
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
36
37
38
39
40
41
42
```
| ```
@dataclass
class RenamedToolset(WrapperToolset[AgentDepsT]):
    """A toolset that renames the tools it contains using a dictionary mapping new names to original names.

    See [toolset docs](../toolsets.md#renaming-tools) for more information.
    """

    name_map: dict[str, str]

    async def get_tools(self, ctx: RunContext[AgentDepsT]) -> dict[str, ToolsetTool[AgentDepsT]]:
        original_to_new_name_map = {v: k for k, v in self.name_map.items()}
        original_tools = await super().get_tools(ctx)
        tools: dict[str, ToolsetTool[AgentDepsT]] = {}
        for original_name, tool in original_tools.items():
            new_name = original_to_new_name_map.get(original_name, None)
            if new_name:
                tools[new_name] = replace(
                    tool,
                    toolset=self,
                    tool_def=replace(tool.tool_def, name=new_name),
                )
            else:
                tools[original_name] = tool
        return tools

    async def call_tool(
        self, name: str, tool_args: dict[str, Any], ctx: RunContext[AgentDepsT], tool: ToolsetTool[AgentDepsT]
    ) -> Any:
        original_name = self.name_map.get(name, name)
        ctx = replace(ctx, tool_name=original_name)
        tool = replace(tool, tool_def=replace(tool.tool_def, name=original_name))
        return await super().call_tool(original_name, tool_args, ctx, tool)

```

---|---
###  PreparedToolset `dataclass`
Bases: `WrapperToolset[](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.WrapperToolset "WrapperToolset



      dataclass
   \(pydantic_ai.toolsets.wrapper.WrapperToolset\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai._run_context.AgentDepsT\)")]`
A toolset that prepares the tools it contains using a prepare function that takes the agent context and the original tool definitions.
See [toolset docs](https://ai.pydantic.dev/toolsets/#preparing-tool-definitions) for more information.
Source code in `pydantic_ai_slim/pydantic_ai/toolsets/prepared.py`
```
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
36
```
| ```
@dataclass
class PreparedToolset(WrapperToolset[AgentDepsT]):
    """A toolset that prepares the tools it contains using a prepare function that takes the agent context and the original tool definitions.

    See [toolset docs](../toolsets.md#preparing-tool-definitions) for more information.
    """

    prepare_func: ToolsPrepareFunc[AgentDepsT]

    async def get_tools(self, ctx: RunContext[AgentDepsT]) -> dict[str, ToolsetTool[AgentDepsT]]:
        original_tools = await super().get_tools(ctx)
        original_tool_defs = [tool.tool_def for tool in original_tools.values()]
        prepared_tool_defs_by_name = {
            tool_def.name: tool_def for tool_def in (await self.prepare_func(ctx, original_tool_defs) or [])
        }

        if len(prepared_tool_defs_by_name.keys() - original_tools.keys()) > 0:
            raise UserError(
                'Prepare function cannot add or rename tools. Use `FunctionToolset.add_function()` or `RenamedToolset` instead.'
            )

        return {
            name: replace(original_tools[name], tool_def=tool_def)
            for name, tool_def in prepared_tool_defs_by_name.items()
        }

```

---|---
###  WrapperToolset `dataclass`
Bases: `AbstractToolset[](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.AbstractToolset "AbstractToolset \(pydantic_ai.toolsets.abstract.AbstractToolset\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai._run_context.AgentDepsT\)")]`
A toolset that wraps another toolset and delegates to it.
See [toolset docs](https://ai.pydantic.dev/toolsets/#wrapping-a-toolset) for more information.
Source code in `pydantic_ai_slim/pydantic_ai/toolsets/wrapper.py`
```
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
```
| ```
@dataclass
class WrapperToolset(AbstractToolset[AgentDepsT]):
    """A toolset that wraps another toolset and delegates to it.

    See [toolset docs](../toolsets.md#wrapping-a-toolset) for more information.
    """

    wrapped: AbstractToolset[AgentDepsT]

    @property
    def id(self) -> str | None:
        return None  # pragma: no cover

    @property
    def label(self) -> str:
        return f'{self.__class__.__name__}({self.wrapped.label})'

    async def __aenter__(self) -> Self:
        await self.wrapped.__aenter__()
        return self

    async def __aexit__(self, *args: Any) -> bool | None:
        return await self.wrapped.__aexit__(*args)

    async def get_tools(self, ctx: RunContext[AgentDepsT]) -> dict[str, ToolsetTool[AgentDepsT]]:
        return await self.wrapped.get_tools(ctx)

    async def call_tool(
        self, name: str, tool_args: dict[str, Any], ctx: RunContext[AgentDepsT], tool: ToolsetTool[AgentDepsT]
    ) -> Any:
        return await self.wrapped.call_tool(name, tool_args, ctx, tool)

    def apply(self, visitor: Callable[[AbstractToolset[AgentDepsT]], None]) -> None:
        self.wrapped.apply(visitor)

    def visit_and_replace(
        self, visitor: Callable[[AbstractToolset[AgentDepsT]], AbstractToolset[AgentDepsT]]
    ) -> AbstractToolset[AgentDepsT]:
        return replace(self, wrapped=self.wrapped.visit_and_replace(visitor))

```

---|---
###  ToolsetFunc `module-attribute`
```
ToolsetFunc:  = [
    [RunContext[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext



      dataclass
   \(pydantic_ai._run_context.RunContext\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai._run_context.AgentDepsT\)")]],
    AbstractToolset[](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.AbstractToolset "AbstractToolset \(pydantic_ai.toolsets.abstract.AbstractToolset\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai._run_context.AgentDepsT\)")]
    | None
    | [AbstractToolset[](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.AbstractToolset "AbstractToolset \(pydantic_ai.toolsets.abstract.AbstractToolset\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai._run_context.AgentDepsT\)")] | None],
]

```

A sync/async function which takes a run context and returns a toolset.
###  FastMCPToolset `dataclass`
Bases: `AbstractToolset[](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.AbstractToolset "AbstractToolset \(pydantic_ai.toolsets.AbstractToolset\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]`
A FastMCP Toolset that uses the FastMCP Client to call tools from a local or remote MCP Server.
The Toolset can accept a FastMCP Client, a FastMCP Transport, or any other object which a FastMCP Transport can be created from.
See https://gofastmcp.com/clients/transports for a full list of transports available.
Source code in `pydantic_ai_slim/pydantic_ai/toolsets/fastmcp_server.py`
```
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
