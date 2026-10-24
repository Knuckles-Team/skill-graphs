## Model signature[¶](https://docs.pydantic.dev/latest/concepts/models/#model-signature)
All Pydantic models will have their signature generated based on their fields:
```
import inspect

from pydantic import BaseModel, Field


class FooModel(BaseModel):
    id: int
    name: str = None
    description: str = 'Foo'
    apple: int = Field(alias='pear')


print(inspect.signature(FooModel))
#> (*, id: int, name: str = None, description: str = 'Foo', pear: int) -> None

```

An accurate signature is useful for introspection purposes and libraries like `FastAPI` or `hypothesis`.
The generated signature will also respect custom `__init__` functions:
```
import inspect

from pydantic import BaseModel


class MyModel(BaseModel):
    id: int
    info: str = 'Foo'

    def __init__(self, id: int = 1, *, bar: str, **data) -> None:
        """My custom init!"""
        super().__init__(id=id, bar=bar, **data)


print(inspect.signature(MyModel))
#> (id: int = 1, *, bar: str, info: str = 'Foo') -> None

```

To be included in the signature, a field's alias or name must be a valid Python identifier. Pydantic will prioritize a field's alias over its name when generating the signature, but may use the field name if the alias is not a valid Python identifier.
If a field's alias and name are _both_ not valid identifiers (which may be possible through exotic use of `create_model`), a `**data` argument will be added. In addition, the `**data` argument will always be present in the signature if `model_config['extra'] == 'allow'`.
