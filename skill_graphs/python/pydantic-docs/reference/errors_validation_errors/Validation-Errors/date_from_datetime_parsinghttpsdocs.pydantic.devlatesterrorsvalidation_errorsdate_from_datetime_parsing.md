##  `date_from_datetime_parsing`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#date_from_datetime_parsing)
This error is raised when the input value is a string that cannot be parsed for a `date` field:
```
from datetime import date

from pydantic import BaseModel, ValidationError


class Model(BaseModel):
    x: date


try:
    Model(x='XX1494012000')
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'date_from_datetime_parsing'

```
