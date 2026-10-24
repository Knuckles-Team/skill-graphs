[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`annotationlib` — Functionality for introspecting annotations](https://docs.python.org/3/library/annotationlib.html)
    * [Annotation semantics](https://docs.python.org/3/library/annotationlib.html#annotation-semantics)
    * [Classes](https://docs.python.org/3/library/annotationlib.html#classes)
    * [Functions](https://docs.python.org/3/library/annotationlib.html#functions)
    * [Recipes](https://docs.python.org/3/library/annotationlib.html#recipes)
      * [Using annotations in a metaclass](https://docs.python.org/3/library/annotationlib.html#using-annotations-in-a-metaclass)
    * [Limitations of the `STRING` format](https://docs.python.org/3/library/annotationlib.html#limitations-of-the-string-format)
    * [Limitations of the `FORWARDREF` format](https://docs.python.org/3/library/annotationlib.html#limitations-of-the-forwardref-format)
    * [Security implications of introspecting annotations](https://docs.python.org/3/library/annotationlib.html#security-implications-of-introspecting-annotations)


#### Previous topic
[`inspect` — Inspect live objects](https://docs.python.org/3/library/inspect.html "previous chapter")
#### Next topic
[`site` — Site-specific configuration hook](https://docs.python.org/3/library/site.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=annotationlib+%E2%80%94+Functionality+for+introspecting+annotations&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fannotationlib.html&pagesource=library%2Fannotationlib.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/site.html "site — Site-specific configuration hook") |
  * [previous](https://docs.python.org/3/library/inspect.html "inspect — Inspect live objects") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Python Runtime Services](https://docs.python.org/3/library/python.html) »
  * [`annotationlib` — Functionality for introspecting annotations](https://docs.python.org/3/library/annotationlib.html)
  * |
  * Theme  Auto Light Dark |


#  `annotationlib` — Functionality for introspecting annotations[¶](https://docs.python.org/3/library/annotationlib.html#module-annotationlib "Link to this heading")
Added in version 3.14.
**Source code:**
* * *
The `annotationlib` module provides tools for introspecting [annotations](https://docs.python.org/3/glossary.html#term-annotation) on modules, classes, and functions.
Annotations are [lazily evaluated](https://docs.python.org/3/reference/executionmodel.html#lazy-evaluation) and often contain forward references to objects that are not yet defined when the annotation is created. This module provides a set of low-level tools that can be used to retrieve annotations in a reliable way, even in the presence of forward references and other edge cases.
This module supports retrieving annotations in three main formats (see [`Format`](https://docs.python.org/3/library/annotationlib.html#annotationlib.Format "annotationlib.Format")), each of which works best for different use cases:
  * [`VALUE`](https://docs.python.org/3/library/annotationlib.html#annotationlib.Format.VALUE "annotationlib.Format.VALUE") evaluates the annotations and returns their value. This is most straightforward to work with, but it may raise errors, for example if the annotations contain references to undefined names.
  * [`FORWARDREF`](https://docs.python.org/3/library/annotationlib.html#annotationlib.Format.FORWARDREF "annotationlib.Format.FORWARDREF") returns [`ForwardRef`](https://docs.python.org/3/library/annotationlib.html#annotationlib.ForwardRef "annotationlib.ForwardRef") objects for annotations that cannot be resolved, allowing you to inspect the annotations without evaluating them. This is useful when you need to work with annotations that may contain unresolved forward references.
  * [`STRING`](https://docs.python.org/3/library/annotationlib.html#annotationlib.Format.STRING "annotationlib.Format.STRING") returns the annotations as a string, similar to how it would appear in the source file. This is useful for documentation generators that want to display annotations in a readable way.


The [`get_annotations()`](https://docs.python.org/3/library/annotationlib.html#annotationlib.get_annotations "annotationlib.get_annotations") function is the main entry point for retrieving annotations. Given a function, class, or module, it returns an annotations dictionary in the requested format. This module also provides functionality for working directly with the [annotate function](https://docs.python.org/3/glossary.html#term-annotate-function) that is used to evaluate annotations, such as [`get_annotate_from_class_namespace()`](https://docs.python.org/3/library/annotationlib.html#annotationlib.get_annotate_from_class_namespace "annotationlib.get_annotate_from_class_namespace") and [`call_annotate_function()`](https://docs.python.org/3/library/annotationlib.html#annotationlib.call_annotate_function "annotationlib.call_annotate_function"), as well as the [`call_evaluate_function()`](https://docs.python.org/3/library/annotationlib.html#annotationlib.call_evaluate_function "annotationlib.call_evaluate_function") function for working with [evaluate functions](https://docs.python.org/3/glossary.html#term-evaluate-function).
Caution
Most functionality in this module can execute arbitrary code; see [the security section](https://docs.python.org/3/library/annotationlib.html#annotationlib-security) for more information.
See also
[**PEP 649**](https://peps.python.org/pep-0649/) proposed the current model for how annotations work in Python.
[**PEP 749**](https://peps.python.org/pep-0749/) expanded on various aspects of [**PEP 649**](https://peps.python.org/pep-0649/) and introduced the `annotationlib` module.
[Annotations Best Practices](https://docs.python.org/3/howto/annotations.html#annotations-howto) provides best practices for working with annotations.
[`get_annotations()`](https://docs.python.org/3/library/annotationlib.html#annotationlib.get_annotations "annotationlib.get_annotations") that works on earlier versions of Python.
## Annotation semantics[¶](https://docs.python.org/3/library/annotationlib.html#annotation-semantics "Link to this heading")
The way annotations are evaluated has changed over the history of Python 3, and currently still depends on a [future import](https://docs.python.org/3/reference/simple_stmts.html#future). There have been execution models for annotations:
  * _Stock semantics_ (default in Python 3.0 through 3.13; see [**PEP 3107**](https://peps.python.org/pep-3107/) and [**PEP 526**](https://peps.python.org/pep-0526/)): Annotations are evaluated eagerly, as they are encountered in the source code.
  * _Stringified annotations_ (used with `from __future__ import annotations` in Python 3.7 and newer; see [**PEP 563**](https://peps.python.org/pep-0563/)): Annotations are stored as strings only.
  * _Deferred evaluation_ (default in Python 3.14 and newer; see [**PEP 649**](https://peps.python.org/pep-0649/) and [**PEP 749**](https://peps.python.org/pep-0749/)): Annotations are evaluated lazily, only when they are accessed.


As an example, consider the following program:
Copy```
def func(a: Cls) -> None:
    print(a)

class Cls: pass

print(func.__annotations__)

```

This will behave as follows:
  * Under stock semantics (Python 3.13 and earlier), it will throw a [`NameError`](https://docs.python.org/3/library/exceptions.html#NameError "NameError") at the line where `func` is defined, because `Cls` is an undefined name at that point.
  * Under stringified annotations (if `from __future__ import annotations` is used), it will print `{'a': 'Cls', 'return': 'None'}`.
  * Under deferred evaluation (Python 3.14 and later), it will print `{'a': <class 'Cls'>, 'return': None}`.


Stock semantics were used when function annotations were first introduced in Python 3.0 (by [**PEP 3107**](https://peps.python.org/pep-3107/)) because this was the simplest, most obvious way to implement annotations. The same execution model was used when variable annotations were introduced in Python 3.6 (by [**PEP 526**](https://peps.python.org/pep-0526/)). However, stock semantics caused problems when using annotations as type hints, such as a need to refer to names that are not yet defined when the annotation is encountered. In addition, there were performance problems with executing annotations at module import time. Therefore, in Python 3.7, [**PEP 563**](https://peps.python.org/pep-0563/) introduced the ability to store annotations as strings using the `from __future__ import annotations` syntax. The plan at the time was to eventually make this behavior the default, but a problem appeared: stringified annotations are more difficult to process for those who introspect annotations at runtime. An alternative proposal, [**PEP 649**](https://peps.python.org/pep-0649/), introduced the third execution model, deferred evaluation, and was implemented in Python 3.14. Stringified annotations are still used if `from __future__ import annotations` is present, but this behavior will eventually be removed.
## Classes[¶](https://docs.python.org/3/library/annotationlib.html#classes "Link to this heading")

_class_ annotationlib.Format[¶](https://docs.python.org/3/library/annotationlib.html#annotationlib.Format "Link to this definition")

An [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "enum.IntEnum") describing the formats in which annotations can be returned. Members of the enum, or their equivalent integer values, can be passed to [`get_annotations()`](https://docs.python.org/3/library/annotationlib.html#annotationlib.get_annotations "annotationlib.get_annotations") and other functions in this module, as well as to [`__annotate__`](https://docs.python.org/3/reference/datamodel.html#object.__annotate__ "object.__annotate__") functions.

VALUE _= 1_[¶](https://docs.python.org/3/library/annotationlib.html#annotationlib.Format.VALUE "Link to this definition")

Values are the result of evaluating the annotation expressions.

VALUE_WITH_FAKE_GLOBALS _= 2_[¶](https://docs.python.org/3/library/annotationlib.html#annotationlib.Format.VALUE_WITH_FAKE_GLOBALS "Link to this definition")

Special value used to signal that an annotate function is being evaluated in a special environment with fake globals. When passed this value, annotate functions should either return the same value as for the [`Format.VALUE`](https://docs.python.org/3/library/annotationlib.html#annotationlib.Format.VALUE "annotationlib.Format.VALUE") format, or raise [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "NotImplementedError") to signal that they do not support execution in this environment. This format is only used internally and should not be passed to the functions in this module.

FORWARDREF _= 3_[¶](https://docs.python.org/3/library/annotationlib.html#annotationlib.Format.FORWARDREF "Link to this definition")

Values are real annotation values (as per [`Format.VALUE`](https://docs.python.org/3/library/annotationlib.html#annotationlib.Format.VALUE "annotationlib.Format.VALUE") format) for defined values, and [`ForwardRef`](https://docs.python.org/3/library/annotationlib.html#annotationlib.ForwardRef "annotationlib.ForwardRef") proxies for undefined values. Real objects may contain references to `ForwardRef` proxy objects.

STRING _= 4_[¶](https://docs.python.org/3/library/annotationlib.html#annotationlib.Format.STRING "Link to this definition")

Values are the text string of the annotation as it appears in the source code, up to modifications including, but not restricted to, whitespace normalizations and constant values optimizations.
The exact values of these strings may change in future versions of Python.
Added in version 3.14.

_class_ annotationlib.ForwardRef[¶](https://docs.python.org/3/library/annotationlib.html#annotationlib.ForwardRef "Link to this definition")

A proxy object for forward references in annotations.
Instances of this class are returned when the [`FORWARDREF`](https://docs.python.org/3/library/annotationlib.html#annotationlib.Format.FORWARDREF "annotationlib.Format.FORWARDREF") format is used and annotations contain a name that cannot be resolved. This can happen when a forward reference is used in an annotation, such as when a class is referenced before it is defined.

__forward_arg__[¶](https://docs.python.org/3/library/annotationlib.html#annotationlib.ForwardRef.__forward_arg__ "Link to this definition")

A string containing the code that was evaluated to produce the `ForwardRef`. The string may not be exactly equivalent to the original source.

evaluate(_*_ , _owner =None_, _globals =None_, _locals =None_, _type_params =None_, _format =Format.VALUE_)[¶](https://docs.python.org/3/library/annotationlib.html#annotationlib.ForwardRef.evaluate "Link to this definition")

Evaluate the forward reference, returning its value.
If the _format_ argument is [`VALUE`](https://docs.python.org/3/library/annotationlib.html#annotationlib.Format.VALUE "annotationlib.Format.VALUE") (the default), this method may throw an exception, such as [`NameError`](https://docs.python.org/3/library/exceptions.html#NameError "NameError"), if the forward reference refers to a name that cannot be resolved. The arguments to this method can be used to provide bindings for names that would otherwise be undefined. If the _format_ argument is [`FORWARDREF`](https://docs.python.org/3/library/annotationlib.html#annotationlib.Format.FORWARDREF "annotationlib.Format.FORWARDREF"), the method will never throw an exception, but may return a `ForwardRef` instance. For example, if the forward reference object contains the code `list[undefined]`, where `undefined` is a name that is not defined, evaluating it with the `FORWARDREF` format will return `list[ForwardRef('undefined')]`. If the _format_ argument is [`STRING`](https://docs.python.org/3/library/annotationlib.html#annotationlib.Format.STRING "annotationlib.Format.STRING"), the method will return [`__forward_arg__`](https://docs.python.org/3/library/annotationlib.html#annotationlib.ForwardRef.__forward_arg__ "annotationlib.ForwardRef.__forward_arg__").
The _owner_ parameter provides the preferred mechanism for passing scope information to this method. The owner of a `ForwardRef` is the object that contains the annotation from which the `ForwardRef` derives, such as a module object, type object, or function object.
The _globals_ , _locals_ , and _type_params_ parameters provide a more precise mechanism for influencing the names that are available when the `ForwardRef` is evaluated. _globals_ and _locals_ are passed to [`eval()`](https://docs.python.org/3/library/functions.html#eval "eval"), representing the global and local namespaces in which the name is evaluated. The _type_params_ parameter is relevant for objects created using the native syntax for [generic classes](https://docs.python.org/3/reference/compound_stmts.html#generic-classes) and [functions](https://docs.python.org/3/reference/compound_stmts.html#generic-functions). It is a tuple of [type parameters](https://docs.python.org/3/reference/compound_stmts.html#type-params) that are in scope while the forward reference is being evaluated. For example, if evaluating a `ForwardRef` retrieved from an annotation found in the class namespace of a generic class `C`, _type_params_ should be set to `C.__type_params__`.
`ForwardRef` instances returned by [`get_annotations()`](https://docs.python.org/3/library/annotationlib.html#annotationlib.get_annotations "annotationlib.get_annotations") retain references to information about the scope they originated from, so calling this method with no further arguments may be sufficient to evaluate such objects. `ForwardRef` instances created by other means may not have any information about their scope, so passing arguments to this method may be necessary to evaluate them successfully.
If no _owner_ , _globals_ , _locals_ , or _type_params_ are provided and the `ForwardRef` does not contain information about its origin, empty globals and locals dictionaries are used.
Added in version 3.14.
## Functions[¶](https://docs.python.org/3/library/annotationlib.html#functions "Link to this heading")

annotationlib.annotations_to_string(_annotations_)[¶](https://docs.python.org/3/library/annotationlib.html#annotationlib.annotations_to_string "Link to this definition")

Convert an annotations dict containing runtime values to a dict containing only strings. If the values are not already strings, they are converted using [`type_repr()`](https://docs.python.org/3/library/annotationlib.html#annotationlib.type_repr "annotationlib.type_repr"). This is meant as a helper for user-provided annotate functions that support the [`STRING`](https://docs.python.org/3/library/annotationlib.html#annotationlib.Format.STRING "annotationlib.Format.STRING") format but do not have access to the code creating the annotations.
For example, this is used to implement the [`STRING`](https://docs.python.org/3/library/annotationlib.html#annotationlib.Format.STRING "annotationlib.Format.STRING") for [`typing.TypedDict`](https://docs.python.org/3/library/typing.html#typing.TypedDict "typing.TypedDict") classes created through the functional syntax:
Copy```
>>> from typing import TypedDict
>>> Movie = TypedDict("movie", {"name": str, "year": int})
>>> get_annotations(Movie, format=Format.STRING)
{'name': 'str', 'year': 'int'}

```

Added in version 3.14.

annotationlib.call_annotate_function(_annotate_ , _format_ , _*_ , _owner =None_)[¶](https://docs.python.org/3/library/annotationlib.html#annotationlib.call_annotate_function "Link to this definition")

Call the [annotate function](https://docs.python.org/3/glossary.html#term-annotate-function) _annotate_ with the given _format_ , a member of the [`Format`](https://docs.python.org/3/library/annotationlib.html#annotationlib.Format "annotationlib.Format") enum, and return the annotations dictionary produced by the function.
This helper function is required because annotate functions generated by the compiler for functions, classes, and modules only support the [`VALUE`](https://docs.python.org/3/library/annotationlib.html#annotationlib.Format.VALUE "annotationlib.Format.VALUE") format when called directly. To support other formats, this function calls the annotate function in a special environment that allows it to produce annotations in the other formats. This is a useful building block when implementing functionality that needs to partially evaluate annotations while a class is being constructed.
_owner_ is the object that owns the annotation function, usually a function, class, or module. If provided, it is used in the [`FORWARDREF`](https://docs.python.org/3/library/annotationlib.html#annotationlib.Format.FORWARDREF "annotationlib.Format.FORWARDREF") format to produce a [`ForwardRef`](https://docs.python.org/3/library/annotationlib.html#annotationlib.ForwardRef "annotationlib.ForwardRef") object that carries more information.
See also
[**PEP 649**](https://peps.python.org/pep-0649/#the-stringizer-and-the-fake-globals-environment) contains an explanation of the implementation technique used by this function.
Added in version 3.14.

annotationlib.call_evaluate_function(_evaluate_ , _format_ , _*_ , _owner =None_)[¶](https://docs.python.org/3/library/annotationlib.html#annotationlib.call_evaluate_function "Link to this definition")

Call the [evaluate function](https://docs.python.org/3/glossary.html#term-evaluate-function) _evaluate_ with the given _format_ , a member of the [`Format`](https://docs.python.org/3/library/annotationlib.html#annotationlib.Format "annotationlib.Format") enum, and return the value produced by the function. This is similar to [`call_annotate_function()`](https://docs.python.org/3/library/annotationlib.html#annotationlib.call_annotate_function "annotationlib.call_annotate_function"), but the latter always returns a dictionary mapping strings to annotations, while this function returns a single value.
This is intended for use with the evaluate functions generated for lazily evaluated elements related to type aliases and type parameters:
  * [`typing.TypeAliasType.evaluate_value()`](https://docs.python.org/3/library/typing.html#typing.TypeAliasType.evaluate_value "typing.TypeAliasType.evaluate_value"), the value of type aliases
  * [`typing.TypeVar.evaluate_bound()`](https://docs.python.org/3/library/typing.html#typing.TypeVar.evaluate_bound "typing.TypeVar.evaluate_bound"), the bound of type variables
  * [`typing.TypeVar.evaluate_constraints()`](https://docs.python.org/3/library/typing.html#typing.TypeVar.evaluate_constraints "typing.TypeVar.evaluate_constraints"), the constraints of type variables
  * [`typing.TypeVar.evaluate_default()`](https://docs.python.org/3/library/typing.html#typing.TypeVar.evaluate_default "typing.TypeVar.evaluate_default"), the default value of type variables
  * [`typing.ParamSpec.evaluate_default()`](https://docs.python.org/3/library/typing.html#typing.ParamSpec.evaluate_default "typing.ParamSpec.evaluate_default"), the default value of parameter specifications
  * [`typing.TypeVarTuple.evaluate_default()`](https://docs.python.org/3/library/typing.html#typing.TypeVarTuple.evaluate_default "typing.TypeVarTuple.evaluate_default"), the default value of type variable tuples


_owner_ is the object that owns the evaluate function, such as the type alias or type variable object.
_format_ can be used to control the format in which the value is returned:
Copy```
>>> type Alias = undefined
>>> call_evaluate_function(Alias.evaluate_value, Format.VALUE)
Traceback (most recent call last):
...
NameError: name 'undefined' is not defined
>>> call_evaluate_function(Alias.evaluate_value, Format.FORWARDREF)
ForwardRef('undefined')
>>> call_evaluate_function(Alias.evaluate_value, Format.STRING)
'undefined'

```

Added in version 3.14.

annotationlib.get_annotate_from_class_namespace(_namespace_)[¶](https://docs.python.org/3/library/annotationlib.html#annotationlib.get_annotate_from_class_namespace "Link to this definition")

Retrieve the [annotate function](https://docs.python.org/3/glossary.html#term-annotate-function) from a class namespace dictionary _namespace_. Return `None` if the namespace does not contain an annotate function. This is primarily useful before the class has been fully created (e.g., in a metaclass); after the class exists, the annotate function can be retrieved with `cls.__annotate__`. See [below](https://docs.python.org/3/library/annotationlib.html#annotationlib-metaclass) for an example using this function in a metaclass.
Added in version 3.14.

annotationlib.get_annotations(_obj_ , _*_ , _globals =None_, _locals =None_, _eval_str =False_, _format =Format.VALUE_)[¶](https://docs.python.org/3/library/annotationlib.html#annotationlib.get_annotations "Link to this definition")

Compute the annotations dict for an object.
_obj_ may be a callable, class, module, or other object with [`__annotate__`](https://docs.python.org/3/reference/datamodel.html#object.__annotate__ "object.__annotate__") or [`__annotations__`](https://docs.python.org/3/reference/datamodel.html#object.__annotations__ "object.__annotations__") attributes. Passing any other object raises [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError").
The _format_ parameter controls the format in which annotations are returned, and must be a member of the [`Format`](https://docs.python.org/3/library/annotationlib.html#annotationlib.Format "annotationlib.Format") enum or its integer equivalent. The different formats work as follows:
  * VALUE: `object.__annotations__` is tried first; if that does not exist, the `object.__annotate__` function is called if it exists.
  * FORWARDREF: If `object.__annotations__` exists and can be evaluated successfully, it is used; otherwise, the `object.__annotate__` function is called. If it does not exist either, `object.__annotations__` is tried again and any error from accessing it is re-raised.
    * When calling `object.__annotate__` it is first called with [`FORWARDREF`](https://docs.python.org/3/library/annotationlib.html#annotationlib.Format.FORWARDREF "annotationlib.Format.FORWARDREF"). If this is not implemented, it will then check if [`VALUE_WITH_FAKE_GLOBALS`](https://docs.python.org/3/library/annotationlib.html#annotationlib.Format.VALUE_WITH_FAKE_GLOBALS "annotationlib.Format.VALUE_WITH_FAKE_GLOBALS") is supported and use that in the fake globals environment. If neither of these formats are supported, it will fall back to using [`VALUE`](https://docs.python.org/3/library/annotationlib.html#annotationlib.Format.VALUE "annotationlib.Format.VALUE"). If `VALUE` fails, the error from this call will be raised.
  * STRING: If `object.__annotate__` exists, it is called first; otherwise, `object.__annotations__` is used and stringified using [`annotations_to_string()`](https://docs.python.org/3/library/annotationlib.html#annotationlib.annotations_to_string "annotationlib.annotations_to_string").
    * When calling `object.__annotate__` it is first called with [`STRING`](https://docs.python.org/3/library/annotationlib.html#annotationlib.Format.STRING "annotationlib.Format.STRING"). If this is not implemented, it will then check if [`VALUE_WITH_FAKE_GLOBALS`](https://docs.python.org/3/library/annotationlib.html#annotationlib.Format.VALUE_WITH_FAKE_GLOBALS "annotationlib.Format.VALUE_WITH_FAKE_GLOBALS") is supported and use that in the fake globals environment. If neither of these formats are supported, it will fall back to using [`VALUE`](https://docs.python.org/3/library/annotationlib.html#annotationlib.Format.VALUE "annotationlib.Format.VALUE") with the result converted using [`annotations_to_string()`](https://docs.python.org/3/library/annotationlib.html#annotationlib.annotations_to_string "annotationlib.annotations_to_string"). If `VALUE` fails, the error from this call will be raised.


Returns a dict. `get_annotations()` returns a new dict every time it’s called; calling it twice on the same object will return two different but equivalent dicts.
This function handles several details for you:
  * If _eval_str_ is true, values of type `str` will be un-stringized using [`eval()`](https://docs.python.org/3/library/functions.html#eval "eval"). This is intended for use with stringized annotations (`from __future__ import annotations`). It is an error to set _eval_str_ to true with formats other than [`Format.VALUE`](https://docs.python.org/3/library/annotationlib.html#annotationlib.Format.VALUE "annotationlib.Format.VALUE").
  * If _obj_ doesn’t have an annotations dict, returns an empty dict. (Functions and methods always have an annotations dict; classes, modules, and other types of callables may not.)
  * Ignores inherited annotations on classes, as well as annotations on metaclasses. If a class doesn’t have its own annotations dict, returns an empty dict.
  * All accesses to object members and dict values are done using `getattr()` and `dict.get()` for safety.


_eval_str_ controls whether or not values of type `str` are replaced with the result of calling [`eval()`](https://docs.python.org/3/library/functions.html#eval "eval") on those values:
  * If eval_str is true, [`eval()`](https://docs.python.org/3/library/functions.html#eval "eval") is called on values of type `str`. (Note that `get_annotations()` doesn’t catch exceptions; if `eval()` raises an exception, it will unwind the stack past the `get_annotations()` call.)
  * If _eval_str_ is false (the default), values of type `str` are unchanged.


_globals_ and _locals_ are passed in to [`eval()`](https://docs.python.org/3/library/functions.html#eval "eval"); see the documentation for `eval()` for more information. If _globals_ or _locals_ is `None`, this function may replace that value with a context-specific default, contingent on `type(obj)`:
  * If _obj_ is a module, _globals_ defaults to `obj.__dict__`.
  * If _obj_ is a class, _globals_ defaults to `sys.modules[obj.__module__].__dict__` and _locals_ defaults to the _obj_ class namespace.
  * If _obj_ is a callable, _globals_ defaults to [`obj.__globals__`](https://docs.python.org/3/reference/datamodel.html#function.__globals__ "function.__globals__"), although if _obj_ is a wrapped function (using [`functools.update_wrapper()`](https://docs.python.org/3/library/functools.html#functools.update_wrapper "functools.update_wrapper")) or a [`functools.partial`](https://docs.python.org/3/library/functools.html#functools.partial "functools.partial") object, it is unwrapped until a non-wrapped function is found.


Calling `get_annotations()` is best practice for accessing the annotations dict of any object. See [Annotations Best Practices](https://docs.python.org/3/howto/annotations.html#annotations-howto) for more information on annotations best practices.
Copy```
>>> def f(a: int, b: str) -> float:
...     pass
>>> get_annotations(f)
{'a': <class 'int'>, 'b': <class 'str'>, 'return': <class 'float'>}

```

Added in version 3.14.

annotationlib.type_repr(_value_)[¶](https://docs.python.org/3/library/annotationlib.html#annotationlib.type_repr "Link to this definition")

Convert an arbitrary Python value to a format suitable for use by the [`STRING`](https://docs.python.org/3/library/annotationlib.html#annotationlib.Format.STRING "annotationlib.Format.STRING") format. This calls [`repr()`](https://docs.python.org/3/library/functions.html#repr "repr") for most objects, but has special handling for some objects, such as type objects.
This is meant as a helper for user-provided annotate functions that support the [`STRING`](https://docs.python.org/3/library/annotationlib.html#annotationlib.Format.STRING "annotationlib.Format.STRING") format but do not have access to the code creating the annotations. It can also be used to provide a user-friendly string representation for other objects that contain values that are commonly encountered in annotations.
Added in version 3.14.
## Recipes[¶](https://docs.python.org/3/library/annotationlib.html#recipes "Link to this heading")
### Using annotations in a metaclass[¶](https://docs.python.org/3/library/annotationlib.html#using-annotations-in-a-metaclass "Link to this heading")
A [metaclass](https://docs.python.org/3/reference/datamodel.html#metaclasses) may want to inspect or even modify the annotations in a class body during class creation. Doing so requires retrieving annotations from the class namespace dictionary. For classes created with `from __future__ import annotations`, the annotations will be in the `__annotations__` key of the dictionary. For other classes with annotations, [`get_annotate_from_class_namespace()`](https://docs.python.org/3/library/annotationlib.html#annotationlib.get_annotate_from_class_namespace "annotationlib.get_annotate_from_class_namespace") can be used to get the annotate function, and [`call_annotate_function()`](https://docs.python.org/3/library/annotationlib.html#annotationlib.call_annotate_function "annotationlib.call_annotate_function") can be used to call it and retrieve the annotations. Using the [`FORWARDREF`](https://docs.python.org/3/library/annotationlib.html#annotationlib.Format.FORWARDREF "annotationlib.Format.FORWARDREF") format will usually be best, because this allows the annotations to refer to names that cannot yet be resolved when the class is created.
To modify the annotations, it is best to create a wrapper annotate function that calls the original annotate function, makes any necessary adjustments, and returns the result.
Below is an example of a metaclass that filters out all [`typing.ClassVar`](https://docs.python.org/3/library/typing.html#typing.ClassVar "typing.ClassVar") annotations from the class and puts them in a separate attribute:
Copy```
import annotationlib
import typing

class ClassVarSeparator(type):
   def __new__(mcls, name, bases, ns):
      if "__annotations__" in ns:  # from __future__ import annotations
         annotations = ns["__annotations__"]
         classvar_keys = {
            key for key, value in annotations.items()
            # Use string comparison for simplicity; a more robust solution
            # could use annotationlib.ForwardRef.evaluate
            if value.startswith("ClassVar")
         }
         classvars = {key: annotations[key] for key in classvar_keys}
         ns["__annotations__"] = {
            key: value for key, value in annotations.items()
            if key not in classvar_keys
         }
         wrapped_annotate = None
      elif annotate := annotationlib.get_annotate_from_class_namespace(ns):
         annotations = annotationlib.call_annotate_function(
            annotate, format=annotationlib.Format.FORWARDREF
         )
         classvar_keys = {
            key for key, value in annotations.items()
            if typing.get_origin(value) is typing.ClassVar
         }
         classvars = {key: annotations[key] for key in classvar_keys}

         def wrapped_annotate(format):
            annos = annotationlib.call_annotate_function(annotate, format, owner=typ)
            return {key: value for key, value in annos.items() if key not in classvar_keys}

      else:  # no annotations
         classvars = {}
         wrapped_annotate = None
      typ = super().__new__(mcls, name, bases, ns)

      if wrapped_annotate is not None:
         # Wrap the original __annotate__ with a wrapper that removes ClassVars
         typ.__annotate__ = wrapped_annotate
      typ.classvars = classvars  # Store the ClassVars in a separate attribute
      return typ

```

## Limitations of the `STRING` format[¶](https://docs.python.org/3/library/annotationlib.html#limitations-of-the-string-format "Link to this heading")
The [`STRING`](https://docs.python.org/3/library/annotationlib.html#annotationlib.Format.STRING "annotationlib.Format.STRING") format is meant to approximate the source code of the annotation, but the implementation strategy used means that it is not always possible to recover the exact source code.
First, the stringifier of course cannot recover any information that is not present in the compiled code, including comments, whitespace, parenthesization, and operations that get simplified by the compiler.
Second, the stringifier can intercept almost all operations that involve names looked up in some scope, but it cannot intercept operations that operate fully on constants. As a corollary, this also means it is not safe to request the `STRING` format on untrusted code: Python is powerful enough that it is possible to achieve arbitrary code execution even with no access to any globals or builtins. For example:
Copy```
>>> def f(x: (1).__class__.__base__.__subclasses__()[-1].__init__.__builtins__["print"]("Hello world")): pass
...
>>> annotationlib.get_annotations(f, format=annotationlib.Format.STRING)
Hello world
{'x': 'None'}

```

Note
This particular example works as of the time of writing, but it relies on implementation details and is not guaranteed to work in the future.
Among the different kinds of expressions that exist in Python, as represented by the [`ast`](https://docs.python.org/3/library/ast.html#module-ast "ast: Abstract Syntax Tree classes and manipulation.") module, some expressions are supported, meaning that the `STRING` format can generally recover the original source code; others are unsupported, meaning that they may result in incorrect output or an error.
The following are supported (sometimes with caveats):
  * [`ast.BinOp`](https://docs.python.org/3/library/ast.html#ast.BinOp "ast.BinOp")
  * [`ast.UnaryOp`](https://docs.python.org/3/library/ast.html#ast.UnaryOp "ast.UnaryOp")
    * [`ast.Invert`](https://docs.python.org/3/library/ast.html#ast.Invert "ast.Invert") (`~`), [`ast.UAdd`](https://docs.python.org/3/library/ast.html#ast.UAdd "ast.UAdd") (`+`), and [`ast.USub`](https://docs.python.org/3/library/ast.html#ast.USub "ast.USub") (`-`) are supported
    * [`ast.Not`](https://docs.python.org/3/library/ast.html#ast.Not "ast.Not") (`not`) is not supported
  * [`ast.Dict`](https://docs.python.org/3/library/ast.html#ast.Dict "ast.Dict") (except when using `**` unpacking)
  * [`ast.Set`](https://docs.python.org/3/library/ast.html#ast.Set "ast.Set")
  * [`ast.Compare`](https://docs.python.org/3/library/ast.html#ast.Compare "ast.Compare")
    * [`ast.Eq`](https://docs.python.org/3/library/ast.html#ast.Eq "ast.Eq") and [`ast.NotEq`](https://docs.python.org/3/library/ast.html#ast.NotEq "ast.NotEq") are supported
    * [`ast.Lt`](https://docs.python.org/3/library/ast.html#ast.Lt "ast.Lt"), [`ast.LtE`](https://docs.python.org/3/library/ast.html#ast.LtE "ast.LtE"), [`ast.Gt`](https://docs.python.org/3/library/ast.html#ast.Gt "ast.Gt"), and [`ast.GtE`](https://docs.python.org/3/library/ast.html#ast.GtE "ast.GtE") are supported, but the operand may be flipped
    * [`ast.Is`](https://docs.python.org/3/library/ast.html#ast.Is "ast.Is"), [`ast.IsNot`](https://docs.python.org/3/library/ast.html#ast.IsNot "ast.IsNot"), [`ast.In`](https://docs.python.org/3/library/ast.html#ast.In "ast.In"), and [`ast.NotIn`](https://docs.python.org/3/library/ast.html#ast.NotIn "ast.NotIn") are not supported
  * [`ast.Call`](https://docs.python.org/3/library/ast.html#ast.Call "ast.Call") (except when using `**` unpacking)
  * [`ast.Constant`](https://docs.python.org/3/library/ast.html#ast.Constant "ast.Constant") (though not the exact representation of the constant; for example, escape sequences in strings are lost; hexadecimal numbers are converted to decimal)
  * [`ast.Attribute`](https://docs.python.org/3/library/ast.html#ast.Attribute "ast.Attribute") (assuming the value is not a constant)
  * [`ast.Subscript`](https://docs.python.org/3/library/ast.html#ast.Subscript "ast.Subscript") (assuming the value is not a constant)
  * [`ast.Starred`](https://docs.python.org/3/library/ast.html#ast.Starred "ast.Starred") (`*` unpacking)
  * [`ast.Name`](https://docs.python.org/3/library/ast.html#ast.Name "ast.Name")
  * [`ast.List`](https://docs.python.org/3/library/ast.html#ast.List "ast.List")
  * [`ast.Tuple`](https://docs.python.org/3/library/ast.html#ast.Tuple "ast.Tuple")
  * [`ast.Slice`](https://docs.python.org/3/library/ast.html#ast.Slice "ast.Slice")


The following are unsupported, but throw an informative error when encountered by the stringifier:
  * [`ast.FormattedValue`](https://docs.python.org/3/library/ast.html#ast.FormattedValue "ast.FormattedValue") (f-strings; error is not detected if conversion specifiers like `!r` are used)
  * [`ast.JoinedStr`](https://docs.python.org/3/library/ast.html#ast.JoinedStr "ast.JoinedStr") (f-strings)


The following are unsupported and result in incorrect output:
  * [`ast.BoolOp`](https://docs.python.org/3/library/ast.html#ast.BoolOp "ast.BoolOp") (`and` and `or`)
  * [`ast.IfExp`](https://docs.python.org/3/library/ast.html#ast.IfExp "ast.IfExp")
  * [`ast.Lambda`](https://docs.python.org/3/library/ast.html#ast.Lambda "ast.Lambda")
  * [`ast.ListComp`](https://docs.python.org/3/library/ast.html#ast.ListComp "ast.ListComp")
  * [`ast.SetComp`](https://docs.python.org/3/library/ast.html#ast.SetComp "ast.SetComp")
  * [`ast.DictComp`](https://docs.python.org/3/library/ast.html#ast.DictComp "ast.DictComp")
  * [`ast.GeneratorExp`](https://docs.python.org/3/library/ast.html#ast.GeneratorExp "ast.GeneratorExp")


The following are disallowed in annotation scopes and therefore not relevant:
  * [`ast.NamedExpr`](https://docs.python.org/3/library/ast.html#ast.NamedExpr "ast.NamedExpr") (`:=`)
  * [`ast.Await`](https://docs.python.org/3/library/ast.html#ast.Await "ast.Await")
  * [`ast.Yield`](https://docs.python.org/3/library/ast.html#ast.Yield "ast.Yield")
  * [`ast.YieldFrom`](https://docs.python.org/3/library/ast.html#ast.YieldFrom "ast.YieldFrom")


## Limitations of the `FORWARDREF` format[¶](https://docs.python.org/3/library/annotationlib.html#limitations-of-the-forwardref-format "Link to this heading")
The [`FORWARDREF`](https://docs.python.org/3/library/annotationlib.html#annotationlib.Format.FORWARDREF "annotationlib.Format.FORWARDREF") format aims to produce real values as much as possible, with anything that cannot be resolved replaced with [`ForwardRef`](https://docs.python.org/3/library/annotationlib.html#annotationlib.ForwardRef "annotationlib.ForwardRef") objects. It is affected by broadly the same Limitations as the [`STRING`](https://docs.python.org/3/library/annotationlib.html#annotationlib.Format.STRING "annotationlib.Format.STRING") format: annotations that perform operations on literals or that use unsupported expression types may raise exceptions when evaluated using the `FORWARDREF` format.
Below are a few examples of the behavior with unsupported expressions:
Copy```
>>> from annotationlib import get_annotations, Format
>>> def zerodiv(x: 1 / 0): ...
>>> get_annotations(zerodiv, format=Format.STRING)
Traceback (most recent call last):
  ...
ZeroDivisionError: division by zero
>>> get_annotations(zerodiv, format=Format.FORWARDREF)
Traceback (most recent call last):
  ...
ZeroDivisionError: division by zero
>>> def ifexp(x: 1 if y else 0): ...
>>> get_annotations(ifexp, format=Format.STRING)
{'x': '1'}

```

## Security implications of introspecting annotations[¶](https://docs.python.org/3/library/annotationlib.html#security-implications-of-introspecting-annotations "Link to this heading")
Much of the functionality in this module involves executing code related to annotations, which can then do arbitrary things. For example, [`get_annotations()`](https://docs.python.org/3/library/annotationlib.html#annotationlib.get_annotations "annotationlib.get_annotations") may call an arbitrary [annotate function](https://docs.python.org/3/glossary.html#term-annotate-function), and [`ForwardRef.evaluate()`](https://docs.python.org/3/library/annotationlib.html#annotationlib.ForwardRef.evaluate "annotationlib.ForwardRef.evaluate") may call [`eval()`](https://docs.python.org/3/library/functions.html#eval "eval") on an arbitrary string. Code contained in an annotation might make arbitrary system calls, enter an infinite loop, or perform any other operation. This is also true for any access of the [`__annotations__`](https://docs.python.org/3/reference/datamodel.html#object.__annotations__ "object.__annotations__") attribute, and for various functions in the [`typing`](https://docs.python.org/3/library/typing.html#module-typing "typing: Support for type hints \(see :pep:`484`\).") module that work with annotations, such as [`typing.get_type_hints()`](https://docs.python.org/3/library/typing.html#typing.get_type_hints "typing.get_type_hints").
Any security issue arising from this also applies immediately after importing code that may contain untrusted annotations: importing code can always cause arbitrary operations to be performed. However, it is unsafe to accept strings or other input from an untrusted source and pass them to any of the APIs for introspecting annotations, for example by editing an `__annotations__` dictionary or directly creating a [`ForwardRef`](https://docs.python.org/3/library/annotationlib.html#annotationlib.ForwardRef "annotationlib.ForwardRef") object.
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`annotationlib` — Functionality for introspecting annotations](https://docs.python.org/3/library/annotationlib.html)
    * [Annotation semantics](https://docs.python.org/3/library/annotationlib.html#annotation-semantics)
    * [Classes](https://docs.python.org/3/library/annotationlib.html#classes)
    * [Functions](https://docs.python.org/3/library/annotationlib.html#functions)
    * [Recipes](https://docs.python.org/3/library/annotationlib.html#recipes)
      * [Using annotations in a metaclass](https://docs.python.org/3/library/annotationlib.html#using-annotations-in-a-metaclass)
    * [Limitations of the `STRING` format](https://docs.python.org/3/library/annotationlib.html#limitations-of-the-string-format)
    * [Limitations of the `FORWARDREF` format](https://docs.python.org/3/library/annotationlib.html#limitations-of-the-forwardref-format)
    * [Security implications of introspecting annotations](https://docs.python.org/3/library/annotationlib.html#security-implications-of-introspecting-annotations)


#### Previous topic
[`inspect` — Inspect live objects](https://docs.python.org/3/library/inspect.html "previous chapter")
#### Next topic
[`site` — Site-specific configuration hook](https://docs.python.org/3/library/site.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=annotationlib+%E2%80%94+Functionality+for+introspecting+annotations&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fannotationlib.html&pagesource=library%2Fannotationlib.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/site.html "site — Site-specific configuration hook") |
  * [previous](https://docs.python.org/3/library/inspect.html "inspect — Inspect live objects") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Python Runtime Services](https://docs.python.org/3/library/python.html) »
  * [`annotationlib` — Functionality for introspecting annotations](https://docs.python.org/3/library/annotationlib.html)
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
