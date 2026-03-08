##  `time_delta_type`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#time_delta_type)
This error is raised when the input value's type is not valid for a `timedelta` field:
```
from datetime import timedelta

from pydantic import BaseModel, ValidationError


class Model(BaseModel):
    x: timedelta


try:
    Model(x=None)
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'time_delta_type'

```

This error is also raised for strict fields when the input value is not an instance of `timedelta`.
