##  `time_type`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#time_type)
This error is raised when the value type is not valid for a `time` field:
```
from datetime import time

from pydantic import BaseModel, ValidationError


class Model(BaseModel):
    x: time


try:
    Model(x=None)
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'time_type'

```

This error is also raised for strict fields when the input value is not an instance of `time`.
