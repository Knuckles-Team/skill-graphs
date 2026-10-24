##  `list_type`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#list_type)
This error is raised when the input value's type is not valid for a `list` field:
```
from pydantic import BaseModel, ValidationError


class Model(BaseModel):
    x: list[int]


try:
    Model(x=1)
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'list_type'

```
