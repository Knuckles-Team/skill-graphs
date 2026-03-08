## Data conversion[¶](https://docs.pydantic.dev/latest/concepts/models/#data-conversion)
Pydantic may cast input data to force it to conform to model field types, and in some cases this may result in a loss of information. For example:
```
from pydantic import BaseModel


class Model(BaseModel):
    a: int
    b: float
    c: str


print(Model(a=3.000, b='2.72', c=b'binary data').model_dump())
#> {'a': 3, 'b': 2.72, 'c': 'binary data'}

```

This is a deliberate decision of Pydantic, and is frequently the most useful approach. See
Nevertheless, Pydantic provides a [strict mode](https://docs.pydantic.dev/latest/concepts/strict_mode/), where no data conversion is performed. Values must be of the same type as the declared field type.
This is also the case for collections. In most cases, you shouldn't make use of abstract container classes and just use a concrete type, such as
```
from pydantic import BaseModel


class Model(BaseModel):
    items: list[int]  [](https://docs.pydantic.dev/latest/concepts/models/#__code_7_annotation_1)


print(Model(items=(1, 2, 3)))
#> items=[1, 2, 3]

```

Besides, using these abstract types can also lead to [poor validation performance](https://docs.pydantic.dev/latest/concepts/performance/#sequence-vs-list-or-tuple-with-mapping-vs-dict), and in general using concrete container types will avoid unnecessary checks.
[](https://docs.pydantic.dev/latest/concepts/models/)
