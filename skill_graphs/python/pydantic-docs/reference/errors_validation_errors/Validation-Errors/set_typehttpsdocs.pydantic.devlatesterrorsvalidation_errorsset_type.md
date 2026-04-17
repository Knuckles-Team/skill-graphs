##  `set_type`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#set_type)
This error is raised when the value type is not valid for a `set` field:
```
from pydantic import BaseModel, ValidationError


class Model(BaseModel):
    x: set[int]


try:
    Model(x='test')
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'set_type'

```
