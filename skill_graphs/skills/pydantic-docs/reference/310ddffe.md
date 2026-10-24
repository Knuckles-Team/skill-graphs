##  typed_dict_field [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.typed_dict_field)
```
typed_dict_field(
    schema: CoreSchema,
    *,
    required:  | None = None,
    validation_alias: (
         | [ | ] | [[ | ]] | None
    ) = None,
    serialization_alias:  | None = None,
    serialization_exclude:  | None = None,
    metadata: [, ] | None = None,
    serialization_exclude_if: (
        [[], ] | None
    ) = None
) -> TypedDictField

```

Returns a schema that matches a typed dict field, e.g.:
```
from pydantic_core import core_schema

field = core_schema.typed_dict_field(schema=core_schema.int_schema(), required=True)

```

Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `CoreSchema` |  The schema to use for the field |  _required_
`required` |  |  Whether the field is required, otherwise uses the value from `total` on the typed dict |  `None`
`validation_alias` |  |  The alias(es) to use to find the field in the validation data |  `None`
`serialization_alias` |  |  The alias to use as a key when serializing |  `None`
`serialization_exclude` |  |  Whether to exclude the field when serializing |  `None`
`serialization_exclude_if` |  |  A callable that determines whether to exclude the field when serializing based on its value. |  `None`
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`
Source code in `pydantic_core/core_schema.py`
```
2933
2934
2935
2936
2937
2938
2939
2940
2941
2942
2943
2944
2945
2946
2947
2948
2949
2950
2951
2952
2953
2954
2955
2956
2957
2958
2959
2960
2961
2962
2963
2964
2965
2966
2967
2968
2969
2970
```
| ```
def typed_dict_field(
    schema: CoreSchema,
    *,
    required: bool | None = None,
    validation_alias: str | list[str | int] | list[list[str | int]] | None = None,
    serialization_alias: str | None = None,
    serialization_exclude: bool | None = None,
    metadata: dict[str, Any] | None = None,
    serialization_exclude_if: Callable[[Any], bool] | None = None,
) -> TypedDictField:
    """
    Returns a schema that matches a typed dict field, e.g.:

```py
    from pydantic_core import core_schema

    field = core_schema.typed_dict_field(schema=core_schema.int_schema(), required=True)
```

    Args:
        schema: The schema to use for the field
        required: Whether the field is required, otherwise uses the value from `total` on the typed dict
        validation_alias: The alias(es) to use to find the field in the validation data
        serialization_alias: The alias to use as a key when serializing
        serialization_exclude: Whether to exclude the field when serializing
        serialization_exclude_if: A callable that determines whether to exclude the field when serializing based on its value.
        metadata: Any other information you want to include with the schema, not used by pydantic-core
    """
    return _dict_not_none(
        type='typed-dict-field',
        schema=schema,
        required=required,
        validation_alias=validation_alias,
        serialization_alias=serialization_alias,
        serialization_exclude=serialization_exclude,
        serialization_exclude_if=serialization_exclude_if,
        metadata=metadata,
    )

```

---|---
##  typed_dict_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.typed_dict_schema)
```
typed_dict_schema(
    fields: [, TypedDictField],
    *,
    cls: [] | None = None,
    cls_name:  | None = None,
    computed_fields: [ComputedField] | None = None,
    strict:  | None = None,
    extras_schema: CoreSchema | None = None,
    extra_behavior: ExtraBehavior | None = None,
    total:  | None = None,
    ref:  | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None,
    config: CoreConfig[](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.CoreConfig) | None = None
) -> TypedDictSchema

```

Returns a schema that matches a typed dict, e.g.:
```
from typing_extensions import TypedDict

from pydantic_core import SchemaValidator, core_schema

class MyTypedDict(TypedDict):
    a: str

wrapper_schema = core_schema.typed_dict_schema(
    {'a': core_schema.typed_dict_field(core_schema.str_schema())}, cls=MyTypedDict
)
v = SchemaValidator(wrapper_schema)
assert v.validate_python({'a': 'hello'}) == {'a': 'hello'}

```

Parameters:
Name | Type | Description | Default
---|---|---|---
`fields` |  `TypedDictField]` |  The fields to use for the typed dict |  _required_
`cls` |  |  The class to use for the typed dict |  `None`
`cls_name` |  |  The name to use in error locations. Falls back to `cls.__name__`, or the validator name if no class is provided. |  `None`
`computed_fields` |  `ComputedField] | None` |  Computed fields to use when serializing the model, only applies when directly inside a model |  `None`
`strict` |  |  Whether the typed dict is strict |  `None`
`extras_schema` |  `CoreSchema | None` |  The extra validator to use for the typed dict |  `None`
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`
`extra_behavior` |  `ExtraBehavior | None` |  The extra behavior to use for the typed dict |  `None`
`total` |  |  Whether the typed dict is total, otherwise uses `typed_dict_total` from config |  `None`
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`
Source code in `pydantic_core/core_schema.py`
```
2990
2991
2992
2993
2994
2995
2996
2997
2998
2999
3000
3001
3002
3003
3004
3005
3006
3007
3008
3009
3010
3011
3012
3013
3014
3015
3016
3017
3018
3019
3020
3021
3022
3023
3024
3025
3026
3027
3028
3029
3030
3031
3032
3033
3034
3035
3036
3037
3038
3039
3040
3041
3042
3043
3044
3045
3046
3047
3048
3049
3050
3051
```
| ```
def typed_dict_schema(
    fields: dict[str, TypedDictField],
    *,
    cls: type[Any] | None = None,
    cls_name: str | None = None,
    computed_fields: list[ComputedField] | None = None,
    strict: bool | None = None,
    extras_schema: CoreSchema | None = None,
    extra_behavior: ExtraBehavior | None = None,
    total: bool | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
    config: CoreConfig | None = None,
) -> TypedDictSchema:
    """
    Returns a schema that matches a typed dict, e.g.:

```py
    from typing_extensions import TypedDict

    from pydantic_core import SchemaValidator, core_schema

    class MyTypedDict(TypedDict):
        a: str

    wrapper_schema = core_schema.typed_dict_schema(
        {'a': core_schema.typed_dict_field(core_schema.str_schema())}, cls=MyTypedDict
    )
    v = SchemaValidator(wrapper_schema)
    assert v.validate_python({'a': 'hello'}) == {'a': 'hello'}
```

    Args:
        fields: The fields to use for the typed dict
        cls: The class to use for the typed dict
        cls_name: The name to use in error locations. Falls back to `cls.__name__`, or the validator name if no class
            is provided.
        computed_fields: Computed fields to use when serializing the model, only applies when directly inside a model
        strict: Whether the typed dict is strict
        extras_schema: The extra validator to use for the typed dict
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        extra_behavior: The extra behavior to use for the typed dict
        total: Whether the typed dict is total, otherwise uses `typed_dict_total` from config
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='typed-dict',
        fields=fields,
        cls=cls,
        cls_name=cls_name,
        computed_fields=computed_fields,
        strict=strict,
        extras_schema=extras_schema,
        extra_behavior=extra_behavior,
        total=total,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
        config=config,
    )

```

---|---
