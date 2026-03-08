##  time_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.time_schema)
```
time_schema(
    *,
    strict:  | None = None,
    le:  | None = None,
    ge:  | None = None,
    lt:  | None = None,
    gt:  | None = None,
    tz_constraint: (
        ["aware", "naive"] |  | None
    ) = None,
    microseconds_precision: [
        "truncate", "error"
    ] = "truncate",
    ref:  | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> TimeSchema

```

Returns a schema that matches a time value, e.g.:
```
from datetime import time
from pydantic_core import SchemaValidator, core_schema

schema = core_schema.time_schema(le=time(12, 0, 0), ge=time(6, 0, 0))
v = SchemaValidator(schema)
assert v.validate_python(time(9, 0, 0)) == time(9, 0, 0)

```

Parameters:
Name | Type | Description | Default
---|---|---|---
`strict` |  |  Whether the value should be a time or a value that can be converted to a time |  `None`
`le` |  |  The value must be less than or equal to this time |  `None`
`ge` |  |  The value must be greater than or equal to this time |  `None`
`lt` |  |  The value must be strictly less than this time |  `None`
`gt` |  |  The value must be strictly greater than this time |  `None`
`tz_constraint` |  |  The value must be timezone aware or naive, or an int to indicate required tz offset |  `None`
`microseconds_precision` |  |  The behavior when seconds have more than 6 digits or microseconds is too large |  `'truncate'`
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`
Source code in `pydantic_core/core_schema.py`
```
1066
1067
1068
1069
1070
1071
1072
1073
1074
1075
1076
1077
1078
1079
1080
1081
1082
1083
1084
1085
1086
1087
1088
1089
1090
1091
1092
1093
1094
1095
1096
1097
1098
1099
1100
1101
1102
1103
1104
1105
1106
1107
1108
1109
1110
1111
1112
1113
1114
1115
```
| ```
def time_schema(
    *,
    strict: bool | None = None,
    le: time | None = None,
    ge: time | None = None,
    lt: time | None = None,
    gt: time | None = None,
    tz_constraint: Literal['aware', 'naive'] | int | None = None,
    microseconds_precision: Literal['truncate', 'error'] = 'truncate',
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> TimeSchema:
    """
    Returns a schema that matches a time value, e.g.:

```py
    from datetime import time
    from pydantic_core import SchemaValidator, core_schema

    schema = core_schema.time_schema(le=time(12, 0, 0), ge=time(6, 0, 0))
    v = SchemaValidator(schema)
    assert v.validate_python(time(9, 0, 0)) == time(9, 0, 0)
```

    Args:
        strict: Whether the value should be a time or a value that can be converted to a time
        le: The value must be less than or equal to this time
        ge: The value must be greater than or equal to this time
        lt: The value must be strictly less than this time
        gt: The value must be strictly greater than this time
        tz_constraint: The value must be timezone aware or naive, or an int to indicate required tz offset
        microseconds_precision: The behavior when seconds have more than 6 digits or microseconds is too large
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='time',
        strict=strict,
        le=le,
        ge=ge,
        lt=lt,
        gt=gt,
        tz_constraint=tz_constraint,
        microseconds_precision=microseconds_precision,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
    )

```

---|---
##  datetime_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.datetime_schema)
```
datetime_schema(
    *,
    strict:  | None = None,
    le:  | None = None,
    ge:  | None = None,
    lt:  | None = None,
    gt:  | None = None,
    now_op: ["past", "future"] | None = None,
    tz_constraint: (
        ["aware", "naive"] |  | None
    ) = None,
    now_utc_offset:  | None = None,
    microseconds_precision: [
        "truncate", "error"
    ] = "truncate",
    ref:  | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> DatetimeSchema

```

Returns a schema that matches a datetime value, e.g.:
```
from datetime import datetime
from pydantic_core import SchemaValidator, core_schema

schema = core_schema.datetime_schema()
v = SchemaValidator(schema)
now = datetime.now()
assert v.validate_python(str(now)) == now

```

Parameters:
Name | Type | Description | Default
---|---|---|---
`strict` |  |  Whether the value should be a datetime or a value that can be converted to a datetime |  `None`
`le` |  |  The value must be less than or equal to this datetime |  `None`
`ge` |  |  The value must be greater than or equal to this datetime |  `None`
`lt` |  |  The value must be strictly less than this datetime |  `None`
`gt` |  |  The value must be strictly greater than this datetime |  `None`
`now_op` |  |  The value must be in the past or future relative to the current datetime |  `None`
`tz_constraint` |  |  The value must be timezone aware or naive, or an int to indicate required tz offset TODO: use of a tzinfo where offset changes based on the datetime is not yet supported |  `None`
`now_utc_offset` |  |  The value must be in the past or future relative to the current datetime with this utc offset |  `None`
`microseconds_precision` |  |  The behavior when seconds have more than 6 digits or microseconds is too large |  `'truncate'`
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`
Source code in `pydantic_core/core_schema.py`
```
1136
1137
1138
1139
1140
1141
1142
1143
1144
1145
1146
1147
1148
1149
1150
1151
1152
1153
1154
1155
1156
1157
1158
1159
1160
1161
1162
1163
1164
1165
1166
1167
1168
1169
1170
1171
1172
1173
1174
1175
1176
1177
1178
1179
1180
1181
1182
1183
1184
1185
1186
1187
1188
1189
1190
1191
1192
1193
```
| ```
def datetime_schema(
    *,
    strict: bool | None = None,
    le: datetime | None = None,
    ge: datetime | None = None,
    lt: datetime | None = None,
    gt: datetime | None = None,
    now_op: Literal['past', 'future'] | None = None,
    tz_constraint: Literal['aware', 'naive'] | int | None = None,
    now_utc_offset: int | None = None,
    microseconds_precision: Literal['truncate', 'error'] = 'truncate',
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> DatetimeSchema:
    """
    Returns a schema that matches a datetime value, e.g.:

```py
    from datetime import datetime
    from pydantic_core import SchemaValidator, core_schema

    schema = core_schema.datetime_schema()
    v = SchemaValidator(schema)
    now = datetime.now()
    assert v.validate_python(str(now)) == now
```

    Args:
        strict: Whether the value should be a datetime or a value that can be converted to a datetime
        le: The value must be less than or equal to this datetime
        ge: The value must be greater than or equal to this datetime
        lt: The value must be strictly less than this datetime
        gt: The value must be strictly greater than this datetime
        now_op: The value must be in the past or future relative to the current datetime
        tz_constraint: The value must be timezone aware or naive, or an int to indicate required tz offset
            TODO: use of a tzinfo where offset changes based on the datetime is not yet supported
        now_utc_offset: The value must be in the past or future relative to the current datetime with this utc offset
        microseconds_precision: The behavior when seconds have more than 6 digits or microseconds is too large
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='datetime',
        strict=strict,
        le=le,
        ge=ge,
        lt=lt,
        gt=gt,
        now_op=now_op,
        tz_constraint=tz_constraint,
        now_utc_offset=now_utc_offset,
        microseconds_precision=microseconds_precision,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
    )

```

---|---
