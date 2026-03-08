##  validate_python [¶](https://docs.pydantic.dev/latest/api/type_adapter/#pydantic.type_adapter.TypeAdapter.validate_python "Permanent link")
```
validate_python(
    object: ,
    /,
    *,
    strict:  | None = None,
    extra: ExtraValues[](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ExtraValues "pydantic.config.ExtraValues") | None = None,
    from_attributes:  | None = None,
    context:  | None = None,
    experimental_allow_partial: (
         | ["off", "on", "trailing-strings"]
    ) = False,
    by_alias:  | None = None,
    by_name:  | None = None,
) -> T

```

Validate a Python object against the model.
Parameters:
Name | Type | Description | Default
---|---|---|---
`object` |  |  The Python object to validate against the model. |  _required_
`strict` |  |  Whether to strictly check types. |  `None`
`extra` |  `ExtraValues[](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ExtraValues "pydantic.config.ExtraValues") | None` |  Whether to ignore, allow, or forbid extra data during model validation. See the [`extra` configuration value](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict.extra) for details. |  `None`
`from_attributes` |  |  Whether to extract data from object attributes. |  `None`
`context` |  |  Additional context to pass to the validator. |  `None`
`experimental_allow_partial` |  |  **Experimental** whether to enable [partial validation](https://docs.pydantic.dev/latest/concepts/experimental/#partial-validation), e.g. to process streams. * False / 'off': Default behavior, no partial validation. * True / 'on': Enable partial validation. * 'trailing-strings': Enable partial validation and allow trailing strings in the input. |  `False`
`by_alias` |  |  Whether to use the field's alias when validating against the provided input data. |  `None`
`by_name` |  |  Whether to use the field's name when validating against the provided input data. |  `None`
Note
When using `TypeAdapter` with a Pydantic `dataclass`, the use of the `from_attributes` argument is not supported.
Returns:
Type | Description
---|---
`T` |  The validated object.
Source code in `pydantic/type_adapter.py`
```
398
399
400
401
402
403
404
405
406
407
408
409
410
411
412
413
414
415
416
417
418
419
420
421
422
423
424
425
426
427
428
429
430
431
432
433
434
435
436
437
438
439
440
441
442
443
444
445
446
447
448
449
450
```
| ```
def validate_python(
    self,
    object: Any,
    /,
    *,
    strict: bool | None = None,
    extra: ExtraValues | None = None,
    from_attributes: bool | None = None,
    context: Any | None = None,
    experimental_allow_partial: bool | Literal['off', 'on', 'trailing-strings'] = False,
    by_alias: bool | None = None,
    by_name: bool | None = None,
) -> T:
    """Validate a Python object against the model.

    Args:
        object: The Python object to validate against the model.
        strict: Whether to strictly check types.
        extra: Whether to ignore, allow, or forbid extra data during model validation.
            See the [`extra` configuration value][pydantic.ConfigDict.extra] for details.
        from_attributes: Whether to extract data from object attributes.
        context: Additional context to pass to the validator.
        experimental_allow_partial: **Experimental** whether to enable
            [partial validation](../concepts/experimental.md#partial-validation), e.g. to process streams.
            * False / 'off': Default behavior, no partial validation.
            * True / 'on': Enable partial validation.
            * 'trailing-strings': Enable partial validation and allow trailing strings in the input.
        by_alias: Whether to use the field's alias when validating against the provided input data.
        by_name: Whether to use the field's name when validating against the provided input data.

    !!! note
        When using `TypeAdapter` with a Pydantic `dataclass`, the use of the `from_attributes`
        argument is not supported.

    Returns:
        The validated object.
    """
    if by_alias is False and by_name is not True:
        raise PydanticUserError(
            'At least one of `by_alias` or `by_name` must be set to True.',
            code='validate-by-alias-and-name-false',
        )

    return self.validator.validate_python(
        object,
        strict=strict,
        extra=extra,
        from_attributes=from_attributes,
        context=context,
        allow_partial=experimental_allow_partial,
        by_alias=by_alias,
        by_name=by_name,
    )

```

---|---
##  validate_json [¶](https://docs.pydantic.dev/latest/api/type_adapter/#pydantic.type_adapter.TypeAdapter.validate_json "Permanent link")
```
validate_json(
    data:  |  | ,
    /,
    *,
    strict:  | None = None,
    extra: ExtraValues[](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ExtraValues "pydantic.config.ExtraValues") | None = None,
    context:  | None = None,
    experimental_allow_partial: (
         | ["off", "on", "trailing-strings"]
    ) = False,
    by_alias:  | None = None,
    by_name:  | None = None,
) -> T

```

Usage Documentation
[JSON Parsing](https://docs.pydantic.dev/latest/concepts/json/#json-parsing)
Validate a JSON string or bytes against the model.
Parameters:
Name | Type | Description | Default
---|---|---|---
`data` |  |  The JSON data to validate against the model. |  _required_
`strict` |  |  Whether to strictly check types. |  `None`
`extra` |  `ExtraValues[](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ExtraValues "pydantic.config.ExtraValues") | None` |  Whether to ignore, allow, or forbid extra data during model validation. See the [`extra` configuration value](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict.extra) for details. |  `None`
`context` |  |  Additional context to use during validation. |  `None`
`experimental_allow_partial` |  |  **Experimental** whether to enable [partial validation](https://docs.pydantic.dev/latest/concepts/experimental/#partial-validation), e.g. to process streams. * False / 'off': Default behavior, no partial validation. * True / 'on': Enable partial validation. * 'trailing-strings': Enable partial validation and allow trailing strings in the input. |  `False`
`by_alias` |  |  Whether to use the field's alias when validating against the provided input data. |  `None`
`by_name` |  |  Whether to use the field's name when validating against the provided input data. |  `None`
Returns:
Type | Description
---|---
`T` |  The validated object.
Source code in `pydantic/type_adapter.py`
```
452
453
454
455
456
457
458
459
460
461
462
463
464
465
466
467
468
469
470
471
472
473
474
475
476
477
478
479
480
481
482
483
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
496
497
498
499
500
```
| ```
def validate_json(
    self,
    data: str | bytes | bytearray,
    /,
    *,
    strict: bool | None = None,
    extra: ExtraValues | None = None,
    context: Any | None = None,
    experimental_allow_partial: bool | Literal['off', 'on', 'trailing-strings'] = False,
    by_alias: bool | None = None,
    by_name: bool | None = None,
) -> T:
    """!!! abstract "Usage Documentation"
        [JSON Parsing](../concepts/json.md#json-parsing)

    Validate a JSON string or bytes against the model.

    Args:
        data: The JSON data to validate against the model.
        strict: Whether to strictly check types.
        extra: Whether to ignore, allow, or forbid extra data during model validation.
            See the [`extra` configuration value][pydantic.ConfigDict.extra] for details.
        context: Additional context to use during validation.
        experimental_allow_partial: **Experimental** whether to enable
            [partial validation](../concepts/experimental.md#partial-validation), e.g. to process streams.
            * False / 'off': Default behavior, no partial validation.
            * True / 'on': Enable partial validation.
            * 'trailing-strings': Enable partial validation and allow trailing strings in the input.
        by_alias: Whether to use the field's alias when validating against the provided input data.
        by_name: Whether to use the field's name when validating against the provided input data.

    Returns:
        The validated object.
    """
    if by_alias is False and by_name is not True:
        raise PydanticUserError(
            'At least one of `by_alias` or `by_name` must be set to True.',
            code='validate-by-alias-and-name-false',
        )

    return self.validator.validate_json(
        data,
        strict=strict,
        extra=extra,
        context=context,
        allow_partial=experimental_allow_partial,
        by_alias=by_alias,
        by_name=by_name,
    )

```

---|---
