Parameters:
Name | Type | Description | Default
---|---|---|---
`function` |  |  The function to call. This will be called with keywords only. Schema validation of the arguments is skipped, but a custom `args_validator` will still run if provided. |  _required_
`name` |  |  The unique name of the tool that clearly communicates its purpose |  _required_
`description` |  |  Used to tell the model how/when/why to use the tool. You can provide few-shot examples as a part of the description. |  _required_
`json_schema` |  `JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue "pydantic.json_schema.JsonSchemaValue")` |  The schema for the function arguments |  _required_
`takes_ctx` |  |  An optional boolean parameter indicating whether the function accepts the context object as an argument. |  `False`
`sequential` |  |  Whether the function requires a sequential/serial execution environment. Defaults to False. |  `False`
`args_validator` |  `ArgsValidatorFunc[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ArgsValidatorFunc "ArgsValidatorFunc



      module-attribute
   \(pydantic_ai.tools.ArgsValidatorFunc\)")[` |  custom method to validate tool arguments after schema validation has passed, before execution. The validator receives the already-validated and type-converted parameters, with `RunContext` as the first argument. Should raise [`ModelRetry`](https://ai.pydantic.dev/api/exceptions/#pydantic_ai.exceptions.ModelRetry "ModelRetry") on validation failure, return `None` on success. See [`ArgsValidatorFunc`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ArgsValidatorFunc "ArgsValidatorFunc



      module-attribute
  "). |  `None`
Returns:
Type | Description
---|---
|  A Pydantic tool that calls the function
Source code in `pydantic_ai_slim/pydantic_ai/tools.py`
```
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
```
| ```
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

```

---|---
####  prepare_tool_def `async`
```
prepare_tool_def(
    ctx: RunContext[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext



      dataclass
   \(pydantic_ai._run_context.RunContext\)")[ToolAgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolAgentDepsT "ToolAgentDepsT



      module-attribute
   \(pydantic_ai.tools.ToolAgentDepsT\)")],
) -> ToolDefinition[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolDefinition "ToolDefinition



      dataclass
   \(pydantic_ai.tools.ToolDefinition\)") | None

```

Get the tool definition.
By default, this method creates a tool definition, then either returns it, or calls `self.prepare` if it's set.
Returns:
Type | Description
---|---
`ToolDefinition[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolDefinition "ToolDefinition



      dataclass
   \(pydantic_ai.tools.ToolDefinition\)") | None` |  return a `ToolDefinition` or `None` if the tools should not be registered for this run.
Source code in `pydantic_ai_slim/pydantic_ai/tools.py`
```
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
###  ObjectJsonSchema `module-attribute`
```
ObjectJsonSchema:  = [, ]

```

Type representing JSON schema of an object, e.g. where `"type": "object"`.
This type is used to define tools parameters (aka arguments) in [ToolDefinition](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolDefinition "ToolDefinition



      dataclass
  ").
With PEP-728 this should be a TypedDict with `type: Literal['object']`, and `extra_parts=Any`
###  ToolKind `module-attribute`
```
ToolKind:  = [
    "function", "output", "external", "unapproved"
]

```

Kind of tool.
###  ToolDefinition `dataclass`
Definition of a tool passed to a model.
This is used for both function tools and output tools.
Source code in `pydantic_ai_slim/pydantic_ai/tools.py`
```
490
491
492
493
494
495
496
497
498
499
500
501
502
503
504
505
506
507
508
509
510
511
512
513
514
515
516
517
518
519
520
521
522
523
524
525
526
527
528
529
530
531
532
533
534
535
536
537
538
539
540
541
542
543
544
545
546
547
548
549
550
551
552
553
554
555
556
557
558
559
```
| ```
@dataclass(repr=False, kw_only=True)
class ToolDefinition:
    """Definition of a tool passed to a model.

    This is used for both function tools and output tools.
    """

    name: str
    """The name of the tool."""

    parameters_json_schema: ObjectJsonSchema = field(default_factory=lambda: {'type': 'object', 'properties': {}})
    """The JSON schema for the tool's parameters."""

    description: str | None = None
    """The description of the tool."""

    outer_typed_dict_key: str | None = None
    """The key in the outer [TypedDict] that wraps an output tool.

    This will only be set for output tools which don't have an `object` JSON schema.
    """

    strict: bool | None = None
    """Whether to enforce (vendor-specific) strict JSON schema validation for tool calls.

    Setting this to `True` while using a supported model generally imposes some restrictions on the tool's JSON schema
    in exchange for guaranteeing the API responses strictly match that schema.

    When `False`, the model may be free to generate other properties or types (depending on the vendor).
    When `None` (the default), the value will be inferred based on the compatibility of the parameters_json_schema.

    Note: this is currently supported by OpenAI and Anthropic models.
    """

    sequential: bool = False
    """Whether this tool requires a sequential/serial execution environment."""

    kind: ToolKind = field(default='function')
    """The kind of tool:

    - `'function'`: a tool that will be executed by Pydantic AI during an agent run and has its result returned to the model
    - `'output'`: a tool that passes through an output value that ends the run
    - `'external'`: a tool whose result will be produced outside of the Pydantic AI agent run in which it was called, because it depends on an upstream service (or user) or could take longer to generate than it's reasonable to keep the agent process running.
        See the [tools documentation](../deferred-tools.md#deferred-tools) for more info.
    - `'unapproved'`: a tool that requires human-in-the-loop approval.
        See the [tools documentation](../deferred-tools.md#human-in-the-loop-tool-approval) for more info.
    """

    metadata: dict[str, Any] | None = None
    """Tool metadata that can be set by the toolset this tool came from. It is not sent to the model, but can be used for filtering and tool behavior customization.

    For MCP tools, this contains the `meta`, `annotations`, and `output_schema` fields from the tool definition.
    """

    timeout: float | None = None
    """Timeout in seconds for tool execution.

    If the tool takes longer than this, a retry prompt is returned to the model.
    Defaults to None (no timeout).
    """

    @property
    def defer(self) -> bool:
        """Whether calls to this tool will be deferred.

        See the [tools documentation](../deferred-tools.md#deferred-tools) for more info.
        """
        return self.kind in ('external', 'unapproved')

    __repr__ = _utils.dataclasses_no_defaults_repr

```

---|---
####  name `instance-attribute`
```
name:

```

The name of the tool.
####  parameters_json_schema `class-attribute` `instance-attribute`
```
parameters_json_schema: ObjectJsonSchema[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ObjectJsonSchema "ObjectJsonSchema



      module-attribute
   \(pydantic_ai.tools.ObjectJsonSchema\)") = (
    default_factory=lambda: {
        "type": "object",
        "properties": {},
    }
)

```

The JSON schema for the tool's parameters.
####  description `class-attribute` `instance-attribute`
```
description:  | None = None

```

The description of the tool.
####  outer_typed_dict_key `class-attribute` `instance-attribute`
```
outer_typed_dict_key:  | None = None

```

The key in the outer [TypedDict] that wraps an output tool.
This will only be set for output tools which don't have an `object` JSON schema.
####  strict `class-attribute` `instance-attribute`
```
strict:  | None = None

```

Whether to enforce (vendor-specific) strict JSON schema validation for tool calls.
Setting this to `True` while using a supported model generally imposes some restrictions on the tool's JSON schema in exchange for guaranteeing the API responses strictly match that schema.
When `False`, the model may be free to generate other properties or types (depending on the vendor). When `None` (the default), the value will be inferred based on the compatibility of the parameters_json_schema.
Note: this is currently supported by OpenAI and Anthropic models.
####  sequential `class-attribute` `instance-attribute`
```
sequential:  = False

```

Whether this tool requires a sequential/serial execution environment.
####  kind `class-attribute` `instance-attribute`
```
kind: ToolKind[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolKind "ToolKind



      module-attribute
   \(pydantic_ai.tools.ToolKind\)") = (default='function')

```

The kind of tool:
  * `'function'`: a tool that will be executed by Pydantic AI during an agent run and has its result returned to the model
  * `'output'`: a tool that passes through an output value that ends the run
  * `'external'`: a tool whose result will be produced outside of the Pydantic AI agent run in which it was called, because it depends on an upstream service (or user) or could take longer to generate than it's reasonable to keep the agent process running. See the [tools documentation](https://ai.pydantic.dev/deferred-tools/#deferred-tools) for more info.
  * `'unapproved'`: a tool that requires human-in-the-loop approval. See the [tools documentation](https://ai.pydantic.dev/deferred-tools/#human-in-the-loop-tool-approval) for more info.


####  metadata `class-attribute` `instance-attribute`
```
metadata: [, ] | None = None

```

Tool metadata that can be set by the toolset this tool came from. It is not sent to the model, but can be used for filtering and tool behavior customization.
For MCP tools, this contains the `meta`, `annotations`, and `output_schema` fields from the tool definition.
####  timeout `class-attribute` `instance-attribute`
```
timeout:  | None = None

```

Timeout in seconds for tool execution.
If the tool takes longer than this, a retry prompt is returned to the model. Defaults to None (no timeout).
####  defer `property`
```
defer:

```

Whether calls to this tool will be deferred.
See the [tools documentation](https://ai.pydantic.dev/deferred-tools/#deferred-tools) for more info.
© Pydantic Services Inc. 2024 to present
