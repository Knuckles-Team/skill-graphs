##  `no_such_attribute`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#no_such_attribute)
This error is raised when `validate_assignment=True` in the config, and you attempt to assign a value to an attribute that is not an existing field:
```
from pydantic import ConfigDict, ValidationError, dataclasses


@dataclasses.dataclass(config=ConfigDict(validate_assignment=True))
class MyDataclass:
    x: int


m = MyDataclass(x=1)
try:
    m.y = 10
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'no_such_attribute'

```
