##  to_jsonable_python [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.to_jsonable_python)
```
to_jsonable_python(
    value: ,
    *,
    include: _IncEx | None = None,
    exclude: _IncEx | None = None,
    by_alias:  = True,
    exclude_none:  = False,
    round_trip:  = False,
    timedelta_mode: ["iso8601", "float"] = "iso8601",
    temporal_mode: [
        "iso8601", "seconds", "milliseconds"
    ] = "iso8601",
    bytes_mode: ["utf8", "base64", "hex"] = "utf8",
    inf_nan_mode: [
        "null", "constants", "strings"
    ] = "constants",
    serialize_unknown:  = False,
    fallback: [[], ] | None = None,
    serialize_as_any:  = False,
    context:  | None = None
) ->

```

Serialize/marshal a Python object to a JSON-serializable Python object including transforming and filtering data.
This is effectively a standalone version of [`SchemaSerializer.to_python(mode='json')`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.SchemaSerializer.to_python).
Parameters:
Name | Type | Description | Default
---|---|---|---
`value` |  |  The Python object to serialize. |  _required_
`include` |  `_IncEx | None` |  A set of fields to include, if `None` all fields are included. |  `None`
`exclude` |  `_IncEx | None` |  A set of fields to exclude, if `None` no fields are excluded. |  `None`
`by_alias` |  |  Whether to use the alias names of fields. |  `True`
`exclude_none` |  |  Whether to exclude fields that have a value of `None`. |  `False`
`round_trip` |  |  Whether to enable serialization and validation round-trip support. |  `False`
`timedelta_mode` |  |  How to serialize `timedelta` objects, either `'iso8601'` or `'float'`. |  `'iso8601'`
`temporal_mode` |  |  How to serialize datetime-like objects (`datetime`, `date`, `time`), either `'iso8601'`, `'seconds'`, or `'milliseconds'`. `iso8601` returns an ISO 8601 string; `seconds` returns the Unix timestamp in seconds as a float; `milliseconds` returns the Unix timestamp in milliseconds as a float. |  `'iso8601'`
`bytes_mode` |  |  How to serialize `bytes` objects, either `'utf8'`, `'base64'`, or `'hex'`. |  `'utf8'`
`inf_nan_mode` |  |  How to serialize `Infinity`, `-Infinity` and `NaN` values, either `'null'`, `'constants'`, or `'strings'`. |  `'constants'`
`serialize_unknown` |  |  Attempt to serialize unknown types, `str(value)` will be used, if that fails `"<Unserializable {value_type} object>"` will be used. |  `False`
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
Was this page helpful?
Thanks for your feedback!
Thanks for your feedback!
Made with
