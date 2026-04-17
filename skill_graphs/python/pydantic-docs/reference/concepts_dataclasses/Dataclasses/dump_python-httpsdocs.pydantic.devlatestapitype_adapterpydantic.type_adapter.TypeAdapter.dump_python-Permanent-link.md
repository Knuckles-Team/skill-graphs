##  dump_python [¶](https://docs.pydantic.dev/latest/api/type_adapter/#pydantic.type_adapter.TypeAdapter.dump_python "Permanent link")
```
dump_python(
    instance: T,
    /,
    *,
    mode: ["json", "python"] = "python",
    include: IncEx | None = None,
    exclude: IncEx | None = None,
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
    serialize_as_any:  = False,
    context:  | None = None,
) ->

```

Dump an instance of the adapted type to a Python object.
Parameters:
Name | Type | Description | Default
---|---|---|---
`instance` |  `T` |  The Python object to serialize. |  _required_
`mode` |  |  The output format. |  `'python'`
`include` |  `IncEx | None` |  Fields to include in the output. |  `None`
`exclude` |  `IncEx | None` |  Fields to exclude from the output. |  `None`
`by_alias` |  |  Whether to use alias names for field names. |  `None`
`exclude_unset` |  |  Whether to exclude unset fields. |  `False`
`exclude_defaults` |  |  Whether to exclude fields with default values. |  `False`
`exclude_none` |  |  Whether to exclude fields with None values. |  `False`
`exclude_computed_fields` |  |  Whether to exclude computed fields. While this can be useful for round-tripping, it is usually recommended to use the dedicated `round_trip` parameter instead. |  `False`
`round_trip` |  |  Whether to output the serialized data in a way that is compatible with deserialization. |  `False`
`warnings` |  |  How to handle serialization errors. False/"none" ignores them, True/"warn" logs errors, "error" raises a [`PydanticSerializationError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.PydanticSerializationError). |  `True`
`fallback` |  |  A function to call when an unknown value is encountered. If not provided, a [`PydanticSerializationError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.PydanticSerializationError) error is raised. |  `None`
`serialize_as_any` |  |  Whether to serialize fields with duck-typing serialization behavior. |  `False`
`context` |  |  Additional context to pass to the serializer. |  `None`
Returns:
Type | Description
---|---
|  The serialized object.
Source code in `pydantic/type_adapter.py`
```
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
584
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
611
612
613
614
615
616
617
618
619
620
```
| ```
def dump_python(
    self,
    instance: T,
    /,
    *,
    mode: Literal['json', 'python'] = 'python',
    include: IncEx | None = None,
    exclude: IncEx | None = None,
    by_alias: bool | None = None,
    exclude_unset: bool = False,
    exclude_defaults: bool = False,
    exclude_none: bool = False,
    exclude_computed_fields: bool = False,
    round_trip: bool = False,
    warnings: bool | Literal['none', 'warn', 'error'] = True,
    fallback: Callable[[Any], Any] | None = None,
    serialize_as_any: bool = False,
    context: Any | None = None,
) -> Any:
    """Dump an instance of the adapted type to a Python object.

    Args:
        instance: The Python object to serialize.
        mode: The output format.
        include: Fields to include in the output.
        exclude: Fields to exclude from the output.
        by_alias: Whether to use alias names for field names.
        exclude_unset: Whether to exclude unset fields.
        exclude_defaults: Whether to exclude fields with default values.
        exclude_none: Whether to exclude fields with None values.
        exclude_computed_fields: Whether to exclude computed fields.
            While this can be useful for round-tripping, it is usually recommended to use the dedicated
            `round_trip` parameter instead.
        round_trip: Whether to output the serialized data in a way that is compatible with deserialization.
        warnings: How to handle serialization errors. False/"none" ignores them, True/"warn" logs errors,
            "error" raises a [`PydanticSerializationError`][pydantic_core.PydanticSerializationError].
        fallback: A function to call when an unknown value is encountered. If not provided,
            a [`PydanticSerializationError`][pydantic_core.PydanticSerializationError] error is raised.
        serialize_as_any: Whether to serialize fields with duck-typing serialization behavior.
        context: Additional context to pass to the serializer.

    Returns:
        The serialized object.
    """
    return self.serializer.to_python(
        instance,
        mode=mode,
        by_alias=by_alias,
        include=include,
        exclude=exclude,
        exclude_unset=exclude_unset,
        exclude_defaults=exclude_defaults,
        exclude_none=exclude_none,
        exclude_computed_fields=exclude_computed_fields,
        round_trip=round_trip,
        warnings=warnings,
        fallback=fallback,
        serialize_as_any=serialize_as_any,
        context=context,
    )

```

