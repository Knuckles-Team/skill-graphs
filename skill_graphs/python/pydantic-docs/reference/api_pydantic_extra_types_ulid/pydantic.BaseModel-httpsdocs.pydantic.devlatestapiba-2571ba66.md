        "`model_config['from_attributes']=True` and use `model_validate` instead.",
        category=None,
    )
    def from_orm(cls, obj: Any) -> Self:  # noqa: D102
        warnings.warn(
            'The `from_orm` method is deprecated; set '
            "`model_config['from_attributes']=True` and use `model_validate` instead.",
            category=PydanticDeprecatedSince20,
            stacklevel=2,
        )
        if not cls.model_config.get('from_attributes', None):
            raise PydanticUserError(
                'You must set the config attribute `from_attributes=True` to use from_orm', code=None
            )
        return cls.model_validate(obj)

    @classmethod
    @typing_extensions.deprecated('The `construct` method is deprecated; use `model_construct` instead.', category=None)
    def construct(cls, _fields_set: set[str] | None = None, **values: Any) -> Self:  # noqa: D102
        warnings.warn(
            'The `construct` method is deprecated; use `model_construct` instead.',
            category=PydanticDeprecatedSince20,
            stacklevel=2,
        )
        return cls.model_construct(_fields_set=_fields_set, **values)

    @typing_extensions.deprecated(
        'The `copy` method is deprecated; use `model_copy` instead. '
        'See the docstring of `BaseModel.copy` for details about how to handle `include` and `exclude`.',
        category=None,
    )
    def copy(
        self,
        *,
        include: AbstractSetIntStr | MappingIntStrAny | None = None,
        exclude: AbstractSetIntStr | MappingIntStrAny | None = None,
        update: Dict[str, Any] | None = None,  # noqa UP006
        deep: bool = False,
    ) -> Self:  # pragma: no cover
        """Returns a copy of the model.

        !!! warning "Deprecated"
            This method is now deprecated; use `model_copy` instead.

        If you need `include` or `exclude`, use:

    ```python {test="skip" lint="skip"}
        data = self.model_dump(include=include, exclude=exclude, round_trip=True)
        data = {**data, **(update or {})}
        copied = self.model_validate(data)
    ```

        Args:
            include: Optional set or mapping specifying which fields to include in the copied model.
            exclude: Optional set or mapping specifying which fields to exclude in the copied model.
            update: Optional dictionary of field-value pairs to override field values in the copied model.
            deep: If True, the values of fields that are Pydantic models will be deep-copied.

        Returns:
            A copy of the model with included, excluded and updated fields as specified.
        """
        warnings.warn(
            'The `copy` method is deprecated; use `model_copy` instead. '
            'See the docstring of `BaseModel.copy` for details about how to handle `include` and `exclude`.',
            category=PydanticDeprecatedSince20,
            stacklevel=2,
        )
        from .deprecated import copy_internals

        values = dict(
            copy_internals._iter(
                self, to_dict=False, by_alias=False, include=include, exclude=exclude, exclude_unset=False
            ),
            **(update or {}),
        )
        if self.__pydantic_private__ is None:
            private = None
        else:
            private = {k: v for k, v in self.__pydantic_private__.items() if v is not PydanticUndefined}

        if self.__pydantic_extra__ is None:
            extra: dict[str, Any] | None = None
        else:
            extra = self.__pydantic_extra__.copy()
            for k in list(self.__pydantic_extra__):
                if k not in values:  # k was in the exclude
                    extra.pop(k)
            for k in list(values):
                if k in self.__pydantic_extra__:  # k must have come from extra
                    extra[k] = values.pop(k)

        # new `__pydantic_fields_set__` can have unset optional fields with a set value in `update` kwarg
        if update:
            fields_set = self.__pydantic_fields_set__ | update.keys()
        else:
            fields_set = set(self.__pydantic_fields_set__)

        # removing excluded fields from `__pydantic_fields_set__`
        if exclude:
            fields_set -= set(exclude)

        return copy_internals._copy_and_set_values(self, values, fields_set, extra, private, deep=deep)

    @classmethod
    @typing_extensions.deprecated('The `schema` method is deprecated; use `model_json_schema` instead.', category=None)
    def schema(  # noqa: D102
        cls, by_alias: bool = True, ref_template: str = DEFAULT_REF_TEMPLATE
    ) -> Dict[str, Any]:  # noqa UP006
        warnings.warn(
            'The `schema` method is deprecated; use `model_json_schema` instead.',
            category=PydanticDeprecatedSince20,
            stacklevel=2,
        )
        return cls.model_json_schema(by_alias=by_alias, ref_template=ref_template)

    @classmethod
    @typing_extensions.deprecated(
        'The `schema_json` method is deprecated; use `model_json_schema` and json.dumps instead.',
        category=None,
    )
    def schema_json(  # noqa: D102
        cls, *, by_alias: bool = True, ref_template: str = DEFAULT_REF_TEMPLATE, **dumps_kwargs: Any
    ) -> str:  # pragma: no cover
        warnings.warn(
            'The `schema_json` method is deprecated; use `model_json_schema` and json.dumps instead.',
            category=PydanticDeprecatedSince20,
            stacklevel=2,
        )
        import json

        from .deprecated.json import pydantic_encoder

        return json.dumps(
            cls.model_json_schema(by_alias=by_alias, ref_template=ref_template),
            default=pydantic_encoder,
            **dumps_kwargs,
        )

    @classmethod
    @typing_extensions.deprecated('The `validate` method is deprecated; use `model_validate` instead.', category=None)
    def validate(cls, value: Any) -> Self:  # noqa: D102
        warnings.warn(
            'The `validate` method is deprecated; use `model_validate` instead.',
            category=PydanticDeprecatedSince20,
            stacklevel=2,
        )
        return cls.model_validate(value)

    @classmethod
    @typing_extensions.deprecated(
        'The `update_forward_refs` method is deprecated; use `model_rebuild` instead.',
        category=None,
    )
    def update_forward_refs(cls, **localns: Any) -> None:  # noqa: D102
        warnings.warn(
            'The `update_forward_refs` method is deprecated; use `model_rebuild` instead.',
            category=PydanticDeprecatedSince20,
            stacklevel=2,
        )
        if localns:  # pragma: no cover
            raise TypeError('`localns` arguments are not longer accepted.')
        cls.model_rebuild(force=True)

    @typing_extensions.deprecated(
        'The private method `_iter` will be removed and should no longer be used.', category=None
    )
    def _iter(self, *args: Any, **kwargs: Any) -> Any:
        warnings.warn(
            'The private method `_iter` will be removed and should no longer be used.',
            category=PydanticDeprecatedSince20,
            stacklevel=2,
        )
        from .deprecated import copy_internals

        return copy_internals._iter(self, *args, **kwargs)

    @typing_extensions.deprecated(
        'The private method `_copy_and_set_values` will be removed and should no longer be used.',
        category=None,
    )
    def _copy_and_set_values(self, *args: Any, **kwargs: Any) -> Any:
        warnings.warn(
            'The private method `_copy_and_set_values` will be removed and should no longer be used.',
            category=PydanticDeprecatedSince20,
            stacklevel=2,
        )
        from .deprecated import copy_internals

        return copy_internals._copy_and_set_values(self, *args, **kwargs)

    @classmethod
    @typing_extensions.deprecated(
        'The private method `_get_value` will be removed and should no longer be used.',
        category=None,
    )
    def _get_value(cls, *args: Any, **kwargs: Any) -> Any:
        warnings.warn(
            'The private method `_get_value` will be removed and should no longer be used.',
            category=PydanticDeprecatedSince20,
            stacklevel=2,
        )
        from .deprecated import copy_internals

        return copy_internals._get_value(cls, *args, **kwargs)

    @typing_extensions.deprecated(
        'The private method `_calculate_keys` will be removed and should no longer be used.',
        category=None,
    )
    def _calculate_keys(self, *args: Any, **kwargs: Any) -> Any:
        warnings.warn(
            'The private method `_calculate_keys` will be removed and should no longer be used.',
            category=PydanticDeprecatedSince20,
            stacklevel=2,
        )
        from .deprecated import copy_internals

        return copy_internals._calculate_keys(self, *args, **kwargs)

