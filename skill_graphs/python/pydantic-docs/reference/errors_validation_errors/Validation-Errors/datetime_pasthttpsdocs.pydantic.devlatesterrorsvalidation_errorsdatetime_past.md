##  `datetime_past`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#datetime_past)
This error is raised when the value provided for a `PastDatetime` field is not in the past:
```
from datetime import datetime, timedelta

from pydantic import BaseModel, PastDatetime, ValidationError


class Model(BaseModel):
    x: PastDatetime


try:
    Model(x=datetime.now() + timedelta(100))
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'datetime_past'

```
