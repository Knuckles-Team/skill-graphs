```
command:  = command

```

The command to run.
####  args `instance-attribute`
```
args: [] = args

```

The arguments to pass to the command.
####  env `instance-attribute`
```
env: [, ] | None = env

```

The environment variables the CLI server will have access to.
By default the subprocess will not inherit any environment variables from the parent process. If you want to inherit the environment variables from the parent process, use `env=os.environ`.
####  cwd `instance-attribute`
```
cwd:  |  | None = cwd

```

The working directory to use when spawning the process.
###  MCPServerSSE
Bases: `_MCPServerHTTP`
An MCP server that connects over streamable HTTP connections.
This class implements the SSE transport from the MCP specification. See
Note
Using this class as an async context manager will create a new pool of HTTP connections to connect to a server which should already be running.
Example:
```
from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerSSE

server = MCPServerSSE('http://localhost:3001/sse')
agent = Agent('openai:gpt-5.2', toolsets=[server])

```

Source code in `pydantic_ai_slim/pydantic_ai/mcp.py`
```
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
1159
1160
1161
1162
1163
1164
1165
1166
1167
1168
1169
1170
1171
1172
1173
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
```
| ```
class MCPServerSSE(_MCPServerHTTP):
    """An MCP server that connects over streamable HTTP connections.

    This class implements the SSE transport from the MCP specification.
    See <https://spec.modelcontextprotocol.io/specification/2024-11-05/basic/transports/#http-with-sse> for more information.

    !!! note
        Using this class as an async context manager will create a new pool of HTTP connections to connect
        to a server which should already be running.

    Example:
```python {py="3.10"}
    from pydantic_ai import Agent
    from pydantic_ai.mcp import MCPServerSSE

    server = MCPServerSSE('http://localhost:3001/sse')
    agent = Agent('openai:gpt-5.2', toolsets=[server])
```
    """

    @classmethod
    def __get_pydantic_core_schema__(cls, _: Any, __: Any) -> CoreSchema:
        return core_schema.no_info_after_validator_function(
            lambda dct: MCPServerSSE(**dct),
            core_schema.typed_dict_schema(
                {
                    'url': core_schema.typed_dict_field(core_schema.str_schema()),
                    'headers': core_schema.typed_dict_field(
                        core_schema.dict_schema(core_schema.str_schema(), core_schema.str_schema()), required=False
                    ),
                }
            ),
        )

    # sse_client has a hang bug (https://github.com/modelcontextprotocol/python-sdk/issues/1811)
    # that prevents testing SSE transport in CI.
    # TODO: Remove pragma and add a test
    # once https://github.com/modelcontextprotocol/python-sdk/pull/1838 is released.
    @asynccontextmanager
    async def client_streams(  # pragma: no cover
        self,
    ) -> AsyncIterator[
        tuple[
            MemoryObjectReceiveStream[SessionMessage | Exception],
            MemoryObjectSendStream[SessionMessage],
        ]
    ]:
        if self.http_client and self.headers:
            raise ValueError('`http_client` is mutually exclusive with `headers`.')

        if self.http_client is not None:

            def httpx_client_factory(
                headers: dict[str, str] | None = None,
                timeout: httpx.Timeout | None = None,
                auth: httpx.Auth | None = None,
            ) -> httpx.AsyncClient:
                assert self.http_client is not None
                return self.http_client

            async with sse_client(
                url=self.url,
                timeout=self.timeout,
                sse_read_timeout=self.read_timeout,
                httpx_client_factory=httpx_client_factory,
            ) as (read_stream, write_stream, *_):
                yield read_stream, write_stream
        else:
            async with sse_client(
                url=self.url,
                timeout=self.timeout,
                sse_read_timeout=self.read_timeout,
                headers=self.headers,
            ) as (read_stream, write_stream, *_):
                yield read_stream, write_stream

    def __eq__(self, value: object, /) -> bool:
        return super().__eq__(value) and isinstance(value, MCPServerSSE) and self.url == value.url

```

---|---
###  MCPServerHTTP `deprecated`
Bases: `MCPServerSSE[](https://ai.pydantic.dev/api/mcp/#pydantic_ai.mcp.MCPServerSSE "MCPServerSSE \(pydantic_ai.mcp.MCPServerSSE\)")`
Deprecated
The `MCPServerHTTP` class is deprecated, use `MCPServerSSE` instead.
An MCP server that connects over HTTP using the old SSE transport.
This class implements the SSE transport from the MCP specification. See
Note
Using this class as an async context manager will create a new pool of HTTP connections to connect to a server which should already be running.
Example:
```
from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerHTTP

server = MCPServerHTTP('http://localhost:3001/sse')
agent = Agent('openai:gpt-5.2', toolsets=[server])

```

