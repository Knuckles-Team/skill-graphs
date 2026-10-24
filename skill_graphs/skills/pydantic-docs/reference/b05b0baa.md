##  `url_parsing`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#url_parsing)
This error is raised when the input value cannot be parsed as a URL:
```
from pydantic import AnyUrl, BaseModel, ValidationError


class Model(BaseModel):
    x: AnyUrl


try:
    Model(x='test')
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'url_parsing'

```
