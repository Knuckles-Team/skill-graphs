##  `string_pattern_mismatch`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#string_pattern_mismatch)
This error is raised when the input value doesn't match the field's `pattern` constraint:
```
from pydantic import BaseModel, Field, ValidationError


class Model(BaseModel):
    x: str = Field(pattern='test')


try:
    Model(x='1')
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'string_pattern_mismatch'

```
