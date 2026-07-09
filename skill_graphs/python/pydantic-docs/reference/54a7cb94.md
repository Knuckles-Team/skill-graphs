##  tuple_positional_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.tuple_positional_schema)
```
tuple_positional_schema(
    items_schema: [CoreSchema],
    *,
    extras_schema: CoreSchema | None = None,
    strict:  | None = None,
    ref:  | None = None,
    metadata: [, ] | None = None,
    serialization: IncExSeqOrElseSerSchema | None = None
) -> TupleSchema

```

Returns a schema that matches a tuple of schemas, e.g.:
```
from pydantic_core import SchemaValidator, core_schema

schema = core_schema.tuple_positional_schema(
    [core_schema.int_schema(), core_schema.str_schema()]
)
v = SchemaValidator(schema)
assert v.validate_python((1, 'hello')) == (1, 'hello')

```

Parameters:
Name | Type | Description | Default
---|---|---|---
`items_schema` |  `CoreSchema]` |  The value must be a tuple with items that match these schemas |  _required_
`extras_schema` |  `CoreSchema | None` |  The value must be a tuple with items that match this schema This was inspired by JSON schema's `prefixItems` and `items` fields. In python's `typing.Tuple`, you can't specify a type for "extra" items -- they must all be the same type if the length is variable. So this field won't be set from a `typing.Tuple` annotation on a pydantic model. |  `None`
`strict` |  |  The value must be a tuple with exactly this many items |  `None`
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`
`serialization` |  `IncExSeqOrElseSerSchema | None` |  Custom serialization schema |  `None`
Source code in `pydantic_core/core_schema.py`
```
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
```
| ```
def tuple_positional_schema(
    items_schema: list[CoreSchema],
    *,
    extras_schema: CoreSchema | None = None,
    strict: bool | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: IncExSeqOrElseSerSchema | None = None,
) -> TupleSchema:
    """
    Returns a schema that matches a tuple of schemas, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    schema = core_schema.tuple_positional_schema(
        [core_schema.int_schema(), core_schema.str_schema()]
    )
    v = SchemaValidator(schema)
    assert v.validate_python((1, 'hello')) == (1, 'hello')
```

    Args:
        items_schema: The value must be a tuple with items that match these schemas
        extras_schema: The value must be a tuple with items that match this schema
            This was inspired by JSON schema's `prefixItems` and `items` fields.
            In python's `typing.Tuple`, you can't specify a type for "extra" items -- they must all be the same type
            if the length is variable. So this field won't be set from a `typing.Tuple` annotation on a pydantic model.
        strict: The value must be a tuple with exactly this many items
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    if extras_schema is not None:
        variadic_item_index = len(items_schema)
        items_schema = items_schema + [extras_schema]
    else:
        variadic_item_index = None
    return tuple_schema(
        items_schema=items_schema,
        variadic_item_index=variadic_item_index,
        strict=strict,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
    )

```

---|---
##  tuple_variable_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.tuple_variable_schema)
```
tuple_variable_schema(
    items_schema: CoreSchema | None = None,
    *,
    min_length:  | None = None,
    max_length:  | None = None,
    strict:  | None = None,
    ref:  | None = None,
    metadata: [, ] | None = None,
    serialization: IncExSeqOrElseSerSchema | None = None
) -> TupleSchema

```

Returns a schema that matches a tuple of a given schema, e.g.:
```
from pydantic_core import SchemaValidator, core_schema

schema = core_schema.tuple_variable_schema(
    items_schema=core_schema.int_schema(), min_length=0, max_length=10
)
v = SchemaValidator(schema)
assert v.validate_python(('1', 2, 3)) == (1, 2, 3)

```

Parameters:
Name | Type | Description | Default
---|---|---|---
`items_schema` |  `CoreSchema | None` |  The value must be a tuple with items that match this schema |  `None`
`min_length` |  |  The value must be a tuple with at least this many items |  `None`
`max_length` |  |  The value must be a tuple with at most this many items |  `None`
`strict` |  |  The value must be a tuple with exactly this many items |  `None`
`ref` |  |  Optional unique identifier of the schema, used to reference the schema in other places |  `None`
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`
`serialization` |  `IncExSeqOrElseSerSchema | None` |  Custom serialization schema |  `None`
Source code in `pydantic_core/core_schema.py`
```
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
1652
1653
1654
1655
1656
1657
1658
1659
1660
1661
1662
1663
1664
1665
1666
1667
1668
1669
1670
1671
1672
1673
1674
1675
1676
1677
1678
1679
1680
```
| ```
def tuple_variable_schema(
    items_schema: CoreSchema | None = None,
    *,
    min_length: int | None = None,
    max_length: int | None = None,
    strict: bool | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: IncExSeqOrElseSerSchema | None = None,
) -> TupleSchema:
    """
    Returns a schema that matches a tuple of a given schema, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    schema = core_schema.tuple_variable_schema(
        items_schema=core_schema.int_schema(), min_length=0, max_length=10
    )
    v = SchemaValidator(schema)
    assert v.validate_python(('1', 2, 3)) == (1, 2, 3)
```

    Args:
        items_schema: The value must be a tuple with items that match this schema
        min_length: The value must be a tuple with at least this many items
        max_length: The value must be a tuple with at most this many items
        strict: The value must be a tuple with exactly this many items
        ref: Optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return tuple_schema(
        items_schema=[items_schema or any_schema()],
        variadic_item_index=0,
        min_length=min_length,
        max_length=max_length,
        strict=strict,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
    )

```

---|---
