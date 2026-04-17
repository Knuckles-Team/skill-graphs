# Alternative syntax
Point2D = TypedDict('Point2D', {'x': int, 'y': int, 'label': NotRequired[str]})

```

This means that a `Point2D` `TypedDict` can have the `label` key omitted.
It is also possible to mark all keys as non-required by default by specifying a totality of `False`:
Copy```
class Point2D(TypedDict, total=False):
    x: int
    y: int

# Alternative syntax
Point2D = TypedDict('Point2D', {'x': int, 'y': int}, total=False)

```

This means that a `Point2D` `TypedDict` can have any of the keys omitted. A type checker is only expected to support a literal `False` or `True` as the value of the `total` argument. `True` is the default, and makes all items defined in the class body required.
Individual keys of a `total=False` `TypedDict` can be marked as required using [`Required`](https://docs.python.org/3/library/typing.html#typing.Required "typing.Required"):
Copy```
class Point2D(TypedDict, total=False):
    x: Required[int]
    y: Required[int]
    label: str

# Alternative syntax
Point2D = TypedDict('Point2D', {
    'x': Required[int],
    'y': Required[int],
    'label': str
}, total=False)

```

It is possible for a `TypedDict` type to inherit from one or more other `TypedDict` types using the class-based syntax. Usage:
Copy```
class Point3D(Point2D):
    z: int

```

`Point3D` has three items: `x`, `y` and `z`. It is equivalent to this definition:
Copy```
class Point3D(TypedDict):
    x: int
    y: int
    z: int

```

A `TypedDict` cannot inherit from a non-`TypedDict` class, except for [`Generic`](https://docs.python.org/3/library/typing.html#typing.Generic "typing.Generic"). For example:
Copy```
class X(TypedDict):
    x: int

class Y(TypedDict):
    y: int

class Z(object): pass  # A non-TypedDict class

class XY(X, Y): pass  # OK

class XZ(X, Z): pass  # raises TypeError

```

A `TypedDict` can be generic:
Copy```
class Group[T](TypedDict):
    key: T
    group: list[T]

```

To create a generic `TypedDict` that is compatible with Python 3.11 or lower, inherit from [`Generic`](https://docs.python.org/3/library/typing.html#typing.Generic "typing.Generic") explicitly:
Copy```
T = TypeVar("T")

class Group(TypedDict, Generic[T]):
    key: T
    group: list[T]

```

A `TypedDict` can be introspected via annotations dicts (see [Annotations Best Practices](https://docs.python.org/3/howto/annotations.html#annotations-howto) for more information on annotations best practices), [`__total__`](https://docs.python.org/3/library/typing.html#typing.TypedDict.__total__ "typing.TypedDict.__total__"), [`__required_keys__`](https://docs.python.org/3/library/typing.html#typing.TypedDict.__required_keys__ "typing.TypedDict.__required_keys__"), and [`__optional_keys__`](https://docs.python.org/3/library/typing.html#typing.TypedDict.__optional_keys__ "typing.TypedDict.__optional_keys__").

__total__[¶](https://docs.python.org/3/library/typing.html#typing.TypedDict.__total__ "Link to this definition")

`Point2D.__total__` gives the value of the `total` argument. Example:
Copy```
>>> from typing import TypedDict
>>> class Point2D(TypedDict): pass
>>> Point2D.__total__
True
>>> class Point2D(TypedDict, total=False): pass
>>> Point2D.__total__
False
>>> class Point3D(Point2D): pass
>>> Point3D.__total__
True