Source code in `pydantic_ai_slim/pydantic_ai/mcp.py`
```
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
```
| ```
@deprecated('The `MCPServerHTTP` class is deprecated, use `MCPServerSSE` instead.')
class MCPServerHTTP(MCPServerSSE):
    """An MCP server that connects over HTTP using the old SSE transport.

    This class implements the SSE transport from the MCP specification.
    See <https://spec.modelcontextprotocol.io/specification/2024-11-05/basic/transports/#http-with-sse> for more information.

    !!! note
        Using this class as an async context manager will create a new pool of HTTP connections to connect
        to a server which should already be running.

    Example:
```python {py="3.10" test="skip"}
    from pydantic_ai import Agent
    from pydantic_ai.mcp import MCPServerHTTP

    server = MCPServerHTTP('http://localhost:3001/sse')
    agent = Agent('openai:gpt-5.2', toolsets=[server])
```
    """

```

---|---
###  MCPServerStreamableHTTP
Bases: `_MCPServerHTTP`
An MCP server that connects over HTTP using the Streamable HTTP transport.
This class implements the Streamable HTTP transport from the MCP specification. See
Note
Using this class as an async context manager will create a new pool of HTTP connections to connect to a server which should already be running.
Example:
```
from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerStreamableHTTP

server = MCPServerStreamableHTTP('http://localhost:8000/mcp')
agent = Agent('openai:gpt-5.2', toolsets=[server])

```

Source code in `pydantic_ai_slim/pydantic_ai/mcp.py`
```
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
1284
1285
1286
```
| ```
class MCPServerStreamableHTTP(_MCPServerHTTP):
    """An MCP server that connects over HTTP using the Streamable HTTP transport.

    This class implements the Streamable HTTP transport from the MCP specification.
    See <https://modelcontextprotocol.io/introduction#streamable-http> for more information.

    !!! note
        Using this class as an async context manager will create a new pool of HTTP connections to connect
        to a server which should already be running.

    Example:
```python {py="3.10"}
    from pydantic_ai import Agent
    from pydantic_ai.mcp import MCPServerStreamableHTTP

    server = MCPServerStreamableHTTP('http://localhost:8000/mcp')
    agent = Agent('openai:gpt-5.2', toolsets=[server])
```
    """

    @classmethod
    def __get_pydantic_core_schema__(cls, _: Any, __: Any) -> CoreSchema:
        return core_schema.no_info_after_validator_function(
            lambda dct: MCPServerStreamableHTTP(**dct),
            core_schema.typed_dict_schema(
                {
                    'url': core_schema.typed_dict_field(core_schema.str_schema()),
                    'headers': core_schema.typed_dict_field(
                        core_schema.dict_schema(core_schema.str_schema(), core_schema.str_schema()), required=False
                    ),
                }
            ),
        )

    @asynccontextmanager
    async def client_streams(
        self,
    ) -> AsyncIterator[
        tuple[
            MemoryObjectReceiveStream[SessionMessage | Exception],
            MemoryObjectSendStream[SessionMessage],
        ]
    ]:
        if self.http_client and self.headers:
            raise ValueError('`http_client` is mutually exclusive with `headers`.')

        aexit_stack = AsyncExitStack()
        http_client = self.http_client or await aexit_stack.enter_async_context(
            httpx.AsyncClient(timeout=httpx.Timeout(self.timeout, read=self.read_timeout), headers=self.headers)
        )
        read_stream, write_stream, *_ = await aexit_stack.enter_async_context(
            streamable_http_client(self.url, http_client=http_client)
        )
        try:
            yield read_stream, write_stream
        finally:
            await aexit_stack.aclose()

    def __eq__(self, value: object, /) -> bool:
        return super().__eq__(value) and isinstance(value, MCPServerStreamableHTTP) and self.url == value.url

```

---|---
###  ToolResult `module-attribute`
```
ToolResult = (

    | BinaryContent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent "BinaryContent \(pydantic_ai.messages.BinaryContent\)")
    | [, ]
    | []
    | [
         | BinaryContent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent "BinaryContent \(pydantic_ai.messages.BinaryContent\)") | [, ] | []
    ]
)

```

The result type of an MCP tool call.
###  CallToolFunc `module-attribute`
```
CallToolFunc = [
    [, [, ], [, ] | None],
    [ToolResult[](https://ai.pydantic.dev/api/mcp/#pydantic_ai.mcp.ToolResult "ToolResult



      module-attribute
   \(pydantic_ai.mcp.ToolResult\)")],
]

```

A function type that represents a tool call.
###  ProcessToolCallback `module-attribute`
```
ProcessToolCallback = [
    [RunContext[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext



      dataclass
   \(pydantic_ai.tools.RunContext\)")[], CallToolFunc[](https://ai.pydantic.dev/api/mcp/#pydantic_ai.mcp.CallToolFunc "CallToolFunc



      module-attribute
   \(pydantic_ai.mcp.CallToolFunc\)"), , [, ]],
    [ToolResult[](https://ai.pydantic.dev/api/mcp/#pydantic_ai.mcp.ToolResult "ToolResult



      module-attribute
   \(pydantic_ai.mcp.ToolResult\)")],
]

```

