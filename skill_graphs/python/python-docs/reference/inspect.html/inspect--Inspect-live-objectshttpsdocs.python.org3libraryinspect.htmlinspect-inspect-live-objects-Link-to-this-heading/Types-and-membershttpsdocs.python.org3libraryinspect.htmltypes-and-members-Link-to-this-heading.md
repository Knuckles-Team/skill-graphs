## Types and members[¶](https://docs.python.org/3/library/inspect.html#types-and-members "Link to this heading")
The [`getmembers()`](https://docs.python.org/3/library/inspect.html#inspect.getmembers "inspect.getmembers") function retrieves the members of an object such as a class or module. The functions whose names begin with “is” are mainly provided as convenient choices for the second argument to `getmembers()`. They also help you determine when you can expect to find the following special attributes (see [Import-related attributes on module objects](https://docs.python.org/3/reference/datamodel.html#import-mod-attrs) for module attributes):
Type | Attribute | Description
---|---|---
class | __doc__ | documentation string
| __name__ | name with which this class was defined
| __qualname__ | qualified name
| __module__ | name of module in which this class was defined
| __type_params__ | A tuple containing the [type parameters](https://docs.python.org/3/reference/compound_stmts.html#type-params) of a generic class
method | __doc__ | documentation string
| __name__ | name with which this method was defined
| __qualname__ | qualified name
| __func__ | function object containing implementation of method
| __self__ | instance to which this method is bound, or `None`
| __module__ | name of module in which this method was defined
function | __doc__ | documentation string
| __name__ | name with which this function was defined
| __qualname__ | qualified name
| __code__ | code object containing compiled function [bytecode](https://docs.python.org/3/glossary.html#term-bytecode)
| __defaults__ | tuple of any default values for positional or keyword parameters
| __kwdefaults__ | mapping of any default values for keyword-only parameters
| __globals__ | global namespace in which this function was defined
| __builtins__ | builtins namespace
| __annotations__ | mapping of parameters names to annotations; `"return"` key is reserved for return annotations.
| __type_params__ | A tuple containing the [type parameters](https://docs.python.org/3/reference/compound_stmts.html#type-params) of a generic function
| __module__ | name of module in which this function was defined
traceback | tb_frame | frame object at this level
| tb_lasti | index of last attempted instruction in bytecode
| tb_lineno | current line number in Python source code
| tb_next | next inner traceback object (called by this level)
frame | f_back | next outer frame object (this frame’s caller)
| f_builtins | builtins namespace seen by this frame
| f_code | code object being executed in this frame
| f_globals | global namespace seen by this frame
| f_lasti | index of last attempted instruction in bytecode
| f_lineno | current line number in Python source code
| f_locals | local namespace seen by this frame
| f_generator | returns the generator or coroutine object that owns this frame, or `None` if the frame is of a regular function
| f_trace | tracing function for this frame, or `None`
| f_trace_lines | indicate whether a tracing event is triggered for each source source line
| f_trace_opcodes | indicate whether per-opcode events are requested
| clear() | used to clear all references to local variables
code | co_argcount | number of arguments (not including keyword only arguments, * or ** args)
| co_code | string of raw compiled bytecode
| co_cellvars | tuple of names of cell variables (referenced by containing scopes)
| co_consts | tuple of constants used in the bytecode
| co_filename | name of file in which this code object was created
| co_firstlineno | number of first line in Python source code
| co_flags | bitmap of `CO_*` flags, read more [here](https://docs.python.org/3/library/inspect.html#inspect-module-co-flags)
| co_lnotab | encoded mapping of line numbers to bytecode indices
| co_freevars | tuple of names of free variables (referenced via a function’s closure)
| co_posonlyargcount | number of positional only arguments
| co_kwonlyargcount | number of keyword only arguments (not including ** arg)
| co_name | name with which this code object was defined
| co_qualname | fully qualified name with which this code object was defined
| co_names | tuple of names other than arguments and function locals
| co_nlocals | number of local variables
| co_stacksize | virtual machine stack space required
| co_varnames | tuple of names of arguments and local variables
| co_lines() | returns an iterator that yields successive bytecode ranges
| co_positions() | returns an iterator of source code positions for each bytecode instruction
| replace() | returns a copy of the code object with new values
generator | __name__ | name
| __qualname__ | qualified name
| gi_frame | frame
| gi_running | is the generator running?
| gi_suspended | is the generator suspended?
| gi_code | code
| gi_yieldfrom | object being iterated by `yield from`, or `None`
async generator | __name__ | name
| __qualname__ | qualified name
| ag_await | object being awaited on, or `None`
| ag_frame | frame
| ag_running | is the generator running?
| ag_suspended | is the generator suspended?
| ag_code | code
coroutine | __name__ | name
| __qualname__ | qualified name
| cr_await | object being awaited on, or `None`
| cr_frame | frame
| cr_running | is the coroutine running?
| cr_suspended | is the coroutine suspended?
| cr_code | code
| cr_origin | where coroutine was created, or `None`. See [`sys.set_coroutine_origin_tracking_depth()`](https://docs.python.org/3/library/sys.html#sys.set_coroutine_origin_tracking_depth "sys.set_coroutine_origin_tracking_depth")
builtin | __doc__ | documentation string
| __name__ | original name of this function or method
| __qualname__ | qualified name
| __self__ | instance to which a method is bound, or `None`
Changed in version 3.5: Add `__qualname__` and `gi_yieldfrom` attributes to generators.
The `__name__` attribute of generators is now set from the function name, instead of the code name, and it can now be modified.
Changed in version 3.7: Add `cr_origin` attribute to coroutines.
Changed in version 3.10: Add `__builtins__` attribute to functions.
Changed in version 3.11: Add `gi_suspended` attribute to generators.
Changed in version 3.11: Add `cr_suspended` attribute to coroutines.
Changed in version 3.12: Add `ag_suspended` attribute to async generators.
Changed in version 3.14: Add `f_generator` attribute to frames.

inspect.getmembers(_object_[, _predicate_])[¶](https://docs.python.org/3/library/inspect.html#inspect.getmembers "Link to this definition")

Return all the members of an object in a list of `(name, value)` pairs sorted by name. If the optional _predicate_ argument—which will be called with the `value` object of each member—is supplied, only members for which the predicate returns a true value are included.
Note
`getmembers()` will only return class attributes defined in the metaclass when the argument is a class and those attributes have been listed in the metaclass’ custom [`__dir__()`](https://docs.python.org/3/reference/datamodel.html#object.__dir__ "object.__dir__").

inspect.getmembers_static(_object_[, _predicate_])[¶](https://docs.python.org/3/library/inspect.html#inspect.getmembers_static "Link to this definition")

Return all the members of an object in a list of `(name, value)` pairs sorted by name without triggering dynamic lookup via the descriptor protocol, __getattr__ or __getattribute__. Optionally, only return members that satisfy a given predicate.
Note
`getmembers_static()` may not be able to retrieve all members that getmembers can fetch (like dynamically created attributes) and may find members that getmembers can’t (like descriptors that raise AttributeError). It can also return descriptor objects instead of instance members in some cases.
Added in version 3.11.

inspect.getmodulename(_path_)[¶](https://docs.python.org/3/library/inspect.html#inspect.getmodulename "Link to this definition")

Return the name of the module named by the file _path_ , without including the names of enclosing packages. The file extension is checked against all of the entries in [`importlib.machinery.all_suffixes()`](https://docs.python.org/3/library/importlib.html#importlib.machinery.all_suffixes "importlib.machinery.all_suffixes"). If it matches, the final path component is returned with the extension removed. Otherwise, `None` is returned.
Note that this function _only_ returns a meaningful name for actual Python modules - paths that potentially refer to Python packages will still return `None`.
Changed in version 3.3: The function is based directly on [`importlib`](https://docs.python.org/3/library/importlib.html#module-importlib "importlib: The implementation of the import machinery.").

inspect.ismodule(_object_)[¶](https://docs.python.org/3/library/inspect.html#inspect.ismodule "Link to this definition")

Return `True` if the object is a module.

inspect.isclass(_object_)[¶](https://docs.python.org/3/library/inspect.html#inspect.isclass "Link to this definition")

Return `True` if the object is a class, whether built-in or created in Python code.

inspect.ismethod(_object_)[¶](https://docs.python.org/3/library/inspect.html#inspect.ismethod "Link to this definition")

Return `True` if the object is a bound method written in Python.

inspect.ispackage(_object_)[¶](https://docs.python.org/3/library/inspect.html#inspect.ispackage "Link to this definition")

Return `True` if the object is a [package](https://docs.python.org/3/glossary.html#term-package).
Added in version 3.14.

inspect.isfunction(_object_)[¶](https://docs.python.org/3/library/inspect.html#inspect.isfunction "Link to this definition")

Return `True` if the object is a Python function, which includes functions created by a [lambda](https://docs.python.org/3/glossary.html#term-lambda) expression.

inspect.isgeneratorfunction(_object_)[¶](https://docs.python.org/3/library/inspect.html#inspect.isgeneratorfunction "Link to this definition")

Return `True` if the object is a Python generator function.
Changed in version 3.8: Functions wrapped in [`functools.partial()`](https://docs.python.org/3/library/functools.html#functools.partial "functools.partial") now return `True` if the wrapped function is a Python generator function.
Changed in version 3.13: Functions wrapped in [`functools.partialmethod()`](https://docs.python.org/3/library/functools.html#functools.partialmethod "functools.partialmethod") now return `True` if the wrapped function is a Python generator function.

inspect.isgenerator(_object_)[¶](https://docs.python.org/3/library/inspect.html#inspect.isgenerator "Link to this definition")

Return `True` if the object is a generator.

inspect.iscoroutinefunction(_object_)[¶](https://docs.python.org/3/library/inspect.html#inspect.iscoroutinefunction "Link to this definition")

Return `True` if the object is a [coroutine function](https://docs.python.org/3/glossary.html#term-coroutine-function) (a function defined with an [`async def`](https://docs.python.org/3/reference/compound_stmts.html#async-def) syntax), a [`functools.partial()`](https://docs.python.org/3/library/functools.html#functools.partial "functools.partial") wrapping a coroutine function, or a sync function marked with [`markcoroutinefunction()`](https://docs.python.org/3/library/inspect.html#inspect.markcoroutinefunction "inspect.markcoroutinefunction").
Added in version 3.5.
Changed in version 3.8: Functions wrapped in [`functools.partial()`](https://docs.python.org/3/library/functools.html#functools.partial "functools.partial") now return `True` if the wrapped function is a [coroutine function](https://docs.python.org/3/glossary.html#term-coroutine-function).
Changed in version 3.12: Sync functions marked with [`markcoroutinefunction()`](https://docs.python.org/3/library/inspect.html#inspect.markcoroutinefunction "inspect.markcoroutinefunction") now return `True`.
Changed in version 3.13: Functions wrapped in [`functools.partialmethod()`](https://docs.python.org/3/library/functools.html#functools.partialmethod "functools.partialmethod") now return `True` if the wrapped function is a [coroutine function](https://docs.python.org/3/glossary.html#term-coroutine-function).

inspect.markcoroutinefunction(_func_)[¶](https://docs.python.org/3/library/inspect.html#inspect.markcoroutinefunction "Link to this definition")

Decorator to mark a callable as a [coroutine function](https://docs.python.org/3/glossary.html#term-coroutine-function) if it would not otherwise be detected by [`iscoroutinefunction()`](https://docs.python.org/3/library/inspect.html#inspect.iscoroutinefunction "inspect.iscoroutinefunction").
This may be of use for sync functions that return a [coroutine](https://docs.python.org/3/glossary.html#term-coroutine), if the function is passed to an API that requires [`iscoroutinefunction()`](https://docs.python.org/3/library/inspect.html#inspect.iscoroutinefunction "inspect.iscoroutinefunction").
When possible, using an [`async def`](https://docs.python.org/3/reference/compound_stmts.html#async-def) function is preferred. Also acceptable is calling the function and testing the return with [`iscoroutine()`](https://docs.python.org/3/library/inspect.html#inspect.iscoroutine "inspect.iscoroutine").
Added in version 3.12.

inspect.iscoroutine(_object_)[¶](https://docs.python.org/3/library/inspect.html#inspect.iscoroutine "Link to this definition")

Return `True` if the object is a [coroutine](https://docs.python.org/3/glossary.html#term-coroutine) created by an [`async def`](https://docs.python.org/3/reference/compound_stmts.html#async-def) function.
Added in version 3.5.

inspect.isawaitable(_object_)[¶](https://docs.python.org/3/library/inspect.html#inspect.isawaitable "Link to this definition")

Return `True` if the object can be used in [`await`](https://docs.python.org/3/reference/expressions.html#await) expression.
Can also be used to distinguish generator-based coroutines from regular generators:
Copy```
import types

def gen():
    yield
@types.coroutine
def gen_coro():
    yield

assert not isawaitable(gen())
assert isawaitable(gen_coro())

```

Added in version 3.5.

inspect.isasyncgenfunction(_object_)[¶](https://docs.python.org/3/library/inspect.html#inspect.isasyncgenfunction "Link to this definition")

Return `True` if the object is an [asynchronous generator](https://docs.python.org/3/glossary.html#term-asynchronous-generator) function, for example:
Copy```
>>> async def agen():
...     yield 1
...
>>> inspect.isasyncgenfunction(agen)
True

```

Added in version 3.6.
Changed in version 3.8: Functions wrapped in [`functools.partial()`](https://docs.python.org/3/library/functools.html#functools.partial "functools.partial") now return `True` if the wrapped function is an [asynchronous generator](https://docs.python.org/3/glossary.html#term-asynchronous-generator) function.
Changed in version 3.13: Functions wrapped in [`functools.partialmethod()`](https://docs.python.org/3/library/functools.html#functools.partialmethod "functools.partialmethod") now return `True` if the wrapped function is a [asynchronous generator](https://docs.python.org/3/glossary.html#term-asynchronous-generator) function.

inspect.isasyncgen(_object_)[¶](https://docs.python.org/3/library/inspect.html#inspect.isasyncgen "Link to this definition")

Return `True` if the object is an [asynchronous generator iterator](https://docs.python.org/3/glossary.html#term-asynchronous-generator-iterator) created by an [asynchronous generator](https://docs.python.org/3/glossary.html#term-asynchronous-generator) function.
Added in version 3.6.

inspect.istraceback(_object_)[¶](https://docs.python.org/3/library/inspect.html#inspect.istraceback "Link to this definition")

Return `True` if the object is a traceback.

inspect.isframe(_object_)[¶](https://docs.python.org/3/library/inspect.html#inspect.isframe "Link to this definition")

Return `True` if the object is a frame.

inspect.iscode(_object_)[¶](https://docs.python.org/3/library/inspect.html#inspect.iscode "Link to this definition")

Return `True` if the object is a code.

inspect.isbuiltin(_object_)[¶](https://docs.python.org/3/library/inspect.html#inspect.isbuiltin "Link to this definition")

Return `True` if the object is a built-in function or a bound built-in method.

inspect.ismethodwrapper(_object_)[¶](https://docs.python.org/3/library/inspect.html#inspect.ismethodwrapper "Link to this definition")

Return `True` if the type of object is a [`MethodWrapperType`](https://docs.python.org/3/library/types.html#types.MethodWrapperType "types.MethodWrapperType").
These are instances of [`MethodWrapperType`](https://docs.python.org/3/library/types.html#types.MethodWrapperType "types.MethodWrapperType"), such as [`__str__()`](https://docs.python.org/3/reference/datamodel.html#object.__str__ "object.__str__"), [`__eq__()`](https://docs.python.org/3/reference/datamodel.html#object.__eq__ "object.__eq__") and [`__repr__()`](https://docs.python.org/3/reference/datamodel.html#object.__repr__ "object.__repr__").
Added in version 3.11.

inspect.isroutine(_object_)[¶](https://docs.python.org/3/library/inspect.html#inspect.isroutine "Link to this definition")

Return `True` if the object is a user-defined or built-in function or method.

inspect.isabstract(_object_)[¶](https://docs.python.org/3/library/inspect.html#inspect.isabstract "Link to this definition")

Return `True` if the object is an abstract base class.

inspect.ismethoddescriptor(_object_)[¶](https://docs.python.org/3/library/inspect.html#inspect.ismethoddescriptor "Link to this definition")

Return `True` if the object is a method descriptor, but not if [`ismethod()`](https://docs.python.org/3/library/inspect.html#inspect.ismethod "inspect.ismethod"), [`isclass()`](https://docs.python.org/3/library/inspect.html#inspect.isclass "inspect.isclass"), [`isfunction()`](https://docs.python.org/3/library/inspect.html#inspect.isfunction "inspect.isfunction") or [`isbuiltin()`](https://docs.python.org/3/library/inspect.html#inspect.isbuiltin "inspect.isbuiltin") are true.
This, for example, is true of `int.__add__`. An object passing this test has a [`__get__()`](https://docs.python.org/3/reference/datamodel.html#object.__get__ "object.__get__") method, but not a [`__set__()`](https://docs.python.org/3/reference/datamodel.html#object.__set__ "object.__set__") method or a [`__delete__()`](https://docs.python.org/3/reference/datamodel.html#object.__delete__ "object.__delete__") method. Beyond that, the set of attributes varies. A [`__name__`](https://docs.python.org/3/library/stdtypes.html#definition.__name__ "definition.__name__") attribute is usually sensible, and [`__doc__`](https://docs.python.org/3/library/stdtypes.html#definition.__doc__ "definition.__doc__") often is.
Methods implemented via descriptors that also pass one of the other tests return `False` from the `ismethoddescriptor()` test, simply because the other tests promise more – you can, e.g., count on having the [`__func__`](https://docs.python.org/3/reference/datamodel.html#method.__func__ "method.__func__") attribute (etc) when an object passes [`ismethod()`](https://docs.python.org/3/library/inspect.html#inspect.ismethod "inspect.ismethod").
Changed in version 3.13: This function no longer incorrectly reports objects with [`__get__()`](https://docs.python.org/3/reference/datamodel.html#object.__get__ "object.__get__") and [`__delete__()`](https://docs.python.org/3/reference/datamodel.html#object.__delete__ "object.__delete__"), but not [`__set__()`](https://docs.python.org/3/reference/datamodel.html#object.__set__ "object.__set__"), as being method descriptors (such objects are data descriptors, not method descriptors).

inspect.isdatadescriptor(_object_)[¶](https://docs.python.org/3/library/inspect.html#inspect.isdatadescriptor "Link to this definition")

Return `True` if the object is a data descriptor.
Data descriptors have a [`__set__`](https://docs.python.org/3/reference/datamodel.html#object.__set__ "object.__set__") or a [`__delete__`](https://docs.python.org/3/reference/datamodel.html#object.__delete__ "object.__delete__") method. Examples are properties (defined in Python), getsets, and members. The latter two are defined in C and there are more specific tests available for those types, which is robust across Python implementations. Typically, data descriptors will also have [`__name__`](https://docs.python.org/3/library/stdtypes.html#definition.__name__ "definition.__name__") and `__doc__` attributes (properties, getsets, and members have both of these attributes), but this is not guaranteed.

inspect.isgetsetdescriptor(_object_)[¶](https://docs.python.org/3/library/inspect.html#inspect.isgetsetdescriptor "Link to this definition")

Return `True` if the object is a getset descriptor.
**CPython implementation detail:** getsets are attributes defined in extension modules via [`PyGetSetDef`](https://docs.python.org/3/c-api/structures.html#c.PyGetSetDef "PyGetSetDef") structures. For Python implementations without such types, this method will always return `False`.

inspect.ismemberdescriptor(_object_)[¶](https://docs.python.org/3/library/inspect.html#inspect.ismemberdescriptor "Link to this definition")

Return `True` if the object is a member descriptor.
**CPython implementation detail:** Member descriptors are attributes defined in extension modules via [`PyMemberDef`](https://docs.python.org/3/c-api/structures.html#c.PyMemberDef "PyMemberDef") structures. For Python implementations without such types, this method will always return `False`.
