##  dict_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.dict_schema)
```
dict_schema(
    keys_schema: CoreSchema | None = None,
    values_schema: CoreSchema | None = None,
    *,
    min_length:  | None = None,
    max_length:  | None = None,
    fail_fast:  | None = None,
    strict:  | None = None,
    ref:  | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> DictSchema

```

Returns a schema that matches a dict value, e.g.:
```
from pydantic_core import SchemaValidator, core_schema

schema = core_schema.dict_schema(
    keys_schema=core_schema.str_schema(), values_schema=core_schema.int_schema()
)
v = SchemaValidator(schema)
assert v.validate_python({'a': '1', 'b': 2}) == {'a': 1, 'b': 2}

```

Parameters:
Name | Type | Description | Default
---|---|---|---
`keys_schema` |  `CoreSchema | None` |  The value must be a dict with keys that match this schema |  `None`
`values_schema` |  `CoreSchema | None` |  The value must be a dict with values that match this schema |  `None`
`min_length` |  |  The value must be a dict with at least this many items |  `None`
`max_length` |  |  The value must be a dict with at most this many items |  `None`
`fail_fast` |  |  Stop validation on the first error |  `None`
`strict` |  |  Whether the keys and values should be validated with strict mode |  `None`
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`
Source code in `pydantic_core/core_schema.py`
```
1951
1952
1953
1954
1955
1956
1957
1958
1959
1960
1961
1962
1963
1964
1965
1966
1967
1968
1969
1970
1971
1972
1973
1974
1975
1976
1977
1978
1979
1980
1981
1982
1983
1984
1985
1986
1987
1988
1989
1990
1991
1992
1993
1994
1995
1996
1997
1998
```
| ```
def dict_schema(
    keys_schema: CoreSchema | None = None,
    values_schema: CoreSchema | None = None,
    *,
    min_length: int | None = None,
    max_length: int | None = None,
    fail_fast: bool | None = None,
    strict: bool | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> DictSchema:
    """
    Returns a schema that matches a dict value, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    schema = core_schema.dict_schema(
        keys_schema=core_schema.str_schema(), values_schema=core_schema.int_schema()
    )
    v = SchemaValidator(schema)
    assert v.validate_python({'a': '1', 'b': 2}) == {'a': 1, 'b': 2}
```

    Args:
        keys_schema: The value must be a dict with keys that match this schema
        values_schema: The value must be a dict with values that match this schema
        min_length: The value must be a dict with at least this many items
        max_length: The value must be a dict with at most this many items
        fail_fast: Stop validation on the first error
        strict: Whether the keys and values should be validated with strict mode
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='dict',
        keys_schema=keys_schema,
        values_schema=values_schema,
        min_length=min_length,
        max_length=max_length,
        fail_fast=fail_fast,
        strict=strict,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
    )

```

---|---
##  no_info_before_validator_function [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.no_info_before_validator_function)
```
no_info_before_validator_function(
    function: NoInfoValidatorFunction,
    schema: CoreSchema,
    *,
    ref:  | None = None,
    json_schema_input_schema: CoreSchema | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> BeforeValidatorFunctionSchema

```

Returns a schema that calls a validator function before validating, no `info` argument is provided, e.g.:
```
from pydantic_core import SchemaValidator, core_schema

def fn(v: bytes) -> str:
    return v.decode() + 'world'

func_schema = core_schema.no_info_before_validator_function(
    function=fn, schema=core_schema.str_schema()
)
schema = core_schema.typed_dict_schema({'a': core_schema.typed_dict_field(func_schema)})

v = SchemaValidator(schema)
assert v.validate_python({'a': b'hello '}) == {'a': 'hello world'}

```

Parameters:
Name | Type | Description | Default
---|---|---|---
`function` |  `NoInfoValidatorFunction` |  The validator function to call |  _required_
`schema` |  `CoreSchema` |  The schema to validate the output of the validator function |  _required_
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`
`json_schema_input_schema` |  `CoreSchema | None` |  The core schema to be used to generate the corresponding JSON Schema input type |  `None`
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`
Source code in `pydantic_core/core_schema.py`
```
2036
2037
2038
2039
2040
2041
2042
2043
2044
2045
2046
2047
2048
2049
2050
2051
2052
2053
2054
2055
2056
2057
2058
2059
2060
2061
2062
2063
2064
2065
2066
2067
2068
2069
2070
2071
2072
2073
2074
2075
2076
2077
2078
2079
```
| ```
def no_info_before_validator_function(
    function: NoInfoValidatorFunction,
    schema: CoreSchema,
    *,
    ref: str | None = None,
    json_schema_input_schema: CoreSchema | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> BeforeValidatorFunctionSchema:
    """
    Returns a schema that calls a validator function before validating, no `info` argument is provided, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    def fn(v: bytes) -> str:
        return v.decode() + 'world'

    func_schema = core_schema.no_info_before_validator_function(
        function=fn, schema=core_schema.str_schema()
    )
    schema = core_schema.typed_dict_schema({'a': core_schema.typed_dict_field(func_schema)})

    v = SchemaValidator(schema)
    assert v.validate_python({'a': b'hello '}) == {'a': 'hello world'}
```

    Args:
        function: The validator function to call
        schema: The schema to validate the output of the validator function
        ref: optional unique identifier of the schema, used to reference the schema in other places
        json_schema_input_schema: The core schema to be used to generate the corresponding JSON Schema input type
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='function-before',
        function={'type': 'no-info', 'function': function},
        schema=schema,
        ref=ref,
        json_schema_input_schema=json_schema_input_schema,
        metadata=metadata,
        serialization=serialization,
    )

```

---|---
