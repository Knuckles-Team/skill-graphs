##  invalid_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.invalid_schema)
```
invalid_schema(
    ref:  | None = None,
    metadata: [, ] | None = None,
) -> InvalidSchema

```

Returns an invalid schema, used to indicate that a schema is invalid.
```
Returns a schema that matches any value, e.g.:

```

Parameters:
Name | Type | Description | Default
---|---|---|---
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`
Source code in `pydantic_core/core_schema.py`
```
484
485
486
487
488
489
490
491
492
493
494
495
```
| ```
def invalid_schema(ref: str | None = None, metadata: dict[str, Any] | None = None) -> InvalidSchema:
    """
    Returns an invalid schema, used to indicate that a schema is invalid.

        Returns a schema that matches any value, e.g.:

    Args:
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
    """

    return _dict_not_none(type='invalid', ref=ref, metadata=metadata)

```

---|---
##  computed_field [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.computed_field)
```
computed_field(
    property_name: ,
    return_schema: CoreSchema,
    *,
    alias:  | None = None,
    metadata: [, ] | None = None
) -> ComputedField

```

ComputedFields are properties of a model or dataclass that are included in serialization.
Parameters:
Name | Type | Description | Default
---|---|---|---
`property_name` |  |  The name of the property on the model or dataclass |  _required_
`return_schema` |  `CoreSchema` |  The schema used for the type returned by the computed field |  _required_
`alias` |  |  The name to use in the serialized output |  `None`
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`
Source code in `pydantic_core/core_schema.py`
```
506
507
508
509
510
511
512
513
514
515
516
517
518
519
520
```
| ```
def computed_field(
    property_name: str, return_schema: CoreSchema, *, alias: str | None = None, metadata: dict[str, Any] | None = None
) -> ComputedField:
    """
    ComputedFields are properties of a model or dataclass that are included in serialization.

    Args:
        property_name: The name of the property on the model or dataclass
        return_schema: The schema used for the type returned by the computed field
        alias: The name to use in the serialized output
        metadata: Any other information you want to include with the schema, not used by pydantic-core
    """
    return _dict_not_none(
        type='computed-field', property_name=property_name, return_schema=return_schema, alias=alias, metadata=metadata
    )

```

---|---