A process tool callback.
It accepts a run context, the original tool call function, a tool name, and arguments.
Allows wrapping an MCP server tool call to customize it, including adding extra request metadata.
###  MCPServerConfig
Bases: `BaseModel[](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel "pydantic.BaseModel")`
Configuration for MCP servers.
Source code in `pydantic_ai_slim/pydantic_ai/mcp.py`
```
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
```
| ```
class MCPServerConfig(BaseModel):
    """Configuration for MCP servers."""

    mcp_servers: Annotated[
        dict[
            str,
            Annotated[
                Annotated[MCPServerStdio, Tag('stdio')]
                | Annotated[MCPServerStreamableHTTP, Tag('streamable-http')]
                | Annotated[MCPServerSSE, Tag('sse')],
                Discriminator(_mcp_server_discriminator),
            ],
        ],
        Field(alias='mcpServers'),
    ]

```

---|---
###  load_mcp_servers
```
load_mcp_servers(
    config_path:  | ,
) -> [
    MCPServerStdio[](https://ai.pydantic.dev/api/mcp/#pydantic_ai.mcp.MCPServerStdio "MCPServerStdio \(pydantic_ai.mcp.MCPServerStdio\)") | MCPServerStreamableHTTP[](https://ai.pydantic.dev/api/mcp/#pydantic_ai.mcp.MCPServerStreamableHTTP "MCPServerStreamableHTTP \(pydantic_ai.mcp.MCPServerStreamableHTTP\)") | MCPServerSSE[](https://ai.pydantic.dev/api/mcp/#pydantic_ai.mcp.MCPServerSSE "MCPServerSSE \(pydantic_ai.mcp.MCPServerSSE\)")
]

```

Load MCP servers from a configuration file.
Environment variables can be referenced in the configuration file using: - `${VAR_NAME}` syntax - expands to the value of VAR_NAME, raises error if not defined - `${VAR_NAME:-default}` syntax - expands to VAR_NAME if set, otherwise uses the default value
Parameters:
Name | Type | Description | Default
---|---|---|---
`config_path` |  |  The path to the configuration file. |  _required_
Returns:
Type | Description
---|---
`MCPServerStdio[](https://ai.pydantic.dev/api/mcp/#pydantic_ai.mcp.MCPServerStdio "MCPServerStdio \(pydantic_ai.mcp.MCPServerStdio\)") | MCPServerStreamableHTTP[](https://ai.pydantic.dev/api/mcp/#pydantic_ai.mcp.MCPServerStreamableHTTP "MCPServerStreamableHTTP \(pydantic_ai.mcp.MCPServerStreamableHTTP\)") | MCPServerSSE[](https://ai.pydantic.dev/api/mcp/#pydantic_ai.mcp.MCPServerSSE "MCPServerSSE \(pydantic_ai.mcp.MCPServerSSE\)")]` |  A list of MCP servers.
Raises:
Type | Description
---|---
|  If the configuration file does not exist.
`ValidationError` |  If the configuration file does not match the schema.
|  If an environment variable referenced in the configuration is not defined and no default value is provided.
Source code in `pydantic_ai_slim/pydantic_ai/mcp.py`
```
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
1408
1409
1410
1411
1412
1413
1414
1415
1416
1417
1418
1419
1420
1421
```
| ```
def load_mcp_servers(config_path: str | Path) -> list[MCPServerStdio | MCPServerStreamableHTTP | MCPServerSSE]:
    """Load MCP servers from a configuration file.

    Environment variables can be referenced in the configuration file using:
    - `${VAR_NAME}` syntax - expands to the value of VAR_NAME, raises error if not defined
    - `${VAR_NAME:-default}` syntax - expands to VAR_NAME if set, otherwise uses the default value

    Args:
        config_path: The path to the configuration file.

    Returns:
        A list of MCP servers.

    Raises:
        FileNotFoundError: If the configuration file does not exist.
        ValidationError: If the configuration file does not match the schema.
        ValueError: If an environment variable referenced in the configuration is not defined and no default value is provided.
    """
    config_path = Path(config_path)

    if not config_path.exists():
        raise FileNotFoundError(f'Config file {config_path} not found')

    config_data = pydantic_core.from_json(config_path.read_bytes())
    expanded_config_data = _expand_env_vars(config_data)
    config = MCPServerConfig.model_validate(expanded_config_data)

    servers: list[MCPServerStdio | MCPServerStreamableHTTP | MCPServerSSE] = []
    for name, server in config.mcp_servers.items():
        server.id = name
        server.tool_prefix = name
        servers.append(server)

    return servers

```

---|---
© Pydantic Services Inc. 2024 to present
