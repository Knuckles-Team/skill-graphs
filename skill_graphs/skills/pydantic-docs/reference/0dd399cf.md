##  SchemaValidator [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.SchemaValidator)
```
SchemaValidator(
    schema: CoreSchema, config: CoreConfig[](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.CoreConfig) | None = None
)

```

`SchemaValidator` is the Python wrapper for `pydantic-core`'s Rust validation logic, internally it owns one `CombinedValidator` which may in turn own more `CombinedValidator`s which make up the full schema validator.
Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `CoreSchema` |  The `CoreSchema` to use for validation. |  _required_
`config` |  `CoreConfig[](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.CoreConfig) | None` |  Optionally a [`CoreConfig`](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.CoreConfig) to configure validation. |  `None`
###  title `property` [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.SchemaValidator.title)
```
title:

```

The title of the schema, as used in the heading of [`ValidationError.__str__()`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError).
###  validate_python [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.SchemaValidator.validate_python)
```
validate_python(
    input: ,
    *,
    strict:  | None = None,
    extra: ExtraBehavior | None = None,
    from_attributes:  | None = None,
    context:  | None = None,
    self_instance:  | None = None,
    allow_partial: (
         | ["off", "on", "trailing-strings"]
    ) = False,
    by_alias:  | None = None,
    by_name:  | None = None
) ->

```

Validate a Python object against the schema and return the validated object.
Parameters:
Name | Type | Description | Default
---|---|---|---
`input` |  |  The Python object to validate. |  _required_
`strict` |  |  Whether to validate the object in strict mode. If `None`, the value of [`CoreConfig.strict`](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.CoreConfig) is used. |  `None`
`extra` |  `ExtraBehavior | None` |  Whether to ignore, allow, or forbid extra data during model validation. If `None`, the value of [`CoreConfig.extra_fields_behavior`](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.CoreConfig) is used. |  `None`
`from_attributes` |  |  Whether to validate objects as inputs to models by extracting attributes. If `None`, the value of [`CoreConfig.from_attributes`](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.CoreConfig) is used. |  `None`
`context` |  |  The context to use for validation, this is passed to functional validators as [`info.context`](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.ValidationInfo.context). |  `None`
`self_instance` |  |  An instance of a model set attributes on from validation, this is used when running validation from the `__init__` method of a model. |  `None`
`allow_partial` |  |  Whether to allow partial validation; if `True` errors in the last element of sequences and mappings are ignored. `'trailing-strings'` means any final unfinished JSON string is included in the result. |  `False`
`by_alias` |  |  Whether to use the field's alias when validating against the provided input data. |  `None`
`by_name` |  |  Whether to use the field's name when validating against the provided input data. |  `None`
Raises:
Type | Description
---|---
`ValidationError[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError)` |  If validation fails.
|  Other error types maybe raised if internal errors occur.
Returns:
Type | Description
---|---
|  The validated object.
###  isinstance_python [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.SchemaValidator.isinstance_python)
```
isinstance_python(
    input: ,
    *,
    strict:  | None = None,
    extra: ExtraBehavior | None = None,
    from_attributes:  | None = None,
    context:  | None = None,
    self_instance:  | None = None,
    by_alias:  | None = None,
    by_name:  | None = None
) ->

```

Similar to [`validate_python()`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.SchemaValidator.validate_python) but returns a boolean.
Arguments match `validate_python()`. This method will not raise `ValidationError`s but will raise internal errors.
Returns:
Type | Description
---|---
|  `True` if validation succeeds, `False` if validation fails.
###  validate_json [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.SchemaValidator.validate_json)
```
validate_json(
    input:  |  | ,
    *,
    strict:  | None = None,
    extra: ExtraBehavior | None = None,
    context:  | None = None,
    self_instance:  | None = None,
    allow_partial: (
         | ["off", "on", "trailing-strings"]
    ) = False,
    by_alias:  | None = None,
    by_name:  | None = None
) ->

```

Validate JSON data directly against the schema and return the validated Python object.
This method should be significantly faster than `validate_python(json.loads(json_data))` as it avoids the need to create intermediate Python objects
It also handles constructing the correct Python type even in strict mode, where `validate_python(json.loads(json_data))` would fail validation.
Parameters:
Name | Type | Description | Default
---|---|---|---
`input` |  |  The JSON data to validate. |  _required_
`strict` |  |  Whether to validate the object in strict mode. If `None`, the value of [`CoreConfig.strict`](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.CoreConfig) is used. |  `None`
`extra` |  `ExtraBehavior | None` |  Whether to ignore, allow, or forbid extra data during model validation. If `None`, the value of [`CoreConfig.extra_fields_behavior`](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.CoreConfig) is used. |  `None`
`context` |  |  The context to use for validation, this is passed to functional validators as [`info.context`](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.ValidationInfo.context). |  `None`
`self_instance` |  |  An instance of a model set attributes on from validation. |  `None`
`allow_partial` |  |  Whether to allow partial validation; if `True` incomplete JSON will be parsed successfully and errors in the last element of sequences and mappings are ignored. `'trailing-strings'` means any final unfinished JSON string is included in the result. |  `False`
`by_alias` |  |  Whether to use the field's alias when validating against the provided input data. |  `None`
`by_name` |  |  Whether to use the field's name when validating against the provided input data. |  `None`
Raises:
Type | Description
---|---
`ValidationError[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError)` |  If validation fails or if the JSON data is invalid.
|  Other error types maybe raised if internal errors occur.
Returns:
Type | Description
---|---
|  The validated Python object.
###  validate_strings [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.SchemaValidator.validate_strings)
```
validate_strings(
    input: _StringInput,
    *,
    strict:  | None = None,
    extra: ExtraBehavior | None = None,
    context:  | None = None,
    allow_partial: (
         | ["off", "on", "trailing-strings"]
    ) = False,
    by_alias:  | None = None,
    by_name:  | None = None
) ->

```

