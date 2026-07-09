)

```

Type variable for agent dependencies for a tool.
###  Tool `dataclass`
Bases: `ToolAgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolAgentDepsT "ToolAgentDepsT



      module-attribute
   \(pydantic_ai.tools.ToolAgentDepsT\)")]`
A tool function for an agent.
Source code in `pydantic_ai_slim/pydantic_ai/tools.py`
```
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
420
421
422
423
424
425
426
427
428
429
430
431
432
433
434
435
436
437
438
439
440
441
442
443
444
445
446
447
448
449
450
451
452
453
454
455
456
457
458
459
460
461
462
463
464
465
466
467
468
469
470
471
472
473
474
475
```
| ```
@dataclass(init=False)
class Tool(Generic[ToolAgentDepsT]):
    """A tool function for an agent."""

    function: ToolFuncEither[ToolAgentDepsT]
    takes_ctx: bool
    max_retries: int | None
    name: str
    description: str | None
    prepare: ToolPrepareFunc[ToolAgentDepsT] | None
    args_validator: ArgsValidatorFunc[ToolAgentDepsT, ...] | None
    docstring_format: DocstringFormat
    require_parameter_descriptions: bool
    strict: bool | None
    sequential: bool
    requires_approval: bool
    metadata: dict[str, Any] | None
    timeout: float | None
    function_schema: _function_schema.FunctionSchema
    """
    The base JSON schema for the tool's parameters.

    This schema may be modified by the `prepare` function or by the Model class prior to including it in an API request.
    """

    def __init__(
        self,
        function: ToolFuncEither[ToolAgentDepsT, ToolParams],
        *,
        takes_ctx: bool | None = None,
        max_retries: int | None = None,
        name: str | None = None,
        description: str | None = None,
        prepare: ToolPrepareFunc[ToolAgentDepsT] | None = None,
        args_validator: ArgsValidatorFunc[ToolAgentDepsT, ToolParams] | None = None,
        docstring_format: DocstringFormat = 'auto',
        require_parameter_descriptions: bool = False,
        schema_generator: type[GenerateJsonSchema] = GenerateToolJsonSchema,
        strict: bool | None = None,
        sequential: bool = False,
        requires_approval: bool = False,
        metadata: dict[str, Any] | None = None,
        timeout: float | None = None,
        function_schema: _function_schema.FunctionSchema | None = None,
    ):
        """Create a new tool instance.

        Example usage:

    ```python {noqa="I001"}
        from pydantic_ai import Agent, RunContext, Tool

        async def my_tool(ctx: RunContext[int], x: int, y: int) -> str:
            return f'{ctx.deps} {x} {y}'

        agent = Agent('test', tools=[Tool(my_tool)])
    ```

        or with a custom prepare method:

    ```python {noqa="I001"}

        from pydantic_ai import Agent, RunContext, Tool
        from pydantic_ai.tools import ToolDefinition

        async def my_tool(ctx: RunContext[int], x: int, y: int) -> str:
            return f'{ctx.deps} {x} {y}'

        async def prep_my_tool(
            ctx: RunContext[int], tool_def: ToolDefinition
        ) -> ToolDefinition | None:
            # only register the tool if `deps == 42`
            if ctx.deps == 42:
                return tool_def

        agent = Agent('test', tools=[Tool(my_tool, prepare=prep_my_tool)])
    ```


        Args:
            function: The Python function to call as the tool.
            takes_ctx: Whether the function takes a [`RunContext`][pydantic_ai.tools.RunContext] first argument,
                this is inferred if unset.
            max_retries: Maximum number of retries allowed for this tool, set to the agent default if `None`.
            name: Name of the tool, inferred from the function if `None`.
            description: Description of the tool, inferred from the function if `None`.
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
            schema_generator: The JSON schema generator class to use. Defaults to `GenerateToolJsonSchema`.
            strict: Whether to enforce JSON schema compliance (only affects OpenAI).
                See [`ToolDefinition`][pydantic_ai.tools.ToolDefinition] for more info.
            sequential: Whether the function requires a sequential/serial execution environment. Defaults to False.
            requires_approval: Whether this tool requires human-in-the-loop approval. Defaults to False.
                See the [tools documentation](../deferred-tools.md#human-in-the-loop-tool-approval) for more info.
            metadata: Optional metadata for the tool. This is not sent to the model but can be used for filtering and tool behavior customization.
            timeout: Timeout in seconds for tool execution. If the tool takes longer, a retry prompt is returned to the model.
                Defaults to None (no timeout).
            function_schema: The function schema to use for the tool. If not provided, it will be generated.
        """
        self.function = function
        self.function_schema = function_schema or _function_schema.function_schema(
            function,
            schema_generator,
            takes_ctx=takes_ctx,
            docstring_format=docstring_format,
            require_parameter_descriptions=require_parameter_descriptions,
        )
        self.takes_ctx = self.function_schema.takes_ctx
        self.max_retries = max_retries
        self.name = name or function.__name__
        self.description = description or self.function_schema.description
        self.prepare = prepare
        self.args_validator = args_validator
        self.docstring_format = docstring_format
        self.require_parameter_descriptions = require_parameter_descriptions
        self.strict = strict
        self.sequential = sequential
        self.requires_approval = requires_approval
        self.metadata = metadata
        self.timeout = timeout

    @classmethod
    def from_schema(
        cls,
        function: Callable[..., Any],
        name: str,
        description: str | None,
        json_schema: JsonSchemaValue,
        takes_ctx: bool = False,
        sequential: bool = False,
        args_validator: ArgsValidatorFunc[Any, ...] | None = None,
    ) -> Self:
        """Creates a Pydantic tool from a function and a JSON schema.

        Args:
            function: The function to call.
                This will be called with keywords only. Schema validation of
                the arguments is skipped, but a custom `args_validator` will
                still run if provided.
            name: The unique name of the tool that clearly communicates its purpose
            description: Used to tell the model how/when/why to use the tool.
                You can provide few-shot examples as a part of the description.
            json_schema: The schema for the function arguments
            takes_ctx: An optional boolean parameter indicating whether the function
                accepts the context object as an argument.
            sequential: Whether the function requires a sequential/serial execution environment. Defaults to False.
            args_validator: custom method to validate tool arguments after schema validation has passed,
                before execution. The validator receives the already-validated and type-converted parameters,
                with `RunContext` as the first argument.
                Should raise [`ModelRetry`][pydantic_ai.exceptions.ModelRetry] on validation failure,
                return `None` on success.
                See [`ArgsValidatorFunc`][pydantic_ai.tools.ArgsValidatorFunc].

        Returns:
            A Pydantic tool that calls the function
        """
        function_schema = _function_schema.FunctionSchema(
            function=function,
            description=description,
            validator=SchemaValidator(schema=core_schema.any_schema()),
            json_schema=json_schema,
            takes_ctx=takes_ctx,
            is_async=_utils.is_async_callable(function),
        )

        return cls(
            function,
            takes_ctx=takes_ctx,
            name=name,
            description=description,
            function_schema=function_schema,
            sequential=sequential,
            args_validator=args_validator,
        )

    @property
    def tool_def(self):
        return ToolDefinition(
            name=self.name,
            description=self.description,
            parameters_json_schema=self.function_schema.json_schema,
            strict=self.strict,
            sequential=self.sequential,
            metadata=self.metadata,
            timeout=self.timeout,
            kind='unapproved' if self.requires_approval else 'function',
        )

    async def prepare_tool_def(self, ctx: RunContext[ToolAgentDepsT]) -> ToolDefinition | None:
        """Get the tool definition.

        By default, this method creates a tool definition, then either returns it, or calls `self.prepare`
        if it's set.

        Returns:
            return a `ToolDefinition` or `None` if the tools should not be registered for this run.
        """
        base_tool_def = self.tool_def

        if self.prepare is not None:
            return await self.prepare(ctx, base_tool_def)
        else:
            return base_tool_def

```

