## Automatically excluded attributes[¶](https://docs.pydantic.dev/latest/concepts/models/#automatically-excluded-attributes)
### Class variables[¶](https://docs.pydantic.dev/latest/concepts/models/#class-variables)
Attributes annotated with
```
from typing import ClassVar

from pydantic import BaseModel


class Model(BaseModel):
    x: ClassVar[int] = 1

    y: int = 2


m = Model()
print(m)
#> y=2
print(Model.x)
#> 1

```

### Private model attributes[¶](https://docs.pydantic.dev/latest/concepts/models/#private-model-attributes)
API Documentation
[`pydantic.fields.PrivateAttr`](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.PrivateAttr)

Attributes whose name has a leading underscore are not treated as fields by Pydantic, and are not included in the model schema. Instead, these are converted into a "private attribute" which is not validated or even set during calls to `__init__`, `model_validate`, etc.
Here is an example of usage:
```
from datetime import datetime
from random import randint
from typing import Any

from pydantic import BaseModel, PrivateAttr


class TimeAwareModel(BaseModel):
    _processed_at: datetime = PrivateAttr(default_factory=datetime.now)
    _secret_value: str

    def model_post_init(self, context: Any) -> None:
        # this could also be done with `default_factory`:
        self._secret_value = randint(1, 5)


m = TimeAwareModel()
print(m._processed_at)
#> 2032-01-02 03:04:05.000006
print(m._secret_value)
#> 3

```

Private attribute names must start with underscore to prevent conflicts with model fields. However, dunder names (such as `__attr__`) are not supported, and will be completely ignored from the model definition.
