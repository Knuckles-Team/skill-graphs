##  `json_invalid`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#json_invalid)
This error is raised when the input value is not a valid JSON string:
```
from pydantic import BaseModel, Json, ValidationError


class Model(BaseModel):
    x: Json


try:
    Model(x='test')
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'json_invalid'

```
