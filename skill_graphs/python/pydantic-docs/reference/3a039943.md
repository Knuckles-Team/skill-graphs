##  `float_parsing`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#float_parsing)
This error is raised when the value is a string that can't be parsed as a `float`:
```
from pydantic import BaseModel, ValidationError


class Model(BaseModel):
    x: float


try:
    Model(x='test')
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'float_parsing'

```
