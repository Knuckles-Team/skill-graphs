##  callable_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.callable_schema)
```
callable_schema(
    *,
    ref:  | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> CallableSchema

```

Returns a schema that checks if a value is callable, equivalent to python's `callable` method, e.g.:
```
from pydantic_core import SchemaValidator, core_schema

schema = core_schema.callable_schema()
v = SchemaValidator(schema)
v.validate_python(min)

```

Parameters:
Name | Type | Description | Default
---|---|---|---
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`
Source code in `pydantic_core/core_schema.py`
```
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
```
| ```
def callable_schema(
    *, ref: str | None = None, metadata: dict[str, Any] | None = None, serialization: SerSchema | None = None
) -> CallableSchema:
    """
    Returns a schema that checks if a value is callable, equivalent to python's `callable` method, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    schema = core_schema.callable_schema()
    v = SchemaValidator(schema)
    v.validate_python(min)
```

    Args:
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(type='callable', ref=ref, metadata=metadata, serialization=serialization)

```

---|---
##  list_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.list_schema)
```
list_schema(
    items_schema: CoreSchema | None = None,
    *,
    min_length:  | None = None,
    max_length:  | None = None,
    fail_fast:  | None = None,
    strict:  | None = None,
    ref:  | None = None,
    metadata: [, ] | None = None,
    serialization: IncExSeqOrElseSerSchema | None = None
) -> ListSchema

```

Returns a schema that matches a list value, e.g.:
```
from pydantic_core import SchemaValidator, core_schema

schema = core_schema.list_schema(core_schema.int_schema(), min_length=0, max_length=10)
v = SchemaValidator(schema)
assert v.validate_python(['4']) == [4]

```

Parameters:
Name | Type | Description | Default
---|---|---|---
`items_schema` |  `CoreSchema | None` |  The value must be a list of items that match this schema |  `None`
`min_length` |  |  The value must be a list with at least this many items |  `None`
`max_length` |  |  The value must be a list with at most this many items |  `None`
`fail_fast` |  |  Stop validation on the first error |  `None`
`strict` |  |  The value must be a list with exactly this many items |  `None`
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`
`serialization` |  `IncExSeqOrElseSerSchema | None` |  Custom serialization schema |  `None`
Source code in `pydantic_core/core_schema.py`
```
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
```
| ```
def list_schema(
    items_schema: CoreSchema | None = None,
    *,
    min_length: int | None = None,
    max_length: int | None = None,
    fail_fast: bool | None = None,
    strict: bool | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: IncExSeqOrElseSerSchema | None = None,
) -> ListSchema:
    """
    Returns a schema that matches a list value, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    schema = core_schema.list_schema(core_schema.int_schema(), min_length=0, max_length=10)
    v = SchemaValidator(schema)
    assert v.validate_python(['4']) == [4]
```

    Args:
        items_schema: The value must be a list of items that match this schema
        min_length: The value must be a list with at least this many items
        max_length: The value must be a list with at most this many items
        fail_fast: Stop validation on the first error
        strict: The value must be a list with exactly this many items
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='list',
        items_schema=items_schema,
        min_length=min_length,
        max_length=max_length,
        fail_fast=fail_fast,
        strict=strict,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
    )

```

---|---
