##  `arguments_type`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#arguments_type)
This error is raised when an object that would be passed as arguments to a function during validation is not a `tuple`, `list`, or `dict`. Because `NamedTuple` uses function calls in its implementation, that is one way to produce this error:
```
from typing import NamedTuple

from pydantic import BaseModel, ValidationError


class MyNamedTuple(NamedTuple):
    x: int


class MyModel(BaseModel):
    field: MyNamedTuple


try:
    MyModel.model_validate({'field': 'invalid'})
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'arguments_type'

```
