##  ArgsKwargs [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ArgsKwargs)
```
ArgsKwargs(
    args: [, ...],
    kwargs: [, ] | None = None,
)

```

A construct used to store arguments and keyword arguments for a function call.
This data structure is generally used to store information for core schemas associated with functions (like in an arguments schema). This data structure is also currently used for some validation against dataclasses.
Example
```
from pydantic.dataclasses import dataclass
from pydantic import model_validator


@dataclass
class Model:
    a: int
    b: int

    @model_validator(mode="before")
    @classmethod
    def no_op_validator(cls, values):
        print(values)
        return values

Model(1, b=2)
#> ArgsKwargs((1,), {"b": 2})

Model(1, 2)
#> ArgsKwargs((1, 2), {})

Model(a=1, b=2)
#> ArgsKwargs((), {"a": 1, "b": 2})

```

Parameters:
Name | Type | Description | Default
---|---|---|---
`args` |  |  The arguments (inherently ordered) for a function call. |  _required_
`kwargs` |  |  The keyword arguments for a function call |  `None`
###  args `property` [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ArgsKwargs.args)
```
args: [, ...]

```

The arguments (inherently ordered) for a function call.
###  kwargs `property` [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ArgsKwargs.kwargs)
```
kwargs: [, ] | None

```

The keyword arguments for a function call.
