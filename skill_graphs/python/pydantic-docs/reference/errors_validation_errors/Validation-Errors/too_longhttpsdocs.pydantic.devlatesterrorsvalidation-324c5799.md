##  `too_long`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#too_long)
This error is raised when the input value's length is greater than the field's `max_length` constraint:
```
from pydantic import BaseModel, Field, ValidationError


class Model(BaseModel):
    x: list[int] = Field(max_length=3)


try:
    Model(x=[1, 2, 3, 4])
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'too_long'

```
