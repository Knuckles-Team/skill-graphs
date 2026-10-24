##  model_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.model_schema)
```
model_schema(
    cls: [],
    schema: CoreSchema,
    *,
    generic_origin: [] | None = None,
    custom_init:  | None = None,
    root_model:  | None = None,
    post_init:  | None = None,
    revalidate_instances: (
        ["always", "never", "subclass-instances"]
        | None
    ) = None,
    strict:  | None = None,
    frozen:  | None = None,
    extra_behavior: ExtraBehavior | None = None,
    config: CoreConfig[](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.CoreConfig) | None = None,
    ref:  | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> ModelSchema

```

A model schema generally contains a typed-dict schema. It will run the typed dict validator, then create a new class and set the dict and fields set returned from the typed dict validator to `__dict__` and `__pydantic_fields_set__` respectively.
Example:
```
from pydantic_core import CoreConfig, SchemaValidator, core_schema

class MyModel:
    __slots__ = (
        '__dict__',
        '__pydantic_fields_set__',
        '__pydantic_extra__',
        '__pydantic_private__',
    )

schema = core_schema.model_schema(
    cls=MyModel,
    config=CoreConfig(str_max_length=5),
    schema=core_schema.model_fields_schema(
        fields={'a': core_schema.model_field(core_schema.str_schema())},
    ),
)
v = SchemaValidator(schema)
assert v.isinstance_python({'a': 'hello'}) is True
assert v.isinstance_python({'a': 'too long'}) is False

```

