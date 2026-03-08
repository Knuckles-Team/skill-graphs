##  models_json_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.models_json_schema)
```
models_json_schema(
    models: [
        [
            [BaseModel[](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel)] | [PydanticDataclass],
            JsonSchemaMode[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaMode),
        ]
    ],
    *,
    by_alias:  = True,
    title:  | None = None,
    description:  | None = None,
    ref_template:  = DEFAULT_REF_TEMPLATE[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.DEFAULT_REF_TEMPLATE),
    union_format: [
        "any_of", "primitive_type_array"
    ] = "any_of",
    schema_generator: [
        GenerateJsonSchema[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema)
    ] = GenerateJsonSchema[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema)
) -> [
    [
        [
            [BaseModel[](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel)] | [PydanticDataclass],
            JsonSchemaMode[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaMode),
        ],
        JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue),
    ],
    JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue),
]

```

Utility function to generate a JSON Schema for multiple models.
Parameters:
Name | Type | Description | Default
---|---|---|---
`models` |  `BaseModel[](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel)] | PydanticDataclass], JsonSchemaMode[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaMode)]]` |  A sequence of tuples of the form (model, mode). |  _required_
`by_alias` |  |  Whether field aliases should be used as keys in the generated JSON Schema. |  `True`
`title` |  |  The title of the generated JSON Schema. |  `None`
`description` |  |  The description of the generated JSON Schema. |  `None`
`ref_template` |  |  The reference template to use for generating JSON Schema references. |  `DEFAULT_REF_TEMPLATE[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.DEFAULT_REF_TEMPLATE)`
`union_format` |  |  The format to use when combining schemas from unions together. Can be one of:
  * `'any_of'`: Use the
  * `'primitive_type_array'`: Use the `string`, `boolean`, `null`, `integer` or `number`) or contains constraints/metadata, falls back to `any_of`.

|  `'any_of'`
`schema_generator` |  `GenerateJsonSchema[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema)]` |  The schema generator to use for generating the JSON Schema. |  `GenerateJsonSchema[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema)`
Returns:
Type | Description
---|---
`BaseModel[](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel)] | PydanticDataclass], JsonSchemaMode[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaMode)], JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)], JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)]` |  A tuple where: - The first element is a dictionary whose keys are tuples of JSON schema key type and JSON mode, and whose values are the JSON schema corresponding to that pair of inputs. (These schemas may have JsonRef references to definitions that are defined in the second returned element.) - The second element is a JSON schema containing all definitions referenced in the first returned element, along with the optional title and description keys.
Source code in `pydantic/json_schema.py`
```
2551
2552
2553
2554
2555
2556
2557
2558
2559
2560
2561
2562
2563
2564
2565
2566
2567
2568
2569
2570
2571
2572
2573
2574
2575
2576
2577
2578
2579
2580
2581
2582
2583
2584
2585
2586
2587
2588
2589
2590
2591
2592
2593
2594
2595
2596
2597
2598
2599
2600
2601
2602
2603
2604
2605
```
| ```
def models_json_schema(
    models: Sequence[tuple[type[BaseModel] | type[PydanticDataclass], JsonSchemaMode]],
    *,
    by_alias: bool = True,
    title: str | None = None,
    description: str | None = None,
    ref_template: str = DEFAULT_REF_TEMPLATE,
    union_format: Literal['any_of', 'primitive_type_array'] = 'any_of',
    schema_generator: type[GenerateJsonSchema] = GenerateJsonSchema,
) -> tuple[dict[tuple[type[BaseModel] | type[PydanticDataclass], JsonSchemaMode], JsonSchemaValue], JsonSchemaValue]:
    """Utility function to generate a JSON Schema for multiple models.

    Args:
        models: A sequence of tuples of the form (model, mode).
        by_alias: Whether field aliases should be used as keys in the generated JSON Schema.
        title: The title of the generated JSON Schema.
        description: The description of the generated JSON Schema.
        ref_template: The reference template to use for generating JSON Schema references.
        union_format: The format to use when combining schemas from unions together. Can be one of:

            - `'any_of'`: Use the [`anyOf`](https://json-schema.org/understanding-json-schema/reference/combining#anyOf)
              keyword to combine schemas (the default).
            - `'primitive_type_array'`: Use the [`type`](https://json-schema.org/understanding-json-schema/reference/type)
              keyword as an array of strings, containing each type of the combination. If any of the schemas is not a primitive
              type (`string`, `boolean`, `null`, `integer` or `number`) or contains constraints/metadata, falls back to
              `any_of`.
        schema_generator: The schema generator to use for generating the JSON Schema.

    Returns:
        A tuple where:
            - The first element is a dictionary whose keys are tuples of JSON schema key type and JSON mode, and
                whose values are the JSON schema corresponding to that pair of inputs. (These schemas may have
                JsonRef references to definitions that are defined in the second returned element.)
            - The second element is a JSON schema containing all definitions referenced in the first returned
                    element, along with the optional title and description keys.
    """
    for cls, _ in models:
        if isinstance(cls.__pydantic_core_schema__, _mock_val_ser.MockCoreSchema):
            cls.__pydantic_core_schema__.rebuild()

    instance = schema_generator(by_alias=by_alias, ref_template=ref_template, union_format=union_format)
    inputs: list[tuple[type[BaseModel] | type[PydanticDataclass], JsonSchemaMode, CoreSchema]] = [
        (m, mode, m.__pydantic_core_schema__) for m, mode in models
    ]
    json_schemas_map, definitions = instance.generate_definitions(inputs)

    json_schema: dict[str, Any] = {}
    if definitions:
        json_schema['$defs'] = definitions
    if title:
        json_schema['title'] = title
    if description:
        json_schema['description'] = description

    return json_schemas_map, json_schema

```

---|---
Was this page helpful?
Thanks for your feedback!
Thanks for your feedback!
Made with
