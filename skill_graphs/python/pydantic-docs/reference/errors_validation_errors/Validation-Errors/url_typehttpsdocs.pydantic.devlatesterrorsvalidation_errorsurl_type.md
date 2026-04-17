##  `url_type`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#url_type)
This error is raised when the input value's type is not valid for a URL field:
```
from pydantic import BaseModel, HttpUrl, ValidationError


class Model(BaseModel):
    x: HttpUrl


try:
    Model(x=None)
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'url_type'

```
