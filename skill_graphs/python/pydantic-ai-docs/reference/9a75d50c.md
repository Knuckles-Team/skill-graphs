        on_startup=on_startup,
        on_shutdown=on_shutdown,
        lifespan=lifespan,
    )

```

---|---
####  to_a2a
```
to_a2a(
    *,
    storage: Storage[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.Storage "Storage \(fasta2a.storage.Storage\)") | None = None,
    broker: Broker[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.Broker "Broker



      dataclass
   \(fasta2a.broker.Broker\)") | None = None,
    name:  | None = None,
    url:  = "http://localhost:8000",
    version:  = "1.0.0",
    description:  | None = None,
    provider: AgentProvider[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.AgentProvider "AgentProvider \(fasta2a.schema.AgentProvider\)") | None = None,
    skills: [Skill[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.Skill "Skill \(fasta2a.schema.Skill\)")] | None = None,
    debug:  = False,
    routes: [Route] | None = None,
    middleware: [Middleware] | None = None,
    exception_handlers: (
        [, ExceptionHandler] | None
    ) = None,
    lifespan: Lifespan[FastA2A[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.FastA2A "FastA2A \(fasta2a.applications.FastA2A\)")] | None = None
) -> FastA2A[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.FastA2A "FastA2A \(fasta2a.applications.FastA2A\)")

```

Convert the agent to a FastA2A application.
Example:
```
from pydantic_ai import Agent

agent = Agent('openai:gpt-5.2')
app = agent.to_a2a()

```

The `app` is an ASGI application that can be used with any ASGI server.
To run the application, you can use the following command:
```
uvicorn app:app --host 0.0.0.0 --port 8000

```

Source code in `pydantic_ai_slim/pydantic_ai/agent/abstract.py`
```
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
1408
```
| ```
def to_a2a(
    self,
    *,
    storage: Storage | None = None,
    broker: Broker | None = None,
    # Agent card
    name: str | None = None,
    url: str = 'http://localhost:8000',
    version: str = '1.0.0',
    description: str | None = None,
    provider: AgentProvider | None = None,
    skills: list[Skill] | None = None,
    # Starlette
    debug: bool = False,
    routes: Sequence[Route] | None = None,
    middleware: Sequence[Middleware] | None = None,
    exception_handlers: dict[Any, ExceptionHandler] | None = None,
    lifespan: Lifespan[FastA2A] | None = None,
) -> FastA2A:
    """Convert the agent to a FastA2A application.

    Example:
```python
    from pydantic_ai import Agent

    agent = Agent('openai:gpt-5.2')
    app = agent.to_a2a()
```

    The `app` is an ASGI application that can be used with any ASGI server.

    To run the application, you can use the following command:

```bash
    uvicorn app:app --host 0.0.0.0 --port 8000
```
    """
    from .._a2a import agent_to_a2a

    return agent_to_a2a(
        self,
        storage=storage,
        broker=broker,
        name=name,
        url=url,
        version=version,
        description=description,
        provider=provider,
        skills=skills,
        debug=debug,
        routes=routes,
        middleware=middleware,
        exception_handlers=exception_handlers,
        lifespan=lifespan,
    )

```

---|---
####  to_cli `async`
```
to_cli(
    deps: AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)") = None,
    prog_name:  = "pydantic-ai",
    message_history: [ModelMessage[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelMessage "ModelMessage



      module-attribute
   \(pydantic_ai.messages.ModelMessage\)")] | None = None,
    model_settings: ModelSettings[](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings \(pydantic_ai.settings.ModelSettings\)") | None = None,
    usage_limits: UsageLimits[](https://ai.pydantic.dev/api/usage/#pydantic_ai.usage.UsageLimits "UsageLimits



      dataclass
   \(pydantic_ai.usage.UsageLimits\)") | None = None,
) -> None

```

Run the agent in a CLI chat interface.
Parameters:
Name | Type | Description | Default
---|---|---|---
`deps` |  `AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")` |  The dependencies to pass to the agent. |  `None`
`prog_name` |  |  The name of the program to use for the CLI. Defaults to 'pydantic-ai'. |  `'pydantic-ai'`
`message_history` |  `ModelMessage[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelMessage "ModelMessage



      module-attribute
   \(pydantic_ai.messages.ModelMessage\)")] | None` |  History of the conversation so far. |  `None`
`model_settings` |  `ModelSettings[](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings \(pydantic_ai.settings.ModelSettings\)") | None` |  Optional settings to use for this model's request. |  `None`
`usage_limits` |  `UsageLimits[](https://ai.pydantic.dev/api/usage/#pydantic_ai.usage.UsageLimits "UsageLimits



      dataclass
   \(pydantic_ai.usage.UsageLimits\)") | None` |  Optional limits on model request count or token usage. |  `None`
Example:
agent_to_cli.py```
from pydantic_ai import Agent

agent = Agent('openai:gpt-5.2', instructions='You always respond in Italian.')

async def main():
    await agent.to_cli()

```

Source code in `pydantic_ai_slim/pydantic_ai/agent/abstract.py`
```
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
```
| ```
async def to_cli(
    self: Self,
    deps: AgentDepsT = None,
    prog_name: str = 'pydantic-ai',
    message_history: Sequence[_messages.ModelMessage] | None = None,
    model_settings: ModelSettings | None = None,
    usage_limits: _usage.UsageLimits | None = None,
) -> None:
    """Run the agent in a CLI chat interface.

    Args:
        deps: The dependencies to pass to the agent.
        prog_name: The name of the program to use for the CLI. Defaults to 'pydantic-ai'.
        message_history: History of the conversation so far.
        model_settings: Optional settings to use for this model's request.
        usage_limits: Optional limits on model request count or token usage.

    Example:
```python {title="agent_to_cli.py" test="skip"}
    from pydantic_ai import Agent

    agent = Agent('openai:gpt-5.2', instructions='You always respond in Italian.')

    async def main():
        await agent.to_cli()
```
    """
    from rich.console import Console

    from pydantic_ai._cli import run_chat

    await run_chat(
        stream=True,
        agent=self,
        deps=deps,
        console=Console(),
        code_theme='monokai',
        prog_name=prog_name,
        message_history=message_history,
        model_settings=model_settings,
        usage_limits=usage_limits,
    )

```

---|---
####  to_cli_sync
```
to_cli_sync(
    deps: AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)") = None,
    prog_name:  = "pydantic-ai",
    message_history: [ModelMessage[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelMessage "ModelMessage



      module-attribute
   \(pydantic_ai.messages.ModelMessage\)")] | None = None,
    model_settings: ModelSettings[](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings \(pydantic_ai.settings.ModelSettings\)") | None = None,
    usage_limits: UsageLimits[](https://ai.pydantic.dev/api/usage/#pydantic_ai.usage.UsageLimits "UsageLimits



      dataclass
   \(pydantic_ai.usage.UsageLimits\)") | None = None,
) -> None

```

Run the agent in a CLI chat interface with the non-async interface.
Parameters:
Name | Type | Description | Default
---|---|---|---
`deps` |  `AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")` |  The dependencies to pass to the agent. |  `None`
`prog_name` |  |  The name of the program to use for the CLI. Defaults to 'pydantic-ai'. |  `'pydantic-ai'`
`message_history` |  `ModelMessage[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelMessage "ModelMessage



      module-attribute
   \(pydantic_ai.messages.ModelMessage\)")] | None` |  History of the conversation so far. |  `None`
`model_settings` |  `ModelSettings[](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings \(pydantic_ai.settings.ModelSettings\)") | None` |  Optional settings to use for this model's request. |  `None`
`usage_limits` |  `UsageLimits[](https://ai.pydantic.dev/api/usage/#pydantic_ai.usage.UsageLimits "UsageLimits



      dataclass
   \(pydantic_ai.usage.UsageLimits\)") | None` |  Optional limits on model request count or token usage. |  `None`
agent_to_cli_sync.py```
from pydantic_ai import Agent

agent = Agent('openai:gpt-5.2', instructions='You always respond in Italian.')
agent.to_cli_sync()
agent.to_cli_sync(prog_name='assistant')

```

Source code in `pydantic_ai_slim/pydantic_ai/agent/abstract.py`
```
1453
1454
1455
1456
1457
1458
1459
1460
1461
1462
1463
1464
1465
1466
1467
1468
1469
1470
1471
1472
1473
1474
1475
1476
1477
1478
1479
1480
1481
1482
1483
1484
1485
1486
```
| ```
def to_cli_sync(
    self: Self,
    deps: AgentDepsT = None,
    prog_name: str = 'pydantic-ai',
    message_history: Sequence[_messages.ModelMessage] | None = None,
    model_settings: ModelSettings | None = None,
    usage_limits: _usage.UsageLimits | None = None,
) -> None:
    """Run the agent in a CLI chat interface with the non-async interface.

    Args:
        deps: The dependencies to pass to the agent.
        prog_name: The name of the program to use for the CLI. Defaults to 'pydantic-ai'.
        message_history: History of the conversation so far.
        model_settings: Optional settings to use for this model's request.
        usage_limits: Optional limits on model request count or token usage.

```python {title="agent_to_cli_sync.py" test="skip"}
    from pydantic_ai import Agent

    agent = Agent('openai:gpt-5.2', instructions='You always respond in Italian.')
    agent.to_cli_sync()
    agent.to_cli_sync(prog_name='assistant')
```
    """
    return _utils.get_event_loop().run_until_complete(
        self.to_cli(
            deps=deps,
            prog_name=prog_name,
            message_history=message_history,
            model_settings=model_settings,
            usage_limits=usage_limits,
        )
    )

```

---|---
###  WrapperAgent
Bases: `AbstractAgent[](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AbstractAgent "AbstractAgent \(pydantic_ai.agent.abstract.AbstractAgent\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)"), OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")]`
Agent which wraps another agent.
Does nothing on its own, used as a base class.
Source code in `pydantic_ai_slim/pydantic_ai/agent/wrapper.py`
```
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
139
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
248
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
```
| ```
class WrapperAgent(AbstractAgent[AgentDepsT, OutputDataT]):
    """Agent which wraps another agent.

    Does nothing on its own, used as a base class.
    """

    def __init__(self, wrapped: AbstractAgent[AgentDepsT, OutputDataT]):
        self.wrapped = wrapped

    @property
    def model(self) -> models.Model | models.KnownModelName | str | None:
        return self.wrapped.model

    @property
    def name(self) -> str | None:
        return self.wrapped.name

    @name.setter
    def name(self, value: str | None) -> None:
        self.wrapped.name = value

    @property
    def deps_type(self) -> type:
        return self.wrapped.deps_type

    @property
    def output_type(self) -> OutputSpec[OutputDataT]:
        return self.wrapped.output_type

    @property
    def event_stream_handler(self) -> EventStreamHandler[AgentDepsT] | None:
        return self.wrapped.event_stream_handler

    @property
    def toolsets(self) -> Sequence[AbstractToolset[AgentDepsT]]:
        return self.wrapped.toolsets

    async def __aenter__(self) -> AbstractAgent[AgentDepsT, OutputDataT]:
        return await self.wrapped.__aenter__()

    async def __aexit__(self, *args: Any) -> bool | None:
        return await self.wrapped.__aexit__(*args)

    def output_json_schema(self, output_type: OutputSpec[OutputDataT | RunOutputDataT] | None = None) -> JsonSchema:
        return self.wrapped.output_json_schema(output_type=output_type)

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
            metadata: Optional metadata to attach to this run.
            infer_name: Whether to try to infer the agent name from the call frame if it's not set.
            toolsets: Optional additional toolsets for this run.
            builtin_tools: Optional additional builtin tools for this run.

        Returns:
            The result of the run.
        """
        async with self.wrapped.iter(
            user_prompt=user_prompt,
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
            infer_name=infer_name,
            toolsets=toolsets,
            builtin_tools=builtin_tools,
        ) as run:
            yield run

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
        with self.wrapped.override(
            name=name,
            deps=deps,
            model=model,
            toolsets=toolsets,
            tools=tools,
            instructions=instructions,
        ):
            yield

```

---|---
####  iter `async`
```
iter(
    user_prompt:  | [UserContent] | None = None,
    *,
    output_type: None = None,
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
    instructions: Instructions[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")] = None,
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
    metadata: AgentMetadata[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")] | None = None,
    infer_name:  = True,
    toolsets: (
        [AbstractToolset[](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.AbstractToolset "AbstractToolset \(pydantic_ai.toolsets.AbstractToolset\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]] | None
    ) = None,
    builtin_tools: (
        [
            AbstractBuiltinTool[](https://ai.pydantic.dev/api/builtin_tools/#pydantic_ai.builtin_tools.AbstractBuiltinTool "AbstractBuiltinTool
