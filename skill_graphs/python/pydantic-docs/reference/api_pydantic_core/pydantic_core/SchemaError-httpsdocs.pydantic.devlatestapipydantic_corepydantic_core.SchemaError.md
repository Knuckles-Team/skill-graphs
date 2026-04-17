##  SchemaError [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.SchemaError)
Bases:
Information about errors that occur while building a [`SchemaValidator`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.SchemaValidator) or [`SchemaSerializer`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.SchemaSerializer).
###  error_count [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.SchemaError.error_count)
```
error_count() ->

```

Returns:
Type | Description
---|---
|  The number of errors in the schema.
###  errors [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.SchemaError.errors)
```
errors() -> [ErrorDetails[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ErrorDetails)]

```

Returns:
Type | Description
---|---
`ErrorDetails[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ErrorDetails)]` |  A list of [`ErrorDetails`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ErrorDetails) for each error in the schema.