```

---|---
###  __init__ [¶](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.__init__ "Permanent link")
```
__init__(**data: ) -> None

```

Raises [`ValidationError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError) if the input data cannot be validated to form a valid model.
`self` is explicitly positional-only to allow `self` as a field name.
Source code in `pydantic/main.py`
```
240
241
242
243
244
245
246
247
248
249
250
251
252
253
254
255
256
257
```
| ```
def __init__(self, /, **data: Any) -> None:
    """Create a new model by parsing and validating input data from keyword arguments.

    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.

    `self` is explicitly positional-only to allow `self` as a field name.
    """
    # `__tracebackhide__` tells pytest and some other tools to omit this function from tracebacks
    __tracebackhide__ = True
    validated_self = self.__pydantic_validator__.validate_python(data, self_instance=self)
    if self is not validated_self:
        warnings.warn(
            'A custom validator is returning a value other than `self`.\n'
            "Returning anything other than `self` from a top level model validator isn't supported when validating via `__init__`.\n"
            'See the `model_validator` docs (https://docs.pydantic.dev/latest/concepts/validators/#model-validators) for more details.',
            stacklevel=2,
        )

```

---|---
###  model_config `class-attribute` [¶](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_config "Permanent link")
```
model_config: ConfigDict[](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict "pydantic.config.ConfigDict") = ConfigDict[](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict "pydantic.config.ConfigDict")()

```

