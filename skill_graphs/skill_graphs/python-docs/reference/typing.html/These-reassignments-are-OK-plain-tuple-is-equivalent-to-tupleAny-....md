# These reassignments are OK: plain ``tuple`` is equivalent to ``tuple[Any, ...]``
z = (1, 2, 3)
z = ()

```

## The type of class objects[¶](https://docs.python.org/3/library/typing.html#the-type-of-class-objects "Link to this heading")
A variable annotated with `C` may accept a value of type `C`. In contrast, a variable annotated with `type[C]` (or deprecated [`typing.Type[C]`](https://docs.python.org/3/library/typing.html#typing.Type "typing.Type")) may accept values that are classes themselves – specifically, it will accept the _class object_ of `C`. For example:
Copy```
a = 3         # Has type ``int``
b = int       # Has type ``type[int]``
c = type(a)   # Also has type ``type[int]``

```

Note that `type[C]` is covariant:
Copy```
class User: ...
class ProUser(User): ...
class TeamUser(User): ...

def make_new_user(user_class: type[User]) -> User:
    # ...
    return user_class()

make_new_user(User)      # OK
make_new_user(ProUser)   # Also OK: ``type[ProUser]`` is a subtype of ``type[User]``
make_new_user(TeamUser)  # Still fine
make_new_user(User())    # Error: expected ``type[User]`` but got ``User``
make_new_user(int)       # Error: ``type[int]`` is not a subtype of ``type[User]``

```

The only legal parameters for [`type`](https://docs.python.org/3/library/functions.html#type "type") are classes, [`Any`](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any"), [type variables](https://docs.python.org/3/library/typing.html#generics), and unions of any of these types. For example:
Copy```
def new_non_team_user(user_class: type[BasicUser | ProUser]): ...

new_non_team_user(BasicUser)  # OK
new_non_team_user(ProUser)    # OK
new_non_team_user(TeamUser)   # Error: ``type[TeamUser]`` is not a subtype
                              # of ``type[BasicUser | ProUser]``
new_non_team_user(User)       # Also an error

```

`type[Any]` is equivalent to [`type`](https://docs.python.org/3/library/functions.html#type "type"), which is the root of Python’s [metaclass hierarchy](https://docs.python.org/3/reference/datamodel.html#metaclasses).
## Annotating generators and coroutines[¶](https://docs.python.org/3/library/typing.html#annotating-generators-and-coroutines "Link to this heading")
A generator can be annotated using the generic type [`Generator[YieldType, SendType, ReturnType]`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Generator "collections.abc.Generator"). For example:
Copy```
def echo_round() -> Generator[int, float, str]:
    sent = yield 0
    while sent >= 0:
        sent = yield round(sent)
    return 'Done'

```

Note that unlike many other generic classes in the standard library, the `SendType` of [`Generator`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Generator "collections.abc.Generator") behaves contravariantly, not covariantly or invariantly.
The `SendType` and `ReturnType` parameters default to `None`:
Copy```
def infinite_stream(start: int) -> Generator[int]:
    while True:
        yield start
        start += 1

```

It is also possible to set these types explicitly:
Copy```
def infinite_stream(start: int) -> Generator[int, None, None]:
    while True:
        yield start
        start += 1

```

Simple generators that only ever yield values can also be annotated as having a return type of either [`Iterable[YieldType]`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "collections.abc.Iterable") or [`Iterator[YieldType]`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "collections.abc.Iterator"):
Copy```
def infinite_stream(start: int) -> Iterator[int]:
    while True:
        yield start
        start += 1

```

Async generators are handled in a similar fashion, but don’t expect a `ReturnType` type argument ([`AsyncGenerator[YieldType, SendType]`](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncGenerator "collections.abc.AsyncGenerator")). The `SendType` argument defaults to `None`, so the following definitions are equivalent:
Copy```
async def infinite_stream(start: int) -> AsyncGenerator[int]:
    while True:
        yield start
        start = await increment(start)

async def infinite_stream(start: int) -> AsyncGenerator[int, None]:
    while True:
        yield start
        start = await increment(start)

```

As in the synchronous case, [`AsyncIterable[YieldType]`](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterable "collections.abc.AsyncIterable") and [`AsyncIterator[YieldType]`](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator "collections.abc.AsyncIterator") are available as well:
Copy```
async def infinite_stream(start: int) -> AsyncIterator[int]:
    while True:
        yield start
        start = await increment(start)

