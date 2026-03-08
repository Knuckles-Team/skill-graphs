##  `datetime_parsing`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#datetime_parsing)
This error is raised when the value is a string that cannot be parsed for a `datetime` field:
```
import json
from datetime import datetime

from pydantic import BaseModel, Field, ValidationError


class Model(BaseModel):
    x: datetime = Field(strict=True)


try:
    Model.model_validate_json(json.dumps({'x': 'not a datetime'}))
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'datetime_parsing'

```
