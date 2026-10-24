##  `multiple_of`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#multiple_of)
This error is raised when the input is not a multiple of a field's `multiple_of` constraint:
```
from pydantic import BaseModel, Field, ValidationError


class Model(BaseModel):
    x: int = Field(multiple_of=5)


try:
    Model(x=1)
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'multiple_of'

```
