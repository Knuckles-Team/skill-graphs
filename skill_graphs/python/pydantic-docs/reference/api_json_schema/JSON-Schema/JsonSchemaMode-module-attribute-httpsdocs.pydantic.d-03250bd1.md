##  JsonSchemaMode `module-attribute` [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaMode)
```
JsonSchemaMode = ['validation', 'serialization']

```

A type alias that represents the mode of a JSON schema; either 'validation' or 'serialization'.
For some types, the inputs to validation differ from the outputs of serialization. For example, computed fields will only be present when serializing, and should not be provided when validating. This flag provides a way to indicate whether you want the JSON schema required for validation inputs, or that will be matched by serialization outputs.
