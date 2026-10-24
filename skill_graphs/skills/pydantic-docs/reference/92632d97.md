##  `uuid_type`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#uuid_type)
This error is raised when the input value's type is not valid instance for a UUID field (str, bytes or UUID):
```
from uuid import UUID

from pydantic import BaseModel, ValidationError


class Model(BaseModel):
    u: UUID


try:
    Model(u=1234567812412341234567812345678)
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'uuid_type'

```
