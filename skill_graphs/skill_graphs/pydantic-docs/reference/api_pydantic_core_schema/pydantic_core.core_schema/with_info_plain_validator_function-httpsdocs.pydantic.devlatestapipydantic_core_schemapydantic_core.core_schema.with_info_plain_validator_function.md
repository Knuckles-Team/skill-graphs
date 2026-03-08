##  with_info_plain_validator_function [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.with_info_plain_validator_function)
```
with_info_plain_validator_function(
    function: WithInfoValidatorFunction,
    *,
    field_name:  | None = None,
    ref:  | None = None,
    json_schema_input_schema: CoreSchema | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> PlainValidatorFunctionSchema

```

Returns a schema that uses the provided function for validation, an `info` argument is passed, e.g.:
```
from pydantic_core import SchemaValidator, core_schema

def fn(v: str, info: core_schema.ValidationInfo) -> str:
    assert 'hello' in v
    return v + 'world'

schema = core_schema.with_info_plain_validator_function(function=fn)
v = SchemaValidator(schema)
assert v.validate_python('hello ') == 'hello world'

```

Parameters:
Name | Type | Description | Default
---|---|---|---
`function` |  `WithInfoValidatorFunction` |  The validator function to call |  _required_
`field_name` |  |  The name of the field this validator is applied to, if any (deprecated) |  `None`
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`
`json_schema_input_schema` |  `CoreSchema | None` |  The core schema to be used to generate the corresponding JSON Schema input type |  `None`
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`
Source code in `pydantic_core/core_schema.py`
```
2437
2438
2439
2440
2441
2442
2443
2444
2445
2446
2447
2448
2449
2450
2451
2452
2453
2454
2455
2456
2457
2458
2459
2460
2461
2462
2463
2464
2465
2466
2467
2468
2469
2470
2471
2472
2473
2474
2475
2476
2477
2478
2479
2480
2481
2482
2483
```
| ```
def with_info_plain_validator_function(
    function: WithInfoValidatorFunction,
    *,
    field_name: str | None = None,
    ref: str | None = None,
    json_schema_input_schema: CoreSchema | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> PlainValidatorFunctionSchema:
    """
    Returns a schema that uses the provided function for validation, an `info` argument is passed, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    def fn(v: str, info: core_schema.ValidationInfo) -> str:
        assert 'hello' in v
        return v + 'world'

    schema = core_schema.with_info_plain_validator_function(function=fn)
    v = SchemaValidator(schema)
    assert v.validate_python('hello ') == 'hello world'
```

    Args:
        function: The validator function to call
        field_name: The name of the field this validator is applied to, if any (deprecated)
        ref: optional unique identifier of the schema, used to reference the schema in other places
        json_schema_input_schema: The core schema to be used to generate the corresponding JSON Schema input type
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    if field_name is not None:
        warnings.warn(
            'The `field_name` argument on `with_info_plain_validator_function` is deprecated, it will be passed to the function through `ValidationState` instead.',
            DeprecationWarning,
            stacklevel=2,
        )

    return _dict_not_none(
        type='function-plain',
        function=_dict_not_none(type='with-info', function=function, field_name=field_name),
        ref=ref,
        json_schema_input_schema=json_schema_input_schema,
        metadata=metadata,
        serialization=serialization,
    )

```

---|---
##  with_default_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.with_default_schema)
```
with_default_schema(
    schema: CoreSchema,
    *,
    default:  = PydanticUndefined,
    default_factory: [
        [[], ],
        [[[, ]], ],
        None,
    ] = None,
    default_factory_takes_data:  | None = None,
    on_error: (
        ["raise", "omit", "default"] | None
    ) = None,
    validate_default:  | None = None,
    strict:  | None = None,
    ref:  | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> WithDefaultSchema

```

Returns a schema that adds a default value to the given schema, e.g.:
```
from pydantic_core import SchemaValidator, core_schema

schema = core_schema.with_default_schema(core_schema.str_schema(), default='hello')
wrapper_schema = core_schema.typed_dict_schema(
    {'a': core_schema.typed_dict_field(schema)}
)
v = SchemaValidator(wrapper_schema)
assert v.validate_python({}) == v.validate_python({'a': 'hello'})

```

Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `CoreSchema` |  The schema to add a default value to |  _required_
`default` |  |  The default value to use |  `PydanticUndefined`
`default_factory` |  |  A callable that returns the default value to use |  `None`
`default_factory_takes_data` |  |  Whether the default factory takes a validated data argument |  `None`
`on_error` |  |  What to do if the schema validation fails. One of 'raise', 'omit', 'default' |  `None`
`validate_default` |  |  Whether the default value should be validated |  `None`
`strict` |  |  Whether the underlying schema should be validated with strict mode |  `None`
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`
Source code in `pydantic_core/core_schema.py`
```
2500
2501
2502
2503
2504
2505
2506
2507
2508
2509
2510
2511
2512
2513
2514
2515
2516
2517
2518
2519
2520
2521
2522
2523
2524
2525
2526
2527
2528
2529
2530
2531
2532
2533
2534
2535
2536
2537
2538
2539
2540
2541
2542
2543
2544
2545
2546
2547
2548
2549
2550
2551
2552
2553
```
| ```
def with_default_schema(
    schema: CoreSchema,
    *,
    default: Any = PydanticUndefined,
    default_factory: Union[Callable[[], Any], Callable[[dict[str, Any]], Any], None] = None,
    default_factory_takes_data: bool | None = None,
    on_error: Literal['raise', 'omit', 'default'] | None = None,
    validate_default: bool | None = None,
    strict: bool | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> WithDefaultSchema:
    """
    Returns a schema that adds a default value to the given schema, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    schema = core_schema.with_default_schema(core_schema.str_schema(), default='hello')
    wrapper_schema = core_schema.typed_dict_schema(
        {'a': core_schema.typed_dict_field(schema)}
    )
    v = SchemaValidator(wrapper_schema)
    assert v.validate_python({}) == v.validate_python({'a': 'hello'})
```

    Args:
        schema: The schema to add a default value to
        default: The default value to use
        default_factory: A callable that returns the default value to use
        default_factory_takes_data: Whether the default factory takes a validated data argument
        on_error: What to do if the schema validation fails. One of 'raise', 'omit', 'default'
        validate_default: Whether the default value should be validated
        strict: Whether the underlying schema should be validated with strict mode
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    s = _dict_not_none(
        type='default',
        schema=schema,
        default_factory=default_factory,
        default_factory_takes_data=default_factory_takes_data,
        on_error=on_error,
        validate_default=validate_default,
        strict=strict,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
    )
    if default is not PydanticUndefined:
        s['default'] = default
    return s

```

---|---
