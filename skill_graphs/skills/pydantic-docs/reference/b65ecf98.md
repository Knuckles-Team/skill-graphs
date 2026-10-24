##  PydanticCustomError [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.PydanticCustomError)
```
PydanticCustomError(
    error_type: ,
    message_template: ,
    context: [, ] | None = None,
)

```

Bases:
A custom exception providing flexible error handling for Pydantic validators.
You can raise this error in custom validators when you'd like flexibility in regards to the error type, message, and context.
Example
```
from pydantic_core import PydanticCustomError

def custom_validator(v) -> None:
    if v <= 10:
        raise PydanticCustomError('custom_value_error', 'Value must be greater than {value}', {'value': 10, 'extra_context': 'extra_data'})
    return v

```

Parameters:
Name | Type | Description | Default
---|---|---|---
`error_type` |  |  The error type. |  _required_
`message_template` |  |  The message template. |  _required_
`context` |  |  The data to inject into the message template. |  `None`
###  context `property` [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.PydanticCustomError.context)
```
context: [, ] | None

```

Values which are required to render the error message, and could hence be useful in passing error data forward.
###  type `property` [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.PydanticCustomError.type)
```
type:

```

The error type associated with the error. For consistency with Pydantic, this is typically a snake_case string.
###  message_template `property` [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.PydanticCustomError.message_template)
```
message_template:

```

The message template associated with the error. This is a string that can be formatted with context variables in `{curly_braces}`.
###  message [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.PydanticCustomError.message)
```
message() ->

```

The formatted message associated with the error. This presents as the message template with context variables appropriately injected.
