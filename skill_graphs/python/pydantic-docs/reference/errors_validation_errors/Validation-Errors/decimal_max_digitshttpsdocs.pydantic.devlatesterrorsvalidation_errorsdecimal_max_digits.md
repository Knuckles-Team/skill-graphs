##  `decimal_max_digits`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#decimal_max_digits)
This error is raised when the value provided for a `Decimal` has too many digits:
```
from decimal import Decimal

from pydantic import BaseModel, Field, ValidationError


class Model(BaseModel):
    x: Decimal = Field(max_digits=3)


try:
    Model(x='42.1234')
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'decimal_max_digits'

```