```

Coroutines can be annotated using [`Coroutine[YieldType, SendType, ReturnType]`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Coroutine "collections.abc.Coroutine"). Generic arguments correspond to those of [`Generator`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Generator "collections.abc.Generator"), for example:
Copy```
from collections.abc import Coroutine
c: Coroutine[list[str], str, int]  # Some coroutine defined elsewhere
x = c.send('hi')                   # Inferred type of 'x' is list[str]
async def bar() -> None:
    y = await c                    # Inferred type of 'y' is int

```

## User-defined generic types[¶](https://docs.python.org/3/library/typing.html#user-defined-generic-types "Link to this heading")
A user-defined class can be defined as a generic class.
Copy```
from logging import Logger

class LoggedVar[T]:
    def __init__(self, value: T, name: str, logger: Logger) -> None:
        self.name = name
        self.logger = logger
        self.value = value

    def set(self, new: T) -> None:
        self.log('Set ' + repr(self.value))
        self.value = new

    def get(self) -> T:
        self.log('Get ' + repr(self.value))
        return self.value

    def log(self, message: str) -> None:
        self.logger.info('%s: %s', self.name, message)

```

This syntax indicates that the class `LoggedVar` is parameterised around a single [type variable](https://docs.python.org/3/library/typing.html#typevar) `T` . This also makes `T` valid as a type within the class body.
Generic classes implicitly inherit from [`Generic`](https://docs.python.org/3/library/typing.html#typing.Generic "typing.Generic"). For compatibility with Python 3.11 and lower, it is also possible to inherit explicitly from `Generic` to indicate a generic class:
Copy```
from typing import TypeVar, Generic

T = TypeVar('T')

class LoggedVar(Generic[T]):
    ...

```

Generic classes have [`__class_getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__class_getitem__ "object.__class_getitem__") methods, meaning they can be parameterised at runtime (e.g. `LoggedVar[int]` below):
Copy```
from collections.abc import Iterable

def zero_all_vars(vars: Iterable[LoggedVar[int]]) -> None:
    for var in vars:
        var.set(0)

```

