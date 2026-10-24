
```

Generates a JSON schema that matches a callable value.
Unless overridden in a subclass, this raises an error.
Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `CallableSchema` |  The core schema. |  _required_
Returns:
Type | Description
---|---
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.
Source code in `pydantic/json_schema.py`
```
937
938
939
940
941
942
943
944
945
946
947
948
```
| ```
def callable_schema(self, schema: core_schema.CallableSchema) -> JsonSchemaValue:
    """Generates a JSON schema that matches a callable value.

    Unless overridden in a subclass, this raises an error.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    return self.handle_invalid_for_json_schema(schema, 'core_schema.CallableSchema')

```

---|---
###  list_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.list_schema)
```
list_schema(schema: ListSchema) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Returns a schema that matches a list schema.
Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `ListSchema` |  The core schema. |  _required_
Returns:
Type | Description
---|---
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.
Source code in `pydantic/json_schema.py`
```
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
```
| ```
def list_schema(self, schema: core_schema.ListSchema) -> JsonSchemaValue:
    """Returns a schema that matches a list schema.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    items_schema = {} if 'items_schema' not in schema else self.generate_inner(schema['items_schema'])
    json_schema = {'type': 'array', 'items': items_schema}
    self.update_with_validations(json_schema, schema, self.ValidationsMapping.array)
    return json_schema

