##  json_schema [¶](https://docs.pydantic.dev/latest/api/type_adapter/#pydantic.type_adapter.TypeAdapter.json_schema "Permanent link")
```
json_schema(
    *,
    by_alias:  = True,
    ref_template:  = DEFAULT_REF_TEMPLATE[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.DEFAULT_REF_TEMPLATE "pydantic.json_schema.DEFAULT_REF_TEMPLATE"),
    union_format: [
        "any_of", "primitive_type_array"
    ] = "any_of",
    schema_generator: [
        GenerateJsonSchema[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema "pydantic.json_schema.GenerateJsonSchema")
    ] = GenerateJsonSchema[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema "pydantic.json_schema.GenerateJsonSchema"),
    mode: JsonSchemaMode[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaMode "pydantic.json_schema.JsonSchemaMode") = "validation"
) -> [, ]

```

Generate a JSON schema for the adapted type.
Parameters:
Name | Type | Description | Default
---|---|---|---
`by_alias` |  |  Whether to use alias names for field names. |  `True`
`ref_template` |  |  The format string used for generating $ref strings. |  `DEFAULT_REF_TEMPLATE[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.DEFAULT_REF_TEMPLATE "pydantic.json_schema.DEFAULT_REF_TEMPLATE")`
`union_format` |  |  The format to use when combining schemas from unions together. Can be one of:
  * `'any_of'`: Use the
  * `'primitive_type_array'`: Use the `string`, `boolean`, `null`, `integer` or `number`) or contains constraints/metadata, falls back to `any_of`.

|  `'any_of'`
`schema_generator` |  `GenerateJsonSchema[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema "pydantic.json_schema.GenerateJsonSchema")]` |  To override the logic used to generate the JSON schema, as a subclass of `GenerateJsonSchema` with your desired modifications |  `GenerateJsonSchema[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema "pydantic.json_schema.GenerateJsonSchema")`
`mode` |  `JsonSchemaMode[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaMode "pydantic.json_schema.JsonSchemaMode")` |  The mode in which to generate the schema. |  `'validation'`
`schema_generator` |  `GenerateJsonSchema[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema "pydantic.json_schema.GenerateJsonSchema")]` |  The generator class used for creating the schema. |  `GenerateJsonSchema[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema "pydantic.json_schema.GenerateJsonSchema")`
`mode` |  `JsonSchemaMode[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaMode "pydantic.json_schema.JsonSchemaMode")` |  The mode to use for schema generation. |  `'validation'`
Returns:
Type | Description
---|---
|  The JSON schema for the model as a dictionary.
Source code in `pydantic/type_adapter.py`
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
```
| ```
def json_schema(
    self,
    *,
    by_alias: bool = True,
    ref_template: str = DEFAULT_REF_TEMPLATE,
    union_format: Literal['any_of', 'primitive_type_array'] = 'any_of',
    schema_generator: type[GenerateJsonSchema] = GenerateJsonSchema,
    mode: JsonSchemaMode = 'validation',
) -> dict[str, Any]:
    """Generate a JSON schema for the adapted type.

    Args:
        by_alias: Whether to use alias names for field names.
        ref_template: The format string used for generating $ref strings.
        union_format: The format to use when combining schemas from unions together. Can be one of:

            - `'any_of'`: Use the [`anyOf`](https://json-schema.org/understanding-json-schema/reference/combining#anyOf)
            keyword to combine schemas (the default).
            - `'primitive_type_array'`: Use the [`type`](https://json-schema.org/understanding-json-schema/reference/type)
            keyword as an array of strings, containing each type of the combination. If any of the schemas is not a primitive
            type (`string`, `boolean`, `null`, `integer` or `number`) or contains constraints/metadata, falls back to
            `any_of`.
        schema_generator: To override the logic used to generate the JSON schema, as a subclass of
            `GenerateJsonSchema` with your desired modifications
        mode: The mode in which to generate the schema.
        schema_generator: The generator class used for creating the schema.
        mode: The mode to use for schema generation.

    Returns:
        The JSON schema for the model as a dictionary.
    """
    schema_generator_instance = schema_generator(
        by_alias=by_alias, ref_template=ref_template, union_format=union_format
    )
    if isinstance(self.core_schema, _mock_val_ser.MockCoreSchema):
        self.core_schema.rebuild()
        assert not isinstance(self.core_schema, _mock_val_ser.MockCoreSchema), 'this is a bug! please report it'
    return schema_generator_instance.generate(self.core_schema, mode=mode)

```

---|---
##  json_schemas `staticmethod` [¶](https://docs.pydantic.dev/latest/api/type_adapter/#pydantic.type_adapter.TypeAdapter.json_schemas "Permanent link")
```
json_schemas(
    inputs: [
        [
            JsonSchemaKeyT, JsonSchemaMode[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaMode "pydantic.json_schema.JsonSchemaMode"), TypeAdapter[](https://docs.pydantic.dev/latest/api/type_adapter/#pydantic.type_adapter.TypeAdapter "pydantic.type_adapter.TypeAdapter")[]
        ]
    ],
    /,
    *,
    by_alias:  = True,
    title:  | None = None,
    description:  | None = None,
    ref_template:  = DEFAULT_REF_TEMPLATE[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.DEFAULT_REF_TEMPLATE "pydantic.json_schema.DEFAULT_REF_TEMPLATE"),
    union_format: [
        "any_of", "primitive_type_array"
    ] = "any_of",
    schema_generator: [
        GenerateJsonSchema[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema "pydantic.json_schema.GenerateJsonSchema")
    ] = GenerateJsonSchema[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema "pydantic.json_schema.GenerateJsonSchema"),
) -> [
    [
        [JsonSchemaKeyT, JsonSchemaMode[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaMode "pydantic.json_schema.JsonSchemaMode")],
        JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue "pydantic.json_schema.JsonSchemaValue"),
    ],
    JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue "pydantic.json_schema.JsonSchemaValue"),
]

