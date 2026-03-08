##  `less_than_equal`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#less_than_equal)
This error is raised when the input value is not less than or equal to the field's `le` constraint:
```
from pydantic import BaseModel, Field, ValidationError


class Model(BaseModel):
    x: int = Field(le=10)


try:
    Model(x=11)
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'less_than_equal'

```
