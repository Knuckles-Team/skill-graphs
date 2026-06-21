##  `timezone_naive`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#timezone_naive)
This error is raised when the `datetime` value provided for a timezone-naive `datetime` field has timezone info:
```
from datetime import datetime, timezone

from pydantic import BaseModel, NaiveDatetime, ValidationError


class Model(BaseModel):
    x: NaiveDatetime


try:
    Model(x=datetime.now(tz=timezone.utc))
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'timezone_naive'

```
