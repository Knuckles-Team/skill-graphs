# A functional syntax is also supported
Employee = NamedTuple('Employee', [('name', str), ('id', int)])

```

Changed in version 3.6: Added support for [**PEP 526**](https://peps.python.org/pep-0526/) variable annotation syntax.
Changed in version 3.6.1: Added support for default values, methods, and docstrings.
Changed in version 3.8: The `_field_types` and `__annotations__` attributes are now regular dictionaries instead of instances of `OrderedDict`.
Changed in version 3.9: Removed the `_field_types` attribute in favor of the more standard `__annotations__` attribute which has the same information.
Changed in version 3.9: `NamedTuple` is now a function rather than a class. It can still be used as a class base, as described above.
Changed in version 3.11: Added support for generic namedtuples.
Changed in version 3.14: Using [`super()`](https://docs.python.org/3/library/functions.html#super "super") (and the `__class__` [closure variable](https://docs.python.org/3/glossary.html#term-closure-variable)) in methods of `NamedTuple` subclasses is unsupported and causes a [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError").
Deprecated since version 3.13, will be removed in version 3.15: The undocumented keyword argument syntax for creating NamedTuple classes (`NT = NamedTuple("NT", x=int)`) is deprecated, and will be disallowed in 3.15. Use the class-based syntax or the functional syntax instead.
Deprecated since version 3.13, will be removed in version 3.15: When using the functional syntax to create a NamedTuple class, failing to pass a value to the ‘fields’ parameter (`NT = NamedTuple("NT")`) is deprecated. Passing `None` to the ‘fields’ parameter (`NT = NamedTuple("NT", None)`) is also deprecated. Both will be disallowed in Python 3.15. To create a NamedTuple class with 0 fields, use `class NT(NamedTuple): pass` or `NT = NamedTuple("NT", [])`.

_class_ typing.NewType(_name_ , _tp_)[¶](https://docs.python.org/3/library/typing.html#typing.NewType "Link to this definition")

Helper class to create low-overhead [distinct types](https://docs.python.org/3/library/typing.html#distinct).
A `NewType` is considered a distinct type by a typechecker. At runtime, however, calling a `NewType` returns its argument unchanged.
Usage:
Copy```
UserId = NewType('UserId', int)  # Declare the NewType "UserId"
first_user = UserId(1)  # "UserId" returns the argument unchanged at runtime

```


__module__[¶](https://docs.python.org/3/library/typing.html#typing.NewType.__module__ "Link to this definition")

The name of the module in which the new type is defined.

__name__[¶](https://docs.python.org/3/library/typing.html#typing.NewType.__name__ "Link to this definition")

The name of the new type.

__supertype__[¶](https://docs.python.org/3/library/typing.html#typing.NewType.__supertype__ "Link to this definition")

The type that the new type is based on.
Added in version 3.5.2.
Changed in version 3.10: `NewType` is now a class rather than a function.

_class_ typing.Protocol(_Generic_)[¶](https://docs.python.org/3/library/typing.html#typing.Protocol "Link to this definition")

Base class for protocol classes.
Protocol classes are defined like this:
Copy```
class Proto(Protocol):
    def meth(self) -> int:
        ...

```

Such classes are primarily used with static type checkers that recognize structural subtyping (static duck-typing), for example:
Copy```
class C:
    def meth(self) -> int:
        return 0

def func(x: Proto) -> int:
    return x.meth()

func(C())  # Passes static type check

```

See [**PEP 544**](https://peps.python.org/pep-0544/) for more details. Protocol classes decorated with [`runtime_checkable()`](https://docs.python.org/3/library/typing.html#typing.runtime_checkable "typing.runtime_checkable") (described later) act as simple-minded runtime protocols that check only the presence of given attributes, ignoring their type signatures. Protocol classes without this decorator cannot be used as the second argument to [`isinstance()`](https://docs.python.org/3/library/functions.html#isinstance "isinstance") or [`issubclass()`](https://docs.python.org/3/library/functions.html#issubclass "issubclass").
Protocol classes can be generic, for example:
Copy```
class GenProto[T](Protocol):
    def meth(self) -> T:
        ...

```

In code that needs to be compatible with Python 3.11 or older, generic Protocols can be written as follows:
Copy```
T = TypeVar("T")

class GenProto(Protocol[T]):
    def meth(self) -> T:
        ...