```

This attribute reflects _only_ the value of the `total` argument to the current `TypedDict` class, not whether the class is semantically total. For example, a `TypedDict` with `__total__` set to `True` may have keys marked with [`NotRequired`](https://docs.python.org/3/library/typing.html#typing.NotRequired "typing.NotRequired"), or it may inherit from another `TypedDict` with `total=False`. Therefore, it is generally better to use [`__required_keys__`](https://docs.python.org/3/library/typing.html#typing.TypedDict.__required_keys__ "typing.TypedDict.__required_keys__") and [`__optional_keys__`](https://docs.python.org/3/library/typing.html#typing.TypedDict.__optional_keys__ "typing.TypedDict.__optional_keys__") for introspection.

__required_keys__[¶](https://docs.python.org/3/library/typing.html#typing.TypedDict.__required_keys__ "Link to this definition")

Added in version 3.9.

__optional_keys__[¶](https://docs.python.org/3/library/typing.html#typing.TypedDict.__optional_keys__ "Link to this definition")

`Point2D.__required_keys__` and `Point2D.__optional_keys__` return [`frozenset`](https://docs.python.org/3/library/stdtypes.html#frozenset "frozenset") objects containing required and non-required keys, respectively.
Keys marked with [`Required`](https://docs.python.org/3/library/typing.html#typing.Required "typing.Required") will always appear in `__required_keys__` and keys marked with [`NotRequired`](https://docs.python.org/3/library/typing.html#typing.NotRequired "typing.NotRequired") will always appear in `__optional_keys__`.
For backwards compatibility with Python 3.10 and below, it is also possible to use inheritance to declare both required and non-required keys in the same `TypedDict` . This is done by declaring a `TypedDict` with one value for the `total` argument and then inheriting from it in another `TypedDict` with a different value for `total`:
Copy```
>>> class Point2D(TypedDict, total=False):
...     x: int
...     y: int
...
>>> class Point3D(Point2D):
...     z: int
...
>>> Point3D.__required_keys__ == frozenset({'z'})
True
>>> Point3D.__optional_keys__ == frozenset({'x', 'y'})
True

