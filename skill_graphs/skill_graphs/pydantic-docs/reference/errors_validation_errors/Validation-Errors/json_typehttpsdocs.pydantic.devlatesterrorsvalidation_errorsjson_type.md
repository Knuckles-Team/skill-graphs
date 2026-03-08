##  `json_type`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#json_type)
This error is raised when the input value is of a type that cannot be parsed as JSON:
```
from pydantic import BaseModel, Json, ValidationError


class Model(BaseModel):
    x: Json


try:
    Model(x=None)
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'json_type'

```
