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
```
| ```
def model_dump(
    self,
    *,
    mode: Literal['json', 'python'] | str = 'python',
    include: IncEx | None = None,
    exclude: IncEx | None = None,
    context: Any | None = None,
    by_alias: bool | None = None,
    exclude_unset: bool = False,
    exclude_defaults: bool = False,
    exclude_none: bool = False,
    exclude_computed_fields: bool = False,
    round_trip: bool = False,
    warnings: bool | Literal['none', 'warn', 'error'] = True,
    fallback: Callable[[Any], Any] | None = None,
    serialize_as_any: bool = False,
) -> dict[str, Any]:
    """!!! abstract "Usage Documentation"
        [`model_dump`](../concepts/serialization.md#python-mode)

    Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

    Args:
        mode: The mode in which `to_python` should run.
            If mode is 'json', the output will only contain JSON serializable types.
            If mode is 'python', the output may contain non-JSON-serializable Python objects.
        include: A set of fields to include in the output.
        exclude: A set of fields to exclude from the output.
        context: Additional context to pass to the serializer.
        by_alias: Whether to use the field's alias in the dictionary key if defined.
        exclude_unset: Whether to exclude fields that have not been explicitly set.
        exclude_defaults: Whether to exclude fields that are set to their default value.
        exclude_none: Whether to exclude fields that have a value of `None`.
        exclude_computed_fields: Whether to exclude computed fields.
            While this can be useful for round-tripping, it is usually recommended to use the dedicated
            `round_trip` parameter instead.
        round_trip: If True, dumped values should be valid as input for non-idempotent types such as Json[T].
        warnings: How to handle serialization errors. False/"none" ignores them, True/"warn" logs errors,
            "error" raises a [`PydanticSerializationError`][pydantic_core.PydanticSerializationError].
        fallback: A function to call when an unknown value is encountered. If not provided,
            a [`PydanticSerializationError`][pydantic_core.PydanticSerializationError] error is raised.
        serialize_as_any: Whether to serialize fields with duck-typing serialization behavior.

    Returns:
        A dictionary representation of the model.
    """
    return self.__pydantic_serializer__.to_python(
        self,
        mode=mode,
        by_alias=by_alias,
        include=include,
        exclude=exclude,
        context=context,
        exclude_unset=exclude_unset,
        exclude_defaults=exclude_defaults,
        exclude_none=exclude_none,
        exclude_computed_fields=exclude_computed_fields,
        round_trip=round_trip,
        warnings=warnings,
        fallback=fallback,
        serialize_as_any=serialize_as_any,
    )

```

---|---
###  model_dump_json [¶](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_dump_json "Permanent link")
```
model_dump_json(
    *,
    indent:  | None = None,
    ensure_ascii:  = False,
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
) ->

