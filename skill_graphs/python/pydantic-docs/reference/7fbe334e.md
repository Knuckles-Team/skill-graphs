##  `url_scheme`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#url_scheme)
This error is raised when the URL scheme is not valid for the URL type of the field:
```
from pydantic import BaseModel, HttpUrl, ValidationError


class Model(BaseModel):
    x: HttpUrl


try:
    Model(x='ftp://example.com')
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'url_scheme'

```
