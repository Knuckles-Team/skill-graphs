##  bytes_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.bytes_schema)
```
bytes_schema(
    *,
    max_length:  | None = None,
    min_length:  | None = None,
    strict:  | None = None,
    ref:  | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> BytesSchema

```

Returns a schema that matches a bytes value, e.g.:
```
from pydantic_core import SchemaValidator, core_schema

schema = core_schema.bytes_schema(max_length=10, min_length=2)
v = SchemaValidator(schema)
assert v.validate_python(b'hello') == b'hello'

```

Parameters:
Name | Type | Description | Default
---|---|---|---
`max_length` |  |  The value must be at most this length |  `None`
`min_length` |  |  The value must be at least this length |  `None`
`strict` |  |  Whether the value should be a bytes or a value that can be converted to a bytes |  `None`
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`
Source code in `pydantic_core/core_schema.py`
```
945
946
947
948
949
950
951
952
953
954
955
956
957
958
959
960
961
962
963
964
965
966
967
968
969
970
971
972
973
974
975
976
977
978
979
980
981
```
| ```
def bytes_schema(
    *,
    max_length: int | None = None,
    min_length: int | None = None,
    strict: bool | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> BytesSchema:
    """
    Returns a schema that matches a bytes value, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    schema = core_schema.bytes_schema(max_length=10, min_length=2)
    v = SchemaValidator(schema)
    assert v.validate_python(b'hello') == b'hello'
```

    Args:
        max_length: The value must be at most this length
        min_length: The value must be at least this length
        strict: Whether the value should be a bytes or a value that can be converted to a bytes
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='bytes',
        max_length=max_length,
        min_length=min_length,
        strict=strict,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
    )

```

---|---
##  date_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.date_schema)
```
date_schema(
    *,
    strict:  | None = None,
    le:  | None = None,
    ge:  | None = None,
    lt:  | None = None,
    gt:  | None = None,
    now_op: ["past", "future"] | None = None,
    now_utc_offset:  | None = None,
    ref:  | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> DateSchema

```

Returns a schema that matches a date value, e.g.:
```
from datetime import date
from pydantic_core import SchemaValidator, core_schema

schema = core_schema.date_schema(le=date(2020, 1, 1), ge=date(2019, 1, 1))
v = SchemaValidator(schema)
assert v.validate_python(date(2019, 6, 1)) == date(2019, 6, 1)

```

Parameters:
Name | Type | Description | Default
---|---|---|---
`strict` |  |  Whether the value should be a date or a value that can be converted to a date |  `None`
`le` |  |  The value must be less than or equal to this date |  `None`
`ge` |  |  The value must be greater than or equal to this date |  `None`
`lt` |  |  The value must be strictly less than this date |  `None`
`gt` |  |  The value must be strictly greater than this date |  `None`
`now_op` |  |  The value must be in the past or future relative to the current date |  `None`
`now_utc_offset` |  |  The value must be in the past or future relative to the current date with this utc offset |  `None`
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`
Source code in `pydantic_core/core_schema.py`
```
1000
1001
1002
1003
1004
1005
1006
1007
1008
1009
1010
1011
1012
1013
1014
1015
1016
1017
1018
1019
1020
1021
1022
1023
1024
1025
1026
1027
1028
1029
1030
1031
1032
1033
1034
1035
1036
1037
1038
1039
1040
1041
1042
1043
1044
1045
1046
1047
1048
1049
```
| ```
def date_schema(
    *,
    strict: bool | None = None,
    le: date | None = None,
    ge: date | None = None,
    lt: date | None = None,
    gt: date | None = None,
    now_op: Literal['past', 'future'] | None = None,
    now_utc_offset: int | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> DateSchema:
    """
    Returns a schema that matches a date value, e.g.:

```py
    from datetime import date
    from pydantic_core import SchemaValidator, core_schema

    schema = core_schema.date_schema(le=date(2020, 1, 1), ge=date(2019, 1, 1))
    v = SchemaValidator(schema)
    assert v.validate_python(date(2019, 6, 1)) == date(2019, 6, 1)
```

    Args:
        strict: Whether the value should be a date or a value that can be converted to a date
        le: The value must be less than or equal to this date
        ge: The value must be greater than or equal to this date
        lt: The value must be strictly less than this date
        gt: The value must be strictly greater than this date
        now_op: The value must be in the past or future relative to the current date
        now_utc_offset: The value must be in the past or future relative to the current date with this utc offset
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='date',
        strict=strict,
        le=le,
        ge=ge,
        lt=lt,
        gt=gt,
        now_op=now_op,
        now_utc_offset=now_utc_offset,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
    )

```

---|---
