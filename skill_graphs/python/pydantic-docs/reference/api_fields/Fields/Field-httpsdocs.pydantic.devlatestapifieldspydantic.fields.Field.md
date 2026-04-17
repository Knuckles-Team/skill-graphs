##  Field [¶](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field)
```
Field(
    default: ellipsis,
    *,
    alias:  | None = _Unset,
    alias_priority:  | None = _Unset,
    validation_alias: (
         | AliasPath[](https://docs.pydantic.dev/latest/api/aliases/#pydantic.aliases.AliasPath) | AliasChoices[](https://docs.pydantic.dev/latest/api/aliases/#pydantic.aliases.AliasChoices) | None
    ) = _Unset,
    serialization_alias:  | None = _Unset,
    title:  | None = _Unset,
    field_title_generator: (
        [[, FieldInfo[](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.FieldInfo)], ] | None
    ) = _Unset,
    description:  | None = _Unset,
    examples: [] | None = _Unset,
    exclude:  | None = _Unset,
    exclude_if: [[], ] | None = _Unset,
    discriminator:  | Discriminator[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Discriminator) | None = _Unset,
    deprecated: Deprecated |  |  | None = _Unset,
    json_schema_extra: (
        JsonDict | [[JsonDict], None] | None
    ) = _Unset,
    frozen:  | None = _Unset,
    validate_default:  | None = _Unset,
    repr:  = _Unset,
    init:  | None = _Unset,
    init_var:  | None = _Unset,
    kw_only:  | None = _Unset,
    pattern:  | [] | None = _Unset,
    strict:  | None = _Unset,
    coerce_numbers_to_str:  | None = _Unset,
    gt: SupportsGt | None = _Unset,
    ge: SupportsGe | None = _Unset,
    lt: SupportsLt | None = _Unset,
    le: SupportsLe | None = _Unset,
    multiple_of:  | None = _Unset,
    allow_inf_nan:  | None = _Unset,
    max_digits:  | None = _Unset,
    decimal_places:  | None = _Unset,
    min_length:  | None = _Unset,
    max_length:  | None = _Unset,
    union_mode: ["smart", "left_to_right"] = _Unset,
    fail_fast:  | None = _Unset,
    **extra: [_EmptyKwargs]
) ->

```

```
Field(
    default: ,
    *,
    alias:  | None = _Unset,
    alias_priority:  | None = _Unset,
    validation_alias: (
         | AliasPath[](https://docs.pydantic.dev/latest/api/aliases/#pydantic.aliases.AliasPath) | AliasChoices[](https://docs.pydantic.dev/latest/api/aliases/#pydantic.aliases.AliasChoices) | None
    ) = _Unset,
    serialization_alias:  | None = _Unset,
    title:  | None = _Unset,
    field_title_generator: (
        [[, FieldInfo[](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.FieldInfo)], ] | None
    ) = _Unset,
    description:  | None = _Unset,
    examples: [] | None = _Unset,
    exclude:  | None = _Unset,
    exclude_if: [[], ] | None = _Unset,
    discriminator:  | Discriminator[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Discriminator) | None = _Unset,
    deprecated: Deprecated |  |  | None = _Unset,
    json_schema_extra: (
        JsonDict | [[JsonDict], None] | None
    ) = _Unset,
    frozen:  | None = _Unset,
    validate_default: [True],
    repr:  = _Unset,
    init:  | None = _Unset,
    init_var:  | None = _Unset,
    kw_only:  | None = _Unset,
    pattern:  | [] | None = _Unset,
    strict:  | None = _Unset,
    coerce_numbers_to_str:  | None = _Unset,
    gt: SupportsGt | None = _Unset,
    ge: SupportsGe | None = _Unset,
    lt: SupportsLt | None = _Unset,
    le: SupportsLe | None = _Unset,
    multiple_of:  | None = _Unset,
    allow_inf_nan:  | None = _Unset,
    max_digits:  | None = _Unset,
    decimal_places:  | None = _Unset,
    min_length:  | None = _Unset,
    max_length:  | None = _Unset,
    union_mode: ["smart", "left_to_right"] = _Unset,
    fail_fast:  | None = _Unset,
    **extra: [_EmptyKwargs]
) ->

```

```
Field(
    default: _T,
    *,
    alias:  | None = _Unset,
    alias_priority:  | None = _Unset,
    validation_alias: (
         | AliasPath[](https://docs.pydantic.dev/latest/api/aliases/#pydantic.aliases.AliasPath) | AliasChoices[](https://docs.pydantic.dev/latest/api/aliases/#pydantic.aliases.AliasChoices) | None
    ) = _Unset,
    serialization_alias:  | None = _Unset,
    title:  | None = _Unset,
    field_title_generator: (
        [[, FieldInfo[](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.FieldInfo)], ] | None
    ) = _Unset,
    description:  | None = _Unset,
    examples: [] | None = _Unset,
    exclude:  | None = _Unset,
    exclude_if: [[], ] | None = _Unset,
    discriminator:  | Discriminator[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Discriminator) | None = _Unset,
    deprecated: Deprecated |  |  | None = _Unset,
    json_schema_extra: (
        JsonDict | [[JsonDict], None] | None
    ) = _Unset,
    frozen:  | None = _Unset,
    validate_default: [False] = ...,
    repr:  = _Unset,
    init:  | None = _Unset,
    init_var:  | None = _Unset,
    kw_only:  | None = _Unset,
    pattern:  | [] | None = _Unset,
    strict:  | None = _Unset,
    coerce_numbers_to_str:  | None = _Unset,
    gt: SupportsGt | None = _Unset,
    ge: SupportsGe | None = _Unset,
    lt: SupportsLt | None = _Unset,
    le: SupportsLe | None = _Unset,
    multiple_of:  | None = _Unset,
    allow_inf_nan:  | None = _Unset,
    max_digits:  | None = _Unset,
    decimal_places:  | None = _Unset,
    min_length:  | None = _Unset,
    max_length:  | None = _Unset,
    union_mode: ["smart", "left_to_right"] = _Unset,
    fail_fast:  | None = _Unset,
    **extra: [_EmptyKwargs]
) -> _T

```

