##  `date_past`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#date_past)
This error is raised when the value provided for a `PastDate` field is not in the past:
```
from datetime import date, timedelta

from pydantic import BaseModel, PastDate, ValidationError


class Model(BaseModel):
    x: PastDate


try:
    Model(x=date.today() + timedelta(1))
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'date_past'

```
