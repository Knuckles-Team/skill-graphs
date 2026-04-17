##  `datetime_from_date_parsing`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#datetime_from_date_parsing)
This error is raised when the input value is a string that cannot be parsed for a `datetime` field:
```
from datetime import datetime

from pydantic import BaseModel, ValidationError


class Model(BaseModel):
    x: datetime


try:
    # there is no 13th month
    Model(x='2023-13-01')
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'datetime_from_date_parsing'

```
