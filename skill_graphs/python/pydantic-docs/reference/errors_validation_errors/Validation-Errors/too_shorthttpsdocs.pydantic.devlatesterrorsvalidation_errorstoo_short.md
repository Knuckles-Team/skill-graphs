##  `too_short`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#too_short)
This error is raised when the value length is less than the field's `min_length` constraint:
```
from pydantic import BaseModel, Field, ValidationError


class Model(BaseModel):
    x: list[int] = Field(min_length=3)


try:
    Model(x=[1, 2])
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'too_short'

```
