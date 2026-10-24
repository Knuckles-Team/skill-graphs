##  `timezone_aware`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#timezone_aware)
This error is raised when the `datetime` value provided for a timezone-aware `datetime` field doesn't have timezone information:
```
from datetime import datetime

from pydantic import AwareDatetime, BaseModel, ValidationError


class Model(BaseModel):
    x: AwareDatetime


try:
    Model(x=datetime.now())
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'timezone_aware'

```
