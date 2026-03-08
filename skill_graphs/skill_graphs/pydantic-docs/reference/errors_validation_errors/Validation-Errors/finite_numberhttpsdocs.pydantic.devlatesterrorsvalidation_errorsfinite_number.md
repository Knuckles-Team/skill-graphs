##  `finite_number`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#finite_number)
This error is raised when the value is infinite, or too large to be represented as a 64-bit floating point number during validation:
```
from pydantic import BaseModel, ValidationError


class Model(BaseModel):
    x: int


try:
    Model(x=2.2250738585072011e308)
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'finite_number'

```
