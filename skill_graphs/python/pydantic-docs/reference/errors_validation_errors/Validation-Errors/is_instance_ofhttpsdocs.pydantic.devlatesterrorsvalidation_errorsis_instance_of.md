##  `is_instance_of`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#is_instance_of)
This error is raised when the input value is not an instance of the expected type:
```
from pydantic import BaseModel, ConfigDict, ValidationError


class Nested:
    x: str


class Model(BaseModel):
    y: Nested

    model_config = ConfigDict(arbitrary_types_allowed=True)


try:
    Model(y='test')
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'is_instance_of'

```
