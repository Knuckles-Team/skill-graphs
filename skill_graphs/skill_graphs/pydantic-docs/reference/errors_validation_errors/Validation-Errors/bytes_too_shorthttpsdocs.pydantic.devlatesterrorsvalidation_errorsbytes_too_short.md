##  `bytes_too_short`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#bytes_too_short)
This error is raised when the length of a `bytes` value is less than the field's `min_length` constraint:
```
from pydantic import BaseModel, Field, ValidationError


class Model(BaseModel):
    x: bytes = Field(min_length=3)


try:
    Model(x=b't')
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'bytes_too_short'

```
