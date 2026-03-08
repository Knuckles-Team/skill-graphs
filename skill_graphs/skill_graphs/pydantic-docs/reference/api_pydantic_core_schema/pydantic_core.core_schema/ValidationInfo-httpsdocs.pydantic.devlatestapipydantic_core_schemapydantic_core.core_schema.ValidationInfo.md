##  ValidationInfo [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.ValidationInfo)
Bases: `ContextT]`
Extra data used during validation.
###  context `property` [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.ValidationInfo.context)
```
context: ContextT

```

The current validation context.
###  config `property` [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.ValidationInfo.config)
```
config: CoreConfig[](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.CoreConfig) | None

```

The CoreConfig that applies to this validation.
###  mode `property` [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.ValidationInfo.mode)
```
mode: ['python', 'json']

```

The type of input data we are currently validating.
###  data `property` [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.ValidationInfo.data)
```
data: [, ]

```

The data being validated for this model.
###  field_name `property` [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.ValidationInfo.field_name)
```
field_name:  | None

```

The name of the current field being validated if this validator is attached to a model field.