```

Generate a JSON schema including definitions from multiple type adapters.
Parameters:
Name | Type | Description | Default
---|---|---|---
`inputs` |  `JsonSchemaKeyT, JsonSchemaMode[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaMode "pydantic.json_schema.JsonSchemaMode"), TypeAdapter[](https://docs.pydantic.dev/latest/api/type_adapter/#pydantic.type_adapter.TypeAdapter "pydantic.type_adapter.TypeAdapter")[` |  Inputs to schema generation. The first two items will form the keys of the (first) output mapping; the type adapters will provide the core schemas that get converted into definitions in the output JSON schema. |  _required_
`by_alias` |  |  Whether to use alias names. |  `True`
`title` |  |  The title for the schema. |  `None`
`description` |  |  The description for the schema. |  `None`
`ref_template` |  |  The format string used for generating $ref strings. |  `DEFAULT_REF_TEMPLATE[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.DEFAULT_REF_TEMPLATE "pydantic.json_schema.DEFAULT_REF_TEMPLATE")`
`union_format` |  |  The format to use when combining schemas from unions together. Can be one of:
  * `'any_of'`: Use the
  * `'primitive_type_array'`: Use the `string`, `boolean`, `null`, `integer` or `number`) or contains constraints/metadata, falls back to `any_of`.

|  `'any_of'`
`schema_generator` |  `GenerateJsonSchema[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema "pydantic.json_schema.GenerateJsonSchema")]` |  The generator class used for creating the schema. |  `GenerateJsonSchema[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema "pydantic.json_schema.GenerateJsonSchema")`
Returns:
Type | Description
---|---
`JsonSchemaKeyT, JsonSchemaMode[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaMode "pydantic.json_schema.JsonSchemaMode")], JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue "pydantic.json_schema.JsonSchemaValue")], JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue "pydantic.json_schema.JsonSchemaValue")]` |  A tuple where:
  * The first element is a dictionary whose keys are tuples of JSON schema key type and JSON mode, and whose values are the JSON schema corresponding to that pair of inputs. (These schemas may have JsonRef references to definitions that are defined in the second returned element.)
  * The second element is a JSON schema containing all definitions referenced in the first returned element, along with the optional title and description keys.


Source code in `pydantic/type_adapter.py`
```
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
755
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
```
| ```
@staticmethod
def json_schemas(
    inputs: Iterable[tuple[JsonSchemaKeyT, JsonSchemaMode, TypeAdapter[Any]]],
    /,
    *,
    by_alias: bool = True,
    title: str | None = None,
    description: str | None = None,
    ref_template: str = DEFAULT_REF_TEMPLATE,
    union_format: Literal['any_of', 'primitive_type_array'] = 'any_of',
    schema_generator: type[GenerateJsonSchema] = GenerateJsonSchema,
) -> tuple[dict[tuple[JsonSchemaKeyT, JsonSchemaMode], JsonSchemaValue], JsonSchemaValue]:
    """Generate a JSON schema including definitions from multiple type adapters.

    Args:
        inputs: Inputs to schema generation. The first two items will form the keys of the (first)
            output mapping; the type adapters will provide the core schemas that get converted into
            definitions in the output JSON schema.
        by_alias: Whether to use alias names.
        title: The title for the schema.
        description: The description for the schema.
        ref_template: The format string used for generating $ref strings.
        union_format: The format to use when combining schemas from unions together. Can be one of:

            - `'any_of'`: Use the [`anyOf`](https://json-schema.org/understanding-json-schema/reference/combining#anyOf)
            keyword to combine schemas (the default).
            - `'primitive_type_array'`: Use the [`type`](https://json-schema.org/understanding-json-schema/reference/type)
            keyword as an array of strings, containing each type of the combination. If any of the schemas is not a primitive
            type (`string`, `boolean`, `null`, `integer` or `number`) or contains constraints/metadata, falls back to
            `any_of`.
        schema_generator: The generator class used for creating the schema.

    Returns:
        A tuple where:

            - The first element is a dictionary whose keys are tuples of JSON schema key type and JSON mode, and
                whose values are the JSON schema corresponding to that pair of inputs. (These schemas may have
                JsonRef references to definitions that are defined in the second returned element.)
            - The second element is a JSON schema containing all definitions referenced in the first returned
                element, along with the optional title and description keys.

    """
    schema_generator_instance = schema_generator(
        by_alias=by_alias, ref_template=ref_template, union_format=union_format
    )

    inputs_ = []
    for key, mode, adapter in inputs:
        # This is the same pattern we follow for model json schemas - we attempt a core schema rebuild if we detect a mock
        if isinstance(adapter.core_schema, _mock_val_ser.MockCoreSchema):
            adapter.core_schema.rebuild()
            assert not isinstance(adapter.core_schema, _mock_val_ser.MockCoreSchema), (
                'this is a bug! please report it'
            )
        inputs_.append((key, mode, adapter.core_schema))

    json_schemas_map, definitions = schema_generator_instance.generate_definitions(inputs_)

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
