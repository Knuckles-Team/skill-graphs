##  `float_type`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#float_type)
This error is raised when the input value's type is not valid for a `float` field:
```
from pydantic import BaseModel, ValidationError


class Model(BaseModel):
    x: float


try:
    Model(x=None)
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'float_type'

```
