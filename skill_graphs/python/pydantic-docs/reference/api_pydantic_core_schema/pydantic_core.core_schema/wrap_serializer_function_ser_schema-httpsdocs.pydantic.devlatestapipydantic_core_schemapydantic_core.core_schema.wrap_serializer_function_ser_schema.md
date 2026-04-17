##  wrap_serializer_function_ser_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.wrap_serializer_function_ser_schema)
```
wrap_serializer_function_ser_schema(
    function: WrapSerializerFunction,
    *,
    is_field_serializer:  | None = None,
    info_arg:  | None = None,
    schema: CoreSchema | None = None,
    return_schema: CoreSchema | None = None,
    when_used: WhenUsed[](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.WhenUsed) = "always"
) -> WrapSerializerFunctionSerSchema

```

Returns a schema for serialization with a wrap function, can be either a "general" or "field" function.
Parameters:
Name | Type | Description | Default
---|---|---|---
`function` |  `WrapSerializerFunction` |  The function to use for serialization |  _required_
`is_field_serializer` |  |  Whether the serializer is for a field, e.g. takes `model` as the first argument, and `info` includes `field_name` |  `None`
`info_arg` |  |  Whether the function takes an `info` argument |  `None`
`schema` |  `CoreSchema | None` |  The schema to use for the inner serialization |  `None`
`return_schema` |  `CoreSchema | None` |  Schema to use for serializing return value |  `None`
`when_used` |  `WhenUsed[](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.WhenUsed)` |  When the function should be called |  `'always'`
Source code in `pydantic_core/core_schema.py`
```
374
375
376
377
378
379
380
381
382
383
384
385
386
387
388
389
390
391
392
393
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
```
| ```
def wrap_serializer_function_ser_schema(
    function: WrapSerializerFunction,
    *,
    is_field_serializer: bool | None = None,
    info_arg: bool | None = None,
    schema: CoreSchema | None = None,
    return_schema: CoreSchema | None = None,
    when_used: WhenUsed = 'always',
) -> WrapSerializerFunctionSerSchema:
    """
    Returns a schema for serialization with a wrap function, can be either a "general" or "field" function.

    Args:
        function: The function to use for serialization
        is_field_serializer: Whether the serializer is for a field, e.g. takes `model` as the first argument,
            and `info` includes `field_name`
        info_arg: Whether the function takes an `info` argument
        schema: The schema to use for the inner serialization
        return_schema: Schema to use for serializing return value
        when_used: When the function should be called
    """
    if when_used == 'always':
        # just to avoid extra elements in schema, and to use the actual default defined in rust
        when_used = None  # type: ignore
    return _dict_not_none(
        type='function-wrap',
        function=function,
        is_field_serializer=is_field_serializer,
        info_arg=info_arg,
        schema=schema,
        return_schema=return_schema,
        when_used=when_used,
    )

```

---|---
##  format_ser_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.format_ser_schema)
```
format_ser_schema(
    formatting_string: ,
    *,
    when_used: WhenUsed[](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.WhenUsed) = "json-unless-none"
) -> FormatSerSchema

```

Returns a schema for serialization using python's `format` method.
Parameters:
Name | Type | Description | Default
---|---|---|---
`formatting_string` |  |  String defining the format to use |  _required_
`when_used` |  `WhenUsed[](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.WhenUsed)` |  Same meaning as for [general_function_plain_ser_schema], but with a different default |  `'json-unless-none'`
Source code in `pydantic_core/core_schema.py`
```
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
```
| ```
def format_ser_schema(formatting_string: str, *, when_used: WhenUsed = 'json-unless-none') -> FormatSerSchema:
    """
    Returns a schema for serialization using python's `format` method.

    Args:
        formatting_string: String defining the format to use
        when_used: Same meaning as for [general_function_plain_ser_schema], but with a different default
    """
    if when_used == 'json-unless-none':
        # just to avoid extra elements in schema, and to use the actual default defined in rust
        when_used = None  # type: ignore
    return _dict_not_none(type='format', formatting_string=formatting_string, when_used=when_used)

```

---|---
