##  `string_type`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#string_type)
This error is raised when the input value's type is not valid for a `str` field:
```
from pydantic import BaseModel, ValidationError


class Model(BaseModel):
    x: str


try:
    Model(x=1)
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'string_type'

```

This error is also raised for strict fields when the input value is not an instance of `str`.
