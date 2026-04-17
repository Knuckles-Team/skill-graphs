##  ErrorTypeInfo [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ErrorTypeInfo)
Bases:
Gives information about errors.
###  type `instance-attribute` [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ErrorTypeInfo.type)
```
type: ErrorType

```

The type of error that occurred, this should be a "slug" identifier that changes rarely or never.
###  message_template_python `instance-attribute` [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ErrorTypeInfo.message_template_python)
```
message_template_python:

```

String template to render a human readable error message from using context, when the input is Python.
###  example_message_python `instance-attribute` [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ErrorTypeInfo.example_message_python)
```
example_message_python:

```

Example of a human readable error message, when the input is Python.
###  message_template_json `instance-attribute` [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ErrorTypeInfo.message_template_json)
```
message_template_json: []

```

String template to render a human readable error message from using context, when the input is JSON data.
###  example_message_json `instance-attribute` [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ErrorTypeInfo.example_message_json)
```
example_message_json: []

```

Example of a human readable error message, when the input is JSON data.
###  example_context `instance-attribute` [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ErrorTypeInfo.example_context)
```
example_context: [, ] | None

```

Example of context values.
