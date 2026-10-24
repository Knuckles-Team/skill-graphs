## Field ordering[¶](https://docs.pydantic.dev/latest/concepts/models/#field-ordering)
Field order affects models in the following ways:
  * field order is preserved in the model [JSON Schema](https://docs.pydantic.dev/latest/concepts/json_schema/)
  * field order is preserved in [validation errors](https://docs.pydantic.dev/latest/concepts/models/#error-handling)
  * field order is preserved when [serializing data](https://docs.pydantic.dev/latest/concepts/serialization/#serializing-data)


```
from pydantic import BaseModel, ValidationError


class Model(BaseModel):
    a: int
    b: int = 2
    c: int = 1
    d: int = 0
    e: float


print(Model.model_fields.keys())
#> dict_keys(['a', 'b', 'c', 'd', 'e'])
m = Model(e=2, a=1)
print(m.model_dump())
#> {'a': 1, 'b': 2, 'c': 1, 'd': 0, 'e': 2.0}
try:
    Model(a='x', b='x', c='x', d='x', e='x')
except ValidationError as err:
    error_locations = [e['loc'] for e in err.errors()]

print(error_locations)
#> [('a',), ('b',), ('c',), ('d',), ('e',)]

```
