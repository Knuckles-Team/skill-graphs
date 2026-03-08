# Fails at runtime and does not pass type checking
class AdminUserId(UserId): pass

```

However, it is possible to create a [`NewType`](https://docs.python.org/3/library/typing.html#typing.NewType "typing.NewType") based on a ‘derived’ `NewType`:
Copy```
from typing import NewType

UserId = NewType('UserId', int)

ProUserId = NewType('ProUserId', UserId)

```

and typechecking for `ProUserId` will work as expected.
See [**PEP 484**](https://peps.python.org/pep-0484/) for more details.
Note
Recall that the use of a type alias declares two types to be _equivalent_ to one another. Doing `type Alias = Original` will make the static type checker treat `Alias` as being _exactly equivalent_ to `Original` in all cases. This is useful when you want to simplify complex type signatures.
In contrast, `NewType` declares one type to be a _subtype_ of another. Doing `Derived = NewType('Derived', Original)` will make the static type checker treat `Derived` as a _subclass_ of `Original`, which means a value of type `Original` cannot be used in places where a value of type `Derived` is expected. This is useful when you want to prevent logic errors with minimal runtime cost.
Added in version 3.5.2.
Changed in version 3.10: `NewType` is now a class rather than a function. As a result, there is some additional runtime cost when calling `NewType` over a regular function.
Changed in version 3.11: The performance of calling `NewType` has been restored to its level in Python 3.9.
## Annotating callable objects[¶](https://docs.python.org/3/library/typing.html#annotating-callable-objects "Link to this heading")
Functions – or other [callable](https://docs.python.org/3/glossary.html#term-callable) objects – can be annotated using [`collections.abc.Callable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "collections.abc.Callable") or deprecated [`typing.Callable`](https://docs.python.org/3/library/typing.html#typing.Callable "typing.Callable"). `Callable[[int], str]` signifies a function that takes a single parameter of type [`int`](https://docs.python.org/3/library/functions.html#int "int") and returns a [`str`](https://docs.python.org/3/library/stdtypes.html#str "str").
For example:
Copy```
from collections.abc import Callable, Awaitable

def feeder(get_next_item: Callable[[], str]) -> None:
    ...  # Body

def async_query(on_success: Callable[[int], None],
                on_error: Callable[[int, Exception], None]) -> None:
    ...  # Body

async def on_update(value: str) -> None:
    ...  # Body

callback: Callable[[str], Awaitable[None]] = on_update

```

The subscription syntax must always be used with exactly two values: the argument list and the return type. The argument list must be a list of types, a [`ParamSpec`](https://docs.python.org/3/library/typing.html#typing.ParamSpec "typing.ParamSpec"), [`Concatenate`](https://docs.python.org/3/library/typing.html#typing.Concatenate "typing.Concatenate"), or an ellipsis (`...`). The return type must be a single type.
If a literal ellipsis `...` is given as the argument list, it indicates that a callable with any arbitrary parameter list would be acceptable:
Copy```
def concat(x: str, y: str) -> str:
    return x + y

x: Callable[..., str]
x = str     # OK
x = concat  # Also OK

```

`Callable` cannot express complex signatures such as functions that take a variadic number of arguments, [overloaded functions](https://docs.python.org/3/library/typing.html#overload), or functions that have keyword-only parameters. However, these signatures can be expressed by defining a [`Protocol`](https://docs.python.org/3/library/typing.html#typing.Protocol "typing.Protocol") class with a [`__call__()`](https://docs.python.org/3/reference/datamodel.html#object.__call__ "object.__call__") method:
Copy```
from collections.abc import Iterable
from typing import Protocol

class Combiner(Protocol):
    def __call__(self, *vals: bytes, maxlen: int | None = None) -> list[bytes]: ...

def batch_proc(data: Iterable[bytes], cb_results: Combiner) -> bytes:
    for item in data:
        ...

def good_cb(*vals: bytes, maxlen: int | None = None) -> list[bytes]:
    ...
def bad_cb(*vals: bytes, maxitems: int | None) -> list[bytes]:
    ...

batch_proc([], good_cb)  # OK
batch_proc([], bad_cb)   # Error! Argument 2 has incompatible type because of
                         # different name and kind in the callback

```

Callables which take other callables as arguments may indicate that their parameter types are dependent on each other using [`ParamSpec`](https://docs.python.org/3/library/typing.html#typing.ParamSpec "typing.ParamSpec"). Additionally, if that callable adds or removes arguments from other callables, the [`Concatenate`](https://docs.python.org/3/library/typing.html#typing.Concatenate "typing.Concatenate") operator may be used. They take the form `Callable[ParamSpecVariable, ReturnType]` and `Callable[Concatenate[Arg1Type, Arg2Type, ..., ParamSpecVariable], ReturnType]` respectively.
Changed in version 3.10: `Callable` now supports [`ParamSpec`](https://docs.python.org/3/library/typing.html#typing.ParamSpec "typing.ParamSpec") and [`Concatenate`](https://docs.python.org/3/library/typing.html#typing.Concatenate "typing.Concatenate"). See [**PEP 612**](https://peps.python.org/pep-0612/) for more details.
See also
The documentation for [`ParamSpec`](https://docs.python.org/3/library/typing.html#typing.ParamSpec "typing.ParamSpec") and [`Concatenate`](https://docs.python.org/3/library/typing.html#typing.Concatenate "typing.Concatenate") provides examples of usage in `Callable`.
## Generics[¶](https://docs.python.org/3/library/typing.html#generics "Link to this heading")
Since type information about objects kept in containers cannot be statically inferred in a generic way, many container classes in the standard library support subscription to denote the expected types of container elements.
Copy```
from collections.abc import Mapping, Sequence

class Employee: ...

# Sequence[Employee] indicates that all elements in the sequence
# must be instances of "Employee".
# Mapping[str, str] indicates that all keys and all values in the mapping
# must be strings.
def notify_by_email(employees: Sequence[Employee],
                    overrides: Mapping[str, str]) -> None: ...

```

Generic functions and classes can be parameterized by using [type parameter syntax](https://docs.python.org/3/reference/compound_stmts.html#type-params):
Copy```
from collections.abc import Sequence

def first[T](l: Sequence[T]) -> T:  # Function is generic over the TypeVar "T"
    return l[0]

```

Or by using the [`TypeVar`](https://docs.python.org/3/library/typing.html#typing.TypeVar "typing.TypeVar") factory directly:
Copy```
from collections.abc import Sequence
from typing import TypeVar

U = TypeVar('U')                  # Declare type variable "U"

def second(l: Sequence[U]) -> U:  # Function is generic over the TypeVar "U"
    return l[1]

```

Changed in version 3.12: Syntactic support for generics is new in Python 3.12.
## Annotating tuples[¶](https://docs.python.org/3/library/typing.html#annotating-tuples "Link to this heading")
For most containers in Python, the typing system assumes that all elements in the container will be of the same type. For example:
Copy```
from collections.abc import Mapping
