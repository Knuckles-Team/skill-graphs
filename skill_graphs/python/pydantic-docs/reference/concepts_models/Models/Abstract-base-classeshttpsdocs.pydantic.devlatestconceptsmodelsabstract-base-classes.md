## Abstract base classes[¶](https://docs.pydantic.dev/latest/concepts/models/#abstract-base-classes)
Pydantic models can be used alongside Python's
```
import abc

from pydantic import BaseModel


class FooBarModel(BaseModel, abc.ABC):
    a: str
    b: int

    @abc.abstractmethod
    def my_abstract_method(self):
        pass

```
