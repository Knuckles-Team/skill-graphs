# (at least one element is required)
move_first_element_to_last(tup=())

```

Note the use of the unpacking operator `*` in `tuple[T, *Ts]`. Conceptually, you can think of `Ts` as a tuple of type variables `(T1, T2, ...)`. `tuple[T, *Ts]` would then become `tuple[T, *(T1, T2, ...)]`, which is equivalent to `tuple[T, T1, T2, ...]`. (Note that in older versions of Python, you might see this written using [`Unpack`](https://docs.python.org/3/library/typing.html#typing.Unpack "typing.Unpack") instead, as `Unpack[Ts]`.)
Type variable tuples must _always_ be unpacked. This helps distinguish type variable tuples from normal type variables:
Copy```
x: Ts          # Not valid
x: tuple[Ts]   # Not valid
x: tuple[*Ts]  # The correct way to do it

```

Type variable tuples can be used in the same contexts as normal type variables. For example, in class definitions, arguments, and return types:
Copy```
class Array[*Shape]:
    def __getitem__(self, key: tuple[*Shape]) -> float: ...
    def __abs__(self) -> "Array[*Shape]": ...
    def get_shape(self) -> tuple[*Shape]: ...

```

Type variable tuples can be happily combined with normal type variables:
Copy```
class Array[DType, *Shape]:  # This is fine
    pass

class Array2[*Shape, DType]:  # This would also be fine
    pass

class Height: ...
class Width: ...

float_array_1d: Array[float, Height] = Array()     # Totally fine
int_array_2d: Array[int, Height, Width] = Array()  # Yup, fine too

```

However, note that at most one type variable tuple may appear in a single list of type arguments or type parameters:
Copy```
x: tuple[*Ts, *Ts]            # Not valid
class Array[*Shape, *Shape]:  # Not valid
    pass

```

Finally, an unpacked type variable tuple can be used as the type annotation of `*args`:
Copy```
def call_soon[*Ts](
    callback: Callable[[*Ts], None],
    *args: *Ts
) -> None:
    ...
    callback(*args)

```

In contrast to non-unpacked annotations of `*args` - e.g. `*args: int`, which would specify that _all_ arguments are `int` - `*args: *Ts` enables reference to the types of the _individual_ arguments in `*args`. Here, this allows us to ensure the types of the `*args` passed to `call_soon` match the types of the (positional) arguments of `callback`.
See [**PEP 646**](https://peps.python.org/pep-0646/) for more details on type variable tuples.

__name__[¶](https://docs.python.org/3/library/typing.html#typing.TypeVarTuple.__name__ "Link to this definition")

The name of the type variable tuple.

__default__[¶](https://docs.python.org/3/library/typing.html#typing.TypeVarTuple.__default__ "Link to this definition")

The default value of the type variable tuple, or [`typing.NoDefault`](https://docs.python.org/3/library/typing.html#typing.NoDefault "typing.NoDefault") if it has no default.
Added in version 3.13.

evaluate_default()[¶](https://docs.python.org/3/library/typing.html#typing.TypeVarTuple.evaluate_default "Link to this definition")

An [evaluate function](https://docs.python.org/3/glossary.html#term-evaluate-function) corresponding to the [`__default__`](https://docs.python.org/3/library/typing.html#typing.TypeVarTuple.__default__ "typing.TypeVarTuple.__default__") attribute. When called directly, this method supports only the [`VALUE`](https://docs.python.org/3/library/annotationlib.html#annotationlib.Format.VALUE "annotationlib.Format.VALUE") format, which is equivalent to accessing the `__default__` attribute directly, but the method object can be passed to [`annotationlib.call_evaluate_function()`](https://docs.python.org/3/library/annotationlib.html#annotationlib.call_evaluate_function "annotationlib.call_evaluate_function") to evaluate the value in a different format.
Added in version 3.14.

has_default()[¶](https://docs.python.org/3/library/typing.html#typing.TypeVarTuple.has_default "Link to this definition")

Return whether or not the type variable tuple has a default value. This is equivalent to checking whether [`__default__`](https://docs.python.org/3/library/typing.html#typing.TypeVarTuple.__default__ "typing.TypeVarTuple.__default__") is not the [`typing.NoDefault`](https://docs.python.org/3/library/typing.html#typing.NoDefault "typing.NoDefault") singleton, except that it does not force evaluation of the [lazily evaluated](https://docs.python.org/3/reference/executionmodel.html#lazy-evaluation) default value.
Added in version 3.13.
Added in version 3.11.
Changed in version 3.12: Type variable tuples can now be declared using the [type parameter](https://docs.python.org/3/reference/compound_stmts.html#type-params) syntax introduced by [**PEP 695**](https://peps.python.org/pep-0695/).
Changed in version 3.13: Support for default values was added.

_class_ typing.ParamSpec(_name_ , _*_ , _bound =None_, _covariant =False_, _contravariant =False_, _default =typing.NoDefault_)[¶](https://docs.python.org/3/library/typing.html#typing.ParamSpec "Link to this definition")

Parameter specification variable. A specialized version of [type variables](https://docs.python.org/3/library/typing.html#typevar).
In [type parameter lists](https://docs.python.org/3/reference/compound_stmts.html#type-params), parameter specifications can be declared with two asterisks (`**`):
Copy```
type IntFunc[**P] = Callable[P, int]

