        The generated JSON schema.
    """
    generated: list[JsonSchemaValue] = []

    choices = schema['choices']
    for choice in choices:
        # choice will be a tuple if an explicit label was provided
        choice_schema = choice[0] if isinstance(choice, tuple) else choice
        try:
            generated.append(self.generate_inner(choice_schema))
        except PydanticOmit:
            continue
        except PydanticInvalidForJsonSchema as exc:
            self.emit_warning('skipped-choice', exc.message)
    if len(generated) == 1:
        return generated[0]
    return self.get_union_of_schemas(generated)

```

---|---
###  get_union_of_schemas [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.get_union_of_schemas)
```
get_union_of_schemas(
    schemas: [JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)],
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Returns the JSON Schema representation for the union of the provided JSON Schemas.
The result depends on the configured `'union_format'`.
Parameters:
Name | Type | Description | Default
---|---|---|---
`schemas` |  `JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)]` |  The list of JSON Schemas to be included in the union. |  _required_
Returns:
Type | Description
---|---
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The JSON Schema representing the union of schemas.
Source code in `pydantic/json_schema.py`
```
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
```
| ```
def get_union_of_schemas(self, schemas: list[JsonSchemaValue]) -> JsonSchemaValue:
    """Returns the JSON Schema representation for the union of the provided JSON Schemas.

    The result depends on the configured `'union_format'`.

    Args:
        schemas: The list of JSON Schemas to be included in the union.

    Returns:
        The JSON Schema representing the union of schemas.
    """
    if self.union_format == 'primitive_type_array':
        types: list[str] = []
        for schema in schemas:
            schema_types: list[str] | str | None = schema.get('type')
            if schema_types is None:
                # No type, meaning it can be a ref or an empty schema.
                break
            if not isinstance(schema_types, list):
                schema_types = [schema_types]
            if not all(t in _PRIMITIVE_JSON_SCHEMA_TYPES for t in schema_types):
                break
            if len(schema) != 1:
                # We only want to include types that don't have any constraints. For instance,
                # if `schemas = [{'type': 'string', 'maxLength': 3}, {'type': 'string', 'minLength': 5}]`,
                # we don't want to produce `{'type': 'string', 'maxLength': 3, 'minLength': 5}`.
                # Same if we have some metadata (e.g. `title`) on a specific union member, we want to preserve it.
                break

            types.extend(schema_types)
        else:
            # If we got there, all the schemas where valid to be used with the `'primitive_type_array` format
            return {'type': list(dict.fromkeys(types))}

    return self.get_flattened_anyof(schemas)

```

---|---
###  tagged_union_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.tagged_union_schema)
```
tagged_union_schema(
    schema: TaggedUnionSchema,
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a schema that allows values matching any of the given schemas, where the schemas are tagged with a discriminator field that indicates which schema should be used to validate the value.
Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `TaggedUnionSchema` |  The core schema. |  _required_
Returns:
Type | Description
---|---
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.
Source code in `pydantic/json_schema.py`
```
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
```
| ```
def tagged_union_schema(self, schema: core_schema.TaggedUnionSchema) -> JsonSchemaValue:
    """Generates a JSON schema that matches a schema that allows values matching any of the given schemas, where
    the schemas are tagged with a discriminator field that indicates which schema should be used to validate
    the value.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    generated: dict[str, JsonSchemaValue] = {}
    for k, v in schema['choices'].items():
        if isinstance(k, Enum):
            k = k.value
        try:
            # Use str(k) since keys must be strings for json; while not technically correct,
            # it's the closest that can be represented in valid JSON
            generated[str(k)] = self.generate_inner(v).copy()
        except PydanticOmit:
            continue
        except PydanticInvalidForJsonSchema as exc:
            self.emit_warning('skipped-choice', exc.message)

    one_of_choices = _deduplicate_schemas(generated.values())
    json_schema: JsonSchemaValue = {'oneOf': one_of_choices}

    # This reflects the v1 behavior; TODO: we should make it possible to exclude OpenAPI stuff from the JSON schema
    openapi_discriminator = self._extract_discriminator(schema, one_of_choices)
    if openapi_discriminator is not None:
        json_schema['discriminator'] = {
            'propertyName': openapi_discriminator,
            'mapping': {k: v.get('$ref', v) for k, v in generated.items()},
        }

    return json_schema

