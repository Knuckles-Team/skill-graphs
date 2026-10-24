##  `get_attribute_error`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#get_attribute_error)
This error is raised when `model_config['from_attributes'] == True` and an error is raised while reading the attributes:
```
from pydantic import BaseModel, ConfigDict, ValidationError


class Foobar:
    def __init__(self):
        self.x = 1

    @property
    def y(self):
        raise RuntimeError('intentional error')


class Model(BaseModel):
    x: int
    y: str

    model_config = ConfigDict(from_attributes=True)


try:
    Model.model_validate(Foobar())
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'get_attribute_error'

```
