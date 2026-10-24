##  `RootModel` and custom root types[¶](https://docs.pydantic.dev/latest/concepts/models/#rootmodel-and-custom-root-types)
API Documentation
[`pydantic.root_model.RootModel`](https://docs.pydantic.dev/latest/api/root_model/#pydantic.root_model.RootModel)

Pydantic models can be defined with a "custom root type" by subclassing [`pydantic.RootModel`](https://docs.pydantic.dev/latest/api/root_model/#pydantic.root_model.RootModel).
The root type can be any type supported by Pydantic, and is specified by the generic parameter to `RootModel`. The root value can be passed to the model `__init__` or [`model_validate`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_validate) via the first and only argument.
Here's an example of how this works:
```
from pydantic import RootModel

Pets = RootModel[list[str]]
PetsByName = RootModel[dict[str, str]]


print(Pets(['dog', 'cat']))
#> root=['dog', 'cat']
print(Pets(['dog', 'cat']).model_dump_json())
#> ["dog","cat"]
print(Pets.model_validate(['dog', 'cat']))
#> root=['dog', 'cat']
print(Pets.model_json_schema())
"""
{'items': {'type': 'string'}, 'title': 'RootModel[list[str]]', 'type': 'array'}
"""

print(PetsByName({'Otis': 'dog', 'Milo': 'cat'}))
#> root={'Otis': 'dog', 'Milo': 'cat'}
print(PetsByName({'Otis': 'dog', 'Milo': 'cat'}).model_dump_json())
#> {"Otis":"dog","Milo":"cat"}
print(PetsByName.model_validate({'Otis': 'dog', 'Milo': 'cat'}))
#> root={'Otis': 'dog', 'Milo': 'cat'}

```

If you want to access items in the `root` field directly or to iterate over the items, you can implement custom `__iter__` and `__getitem__` functions, as shown in the following example.
```
from pydantic import RootModel


class Pets(RootModel):
    root: list[str]

    def __iter__(self):
        return iter(self.root)

    def __getitem__(self, item):
        return self.root[item]


pets = Pets.model_validate(['dog', 'cat'])
print(pets[0])
#> dog
print([pet for pet in pets])
#> ['dog', 'cat']

```

You can also create subclasses of the parametrized root model directly:
```
from pydantic import RootModel


class Pets(RootModel[list[str]]):
    def describe(self) -> str:
        return f'Pets: {", ".join(self.root)}'


my_pets = Pets.model_validate(['dog', 'cat'])

print(my_pets.describe())
#> Pets: dog, cat

```
