##  `mapping_type`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#mapping_type)
This error is raised when a problem occurs during validation due to a failure in a call to the methods from the `Mapping` protocol, such as `.items()`:
```
from collections.abc import Mapping

from pydantic import BaseModel, ValidationError


class BadMapping(Mapping):
    def items(self):
        raise ValueError()

    def __iter__(self):
        raise ValueError()

    def __getitem__(self, key):
        raise ValueError()

    def __len__(self):
        return 1


class Model(BaseModel):
    x: dict[str, str]


try:
    Model(x=BadMapping())
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'mapping_type'

```
