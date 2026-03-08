##  enum_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.enum_schema)
```
enum_schema(
    cls: ,
    members: [],
    *,
    sub_type: ["str", "int", "float"] | None = None,
    missing: [[], ] | None = None,
    strict:  | None = None,
    ref:  | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> EnumSchema

```

Returns a schema that matches an enum value, e.g.:
```
from enum import Enum
from pydantic_core import SchemaValidator, core_schema

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

schema = core_schema.enum_schema(Color, list(Color.__members__.values()))
v = SchemaValidator(schema)
assert v.validate_python(2) is Color.GREEN

```

Parameters:
Name | Type | Description | Default
---|---|---|---
`cls` |  |  The enum class |  _required_
`members` |  |  The members of the enum, generally `list(MyEnum.__members__.values())` |  _required_
`sub_type` |  |  The type of the enum, either 'str' or 'int' or None for plain enums |  `None`
`missing` |  |  A function to use when the value is not found in the enum, from `_missing_` |  `None`
`strict` |  |  Whether to use strict mode, defaults to False |  `None`
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`
Source code in `pydantic_core/core_schema.py`
```
1305
1306
1307
1308
1309
1310
1311
1312
1313
1314
1315
1316
1317
1318
1319
1320
1321
1322
1323
1324
1325
1326
1327
1328
1329
1330
1331
1332
1333
1334
1335
1336
1337
1338
1339
1340
1341
1342
1343
1344
1345
1346
1347
1348
1349
1350
1351
1352
1353
```
| ```
def enum_schema(
    cls: Any,
    members: list[Any],
    *,
    sub_type: Literal['str', 'int', 'float'] | None = None,
    missing: Callable[[Any], Any] | None = None,
    strict: bool | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> EnumSchema:
    """
    Returns a schema that matches an enum value, e.g.:

```py
    from enum import Enum
    from pydantic_core import SchemaValidator, core_schema

    class Color(Enum):
        RED = 1
        GREEN = 2
        BLUE = 3

    schema = core_schema.enum_schema(Color, list(Color.__members__.values()))
    v = SchemaValidator(schema)
    assert v.validate_python(2) is Color.GREEN
```

    Args:
        cls: The enum class
        members: The members of the enum, generally `list(MyEnum.__members__.values())`
        sub_type: The type of the enum, either 'str' or 'int' or None for plain enums
        missing: A function to use when the value is not found in the enum, from `_missing_`
        strict: Whether to use strict mode, defaults to False
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='enum',
        cls=cls,
        members=members,
        sub_type=sub_type,
        missing=missing,
        strict=strict,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
    )

```

---|---
##  missing_sentinel_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.missing_sentinel_schema)
```
missing_sentinel_schema(
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None,
) -> MissingSentinelSchema

```

Returns a schema for the `MISSING` sentinel.
Source code in `pydantic_core/core_schema.py`
```
1362
1363
1364
1365
1366
1367
1368
1369
1370
1371
1372
```
| ```
def missing_sentinel_schema(
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> MissingSentinelSchema:
    """Returns a schema for the `MISSING` sentinel."""

    return _dict_not_none(
        type='missing-sentinel',
        metadata=metadata,
        serialization=serialization,
    )

```

---|---
