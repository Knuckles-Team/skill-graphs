##  simple_ser_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.simple_ser_schema)
```
simple_ser_schema(
    type: ExpectedSerializationTypes,
) -> SimpleSerSchema

```

Returns a schema for serialization with a custom type.
Parameters:
Name | Type | Description | Default
---|---|---|---
`type` |  `ExpectedSerializationTypes` |  The type to use for serialization |  _required_
Source code in `pydantic_core/core_schema.py`
```
267
268
269
270
271
272
273
274
```
| ```
def simple_ser_schema(type: ExpectedSerializationTypes) -> SimpleSerSchema:
    """
    Returns a schema for serialization with a custom type.

    Args:
        type: The type to use for serialization
    """
    return SimpleSerSchema(type=type)

```

---|---
##  plain_serializer_function_ser_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.plain_serializer_function_ser_schema)
```
plain_serializer_function_ser_schema(
    function: SerializerFunction,
    *,
    is_field_serializer:  | None = None,
    info_arg:  | None = None,
    return_schema: CoreSchema | None = None,
    when_used: WhenUsed[](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.WhenUsed) = "always"
) -> PlainSerializerFunctionSerSchema

```

Returns a schema for serialization with a function, can be either a "general" or "field" function.
Parameters:
Name | Type | Description | Default
---|---|---|---
`function` |  `SerializerFunction` |  The function to use for serialization |  _required_
`is_field_serializer` |  |  Whether the serializer is for a field, e.g. takes `model` as the first argument, and `info` includes `field_name` |  `None`
`info_arg` |  |  Whether the function takes an `info` argument |  `None`
`return_schema` |  `CoreSchema | None` |  Schema to use for serializing return value |  `None`
`when_used` |  `WhenUsed[](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.WhenUsed)` |  When the function should be called |  `'always'`
Source code in `pydantic_core/core_schema.py`
```
312
313
314
315
316
317
318
319
320
321
322
323
324
325
326
327
328
329
330
331
332
333
334
335
336
337
338
339
340
341
```
| ```
def plain_serializer_function_ser_schema(
    function: SerializerFunction,
    *,
    is_field_serializer: bool | None = None,
    info_arg: bool | None = None,
    return_schema: CoreSchema | None = None,
    when_used: WhenUsed = 'always',
) -> PlainSerializerFunctionSerSchema:
    """
    Returns a schema for serialization with a function, can be either a "general" or "field" function.

    Args:
        function: The function to use for serialization
        is_field_serializer: Whether the serializer is for a field, e.g. takes `model` as the first argument,
            and `info` includes `field_name`
        info_arg: Whether the function takes an `info` argument
        return_schema: Schema to use for serializing return value
        when_used: When the function should be called
    """
    if when_used == 'always':
        # just to avoid extra elements in schema, and to use the actual default defined in rust
        when_used = None  # type: ignore
    return _dict_not_none(
        type='function-plain',
        function=function,
        is_field_serializer=is_field_serializer,
        info_arg=info_arg,
        return_schema=return_schema,
        when_used=when_used,
    )

```

---|---
