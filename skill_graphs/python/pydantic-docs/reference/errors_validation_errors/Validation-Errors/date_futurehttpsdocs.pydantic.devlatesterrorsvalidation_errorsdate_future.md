##  `date_future`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#date_future)
This error is raised when the input value provided for a `FutureDate` field is not in the future:
```
from datetime import date

from pydantic import BaseModel, FutureDate, ValidationError


class Model(BaseModel):
    x: FutureDate


try:
    Model(x=date(2000, 1, 1))
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'date_future'

```
