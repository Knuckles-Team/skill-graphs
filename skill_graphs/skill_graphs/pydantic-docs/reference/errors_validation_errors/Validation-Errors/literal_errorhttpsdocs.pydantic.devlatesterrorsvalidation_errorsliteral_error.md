##  `literal_error`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#literal_error)
This error is raised when the input value is not one of the expected literal values:
```
from typing import Literal

from pydantic import BaseModel, ValidationError


class Model(BaseModel):
    x: Literal['a', 'b']


Model(x='a')  # OK

try:
    Model(x='c')
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'literal_error'

```
