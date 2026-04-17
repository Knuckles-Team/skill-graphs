##  call_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.call_schema)
```
call_schema(
    arguments: CoreSchema,
    function: [..., ],
    *,
    function_name:  | None = None,
    return_schema: CoreSchema | None = None,
    ref:  | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> CallSchema

```

Returns a schema that matches an arguments schema, then calls a function, e.g.:
```
from pydantic_core import SchemaValidator, core_schema

param_a = core_schema.arguments_parameter(
    name='a', schema=core_schema.str_schema(), mode='positional_only'
)
param_b = core_schema.arguments_parameter(
    name='b', schema=core_schema.bool_schema(), mode='positional_only'
)
args_schema = core_schema.arguments_schema([param_a, param_b])

schema = core_schema.call_schema(
    arguments=args_schema,
    function=lambda a, b: a + str(not b),
    return_schema=core_schema.str_schema(),
)
v = SchemaValidator(schema)
assert v.validate_python((('hello', True))) == 'helloFalse'

```

Parameters:
Name | Type | Description | Default
---|---|---|---
`arguments` |  `CoreSchema` |  The arguments to use for the arguments schema |  _required_
`function` |  |  The function to use for the call schema |  _required_
`function_name` |  |  The function name to use for the call schema, if not provided `function.__name__` is used |  `None`
`return_schema` |  `CoreSchema | None` |  The return schema to use for the call schema |  `None`
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`
Source code in `pydantic_core/core_schema.py`
```
3726
3727
3728
3729
3730
3731
3732
3733
3734
3735
3736
3737
3738
3739
3740
3741
3742
3743
3744
3745
3746
3747
3748
3749
3750
3751
3752
3753
3754
3755
3756
3757
3758
3759
3760
3761
3762
3763
3764
3765
3766
3767
3768
3769
3770
3771
3772
3773
3774
3775
3776
3777
```
| ```
def call_schema(
    arguments: CoreSchema,
    function: Callable[..., Any],
    *,
    function_name: str | None = None,
    return_schema: CoreSchema | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> CallSchema:
    """
    Returns a schema that matches an arguments schema, then calls a function, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    param_a = core_schema.arguments_parameter(
        name='a', schema=core_schema.str_schema(), mode='positional_only'
    )
    param_b = core_schema.arguments_parameter(
        name='b', schema=core_schema.bool_schema(), mode='positional_only'
    )
    args_schema = core_schema.arguments_schema([param_a, param_b])

    schema = core_schema.call_schema(
        arguments=args_schema,
        function=lambda a, b: a + str(not b),
        return_schema=core_schema.str_schema(),
    )
    v = SchemaValidator(schema)
    assert v.validate_python((('hello', True))) == 'helloFalse'
```

    Args:
        arguments: The arguments to use for the arguments schema
        function: The function to use for the call schema
        function_name: The function name to use for the call schema, if not provided `function.__name__` is used
        return_schema: The return schema to use for the call schema
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='call',
        arguments_schema=arguments,
        function=function,
        function_name=function_name,
        return_schema=return_schema,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
    )

```

---|---
##  custom_error_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.custom_error_schema)
```
custom_error_schema(
    schema: CoreSchema,
    custom_error_type: ,
    *,
    custom_error_message:  | None = None,
    custom_error_context: [, ] | None = None,
    ref:  | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> CustomErrorSchema

```

Returns a schema that matches a custom error value, e.g.:
```
from pydantic_core import SchemaValidator, core_schema

schema = core_schema.custom_error_schema(
    schema=core_schema.int_schema(),
    custom_error_type='MyError',
    custom_error_message='Error msg',
)
v = SchemaValidator(schema)
v.validate_python(1)

```

Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `CoreSchema` |  The schema to use for the custom error schema |  _required_
`custom_error_type` |  |  The custom error type to use for the custom error schema |  _required_
`custom_error_message` |  |  The custom error message to use for the custom error schema |  `None`
`custom_error_context` |  |  The custom error context to use for the custom error schema |  `None`
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`
Source code in `pydantic_core/core_schema.py`
```
3791
3792
3793
3794
3795
3796
3797
3798
3799
3800
3801
3802
3803
3804
3805
3806
3807
3808
3809
3810
3811
3812
3813
3814
3815
3816
3817
3818
3819
3820
3821
3822
3823
3824
3825
3826
3827
3828
3829
3830
3831
3832
3833
3834
```
| ```
def custom_error_schema(
    schema: CoreSchema,
    custom_error_type: str,
    *,
    custom_error_message: str | None = None,
    custom_error_context: dict[str, Any] | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> CustomErrorSchema:
    """
    Returns a schema that matches a custom error value, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    schema = core_schema.custom_error_schema(
        schema=core_schema.int_schema(),
        custom_error_type='MyError',
        custom_error_message='Error msg',
    )
    v = SchemaValidator(schema)
    v.validate_python(1)
```

    Args:
        schema: The schema to use for the custom error schema
        custom_error_type: The custom error type to use for the custom error schema
        custom_error_message: The custom error message to use for the custom error schema
        custom_error_context: The custom error context to use for the custom error schema
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='custom-error',
        schema=schema,
        custom_error_type=custom_error_type,
        custom_error_message=custom_error_message,
        custom_error_context=custom_error_context,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
    )

```

---|---