```

For compatibility with Python 3.11 and earlier, `ParamSpec` objects can also be created as follows:
Copy```
P = ParamSpec('P')

```

Parameter specification variables exist primarily for the benefit of static type checkers. They are used to forward the parameter types of one callable to another callable – a pattern commonly found in higher order functions and decorators. They are only valid when used in `Concatenate`, or as the first argument to `Callable`, or as parameters for user-defined Generics. See [`Generic`](https://docs.python.org/3/library/typing.html#typing.Generic "typing.Generic") for more information on generic types.
For example, to add basic logging to a function, one can create a decorator `add_logging` to log function calls. The parameter specification variable tells the type checker that the callable passed into the decorator and the new callable returned by it have inter-dependent type parameters:
Copy```
from collections.abc import Callable
import logging

def add_logging[T, **P](f: Callable[P, T]) -> Callable[P, T]:
    '''A type-safe decorator to add logging to a function.'''
    def inner(*args: P.args, **kwargs: P.kwargs) -> T:
        logging.info(f'{f.__name__} was called')
        return f(*args, **kwargs)
    return inner

@add_logging
def add_two(x: float, y: float) -> float:
    '''Add two numbers together.'''
    return x + y

```

Without `ParamSpec`, the simplest way to annotate this previously was to use a [`TypeVar`](https://docs.python.org/3/library/typing.html#typing.TypeVar "typing.TypeVar") with upper bound `Callable[..., Any]`. However this causes two problems:
  1. The type checker can’t type check the `inner` function because `*args` and `**kwargs` have to be typed [`Any`](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any").
  2. [`cast()`](https://docs.python.org/3/library/typing.html#typing.cast "typing.cast") may be required in the body of the `add_logging` decorator when returning the `inner` function, or the static type checker must be told to ignore the `return inner`.



args[¶](https://docs.python.org/3/library/typing.html#typing.ParamSpec.args "Link to this definition")


kwargs[¶](https://docs.python.org/3/library/typing.html#typing.ParamSpec.kwargs "Link to this definition")

Since `ParamSpec` captures both positional and keyword parameters, `P.args` and `P.kwargs` can be used to split a `ParamSpec` into its components. `P.args` represents the tuple of positional parameters in a given call and should only be used to annotate `*args`. `P.kwargs` represents the mapping of keyword parameters to their values in a given call, and should be only be used to annotate `**kwargs`. Both attributes require the annotated parameter to be in scope. At runtime, `P.args` and `P.kwargs` are instances respectively of [`ParamSpecArgs`](https://docs.python.org/3/library/typing.html#typing.ParamSpecArgs "typing.ParamSpecArgs") and [`ParamSpecKwargs`](https://docs.python.org/3/library/typing.html#typing.ParamSpecKwargs "typing.ParamSpecKwargs").

__name__[¶](https://docs.python.org/3/library/typing.html#typing.ParamSpec.__name__ "Link to this definition")

The name of the parameter specification.

__default__[¶](https://docs.python.org/3/library/typing.html#typing.ParamSpec.__default__ "Link to this definition")

The default value of the parameter specification, or [`typing.NoDefault`](https://docs.python.org/3/library/typing.html#typing.NoDefault "typing.NoDefault") if it has no default.
Added in version 3.13.

evaluate_default()[¶](https://docs.python.org/3/library/typing.html#typing.ParamSpec.evaluate_default "Link to this definition")

An [evaluate function](https://docs.python.org/3/glossary.html#term-evaluate-function) corresponding to the [`__default__`](https://docs.python.org/3/library/typing.html#typing.ParamSpec.__default__ "typing.ParamSpec.__default__") attribute. When called directly, this method supports only the [`VALUE`](https://docs.python.org/3/library/annotationlib.html#annotationlib.Format.VALUE "annotationlib.Format.VALUE") format, which is equivalent to accessing the `__default__` attribute directly, but the method object can be passed to [`annotationlib.call_evaluate_function()`](https://docs.python.org/3/library/annotationlib.html#annotationlib.call_evaluate_function "annotationlib.call_evaluate_function") to evaluate the value in a different format.
Added in version 3.14.

has_default()[¶](https://docs.python.org/3/library/typing.html#typing.ParamSpec.has_default "Link to this definition")

Return whether or not the parameter specification has a default value. This is equivalent to checking whether [`__default__`](https://docs.python.org/3/library/typing.html#typing.ParamSpec.__default__ "typing.ParamSpec.__default__") is not the [`typing.NoDefault`](https://docs.python.org/3/library/typing.html#typing.NoDefault "typing.NoDefault") singleton, except that it does not force evaluation of the [lazily evaluated](https://docs.python.org/3/reference/executionmodel.html#lazy-evaluation) default value.
Added in version 3.13.
Parameter specification variables created with `covariant=True` or `contravariant=True` can be used to declare covariant or contravariant generic types. The `bound` argument is also accepted, similar to [`TypeVar`](https://docs.python.org/3/library/typing.html#typing.TypeVar "typing.TypeVar"). However the actual semantics of these keywords are yet to be decided.
Added in version 3.10.
Changed in version 3.12: Parameter specifications can now be declared using the [type parameter](https://docs.python.org/3/reference/compound_stmts.html#type-params) syntax introduced by [**PEP 695**](https://peps.python.org/pep-0695/).
Changed in version 3.13: Support for default values was added.
Note
Only parameter specification variables defined in global scope can be pickled.
See also
  * [**PEP 612**](https://peps.python.org/pep-0612/) – Parameter Specification Variables (the PEP which introduced `ParamSpec` and `Concatenate`)
  * [`Concatenate`](https://docs.python.org/3/library/typing.html#typing.Concatenate "typing.Concatenate")
  * [Annotating callable objects](https://docs.python.org/3/library/typing.html#annotating-callables)



typing.ParamSpecArgs[¶](https://docs.python.org/3/library/typing.html#typing.ParamSpecArgs "Link to this definition")


typing.ParamSpecKwargs[¶](https://docs.python.org/3/library/typing.html#typing.ParamSpecKwargs "Link to this definition")

Arguments and keyword arguments attributes of a [`ParamSpec`](https://docs.python.org/3/library/typing.html#typing.ParamSpec "typing.ParamSpec"). The `P.args` attribute of a `ParamSpec` is an instance of `ParamSpecArgs`, and `P.kwargs` is an instance of `ParamSpecKwargs`. They are intended for runtime introspection and have no special meaning to static type checkers.
Calling [`get_origin()`](https://docs.python.org/3/library/typing.html#typing.get_origin "typing.get_origin") on either of these objects will return the original `ParamSpec`:
Copy```
>>> from typing import ParamSpec, get_origin
>>> P = ParamSpec("P")
>>> get_origin(P.args) is P
True
>>> get_origin(P.kwargs) is P
True

