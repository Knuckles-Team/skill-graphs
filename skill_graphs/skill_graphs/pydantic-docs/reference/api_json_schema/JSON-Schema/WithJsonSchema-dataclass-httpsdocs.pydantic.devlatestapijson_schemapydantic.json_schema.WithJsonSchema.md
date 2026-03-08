##  WithJsonSchema `dataclass` [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.WithJsonSchema)
```
WithJsonSchema(
    json_schema: JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue) | None,
    mode: (
        ["validation", "serialization"] | None
    ) = None,
)

```

Usage Documentation
[`WithJsonSchema` Annotation](https://docs.pydantic.dev/latest/concepts/json_schema/#withjsonschema-annotation)
Add this as an annotation on a field to override the (base) JSON schema that would be generated for that field. This provides a way to set a JSON schema for types that would otherwise raise errors when producing a JSON schema, such as Callable, or types that have an is-instance core schema, without needing to go so far as creating a custom subclass of pydantic.json_schema.GenerateJsonSchema. Note that any _modifications_ to the schema that would normally be made (such as setting the title for model fields) will still be performed.
If `mode` is set this will only apply to that schema generation mode, allowing you to set different json schemas for validation and serialization.
