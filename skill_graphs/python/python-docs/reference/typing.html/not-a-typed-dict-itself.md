# not a typed dict itself
assert not is_typeddict(TypedDict)

```

Added in version 3.10.

_class_ typing.ForwardRef[¶](https://docs.python.org/3/library/typing.html#typing.ForwardRef "Link to this definition")

Class used for internal typing representation of string forward references.
For example, `List["SomeClass"]` is implicitly transformed into `List[ForwardRef("SomeClass")]`. `ForwardRef` should not be instantiated by a user, but may be used by introspection tools.
Note
[**PEP 585**](https://peps.python.org/pep-0585/) generic types such as `list["SomeClass"]` will not be implicitly transformed into `list[ForwardRef("SomeClass")]` and thus will not automatically resolve to `list[SomeClass]`.
Added in version 3.7.4.
Changed in version 3.14: This is now an alias for [`annotationlib.ForwardRef`](https://docs.python.org/3/library/annotationlib.html#annotationlib.ForwardRef "annotationlib.ForwardRef"). Several undocumented behaviors of this class have been changed; for example, after a `ForwardRef` has been evaluated, the evaluated value is no longer cached.

typing.evaluate_forward_ref(_forward_ref_ , _*_ , _owner =None_, _globals =None_, _locals =None_, _type_params =None_, _format =annotationlib.Format.VALUE_)[¶](https://docs.python.org/3/library/typing.html#typing.evaluate_forward_ref "Link to this definition")

Evaluate an [`annotationlib.ForwardRef`](https://docs.python.org/3/library/annotationlib.html#annotationlib.ForwardRef "annotationlib.ForwardRef") as a [type hint](https://docs.python.org/3/glossary.html#term-type-hint).
This is similar to calling [`annotationlib.ForwardRef.evaluate()`](https://docs.python.org/3/library/annotationlib.html#annotationlib.ForwardRef.evaluate "annotationlib.ForwardRef.evaluate"), but unlike that method, `evaluate_forward_ref()` also recursively evaluates forward references nested within the type hint.
See the documentation for [`annotationlib.ForwardRef.evaluate()`](https://docs.python.org/3/library/annotationlib.html#annotationlib.ForwardRef.evaluate "annotationlib.ForwardRef.evaluate") for the meaning of the _owner_ , _globals_ , _locals_ , _type_params_ , and _format_ parameters.
Caution
This function may execute arbitrary code contained in annotations. See [Security implications of introspecting annotations](https://docs.python.org/3/library/annotationlib.html#annotationlib-security) for more information.
Added in version 3.14.

typing.NoDefault[¶](https://docs.python.org/3/library/typing.html#typing.NoDefault "Link to this definition")

A sentinel object used to indicate that a type parameter has no default value. For example:
Copy```
>>> T = TypeVar("T")
>>> T.__default__ is typing.NoDefault
True
>>> S = TypeVar("S", default=None)
>>> S.__default__ is None
True

```

Added in version 3.13.
### Constant[¶](https://docs.python.org/3/library/typing.html#constant "Link to this heading")

typing.TYPE_CHECKING[¶](https://docs.python.org/3/library/typing.html#typing.TYPE_CHECKING "Link to this definition")

A special constant that is assumed to be `True` by 3rd party static type checkers. It’s `False` at runtime.
A module which is expensive to import, and which only contain types used for typing annotations, can be safely imported inside an `if TYPE_CHECKING:` block. This prevents the module from actually being imported at runtime; annotations aren’t eagerly evaluated (see [**PEP 649**](https://peps.python.org/pep-0649/)) so using undefined symbols in annotations is harmless–as long as you don’t later examine them. Your static type analysis tool will set `TYPE_CHECKING` to `True` during static type analysis, which means the module will be imported and the types will be checked properly during such analysis.
Usage:
Copy```
if TYPE_CHECKING:
    import expensive_mod

def fun(arg: expensive_mod.SomeType) -> None:
    local_var: expensive_mod.AnotherType = other_fun()

```

If you occasionally need to examine type annotations at runtime which may contain undefined symbols, use [`annotationlib.get_annotations()`](https://docs.python.org/3/library/annotationlib.html#annotationlib.get_annotations "annotationlib.get_annotations") with a `format` parameter of [`annotationlib.Format.STRING`](https://docs.python.org/3/library/annotationlib.html#annotationlib.Format.STRING "annotationlib.Format.STRING") or [`annotationlib.Format.FORWARDREF`](https://docs.python.org/3/library/annotationlib.html#annotationlib.Format.FORWARDREF "annotationlib.Format.FORWARDREF") to safely retrieve the annotations without raising [`NameError`](https://docs.python.org/3/library/exceptions.html#NameError "NameError").
Added in version 3.5.2.
### Deprecated aliases[¶](https://docs.python.org/3/library/typing.html#deprecated-aliases "Link to this heading")
This module defines several deprecated aliases to pre-existing standard library classes. These were originally included in the `typing` module in order to support parameterizing these generic classes using `[]`. However, the aliases became redundant in Python 3.9 when the corresponding pre-existing classes were enhanced to support `[]` (see [**PEP 585**](https://peps.python.org/pep-0585/)).
The redundant types are deprecated as of Python 3.9. However, while the aliases may be removed at some point, removal of these aliases is not currently planned. As such, no deprecation warnings are currently issued by the interpreter for these aliases.
If at some point it is decided to remove these deprecated aliases, a deprecation warning will be issued by the interpreter for at least two releases prior to removal. The aliases are guaranteed to remain in the `typing` module without deprecation warnings until at least Python 3.14.
Type checkers are encouraged to flag uses of the deprecated types if the program they are checking targets a minimum Python version of 3.9 or newer.
#### Aliases to built-in types[¶](https://docs.python.org/3/library/typing.html#aliases-to-built-in-types "Link to this heading")

_class_ typing.Dict(_dict, MutableMapping[KT, VT]_)[¶](https://docs.python.org/3/library/typing.html#typing.Dict "Link to this definition")

Deprecated alias to [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict").
Note that to annotate arguments, it is preferred to use an abstract collection type such as [`Mapping`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "collections.abc.Mapping") rather than to use [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict") or `typing.Dict`.
Deprecated since version 3.9: [`builtins.dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict") now supports subscripting (`[]`). See [**PEP 585**](https://peps.python.org/pep-0585/) and [Generic Alias Type](https://docs.python.org/3/library/stdtypes.html#types-genericalias).

