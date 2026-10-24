##  `iterable_type`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#iterable_type)
This error is raised when the input value is not valid as an `Iterable`:
```
from collections.abc import Iterable

from pydantic import BaseModel, ValidationError


class Model(BaseModel):
    y: Iterable[str]


try:
    Model(y=123)
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'iterable_type'

```
