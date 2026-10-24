##  `iteration_error`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#iteration_error)
This error is raised when an error occurs during iteration:
```
from pydantic import BaseModel, ValidationError


def gen():
    yield 1
    raise RuntimeError('error')


class Model(BaseModel):
    x: list[int]


try:
    Model(x=gen())
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'iteration_error'

```