```

Added in version 3.10.

_class_ typing.TypeAliasType(_name_ , _value_ , _*_ , _type_params =()_)[¶](https://docs.python.org/3/library/typing.html#typing.TypeAliasType "Link to this definition")

The type of type aliases created through the [`type`](https://docs.python.org/3/reference/simple_stmts.html#type) statement.
Example:
Copy```
>>> type Alias = int
>>> type(Alias)
<class 'typing.TypeAliasType'>

```

Added in version 3.12.

__name__[¶](https://docs.python.org/3/library/typing.html#typing.TypeAliasType.__name__ "Link to this definition")

The name of the type alias:
Copy```
>>> type Alias = int
>>> Alias.__name__
'Alias'

```


__module__[¶](https://docs.python.org/3/library/typing.html#typing.TypeAliasType.__module__ "Link to this definition")

The name of the module in which the type alias was defined:
Copy```
>>> type Alias = int
>>> Alias.__module__
'__main__'

```


__type_params__[¶](https://docs.python.org/3/library/typing.html#typing.TypeAliasType.__type_params__ "Link to this definition")

The type parameters of the type alias, or an empty tuple if the alias is not generic:
Copy```
>>> type ListOrSet[T] = list[T] | set[T]
>>> ListOrSet.__type_params__
(T,)
>>> type NotGeneric = int
>>> NotGeneric.__type_params__
()

