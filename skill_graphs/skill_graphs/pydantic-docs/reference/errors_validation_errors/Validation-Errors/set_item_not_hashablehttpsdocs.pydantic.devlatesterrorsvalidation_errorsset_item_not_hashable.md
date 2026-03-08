##  `set_item_not_hashable`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#set_item_not_hashable)
This error is raised when an unhashable value is validated against a
```
from pydantic import BaseModel, ValidationError


class Model(BaseModel):
    x: set[object]


class Unhashable:
    __hash__ = None


try:
    Model(x=[{'a': 'b'}, Unhashable()])
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'set_item_not_hashable'
    print(repr(exc.errors()[1]['type']))
    #> 'set_item_not_hashable'

```
