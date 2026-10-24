# are located in the `typing_extensions` backports package.
from typing_extensions import TypeVarTuple, Unpack

Ts = TypeVarTuple('Ts')
tup: tuple[*Ts]         # Syntax error on Python <= 3.10!
tup: tuple[Unpack[Ts]]  # Semantically equivalent, and backwards-compatible

```

`Unpack` can also be used along with [`typing.TypedDict`](https://docs.python.org/3/library/typing.html#typing.TypedDict "typing.TypedDict") for typing `**kwargs` in a function signature:
Copy```
from typing import TypedDict, Unpack

class Movie(TypedDict):
    name: str
    year: int

# This function expects two keyword arguments - `name` of type `str`
# and `year` of type `int`.
def foo(**kwargs: Unpack[Movie]): ...

```

See [**PEP 692**](https://peps.python.org/pep-0692/) for more details on using `Unpack` for `**kwargs` typing.
Added in version 3.11.
#### Building generic types and type aliases[¶](https://docs.python.org/3/library/typing.html#building-generic-types-and-type-aliases "Link to this heading")
The following classes should not be used directly as annotations. Their intended purpose is to be building blocks for creating generic types and type aliases.
These objects can be created through special syntax ([type parameter lists](https://docs.python.org/3/reference/compound_stmts.html#type-params) and the [`type`](https://docs.python.org/3/reference/simple_stmts.html#type) statement). For compatibility with Python 3.11 and earlier, they can also be created without the dedicated syntax, as documented below.

_class_ typing.Generic[¶](https://docs.python.org/3/library/typing.html#typing.Generic "Link to this definition")

Abstract base class for generic types.
A generic type is typically declared by adding a list of type parameters after the class name:
Copy```
class Mapping[KT, VT]:
    def __getitem__(self, key: KT) -> VT:
        ...
        # Etc.

```

Such a class implicitly inherits from `Generic`. The runtime semantics of this syntax are discussed in the [Language Reference](https://docs.python.org/3/reference/compound_stmts.html#generic-classes).
This class can then be used as follows:
Copy```
def lookup_name[X, Y](mapping: Mapping[X, Y], key: X, default: Y) -> Y:
    try:
        return mapping[key]
    except KeyError:
        return default

```

Here the brackets after the function name indicate a [generic function](https://docs.python.org/3/reference/compound_stmts.html#generic-functions).
For backwards compatibility, generic classes can also be declared by explicitly inheriting from `Generic`. In this case, the type parameters must be declared separately:
Copy```
KT = TypeVar('KT')
VT = TypeVar('VT')

class Mapping(Generic[KT, VT]):
    def __getitem__(self, key: KT) -> VT:
        ...
        # Etc.

```


_class_ typing.TypeVar(_name_ , _* constraints_, _bound =None_, _covariant =False_, _contravariant =False_, _infer_variance =False_, _default =typing.NoDefault_)[¶](https://docs.python.org/3/library/typing.html#typing.TypeVar "Link to this definition")

Type variable.
The preferred way to construct a type variable is via the dedicated syntax for [generic functions](https://docs.python.org/3/reference/compound_stmts.html#generic-functions), [generic classes](https://docs.python.org/3/reference/compound_stmts.html#generic-classes), and [generic type aliases](https://docs.python.org/3/reference/compound_stmts.html#generic-type-aliases):
Copy```
class Sequence[T]:  # T is a TypeVar
    ...

```

This syntax can also be used to create bounded and constrained type variables:
Copy```
class StrSequence[S: str]:  # S is a TypeVar with a `str` upper bound;
    ...                     # we can say that S is "bounded by `str`"


class StrOrBytesSequence[A: (str, bytes)]:  # A is a TypeVar constrained to str or bytes
    ...

```

However, if desired, reusable type variables can also be constructed manually, like so:
Copy```
T = TypeVar('T')  # Can be anything
S = TypeVar('S', bound=str)  # Can be any subtype of str
A = TypeVar('A', str, bytes)  # Must be exactly str or bytes

```

Type variables exist primarily for the benefit of static type checkers. They serve as the parameters for generic types as well as for generic function and type alias definitions. See [`Generic`](https://docs.python.org/3/library/typing.html#typing.Generic "typing.Generic") for more information on generic types. Generic functions work as follows:
Copy```
def repeat[T](x: T, n: int) -> Sequence[T]:
    """Return a list containing n references to x."""
    return [x]*n


def print_capitalized[S: str](x: S) -> S:
    """Print x capitalized, and return x."""
    print(x.capitalize())
    return x


def concatenate[A: (str, bytes)](x: A, y: A) -> A:
    """Add two strings or bytes objects together."""
    return x + y

```

Note that type variables can be _bounded_ , _constrained_ , or neither, but cannot be both bounded _and_ constrained.
The variance of type variables is inferred by type checkers when they are created through the [type parameter syntax](https://docs.python.org/3/reference/compound_stmts.html#type-params) or when `infer_variance=True` is passed. Manually created type variables may be explicitly marked covariant or contravariant by passing `covariant=True` or `contravariant=True`. By default, manually created type variables are invariant. See [**PEP 484**](https://peps.python.org/pep-0484/) and [**PEP 695**](https://peps.python.org/pep-0695/) for more details.
Bounded type variables and constrained type variables have different semantics in several important ways. Using a _bounded_ type variable means that the `TypeVar` will be solved using the most specific type possible:
Copy```
x = print_capitalized('a string')
reveal_type(x)  # revealed type is str

class StringSubclass(str):
    pass

y = print_capitalized(StringSubclass('another string'))
reveal_type(y)  # revealed type is StringSubclass

z = print_capitalized(45)  # error: int is not a subtype of str

```

The upper bound of a type variable can be a concrete type, abstract type (ABC or Protocol), or even a union of types:
Copy```
