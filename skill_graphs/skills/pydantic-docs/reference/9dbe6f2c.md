##  `value_error`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#value_error)
This error is raised when a `ValueError` is raised during validation:
```
from pydantic import BaseModel, ValidationError, field_validator


class Model(BaseModel):
    x: str

    @field_validator('x')
    @classmethod
    def repeat_b(cls, v):
        raise ValueError()


try:
    Model(x='test')
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'value_error'

```

Was this page helpful?
Thanks for your feedback!
Thanks for your feedback!
Made with
