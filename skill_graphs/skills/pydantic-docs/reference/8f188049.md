##  `dict_type`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#dict_type)
This error is raised when the input value's type is not `dict` for a `dict` field:
```
from pydantic import BaseModel, ValidationError


class Model(BaseModel):
    x: dict


try:
    Model(x=['1', '2'])
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'dict_type'

```
