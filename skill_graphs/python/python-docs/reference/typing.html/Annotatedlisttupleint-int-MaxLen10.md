# ``Annotated[list[tuple[int, int]], MaxLen(10)]``:
type V = Vec[int]

```

`Annotated` cannot be used with an unpacked [`TypeVarTuple`](https://docs.python.org/3/library/typing.html#typing.TypeVarTuple "typing.TypeVarTuple"):
Copy```
type Variadic[*Ts] = Annotated[*Ts, Ann1] = Annotated[T1, T2, T3, ..., Ann1]  # NOT valid

```

where `T1`, `T2`, … are [`TypeVars`](https://docs.python.org/3/library/typing.html#typing.TypeVar "typing.TypeVar"). This is invalid as only one type should be passed to Annotated.
By default, [`get_type_hints()`](https://docs.python.org/3/library/typing.html#typing.get_type_hints "typing.get_type_hints") strips the metadata from annotations. Pass `include_extras=True` to have the metadata preserved:
> Copy```
>>> from typing import Annotated, get_type_hints
>>> def func(x: Annotated[int, "metadata"]) -> None: pass
...
>>> get_type_hints(func)
{'x': <class 'int'>, 'return': <class 'NoneType'>}
>>> get_type_hints(func, include_extras=True)
{'x': typing.Annotated[int, 'metadata'], 'return': <class 'NoneType'>}

```

At runtime, the metadata associated with an `Annotated` type can be retrieved via the `__metadata__` attribute:
> Copy```
>>> from typing import Annotated
>>> X = Annotated[int, "very", "important", "metadata"]
>>> X
typing.Annotated[int, 'very', 'important', 'metadata']
>>> X.__metadata__
('very', 'important', 'metadata')

```

If you want to retrieve the original type wrapped by `Annotated`, use the `__origin__` attribute:
> Copy```
>>> from typing import Annotated, get_origin
>>> Password = Annotated[str, "secret"]
>>> Password.__origin__
<class 'str'>

```

Note that using [`get_origin()`](https://docs.python.org/3/library/typing.html#typing.get_origin "typing.get_origin") will return `Annotated` itself:
> Copy```
>>> get_origin(Password)
typing.Annotated

```

See also

[**PEP 593**](https://peps.python.org/pep-0593/) - Flexible function and variable annotations

The PEP introducing `Annotated` to the standard library.
Added in version 3.9.

typing.TypeIs[¶](https://docs.python.org/3/library/typing.html#typing.TypeIs "Link to this definition")

Special typing construct for marking user-defined type predicate functions.
`TypeIs` can be used to annotate the return type of a user-defined type predicate function. `TypeIs` only accepts a single type argument. At runtime, functions marked this way should return a boolean and take at least one positional argument.
`TypeIs` aims to benefit _type narrowing_ – a technique used by static type checkers to determine a more precise type of an expression within a program’s code flow. Usually type narrowing is done by analyzing conditional code flow and applying the narrowing to a block of code. The conditional expression here is sometimes referred to as a “type predicate”:
Copy```
def is_str(val: str | float):
    # "isinstance" type predicate
    if isinstance(val, str):
        # Type of ``val`` is narrowed to ``str``
        ...
    else:
        # Else, type of ``val`` is narrowed to ``float``.
        ...

```

Sometimes it would be convenient to use a user-defined boolean function as a type predicate. Such a function should use `TypeIs[...]` or [`TypeGuard`](https://docs.python.org/3/library/typing.html#typing.TypeGuard "typing.TypeGuard") as its return type to alert static type checkers to this intention. `TypeIs` usually has more intuitive behavior than `TypeGuard`, but it cannot be used when the input and output types are incompatible (e.g., `list[object]` to `list[int]`) or when the function does not return `True` for all instances of the narrowed type.
Using `-> TypeIs[NarrowedType]` tells the static type checker that for a given function:
  1. The return value is a boolean.
  2. If the return value is `True`, the type of its argument is the intersection of the argument’s original type and `NarrowedType`.
  3. If the return value is `False`, the type of its argument is narrowed to exclude `NarrowedType`.


For example:
Copy```
from typing import assert_type, final, TypeIs

class Parent: pass
class Child(Parent): pass
@final
class Unrelated: pass

