##  `extra_forbidden`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#extra_forbidden)
This error is raised when the input value contains extra fields, but `model_config['extra'] == 'forbid'`:
```
from pydantic import BaseModel, ConfigDict, ValidationError


class Model(BaseModel):
    x: str

    model_config = ConfigDict(extra='forbid')


try:
    Model(x='test', y='test')
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'extra_forbidden'

```

You can read more about the `extra` configuration in the [Extra Attributes](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict.extra) section.
