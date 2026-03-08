##  `assertion_error`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#assertion_error)
This error is raised when a failing `assert` statement is encountered during validation:
```
from pydantic import BaseModel, ValidationError, field_validator


class Model(BaseModel):
    x: int

    @field_validator('x')
    @classmethod
    def force_x_positive(cls, v):
        assert v > 0
        return v


try:
    Model(x=-1)
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'assertion_error'

```
