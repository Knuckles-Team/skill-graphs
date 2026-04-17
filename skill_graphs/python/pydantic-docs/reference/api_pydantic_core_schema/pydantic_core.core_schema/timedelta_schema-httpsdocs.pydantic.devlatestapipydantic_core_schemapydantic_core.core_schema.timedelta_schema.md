##  timedelta_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.timedelta_schema)
```
timedelta_schema(
    *,
    strict:  | None = None,
    le:  | None = None,
    ge:  | None = None,
    lt:  | None = None,
    gt:  | None = None,
    microseconds_precision: [
        "truncate", "error"
    ] = "truncate",
    ref:  | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> TimedeltaSchema

```

Returns a schema that matches a timedelta value, e.g.:
```
from datetime import timedelta
from pydantic_core import SchemaValidator, core_schema

schema = core_schema.timedelta_schema(le=timedelta(days=1), ge=timedelta(days=0))
v = SchemaValidator(schema)
assert v.validate_python(timedelta(hours=12)) == timedelta(hours=12)

```

Parameters:
Name | Type | Description | Default
---|---|---|---
`strict` |  |  Whether the value should be a timedelta or a value that can be converted to a timedelta |  `None`
`le` |  |  The value must be less than or equal to this timedelta |  `None`
`ge` |  |  The value must be greater than or equal to this timedelta |  `None`
`lt` |  |  The value must be strictly less than this timedelta |  `None`
`gt` |  |  The value must be strictly greater than this timedelta |  `None`
`microseconds_precision` |  |  The behavior when seconds have more than 6 digits or microseconds is too large |  `'truncate'`
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`
Source code in `pydantic_core/core_schema.py`
```
1209
1210
1211
1212
1213
1214
1215
1216
1217
1218
1219
1220
1221
1222
1223
1224
1225
1226
1227
1228
1229
1230
1231
1232
1233
1234
1235
1236
1237
1238
1239
1240
1241
1242
1243
1244
1245
1246
1247
1248
1249
1250
1251
1252
1253
1254
1255
```
| ```
def timedelta_schema(
    *,
    strict: bool | None = None,
    le: timedelta | None = None,
    ge: timedelta | None = None,
    lt: timedelta | None = None,
    gt: timedelta | None = None,
    microseconds_precision: Literal['truncate', 'error'] = 'truncate',
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> TimedeltaSchema:
    """
    Returns a schema that matches a timedelta value, e.g.:

```py
    from datetime import timedelta
    from pydantic_core import SchemaValidator, core_schema

    schema = core_schema.timedelta_schema(le=timedelta(days=1), ge=timedelta(days=0))
    v = SchemaValidator(schema)
    assert v.validate_python(timedelta(hours=12)) == timedelta(hours=12)
```

    Args:
        strict: Whether the value should be a timedelta or a value that can be converted to a timedelta
        le: The value must be less than or equal to this timedelta
        ge: The value must be greater than or equal to this timedelta
        lt: The value must be strictly less than this timedelta
        gt: The value must be strictly greater than this timedelta
        microseconds_precision: The behavior when seconds have more than 6 digits or microseconds is too large
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='timedelta',
        strict=strict,
        le=le,
        ge=ge,
        lt=lt,
        gt=gt,
        microseconds_precision=microseconds_precision,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
    )

```

---|---
##  literal_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.literal_schema)
```
literal_schema(
    expected: [],
    *,
    ref:  | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> LiteralSchema

```

Returns a schema that matches a literal value, e.g.:
```
from pydantic_core import SchemaValidator, core_schema

schema = core_schema.literal_schema(['hello', 'world'])
v = SchemaValidator(schema)
assert v.validate_python('hello') == 'hello'

```

Parameters:
Name | Type | Description | Default
---|---|---|---
`expected` |  |  The value must be one of these values |  _required_
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`
Source code in `pydantic_core/core_schema.py`
```
1266
1267
1268
1269
1270
1271
1272
1273
1274
1275
1276
1277
1278
1279
1280
1281
1282
1283
1284
1285
1286
1287
1288
1289
1290
```
| ```
def literal_schema(
    expected: list[Any],
    *,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> LiteralSchema:
    """
    Returns a schema that matches a literal value, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    schema = core_schema.literal_schema(['hello', 'world'])
    v = SchemaValidator(schema)
    assert v.validate_python('hello') == 'hello'
```

    Args:
        expected: The value must be one of these values
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(type='literal', expected=expected, ref=ref, metadata=metadata, serialization=serialization)

```

---|---