Configuration for the model, should be a dictionary conforming to [`ConfigDict`](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict).
###  model_fields `classmethod` [¶](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_fields "Permanent link")
```
model_fields() -> dict[, FieldInfo[](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.FieldInfo "pydantic.fields.FieldInfo")]

```

A mapping of field names to their respective [`FieldInfo`](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.FieldInfo) instances.
Warning
Accessing this attribute from a model instance is deprecated, and will not work in Pydantic V3. Instead, you should access this attribute from the model class.
Source code in `pydantic/main.py`
```
262
263
264
265
266
267
268
269
270
271
```
| ```
@_utils.deprecated_instance_property
@classmethod
def model_fields(cls) -> dict[str, FieldInfo]:
    """A mapping of field names to their respective [`FieldInfo`][pydantic.fields.FieldInfo] instances.

    !!! warning
        Accessing this attribute from a model instance is deprecated, and will not work in Pydantic V3.
        Instead, you should access this attribute from the model class.
    """
    return getattr(cls, '__pydantic_fields__', {})

```

---|---
###  model_computed_fields `classmethod` [¶](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_computed_fields "Permanent link")
```
model_computed_fields() -> dict[, ComputedFieldInfo[](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.ComputedFieldInfo "pydantic.fields.ComputedFieldInfo")]

```

A mapping of computed field names to their respective [`ComputedFieldInfo`](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.ComputedFieldInfo) instances.
Warning
Accessing this attribute from a model instance is deprecated, and will not work in Pydantic V3. Instead, you should access this attribute from the model class.
Source code in `pydantic/main.py`
```
273
274
275
276
277
278
279
280
281
282
```
| ```
@_utils.deprecated_instance_property
@classmethod
def model_computed_fields(cls) -> dict[str, ComputedFieldInfo]:
    """A mapping of computed field names to their respective [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] instances.

    !!! warning
        Accessing this attribute from a model instance is deprecated, and will not work in Pydantic V3.
        Instead, you should access this attribute from the model class.
    """
    return getattr(cls, '__pydantic_computed_fields__', {})

```

---|---
###  __pydantic_core_schema__ `class-attribute` [¶](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.__pydantic_core_schema__ "Permanent link")
```
__pydantic_core_schema__: CoreSchema

```

The core schema of the model.
###  model_extra `property` [¶](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_extra "Permanent link")
```
model_extra: dict[, ] | None

```

Get extra fields set during validation.
Returns:
Type | Description
---|---
`dict[` |  A dictionary of extra fields, or `None` if `config.extra` is not set to `"allow"`.
###  model_fields_set `property` [¶](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_fields_set "Permanent link")
```
model_fields_set: []

```

Returns the set of fields that have been explicitly set on this model instance.
Returns:
Type | Description
---|---
|  A set of strings representing the fields that have been set, i.e. that were not filled from defaults.
###  model_construct `classmethod` [¶](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_construct "Permanent link")
```
model_construct(
    _fields_set: [] | None = None, **values:
) ->

```