A generic type can have any number of type variables. All varieties of [`TypeVar`](https://docs.python.org/3/library/typing.html#typing.TypeVar "typing.TypeVar") are permissible as parameters for a generic type:
Copy```
from typing import TypeVar, Generic, Sequence

class WeirdTrio[T, B: Sequence[bytes], S: (int, str)]:
    ...

OldT = TypeVar('OldT', contravariant=True)
OldB = TypeVar('OldB', bound=Sequence[bytes], covariant=True)
OldS = TypeVar('OldS', int, str)

class OldWeirdTrio(Generic[OldT, OldB, OldS]):
    ...

```

Each type variable argument to [`Generic`](https://docs.python.org/3/library/typing.html#typing.Generic "typing.Generic") must be distinct. This is thus invalid:
Copy```
from typing import TypeVar, Generic
...

class Pair[M, M]:  # SyntaxError
    ...

T = TypeVar('T')

class Pair(Generic[T, T]):   # INVALID
    ...

```

Generic classes can also inherit from other classes:
Copy```
from collections.abc import Sized

class LinkedList[T](Sized):
    ...

```

When inheriting from generic classes, some type parameters could be fixed:
Copy```
from collections.abc import Mapping

class MyDict[T](Mapping[str, T]):
    ...

```

In this case `MyDict` has a single parameter, `T`.
Using a generic class without specifying type parameters assumes [`Any`](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any") for each position. In the following example, `MyIterable` is not generic but implicitly inherits from `Iterable[Any]`:
Copy```
from collections.abc import Iterable

class MyIterable(Iterable): # Same as Iterable[Any]
    ...

```

User-defined generic type aliases are also supported. Examples:
Copy```
from collections.abc import Iterable

type Response[S] = Iterable[S] | int

# Return type here is same as Iterable[str] | int
def response(query: str) -> Response[str]:
    ...

type Vec[T] = Iterable[tuple[T, T]]

def inproduct[T: (int, float, complex)](v: Vec[T]) -> T: # Same as Iterable[tuple[T, T]]
    return sum(x*y for x, y in v)

```

For backward compatibility, generic type aliases can also be created through a simple assignment:
Copy```
from collections.abc import Iterable
from typing import TypeVar

S = TypeVar("S")
Response = Iterable[S] | int

```

Changed in version 3.7: [`Generic`](https://docs.python.org/3/library/typing.html#typing.Generic "typing.Generic") no longer has a custom metaclass.
Changed in version 3.12: Syntactic support for generics and type aliases is new in version 3.12. Previously, generic classes had to explicitly inherit from [`Generic`](https://docs.python.org/3/library/typing.html#typing.Generic "typing.Generic") or contain a type variable in one of their bases.
User-defined generics for parameter expressions are also supported via parameter specification variables in the form `[**P]`. The behavior is consistent with type variables’ described above as parameter specification variables are treated by the `typing` module as a specialized type variable. The one exception to this is that a list of types can be used to substitute a [`ParamSpec`](https://docs.python.org/3/library/typing.html#typing.ParamSpec "typing.ParamSpec"):
Copy```
>>> class Z[T, **P]: ...  # T is a TypeVar; P is a ParamSpec
...
>>> Z[int, [dict, float]]
__main__.Z[int, [dict, float]]

```

Classes generic over a [`ParamSpec`](https://docs.python.org/3/library/typing.html#typing.ParamSpec "typing.ParamSpec") can also be created using explicit inheritance from [`Generic`](https://docs.python.org/3/library/typing.html#typing.Generic "typing.Generic"). In this case, `**` is not used:
Copy```
from typing import ParamSpec, Generic

P = ParamSpec('P')

class Z(Generic[P]):
    ...

```

Another difference between [`TypeVar`](https://docs.python.org/3/library/typing.html#typing.TypeVar "typing.TypeVar") and [`ParamSpec`](https://docs.python.org/3/library/typing.html#typing.ParamSpec "typing.ParamSpec") is that a generic with only one parameter specification variable will accept parameter lists in the forms `X[[Type1, Type2, ...]]` and also `X[Type1, Type2, ...]` for aesthetic reasons. Internally, the latter is converted to the former, so the following are equivalent:
Copy```
>>> class X[**P]: ...
...
>>> X[int, str]
__main__.X[[int, str]]
>>> X[[int, str]]
__main__.X[[int, str]]

```

Note that generics with [`ParamSpec`](https://docs.python.org/3/library/typing.html#typing.ParamSpec "typing.ParamSpec") may not have correct `__parameters__` after substitution in some cases because they are intended primarily for static type checking.
Changed in version 3.10: [`Generic`](https://docs.python.org/3/library/typing.html#typing.Generic "typing.Generic") can now be parameterized over parameter expressions. See [`ParamSpec`](https://docs.python.org/3/library/typing.html#typing.ParamSpec "typing.ParamSpec") and [**PEP 612**](https://peps.python.org/pep-0612/) for more details.
A user-defined generic class can have ABCs as base classes without a metaclass conflict. Generic metaclasses are not supported. The outcome of parameterizing generics is cached, and most types in the `typing` module are [hashable](https://docs.python.org/3/glossary.html#term-hashable) and comparable for equality.
## The [`Any`](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any") type[¶](https://docs.python.org/3/library/typing.html#the-any-type "Link to this heading")
A special kind of type is [`Any`](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any"). A static type checker will treat every type as being compatible with `Any` and `Any` as being compatible with every type.
This means that it is possible to perform any operation or method call on a value of type [`Any`](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any") and assign it to any variable:
Copy```
from typing import Any

a: Any = None
a = []          # OK
a = 2           # OK

s: str = ''
s = a           # OK

def foo(item: Any) -> int:
    # Passes type checking; 'item' could be any type,
    # and that type might have a 'bar' method
    item.bar()
    ...

```

Notice that no type checking is performed when assigning a value of type [`Any`](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any") to a more precise type. For example, the static type checker did not report an error when assigning `a` to `s` even though `s` was declared to be of type [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") and receives an [`int`](https://docs.python.org/3/library/functions.html#int "int") value at runtime!
Furthermore, all functions without a return type or parameter types will implicitly default to using [`Any`](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any"):
Copy```
def legacy_parser(text):
    ...
    return data

# A static type checker will treat the above
# as having the same signature as:
def legacy_parser(text: Any) -> Any:
    ...
    return data

```

This behavior allows [`Any`](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any") to be used as an _escape hatch_ when you need to mix dynamically and statically typed code.
Contrast the behavior of [`Any`](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any") with the behavior of [`object`](https://docs.python.org/3/library/functions.html#object "object"). Similar to `Any`, every type is a subtype of `object`. However, unlike `Any`, the reverse is not true: `object` is _not_ a subtype of every other type.
That means when the type of a value is [`object`](https://docs.python.org/3/library/functions.html#object "object"), a type checker will reject almost all operations on it, and assigning it to a variable (or using it as a return value) of a more specialized type is a type error. For example:
Copy```
def hash_a(item: object) -> int:
    # Fails type checking; an object does not have a 'magic' method.
    item.magic()
    ...

def hash_b(item: Any) -> int:
    # Passes type checking
    item.magic()
    ...
