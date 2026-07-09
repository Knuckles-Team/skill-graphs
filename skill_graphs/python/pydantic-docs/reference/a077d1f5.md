##  `decimal_max_places`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#decimal_max_places)
This error is raised when the value provided for a `Decimal` has too many digits after the decimal point:
```
from decimal import Decimal

from pydantic import BaseModel, Field, ValidationError


class Model(BaseModel):
    x: Decimal = Field(decimal_places=3)


try:
    Model(x='42.1234')
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'decimal_max_places'

```
