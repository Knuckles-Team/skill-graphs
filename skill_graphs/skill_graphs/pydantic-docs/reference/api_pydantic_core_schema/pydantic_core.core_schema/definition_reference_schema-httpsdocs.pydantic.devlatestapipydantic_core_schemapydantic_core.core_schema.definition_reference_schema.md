##  definition_reference_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.definition_reference_schema)
```
definition_reference_schema(
    schema_ref: ,
    ref:  | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None,
) -> DefinitionReferenceSchema

```

Returns a schema that points to a schema stored in "definitions", this is useful for nested recursive models and also when you want to define validators separately from the main schema, e.g.:
```
from pydantic_core import SchemaValidator, core_schema

schema_definition = core_schema.definition_reference_schema('list-schema')
schema = core_schema.definitions_schema(
    schema=schema_definition,
    definitions=[
        core_schema.list_schema(items_schema=schema_definition, ref='list-schema'),
    ],
)
v = SchemaValidator(schema)
assert v.validate_python([()]) == [[]]

```

Parameters:
Name | Type | Description | Default
---|---|---|---
`schema_ref` |  |  The schema ref to use for the definition reference schema |  _required_
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`
Source code in `pydantic_core/core_schema.py`
```
4068
4069
4070
4071
4072
4073
4074
4075
4076
4077
4078
4079
4080
4081
4082
4083
4084
4085
4086
4087
4088
4089
4090
4091
4092
4093
4094
4095
4096
4097
4098
4099
```
| ```
def definition_reference_schema(
    schema_ref: str,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> DefinitionReferenceSchema:
    """
    Returns a schema that points to a schema stored in "definitions", this is useful for nested recursive
    models and also when you want to define validators separately from the main schema, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    schema_definition = core_schema.definition_reference_schema('list-schema')
    schema = core_schema.definitions_schema(
        schema=schema_definition,
        definitions=[
            core_schema.list_schema(items_schema=schema_definition, ref='list-schema'),
        ],
    )
    v = SchemaValidator(schema)
    assert v.validate_python([()]) == [[]]
```

    Args:
        schema_ref: The schema ref to use for the definition reference schema
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='definition-ref', schema_ref=schema_ref, ref=ref, metadata=metadata, serialization=serialization
    )

```

---|---
Was this page helpful?
Thanks for your feedback!
Thanks for your feedback!
Made with
