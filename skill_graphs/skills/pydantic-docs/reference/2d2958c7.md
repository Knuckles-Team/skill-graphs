Source code in `pydantic/json_schema.py`
```
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
```
| ```
def sort(self, value: JsonSchemaValue, parent_key: str | None = None) -> JsonSchemaValue:
    """Override this method to customize the sorting of the JSON schema (e.g., don't sort at all, sort all keys unconditionally, etc.)

    By default, alphabetically sort the keys in the JSON schema, skipping the 'properties' and 'default' keys to preserve field definition order.
    This sort is recursive, so it will sort all nested dictionaries as well.
    """
    sorted_dict: dict[str, JsonSchemaValue] = {}
    keys = value.keys()
    if parent_key not in ('properties', 'default'):
        keys = sorted(keys)
    for key in keys:
        sorted_dict[key] = self._sort_recursive(value[key], parent_key=key)
    return sorted_dict

```

---|---
###  invalid_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.invalid_schema)
```
invalid_schema(schema: InvalidSchema) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Placeholder - should never be called.
Source code in `pydantic/json_schema.py`
```
615
616
617
618
```
| ```
def invalid_schema(self, schema: core_schema.InvalidSchema) -> JsonSchemaValue:
    """Placeholder - should never be called."""

    raise RuntimeError('Cannot generate schema for invalid_schema. This is a bug! Please report it.')

```

---|---
###  any_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.any_schema)
```
any_schema(schema: AnySchema) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches any value.
Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `AnySchema` |  The core schema. |  _required_
Returns:
Type | Description
---|---
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.
Source code in `pydantic/json_schema.py`
```
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
```
| ```
def any_schema(self, schema: core_schema.AnySchema) -> JsonSchemaValue:
    """Generates a JSON schema that matches any value.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    return {}

```

---|---
###  none_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.none_schema)
```
none_schema(schema: NoneSchema) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches `None`.
Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `NoneSchema` |  The core schema. |  _required_
Returns:
Type | Description
---|---
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.
Source code in `pydantic/json_schema.py`
```
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
```
| ```
def none_schema(self, schema: core_schema.NoneSchema) -> JsonSchemaValue:
    """Generates a JSON schema that matches `None`.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    return {'type': 'null'}

```

---|---
###  bool_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.bool_schema)
```
bool_schema(schema: BoolSchema) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a bool value.
Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `BoolSchema` |  The core schema. |  _required_
Returns:
Type | Description
---|---
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.
Source code in `pydantic/json_schema.py`
```
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
```
| ```
def bool_schema(self, schema: core_schema.BoolSchema) -> JsonSchemaValue:
    """Generates a JSON schema that matches a bool value.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    return {'type': 'boolean'}

```

---|---
###  int_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.int_schema)
```
int_schema(schema: IntSchema) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches an int value.
Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `IntSchema` |  The core schema. |  _required_
Returns:
Type | Description
---|---
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.
Source code in `pydantic/json_schema.py`
```
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
```
| ```
def int_schema(self, schema: core_schema.IntSchema) -> JsonSchemaValue:
    """Generates a JSON schema that matches an int value.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    json_schema: dict[str, Any] = {'type': 'integer'}
    self.update_with_validations(json_schema, schema, self.ValidationsMapping.numeric)
    json_schema = {k: v for k, v in json_schema.items() if v not in {math.inf, -math.inf}}
    return json_schema

```

