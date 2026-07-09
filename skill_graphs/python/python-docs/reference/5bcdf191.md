# Can be anything with an __abs__ method
def print_abs[T: SupportsAbs](arg: T) -> None:
    print("Absolute value:", abs(arg))

U = TypeVar('U', bound=str|bytes)  # Can be any subtype of the union str|bytes
V = TypeVar('V', bound=SupportsAbs)  # Can be anything with an __abs__ method

```

Using a _constrained_ type variable, however, means that the `TypeVar` can only ever be solved as being exactly one of the constraints given:
Copy```
a = concatenate('one', 'two')
reveal_type(a)  # revealed type is str

b = concatenate(StringSubclass('one'), StringSubclass('two'))
reveal_type(b)  # revealed type is str, despite StringSubclass being passed in

c = concatenate('one', b'two')  # error: type variable 'A' can be either str or bytes in a function call, but not both

```

At runtime, `isinstance(x, T)` will raise [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError").

__name__[¶](https://docs.python.org/3/library/typing.html#typing.TypeVar.__name__ "Link to this definition")

The name of the type variable.

__covariant__[¶](https://docs.python.org/3/library/typing.html#typing.TypeVar.__covariant__ "Link to this definition")

Whether the type var has been explicitly marked as covariant.

__contravariant__[¶](https://docs.python.org/3/library/typing.html#typing.TypeVar.__contravariant__ "Link to this definition")

Whether the type var has been explicitly marked as contravariant.

__infer_variance__[¶](https://docs.python.org/3/library/typing.html#typing.TypeVar.__infer_variance__ "Link to this definition")

Whether the type variable’s variance should be inferred by type checkers.
Added in version 3.12.

__bound__[¶](https://docs.python.org/3/library/typing.html#typing.TypeVar.__bound__ "Link to this definition")

The upper bound of the type variable, if any.
Changed in version 3.12: For type variables created through [type parameter syntax](https://docs.python.org/3/reference/compound_stmts.html#type-params), the bound is evaluated only when the attribute is accessed, not when the type variable is created (see [Lazy evaluation](https://docs.python.org/3/reference/executionmodel.html#lazy-evaluation)).

evaluate_bound()[¶](https://docs.python.org/3/library/typing.html#typing.TypeVar.evaluate_bound "Link to this definition")

An [evaluate function](https://docs.python.org/3/glossary.html#term-evaluate-function) corresponding to the [`__bound__`](https://docs.python.org/3/library/typing.html#typing.TypeVar.__bound__ "typing.TypeVar.__bound__") attribute. When called directly, this method supports only the [`VALUE`](https://docs.python.org/3/library/annotationlib.html#annotationlib.Format.VALUE "annotationlib.Format.VALUE") format, which is equivalent to accessing the `__bound__` attribute directly, but the method object can be passed to [`annotationlib.call_evaluate_function()`](https://docs.python.org/3/library/annotationlib.html#annotationlib.call_evaluate_function "annotationlib.call_evaluate_function") to evaluate the value in a different format.
Added in version 3.14.

__constraints__[¶](https://docs.python.org/3/library/typing.html#typing.TypeVar.__constraints__ "Link to this definition")

A tuple containing the constraints of the type variable, if any.
Changed in version 3.12: For type variables created through [type parameter syntax](https://docs.python.org/3/reference/compound_stmts.html#type-params), the constraints are evaluated only when the attribute is accessed, not when the type variable is created (see [Lazy evaluation](https://docs.python.org/3/reference/executionmodel.html#lazy-evaluation)).

evaluate_constraints()[¶](https://docs.python.org/3/library/typing.html#typing.TypeVar.evaluate_constraints "Link to this definition")

An [evaluate function](https://docs.python.org/3/glossary.html#term-evaluate-function) corresponding to the [`__constraints__`](https://docs.python.org/3/library/typing.html#typing.TypeVar.__constraints__ "typing.TypeVar.__constraints__") attribute. When called directly, this method supports only the [`VALUE`](https://docs.python.org/3/library/annotationlib.html#annotationlib.Format.VALUE "annotationlib.Format.VALUE") format, which is equivalent to accessing the `__constraints__` attribute directly, but the method object can be passed to [`annotationlib.call_evaluate_function()`](https://docs.python.org/3/library/annotationlib.html#annotationlib.call_evaluate_function "annotationlib.call_evaluate_function") to evaluate the value in a different format.
Added in version 3.14.

__default__[¶](https://docs.python.org/3/library/typing.html#typing.TypeVar.__default__ "Link to this definition")

The default value of the type variable, or [`typing.NoDefault`](https://docs.python.org/3/library/typing.html#typing.NoDefault "typing.NoDefault") if it has no default.
Added in version 3.13.

evaluate_default()[¶](https://docs.python.org/3/library/typing.html#typing.TypeVar.evaluate_default "Link to this definition")

An [evaluate function](https://docs.python.org/3/glossary.html#term-evaluate-function) corresponding to the [`__default__`](https://docs.python.org/3/library/typing.html#typing.TypeVar.__default__ "typing.TypeVar.__default__") attribute. When called directly, this method supports only the [`VALUE`](https://docs.python.org/3/library/annotationlib.html#annotationlib.Format.VALUE "annotationlib.Format.VALUE") format, which is equivalent to accessing the `__default__` attribute directly, but the method object can be passed to [`annotationlib.call_evaluate_function()`](https://docs.python.org/3/library/annotationlib.html#annotationlib.call_evaluate_function "annotationlib.call_evaluate_function") to evaluate the value in a different format.
Added in version 3.14.

has_default()[¶](https://docs.python.org/3/library/typing.html#typing.TypeVar.has_default "Link to this definition")

Return whether or not the type variable has a default value. This is equivalent to checking whether [`__default__`](https://docs.python.org/3/library/typing.html#typing.TypeVar.__default__ "typing.TypeVar.__default__") is not the [`typing.NoDefault`](https://docs.python.org/3/library/typing.html#typing.NoDefault "typing.NoDefault") singleton, except that it does not force evaluation of the [lazily evaluated](https://docs.python.org/3/reference/executionmodel.html#lazy-evaluation) default value.
Added in version 3.13.
Changed in version 3.12: Type variables can now be declared using the [type parameter](https://docs.python.org/3/reference/compound_stmts.html#type-params) syntax introduced by [**PEP 695**](https://peps.python.org/pep-0695/). The `infer_variance` parameter was added.
Changed in version 3.13: Support for default values was added.

_class_ typing.TypeVarTuple(_name_ , _*_ , _default =typing.NoDefault_)[¶](https://docs.python.org/3/library/typing.html#typing.TypeVarTuple "Link to this definition")

Type variable tuple. A specialized form of [type variable](https://docs.python.org/3/library/typing.html#typevar) that enables _variadic_ generics.
Type variable tuples can be declared in [type parameter lists](https://docs.python.org/3/reference/compound_stmts.html#type-params) using a single asterisk (`*`) before the name:
Copy```
def move_first_element_to_last[T, *Ts](tup: tuple[T, *Ts]) -> tuple[*Ts, T]:
    return (*tup[1:], tup[0])

```

Or by explicitly invoking the `TypeVarTuple` constructor:
Copy```
T = TypeVar("T")
Ts = TypeVarTuple("Ts")

def move_first_element_to_last(tup: tuple[T, *Ts]) -> tuple[*Ts, T]:
    return (*tup[1:], tup[0])

```

A normal type variable enables parameterization with a single type. A type variable tuple, in contrast, allows parameterization with an _arbitrary_ number of types by acting like an _arbitrary_ number of type variables wrapped in a tuple. For example:
Copy```
