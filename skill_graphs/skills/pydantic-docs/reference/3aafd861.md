## Structural pattern matching[¶](https://docs.pydantic.dev/latest/concepts/models/#structural-pattern-matching)
Pydantic supports structural pattern matching for models, as introduced by
```
from pydantic import BaseModel


class Pet(BaseModel):
    name: str
    species: str


a = Pet(name='Bones', species='dog')

match a:
    # match `species` to 'dog', declare and initialize `dog_name`
    case Pet(species='dog', name=dog_name):
        print(f'{dog_name} is a dog')
#> Bones is a dog
    # default case
    case _:
        print('No dog matched')

```

Note
A match-case statement may seem as if it creates a new model, but don't be fooled; it is just syntactic sugar for getting an attribute and either comparing it or declaring and initializing it.
