    history_processors: (
        [HistoryProcessor[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]] | None
    ) = None,
    event_stream_handler: (
        EventStreamHandler[](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.EventStreamHandler "EventStreamHandler



      module-attribute
   \(pydantic_ai.agent.abstract.EventStreamHandler\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")] | None
    ) = None,
    tool_timeout:  | None = None,
    max_concurrency: AnyConcurrencyLimit[](https://ai.pydantic.dev/api/concurrency/#pydantic_ai.AnyConcurrencyLimit "pydantic_ai.concurrency.AnyConcurrencyLimit") = None,
    **_deprecated_kwargs:
)

```

Create an agent.
Parameters:
Name | Type | Description | Default
---|---|---|---
`model` |  `Model[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.Model "Model \(pydantic_ai.models.Model\)") | KnownModelName[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.KnownModelName "KnownModelName



      module-attribute
   \(pydantic_ai.models.KnownModelName\)") | ` |  The default model to use for this agent, if not provided, you must provide the model when calling it. We allow `str` here since the actual list of allowed models changes frequently. |  `None`
`output_type` |  `OutputSpec[OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")]` |  The type of the output data, used to validate the data returned by the model, defaults to `str`. |
`instructions` |  `Instructions[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]` |  Instructions to use for this agent, you can also register instructions via a function with [`instructions`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.instructions "instructions") or pass additional, temporary, instructions when executing a run. |  `None`
`system_prompt` |  |  Static system prompts to use for this agent, you can also register system prompts via a function with [`system_prompt`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.system_prompt "system_prompt"). |  `()`
`deps_type` |  `AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]` |  The type used for dependency injection, this parameter exists solely to allow you to fully parameterize the agent, and therefore get the best out of static type checking. If you're not using deps, but want type checking to pass, you can set `deps=None` to satisfy Pyright or add a type hint `: Agent[None, <return type>]`. |  `NoneType`
`name` |  |  The name of the agent, used for logging. If `None`, we try to infer the agent name from the call frame when the agent is first run. |  `None`
`model_settings` |  `ModelSettings[](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings \(pydantic_ai.settings.ModelSettings\)") | None` |  Optional model request settings to use for this agent's runs, by default. |  `None`
`retries` |  |  The default number of retries to allow for tool calls and output validation, before raising an error. For model request retries, see the [HTTP Request Retries](https://ai.pydantic.dev/retries/) documentation. |  `1`
`validation_context` |  `RunContext[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext



      dataclass
   \(pydantic_ai.tools.RunContext\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]], ` |  Pydantic [validation context](https://docs.pydantic.dev/latest/concepts/validators/#validation-context) used to validate tool arguments and outputs. |  `None`
`output_retries` |  |  The maximum number of retries to allow for output validation, defaults to `retries`. |  `None`
`tools` |  `Tool[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.Tool "Tool



      dataclass
   \(pydantic_ai.tools.Tool\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")] | ToolFuncEither[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolFuncEither "ToolFuncEither



      module-attribute
   \(pydantic_ai.tools.ToolFuncEither\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)"), ...]]` |  Tools to register with the agent, you can also register tools via the decorators [`@agent.tool`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.tool "tool") and [`@agent.tool_plain`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.tool_plain "tool_plain"). |  `()`
`builtin_tools` |  `AbstractBuiltinTool[](https://ai.pydantic.dev/api/builtin_tools/#pydantic_ai.builtin_tools.AbstractBuiltinTool "AbstractBuiltinTool



      dataclass
   \(pydantic_ai.builtin_tools.AbstractBuiltinTool\)") | BuiltinToolFunc[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.BuiltinToolFunc "BuiltinToolFunc



      module-attribute
   \(pydantic_ai.tools.BuiltinToolFunc\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]]` |  The builtin tools that the agent will use. This depends on the model, as some models may not support certain tools. If the model doesn't support the builtin tools, an error will be raised. |  `()`
`prepare_tools` |  `ToolsPrepareFunc[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolsPrepareFunc "ToolsPrepareFunc



      module-attribute
   \(pydantic_ai.tools.ToolsPrepareFunc\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")] | None` |  Custom function to prepare the tool definition of all tools for each step, except output tools. This is useful if you want to customize the definition of multiple tools or you want to register a subset of tools for a given step. See [`ToolsPrepareFunc`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolsPrepareFunc "ToolsPrepareFunc



      module-attribute
  ") |  `None`
`prepare_output_tools` |  `ToolsPrepareFunc[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolsPrepareFunc "ToolsPrepareFunc



      module-attribute
   \(pydantic_ai.tools.ToolsPrepareFunc\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")] | None` |  Custom function to prepare the tool definition of all output tools for each step. This is useful if you want to customize the definition of multiple output tools or you want to register a subset of output tools for a given step. See [`ToolsPrepareFunc`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolsPrepareFunc "ToolsPrepareFunc



      module-attribute
  ") |  `None`
`toolsets` |  `AbstractToolset[](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.AbstractToolset "AbstractToolset \(pydantic_ai.toolsets.AbstractToolset\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")] | ToolsetFunc[](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.ToolsetFunc "ToolsetFunc



      module-attribute
   \(pydantic_ai.toolsets._dynamic.ToolsetFunc\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]] | None` |  Toolsets to register with the agent, including MCP servers and functions which take a run context and return a toolset. See [`ToolsetFunc`](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.ToolsetFunc "ToolsetFunc



      module-attribute
  ") for more information. |  `None`
`defer_model_check` |  |  by default, if you provide a [named](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.KnownModelName "KnownModelName



      module-attribute
  ") model, it's evaluated to create a [`Model`](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.Model "Model") instance immediately, which checks for the necessary environment variables. Set this to `false` to defer the evaluation until the first run. Useful if you want to [override the model](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.override "override") for testing. |  `False`
`end_strategy` |  `EndStrategy[](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.EndStrategy "EndStrategy



      module-attribute
   \(pydantic_ai._agent_graph.EndStrategy\)")` |  Strategy for handling tool calls that are requested alongside a final result. See [`EndStrategy`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.EndStrategy "EndStrategy



      module-attribute
  ") for more information. |  `'early'`
`instrument` |  `InstrumentationSettings[](https://ai.pydantic.dev/api/models/instrumented/#pydantic_ai.models.instrumented.InstrumentationSettings "InstrumentationSettings



      dataclass
   \(pydantic_ai.models.instrumented.InstrumentationSettings\)") | ` |  Set to True to automatically instrument with OpenTelemetry, which will use Logfire if it's configured. Set to an instance of [`InstrumentationSettings`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.InstrumentationSettings "InstrumentationSettings



      dataclass
  ") to customize. If this isn't set, then the last value set by [`Agent.instrument_all()`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.instrument_all "instrument_all



      staticmethod
  ") will be used, which defaults to False. See the [Debugging and Monitoring guide](https://ai.pydantic.dev/logfire/) for more info. |  `None`
`metadata` |  `AgentMetadata[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")] | None` |  Optional metadata to store with each run. Provide a dictionary of primitives, or a callable returning one computed from the [`RunContext`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext



      dataclass
  ") on each run. Metadata is resolved when a run starts and recomputed after a successful run finishes so it can reflect the final state. Resolved metadata can be read after the run completes via [`AgentRun.metadata`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AgentRun "AgentRun



      dataclass
  "), [`AgentRunResult.metadata`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AgentRunResult "AgentRunResult



      dataclass
  "), and [`StreamedRunResult.metadata`](https://ai.pydantic.dev/api/result/#pydantic_ai.result.StreamedRunResult "StreamedRunResult



      dataclass
  "), and is attached to the agent run span when instrumentation is enabled. |  `None`
`history_processors` |  `HistoryProcessor[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")]] | None` |  Optional list of callables to process the message history before sending it to the model. Each processor takes a list of messages and returns a modified list of messages. Processors can be sync or async and are applied in sequence. |  `None`
`event_stream_handler` |  `EventStreamHandler[](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.EventStreamHandler "EventStreamHandler



      module-attribute
   \(pydantic_ai.agent.abstract.EventStreamHandler\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")] | None` |  Optional handler for events from the model's streaming response and the agent's execution of tools. |  `None`
`tool_timeout` |  |  Default timeout in seconds for tool execution. If a tool takes longer than this, the tool is considered to have failed and a retry prompt is returned to the model (counting towards the retry limit). Individual tools can override this with their own timeout. Defaults to None (no timeout). |  `None`
`max_concurrency` |  `AnyConcurrencyLimit[](https://ai.pydantic.dev/api/concurrency/#pydantic_ai.AnyConcurrencyLimit "pydantic_ai.concurrency.AnyConcurrencyLimit")` |  Optional limit on concurrent agent runs. Can be an integer for simple limiting, a [`ConcurrencyLimit`](https://ai.pydantic.dev/api/concurrency/#pydantic_ai.ConcurrencyLimit) for advanced configuration with backpressure, a [`ConcurrencyLimiter`](https://ai.pydantic.dev/api/concurrency/#pydantic_ai.ConcurrencyLimiter) for sharing limits across multiple agents, or None (default) for no limiting. When the limit is reached, additional calls to `run()` or `iter()` will wait until a slot becomes available. |  `None`
Source code in `pydantic_ai_slim/pydantic_ai/agent/__init__.py`
```
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
340
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
354
355
356
357
358
359
360
361
362
363
364
365
366
367
368
369
370
371
372
373
374
375
376
377
378
379
380
381
382
383
384
385
386
387
388
389
390
391
392
393
394
395
396
397
398
399
400
401
402
403
404
405
406
407
408
409
410
411
412
413
414
415
416
417
418
419
```
| ```
def __init__(
    self,
    model: models.Model | models.KnownModelName | str | None = None,
    *,
    output_type: OutputSpec[OutputDataT] = str,
    instructions: Instructions[AgentDepsT] = None,
    system_prompt: str | Sequence[str] = (),
    deps_type: type[AgentDepsT] = NoneType,
    name: str | None = None,
    model_settings: ModelSettings | None = None,
    retries: int = 1,
    validation_context: Any | Callable[[RunContext[AgentDepsT]], Any] = None,
    output_retries: int | None = None,
    tools: Sequence[Tool[AgentDepsT] | ToolFuncEither[AgentDepsT, ...]] = (),
    builtin_tools: Sequence[AbstractBuiltinTool | BuiltinToolFunc[AgentDepsT]] = (),
    prepare_tools: ToolsPrepareFunc[AgentDepsT] | None = None,
    prepare_output_tools: ToolsPrepareFunc[AgentDepsT] | None = None,
    toolsets: Sequence[AbstractToolset[AgentDepsT] | ToolsetFunc[AgentDepsT]] | None = None,
    defer_model_check: bool = False,
    end_strategy: EndStrategy = 'early',
    instrument: InstrumentationSettings | bool | None = None,
    metadata: AgentMetadata[AgentDepsT] | None = None,
    history_processors: Sequence[HistoryProcessor[AgentDepsT]] | None = None,
    event_stream_handler: EventStreamHandler[AgentDepsT] | None = None,
    tool_timeout: float | None = None,
    max_concurrency: _concurrency.AnyConcurrencyLimit = None,
    **_deprecated_kwargs: Any,
):
    """Create an agent.

    Args:
        model: The default model to use for this agent, if not provided,
            you must provide the model when calling it. We allow `str` here since the actual list of allowed models changes frequently.
        output_type: The type of the output data, used to validate the data returned by the model,
            defaults to `str`.
        instructions: Instructions to use for this agent, you can also register instructions via a function with
            [`instructions`][pydantic_ai.agent.Agent.instructions] or pass additional, temporary, instructions when executing a run.
        system_prompt: Static system prompts to use for this agent, you can also register system
            prompts via a function with [`system_prompt`][pydantic_ai.agent.Agent.system_prompt].
        deps_type: The type used for dependency injection, this parameter exists solely to allow you to fully
            parameterize the agent, and therefore get the best out of static type checking.
            If you're not using deps, but want type checking to pass, you can set `deps=None` to satisfy Pyright
            or add a type hint `: Agent[None, <return type>]`.
        name: The name of the agent, used for logging. If `None`, we try to infer the agent name from the call frame
            when the agent is first run.
        model_settings: Optional model request settings to use for this agent's runs, by default.
        retries: The default number of retries to allow for tool calls and output validation, before raising an error.
            For model request retries, see the [HTTP Request Retries](../retries.md) documentation.
        validation_context: Pydantic [validation context](https://docs.pydantic.dev/latest/concepts/validators/#validation-context) used to validate tool arguments and outputs.
        output_retries: The maximum number of retries to allow for output validation, defaults to `retries`.
        tools: Tools to register with the agent, you can also register tools via the decorators
            [`@agent.tool`][pydantic_ai.agent.Agent.tool] and [`@agent.tool_plain`][pydantic_ai.agent.Agent.tool_plain].
        builtin_tools: The builtin tools that the agent will use. This depends on the model, as some models may not
            support certain tools. If the model doesn't support the builtin tools, an error will be raised.
        prepare_tools: Custom function to prepare the tool definition of all tools for each step, except output tools.
            This is useful if you want to customize the definition of multiple tools or you want to register
            a subset of tools for a given step. See [`ToolsPrepareFunc`][pydantic_ai.tools.ToolsPrepareFunc]
        prepare_output_tools: Custom function to prepare the tool definition of all output tools for each step.
            This is useful if you want to customize the definition of multiple output tools or you want to register
            a subset of output tools for a given step. See [`ToolsPrepareFunc`][pydantic_ai.tools.ToolsPrepareFunc]
        toolsets: Toolsets to register with the agent, including MCP servers and functions which take a run context
            and return a toolset. See [`ToolsetFunc`][pydantic_ai.toolsets.ToolsetFunc] for more information.
        defer_model_check: by default, if you provide a [named][pydantic_ai.models.KnownModelName] model,
            it's evaluated to create a [`Model`][pydantic_ai.models.Model] instance immediately,
            which checks for the necessary environment variables. Set this to `false`
            to defer the evaluation until the first run. Useful if you want to
            [override the model][pydantic_ai.agent.Agent.override] for testing.
        end_strategy: Strategy for handling tool calls that are requested alongside a final result.
            See [`EndStrategy`][pydantic_ai.agent.EndStrategy] for more information.
        instrument: Set to True to automatically instrument with OpenTelemetry,
            which will use Logfire if it's configured.
            Set to an instance of [`InstrumentationSettings`][pydantic_ai.agent.InstrumentationSettings] to customize.
            If this isn't set, then the last value set by
            [`Agent.instrument_all()`][pydantic_ai.agent.Agent.instrument_all]
            will be used, which defaults to False.
            See the [Debugging and Monitoring guide](https://ai.pydantic.dev/logfire/) for more info.
        metadata: Optional metadata to store with each run.
            Provide a dictionary of primitives, or a callable returning one
            computed from the [`RunContext`][pydantic_ai.tools.RunContext] on each run.
            Metadata is resolved when a run starts and recomputed after a successful run finishes so it
            can reflect the final state.
            Resolved metadata can be read after the run completes via
            [`AgentRun.metadata`][pydantic_ai.agent.AgentRun],
            [`AgentRunResult.metadata`][pydantic_ai.agent.AgentRunResult], and
            [`StreamedRunResult.metadata`][pydantic_ai.result.StreamedRunResult],
            and is attached to the agent run span when instrumentation is enabled.
        history_processors: Optional list of callables to process the message history before sending it to the model.
            Each processor takes a list of messages and returns a modified list of messages.
            Processors can be sync or async and are applied in sequence.
        event_stream_handler: Optional handler for events from the model's streaming response and the agent's execution of tools.
        tool_timeout: Default timeout in seconds for tool execution. If a tool takes longer than this,
            the tool is considered to have failed and a retry prompt is returned to the model (counting towards the retry limit).
            Individual tools can override this with their own timeout. Defaults to None (no timeout).
        max_concurrency: Optional limit on concurrent agent runs. Can be an integer for simple limiting,
            a [`ConcurrencyLimit`][pydantic_ai.ConcurrencyLimit] for advanced configuration with backpressure,
            a [`ConcurrencyLimiter`][pydantic_ai.ConcurrencyLimiter] for sharing limits across
            multiple agents, or None (default) for no limiting. When the limit is reached, additional calls
            to `run()` or `iter()` will wait until a slot becomes available.
    """
    if model is None or defer_model_check:
        self._model = model
    else:
        self._model = models.infer_model(model)

    self._name = name
    self.end_strategy = end_strategy
    self.model_settings = model_settings

    self._output_type = output_type
    self.instrument = instrument
    self._metadata = metadata
    self._deps_type = deps_type

    if mcp_servers := _deprecated_kwargs.pop('mcp_servers', None):
        if toolsets is not None:  # pragma: no cover
            raise TypeError('`mcp_servers` and `toolsets` cannot be set at the same time.')
        warnings.warn('`mcp_servers` is deprecated, use `toolsets` instead', DeprecationWarning)
        toolsets = mcp_servers

    _utils.validate_empty_kwargs(_deprecated_kwargs)

    self._output_schema = _output.OutputSchema[OutputDataT].build(output_type)
    self._output_validators = []

    self._instructions = self._normalize_instructions(instructions)

    self._system_prompts = (system_prompt,) if isinstance(system_prompt, str) else tuple(system_prompt)
    self._system_prompt_functions = []
    self._system_prompt_dynamic_functions = {}

    self._max_result_retries = output_retries if output_retries is not None else retries
    self._max_tool_retries = retries
    self._tool_timeout = tool_timeout

    self._validation_context = validation_context

    self._builtin_tools = builtin_tools

    self._prepare_tools = prepare_tools
    self._prepare_output_tools = prepare_output_tools

    self._output_toolset = self._output_schema.toolset
    if self._output_toolset:
        self._output_toolset.max_retries = self._max_result_retries

    self._function_toolset = _AgentFunctionToolset(
        tools,
        max_retries=self._max_tool_retries,
        timeout=self._tool_timeout,
        output_schema=self._output_schema,
    )
    self._dynamic_toolsets = [
        DynamicToolset[AgentDepsT](toolset_func=toolset)
        for toolset in toolsets or []
        if not isinstance(toolset, AbstractToolset)
    ]
    self._user_toolsets = [toolset for toolset in toolsets or [] if isinstance(toolset, AbstractToolset)]

    self.history_processors = history_processors or []

    self._event_stream_handler = event_stream_handler

    self._concurrency_limiter = _concurrency.normalize_to_limiter(max_concurrency)

    self._override_name: ContextVar[_utils.Option[str]] = ContextVar('_override_name', default=None)
    self._override_deps: ContextVar[_utils.Option[AgentDepsT]] = ContextVar('_override_deps', default=None)
    self._override_model: ContextVar[_utils.Option[models.Model]] = ContextVar('_override_model', default=None)
    self._override_toolsets: ContextVar[_utils.Option[Sequence[AbstractToolset[AgentDepsT]]]] = ContextVar(
        '_override_toolsets', default=None
    )
    self._override_tools: ContextVar[
        _utils.Option[Sequence[Tool[AgentDepsT] | ToolFuncEither[AgentDepsT, ...]]]
    ] = ContextVar('_override_tools', default=None)
    self._override_instructions: ContextVar[
        _utils.Option[list[str | _system_prompt.SystemPromptFunc[AgentDepsT]]]
    ] = ContextVar('_override_instructions', default=None)
    self._override_metadata: ContextVar[_utils.Option[AgentMetadata[AgentDepsT]]] = ContextVar(
        '_override_metadata', default=None
    )

    self._enter_lock = Lock()
    self._entered_count = 0
    self._exit_stack = None

```

---|---
####  end_strategy `instance-attribute`
```
end_strategy: EndStrategy[](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.EndStrategy "EndStrategy
