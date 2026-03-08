##  `complex_str_parsing`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#complex_str_parsing)
This error is raised when the input value is a string but cannot be parsed as a complex number because it does not follow the
```
from pydantic import BaseModel, ValidationError


class Model(BaseModel):
    num: complex


try:
    # Complex numbers in json are expected to be valid complex strings.
    # This value `abc` is not a valid complex string.
    Model.model_validate_json('{"num": "abc"}')
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'complex_str_parsing'

```