```

Usage Documentation
[`model_dump_json`](https://docs.pydantic.dev/latest/concepts/serialization/#json-mode)
Generates a JSON representation of the model using Pydantic's `to_json` method.
Parameters:
Name | Type | Description | Default
---|---|---|---
`indent` |  |  Indentation to use in the JSON output. If None is passed, the output will be compact. |  `None`
`ensure_ascii` |  |  If `True`, the output is guaranteed to have all incoming non-ASCII characters escaped. If `False` (the default), these characters will be output as-is. |  `False`
`include` |  `IncEx | None` |  Field(s) to include in the JSON output. |  `None`
`exclude` |  `IncEx | None` |  Field(s) to exclude from the JSON output. |  `None`
`context` |  |  Additional context to pass to the serializer. |  `None`
`by_alias` |  |  Whether to serialize using field aliases. |  `None`
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
|  A JSON string representation of the model.
Source code in `pydantic/main.py`
```
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
501
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
```
| ```
def model_dump_json(
    self,
    *,
    indent: int | None = None,
    ensure_ascii: bool = False,
    include: IncEx | None = None,
    exclude: IncEx | None = None,
    context: Any | None = None,
    by_alias: bool | None = None,
    exclude_unset: bool = False,
    exclude_defaults: bool = False,
    exclude_none: bool = False,
    exclude_computed_fields: bool = False,
    round_trip: bool = False,
    warnings: bool | Literal['none', 'warn', 'error'] = True,
    fallback: Callable[[Any], Any] | None = None,
    serialize_as_any: bool = False,
) -> str:
    """!!! abstract "Usage Documentation"
        [`model_dump_json`](../concepts/serialization.md#json-mode)

    Generates a JSON representation of the model using Pydantic's `to_json` method.

    Args:
        indent: Indentation to use in the JSON output. If None is passed, the output will be compact.
        ensure_ascii: If `True`, the output is guaranteed to have all incoming non-ASCII characters escaped.
            If `False` (the default), these characters will be output as-is.
        include: Field(s) to include in the JSON output.
        exclude: Field(s) to exclude from the JSON output.
        context: Additional context to pass to the serializer.
        by_alias: Whether to serialize using field aliases.
        exclude_unset: Whether to exclude fields that have not been explicitly set.
        exclude_defaults: Whether to exclude fields that are set to their default value.
        exclude_none: Whether to exclude fields that have a value of `None`.
        exclude_computed_fields: Whether to exclude computed fields.
            While this can be useful for round-tripping, it is usually recommended to use the dedicated
            `round_trip` parameter instead.
        round_trip: If True, dumped values should be valid as input for non-idempotent types such as Json[T].
        warnings: How to handle serialization errors. False/"none" ignores them, True/"warn" logs errors,
            "error" raises a [`PydanticSerializationError`][pydantic_core.PydanticSerializationError].
        fallback: A function to call when an unknown value is encountered. If not provided,
            a [`PydanticSerializationError`][pydantic_core.PydanticSerializationError] error is raised.
        serialize_as_any: Whether to serialize fields with duck-typing serialization behavior.

    Returns:
        A JSON string representation of the model.
    """
    return self.__pydantic_serializer__.to_json(
        self,
        indent=indent,
        ensure_ascii=ensure_ascii,
        include=include,
        exclude=exclude,
        context=context,
        by_alias=by_alias,
        exclude_unset=exclude_unset,
        exclude_defaults=exclude_defaults,
        exclude_none=exclude_none,
        exclude_computed_fields=exclude_computed_fields,
        round_trip=round_trip,
        warnings=warnings,
        fallback=fallback,
        serialize_as_any=serialize_as_any,
    ).decode()

```

---|---
###  model_json_schema `classmethod` [¶](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_json_schema "Permanent link")
```
model_json_schema(
    by_alias:  = True,
    ref_template:  = DEFAULT_REF_TEMPLATE[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.DEFAULT_REF_TEMPLATE "pydantic.json_schema.DEFAULT_REF_TEMPLATE"),
    schema_generator: [
        GenerateJsonSchema[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema "pydantic.json_schema.GenerateJsonSchema")
    ] = GenerateJsonSchema[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema "pydantic.json_schema.GenerateJsonSchema"),
    mode: JsonSchemaMode[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaMode "pydantic.json_schema.JsonSchemaMode") = "validation",
    *,
    union_format: [
        "any_of", "primitive_type_array"
    ] = "any_of"
) -> dict[, ]