---|---
##  dump_json [¶](https://docs.pydantic.dev/latest/api/type_adapter/#pydantic.type_adapter.TypeAdapter.dump_json "Permanent link")
```
dump_json(
    instance: T,
    /,
    *,
    indent:  | None = None,
    ensure_ascii:  = False,
    include: IncEx | None = None,
    exclude: IncEx | None = None,
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
    serialize_as_any:  = False,
    context:  | None = None,
) ->

```

Usage Documentation
[JSON Serialization](https://docs.pydantic.dev/latest/concepts/json/#json-serialization)
Serialize an instance of the adapted type to JSON.
Parameters:
Name | Type | Description | Default
---|---|---|---
`instance` |  `T` |  The instance to be serialized. |  _required_
`indent` |  |  Number of spaces for JSON indentation. |  `None`
`ensure_ascii` |  |  If `True`, the output is guaranteed to have all incoming non-ASCII characters escaped. If `False` (the default), these characters will be output as-is. |  `False`
`include` |  `IncEx | None` |  Fields to include. |  `None`
`exclude` |  `IncEx | None` |  Fields to exclude. |  `None`
`by_alias` |  |  Whether to use alias names for field names. |  `None`
`exclude_unset` |  |  Whether to exclude unset fields. |  `False`
`exclude_defaults` |  |  Whether to exclude fields with default values. |  `False`
`exclude_none` |  |  Whether to exclude fields with a value of `None`. |  `False`
`exclude_computed_fields` |  |  Whether to exclude computed fields. While this can be useful for round-tripping, it is usually recommended to use the dedicated `round_trip` parameter instead. |  `False`
`round_trip` |  |  Whether to serialize and deserialize the instance to ensure round-tripping. |  `False`
`warnings` |  |  How to handle serialization errors. False/"none" ignores them, True/"warn" logs errors, "error" raises a [`PydanticSerializationError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.PydanticSerializationError). |  `True`
`fallback` |  |  A function to call when an unknown value is encountered. If not provided, a [`PydanticSerializationError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.PydanticSerializationError) error is raised. |  `None`
`serialize_as_any` |  |  Whether to serialize fields with duck-typing serialization behavior. |  `False`
`context` |  |  Additional context to pass to the serializer. |  `None`
Returns:
Type | Description
---|---
|  The JSON representation of the given instance as bytes.
Source code in `pydantic/type_adapter.py`
```
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
676
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
```
| ```
def dump_json(
    self,
    instance: T,
    /,
    *,
    indent: int | None = None,
    ensure_ascii: bool = False,
    include: IncEx | None = None,
    exclude: IncEx | None = None,
    by_alias: bool | None = None,
    exclude_unset: bool = False,
    exclude_defaults: bool = False,
    exclude_none: bool = False,
    exclude_computed_fields: bool = False,
    round_trip: bool = False,
    warnings: bool | Literal['none', 'warn', 'error'] = True,
    fallback: Callable[[Any], Any] | None = None,
    serialize_as_any: bool = False,
    context: Any | None = None,
) -> bytes:
    """!!! abstract "Usage Documentation"
        [JSON Serialization](../concepts/json.md#json-serialization)

    Serialize an instance of the adapted type to JSON.

    Args:
        instance: The instance to be serialized.
        indent: Number of spaces for JSON indentation.
        ensure_ascii: If `True`, the output is guaranteed to have all incoming non-ASCII characters escaped.
            If `False` (the default), these characters will be output as-is.
        include: Fields to include.
        exclude: Fields to exclude.
        by_alias: Whether to use alias names for field names.
        exclude_unset: Whether to exclude unset fields.
        exclude_defaults: Whether to exclude fields with default values.
        exclude_none: Whether to exclude fields with a value of `None`.
        exclude_computed_fields: Whether to exclude computed fields.
            While this can be useful for round-tripping, it is usually recommended to use the dedicated
            `round_trip` parameter instead.
        round_trip: Whether to serialize and deserialize the instance to ensure round-tripping.
        warnings: How to handle serialization errors. False/"none" ignores them, True/"warn" logs errors,
            "error" raises a [`PydanticSerializationError`][pydantic_core.PydanticSerializationError].
        fallback: A function to call when an unknown value is encountered. If not provided,
            a [`PydanticSerializationError`][pydantic_core.PydanticSerializationError] error is raised.
        serialize_as_any: Whether to serialize fields with duck-typing serialization behavior.
        context: Additional context to pass to the serializer.

    Returns:
        The JSON representation of the given instance as bytes.
    """
    return self.serializer.to_json(
        instance,
        indent=indent,
        ensure_ascii=ensure_ascii,
        include=include,
        exclude=exclude,
        by_alias=by_alias,
        exclude_unset=exclude_unset,
        exclude_defaults=exclude_defaults,
        exclude_none=exclude_none,
        exclude_computed_fields=exclude_computed_fields,
        round_trip=round_trip,
        warnings=warnings,
        fallback=fallback,
        serialize_as_any=serialize_as_any,
        context=context,
    )

```

---|---
