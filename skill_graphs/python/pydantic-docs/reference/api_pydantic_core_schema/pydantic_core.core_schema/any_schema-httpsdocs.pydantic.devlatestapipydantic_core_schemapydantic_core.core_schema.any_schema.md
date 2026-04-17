##  any_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.any_schema)
```
any_schema(
    *,
    ref:  | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> AnySchema

```

Returns a schema that matches any value, e.g.:
```
from pydantic_core import SchemaValidator, core_schema

schema = core_schema.any_schema()
v = SchemaValidator(schema)
assert v.validate_python(1) == 1

```

Parameters:
Name | Type | Description | Default
---|---|---|---
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`
Source code in `pydantic_core/core_schema.py`
```
530
531
532
533
534
535
536
537
538
539
540
541
542
543
544
545
546
547
548
549
```
| ```
def any_schema(
    *, ref: str | None = None, metadata: dict[str, Any] | None = None, serialization: SerSchema | None = None
) -> AnySchema:
    """
    Returns a schema that matches any value, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    schema = core_schema.any_schema()
    v = SchemaValidator(schema)
    assert v.validate_python(1) == 1
```

    Args:
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(type='any', ref=ref, metadata=metadata, serialization=serialization)

```

---|---
##  none_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.none_schema)
```
none_schema(
    *,
    ref:  | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> NoneSchema

```

Returns a schema that matches a None value, e.g.:
```
from pydantic_core import SchemaValidator, core_schema

schema = core_schema.none_schema()
v = SchemaValidator(schema)
assert v.validate_python(None) is None

```

Parameters:
Name | Type | Description | Default
---|---|---|---
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`
Source code in `pydantic_core/core_schema.py`
```
559
560
561
562
563
564
565
566
567
568
569
570
571
572
573
574
575
576
577
578
```
| ```
def none_schema(
    *, ref: str | None = None, metadata: dict[str, Any] | None = None, serialization: SerSchema | None = None
) -> NoneSchema:
    """
    Returns a schema that matches a None value, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    schema = core_schema.none_schema()
    v = SchemaValidator(schema)
    assert v.validate_python(None) is None
```

    Args:
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(type='none', ref=ref, metadata=metadata, serialization=serialization)

```

---|---
