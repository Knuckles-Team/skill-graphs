##  Examples [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.Examples)
```
Examples(
    examples: [, ],
    mode: (
        ["validation", "serialization"] | None
    ) = None,
)

```

```
Examples(
    examples: [],
    mode: (
        ["validation", "serialization"] | None
    ) = None,
)

```

```
Examples(
    examples: [, ] | [],
    mode: (
        ["validation", "serialization"] | None
    ) = None,
)

```

Add examples to a JSON schema.
If the JSON Schema already contains examples, the provided examples will be appended.
If `mode` is set this will only apply to that schema generation mode, allowing you to add different examples for validation and serialization.
Source code in `pydantic/json_schema.py`
```
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
```
| ```
def __init__(
    self, examples: dict[str, Any] | list[Any], mode: Literal['validation', 'serialization'] | None = None
) -> None:
    if isinstance(examples, dict):
        warnings.warn(
            'Using a dict for `examples` is deprecated, use a list instead.',
            PydanticDeprecatedSince29,
            stacklevel=2,
        )
    self.examples = examples
    self.mode = mode

```

---|---
##  SkipJsonSchema `dataclass` [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.SkipJsonSchema)
```
SkipJsonSchema()

```

Usage Documentation
[`SkipJsonSchema` Annotation](https://docs.pydantic.dev/latest/concepts/json_schema/#skipjsonschema-annotation)
Add this as an annotation on a field to skip generating a JSON schema for that field.
Example
```
from pprint import pprint
from typing import Union

from pydantic import BaseModel
from pydantic.json_schema import SkipJsonSchema

class Model(BaseModel):
    a: Union[int, None] = None  [](https://docs.pydantic.dev/latest/api/json_schema/#__code_180_annotation_1)
    b: Union[int, SkipJsonSchema[None]] = None  [](https://docs.pydantic.dev/latest/api/json_schema/#__code_180_annotation_2)
    c: SkipJsonSchema[Union[int, None]] = None  [](https://docs.pydantic.dev/latest/api/json_schema/#__code_180_annotation_3)

pprint(Model.model_json_schema())
'''
{
    'properties': {
        'a': {
            'anyOf': [
                {'type': 'integer'},
                {'type': 'null'}
            ],
            'default': None,
            'title': 'A'
        },
        'b': {
            'default': None,
            'title': 'B',
            'type': 'integer'
        }
    },
    'title': 'Model',
    'type': 'object'
}
'''

```

##  model_json_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.model_json_schema)
```
model_json_schema(
    cls: [BaseModel[](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel)] | [PydanticDataclass],
    by_alias:  = True,
    ref_template:  = DEFAULT_REF_TEMPLATE[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.DEFAULT_REF_TEMPLATE),
    union_format: [
        "any_of", "primitive_type_array"
    ] = "any_of",
    schema_generator: [
        GenerateJsonSchema[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema)
    ] = GenerateJsonSchema[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema),
    mode: JsonSchemaMode[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaMode) = "validation",
) -> [, ]

```

Utility function to generate a JSON Schema for a model.
Parameters:
Name | Type | Description | Default
---|---|---|---
`cls` |  `BaseModel[](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel)] | PydanticDataclass]` |  The model class to generate a JSON Schema for. |  _required_
`by_alias` |  |  If `True` (the default), fields will be serialized according to their alias. If `False`, fields will be serialized according to their attribute name. |  `True`
`ref_template` |  |  The template to use for generating JSON Schema references. |  `DEFAULT_REF_TEMPLATE[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.DEFAULT_REF_TEMPLATE)`
`union_format` |  |  The format to use when combining schemas from unions together. Can be one of:
  * `'any_of'`: Use the
  * `'primitive_type_array'`: Use the `string`, `boolean`, `null`, `integer` or `number`) or contains constraints/metadata, falls back to `any_of`.

|  `'any_of'`
`schema_generator` |  `GenerateJsonSchema[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema)]` |  The class to use for generating the JSON Schema. |  `GenerateJsonSchema[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema)`
`mode` |  `JsonSchemaMode[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaMode)` |  The mode to use for generating the JSON Schema. It can be one of the following:
  * 'validation': Generate a JSON Schema for validating data.
  * 'serialization': Generate a JSON Schema for serializing data.

|  `'validation'`
Returns:
Type | Description
---|---
|  The generated JSON Schema.
Source code in `pydantic/json_schema.py`
```
2503
2504
2505
2506
2507
2508
2509
2510
2511
2512
2513
2514
2515
2516
2517
2518
2519
2520
2521
2522
2523
2524
2525
2526
2527
2528
2529
2530
2531
2532
2533
2534
2535
2536
2537
2538
2539
2540
2541
2542
2543
2544
2545
2546
2547
2548
```
| ```
def model_json_schema(
    cls: type[BaseModel] | type[PydanticDataclass],
    by_alias: bool = True,
    ref_template: str = DEFAULT_REF_TEMPLATE,
    union_format: Literal['any_of', 'primitive_type_array'] = 'any_of',
    schema_generator: type[GenerateJsonSchema] = GenerateJsonSchema,
    mode: JsonSchemaMode = 'validation',
) -> dict[str, Any]:
    """Utility function to generate a JSON Schema for a model.

    Args:
        cls: The model class to generate a JSON Schema for.
        by_alias: If `True` (the default), fields will be serialized according to their alias.
            If `False`, fields will be serialized according to their attribute name.
        ref_template: The template to use for generating JSON Schema references.
        union_format: The format to use when combining schemas from unions together. Can be one of:

            - `'any_of'`: Use the [`anyOf`](https://json-schema.org/understanding-json-schema/reference/combining#anyOf)
              keyword to combine schemas (the default).
            - `'primitive_type_array'`: Use the [`type`](https://json-schema.org/understanding-json-schema/reference/type)
              keyword as an array of strings, containing each type of the combination. If any of the schemas is not a primitive
              type (`string`, `boolean`, `null`, `integer` or `number`) or contains constraints/metadata, falls back to
              `any_of`.
        schema_generator: The class to use for generating the JSON Schema.
        mode: The mode to use for generating the JSON Schema. It can be one of the following:

            - 'validation': Generate a JSON Schema for validating data.
            - 'serialization': Generate a JSON Schema for serializing data.

    Returns:
        The generated JSON Schema.
    """
    from .main import BaseModel

    schema_generator_instance = schema_generator(
        by_alias=by_alias, ref_template=ref_template, union_format=union_format
    )

    if isinstance(cls.__pydantic_core_schema__, _mock_val_ser.MockCoreSchema):
        cls.__pydantic_core_schema__.rebuild()

    if cls is BaseModel:
        raise AttributeError('model_json_schema() must be called on a subclass of BaseModel, not BaseModel itself.')

    assert not isinstance(cls.__pydantic_core_schema__, _mock_val_ser.MockCoreSchema), 'this is a bug! please report it'
    return schema_generator_instance.generate(cls.__pydantic_core_schema__, mode=mode)

```

---|---