```

Added in version 3.9.
Note
If `from __future__ import annotations` is used or if annotations are given as strings, annotations are not evaluated when the `TypedDict` is defined. Therefore, the runtime introspection that `__required_keys__` and `__optional_keys__` rely on may not work properly, and the values of the attributes may be incorrect.
Support for [`ReadOnly`](https://docs.python.org/3/library/typing.html#typing.ReadOnly "typing.ReadOnly") is reflected in the following attributes:

__readonly_keys__[¶](https://docs.python.org/3/library/typing.html#typing.TypedDict.__readonly_keys__ "Link to this definition")

A [`frozenset`](https://docs.python.org/3/library/stdtypes.html#frozenset "frozenset") containing the names of all read-only keys. Keys are read-only if they carry the [`ReadOnly`](https://docs.python.org/3/library/typing.html#typing.ReadOnly "typing.ReadOnly") qualifier.
Added in version 3.13.

__mutable_keys__[¶](https://docs.python.org/3/library/typing.html#typing.TypedDict.__mutable_keys__ "Link to this definition")

A [`frozenset`](https://docs.python.org/3/library/stdtypes.html#frozenset "frozenset") containing the names of all mutable keys. Keys are mutable if they do not carry the [`ReadOnly`](https://docs.python.org/3/library/typing.html#typing.ReadOnly "typing.ReadOnly") qualifier.
Added in version 3.13.
See the [TypedDict](https://typing.python.org/en/latest/spec/typeddict.html#typeddict) section in the typing documentation for more examples and detailed rules.
Added in version 3.8.
Changed in version 3.9: `TypedDict` is now a function rather than a class. It can still be used as a class base, as described above.
Changed in version 3.11: Added support for marking individual keys as [`Required`](https://docs.python.org/3/library/typing.html#typing.Required "typing.Required") or [`NotRequired`](https://docs.python.org/3/library/typing.html#typing.NotRequired "typing.NotRequired"). See [**PEP 655**](https://peps.python.org/pep-0655/).
Changed in version 3.11: Added support for generic `TypedDict`s.
Changed in version 3.13: Removed support for the keyword-argument method of creating `TypedDict`s.
Changed in version 3.13: Support for the [`ReadOnly`](https://docs.python.org/3/library/typing.html#typing.ReadOnly "typing.ReadOnly") qualifier was added.
Deprecated since version 3.13, will be removed in version 3.15: When using the functional syntax to create a TypedDict class, failing to pass a value to the ‘fields’ parameter (`TD = TypedDict("TD")`) is deprecated. Passing `None` to the ‘fields’ parameter (`TD = TypedDict("TD", None)`) is also deprecated. Both will be disallowed in Python 3.15. To create a TypedDict class with 0 fields, use `class TD(TypedDict): pass` or `TD = TypedDict("TD", {})`.
### Protocols[¶](https://docs.python.org/3/library/typing.html#protocols "Link to this heading")
The following protocols are provided by the `typing` module. All are decorated with [`@runtime_checkable`](https://docs.python.org/3/library/typing.html#typing.runtime_checkable "typing.runtime_checkable").

_class_ typing.SupportsAbs[¶](https://docs.python.org/3/library/typing.html#typing.SupportsAbs "Link to this definition")

An ABC with one abstract method `__abs__` that is covariant in its return type.

_class_ typing.SupportsBytes[¶](https://docs.python.org/3/library/typing.html#typing.SupportsBytes "Link to this definition")

An ABC with one abstract method `__bytes__`.

_class_ typing.SupportsComplex[¶](https://docs.python.org/3/library/typing.html#typing.SupportsComplex "Link to this definition")

An ABC with one abstract method `__complex__`.

_class_ typing.SupportsFloat[¶](https://docs.python.org/3/library/typing.html#typing.SupportsFloat "Link to this definition")

An ABC with one abstract method `__float__`.

_class_ typing.SupportsIndex[¶](https://docs.python.org/3/library/typing.html#typing.SupportsIndex "Link to this definition")

An ABC with one abstract method `__index__`.
Added in version 3.8.

_class_ typing.SupportsInt[¶](https://docs.python.org/3/library/typing.html#typing.SupportsInt "Link to this definition")

An ABC with one abstract method `__int__`.

_class_ typing.SupportsRound[¶](https://docs.python.org/3/library/typing.html#typing.SupportsRound "Link to this definition")

An ABC with one abstract method `__round__` that is covariant in its return type.
### ABCs and Protocols for working with I/O[¶](https://docs.python.org/3/library/typing.html#abcs-and-protocols-for-working-with-i-o "Link to this heading")

_class_ typing.IO[_AnyStr_][¶](https://docs.python.org/3/library/typing.html#typing.IO "Link to this definition")


_class_ typing.TextIO[¶](https://docs.python.org/3/library/typing.html#typing.TextIO "Link to this definition")


_class_ typing.BinaryIO[¶](https://docs.python.org/3/library/typing.html#typing.BinaryIO "Link to this definition")

Generic class `IO[AnyStr]` and its subclasses `TextIO(IO[str])` and `BinaryIO(IO[bytes])` represent the types of I/O streams such as returned by [`open()`](https://docs.python.org/3/library/functions.html#open "open"). Please note that these classes are not protocols, and their interface is fairly broad.
The protocols [`io.Reader`](https://docs.python.org/3/library/io.html#io.Reader "io.Reader") and [`io.Writer`](https://docs.python.org/3/library/io.html#io.Writer "io.Writer") offer a simpler alternative for argument types, when only the `read()` or `write()` methods are accessed, respectively:
Copy```
def read_and_write(reader: Reader[str], writer: Writer[bytes]):
    data = reader.read()
    writer.write(data.encode())

```

Also consider using [`collections.abc.Iterable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "collections.abc.Iterable") for iterating over the lines of an input stream:
Copy```
def read_config(stream: Iterable[str]):
    for line in stream:
        ...

```

### Functions and decorators[¶](https://docs.python.org/3/library/typing.html#functions-and-decorators "Link to this heading")

