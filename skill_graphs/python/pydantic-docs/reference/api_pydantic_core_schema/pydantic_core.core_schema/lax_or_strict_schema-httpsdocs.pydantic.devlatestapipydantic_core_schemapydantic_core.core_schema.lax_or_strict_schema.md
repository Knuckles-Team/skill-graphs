##  lax_or_strict_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.lax_or_strict_schema)
```
lax_or_strict_schema(
    lax_schema: CoreSchema,
    strict_schema: CoreSchema,
    *,
    strict:  | None = None,
    ref:  | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> LaxOrStrictSchema

```

Returns a schema that uses the lax or strict schema, e.g.:
```
from pydantic_core import SchemaValidator, core_schema

def fn(v: str, info: core_schema.ValidationInfo) -> str:
    assert 'hello' in v
    return v + ' world'

lax_schema = core_schema.int_schema(strict=False)
strict_schema = core_schema.int_schema(strict=True)

schema = core_schema.lax_or_strict_schema(
    lax_schema=lax_schema, strict_schema=strict_schema, strict=True
)
v = SchemaValidator(schema)
assert v.validate_python(123) == 123

schema = core_schema.lax_or_strict_schema(
    lax_schema=lax_schema, strict_schema=strict_schema, strict=False
)
v = SchemaValidator(schema)
assert v.validate_python('123') == 123

```

Parameters:
Name | Type | Description | Default
---|---|---|---
`lax_schema` |  `CoreSchema` |  The lax schema to use |  _required_
`strict_schema` |  `CoreSchema` |  The strict schema to use |  _required_
`strict` |  |  Whether the strict schema should be used |  `None`
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`
Source code in `pydantic_core/core_schema.py`
```
2811
2812
2813
2814
2815
2816
2817
2818
2819
2820
2821
2822
2823
2824
2825
2826
2827
2828
2829
2830
2831
2832
2833
2834
2835
2836
2837
2838
2839
2840
2841
2842
2843
2844
2845
2846
2847
2848
2849
2850
2851
2852
2853
2854
2855
2856
2857
2858
2859
2860
2861
2862
```
| ```
def lax_or_strict_schema(
    lax_schema: CoreSchema,
    strict_schema: CoreSchema,
    *,
    strict: bool | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> LaxOrStrictSchema:
    """
    Returns a schema that uses the lax or strict schema, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    def fn(v: str, info: core_schema.ValidationInfo) -> str:
        assert 'hello' in v
        return v + ' world'

    lax_schema = core_schema.int_schema(strict=False)
    strict_schema = core_schema.int_schema(strict=True)

    schema = core_schema.lax_or_strict_schema(
        lax_schema=lax_schema, strict_schema=strict_schema, strict=True
    )
    v = SchemaValidator(schema)
    assert v.validate_python(123) == 123

    schema = core_schema.lax_or_strict_schema(
        lax_schema=lax_schema, strict_schema=strict_schema, strict=False
    )
    v = SchemaValidator(schema)
    assert v.validate_python('123') == 123
```

    Args:
        lax_schema: The lax schema to use
        strict_schema: The strict schema to use
        strict: Whether the strict schema should be used
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='lax-or-strict',
        lax_schema=lax_schema,
        strict_schema=strict_schema,
        strict=strict,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
    )

```

---|---
##  json_or_python_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.json_or_python_schema)
```
json_or_python_schema(
    json_schema: CoreSchema,
    python_schema: CoreSchema,
    *,
    ref:  | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> JsonOrPythonSchema

```

Returns a schema that uses the Json or Python schema depending on the input:
```
from pydantic_core import SchemaValidator, ValidationError, core_schema

v = SchemaValidator(
    core_schema.json_or_python_schema(
        json_schema=core_schema.int_schema(),
        python_schema=core_schema.int_schema(strict=True),
    )
)

assert v.validate_json('"123"') == 123

try:
    v.validate_python('123')
except ValidationError:
    pass
else:
    raise AssertionError('Validation should have failed')

```

Parameters:
Name | Type | Description | Default
---|---|---|---
`json_schema` |  `CoreSchema` |  The schema to use for Json inputs |  _required_
`python_schema` |  `CoreSchema` |  The schema to use for Python inputs |  _required_
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`
Source code in `pydantic_core/core_schema.py`
```
2874
2875
2876
2877
2878
2879
2880
2881
2882
2883
2884
2885
2886
2887
2888
2889
2890
2891
2892
2893
2894
2895
2896
2897
2898
2899
2900
2901
2902
2903
2904
2905
2906
2907
2908
2909
2910
2911
2912
2913
2914
2915
2916
2917
2918
2919
```
| ```
def json_or_python_schema(
    json_schema: CoreSchema,
    python_schema: CoreSchema,
    *,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> JsonOrPythonSchema:
    """
    Returns a schema that uses the Json or Python schema depending on the input:

```py
    from pydantic_core import SchemaValidator, ValidationError, core_schema

    v = SchemaValidator(
        core_schema.json_or_python_schema(
            json_schema=core_schema.int_schema(),
            python_schema=core_schema.int_schema(strict=True),
        )
    )

    assert v.validate_json('"123"') == 123

    try:
        v.validate_python('123')
    except ValidationError:
        pass
    else:
        raise AssertionError('Validation should have failed')
```

    Args:
        json_schema: The schema to use for Json inputs
        python_schema: The schema to use for Python inputs
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='json-or-python',
        json_schema=json_schema,
        python_schema=python_schema,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
    )

```

---|---
