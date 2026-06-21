##  `default_factory_not_called`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#default_factory_not_called)
This error is raised when a [default factory taking validated data](https://docs.pydantic.dev/latest/concepts/fields/#default-factory-validated-data) can't be called, because validation failed on previous fields:
```
from pydantic import BaseModel, Field, ValidationError


class Model(BaseModel):
    a: int = Field(gt=10)
    b: int = Field(default_factory=lambda data: data['a'])


try:
    Model(a=1)
except ValidationError as exc:
    print(exc)
    """
    2 validation errors for Model
    a
      Input should be greater than 10 [type=greater_than, input_value=1, input_type=int]
    b
      The default factory uses validated data, but at least one validation error occurred [type=default_factory_not_called]
    """
    print(repr(exc.errors()[1]['type']))
    #> 'default_factory_not_called'

```
