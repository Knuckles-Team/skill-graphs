##  InitErrorDetails [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.InitErrorDetails)
Bases:
###  type `instance-attribute` [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.InitErrorDetails.type)
```
type:  | PydanticCustomError[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.PydanticCustomError)

```

The type of error that occurred, this should be a "slug" identifier that changes rarely or never.
###  loc `instance-attribute` [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.InitErrorDetails.loc)
```
loc: [[ | , ...]]

```

Tuple of strings and ints identifying where in the schema the error occurred.
###  input `instance-attribute` [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.InitErrorDetails.input)
```
input:

```

The input data at this `loc` that caused the error.
###  ctx `instance-attribute` [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.InitErrorDetails.ctx)
```
ctx: [[, ]]

```

Values which are required to render the error message, and could hence be useful in rendering custom error messages. Also useful for passing custom error data forward.
