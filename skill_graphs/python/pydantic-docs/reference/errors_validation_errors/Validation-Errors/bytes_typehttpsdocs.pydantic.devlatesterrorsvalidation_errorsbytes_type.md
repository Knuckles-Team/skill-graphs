##  `bytes_type`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#bytes_type)
This error is raised when the input value's type is not valid for a `bytes` field:
```
from pydantic import BaseModel, ValidationError


class Model(BaseModel):
    x: bytes


try:
    Model(x=123)
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'bytes_type'

```

This error is also raised for strict fields when the input value is not an instance of `bytes`.
