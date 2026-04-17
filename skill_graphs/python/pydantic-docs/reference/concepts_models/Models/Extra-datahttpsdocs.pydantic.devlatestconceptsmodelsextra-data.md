## Extra data[¶](https://docs.pydantic.dev/latest/concepts/models/#extra-data)
By default, Pydantic models **won't error when you provide extra data** , and these values will simply be ignored:
```
from pydantic import BaseModel


class Model(BaseModel):
    x: int


m = Model(x=1, y='a')
assert m.model_dump() == {'x': 1}

```

The [`extra`](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict.extra) configuration value can be used to control this behavior:
```
from pydantic import BaseModel, ConfigDict


class Model(BaseModel):
    x: int

    model_config = ConfigDict(extra='allow')


m = Model(x=1, y='a')  [](https://docs.pydantic.dev/latest/concepts/models/#__code_9_annotation_1)
assert m.model_dump() == {'x': 1, 'y': 'a'}
assert m.__pydantic_extra__ == {'y': 'a'}

```

The configuration can take three values:
  * `'ignore'`: Providing extra data is ignored (the default).
  * `'forbid'`: Providing extra data is not permitted.
  * `'allow'`: Providing extra data is allowed and stored in the `__pydantic_extra__` dictionary attribute. The `__pydantic_extra__` can explicitly be annotated to provide validation for extra fields.


The validation methods (e.g. [`model_validate()`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_validate)) have an optional `extra` argument that will override the `extra` configuration value of the model for that validation call.
For more details, refer to the [`extra`](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict.extra) API documentation.
Pydantic dataclasses also support extra data (see the [dataclass configuration](https://docs.pydantic.dev/latest/concepts/dataclasses/#dataclass-config) section).
