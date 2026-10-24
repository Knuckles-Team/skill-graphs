## Classes and functions[¶](https://docs.python.org/3/library/inspect.html#classes-and-functions "Link to this heading")

inspect.getclasstree(_classes_ , _unique =False_)[¶](https://docs.python.org/3/library/inspect.html#inspect.getclasstree "Link to this definition")

Arrange the given list of classes into a hierarchy of nested lists. Where a nested list appears, it contains classes derived from the class whose entry immediately precedes the list. Each entry is a 2-tuple containing a class and a tuple of its base classes. If the _unique_ argument is true, exactly one entry appears in the returned structure for each class in the given list. Otherwise, classes using multiple inheritance and their descendants will appear multiple times.

inspect.getfullargspec(_func_)[¶](https://docs.python.org/3/library/inspect.html#inspect.getfullargspec "Link to this definition")

Get the names and default values of a Python function’s parameters. A [named tuple](https://docs.python.org/3/glossary.html#term-named-tuple) is returned:
`FullArgSpec(args, varargs, varkw, defaults, kwonlyargs, kwonlydefaults, annotations)`
_args_ is a list of the positional parameter names. _varargs_ is the name of the `*` parameter or `None` if arbitrary positional arguments are not accepted. _varkw_ is the name of the `**` parameter or `None` if arbitrary keyword arguments are not accepted. _defaults_ is an _n_ -tuple of default argument values corresponding to the last _n_ positional parameters, or `None` if there are no such defaults defined. _kwonlyargs_ is a list of keyword-only parameter names in declaration order. _kwonlydefaults_ is a dictionary mapping parameter names from _kwonlyargs_ to the default values used if no argument is supplied. _annotations_ is a dictionary mapping parameter names to annotations. The special key `"return"` is used to report the function return value annotation (if any).
Note that [`signature()`](https://docs.python.org/3/library/inspect.html#inspect.signature "inspect.signature") and [Signature Object](https://docs.python.org/3/library/inspect.html#inspect-signature-object) provide the recommended API for callable introspection, and support additional behaviours (like positional-only arguments) that are sometimes encountered in extension module APIs. This function is retained primarily for use in code that needs to maintain compatibility with the Python 2 `inspect` module API.
Changed in version 3.4: This function is now based on [`signature()`](https://docs.python.org/3/library/inspect.html#inspect.signature "inspect.signature"), but still ignores `__wrapped__` attributes and includes the already bound first parameter in the signature output for bound methods.
Changed in version 3.6: This method was previously documented as deprecated in favour of [`signature()`](https://docs.python.org/3/library/inspect.html#inspect.signature "inspect.signature") in Python 3.5, but that decision has been reversed in order to restore a clearly supported standard interface for single-source Python 2/3 code migrating away from the legacy `getargspec()` API.
Changed in version 3.7: Python only explicitly guaranteed that it preserved the declaration order of keyword-only parameters as of version 3.7, although in practice this order had always been preserved in Python 3.

inspect.getargvalues(_frame_)[¶](https://docs.python.org/3/library/inspect.html#inspect.getargvalues "Link to this definition")

Get information about arguments passed into a particular frame. A [named tuple](https://docs.python.org/3/glossary.html#term-named-tuple) `ArgInfo(args, varargs, keywords, locals)` is returned. _args_ is a list of the argument names. _varargs_ and _keywords_ are the names of the `*` and `**` arguments or `None`. _locals_ is the locals dictionary of the given frame.
Note
This function was inadvertently marked as deprecated in Python 3.5.

inspect.formatargvalues(_args_[, _varargs_ , _varkw_ , _locals_ , _formatarg_ , _formatvarargs_ , _formatvarkw_ , _formatvalue_])[¶](https://docs.python.org/3/library/inspect.html#inspect.formatargvalues "Link to this definition")

Format a pretty argument spec from the four values returned by [`getargvalues()`](https://docs.python.org/3/library/inspect.html#inspect.getargvalues "inspect.getargvalues"). The format* arguments are the corresponding optional formatting functions that are called to turn names and values into strings.
Note
This function was inadvertently marked as deprecated in Python 3.5.

inspect.getmro(_cls_)[¶](https://docs.python.org/3/library/inspect.html#inspect.getmro "Link to this definition")

Return a tuple of class cls’s base classes, including cls, in method resolution order. No class appears more than once in this tuple. Note that the method resolution order depends on cls’s type. Unless a very peculiar user-defined metatype is in use, cls will be the first element of the tuple.

inspect.getcallargs(_func_ , _/_ , _* args_, _** kwds_)[¶](https://docs.python.org/3/library/inspect.html#inspect.getcallargs "Link to this definition")

Bind the _args_ and _kwds_ to the argument names of the Python function or method _func_ , as if it was called with them. For bound methods, bind also the first argument (typically named `self`) to the associated instance. A dict is returned, mapping the argument names (including the names of the `*` and `**` arguments, if any) to their values from _args_ and _kwds_. In case of invoking _func_ incorrectly, i.e. whenever `func(*args, **kwds)` would raise an exception because of incompatible signature, an exception of the same type and the same or similar message is raised. For example:
Copy```
>>> from inspect import getcallargs
>>> def f(a, b=1, *pos, **named):
...     pass
...
>>> getcallargs(f, 1, 2, 3) == {'a': 1, 'named': {}, 'b': 2, 'pos': (3,)}
True
>>> getcallargs(f, a=2, x=4) == {'a': 2, 'named': {'x': 4}, 'b': 1, 'pos': ()}
True
>>> getcallargs(f)
Traceback (most recent call last):
...
TypeError: f() missing 1 required positional argument: 'a'

```

Added in version 3.2.
Deprecated since version 3.5: Use [`Signature.bind()`](https://docs.python.org/3/library/inspect.html#inspect.Signature.bind "inspect.Signature.bind") and [`Signature.bind_partial()`](https://docs.python.org/3/library/inspect.html#inspect.Signature.bind_partial "inspect.Signature.bind_partial") instead.

inspect.getclosurevars(_func_)[¶](https://docs.python.org/3/library/inspect.html#inspect.getclosurevars "Link to this definition")

Get the mapping of external name references in a Python function or method _func_ to their current values. A [named tuple](https://docs.python.org/3/glossary.html#term-named-tuple) `ClosureVars(nonlocals, globals, builtins, unbound)` is returned. _nonlocals_ maps referenced names to lexical closure variables, _globals_ to the function’s module globals and _builtins_ to the builtins visible from the function body. _unbound_ is the set of names referenced in the function that could not be resolved at all given the current module globals and builtins.
[`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") is raised if _func_ is not a Python function or method.
Added in version 3.3.

inspect.unwrap(_func_ , _*_ , _stop =None_)[¶](https://docs.python.org/3/library/inspect.html#inspect.unwrap "Link to this definition")

Get the object wrapped by _func_. It follows the chain of `__wrapped__` attributes returning the last object in the chain.
_stop_ is an optional callback accepting an object in the wrapper chain as its sole argument that allows the unwrapping to be terminated early if the callback returns a true value. If the callback never returns a true value, the last object in the chain is returned as usual. For example, [`signature()`](https://docs.python.org/3/library/inspect.html#inspect.signature "inspect.signature") uses this to stop unwrapping if any object in the chain has a `__signature__` attribute defined.
[`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised if a cycle is encountered.
Added in version 3.4.

inspect.get_annotations(_obj_ , _*_ , _globals =None_, _locals =None_, _eval_str =False_, _format =annotationlib.Format.VALUE_)[¶](https://docs.python.org/3/library/inspect.html#inspect.get_annotations "Link to this definition")

Compute the annotations dict for an object.
This is an alias for [`annotationlib.get_annotations()`](https://docs.python.org/3/library/annotationlib.html#annotationlib.get_annotations "annotationlib.get_annotations"); see the documentation of that function for more information.
Caution
This function may execute arbitrary code contained in annotations. See [Security implications of introspecting annotations](https://docs.python.org/3/library/annotationlib.html#annotationlib-security) for more information.
Added in version 3.10.
Changed in version 3.14: This function is now an alias for [`annotationlib.get_annotations()`](https://docs.python.org/3/library/annotationlib.html#annotationlib.get_annotations "annotationlib.get_annotations"). Calling it as `inspect.get_annotations` will continue to work.
## The interpreter stack[¶](https://docs.python.org/3/library/inspect.html#the-interpreter-stack "Link to this heading")
Some of the following functions return [`FrameInfo`](https://docs.python.org/3/library/inspect.html#inspect.FrameInfo "inspect.FrameInfo") objects. For backwards compatibility these objects allow tuple-like operations on all attributes except `positions`. This behavior is considered deprecated and may be removed in the future.

_class_ inspect.FrameInfo[¶](https://docs.python.org/3/library/inspect.html#inspect.FrameInfo "Link to this definition")


frame[¶](https://docs.python.org/3/library/inspect.html#inspect.FrameInfo.frame "Link to this definition")

The [frame object](https://docs.python.org/3/reference/datamodel.html#frame-objects) that the record corresponds to.

filename[¶](https://docs.python.org/3/library/inspect.html#inspect.FrameInfo.filename "Link to this definition")

The file name associated with the code being executed by the frame this record corresponds to.

lineno[¶](https://docs.python.org/3/library/inspect.html#inspect.FrameInfo.lineno "Link to this definition")

The line number of the current line associated with the code being executed by the frame this record corresponds to.

function[¶](https://docs.python.org/3/library/inspect.html#inspect.FrameInfo.function "Link to this definition")

The function name that is being executed by the frame this record corresponds to.

code_context[¶](https://docs.python.org/3/library/inspect.html#inspect.FrameInfo.code_context "Link to this definition")

A list of lines of context from the source code that’s being executed by the frame this record corresponds to.

index[¶](https://docs.python.org/3/library/inspect.html#inspect.FrameInfo.index "Link to this definition")

The index of the current line being executed in the [`code_context`](https://docs.python.org/3/library/inspect.html#inspect.FrameInfo.code_context "inspect.FrameInfo.code_context") list.

positions[¶](https://docs.python.org/3/library/inspect.html#inspect.FrameInfo.positions "Link to this definition")

A [`dis.Positions`](https://docs.python.org/3/library/dis.html#dis.Positions "dis.Positions") object containing the start line number, end line number, start column offset, and end column offset associated with the instruction being executed by the frame this record corresponds to.
Changed in version 3.5: Return a [named tuple](https://docs.python.org/3/glossary.html#term-named-tuple) instead of a [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "tuple").
Changed in version 3.11: `FrameInfo` is now a class instance (that is backwards compatible with the previous [named tuple](https://docs.python.org/3/glossary.html#term-named-tuple)).

_class_ inspect.Traceback[¶](https://docs.python.org/3/library/inspect.html#inspect.Traceback "Link to this definition")


filename[¶](https://docs.python.org/3/library/inspect.html#inspect.Traceback.filename "Link to this definition")

The file name associated with the code being executed by the frame this traceback corresponds to.

lineno[¶](https://docs.python.org/3/library/inspect.html#inspect.Traceback.lineno "Link to this definition")

The line number of the current line associated with the code being executed by the frame this traceback corresponds to.

function[¶](https://docs.python.org/3/library/inspect.html#inspect.Traceback.function "Link to this definition")

The function name that is being executed by the frame this traceback corresponds to.

code_context[¶](https://docs.python.org/3/library/inspect.html#inspect.Traceback.code_context "Link to this definition")

A list of lines of context from the source code that’s being executed by the frame this traceback corresponds to.

index[¶](https://docs.python.org/3/library/inspect.html#inspect.Traceback.index "Link to this definition")

The index of the current line being executed in the [`code_context`](https://docs.python.org/3/library/inspect.html#inspect.Traceback.code_context "inspect.Traceback.code_context") list.

positions[¶](https://docs.python.org/3/library/inspect.html#inspect.Traceback.positions "Link to this definition")

A [`dis.Positions`](https://docs.python.org/3/library/dis.html#dis.Positions "dis.Positions") object containing the start line number, end line number, start column offset, and end column offset associated with the instruction being executed by the frame this traceback corresponds to.
Changed in version 3.11: `Traceback` is now a class instance (that is backwards compatible with the previous [named tuple](https://docs.python.org/3/glossary.html#term-named-tuple)).
Note
Keeping references to frame objects, as found in the first element of the frame records these functions return, can cause your program to create reference cycles. Once a reference cycle has been created, the lifespan of all objects which can be accessed from the objects which form the cycle can become much longer even if Python’s optional cycle detector is enabled. If such cycles must be created, it is important to ensure they are explicitly broken to avoid the delayed destruction of objects and increased memory consumption which occurs.
Though the cycle detector will catch these, destruction of the frames (and local variables) can be made deterministic by removing the cycle in a [`finally`](https://docs.python.org/3/reference/compound_stmts.html#finally) clause. This is also important if the cycle detector was disabled when Python was compiled or using [`gc.disable()`](https://docs.python.org/3/library/gc.html#gc.disable "gc.disable"). For example:
Copy```
def handle_stackframe_without_leak():
    frame = inspect.currentframe()
    try:
        # do something with the frame
    finally:
        del frame

```

If you want to keep the frame around (for example to print a traceback later), you can also break reference cycles by using the [`frame.clear()`](https://docs.python.org/3/reference/datamodel.html#frame.clear "frame.clear") method.
The optional _context_ argument supported by most of these functions specifies the number of lines of context to return, which are centered around the current line.

inspect.getframeinfo(_frame_ , _context =1_)[¶](https://docs.python.org/3/library/inspect.html#inspect.getframeinfo "Link to this definition")

Get information about a frame or traceback object. A [`Traceback`](https://docs.python.org/3/library/inspect.html#inspect.Traceback "inspect.Traceback") object is returned.
Changed in version 3.11: A [`Traceback`](https://docs.python.org/3/library/inspect.html#inspect.Traceback "inspect.Traceback") object is returned instead of a named tuple.

inspect.getouterframes(_frame_ , _context =1_)[¶](https://docs.python.org/3/library/inspect.html#inspect.getouterframes "Link to this definition")

Get a list of [`FrameInfo`](https://docs.python.org/3/library/inspect.html#inspect.FrameInfo "inspect.FrameInfo") objects for a frame and all outer frames. These frames represent the calls that lead to the creation of _frame_. The first entry in the returned list represents _frame_ ; the last entry represents the outermost call on _frame_ ’s stack.
Changed in version 3.5: A list of [named tuples](https://docs.python.org/3/glossary.html#term-named-tuple) `FrameInfo(frame, filename, lineno, function, code_context, index)` is returned.
Changed in version 3.11: A list of [`FrameInfo`](https://docs.python.org/3/library/inspect.html#inspect.FrameInfo "inspect.FrameInfo") objects is returned.

inspect.getinnerframes(_traceback_ , _context =1_)[¶](https://docs.python.org/3/library/inspect.html#inspect.getinnerframes "Link to this definition")

Get a list of [`FrameInfo`](https://docs.python.org/3/library/inspect.html#inspect.FrameInfo "inspect.FrameInfo") objects for a traceback’s frame and all inner frames. These frames represent calls made as a consequence of _frame_. The first entry in the list represents _traceback_ ; the last entry represents where the exception was raised.
Changed in version 3.5: A list of [named tuples](https://docs.python.org/3/glossary.html#term-named-tuple) `FrameInfo(frame, filename, lineno, function, code_context, index)` is returned.
Changed in version 3.11: A list of [`FrameInfo`](https://docs.python.org/3/library/inspect.html#inspect.FrameInfo "inspect.FrameInfo") objects is returned.

inspect.currentframe()[¶](https://docs.python.org/3/library/inspect.html#inspect.currentframe "Link to this definition")

Return the frame object for the caller’s stack frame.
**CPython implementation detail:** This function relies on Python stack frame support in the interpreter, which isn’t guaranteed to exist in all implementations of Python. If running in an implementation without Python stack frame support this function returns `None`.

inspect.stack(_context =1_)[¶](https://docs.python.org/3/library/inspect.html#inspect.stack "Link to this definition")

Return a list of [`FrameInfo`](https://docs.python.org/3/library/inspect.html#inspect.FrameInfo "inspect.FrameInfo") objects for the caller’s stack. The first entry in the returned list represents the caller; the last entry represents the outermost call on the stack.
Changed in version 3.5: A list of [named tuples](https://docs.python.org/3/glossary.html#term-named-tuple) `FrameInfo(frame, filename, lineno, function, code_context, index)` is returned.
Changed in version 3.11: A list of [`FrameInfo`](https://docs.python.org/3/library/inspect.html#inspect.FrameInfo "inspect.FrameInfo") objects is returned.

inspect.trace(_context =1_)[¶](https://docs.python.org/3/library/inspect.html#inspect.trace "Link to this definition")

Return a list of [`FrameInfo`](https://docs.python.org/3/library/inspect.html#inspect.FrameInfo "inspect.FrameInfo") objects for the stack between the current frame and the frame in which an exception currently being handled was raised in. The first entry in the list represents the caller; the last entry represents where the exception was raised.
Changed in version 3.5: A list of [named tuples](https://docs.python.org/3/glossary.html#term-named-tuple) `FrameInfo(frame, filename, lineno, function, code_context, index)` is returned.
Changed in version 3.11: A list of [`FrameInfo`](https://docs.python.org/3/library/inspect.html#inspect.FrameInfo "inspect.FrameInfo") objects is returned.
