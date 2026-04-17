##  `none_required`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#none_required)
This error is raised when the input value is not `None` for a field that requires `None`:
```
from pydantic import BaseModel, ValidationError


class Model(BaseModel):
    x: None


try:
    Model(x=1)
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'none_required'

```

Note
You may encounter this error when there is a naming collision in your model between a field name and its type. More specifically, this error is likely to be thrown when the default value of that field is `None`.
For example, the following would yield the `none_required` validation error since the field `int` is set to a default value of `None` and has the exact same name as its type, which causes problems with validation.
```
from typing import Optional

from pydantic import BaseModel


class M1(BaseModel):
    int: Optional[int] = None


m = M1(int=123)  # errors

```
