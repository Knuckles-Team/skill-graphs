##  `greater_than_equal`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#greater_than_equal)
This error is raised when the value is not greater than or equal to the field's `ge` constraint:
```
from pydantic import BaseModel, Field, ValidationError


class Model(BaseModel):
    x: int = Field(ge=10)


try:
    Model(x=9)
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'greater_than_equal'

```
