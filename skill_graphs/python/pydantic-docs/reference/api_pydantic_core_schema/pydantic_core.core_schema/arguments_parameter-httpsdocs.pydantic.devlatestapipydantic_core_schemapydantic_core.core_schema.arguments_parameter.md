##  arguments_parameter [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.arguments_parameter)
```
arguments_parameter(
    name: ,
    schema: CoreSchema,
    *,
    mode: (
        [
            "positional_only",
            "positional_or_keyword",
            "keyword_only",
        ]
        | None
    ) = None,
    alias: (
         | [ | ] | [[ | ]] | None
    ) = None
) -> ArgumentsParameter

```

Returns a schema that matches an argument parameter, e.g.:
```
from pydantic_core import SchemaValidator, core_schema

param = core_schema.arguments_parameter(
    name='a', schema=core_schema.str_schema(), mode='positional_only'
)
schema = core_schema.arguments_schema([param])
v = SchemaValidator(schema)
assert v.validate_python(('hello',)) == (('hello',), {})

```

Parameters:
Name | Type | Description | Default
---|---|---|---
`name` |  |  The name to use for the argument parameter |  _required_
`schema` |  `CoreSchema` |  The schema to use for the argument parameter |  _required_
`mode` |  |  The mode to use for the argument parameter |  `None`
`alias` |  |  The alias to use for the argument parameter |  `None`
Source code in `pydantic_core/core_schema.py`
```
3499
3500
3501
3502
3503
3504
3505
3506
3507
3508
3509
3510
3511
3512
3513
3514
3515
3516
3517
3518
3519
3520
3521
3522
3523
3524
3525
3526
```
| ```
def arguments_parameter(
    name: str,
    schema: CoreSchema,
    *,
    mode: Literal['positional_only', 'positional_or_keyword', 'keyword_only'] | None = None,
    alias: str | list[str | int] | list[list[str | int]] | None = None,
) -> ArgumentsParameter:
    """
    Returns a schema that matches an argument parameter, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    param = core_schema.arguments_parameter(
        name='a', schema=core_schema.str_schema(), mode='positional_only'
    )
    schema = core_schema.arguments_schema([param])
    v = SchemaValidator(schema)
    assert v.validate_python(('hello',)) == (('hello',), {})
```

    Args:
        name: The name to use for the argument parameter
        schema: The schema to use for the argument parameter
        mode: The mode to use for the argument parameter
        alias: The alias to use for the argument parameter
    """
    return _dict_not_none(name=name, schema=schema, mode=mode, alias=alias)

```

---|---
##  arguments_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.arguments_schema)
```
arguments_schema(
    arguments: [ArgumentsParameter],
    *,
    validate_by_name:  | None = None,
    validate_by_alias:  | None = None,
    var_args_schema: CoreSchema | None = None,
    var_kwargs_mode: VarKwargsMode | None = None,
    var_kwargs_schema: CoreSchema | None = None,
    ref:  | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> ArgumentsSchema

```

Returns a schema that matches an arguments schema, e.g.:
```
from pydantic_core import SchemaValidator, core_schema

param_a = core_schema.arguments_parameter(
    name='a', schema=core_schema.str_schema(), mode='positional_only'
)
param_b = core_schema.arguments_parameter(
    name='b', schema=core_schema.bool_schema(), mode='positional_only'
)
schema = core_schema.arguments_schema([param_a, param_b])
v = SchemaValidator(schema)
assert v.validate_python(('hello', True)) == (('hello', True), {})

```

Parameters:
Name | Type | Description | Default
---|---|---|---
`arguments` |  `ArgumentsParameter]` |  The arguments to use for the arguments schema |  _required_
`validate_by_name` |  |  Whether to populate by the parameter names, defaults to `False`. |  `None`
`validate_by_alias` |  |  Whether to populate by the parameter aliases, defaults to `True`. |  `None`
`var_args_schema` |  `CoreSchema | None` |  The variable args schema to use for the arguments schema |  `None`
`var_kwargs_mode` |  `VarKwargsMode | None` |  The validation mode to use for variadic keyword arguments. If `'uniform'`, every value of the keyword arguments will be validated against the `var_kwargs_schema` schema. If `'unpacked-typed-dict'`, the `var_kwargs_schema` argument must be a [`typed_dict_schema`](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.typed_dict_schema) |  `None`
`var_kwargs_schema` |  `CoreSchema | None` |  The variable kwargs schema to use for the arguments schema |  `None`
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`
Source code in `pydantic_core/core_schema.py`
```
3545
3546
3547
3548
3549
3550
3551
3552
3553
3554
3555
3556
3557
3558
3559
3560
3561
3562
3563
3564
3565
3566
3567
3568
3569
3570
3571
3572
3573
3574
3575
3576
3577
3578
3579
3580
3581
3582
3583
3584
3585
3586
3587
3588
3589
3590
3591
3592
3593
3594
3595
3596
3597
3598
```
| ```
def arguments_schema(
    arguments: list[ArgumentsParameter],
    *,
    validate_by_name: bool | None = None,
    validate_by_alias: bool | None = None,
    var_args_schema: CoreSchema | None = None,
    var_kwargs_mode: VarKwargsMode | None = None,
    var_kwargs_schema: CoreSchema | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> ArgumentsSchema:
    """
    Returns a schema that matches an arguments schema, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    param_a = core_schema.arguments_parameter(
        name='a', schema=core_schema.str_schema(), mode='positional_only'
    )
    param_b = core_schema.arguments_parameter(
        name='b', schema=core_schema.bool_schema(), mode='positional_only'
    )
    schema = core_schema.arguments_schema([param_a, param_b])
    v = SchemaValidator(schema)
    assert v.validate_python(('hello', True)) == (('hello', True), {})
```

    Args:
        arguments: The arguments to use for the arguments schema
        validate_by_name: Whether to populate by the parameter names, defaults to `False`.
        validate_by_alias: Whether to populate by the parameter aliases, defaults to `True`.
        var_args_schema: The variable args schema to use for the arguments schema
        var_kwargs_mode: The validation mode to use for variadic keyword arguments. If `'uniform'`, every value of the
            keyword arguments will be validated against the `var_kwargs_schema` schema. If `'unpacked-typed-dict'`,
            the `var_kwargs_schema` argument must be a [`typed_dict_schema`][pydantic_core.core_schema.typed_dict_schema]
        var_kwargs_schema: The variable kwargs schema to use for the arguments schema
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='arguments',
        arguments_schema=arguments,
        validate_by_name=validate_by_name,
        validate_by_alias=validate_by_alias,
        var_args_schema=var_args_schema,
        var_kwargs_mode=var_kwargs_mode,
        var_kwargs_schema=var_kwargs_schema,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
    )

```

---|---
