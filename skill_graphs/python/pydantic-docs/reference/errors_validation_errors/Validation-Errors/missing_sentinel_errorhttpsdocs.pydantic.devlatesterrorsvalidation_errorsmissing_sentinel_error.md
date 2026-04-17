##  `missing_sentinel_error`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#missing_sentinel_error)
This error is raised when the experimental `MISSING` sentinel is the only value allowed, and wasn't provided during validation:
```
from pydantic import BaseModel, ValidationError
from pydantic.experimental.missing_sentinel import MISSING


class Model(BaseModel):
    f: MISSING


try:
    Model(f=1)
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'missing_sentinel_error'

```
