##  `needs_python_object`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#needs_python_object)
This type of error is raised when validation is attempted from a format that cannot be converted to a Python object. For example, we cannot check `isinstance` or `issubclass` from JSON:
```
import json

from pydantic import BaseModel, ValidationError


class Model(BaseModel):
    bm: type[BaseModel]


try:
    Model.model_validate_json(json.dumps({'bm': 'not a basemodel class'}))
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'needs_python_object'

```
