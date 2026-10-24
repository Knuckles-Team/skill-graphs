##  multi_host_url_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.multi_host_url_schema)
```
multi_host_url_schema(
    *,
    max_length:  | None = None,
    allowed_schemes: [] | None = None,
    host_required:  | None = None,
    default_host:  | None = None,
    default_port:  | None = None,
    default_path:  | None = None,
    preserve_empty_path:  | None = None,
    strict:  | None = None,
    ref:  | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> MultiHostUrlSchema

```

Returns a schema that matches a URL value with possibly multiple hosts, e.g.:
```
from pydantic_core import SchemaValidator, core_schema

schema = core_schema.multi_host_url_schema()
v = SchemaValidator(schema)
print(v.validate_python('redis://localhost,0.0.0.0,127.0.0.1'))
#> redis://localhost,0.0.0.0,127.0.0.1

```

Parameters:
Name | Type | Description | Default
---|---|---|---
`max_length` |  |  The maximum length of the URL |  `None`
`allowed_schemes` |  |  The allowed URL schemes |  `None`
`host_required` |  |  Whether the URL must have a host |  `None`
`default_host` |  |  The default host to use if the URL does not have a host |  `None`
`default_port` |  |  The default port to use if the URL does not have a port |  `None`
`default_path` |  |  The default path to use if the URL does not have a path |  `None`
`preserve_empty_path` |  |  Whether to preserve an empty path or convert it to '/', default False |  `None`
`strict` |  |  Whether to use strict URL parsing |  `None`
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`
Source code in `pydantic_core/core_schema.py`
```
3974
3975
3976
3977
3978
3979
3980
3981
3982
3983
3984
3985
3986
3987
3988
3989
3990
3991
3992
3993
3994
3995
3996
3997
3998
3999
4000
4001
4002
4003
4004
4005
4006
4007
4008
4009
4010
4011
4012
4013
4014
4015
4016
4017
4018
4019
4020
4021
4022
4023
4024
4025
4026
```
| ```
def multi_host_url_schema(
    *,
    max_length: int | None = None,
    allowed_schemes: list[str] | None = None,
    host_required: bool | None = None,
    default_host: str | None = None,
    default_port: int | None = None,
    default_path: str | None = None,
    preserve_empty_path: bool | None = None,
    strict: bool | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> MultiHostUrlSchema:
    """
    Returns a schema that matches a URL value with possibly multiple hosts, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    schema = core_schema.multi_host_url_schema()
    v = SchemaValidator(schema)
    print(v.validate_python('redis://localhost,0.0.0.0,127.0.0.1'))
    #> redis://localhost,0.0.0.0,127.0.0.1
```

    Args:
        max_length: The maximum length of the URL
        allowed_schemes: The allowed URL schemes
        host_required: Whether the URL must have a host
        default_host: The default host to use if the URL does not have a host
        default_port: The default port to use if the URL does not have a port
        default_path: The default path to use if the URL does not have a path
        preserve_empty_path: Whether to preserve an empty path or convert it to '/', default False
        strict: Whether to use strict URL parsing
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='multi-host-url',
        max_length=max_length,
        allowed_schemes=allowed_schemes,
        host_required=host_required,
        default_host=default_host,
        default_port=default_port,
        default_path=default_path,
        preserve_empty_path=preserve_empty_path,
        strict=strict,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
    )

```

---|---
##  definitions_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.definitions_schema)
```
definitions_schema(
    schema: CoreSchema, definitions: [CoreSchema]
) -> DefinitionsSchema

```

Build a schema that contains both an inner schema and a list of definitions which can be used within the inner schema.
```
from pydantic_core import SchemaValidator, core_schema

schema = core_schema.definitions_schema(
    core_schema.list_schema(core_schema.definition_reference_schema('foobar')),
    [core_schema.int_schema(ref='foobar')],
)
v = SchemaValidator(schema)
assert v.validate_python([1, 2, '3']) == [1, 2, 3]

```

Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `CoreSchema` |  The inner schema |  _required_
`definitions` |  `CoreSchema]` |  List of definitions which can be referenced within inner schema |  _required_
Source code in `pydantic_core/core_schema.py`
```
4037
4038
4039
4040
4041
4042
4043
4044
4045
4046
4047
4048
4049
4050
4051
4052
4053
4054
4055
4056
4057
```
| ```
def definitions_schema(schema: CoreSchema, definitions: list[CoreSchema]) -> DefinitionsSchema:
    """
    Build a schema that contains both an inner schema and a list of definitions which can be used
    within the inner schema.

```py
    from pydantic_core import SchemaValidator, core_schema

    schema = core_schema.definitions_schema(
        core_schema.list_schema(core_schema.definition_reference_schema('foobar')),
        [core_schema.int_schema(ref='foobar')],
    )
    v = SchemaValidator(schema)
    assert v.validate_python([1, 2, '3']) == [1, 2, 3]
```

    Args:
        schema: The inner schema
        definitions: List of definitions which can be referenced within inner schema
    """
    return DefinitionsSchema(type='definitions', schema=schema, definitions=definitions)

```

---|---
