##  `uuid_parsing`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#uuid_parsing)
This error is raised when the input value's type is not valid for a UUID field:
```
from uuid import UUID

from pydantic import BaseModel, ValidationError


class Model(BaseModel):
    u: UUID


try:
    Model(u='12345678-124-1234-1234-567812345678')
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'uuid_parsing'

```
