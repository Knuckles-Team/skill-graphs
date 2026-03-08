##  `string_unicode`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#string_unicode)
This error is raised when the value cannot be parsed as a Unicode string:
```
from pydantic import BaseModel, ValidationError


class Model(BaseModel):
    x: str


try:
    Model(x=b'\x81')
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'string_unicode'

```
