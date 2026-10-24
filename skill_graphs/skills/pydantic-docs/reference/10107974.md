##  validate_strings [¶](https://docs.pydantic.dev/latest/api/type_adapter/#pydantic.type_adapter.TypeAdapter.validate_strings "Permanent link")
```
validate_strings(
    obj: ,
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

Validate object contains string data against the model.
Parameters:
Name | Type | Description | Default
---|---|---|---
`obj` |  |  The object contains string data to validate. |  _required_
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
502
503
504
505
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
521
522
523
524
525
526
527
528
529
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
```
| ```
def validate_strings(
    self,
    obj: Any,
    /,
    *,
    strict: bool | None = None,
    extra: ExtraValues | None = None,
    context: Any | None = None,
    experimental_allow_partial: bool | Literal['off', 'on', 'trailing-strings'] = False,
    by_alias: bool | None = None,
    by_name: bool | None = None,
) -> T:
    """Validate object contains string data against the model.

    Args:
        obj: The object contains string data to validate.
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

    return self.validator.validate_strings(
        obj,
        strict=strict,
        extra=extra,
        context=context,
        allow_partial=experimental_allow_partial,
        by_alias=by_alias,
        by_name=by_name,
    )

```

---|---
##  get_default_value [¶](https://docs.pydantic.dev/latest/api/type_adapter/#pydantic.type_adapter.TypeAdapter.get_default_value "Permanent link")
```
get_default_value(
    *,
    strict:  | None = None,
    context:  | None = None
) -> Some[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.Some "pydantic_core.Some")[T] | None

```

Get the default value for the wrapped type.
Parameters:
Name | Type | Description | Default
---|---|---|---
`strict` |  |  Whether to strictly check types. |  `None`
`context` |  |  Additional context to pass to the validator. |  `None`
Returns:
Type | Description
---|---
`Some[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.Some "pydantic_core.Some")[T] | None` |  The default value wrapped in a `Some` if there is one or None if not.
Source code in `pydantic/type_adapter.py`
```
549
550
551
552
553
554
555
556
557
558
559
```
| ```
def get_default_value(self, *, strict: bool | None = None, context: Any | None = None) -> Some[T] | None:
    """Get the default value for the wrapped type.

    Args:
        strict: Whether to strictly check types.
        context: Additional context to pass to the validator.

    Returns:
        The default value wrapped in a `Some` if there is one or None if not.
    """
    return self.validator.get_default_value(strict=strict, context=context)

```

---|---