Creates a new instance of the `Model` class with validated data.
Creates a new model setting `__dict__` and `__pydantic_fields_set__` from trusted or pre-validated data. Default values are respected, but no other validation is performed.
Note
`model_construct()` generally respects the `model_config.extra` setting on the provided model. That is, if `model_config.extra == 'allow'`, then all extra passed values are added to the model instance's `__dict__` and `__pydantic_extra__` fields. If `model_config.extra == 'ignore'` (the default), then all extra passed values are ignored. Because no validation is performed with a call to `model_construct()`, having `model_config.extra == 'forbid'` does not result in an error if extra values are passed, but they will be ignored.
Parameters:
Name | Type | Description | Default
---|---|---|---
`_fields_set` |  |  A set of field names that were originally explicitly set during instantiation. If provided, this is directly used for the [`model_fields_set`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_fields_set) attribute. Otherwise, the field names from the `values` argument will be used. |  `None`
`values` |  |  Trusted or pre-validated data dictionary. |  `{}`
Returns:
Type | Description
---|---
|  A new instance of the `Model` class with validated data.
Source code in `pydantic/main.py`
```
303
304
305
306
307
308
309
310
311
312
313
314
315
316
317
318
319
320
321
322
323
324
325
326
327
328
329
330
331
332
333
334
335
336
337
338
339
340
341
342
343
344
345
346
347
348
349
350
351
352
353
354
355
356
357
358
359
360
361
362
363
364
365
366
367
368
369
370
371
372
373
374
375
376
377
378
379
380
381
382
```
| ```
@classmethod
def model_construct(cls, _fields_set: set[str] | None = None, **values: Any) -> Self:  # noqa: C901
    """Creates a new instance of the `Model` class with validated data.

    Creates a new model setting `__dict__` and `__pydantic_fields_set__` from trusted or pre-validated data.
    Default values are respected, but no other validation is performed.

    !!! note
        `model_construct()` generally respects the `model_config.extra` setting on the provided model.
        That is, if `model_config.extra == 'allow'`, then all extra passed values are added to the model instance's `__dict__`
        and `__pydantic_extra__` fields. If `model_config.extra == 'ignore'` (the default), then all extra passed values are ignored.
        Because no validation is performed with a call to `model_construct()`, having `model_config.extra == 'forbid'` does not result in
        an error if extra values are passed, but they will be ignored.

    Args:
        _fields_set: A set of field names that were originally explicitly set during instantiation. If provided,
            this is directly used for the [`model_fields_set`][pydantic.BaseModel.model_fields_set] attribute.
            Otherwise, the field names from the `values` argument will be used.
        values: Trusted or pre-validated data dictionary.

    Returns:
        A new instance of the `Model` class with validated data.
    """
    m = cls.__new__(cls)
    fields_values: dict[str, Any] = {}
    fields_set = set()

    for name, field in cls.__pydantic_fields__.items():
        if field.alias is not None and field.alias in values:
            fields_values[name] = values.pop(field.alias)
            fields_set.add(name)

        if (name not in fields_set) and (field.validation_alias is not None):
            validation_aliases: list[str | AliasPath] = (
                field.validation_alias.choices
                if isinstance(field.validation_alias, AliasChoices)
                else [field.validation_alias]
            )

            for alias in validation_aliases:
                if isinstance(alias, str) and alias in values:
                    fields_values[name] = values.pop(alias)
                    fields_set.add(name)
                    break
                elif isinstance(alias, AliasPath):
                    value = alias.search_dict_for_path(values)
                    if value is not PydanticUndefined:
                        fields_values[name] = value
                        fields_set.add(name)
                        break

        if name not in fields_set:
            if name in values:
                fields_values[name] = values.pop(name)
                fields_set.add(name)
            elif not field.is_required():
                fields_values[name] = field.get_default(call_default_factory=True, validated_data=fields_values)
    if _fields_set is None:
        _fields_set = fields_set

    _extra: dict[str, Any] | None = values if cls.model_config.get('extra') == 'allow' else None
    _object_setattr(m, '__dict__', fields_values)
    _object_setattr(m, '__pydantic_fields_set__', _fields_set)
    if not cls.__pydantic_root_model__:
        _object_setattr(m, '__pydantic_extra__', _extra)

    if cls.__pydantic_post_init__:
        m.model_post_init(None)
        # update private attributes with values set
        if hasattr(m, '__pydantic_private__') and m.__pydantic_private__ is not None:
            for k, v in values.items():
                if k in m.__private_attributes__:
                    m.__pydantic_private__[k] = v

    elif not cls.__pydantic_root_model__:
        # Note: if there are any private attributes, cls.__pydantic_post_init__ would exist
        # Since it doesn't, that means that `__pydantic_private__` should be set to None
        _object_setattr(m, '__pydantic_private__', None)

    return m

```