```

---|---
###  chain_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.chain_schema)
```
chain_schema(schema: ChainSchema) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a core_schema.ChainSchema.
When generating a schema for validation, we return the validation JSON schema for the first step in the chain. For serialization, we return the serialization JSON schema for the last step in the chain.
Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `ChainSchema` |  The core schema. |  _required_
Returns:
Type | Description
---|---
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.
Source code in `pydantic/json_schema.py`
```
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
```
| ```
def chain_schema(self, schema: core_schema.ChainSchema) -> JsonSchemaValue:
    """Generates a JSON schema that matches a core_schema.ChainSchema.

    When generating a schema for validation, we return the validation JSON schema for the first step in the chain.
    For serialization, we return the serialization JSON schema for the last step in the chain.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    step_index = 0 if self.mode == 'validation' else -1  # use first step for validation, last for serialization
    return self.generate_inner(schema['steps'][step_index])

```

---|---
###  lax_or_strict_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.lax_or_strict_schema)
```
lax_or_strict_schema(
    schema: LaxOrStrictSchema,
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a schema that allows values matching either the lax schema or the strict schema.
Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `LaxOrStrictSchema` |  The core schema. |  _required_
Returns:
Type | Description
---|---
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.
Source code in `pydantic/json_schema.py`
```
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
```
| ```
def lax_or_strict_schema(self, schema: core_schema.LaxOrStrictSchema) -> JsonSchemaValue:
    """Generates a JSON schema that matches a schema that allows values matching either the lax schema or the
    strict schema.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    # TODO: Need to read the default value off of model config or whatever
    use_strict = schema.get('strict', False)  # TODO: replace this default False
    # If your JSON schema fails to generate it is probably
    # because one of the following two branches failed.
    if use_strict:
        return self.generate_inner(schema['strict_schema'])
    else:
        return self.generate_inner(schema['lax_schema'])

```

---|---
###  json_or_python_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.json_or_python_schema)
```
json_or_python_schema(
    schema: JsonOrPythonSchema,
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a schema that allows values matching either the JSON schema or the Python schema.
The JSON schema is used instead of the Python schema. If you want to use the Python schema, you should override this method.
Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `JsonOrPythonSchema` |  The core schema. |  _required_
Returns:
Type | Description
---|---
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.
Source code in `pydantic/json_schema.py`
```
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
```
| ```
def json_or_python_schema(self, schema: core_schema.JsonOrPythonSchema) -> JsonSchemaValue:
    """Generates a JSON schema that matches a schema that allows values matching either the JSON schema or the
    Python schema.

    The JSON schema is used instead of the Python schema. If you want to use the Python schema, you should override
    this method.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    return self.generate_inner(schema['json_schema'])