---|---
####  __init__
```
__init__(
    function: ToolFuncEither[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolFuncEither "ToolFuncEither



      module-attribute
   \(pydantic_ai.tools.ToolFuncEither\)")[ToolAgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolAgentDepsT "ToolAgentDepsT



      module-attribute
   \(pydantic_ai.tools.ToolAgentDepsT\)"), ToolParams[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolParams "ToolParams



      module-attribute
   \(pydantic_ai.tools.ToolParams\)")],
    *,
    takes_ctx:  | None = None,
    max_retries:  | None = None,
    name:  | None = None,
    description:  | None = None,
    prepare: ToolPrepareFunc[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolPrepareFunc "ToolPrepareFunc



      module-attribute
   \(pydantic_ai.tools.ToolPrepareFunc\)")[ToolAgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolAgentDepsT "ToolAgentDepsT



      module-attribute
   \(pydantic_ai.tools.ToolAgentDepsT\)")] | None = None,
    args_validator: (
        ArgsValidatorFunc[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ArgsValidatorFunc "ArgsValidatorFunc



      module-attribute
   \(pydantic_ai.tools.ArgsValidatorFunc\)")[ToolAgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolAgentDepsT "ToolAgentDepsT



      module-attribute
   \(pydantic_ai.tools.ToolAgentDepsT\)"), ToolParams[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolParams "ToolParams



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
    function_schema: FunctionSchema | None = None
)

```

