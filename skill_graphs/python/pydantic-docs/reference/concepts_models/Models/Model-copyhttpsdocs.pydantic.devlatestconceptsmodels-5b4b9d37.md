## Model copy[¶](https://docs.pydantic.dev/latest/concepts/models/#model-copy)
API Documentation
[`pydantic.main.BaseModel.model_copy`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_copy)

The [`model_copy()`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_copy) method allows models to be duplicated (with optional updates), which is particularly useful when working with frozen models.
```
from pydantic import BaseModel


class BarModel(BaseModel):
    whatever: int


class FooBarModel(BaseModel):
    banana: float
    foo: str
    bar: BarModel


m = FooBarModel(banana=3.14, foo='hello', bar={'whatever': 123})

print(m.model_copy(update={'banana': 0}))
#> banana=0 foo='hello' bar=BarModel(whatever=123)

# normal copy gives the same object reference for bar:
print(id(m.bar) == id(m.model_copy().bar))
#> True
# deep copy gives a new object reference for `bar`:
print(id(m.bar) == id(m.model_copy(deep=True).bar))
#> False

```
