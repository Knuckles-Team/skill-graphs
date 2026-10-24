##  `frozen_field`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#frozen_field)
This error is raised when you attempt to assign a value to a field with `frozen=True`, or to delete such a field:
```
from pydantic import BaseModel, Field, ValidationError


class Model(BaseModel):
    x: str = Field('test', frozen=True)


model = Model()

try:
    model.x = 'test1'
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'frozen_field'

try:
    del model.x
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'frozen_field'

```
