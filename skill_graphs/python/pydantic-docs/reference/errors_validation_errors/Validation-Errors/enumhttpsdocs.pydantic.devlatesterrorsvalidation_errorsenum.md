##  `enum`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#enum)
This error is raised when the input value does not exist in an `enum` field members:
```
from enum import Enum

from pydantic import BaseModel, ValidationError


class MyEnum(str, Enum):
    option = 'option'


class Model(BaseModel):
    x: MyEnum


try:
    Model(x='other_option')
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'enum'

```