---|---
###  float_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.float_schema)
```
float_schema(schema: FloatSchema) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a float value.
Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `FloatSchema` |  The core schema. |  _required_
Returns:
Type | Description
---|---
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.
Source code in `pydantic/json_schema.py`
```
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
```
| ```
def float_schema(self, schema: core_schema.FloatSchema) -> JsonSchemaValue:
    """Generates a JSON schema that matches a float value.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    json_schema: dict[str, Any] = {'type': 'number'}
    self.update_with_validations(json_schema, schema, self.ValidationsMapping.numeric)
    json_schema = {k: v for k, v in json_schema.items() if v not in {math.inf, -math.inf}}
    return json_schema

```

---|---
###  decimal_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.decimal_schema)
```
decimal_schema(schema: DecimalSchema) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a decimal value.
Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `DecimalSchema` |  The core schema. |  _required_
Returns:
Type | Description
---|---
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.
Source code in `pydantic/json_schema.py`
```
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
739
740
741
742
743
744
745
746
747
748
749
750
751
752
753
754
```
| ```
def decimal_schema(self, schema: core_schema.DecimalSchema) -> JsonSchemaValue:
    """Generates a JSON schema that matches a decimal value.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """

    def get_decimal_pattern(schema: core_schema.DecimalSchema) -> str:
        max_digits = schema.get('max_digits')
        decimal_places = schema.get('decimal_places')

        pattern = (
            r'^(?!^[-+.]*$)[+-]?0*'  # check it is not empty string and not one or sequence of ".+-" characters.
        )

        # Case 1: Both max_digits and decimal_places are set
        if max_digits is not None and decimal_places is not None:
            integer_places = max(0, max_digits - decimal_places)
            pattern += (
                rf'(?:'
                rf'\d{{0,{integer_places}}}'
                rf'|'
                rf'(?=[\d.]{{1,{max_digits + 1}}}0*$)'
                rf'\d{{0,{integer_places}}}\.\d{{0,{decimal_places}}}0*$'
                rf')'
            )

        # Case 2: Only max_digits is set
        elif max_digits is not None and decimal_places is None:
            pattern += (
                rf'(?:'
                rf'\d{{0,{max_digits}}}'
                rf'|'
                rf'(?=[\d.]{{1,{max_digits + 1}}}0*$)'
                rf'\d*\.\d*0*$'
                rf')'
            )

        # Case 3: Only decimal_places is set
        elif max_digits is None and decimal_places is not None:
            pattern += rf'\d*\.?\d{{0,{decimal_places}}}0*$'

        # Case 4: Both are None (no restrictions)
        else:
            pattern += r'\d*\.?\d*$'  # look for arbitrary integer or decimal

        return pattern

    json_schema = self.str_schema(core_schema.str_schema(pattern=get_decimal_pattern(schema)))
    if self.mode == 'validation':
        multiple_of = schema.get('multiple_of')
        le = schema.get('le')
        ge = schema.get('ge')
        lt = schema.get('lt')
        gt = schema.get('gt')
        json_schema = {
            'anyOf': [
                self.float_schema(
                    core_schema.float_schema(
                        allow_inf_nan=schema.get('allow_inf_nan'),
                        multiple_of=None if multiple_of is None else float(multiple_of),
                        le=None if le is None else float(le),
                        ge=None if ge is None else float(ge),
                        lt=None if lt is None else float(lt),
                        gt=None if gt is None else float(gt),
                    )
                ),
                json_schema,
            ],
        }
    return json_schema

```

---|---
###  str_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.str_schema)
```
str_schema(schema: StringSchema) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a string value.
Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `StringSchema` |  The core schema. |  _required_
Returns:
Type | Description
---|---
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.
Source code in `pydantic/json_schema.py`
```
756
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
```
| ```
def str_schema(self, schema: core_schema.StringSchema) -> JsonSchemaValue:
    """Generates a JSON schema that matches a string value.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    json_schema = {'type': 'string'}
    self.update_with_validations(json_schema, schema, self.ValidationsMapping.string)
    if isinstance(json_schema.get('pattern'), Pattern):
        # TODO: should we add regex flags to the pattern?
        json_schema['pattern'] = json_schema.get('pattern').pattern  # type: ignore
    return json_schema