```

Generates a JSON schema for a model class.
Parameters:
Name | Type | Description | Default
---|---|---|---
`by_alias` |  |  Whether to use attribute aliases or not. |  `True`
`ref_template` |  |  The reference template. |  `DEFAULT_REF_TEMPLATE[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.DEFAULT_REF_TEMPLATE "pydantic.json_schema.DEFAULT_REF_TEMPLATE")`
`union_format` |  |  The format to use when combining schemas from unions together. Can be one of:
  * `'any_of'`: Use the
  * `'primitive_type_array'`: Use the `string`, `boolean`, `null`, `integer` or `number`) or contains constraints/metadata, falls back to `any_of`.

|  `'any_of'`
`schema_generator` |  `GenerateJsonSchema[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema "pydantic.json_schema.GenerateJsonSchema")]` |  To override the logic used to generate the JSON schema, as a subclass of `GenerateJsonSchema` with your desired modifications |  `GenerateJsonSchema[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema "pydantic.json_schema.GenerateJsonSchema")`
`mode` |  `JsonSchemaMode[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaMode "pydantic.json_schema.JsonSchemaMode")` |  The mode in which to generate the schema. |  `'validation'`
Returns:
Type | Description
---|---
`dict[` |  The JSON schema for the given model class.
Source code in `pydantic/main.py`
```
546
547
548
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
560
561
562
563
564
565
566
567
568
569
570
571
572
573
574
575
576
577
578
579
580
581
582
583
```
| ```
@classmethod
def model_json_schema(
    cls,
    by_alias: bool = True,
    ref_template: str = DEFAULT_REF_TEMPLATE,
    schema_generator: type[GenerateJsonSchema] = GenerateJsonSchema,
    mode: JsonSchemaMode = 'validation',
    *,
    union_format: Literal['any_of', 'primitive_type_array'] = 'any_of',
) -> dict[str, Any]:
    """Generates a JSON schema for a model class.

    Args:
        by_alias: Whether to use attribute aliases or not.
        ref_template: The reference template.
        union_format: The format to use when combining schemas from unions together. Can be one of:

            - `'any_of'`: Use the [`anyOf`](https://json-schema.org/understanding-json-schema/reference/combining#anyOf)
            keyword to combine schemas (the default).
            - `'primitive_type_array'`: Use the [`type`](https://json-schema.org/understanding-json-schema/reference/type)
            keyword as an array of strings, containing each type of the combination. If any of the schemas is not a primitive
            type (`string`, `boolean`, `null`, `integer` or `number`) or contains constraints/metadata, falls back to
            `any_of`.
        schema_generator: To override the logic used to generate the JSON schema, as a subclass of
            `GenerateJsonSchema` with your desired modifications
        mode: The mode in which to generate the schema.

    Returns:
        The JSON schema for the given model class.
    """
    return model_json_schema(
        cls,
        by_alias=by_alias,
        ref_template=ref_template,
        union_format=union_format,
        schema_generator=schema_generator,
        mode=mode,
    )

```

---|---
###  model_parametrized_name `classmethod` [¶](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_parametrized_name "Permanent link")
```
model_parametrized_name(
    params: [[], ...]
) ->

```

Compute the class name for parametrizations of generic classes.
This method can be overridden to achieve a custom naming scheme for generic BaseModels.
Parameters:
Name | Type | Description | Default
---|---|---|---
`params` |  |  Tuple of types of the class. Given a generic class `Model` with 2 type variables and a concrete model `Model[str, int]`, the value `(str, int)` would be passed to `params`. |  _required_
Returns:
Type | Description
---|---
|  String representing the new class where `params` are passed to `cls` as type variables.
Raises:
Type | Description
---|---
|  Raised when trying to generate concrete names for non-generic models.
Source code in `pydantic/main.py`
```
585
586
587
588
589
590
591
592
593
594
595
596
597
598
599
600
601
602
603
604
605
606
607
608
609
610
```
| ```
@classmethod
def model_parametrized_name(cls, params: tuple[type[Any], ...]) -> str:
    """Compute the class name for parametrizations of generic classes.

    This method can be overridden to achieve a custom naming scheme for generic BaseModels.

    Args:
        params: Tuple of types of the class. Given a generic class
            `Model` with 2 type variables and a concrete model `Model[str, int]`,
            the value `(str, int)` would be passed to `params`.

    Returns:
        String representing the new class where `params` are passed to `cls` as type variables.

    Raises:
        TypeError: Raised when trying to generate concrete names for non-generic models.
    """
    if not issubclass(cls, Generic):
        raise TypeError('Concrete names should only be generated for generic models.')

    # Any strings received should represent forward references, so we handle them specially below.
    # If we eventually move toward wrapping them in a ForwardRef in __class_getitem__ in the future,
    # we may be able to remove this special case.
    param_names = [param if isinstance(param, str) else _repr.display_as_type(param) for param in params]
    params_component = ', '.join(param_names)
    return f'{cls.__name__}[{params_component}]'

```

---|---
###  model_post_init [¶](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_post_init "Permanent link")
```
model_post_init(context: ) -> None

```

Override this method to perform additional initialization after `__init__` and `model_construct`. This is useful if you want to do some validation that requires the entire model to be initialized.
Source code in `pydantic/main.py`
```
612
613
614
615
```
| ```
def model_post_init(self, context: Any, /) -> None:
    """Override this method to perform additional initialization after `__init__` and `model_construct`.
    This is useful if you want to do some validation that requires the entire model to be initialized.
    """

```

---|---
###  model_rebuild `classmethod` [¶](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_rebuild "Permanent link")
```
model_rebuild(
    *,
    force:  = False,
    raise_errors:  = True,
    _parent_namespace_depth:  = 2,
    _types_namespace: MappingNamespace | None = None
) ->  | None

```

Try to rebuild the pydantic-core schema for the model.
This may be necessary when one of the annotations is a ForwardRef which could not be resolved during the initial attempt to build the schema, and automatic rebuilding fails.
Parameters:
Name | Type | Description | Default
---|---|---|---
`force` |  |  Whether to force the rebuilding of the model schema, defaults to `False`. |  `False`
`raise_errors` |  |  Whether to raise errors, defaults to `True`. |  `True`
`_parent_namespace_depth` |  |  The depth level of the parent namespace, defaults to 2. |  `2`
`_types_namespace` |  `MappingNamespace | None` |  The types namespace, defaults to `None`. |  `None`
Returns:
Type | Description
---|---
|  Returns `None` if the schema is already "complete" and rebuilding was not required.
|  If rebuilding _was_ required, returns `True` if rebuilding was successful, otherwise `False`.
Source code in `pydantic/main.py`
```
617
618
619
620
621
622
623
624
625
626
627
628
629
630
631
632
633
634
635
636
637
638
639
640
641
642
643
644
645
646
647
648
649
650
651
652
653
654
655
656
657
658
659
660
661
662
663
664
665
666
667
668
669
670
671
672
673
674
675
```
| ```
@classmethod
def model_rebuild(
    cls,
    *,
    force: bool = False,
    raise_errors: bool = True,
    _parent_namespace_depth: int = 2,
    _types_namespace: MappingNamespace | None = None,
) -> bool | None:
    """Try to rebuild the pydantic-core schema for the model.

    This may be necessary when one of the annotations is a ForwardRef which could not be resolved during
    the initial attempt to build the schema, and automatic rebuilding fails.

    Args:
        force: Whether to force the rebuilding of the model schema, defaults to `False`.
        raise_errors: Whether to raise errors, defaults to `True`.
        _parent_namespace_depth: The depth level of the parent namespace, defaults to 2.
        _types_namespace: The types namespace, defaults to `None`.

    Returns:
        Returns `None` if the schema is already "complete" and rebuilding was not required.
        If rebuilding _was_ required, returns `True` if rebuilding was successful, otherwise `False`.
    """
    already_complete = cls.__pydantic_complete__
    if already_complete and not force:
        return None

    cls.__pydantic_complete__ = False

    for attr in ('__pydantic_core_schema__', '__pydantic_validator__', '__pydantic_serializer__'):
        if attr in cls.__dict__ and not isinstance(getattr(cls, attr), _mock_val_ser.MockValSer):
            # Deleting the validator/serializer is necessary as otherwise they can get reused in
            # pydantic-core. We do so only if they aren't mock instances, otherwise — as `model_rebuild()`
            # isn't thread-safe — concurrent model instantiations can lead to the parent validator being used.
            # Same applies for the core schema that can be reused in schema generation.
            delattr(cls, attr)

    if _types_namespace is not None:
        rebuild_ns = _types_namespace
    elif _parent_namespace_depth > 0:
        rebuild_ns = _typing_extra.parent_frame_namespace(parent_depth=_parent_namespace_depth, force=True) or {}
    else:
        rebuild_ns = {}

    parent_ns = _model_construction.unpack_lenient_weakvaluedict(cls.__pydantic_parent_namespace__) or {}

    ns_resolver = _namespace_utils.NsResolver(
        parent_namespace={**rebuild_ns, **parent_ns},
    )

    return _model_construction.complete_model_class(
        cls,
        _config.ConfigWrapper(cls.model_config, check=False),
        ns_resolver,
        raise_errors=raise_errors,
        # If the model was already complete, we don't need to call the hook again.
        call_on_complete_hook=not already_complete,
    )

```

---|---
###  model_validate `classmethod` [¶](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_validate "Permanent link")
```
model_validate(
    obj: ,
    *,
    strict:  | None = None,
    extra: ExtraValues[](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ExtraValues "pydantic.config.ExtraValues") | None = None,
    from_attributes:  | None = None,
    context:  | None = None,
    by_alias:  | None = None,
    by_name:  | None = None
) ->

```

Validate a pydantic model instance.
Parameters:
Name | Type | Description | Default
---|---|---|---
`obj` |  |  The object to validate. |  _required_
`strict` |  |  Whether to enforce types strictly. |  `None`
`extra` |  `ExtraValues[](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ExtraValues "pydantic.config.ExtraValues") | None` |  Whether to ignore, allow, or forbid extra data during model validation. See the [`extra` configuration value](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict.extra) for details. |  `None`
`from_attributes` |  |  Whether to extract data from object attributes. |  `None`
`context` |  |  Additional context to pass to the validator. |  `None`
`by_alias` |  |  Whether to use the field's alias when validating against the provided input data. |  `None`
`by_name` |  |  Whether to use the field's name when validating against the provided input data. |  `None`
Raises:
Type | Description
---|---
`ValidationError[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError "pydantic_core.ValidationError")` |  If the object could not be validated.
Returns:
Type | Description
---|---
|  The validated model instance.
Source code in `pydantic/main.py`
```
677
678
679
680
681
682
683
684
685
686
687
688
689
690
691
692
693
694
695
696
697
698
699
700
701
702
703
704
705
706
707
708
709
710
711
712
713
714
715
716
717
718
719
720
721
722
723
724
```
| ```
@classmethod
def model_validate(
    cls,
    obj: Any,
    *,
    strict: bool | None = None,
    extra: ExtraValues | None = None,
    from_attributes: bool | None = None,
    context: Any | None = None,
    by_alias: bool | None = None,
    by_name: bool | None = None,
) -> Self:
    """Validate a pydantic model instance.

    Args:
        obj: The object to validate.
        strict: Whether to enforce types strictly.
        extra: Whether to ignore, allow, or forbid extra data during model validation.
            See the [`extra` configuration value][pydantic.ConfigDict.extra] for details.
        from_attributes: Whether to extract data from object attributes.
        context: Additional context to pass to the validator.
        by_alias: Whether to use the field's alias when validating against the provided input data.
        by_name: Whether to use the field's name when validating against the provided input data.

    Raises:
        ValidationError: If the object could not be validated.

    Returns:
        The validated model instance.
    """
    # `__tracebackhide__` tells pytest and some other tools to omit this function from tracebacks
    __tracebackhide__ = True

    if by_alias is False and by_name is not True:
        raise PydanticUserError(
            'At least one of `by_alias` or `by_name` must be set to True.',
            code='validate-by-alias-and-name-false',
        )

    return cls.__pydantic_validator__.validate_python(
        obj,
        strict=strict,
        extra=extra,
        from_attributes=from_attributes,
        context=context,
        by_alias=by_alias,
        by_name=by_name,
    )

```

---|---
###  model_validate_json `classmethod` [¶](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_validate_json "Permanent link")
```
model_validate_json(
    json_data:  |  | ,
    *,
    strict:  | None = None,
    extra: ExtraValues[](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ExtraValues "pydantic.config.ExtraValues") | None = None,
    context:  | None = None,
    by_alias:  | None = None,
    by_name:  | None = None
) ->

```

Usage Documentation
[JSON Parsing](https://docs.pydantic.dev/latest/concepts/json/#json-parsing)
Validate the given JSON data against the Pydantic model.
Parameters:
Name | Type | Description | Default
---|---|---|---
`json_data` |  |  The JSON data to validate. |  _required_
`strict` |  |  Whether to enforce types strictly. |  `None`
`extra` |  `ExtraValues[](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ExtraValues "pydantic.config.ExtraValues") | None` |  Whether to ignore, allow, or forbid extra data during model validation. See the [`extra` configuration value](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict.extra) for details. |  `None`
`context` |  |  Extra variables to pass to the validator. |  `None`
`by_alias` |  |  Whether to use the field's alias when validating against the provided input data. |  `None`
