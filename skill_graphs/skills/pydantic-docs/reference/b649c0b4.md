## Stdlib dataclasses and Pydantic dataclasses[¶](https://docs.pydantic.dev/latest/concepts/dataclasses/#stdlib-dataclasses-and-pydantic-dataclasses)
### Inherit from stdlib dataclasses[¶](https://docs.pydantic.dev/latest/concepts/dataclasses/#inherit-from-stdlib-dataclasses)
Stdlib dataclasses (nested or not) can also be inherited and Pydantic will automatically validate all the inherited fields.
```
import dataclasses

import pydantic


@dataclasses.dataclass
class Z:
    z: int


@dataclasses.dataclass
class Y(Z):
    y: int = 0


@pydantic.dataclasses.dataclass
class X(Y):
    x: int = 0


foo = X(x=b'1', y='2', z='3')
print(foo)
#> X(z=3, y=2, x=1)

try:
    X(z='pika')
except pydantic.ValidationError as e:
    print(e)
    """
    1 validation error for X
    z
      Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='pika', input_type=str]
    """

```

The decorator can also be applied directly on a stdlib dataclass, in which case a new subclass will be created:
```
import dataclasses

import pydantic


@dataclasses.dataclass
class A:
    a: int


PydanticA = pydantic.dataclasses.dataclass(A)
print(PydanticA(a='1'))
#> A(a=1)

```

### Usage of stdlib dataclasses with `BaseModel`[¶](https://docs.pydantic.dev/latest/concepts/dataclasses/#usage-of-stdlib-dataclasses-with-basemodel)
When a standard library dataclass is used within a Pydantic model, a Pydantic dataclass or a [`TypeAdapter`](https://docs.pydantic.dev/latest/api/type_adapter/#pydantic.type_adapter.TypeAdapter), validation will be applied (and the [configuration](https://docs.pydantic.dev/latest/concepts/dataclasses/#dataclass-config) stays the same). This means that using a stdlib or a Pydantic dataclass as a field annotation is functionally equivalent.
[Python 3.9 and above](https://docs.pydantic.dev/latest/concepts/dataclasses/#__tabbed_3_1)[Python 3.10 and above](https://docs.pydantic.dev/latest/concepts/dataclasses/#__tabbed_3_2)
```
import dataclasses
from typing import Optional

from pydantic import BaseModel, ConfigDict, ValidationError


@dataclasses.dataclass(frozen=True)
class User:
    name: str


class Foo(BaseModel):
    # Required so that pydantic revalidates the model attributes:
    model_config = ConfigDict(revalidate_instances='always')

    user: Optional[User] = None


# nothing is validated as expected:
user = User(name=['not', 'a', 'string'])
print(user)
#> User(name=['not', 'a', 'string'])


try:
    Foo(user=user)
except ValidationError as e:
    print(e)
    """
    1 validation error for Foo
    user.name
      Input should be a valid string [type=string_type, input_value=['not', 'a', 'string'], input_type=list]
    """

foo = Foo(user=User(name='pika'))
try:
    foo.user.name = 'bulbi'
except dataclasses.FrozenInstanceError as e:
    print(e)
    #> cannot assign to field 'name'

```

```
import dataclasses

from pydantic import BaseModel, ConfigDict, ValidationError


@dataclasses.dataclass(frozen=True)
class User:
    name: str


class Foo(BaseModel):
    # Required so that pydantic revalidates the model attributes:
    model_config = ConfigDict(revalidate_instances='always')

    user: User | None = None


# nothing is validated as expected:
user = User(name=['not', 'a', 'string'])
print(user)
#> User(name=['not', 'a', 'string'])


try:
    Foo(user=user)
except ValidationError as e:
    print(e)
    """
    1 validation error for Foo
    user.name
      Input should be a valid string [type=string_type, input_value=['not', 'a', 'string'], input_type=list]
    """

foo = Foo(user=User(name='pika'))
try:
    foo.user.name = 'bulbi'
except dataclasses.FrozenInstanceError as e:
    print(e)
    #> cannot assign to field 'name'

```

### Using custom types[¶](https://docs.pydantic.dev/latest/concepts/dataclasses/#using-custom-types)
As said above, validation is applied on standard library dataclasses. If you make use of custom types, you will get an error when trying to refer to the dataclass. To circumvent the issue, you can set the [`arbitrary_types_allowed`](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict.arbitrary_types_allowed) configuration value on the dataclass:
```
import dataclasses

from pydantic import BaseModel, ConfigDict
from pydantic.errors import PydanticSchemaGenerationError


class ArbitraryType:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f'ArbitraryType(value={self.value!r})'


@dataclasses.dataclass
class DC:
    a: ArbitraryType
    b: str


# valid as it is a stdlib dataclass without validation:
my_dc = DC(a=ArbitraryType(value=3), b='qwe')

try:

    class Model(BaseModel):
        dc: DC
        other: str

    # invalid as dc is now validated with pydantic, and ArbitraryType is not a known type
    Model(dc=my_dc, other='other')

except PydanticSchemaGenerationError as e:
    print(e.message)
    """
    Unable to generate pydantic-core schema for <class '__main__.ArbitraryType'>. Set `arbitrary_types_allowed=True` in the model_config to ignore this error or implement `__get_pydantic_core_schema__` on your type to fully support it.

    If you got this error by calling handler(<some type>) within `__get_pydantic_core_schema__` then you likely need to call `handler.generate_schema(<some type>)` since we do not call `__get_pydantic_core_schema__` on `<some type>` otherwise to avoid infinite recursion.
    """


# valid as we set arbitrary_types_allowed=True, and that config pushes down to the nested vanilla dataclass
class Model(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    dc: DC
    other: str


m = Model(dc=my_dc, other='other')
print(repr(m))
#> Model(dc=DC(a=ArbitraryType(value=3), b='qwe'), other='other')

```

### Checking if a dataclass is a Pydantic dataclass[¶](https://docs.pydantic.dev/latest/concepts/dataclasses/#checking-if-a-dataclass-is-a-pydantic-dataclass)
Pydantic dataclasses are still considered dataclasses, so using `True`. To check if a type is specifically a Pydantic dataclass you can use the [`is_pydantic_dataclass()`](https://docs.pydantic.dev/latest/api/dataclasses/#pydantic.dataclasses.is_pydantic_dataclass) function.
```
import dataclasses

import pydantic


@dataclasses.dataclass
class StdLibDataclass:
    id: int


PydanticDataclass = pydantic.dataclasses.dataclass(StdLibDataclass)

print(dataclasses.is_dataclass(StdLibDataclass))
#> True
print(pydantic.dataclasses.is_pydantic_dataclass(StdLibDataclass))
#> False

print(dataclasses.is_dataclass(PydanticDataclass))
#> True
print(pydantic.dataclasses.is_pydantic_dataclass(PydanticDataclass))
#> True

```
