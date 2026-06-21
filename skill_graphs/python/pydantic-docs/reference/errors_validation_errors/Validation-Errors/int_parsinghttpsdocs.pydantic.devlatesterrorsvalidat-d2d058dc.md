##  `int_parsing`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#int_parsing)
This error is raised when the value can't be parsed as `int`:
```
from pydantic import BaseModel, ValidationError


class Model(BaseModel):
    x: int


try:
    Model(x='test')
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'int_parsing'

```