```

Added in version 3.8.

@typing.runtime_checkable[¶](https://docs.python.org/3/library/typing.html#typing.runtime_checkable "Link to this definition")

Mark a protocol class as a runtime protocol.
Such a protocol can be used with [`isinstance()`](https://docs.python.org/3/library/functions.html#isinstance "isinstance") and [`issubclass()`](https://docs.python.org/3/library/functions.html#issubclass "issubclass"). This allows a simple-minded structural check, very similar to “one trick ponies” in [`collections.abc`](https://docs.python.org/3/library/collections.abc.html#module-collections.abc "collections.abc: Abstract base classes for containers") such as [`Iterable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "collections.abc.Iterable"). For example:
Copy```
@runtime_checkable
class Closable(Protocol):
    def close(self): ...

assert isinstance(open('/some/file'), Closable)

@runtime_checkable
class Named(Protocol):
    name: str

import threading
assert isinstance(threading.Thread(name='Bob'), Named)

```

This decorator raises [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") when applied to a non-protocol class.
Note
`runtime_checkable()` will check only the presence of the required methods or attributes, not their type signatures or types. For example, [`ssl.SSLObject`](https://docs.python.org/3/library/ssl.html#ssl.SSLObject "ssl.SSLObject") is a class, therefore it passes an [`issubclass()`](https://docs.python.org/3/library/functions.html#issubclass "issubclass") check against [Callable](https://docs.python.org/3/library/typing.html#annotating-callables). However, the `ssl.SSLObject.__init__` method exists only to raise a [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") with a more informative message, therefore making it impossible to call (instantiate) `ssl.SSLObject`.
Note
An [`isinstance()`](https://docs.python.org/3/library/functions.html#isinstance "isinstance") check against a runtime-checkable protocol can be surprisingly slow compared to an `isinstance()` check against a non-protocol class. Consider using alternative idioms such as [`hasattr()`](https://docs.python.org/3/library/functions.html#hasattr "hasattr") calls for structural checks in performance-sensitive code.
Added in version 3.8.
Changed in version 3.12: The internal implementation of [`isinstance()`](https://docs.python.org/3/library/functions.html#isinstance "isinstance") checks against runtime-checkable protocols now uses [`inspect.getattr_static()`](https://docs.python.org/3/library/inspect.html#inspect.getattr_static "inspect.getattr_static") to look up attributes (previously, [`hasattr()`](https://docs.python.org/3/library/functions.html#hasattr "hasattr") was used). As a result, some objects which used to be considered instances of a runtime-checkable protocol may no longer be considered instances of that protocol on Python 3.12+, and vice versa. Most users are unlikely to be affected by this change.
Changed in version 3.12: The members of a runtime-checkable protocol are now considered “frozen” at runtime as soon as the class has been created. Monkey-patching attributes onto a runtime-checkable protocol will still work, but will have no impact on [`isinstance()`](https://docs.python.org/3/library/functions.html#isinstance "isinstance") checks comparing objects to the protocol. See [What’s new in Python 3.12](https://docs.python.org/3/whatsnew/3.12.html#whatsnew-typing-py312) for more details.

_class_ typing.TypedDict(_dict_)[¶](https://docs.python.org/3/library/typing.html#typing.TypedDict "Link to this definition")

Special construct to add type hints to a dictionary. At runtime “`TypedDict` instances” are simply [`dicts`](https://docs.python.org/3/library/stdtypes.html#dict "dict").
`TypedDict` declares a dictionary type that expects all of its instances to have a certain set of keys, where each key is associated with a value of a consistent type. This expectation is not checked at runtime but is only enforced by type checkers. Usage:
Copy```
class Point2D(TypedDict):
    x: int
    y: int
    label: str

a: Point2D = {'x': 1, 'y': 2, 'label': 'good'}  # OK
b: Point2D = {'z': 3, 'label': 'bad'}           # Fails type check

assert Point2D(x=1, y=2, label='first') == dict(x=1, y=2, label='first')

```

An alternative way to create a `TypedDict` is by using function-call syntax. The second argument must be a literal [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict"):
Copy```
Point2D = TypedDict('Point2D', {'x': int, 'y': int, 'label': str})

```

This functional syntax allows defining keys which are not valid [identifiers](https://docs.python.org/3/reference/lexical_analysis.html#identifiers), for example because they are keywords or contain hyphens, or when key names must not be [mangled](https://docs.python.org/3/reference/expressions.html#private-name-mangling) like regular private names:
Copy```
# raises SyntaxError
class Point2D(TypedDict):
    in: int  # 'in' is a keyword
    x-y: int  # name with hyphens

class Definition(TypedDict):
    __schema: str  # mangled to `_Definition__schema`

# OK, functional syntax
Point2D = TypedDict('Point2D', {'in': int, 'x-y': int})
Definition = TypedDict('Definition', {'__schema': str})  # not mangled

```

By default, all keys must be present in a `TypedDict`. It is possible to mark individual keys as non-required using [`NotRequired`](https://docs.python.org/3/library/typing.html#typing.NotRequired "typing.NotRequired"):
Copy```
class Point2D(TypedDict):
    x: int
    y: int
    label: NotRequired[str]
