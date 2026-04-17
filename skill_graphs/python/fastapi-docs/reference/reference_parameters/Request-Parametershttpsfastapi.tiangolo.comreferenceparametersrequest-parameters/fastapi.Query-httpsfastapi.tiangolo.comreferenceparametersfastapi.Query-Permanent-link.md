##  fastapi.Query [¶](https://fastapi.tiangolo.com/reference/parameters/#fastapi.Query "Permanent link")
```
Query(
    default=Undefined,
    *,
    default_factory=_Unset,
    alias=None,
    alias_priority=_Unset,
    validation_alias=None,
    serialization_alias=None,
    title=None,
    description=None,
    gt=None,
    ge=None,
    lt=None,
    le=None,
    min_length=None,
    max_length=None,
    pattern=None,
    regex=None,
    discriminator=None,
    strict=_Unset,
    multiple_of=_Unset,
    allow_inf_nan=_Unset,
    max_digits=_Unset,
    decimal_places=_Unset,
    examples=None,
    example=_Unset,
    openapi_examples=None,
    deprecated=None,
    include_in_schema=True,
    json_schema_extra=None,
    **extra
)

```

PARAMETER | DESCRIPTION
---|---
`default` |  Default value if the parameter field is not set. Read more about it in the [FastAPI docs about Query parameters](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#alternative-old-query-as-the-default-value) **TYPE:** `Any` **DEFAULT:** `Undefined`
`default_factory` |  A callable to generate the default value. This doesn't affect `Path` parameters as the value is always required. The parameter is available only for compatibility. **TYPE:** `Callable[[], Any] | None` **DEFAULT:** `_Unset`
`alias` |  An alternative name for the parameter field. This will be used to extract the data and for the generated OpenAPI. It is particularly useful when you can't use the name you want because it is a Python reserved keyword or similar. Read more about it in the [FastAPI docs about Query parameters](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#alias-parameters) **TYPE:** `str | None` **DEFAULT:** `None`
`alias_priority` |  Priority of the alias. This affects whether an alias generator is used. **TYPE:** `int | None` **DEFAULT:** `_Unset`
`validation_alias` |  'Whitelist' validation step. The parameter field will be the single one allowed by the alias or set of aliases defined. **TYPE:** `str | AliasPath | AliasChoices | None` **DEFAULT:** `None`
`serialization_alias` |  'Blacklist' validation step. The vanilla parameter field will be the single one of the alias' or set of aliases' fields and all the other fields will be ignored at serialization time. **TYPE:** `str | None` **DEFAULT:** `None`
`title` |  Human-readable title. Read more about it in the [FastAPI docs about Query parameters](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#declare-more-metadata) **TYPE:** `str | None` **DEFAULT:** `None`
`description` |  Human-readable description. Read more about it in the [FastAPI docs about Query parameters](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#declare-more-metadata) **TYPE:** `str | None` **DEFAULT:** `None`
`gt` |  Greater than. If set, value must be greater than this. Only applicable to numbers. Read more about it in the [FastAPI docs about Path parameters numeric validations](https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/#number-validations-greater-than-and-less-than-or-equal) **TYPE:** `float | None` **DEFAULT:** `None`
`ge` |  Greater than or equal. If set, value must be greater than or equal to this. Only applicable to numbers. Read more about it in the [FastAPI docs about Path parameters numeric validations](https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/#number-validations-greater-than-and-less-than-or-equal) **TYPE:** `float | None` **DEFAULT:** `None`
`lt` |  Less than. If set, value must be less than this. Only applicable to numbers. Read more about it in the [FastAPI docs about Path parameters numeric validations](https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/#number-validations-greater-than-and-less-than-or-equal) **TYPE:** `float | None` **DEFAULT:** `None`
`le` |  Less than or equal. If set, value must be less than or equal to this. Only applicable to numbers. Read more about it in the [FastAPI docs about Path parameters numeric validations](https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/#number-validations-greater-than-and-less-than-or-equal) **TYPE:** `float | None` **DEFAULT:** `None`
`min_length` |  Minimum length for strings. Read more about it in the [FastAPI docs about Query parameters](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/) **TYPE:** `int | None` **DEFAULT:** `None`
`max_length` |  Maximum length for strings. Read more about it in the [FastAPI docs about Query parameters](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/) **TYPE:** `int | None` **DEFAULT:** `None`
`pattern` |  RegEx pattern for strings. Read more about it in the [FastAPI docs about Query parameters](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#add-regular-expressions **TYPE:** `str | None` **DEFAULT:** `None`
`regex` |  Deprecated in FastAPI 0.100.0 and Pydantic v2, use `pattern` instead. RegEx pattern for strings. **TYPE:** `str | None` **DEFAULT:** `None`
`discriminator` |  Parameter field name for discriminating the type in a tagged union. **TYPE:** `str | None` **DEFAULT:** `None`
`strict` |  If `True`, strict validation is applied to the field. **TYPE:** `bool | None` **DEFAULT:** `_Unset`
`multiple_of` |  Value must be a multiple of this. Only applicable to numbers. **TYPE:** `float | None` **DEFAULT:** `_Unset`
`allow_inf_nan` |  Allow `inf`, `-inf`, `nan`. Only applicable to numbers. **TYPE:** `bool | None` **DEFAULT:** `_Unset`
`max_digits` |  Maximum number of digits allowed for decimal values. **TYPE:** `int | None` **DEFAULT:** `_Unset`
`decimal_places` |  Maximum number of decimal places allowed for decimal values. **TYPE:** `int | None` **DEFAULT:** `_Unset`
`examples` |  Example values for this field. Read more about it in the [FastAPI docs for Declare Request Example Data](https://fastapi.tiangolo.com/tutorial/schema-extra-example/) **TYPE:** `list[Any] | None` **DEFAULT:** `None`
`example` |  Deprecated in OpenAPI 3.1.0 that now uses JSON Schema 2020-12, although still supported. Use examples instead.  **TYPE:** `Any | None` **DEFAULT:** `_Unset`
`openapi_examples` |  OpenAPI-specific examples. It will be added to the generated OpenAPI (e.g. visible at `/docs`). Swagger UI (that provides the `/docs` interface) has better support for the OpenAPI-specific examples than the JSON Schema `examples`, that's the main use case for this. Read more about it in the [FastAPI docs for Declare Request Example Data](https://fastapi.tiangolo.com/tutorial/schema-extra-example/#using-the-openapi_examples-parameter). **TYPE:** `dict[str, Example[](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Example "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">Example</span> \(<code>fastapi.openapi.models.Example</code>\)")] | None` **DEFAULT:** `None`
`deprecated` |  Mark this parameter field as deprecated. It will affect the generated OpenAPI (e.g. visible at `/docs`). Read more about it in the [FastAPI docs about Query parameters](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#deprecating-parameters) **TYPE:** `deprecated | str | bool | None` **DEFAULT:** `None`
`include_in_schema` |  To include (or not) this parameter field in the generated OpenAPI. You probably don't need it, but it's available. This affects the generated OpenAPI (e.g. visible at `/docs`). Read more about it in the [FastAPI docs about Query parameters](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#exclude-parameters-from-openapi **TYPE:** `bool` **DEFAULT:** `True`
`json_schema_extra` |  Any additional JSON schema data. **TYPE:** `dict[str, Any] | None` **DEFAULT:** `None`
`**extra` |  The `extra` kwargs is deprecated. Use `json_schema_extra` instead. Include extra fields used by the JSON Schema. **TYPE:** `Any` **DEFAULT:** `{}`
Source code in `fastapi/param_functions.py`
```
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
383
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
545
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
```
| ```
def Query(  # noqa: N802
    default: Annotated[
        Any,
        Doc(
            """
            Default value if the parameter field is not set.

            Read more about it in the
            [FastAPI docs about Query parameters](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#alternative-old-query-as-the-default-value)
            """
        ),
    ] = Undefined,
    *,
    default_factory: Annotated[
        Callable[[], Any] | None,
        Doc(
            """
            A callable to generate the default value.

            This doesn't affect `Path` parameters as the value is always required.
            The parameter is available only for compatibility.
            """
        ),
    ] = _Unset,
    alias: Annotated[
        str | None,
        Doc(
            """
            An alternative name for the parameter field.

            This will be used to extract the data and for the generated OpenAPI.
            It is particularly useful when you can't use the name you want because it
            is a Python reserved keyword or similar.

            Read more about it in the
            [FastAPI docs about Query parameters](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#alias-parameters)
            """
        ),
    ] = None,
    alias_priority: Annotated[
        int | None,
        Doc(
            """
            Priority of the alias. This affects whether an alias generator is used.
            """
        ),
    ] = _Unset,
    validation_alias: Annotated[
        str | AliasPath | AliasChoices | None,
        Doc(
            """
            'Whitelist' validation step. The parameter field will be the single one
            allowed by the alias or set of aliases defined.
            """
        ),
    ] = None,
    serialization_alias: Annotated[
        str | None,
        Doc(
            """
            'Blacklist' validation step. The vanilla parameter field will be the
            single one of the alias' or set of aliases' fields and all the other
            fields will be ignored at serialization time.
            """
        ),
    ] = None,
    title: Annotated[
        str | None,
        Doc(
            """
            Human-readable title.

            Read more about it in the
            [FastAPI docs about Query parameters](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#declare-more-metadata)
            """
        ),
    ] = None,
    description: Annotated[
        str | None,
        Doc(
            """
            Human-readable description.

            Read more about it in the
            [FastAPI docs about Query parameters](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#declare-more-metadata)
            """
        ),
    ] = None,
    gt: Annotated[
        float | None,
        Doc(
            """
            Greater than. If set, value must be greater than this. Only applicable to
            numbers.

            Read more about it in the
            [FastAPI docs about Path parameters numeric validations](https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/#number-validations-greater-than-and-less-than-or-equal)
            """
        ),
    ] = None,
    ge: Annotated[
        float | None,
        Doc(
            """
            Greater than or equal. If set, value must be greater than or equal to
            this. Only applicable to numbers.

            Read more about it in the
            [FastAPI docs about Path parameters numeric validations](https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/#number-validations-greater-than-and-less-than-or-equal)
            """
        ),
    ] = None,
    lt: Annotated[
        float | None,
        Doc(
            """
            Less than. If set, value must be less than this. Only applicable to numbers.

            Read more about it in the
            [FastAPI docs about Path parameters numeric validations](https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/#number-validations-greater-than-and-less-than-or-equal)
            """
        ),
    ] = None,
    le: Annotated[
        float | None,
        Doc(
            """
            Less than or equal. If set, value must be less than or equal to this.
            Only applicable to numbers.

            Read more about it in the
            [FastAPI docs about Path parameters numeric validations](https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/#number-validations-greater-than-and-less-than-or-equal)
            """
        ),
    ] = None,
    min_length: Annotated[
        int | None,
        Doc(
            """
            Minimum length for strings.

            Read more about it in the
            [FastAPI docs about Query parameters](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/)
            """
        ),
    ] = None,
    max_length: Annotated[
        int | None,
        Doc(
            """
            Maximum length for strings.

            Read more about it in the
            [FastAPI docs about Query parameters](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/)
            """
        ),
    ] = None,
    pattern: Annotated[
        str | None,
        Doc(
            """
            RegEx pattern for strings.

            Read more about it in the
            [FastAPI docs about Query parameters](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#add-regular-expressions
            """
        ),
    ] = None,
    regex: Annotated[
        str | None,
        Doc(
            """
            RegEx pattern for strings.
            """
        ),
        deprecated(
            "Deprecated in FastAPI 0.100.0 and Pydantic v2, use `pattern` instead."
        ),
    ] = None,
    discriminator: Annotated[
        str | None,
        Doc(
            """
            Parameter field name for discriminating the type in a tagged union.
            """
        ),
    ] = None,
    strict: Annotated[
        bool | None,
        Doc(
            """
            If `True`, strict validation is applied to the field.
            """
        ),
    ] = _Unset,
    multiple_of: Annotated[
        float | None,
        Doc(
            """
            Value must be a multiple of this. Only applicable to numbers.
            """
        ),
    ] = _Unset,
    allow_inf_nan: Annotated[
        bool | None,
        Doc(
            """
            Allow `inf`, `-inf`, `nan`. Only applicable to numbers.
            """
        ),
    ] = _Unset,
    max_digits: Annotated[
        int | None,
        Doc(
            """
            Maximum number of digits allowed for decimal values.
            """
        ),
    ] = _Unset,
    decimal_places: Annotated[
        int | None,
        Doc(
            """
            Maximum number of decimal places allowed for decimal values.
            """
        ),
    ] = _Unset,
    examples: Annotated[
        list[Any] | None,
        Doc(
            """
            Example values for this field.

            Read more about it in the
            [FastAPI docs for Declare Request Example Data](https://fastapi.tiangolo.com/tutorial/schema-extra-example/)
            """
        ),
    ] = None,
    example: Annotated[
        Any | None,
        deprecated(
            "Deprecated in OpenAPI 3.1.0 that now uses JSON Schema 2020-12, "
            "although still supported. Use examples instead."
        ),
    ] = _Unset,
    openapi_examples: Annotated[
        dict[str, Example] | None,
        Doc(
            """
            OpenAPI-specific examples.

            It will be added to the generated OpenAPI (e.g. visible at `/docs`).

            Swagger UI (that provides the `/docs` interface) has better support for the
            OpenAPI-specific examples than the JSON Schema `examples`, that's the main
            use case for this.

            Read more about it in the
            [FastAPI docs for Declare Request Example Data](https://fastapi.tiangolo.com/tutorial/schema-extra-example/#using-the-openapi_examples-parameter).
            """
        ),
    ] = None,
    deprecated: Annotated[
        deprecated | str | bool | None,
        Doc(
            """
            Mark this parameter field as deprecated.

            It will affect the generated OpenAPI (e.g. visible at `/docs`).

            Read more about it in the
            [FastAPI docs about Query parameters](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#deprecating-parameters)
            """
        ),
    ] = None,
    include_in_schema: Annotated[
        bool,
        Doc(
            """
            To include (or not) this parameter field in the generated OpenAPI.
            You probably don't need it, but it's available.

            This affects the generated OpenAPI (e.g. visible at `/docs`).

            Read more about it in the
            [FastAPI docs about Query parameters](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#exclude-parameters-from-openapi
            """
        ),
    ] = True,
    json_schema_extra: Annotated[
        dict[str, Any] | None,
        Doc(
            """
            Any additional JSON schema data.
            """
        ),
    ] = None,
    **extra: Annotated[
        Any,
        Doc(
            """
            Include extra fields used by the JSON Schema.
            """
        ),
        deprecated(
            """
            The `extra` kwargs is deprecated. Use `json_schema_extra` instead.
            """
        ),
    ],
) -> Any:
    return params.Query(
        default=default,
        default_factory=default_factory,
        alias=alias,
        alias_priority=alias_priority,
        validation_alias=validation_alias,
        serialization_alias=serialization_alias,
        title=title,
        description=description,
        gt=gt,
        ge=ge,
        lt=lt,
        le=le,
        min_length=min_length,
        max_length=max_length,
        pattern=pattern,
        regex=regex,
        discriminator=discriminator,
        strict=strict,
        multiple_of=multiple_of,
        allow_inf_nan=allow_inf_nan,
        max_digits=max_digits,
        decimal_places=decimal_places,
        example=example,
        examples=examples,
        openapi_examples=openapi_examples,
        deprecated=deprecated,
        include_in_schema=include_in_schema,
        json_schema_extra=json_schema_extra,
        **extra,
    )

```

---|---
##  fastapi.Path [¶](https://fastapi.tiangolo.com/reference/parameters/#fastapi.Path "Permanent link")
```
Path(
    default=...,
    *,
    default_factory=_Unset,
    alias=None,
    alias_priority=_Unset,
    validation_alias=None,
    serialization_alias=None,
    title=None,
    description=None,
    gt=None,
    ge=None,
    lt=None,
    le=None,
    min_length=None,
    max_length=None,
    pattern=None,
    regex=None,
    discriminator=None,
    strict=_Unset,
    multiple_of=_Unset,
    allow_inf_nan=_Unset,
    max_digits=_Unset,
    decimal_places=_Unset,
    examples=None,
    example=_Unset,
    openapi_examples=None,
    deprecated=None,
    include_in_schema=True,
    json_schema_extra=None,
    **extra
)

```

Declare a path parameter for a _path operation_.
Read more about it in the [FastAPI docs for Path Parameters and Numeric Validations](https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/).
```
from typing import Annotated

from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get")],
):
    return {"item_id": item_id}

```

PARAMETER | DESCRIPTION
---|---
`default` |  Default value if the parameter field is not set. This doesn't affect `Path` parameters as the value is always required. The parameter is available only for compatibility. **TYPE:** `Any` **DEFAULT:** `...`
`default_factory` |  A callable to generate the default value. This doesn't affect `Path` parameters as the value is always required. The parameter is available only for compatibility. **TYPE:** `Callable[[], Any] | None` **DEFAULT:** `_Unset`
`alias` |  An alternative name for the parameter field. This will be used to extract the data and for the generated OpenAPI. It is particularly useful when you can't use the name you want because it is a Python reserved keyword or similar. **TYPE:** `str | None` **DEFAULT:** `None`
`alias_priority` |  Priority of the alias. This affects whether an alias generator is used. **TYPE:** `int | None` **DEFAULT:** `_Unset`
`validation_alias` |  'Whitelist' validation step. The parameter field will be the single one allowed by the alias or set of aliases defined. **TYPE:** `str | AliasPath | AliasChoices | None` **DEFAULT:** `None`
`serialization_alias` |  'Blacklist' validation step. The vanilla parameter field will be the single one of the alias' or set of aliases' fields and all the other fields will be ignored at serialization time. **TYPE:** `str | None` **DEFAULT:** `None`
`title` |  Human-readable title. Read more about it in the [FastAPI docs for Path Parameters and Numeric Validations](https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/#declare-metadata) **TYPE:** `str | None` **DEFAULT:** `None`
`description` |  Human-readable description. **TYPE:** `str | None` **DEFAULT:** `None`
`gt` |  Greater than. If set, value must be greater than this. Only applicable to numbers. Read more about it in the [FastAPI docs about Path parameters numeric validations](https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/#number-validations-greater-than-and-less-than-or-equal) **TYPE:** `float | None` **DEFAULT:** `None`
`ge` |  Greater than or equal. If set, value must be greater than or equal to this. Only applicable to numbers. Read more about it in the [FastAPI docs about Path parameters numeric validations](https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/#number-validations-greater-than-and-less-than-or-equal) **TYPE:** `float | None` **DEFAULT:** `None`
`lt` |  Less than. If set, value must be less than this. Only applicable to numbers. Read more about it in the [FastAPI docs about Path parameters numeric validations](https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/#number-validations-greater-than-and-less-than-or-equal) **TYPE:** `float | None` **DEFAULT:** `None`
`le` |  Less than or equal. If set, value must be less than or equal to this. Only applicable to numbers. Read more about it in the [FastAPI docs about Path parameters numeric validations](https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/#number-validations-greater-than-and-less-than-or-equal) **TYPE:** `float | None` **DEFAULT:** `None`
`min_length` |  Minimum length for strings. **TYPE:** `int | None` **DEFAULT:** `None`
`max_length` |  Maximum length for strings. **TYPE:** `int | None` **DEFAULT:** `None`
`pattern` |  RegEx pattern for strings. **TYPE:** `str | None` **DEFAULT:** `None`
`regex` |  Deprecated in FastAPI 0.100.0 and Pydantic v2, use `pattern` instead. RegEx pattern for strings. **TYPE:** `str | None` **DEFAULT:** `None`
`discriminator` |  Parameter field name for discriminating the type in a tagged union. **TYPE:** `str | None` **DEFAULT:** `None`
`strict` |  If `True`, strict validation is applied to the field. **TYPE:** `bool | None` **DEFAULT:** `_Unset`
`multiple_of` |  Value must be a multiple of this. Only applicable to numbers. **TYPE:** `float | None` **DEFAULT:** `_Unset`
`allow_inf_nan` |  Allow `inf`, `-inf`, `nan`. Only applicable to numbers. **TYPE:** `bool | None` **DEFAULT:** `_Unset`
`max_digits` |  Maximum number of digits allowed for decimal values. **TYPE:** `int | None` **DEFAULT:** `_Unset`
`decimal_places` |  Maximum number of decimal places allowed for decimal values. **TYPE:** `int | None` **DEFAULT:** `_Unset`
`examples` |  Example values for this field. Read more about it in the [FastAPI docs for Declare Request Example Data](https://fastapi.tiangolo.com/tutorial/schema-extra-example/) **TYPE:** `list[Any] | None` **DEFAULT:** `None`
`example` |  Deprecated in OpenAPI 3.1.0 that now uses JSON Schema 2020-12, although still supported. Use examples instead.  **TYPE:** `Any | None` **DEFAULT:** `_Unset`
`openapi_examples` |  OpenAPI-specific examples. It will be added to the generated OpenAPI (e.g. visible at `/docs`). Swagger UI (that provides the `/docs` interface) has better support for the OpenAPI-specific examples than the JSON Schema `examples`, that's the main use case for this. Read more about it in the [FastAPI docs for Declare Request Example Data](https://fastapi.tiangolo.com/tutorial/schema-extra-example/#using-the-openapi_examples-parameter). **TYPE:** `dict[str, Example[](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Example "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">Example</span> \(<code>fastapi.openapi.models.Example</code>\)")] | None` **DEFAULT:** `None`
`deprecated` |  Mark this parameter field as deprecated. It will affect the generated OpenAPI (e.g. visible at `/docs`). **TYPE:** `deprecated | str | bool | None` **DEFAULT:** `None`
`include_in_schema` |  To include (or not) this parameter field in the generated OpenAPI. You probably don't need it, but it's available. This affects the generated OpenAPI (e.g. visible at `/docs`). **TYPE:** `bool` **DEFAULT:** `True`
`json_schema_extra` |  Any additional JSON schema data. **TYPE:** `dict[str, Any] | None` **DEFAULT:** `None`
`**extra` |  The `extra` kwargs is deprecated. Use `json_schema_extra` instead. Include extra fields used by the JSON Schema. **TYPE:** `Any` **DEFAULT:** `{}`
Source code in `fastapi/param_functions.py`
```
 14
 15
 16
 17
 18
 19
 20
 21
 22
 23
 24
 25
 26
 27
 28
 29
 30
 31
 32
 33
 34
 35
 36
 37
 38
 39
 40
 41
 42
 43
 44
 45
 46
 47
 48
 49
 50
 51
 52
 53
 54
 55
 56
 57
 58
 59
 60
 61
 62
 63
 64
 65
 66
 67
 68
 69
 70
 71
 72
 73
 74
 75
 76
 77
 78
 79
 80
 81
 82
 83
 84
 85
 86
 87
 88
 89
 90
 91
 92
 93
 94
 95
 96
 97
 98
 99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
208
209
210
211
212
213
214
215
216
217
218
219
220
221
222
223
224
225
226
227
228
229
230
231
232
233
234
235
236
237
238
239
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
258
259
260
261
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
272
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
283
284
285
286
287
288
289
290
291
292
293
294
295
296
297
298
299
300
301
302
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
```
| ```
def Path(  # noqa: N802
    default: Annotated[
        Any,
        Doc(
            """
            Default value if the parameter field is not set.

            This doesn't affect `Path` parameters as the value is always required.
            The parameter is available only for compatibility.
            """
        ),
    ] = ...,
    *,
    default_factory: Annotated[
        Callable[[], Any] | None,
        Doc(
            """
            A callable to generate the default value.

            This doesn't affect `Path` parameters as the value is always required.
            The parameter is available only for compatibility.
            """
        ),
    ] = _Unset,
    alias: Annotated[
        str | None,
        Doc(
            """
            An alternative name for the parameter field.

            This will be used to extract the data and for the generated OpenAPI.
            It is particularly useful when you can't use the name you want because it
            is a Python reserved keyword or similar.
            """
        ),
    ] = None,
    alias_priority: Annotated[
        int | None,
        Doc(
            """
            Priority of the alias. This affects whether an alias generator is used.
            """
        ),
    ] = _Unset,
    validation_alias: Annotated[
        str | AliasPath | AliasChoices | None,
        Doc(
            """
            'Whitelist' validation step. The parameter field will be the single one
            allowed by the alias or set of aliases defined.
            """
        ),
    ] = None,
    serialization_alias: Annotated[
        str | None,
        Doc(
            """
            'Blacklist' validation step. The vanilla parameter field will be the
            single one of the alias' or set of aliases' fields and all the other
            fields will be ignored at serialization time.
            """
        ),
    ] = None,
    title: Annotated[
        str | None,
        Doc(
            """
            Human-readable title.

            Read more about it in the
            [FastAPI docs for Path Parameters and Numeric Validations](https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/#declare-metadata)
            """
        ),
    ] = None,
    description: Annotated[
        str | None,
        Doc(
            """
            Human-readable description.
            """
        ),
    ] = None,
    gt: Annotated[
        float | None,
        Doc(
            """
            Greater than. If set, value must be greater than this. Only applicable to
            numbers.

            Read more about it in the
            [FastAPI docs about Path parameters numeric validations](https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/#number-validations-greater-than-and-less-than-or-equal)
            """
        ),
    ] = None,
    ge: Annotated[
        float | None,
        Doc(
            """
            Greater than or equal. If set, value must be greater than or equal to
            this. Only applicable to numbers.

            Read more about it in the
            [FastAPI docs about Path parameters numeric validations](https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/#number-validations-greater-than-and-less-than-or-equal)
            """
        ),
    ] = None,
    lt: Annotated[
        float | None,
        Doc(
            """
            Less than. If set, value must be less than this. Only applicable to numbers.

            Read more about it in the
            [FastAPI docs about Path parameters numeric validations](https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/#number-validations-greater-than-and-less-than-or-equal)
            """
        ),
    ] = None,
    le: Annotated[
        float | None,
        Doc(
            """
            Less than or equal. If set, value must be less than or equal to this.
            Only applicable to numbers.

            Read more about it in the
            [FastAPI docs about Path parameters numeric validations](https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/#number-validations-greater-than-and-less-than-or-equal)
            """
        ),
    ] = None,
    min_length: Annotated[
        int | None,
        Doc(
            """
            Minimum length for strings.
            """
        ),
    ] = None,
    max_length: Annotated[
        int | None,
        Doc(
            """
            Maximum length for strings.
            """
        ),
    ] = None,
    pattern: Annotated[
        str | None,
        Doc(
            """
            RegEx pattern for strings.
            """
        ),
    ] = None,
    regex: Annotated[
        str | None,
        Doc(
            """
            RegEx pattern for strings.
            """
        ),
        deprecated(
            "Deprecated in FastAPI 0.100.0 and Pydantic v2, use `pattern` instead."
        ),
    ] = None,
    discriminator: Annotated[
        str | None,
        Doc(
            """
            Parameter field name for discriminating the type in a tagged union.
            """
        ),
    ] = None,
    strict: Annotated[
        bool | None,
        Doc(
            """
            If `True`, strict validation is applied to the field.
            """
        ),
    ] = _Unset,
    multiple_of: Annotated[
        float | None,
        Doc(
            """
            Value must be a multiple of this. Only applicable to numbers.
            """
        ),
    ] = _Unset,
    allow_inf_nan: Annotated[
        bool | None,
        Doc(
            """
            Allow `inf`, `-inf`, `nan`. Only applicable to numbers.
            """
        ),
    ] = _Unset,
    max_digits: Annotated[
        int | None,
        Doc(
            """
            Maximum number of digits allowed for decimal values.
            """
        ),
    ] = _Unset,
    decimal_places: Annotated[
        int | None,
        Doc(
            """
            Maximum number of decimal places allowed for decimal values.
            """
        ),
    ] = _Unset,
    examples: Annotated[
        list[Any] | None,
        Doc(
            """
            Example values for this field.

            Read more about it in the
            [FastAPI docs for Declare Request Example Data](https://fastapi.tiangolo.com/tutorial/schema-extra-example/)
            """
        ),
    ] = None,
    example: Annotated[
        Any | None,
        deprecated(
            "Deprecated in OpenAPI 3.1.0 that now uses JSON Schema 2020-12, "
            "although still supported. Use examples instead."
        ),
    ] = _Unset,
    openapi_examples: Annotated[
        dict[str, Example] | None,
        Doc(
            """
            OpenAPI-specific examples.

            It will be added to the generated OpenAPI (e.g. visible at `/docs`).

            Swagger UI (that provides the `/docs` interface) has better support for the
            OpenAPI-specific examples than the JSON Schema `examples`, that's the main
            use case for this.

            Read more about it in the
            [FastAPI docs for Declare Request Example Data](https://fastapi.tiangolo.com/tutorial/schema-extra-example/#using-the-openapi_examples-parameter).
            """
        ),
    ] = None,
    deprecated: Annotated[
        deprecated | str | bool | None,
        Doc(
            """
            Mark this parameter field as deprecated.

            It will affect the generated OpenAPI (e.g. visible at `/docs`).
            """
        ),
    ] = None,
    include_in_schema: Annotated[
        bool,
        Doc(
            """
            To include (or not) this parameter field in the generated OpenAPI.
            You probably don't need it, but it's available.

            This affects the generated OpenAPI (e.g. visible at `/docs`).
            """
        ),
    ] = True,
    json_schema_extra: Annotated[
        dict[str, Any] | None,
        Doc(
            """
            Any additional JSON schema data.
            """
        ),
    ] = None,
    **extra: Annotated[
        Any,
        Doc(
            """
            Include extra fields used by the JSON Schema.
            """
        ),
        deprecated(
            """
            The `extra` kwargs is deprecated. Use `json_schema_extra` instead.
            """
        ),
    ],
) -> Any:
    """
    Declare a path parameter for a *path operation*.

    Read more about it in the
    [FastAPI docs for Path Parameters and Numeric Validations](https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/).

```python
    from typing import Annotated

    from fastapi import FastAPI, Path

    app = FastAPI()


    @app.get("/items/{item_id}")
    async def read_items(
        item_id: Annotated[int, Path(title="The ID of the item to get")],
    ):
        return {"item_id": item_id}
```
    """
    return params.Path(
        default=default,
        default_factory=default_factory,
        alias=alias,
        alias_priority=alias_priority,
        validation_alias=validation_alias,
        serialization_alias=serialization_alias,
        title=title,
        description=description,
        gt=gt,
        ge=ge,
        lt=lt,
        le=le,
        min_length=min_length,
        max_length=max_length,
        pattern=pattern,
        regex=regex,
        discriminator=discriminator,
        strict=strict,
        multiple_of=multiple_of,
        allow_inf_nan=allow_inf_nan,
        max_digits=max_digits,
        decimal_places=decimal_places,
        example=example,
        examples=examples,
        openapi_examples=openapi_examples,
        deprecated=deprecated,
        include_in_schema=include_in_schema,
        json_schema_extra=json_schema_extra,
        **extra,
    )

```

---|---
