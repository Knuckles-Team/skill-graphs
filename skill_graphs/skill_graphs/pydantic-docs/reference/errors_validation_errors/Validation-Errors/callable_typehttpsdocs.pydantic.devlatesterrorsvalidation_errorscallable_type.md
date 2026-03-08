##  `callable_type`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#callable_type)
This error is raised when the input value is not valid as a `Callable`:
[Python 3.9 and above](https://docs.pydantic.dev/latest/errors/validation_errors/#__tabbed_1_1)[Python 3.10 and above](https://docs.pydantic.dev/latest/errors/validation_errors/#__tabbed_1_2)
```
from typing import Any, Callable

from pydantic import BaseModel, ImportString, ValidationError


class Model(BaseModel):
    x: ImportString[Callable[[Any], Any]]


Model(x='math:cos')  # OK

try:
    Model(x='os.path')
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'callable_type'

```

```
from typing import Any
from collections.abc import Callable

from pydantic import BaseModel, ImportString, ValidationError


class Model(BaseModel):
    x: ImportString[Callable[[Any], Any]]


Model(x='math:cos')  # OK

try:
    Model(x='os.path')
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'callable_type'

```