```
Field(
    *,
    default_factory: (
        [[], ] | [[[, ]], ]
    ),
    alias:  | None = _Unset,
    alias_priority:  | None = _Unset,
    validation_alias: (
         | AliasPath[](https://docs.pydantic.dev/latest/api/aliases/#pydantic.aliases.AliasPath) | AliasChoices[](https://docs.pydantic.dev/latest/api/aliases/#pydantic.aliases.AliasChoices) | None
    ) = _Unset,
    serialization_alias:  | None = _Unset,
    title:  | None = _Unset,
    field_title_generator: (
        [[, FieldInfo[](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.FieldInfo)], ] | None
    ) = _Unset,
    description:  | None = _Unset,
    examples: [] | None = _Unset,
    exclude:  | None = _Unset,
    exclude_if: [[], ] | None = _Unset,
    discriminator:  | Discriminator[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Discriminator) | None = _Unset,
    deprecated: Deprecated |  |  | None = _Unset,
    json_schema_extra: (
        JsonDict | [[JsonDict], None] | None
    ) = _Unset,
    frozen:  | None = _Unset,
    validate_default: [True],
    repr:  = _Unset,
    init:  | None = _Unset,
    init_var:  | None = _Unset,
    kw_only:  | None = _Unset,
    pattern:  | [] | None = _Unset,
    strict:  | None = _Unset,
    coerce_numbers_to_str:  | None = _Unset,
    gt: SupportsGt | None = _Unset,
    ge: SupportsGe | None = _Unset,
    lt: SupportsLt | None = _Unset,
    le: SupportsLe | None = _Unset,
    multiple_of:  | None = _Unset,
    allow_inf_nan:  | None = _Unset,
    max_digits:  | None = _Unset,
    decimal_places:  | None = _Unset,
    min_length:  | None = _Unset,
    max_length:  | None = _Unset,
    union_mode: ["smart", "left_to_right"] = _Unset,
    fail_fast:  | None = _Unset,
    **extra: [_EmptyKwargs]
) ->

```

```
Field(
    *,
    default_factory: (
        [[], _T] | [[[, ]], _T]
    ),
    alias:  | None = _Unset,
    alias_priority:  | None = _Unset,
    validation_alias: (
         | AliasPath[](https://docs.pydantic.dev/latest/api/aliases/#pydantic.aliases.AliasPath) | AliasChoices[](https://docs.pydantic.dev/latest/api/aliases/#pydantic.aliases.AliasChoices) | None
    ) = _Unset,
    serialization_alias:  | None = _Unset,
    title:  | None = _Unset,
    field_title_generator: (
        [[, FieldInfo[](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.FieldInfo)], ] | None
    ) = _Unset,
    description:  | None = _Unset,
    examples: [] | None = _Unset,
    exclude:  | None = _Unset,
    exclude_if: [[], ] | None = _Unset,
    discriminator:  | Discriminator[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Discriminator) | None = _Unset,
    deprecated: Deprecated |  |  | None = _Unset,
    json_schema_extra: (
        JsonDict | [[JsonDict], None] | None
    ) = _Unset,
    frozen:  | None = _Unset,
    validate_default: [False] | None = _Unset,
    repr:  = _Unset,
    init:  | None = _Unset,
    init_var:  | None = _Unset,
    kw_only:  | None = _Unset,
    pattern:  | [] | None = _Unset,
    strict:  | None = _Unset,
    coerce_numbers_to_str:  | None = _Unset,
    gt: SupportsGt | None = _Unset,
    ge: SupportsGe | None = _Unset,
    lt: SupportsLt | None = _Unset,
    le: SupportsLe | None = _Unset,
    multiple_of:  | None = _Unset,
    allow_inf_nan:  | None = _Unset,
    max_digits:  | None = _Unset,
    decimal_places:  | None = _Unset,
    min_length:  | None = _Unset,
    max_length:  | None = _Unset,
    union_mode: ["smart", "left_to_right"] = _Unset,
    fail_fast:  | None = _Unset,
    **extra: [_EmptyKwargs]
) -> _T

```