typing.cast(_typ_ , _val_)[¶](https://docs.python.org/3/library/typing.html#typing.cast "Link to this definition")

Cast a value to a type.
This returns the value unchanged. To the type checker this signals that the return value has the designated type, but at runtime we intentionally don’t check anything (we want this to be as fast as possible).

typing.assert_type(_val_ , _typ_ , _/_)[¶](https://docs.python.org/3/library/typing.html#typing.assert_type "Link to this definition")

Ask a static type checker to confirm that _val_ has an inferred type of _typ_.
At runtime this does nothing: it returns the first argument unchanged with no checks or side effects, no matter the actual type of the argument.
When a static type checker encounters a call to `assert_type()`, it emits an error if the value is not of the specified type:
Copy```
def greet(name: str) -> None:
    assert_type(name, str)  # OK, inferred type of `name` is `str`
    assert_type(name, int)  # type checker error

```

This function is useful for ensuring the type checker’s understanding of a script is in line with the developer’s intentions:
Copy```
def complex_function(arg: object):
    # Do some complex type-narrowing logic,
    # after which we hope the inferred type will be `int`
    ...
    # Test whether the type checker correctly understands our function
    assert_type(arg, int)

```

Added in version 3.11.

typing.assert_never(_arg_ , _/_)[¶](https://docs.python.org/3/library/typing.html#typing.assert_never "Link to this definition")

Ask a static type checker to confirm that a line of code is unreachable.
Example:
Copy```
def int_or_str(arg: int | str) -> None:
    match arg:
        case int():
            print("It's an int")
        case str():
            print("It's a str")
        case _ as unreachable:
            assert_never(unreachable)

```

Here, the annotations allow the type checker to infer that the last case can never execute, because `arg` is either an [`int`](https://docs.python.org/3/library/functions.html#int "int") or a [`str`](https://docs.python.org/3/library/stdtypes.html#str "str"), and both options are covered by earlier cases.
If a type checker finds that a call to `assert_never()` is reachable, it will emit an error. For example, if the type annotation for `arg` was instead `int | str | float`, the type checker would emit an error pointing out that `unreachable` is of type [`float`](https://docs.python.org/3/library/functions.html#float "float"). For a call to `assert_never` to pass type checking, the inferred type of the argument passed in must be the bottom type, [`Never`](https://docs.python.org/3/library/typing.html#typing.Never "typing.Never"), and nothing else.
At runtime, this throws an exception when called.
See also
[Unreachable Code and Exhaustiveness Checking](https://typing.python.org/en/latest/guides/unreachable.html) has more information about exhaustiveness checking with static typing.
Added in version 3.11.

typing.reveal_type(_obj_ , _/_)[¶](https://docs.python.org/3/library/typing.html#typing.reveal_type "Link to this definition")

Ask a static type checker to reveal the inferred type of an expression.
When a static type checker encounters a call to this function, it emits a diagnostic with the inferred type of the argument. For example:
Copy```
x: int = 1
reveal_type(x)  # Revealed type is "builtins.int"

```

This can be useful when you want to debug how your type checker handles a particular piece of code.
At runtime, this function prints the runtime type of its argument to [`sys.stderr`](https://docs.python.org/3/library/sys.html#sys.stderr "sys.stderr") and returns the argument unchanged (allowing the call to be used within an expression):
Copy```
x = reveal_type(1)  # prints "Runtime type is int"
print(x)  # prints "1"

```

Note that the runtime type may be different from (more or less specific than) the type statically inferred by a type checker.
Most type checkers support `reveal_type()` anywhere, even if the name is not imported from `typing`. Importing the name from `typing`, however, allows your code to run without runtime errors and communicates intent more clearly.
Added in version 3.11.

@typing.dataclass_transform(_*_ , _eq_default =True_, _order_default =False_, _kw_only_default =False_, _frozen_default =False_, _field_specifiers =()_, _** kwargs_)[¶](https://docs.python.org/3/library/typing.html#typing.dataclass_transform "Link to this definition")

Decorator to mark an object as providing [`dataclass`](https://docs.python.org/3/library/dataclasses.html#dataclasses.dataclass "dataclasses.dataclass")-like behavior.
`dataclass_transform` may be used to decorate a class, metaclass, or a function that is itself a decorator. The presence of `@dataclass_transform()` tells a static type checker that the decorated object performs runtime “magic” that transforms a class in a similar way to [`@dataclasses.dataclass`](https://docs.python.org/3/library/dataclasses.html#dataclasses.dataclass "dataclasses.dataclass").
Example usage with a decorator function:
Copy```
@dataclass_transform()
def create_model[T](cls: type[T]) -> type[T]:
    ...
    return cls

@create_model
class CustomerModel:
    id: int
    name: str

```

On a base class:
Copy```
@dataclass_transform()
class ModelBase: ...

class CustomerModel(ModelBase):
    id: int
    name: str

```

On a metaclass:
Copy```
@dataclass_transform()
class ModelMeta(type): ...

class ModelBase(metaclass=ModelMeta): ...

class CustomerModel(ModelBase):
    id: int
    name: str

```

The `CustomerModel` classes defined above will be treated by type checkers similarly to classes created with [`@dataclasses.dataclass`](https://docs.python.org/3/library/dataclasses.html#dataclasses.dataclass "dataclasses.dataclass"). For example, type checkers will assume these classes have `__init__` methods that accept `id` and `name`.
The decorated class, metaclass, or function may accept the following bool arguments which type checkers will assume have the same effect as they would have on the [`@dataclasses.dataclass`](https://docs.python.org/3/library/dataclasses.html#dataclasses.dataclass "dataclasses.dataclass") decorator: `init`, `eq`, `order`, `unsafe_hash`, `frozen`, `match_args`, `kw_only`, and `slots`. It must be possible for the value of these arguments (`True` or `False`) to be statically evaluated.
The arguments to the `dataclass_transform` decorator can be used to customize the default behaviors of the decorated class, metaclass, or function:

Parameters:

  * **eq_default** ([_bool_](https://docs.python.org/3/library/functions.html#bool "bool")) – Indicates whether the `eq` parameter is assumed to be `True` or `False` if it is omitted by the caller. Defaults to `True`.
  * **order_default** ([_bool_](https://docs.python.org/3/library/functions.html#bool "bool")) – Indicates whether the `order` parameter is assumed to be `True` or `False` if it is omitted by the caller. Defaults to `False`.
  * **kw_only_default** ([_bool_](https://docs.python.org/3/library/functions.html#bool "bool")) – Indicates whether the `kw_only` parameter is assumed to be `True` or `False` if it is omitted by the caller. Defaults to `False`.
  * **frozen_default** ([_bool_](https://docs.python.org/3/library/functions.html#bool "bool")) –
Indicates whether the `frozen` parameter is assumed to be `True` or `False` if it is omitted by the caller. Defaults to `False`.
Added in version 3.12.
  * **field_specifiers** ([_tuple_](https://docs.python.org/3/library/stdtypes.html#tuple "tuple") _[_[_Callable_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "collections.abc.Callable") _[__...__,__Any_ _]__,__...__]_) – Specifies a static list of supported classes or functions that describe fields, similar to [`dataclasses.field()`](https://docs.python.org/3/library/dataclasses.html#dataclasses.field "dataclasses.field"). Defaults to `()`.
  * ****kwargs** (_Any_) – Arbitrary other keyword arguments are accepted in order to allow for possible future extensions.


Type checkers recognize the following optional parameters on field specifiers:
**Recognised parameters for field specifiers**[¶](https://docs.python.org/3/library/typing.html#id7 "Link to this table") Parameter name | Description
---|---
`init` | Indicates whether the field should be included in the synthesized `__init__` method. If unspecified, `init` defaults to `True`.
`default` | Provides the default value for the field.
`default_factory` | Provides a runtime callback that returns the default value for the field. If neither `default` nor `default_factory` are specified, the field is assumed to have no default value and must be provided a value when the class is instantiated.
`factory` | An alias for the `default_factory` parameter on field specifiers.
`kw_only` | Indicates whether the field should be marked as keyword-only. If `True`, the field will be keyword-only. If `False`, it will not be keyword-only. If unspecified, the value of the `kw_only` parameter on the object decorated with `dataclass_transform` will be used, or if that is unspecified, the value of `kw_only_default` on `dataclass_transform` will be used.
`alias` | Provides an alternative name for the field. This alternative name is used in the synthesized `__init__` method.
At runtime, this decorator records its arguments in the `__dataclass_transform__` attribute on the decorated object. It has no other runtime effect.
See [**PEP 681**](https://peps.python.org/pep-0681/) for more details.
Added in version 3.11.

@typing.overload[¶](https://docs.python.org/3/library/typing.html#typing.overload "Link to this definition")

Decorator for creating overloaded functions and methods.
The `@overload` decorator allows describing functions and methods that support multiple different combinations of argument types. A series of `@overload`-decorated definitions must be followed by exactly one non-`@overload`-decorated definition (for the same function/method).
`@overload`-decorated definitions are for the benefit of the type checker only, since they will be overwritten by the non-`@overload`-decorated definition. The non-`@overload`-decorated definition, meanwhile, will be used at runtime but should be ignored by a type checker. At runtime, calling an `@overload`-decorated function directly will raise [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "NotImplementedError").
An example of overload that gives a more precise type than can be expressed using a union or a type variable:
Copy```
@overload
def process(response: None) -> None:
    ...
@overload
def process(response: int) -> tuple[int, str]:
    ...
@overload
def process(response: bytes) -> str:
    ...
def process(response):
    ...  # actual implementation goes here

```

See [**PEP 484**](https://peps.python.org/pep-0484/) for more details and comparison with other typing semantics.
Changed in version 3.11: Overloaded functions can now be introspected at runtime using [`get_overloads()`](https://docs.python.org/3/library/typing.html#typing.get_overloads "typing.get_overloads").

typing.get_overloads(_func_)[¶](https://docs.python.org/3/library/typing.html#typing.get_overloads "Link to this definition")

Return a sequence of [`@overload`](https://docs.python.org/3/library/typing.html#typing.overload "typing.overload")-decorated definitions for _func_.
_func_ is the function object for the implementation of the overloaded function. For example, given the definition of `process` in the documentation for [`@overload`](https://docs.python.org/3/library/typing.html#typing.overload "typing.overload"), `get_overloads(process)` will return a sequence of three function objects for the three defined overloads. If called on a function with no overloads, `get_overloads()` returns an empty sequence.
`get_overloads()` can be used for introspecting an overloaded function at runtime.
Added in version 3.11.

typing.clear_overloads()[¶](https://docs.python.org/3/library/typing.html#typing.clear_overloads "Link to this definition")

Clear all registered overloads in the internal registry.
This can be used to reclaim the memory used by the registry.
Added in version 3.11.

@typing.final[¶](https://docs.python.org/3/library/typing.html#typing.final "Link to this definition")

Decorator to indicate final methods and final classes.
Decorating a method with `@final` indicates to a type checker that the method cannot be overridden in a subclass. Decorating a class with `@final` indicates that it cannot be subclassed.
For example:
Copy```
class Base:
    @final
    def done(self) -> None:
        ...
class Sub(Base):
    def done(self) -> None:  # Error reported by type checker
        ...

@final
class Leaf:
    ...
class Other(Leaf):  # Error reported by type checker
    ...

```

There is no runtime checking of these properties. See [**PEP 591**](https://peps.python.org/pep-0591/) for more details.
Added in version 3.8.
Changed in version 3.11: The decorator will now attempt to set a `__final__` attribute to `True` on the decorated object. Thus, a check like `if getattr(obj, "__final__", False)` can be used at runtime to determine whether an object `obj` has been marked as final. If the decorated object does not support setting attributes, the decorator returns the object unchanged without raising an exception.

@typing.no_type_check[¶](https://docs.python.org/3/library/typing.html#typing.no_type_check "Link to this definition")

Decorator to indicate that annotations are not type hints.
This works as a class or function [decorator](https://docs.python.org/3/glossary.html#term-decorator). With a class, it applies recursively to all methods and classes defined in that class (but not to methods defined in its superclasses or subclasses). Type checkers will ignore all annotations in a function or class with this decorator.
`@no_type_check` mutates the decorated object in place.

@typing.no_type_check_decorator[¶](https://docs.python.org/3/library/typing.html#typing.no_type_check_decorator "Link to this definition")

Decorator to give another decorator the [`no_type_check()`](https://docs.python.org/3/library/typing.html#typing.no_type_check "typing.no_type_check") effect.
This wraps the decorator with something that wraps the decorated function in [`no_type_check()`](https://docs.python.org/3/library/typing.html#typing.no_type_check "typing.no_type_check").
Deprecated since version 3.13, will be removed in version 3.15: No type checker ever added support for `@no_type_check_decorator`. It is therefore deprecated, and will be removed in Python 3.15.

@typing.override[¶](https://docs.python.org/3/library/typing.html#typing.override "Link to this definition")

Decorator to indicate that a method in a subclass is intended to override a method or attribute in a superclass.
Type checkers should emit an error if a method decorated with `@override` does not, in fact, override anything. This helps prevent bugs that may occur when a base class is changed without an equivalent change to a child class.
For example:
Copy```
class Base:
    def log_status(self) -> None:
        ...

class Sub(Base):
    @override
    def log_status(self) -> None:  # Okay: overrides Base.log_status
        ...

    @override
    def done(self) -> None:  # Error reported by type checker
        ...

```

There is no runtime checking of this property.
The decorator will attempt to set an `__override__` attribute to `True` on the decorated object. Thus, a check like `if getattr(obj, "__override__", False)` can be used at runtime to determine whether an object `obj` has been marked as an override. If the decorated object does not support setting attributes, the decorator returns the object unchanged without raising an exception.
See [**PEP 698**](https://peps.python.org/pep-0698/) for more details.
Added in version 3.12.

@typing.type_check_only[¶](https://docs.python.org/3/library/typing.html#typing.type_check_only "Link to this definition")

Decorator to mark a class or function as unavailable at runtime.
This decorator is itself not available at runtime. It is mainly intended to mark classes that are defined in type stub files if an implementation returns an instance of a private class:
Copy```
@type_check_only
class Response:  # private or not available at runtime
    code: int
    def get_header(self, name: str) -> str: ...

def fetch_response() -> Response: ...

```

Note that returning instances of private classes is not recommended. It is usually preferable to make such classes public.
### Introspection helpers[¶](https://docs.python.org/3/library/typing.html#introspection-helpers "Link to this heading")

typing.get_type_hints(_obj_ , _globalns =None_, _localns =None_, _include_extras =False_)[¶](https://docs.python.org/3/library/typing.html#typing.get_type_hints "Link to this definition")

Return a dictionary containing type hints for a function, method, module, class object, or other callable object.
This is often the same as `obj.__annotations__`, but this function makes the following changes to the annotations dictionary:
  * Forward references encoded as string literals or [`ForwardRef`](https://docs.python.org/3/library/typing.html#typing.ForwardRef "typing.ForwardRef") objects are handled by evaluating them in _globalns_ , _localns_ , and (where applicable) _obj_ ’s [type parameter](https://docs.python.org/3/reference/compound_stmts.html#type-params) namespace. If _globalns_ or _localns_ is not given, appropriate namespace dictionaries are inferred from _obj_.
  * `None` is replaced with [`types.NoneType`](https://docs.python.org/3/library/types.html#types.NoneType "types.NoneType").
  * If [`@no_type_check`](https://docs.python.org/3/library/typing.html#typing.no_type_check "typing.no_type_check") has been applied to _obj_ , an empty dictionary is returned.
  * If _obj_ is a class `C`, the function returns a dictionary that merges annotations from `C`’s base classes with those on `C` directly. This is done by traversing [`C.__mro__`](https://docs.python.org/3/reference/datamodel.html#type.__mro__ "type.__mro__") and iteratively combining `__annotations__` dictionaries. Annotations on classes appearing earlier in the [method resolution order](https://docs.python.org/3/glossary.html#term-method-resolution-order) always take precedence over annotations on classes appearing later in the method resolution order.
  * The function recursively replaces all occurrences of `Annotated[T, ...]`, `Required[T]`, `NotRequired[T]`, and `ReadOnly[T]` with `T`, unless _include_extras_ is set to `True` (see [`Annotated`](https://docs.python.org/3/library/typing.html#typing.Annotated "typing.Annotated") for more information).


See also [`annotationlib.get_annotations()`](https://docs.python.org/3/library/annotationlib.html#annotationlib.get_annotations "annotationlib.get_annotations"), a lower-level function that returns annotations more directly.
Caution
This function may execute arbitrary code contained in annotations. See [Security implications of introspecting annotations](https://docs.python.org/3/library/annotationlib.html#annotationlib-security) for more information.
Note
If any forward references in the annotations of _obj_ are not resolvable or are not valid Python code, this function will raise an exception such as [`NameError`](https://docs.python.org/3/library/exceptions.html#NameError "NameError"). For example, this can happen with imported [type aliases](https://docs.python.org/3/library/typing.html#type-aliases) that include forward references, or with names imported under [`if TYPE_CHECKING`](https://docs.python.org/3/library/typing.html#typing.TYPE_CHECKING "typing.TYPE_CHECKING").
Note
Calling `get_type_hints()` on an instance is not supported. To retrieve annotations for an instance, call `get_type_hints()` on the instance’s class instead (for example, `get_type_hints(type(obj))`).
Changed in version 3.9: Added `include_extras` parameter as part of [**PEP 593**](https://peps.python.org/pep-0593/). See the documentation on [`Annotated`](https://docs.python.org/3/library/typing.html#typing.Annotated "typing.Annotated") for more information.
Changed in version 3.11: Previously, `Optional[t]` was added for function and method annotations if a default value equal to `None` was set. Now the annotation is returned unchanged.
Changed in version 3.14: Calling `get_type_hints()` on instances is no longer supported. Some instances were accepted in earlier versions as an undocumented implementation detail.

typing.get_origin(_tp_)[¶](https://docs.python.org/3/library/typing.html#typing.get_origin "Link to this definition")

Get the unsubscripted version of a type: for a typing object of the form `X[Y, Z, ...]` return `X`.
If `X` is a typing-module alias for a builtin or [`collections`](https://docs.python.org/3/library/collections.html#module-collections "collections: Container datatypes") class, it will be normalized to the original class. If `X` is an instance of [`ParamSpecArgs`](https://docs.python.org/3/library/typing.html#typing.ParamSpecArgs "typing.ParamSpecArgs") or [`ParamSpecKwargs`](https://docs.python.org/3/library/typing.html#typing.ParamSpecKwargs "typing.ParamSpecKwargs"), return the underlying [`ParamSpec`](https://docs.python.org/3/library/typing.html#typing.ParamSpec "typing.ParamSpec"). Return `None` for unsupported objects.
Examples:
Copy```
assert get_origin(str) is None
assert get_origin(Dict[str, int]) is dict
assert get_origin(Union[int, str]) is Union
assert get_origin(Annotated[str, "metadata"]) is Annotated
P = ParamSpec('P')
assert get_origin(P.args) is P
assert get_origin(P.kwargs) is P

```

Added in version 3.8.

typing.get_args(_tp_)[¶](https://docs.python.org/3/library/typing.html#typing.get_args "Link to this definition")

Get type arguments with all substitutions performed: for a typing object of the form `X[Y, Z, ...]` return `(Y, Z, ...)`.
If `X` is a union or [`Literal`](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal") contained in another generic type, the order of `(Y, Z, ...)` may be different from the order of the original arguments `[Y, Z, ...]` due to type caching. Return `()` for unsupported objects.
Examples:
Copy```
assert get_args(int) == ()
assert get_args(Dict[int, str]) == (int, str)
assert get_args(Union[int, str]) == (int, str)

```

Added in version 3.8.

typing.get_protocol_members(_tp_)[¶](https://docs.python.org/3/library/typing.html#typing.get_protocol_members "Link to this definition")

Return the set of members defined in a [`Protocol`](https://docs.python.org/3/library/typing.html#typing.Protocol "typing.Protocol").
Copy```
>>> from typing import Protocol, get_protocol_members
>>> class P(Protocol):
...     def a(self) -> str: ...
...     b: int
>>> get_protocol_members(P) == frozenset({'a', 'b'})
True

```

Raise [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") for arguments that are not Protocols.
Added in version 3.13.

typing.is_protocol(_tp_)[¶](https://docs.python.org/3/library/typing.html#typing.is_protocol "Link to this definition")

Determine if a type is a [`Protocol`](https://docs.python.org/3/library/typing.html#typing.Protocol "typing.Protocol").
For example:
Copy```
class P(Protocol):
    def a(self) -> str: ...
    b: int

is_protocol(P)    # => True
is_protocol(int)  # => False

```

Added in version 3.13.

typing.is_typeddict(_tp_)[¶](https://docs.python.org/3/library/typing.html#typing.is_typeddict "Link to this definition")

Check if a type is a [`TypedDict`](https://docs.python.org/3/library/typing.html#typing.TypedDict "typing.TypedDict").
For example:
Copy```
class Film(TypedDict):
    title: str
    year: int

assert is_typeddict(Film)
assert not is_typeddict(list | str)