Create a new tool instance.
Example usage:
```
from pydantic_ai import Agent, RunContext, Tool

async def my_tool(ctx: RunContext[int], x: int, y: int) -> str:
    return f'{ctx.deps} {x} {y}'

agent = Agent('test', tools=[Tool(my_tool)])

```

or with a custom prepare method:
```
from pydantic_ai import Agent, RunContext, Tool
from pydantic_ai.tools import ToolDefinition

async def my_tool(ctx: RunContext[int], x: int, y: int) -> str:
    return f'{ctx.deps} {x} {y}'

async def prep_my_tool(
    ctx: RunContext[int], tool_def: ToolDefinition
) -> ToolDefinition | None:
    # only register the tool if `deps == 42`
    if ctx.deps == 42:
        return tool_def

agent = Agent('test', tools=[Tool(my_tool, prepare=prep_my_tool)])

```

Parameters:
Name | Type | Description | Default
---|---|---|---
`function` |  `ToolFuncEither[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolFuncEither "ToolFuncEither



      module-attribute
   \(pydantic_ai.tools.ToolFuncEither\)")[ToolAgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolAgentDepsT "ToolAgentDepsT



      module-attribute
   \(pydantic_ai.tools.ToolAgentDepsT\)"), ToolParams[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolParams "ToolParams



      module-attribute
   \(pydantic_ai.tools.ToolParams\)")]` |  The Python function to call as the tool. |  _required_
