##  ValidationError [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError)
Bases:
`ValidationError` is the exception raised by `pydantic-core` when validation fails, it contains a list of errors which detail why validation failed.
###  title `property` [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError.title)
```
title:

```

The title of the error, as used in the heading of `str(validation_error)`.
###  from_exception_data `classmethod` [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError.from_exception_data)
```
from_exception_data(
    title: ,
    line_errors: [InitErrorDetails[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.InitErrorDetails)],
    input_type: ["python", "json"] = "python",
    hide_input:  = False,
) ->

```

Python constructor for a Validation Error.
Parameters:
Name | Type | Description | Default
---|---|---|---
`title` |  |  The title of the error, as used in the heading of `str(validation_error)` |  _required_
`line_errors` |  `InitErrorDetails[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.InitErrorDetails)]` |  A list of [`InitErrorDetails`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.InitErrorDetails) which contain information about errors that occurred during validation. |  _required_
`input_type` |  |  Whether the error is for a Python object or JSON. |  `'python'`
`hide_input` |  |  Whether to hide the input value in the error message. |  `False`
###  error_count [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError.error_count)
```
error_count() ->

```

Returns:
Type | Description
---|---
|  The number of errors in the validation error.
###  errors [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError.errors)
```
errors(
    *,
    include_url:  = True,
    include_context:  = True,
    include_input:  = True
) -> [ErrorDetails[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ErrorDetails)]

```

Details about each error in the validation error.
Parameters:
Name | Type | Description | Default
---|---|---|---
`include_url` |  |  Whether to include a URL to documentation on the error each error. |  `True`
`include_context` |  |  Whether to include the context of each error. |  `True`
`include_input` |  |  Whether to include the input value of each error. |  `True`
Returns:
Type | Description
---|---
`ErrorDetails[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ErrorDetails)]` |  A list of [`ErrorDetails`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ErrorDetails) for each error in the validation error.
###  json [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError.json)
```
json(
    *,
    indent:  | None = None,
    include_url:  = True,
    include_context:  = True,
    include_input:  = True
) ->

```

Same as [`errors()`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError.errors) but returns a JSON string.
Parameters:
Name | Type | Description | Default
---|---|---|---
`indent` |  |  The number of spaces to indent the JSON by, or `None` for no indentation - compact JSON. |  `None`
`include_url` |  |  Whether to include a URL to documentation on the error each error. |  `True`
`include_context` |  |  Whether to include the context of each error. |  `True`
`include_input` |  |  Whether to include the input value of each error. |  `True`
Returns:
Type | Description
---|---
|  a JSON string.
