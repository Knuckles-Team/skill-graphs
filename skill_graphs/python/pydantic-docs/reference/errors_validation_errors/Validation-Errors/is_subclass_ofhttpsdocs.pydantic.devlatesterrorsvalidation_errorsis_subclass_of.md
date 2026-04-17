##  `is_subclass_of`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#is_subclass_of)
This error is raised when the input value is not a subclass of the expected type:
```
from pydantic import BaseModel, ValidationError


class Nested:
    x: str


class Model(BaseModel):
    y: type[Nested]


try:
    Model(y='test')
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'is_subclass_of'

```
