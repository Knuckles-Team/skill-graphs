##  with_info_after_validator_function [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.with_info_after_validator_function)
```
with_info_after_validator_function(
    function: WithInfoValidatorFunction,
    schema: CoreSchema,
    *,
    field_name:  | None = None,
    ref:  | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> AfterValidatorFunctionSchema

```

Returns a schema that calls a validator function after validation, the function is called with an `info` argument, e.g.:
```
from pydantic_core import SchemaValidator, core_schema

def fn(v: str, info: core_schema.ValidationInfo) -> str:
    assert info.data is not None
    assert info.field_name is not None
    return v + 'world'

func_schema = core_schema.with_info_after_validator_function(
    function=fn, schema=core_schema.str_schema()
)
schema = core_schema.typed_dict_schema({'a': core_schema.typed_dict_field(func_schema)})

v = SchemaValidator(schema)
assert v.validate_python({'a': b'hello '}) == {'a': 'hello world'}

```

Parameters:
Name | Type | Description | Default
---|---|---|---
`function` |  `WithInfoValidatorFunction` |  The validator function to call after the schema is validated |  _required_
`schema` |  `CoreSchema` |  The schema to validate before the validator function |  _required_
`field_name` |  |  The name of the field this validator is applied to, if any (deprecated) |  `None`
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`
Source code in `pydantic_core/core_schema.py`
```
2188
2189
2190
2191
2192
2193
2194
2195
2196
2197
2198
2199
2200
2201
2202
2203
2204
2205
2206
2207
2208
2209
2210
2211
2212
2213
2214
2215
2216
2217
2218
2219
2220
2221
2222
2223
2224
2225
2226
2227
2228
2229
2230
2231
2232
2233
2234
2235
2236
2237
2238
2239
2240
```
| ```
def with_info_after_validator_function(
    function: WithInfoValidatorFunction,
    schema: CoreSchema,
    *,
    field_name: str | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> AfterValidatorFunctionSchema:
    """
    Returns a schema that calls a validator function after validation, the function is called with
    an `info` argument, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    def fn(v: str, info: core_schema.ValidationInfo) -> str:
        assert info.data is not None
        assert info.field_name is not None
        return v + 'world'

    func_schema = core_schema.with_info_after_validator_function(
        function=fn, schema=core_schema.str_schema()
    )
    schema = core_schema.typed_dict_schema({'a': core_schema.typed_dict_field(func_schema)})

    v = SchemaValidator(schema)
    assert v.validate_python({'a': b'hello '}) == {'a': 'hello world'}
```

    Args:
        function: The validator function to call after the schema is validated
        schema: The schema to validate before the validator function
        field_name: The name of the field this validator is applied to, if any (deprecated)
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    if field_name is not None:
        warnings.warn(
            'The `field_name` argument on `with_info_after_validator_function` is deprecated, it will be passed to the function through `ValidationState` instead.',
            DeprecationWarning,
            stacklevel=2,
        )

    return _dict_not_none(
        type='function-after',
        function=_dict_not_none(type='with-info', function=function, field_name=field_name),
        schema=schema,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
    )

```

---|---
##  no_info_wrap_validator_function [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.no_info_wrap_validator_function)
```
no_info_wrap_validator_function(
    function: NoInfoWrapValidatorFunction,
    schema: CoreSchema,
    *,
    ref:  | None = None,
    json_schema_input_schema: CoreSchema | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> WrapValidatorFunctionSchema

```

Returns a schema which calls a function with a `validator` callable argument which can optionally be used to call inner validation with the function logic, this is much like the "onion" implementation of middleware in many popular web frameworks, no `info` argument is passed, e.g.:
```
from pydantic_core import SchemaValidator, core_schema

def fn(
    v: str,
    validator: core_schema.ValidatorFunctionWrapHandler,
) -> str:
    return validator(input_value=v) + 'world'

schema = core_schema.no_info_wrap_validator_function(
    function=fn, schema=core_schema.str_schema()
)
v = SchemaValidator(schema)
assert v.validate_python('hello ') == 'hello world'

```

Parameters:
Name | Type | Description | Default
---|---|---|---
`function` |  `NoInfoWrapValidatorFunction` |  The validator function to call |  _required_
`schema` |  `CoreSchema` |  The schema to validate the output of the validator function |  _required_
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`
`json_schema_input_schema` |  `CoreSchema | None` |  The core schema to be used to generate the corresponding JSON Schema input type |  `None`
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`
Source code in `pydantic_core/core_schema.py`
```
2280
2281
2282
2283
2284
2285
2286
2287
2288
2289
2290
2291
2292
2293
2294
2295
2296
2297
2298
2299
2300
2301
2302
2303
2304
2305
2306
2307
2308
2309
2310
2311
2312
2313
2314
2315
2316
2317
2318
2319
2320
2321
2322
2323
2324
2325
2326
```
| ```
def no_info_wrap_validator_function(
    function: NoInfoWrapValidatorFunction,
    schema: CoreSchema,
    *,
    ref: str | None = None,
    json_schema_input_schema: CoreSchema | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> WrapValidatorFunctionSchema:
    """
    Returns a schema which calls a function with a `validator` callable argument which can
    optionally be used to call inner validation with the function logic, this is much like the
    "onion" implementation of middleware in many popular web frameworks, no `info` argument is passed, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    def fn(
        v: str,
        validator: core_schema.ValidatorFunctionWrapHandler,
    ) -> str:
        return validator(input_value=v) + 'world'

    schema = core_schema.no_info_wrap_validator_function(
        function=fn, schema=core_schema.str_schema()
    )
    v = SchemaValidator(schema)
    assert v.validate_python('hello ') == 'hello world'
```

    Args:
        function: The validator function to call
        schema: The schema to validate the output of the validator function
        ref: optional unique identifier of the schema, used to reference the schema in other places
        json_schema_input_schema: The core schema to be used to generate the corresponding JSON Schema input type
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='function-wrap',
        function={'type': 'no-info', 'function': function},
        schema=schema,
        json_schema_input_schema=json_schema_input_schema,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
    )

```

---|---