---|---
###  model_copy [¶](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_copy "Permanent link")
```
model_copy(
    *,
    update: [, ] | None = None,
    deep:  = False
) ->

```

Usage Documentation
[`model_copy`](https://docs.pydantic.dev/latest/concepts/models/#model-copy)
Returns a copy of the model.
Note
The underlying instance's
Parameters:
Name | Type | Description | Default
---|---|---|---
`update` |  |  Values to change/add in the new model. Note: the data is not validated before creating the new model. You should trust this data. |  `None`
`deep` |  |  Set to `True` to make a deep copy of the model. |  `False`
Returns:
Type | Description
---|---
|  New model instance.
Source code in `pydantic/main.py`
```
384
385
386
387
388
389
390
391
392
393
394
395
396
397
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
```
| ```
def model_copy(self, *, update: Mapping[str, Any] | None = None, deep: bool = False) -> Self:
    """!!! abstract "Usage Documentation"
        [`model_copy`](../concepts/models.md#model-copy)

    Returns a copy of the model.

    !!! note
        The underlying instance's [`__dict__`][object.__dict__] attribute is copied. This
        might have unexpected side effects if you store anything in it, on top of the model
        fields (e.g. the value of [cached properties][functools.cached_property]).

    Args:
        update: Values to change/add in the new model. Note: the data is not validated
            before creating the new model. You should trust this data.
        deep: Set to `True` to make a deep copy of the model.

    Returns:
        New model instance.
    """
    copied = self.__deepcopy__() if deep else self.__copy__()
    if update:
        if self.model_config.get('extra') == 'allow':
            for k, v in update.items():
                if k in self.__pydantic_fields__:
                    copied.__dict__[k] = v
                else:
                    if copied.__pydantic_extra__ is None:
                        copied.__pydantic_extra__ = {}
                    copied.__pydantic_extra__[k] = v
        else:
            copied.__dict__.update(update)
        copied.__pydantic_fields_set__.update(update.keys())
    return copied

```

---|---
###  model_dump [¶](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_dump "Permanent link")
```
model_dump(
    *,
    mode: ["json", "python"] |  = "python",
    include: IncEx | None = None,
    exclude: IncEx | None = None,
    context:  | None = None,
    by_alias:  | None = None,
    exclude_unset:  = False,
    exclude_defaults:  = False,
    exclude_none:  = False,
    exclude_computed_fields:  = False,
    round_trip:  = False,
    warnings: (
         | ["none", "warn", "error"]
    ) = True,
    fallback: [[], ] | None = None,
    serialize_as_any:  = False
) -> dict[, ]

```

Usage Documentation
[`model_dump`](https://docs.pydantic.dev/latest/concepts/serialization/#python-mode)
Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.
Parameters:
Name | Type | Description | Default
---|---|---|---
`mode` |  |  The mode in which `to_python` should run. If mode is 'json', the output will only contain JSON serializable types. If mode is 'python', the output may contain non-JSON-serializable Python objects. |  `'python'`
`include` |  `IncEx | None` |  A set of fields to include in the output. |  `None`
`exclude` |  `IncEx | None` |  A set of fields to exclude from the output. |  `None`
`context` |  |  Additional context to pass to the serializer. |  `None`
`by_alias` |  |  Whether to use the field's alias in the dictionary key if defined. |  `None`
`exclude_unset` |  |  Whether to exclude fields that have not been explicitly set. |  `False`
`exclude_defaults` |  |  Whether to exclude fields that are set to their default value. |  `False`
`exclude_none` |  |  Whether to exclude fields that have a value of `None`. |  `False`
`exclude_computed_fields` |  |  Whether to exclude computed fields. While this can be useful for round-tripping, it is usually recommended to use the dedicated `round_trip` parameter instead. |  `False`
`round_trip` |  |  If True, dumped values should be valid as input for non-idempotent types such as Json[T]. |  `False`
`warnings` |  |  How to handle serialization errors. False/"none" ignores them, True/"warn" logs errors, "error" raises a [`PydanticSerializationError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.PydanticSerializationError). |  `True`
`fallback` |  |  A function to call when an unknown value is encountered. If not provided, a [`PydanticSerializationError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.PydanticSerializationError) error is raised. |  `None`
`serialize_as_any` |  |  Whether to serialize fields with duck-typing serialization behavior. |  `False`
Returns:
Type | Description
---|---
`dict[` |  A dictionary representation of the model.
Source code in `pydantic/main.py`
```
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
451
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
