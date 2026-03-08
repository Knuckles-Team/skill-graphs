##  float_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.float_schema)
```
float_schema(
    *,
    allow_inf_nan:  | None = None,
    multiple_of:  | None = None,
    le:  | None = None,
    ge:  | None = None,
    lt:  | None = None,
    gt:  | None = None,
    strict:  | None = None,
    ref:  | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> FloatSchema

```

Returns a schema that matches a float value, e.g.:
```
from pydantic_core import SchemaValidator, core_schema

schema = core_schema.float_schema(le=0.8, ge=0.2)
v = SchemaValidator(schema)
assert v.validate_python('0.5') == 0.5

```

Parameters:
Name | Type | Description | Default
---|---|---|---
`allow_inf_nan` |  |  Whether to allow inf and nan values |  `None`
`multiple_of` |  |  The value must be a multiple of this number |  `None`
`le` |  |  The value must be less than or equal to this number |  `None`
`ge` |  |  The value must be greater than or equal to this number |  `None`
`lt` |  |  The value must be strictly less than this number |  `None`
`gt` |  |  The value must be strictly greater than this number |  `None`
`strict` |  |  Whether the value should be a float or a value that can be converted to a float |  `None`
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`
Source code in `pydantic_core/core_schema.py`
```
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
725
726
727
728
729
730
731
732
733
734
735
736
737
738
```
| ```
def float_schema(
    *,
    allow_inf_nan: bool | None = None,
    multiple_of: float | None = None,
    le: float | None = None,
    ge: float | None = None,
    lt: float | None = None,
    gt: float | None = None,
    strict: bool | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> FloatSchema:
    """
    Returns a schema that matches a float value, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    schema = core_schema.float_schema(le=0.8, ge=0.2)
    v = SchemaValidator(schema)
    assert v.validate_python('0.5') == 0.5
```

    Args:
        allow_inf_nan: Whether to allow inf and nan values
        multiple_of: The value must be a multiple of this number
        le: The value must be less than or equal to this number
        ge: The value must be greater than or equal to this number
        lt: The value must be strictly less than this number
        gt: The value must be strictly greater than this number
        strict: Whether the value should be a float or a value that can be converted to a float
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='float',
        allow_inf_nan=allow_inf_nan,
        multiple_of=multiple_of,
        le=le,
        ge=ge,
        lt=lt,
        gt=gt,
        strict=strict,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
    )

```

---|---
##  decimal_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.decimal_schema)
```
decimal_schema(
    *,
    allow_inf_nan:  | None = None,
    multiple_of:  | None = None,
    le:  | None = None,
    ge:  | None = None,
    lt:  | None = None,
    gt:  | None = None,
    max_digits:  | None = None,
    decimal_places:  | None = None,
    strict:  | None = None,
    ref:  | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> DecimalSchema

```

Returns a schema that matches a decimal value, e.g.:
```
from decimal import Decimal
from pydantic_core import SchemaValidator, core_schema

schema = core_schema.decimal_schema(le=0.8, ge=0.2)
v = SchemaValidator(schema)
assert v.validate_python('0.5') == Decimal('0.5')

```

Parameters:
Name | Type | Description | Default
---|---|---|---
`allow_inf_nan` |  |  Whether to allow inf and nan values |  `None`
`multiple_of` |  |  The value must be a multiple of this number |  `None`
`le` |  |  The value must be less than or equal to this number |  `None`
`ge` |  |  The value must be greater than or equal to this number |  `None`
`lt` |  |  The value must be strictly less than this number |  `None`
`gt` |  |  The value must be strictly greater than this number |  `None`
`max_digits` |  |  The maximum number of decimal digits allowed |  `None`
`decimal_places` |  |  The maximum number of decimal places allowed |  `None`
`strict` |  |  Whether the value should be a float or a value that can be converted to a float |  `None`
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`
Source code in `pydantic_core/core_schema.py`
```
757
758
759
760
761
762
763
764
765
766
767
768
769
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
807
808
809
810
811
812
```
| ```
def decimal_schema(
    *,
    allow_inf_nan: bool | None = None,
    multiple_of: Decimal | None = None,
    le: Decimal | None = None,
    ge: Decimal | None = None,
    lt: Decimal | None = None,
    gt: Decimal | None = None,
    max_digits: int | None = None,
    decimal_places: int | None = None,
    strict: bool | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> DecimalSchema:
    """
    Returns a schema that matches a decimal value, e.g.:

```py
    from decimal import Decimal
    from pydantic_core import SchemaValidator, core_schema

    schema = core_schema.decimal_schema(le=0.8, ge=0.2)
    v = SchemaValidator(schema)
    assert v.validate_python('0.5') == Decimal('0.5')
```

    Args:
        allow_inf_nan: Whether to allow inf and nan values
        multiple_of: The value must be a multiple of this number
        le: The value must be less than or equal to this number
        ge: The value must be greater than or equal to this number
        lt: The value must be strictly less than this number
        gt: The value must be strictly greater than this number
        max_digits: The maximum number of decimal digits allowed
        decimal_places: The maximum number of decimal places allowed
        strict: Whether the value should be a float or a value that can be converted to a float
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='decimal',
        gt=gt,
        ge=ge,
        lt=lt,
        le=le,
        max_digits=max_digits,
        decimal_places=decimal_places,
        multiple_of=multiple_of,
        allow_inf_nan=allow_inf_nan,
        strict=strict,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
    )

```

---|---
