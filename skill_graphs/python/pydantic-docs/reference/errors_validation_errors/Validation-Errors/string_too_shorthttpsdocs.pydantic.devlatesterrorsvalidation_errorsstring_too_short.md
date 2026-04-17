##  `string_too_short`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#string_too_short)
This error is raised when the input value is a string whose length is less than the field's `min_length` constraint:
```
from pydantic import BaseModel, Field, ValidationError


class Model(BaseModel):
    x: str = Field(min_length=3)


try:
    Model(x='t')
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'string_too_short'

```
