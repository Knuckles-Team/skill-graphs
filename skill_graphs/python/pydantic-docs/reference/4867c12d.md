##  nullable_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.nullable_schema)
```
nullable_schema(
    schema: CoreSchema,
    *,
    strict:  | None = None,
    ref:  | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> NullableSchema

```

Returns a schema that matches a nullable value, e.g.:
```
from pydantic_core import SchemaValidator, core_schema

schema = core_schema.nullable_schema(core_schema.str_schema())
v = SchemaValidator(schema)
assert v.validate_python(None) is None

```

Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `CoreSchema` |  The schema to wrap |  _required_
`strict` |  |  Whether the underlying schema should be validated with strict mode |  `None`
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`
Source code in `pydantic_core/core_schema.py`
```
2565
2566
2567
2568
2569
2570
2571
2572
2573
2574
2575
2576
2577
2578
2579
2580
2581
2582
2583
2584
2585
2586
2587
2588
2589
2590
2591
2592
2593
```
| ```
def nullable_schema(
    schema: CoreSchema,
    *,
    strict: bool | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> NullableSchema:
    """
    Returns a schema that matches a nullable value, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    schema = core_schema.nullable_schema(core_schema.str_schema())
    v = SchemaValidator(schema)
    assert v.validate_python(None) is None
```

    Args:
        schema: The schema to wrap
        strict: Whether the underlying schema should be validated with strict mode
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='nullable', schema=schema, strict=strict, ref=ref, metadata=metadata, serialization=serialization
    )

```

---|---
##  union_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.union_schema)
```
union_schema(
    choices: [CoreSchema | [CoreSchema, ]],
    *,
    auto_collapse:  | None = None,
    custom_error_type:  | None = None,
    custom_error_message:  | None = None,
    custom_error_context: (
        [,  | ] | None
    ) = None,
    mode: ["smart", "left_to_right"] | None = None,
    ref:  | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> UnionSchema

```

Returns a schema that matches a union value, e.g.:
```
from pydantic_core import SchemaValidator, core_schema

schema = core_schema.union_schema([core_schema.str_schema(), core_schema.int_schema()])
v = SchemaValidator(schema)
assert v.validate_python('hello') == 'hello'
assert v.validate_python(1) == 1

```

Parameters:
Name | Type | Description | Default
---|---|---|---
`choices` |  `CoreSchema | CoreSchema, ` |  The schemas to match. If a tuple, the second item is used as the label for the case. |  _required_
`auto_collapse` |  |  whether to automatically collapse unions with one element to the inner validator, default true |  `None`
`custom_error_type` |  |  The custom error type to use if the validation fails |  `None`
`custom_error_message` |  |  The custom error message to use if the validation fails |  `None`
`custom_error_context` |  |  The custom error context to use if the validation fails |  `None`
`mode` |  |  How to select which choice to return * `smart` (default) will try to return the choice which is the closest match to the input value * `left_to_right` will return the first choice in `choices` which succeeds validation |  `None`
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`
Source code in `pydantic_core/core_schema.py`
```
2611
2612
2613
2614
2615
2616
2617
2618
2619
2620
2621
2622
2623
2624
2625
2626
2627
2628
2629
2630
2631
2632
2633
2634
2635
2636
2637
2638
2639
2640
2641
2642
2643
2644
2645
2646
2647
2648
2649
2650
2651
2652
2653
2654
2655
2656
2657
2658
2659
```
| ```
def union_schema(
    choices: list[CoreSchema | tuple[CoreSchema, str]],
    *,
    auto_collapse: bool | None = None,
    custom_error_type: str | None = None,
    custom_error_message: str | None = None,
    custom_error_context: dict[str, str | int] | None = None,
    mode: Literal['smart', 'left_to_right'] | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> UnionSchema:
    """
    Returns a schema that matches a union value, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    schema = core_schema.union_schema([core_schema.str_schema(), core_schema.int_schema()])
    v = SchemaValidator(schema)
    assert v.validate_python('hello') == 'hello'
    assert v.validate_python(1) == 1
```

    Args:
        choices: The schemas to match. If a tuple, the second item is used as the label for the case.
        auto_collapse: whether to automatically collapse unions with one element to the inner validator, default true
        custom_error_type: The custom error type to use if the validation fails
        custom_error_message: The custom error message to use if the validation fails
        custom_error_context: The custom error context to use if the validation fails
        mode: How to select which choice to return
            * `smart` (default) will try to return the choice which is the closest match to the input value
            * `left_to_right` will return the first choice in `choices` which succeeds validation
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='union',
        choices=choices,
        auto_collapse=auto_collapse,
        custom_error_type=custom_error_type,
        custom_error_message=custom_error_message,
        custom_error_context=custom_error_context,
        mode=mode,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
    )

```

---|---
