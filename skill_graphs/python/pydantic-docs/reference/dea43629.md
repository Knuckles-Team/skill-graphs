##  tuple_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.tuple_schema)
```
tuple_schema(
    items_schema: [CoreSchema],
    *,
    variadic_item_index:  | None = None,
    min_length:  | None = None,
    max_length:  | None = None,
    fail_fast:  | None = None,
    strict:  | None = None,
    ref:  | None = None,
    metadata: [, ] | None = None,
    serialization: IncExSeqOrElseSerSchema | None = None
) -> TupleSchema

```

Returns a schema that matches a tuple of schemas, with an optional variadic item, e.g.:
```
from pydantic_core import SchemaValidator, core_schema

schema = core_schema.tuple_schema(
    [core_schema.int_schema(), core_schema.str_schema(), core_schema.float_schema()],
    variadic_item_index=1,
)
v = SchemaValidator(schema)
assert v.validate_python((1, 'hello', 'world', 1.5)) == (1, 'hello', 'world', 1.5)

```

Parameters:
Name | Type | Description | Default
---|---|---|---
`items_schema` |  `CoreSchema]` |  The value must be a tuple with items that match these schemas |  _required_
`variadic_item_index` |  |  The index of the schema in `items_schema` to be treated as variadic (following PEP 646) |  `None`
`min_length` |  |  The value must be a tuple with at least this many items |  `None`
`max_length` |  |  The value must be a tuple with at most this many items |  `None`
`fail_fast` |  |  Stop validation on the first error |  `None`
`strict` |  |  The value must be a tuple with exactly this many items |  `None`
`ref` |  |  Optional unique identifier of the schema, used to reference the schema in other places |  `None`
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`
`serialization` |  `IncExSeqOrElseSerSchema | None` |  Custom serialization schema |  `None`
Source code in `pydantic_core/core_schema.py`
```
1696
1697
1698
1699
1700
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
1723
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
1741
1742
1743
1744
```
| ```
def tuple_schema(
    items_schema: list[CoreSchema],
    *,
    variadic_item_index: int | None = None,
    min_length: int | None = None,
    max_length: int | None = None,
    fail_fast: bool | None = None,
    strict: bool | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: IncExSeqOrElseSerSchema | None = None,
) -> TupleSchema:
    """
    Returns a schema that matches a tuple of schemas, with an optional variadic item, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    schema = core_schema.tuple_schema(
        [core_schema.int_schema(), core_schema.str_schema(), core_schema.float_schema()],
        variadic_item_index=1,
    )
    v = SchemaValidator(schema)
    assert v.validate_python((1, 'hello', 'world', 1.5)) == (1, 'hello', 'world', 1.5)
```

    Args:
        items_schema: The value must be a tuple with items that match these schemas
        variadic_item_index: The index of the schema in `items_schema` to be treated as variadic (following PEP 646)
        min_length: The value must be a tuple with at least this many items
        max_length: The value must be a tuple with at most this many items
        fail_fast: Stop validation on the first error
        strict: The value must be a tuple with exactly this many items
        ref: Optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='tuple',
        items_schema=items_schema,
        variadic_item_index=variadic_item_index,
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
##  set_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.set_schema)
```
set_schema(
    items_schema: CoreSchema | None = None,
    *,
    min_length:  | None = None,
    max_length:  | None = None,
    fail_fast:  | None = None,
    strict:  | None = None,
    ref:  | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> SetSchema

```

Returns a schema that matches a set of a given schema, e.g.:
```
from pydantic_core import SchemaValidator, core_schema

schema = core_schema.set_schema(
    items_schema=core_schema.int_schema(), min_length=0, max_length=10
)
v = SchemaValidator(schema)
assert v.validate_python({1, '2', 3}) == {1, 2, 3}

```

Parameters:
Name | Type | Description | Default
---|---|---|---
`items_schema` |  `CoreSchema | None` |  The value must be a set with items that match this schema |  `None`
`min_length` |  |  The value must be a set with at least this many items |  `None`
`max_length` |  |  The value must be a set with at most this many items |  `None`
`fail_fast` |  |  Stop validation on the first error |  `None`
`strict` |  |  The value must be a set with exactly this many items |  `None`
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`
Source code in `pydantic_core/core_schema.py`
```
1759
1760
1761
1762
1763
1764
1765
1766
1767
1768
1769
1770
1771
1772
1773
1774
1775
1776
1777
1778
1779
1780
1781
1782
1783
1784
1785
1786
1787
1788
1789
1790
1791
1792
1793
1794
1795
1796
1797
1798
1799
1800
1801
1802
1803
```
| ```
def set_schema(
    items_schema: CoreSchema | None = None,
    *,
    min_length: int | None = None,
    max_length: int | None = None,
    fail_fast: bool | None = None,
    strict: bool | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> SetSchema:
    """
    Returns a schema that matches a set of a given schema, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    schema = core_schema.set_schema(
        items_schema=core_schema.int_schema(), min_length=0, max_length=10
    )
    v = SchemaValidator(schema)
    assert v.validate_python({1, '2', 3}) == {1, 2, 3}
```

    Args:
        items_schema: The value must be a set with items that match this schema
        min_length: The value must be a set with at least this many items
        max_length: The value must be a set with at most this many items
        fail_fast: Stop validation on the first error
        strict: The value must be a set with exactly this many items
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='set',
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
