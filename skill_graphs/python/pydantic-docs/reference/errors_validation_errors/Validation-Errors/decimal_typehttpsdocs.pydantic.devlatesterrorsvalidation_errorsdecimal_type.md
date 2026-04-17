##  `decimal_type`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#decimal_type)
This error is raised when the value provided for a `Decimal` is of the wrong type:
```
from decimal import Decimal

from pydantic import BaseModel, Field, ValidationError


class Model(BaseModel):
    x: Decimal = Field(decimal_places=3)


try:
    Model(x=[1, 2, 3])
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'decimal_type'

```

This error is also raised for strict fields when the input value is not an instance of `Decimal`.
