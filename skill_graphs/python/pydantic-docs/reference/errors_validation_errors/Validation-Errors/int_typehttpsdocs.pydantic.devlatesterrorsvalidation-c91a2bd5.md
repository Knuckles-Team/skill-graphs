##  `int_type`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#int_type)
This error is raised when the input value's type is not valid for an `int` field:
```
from pydantic import BaseModel, ValidationError


class Model(BaseModel):
    x: int


try:
    Model(x=None)
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'int_type'

```
