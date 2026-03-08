##  ErrorDetails [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ErrorDetails)
Bases:
###  type `instance-attribute` [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ErrorDetails.type)
```
type:

```

The type of error that occurred, this is an identifier designed for programmatic use that will change rarely or never.
`type` is unique for each error message, and can hence be used as an identifier to build custom error messages.
###  loc `instance-attribute` [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ErrorDetails.loc)
```
loc: [ | , ...]

```

Tuple of strings and ints identifying where in the schema the error occurred.
###  msg `instance-attribute` [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ErrorDetails.msg)
```
msg:

```

A human readable error message.
###  input `instance-attribute` [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ErrorDetails.input)
```
input:

```

The input data at this `loc` that caused the error.
###  ctx `instance-attribute` [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ErrorDetails.ctx)
```
ctx: [[, ]]

```

Values which are required to render the error message, and could hence be useful in rendering custom error messages. Also useful for passing custom error data forward.
###  url `instance-attribute` [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ErrorDetails.url)
```
url: []

```

The documentation URL giving information about the error. No URL is available if a [`PydanticCustomError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.PydanticCustomError) is used.