```

---|---
###  typed_dict_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.typed_dict_schema)
```
typed_dict_schema(
    schema: TypedDictSchema,
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a schema that defines a typed dict.
Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `TypedDictSchema` |  The core schema. |  _required_
Returns:
Type | Description
---|---
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.
Source code in `pydantic/json_schema.py`
```
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
```
| ```
def typed_dict_schema(self, schema: core_schema.TypedDictSchema) -> JsonSchemaValue:
    """Generates a JSON schema that matches a schema that defines a typed dict.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    total = schema.get('total', True)
    named_required_fields: list[tuple[str, bool, CoreSchemaField]] = [
        (name, self.field_is_required(field, total), field)
        for name, field in schema['fields'].items()
        if self.field_is_present(field)
    ]
    if self.mode == 'serialization':
        named_required_fields.extend(self._name_required_computed_fields(schema.get('computed_fields', [])))
    cls = schema.get('cls')
    config = _get_typed_dict_config(cls)
    with self._config_wrapper_stack.push(config):
        json_schema = self._named_required_fields_schema(named_required_fields)

    # There's some duplication between `extra_behavior` and
    # the config's `extra`/core config's `extra_fields_behavior`.
    # However, it is common to manually create TypedDictSchemas,
    # where you don't necessarily have a class.
    # At runtime, `extra_behavior` takes priority over the config
    # for validation, so follow the same for the JSON Schema:
    if schema.get('extra_behavior') == 'forbid':
        json_schema['additionalProperties'] = False
    elif schema.get('extra_behavior') == 'allow':
        if 'extras_schema' in schema and schema['extras_schema'] != {'type': 'any'}:
            json_schema['additionalProperties'] = self.generate_inner(schema['extras_schema'])
        else:
            json_schema['additionalProperties'] = True

    if cls is not None:
        # `_update_class_schema()` will not override
        # `additionalProperties` if already present:
        self._update_class_schema(json_schema, cls, config)
    elif 'additionalProperties' not in json_schema:
        extra = schema.get('config', {}).get('extra_fields_behavior')
        if extra == 'forbid':
            json_schema['additionalProperties'] = False
        elif extra == 'allow':
            json_schema['additionalProperties'] = True

    return json_schema

```

---|---
###  typed_dict_field_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.typed_dict_field_schema)
```
typed_dict_field_schema(
    schema: TypedDictField,
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a schema that defines a typed dict field.
Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `TypedDictField` |  The core schema. |  _required_
Returns:
Type | Description
---|---
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.
Source code in `pydantic/json_schema.py`
```
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
```
| ```
def typed_dict_field_schema(self, schema: core_schema.TypedDictField) -> JsonSchemaValue:
    """Generates a JSON schema that matches a schema that defines a typed dict field.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    return self.generate_inner(schema['schema'])

```

---|---
###  dataclass_field_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.dataclass_field_schema)
```
dataclass_field_schema(
    schema: DataclassField,
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a schema that defines a dataclass field.
Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `DataclassField` |  The core schema. |  _required_
Returns:
Type | Description
---|---
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.
Source code in `pydantic/json_schema.py`
```
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
```
| ```
def dataclass_field_schema(self, schema: core_schema.DataclassField) -> JsonSchemaValue:
    """Generates a JSON schema that matches a schema that defines a dataclass field.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    return self.generate_inner(schema['schema'])

```

---|---
###  model_field_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.model_field_schema)
```
model_field_schema(schema: ModelField) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a schema that defines a model field.
Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `ModelField` |  The core schema. |  _required_
Returns:
Type | Description
---|---
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.
Source code in `pydantic/json_schema.py`
```
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
```
| ```
def model_field_schema(self, schema: core_schema.ModelField) -> JsonSchemaValue:
    """Generates a JSON schema that matches a schema that defines a model field.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    return self.generate_inner(schema['schema'])

```

---|---
###  computed_field_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.computed_field_schema)
```
computed_field_schema(
    schema: ComputedField,
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a schema that defines a computed field.
Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `ComputedField` |  The core schema. |  _required_
Returns:
Type | Description
---|---
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.
Source code in `pydantic/json_schema.py`
```
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
```
| ```
def computed_field_schema(self, schema: core_schema.ComputedField) -> JsonSchemaValue:
    """Generates a JSON schema that matches a schema that defines a computed field.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    return self.generate_inner(schema['return_schema'])

```

---|---
###  model_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.model_schema)
```
model_schema(schema: ModelSchema) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a schema that defines a model.
Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `ModelSchema` |  The core schema. |  _required_
Returns:
Type | Description
---|---
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.
Source code in `pydantic/json_schema.py`
```
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
```
| ```
def model_schema(self, schema: core_schema.ModelSchema) -> JsonSchemaValue:
    """Generates a JSON schema that matches a schema that defines a model.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    # We do not use schema['model'].model_json_schema() here
    # because it could lead to inconsistent refs handling, etc.
    cls = cast('type[BaseModel]', schema['cls'])
    config = cls.model_config

    with self._config_wrapper_stack.push(config):
        json_schema = self.generate_inner(schema['schema'])

    self._update_class_schema(json_schema, cls, config)

    return json_schema

```

---|---
###  resolve_ref_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.resolve_ref_schema)
```
resolve_ref_schema(
    json_schema: JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue),
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Resolve a JsonSchemaValue to the non-ref schema if it is a $ref schema.
Parameters:
Name | Type | Description | Default
---|---|---|---
`json_schema` |  `JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The schema to resolve. |  _required_
Returns:
Type | Description
---|---
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The resolved schema.
Raises:
Type | Description
---|---
|  If the schema reference can't be found in definitions.
Source code in `pydantic/json_schema.py`
```
1681
1682
1683
1684
1685
1686
1687
1688
1689
1690
1691
1692
1693
1694
1695
1696
1697
1698
1699
```
| ```
def resolve_ref_schema(self, json_schema: JsonSchemaValue) -> JsonSchemaValue:
    """Resolve a JsonSchemaValue to the non-ref schema if it is a $ref schema.

    Args:
        json_schema: The schema to resolve.

    Returns:
        The resolved schema.

    Raises:
        RuntimeError: If the schema reference can't be found in definitions.
    """
    while '$ref' in json_schema:
        ref = json_schema['$ref']
        schema_to_update = self.get_schema_from_definitions(JsonRef(ref))
        if schema_to_update is None:
            raise RuntimeError(f'Cannot update undefined schema for $ref={ref}')
        json_schema = schema_to_update
    return json_schema

```

---|---
###  model_fields_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.model_fields_schema)
```
model_fields_schema(
    schema: ModelFieldsSchema,
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a schema that defines a model's fields.
Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `ModelFieldsSchema` |  The core schema. |  _required_
Returns:
Type | Description
---|---
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.
Source code in `pydantic/json_schema.py`
```
1701
1702
1703
1704
1705
1706
1707
1708
1709
1710
1711
1712
1713
1714
1715
1716
1717
1718
1719
1720
1721
1722
```
| ```
def model_fields_schema(self, schema: core_schema.ModelFieldsSchema) -> JsonSchemaValue:
    """Generates a JSON schema that matches a schema that defines a model's fields.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    named_required_fields: list[tuple[str, bool, CoreSchemaField]] = [
        (name, self.field_is_required(field, total=True), field)
        for name, field in schema['fields'].items()
        if self.field_is_present(field)
    ]
    if self.mode == 'serialization':
        named_required_fields.extend(self._name_required_computed_fields(schema.get('computed_fields', [])))
    json_schema = self._named_required_fields_schema(named_required_fields)
    extras_schema = schema.get('extras_schema', None)
    if extras_schema is not None:
        schema_to_update = self.resolve_ref_schema(json_schema)
        schema_to_update['additionalProperties'] = self.generate_inner(extras_schema)
    return json_schema

```

---|---
###  field_is_present [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.field_is_present)
```
field_is_present(field: CoreSchemaField) ->

```

Whether the field should be included in the generated JSON schema.
Parameters:
Name | Type | Description | Default
---|---|---|---
`field` |  `CoreSchemaField` |  The schema for the field itself. |  _required_
Returns:
Type | Description
---|---
|  `True` if the field should be included in the generated JSON schema, `False` otherwise.
Source code in `pydantic/json_schema.py`
```
1724
1725
1726
1727
1728
1729
1730
1731
1732
1733
1734
1735
1736
1737
1738
1739
1740
```
| ```
def field_is_present(self, field: CoreSchemaField) -> bool:
    """Whether the field should be included in the generated JSON schema.

    Args:
        field: The schema for the field itself.

    Returns:
        `True` if the field should be included in the generated JSON schema, `False` otherwise.
    """
    if self.mode == 'serialization':
        # If you still want to include the field in the generated JSON schema,
        # override this method and return True
        return not field.get('serialization_exclude')
    elif self.mode == 'validation':
        return True
    else:
        assert_never(self.mode)

```

---|---
###  field_is_required [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.field_is_required)
```
field_is_required(
    field: ModelField | DataclassField | TypedDictField,
    total: ,
) ->

```

Whether the field should be marked as required in the generated JSON schema. (Note that this is irrelevant if the field is not present in the JSON schema.).
