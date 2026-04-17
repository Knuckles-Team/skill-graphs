##  `missing`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#missing)
This error is raised when there are required fields missing from the input value:
```
from pydantic import BaseModel, ValidationError


class Model(BaseModel):
    x: str


try:
    Model()
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'missing'

```
