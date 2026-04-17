##  with_info_wrap_validator_function [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.with_info_wrap_validator_function)
```
with_info_wrap_validator_function(
    function: WithInfoWrapValidatorFunction,
    schema: CoreSchema,
    *,
    field_name:  | None = None,
    json_schema_input_schema: CoreSchema | None = None,
    ref:  | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> WrapValidatorFunctionSchema

```

Returns a schema which calls a function with a `validator` callable argument which can optionally be used to call inner validation with the function logic, this is much like the "onion" implementation of middleware in many popular web frameworks, an `info` argument is also passed, e.g.:
```
from pydantic_core import SchemaValidator, core_schema

def fn(
    v: str,
    validator: core_schema.ValidatorFunctionWrapHandler,
    info: core_schema.ValidationInfo,
) -> str:
    return validator(input_value=v) + 'world'

schema = core_schema.with_info_wrap_validator_function(
    function=fn, schema=core_schema.str_schema()
)
v = SchemaValidator(schema)
assert v.validate_python('hello ') == 'hello world'

```

Parameters:
Name | Type | Description | Default
---|---|---|---
`function` |  `WithInfoWrapValidatorFunction` |  The validator function to call |  _required_
`schema` |  `CoreSchema` |  The schema to validate the output of the validator function |  _required_
`field_name` |  |  The name of the field this validator is applied to, if any (deprecated) |  `None`
`json_schema_input_schema` |  `CoreSchema | None` |  The core schema to be used to generate the corresponding JSON Schema input type |  `None`
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`
Source code in `pydantic_core/core_schema.py`
```
2329
2330
2331
2332
2333
2334
2335
2336
2337
2338
2339
2340
2341
2342
2343
2344
2345
2346
2347
2348
2349
2350
2351
2352
2353
2354
2355
2356
2357
2358
2359
2360
2361
2362
2363
2364
2365
2366
2367
2368
2369
2370
2371
2372
2373
2374
2375
2376
2377
2378
2379
2380
2381
2382
2383
2384
2385
```
| ```
def with_info_wrap_validator_function(
    function: WithInfoWrapValidatorFunction,
    schema: CoreSchema,
    *,
    field_name: str | None = None,
    json_schema_input_schema: CoreSchema | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> WrapValidatorFunctionSchema:
    """
    Returns a schema which calls a function with a `validator` callable argument which can
    optionally be used to call inner validation with the function logic, this is much like the
    "onion" implementation of middleware in many popular web frameworks, an `info` argument is also passed, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    def fn(
        v: str,
        validator: core_schema.ValidatorFunctionWrapHandler,
        info: core_schema.ValidationInfo,
    ) -> str:
        return validator(input_value=v) + 'world'

    schema = core_schema.with_info_wrap_validator_function(
        function=fn, schema=core_schema.str_schema()
    )
    v = SchemaValidator(schema)
    assert v.validate_python('hello ') == 'hello world'
```

    Args:
        function: The validator function to call
        schema: The schema to validate the output of the validator function
        field_name: The name of the field this validator is applied to, if any (deprecated)
        json_schema_input_schema: The core schema to be used to generate the corresponding JSON Schema input type
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    if field_name is not None:
        warnings.warn(
            'The `field_name` argument on `with_info_wrap_validator_function` is deprecated, it will be passed to the function through `ValidationState` instead.',
            DeprecationWarning,
            stacklevel=2,
        )

    return _dict_not_none(
        type='function-wrap',
        function=_dict_not_none(type='with-info', function=function, field_name=field_name),
        schema=schema,
        json_schema_input_schema=json_schema_input_schema,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
    )

```

---|---
##  no_info_plain_validator_function [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.no_info_plain_validator_function)
```
no_info_plain_validator_function(
    function: NoInfoValidatorFunction,
    *,
    ref:  | None = None,
    json_schema_input_schema: CoreSchema | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> PlainValidatorFunctionSchema

```

Returns a schema that uses the provided function for validation, no `info` argument is passed, e.g.:
```
from pydantic_core import SchemaValidator, core_schema

def fn(v: str) -> str:
    assert 'hello' in v
    return v + 'world'

schema = core_schema.no_info_plain_validator_function(function=fn)
v = SchemaValidator(schema)
assert v.validate_python('hello ') == 'hello world'

```

Parameters:
Name | Type | Description | Default
---|---|---|---
`function` |  `NoInfoValidatorFunction` |  The validator function to call |  _required_
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`
`json_schema_input_schema` |  `CoreSchema | None` |  The core schema to be used to generate the corresponding JSON Schema input type |  `None`
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`
Source code in `pydantic_core/core_schema.py`
```
2397
2398
2399
2400
2401
2402
2403
2404
2405
2406
2407
2408
2409
2410
2411
2412
2413
2414
2415
2416
2417
2418
2419
2420
2421
2422
2423
2424
2425
2426
2427
2428
2429
2430
2431
2432
2433
2434
```
| ```
def no_info_plain_validator_function(
    function: NoInfoValidatorFunction,
    *,
    ref: str | None = None,
    json_schema_input_schema: CoreSchema | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> PlainValidatorFunctionSchema:
    """
    Returns a schema that uses the provided function for validation, no `info` argument is passed, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    def fn(v: str) -> str:
        assert 'hello' in v
        return v + 'world'

    schema = core_schema.no_info_plain_validator_function(function=fn)
    v = SchemaValidator(schema)
    assert v.validate_python('hello ') == 'hello world'
```

    Args:
        function: The validator function to call
        ref: optional unique identifier of the schema, used to reference the schema in other places
        json_schema_input_schema: The core schema to be used to generate the corresponding JSON Schema input type
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='function-plain',
        function={'type': 'no-info', 'function': function},
        ref=ref,
        json_schema_input_schema=json_schema_input_schema,
        metadata=metadata,
        serialization=serialization,
    )

```

---|---
