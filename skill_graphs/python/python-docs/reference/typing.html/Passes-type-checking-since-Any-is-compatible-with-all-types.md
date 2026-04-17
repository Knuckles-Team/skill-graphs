# Passes type checking, since Any is compatible with all types
hash_b(42)
hash_b("foo")

```

Use [`object`](https://docs.python.org/3/library/functions.html#object "object") to indicate that a value could be any type in a typesafe manner. Use [`Any`](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any") to indicate that a value is dynamically typed.
## Nominal vs structural subtyping[¶](https://docs.python.org/3/library/typing.html#nominal-vs-structural-subtyping "Link to this heading")
Initially [**PEP 484**](https://peps.python.org/pep-0484/) defined the Python static type system as using _nominal subtyping_. This means that a class `A` is allowed where a class `B` is expected if and only if `A` is a subclass of `B`.
This requirement previously also applied to abstract base classes, such as [`Iterable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "collections.abc.Iterable"). The problem with this approach is that a class had to be explicitly marked to support them, which is unpythonic and unlike what one would normally do in idiomatic dynamically typed Python code. For example, this conforms to [**PEP 484**](https://peps.python.org/pep-0484/):
Copy```
from collections.abc import Sized, Iterable, Iterator

class Bucket(Sized, Iterable[int]):
    ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[int]: ...

```

[**PEP 544**](https://peps.python.org/pep-0544/) solves this problem by allowing users to write the above code without explicit base classes in the class definition, allowing `Bucket` to be implicitly considered a subtype of both `Sized` and `Iterable[int]` by static type checkers. This is known as _structural subtyping_ (or static duck-typing):
Copy```
from collections.abc import Iterator, Iterable

class Bucket:  # Note: no base classes
    ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[int]: ...

def collect(items: Iterable[int]) -> int: ...
result = collect(Bucket())  # Passes type check

```

Moreover, by subclassing a special class [`Protocol`](https://docs.python.org/3/library/typing.html#typing.Protocol "typing.Protocol"), a user can define new custom protocols to fully enjoy structural subtyping (see examples below).
## Module contents[¶](https://docs.python.org/3/library/typing.html#module-contents "Link to this heading")
The `typing` module defines the following classes, functions and decorators.
### Special typing primitives[¶](https://docs.python.org/3/library/typing.html#special-typing-primitives "Link to this heading")
#### Special types[¶](https://docs.python.org/3/library/typing.html#special-types "Link to this heading")
These can be used as types in annotations. They do not support subscription using `[]`.

typing.Any[¶](https://docs.python.org/3/library/typing.html#typing.Any "Link to this definition")

Special type indicating an unconstrained type.
  * Every type is compatible with `Any`.
  * `Any` is compatible with every type.


Changed in version 3.11: `Any` can now be used as a base class. This can be useful for avoiding type checker errors with classes that can duck type anywhere or are highly dynamic.

typing.AnyStr[¶](https://docs.python.org/3/library/typing.html#typing.AnyStr "Link to this definition")

A [constrained type variable](https://docs.python.org/3/library/typing.html#typing-constrained-typevar).
Definition:
Copy```
AnyStr = TypeVar('AnyStr', str, bytes)

```

`AnyStr` is meant to be used for functions that may accept [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") or [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") arguments but cannot allow the two to mix.
For example:
Copy```
def concat(a: AnyStr, b: AnyStr) -> AnyStr:
    return a + b

concat("foo", "bar")    # OK, output has type 'str'
concat(b"foo", b"bar")  # OK, output has type 'bytes'
concat("foo", b"bar")   # Error, cannot mix str and bytes

```

Note that, despite its name, `AnyStr` has nothing to do with the [`Any`](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any") type, nor does it mean “any string”. In particular, `AnyStr` and `str | bytes` are different from each other and have different use cases:
Copy```
# Invalid use of AnyStr:
# The type variable is used only once in the function signature,
# so cannot be "solved" by the type checker
def greet_bad(cond: bool) -> AnyStr:
    return "hi there!" if cond else b"greetings!"

# The better way of annotating this function:
def greet_proper(cond: bool) -> str | bytes:
    return "hi there!" if cond else b"greetings!"

```

Deprecated since version 3.13, will be removed in version 3.18: Deprecated in favor of the new [type parameter syntax](https://docs.python.org/3/reference/compound_stmts.html#type-params). Use `class A[T: (str, bytes)]: ...` instead of importing `AnyStr`. See [**PEP 695**](https://peps.python.org/pep-0695/) for more details.
In Python 3.16, `AnyStr` will be removed from `typing.__all__`, and deprecation warnings will be emitted at runtime when it is accessed or imported from `typing`. `AnyStr` will be removed from `typing` in Python 3.18.

typing.LiteralString[¶](https://docs.python.org/3/library/typing.html#typing.LiteralString "Link to this definition")

Special type that includes only literal strings.
Any string literal is compatible with `LiteralString`, as is another `LiteralString`. However, an object typed as just `str` is not. A string created by composing `LiteralString`-typed objects is also acceptable as a `LiteralString`.
Example:
Copy```
def run_query(sql: LiteralString) -> None:
    ...

def caller(arbitrary_string: str, literal_string: LiteralString) -> None:
    run_query("SELECT * FROM students")  # OK
    run_query(literal_string)  # OK
    run_query("SELECT * FROM " + literal_string)  # OK
    run_query(arbitrary_string)  # type checker error
    run_query(  # type checker error
        f"SELECT * FROM students WHERE name = {arbitrary_string}"
    )

```

`LiteralString` is useful for sensitive APIs where arbitrary user-generated strings could generate problems. For example, the two cases above that generate type checker errors could be vulnerable to an SQL injection attack.
See [**PEP 675**](https://peps.python.org/pep-0675/) for more details.
Added in version 3.11.

typing.Never[¶](https://docs.python.org/3/library/typing.html#typing.Never "Link to this definition")


typing.NoReturn[¶](https://docs.python.org/3/library/typing.html#typing.NoReturn "Link to this definition")

`Never` and `NoReturn` represent the
They can be used to indicate that a function never returns, such as [`sys.exit()`](https://docs.python.org/3/library/sys.html#sys.exit "sys.exit"):
Copy```
from typing import Never  # or NoReturn

def stop() -> Never:
    raise RuntimeError('no way')

```

Or to define a function that should never be called, as there are no valid arguments, such as [`assert_never()`](https://docs.python.org/3/library/typing.html#typing.assert_never "typing.assert_never"):
Copy```
from typing import Never  # or NoReturn

def never_call_me(arg: Never) -> None:
    pass

def int_or_str(arg: int | str) -> None:
    never_call_me(arg)  # type checker error
    match arg:
        case int():
            print("It's an int")
        case str():
            print("It's a str")
        case _:
            never_call_me(arg)  # OK, arg is of type Never (or NoReturn)

```

`Never` and `NoReturn` have the same meaning in the type system and static type checkers treat both equivalently.
Added in version 3.6.2: Added `NoReturn`.
Added in version 3.11: Added `Never`.

typing.Self[¶](https://docs.python.org/3/library/typing.html#typing.Self "Link to this definition")

Special type to represent the current enclosed class.
For example:
Copy```
from typing import Self, reveal_type

class Foo:
    def return_self(self) -> Self:
        ...
        return self

class SubclassOfFoo(Foo): pass

reveal_type(Foo().return_self())  # Revealed type is "Foo"
reveal_type(SubclassOfFoo().return_self())  # Revealed type is "SubclassOfFoo"

```

This annotation is semantically equivalent to the following, albeit in a more succinct fashion:
Copy```
from typing import TypeVar

Self = TypeVar("Self", bound="Foo")

class Foo:
    def return_self(self: Self) -> Self:
        ...
        return self

```

In general, if something returns `self`, as in the above examples, you should use `Self` as the return annotation. If `Foo.return_self` was annotated as returning `"Foo"`, then the type checker would infer the object returned from `SubclassOfFoo.return_self` as being of type `Foo` rather than `SubclassOfFoo`.
Other common use cases include:
  * [`classmethod`](https://docs.python.org/3/library/functions.html#classmethod "classmethod")s that are used as alternative constructors and return instances of the `cls` parameter.
  * Annotating an [`__enter__()`](https://docs.python.org/3/reference/datamodel.html#object.__enter__ "object.__enter__") method which returns self.


You should not use `Self` as the return annotation if the method is not guaranteed to return an instance of a subclass when the class is subclassed:
Copy```
class Eggs:
    # Self would be an incorrect return annotation here,
    # as the object returned is always an instance of Eggs,
    # even in subclasses
    def returns_eggs(self) -> "Eggs":
        return Eggs()

```

See [**PEP 673**](https://peps.python.org/pep-0673/) for more details.
Added in version 3.11.

typing.TypeAlias[¶](https://docs.python.org/3/library/typing.html#typing.TypeAlias "Link to this definition")

Special annotation for explicitly declaring a [type alias](https://docs.python.org/3/library/typing.html#type-aliases).
For example:
Copy```
from typing import TypeAlias

Factors: TypeAlias = list[int]

```

`TypeAlias` is particularly useful on older Python versions for annotating aliases that make use of forward references, as it can be hard for type checkers to distinguish these from normal variable assignments:
Copy```
from typing import Generic, TypeAlias, TypeVar

T = TypeVar("T")

# "Box" does not exist yet,
# so we have to use quotes for the forward reference on Python <3.12.
# Using ``TypeAlias`` tells the type checker that this is a type alias declaration,
# not a variable assignment to a string.
BoxOfStrings: TypeAlias = "Box[str]"

class Box(Generic[T]):
    @classmethod
    def make_box_of_strings(cls) -> BoxOfStrings: ...

```

See [**PEP 613**](https://peps.python.org/pep-0613/) for more details.
Added in version 3.10.
Deprecated since version 3.12: `TypeAlias` is deprecated in favor of the [`type`](https://docs.python.org/3/reference/simple_stmts.html#type) statement, which creates instances of [`TypeAliasType`](https://docs.python.org/3/library/typing.html#typing.TypeAliasType "typing.TypeAliasType") and which natively supports forward references. Note that while `TypeAlias` and `TypeAliasType` serve similar purposes and have similar names, they are distinct and the latter is not the type of the former. Removal of `TypeAlias` is not currently planned, but users are encouraged to migrate to `type` statements.
#### Special forms[¶](https://docs.python.org/3/library/typing.html#special-forms "Link to this heading")
These can be used as types in annotations. They all support subscription using `[]`, but each has a unique syntax.

_class_ typing.Union[¶](https://docs.python.org/3/library/typing.html#typing.Union "Link to this definition")

Union type; `Union[X, Y]` is equivalent to `X | Y` and means either X or Y.
To define a union, use e.g. `Union[int, str]` or the shorthand `int | str`. Using that shorthand is recommended. Details:
  * The arguments must be types and there must be at least one.
  * Unions of unions are flattened, e.g.:
Copy```
Union[Union[int, str], float] == Union[int, str, float]

```

However, this does not apply to unions referenced through a type alias, to avoid forcing evaluation of the underlying [`TypeAliasType`](https://docs.python.org/3/library/typing.html#typing.TypeAliasType "typing.TypeAliasType"):
Copy```
type A = Union[int, str]
Union[A, float] != Union[int, str, float]

```

  * Unions of a single argument vanish, e.g.:
Copy```
Union[int] == int  # The constructor actually returns int

```

  * Redundant arguments are skipped, e.g.:
Copy```
Union[int, str, int] == Union[int, str] == int | str

```

  * When comparing unions, the argument order is ignored, e.g.:
Copy```
Union[int, str] == Union[str, int]

```

  * You cannot subclass or instantiate a `Union`.
  * You cannot write `Union[X][Y]`.


Changed in version 3.7: Don’t remove explicit subclasses from unions at runtime.
Changed in version 3.10: Unions can now be written as `X | Y`. See [union type expressions](https://docs.python.org/3/library/stdtypes.html#types-union).
Changed in version 3.14: [`types.UnionType`](https://docs.python.org/3/library/types.html#types.UnionType "types.UnionType") is now an alias for `Union`, and both `Union[int, str]` and `int | str` create instances of the same class. To check whether an object is a `Union` at runtime, use `isinstance(obj, Union)`. For compatibility with earlier versions of Python, use `get_origin(obj) is typing.Union or get_origin(obj) is types.UnionType`.

typing.Optional[¶](https://docs.python.org/3/library/typing.html#typing.Optional "Link to this definition")

`Optional[X]` is equivalent to `X | None` (or `Union[X, None]`).
Note that this is not the same concept as an optional argument, which is one that has a default. An optional argument with a default does not require the `Optional` qualifier on its type annotation just because it is optional. For example:
Copy```
def foo(arg: int = 0) -> None:
    ...

```

On the other hand, if an explicit value of `None` is allowed, the use of `Optional` is appropriate, whether the argument is optional or not. For example:
Copy```
def foo(arg: Optional[int] = None) -> None:
    ...

```

Changed in version 3.10: Optional can now be written as `X | None`. See [union type expressions](https://docs.python.org/3/library/stdtypes.html#types-union).

typing.Concatenate[¶](https://docs.python.org/3/library/typing.html#typing.Concatenate "Link to this definition")

Special form for annotating higher-order functions.
`Concatenate` can be used in conjunction with [Callable](https://docs.python.org/3/library/typing.html#annotating-callables) and [`ParamSpec`](https://docs.python.org/3/library/typing.html#typing.ParamSpec "typing.ParamSpec") to annotate a higher-order callable which adds, removes, or transforms parameters of another callable. Usage is in the form `Concatenate[Arg1Type, Arg2Type, ..., ParamSpecVariable]`. `Concatenate` is currently only valid when used as the first argument to a Callable. The last parameter to `Concatenate` must be a `ParamSpec` or ellipsis (`...`).
For example, to annotate a decorator `with_lock` which provides a [`threading.Lock`](https://docs.python.org/3/library/threading.html#threading.Lock "threading.Lock") to the decorated function, `Concatenate` can be used to indicate that `with_lock` expects a callable which takes in a `Lock` as the first argument, and returns a callable with a different type signature. In this case, the [`ParamSpec`](https://docs.python.org/3/library/typing.html#typing.ParamSpec "typing.ParamSpec") indicates that the returned callable’s parameter types are dependent on the parameter types of the callable being passed in:
Copy```
from collections.abc import Callable
from threading import Lock
from typing import Concatenate

# Use this lock to ensure that only one thread is executing a function
# at any time.
my_lock = Lock()

def with_lock[**P, R](f: Callable[Concatenate[Lock, P], R]) -> Callable[P, R]:
    '''A type-safe decorator which provides a lock.'''
    def inner(*args: P.args, **kwargs: P.kwargs) -> R:
        # Provide the lock as the first argument.
        return f(my_lock, *args, **kwargs)
    return inner

@with_lock
def sum_threadsafe(lock: Lock, numbers: list[float]) -> float:
    '''Add a list of numbers together in a thread-safe manner.'''
    with lock:
        return sum(numbers)

# We don't need to pass in the lock ourselves thanks to the decorator.
sum_threadsafe([1.1, 2.2, 3.3])

```

Added in version 3.10.
See also
  * [**PEP 612**](https://peps.python.org/pep-0612/) – Parameter Specification Variables (the PEP which introduced `ParamSpec` and `Concatenate`)
  * [`ParamSpec`](https://docs.python.org/3/library/typing.html#typing.ParamSpec "typing.ParamSpec")
  * [Annotating callable objects](https://docs.python.org/3/library/typing.html#annotating-callables)



typing.Literal[¶](https://docs.python.org/3/library/typing.html#typing.Literal "Link to this definition")

Special typing form to define “literal types”.
`Literal` can be used to indicate to type checkers that the annotated object has a value equivalent to one of the provided literals.
For example:
Copy```
def validate_simple(data: Any) -> Literal[True]:  # always returns True
    ...

type Mode = Literal['r', 'rb', 'w', 'wb']
def open_helper(file: str, mode: Mode) -> str:
    ...

open_helper('/some/path', 'r')      # Passes type check
open_helper('/other/path', 'typo')  # Error in type checker

```

`Literal[...]` cannot be subclassed. At runtime, an arbitrary value is allowed as type argument to `Literal[...]`, but type checkers may impose restrictions. See [**PEP 586**](https://peps.python.org/pep-0586/) for more details about literal types.
Additional details:
  * The arguments must be literal values and there must be at least one.
  * Nested `Literal` types are flattened, e.g.:
Copy```
assert Literal[Literal[1, 2], 3] == Literal[1, 2, 3]

```

However, this does not apply to `Literal` types referenced through a type alias, to avoid forcing evaluation of the underlying [`TypeAliasType`](https://docs.python.org/3/library/typing.html#typing.TypeAliasType "typing.TypeAliasType"):
Copy```
type A = Literal[1, 2]
assert Literal[A, 3] != Literal[1, 2, 3]

```

  * Redundant arguments are skipped, e.g.:
Copy```
assert Literal[1, 2, 1] == Literal[1, 2]

```

  * When comparing literals, the argument order is ignored, e.g.:
Copy```
assert Literal[1, 2] == Literal[2, 1]

```

  * You cannot subclass or instantiate a `Literal`.
  * You cannot write `Literal[X][Y]`.


Added in version 3.8.
Changed in version 3.9.1: `Literal` now de-duplicates parameters. Equality comparisons of `Literal` objects are no longer order dependent. `Literal` objects will now raise a [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") exception during equality comparisons if one of their parameters are not [hashable](https://docs.python.org/3/glossary.html#term-hashable).

typing.ClassVar[¶](https://docs.python.org/3/library/typing.html#typing.ClassVar "Link to this definition")

Special type construct to mark class variables.
As introduced in [**PEP 526**](https://peps.python.org/pep-0526/), a variable annotation wrapped in ClassVar indicates that a given attribute is intended to be used as a class variable and should not be set on instances of that class. Usage:
Copy```
class Starship:
    stats: ClassVar[dict[str, int]] = {} # class variable
    damage: int = 10                     # instance variable

```

`ClassVar` accepts only types and cannot be further subscribed.
`ClassVar` is not a class itself, and should not be used with [`isinstance()`](https://docs.python.org/3/library/functions.html#isinstance "isinstance") or [`issubclass()`](https://docs.python.org/3/library/functions.html#issubclass "issubclass"). `ClassVar` does not change Python runtime behavior, but it can be used by third-party type checkers. For example, a type checker might flag the following code as an error:
Copy```
enterprise_d = Starship(3000)
enterprise_d.stats = {} # Error, setting class variable on instance
Starship.stats = {}     # This is OK

```

Added in version 3.5.3.
Changed in version 3.13: `ClassVar` can now be nested in [`Final`](https://docs.python.org/3/library/typing.html#typing.Final "typing.Final") and vice versa.

typing.Final[¶](https://docs.python.org/3/library/typing.html#typing.Final "Link to this definition")

Special typing construct to indicate final names to type checkers.
Final names cannot be reassigned in any scope. Final names declared in class scopes cannot be overridden in subclasses.
For example:
Copy```
MAX_SIZE: Final = 9000
MAX_SIZE += 1  # Error reported by type checker

class Connection:
    TIMEOUT: Final[int] = 10

class FastConnector(Connection):
    TIMEOUT = 1  # Error reported by type checker

```

There is no runtime checking of these properties. See [**PEP 591**](https://peps.python.org/pep-0591/) for more details.
Added in version 3.8.
Changed in version 3.13: `Final` can now be nested in [`ClassVar`](https://docs.python.org/3/library/typing.html#typing.ClassVar "typing.ClassVar") and vice versa.

typing.Required[¶](https://docs.python.org/3/library/typing.html#typing.Required "Link to this definition")

Special typing construct to mark a [`TypedDict`](https://docs.python.org/3/library/typing.html#typing.TypedDict "typing.TypedDict") key as required.
This is mainly useful for `total=False` TypedDicts. See [`TypedDict`](https://docs.python.org/3/library/typing.html#typing.TypedDict "typing.TypedDict") and [**PEP 655**](https://peps.python.org/pep-0655/) for more details.
Added in version 3.11.

typing.NotRequired[¶](https://docs.python.org/3/library/typing.html#typing.NotRequired "Link to this definition")

Special typing construct to mark a [`TypedDict`](https://docs.python.org/3/library/typing.html#typing.TypedDict "typing.TypedDict") key as potentially missing.
See [`TypedDict`](https://docs.python.org/3/library/typing.html#typing.TypedDict "typing.TypedDict") and [**PEP 655**](https://peps.python.org/pep-0655/) for more details.
Added in version 3.11.

typing.ReadOnly[¶](https://docs.python.org/3/library/typing.html#typing.ReadOnly "Link to this definition")

A special typing construct to mark an item of a [`TypedDict`](https://docs.python.org/3/library/typing.html#typing.TypedDict "typing.TypedDict") as read-only.
For example:
Copy```
class Movie(TypedDict):
   title: ReadOnly[str]
   year: int

def mutate_movie(m: Movie) -> None:
   m["year"] = 1999  # allowed
   m["title"] = "The Matrix"  # typechecker error

```

There is no runtime checking for this property.
See [`TypedDict`](https://docs.python.org/3/library/typing.html#typing.TypedDict "typing.TypedDict") and [**PEP 705**](https://peps.python.org/pep-0705/) for more details.
Added in version 3.13.

typing.Annotated[¶](https://docs.python.org/3/library/typing.html#typing.Annotated "Link to this definition")

Special typing form to add context-specific metadata to an annotation.
Add metadata `x` to a given type `T` by using the annotation `Annotated[T, x]`. Metadata added using `Annotated` can be used by static analysis tools or at runtime. At runtime, the metadata is stored in a `__metadata__` attribute.
If a library or tool encounters an annotation `Annotated[T, x]` and has no special logic for the metadata, it should ignore the metadata and simply treat the annotation as `T`. As such, `Annotated` can be useful for code that wants to use annotations for purposes outside Python’s static typing system.
Using `Annotated[T, x]` as an annotation still allows for static typechecking of `T`, as type checkers will simply ignore the metadata `x`. In this way, `Annotated` differs from the [`@no_type_check`](https://docs.python.org/3/library/typing.html#typing.no_type_check "typing.no_type_check") decorator, which can also be used for adding annotations outside the scope of the typing system, but completely disables typechecking for a function or class.
The responsibility of how to interpret the metadata lies with the tool or library encountering an `Annotated` annotation. A tool or library encountering an `Annotated` type can scan through the metadata elements to determine if they are of interest (e.g., using [`isinstance()`](https://docs.python.org/3/library/functions.html#isinstance "isinstance")).

Annotated[<type>, <metadata>]

Here is an example of how you might use `Annotated` to add metadata to type annotations if you were doing range analysis:
Copy```
@dataclass
class ValueRange:
    lo: int
    hi: int

T1 = Annotated[int, ValueRange(-10, 5)]
T2 = Annotated[T1, ValueRange(-20, 3)]

```

The first argument to `Annotated` must be a valid type. Multiple metadata elements can be supplied as `Annotated` supports variadic arguments. The order of the metadata elements is preserved and matters for equality checks:
Copy```
@dataclass
class ctype:
     kind: str

a1 = Annotated[int, ValueRange(3, 10), ctype("char")]
a2 = Annotated[int, ctype("char"), ValueRange(3, 10)]

assert a1 != a2  # Order matters

```

It is up to the tool consuming the annotations to decide whether the client is allowed to add multiple metadata elements to one annotation and how to merge those annotations.
Nested `Annotated` types are flattened. The order of the metadata elements starts with the innermost annotation:
Copy```
assert Annotated[Annotated[int, ValueRange(3, 10)], ctype("char")] == Annotated[
    int, ValueRange(3, 10), ctype("char")
]

```

However, this does not apply to `Annotated` types referenced through a type alias, to avoid forcing evaluation of the underlying [`TypeAliasType`](https://docs.python.org/3/library/typing.html#typing.TypeAliasType "typing.TypeAliasType"):
Copy```
type From3To10[T] = Annotated[T, ValueRange(3, 10)]
assert Annotated[From3To10[int], ctype("char")] != Annotated[
   int, ValueRange(3, 10), ctype("char")
]

```

Duplicated metadata elements are not removed:
Copy```
assert Annotated[int, ValueRange(3, 10)] != Annotated[
    int, ValueRange(3, 10), ValueRange(3, 10)
]

```

`Annotated` can be used with nested and generic aliases:
> Copy```
@dataclass
class MaxLen:
    value: int

type Vec[T] = Annotated[list[tuple[T, T]], MaxLen(10)]
