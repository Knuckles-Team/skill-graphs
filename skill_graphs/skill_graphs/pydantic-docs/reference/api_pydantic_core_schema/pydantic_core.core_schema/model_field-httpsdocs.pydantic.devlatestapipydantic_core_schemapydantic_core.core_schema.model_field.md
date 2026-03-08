##  model_field [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.model_field)
```
model_field(
    schema: CoreSchema,
    *,
    validation_alias: (
         | [ | ] | [[ | ]] | None
    ) = None,
    serialization_alias:  | None = None,
    serialization_exclude:  | None = None,
    serialization_exclude_if: (
        [[], ] | None
    ) = None,
    frozen:  | None = None,
    metadata: [, ] | None = None
) -> ModelField

```

Returns a schema for a model field, e.g.:
```
from pydantic_core import core_schema

field = core_schema.model_field(schema=core_schema.int_schema())

```

Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `CoreSchema` |  The schema to use for the field |  _required_
`validation_alias` |  |  The alias(es) to use to find the field in the validation data |  `None`
`serialization_alias` |  |  The alias to use as a key when serializing |  `None`
`serialization_exclude` |  |  Whether to exclude the field when serializing |  `None`
`serialization_exclude_if` |  |  A Callable that determines whether to exclude a field during serialization based on its value. |  `None`
`frozen` |  |  Whether the field is frozen |  `None`
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`
Source code in `pydantic_core/core_schema.py`
```
3065
3066
3067
3068
3069
3070
3071
3072
3073
3074
3075
3076
3077
3078
3079
3080
3081
3082
3083
3084
3085
3086
3087
3088
3089
3090
3091
3092
3093
3094
3095
3096
3097
3098
3099
3100
3101
3102
```
| ```
def model_field(
    schema: CoreSchema,
    *,
    validation_alias: str | list[str | int] | list[list[str | int]] | None = None,
    serialization_alias: str | None = None,
    serialization_exclude: bool | None = None,
    serialization_exclude_if: Callable[[Any], bool] | None = None,
    frozen: bool | None = None,
    metadata: dict[str, Any] | None = None,
) -> ModelField:
    """
    Returns a schema for a model field, e.g.:

```py
    from pydantic_core import core_schema

    field = core_schema.model_field(schema=core_schema.int_schema())
```

    Args:
        schema: The schema to use for the field
        validation_alias: The alias(es) to use to find the field in the validation data
        serialization_alias: The alias to use as a key when serializing
        serialization_exclude: Whether to exclude the field when serializing
        serialization_exclude_if: A Callable that determines whether to exclude a field during serialization based on its value.
        frozen: Whether the field is frozen
        metadata: Any other information you want to include with the schema, not used by pydantic-core
    """
    return _dict_not_none(
        type='model-field',
        schema=schema,
        validation_alias=validation_alias,
        serialization_alias=serialization_alias,
        serialization_exclude=serialization_exclude,
        serialization_exclude_if=serialization_exclude_if,
        frozen=frozen,
        metadata=metadata,
    )

```

---|---
##  model_fields_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.model_fields_schema)
```
model_fields_schema(
    fields: [, ModelField],
    *,
    model_name:  | None = None,
    computed_fields: [ComputedField] | None = None,
    strict:  | None = None,
    extras_schema: CoreSchema | None = None,
    extras_keys_schema: CoreSchema | None = None,
    extra_behavior: ExtraBehavior | None = None,
    from_attributes:  | None = None,
    ref:  | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> ModelFieldsSchema

```

Returns a schema that matches the fields of a Pydantic model, e.g.:
```
from pydantic_core import SchemaValidator, core_schema

wrapper_schema = core_schema.model_fields_schema(
    {'a': core_schema.model_field(core_schema.str_schema())}
)
v = SchemaValidator(wrapper_schema)
print(v.validate_python({'a': 'hello'}))
#> ({'a': 'hello'}, None, {'a'})

```

Parameters:
Name | Type | Description | Default
---|---|---|---
`fields` |  `ModelField]` |  The fields of the model |  _required_
`model_name` |  |  The name of the model, used for error messages, defaults to "Model" |  `None`
`computed_fields` |  `ComputedField] | None` |  Computed fields to use when serializing the model, only applies when directly inside a model |  `None`
`strict` |  |  Whether the model is strict |  `None`
`extras_schema` |  `CoreSchema | None` |  The schema to use when validating extra input data |  `None`
`extras_keys_schema` |  `CoreSchema | None` |  The schema to use when validating the keys of extra input data |  `None`
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`
`extra_behavior` |  `ExtraBehavior | None` |  The extra behavior to use for the model fields |  `None`
`from_attributes` |  |  Whether the model fields should be populated from attributes |  `None`
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`
Source code in `pydantic_core/core_schema.py`
```
3120
3121
3122
3123
3124
3125
3126
3127
3128
3129
3130
3131
3132
3133
3134
3135
3136
3137
3138
3139
3140
3141
3142
3143
3144
3145
3146
3147
3148
3149
3150
3151
3152
3153
3154
3155
3156
3157
3158
3159
3160
3161
3162
3163
3164
3165
3166
3167
3168
3169
3170
3171
3172
3173
3174
```
| ```
def model_fields_schema(
    fields: dict[str, ModelField],
    *,
    model_name: str | None = None,
    computed_fields: list[ComputedField] | None = None,
    strict: bool | None = None,
    extras_schema: CoreSchema | None = None,
    extras_keys_schema: CoreSchema | None = None,
    extra_behavior: ExtraBehavior | None = None,
    from_attributes: bool | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> ModelFieldsSchema:
    """
    Returns a schema that matches the fields of a Pydantic model, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    wrapper_schema = core_schema.model_fields_schema(
        {'a': core_schema.model_field(core_schema.str_schema())}
    )
    v = SchemaValidator(wrapper_schema)
    print(v.validate_python({'a': 'hello'}))
    #> ({'a': 'hello'}, None, {'a'})
```

    Args:
        fields: The fields of the model
        model_name: The name of the model, used for error messages, defaults to "Model"
        computed_fields: Computed fields to use when serializing the model, only applies when directly inside a model
        strict: Whether the model is strict
        extras_schema: The schema to use when validating extra input data
        extras_keys_schema: The schema to use when validating the keys of extra input data
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        extra_behavior: The extra behavior to use for the model fields
        from_attributes: Whether the model fields should be populated from attributes
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='model-fields',
        fields=fields,
        model_name=model_name,
        computed_fields=computed_fields,
        strict=strict,
        extras_schema=extras_schema,
        extras_keys_schema=extras_keys_schema,
        extra_behavior=extra_behavior,
        from_attributes=from_attributes,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
    )

```

---|---
