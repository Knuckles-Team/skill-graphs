##  `decimal_parsing`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#decimal_parsing)
This error is raised when the value provided for a `Decimal` could not be parsed as a decimal number:
```
from decimal import Decimal

from pydantic import BaseModel, Field, ValidationError


class Model(BaseModel):
    x: Decimal = Field(decimal_places=3)


try:
    Model(x='test')
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'decimal_parsing'

```
