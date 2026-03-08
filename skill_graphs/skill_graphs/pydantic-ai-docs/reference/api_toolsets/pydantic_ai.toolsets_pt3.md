        else:
            return await tool.call_func(tool_args, ctx)

```

---|---
####  __init__
```
__init__(
    tools: [
        Tool[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.Tool "Tool



      dataclass
   \(pydantic_ai.tools.Tool\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai._run_context.AgentDepsT\)")] | ToolFuncEither[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolFuncEither "ToolFuncEither



      module-attribute
   \(pydantic_ai.tools.ToolFuncEither\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai._run_context.AgentDepsT\)"), ...]
    ] = [],
    *,
    max_retries:  = 1,
    timeout:  | None = None,
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
    id:  | None = None
)

```

Build a new function toolset.
Parameters:
Name | Type | Description | Default
---|---|---|---
`tools` |  `Tool[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.Tool "Tool



      dataclass
   \(pydantic_ai.tools.Tool\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai._run_context.AgentDepsT\)")] | ToolFuncEither[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolFuncEither "ToolFuncEither



      module-attribute
   \(pydantic_ai.tools.ToolFuncEither\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai._run_context.AgentDepsT\)"), ...]]` |  The tools to add to the toolset. |  `[]`
`max_retries` |  |  The maximum number of retries for each tool during a run. Applies to all tools, unless overridden when adding a tool. |  `1`
`timeout` |  |  Timeout in seconds for tool execution. If a tool takes longer than this, a retry prompt is returned to the model. Individual tools can override this with their own timeout. Defaults to None (no timeout). |  `None`
`docstring_format` |  `DocstringFormat[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.DocstringFormat "DocstringFormat



      module-attribute
   \(pydantic_ai.tools.DocstringFormat\)")` |  Format of tool docstring, see [`DocstringFormat`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.DocstringFormat "DocstringFormat



      module-attribute
  "). Defaults to `'auto'`, such that the format is inferred from the structure of the docstring. Applies to all tools, unless overridden when adding a tool. |  `'auto'`
`require_parameter_descriptions` |  |  If True, raise an error if a parameter description is missing. Defaults to False. Applies to all tools, unless overridden when adding a tool. |  `False`
`schema_generator` |  `GenerateJsonSchema[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema "pydantic.json_schema.GenerateJsonSchema")]` |  The JSON schema generator class to use for this tool. Defaults to `GenerateToolJsonSchema`. Applies to all tools, unless overridden when adding a tool. |  `GenerateToolJsonSchema`
`strict` |  |  Whether to enforce JSON schema compliance (only affects OpenAI). See [`ToolDefinition`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolDefinition "ToolDefinition



      dataclass
  ") for more info. |  `None`
`sequential` |  |  Whether the function requires a sequential/serial execution environment. Defaults to False. Applies to all tools, unless overridden when adding a tool. |  `False`
`requires_approval` |  |  Whether this tool requires human-in-the-loop approval. Defaults to False. See the [tools documentation](https://ai.pydantic.dev/deferred-tools/#human-in-the-loop-tool-approval) for more info. Applies to all tools, unless overridden when adding a tool. |  `False`
`metadata` |  |  Optional metadata for the tool. This is not sent to the model but can be used for filtering and tool behavior customization. Applies to all tools, unless overridden when adding a tool, which will be merged with the toolset's metadata. |  `None`
`id` |  |  An optional unique ID for the toolset. A toolset needs to have an ID in order to be used in a durable execution environment like Temporal, in which case the ID will be used to identify the toolset's activities within the workflow. |  `None`
Source code in `pydantic_ai_slim/pydantic_ai/toolsets/function.py`
```
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
```
| ```
def __init__(
    self,
    tools: Sequence[Tool[AgentDepsT] | ToolFuncEither[AgentDepsT, ...]] = [],
    *,
    max_retries: int = 1,
    timeout: float | None = None,
    docstring_format: DocstringFormat = 'auto',
    require_parameter_descriptions: bool = False,
    schema_generator: type[GenerateJsonSchema] = GenerateToolJsonSchema,
    strict: bool | None = None,
    sequential: bool = False,
    requires_approval: bool = False,
    metadata: dict[str, Any] | None = None,
    id: str | None = None,
):
    """Build a new function toolset.

    Args:
        tools: The tools to add to the toolset.
        max_retries: The maximum number of retries for each tool during a run.
            Applies to all tools, unless overridden when adding a tool.
        timeout: Timeout in seconds for tool execution. If a tool takes longer than this,
            a retry prompt is returned to the model. Individual tools can override this with their own timeout.
            Defaults to None (no timeout).
        docstring_format: Format of tool docstring, see [`DocstringFormat`][pydantic_ai.tools.DocstringFormat].
            Defaults to `'auto'`, such that the format is inferred from the structure of the docstring.
            Applies to all tools, unless overridden when adding a tool.
        require_parameter_descriptions: If True, raise an error if a parameter description is missing. Defaults to False.
            Applies to all tools, unless overridden when adding a tool.
        schema_generator: The JSON schema generator class to use for this tool. Defaults to `GenerateToolJsonSchema`.
            Applies to all tools, unless overridden when adding a tool.
        strict: Whether to enforce JSON schema compliance (only affects OpenAI).
            See [`ToolDefinition`][pydantic_ai.tools.ToolDefinition] for more info.
        sequential: Whether the function requires a sequential/serial execution environment. Defaults to False.
            Applies to all tools, unless overridden when adding a tool.
        requires_approval: Whether this tool requires human-in-the-loop approval. Defaults to False.
            See the [tools documentation](../deferred-tools.md#human-in-the-loop-tool-approval) for more info.
            Applies to all tools, unless overridden when adding a tool.
        metadata: Optional metadata for the tool. This is not sent to the model but can be used for filtering and tool behavior customization.
            Applies to all tools, unless overridden when adding a tool, which will be merged with the toolset's metadata.
        id: An optional unique ID for the toolset. A toolset needs to have an ID in order to be used in a durable execution environment like Temporal,
            in which case the ID will be used to identify the toolset's activities within the workflow.
    """
    self.max_retries = max_retries
    self.timeout = timeout
    self._id = id
    self.docstring_format = docstring_format
    self.require_parameter_descriptions = require_parameter_descriptions
    self.schema_generator = schema_generator
    self.strict = strict
    self.sequential = sequential
    self.requires_approval = requires_approval
    self.metadata = metadata

    self.tools = {}
    for tool in tools:
        if isinstance(tool, Tool):
            self.add_tool(tool)  # pyright: ignore[reportUnknownArgumentType]
        else:
            self.add_function(tool)

```

---|---
####  tool
```
tool(
    func: ToolFuncEither[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolFuncEither "ToolFuncEither



      module-attribute
   \(pydantic_ai.tools.ToolFuncEither\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai._run_context.AgentDepsT\)"), ToolParams[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolParams "ToolParams



      module-attribute
   \(pydantic_ai.tools.ToolParams\)")],
) -> ToolFuncEither[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolFuncEither "ToolFuncEither



      module-attribute
   \(pydantic_ai.tools.ToolFuncEither\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai._run_context.AgentDepsT\)"), ToolParams[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolParams "ToolParams



      module-attribute
   \(pydantic_ai.tools.ToolParams\)")]

```

```
tool(
    *,
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
    timeout:  | None = None
) -> [
    [ToolFuncEither[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolFuncEither "ToolFuncEither



      module-attribute
   \(pydantic_ai.tools.ToolFuncEither\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai._run_context.AgentDepsT\)"), ToolParams[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolParams "ToolParams



      module-attribute
   \(pydantic_ai.tools.ToolParams\)")]],
    ToolFuncEither[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolFuncEither "ToolFuncEither



      module-attribute
   \(pydantic_ai.tools.ToolFuncEither\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai._run_context.AgentDepsT\)"), ToolParams[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolParams "ToolParams



      module-attribute
   \(pydantic_ai.tools.ToolParams\)")],
]

```

```
tool(
    func: (
        ToolFuncEither[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolFuncEither "ToolFuncEither



      module-attribute
   \(pydantic_ai.tools.ToolFuncEither\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai._run_context.AgentDepsT\)"), ToolParams[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolParams "ToolParams



      module-attribute
   \(pydantic_ai.tools.ToolParams\)")] | None
    ) = None,
    /,
    *,
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
) ->

```

Decorator to register a tool function which takes [`RunContext`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext



      dataclass
  ") as its first argument.
Can decorate a sync or async functions.
The docstring is inspected to extract both the tool description and description of each parameter, [learn more](https://ai.pydantic.dev/tools/#function-tools-and-schema).
We can't add overloads for every possible signature of tool, since the return type is a recursive union so the signature of functions decorated with `@toolset.tool` is obscured.
Example:
```
from pydantic_ai import Agent, FunctionToolset, RunContext

toolset = FunctionToolset()

@toolset.tool
def foobar(ctx: RunContext[int], x: int) -> int:
    return ctx.deps + x

@toolset.tool(retries=2)
async def spam(ctx: RunContext[str], y: float) -> float:
    return ctx.deps + y

agent = Agent('test', toolsets=[toolset], deps_type=int)
result = agent.run_sync('foobar', deps=1)
print(result.output)
#> {"foobar":1,"spam":1.0}

```

Parameters:
Name | Type | Description | Default
---|---|---|---
`func` |  `ToolFuncEither[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolFuncEither "ToolFuncEither



      module-attribute
   \(pydantic_ai.tools.ToolFuncEither\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai._run_context.AgentDepsT\)"), ToolParams[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolParams "ToolParams



      module-attribute
   \(pydantic_ai.tools.ToolParams\)")] | None` |  The tool function to register. |  `None`
`name` |  |  The name of the tool, defaults to the function name. |  `None`
`description` |  |  The description of the tool,defaults to the function docstring. |  `None`
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
229
230
231
232
233
234
235
236
237
238
239
240
241
242
243
244
245
246
247
```
| ```
def tool(
    self,
    func: ToolFuncEither[AgentDepsT, ToolParams] | None = None,
    /,
    *,
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
) -> Any:
    """Decorator to register a tool function which takes [`RunContext`][pydantic_ai.tools.RunContext] as its first argument.

    Can decorate a sync or async functions.

    The docstring is inspected to extract both the tool description and description of each parameter,
    [learn more](../tools.md#function-tools-and-schema).

    We can't add overloads for every possible signature of tool, since the return type is a recursive union
    so the signature of functions decorated with `@toolset.tool` is obscured.

    Example:
```python
    from pydantic_ai import Agent, FunctionToolset, RunContext

    toolset = FunctionToolset()

    @toolset.tool
    def foobar(ctx: RunContext[int], x: int) -> int:
        return ctx.deps + x

    @toolset.tool(retries=2)
    async def spam(ctx: RunContext[str], y: float) -> float:
        return ctx.deps + y

    agent = Agent('test', toolsets=[toolset], deps_type=int)
    result = agent.run_sync('foobar', deps=1)
    print(result.output)
    #> {"foobar":1,"spam":1.0}
```

    Args:
        func: The tool function to register.
        name: The name of the tool, defaults to the function name.
        description: The description of the tool,defaults to the function docstring.
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

    def tool_decorator(
        func_: ToolFuncEither[AgentDepsT, ToolParams],
