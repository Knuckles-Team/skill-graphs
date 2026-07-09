##  tagged_union_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.tagged_union_schema)
```
tagged_union_schema(
    choices: [, CoreSchema],
    discriminator: (

        | [ | ]
        | [[ | ]]
        | [[], ]
    ),
    *,
    custom_error_type:  | None = None,
    custom_error_message:  | None = None,
    custom_error_context: (
        [,  |  | ] | None
    ) = None,
    strict:  | None = None,
    from_attributes:  | None = None,
    ref:  | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> TaggedUnionSchema

```

Returns a schema that matches a tagged union value, e.g.:
```
from pydantic_core import SchemaValidator, core_schema

apple_schema = core_schema.typed_dict_schema(
    {
        'foo': core_schema.typed_dict_field(core_schema.str_schema()),
        'bar': core_schema.typed_dict_field(core_schema.int_schema()),
    }
)
banana_schema = core_schema.typed_dict_schema(
    {
        'foo': core_schema.typed_dict_field(core_schema.str_schema()),
        'spam': core_schema.typed_dict_field(
            core_schema.list_schema(items_schema=core_schema.int_schema())
        ),
    }
)
schema = core_schema.tagged_union_schema(
    choices={
        'apple': apple_schema,
        'banana': banana_schema,
    },
    discriminator='foo',
)
v = SchemaValidator(schema)
assert v.validate_python({'foo': 'apple', 'bar': '123'}) == {'foo': 'apple', 'bar': 123}
assert v.validate_python({'foo': 'banana', 'spam': [1, 2, 3]}) == {
    'foo': 'banana',
    'spam': [1, 2, 3],
}

```

