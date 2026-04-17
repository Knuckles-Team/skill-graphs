##  `int_from_float`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#int_from_float)
This error is raised when you provide a `float` value for an `int` field:
```
from pydantic import BaseModel, ValidationError


class Model(BaseModel):
    x: int


try:
    Model(x=0.5)
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'int_from_float'

```
