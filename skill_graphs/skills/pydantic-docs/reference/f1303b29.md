##  complex_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.complex_schema)
```
complex_schema(
    *,
    strict:  | None = None,
    ref:  | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> ComplexSchema

```

Returns a schema that matches a complex value, e.g.:
```
from pydantic_core import SchemaValidator, core_schema

schema = core_schema.complex_schema()
v = SchemaValidator(schema)
assert v.validate_python('1+2j') == complex(1, 2)
assert v.validate_python(complex(1, 2)) == complex(1, 2)

```

Parameters:
Name | Type | Description | Default
---|---|---|---
`strict` |  |  Whether the value should be a complex object instance or a value that can be converted to a complex object |  `None`
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`
Source code in `pydantic_core/core_schema.py`
```
823
824
825
826
827
828
829
830
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
```
| ```
def complex_schema(
    *,
    strict: bool | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> ComplexSchema:
    """
    Returns a schema that matches a complex value, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    schema = core_schema.complex_schema()
    v = SchemaValidator(schema)
    assert v.validate_python('1+2j') == complex(1, 2)
    assert v.validate_python(complex(1, 2)) == complex(1, 2)
```

    Args:
        strict: Whether the value should be a complex object instance or a value that can be converted to a complex object
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='complex',
        strict=strict,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
    )

```

---|---
##  str_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.str_schema)
```
str_schema(
    *,
    pattern:  | [] | None = None,
    max_length:  | None = None,
    min_length:  | None = None,
    strip_whitespace:  | None = None,
    to_lower:  | None = None,
    to_upper:  | None = None,
    regex_engine: (
        ["rust-regex", "python-re"] | None
    ) = None,
    strict:  | None = None,
    coerce_numbers_to_str:  | None = None,
    ref:  | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> StringSchema

```

Returns a schema that matches a string value, e.g.:
```
from pydantic_core import SchemaValidator, core_schema

schema = core_schema.str_schema(max_length=10, min_length=2)
v = SchemaValidator(schema)
assert v.validate_python('hello') == 'hello'

```

Parameters:
Name | Type | Description | Default
---|---|---|---
`pattern` |  |  A regex pattern that the value must match |  `None`
`max_length` |  |  The value must be at most this length |  `None`
`min_length` |  |  The value must be at least this length |  `None`
`strip_whitespace` |  |  Whether to strip whitespace from the value |  `None`
`to_lower` |  |  Whether to convert the value to lowercase |  `None`
`to_upper` |  |  Whether to convert the value to uppercase |  `None`
`regex_engine` |  |  The regex engine to use for pattern validation. Default is 'rust-regex'. - `rust-regex` uses the `python-re` use the  |  `None`
`strict` |  |  Whether the value should be a string or a value that can be converted to a string |  `None`
`coerce_numbers_to_str` |  |  Whether to enable coercion of any `Number` type to `str` (not applicable in `strict` mode). |  `None`
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`
Source code in `pydantic_core/core_schema.py`
```
873
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
909
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
922
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
```
| ```
def str_schema(
    *,
    pattern: str | Pattern[str] | None = None,
    max_length: int | None = None,
    min_length: int | None = None,
    strip_whitespace: bool | None = None,
    to_lower: bool | None = None,
    to_upper: bool | None = None,
    regex_engine: Literal['rust-regex', 'python-re'] | None = None,
    strict: bool | None = None,
    coerce_numbers_to_str: bool | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> StringSchema:
    """
    Returns a schema that matches a string value, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    schema = core_schema.str_schema(max_length=10, min_length=2)
    v = SchemaValidator(schema)
    assert v.validate_python('hello') == 'hello'
```

    Args:
        pattern: A regex pattern that the value must match
        max_length: The value must be at most this length
        min_length: The value must be at least this length
        strip_whitespace: Whether to strip whitespace from the value
        to_lower: Whether to convert the value to lowercase
        to_upper: Whether to convert the value to uppercase
        regex_engine: The regex engine to use for pattern validation. Default is 'rust-regex'.
            - `rust-regex` uses the [`regex`](https://docs.rs/regex) Rust
              crate, which is non-backtracking and therefore more DDoS
              resistant, but does not support all regex features.
            - `python-re` use the [`re`](https://docs.python.org/3/library/re.html) module,
              which supports all regex features, but may be slower.
        strict: Whether the value should be a string or a value that can be converted to a string
        coerce_numbers_to_str: Whether to enable coercion of any `Number` type to `str` (not applicable in `strict` mode).
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='str',
        pattern=pattern,
        max_length=max_length,
        min_length=min_length,
        strip_whitespace=strip_whitespace,
        to_lower=to_lower,
        to_upper=to_upper,
        regex_engine=regex_engine,
        strict=strict,
        coerce_numbers_to_str=coerce_numbers_to_str,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
    )

```

---|---
