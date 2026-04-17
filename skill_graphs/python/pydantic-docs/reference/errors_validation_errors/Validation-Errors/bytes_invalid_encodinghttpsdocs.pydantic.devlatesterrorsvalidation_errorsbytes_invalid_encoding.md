##  `bytes_invalid_encoding`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#bytes_invalid_encoding)
This error is raised when a `bytes` value is invalid under the configured encoding. In the following example, `'a'` is invalid hex (odd number of digits).
```
from pydantic import BaseModel, ValidationError


class Model(BaseModel):
    x: bytes
    model_config = {'val_json_bytes': 'hex'}


try:
    Model(x='a')
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'bytes_invalid_encoding'

```
