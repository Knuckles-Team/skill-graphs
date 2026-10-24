##  `int_parsing_size`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#int_parsing_size)
This error is raised when attempting to parse a python or JSON value from a string outside the maximum range that Python `str` to `int` parsing permits:
```
import json

from pydantic import BaseModel, ValidationError


class Model(BaseModel):
    x: int


# from Python
assert Model(x='1' * 4_300).x == int('1' * 4_300)  # OK

too_long = '1' * 4_301
try:
    Model(x=too_long)
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'int_parsing_size'

# from JSON
try:
    Model.model_validate_json(json.dumps({'x': too_long}))
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'int_parsing_size'

```