_class_ typing.List(_list, MutableSequence[T]_)[¶](https://docs.python.org/3/library/typing.html#typing.List "Link to this definition")

Deprecated alias to [`list`](https://docs.python.org/3/library/stdtypes.html#list "list").
Note that to annotate arguments, it is preferred to use an abstract collection type such as [`Sequence`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "collections.abc.Sequence") or [`Iterable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "collections.abc.Iterable") rather than to use [`list`](https://docs.python.org/3/library/stdtypes.html#list "list") or `typing.List`.
Deprecated since version 3.9: [`builtins.list`](https://docs.python.org/3/library/stdtypes.html#list "list") now supports subscripting (`[]`). See [**PEP 585**](https://peps.python.org/pep-0585/) and [Generic Alias Type](https://docs.python.org/3/library/stdtypes.html#types-genericalias).

_class_ typing.Set(_set, MutableSet[T]_)[¶](https://docs.python.org/3/library/typing.html#typing.Set "Link to this definition")

Deprecated alias to [`builtins.set`](https://docs.python.org/3/library/stdtypes.html#set "set").
Note that to annotate arguments, it is preferred to use an abstract collection type such as [`collections.abc.Set`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Set "collections.abc.Set") rather than to use [`set`](https://docs.python.org/3/library/stdtypes.html#set "set") or [`typing.Set`](https://docs.python.org/3/library/typing.html#typing.Set "typing.Set").
Deprecated since version 3.9: [`builtins.set`](https://docs.python.org/3/library/stdtypes.html#set "set") now supports subscripting (`[]`). See [**PEP 585**](https://peps.python.org/pep-0585/) and [Generic Alias Type](https://docs.python.org/3/library/stdtypes.html#types-genericalias).

_class_ typing.FrozenSet(_frozenset, AbstractSet[T_co]_)[¶](https://docs.python.org/3/library/typing.html#typing.FrozenSet "Link to this definition")

Deprecated alias to [`builtins.frozenset`](https://docs.python.org/3/library/stdtypes.html#frozenset "frozenset").
Deprecated since version 3.9: [`builtins.frozenset`](https://docs.python.org/3/library/stdtypes.html#frozenset "frozenset") now supports subscripting (`[]`). See [**PEP 585**](https://peps.python.org/pep-0585/) and [Generic Alias Type](https://docs.python.org/3/library/stdtypes.html#types-genericalias).

typing.Tuple[¶](https://docs.python.org/3/library/typing.html#typing.Tuple "Link to this definition")

Deprecated alias for [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "tuple").
[`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "tuple") and `Tuple` are special-cased in the type system; see [Annotating tuples](https://docs.python.org/3/library/typing.html#annotating-tuples) for more details.
Deprecated since version 3.9: [`builtins.tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "tuple") now supports subscripting (`[]`). See [**PEP 585**](https://peps.python.org/pep-0585/) and [Generic Alias Type](https://docs.python.org/3/library/stdtypes.html#types-genericalias).

_class_ typing.Type(_Generic[CT_co]_)[¶](https://docs.python.org/3/library/typing.html#typing.Type "Link to this definition")

Deprecated alias to [`type`](https://docs.python.org/3/library/functions.html#type "type").
See [The type of class objects](https://docs.python.org/3/library/typing.html#type-of-class-objects) for details on using [`type`](https://docs.python.org/3/library/functions.html#type "type") or `typing.Type` in type annotations.
Added in version 3.5.2.
Deprecated since version 3.9: [`builtins.type`](https://docs.python.org/3/library/functions.html#type "type") now supports subscripting (`[]`). See [**PEP 585**](https://peps.python.org/pep-0585/) and [Generic Alias Type](https://docs.python.org/3/library/stdtypes.html#types-genericalias).
#### Aliases to types in [`collections`](https://docs.python.org/3/library/collections.html#module-collections "collections: Container datatypes")[¶](https://docs.python.org/3/library/typing.html#aliases-to-types-in-collections "Link to this heading")

_class_ typing.DefaultDict(_collections.defaultdict, MutableMapping[KT, VT]_)[¶](https://docs.python.org/3/library/typing.html#typing.DefaultDict "Link to this definition")

Deprecated alias to [`collections.defaultdict`](https://docs.python.org/3/library/collections.html#collections.defaultdict "collections.defaultdict").
Added in version 3.5.2.
Deprecated since version 3.9: [`collections.defaultdict`](https://docs.python.org/3/library/collections.html#collections.defaultdict "collections.defaultdict") now supports subscripting (`[]`). See [**PEP 585**](https://peps.python.org/pep-0585/) and [Generic Alias Type](https://docs.python.org/3/library/stdtypes.html#types-genericalias).

_class_ typing.OrderedDict(_collections.OrderedDict, MutableMapping[KT, VT]_)[¶](https://docs.python.org/3/library/typing.html#typing.OrderedDict "Link to this definition")

Deprecated alias to [`collections.OrderedDict`](https://docs.python.org/3/library/collections.html#collections.OrderedDict "collections.OrderedDict").
Added in version 3.7.2.
Deprecated since version 3.9: [`collections.OrderedDict`](https://docs.python.org/3/library/collections.html#collections.OrderedDict "collections.OrderedDict") now supports subscripting (`[]`). See [**PEP 585**](https://peps.python.org/pep-0585/) and [Generic Alias Type](https://docs.python.org/3/library/stdtypes.html#types-genericalias).

_class_ typing.ChainMap(_collections.ChainMap, MutableMapping[KT, VT]_)[¶](https://docs.python.org/3/library/typing.html#typing.ChainMap "Link to this definition")

Deprecated alias to [`collections.ChainMap`](https://docs.python.org/3/library/collections.html#collections.ChainMap "collections.ChainMap").
Added in version 3.6.1.
Deprecated since version 3.9: [`collections.ChainMap`](https://docs.python.org/3/library/collections.html#collections.ChainMap "collections.ChainMap") now supports subscripting (`[]`). See [**PEP 585**](https://peps.python.org/pep-0585/) and [Generic Alias Type](https://docs.python.org/3/library/stdtypes.html#types-genericalias).

_class_ typing.Counter(_collections.Counter, Dict[T, int]_)[¶](https://docs.python.org/3/library/typing.html#typing.Counter "Link to this definition")

Deprecated alias to [`collections.Counter`](https://docs.python.org/3/library/collections.html#collections.Counter "collections.Counter").
Added in version 3.6.1.
Deprecated since version 3.9: [`collections.Counter`](https://docs.python.org/3/library/collections.html#collections.Counter "collections.Counter") now supports subscripting (`[]`). See [**PEP 585**](https://peps.python.org/pep-0585/) and [Generic Alias Type](https://docs.python.org/3/library/stdtypes.html#types-genericalias).

_class_ typing.Deque(_deque, MutableSequence[T]_)[¶](https://docs.python.org/3/library/typing.html#typing.Deque "Link to this definition")

Deprecated alias to [`collections.deque`](https://docs.python.org/3/library/collections.html#collections.deque "collections.deque").
Added in version 3.6.1.
Deprecated since version 3.9: [`collections.deque`](https://docs.python.org/3/library/collections.html#collections.deque "collections.deque") now supports subscripting (`[]`). See [**PEP 585**](https://peps.python.org/pep-0585/) and [Generic Alias Type](https://docs.python.org/3/library/stdtypes.html#types-genericalias).
#### Aliases to other concrete types[¶](https://docs.python.org/3/library/typing.html#aliases-to-other-concrete-types "Link to this heading")

_class_ typing.Pattern[¶](https://docs.python.org/3/library/typing.html#typing.Pattern "Link to this definition")


_class_ typing.Match[¶](https://docs.python.org/3/library/typing.html#typing.Match "Link to this definition")

Deprecated aliases corresponding to the return types from [`re.compile()`](https://docs.python.org/3/library/re.html#re.compile "re.compile") and [`re.match()`](https://docs.python.org/3/library/re.html#re.match "re.match").
These types (and the corresponding functions) are generic over [`AnyStr`](https://docs.python.org/3/library/typing.html#typing.AnyStr "typing.AnyStr"). `Pattern` can be specialised as `Pattern[str]` or `Pattern[bytes]`; `Match` can be specialised as `Match[str]` or `Match[bytes]`.
Deprecated since version 3.9: Classes `Pattern` and `Match` from [`re`](https://docs.python.org/3/library/re.html#module-re "re: Regular expression operations.") now support `[]`. See [**PEP 585**](https://peps.python.org/pep-0585/) and [Generic Alias Type](https://docs.python.org/3/library/stdtypes.html#types-genericalias).

_class_ typing.Text[¶](https://docs.python.org/3/library/typing.html#typing.Text "Link to this definition")

Deprecated alias for [`str`](https://docs.python.org/3/library/stdtypes.html#str "str").
`Text` is provided to supply a forward compatible path for Python 2 code: in Python 2, `Text` is an alias for `unicode`.
Use `Text` to indicate that a value must contain a unicode string in a manner that is compatible with both Python 2 and Python 3:
Copy```
def add_unicode_checkmark(text: Text) -> Text:
    return text + u' \u2713'

```

Added in version 3.5.2.
Deprecated since version 3.11: Python 2 is no longer supported, and most type checkers also no longer support type checking Python 2 code. Removal of the alias is not currently planned, but users are encouraged to use [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") instead of `Text`.
#### Aliases to container ABCs in [`collections.abc`](https://docs.python.org/3/library/collections.abc.html#module-collections.abc "collections.abc: Abstract base classes for containers")[¶](https://docs.python.org/3/library/typing.html#aliases-to-container-abcs-in-collections-abc "Link to this heading")

_class_ typing.AbstractSet(_Collection[T_co]_)[¶](https://docs.python.org/3/library/typing.html#typing.AbstractSet "Link to this definition")

Deprecated alias to [`collections.abc.Set`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Set "collections.abc.Set").
Deprecated since version 3.9: [`collections.abc.Set`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Set "collections.abc.Set") now supports subscripting (`[]`). See [**PEP 585**](https://peps.python.org/pep-0585/) and [Generic Alias Type](https://docs.python.org/3/library/stdtypes.html#types-genericalias).

_class_ typing.ByteString(_Sequence[int]_)[¶](https://docs.python.org/3/library/typing.html#typing.ByteString "Link to this definition")

Deprecated alias to [`collections.abc.ByteString`](https://docs.python.org/3/library/collections.abc.html#collections.abc.ByteString "collections.abc.ByteString").
Use `isinstance(obj, collections.abc.Buffer)` to test if `obj` implements the [buffer protocol](https://docs.python.org/3/c-api/buffer.html#bufferobjects) at runtime. For use in type annotations, either use [`Buffer`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Buffer "collections.abc.Buffer") or a union that explicitly specifies the types your code supports (e.g., `bytes | bytearray | memoryview`).
`ByteString` was originally intended to be an abstract class that would serve as a supertype of both [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") and [`bytearray`](https://docs.python.org/3/library/stdtypes.html#bytearray "bytearray"). However, since the ABC never had any methods, knowing that an object was an instance of `ByteString` never actually told you anything useful about the object. Other common buffer types such as [`memoryview`](https://docs.python.org/3/library/stdtypes.html#memoryview "memoryview") were also never understood as subtypes of `ByteString` (either at runtime or by static type checkers).
See [**PEP 688**](https://peps.python.org/pep-0688/#current-options) for more details.
Deprecated since version 3.9, will be removed in version 3.17.

_class_ typing.Collection(_Sized, Iterable[T_co], Container[T_co]_)[¶](https://docs.python.org/3/library/typing.html#typing.Collection "Link to this definition")

Deprecated alias to [`collections.abc.Collection`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Collection "collections.abc.Collection").
Added in version 3.6.
Deprecated since version 3.9: [`collections.abc.Collection`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Collection "collections.abc.Collection") now supports subscripting (`[]`). See [**PEP 585**](https://peps.python.org/pep-0585/) and [Generic Alias Type](https://docs.python.org/3/library/stdtypes.html#types-genericalias).

_class_ typing.Container(_Generic[T_co]_)[¶](https://docs.python.org/3/library/typing.html#typing.Container "Link to this definition")

Deprecated alias to [`collections.abc.Container`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Container "collections.abc.Container").
Deprecated since version 3.9: [`collections.abc.Container`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Container "collections.abc.Container") now supports subscripting (`[]`). See [**PEP 585**](https://peps.python.org/pep-0585/) and [Generic Alias Type](https://docs.python.org/3/library/stdtypes.html#types-genericalias).

_class_ typing.ItemsView(_MappingView, AbstractSet[tuple[KT_co, VT_co]]_)[¶](https://docs.python.org/3/library/typing.html#typing.ItemsView "Link to this definition")

Deprecated alias to [`collections.abc.ItemsView`](https://docs.python.org/3/library/collections.abc.html#collections.abc.ItemsView "collections.abc.ItemsView").
Deprecated since version 3.9: [`collections.abc.ItemsView`](https://docs.python.org/3/library/collections.abc.html#collections.abc.ItemsView "collections.abc.ItemsView") now supports subscripting (`[]`). See [**PEP 585**](https://peps.python.org/pep-0585/) and [Generic Alias Type](https://docs.python.org/3/library/stdtypes.html#types-genericalias).

_class_ typing.KeysView(_MappingView, AbstractSet[KT_co]_)[¶](https://docs.python.org/3/library/typing.html#typing.KeysView "Link to this definition")

Deprecated alias to [`collections.abc.KeysView`](https://docs.python.org/3/library/collections.abc.html#collections.abc.KeysView "collections.abc.KeysView").
Deprecated since version 3.9: [`collections.abc.KeysView`](https://docs.python.org/3/library/collections.abc.html#collections.abc.KeysView "collections.abc.KeysView") now supports subscripting (`[]`). See [**PEP 585**](https://peps.python.org/pep-0585/) and [Generic Alias Type](https://docs.python.org/3/library/stdtypes.html#types-genericalias).

_class_ typing.Mapping(_Collection[KT], Generic[KT, VT_co]_)[¶](https://docs.python.org/3/library/typing.html#typing.Mapping "Link to this definition")

Deprecated alias to [`collections.abc.Mapping`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "collections.abc.Mapping").
Deprecated since version 3.9: [`collections.abc.Mapping`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "collections.abc.Mapping") now supports subscripting (`[]`). See [**PEP 585**](https://peps.python.org/pep-0585/) and [Generic Alias Type](https://docs.python.org/3/library/stdtypes.html#types-genericalias).

_class_ typing.MappingView(_Sized_)[¶](https://docs.python.org/3/library/typing.html#typing.MappingView "Link to this definition")

Deprecated alias to [`collections.abc.MappingView`](https://docs.python.org/3/library/collections.abc.html#collections.abc.MappingView "collections.abc.MappingView").
Deprecated since version 3.9: [`collections.abc.MappingView`](https://docs.python.org/3/library/collections.abc.html#collections.abc.MappingView "collections.abc.MappingView") now supports subscripting (`[]`). See [**PEP 585**](https://peps.python.org/pep-0585/) and [Generic Alias Type](https://docs.python.org/3/library/stdtypes.html#types-genericalias).

_class_ typing.MutableMapping(_Mapping[KT, VT]_)[¶](https://docs.python.org/3/library/typing.html#typing.MutableMapping "Link to this definition")

Deprecated alias to [`collections.abc.MutableMapping`](https://docs.python.org/3/library/collections.abc.html#collections.abc.MutableMapping "collections.abc.MutableMapping").
Deprecated since version 3.9: [`collections.abc.MutableMapping`](https://docs.python.org/3/library/collections.abc.html#collections.abc.MutableMapping "collections.abc.MutableMapping") now supports subscripting (`[]`). See [**PEP 585**](https://peps.python.org/pep-0585/) and [Generic Alias Type](https://docs.python.org/3/library/stdtypes.html#types-genericalias).

_class_ typing.MutableSequence(_Sequence[T]_)[¶](https://docs.python.org/3/library/typing.html#typing.MutableSequence "Link to this definition")

Deprecated alias to [`collections.abc.MutableSequence`](https://docs.python.org/3/library/collections.abc.html#collections.abc.MutableSequence "collections.abc.MutableSequence").
Deprecated since version 3.9: [`collections.abc.MutableSequence`](https://docs.python.org/3/library/collections.abc.html#collections.abc.MutableSequence "collections.abc.MutableSequence") now supports subscripting (`[]`). See [**PEP 585**](https://peps.python.org/pep-0585/) and [Generic Alias Type](https://docs.python.org/3/library/stdtypes.html#types-genericalias).

_class_ typing.MutableSet(_AbstractSet[T]_)[¶](https://docs.python.org/3/library/typing.html#typing.MutableSet "Link to this definition")

Deprecated alias to [`collections.abc.MutableSet`](https://docs.python.org/3/library/collections.abc.html#collections.abc.MutableSet "collections.abc.MutableSet").
Deprecated since version 3.9: [`collections.abc.MutableSet`](https://docs.python.org/3/library/collections.abc.html#collections.abc.MutableSet "collections.abc.MutableSet") now supports subscripting (`[]`). See [**PEP 585**](https://peps.python.org/pep-0585/) and [Generic Alias Type](https://docs.python.org/3/library/stdtypes.html#types-genericalias).

_class_ typing.Sequence(_Reversible[T_co], Collection[T_co]_)[¶](https://docs.python.org/3/library/typing.html#typing.Sequence "Link to this definition")

Deprecated alias to [`collections.abc.Sequence`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "collections.abc.Sequence").
Deprecated since version 3.9: [`collections.abc.Sequence`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "collections.abc.Sequence") now supports subscripting (`[]`). See [**PEP 585**](https://peps.python.org/pep-0585/) and [Generic Alias Type](https://docs.python.org/3/library/stdtypes.html#types-genericalias).

_class_ typing.ValuesView(_MappingView, Collection[_VT_co]_)[¶](https://docs.python.org/3/library/typing.html#typing.ValuesView "Link to this definition")

Deprecated alias to [`collections.abc.ValuesView`](https://docs.python.org/3/library/collections.abc.html#collections.abc.ValuesView "collections.abc.ValuesView").
Deprecated since version 3.9: [`collections.abc.ValuesView`](https://docs.python.org/3/library/collections.abc.html#collections.abc.ValuesView "collections.abc.ValuesView") now supports subscripting (`[]`). See [**PEP 585**](https://peps.python.org/pep-0585/) and [Generic Alias Type](https://docs.python.org/3/library/stdtypes.html#types-genericalias).
#### Aliases to asynchronous ABCs in [`collections.abc`](https://docs.python.org/3/library/collections.abc.html#module-collections.abc "collections.abc: Abstract base classes for containers")[¶](https://docs.python.org/3/library/typing.html#aliases-to-asynchronous-abcs-in-collections-abc "Link to this heading")

_class_ typing.Coroutine(_Awaitable[ReturnType], Generic[YieldType, SendType, ReturnType]_)[¶](https://docs.python.org/3/library/typing.html#typing.Coroutine "Link to this definition")

Deprecated alias to [`collections.abc.Coroutine`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Coroutine "collections.abc.Coroutine").
See [Annotating generators and coroutines](https://docs.python.org/3/library/typing.html#annotating-generators-and-coroutines) for details on using [`collections.abc.Coroutine`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Coroutine "collections.abc.Coroutine") and `typing.Coroutine` in type annotations.
Added in version 3.5.3.
Deprecated since version 3.9: [`collections.abc.Coroutine`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Coroutine "collections.abc.Coroutine") now supports subscripting (`[]`). See [**PEP 585**](https://peps.python.org/pep-0585/) and [Generic Alias Type](https://docs.python.org/3/library/stdtypes.html#types-genericalias).

_class_ typing.AsyncGenerator(_AsyncIterator[YieldType], Generic[YieldType, SendType]_)[¶](https://docs.python.org/3/library/typing.html#typing.AsyncGenerator "Link to this definition")

Deprecated alias to [`collections.abc.AsyncGenerator`](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncGenerator "collections.abc.AsyncGenerator").
See [Annotating generators and coroutines](https://docs.python.org/3/library/typing.html#annotating-generators-and-coroutines) for details on using [`collections.abc.AsyncGenerator`](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncGenerator "collections.abc.AsyncGenerator") and `typing.AsyncGenerator` in type annotations.
Added in version 3.6.1.
Deprecated since version 3.9: [`collections.abc.AsyncGenerator`](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncGenerator "collections.abc.AsyncGenerator") now supports subscripting (`[]`). See [**PEP 585**](https://peps.python.org/pep-0585/) and [Generic Alias Type](https://docs.python.org/3/library/stdtypes.html#types-genericalias).
Changed in version 3.13: The `SendType` parameter now has a default.

_class_ typing.AsyncIterable(_Generic[T_co]_)[¶](https://docs.python.org/3/library/typing.html#typing.AsyncIterable "Link to this definition")

Deprecated alias to [`collections.abc.AsyncIterable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterable "collections.abc.AsyncIterable").
Added in version 3.5.2.
Deprecated since version 3.9: [`collections.abc.AsyncIterable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterable "collections.abc.AsyncIterable") now supports subscripting (`[]`). See [**PEP 585**](https://peps.python.org/pep-0585/) and [Generic Alias Type](https://docs.python.org/3/library/stdtypes.html#types-genericalias).

_class_ typing.AsyncIterator(_AsyncIterable[T_co]_)[¶](https://docs.python.org/3/library/typing.html#typing.AsyncIterator "Link to this definition")

Deprecated alias to [`collections.abc.AsyncIterator`](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator "collections.abc.AsyncIterator").
Added in version 3.5.2.
Deprecated since version 3.9: [`collections.abc.AsyncIterator`](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator "collections.abc.AsyncIterator") now supports subscripting (`[]`). See [**PEP 585**](https://peps.python.org/pep-0585/) and [Generic Alias Type](https://docs.python.org/3/library/stdtypes.html#types-genericalias).

_class_ typing.Awaitable(_Generic[T_co]_)[¶](https://docs.python.org/3/library/typing.html#typing.Awaitable "Link to this definition")

Deprecated alias to [`collections.abc.Awaitable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Awaitable "collections.abc.Awaitable").
Added in version 3.5.2.
Deprecated since version 3.9: [`collections.abc.Awaitable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Awaitable "collections.abc.Awaitable") now supports subscripting (`[]`). See [**PEP 585**](https://peps.python.org/pep-0585/) and [Generic Alias Type](https://docs.python.org/3/library/stdtypes.html#types-genericalias).
#### Aliases to other ABCs in [`collections.abc`](https://docs.python.org/3/library/collections.abc.html#module-collections.abc "collections.abc: Abstract base classes for containers")[¶](https://docs.python.org/3/library/typing.html#aliases-to-other-abcs-in-collections-abc "Link to this heading")

_class_ typing.Iterable(_Generic[T_co]_)[¶](https://docs.python.org/3/library/typing.html#typing.Iterable "Link to this definition")

Deprecated alias to [`collections.abc.Iterable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "collections.abc.Iterable").
Deprecated since version 3.9: [`collections.abc.Iterable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "collections.abc.Iterable") now supports subscripting (`[]`). See [**PEP 585**](https://peps.python.org/pep-0585/) and [Generic Alias Type](https://docs.python.org/3/library/stdtypes.html#types-genericalias).

_class_ typing.Iterator(_Iterable[T_co]_)[¶](https://docs.python.org/3/library/typing.html#typing.Iterator "Link to this definition")

Deprecated alias to [`collections.abc.Iterator`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "collections.abc.Iterator").
Deprecated since version 3.9: [`collections.abc.Iterator`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "collections.abc.Iterator") now supports subscripting (`[]`). See [**PEP 585**](https://peps.python.org/pep-0585/) and [Generic Alias Type](https://docs.python.org/3/library/stdtypes.html#types-genericalias).

typing.Callable[¶](https://docs.python.org/3/library/typing.html#typing.Callable "Link to this definition")

Deprecated alias to [`collections.abc.Callable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "collections.abc.Callable").
See [Annotating callable objects](https://docs.python.org/3/library/typing.html#annotating-callables) for details on how to use [`collections.abc.Callable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "collections.abc.Callable") and `typing.Callable` in type annotations.
Deprecated since version 3.9: [`collections.abc.Callable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "collections.abc.Callable") now supports subscripting (`[]`). See [**PEP 585**](https://peps.python.org/pep-0585/) and [Generic Alias Type](https://docs.python.org/3/library/stdtypes.html#types-genericalias).
Changed in version 3.10: `Callable` now supports [`ParamSpec`](https://docs.python.org/3/library/typing.html#typing.ParamSpec "typing.ParamSpec") and [`Concatenate`](https://docs.python.org/3/library/typing.html#typing.Concatenate "typing.Concatenate"). See [**PEP 612**](https://peps.python.org/pep-0612/) for more details.

_class_ typing.Generator(_Iterator[YieldType], Generic[YieldType, SendType, ReturnType]_)[¶](https://docs.python.org/3/library/typing.html#typing.Generator "Link to this definition")

Deprecated alias to [`collections.abc.Generator`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Generator "collections.abc.Generator").
See [Annotating generators and coroutines](https://docs.python.org/3/library/typing.html#annotating-generators-and-coroutines) for details on using [`collections.abc.Generator`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Generator "collections.abc.Generator") and `typing.Generator` in type annotations.
Deprecated since version 3.9: [`collections.abc.Generator`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Generator "collections.abc.Generator") now supports subscripting (`[]`). See [**PEP 585**](https://peps.python.org/pep-0585/) and [Generic Alias Type](https://docs.python.org/3/library/stdtypes.html#types-genericalias).
Changed in version 3.13: Default values for the send and return types were added.

_class_ typing.Hashable[¶](https://docs.python.org/3/library/typing.html#typing.Hashable "Link to this definition")

Deprecated alias to [`collections.abc.Hashable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Hashable "collections.abc.Hashable").
Deprecated since version 3.12: Use [`collections.abc.Hashable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Hashable "collections.abc.Hashable") directly instead.

_class_ typing.Reversible(_Iterable[T_co]_)[¶](https://docs.python.org/3/library/typing.html#typing.Reversible "Link to this definition")

Deprecated alias to [`collections.abc.Reversible`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Reversible "collections.abc.Reversible").
Deprecated since version 3.9: [`collections.abc.Reversible`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Reversible "collections.abc.Reversible") now supports subscripting (`[]`). See [**PEP 585**](https://peps.python.org/pep-0585/) and [Generic Alias Type](https://docs.python.org/3/library/stdtypes.html#types-genericalias).

_class_ typing.Sized[¶](https://docs.python.org/3/library/typing.html#typing.Sized "Link to this definition")

Deprecated alias to [`collections.abc.Sized`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sized "collections.abc.Sized").
Deprecated since version 3.12: Use [`collections.abc.Sized`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sized "collections.abc.Sized") directly instead.
#### Aliases to [`contextlib`](https://docs.python.org/3/library/contextlib.html#module-contextlib "contextlib: Utilities for with-statement contexts.") ABCs[¶](https://docs.python.org/3/library/typing.html#aliases-to-contextlib-abcs "Link to this heading")

_class_ typing.ContextManager(_Generic[T_co, ExitT_co]_)[¶](https://docs.python.org/3/library/typing.html#typing.ContextManager "Link to this definition")

Deprecated alias to [`contextlib.AbstractContextManager`](https://docs.python.org/3/library/contextlib.html#contextlib.AbstractContextManager "contextlib.AbstractContextManager").
The first type parameter, `T_co`, represents the type returned by the [`__enter__()`](https://docs.python.org/3/reference/datamodel.html#object.__enter__ "object.__enter__") method. The optional second type parameter, `ExitT_co`, which defaults to `bool | None`, represents the type returned by the [`__exit__()`](https://docs.python.org/3/reference/datamodel.html#object.__exit__ "object.__exit__") method.
Added in version 3.5.4.
Deprecated since version 3.9: [`contextlib.AbstractContextManager`](https://docs.python.org/3/library/contextlib.html#contextlib.AbstractContextManager "contextlib.AbstractContextManager") now supports subscripting (`[]`). See [**PEP 585**](https://peps.python.org/pep-0585/) and [Generic Alias Type](https://docs.python.org/3/library/stdtypes.html#types-genericalias).
Changed in version 3.13: Added the optional second type parameter, `ExitT_co`.

_class_ typing.AsyncContextManager(_Generic[T_co, AExitT_co]_)[¶](https://docs.python.org/3/library/typing.html#typing.AsyncContextManager "Link to this definition")

Deprecated alias to [`contextlib.AbstractAsyncContextManager`](https://docs.python.org/3/library/contextlib.html#contextlib.AbstractAsyncContextManager "contextlib.AbstractAsyncContextManager").
The first type parameter, `T_co`, represents the type returned by the [`__aenter__()`](https://docs.python.org/3/reference/datamodel.html#object.__aenter__ "object.__aenter__") method. The optional second type parameter, `AExitT_co`, which defaults to `bool | None`, represents the type returned by the [`__aexit__()`](https://docs.python.org/3/reference/datamodel.html#object.__aexit__ "object.__aexit__") method.
Added in version 3.6.2.
Deprecated since version 3.9: [`contextlib.AbstractAsyncContextManager`](https://docs.python.org/3/library/contextlib.html#contextlib.AbstractAsyncContextManager "contextlib.AbstractAsyncContextManager") now supports subscripting (`[]`). See [**PEP 585**](https://peps.python.org/pep-0585/) and [Generic Alias Type](https://docs.python.org/3/library/stdtypes.html#types-genericalias).
Changed in version 3.13: Added the optional second type parameter, `AExitT_co`.
## Deprecation Timeline of Major Features[¶](https://docs.python.org/3/library/typing.html#deprecation-timeline-of-major-features "Link to this heading")
Certain features in `typing` are deprecated and may be removed in a future version of Python. The following table summarizes major deprecations for your convenience. This is subject to change, and not all deprecations are listed.
Feature | Deprecated in | Projected removal | PEP/issue
---|---|---|---
`typing` versions of standard collections | 3.9 | Undecided (see [Deprecated aliases](https://docs.python.org/3/library/typing.html#deprecated-aliases) for more information) | [**PEP 585**](https://peps.python.org/pep-0585/)
[`typing.ByteString`](https://docs.python.org/3/library/typing.html#typing.ByteString "typing.ByteString") | 3.9 | 3.17 |
[`typing.Text`](https://docs.python.org/3/library/typing.html#typing.Text "typing.Text") | 3.11 | Undecided |
[`typing.Hashable`](https://docs.python.org/3/library/typing.html#typing.Hashable "typing.Hashable") and [`typing.Sized`](https://docs.python.org/3/library/typing.html#typing.Sized "typing.Sized") | 3.12 | Undecided |
[`typing.TypeAlias`](https://docs.python.org/3/library/typing.html#typing.TypeAlias "typing.TypeAlias") | 3.12 | Undecided | [**PEP 695**](https://peps.python.org/pep-0695/)
[`@typing.no_type_check_decorator`](https://docs.python.org/3/library/typing.html#typing.no_type_check_decorator "typing.no_type_check_decorator") | 3.13 | 3.15 |
[`typing.AnyStr`](https://docs.python.org/3/library/typing.html#typing.AnyStr "typing.AnyStr") | 3.13 | 3.18 |
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`typing` — Support for type hints](https://docs.python.org/3/library/typing.html)
    * [Specification for the Python Type System](https://docs.python.org/3/library/typing.html#specification-for-the-python-type-system)
    * [Type aliases](https://docs.python.org/3/library/typing.html#type-aliases)
    * [NewType](https://docs.python.org/3/library/typing.html#newtype)
    * [Annotating callable objects](https://docs.python.org/3/library/typing.html#annotating-callable-objects)
    * [Generics](https://docs.python.org/3/library/typing.html#generics)
    * [Annotating tuples](https://docs.python.org/3/library/typing.html#annotating-tuples)
    * [The type of class objects](https://docs.python.org/3/library/typing.html#the-type-of-class-objects)
    * [Annotating generators and coroutines](https://docs.python.org/3/library/typing.html#annotating-generators-and-coroutines)
    * [User-defined generic types](https://docs.python.org/3/library/typing.html#user-defined-generic-types)
    * [The `Any` type](https://docs.python.org/3/library/typing.html#the-any-type)
    * [Nominal vs structural subtyping](https://docs.python.org/3/library/typing.html#nominal-vs-structural-subtyping)
    * [Module contents](https://docs.python.org/3/library/typing.html#module-contents)
      * [Special typing primitives](https://docs.python.org/3/library/typing.html#special-typing-primitives)
        * [Special types](https://docs.python.org/3/library/typing.html#special-types)
        * [Special forms](https://docs.python.org/3/library/typing.html#special-forms)
        * [Building generic types and type aliases](https://docs.python.org/3/library/typing.html#building-generic-types-and-type-aliases)
        * [Other special directives](https://docs.python.org/3/library/typing.html#other-special-directives)
      * [Protocols](https://docs.python.org/3/library/typing.html#protocols)
      * [ABCs and Protocols for working with I/O](https://docs.python.org/3/library/typing.html#abcs-and-protocols-for-working-with-i-o)
      * [Functions and decorators](https://docs.python.org/3/library/typing.html#functions-and-decorators)
      * [Introspection helpers](https://docs.python.org/3/library/typing.html#introspection-helpers)
      * [Constant](https://docs.python.org/3/library/typing.html#constant)
      * [Deprecated aliases](https://docs.python.org/3/library/typing.html#deprecated-aliases)
        * [Aliases to built-in types](https://docs.python.org/3/library/typing.html#aliases-to-built-in-types)
        * [Aliases to types in `collections`](https://docs.python.org/3/library/typing.html#aliases-to-types-in-collections)
        * [Aliases to other concrete types](https://docs.python.org/3/library/typing.html#aliases-to-other-concrete-types)
        * [Aliases to container ABCs in `collections.abc`](https://docs.python.org/3/library/typing.html#aliases-to-container-abcs-in-collections-abc)
        * [Aliases to asynchronous ABCs in `collections.abc`](https://docs.python.org/3/library/typing.html#aliases-to-asynchronous-abcs-in-collections-abc)
        * [Aliases to other ABCs in `collections.abc`](https://docs.python.org/3/library/typing.html#aliases-to-other-abcs-in-collections-abc)
        * [Aliases to `contextlib` ABCs](https://docs.python.org/3/library/typing.html#aliases-to-contextlib-abcs)
    * [Deprecation Timeline of Major Features](https://docs.python.org/3/library/typing.html#deprecation-timeline-of-major-features)


#### Previous topic
[Development Tools](https://docs.python.org/3/library/development.html "previous chapter")
#### Next topic
[`pydoc` — Documentation generator and online help system](https://docs.python.org/3/library/pydoc.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=typing+%E2%80%94+Support+for+type+hints&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ftyping.html&pagesource=library%2Ftyping.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/pydoc.html "pydoc — Documentation generator and online help system") |
  * [previous](https://docs.python.org/3/library/development.html "Development Tools") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Development Tools](https://docs.python.org/3/library/development.html) »
  * [`typing` — Support for type hints](https://docs.python.org/3/library/typing.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
