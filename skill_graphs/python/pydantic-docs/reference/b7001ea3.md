##  dataclass_args_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.dataclass_args_schema)
```
dataclass_args_schema(
    dataclass_name: ,
    fields: [DataclassField],
    *,
    computed_fields: [ComputedField] | None = None,
    collect_init_only:  | None = None,
    ref:  | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None,
    extra_behavior: ExtraBehavior | None = None
) -> DataclassArgsSchema

```

Returns a schema for validating dataclass arguments, e.g.:
```
from pydantic_core import SchemaValidator, core_schema

field_a = core_schema.dataclass_field(
    name='a', schema=core_schema.str_schema(), kw_only=False
)
field_b = core_schema.dataclass_field(
    name='b', schema=core_schema.bool_schema(), kw_only=False
)
schema = core_schema.dataclass_args_schema('Foobar', [field_a, field_b])
v = SchemaValidator(schema)
assert v.validate_python({'a': 'hello', 'b': True}) == ({'a': 'hello', 'b': True}, None)

```

Parameters:
Name | Type | Description | Default
---|---|---|---
`dataclass_name` |  |  The name of the dataclass being validated |  _required_
`fields` |  `DataclassField]` |  The fields to use for the dataclass |  _required_
`computed_fields` |  `ComputedField] | None` |  Computed fields to use when serializing the dataclass |  `None`
`collect_init_only` |  |  Whether to collect init only fields into a dict to pass to `__post_init__` |  `None`
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`
`extra_behavior` |  `ExtraBehavior | None` |  How to handle extra fields |  `None`
Source code in `pydantic_core/core_schema.py`
```
3364
3365
3366
3367
3368
3369
3370
3371
3372
3373
3374
3375
3376
3377
3378
3379
3380
3381
3382
3383
3384
3385
3386
3387
3388
3389
3390
3391
3392
3393
3394
3395
3396
3397
3398
3399
3400
3401
3402
3403
3404
3405
3406
3407
3408
3409
3410
3411
3412
```
| ```
def dataclass_args_schema(
    dataclass_name: str,
    fields: list[DataclassField],
    *,
    computed_fields: list[ComputedField] | None = None,
    collect_init_only: bool | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
    extra_behavior: ExtraBehavior | None = None,
) -> DataclassArgsSchema:
    """
    Returns a schema for validating dataclass arguments, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    field_a = core_schema.dataclass_field(
        name='a', schema=core_schema.str_schema(), kw_only=False
    )
    field_b = core_schema.dataclass_field(
        name='b', schema=core_schema.bool_schema(), kw_only=False
    )
    schema = core_schema.dataclass_args_schema('Foobar', [field_a, field_b])
    v = SchemaValidator(schema)
    assert v.validate_python({'a': 'hello', 'b': True}) == ({'a': 'hello', 'b': True}, None)
```

    Args:
        dataclass_name: The name of the dataclass being validated
        fields: The fields to use for the dataclass
        computed_fields: Computed fields to use when serializing the dataclass
        collect_init_only: Whether to collect init only fields into a dict to pass to `__post_init__`
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
        extra_behavior: How to handle extra fields
    """
    return _dict_not_none(
        type='dataclass-args',
        dataclass_name=dataclass_name,
        fields=fields,
        computed_fields=computed_fields,
        collect_init_only=collect_init_only,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
        extra_behavior=extra_behavior,
    )

```

---|---
##  dataclass_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.dataclass_schema)
```
dataclass_schema(
    cls: [],
    schema: CoreSchema,
    fields: [],
    *,
    generic_origin: [] | None = None,
    cls_name:  | None = None,
    post_init:  | None = None,
    revalidate_instances: (
        ["always", "never", "subclass-instances"]
        | None
    ) = None,
    strict:  | None = None,
    ref:  | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None,
    frozen:  | None = None,
    slots:  | None = None,
    config: CoreConfig[](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.CoreConfig) | None = None
) -> DataclassSchema

```

Returns a schema for a dataclass. As with `ModelSchema`, this schema can only be used as a field within another schema, not as the root type.
Parameters:
Name | Type | Description | Default
---|---|---|---
`cls` |  |  The dataclass type, used to perform subclass checks |  _required_
`schema` |  `CoreSchema` |  The schema to use for the dataclass fields |  _required_
`fields` |  |  Fields of the dataclass, this is used in serialization and in validation during re-validation and while validating assignment |  _required_
`generic_origin` |  |  The origin type used for this dataclass, if it's a parametrized generic. Ex, if this model schema represents `SomeDataclass[int]`, generic_origin is `SomeDataclass` |  `None`
`cls_name` |  |  The name to use in error locs, etc; this is useful for generics (default: `cls.__name__`) |  `None`
`post_init` |  |  Whether to call `__post_init__` after validation |  `None`
`revalidate_instances` |  |  whether instances of models and dataclasses (including subclass instances) should re-validate defaults to config.revalidate_instances, else 'never' |  `None`
`strict` |  |  Whether to require an exact instance of `cls` |  `None`
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`
`frozen` |  |  Whether the dataclass is frozen |  `None`
`slots` |  |  Whether `slots=True` on the dataclass, means each field is assigned independently, rather than simply setting `__dict__`, default false |  `None`
Source code in `pydantic_core/core_schema.py`
```
3433
3434
3435
3436
3437
3438
3439
3440
3441
3442
3443
3444
3445
3446
3447
3448
3449
3450
3451
3452
3453
3454
3455
3456
3457
3458
3459
3460
3461
3462
3463
3464
3465
3466
3467
3468
3469
3470
3471
3472
3473
3474
3475
3476
3477
3478
3479
3480
3481
3482
3483
3484
3485
3486
3487
3488
3489
```
| ```
def dataclass_schema(
    cls: type[Any],
    schema: CoreSchema,
    fields: list[str],
    *,
    generic_origin: type[Any] | None = None,
    cls_name: str | None = None,
    post_init: bool | None = None,
    revalidate_instances: Literal['always', 'never', 'subclass-instances'] | None = None,
    strict: bool | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
    frozen: bool | None = None,
    slots: bool | None = None,
    config: CoreConfig | None = None,
) -> DataclassSchema:
    """
    Returns a schema for a dataclass. As with `ModelSchema`, this schema can only be used as a field within
    another schema, not as the root type.

    Args:
        cls: The dataclass type, used to perform subclass checks
        schema: The schema to use for the dataclass fields
        fields: Fields of the dataclass, this is used in serialization and in validation during re-validation
            and while validating assignment
        generic_origin: The origin type used for this dataclass, if it's a parametrized generic. Ex,
            if this model schema represents `SomeDataclass[int]`, generic_origin is `SomeDataclass`
        cls_name: The name to use in error locs, etc; this is useful for generics (default: `cls.__name__`)
        post_init: Whether to call `__post_init__` after validation
        revalidate_instances: whether instances of models and dataclasses (including subclass instances)
            should re-validate defaults to config.revalidate_instances, else 'never'
        strict: Whether to require an exact instance of `cls`
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
        frozen: Whether the dataclass is frozen
        slots: Whether `slots=True` on the dataclass, means each field is assigned independently, rather than
            simply setting `__dict__`, default false
    """
    return _dict_not_none(
        type='dataclass',
        cls=cls,
        generic_origin=generic_origin,
        fields=fields,
        cls_name=cls_name,
        schema=schema,
        post_init=post_init,
        revalidate_instances=revalidate_instances,
        strict=strict,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
        frozen=frozen,
        slots=slots,
        config=config,
    )

```

---|---
