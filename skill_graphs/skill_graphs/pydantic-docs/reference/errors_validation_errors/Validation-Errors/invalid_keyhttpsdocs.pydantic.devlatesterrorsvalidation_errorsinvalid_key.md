##  `invalid_key`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#invalid_key)
This error is raised when attempting to validate a `dict` that has a key that is not an instance of `str`:
```
from pydantic import BaseModel, ConfigDict, ValidationError


class Model(BaseModel):
    x: int

    model_config = ConfigDict(extra='allow')


try:
    Model.model_validate({'x': 1, b'y': 2})
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'invalid_key'

```