```


__value__[¶](https://docs.python.org/3/library/typing.html#typing.TypeAliasType.__value__ "Link to this definition")

The type alias’s value. This is [lazily evaluated](https://docs.python.org/3/reference/executionmodel.html#lazy-evaluation), so names used in the definition of the alias are not resolved until the `__value__` attribute is accessed:
Copy```
>>> type Mutually = Recursive
>>> type Recursive = Mutually
>>> Mutually
Mutually
>>> Recursive
Recursive
>>> Mutually.__value__
Recursive
>>> Recursive.__value__
Mutually

```


evaluate_value()[¶](https://docs.python.org/3/library/typing.html#typing.TypeAliasType.evaluate_value "Link to this definition")

An [evaluate function](https://docs.python.org/3/glossary.html#term-evaluate-function) corresponding to the [`__value__`](https://docs.python.org/3/library/typing.html#typing.TypeAliasType.__value__ "typing.TypeAliasType.__value__") attribute. When called directly, this method supports only the [`VALUE`](https://docs.python.org/3/library/annotationlib.html#annotationlib.Format.VALUE "annotationlib.Format.VALUE") format, which is equivalent to accessing the `__value__` attribute directly, but the method object can be passed to [`annotationlib.call_evaluate_function()`](https://docs.python.org/3/library/annotationlib.html#annotationlib.call_evaluate_function "annotationlib.call_evaluate_function") to evaluate the value in a different format:
Copy```
>>> type Alias = undefined
>>> Alias.__value__
Traceback (most recent call last):
...
NameError: name 'undefined' is not defined
>>> from annotationlib import Format, call_evaluate_function
>>> Alias.evaluate_value(Format.VALUE)
Traceback (most recent call last):
...
NameError: name 'undefined' is not defined
>>> call_evaluate_function(Alias.evaluate_value, Format.FORWARDREF)
ForwardRef('undefined')

```

Added in version 3.14.
Unpacking
Type aliases support star unpacking using the `*Alias` syntax. This is equivalent to using `Unpack[Alias]` directly:
Copy```
>>> type Alias = tuple[int, str]
>>> type Unpacked = tuple[bool, *Alias]
>>> Unpacked.__value__
tuple[bool, typing.Unpack[Alias]]

```

Added in version 3.14.
#### Other special directives[¶](https://docs.python.org/3/library/typing.html#other-special-directives "Link to this heading")
These functions and classes should not be used directly as annotations. Their intended purpose is to be building blocks for creating and declaring types.

_class_ typing.NamedTuple[¶](https://docs.python.org/3/library/typing.html#typing.NamedTuple "Link to this definition")

Typed version of [`collections.namedtuple()`](https://docs.python.org/3/library/collections.html#collections.namedtuple "collections.namedtuple").
Usage:
Copy```
class Employee(NamedTuple):
    name: str
    id: int

```

This is equivalent to:
Copy```
Employee = collections.namedtuple('Employee', ['name', 'id'])

```

To give a field a default value, you can assign to it in the class body:
Copy```
class Employee(NamedTuple):
    name: str
    id: int = 3

employee = Employee('Guido')
assert employee.id == 3

```

Fields with a default value must come after any fields without a default.
The resulting class has an extra attribute `__annotations__` giving a dict that maps the field names to the field types. (The field names are in the `_fields` attribute and the default values are in the `_field_defaults` attribute, both of which are part of the [`namedtuple()`](https://docs.python.org/3/library/collections.html#collections.namedtuple "collections.namedtuple") API.)
`NamedTuple` subclasses can also have docstrings and methods:
Copy```
class Employee(NamedTuple):
    """Represents an employee."""
    name: str
    id: int = 3

    def __repr__(self) -> str:
        return f'<Employee {self.name}, id={self.id}>'

```

`NamedTuple` subclasses can be generic:
Copy```
class Group[T](NamedTuple):
    key: T
    group: list[T]

```

Backward-compatible usage:
Copy```
