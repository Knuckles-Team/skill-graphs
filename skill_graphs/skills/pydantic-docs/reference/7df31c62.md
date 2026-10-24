##  `complex_type`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#complex_type)
This error is raised when the input value cannot be interpreted as a complex number:
```
from pydantic import BaseModel, ValidationError


class Model(BaseModel):
    num: complex


try:
    Model(num=False)
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'complex_type'

```
