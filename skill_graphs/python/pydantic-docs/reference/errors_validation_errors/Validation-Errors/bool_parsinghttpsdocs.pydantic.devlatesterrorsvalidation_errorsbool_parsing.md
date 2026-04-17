##  `bool_parsing`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#bool_parsing)
This error is raised when the input value is a string that is not valid for coercion to a boolean:
```
from pydantic import BaseModel, ValidationError


class Model(BaseModel):
    x: bool


Model(x='true')  # OK

try:
    Model(x='test')
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'bool_parsing'

```
