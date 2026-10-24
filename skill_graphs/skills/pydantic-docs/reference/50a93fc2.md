##  arguments_v3_parameter [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.arguments_v3_parameter)
```
arguments_v3_parameter(
    name: ,
    schema: CoreSchema,
    *,
    mode: (
        [
            "positional_only",
            "positional_or_keyword",
            "keyword_only",
            "var_args",
            "var_kwargs_uniform",
            "var_kwargs_unpacked_typed_dict",
        ]
        | None
    ) = None,
    alias: (
         | [ | ] | [[ | ]] | None
    ) = None
) -> ArgumentsV3Parameter

```

Returns a schema that matches an argument parameter, e.g.:
```
from pydantic_core import SchemaValidator, core_schema

param = core_schema.arguments_v3_parameter(
    name='a', schema=core_schema.str_schema(), mode='positional_only'
)
schema = core_schema.arguments_v3_schema([param])
v = SchemaValidator(schema)
assert v.validate_python({'a': 'hello'}) == (('hello',), {})

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
3615
3616
3617
3618
3619
3620
3621
3622
3623
3624
3625
3626
3627
3628
3629
3630
3631
3632
3633
3634
3635
3636
3637
3638
3639
3640
3641
3642
3643
3644
3645
3646
3647
3648
3649
3650
```
| ```
def arguments_v3_parameter(
    name: str,
    schema: CoreSchema,
    *,
    mode: Literal[
        'positional_only',
        'positional_or_keyword',
        'keyword_only',
        'var_args',
        'var_kwargs_uniform',
        'var_kwargs_unpacked_typed_dict',
    ]
    | None = None,
    alias: str | list[str | int] | list[list[str | int]] | None = None,
) -> ArgumentsV3Parameter:
    """
    Returns a schema that matches an argument parameter, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    param = core_schema.arguments_v3_parameter(
        name='a', schema=core_schema.str_schema(), mode='positional_only'
    )
    schema = core_schema.arguments_v3_schema([param])
    v = SchemaValidator(schema)
    assert v.validate_python({'a': 'hello'}) == (('hello',), {})
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
##  arguments_v3_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.arguments_v3_schema)
```
arguments_v3_schema(
    arguments: [ArgumentsV3Parameter],
    *,
    validate_by_name:  | None = None,
    validate_by_alias:  | None = None,
    extra_behavior: (
        ["forbid", "ignore"] | None
    ) = None,
    ref:  | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> ArgumentsV3Schema

```

Returns a schema that matches an arguments schema, e.g.:
```
from pydantic_core import SchemaValidator, core_schema

param_a = core_schema.arguments_v3_parameter(
    name='a', schema=core_schema.str_schema(), mode='positional_only'
)
param_b = core_schema.arguments_v3_parameter(
    name='kwargs', schema=core_schema.bool_schema(), mode='var_kwargs_uniform'
)
schema = core_schema.arguments_v3_schema([param_a, param_b])
v = SchemaValidator(schema)
assert v.validate_python({'a': 'hi', 'kwargs': {'b': True}}) == (('hi',), {'b': True})

```

This schema is currently not used by other Pydantic components. In V3, it will most likely become the default arguments schema for the `'call'` schema.
Parameters:
Name | Type | Description | Default
---|---|---|---
`arguments` |  `ArgumentsV3Parameter]` |  The arguments to use for the arguments schema. |  _required_
`validate_by_name` |  |  Whether to populate by the parameter names, defaults to `False`. |  `None`
`validate_by_alias` |  |  Whether to populate by the parameter aliases, defaults to `True`. |  `None`
`extra_behavior` |  |  The extra behavior to use. |  `None`
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places. |  `None`
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core. |  `None`
`serialization` |  `SerSchema | None` |  Custom serialization schema. |  `None`
Source code in `pydantic_core/core_schema.py`
```
3664
3665
3666
3667
3668
3669
3670
3671
3672
3673
3674
3675
3676
3677
3678
3679
3680
3681
3682
3683
3684
3685
3686
3687
3688
3689
3690
3691
3692
3693
3694
3695
3696
3697
3698
3699
3700
3701
3702
3703
3704
3705
3706
3707
3708
3709
3710
3711
3712
```
| ```
def arguments_v3_schema(
    arguments: list[ArgumentsV3Parameter],
    *,
    validate_by_name: bool | None = None,
    validate_by_alias: bool | None = None,
    extra_behavior: Literal['forbid', 'ignore'] | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> ArgumentsV3Schema:
    """
    Returns a schema that matches an arguments schema, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    param_a = core_schema.arguments_v3_parameter(
        name='a', schema=core_schema.str_schema(), mode='positional_only'
    )
    param_b = core_schema.arguments_v3_parameter(
        name='kwargs', schema=core_schema.bool_schema(), mode='var_kwargs_uniform'
    )
    schema = core_schema.arguments_v3_schema([param_a, param_b])
    v = SchemaValidator(schema)
    assert v.validate_python({'a': 'hi', 'kwargs': {'b': True}}) == (('hi',), {'b': True})
```

    This schema is currently not used by other Pydantic components. In V3, it will most likely
    become the default arguments schema for the `'call'` schema.

    Args:
        arguments: The arguments to use for the arguments schema.
        validate_by_name: Whether to populate by the parameter names, defaults to `False`.
        validate_by_alias: Whether to populate by the parameter aliases, defaults to `True`.
        extra_behavior: The extra behavior to use.
        ref: optional unique identifier of the schema, used to reference the schema in other places.
        metadata: Any other information you want to include with the schema, not used by pydantic-core.
        serialization: Custom serialization schema.
    """
    return _dict_not_none(
        type='arguments-v3',
        arguments_schema=arguments,
        validate_by_name=validate_by_name,
        validate_by_alias=validate_by_alias,
        extra_behavior=extra_behavior,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
    )

```

---|---
