##  to_string_ser_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.to_string_ser_schema)
```
to_string_ser_schema(
    *, when_used: WhenUsed[](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.WhenUsed) = "json-unless-none"
) -> ToStringSerSchema

```

Returns a schema for serialization using python's `str()` / `__str__` method.
Parameters:
Name | Type | Description | Default
---|---|---|---
`when_used` |  `WhenUsed[](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.WhenUsed)` |  Same meaning as for [general_function_plain_ser_schema], but with a different default |  `'json-unless-none'`
Source code in `pydantic_core/core_schema.py`
```
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
```
| ```
def to_string_ser_schema(*, when_used: WhenUsed = 'json-unless-none') -> ToStringSerSchema:
    """
    Returns a schema for serialization using python's `str()` / `__str__` method.

    Args:
        when_used: Same meaning as for [general_function_plain_ser_schema], but with a different default
    """
    s = dict(type='to-string')
    if when_used != 'json-unless-none':
        # just to avoid extra elements in schema, and to use the actual default defined in rust
        s['when_used'] = when_used
    return s  # type: ignore

```

---|---
##  model_ser_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.model_ser_schema)
```
model_ser_schema(
    cls: [], schema: CoreSchema
) -> ModelSerSchema

```

Returns a schema for serialization using a model.
Parameters:
Name | Type | Description | Default
---|---|---|---
`cls` |  |  The expected class type, used to generate warnings if the wrong type is passed |  _required_
`schema` |  `CoreSchema` |  Internal schema to use to serialize the model dict |  _required_
Source code in `pydantic_core/core_schema.py`
```
454
455
456
457
458
459
460
461
462
```
| ```
def model_ser_schema(cls: type[Any], schema: CoreSchema) -> ModelSerSchema:
    """
    Returns a schema for serialization using a model.

    Args:
        cls: The expected class type, used to generate warnings if the wrong type is passed
        schema: Internal schema to use to serialize the model dict
    """
    return ModelSerSchema(type='model', cls=cls, schema=schema)

```

---|---
