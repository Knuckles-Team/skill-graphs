##  `uuid_version`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#uuid_version)
This error is raised when the input value's type is not match UUID version:
```
from pydantic import UUID5, BaseModel, ValidationError


class Model(BaseModel):
    u: UUID5


try:
    Model(u='a6cc5730-2261-11ee-9c43-2eb5a363657c')
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'uuid_version'

```
