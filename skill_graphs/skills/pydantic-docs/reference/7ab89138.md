## Faux immutability[¶](https://docs.pydantic.dev/latest/concepts/models/#faux-immutability)
Models can be configured to be immutable via `model_config['frozen'] = True`. When this is set, attempting to change the values of instance attributes will raise errors. See the [API reference](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict.frozen) for more details.
Note
This behavior was achieved in Pydantic V1 via the config setting `allow_mutation = False`. This config flag is deprecated in Pydantic V2, and has been replaced with `frozen`.
Warning
In Python, immutability is not enforced. Developers have the ability to modify objects that are conventionally considered "immutable" if they choose to do so.
```
from pydantic import BaseModel, ConfigDict, ValidationError


class FooBarModel(BaseModel):
    model_config = ConfigDict(frozen=True)

    a: str
    b: dict


foobar = FooBarModel(a='hello', b={'apple': 'pear'})

try:
    foobar.a = 'different'
except ValidationError as e:
    print(e)
    """
    1 validation error for FooBarModel
    a
      Instance is frozen [type=frozen_instance, input_value='different', input_type=str]
    """

print(foobar.a)
#> hello
print(foobar.b)
#> {'apple': 'pear'}
foobar.b['apple'] = 'grape'
print(foobar.b)
#> {'apple': 'grape'}

```

Trying to change `a` caused an error, and `a` remains unchanged. However, the dict `b` is mutable, and the immutability of `foobar` doesn't stop `b` from being changed.
