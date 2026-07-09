## Dataclass config[¶](https://docs.pydantic.dev/latest/concepts/dataclasses/#dataclass-config)
If you want to modify the configuration like you would with a [`BaseModel`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel), you have two options:
  * Use the `config` argument of the decorator.
  * Define the configuration with the `__pydantic_config__` attribute.


```
from pydantic import ConfigDict
from pydantic.dataclasses import dataclass


# Option 1 -- using the decorator argument:
@dataclass(config=ConfigDict(validate_assignment=True))  [](https://docs.pydantic.dev/latest/concepts/dataclasses/#__code_4_annotation_1)
class MyDataclass1:
    a: int


# Option 2 -- using an attribute:
@dataclass
class MyDataclass2:
    a: int

    __pydantic_config__ = ConfigDict(validate_assignment=True)

```

Note
While Pydantic dataclasses support the [`extra`](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict.extra) configuration value, some default behavior of stdlib dataclasses may prevail. For example, any extra fields present on a Pydantic dataclass with [`extra`](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict.extra) set to `'allow'` are omitted in the dataclass' string representation. There is also no way to provide validation [using the `__pydantic_extra__` attribute](https://docs.pydantic.dev/latest/concepts/models/#extra-data).
