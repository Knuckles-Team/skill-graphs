##  PydanticKnownError [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.PydanticKnownError)
```
PydanticKnownError(
    error_type: ErrorType,
    context: [, ] | None = None,
)

```

Bases:
A helper class for raising exceptions that mimic Pydantic's built-in exceptions, with more flexibility in regards to context.
Unlike [`PydanticCustomError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.PydanticCustomError), the `error_type` argument must be a known `ErrorType`.
Example
```
from pydantic_core import PydanticKnownError

def custom_validator(v) -> None:
    if v <= 10:
        raise PydanticKnownError('greater_than', {'gt': 10})
    return v

```

Parameters:
Name | Type | Description | Default
---|---|---|---
`error_type` |  `ErrorType` |  The error type. |  _required_
`context` |  |  The data to inject into the message template. |  `None`
###  context `property` [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.PydanticKnownError.context)
```
context: [, ] | None

```

Values which are required to render the error message, and could hence be useful in passing error data forward.
###  type `property` [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.PydanticKnownError.type)
```
type: ErrorType

```

The type of the error.
###  message_template `property` [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.PydanticKnownError.message_template)
```
message_template:

```

The message template associated with the provided error type. This is a string that can be formatted with context variables in `{curly_braces}`.
###  message [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.PydanticKnownError.message)
```
message() ->

```

The formatted message associated with the error. This presents as the message template with context variables appropriately injected.