```

---|---
###  bytes_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.bytes_schema)
```
bytes_schema(schema: BytesSchema) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a bytes value.
Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `BytesSchema` |  The core schema. |  _required_
Returns:
Type | Description
---|---
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.
Source code in `pydantic/json_schema.py`
```
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
```
| ```
def bytes_schema(self, schema: core_schema.BytesSchema) -> JsonSchemaValue:
    """Generates a JSON schema that matches a bytes value.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    json_schema = {'type': 'string', 'format': 'base64url' if self._config.ser_json_bytes == 'base64' else 'binary'}
    self.update_with_validations(json_schema, schema, self.ValidationsMapping.bytes)
    return json_schema

```

---|---
###  date_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.date_schema)
```
date_schema(schema: DateSchema) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a date value.
Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `DateSchema` |  The core schema. |  _required_
Returns:
Type | Description
---|---
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.
Source code in `pydantic/json_schema.py`
```
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
```
| ```
def date_schema(self, schema: core_schema.DateSchema) -> JsonSchemaValue:
    """Generates a JSON schema that matches a date value.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    return {'type': 'string', 'format': 'date'}

```

---|---
###  time_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.time_schema)
```
time_schema(schema: TimeSchema) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a time value.
Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `TimeSchema` |  The core schema. |  _required_
Returns:
Type | Description
---|---
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.
Source code in `pydantic/json_schema.py`
```
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
```
| ```
def time_schema(self, schema: core_schema.TimeSchema) -> JsonSchemaValue:
    """Generates a JSON schema that matches a time value.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    return {'type': 'string', 'format': 'time'}

```

---|---
###  datetime_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.datetime_schema)
```
datetime_schema(schema: DatetimeSchema) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a datetime value.
Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `DatetimeSchema` |  The core schema. |  _required_
Returns:
Type | Description
---|---
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.
Source code in `pydantic/json_schema.py`
```
807
808
809
810
811
812
813
814
815
816
```
| ```
def datetime_schema(self, schema: core_schema.DatetimeSchema) -> JsonSchemaValue:
    """Generates a JSON schema that matches a datetime value.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    return {'type': 'string', 'format': 'date-time'}

```

---|---
###  timedelta_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.timedelta_schema)
```
timedelta_schema(
    schema: TimedeltaSchema,
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a timedelta value.
Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `TimedeltaSchema` |  The core schema. |  _required_
Returns:
Type | Description
---|---
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.
Source code in `pydantic/json_schema.py`
```
818
819
820
821
822
823
824
825
826
827
828
829
```
| ```
def timedelta_schema(self, schema: core_schema.TimedeltaSchema) -> JsonSchemaValue:
    """Generates a JSON schema that matches a timedelta value.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    if self._config.ser_json_timedelta == 'float':
        return {'type': 'number'}
    return {'type': 'string', 'format': 'duration'}

```

---|---
###  literal_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.literal_schema)
```
literal_schema(schema: LiteralSchema) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a literal value.
Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `LiteralSchema` |  The core schema. |  _required_
Returns:
Type | Description
---|---
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.
Source code in `pydantic/json_schema.py`
```
831
832
833
834
835
836
837
838
839
840
841
842
843
844
845
846
847
848
849
850
851
852
853
854
855
856
857
858
859
860
861
```
| ```
def literal_schema(self, schema: core_schema.LiteralSchema) -> JsonSchemaValue:
    """Generates a JSON schema that matches a literal value.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    expected = [to_jsonable_python(v.value if isinstance(v, Enum) else v) for v in schema['expected']]

    result: dict[str, Any] = {}
    if len(expected) == 1:
        result['const'] = expected[0]
    else:
        result['enum'] = expected

    types = {type(e) for e in expected}
    if types == {str}:
        result['type'] = 'string'
    elif types == {int}:
        result['type'] = 'integer'
    elif types == {float}:
        result['type'] = 'number'
    elif types == {bool}:
        result['type'] = 'boolean'
    elif types == {list}:
        result['type'] = 'array'
    elif types == {type(None)}:
        result['type'] = 'null'
    return result

