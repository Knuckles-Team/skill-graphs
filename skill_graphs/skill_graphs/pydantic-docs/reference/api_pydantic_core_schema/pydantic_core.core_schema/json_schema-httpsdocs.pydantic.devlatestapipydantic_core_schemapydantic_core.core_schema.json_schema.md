##  json_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.json_schema)
```
json_schema(
    schema: CoreSchema | None = None,
    *,
    ref:  | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> JsonSchema

```

Returns a schema that matches a JSON value, e.g.:
```
from pydantic_core import SchemaValidator, core_schema

dict_schema = core_schema.model_fields_schema(
    {
        'field_a': core_schema.model_field(core_schema.str_schema()),
        'field_b': core_schema.model_field(core_schema.bool_schema()),
    },
)

class MyModel:
    __slots__ = (
        '__dict__',
        '__pydantic_fields_set__',
        '__pydantic_extra__',
        '__pydantic_private__',
    )
    field_a: str
    field_b: bool

json_schema = core_schema.json_schema(schema=dict_schema)
schema = core_schema.model_schema(cls=MyModel, schema=json_schema)
v = SchemaValidator(schema)
m = v.validate_python('{"field_a": "hello", "field_b": true}')
assert isinstance(m, MyModel)

```

Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `CoreSchema | None` |  The schema to use for the JSON schema |  `None`
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`
Source code in `pydantic_core/core_schema.py`
```
3845
3846
3847
3848
3849
3850
3851
3852
3853
3854
3855
3856
3857
3858
3859
3860
3861
3862
3863
3864
3865
3866
3867
3868
3869
3870
3871
3872
3873
3874
3875
3876
3877
3878
3879
3880
3881
3882
3883
3884
3885
3886
3887
3888
```
| ```
def json_schema(
    schema: CoreSchema | None = None,
    *,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> JsonSchema:
    """
    Returns a schema that matches a JSON value, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    dict_schema = core_schema.model_fields_schema(
        {
            'field_a': core_schema.model_field(core_schema.str_schema()),
            'field_b': core_schema.model_field(core_schema.bool_schema()),
        },
    )

    class MyModel:
        __slots__ = (
            '__dict__',
            '__pydantic_fields_set__',
            '__pydantic_extra__',
            '__pydantic_private__',
        )
        field_a: str
        field_b: bool

    json_schema = core_schema.json_schema(schema=dict_schema)
    schema = core_schema.model_schema(cls=MyModel, schema=json_schema)
    v = SchemaValidator(schema)
    m = v.validate_python('{"field_a": "hello", "field_b": true}')
    assert isinstance(m, MyModel)
```

    Args:
        schema: The schema to use for the JSON schema
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(type='json', schema=schema, ref=ref, metadata=metadata, serialization=serialization)

```

---|---
##  url_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.url_schema)
```
url_schema(
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
) -> UrlSchema

```

Returns a schema that matches a URL value, e.g.:
```
from pydantic_core import SchemaValidator, core_schema

schema = core_schema.url_schema()
v = SchemaValidator(schema)
print(v.validate_python('https://example.com'))
#> https://example.com/

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
3905
3906
3907
3908
3909
3910
3911
3912
3913
3914
3915
3916
3917
3918
3919
3920
3921
3922
3923
3924
3925
3926
3927
3928
3929
3930
3931
3932
3933
3934
3935
3936
3937
3938
3939
3940
3941
3942
3943
3944
3945
3946
3947
3948
3949
3950
3951
3952
3953
3954
3955
3956
3957
```
| ```
def url_schema(
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
) -> UrlSchema:
    """
    Returns a schema that matches a URL value, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    schema = core_schema.url_schema()
    v = SchemaValidator(schema)
    print(v.validate_python('https://example.com'))
    #> https://example.com/
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
        type='url',
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
