##  `time_delta_parsing`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#time_delta_parsing)
This error is raised when the input value is a string that cannot be parsed for a `timedelta` field:
```
from datetime import timedelta

from pydantic import BaseModel, ValidationError


class Model(BaseModel):
    x: timedelta


try:
    Model(x='t')
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'time_delta_parsing'

```
