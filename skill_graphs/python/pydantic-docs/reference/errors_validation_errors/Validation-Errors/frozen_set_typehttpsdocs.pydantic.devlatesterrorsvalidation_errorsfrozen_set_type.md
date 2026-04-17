##  `frozen_set_type`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#frozen_set_type)
This error is raised when the input value's type is not valid for a `frozenset` field:
```
from pydantic import BaseModel, ValidationError


class Model(BaseModel):
    x: frozenset


try:
    model = Model(x='test')
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'frozen_set_type'

```