Validate a string against the schema and return the validated Python object.
This is similar to `validate_json` but applies to scenarios where the input will be a string but not JSON data, e.g. URL fragments, query parameters, etc.
Parameters:
Name | Type | Description | Default
---|---|---|---
`input` |  `_StringInput` |  The input as a string, or bytes/bytearray if `strict=False`. |  _required_
`strict` |  |  Whether to validate the object in strict mode. If `None`, the value of [`CoreConfig.strict`](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.CoreConfig) is used. |  `None`
`extra` |  `ExtraBehavior | None` |  Whether to ignore, allow, or forbid extra data during model validation. If `None`, the value of [`CoreConfig.extra_fields_behavior`](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.CoreConfig) is used. |  `None`
`context` |  |  The context to use for validation, this is passed to functional validators as [`info.context`](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.ValidationInfo.context). |  `None`
`allow_partial` |  |  Whether to allow partial validation; if `True` errors in the last element of sequences and mappings are ignored. `'trailing-strings'` means any final unfinished JSON string is included in the result. |  `False`
`by_alias` |  |  Whether to use the field's alias when validating against the provided input data. |  `None`
`by_name` |  |  Whether to use the field's name when validating against the provided input data. |  `None`
Raises:
Type | Description
---|---
`ValidationError[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError)` |  If validation fails or if the JSON data is invalid.
|  Other error types maybe raised if internal errors occur.
Returns:
Type | Description
---|---
|  The validated Python object.
###  validate_assignment [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.SchemaValidator.validate_assignment)
```
validate_assignment(
    obj: ,
    field_name: ,
    field_value: ,
    *,
    strict:  | None = None,
    extra: ExtraBehavior | None = None,
    from_attributes:  | None = None,
    context:  | None = None,
    by_alias:  | None = None,
    by_name:  | None = None
) -> (
    [, ]
    | [[, ], [, ] | None, []]
)

```

Validate an assignment to a field on a model.
Parameters:
Name | Type | Description | Default
---|---|---|---
`obj` |  |  The model instance being assigned to. |  _required_
`field_name` |  |  The name of the field to validate assignment for. |  _required_
`field_value` |  |  The value to assign to the field. |  _required_
`strict` |  |  Whether to validate the object in strict mode. If `None`, the value of [`CoreConfig.strict`](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.CoreConfig) is used. |  `None`
`extra` |  `ExtraBehavior | None` |  Whether to ignore, allow, or forbid extra data during model validation. If `None`, the value of [`CoreConfig.extra_fields_behavior`](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.CoreConfig) is used. |  `None`
`from_attributes` |  |  Whether to validate objects as inputs to models by extracting attributes. If `None`, the value of [`CoreConfig.from_attributes`](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.CoreConfig) is used. |  `None`
`context` |  |  The context to use for validation, this is passed to functional validators as [`info.context`](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.ValidationInfo.context). |  `None`
`by_alias` |  |  Whether to use the field's alias when validating against the provided input data. |  `None`
`by_name` |  |  Whether to use the field's name when validating against the provided input data. |  `None`
Raises:
Type | Description
---|---
`ValidationError[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError)` |  If validation fails.
|  Other error types maybe raised if internal errors occur.
Returns:
Type | Description
---|---
|  Either the model dict or a tuple of `(model_data, model_extra, fields_set)`
###  get_default_value [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.SchemaValidator.get_default_value)
```
get_default_value(
    *, strict:  | None = None, context:  = None
) -> Some[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.Some) | None

```

Get the default value for the schema, including running default value validation.
Parameters:
Name | Type | Description | Default
---|---|---|---
`strict` |  |  Whether to validate the default value in strict mode. If `None`, the value of [`CoreConfig.strict`](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.CoreConfig) is used. |  `None`
`context` |  |  The context to use for validation, this is passed to functional validators as [`info.context`](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.ValidationInfo.context). |  `None`
Raises:
Type | Description
---|---
`ValidationError[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError)` |  If validation fails.
|  Other error types maybe raised if internal errors occur.
Returns:
Type | Description
---|---
`Some[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.Some) | None` |  `None` if the schema has no default value, otherwise a [`Some`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.Some) containing the default.