def is_parent(val: object) -> TypeIs[Parent]:
    return isinstance(val, Parent)

def run(arg: Child | Unrelated):
    if is_parent(arg):
        # Type of ``arg`` is narrowed to the intersection
        # of ``Parent`` and ``Child``, which is equivalent to
        # ``Child``.
        assert_type(arg, Child)
    else:
        # Type of ``arg`` is narrowed to exclude ``Parent``,
        # so only ``Unrelated`` is left.
        assert_type(arg, Unrelated)

```

The type inside `TypeIs` must be consistent with the type of the function’s argument; if it is not, static type checkers will raise an error. An incorrectly written `TypeIs` function can lead to unsound behavior in the type system; it is the user’s responsibility to write such functions in a type-safe manner.
If a `TypeIs` function is a class or instance method, then the type in `TypeIs` maps to the type of the second parameter (after `cls` or `self`).
In short, the form `def foo(arg: TypeA) -> TypeIs[TypeB]: ...`, means that if `foo(arg)` returns `True`, then `arg` is an instance of `TypeB`, and if it returns `False`, it is not an instance of `TypeB`.
`TypeIs` also works with type variables. For more information, see [**PEP 742**](https://peps.python.org/pep-0742/) (Narrowing types with `TypeIs`).
Added in version 3.13.

typing.TypeGuard[¶](https://docs.python.org/3/library/typing.html#typing.TypeGuard "Link to this definition")

Special typing construct for marking user-defined type predicate functions.
Type predicate functions are user-defined functions that return whether their argument is an instance of a particular type. `TypeGuard` works similarly to [`TypeIs`](https://docs.python.org/3/library/typing.html#typing.TypeIs "typing.TypeIs"), but has subtly different effects on type checking behavior (see below).
Using `-> TypeGuard` tells the static type checker that for a given function:
  1. The return value is a boolean.
  2. If the return value is `True`, the type of its argument is the type inside `TypeGuard`.


`TypeGuard` also works with type variables. See [**PEP 647**](https://peps.python.org/pep-0647/) for more details.
For example:
Copy```
def is_str_list(val: list[object]) -> TypeGuard[list[str]]:
    '''Determines whether all objects in the list are strings'''
    return all(isinstance(x, str) for x in val)

def func1(val: list[object]):
    if is_str_list(val):
        # Type of ``val`` is narrowed to ``list[str]``.
        print(" ".join(val))
    else:
        # Type of ``val`` remains as ``list[object]``.
        print("Not a list of strings!")

```

`TypeIs` and `TypeGuard` differ in the following ways:
  * `TypeIs` requires the narrowed type to be a subtype of the input type, while `TypeGuard` does not. The main reason is to allow for things like narrowing `list[object]` to `list[str]` even though the latter is not a subtype of the former, since `list` is invariant.
  * When a `TypeGuard` function returns `True`, type checkers narrow the type of the variable to exactly the `TypeGuard` type. When a `TypeIs` function returns `True`, type checkers can infer a more precise type combining the previously known type of the variable with the `TypeIs` type. (Technically, this is known as an intersection type.)
  * When a `TypeGuard` function returns `False`, type checkers cannot narrow the type of the variable at all. When a `TypeIs` function returns `False`, type checkers can narrow the type of the variable to exclude the `TypeIs` type.


Added in version 3.10.

typing.Unpack[¶](https://docs.python.org/3/library/typing.html#typing.Unpack "Link to this definition")

Typing operator to conceptually mark an object as having been unpacked.
For example, using the unpack operator `*` on a [type variable tuple](https://docs.python.org/3/library/typing.html#typevartuple) is equivalent to using `Unpack` to mark the type variable tuple as having been unpacked:
Copy```
Ts = TypeVarTuple('Ts')
tup: tuple[*Ts]
# Effectively does:
tup: tuple[Unpack[Ts]]

```

In fact, `Unpack` can be used interchangeably with `*` in the context of [`typing.TypeVarTuple`](https://docs.python.org/3/library/typing.html#typing.TypeVarTuple "typing.TypeVarTuple") and [`builtins.tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "tuple") types. You might see `Unpack` being used explicitly in older versions of Python, where `*` couldn’t be used in certain places:
Copy```