```

---|---
###  missing_sentinel_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.missing_sentinel_schema)
```
missing_sentinel_schema(
    schema: MissingSentinelSchema,
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches the `MISSING` sentinel value.
Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `MissingSentinelSchema` |  The core schema. |  _required_
Returns:
Type | Description
---|---
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.
Source code in `pydantic/json_schema.py`
```
863
864
865
866
867
868
869
870
871
872
```
| ```
def missing_sentinel_schema(self, schema: core_schema.MissingSentinelSchema) -> JsonSchemaValue:
    """Generates a JSON schema that matches the `MISSING` sentinel value.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    raise PydanticOmit

```

---|---
###  enum_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.enum_schema)
```
enum_schema(schema: EnumSchema) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches an Enum value.
Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `EnumSchema` |  The core schema. |  _required_
Returns:
Type | Description
---|---
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.
Source code in `pydantic/json_schema.py`
```
874
875
876
877
878
879
880
881
882
883
884
885
886
887
888
889
890
891
892
893
894
895
896
897
898
899
900
901
902
903
904
905
906
907
908
```
| ```
def enum_schema(self, schema: core_schema.EnumSchema) -> JsonSchemaValue:
    """Generates a JSON schema that matches an Enum value.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    enum_type = schema['cls']
    description = None if not enum_type.__doc__ else inspect.cleandoc(enum_type.__doc__)
    if (
        description == 'An enumeration.'
    ):  # This is the default value provided by enum.EnumMeta.__new__; don't use it
        description = None
    result: dict[str, Any] = {'title': enum_type.__name__, 'description': description}
    result = {k: v for k, v in result.items() if v is not None}

    expected = [to_jsonable_python(v.value) for v in schema['members']]

    result['enum'] = expected

    types = {type(e) for e in expected}
    if isinstance(enum_type, str) or types == {str}:
        result['type'] = 'string'
    elif isinstance(enum_type, int) or types == {int}:
        result['type'] = 'integer'
    elif isinstance(enum_type, float) or types == {float}:
        result['type'] = 'number'
    elif types == {bool}:
        result['type'] = 'boolean'
    elif types == {list}:
        result['type'] = 'array'

    return result

```

---|---
###  is_instance_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.is_instance_schema)
```
is_instance_schema(
    schema: IsInstanceSchema,
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Handles JSON schema generation for a core schema that checks if a value is an instance of a class.
Unless overridden in a subclass, this raises an error.
Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `IsInstanceSchema` |  The core schema. |  _required_
Returns:
Type | Description
---|---
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.
Source code in `pydantic/json_schema.py`
```
910
911
912
913
914
915
916
917
918
919
920
921
```
| ```
def is_instance_schema(self, schema: core_schema.IsInstanceSchema) -> JsonSchemaValue:
    """Handles JSON schema generation for a core schema that checks if a value is an instance of a class.

    Unless overridden in a subclass, this raises an error.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    return self.handle_invalid_for_json_schema(schema, f'core_schema.IsInstanceSchema ({schema["cls"]})')

```

---|---
###  is_subclass_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.is_subclass_schema)
```
is_subclass_schema(
    schema: IsSubclassSchema,
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Handles JSON schema generation for a core schema that checks if a value is a subclass of a class.
For backwards compatibility with v1, this does not raise an error, but can be overridden to change this.
Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `IsSubclassSchema` |  The core schema. |  _required_
Returns:
Type | Description
---|---
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.
Source code in `pydantic/json_schema.py`
```
923
924
925
926
927
928
929
930
931
932
933
934
935
```
| ```
def is_subclass_schema(self, schema: core_schema.IsSubclassSchema) -> JsonSchemaValue:
    """Handles JSON schema generation for a core schema that checks if a value is a subclass of a class.

    For backwards compatibility with v1, this does not raise an error, but can be overridden to change this.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    # Note: This is for compatibility with V1; you can override if you want different behavior.
    return {}

```

---|---
###  callable_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.callable_schema)
```
callable_schema(schema: CallableSchema) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)