```
Field(
    *,
    alias:  | None = _Unset,
    alias_priority:  | None = _Unset,
    validation_alias: (
         | AliasPath[](https://docs.pydantic.dev/latest/api/aliases/#pydantic.aliases.AliasPath) | AliasChoices[](https://docs.pydantic.dev/latest/api/aliases/#pydantic.aliases.AliasChoices) | None
    ) = _Unset,
    serialization_alias:  | None = _Unset,
    title:  | None = _Unset,
    field_title_generator: (
        [[, FieldInfo[](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.FieldInfo)], ] | None
    ) = _Unset,
    description:  | None = _Unset,
    examples: [] | None = _Unset,
    exclude:  | None = _Unset,
    exclude_if: [[], ] | None = _Unset,
    discriminator:  | Discriminator[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Discriminator) | None = _Unset,
    deprecated: Deprecated |  |  | None = _Unset,
    json_schema_extra: (
        JsonDict | [[JsonDict], None] | None
    ) = _Unset,
    frozen:  | None = _Unset,
    validate_default:  | None = _Unset,
    repr:  = _Unset,
    init:  | None = _Unset,
    init_var:  | None = _Unset,
    kw_only:  | None = _Unset,
    pattern:  | [] | None = _Unset,
    strict:  | None = _Unset,
    coerce_numbers_to_str:  | None = _Unset,
    gt: SupportsGt | None = _Unset,
    ge: SupportsGe | None = _Unset,
    lt: SupportsLt | None = _Unset,
    le: SupportsLe | None = _Unset,
    multiple_of:  | None = _Unset,
    allow_inf_nan:  | None = _Unset,
    max_digits:  | None = _Unset,
    decimal_places:  | None = _Unset,
    min_length:  | None = _Unset,
    max_length:  | None = _Unset,
    union_mode: ["smart", "left_to_right"] = _Unset,
    fail_fast:  | None = _Unset,
    **extra: [_EmptyKwargs]
) ->

```

```
Field(
    default:  = PydanticUndefined,
    *,
    default_factory: (
        [[], ]
        | [[[, ]], ]
        | None
    ) = _Unset,
    alias:  | None = _Unset,
    alias_priority:  | None = _Unset,
    validation_alias: (
         | AliasPath[](https://docs.pydantic.dev/latest/api/aliases/#pydantic.aliases.AliasPath) | AliasChoices[](https://docs.pydantic.dev/latest/api/aliases/#pydantic.aliases.AliasChoices) | None
    ) = _Unset,
    serialization_alias:  | None = _Unset,
    title:  | None = _Unset,
    field_title_generator: (
        [[, FieldInfo[](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.FieldInfo)], ] | None
    ) = _Unset,
    description:  | None = _Unset,
    examples: [] | None = _Unset,
    exclude:  | None = _Unset,
    exclude_if: [[], ] | None = _Unset,
    discriminator:  | Discriminator[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Discriminator) | None = _Unset,
    deprecated: Deprecated |  |  | None = _Unset,
    json_schema_extra: (
        JsonDict | [[JsonDict], None] | None
    ) = _Unset,
    frozen:  | None = _Unset,
    validate_default:  | None = _Unset,
    repr:  = _Unset,
    init:  | None = _Unset,
    init_var:  | None = _Unset,
    kw_only:  | None = _Unset,
    pattern:  | [] | None = _Unset,
    strict:  | None = _Unset,
    coerce_numbers_to_str:  | None = _Unset,
    gt: SupportsGt | None = _Unset,
    ge: SupportsGe | None = _Unset,
    lt: SupportsLt | None = _Unset,
    le: SupportsLe | None = _Unset,
    multiple_of:  | None = _Unset,
    allow_inf_nan:  | None = _Unset,
    max_digits:  | None = _Unset,
    decimal_places:  | None = _Unset,
    min_length:  | None = _Unset,
    max_length:  | None = _Unset,
    union_mode: ["smart", "left_to_right"] = _Unset,
    fail_fast:  | None = _Unset,
    **extra: [_EmptyKwargs]
) ->

```