Parameters:
Name | Type | Description | Default
---|---|---|---
`cls` |  |  The class to use for the model |  _required_
`schema` |  `CoreSchema` |  The schema to use for the model |  _required_
`generic_origin` |  |  The origin type used for this model, if it's a parametrized generic. Ex, if this model schema represents `SomeModel[int]`, generic_origin is `SomeModel` |  `None`
`custom_init` |  |  Whether the model has a custom init method |  `None`
`root_model` |  |  Whether the model is a `RootModel` |  `None`
`post_init` |  |  The call after init to use for the model |  `None`
`revalidate_instances` |  |  whether instances of models and dataclasses (including subclass instances) should re-validate defaults to config.revalidate_instances, else 'never' |  `None`
`strict` |  |  Whether the model is strict |  `None`
`frozen` |  |  Whether the model is frozen |  `None`
`extra_behavior` |  `ExtraBehavior | None` |  The extra behavior to use for the model, used in serialization |  `None`
`config` |  `CoreConfig[](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.CoreConfig) | None` |  The config to use for the model |  `None`
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`
Source code in `pydantic_core/core_schema.py`
```
3195
3196
3197
3198
3199
3200
3201
3202
3203
3204
3205
3206
3207
3208
3209
3210
3211
3212
3213
3214
3215
3216
3217
3218
3219
3220
3221
3222
3223
3224
3225
3226
3227
3228
3229
3230
3231
3232
3233
3234
3235
3236
3237
3238
3239
3240
3241
3242
3243
3244
3245
3246
3247
3248
3249
3250
3251
3252
3253
3254
3255
3256
3257
3258
3259
3260
3261
3262
3263
3264
3265
3266
3267
3268
3269
3270
3271
3272
3273
3274
3275
3276
3277
```
| ```
def model_schema(
    cls: type[Any],
    schema: CoreSchema,
    *,
    generic_origin: type[Any] | None = None,
    custom_init: bool | None = None,
    root_model: bool | None = None,
    post_init: str | None = None,
    revalidate_instances: Literal['always', 'never', 'subclass-instances'] | None = None,
    strict: bool | None = None,
    frozen: bool | None = None,
    extra_behavior: ExtraBehavior | None = None,
    config: CoreConfig | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> ModelSchema:
    """
    A model schema generally contains a typed-dict schema.
    It will run the typed dict validator, then create a new class
    and set the dict and fields set returned from the typed dict validator
    to `__dict__` and `__pydantic_fields_set__` respectively.

    Example:

```py
    from pydantic_core import CoreConfig, SchemaValidator, core_schema

    class MyModel:
        __slots__ = (
            '__dict__',
            '__pydantic_fields_set__',
            '__pydantic_extra__',
            '__pydantic_private__',
        )

    schema = core_schema.model_schema(
        cls=MyModel,
        config=CoreConfig(str_max_length=5),
        schema=core_schema.model_fields_schema(
            fields={'a': core_schema.model_field(core_schema.str_schema())},
        ),
    )
    v = SchemaValidator(schema)
    assert v.isinstance_python({'a': 'hello'}) is True
    assert v.isinstance_python({'a': 'too long'}) is False
```

    Args:
        cls: The class to use for the model
        schema: The schema to use for the model
        generic_origin: The origin type used for this model, if it's a parametrized generic. Ex,
            if this model schema represents `SomeModel[int]`, generic_origin is `SomeModel`
        custom_init: Whether the model has a custom init method
        root_model: Whether the model is a `RootModel`
        post_init: The call after init to use for the model
        revalidate_instances: whether instances of models and dataclasses (including subclass instances)
            should re-validate defaults to config.revalidate_instances, else 'never'
        strict: Whether the model is strict
        frozen: Whether the model is frozen
        extra_behavior: The extra behavior to use for the model, used in serialization
        config: The config to use for the model
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='model',
        cls=cls,
        generic_origin=generic_origin,
        schema=schema,
        custom_init=custom_init,
        root_model=root_model,
        post_init=post_init,
        revalidate_instances=revalidate_instances,
        strict=strict,
        frozen=frozen,
        extra_behavior=extra_behavior,
        config=config,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
    )

```

---|---
##  dataclass_field [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.dataclass_field)
```
dataclass_field(
    name: ,
    schema: CoreSchema,
    *,
    kw_only:  | None = None,
    init:  | None = None,
    init_only:  | None = None,
    validation_alias: (
         | [ | ] | [[ | ]] | None
    ) = None,
    serialization_alias:  | None = None,
    serialization_exclude:  | None = None,
    metadata: [, ] | None = None,
    serialization_exclude_if: (
        [[], ] | None
    ) = None,
    frozen:  | None = None
) -> DataclassField

```

Returns a schema for a dataclass field, e.g.:
```
from pydantic_core import SchemaValidator, core_schema

field = core_schema.dataclass_field(
    name='a', schema=core_schema.str_schema(), kw_only=False
)
schema = core_schema.dataclass_args_schema('Foobar', [field])
v = SchemaValidator(schema)
assert v.validate_python({'a': 'hello'}) == ({'a': 'hello'}, None)

```

Parameters:
Name | Type | Description | Default
---|---|---|---
`name` |  |  The name to use for the argument parameter |  _required_
`schema` |  `CoreSchema` |  The schema to use for the argument parameter |  _required_
`kw_only` |  |  Whether the field can be set with a positional argument as well as a keyword argument |  `None`
`init` |  |  Whether the field should be validated during initialization |  `None`
`init_only` |  |  Whether the field should be omitted from `__dict__` and passed to `__post_init__` |  `None`
`validation_alias` |  |  The alias(es) to use to find the field in the validation data |  `None`
`serialization_alias` |  |  The alias to use as a key when serializing |  `None`
`serialization_exclude` |  |  Whether to exclude the field when serializing |  `None`
`serialization_exclude_if` |  |  A callable that determines whether to exclude the field when serializing based on its value. |  `None`
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`
`frozen` |  |  Whether the field is frozen |  `None`
Source code in `pydantic_core/core_schema.py`
```
3295
3296
3297
3298
3299
3300
3301
3302
3303
3304
3305
3306
3307
3308
3309
3310
3311
3312
3313
3314
3315
3316
3317
3318
3319
3320
3321
3322
3323
3324
3325
3326
3327
3328
3329
3330
3331
3332
3333
3334
3335
3336
3337
3338
3339
3340
3341
3342
3343
3344
3345
3346
3347
3348
3349
```
| ```
def dataclass_field(
    name: str,
    schema: CoreSchema,
    *,
    kw_only: bool | None = None,
    init: bool | None = None,
    init_only: bool | None = None,
    validation_alias: str | list[str | int] | list[list[str | int]] | None = None,
    serialization_alias: str | None = None,
    serialization_exclude: bool | None = None,
    metadata: dict[str, Any] | None = None,
    serialization_exclude_if: Callable[[Any], bool] | None = None,
    frozen: bool | None = None,
) -> DataclassField:
    """
    Returns a schema for a dataclass field, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    field = core_schema.dataclass_field(
        name='a', schema=core_schema.str_schema(), kw_only=False
    )
    schema = core_schema.dataclass_args_schema('Foobar', [field])
    v = SchemaValidator(schema)
    assert v.validate_python({'a': 'hello'}) == ({'a': 'hello'}, None)
```

    Args:
        name: The name to use for the argument parameter
        schema: The schema to use for the argument parameter
        kw_only: Whether the field can be set with a positional argument as well as a keyword argument
        init: Whether the field should be validated during initialization
        init_only: Whether the field should be omitted  from `__dict__` and passed to `__post_init__`
        validation_alias: The alias(es) to use to find the field in the validation data
        serialization_alias: The alias to use as a key when serializing
        serialization_exclude: Whether to exclude the field when serializing
        serialization_exclude_if: A callable that determines whether to exclude the field when serializing based on its value.
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        frozen: Whether the field is frozen
    """
    return _dict_not_none(
        type='dataclass-field',
        name=name,
        schema=schema,
        kw_only=kw_only,
        init=init,
        init_only=init_only,
        validation_alias=validation_alias,
        serialization_alias=serialization_alias,
        serialization_exclude=serialization_exclude,
        serialization_exclude_if=serialization_exclude_if,
        metadata=metadata,
        frozen=frozen,
    )

```

---|---
