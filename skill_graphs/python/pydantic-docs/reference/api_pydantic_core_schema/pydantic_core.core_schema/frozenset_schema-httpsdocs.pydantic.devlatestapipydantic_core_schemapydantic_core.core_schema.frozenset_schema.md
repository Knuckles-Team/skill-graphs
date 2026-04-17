##  frozenset_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.frozenset_schema)
```
frozenset_schema(
    items_schema: CoreSchema | None = None,
    *,
    min_length:  | None = None,
    max_length:  | None = None,
    fail_fast:  | None = None,
    strict:  | None = None,
    ref:  | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> FrozenSetSchema

```

Returns a schema that matches a frozenset of a given schema, e.g.:
```
from pydantic_core import SchemaValidator, core_schema

schema = core_schema.frozenset_schema(
    items_schema=core_schema.int_schema(), min_length=0, max_length=10
)
v = SchemaValidator(schema)
assert v.validate_python(frozenset(range(3))) == frozenset({0, 1, 2})

```

Parameters:
Name | Type | Description | Default
---|---|---|---
`items_schema` |  `CoreSchema | None` |  The value must be a frozenset with items that match this schema |  `None`
`min_length` |  |  The value must be a frozenset with at least this many items |  `None`
`max_length` |  |  The value must be a frozenset with at most this many items |  `None`
`fail_fast` |  |  Stop validation on the first error |  `None`
`strict` |  |  The value must be a frozenset with exactly this many items |  `None`
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`
Source code in `pydantic_core/core_schema.py`
```
1818
1819
1820
1821
1822
1823
1824
1825
1826
1827
1828
1829
1830
1831
1832
1833
1834
1835
1836
1837
1838
1839
1840
1841
1842
1843
1844
1845
1846
1847
1848
1849
1850
1851
1852
1853
1854
1855
1856
1857
1858
1859
1860
1861
1862
```
| ```
def frozenset_schema(
    items_schema: CoreSchema | None = None,
    *,
    min_length: int | None = None,
    max_length: int | None = None,
    fail_fast: bool | None = None,
    strict: bool | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> FrozenSetSchema:
    """
    Returns a schema that matches a frozenset of a given schema, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    schema = core_schema.frozenset_schema(
        items_schema=core_schema.int_schema(), min_length=0, max_length=10
    )
    v = SchemaValidator(schema)
    assert v.validate_python(frozenset(range(3))) == frozenset({0, 1, 2})
```

    Args:
        items_schema: The value must be a frozenset with items that match this schema
        min_length: The value must be a frozenset with at least this many items
        max_length: The value must be a frozenset with at most this many items
        fail_fast: Stop validation on the first error
        strict: The value must be a frozenset with exactly this many items
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='frozenset',
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
##  generator_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.generator_schema)
```
generator_schema(
    items_schema: CoreSchema | None = None,
    *,
    min_length:  | None = None,
    max_length:  | None = None,
    ref:  | None = None,
    metadata: [, ] | None = None,
    serialization: IncExSeqOrElseSerSchema | None = None
) -> GeneratorSchema

```

Returns a schema that matches a generator value, e.g.:
```
from typing import Iterator
from pydantic_core import SchemaValidator, core_schema

def gen() -> Iterator[int]:
    yield 1

schema = core_schema.generator_schema(items_schema=core_schema.int_schema())
v = SchemaValidator(schema)
v.validate_python(gen())

```

Unlike other types, validated generators do not raise ValidationErrors eagerly, but instead will raise a ValidationError when a violating value is actually read from the generator. This is to ensure that "validated" generators retain the benefit of lazy evaluation.
Parameters:
Name | Type | Description | Default
---|---|---|---
`items_schema` |  `CoreSchema | None` |  The value must be a generator with items that match this schema |  `None`
`min_length` |  |  The value must be a generator that yields at least this many items |  `None`
`max_length` |  |  The value must be a generator that yields at most this many items |  `None`
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`
`serialization` |  `IncExSeqOrElseSerSchema | None` |  Custom serialization schema |  `None`
Source code in `pydantic_core/core_schema.py`
```
1875
1876
1877
1878
1879
1880
1881
1882
1883
1884
1885
1886
1887
1888
1889
1890
1891
1892
1893
1894
1895
1896
1897
1898
1899
1900
1901
1902
1903
1904
1905
1906
1907
1908
1909
1910
1911
1912
1913
1914
1915
1916
1917
1918
1919
```
| ```
def generator_schema(
    items_schema: CoreSchema | None = None,
    *,
    min_length: int | None = None,
    max_length: int | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: IncExSeqOrElseSerSchema | None = None,
) -> GeneratorSchema:
    """
    Returns a schema that matches a generator value, e.g.:

```py
    from typing import Iterator
    from pydantic_core import SchemaValidator, core_schema

    def gen() -> Iterator[int]:
        yield 1

    schema = core_schema.generator_schema(items_schema=core_schema.int_schema())
    v = SchemaValidator(schema)
    v.validate_python(gen())
```

    Unlike other types, validated generators do not raise ValidationErrors eagerly,
    but instead will raise a ValidationError when a violating value is actually read from the generator.
    This is to ensure that "validated" generators retain the benefit of lazy evaluation.

    Args:
        items_schema: The value must be a generator with items that match this schema
        min_length: The value must be a generator that yields at least this many items
        max_length: The value must be a generator that yields at most this many items
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='generator',
        items_schema=items_schema,
        min_length=min_length,
        max_length=max_length,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
    )

```

---|---
