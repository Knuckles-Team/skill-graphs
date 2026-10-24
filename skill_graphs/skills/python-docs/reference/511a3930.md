## Introspecting callables with the Signature object[¶](https://docs.python.org/3/library/inspect.html#introspecting-callables-with-the-signature-object "Link to this heading")
Added in version 3.3.
The [`Signature`](https://docs.python.org/3/library/inspect.html#inspect.Signature "inspect.Signature") object represents the call signature of a callable object and its return annotation. To retrieve a `Signature` object, use the `signature()` function.

inspect.signature(_callable_ , _*_ , _follow_wrapped =True_, _globals =None_, _locals =None_, _eval_str =False_, _annotation_format =Format.VALUE_)[¶](https://docs.python.org/3/library/inspect.html#inspect.signature "Link to this definition")

Return a [`Signature`](https://docs.python.org/3/library/inspect.html#inspect.Signature "inspect.Signature") object for the given _callable_ :
Copy```
>>> from inspect import signature
>>> def foo(a, *, b:int, **kwargs):
...     pass

>>> sig = signature(foo)

>>> str(sig)
'(a, *, b: int, **kwargs)'

>>> str(sig.parameters['b'])
'b: int'

>>> sig.parameters['b'].annotation
<class 'int'>

```

Accepts a wide range of Python callables, from plain functions and classes to [`functools.partial()`](https://docs.python.org/3/library/functools.html#functools.partial "functools.partial") objects.
If some of the annotations are strings (e.g., because `from __future__ import annotations` was used), `signature()` will attempt to automatically un-stringize the annotations using [`annotationlib.get_annotations()`](https://docs.python.org/3/library/annotationlib.html#annotationlib.get_annotations "annotationlib.get_annotations"). The _globals_ , _locals_ , and _eval_str_ parameters are passed into `annotationlib.get_annotations()` when resolving the annotations; see the documentation for `annotationlib.get_annotations()` for instructions on how to use these parameters. A member of the [`annotationlib.Format`](https://docs.python.org/3/library/annotationlib.html#annotationlib.Format "annotationlib.Format") enum can be passed to the _annotation_format_ parameter to control the format of the returned annotations. For example, use `annotation_format=annotationlib.Format.STRING` to return annotations in string format.
Raises [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") if no signature can be provided, and [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") if that type of object is not supported. Also, if the annotations are stringized, and _eval_str_ is not false, the `eval()` call(s) to un-stringize the annotations in [`annotationlib.get_annotations()`](https://docs.python.org/3/library/annotationlib.html#annotationlib.get_annotations "annotationlib.get_annotations") could potentially raise any kind of exception.
A slash (/) in the signature of a function denotes that the parameters prior to it are positional-only. For more info, see [the FAQ entry on positional-only parameters](https://docs.python.org/3/faq/programming.html#faq-positional-only-arguments).
Changed in version 3.5: The _follow_wrapped_ parameter was added. Pass `False` to get a signature of _callable_ specifically (`callable.__wrapped__` will not be used to unwrap decorated callables.)
Changed in version 3.10: The _globals_ , _locals_ , and _eval_str_ parameters were added.
Changed in version 3.14: The _annotation_format_ parameter was added.
Note
Some callables may not be introspectable in certain implementations of Python. For example, in CPython, some built-in functions defined in C provide no metadata about their arguments.
**CPython implementation detail:** If the passed object has a `__signature__` attribute, we may use it to create the signature. The exact semantics are an implementation detail and are subject to unannounced changes. Consult the source code for current semantics.

_class_ inspect.Signature(_parameters =None_, _*_ , _return_annotation =Signature.empty_)[¶](https://docs.python.org/3/library/inspect.html#inspect.Signature "Link to this definition")

A `Signature` object represents the call signature of a function and its return annotation. For each parameter accepted by the function it stores a [`Parameter`](https://docs.python.org/3/library/inspect.html#inspect.Parameter "inspect.Parameter") object in its [`parameters`](https://docs.python.org/3/library/inspect.html#inspect.Signature.parameters "inspect.Signature.parameters") collection.
The optional _parameters_ argument is a sequence of [`Parameter`](https://docs.python.org/3/library/inspect.html#inspect.Parameter "inspect.Parameter") objects, which is validated to check that there are no parameters with duplicate names, and that the parameters are in the right order, i.e. positional-only first, then positional-or-keyword, and that parameters with defaults follow parameters without defaults.
The optional _return_annotation_ argument can be an arbitrary Python object. It represents the “return” annotation of the callable.
`Signature` objects are _immutable_. Use [`Signature.replace()`](https://docs.python.org/3/library/inspect.html#inspect.Signature.replace "inspect.Signature.replace") or [`copy.replace()`](https://docs.python.org/3/library/copy.html#copy.replace "copy.replace") to make a modified copy.
Changed in version 3.5: `Signature` objects are now picklable and [hashable](https://docs.python.org/3/glossary.html#term-hashable).

empty[¶](https://docs.python.org/3/library/inspect.html#inspect.Signature.empty "Link to this definition")

A special class-level marker to specify absence of a return annotation.

parameters[¶](https://docs.python.org/3/library/inspect.html#inspect.Signature.parameters "Link to this definition")

An ordered mapping of parameters’ names to the corresponding [`Parameter`](https://docs.python.org/3/library/inspect.html#inspect.Parameter "inspect.Parameter") objects. Parameters appear in strict definition order, including keyword-only parameters.
Changed in version 3.7: Python only explicitly guaranteed that it preserved the declaration order of keyword-only parameters as of version 3.7, although in practice this order had always been preserved in Python 3.

return_annotation[¶](https://docs.python.org/3/library/inspect.html#inspect.Signature.return_annotation "Link to this definition")

The “return” annotation for the callable. If the callable has no “return” annotation, this attribute is set to [`Signature.empty`](https://docs.python.org/3/library/inspect.html#inspect.Signature.empty "inspect.Signature.empty").

bind(_* args_, _** kwargs_)[¶](https://docs.python.org/3/library/inspect.html#inspect.Signature.bind "Link to this definition")

Create a mapping from positional and keyword arguments to parameters. Returns [`BoundArguments`](https://docs.python.org/3/library/inspect.html#inspect.BoundArguments "inspect.BoundArguments") if `*args` and `**kwargs` match the signature, or raises a [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError").

bind_partial(_* args_, _** kwargs_)[¶](https://docs.python.org/3/library/inspect.html#inspect.Signature.bind_partial "Link to this definition")

Works the same way as [`Signature.bind()`](https://docs.python.org/3/library/inspect.html#inspect.Signature.bind "inspect.Signature.bind"), but allows the omission of some required arguments (mimics [`functools.partial()`](https://docs.python.org/3/library/functools.html#functools.partial "functools.partial") behavior.) Returns [`BoundArguments`](https://docs.python.org/3/library/inspect.html#inspect.BoundArguments "inspect.BoundArguments"), or raises a [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") if the passed arguments do not match the signature.

replace(_*[, parameters][, return_annotation]_)[¶](https://docs.python.org/3/library/inspect.html#inspect.Signature.replace "Link to this definition")

Create a new `Signature` instance based on the instance `replace()` was invoked on. It is possible to pass different _parameters_ and/or _return_annotation_ to override the corresponding properties of the base signature. To remove `return_annotation` from the copied `Signature`, pass in [`Signature.empty`](https://docs.python.org/3/library/inspect.html#inspect.Signature.empty "inspect.Signature.empty").
Copy```
>>> def test(a, b):
...     pass
...
>>> sig = signature(test)
>>> new_sig = sig.replace(return_annotation="new return anno")
>>> str(new_sig)
"(a, b) -> 'new return anno'"

```

`Signature` objects are also supported by the generic function [`copy.replace()`](https://docs.python.org/3/library/copy.html#copy.replace "copy.replace").

format(_*_ , _max_width =None_, _quote_annotation_strings =True_)[¶](https://docs.python.org/3/library/inspect.html#inspect.Signature.format "Link to this definition")

Create a string representation of the `Signature` object.
If _max_width_ is passed, the method will attempt to fit the signature into lines of at most _max_width_ characters. If the signature is longer than _max_width_ , all parameters will be on separate lines.
If _quote_annotation_strings_ is False, [annotations](https://docs.python.org/3/glossary.html#term-annotation) in the signature are displayed without opening and closing quotation marks if they are strings. This is useful if the signature was created with the [`STRING`](https://docs.python.org/3/library/annotationlib.html#annotationlib.Format.STRING "annotationlib.Format.STRING") format or if `from __future__ import annotations` was used.
Added in version 3.13.
Changed in version 3.14: The _unquote_annotations_ parameter was added.

_classmethod_ from_callable(_obj_ , _*_ , _follow_wrapped =True_, _globals =None_, _locals =None_, _eval_str =False_)[¶](https://docs.python.org/3/library/inspect.html#inspect.Signature.from_callable "Link to this definition")

Return a `Signature` (or its subclass) object for a given callable _obj_.
This method simplifies subclassing of `Signature`:
Copy```
class MySignature(Signature):
    pass
sig = MySignature.from_callable(sum)
assert isinstance(sig, MySignature)

```

Its behavior is otherwise identical to that of [`signature()`](https://docs.python.org/3/library/inspect.html#inspect.signature "inspect.signature").
Added in version 3.5.
Changed in version 3.10: The _globals_ , _locals_ , and _eval_str_ parameters were added.

_class_ inspect.Parameter(_name_ , _kind_ , _*_ , _default =Parameter.empty_, _annotation =Parameter.empty_)[¶](https://docs.python.org/3/library/inspect.html#inspect.Parameter "Link to this definition")

`Parameter` objects are _immutable_. Instead of modifying a `Parameter` object, you can use [`Parameter.replace()`](https://docs.python.org/3/library/inspect.html#inspect.Parameter.replace "inspect.Parameter.replace") or [`copy.replace()`](https://docs.python.org/3/library/copy.html#copy.replace "copy.replace") to create a modified copy.
Changed in version 3.5: Parameter objects are now picklable and [hashable](https://docs.python.org/3/glossary.html#term-hashable).

empty[¶](https://docs.python.org/3/library/inspect.html#inspect.Parameter.empty "Link to this definition")

A special class-level marker to specify absence of default values and annotations.

name[¶](https://docs.python.org/3/library/inspect.html#inspect.Parameter.name "Link to this definition")

The name of the parameter as a string. The name must be a valid Python identifier.
**CPython implementation detail:** CPython generates implicit parameter names of the form `.0` on the code objects used to implement comprehensions and generator expressions.
Changed in version 3.6: These parameter names are now exposed by this module as names like `implicit0`.

default[¶](https://docs.python.org/3/library/inspect.html#inspect.Parameter.default "Link to this definition")

The default value for the parameter. If the parameter has no default value, this attribute is set to [`Parameter.empty`](https://docs.python.org/3/library/inspect.html#inspect.Parameter.empty "inspect.Parameter.empty").

annotation[¶](https://docs.python.org/3/library/inspect.html#inspect.Parameter.annotation "Link to this definition")

The annotation for the parameter. If the parameter has no annotation, this attribute is set to [`Parameter.empty`](https://docs.python.org/3/library/inspect.html#inspect.Parameter.empty "inspect.Parameter.empty").

kind[¶](https://docs.python.org/3/library/inspect.html#inspect.Parameter.kind "Link to this definition")

Describes how argument values are bound to the parameter. The possible values are accessible via `Parameter` (like `Parameter.KEYWORD_ONLY`), and support comparison and ordering, in the following order:
Name | Meaning
---|---
_POSITIONAL_ONLY_ | Value must be supplied as a positional argument. Positional only parameters are those which appear before a `/` entry (if present) in a Python function definition.
_POSITIONAL_OR_KEYWORD_ | Value may be supplied as either a keyword or positional argument (this is the standard binding behaviour for functions implemented in Python.)
_VAR_POSITIONAL_ | A tuple of positional arguments that aren’t bound to any other parameter. This corresponds to a `*args` parameter in a Python function definition.
_KEYWORD_ONLY_ | Value must be supplied as a keyword argument. Keyword only parameters are those which appear after a `*` or `*args` entry in a Python function definition.
_VAR_KEYWORD_ | A dict of keyword arguments that aren’t bound to any other parameter. This corresponds to a `**kwargs` parameter in a Python function definition.
Example: print all keyword-only arguments without default values:
Copy```
>>> def foo(a, b, *, c, d=10):
...     pass

>>> sig = signature(foo)
>>> for param in sig.parameters.values():
...     if (param.kind == param.KEYWORD_ONLY and
...                        param.default is param.empty):
...         print('Parameter:', param)
Parameter: c

```


kind.description[¶](https://docs.python.org/3/library/inspect.html#inspect.Parameter.kind.description "Link to this definition")

Describes an enum value of [`Parameter.kind`](https://docs.python.org/3/library/inspect.html#inspect.Parameter.kind "inspect.Parameter.kind").
Added in version 3.8.
Example: print all descriptions of arguments:
Copy```
>>> def foo(a, b, *, c, d=10):
...     pass

>>> sig = signature(foo)
>>> for param in sig.parameters.values():
...     print(param.kind.description)
positional or keyword
positional or keyword
keyword-only
keyword-only

```


replace(_*[, name][, kind][, default][, annotation]_)[¶](https://docs.python.org/3/library/inspect.html#inspect.Parameter.replace "Link to this definition")

Create a new `Parameter` instance based on the instance replaced was invoked on. To override a `Parameter` attribute, pass the corresponding argument. To remove a default value or/and an annotation from a `Parameter`, pass [`Parameter.empty`](https://docs.python.org/3/library/inspect.html#inspect.Parameter.empty "inspect.Parameter.empty").
Copy```
>>> from inspect import Parameter
>>> param = Parameter('foo', Parameter.KEYWORD_ONLY, default=42)
>>> str(param)
'foo=42'

>>> str(param.replace()) # Will create a shallow copy of 'param'
'foo=42'

>>> str(param.replace(default=Parameter.empty, annotation='spam'))
"foo: 'spam'"

```

`Parameter` objects are also supported by the generic function [`copy.replace()`](https://docs.python.org/3/library/copy.html#copy.replace "copy.replace").
Changed in version 3.4: In Python 3.3 `Parameter` objects were allowed to have `name` set to `None` if their `kind` was set to `POSITIONAL_ONLY`. This is no longer permitted.

_class_ inspect.BoundArguments[¶](https://docs.python.org/3/library/inspect.html#inspect.BoundArguments "Link to this definition")

Result of a [`Signature.bind()`](https://docs.python.org/3/library/inspect.html#inspect.Signature.bind "inspect.Signature.bind") or [`Signature.bind_partial()`](https://docs.python.org/3/library/inspect.html#inspect.Signature.bind_partial "inspect.Signature.bind_partial") call. Holds the mapping of arguments to the function’s parameters.

arguments[¶](https://docs.python.org/3/library/inspect.html#inspect.BoundArguments.arguments "Link to this definition")

A mutable mapping of parameters’ names to arguments’ values. Contains only explicitly bound arguments. Changes in [`arguments`](https://docs.python.org/3/library/inspect.html#inspect.BoundArguments.arguments "inspect.BoundArguments.arguments") will reflect in [`args`](https://docs.python.org/3/library/inspect.html#inspect.BoundArguments.args "inspect.BoundArguments.args") and [`kwargs`](https://docs.python.org/3/library/inspect.html#inspect.BoundArguments.kwargs "inspect.BoundArguments.kwargs").
Should be used in conjunction with [`Signature.parameters`](https://docs.python.org/3/library/inspect.html#inspect.Signature.parameters "inspect.Signature.parameters") for any argument processing purposes.
Note
Arguments for which [`Signature.bind()`](https://docs.python.org/3/library/inspect.html#inspect.Signature.bind "inspect.Signature.bind") or [`Signature.bind_partial()`](https://docs.python.org/3/library/inspect.html#inspect.Signature.bind_partial "inspect.Signature.bind_partial") relied on a default value are skipped. However, if needed, use [`BoundArguments.apply_defaults()`](https://docs.python.org/3/library/inspect.html#inspect.BoundArguments.apply_defaults "inspect.BoundArguments.apply_defaults") to add them.
Changed in version 3.9: [`arguments`](https://docs.python.org/3/library/inspect.html#inspect.BoundArguments.arguments "inspect.BoundArguments.arguments") is now of type [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict"). Formerly, it was of type [`collections.OrderedDict`](https://docs.python.org/3/library/collections.html#collections.OrderedDict "collections.OrderedDict").

args[¶](https://docs.python.org/3/library/inspect.html#inspect.BoundArguments.args "Link to this definition")

A tuple of positional arguments values. Dynamically computed from the [`arguments`](https://docs.python.org/3/library/inspect.html#inspect.BoundArguments.arguments "inspect.BoundArguments.arguments") attribute.

kwargs[¶](https://docs.python.org/3/library/inspect.html#inspect.BoundArguments.kwargs "Link to this definition")

A dict of keyword arguments values. Dynamically computed from the [`arguments`](https://docs.python.org/3/library/inspect.html#inspect.BoundArguments.arguments "inspect.BoundArguments.arguments") attribute. Arguments that can be passed positionally are included in [`args`](https://docs.python.org/3/library/inspect.html#inspect.BoundArguments.args "inspect.BoundArguments.args") instead.

signature[¶](https://docs.python.org/3/library/inspect.html#inspect.BoundArguments.signature "Link to this definition")

A reference to the parent [`Signature`](https://docs.python.org/3/library/inspect.html#inspect.Signature "inspect.Signature") object.

apply_defaults()[¶](https://docs.python.org/3/library/inspect.html#inspect.BoundArguments.apply_defaults "Link to this definition")

Set default values for missing arguments.
For variable-positional arguments (`*args`) the default is an empty tuple.
For variable-keyword arguments (`**kwargs`) the default is an empty dict.
Copy```
>>> def foo(a, b='ham', *args): pass
>>> ba = inspect.signature(foo).bind('spam')
>>> ba.apply_defaults()
>>> ba.arguments
{'a': 'spam', 'b': 'ham', 'args': ()}

```

Added in version 3.5.
The [`args`](https://docs.python.org/3/library/inspect.html#inspect.BoundArguments.args "inspect.BoundArguments.args") and [`kwargs`](https://docs.python.org/3/library/inspect.html#inspect.BoundArguments.kwargs "inspect.BoundArguments.kwargs") properties can be used to invoke functions:
Copy```
def test(a, *, b):
    ...

sig = signature(test)
ba = sig.bind(10, b=20)
test(*ba.args, **ba.kwargs)

```

See also

[**PEP 362**](https://peps.python.org/pep-0362/) - Function Signature Object.

The detailed specification, implementation details and examples.
