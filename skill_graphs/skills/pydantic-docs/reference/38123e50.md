##  `url_too_long`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#url_too_long)
This error is raised when the URL length is greater than 2083:
```
from pydantic import BaseModel, HttpUrl, ValidationError


class Model(BaseModel):
    x: HttpUrl


try:
    Model(x='x' * 2084)
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'url_too_long'

```
