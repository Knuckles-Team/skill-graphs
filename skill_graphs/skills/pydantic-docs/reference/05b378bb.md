##  `recursion_loop`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#recursion_loop)
This error is raised when a cyclic reference is detected:
```
from pydantic import BaseModel, ValidationError


class Model(BaseModel):
    x: list['Model']


d = {'x': []}
d['x'].append(d)
try:
    Model(**d)
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'recursion_loop'

```
