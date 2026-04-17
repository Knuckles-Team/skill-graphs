##  `greater_than`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#greater_than)
This error is raised when the value is not greater than the field's `gt` constraint:
```
from pydantic import BaseModel, Field, ValidationError


class Model(BaseModel):
    x: int = Field(gt=10)


try:
    Model(x=10)
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'greater_than'

```
