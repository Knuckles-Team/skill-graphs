
    Validate the given JSON data against the Pydantic model.

    Args:
        json_data: The JSON data to validate.
        strict: Whether to enforce types strictly.
        extra: Whether to ignore, allow, or forbid extra data during model validation.
            See the [`extra` configuration value][pydantic.ConfigDict.extra] for details.
        context: Extra variables to pass to the validator.
        by_alias: Whether to use the field's alias when validating against the provided input data.
        by_name: Whether to use the field's name when validating against the provided input data.

    Returns:
        The validated Pydantic model.

    Raises:
        ValidationError: If `json_data` is not a JSON string or the object could not be validated.
    """
    # `__tracebackhide__` tells pytest and some other tools to omit this function from tracebacks
    __tracebackhide__ = True

    if by_alias is False and by_name is not True:
        raise PydanticUserError(
            'At least one of `by_alias` or `by_name` must be set to True.',
            code='validate-by-alias-and-name-false',
        )

    return cls.__pydantic_validator__.validate_json(
        json_data, strict=strict, extra=extra, context=context, by_alias=by_alias, by_name=by_name
    )

```

---|---
###  model_validate_strings `classmethod` [¶](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_validate_strings)
```
model_validate_strings(
    obj: ,
    *,
    strict:  | None = None,
    extra: ExtraValues[](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ExtraValues) | None = None,
    context:  | None = None,
    by_alias:  | None = None,
    by_name:  | None = None
) ->

```

Validate the given object with string data against the Pydantic model.
Parameters:
Name | Type | Description | Default
---|---|---|---
`obj` |  |  The object containing string data to validate. |  _required_
`strict` |  |  Whether to enforce types strictly. |  `None`
`extra` |  `ExtraValues[](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ExtraValues) | None` |  Whether to ignore, allow, or forbid extra data during model validation. See the [`extra` configuration value](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict.extra) for details. |  `None`
`context` |  |  Extra variables to pass to the validator. |  `None`
`by_alias` |  |  Whether to use the field's alias when validating against the provided input data. |  `None`
`by_name` |  |  Whether to use the field's name when validating against the provided input data. |  `None`
Returns:
Type | Description
---|---
|  The validated Pydantic model.
Source code in `pydantic/main.py`
```
770
771
772
773
774
775
776
777
778
779
780
781
782
783
784
785
786
787
788
789
790
791
792
793
794
795
796
797
798
799
800
801
802
803
804
805
806
```
| ```
@classmethod
def model_validate_strings(
    cls,
    obj: Any,
    *,
    strict: bool | None = None,
    extra: ExtraValues | None = None,
    context: Any | None = None,
    by_alias: bool | None = None,
    by_name: bool | None = None,
) -> Self:
    """Validate the given object with string data against the Pydantic model.

    Args:
        obj: The object containing string data to validate.
        strict: Whether to enforce types strictly.
        extra: Whether to ignore, allow, or forbid extra data during model validation.
            See the [`extra` configuration value][pydantic.ConfigDict.extra] for details.
        context: Extra variables to pass to the validator.
        by_alias: Whether to use the field's alias when validating against the provided input data.
        by_name: Whether to use the field's name when validating against the provided input data.

    Returns:
        The validated Pydantic model.
    """
    # `__tracebackhide__` tells pytest and some other tools to omit this function from tracebacks
    __tracebackhide__ = True

    if by_alias is False and by_name is not True:
        raise PydanticUserError(
            'At least one of `by_alias` or `by_name` must be set to True.',
            code='validate-by-alias-and-name-false',
        )

    return cls.__pydantic_validator__.validate_strings(
        obj, strict=strict, extra=extra, context=context, by_alias=by_alias, by_name=by_name
    )

```

---|---
##  pydantic.create_model [¶](https://docs.pydantic.dev/latest/api/base_model/#pydantic.create_model)
```
create_model(
    model_name: ,
    /,
    *,
    __config__: ConfigDict[](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict) | None = None,
    __doc__:  | None = None,
    __base__: None = None,
    __module__:  = __name__,
    __validators__: (
        [, [..., ]] | None
    ) = None,
    __cls_kwargs__: [, ] | None = None,
    __qualname__:  | None = None,
    **field_definitions:  | [, ],
) -> [BaseModel[](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel)]

```

```
create_model(
    model_name: ,
    /,
    *,
    __config__: ConfigDict[](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict) | None = None,
    __doc__:  | None = None,
    __base__: [ModelT] | [[ModelT], ...],
    __module__:  = __name__,
    __validators__: (
        [, [..., ]] | None
    ) = None,
    __cls_kwargs__: [, ] | None = None,
    __qualname__:  | None = None,
    **field_definitions:  | [, ],
) -> [ModelT]

```

```
create_model(
    model_name: ,
    /,
    *,
    __config__: ConfigDict[](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict) | None = None,
    __doc__:  | None = None,
    __base__: (
        [ModelT] | [[ModelT], ...] | None
    ) = None,
    __module__:  | None = None,
    __validators__: (
        [, [..., ]] | None
    ) = None,
    __cls_kwargs__: [, ] | None = None,
    __qualname__:  | None = None,
    **field_definitions:  | [, ],
) -> [ModelT]

```

Usage Documentation
[Dynamic Model Creation](https://docs.pydantic.dev/latest/concepts/models/#dynamic-model-creation)
Dynamically creates and returns a new Pydantic model, in other words, `create_model` dynamically creates a subclass of [`BaseModel`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel).
Warning
This function may execute arbitrary code contained in field annotations, if string references need to be evaluated.
See
Parameters:
Name | Type | Description | Default
---|---|---|---
`model_name` |  |  The name of the newly created model. |  _required_
`__config__` |  `ConfigDict[](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict) | None` |  The configuration of the new model. |  `None`
`__doc__` |  |  The docstring of the new model. |  `None`
`__base__` |  `ModelT] | ModelT], ...] | None` |  The base class or classes for the new model. |  `None`
`__module__` |  |  The name of the module that the model belongs to; if `None`, the value is taken from `sys._getframe(1)` |  `None`
`__validators__` |  |  A dictionary of methods that validate fields. The keys are the names of the validation methods to be added to the model, and the values are the validation methods themselves. You can read more about functional validators [here](https://docs.pydantic.dev/2.9/concepts/validators/#field-validators). |  `None`
`__cls_kwargs__` |  |  A dictionary of keyword arguments for class creation, such as `metaclass`. |  `None`
`__qualname__` |  |  The qualified name of the newly created model. |  `None`
`**field_definitions` |  |  Field definitions of the new model. Either:
  * a single element, representing the type annotation of the field.
  * a two-tuple, the first element being the type and the second element the assigned value (either a default or the [`Field()`](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field) function).

|  `{}`
Returns:
Type | Description
---|---
`ModelT]` |  The new [model](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel).
Raises:
Type | Description
---|---
`PydanticUserError[](https://docs.pydantic.dev/latest/api/errors/#pydantic.errors.PydanticUserError)` |  If `__base__` and `__config__` are both passed.
Source code in `pydantic/main.py`
```
1716
1717
1718
1719
1720
1721
1722
1723
1724
1725
1726
1727
1728
1729
1730
1731
1732
1733
1734
1735
1736
1737
1738
1739
1740
1741
1742
1743
1744
1745
1746
1747
1748
1749
1750
1751
1752
1753
1754
1755
1756
1757
1758
1759
1760
1761
1762
1763
1764
1765
1766
1767
1768
1769
1770
1771
1772
1773
1774
1775
1776
1777
1778
1779
1780
1781
1782
1783
1784
1785
1786
1787
1788
1789
1790
1791
1792
1793
1794
1795
1796
1797
1798
1799
1800
1801
1802
1803
1804
1805
1806
1807
1808
1809
1810
1811
1812
1813
1814
1815
1816
```
| ```
def create_model(  # noqa: C901
    model_name: str,
    /,
    *,
    __config__: ConfigDict | None = None,
    __doc__: str | None = None,
    __base__: type[ModelT] | tuple[type[ModelT], ...] | None = None,
    __module__: str | None = None,
    __validators__: dict[str, Callable[..., Any]] | None = None,
    __cls_kwargs__: dict[str, Any] | None = None,
    __qualname__: str | None = None,
    # TODO PEP 747: replace `Any` by the TypeForm:
    **field_definitions: Any | tuple[str, Any],
) -> type[ModelT]:
    """!!! abstract "Usage Documentation"
        [Dynamic Model Creation](../concepts/models.md#dynamic-model-creation)

    Dynamically creates and returns a new Pydantic model, in other words, `create_model` dynamically creates a
    subclass of [`BaseModel`][pydantic.BaseModel].

    !!! warning
        This function may execute arbitrary code contained in field annotations, if string references need to be evaluated.

        See [Security implications of introspecting annotations](https://docs.python.org/3/library/annotationlib.html#annotationlib-security) for more information.

    Args:
        model_name: The name of the newly created model.
        __config__: The configuration of the new model.
        __doc__: The docstring of the new model.
        __base__: The base class or classes for the new model.
        __module__: The name of the module that the model belongs to;
            if `None`, the value is taken from `sys._getframe(1)`
        __validators__: A dictionary of methods that validate fields. The keys are the names of the validation methods to
            be added to the model, and the values are the validation methods themselves. You can read more about functional
            validators [here](https://docs.pydantic.dev/2.9/concepts/validators/#field-validators).
        __cls_kwargs__: A dictionary of keyword arguments for class creation, such as `metaclass`.
        __qualname__: The qualified name of the newly created model.
        **field_definitions: Field definitions of the new model. Either:

            - a single element, representing the type annotation of the field.
            - a two-tuple, the first element being the type and the second element the assigned value
              (either a default or the [`Field()`][pydantic.Field] function).

    Returns:
        The new [model][pydantic.BaseModel].

    Raises:
        PydanticUserError: If `__base__` and `__config__` are both passed.
    """
    if __base__ is None:
        __base__ = (cast('type[ModelT]', BaseModel),)
    elif not isinstance(__base__, tuple):
        __base__ = (__base__,)

    __cls_kwargs__ = __cls_kwargs__ or {}

    fields: dict[str, Any] = {}
    annotations: dict[str, Any] = {}

    for f_name, f_def in field_definitions.items():
        if isinstance(f_def, tuple):
            if len(f_def) != 2:
                raise PydanticUserError(
                    f'Field definition for {f_name!r} should a single element representing the type or a two-tuple, the first element '
                    'being the type and the second element the assigned value (either a default or the `Field()` function).',
                    code='create-model-field-definitions',
                )

            annotations[f_name] = f_def[0]
            fields[f_name] = f_def[1]
        else:
            annotations[f_name] = f_def

    if __module__ is None:
        f = sys._getframe(1)
        __module__ = f.f_globals['__name__']

    namespace: dict[str, Any] = {'__annotations__': annotations, '__module__': __module__}
    if __doc__:
        namespace['__doc__'] = __doc__
    if __qualname__ is not None:
        namespace['__qualname__'] = __qualname__
    if __validators__:
        namespace.update(__validators__)
    namespace.update(fields)
    if __config__:
        namespace['model_config'] = __config__
    resolved_bases = types.resolve_bases(__base__)
    meta, ns, kwds = types.prepare_class(model_name, resolved_bases, kwds=__cls_kwargs__)
    if resolved_bases is not __base__:
        ns['__orig_bases__'] = __base__
    namespace.update(ns)

    return meta(
        model_name,
        resolved_bases,
        namespace,
        __pydantic_reset_parent_namespace__=False,
        _create_model_module=__module__,
        **kwds,
    )

```

---|---
Was this page helpful?
Thanks for your feedback!
Thanks for your feedback!
Made with
