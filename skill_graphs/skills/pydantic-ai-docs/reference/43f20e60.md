```
1045
1046
1047
1048
1049
1050
1051
1052
1053
1054
1055
1056
1057
1058
1059
1060
1061
1062
1063
1064
1065
1066
1067
1068
1069
1070
1071
1072
1073
1074
1075
1076
1077
1078
1079
1080
1081
1082
1083
1084
1085
1086
1087
1088
1089
1090
1091
1092
1093
1094
1095
1096
1097
1098
1099
1100
1101
```
| ```
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

```

---|---
####  output_validator
```
output_validator(
    func: [
        [RunContext[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext



      dataclass
   \(pydantic_ai.tools.RunContext\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")], OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")], OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")
    ],
) -> [
    [RunContext[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext



      dataclass
   \(pydantic_ai.tools.RunContext\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")], OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")], OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")
]

```

```
output_validator(
    func: [
        [RunContext[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext



      dataclass
   \(pydantic_ai.tools.RunContext\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")], OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")],
        [OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")],
    ],
) -> [
    [RunContext[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext



      dataclass
   \(pydantic_ai.tools.RunContext\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")], OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")],
    [OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")],
]

```

```
output_validator(
    func: [[OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")], OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")],
) -> [[OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")], OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")]

```

```
output_validator(
    func: [[OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")], [OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")]],
) -> [[OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")], [OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")]]

```

```
output_validator(
    func: OutputValidatorFunc[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)"), OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")],
) -> OutputValidatorFunc[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)"), OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")]

```

Decorator to register an output validator function.
Optionally takes [`RunContext`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext



      dataclass
  ") as its first argument. Can decorate a sync or async functions.
Overloads for every possible signature of `output_validator` are included so the decorator doesn't obscure the type of the function, see `tests/typed_agent.py` for tests.
Example:
```
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

Source code in `pydantic_ai_slim/pydantic_ai/agent/__init__.py`
```
1123
1124
1125
1126
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
1154
1155
1156
1157
1158
```
| ```
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

```

---|---
####  tool
```
tool(
    func: ToolFuncContext[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolFuncContext "ToolFuncContext



      module-attribute
   \(pydantic_ai.tools.ToolFuncContext\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)"), ToolParams[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolParams "ToolParams



      module-attribute
   \(pydantic_ai.tools.ToolParams\)")],
) -> ToolFuncContext[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolFuncContext "ToolFuncContext



      module-attribute
   \(pydantic_ai.tools.ToolFuncContext\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)"), ToolParams[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolParams "ToolParams



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
    [ToolFuncContext[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolFuncContext "ToolFuncContext



      module-attribute
   \(pydantic_ai.tools.ToolFuncContext\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)"), ToolParams[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolParams "ToolParams



      module-attribute
   \(pydantic_ai.tools.ToolParams\)")]],
    ToolFuncContext[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolFuncContext "ToolFuncContext



      module-attribute
   \(pydantic_ai.tools.ToolFuncContext\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)"), ToolParams[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolParams "ToolParams



      module-attribute
   \(pydantic_ai.tools.ToolParams\)")],
]

```

```
tool(
    func: (
        ToolFuncContext[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolFuncContext "ToolFuncContext



      module-attribute
   \(pydantic_ai.tools.ToolFuncContext\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)"), ToolParams[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolParams "ToolParams



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

Decorator to register a tool function which takes [`RunContext`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext



      dataclass
  ") as its first argument.
Can decorate a sync or async functions.
The docstring is inspected to extract both the tool description and description of each parameter, [learn more](https://ai.pydantic.dev/tools/#function-tools-and-schema).
We can't add overloads for every possible signature of tool, since the return type is a recursive union so the signature of functions decorated with `@agent.tool` is obscured.
Example:
```
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

Parameters:
Name | Type | Description | Default
---|---|---|---
`func` |  `ToolFuncContext[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolFuncContext "ToolFuncContext



      module-attribute
   \(pydantic_ai.tools.ToolFuncContext\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)"), ToolParams[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolParams "ToolParams



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
   \(pydantic_ai.tools.ToolParams\)")] | None` |  custom method to validate tool arguments after schema validation has passed, before execution. The validator receives the already-validated and type-converted parameters, with `RunContext` as the first argument. Should raise [`ModelRetry`](https://ai.pydantic.dev/api/exceptions/#pydantic_ai.exceptions.ModelRetry "ModelRetry") on validation failure, return `None` on success. See [`ArgsValidatorFunc`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ArgsValidatorFunc "ArgsValidatorFunc



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
1183
1184
1185
1186
1187
1188
1189
1190
1191
1192
1193
1194
1195
1196
1197
1198
1199
1200
1201
1202
1203
1204
1205
1206
1207
1208
1209
1210
1211
1212
1213
1214
1215
1216
1217
1218
1219
1220
1221
1222
1223
1224
1225
1226
1227
1228
1229
1230
1231
1232
1233
1234
1235
1236
1237
1238
1239
1240
1241
1242
1243
1244
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
```
| ```
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