Usage Documentation
[Fields](https://docs.pydantic.dev/latest/concepts/fields/)
Create a field for objects that can be configured.
Used to provide extra information about a field, either for the model schema or complex validation. Some arguments apply only to number fields (`int`, `float`, `Decimal`) and some apply only to `str`.
Note
  * Any `_Unset` objects will be replaced by the corresponding value defined in the `_DefaultValues` dictionary. If a key for the `_Unset` object is not found in the `_DefaultValues` dictionary, it will default to `None`


Parameters:
Name | Type | Description | Default
---|---|---|---
`default` |  |  Default value if the field is not set. |  `PydanticUndefined`
`default_factory` |  |  A callable to generate the default value. The callable can either take 0 arguments (in which case it is called as is) or a single argument containing the already validated data. |  `_Unset`
`alias` |  |  The name to use for the attribute when validating or serializing by alias. This is often used for things like converting between snake and camel case. |  `_Unset`
`alias_priority` |  |  Priority of the alias. This affects whether an alias generator is used. |  `_Unset`
`validation_alias` |  `AliasPath[](https://docs.pydantic.dev/latest/api/aliases/#pydantic.aliases.AliasPath) | AliasChoices[](https://docs.pydantic.dev/latest/api/aliases/#pydantic.aliases.AliasChoices) | None` |  Like `alias`, but only affects validation, not serialization. |  `_Unset`
`serialization_alias` |  |  Like `alias`, but only affects serialization, not validation. |  `_Unset`
`title` |  |  Human-readable title. |  `_Unset`
`field_title_generator` |  `FieldInfo[](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.FieldInfo)], ` |  A callable that takes a field name and returns title for it. |  `_Unset`
`description` |  |  Human-readable description. |  `_Unset`
`examples` |  |  Example values for this field. |  `_Unset`
`exclude` |  |  Whether to exclude the field from the model serialization. |  `_Unset`
`exclude_if` |  |  A callable that determines whether to exclude a field during serialization based on its value. |  `_Unset`
`discriminator` |  `Discriminator[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Discriminator) | None` |  Field name or Discriminator for discriminating the type in a tagged union. |  `_Unset`
`deprecated` |  `Deprecated | ` |  A deprecation message, an instance of `warnings.deprecated` or the `typing_extensions.deprecated` backport, or a boolean. If `True`, a default deprecation message will be emitted when accessing the field. |  `_Unset`
`json_schema_extra` |  `JsonDict | JsonDict], None] | None` |  A dict or callable to provide extra JSON schema properties. |  `_Unset`
`frozen` |  |  Whether the field is frozen. If true, attempts to change the value on an instance will raise an error. |  `_Unset`
`validate_default` |  |  If `True`, apply validation to the default value every time you create an instance. Otherwise, for performance reasons, the default value of the field is trusted and not validated. |  `_Unset`
`repr` |  |  A boolean indicating whether to include the field in the `__repr__` output. |  `_Unset`
`init` |  |  Whether the field should be included in the constructor of the dataclass. (Only applies to dataclasses.) |  `_Unset`
`init_var` |  |  Whether the field should _only_ be included in the constructor of the dataclass. (Only applies to dataclasses.) |  `_Unset`
`kw_only` |  |  Whether the field should be a keyword-only argument in the constructor of the dataclass. (Only applies to dataclasses.) |  `_Unset`
`coerce_numbers_to_str` |  |  Whether to enable coercion of any `Number` type to `str` (not applicable in `strict` mode). |  `_Unset`
`strict` |  |  If `True`, strict validation is applied to the field. See [Strict Mode](https://docs.pydantic.dev/latest/concepts/strict_mode/) for details. |  `_Unset`
`gt` |  `SupportsGt | None` |  Greater than. If set, value must be greater than this. Only applicable to numbers. |  `_Unset`
`ge` |  `SupportsGe | None` |  Greater than or equal. If set, value must be greater than or equal to this. Only applicable to numbers. |  `_Unset`
`lt` |  `SupportsLt | None` |  Less than. If set, value must be less than this. Only applicable to numbers. |  `_Unset`
`le` |  `SupportsLe | None` |  Less than or equal. If set, value must be less than or equal to this. Only applicable to numbers. |  `_Unset`
`multiple_of` |  |  Value must be a multiple of this. Only applicable to numbers. |  `_Unset`
`min_length` |  |  Minimum length for iterables. |  `_Unset`
`max_length` |  |  Maximum length for iterables. |  `_Unset`
`pattern` |  |  Pattern for strings (a regular expression). |  `_Unset`
`allow_inf_nan` |  |  Allow `inf`, `-inf`, `nan`. Only applicable to float and  |  `_Unset`
`max_digits` |  |  Maximum number of allow digits for strings. |  `_Unset`
`decimal_places` |  |  Maximum number of decimal places allowed for numbers. |  `_Unset`
`union_mode` |  |  The strategy to apply when validating a union. Can be `smart` (the default), or `left_to_right`. See [Union Mode](https://docs.pydantic.dev/latest/concepts/unions/#union-modes) for details. |  `_Unset`
`fail_fast` |  |  If `True`, validation will stop on the first error. If `False`, all validation errors will be collected. This option can be applied only to iterable types (list, tuple, set, and frozenset). |  `_Unset`
`extra` |  `_EmptyKwargs]` |  (Deprecated) Extra fields that will be included in the JSON schema. Warning The `extra` kwargs is deprecated. Use `json_schema_extra` instead. |  `{}`
Returns:
Type | Description
---|---
|  A new [`FieldInfo`](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.FieldInfo). The return annotation is `Any` so `Field` can be used on type-annotated fields without causing a type error.
Source code in `pydantic/fields.py`
```
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
1291
1292
1293
1294
1295
1296
1297
1298
1299
1300
1301
1302
1303
1304
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
1354
1355
1356
1357
1358
1359
1360
1361
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
1373
1374
1375
1376
1377
1378
1379
1380
1381
1382
1383
1384
1385
1386
1387
1388
1389
1390
1391
1392
1393
```
| ```
def Field(  # noqa: C901
    default: Any = PydanticUndefined,
    *,
    default_factory: Callable[[], Any] | Callable[[dict[str, Any]], Any] | None = _Unset,
    alias: str | None = _Unset,
    alias_priority: int | None = _Unset,
    validation_alias: str | AliasPath | AliasChoices | None = _Unset,
    serialization_alias: str | None = _Unset,
    title: str | None = _Unset,
    field_title_generator: Callable[[str, FieldInfo], str] | None = _Unset,
    description: str | None = _Unset,
    examples: list[Any] | None = _Unset,
    exclude: bool | None = _Unset,
    exclude_if: Callable[[Any], bool] | None = _Unset,
    discriminator: str | types.Discriminator | None = _Unset,
    deprecated: Deprecated | str | bool | None = _Unset,
    json_schema_extra: JsonDict | Callable[[JsonDict], None] | None = _Unset,
    frozen: bool | None = _Unset,
    validate_default: bool | None = _Unset,
    repr: bool = _Unset,
    init: bool | None = _Unset,
    init_var: bool | None = _Unset,
    kw_only: bool | None = _Unset,
    pattern: str | re.Pattern[str] | None = _Unset,
    strict: bool | None = _Unset,
    coerce_numbers_to_str: bool | None = _Unset,
    gt: annotated_types.SupportsGt | None = _Unset,
    ge: annotated_types.SupportsGe | None = _Unset,
    lt: annotated_types.SupportsLt | None = _Unset,
    le: annotated_types.SupportsLe | None = _Unset,
    multiple_of: float | None = _Unset,
    allow_inf_nan: bool | None = _Unset,
    max_digits: int | None = _Unset,
    decimal_places: int | None = _Unset,
    min_length: int | None = _Unset,
    max_length: int | None = _Unset,
    union_mode: Literal['smart', 'left_to_right'] = _Unset,
    fail_fast: bool | None = _Unset,
    **extra: Unpack[_EmptyKwargs],
) -> Any:
    """!!! abstract "Usage Documentation"
        [Fields](../concepts/fields.md)

    Create a field for objects that can be configured.

    Used to provide extra information about a field, either for the model schema or complex validation. Some arguments
    apply only to number fields (`int`, `float`, `Decimal`) and some apply only to `str`.

    Note:
        - Any `_Unset` objects will be replaced by the corresponding value defined in the `_DefaultValues` dictionary. If a key for the `_Unset` object is not found in the `_DefaultValues` dictionary, it will default to `None`

    Args:
        default: Default value if the field is not set.
        default_factory: A callable to generate the default value. The callable can either take 0 arguments
            (in which case it is called as is) or a single argument containing the already validated data.
        alias: The name to use for the attribute when validating or serializing by alias.
            This is often used for things like converting between snake and camel case.
        alias_priority: Priority of the alias. This affects whether an alias generator is used.
        validation_alias: Like `alias`, but only affects validation, not serialization.
        serialization_alias: Like `alias`, but only affects serialization, not validation.
        title: Human-readable title.
        field_title_generator: A callable that takes a field name and returns title for it.
        description: Human-readable description.
        examples: Example values for this field.
        exclude: Whether to exclude the field from the model serialization.
        exclude_if: A callable that determines whether to exclude a field during serialization based on its value.
        discriminator: Field name or Discriminator for discriminating the type in a tagged union.
        deprecated: A deprecation message, an instance of `warnings.deprecated` or the `typing_extensions.deprecated` backport,
            or a boolean. If `True`, a default deprecation message will be emitted when accessing the field.
        json_schema_extra: A dict or callable to provide extra JSON schema properties.
        frozen: Whether the field is frozen. If true, attempts to change the value on an instance will raise an error.
        validate_default: If `True`, apply validation to the default value every time you create an instance.
            Otherwise, for performance reasons, the default value of the field is trusted and not validated.
        repr: A boolean indicating whether to include the field in the `__repr__` output.
        init: Whether the field should be included in the constructor of the dataclass.
            (Only applies to dataclasses.)
        init_var: Whether the field should _only_ be included in the constructor of the dataclass.
            (Only applies to dataclasses.)
        kw_only: Whether the field should be a keyword-only argument in the constructor of the dataclass.
            (Only applies to dataclasses.)
        coerce_numbers_to_str: Whether to enable coercion of any `Number` type to `str` (not applicable in `strict` mode).
        strict: If `True`, strict validation is applied to the field.
            See [Strict Mode](../concepts/strict_mode.md) for details.
        gt: Greater than. If set, value must be greater than this. Only applicable to numbers.
        ge: Greater than or equal. If set, value must be greater than or equal to this. Only applicable to numbers.
        lt: Less than. If set, value must be less than this. Only applicable to numbers.
        le: Less than or equal. If set, value must be less than or equal to this. Only applicable to numbers.
        multiple_of: Value must be a multiple of this. Only applicable to numbers.
        min_length: Minimum length for iterables.
        max_length: Maximum length for iterables.
        pattern: Pattern for strings (a regular expression).
        allow_inf_nan: Allow `inf`, `-inf`, `nan`. Only applicable to float and [`Decimal`][decimal.Decimal] numbers.
        max_digits: Maximum number of allow digits for strings.
        decimal_places: Maximum number of decimal places allowed for numbers.
        union_mode: The strategy to apply when validating a union. Can be `smart` (the default), or `left_to_right`.
            See [Union Mode](../concepts/unions.md#union-modes) for details.
        fail_fast: If `True`, validation will stop on the first error. If `False`, all validation errors will be collected.
            This option can be applied only to iterable types (list, tuple, set, and frozenset).
        extra: (Deprecated) Extra fields that will be included in the JSON schema.

            !!! warning Deprecated
                The `extra` kwargs is deprecated. Use `json_schema_extra` instead.

    Returns:
        A new [`FieldInfo`][pydantic.fields.FieldInfo]. The return annotation is `Any` so `Field` can be used on
            type-annotated fields without causing a type error.
    """
    # Check deprecated and removed params from V1. This logic should eventually be removed.
    const = extra.pop('const', None)  # type: ignore
    if const is not None:
        raise PydanticUserError('`const` is removed, use `Literal` instead', code='removed-kwargs')

    min_items = extra.pop('min_items', None)  # type: ignore
    if min_items is not None:
        warn(
            '`min_items` is deprecated and will be removed, use `min_length` instead',
            PydanticDeprecatedSince20,
            stacklevel=2,
        )
        if min_length in (None, _Unset):
            min_length = min_items  # type: ignore

    max_items = extra.pop('max_items', None)  # type: ignore
    if max_items is not None:
        warn(
            '`max_items` is deprecated and will be removed, use `max_length` instead',
            PydanticDeprecatedSince20,
            stacklevel=2,
        )
        if max_length in (None, _Unset):
            max_length = max_items  # type: ignore

    unique_items = extra.pop('unique_items', None)  # type: ignore
    if unique_items is not None:
        raise PydanticUserError(
            (
                '`unique_items` is removed, use `Set` instead'
                '(this feature is discussed in https://github.com/pydantic/pydantic-core/issues/296)'
            ),
            code='removed-kwargs',
        )

    allow_mutation = extra.pop('allow_mutation', None)  # type: ignore
    if allow_mutation is not None:
        warn(
            '`allow_mutation` is deprecated and will be removed. use `frozen` instead',
            PydanticDeprecatedSince20,
            stacklevel=2,
        )
        if allow_mutation is False:
            frozen = True

    regex = extra.pop('regex', None)  # type: ignore
    if regex is not None:
        raise PydanticUserError('`regex` is removed. use `pattern` instead', code='removed-kwargs')

    if extra:
        warn(
            'Using extra keyword arguments on `Field` is deprecated and will be removed.'
            ' Use `json_schema_extra` instead.'
            f' (Extra keys: {", ".join(k.__repr__() for k in extra.keys())})',
            PydanticDeprecatedSince20,
            stacklevel=2,
        )
        if not json_schema_extra or json_schema_extra is _Unset:
            json_schema_extra = extra  # type: ignore

    if (
        validation_alias
        and validation_alias is not _Unset
        and not isinstance(validation_alias, (str, AliasChoices, AliasPath))
    ):
        raise TypeError('Invalid `validation_alias` type. it should be `str`, `AliasChoices`, or `AliasPath`')

    if serialization_alias in (_Unset, None) and isinstance(alias, str):
        serialization_alias = alias

    if validation_alias in (_Unset, None):
        validation_alias = alias

    include = extra.pop('include', None)  # type: ignore
    if include is not None:
        warn(
            '`include` is deprecated and does nothing. It will be removed, use `exclude` instead',
            PydanticDeprecatedSince20,
            stacklevel=2,
        )

    return FieldInfo.from_field(
        default,
        default_factory=default_factory,
        alias=alias,
        alias_priority=alias_priority,
        validation_alias=validation_alias,
        serialization_alias=serialization_alias,
        title=title,
        field_title_generator=field_title_generator,
        description=description,
        examples=examples,
        exclude=exclude,
        exclude_if=exclude_if,
        discriminator=discriminator,
        deprecated=deprecated,
        json_schema_extra=json_schema_extra,
        frozen=frozen,
        pattern=pattern,
        validate_default=validate_default,
        repr=repr,
        init=init,
        init_var=init_var,
        kw_only=kw_only,
        coerce_numbers_to_str=coerce_numbers_to_str,
        strict=strict,
        gt=gt,
        ge=ge,
        lt=lt,
        le=le,
        multiple_of=multiple_of,
        min_length=min_length,
        max_length=max_length,
        allow_inf_nan=allow_inf_nan,
        max_digits=max_digits,
        decimal_places=decimal_places,
        union_mode=union_mode,
        fail_fast=fail_fast,
    )

```

---|---
##  FieldInfo [¶](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.FieldInfo)
```
FieldInfo(**kwargs: [_FieldInfoInputs])

```

Bases: `Representation`
This class holds information about a field.
`FieldInfo` is used for any field definition regardless of whether the [`Field()`](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field) function is explicitly used.
Warning
The `FieldInfo` class is meant to expose information about a field in a Pydantic model or dataclass. `FieldInfo` instances shouldn't be instantiated directly, nor mutated.
If you need to derive a new model from another one and are willing to alter `FieldInfo` instances, refer to this [dynamic model example](https://docs.pydantic.dev/latest/examples/dynamic_models/).
Attributes:
Name | Type | Description
---|---|---
`annotation` |  |  The type annotation of the field.
`default` |  |  The default value of the field.
`default_factory` |  |  A callable to generate the default value. The callable can either take 0 arguments (in which case it is called as is) or a single argument containing the already validated data.
`alias` |  |  The alias name of the field.
`alias_priority` |  |  The priority of the field's alias.
`validation_alias` |  `AliasPath[](https://docs.pydantic.dev/latest/api/aliases/#pydantic.aliases.AliasPath) | AliasChoices[](https://docs.pydantic.dev/latest/api/aliases/#pydantic.aliases.AliasChoices) | None` |  The validation alias of the field.
`serialization_alias` |  |  The serialization alias of the field.
`title` |  |  The title of the field.
`field_title_generator` |  `FieldInfo[](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.FieldInfo)], ` |  A callable that takes a field name and returns title for it.
`description` |  |  The description of the field.
`examples` |  |  List of examples of the field.
`exclude` |  |  Whether to exclude the field from the model serialization.
`exclude_if` |  |  A callable that determines whether to exclude a field during serialization based on its value.
`discriminator` |  `Discriminator[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Discriminator) | None` |  Field name or Discriminator for discriminating the type in a tagged union.
`deprecated` |  `Deprecated | ` |  A deprecation message, an instance of `warnings.deprecated` or the `typing_extensions.deprecated` backport, or a boolean. If `True`, a default deprecation message will be emitted when accessing the field.
`json_schema_extra` |  `JsonDict | JsonDict], None] | None` |  A dict or callable to provide extra JSON schema properties.
`frozen` |  |  Whether the field is frozen.
`validate_default` |  |  Whether to validate the default value of the field.
`repr` |  |  Whether to include the field in representation of the model.
`init` |  |  Whether the field should be included in the constructor of the dataclass.
`init_var` |  |  Whether the field should _only_ be included in the constructor of the dataclass, and not stored.
`kw_only` |  |  Whether the field should be a keyword-only argument in the constructor of the dataclass.
`metadata` |  |  The metadata list. Contains all the data that isn't expressed as direct `FieldInfo` attributes, including:
  * Type-specific constraints, such as `gt` or `min_length` (these are converted to metadata classes such as `annotated_types.Gt`).
  * Any other arbitrary object used within [custom types handlers](https://docs.pydantic.dev/latest/concepts/types/#as-an-annotation) or any object not recognized by Pydantic).


See the signature of `pydantic.fields.Field` for more details about the expected arguments.
Source code in `pydantic/fields.py`
```
228
229
230
231
232
233
234
235
236
237
238
239
240
241
242
243
244
245
246
247
248
249
250
251
252
253
254
255
256
257
258
259
260
261
262
263
264
265
266
267
268
269
270
271
272
273
274
275
276
277
278
279
280
281
282
283
284
285
286
287
288
```
| ```
def __init__(self, **kwargs: Unpack[_FieldInfoInputs]) -> None:
    """This class should generally not be initialized directly; instead, use the `pydantic.fields.Field` function
    or one of the constructor classmethods.

    See the signature of `pydantic.fields.Field` for more details about the expected arguments.
    """
    # Tracking the explicitly set attributes is necessary to correctly merge `Field()` functions
    # (e.g. with `Annotated[int, Field(alias='a'), Field(alias=None)]`, even though `None` is the default value,
    # we need to track that `alias=None` was explicitly set):
    self._attributes_set = {k: v for k, v in kwargs.items() if v is not _Unset and k not in self.metadata_lookup}
    kwargs = {k: _DefaultValues.get(k) if v is _Unset else v for k, v in kwargs.items()}  # type: ignore
    self.annotation = kwargs.get('annotation')

    # Note: in theory, the second `pop()` arguments are not required below, as defaults are already set from `_DefaultsValues`.
    default = kwargs.pop('default', PydanticUndefined)
    if default is Ellipsis:
        self.default = PydanticUndefined
        self._attributes_set.pop('default', None)
    else:
        self.default = default

    self.default_factory = kwargs.pop('default_factory', None)

    if self.default is not PydanticUndefined and self.default_factory is not None:
        raise TypeError('cannot specify both default and default_factory')

    self.alias = kwargs.pop('alias', None)
    self.validation_alias = kwargs.pop('validation_alias', None)
    self.serialization_alias = kwargs.pop('serialization_alias', None)
    alias_is_set = any(alias is not None for alias in (self.alias, self.validation_alias, self.serialization_alias))
    self.alias_priority = kwargs.pop('alias_priority', None) or 2 if alias_is_set else None
    self.title = kwargs.pop('title', None)
    self.field_title_generator = kwargs.pop('field_title_generator', None)
    self.description = kwargs.pop('description', None)
    self.examples = kwargs.pop('examples', None)
    self.exclude = kwargs.pop('exclude', None)
    self.exclude_if = kwargs.pop('exclude_if', None)
    self.discriminator = kwargs.pop('discriminator', None)
    # For compatibility with FastAPI<=0.110.0, we preserve the existing value if it is not overridden
    self.deprecated = kwargs.pop('deprecated', getattr(self, 'deprecated', None))
    self.repr = kwargs.pop('repr', True)
    self.json_schema_extra = kwargs.pop('json_schema_extra', None)
    self.validate_default = kwargs.pop('validate_default', None)
    self.frozen = kwargs.pop('frozen', None)
    # currently only used on dataclasses
    self.init = kwargs.pop('init', None)
    self.init_var = kwargs.pop('init_var', None)
    self.kw_only = kwargs.pop('kw_only', None)

    self.metadata = self._collect_metadata(kwargs)  # type: ignore

    # Private attributes:
    self._qualifiers: set[Qualifier] = set()
    # Used to rebuild FieldInfo instances:
    self._complete = True
    self._original_annotation: Any = PydanticUndefined
    self._original_assignment: Any = PydanticUndefined
    # Used to track whether the `FieldInfo` instance represents the data about a field (and is exposed in `model_fields`/`__pydantic_fields__`),
    # or if it is the result of the `Field()` function being used as metadata in an `Annotated` type/as an assignment
    # (not an ideal pattern, see https://github.com/pydantic/pydantic/issues/11122):
    self._final = False

```

---|---
###  deprecation_message `property` [¶](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.FieldInfo.deprecation_message)
```
deprecation_message:  | None

```

The deprecation message to be emitted, or `None` if not set.
###  default_factory_takes_validated_data `property` [¶](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.FieldInfo.default_factory_takes_validated_data)
```
default_factory_takes_validated_data:  | None

```

Whether the provided default factory callable has a validated data parameter.
Returns `None` if no default factory is set.
###  get_default [¶](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.FieldInfo.get_default)
```
get_default(
    *,
    call_default_factory: [True],
    validated_data: [, ] | None = None
) ->

```

```
get_default(
    *, call_default_factory: [False] = ...
) ->

```

```
get_default(
    *,
    call_default_factory:  = False,
    validated_data: [, ] | None = None
) ->

```

Get the default value.
We expose an option for whether to call the default_factory (if present), as calling it may result in side effects that we want to avoid. However, there are times when it really should be called (namely, when instantiating a model via `model_construct`).
Parameters:
Name | Type | Description | Default
---|---|---|---
`call_default_factory` |  |  Whether to call the default factory or not. |  `False`
`validated_data` |  |  The already validated data to be passed to the default factory. |  `None`
Returns:
Type | Description
---|---
|  The default value, calling the default factory if requested or `None` if not set.
Source code in `pydantic/fields.py`
```
721
722
723
724
725
726
727
728
729
730
731
732
733
734
735
736
737
738
739
740
741
742
743
744
745
746
747
748
749
```
| ```
def get_default(self, *, call_default_factory: bool = False, validated_data: dict[str, Any] | None = None) -> Any:
    """Get the default value.

    We expose an option for whether to call the default_factory (if present), as calling it may
    result in side effects that we want to avoid. However, there are times when it really should
    be called (namely, when instantiating a model via `model_construct`).

    Args:
        call_default_factory: Whether to call the default factory or not.
        validated_data: The already validated data to be passed to the default factory.

    Returns:
        The default value, calling the default factory if requested or `None` if not set.
    """
    if self.default_factory is None:
        return _utils.smart_deepcopy(self.default)
    elif call_default_factory:
        if self.default_factory_takes_validated_data:
            fac = cast('Callable[[dict[str, Any]], Any]', self.default_factory)
            if validated_data is None:
                raise ValueError(
                    "The default factory requires the 'validated_data' argument, which was not provided when calling 'get_default'."
                )
            return fac(validated_data)
        else:
            fac = cast('Callable[[], Any]', self.default_factory)
            return fac()
    else:
        return None

```

---|---
###  is_required [¶](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.FieldInfo.is_required)
```
is_required() ->

```

Check if the field is required (i.e., does not have a default value or factory).
Returns:
Type | Description
---|---
|  `True` if the field is required, `False` otherwise.
Source code in `pydantic/fields.py`
```
751
752
753
754
755
756
757
```
| ```
def is_required(self) -> bool:
    """Check if the field is required (i.e., does not have a default value or factory).

    Returns:
        `True` if the field is required, `False` otherwise.
    """
    return self.default is PydanticUndefined and self.default_factory is None

```

---|---
###  asdict [¶](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.FieldInfo.asdict)
```
asdict() -> _FieldInfoAsDict

```

Return a dictionary representation of the `FieldInfo` instance.
The returned value is a dictionary with three items:
  * `annotation`: The type annotation of the field.
  * `metadata`: The metadata list.
  * `attributes`: A mapping of the remaining `FieldInfo` attributes to their values (e.g. `alias`, `title`).

Source code in `pydantic/fields.py`
```
806
807
808
809
810
811
812
813
814
815
816
817
818
819
```
| ```
def asdict(self) -> _FieldInfoAsDict:
    """Return a dictionary representation of the `FieldInfo` instance.

    The returned value is a dictionary with three items:

    * `annotation`: The type annotation of the field.
    * `metadata`: The metadata list.
    * `attributes`: A mapping of the remaining `FieldInfo` attributes to their values (e.g. `alias`, `title`).
    """
    return {
        'annotation': self.annotation,
        'metadata': self.metadata,
        'attributes': {attr: getattr(self, attr) for attr in _Attrs},
    }

```

---|---
##  PrivateAttr [¶](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.PrivateAttr)
```
PrivateAttr(
    default: _T, *, init: [False] = False
) -> _T

```

```
PrivateAttr(
    *,
    default_factory: [[], _T],
    init: [False] = False
) -> _T

```

```
PrivateAttr(*, init: [False] = False) ->

```

```
PrivateAttr(
    default:  = PydanticUndefined,
    *,
    default_factory: [[], ] | None = None,
    init: [False] = False
) ->

```

Usage Documentation
[Private Model Attributes](https://docs.pydantic.dev/latest/concepts/models/#private-model-attributes)
Indicates that an attribute is intended for private use and not handled during normal validation/serialization.
Private attributes are not validated by Pydantic, so it's up to you to ensure they are used in a type-safe manner.
Private attributes are stored in `__private_attributes__` on the model.
Parameters:
Name | Type | Description | Default
---|---|---|---
`default` |  |  The attribute's default value. Defaults to Undefined. |  `PydanticUndefined`
`default_factory` |  |  Callable that will be called when a default value is needed for this attribute. If both `default` and `default_factory` are set, an error will be raised. |  `None`
`init` |  |  Whether the attribute should be included in the constructor of the dataclass. Always `False`. |  `False`
Returns:
Type | Description
---|---
|  An instance of [`ModelPrivateAttr`](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.ModelPrivateAttr) class.
Raises:
Type | Description
---|---
|  If both `default` and `default_factory` are set.
Source code in `pydantic/fields.py`
```
1481
1482
1483
1484
1485
1486
1487
1488
1489
1490
1491
1492
1493
1494
1495
1496
1497
1498
1499
1500
1501
1502
1503
1504
1505
1506
1507
1508
1509
1510
1511
1512
1513
1514
1515
```
| ```
def PrivateAttr(
    default: Any = PydanticUndefined,
    *,
    default_factory: Callable[[], Any] | None = None,
    init: Literal[False] = False,
) -> Any:
    """!!! abstract "Usage Documentation"
        [Private Model Attributes](../concepts/models.md#private-model-attributes)

    Indicates that an attribute is intended for private use and not handled during normal validation/serialization.

    Private attributes are not validated by Pydantic, so it's up to you to ensure they are used in a type-safe manner.

    Private attributes are stored in `__private_attributes__` on the model.

    Args:
        default: The attribute's default value. Defaults to Undefined.
        default_factory: Callable that will be
            called when a default value is needed for this attribute.
            If both `default` and `default_factory` are set, an error will be raised.
        init: Whether the attribute should be included in the constructor of the dataclass. Always `False`.

    Returns:
        An instance of [`ModelPrivateAttr`][pydantic.fields.ModelPrivateAttr] class.

    Raises:
        ValueError: If both `default` and `default_factory` are set.
    """
    if default is not PydanticUndefined and default_factory is not None:
        raise TypeError('cannot specify both default and default_factory')

    return ModelPrivateAttr(
        default,
        default_factory=default_factory,
    )

```

---|---
