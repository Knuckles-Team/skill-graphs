##  `time_parsing`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#time_parsing)
This error is raised when the input value is a string that cannot be parsed for a `time` field:
```
from datetime import time

from pydantic import BaseModel, ValidationError


class Model(BaseModel):
    x: time


try:
    Model(x='25:20:30.400')
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'time_parsing'

```