```

---|---
###  tuple_positional_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.tuple_positional_schema)
```
tuple_positional_schema(
    schema: TupleSchema,
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Replaced by `tuple_schema`.
Source code in `pydantic/json_schema.py`
```
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
```
| ```
@deprecated('`tuple_positional_schema` is deprecated. Use `tuple_schema` instead.', category=None)
@final
def tuple_positional_schema(self, schema: core_schema.TupleSchema) -> JsonSchemaValue:
    """Replaced by `tuple_schema`."""
    warnings.warn(
        '`tuple_positional_schema` is deprecated. Use `tuple_schema` instead.',
        PydanticDeprecatedSince26,
        stacklevel=2,
    )
    return self.tuple_schema(schema)

```

---|---
###  tuple_variable_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.tuple_variable_schema)
```
tuple_variable_schema(
    schema: TupleSchema,
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Replaced by `tuple_schema`.
Source code in `pydantic/json_schema.py`
```
975
976
977
978
979
980
981
982
983
984
```
| ```
@deprecated('`tuple_variable_schema` is deprecated. Use `tuple_schema` instead.', category=None)
@final
def tuple_variable_schema(self, schema: core_schema.TupleSchema) -> JsonSchemaValue:
    """Replaced by `tuple_schema`."""
    warnings.warn(
        '`tuple_variable_schema` is deprecated. Use `tuple_schema` instead.',
        PydanticDeprecatedSince26,
        stacklevel=2,
    )
    return self.tuple_schema(schema)

```

---|---
###  tuple_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.tuple_schema)
```
tuple_schema(schema: TupleSchema) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a tuple schema e.g. `tuple[int, str, bool]` or `tuple[int, ...]`.
Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `TupleSchema` |  The core schema. |  _required_
Returns:
Type | Description
---|---
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.
Source code in `pydantic/json_schema.py`
```
 986
 987
 988
 989
 990
 991
 992
 993
 994
 995
 996
 997
 998
 999
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
```
| ```
def tuple_schema(self, schema: core_schema.TupleSchema) -> JsonSchemaValue:
    """Generates a JSON schema that matches a tuple schema e.g. `tuple[int,
    str, bool]` or `tuple[int, ...]`.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    json_schema: JsonSchemaValue = {'type': 'array'}
    if 'variadic_item_index' in schema:
        variadic_item_index = schema['variadic_item_index']
        if variadic_item_index > 0:
            json_schema['minItems'] = variadic_item_index
            json_schema['prefixItems'] = [
                self.generate_inner(item) for item in schema['items_schema'][:variadic_item_index]
            ]
        if variadic_item_index + 1 == len(schema['items_schema']):
            # if the variadic item is the last item, then represent it faithfully
            json_schema['items'] = self.generate_inner(schema['items_schema'][variadic_item_index])
        else:
            # otherwise, 'items' represents the schema for the variadic
            # item plus the suffix, so just allow anything for simplicity
            # for now
            json_schema['items'] = True
    else:
        prefixItems = [self.generate_inner(item) for item in schema['items_schema']]
        if prefixItems:
            json_schema['prefixItems'] = prefixItems
        json_schema['minItems'] = len(prefixItems)
        json_schema['maxItems'] = len(prefixItems)
    self.update_with_validations(json_schema, schema, self.ValidationsMapping.array)
    return json_schema

```

---|---
###  set_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.set_schema)
```
set_schema(schema: SetSchema) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a set schema.
Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `SetSchema` |  The core schema. |  _required_
Returns:
Type | Description
---|---
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.
Source code in `pydantic/json_schema.py`
```
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
```
| ```
def set_schema(self, schema: core_schema.SetSchema) -> JsonSchemaValue:
    """Generates a JSON schema that matches a set schema.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    return self._common_set_schema(schema)

```

---|---
###  frozenset_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.frozenset_schema)
```
frozenset_schema(
    schema: FrozenSetSchema,
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a frozenset schema.
Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `FrozenSetSchema` |  The core schema. |  _required_
Returns:
Type | Description
---|---
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.
Source code in `pydantic/json_schema.py`
```
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
```
| ```
def frozenset_schema(self, schema: core_schema.FrozenSetSchema) -> JsonSchemaValue:
    """Generates a JSON schema that matches a frozenset schema.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    return self._common_set_schema(schema)

```

---|---
###  generator_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.generator_schema)
```
generator_schema(
    schema: GeneratorSchema,
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Returns a JSON schema that represents the provided GeneratorSchema.
Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `GeneratorSchema` |  The schema. |  _required_
Returns:
Type | Description
---|---
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.
Source code in `pydantic/json_schema.py`
```
1049
1050
1051
1052
1053
1054
1055
1056
1057
1058
1059
1060
1061
```
| ```
def generator_schema(self, schema: core_schema.GeneratorSchema) -> JsonSchemaValue:
    """Returns a JSON schema that represents the provided GeneratorSchema.

    Args:
        schema: The schema.

    Returns:
        The generated JSON schema.
    """
    items_schema = {} if 'items_schema' not in schema else self.generate_inner(schema['items_schema'])
    json_schema = {'type': 'array', 'items': items_schema}
    self.update_with_validations(json_schema, schema, self.ValidationsMapping.array)
    return json_schema

```

---|---
###  dict_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.dict_schema)
```
dict_schema(schema: DictSchema) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a dict schema.
Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `DictSchema` |  The core schema. |  _required_
Returns:
Type | Description
---|---
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.
Source code in `pydantic/json_schema.py`
```
1063
1064
1065
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
```
| ```
def dict_schema(self, schema: core_schema.DictSchema) -> JsonSchemaValue:
    """Generates a JSON schema that matches a dict schema.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    json_schema: JsonSchemaValue = {'type': 'object'}

    keys_schema = self.generate_inner(schema['keys_schema']).copy() if 'keys_schema' in schema else {}
    if '$ref' not in keys_schema:
        keys_pattern = keys_schema.pop('pattern', None)
        # Don't give a title to patternProperties/propertyNames:
        keys_schema.pop('title', None)
    else:
        # Here, we assume that if the keys schema is a definition reference,
        # it can't be a simple string core schema (and thus no pattern can exist).
        # However, this is only in practice (in theory, a definition reference core
        # schema could be generated for a simple string schema).
        # Note that we avoid calling `self.resolve_ref_schema`, as it might not exist yet.
        keys_pattern = None

    values_schema = self.generate_inner(schema['values_schema']).copy() if 'values_schema' in schema else {}
    # don't give a title to additionalProperties:
    values_schema.pop('title', None)

    if values_schema or keys_pattern is not None:
        if keys_pattern is None:
            json_schema['additionalProperties'] = values_schema
        else:
            json_schema['patternProperties'] = {keys_pattern: values_schema}
    else:  # for `dict[str, Any]`, we allow any key and any value, since `str` is the default key type
        json_schema['additionalProperties'] = True

    if (
        # The len check indicates that constraints are probably present:
        (keys_schema.get('type') == 'string' and len(keys_schema) > 1)
        # If this is a definition reference schema, it most likely has constraints:
        or '$ref' in keys_schema
    ):
        keys_schema.pop('type', None)
        json_schema['propertyNames'] = keys_schema

    self.update_with_validations(json_schema, schema, self.ValidationsMapping.object)
    return json_schema

```

---|---
###  function_before_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.function_before_schema)
```
function_before_schema(
    schema: BeforeValidatorFunctionSchema,
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a function-before schema.
Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `BeforeValidatorFunctionSchema` |  The core schema. |  _required_
Returns:
Type | Description
---|---
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.
Source code in `pydantic/json_schema.py`
```
1111
1112
1113
1114
1115
1116
1117
1118
1119
1120
1121
1122
1123
```
| ```
def function_before_schema(self, schema: core_schema.BeforeValidatorFunctionSchema) -> JsonSchemaValue:
    """Generates a JSON schema that matches a function-before schema.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    if self.mode == 'validation' and (input_schema := schema.get('json_schema_input_schema')):
        return self.generate_inner(input_schema)

    return self.generate_inner(schema['schema'])

```

---|---
###  function_after_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.function_after_schema)
```
function_after_schema(
    schema: AfterValidatorFunctionSchema,
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a function-after schema.
Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `AfterValidatorFunctionSchema` |  The core schema. |  _required_
Returns:
Type | Description
---|---
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.
Source code in `pydantic/json_schema.py`
```
1125
1126
1127
1128
1129
1130
1131
1132
1133
1134
```
| ```
def function_after_schema(self, schema: core_schema.AfterValidatorFunctionSchema) -> JsonSchemaValue:
    """Generates a JSON schema that matches a function-after schema.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    return self.generate_inner(schema['schema'])

```

---|---
###  function_plain_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.function_plain_schema)
```
function_plain_schema(
    schema: PlainValidatorFunctionSchema,
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a function-plain schema.
Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `PlainValidatorFunctionSchema` |  The core schema. |  _required_
Returns:
Type | Description
---|---
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.
Source code in `pydantic/json_schema.py`
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
```
| ```
def function_plain_schema(self, schema: core_schema.PlainValidatorFunctionSchema) -> JsonSchemaValue:
    """Generates a JSON schema that matches a function-plain schema.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    if self.mode == 'validation' and (input_schema := schema.get('json_schema_input_schema')):
        return self.generate_inner(input_schema)

    return self.handle_invalid_for_json_schema(
        schema, f'core_schema.PlainValidatorFunctionSchema ({schema["function"]})'
    )

```

---|---
###  function_wrap_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.function_wrap_schema)
```
function_wrap_schema(
    schema: WrapValidatorFunctionSchema,
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a function-wrap schema.
Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `WrapValidatorFunctionSchema` |  The core schema. |  _required_
Returns:
Type | Description
---|---
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.
Source code in `pydantic/json_schema.py`
```
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
```
| ```
def function_wrap_schema(self, schema: core_schema.WrapValidatorFunctionSchema) -> JsonSchemaValue:
    """Generates a JSON schema that matches a function-wrap schema.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    if self.mode == 'validation' and (input_schema := schema.get('json_schema_input_schema')):
        return self.generate_inner(input_schema)

    return self.generate_inner(schema['schema'])

```

---|---
###  default_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.default_schema)
```
default_schema(
    schema: WithDefaultSchema,
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a schema with a default value.
Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `WithDefaultSchema` |  The core schema. |  _required_
Returns:
Type | Description
---|---
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.
Source code in `pydantic/json_schema.py`
```
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
1194
1195
1196
1197
1198
1199
1200
1201
1202
1203
1204
1205
1206
1207
1208
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
```
| ```
def default_schema(self, schema: core_schema.WithDefaultSchema) -> JsonSchemaValue:
    """Generates a JSON schema that matches a schema with a default value.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    json_schema = self.generate_inner(schema['schema'])

    default = self.get_default_value(schema)
    if default is NoDefault or default is MISSING:
        return json_schema

    # we reflect the application of custom plain, no-info serializers to defaults for
    # JSON Schemas viewed in serialization mode:
    # TODO: improvements along with https://github.com/pydantic/pydantic/issues/8208
    if self.mode == 'serialization':
        # `_get_ser_schema_for_default_value()` is used to unpack potentially nested validator schemas:
        ser_schema = _get_ser_schema_for_default_value(schema['schema'])
        if (
            ser_schema is not None
            and (ser_func := ser_schema.get('function'))
            and not (default is None and ser_schema.get('when_used') in ('unless-none', 'json-unless-none'))
        ):
            try:
                default = ser_func(default)  # type: ignore
            except Exception:
                # It might be that the provided default needs to be validated (read: parsed) first
                # (assuming `validate_default` is enabled). However, we can't perform
                # such validation during JSON Schema generation so we don't support
                # this pattern for now.
                # (One example is when using `foo: ByteSize = '1MB'`, which validates and
                # serializes as an int. In this case, `ser_func` is `int` and `int('1MB')` fails).
                self.emit_warning(
                    'non-serializable-default',
                    f'Unable to serialize value {default!r} with the plain serializer; excluding default from JSON schema',
                )
                return json_schema

    try:
        encoded_default = self.encode_default(default)
    except pydantic_core.PydanticSerializationError:
        self.emit_warning(
            'non-serializable-default',
            f'Default value {default} is not JSON serializable; excluding default from JSON schema',
        )
        # Return the inner schema, as though there was no default
        return json_schema

    json_schema['default'] = encoded_default
    return json_schema

```

---|---
###  get_default_value [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.get_default_value)
```
get_default_value(schema: WithDefaultSchema) ->

```

Get the default value to be used when generating a JSON Schema for a core schema with a default.
The default implementation is to use the statically defined default value. This method can be overridden if you want to make use of the default factory.
Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `WithDefaultSchema` |  The `'with-default'` core schema. |  _required_
Returns:
Type | Description
---|---
|  The default value to use, or [`NoDefault`](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.NoDefault) if no default value is available.
Source code in `pydantic/json_schema.py`
```
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
```
| ```
def get_default_value(self, schema: core_schema.WithDefaultSchema) -> Any:
    """Get the default value to be used when generating a JSON Schema for a core schema with a default.

    The default implementation is to use the statically defined default value. This method can be overridden
    if you want to make use of the default factory.

    Args:
        schema: The `'with-default'` core schema.

    Returns:
        The default value to use, or [`NoDefault`][pydantic.json_schema.NoDefault] if no default
            value is available.
    """
    return schema.get('default', NoDefault)

```

---|---
###  nullable_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.nullable_schema)
```
nullable_schema(schema: NullableSchema) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a schema that allows null values.
Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `NullableSchema` |  The core schema. |  _required_
Returns:
Type | Description
---|---
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.
Source code in `pydantic/json_schema.py`
```
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
```
| ```
def nullable_schema(self, schema: core_schema.NullableSchema) -> JsonSchemaValue:
    """Generates a JSON schema that matches a schema that allows null values.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    null_schema = {'type': 'null'}
    inner_json_schema = self.generate_inner(schema['schema'])

    if inner_json_schema == null_schema:
        return null_schema
    else:
        return self.get_union_of_schemas([inner_json_schema, null_schema])

```

---|---
###  union_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.union_schema)
```
union_schema(schema: UnionSchema) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a schema that allows values matching any of the given schemas.
Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `UnionSchema` |  The core schema. |  _required_
Returns:
Type | Description
---|---
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.
Source code in `pydantic/json_schema.py`
```
1252
1253
1254
1255
1256
1257
1258
1259
1260
1261
1262
1263
1264
1265
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
```
| ```
def union_schema(self, schema: core_schema.UnionSchema) -> JsonSchemaValue:
    """Generates a JSON schema that matches a schema that allows values matching any of the given schemas.

    Args:
        schema: The core schema.

    Returns:
