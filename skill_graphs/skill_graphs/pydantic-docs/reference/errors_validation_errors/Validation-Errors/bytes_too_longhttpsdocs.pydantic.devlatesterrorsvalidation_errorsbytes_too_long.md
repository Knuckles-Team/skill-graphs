##  `bytes_too_long`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#bytes_too_long)
This error is raised when the length of a `bytes` value is greater than the field's `max_length` constraint:
```
from pydantic import BaseModel, Field, ValidationError


class Model(BaseModel):
    x: bytes = Field(max_length=3)


try:
    Model(x=b'test')
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'bytes_too_long'

```