`takes_ctx` |  |  Whether the function takes a [`RunContext`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext



      dataclass
  ") first argument, this is inferred if unset. |  `None`
`max_retries` |  |  Maximum number of retries allowed for this tool, set to the agent default if `None`. |  `None`
`name` |  |  Name of the tool, inferred from the function if `None`. |  `None`
`description` |  |  Description of the tool, inferred from the function if `None`. |  `None`
`prepare` |  `ToolPrepareFunc[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolPrepareFunc "ToolPrepareFunc



      module-attribute
   \(pydantic_ai.tools.ToolPrepareFunc\)")[ToolAgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolAgentDepsT "ToolAgentDepsT



      module-attribute
   \(pydantic_ai.tools.ToolAgentDepsT\)")] | None` |  custom method to prepare the tool definition for each step, return `None` to omit this tool from a given step. This is useful if you want to customise a tool at call time, or omit it completely from a step. See [`ToolPrepareFunc`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolPrepareFunc "ToolPrepareFunc



      module-attribute
  "). |  `None`
`args_validator` |  `ArgsValidatorFunc[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ArgsValidatorFunc "ArgsValidatorFunc



      module-attribute
   \(pydantic_ai.tools.ArgsValidatorFunc\)")[ToolAgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolAgentDepsT "ToolAgentDepsT



      module-attribute
   \(pydantic_ai.tools.ToolAgentDepsT\)"), ToolParams[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolParams "ToolParams



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
`schema_generator` |  `GenerateJsonSchema[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema "pydantic.json_schema.GenerateJsonSchema")]` |  The JSON schema generator class to use. Defaults to `GenerateToolJsonSchema`. |  `GenerateToolJsonSchema`
`strict` |  |  Whether to enforce JSON schema compliance (only affects OpenAI). See [`ToolDefinition`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolDefinition "ToolDefinition



      dataclass
  ") for more info. |  `None`
`sequential` |  |  Whether the function requires a sequential/serial execution environment. Defaults to False. |  `False`
`requires_approval` |  |  Whether this tool requires human-in-the-loop approval. Defaults to False. See the [tools documentation](https://ai.pydantic.dev/deferred-tools/#human-in-the-loop-tool-approval) for more info. |  `False`
`metadata` |  |  Optional metadata for the tool. This is not sent to the model but can be used for filtering and tool behavior customization. |  `None`
`timeout` |  |  Timeout in seconds for tool execution. If the tool takes longer, a retry prompt is returned to the model. Defaults to None (no timeout). |  `None`
`function_schema` |  `FunctionSchema | None` |  The function schema to use for the tool. If not provided, it will be generated. |  `None`
Source code in `pydantic_ai_slim/pydantic_ai/tools.py`
```
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
```
| ```
def __init__(
    self,
    function: ToolFuncEither[ToolAgentDepsT, ToolParams],
    *,
    takes_ctx: bool | None = None,
    max_retries: int | None = None,
    name: str | None = None,
    description: str | None = None,
    prepare: ToolPrepareFunc[ToolAgentDepsT] | None = None,
    args_validator: ArgsValidatorFunc[ToolAgentDepsT, ToolParams] | None = None,
    docstring_format: DocstringFormat = 'auto',
    require_parameter_descriptions: bool = False,
    schema_generator: type[GenerateJsonSchema] = GenerateToolJsonSchema,
    strict: bool | None = None,
    sequential: bool = False,
    requires_approval: bool = False,
    metadata: dict[str, Any] | None = None,
    timeout: float | None = None,
    function_schema: _function_schema.FunctionSchema | None = None,
):
    """Create a new tool instance.

    Example usage:

```python {noqa="I001"}
    from pydantic_ai import Agent, RunContext, Tool

    async def my_tool(ctx: RunContext[int], x: int, y: int) -> str:
        return f'{ctx.deps} {x} {y}'

    agent = Agent('test', tools=[Tool(my_tool)])
```

    or with a custom prepare method:

```python {noqa="I001"}

    from pydantic_ai import Agent, RunContext, Tool
    from pydantic_ai.tools import ToolDefinition

    async def my_tool(ctx: RunContext[int], x: int, y: int) -> str:
        return f'{ctx.deps} {x} {y}'

    async def prep_my_tool(
        ctx: RunContext[int], tool_def: ToolDefinition
    ) -> ToolDefinition | None:
        # only register the tool if `deps == 42`
        if ctx.deps == 42:
            return tool_def

    agent = Agent('test', tools=[Tool(my_tool, prepare=prep_my_tool)])
```


    Args:
        function: The Python function to call as the tool.
        takes_ctx: Whether the function takes a [`RunContext`][pydantic_ai.tools.RunContext] first argument,
            this is inferred if unset.
        max_retries: Maximum number of retries allowed for this tool, set to the agent default if `None`.
        name: Name of the tool, inferred from the function if `None`.
        description: Description of the tool, inferred from the function if `None`.
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
        schema_generator: The JSON schema generator class to use. Defaults to `GenerateToolJsonSchema`.
        strict: Whether to enforce JSON schema compliance (only affects OpenAI).
            See [`ToolDefinition`][pydantic_ai.tools.ToolDefinition] for more info.
        sequential: Whether the function requires a sequential/serial execution environment. Defaults to False.
        requires_approval: Whether this tool requires human-in-the-loop approval. Defaults to False.
            See the [tools documentation](../deferred-tools.md#human-in-the-loop-tool-approval) for more info.
        metadata: Optional metadata for the tool. This is not sent to the model but can be used for filtering and tool behavior customization.
        timeout: Timeout in seconds for tool execution. If the tool takes longer, a retry prompt is returned to the model.
            Defaults to None (no timeout).
        function_schema: The function schema to use for the tool. If not provided, it will be generated.
    """
    self.function = function
    self.function_schema = function_schema or _function_schema.function_schema(
        function,
        schema_generator,
        takes_ctx=takes_ctx,
        docstring_format=docstring_format,
        require_parameter_descriptions=require_parameter_descriptions,
    )
    self.takes_ctx = self.function_schema.takes_ctx
    self.max_retries = max_retries
    self.name = name or function.__name__
    self.description = description or self.function_schema.description
    self.prepare = prepare
    self.args_validator = args_validator
    self.docstring_format = docstring_format
    self.require_parameter_descriptions = require_parameter_descriptions
    self.strict = strict
    self.sequential = sequential
    self.requires_approval = requires_approval
    self.metadata = metadata
    self.timeout = timeout

```

---|---
####  function_schema `instance-attribute`
```
function_schema: FunctionSchema = (
    function_schema
    or function_schema(
        function,
        schema_generator,
        takes_ctx=takes_ctx,
        docstring_format=docstring_format,
        require_parameter_descriptions=require_parameter_descriptions,
    )
)

```

The base JSON schema for the tool's parameters.
This schema may be modified by the `prepare` function or by the Model class prior to including it in an API request.
####  from_schema `classmethod`
```
from_schema(
    function: [..., ],
    name: ,
    description:  | None,
    json_schema: JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue "pydantic.json_schema.JsonSchemaValue"),
    takes_ctx:  = False,
    sequential:  = False,
    args_validator: (
        ArgsValidatorFunc[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ArgsValidatorFunc "ArgsValidatorFunc



      module-attribute
   \(pydantic_ai.tools.ArgsValidatorFunc\)")[, ...] | None
    ) = None,
) ->

```

Creates a Pydantic tool from a function and a JSON schema.
