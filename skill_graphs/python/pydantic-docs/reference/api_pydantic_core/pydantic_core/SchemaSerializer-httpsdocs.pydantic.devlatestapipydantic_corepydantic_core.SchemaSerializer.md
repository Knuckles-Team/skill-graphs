##  SchemaSerializer [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.SchemaSerializer)
```
SchemaSerializer(
    schema: CoreSchema, config: CoreConfig[](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.CoreConfig) | None = None
)

```

`SchemaSerializer` is the Python wrapper for `pydantic-core`'s Rust serialization logic, internally it owns one `CombinedSerializer` which may in turn own more `CombinedSerializer`s which make up the full schema serializer.
Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `CoreSchema` |  The `CoreSchema` to use for serialization. |  _required_
`config` |  `CoreConfig[](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.CoreConfig) | None` |  Optionally a [`CoreConfig`](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.CoreConfig) to to configure serialization. |  `None`
###  to_python [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.SchemaSerializer.to_python)
```
to_python(
    value: ,
    *,
    mode:  | None = None,
    include: _IncEx | None = None,
    exclude: _IncEx | None = None,
    by_alias:  | None = None,
    exclude_unset:  = False,
    exclude_defaults:  = False,
    exclude_none:  = False,
    exclude_computed_fields:  = False,
    round_trip:  = False,
    warnings: (
         | ["none", "warn", "error"]
    ) = True,
    fallback: [[], ] | None = None,
    serialize_as_any:  = False,
    context:  | None = None
) ->

```

Serialize/marshal a Python object to a Python object including transforming and filtering data.
Parameters:
Name | Type | Description | Default
---|---|---|---
`value` |  |  The Python object to serialize. |  _required_
`mode` |  |  The serialization mode to use, either `'python'` or `'json'`, defaults to `'python'`. In JSON mode, all values are converted to JSON compatible types, e.g. `None`, `int`, `float`, `str`, `list`, `dict`. |  `None`
`include` |  `_IncEx | None` |  A set of fields to include, if `None` all fields are included. |  `None`
`exclude` |  `_IncEx | None` |  A set of fields to exclude, if `None` no fields are excluded. |  `None`
`by_alias` |  |  Whether to use the alias names of fields. |  `None`
`exclude_unset` |  |  Whether to exclude fields that are not set, e.g. are not included in `__pydantic_fields_set__`. |  `False`
`exclude_defaults` |  |  Whether to exclude fields that are equal to their default value. |  `False`
`exclude_none` |  |  Whether to exclude fields that have a value of `None`. |  `False`
`exclude_computed_fields` |  |  Whether to exclude computed fields. |  `False`
`round_trip` |  |  Whether to enable serialization and validation round-trip support. |  `False`
`warnings` |  |  How to handle invalid fields. False/"none" ignores them, True/"warn" logs errors, "error" raises a [`PydanticSerializationError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.PydanticSerializationError). |  `True`
`fallback` |  |  A function to call when an unknown value is encountered, if `None` a [`PydanticSerializationError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.PydanticSerializationError) error is raised. |  `None`
`serialize_as_any` |  |  Whether to serialize fields with duck-typing serialization behavior. |  `False`
`context` |  |  The context to use for serialization, this is passed to functional serializers as [`info.context`](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.SerializationInfo.context). |  `None`
Raises:
Type | Description
---|---
`PydanticSerializationError[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.PydanticSerializationError)` |  If serialization fails and no `fallback` function is provided.
Returns:
Type | Description
---|---
|  The serialized Python object.
###  to_json [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.SchemaSerializer.to_json)
```
to_json(
    value: ,
    *,
    indent:  | None = None,
    ensure_ascii:  = False,
    include: _IncEx | None = None,
    exclude: _IncEx | None = None,
    by_alias:  | None = None,
    exclude_unset:  = False,
    exclude_defaults:  = False,
    exclude_none:  = False,
    exclude_computed_fields:  = False,
    round_trip:  = False,
    warnings: (
         | ["none", "warn", "error"]
    ) = True,
    fallback: [[], ] | None = None,
    serialize_as_any:  = False,
    context:  | None = None
) ->

```

Serialize a Python object to JSON including transforming and filtering data.
Parameters:
Name | Type | Description | Default
---|---|---|---
`value` |  |  The Python object to serialize. |  _required_
`indent` |  |  If `None`, the JSON will be compact, otherwise it will be pretty-printed with the indent provided. |  `None`
`ensure_ascii` |  |  If `True`, the output is guaranteed to have all incoming non-ASCII characters escaped. If `False` (the default), these characters will be output as-is. |  `False`
`include` |  `_IncEx | None` |  A set of fields to include, if `None` all fields are included. |  `None`
`exclude` |  `_IncEx | None` |  A set of fields to exclude, if `None` no fields are excluded. |  `None`
`by_alias` |  |  Whether to use the alias names of fields. |  `None`
`exclude_unset` |  |  Whether to exclude fields that are not set, e.g. are not included in `__pydantic_fields_set__`. |  `False`
`exclude_defaults` |  |  Whether to exclude fields that are equal to their default value. |  `False`
`exclude_none` |  |  Whether to exclude fields that have a value of `None`. |  `False`
`exclude_computed_fields` |  |  Whether to exclude computed fields. |  `False`
`round_trip` |  |  Whether to enable serialization and validation round-trip support. |  `False`
`warnings` |  |  How to handle invalid fields. False/"none" ignores them, True/"warn" logs errors, "error" raises a [`PydanticSerializationError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.PydanticSerializationError). |  `True`
`fallback` |  |  A function to call when an unknown value is encountered, if `None` a [`PydanticSerializationError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.PydanticSerializationError) error is raised. |  `None`
`serialize_as_any` |  |  Whether to serialize fields with duck-typing serialization behavior. |  `False`
`context` |  |  The context to use for serialization, this is passed to functional serializers as [`info.context`](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.SerializationInfo.context). |  `None`
Raises:
Type | Description
---|---
`PydanticSerializationError[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.PydanticSerializationError)` |  If serialization fails and no `fallback` function is provided.
Returns:
Type | Description
---|---
|  JSON bytes.