Parameters:
Name | Type | Description | Default
---|---|---|---
`choices` |  `CoreSchema]` |  The schemas to match When retrieving a schema from `choices` using the discriminator value, if the value is a str, it should be fed back into the `choices` map until a schema is obtained (This approach is to prevent multiple ownership of a single schema in Rust) |  _required_
`discriminator` |  |  The discriminator to use to determine the schema to use * If `discriminator` is a str, it is the name of the attribute to use as the discriminator * If `discriminator` is a list of int/str, it should be used as a "path" to access the discriminator * If `discriminator` is a list of lists, each inner list is a path, and the first path that exists is used * If `discriminator` is a callable, it should return the discriminator when called on the value to validate; the callable can return `None` to indicate that there is no matching discriminator present on the input |  _required_
`custom_error_type` |  |  The custom error type to use if the validation fails |  `None`
`custom_error_message` |  |  The custom error message to use if the validation fails |  `None`
`custom_error_context` |  |  The custom error context to use if the validation fails |  `None`
`strict` |  |  Whether the underlying schemas should be validated with strict mode |  `None`
`from_attributes` |  |  Whether to use the attributes of the object to retrieve the discriminator value |  `None`
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`
Source code in `pydantic_core/core_schema.py`
```
2676
2677
2678
2679
2680
2681
2682
2683
2684
2685
2686
2687
2688
2689
2690
2691
2692
2693
2694
2695
2696
2697
2698
2699
2700
2701
2702
2703
2704
2705
2706
2707
2708
2709
2710
2711
2712
2713
2714
2715
2716
2717
2718
2719
2720
2721
2722
2723
2724
2725
2726
2727
2728
2729
2730
2731
2732
2733
2734
2735
2736
2737
2738
2739
2740
2741
2742
2743
2744
2745
2746
2747
2748
2749
2750
2751
2752
2753
2754
2755
2756
```
| ```
def tagged_union_schema(
    choices: dict[Any, CoreSchema],
    discriminator: str | list[str | int] | list[list[str | int]] | Callable[[Any], Any],
    *,
    custom_error_type: str | None = None,
    custom_error_message: str | None = None,
    custom_error_context: dict[str, int | str | float] | None = None,
    strict: bool | None = None,
    from_attributes: bool | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> TaggedUnionSchema:
    """
    Returns a schema that matches a tagged union value, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    apple_schema = core_schema.typed_dict_schema(
        {
            'foo': core_schema.typed_dict_field(core_schema.str_schema()),
            'bar': core_schema.typed_dict_field(core_schema.int_schema()),
        }
    )
    banana_schema = core_schema.typed_dict_schema(
        {
            'foo': core_schema.typed_dict_field(core_schema.str_schema()),
            'spam': core_schema.typed_dict_field(
                core_schema.list_schema(items_schema=core_schema.int_schema())
            ),
        }
    )
    schema = core_schema.tagged_union_schema(
        choices={
            'apple': apple_schema,
            'banana': banana_schema,
        },
        discriminator='foo',
    )
    v = SchemaValidator(schema)
    assert v.validate_python({'foo': 'apple', 'bar': '123'}) == {'foo': 'apple', 'bar': 123}
    assert v.validate_python({'foo': 'banana', 'spam': [1, 2, 3]}) == {
        'foo': 'banana',
        'spam': [1, 2, 3],
    }
```

    Args:
        choices: The schemas to match
            When retrieving a schema from `choices` using the discriminator value, if the value is a str,
            it should be fed back into the `choices` map until a schema is obtained
            (This approach is to prevent multiple ownership of a single schema in Rust)
        discriminator: The discriminator to use to determine the schema to use
            * If `discriminator` is a str, it is the name of the attribute to use as the discriminator
            * If `discriminator` is a list of int/str, it should be used as a "path" to access the discriminator
            * If `discriminator` is a list of lists, each inner list is a path, and the first path that exists is used
            * If `discriminator` is a callable, it should return the discriminator when called on the value to validate;
              the callable can return `None` to indicate that there is no matching discriminator present on the input
        custom_error_type: The custom error type to use if the validation fails
        custom_error_message: The custom error message to use if the validation fails
        custom_error_context: The custom error context to use if the validation fails
        strict: Whether the underlying schemas should be validated with strict mode
        from_attributes: Whether to use the attributes of the object to retrieve the discriminator value
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='tagged-union',
        choices=choices,
        discriminator=discriminator,
        custom_error_type=custom_error_type,
        custom_error_message=custom_error_message,
        custom_error_context=custom_error_context,
        strict=strict,
        from_attributes=from_attributes,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
    )

```

---|---
##  chain_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.chain_schema)
```
chain_schema(
    steps: [CoreSchema],
    *,
    ref:  | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> ChainSchema

```

Returns a schema that chains the provided validation schemas, e.g.:
```
from pydantic_core import SchemaValidator, core_schema

def fn(v: str, info: core_schema.ValidationInfo) -> str:
    assert 'hello' in v
    return v + ' world'

fn_schema = core_schema.with_info_plain_validator_function(function=fn)
schema = core_schema.chain_schema(
    [fn_schema, fn_schema, fn_schema, core_schema.str_schema()]
)
v = SchemaValidator(schema)
assert v.validate_python('hello') == 'hello world world world'

```

Parameters:
Name | Type | Description | Default
---|---|---|---
`steps` |  `CoreSchema]` |  The schemas to chain |  _required_
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`
Source code in `pydantic_core/core_schema.py`
```
2767
2768
2769
2770
2771
2772
2773
2774
2775
2776
2777
2778
2779
2780
2781
2782
2783
2784
2785
2786
2787
2788
2789
2790
2791
2792
2793
2794
2795
2796
2797
2798
```
| ```
def chain_schema(
    steps: list[CoreSchema],
    *,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> ChainSchema:
    """
    Returns a schema that chains the provided validation schemas, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    def fn(v: str, info: core_schema.ValidationInfo) -> str:
        assert 'hello' in v
        return v + ' world'

    fn_schema = core_schema.with_info_plain_validator_function(function=fn)
    schema = core_schema.chain_schema(
        [fn_schema, fn_schema, fn_schema, core_schema.str_schema()]
    )
    v = SchemaValidator(schema)
    assert v.validate_python('hello') == 'hello world world world'
```

    Args:
        steps: The schemas to chain
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(type='chain', steps=steps, ref=ref, metadata=metadata, serialization=serialization)

```

---|---
