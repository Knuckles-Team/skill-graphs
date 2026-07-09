##  `bool_type`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#bool_type)
This error is raised when the input value's type is not valid for a `bool` field:
```
from pydantic import BaseModel, ValidationError


class Model(BaseModel):
    x: bool


try:
    Model(x=None)
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'bool_type'

```

This error is also raised for strict fields when the input value is not an instance of `bool`.
