##  `less_than`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#less_than)
This error is raised when the input value is not less than the field's `lt` constraint:
```
from pydantic import BaseModel, Field, ValidationError


class Model(BaseModel):
    x: int = Field(lt=10)


try:
    Model(x=10)
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'less_than'

```
