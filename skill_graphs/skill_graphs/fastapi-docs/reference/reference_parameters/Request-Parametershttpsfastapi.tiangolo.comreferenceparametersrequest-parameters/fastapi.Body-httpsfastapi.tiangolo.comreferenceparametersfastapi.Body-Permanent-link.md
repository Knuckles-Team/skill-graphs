##  fastapi.Body [¶](https://fastapi.tiangolo.com/reference/parameters/#fastapi.Body "Permanent link")
```
Body(
    default=Undefined,
    *,
    default_factory=_Unset,
    embed=None,
    media_type="application/json",
    alias=None,
    alias_priority=_Unset,
    validation_alias=None,
    serialization_alias=None,
    title=None,
    description=None,
    gt=None,
    ge=None,
    lt=None,
    le=None,
    min_length=None,
    max_length=None,
    pattern=None,
    regex=None,
    discriminator=None,
    strict=_Unset,
    multiple_of=_Unset,
    allow_inf_nan=_Unset,
    max_digits=_Unset,
    decimal_places=_Unset,
    examples=None,
    example=_Unset,
    openapi_examples=None,
    deprecated=None,
    include_in_schema=True,
    json_schema_extra=None,
    **extra
)

```

PARAMETER | DESCRIPTION
---|---
`default` |  Default value if the parameter field is not set. **TYPE:** `Any` **DEFAULT:** `Undefined`
`default_factory` |  A callable to generate the default value. This doesn't affect `Path` parameters as the value is always required. The parameter is available only for compatibility. **TYPE:** `Callable[[], Any] | None` **DEFAULT:** `_Unset`
`embed` |  When `embed` is `True`, the parameter will be expected in a JSON body as a key instead of being the JSON body itself. This happens automatically when more than one `Body` parameter is declared. Read more about it in the [FastAPI docs for Body - Multiple Parameters](https://fastapi.tiangolo.com/tutorial/body-multiple-params/#embed-a-single-body-parameter). **TYPE:** `bool | None` **DEFAULT:** `None`
`media_type` |  The media type of this parameter field. Changing it would affect the generated OpenAPI, but currently it doesn't affect the parsing of the data. **TYPE:** `str` **DEFAULT:** `'application/json'`
`alias` |  An alternative name for the parameter field. This will be used to extract the data and for the generated OpenAPI. It is particularly useful when you can't use the name you want because it is a Python reserved keyword or similar. **TYPE:** `str | None` **DEFAULT:** `None`
`alias_priority` |  Priority of the alias. This affects whether an alias generator is used. **TYPE:** `int | None` **DEFAULT:** `_Unset`
`validation_alias` |  'Whitelist' validation step. The parameter field will be the single one allowed by the alias or set of aliases defined. **TYPE:** `str | AliasPath | AliasChoices | None` **DEFAULT:** `None`
`serialization_alias` |  'Blacklist' validation step. The vanilla parameter field will be the single one of the alias' or set of aliases' fields and all the other fields will be ignored at serialization time. **TYPE:** `str | None` **DEFAULT:** `None`
`title` |  Human-readable title. **TYPE:** `str | None` **DEFAULT:** `None`
`description` |  Human-readable description. **TYPE:** `str | None` **DEFAULT:** `None`
`gt` |  Greater than. If set, value must be greater than this. Only applicable to numbers. **TYPE:** `float | None` **DEFAULT:** `None`
`ge` |  Greater than or equal. If set, value must be greater than or equal to this. Only applicable to numbers. **TYPE:** `float | None` **DEFAULT:** `None`
`lt` |  Less than. If set, value must be less than this. Only applicable to numbers. **TYPE:** `float | None` **DEFAULT:** `None`
`le` |  Less than or equal. If set, value must be less than or equal to this. Only applicable to numbers. **TYPE:** `float | None` **DEFAULT:** `None`
`min_length` |  Minimum length for strings. **TYPE:** `int | None` **DEFAULT:** `None`
`max_length` |  Maximum length for strings. **TYPE:** `int | None` **DEFAULT:** `None`
`pattern` |  RegEx pattern for strings. **TYPE:** `str | None` **DEFAULT:** `None`
`regex` |  Deprecated in FastAPI 0.100.0 and Pydantic v2, use `pattern` instead. RegEx pattern for strings. **TYPE:** `str | None` **DEFAULT:** `None`
`discriminator` |  Parameter field name for discriminating the type in a tagged union. **TYPE:** `str | None` **DEFAULT:** `None`
`strict` |  If `True`, strict validation is applied to the field. **TYPE:** `bool | None` **DEFAULT:** `_Unset`
`multiple_of` |  Value must be a multiple of this. Only applicable to numbers. **TYPE:** `float | None` **DEFAULT:** `_Unset`
`allow_inf_nan` |  Allow `inf`, `-inf`, `nan`. Only applicable to numbers. **TYPE:** `bool | None` **DEFAULT:** `_Unset`
`max_digits` |  Maximum number of digits allowed for decimal values. **TYPE:** `int | None` **DEFAULT:** `_Unset`
`decimal_places` |  Maximum number of decimal places allowed for decimal values. **TYPE:** `int | None` **DEFAULT:** `_Unset`
`examples` |  Example values for this field. Read more about it in the [FastAPI docs for Declare Request Example Data](https://fastapi.tiangolo.com/tutorial/schema-extra-example/) **TYPE:** `list[Any] | None` **DEFAULT:** `None`
`example` |  Deprecated in OpenAPI 3.1.0 that now uses JSON Schema 2020-12, although still supported. Use examples instead.  **TYPE:** `Any | None` **DEFAULT:** `_Unset`
`openapi_examples` |  OpenAPI-specific examples. It will be added to the generated OpenAPI (e.g. visible at `/docs`). Swagger UI (that provides the `/docs` interface) has better support for the OpenAPI-specific examples than the JSON Schema `examples`, that's the main use case for this. Read more about it in the [FastAPI docs for Declare Request Example Data](https://fastapi.tiangolo.com/tutorial/schema-extra-example/#using-the-openapi_examples-parameter). **TYPE:** `dict[str, Example[](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Example "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">Example</span> \(<code>fastapi.openapi.models.Example</code>\)")] | None` **DEFAULT:** `None`
`deprecated` |  Mark this parameter field as deprecated. It will affect the generated OpenAPI (e.g. visible at `/docs`). **TYPE:** `deprecated | str | bool | None` **DEFAULT:** `None`
`include_in_schema` |  To include (or not) this parameter field in the generated OpenAPI. You probably don't need it, but it's available. This affects the generated OpenAPI (e.g. visible at `/docs`). **TYPE:** `bool` **DEFAULT:** `True`
`json_schema_extra` |  Any additional JSON schema data. **TYPE:** `dict[str, Any] | None` **DEFAULT:** `None`
`**extra` |  The `extra` kwargs is deprecated. Use `json_schema_extra` instead. Include extra fields used by the JSON Schema. **TYPE:** `Any` **DEFAULT:** `{}`
Source code in `fastapi/param_functions.py`
```
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
1394
1395
1396
1397
1398
1399
1400
1401
1402
1403
1404
1405
1406
1407
1408
1409
1410
1411
1412
1413
1414
1415
1416
1417
1418
1419
1420
1421
1422
1423
1424
1425
1426
1427
1428
1429
1430
1431
1432
1433
1434
1435
1436
1437
1438
1439
1440
1441
1442
1443
1444
1445
1446
1447
1448
1449
1450
1451
1452
1453
1454
1455
1456
1457
1458
1459
1460
1461
1462
1463
1464
1465
1466
1467
1468
1469
1470
1471
1472
1473
1474
1475
1476
1477
1478
1479
1480
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
1516
1517
1518
1519
1520
1521
1522
1523
1524
1525
1526
1527
1528
1529
1530
1531
1532
1533
1534
1535
1536
1537
1538
1539
1540
1541
1542
1543
1544
1545
1546
1547
1548
1549
1550
1551
1552
1553
1554
1555
1556
1557
1558
1559
1560
1561
1562
1563
1564
1565
1566
1567
1568
1569
1570
1571
1572
1573
1574
1575
1576
1577
1578
1579
1580
1581
1582
1583
1584
1585
1586
1587
1588
1589
1590
1591
1592
1593
1594
1595
1596
1597
1598
1599
1600
1601
1602
1603
1604
1605
1606
1607
1608
1609
1610
1611
1612
1613
1614
1615
1616
1617
1618
1619
1620
1621
1622
1623
1624
1625
1626
1627
1628
1629
1630
1631
1632
1633
1634
1635
1636
1637
1638
1639
1640
1641
1642
1643
1644
1645
1646
1647
1648
1649
1650
1651
```
| ```
def Body(  # noqa: N802
    default: Annotated[
        Any,
        Doc(
            """
            Default value if the parameter field is not set.
            """
        ),
    ] = Undefined,
    *,
    default_factory: Annotated[
        Callable[[], Any] | None,
        Doc(
            """
            A callable to generate the default value.

            This doesn't affect `Path` parameters as the value is always required.
            The parameter is available only for compatibility.
            """
        ),
    ] = _Unset,
    embed: Annotated[
        bool | None,
        Doc(
            """
            When `embed` is `True`, the parameter will be expected in a JSON body as a
            key instead of being the JSON body itself.

            This happens automatically when more than one `Body` parameter is declared.

            Read more about it in the
            [FastAPI docs for Body - Multiple Parameters](https://fastapi.tiangolo.com/tutorial/body-multiple-params/#embed-a-single-body-parameter).
            """
        ),
    ] = None,
    media_type: Annotated[
        str,
        Doc(
            """
            The media type of this parameter field. Changing it would affect the
            generated OpenAPI, but currently it doesn't affect the parsing of the data.
            """
        ),
    ] = "application/json",
    alias: Annotated[
        str | None,
        Doc(
            """
            An alternative name for the parameter field.

            This will be used to extract the data and for the generated OpenAPI.
            It is particularly useful when you can't use the name you want because it
            is a Python reserved keyword or similar.
            """
        ),
    ] = None,
    alias_priority: Annotated[
        int | None,
        Doc(
            """
            Priority of the alias. This affects whether an alias generator is used.
            """
        ),
    ] = _Unset,
    validation_alias: Annotated[
        str | AliasPath | AliasChoices | None,
        Doc(
            """
            'Whitelist' validation step. The parameter field will be the single one
            allowed by the alias or set of aliases defined.
            """
        ),
    ] = None,
    serialization_alias: Annotated[
        str | None,
        Doc(
            """
            'Blacklist' validation step. The vanilla parameter field will be the
            single one of the alias' or set of aliases' fields and all the other
            fields will be ignored at serialization time.
            """
        ),
    ] = None,
    title: Annotated[
        str | None,
        Doc(
            """
            Human-readable title.
            """
        ),
    ] = None,
    description: Annotated[
        str | None,
        Doc(
            """
            Human-readable description.
            """
        ),
    ] = None,
    gt: Annotated[
        float | None,
        Doc(
            """
            Greater than. If set, value must be greater than this. Only applicable to
            numbers.
            """
        ),
    ] = None,
    ge: Annotated[
        float | None,
        Doc(
            """
            Greater than or equal. If set, value must be greater than or equal to
            this. Only applicable to numbers.
            """
        ),
    ] = None,
    lt: Annotated[
        float | None,
        Doc(
            """
            Less than. If set, value must be less than this. Only applicable to numbers.
            """
        ),
    ] = None,
    le: Annotated[
        float | None,
        Doc(
            """
            Less than or equal. If set, value must be less than or equal to this.
            Only applicable to numbers.
            """
        ),
    ] = None,
    min_length: Annotated[
        int | None,
        Doc(
            """
            Minimum length for strings.
            """
        ),
    ] = None,
    max_length: Annotated[
        int | None,
        Doc(
            """
            Maximum length for strings.
            """
        ),
    ] = None,
    pattern: Annotated[
        str | None,
        Doc(
            """
            RegEx pattern for strings.
            """
        ),
    ] = None,
    regex: Annotated[
        str | None,
        Doc(
            """
            RegEx pattern for strings.
            """
        ),
        deprecated(
            "Deprecated in FastAPI 0.100.0 and Pydantic v2, use `pattern` instead."
        ),
    ] = None,
    discriminator: Annotated[
        str | None,
        Doc(
            """
            Parameter field name for discriminating the type in a tagged union.
            """
        ),
    ] = None,
    strict: Annotated[
        bool | None,
        Doc(
            """
            If `True`, strict validation is applied to the field.
            """
        ),
    ] = _Unset,
    multiple_of: Annotated[
        float | None,
        Doc(
            """
            Value must be a multiple of this. Only applicable to numbers.
            """
        ),
    ] = _Unset,
    allow_inf_nan: Annotated[
        bool | None,
        Doc(
            """
            Allow `inf`, `-inf`, `nan`. Only applicable to numbers.
            """
        ),
    ] = _Unset,
    max_digits: Annotated[
        int | None,
        Doc(
            """
            Maximum number of digits allowed for decimal values.
            """
        ),
    ] = _Unset,
    decimal_places: Annotated[
        int | None,
        Doc(
            """
            Maximum number of decimal places allowed for decimal values.
            """
        ),
    ] = _Unset,
    examples: Annotated[
        list[Any] | None,
        Doc(
            """
            Example values for this field.

            Read more about it in the
            [FastAPI docs for Declare Request Example Data](https://fastapi.tiangolo.com/tutorial/schema-extra-example/)
            """
        ),
    ] = None,
    example: Annotated[
        Any | None,
        deprecated(
            "Deprecated in OpenAPI 3.1.0 that now uses JSON Schema 2020-12, "
            "although still supported. Use examples instead."
        ),
    ] = _Unset,
    openapi_examples: Annotated[
        dict[str, Example] | None,
        Doc(
            """
            OpenAPI-specific examples.

            It will be added to the generated OpenAPI (e.g. visible at `/docs`).

            Swagger UI (that provides the `/docs` interface) has better support for the
            OpenAPI-specific examples than the JSON Schema `examples`, that's the main
            use case for this.

            Read more about it in the
            [FastAPI docs for Declare Request Example Data](https://fastapi.tiangolo.com/tutorial/schema-extra-example/#using-the-openapi_examples-parameter).
            """
        ),
    ] = None,
    deprecated: Annotated[
        deprecated | str | bool | None,
        Doc(
            """
            Mark this parameter field as deprecated.

            It will affect the generated OpenAPI (e.g. visible at `/docs`).
            """
        ),
    ] = None,
    include_in_schema: Annotated[
        bool,
        Doc(
            """
            To include (or not) this parameter field in the generated OpenAPI.
            You probably don't need it, but it's available.

            This affects the generated OpenAPI (e.g. visible at `/docs`).
            """
        ),
    ] = True,
    json_schema_extra: Annotated[
        dict[str, Any] | None,
        Doc(
            """
            Any additional JSON schema data.
            """
        ),
    ] = None,
    **extra: Annotated[
        Any,
        Doc(
            """
            Include extra fields used by the JSON Schema.
            """
        ),
        deprecated(
            """
            The `extra` kwargs is deprecated. Use `json_schema_extra` instead.
            """
        ),
    ],
) -> Any:
    return params.Body(
        default=default,
        default_factory=default_factory,
        embed=embed,
        media_type=media_type,
        alias=alias,
        alias_priority=alias_priority,
        validation_alias=validation_alias,
        serialization_alias=serialization_alias,
        title=title,
        description=description,
        gt=gt,
        ge=ge,
        lt=lt,
        le=le,
        min_length=min_length,
        max_length=max_length,
        pattern=pattern,
        regex=regex,
        discriminator=discriminator,
        strict=strict,
        multiple_of=multiple_of,
        allow_inf_nan=allow_inf_nan,
        max_digits=max_digits,
        decimal_places=decimal_places,
        example=example,
        examples=examples,
        openapi_examples=openapi_examples,
        deprecated=deprecated,
        include_in_schema=include_in_schema,
        json_schema_extra=json_schema_extra,
        **extra,
    )

```

---|---
##  fastapi.Cookie [¶](https://fastapi.tiangolo.com/reference/parameters/#fastapi.Cookie "Permanent link")
```
Cookie(
    default=Undefined,
    *,
    default_factory=_Unset,
    alias=None,
    alias_priority=_Unset,
    validation_alias=None,
    serialization_alias=None,
    title=None,
    description=None,
    gt=None,
    ge=None,
    lt=None,
    le=None,
    min_length=None,
    max_length=None,
    pattern=None,
    regex=None,
    discriminator=None,
    strict=_Unset,
    multiple_of=_Unset,
    allow_inf_nan=_Unset,
    max_digits=_Unset,
    decimal_places=_Unset,
    examples=None,
    example=_Unset,
    openapi_examples=None,
    deprecated=None,
    include_in_schema=True,
    json_schema_extra=None,
    **extra
)

```

PARAMETER | DESCRIPTION
---|---
`default` |  Default value if the parameter field is not set. **TYPE:** `Any` **DEFAULT:** `Undefined`
`default_factory` |  A callable to generate the default value. This doesn't affect `Path` parameters as the value is always required. The parameter is available only for compatibility. **TYPE:** `Callable[[], Any] | None` **DEFAULT:** `_Unset`
`alias` |  An alternative name for the parameter field. This will be used to extract the data and for the generated OpenAPI. It is particularly useful when you can't use the name you want because it is a Python reserved keyword or similar. **TYPE:** `str | None` **DEFAULT:** `None`
`alias_priority` |  Priority of the alias. This affects whether an alias generator is used. **TYPE:** `int | None` **DEFAULT:** `_Unset`
`validation_alias` |  'Whitelist' validation step. The parameter field will be the single one allowed by the alias or set of aliases defined. **TYPE:** `str | AliasPath | AliasChoices | None` **DEFAULT:** `None`
`serialization_alias` |  'Blacklist' validation step. The vanilla parameter field will be the single one of the alias' or set of aliases' fields and all the other fields will be ignored at serialization time. **TYPE:** `str | None` **DEFAULT:** `None`
`title` |  Human-readable title. **TYPE:** `str | None` **DEFAULT:** `None`
`description` |  Human-readable description. **TYPE:** `str | None` **DEFAULT:** `None`
`gt` |  Greater than. If set, value must be greater than this. Only applicable to numbers. **TYPE:** `float | None` **DEFAULT:** `None`
`ge` |  Greater than or equal. If set, value must be greater than or equal to this. Only applicable to numbers. **TYPE:** `float | None` **DEFAULT:** `None`
`lt` |  Less than. If set, value must be less than this. Only applicable to numbers. **TYPE:** `float | None` **DEFAULT:** `None`
`le` |  Less than or equal. If set, value must be less than or equal to this. Only applicable to numbers. **TYPE:** `float | None` **DEFAULT:** `None`
`min_length` |  Minimum length for strings. **TYPE:** `int | None` **DEFAULT:** `None`
`max_length` |  Maximum length for strings. **TYPE:** `int | None` **DEFAULT:** `None`
`pattern` |  RegEx pattern for strings. **TYPE:** `str | None` **DEFAULT:** `None`
`regex` |  Deprecated in FastAPI 0.100.0 and Pydantic v2, use `pattern` instead. RegEx pattern for strings. **TYPE:** `str | None` **DEFAULT:** `None`
`discriminator` |  Parameter field name for discriminating the type in a tagged union. **TYPE:** `str | None` **DEFAULT:** `None`
`strict` |  If `True`, strict validation is applied to the field. **TYPE:** `bool | None` **DEFAULT:** `_Unset`
`multiple_of` |  Value must be a multiple of this. Only applicable to numbers. **TYPE:** `float | None` **DEFAULT:** `_Unset`
`allow_inf_nan` |  Allow `inf`, `-inf`, `nan`. Only applicable to numbers. **TYPE:** `bool | None` **DEFAULT:** `_Unset`
`max_digits` |  Maximum number of digits allowed for decimal values. **TYPE:** `int | None` **DEFAULT:** `_Unset`
`decimal_places` |  Maximum number of decimal places allowed for decimal values. **TYPE:** `int | None` **DEFAULT:** `_Unset`
`examples` |  Example values for this field. Read more about it in the [FastAPI docs for Declare Request Example Data](https://fastapi.tiangolo.com/tutorial/schema-extra-example/) **TYPE:** `list[Any] | None` **DEFAULT:** `None`
`example` |  Deprecated in OpenAPI 3.1.0 that now uses JSON Schema 2020-12, although still supported. Use examples instead.  **TYPE:** `Any | None` **DEFAULT:** `_Unset`
`openapi_examples` |  OpenAPI-specific examples. It will be added to the generated OpenAPI (e.g. visible at `/docs`). Swagger UI (that provides the `/docs` interface) has better support for the OpenAPI-specific examples than the JSON Schema `examples`, that's the main use case for this. Read more about it in the [FastAPI docs for Declare Request Example Data](https://fastapi.tiangolo.com/tutorial/schema-extra-example/#using-the-openapi_examples-parameter). **TYPE:** `dict[str, Example[](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Example "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">Example</span> \(<code>fastapi.openapi.models.Example</code>\)")] | None` **DEFAULT:** `None`
`deprecated` |  Mark this parameter field as deprecated. It will affect the generated OpenAPI (e.g. visible at `/docs`). **TYPE:** `deprecated | str | bool | None` **DEFAULT:** `None`
`include_in_schema` |  To include (or not) this parameter field in the generated OpenAPI. You probably don't need it, but it's available. This affects the generated OpenAPI (e.g. visible at `/docs`). **TYPE:** `bool` **DEFAULT:** `True`
`json_schema_extra` |  Any additional JSON schema data. **TYPE:** `dict[str, Any] | None` **DEFAULT:** `None`
`**extra` |  The `extra` kwargs is deprecated. Use `json_schema_extra` instead. Include extra fields used by the JSON Schema. **TYPE:** `Any` **DEFAULT:** `{}`
Source code in `fastapi/param_functions.py`
```
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
1062
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
1110
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
1124
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
1135
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
```
| ```
def Cookie(  # noqa: N802
    default: Annotated[
        Any,
        Doc(
            """
            Default value if the parameter field is not set.
            """
        ),
    ] = Undefined,
    *,
    default_factory: Annotated[
        Callable[[], Any] | None,
        Doc(
            """
            A callable to generate the default value.

            This doesn't affect `Path` parameters as the value is always required.
            The parameter is available only for compatibility.
            """
        ),
    ] = _Unset,
    alias: Annotated[
        str | None,
        Doc(
            """
            An alternative name for the parameter field.

            This will be used to extract the data and for the generated OpenAPI.
            It is particularly useful when you can't use the name you want because it
            is a Python reserved keyword or similar.
            """
        ),
    ] = None,
    alias_priority: Annotated[
        int | None,
        Doc(
            """
            Priority of the alias. This affects whether an alias generator is used.
            """
        ),
    ] = _Unset,
    validation_alias: Annotated[
        str | AliasPath | AliasChoices | None,
        Doc(
            """
            'Whitelist' validation step. The parameter field will be the single one
            allowed by the alias or set of aliases defined.
            """
        ),
    ] = None,
    serialization_alias: Annotated[
        str | None,
        Doc(
            """
            'Blacklist' validation step. The vanilla parameter field will be the
            single one of the alias' or set of aliases' fields and all the other
            fields will be ignored at serialization time.
            """
        ),
    ] = None,
    title: Annotated[
        str | None,
        Doc(
            """
            Human-readable title.
            """
        ),
    ] = None,
    description: Annotated[
        str | None,
        Doc(
            """
            Human-readable description.
            """
        ),
    ] = None,
    gt: Annotated[
        float | None,
        Doc(
            """
            Greater than. If set, value must be greater than this. Only applicable to
            numbers.
            """
        ),
    ] = None,
    ge: Annotated[
        float | None,
        Doc(
            """
            Greater than or equal. If set, value must be greater than or equal to
            this. Only applicable to numbers.
            """
        ),
    ] = None,
    lt: Annotated[
        float | None,
        Doc(
            """
            Less than. If set, value must be less than this. Only applicable to numbers.
            """
        ),
    ] = None,
    le: Annotated[
        float | None,
        Doc(
            """
            Less than or equal. If set, value must be less than or equal to this.
            Only applicable to numbers.
            """
        ),
    ] = None,
    min_length: Annotated[
        int | None,
        Doc(
            """
            Minimum length for strings.
            """
        ),
    ] = None,
    max_length: Annotated[
        int | None,
        Doc(
            """
            Maximum length for strings.
            """
        ),
    ] = None,
    pattern: Annotated[
        str | None,
        Doc(
            """
            RegEx pattern for strings.
            """
        ),
    ] = None,
    regex: Annotated[
        str | None,
        Doc(
            """
            RegEx pattern for strings.
            """
        ),
        deprecated(
            "Deprecated in FastAPI 0.100.0 and Pydantic v2, use `pattern` instead."
        ),
    ] = None,
    discriminator: Annotated[
        str | None,
        Doc(
            """
            Parameter field name for discriminating the type in a tagged union.
            """
        ),
    ] = None,
    strict: Annotated[
        bool | None,
        Doc(
            """
            If `True`, strict validation is applied to the field.
            """
        ),
    ] = _Unset,
    multiple_of: Annotated[
        float | None,
        Doc(
            """
            Value must be a multiple of this. Only applicable to numbers.
            """
        ),
    ] = _Unset,
    allow_inf_nan: Annotated[
        bool | None,
        Doc(
            """
            Allow `inf`, `-inf`, `nan`. Only applicable to numbers.
            """
        ),
    ] = _Unset,
    max_digits: Annotated[
        int | None,
        Doc(
            """
            Maximum number of digits allowed for decimal values.
            """
        ),
    ] = _Unset,
    decimal_places: Annotated[
        int | None,
        Doc(
            """
            Maximum number of decimal places allowed for decimal values.
            """
        ),
    ] = _Unset,
    examples: Annotated[
        list[Any] | None,
        Doc(
            """
            Example values for this field.

            Read more about it in the
            [FastAPI docs for Declare Request Example Data](https://fastapi.tiangolo.com/tutorial/schema-extra-example/)
            """
        ),
    ] = None,
    example: Annotated[
        Any | None,
        deprecated(
            "Deprecated in OpenAPI 3.1.0 that now uses JSON Schema 2020-12, "
            "although still supported. Use examples instead."
        ),
    ] = _Unset,
    openapi_examples: Annotated[
        dict[str, Example] | None,
        Doc(
            """
            OpenAPI-specific examples.

            It will be added to the generated OpenAPI (e.g. visible at `/docs`).

            Swagger UI (that provides the `/docs` interface) has better support for the
            OpenAPI-specific examples than the JSON Schema `examples`, that's the main
            use case for this.

            Read more about it in the
            [FastAPI docs for Declare Request Example Data](https://fastapi.tiangolo.com/tutorial/schema-extra-example/#using-the-openapi_examples-parameter).
            """
        ),
    ] = None,
    deprecated: Annotated[
        deprecated | str | bool | None,
        Doc(
            """
            Mark this parameter field as deprecated.

            It will affect the generated OpenAPI (e.g. visible at `/docs`).
            """
        ),
    ] = None,
    include_in_schema: Annotated[
        bool,
        Doc(
            """
            To include (or not) this parameter field in the generated OpenAPI.
            You probably don't need it, but it's available.

            This affects the generated OpenAPI (e.g. visible at `/docs`).
            """
        ),
    ] = True,
    json_schema_extra: Annotated[
        dict[str, Any] | None,
        Doc(
            """
            Any additional JSON schema data.
            """
        ),
    ] = None,
    **extra: Annotated[
        Any,
        Doc(
            """
            Include extra fields used by the JSON Schema.
            """
        ),
        deprecated(
            """
            The `extra` kwargs is deprecated. Use `json_schema_extra` instead.
            """
        ),
    ],
) -> Any:
    return params.Cookie(
        default=default,
        default_factory=default_factory,
        alias=alias,
        alias_priority=alias_priority,
        validation_alias=validation_alias,
        serialization_alias=serialization_alias,
        title=title,
        description=description,
        gt=gt,
        ge=ge,
        lt=lt,
        le=le,
        min_length=min_length,
        max_length=max_length,
        pattern=pattern,
        regex=regex,
        discriminator=discriminator,
        strict=strict,
        multiple_of=multiple_of,
        allow_inf_nan=allow_inf_nan,
        max_digits=max_digits,
        decimal_places=decimal_places,
        example=example,
        examples=examples,
        openapi_examples=openapi_examples,
        deprecated=deprecated,
        include_in_schema=include_in_schema,
        json_schema_extra=json_schema_extra,
        **extra,
    )

```

---|---
