##  `datetime_future`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#datetime_future)
This error is raised when the value provided for a `FutureDatetime` field is not in the future:
```
from datetime import datetime

from pydantic import BaseModel, FutureDatetime, ValidationError


class Model(BaseModel):
    x: FutureDatetime


try:
    Model(x=datetime(2000, 1, 1))
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'datetime_future'

```
