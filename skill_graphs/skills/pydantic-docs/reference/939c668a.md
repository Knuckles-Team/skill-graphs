##  `dataclass_type`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#dataclass_type)
This error is raised when the input value is not valid for a `dataclass` field:
```
from pydantic import ValidationError, dataclasses


@dataclasses.dataclass
class Inner:
    x: int


@dataclasses.dataclass
class Outer:
    y: Inner


Outer(y=Inner(x=1))  # OK

try:
    Outer(y=1)
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'dataclass_type'

```
