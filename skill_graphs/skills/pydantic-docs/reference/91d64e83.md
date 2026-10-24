##  with_info_before_validator_function [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.with_info_before_validator_function)
```
with_info_before_validator_function(
    function: WithInfoValidatorFunction,
    schema: CoreSchema,
    *,
    field_name:  | None = None,
    ref:  | None = None,
    json_schema_input_schema: CoreSchema | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> BeforeValidatorFunctionSchema

```

Returns a schema that calls a validator function before validation, the function is called with an `info` argument, e.g.:
```
from pydantic_core import SchemaValidator, core_schema

def fn(v: bytes, info: core_schema.ValidationInfo) -> str:
    assert info.data is not None
    assert info.field_name is not None
    return v.decode() + 'world'

func_schema = core_schema.with_info_before_validator_function(
    function=fn, schema=core_schema.str_schema()
)
schema = core_schema.typed_dict_schema({'a': core_schema.typed_dict_field(func_schema)})

v = SchemaValidator(schema)
assert v.validate_python({'a': b'hello '}) == {'a': 'hello world'}

```

Parameters:
Name | Type | Description | Default
---|---|---|---
`function` |  `WithInfoValidatorFunction` |  The validator function to call |  _required_
`field_name` |  |  The name of the field this validator is applied to, if any (deprecated) |  `None`
`schema` |  `CoreSchema` |  The schema to validate the output of the validator function |  _required_
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`
`json_schema_input_schema` |  `CoreSchema | None` |  The core schema to be used to generate the corresponding JSON Schema input type |  `None`
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`
Source code in `pydantic_core/core_schema.py`
```
2082
2083
2084
2085
2086
2087
2088
2089
2090
2091
2092
2093
2094
2095
2096
2097
2098
2099
2100
2101
2102
2103
2104
2105
2106
2107
2108
2109
2110
2111
2112
2113
2114
2115
2116
2117
2118
2119
2120
2121
2122
2123
2124
2125
2126
2127
2128
2129
2130
2131
2132
2133
2134
2135
2136
2137
```
| ```
def with_info_before_validator_function(
    function: WithInfoValidatorFunction,
    schema: CoreSchema,
    *,
    field_name: str | None = None,
    ref: str | None = None,
    json_schema_input_schema: CoreSchema | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> BeforeValidatorFunctionSchema:
    """
    Returns a schema that calls a validator function before validation, the function is called with
    an `info` argument, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    def fn(v: bytes, info: core_schema.ValidationInfo) -> str:
        assert info.data is not None
        assert info.field_name is not None
        return v.decode() + 'world'

    func_schema = core_schema.with_info_before_validator_function(
        function=fn, schema=core_schema.str_schema()
    )
    schema = core_schema.typed_dict_schema({'a': core_schema.typed_dict_field(func_schema)})

    v = SchemaValidator(schema)
    assert v.validate_python({'a': b'hello '}) == {'a': 'hello world'}
```

    Args:
        function: The validator function to call
        field_name: The name of the field this validator is applied to, if any (deprecated)
        schema: The schema to validate the output of the validator function
        ref: optional unique identifier of the schema, used to reference the schema in other places
        json_schema_input_schema: The core schema to be used to generate the corresponding JSON Schema input type
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    if field_name is not None:
        warnings.warn(
            'The `field_name` argument on `with_info_before_validator_function` is deprecated, it will be passed to the function through `ValidationState` instead.',
            DeprecationWarning,
            stacklevel=2,
        )

    return _dict_not_none(
        type='function-before',
        function=_dict_not_none(type='with-info', function=function, field_name=field_name),
        schema=schema,
        ref=ref,
        json_schema_input_schema=json_schema_input_schema,
        metadata=metadata,
        serialization=serialization,
    )

```

---|---
##  no_info_after_validator_function [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.no_info_after_validator_function)
```
no_info_after_validator_function(
    function: NoInfoValidatorFunction,
    schema: CoreSchema,
    *,
    ref:  | None = None,
    json_schema_input_schema: CoreSchema | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> AfterValidatorFunctionSchema

```

Returns a schema that calls a validator function after validating, no `info` argument is provided, e.g.:
```
from pydantic_core import SchemaValidator, core_schema

def fn(v: str) -> str:
    return v + 'world'

func_schema = core_schema.no_info_after_validator_function(fn, core_schema.str_schema())
schema = core_schema.typed_dict_schema({'a': core_schema.typed_dict_field(func_schema)})

v = SchemaValidator(schema)
assert v.validate_python({'a': b'hello '}) == {'a': 'hello world'}

```

Parameters:
Name | Type | Description | Default
---|---|---|---
`function` |  `NoInfoValidatorFunction` |  The validator function to call after the schema is validated |  _required_
`schema` |  `CoreSchema` |  The schema to validate before the validator function |  _required_
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`
`json_schema_input_schema` |  `CoreSchema | None` |  The core schema to be used to generate the corresponding JSON Schema input type |  `None`
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`
Source code in `pydantic_core/core_schema.py`
```
2144
2145
2146
2147
2148
2149
2150
2151
2152
2153
2154
2155
2156
2157
2158
2159
2160
2161
2162
2163
2164
2165
2166
2167
2168
2169
2170
2171
2172
2173
2174
2175
2176
2177
2178
2179
2180
2181
2182
2183
2184
2185
```
| ```
def no_info_after_validator_function(
    function: NoInfoValidatorFunction,
    schema: CoreSchema,
    *,
    ref: str | None = None,
    json_schema_input_schema: CoreSchema | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> AfterValidatorFunctionSchema:
    """
    Returns a schema that calls a validator function after validating, no `info` argument is provided, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    def fn(v: str) -> str:
        return v + 'world'

    func_schema = core_schema.no_info_after_validator_function(fn, core_schema.str_schema())
    schema = core_schema.typed_dict_schema({'a': core_schema.typed_dict_field(func_schema)})

    v = SchemaValidator(schema)
    assert v.validate_python({'a': b'hello '}) == {'a': 'hello world'}
```

    Args:
        function: The validator function to call after the schema is validated
        schema: The schema to validate before the validator function
        ref: optional unique identifier of the schema, used to reference the schema in other places
        json_schema_input_schema: The core schema to be used to generate the corresponding JSON Schema input type
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='function-after',
        function={'type': 'no-info', 'function': function},
        schema=schema,
        ref=ref,
        json_schema_input_schema=json_schema_input_schema,
        metadata=metadata,
        serialization=serialization,
    )

```

---|---
