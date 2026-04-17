##  `decimal_whole_digits`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#decimal_whole_digits)
This error is raised when the value provided for a `Decimal` has more digits before the decimal point than `max_digits` - `decimal_places` (as long as both are specified):
```
from decimal import Decimal

from pydantic import BaseModel, Field, ValidationError


class Model(BaseModel):
    x: Decimal = Field(max_digits=6, decimal_places=3)


try:
    Model(x='12345.6')
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'decimal_whole_digits'

```
