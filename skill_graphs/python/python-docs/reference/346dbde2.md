# example code for resolving the builtin descriptor types
class _foo:
    __slots__ = ['foo']

slot_descriptor = type(_foo.foo)
getset_descriptor = type(type(open(__file__)).name)
wrapper_descriptor = type(str.__dict__['__add__'])
descriptor_types = (slot_descriptor, getset_descriptor, wrapper_descriptor)

result = getattr_static(some_object, 'foo')
if type(result) in descriptor_types:
    try:
        result = result.__get__()
    except AttributeError:
        # descriptors can raise AttributeError to
        # indicate there is no underlying value
        # in which case the descriptor itself will
        # have to do
        pass

```

## Current State of Generators, Coroutines, and Asynchronous Generators[¶](https://docs.python.org/3/library/inspect.html#current-state-of-generators-coroutines-and-asynchronous-generators "Link to this heading")
When implementing coroutine schedulers and for other advanced uses of generators, it is useful to determine whether a generator is currently executing, is waiting to start or resume or execution, or has already terminated. [`getgeneratorstate()`](https://docs.python.org/3/library/inspect.html#inspect.getgeneratorstate "inspect.getgeneratorstate") allows the current state of a generator to be determined easily.

inspect.getgeneratorstate(_generator_)[¶](https://docs.python.org/3/library/inspect.html#inspect.getgeneratorstate "Link to this definition")

Get current state of a generator-iterator.
Possible states are:
  * GEN_CREATED: Waiting to start execution.
  * GEN_RUNNING: Currently being executed by the interpreter.
  * GEN_SUSPENDED: Currently suspended at a yield expression.
  * GEN_CLOSED: Execution has completed.


Added in version 3.2.

inspect.getcoroutinestate(_coroutine_)[¶](https://docs.python.org/3/library/inspect.html#inspect.getcoroutinestate "Link to this definition")

Get current state of a coroutine object. The function is intended to be used with coroutine objects created by [`async def`](https://docs.python.org/3/reference/compound_stmts.html#async-def) functions, but will accept any coroutine-like object that has `cr_running` and `cr_frame` attributes.
Possible states are:
  * CORO_CREATED: Waiting to start execution.
  * CORO_RUNNING: Currently being executed by the interpreter.
  * CORO_SUSPENDED: Currently suspended at an await expression.
  * CORO_CLOSED: Execution has completed.


Added in version 3.5.

inspect.getasyncgenstate(_agen_)[¶](https://docs.python.org/3/library/inspect.html#inspect.getasyncgenstate "Link to this definition")

Get current state of an asynchronous generator object. The function is intended to be used with asynchronous iterator objects created by [`async def`](https://docs.python.org/3/reference/compound_stmts.html#async-def) functions which use the [`yield`](https://docs.python.org/3/reference/simple_stmts.html#yield) statement, but will accept any asynchronous generator-like object that has `ag_running` and `ag_frame` attributes.
Possible states are:
  * AGEN_CREATED: Waiting to start execution.
  * AGEN_RUNNING: Currently being executed by the interpreter.
  * AGEN_SUSPENDED: Currently suspended at a yield expression.
  * AGEN_CLOSED: Execution has completed.


Added in version 3.12.
The current internal state of the generator can also be queried. This is mostly useful for testing purposes, to ensure that internal state is being updated as expected:

inspect.getgeneratorlocals(_generator_)[¶](https://docs.python.org/3/library/inspect.html#inspect.getgeneratorlocals "Link to this definition")

Get the mapping of live local variables in _generator_ to their current values. A dictionary is returned that maps from variable names to values. This is the equivalent of calling [`locals()`](https://docs.python.org/3/library/functions.html#locals "locals") in the body of the generator, and all the same caveats apply.
If _generator_ is a [generator](https://docs.python.org/3/glossary.html#term-generator) with no currently associated frame, then an empty dictionary is returned. [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") is raised if _generator_ is not a Python generator object.
**CPython implementation detail:** This function relies on the generator exposing a Python stack frame for introspection, which isn’t guaranteed to be the case in all implementations of Python. In such cases, this function will always return an empty dictionary.
Added in version 3.3.

inspect.getcoroutinelocals(_coroutine_)[¶](https://docs.python.org/3/library/inspect.html#inspect.getcoroutinelocals "Link to this definition")

This function is analogous to [`getgeneratorlocals()`](https://docs.python.org/3/library/inspect.html#inspect.getgeneratorlocals "inspect.getgeneratorlocals"), but works for coroutine objects created by [`async def`](https://docs.python.org/3/reference/compound_stmts.html#async-def) functions.
Added in version 3.5.

inspect.getasyncgenlocals(_agen_)[¶](https://docs.python.org/3/library/inspect.html#inspect.getasyncgenlocals "Link to this definition")

This function is analogous to [`getgeneratorlocals()`](https://docs.python.org/3/library/inspect.html#inspect.getgeneratorlocals "inspect.getgeneratorlocals"), but works for asynchronous generator objects created by [`async def`](https://docs.python.org/3/reference/compound_stmts.html#async-def) functions which use the [`yield`](https://docs.python.org/3/reference/simple_stmts.html#yield) statement.
Added in version 3.12.
## Code Objects Bit Flags[¶](https://docs.python.org/3/library/inspect.html#code-objects-bit-flags "Link to this heading")
Python code objects have a [`co_flags`](https://docs.python.org/3/reference/datamodel.html#codeobject.co_flags "codeobject.co_flags") attribute, which is a bitmap of the following flags:

inspect.CO_OPTIMIZED[¶](https://docs.python.org/3/library/inspect.html#inspect.CO_OPTIMIZED "Link to this definition")

The code object is optimized, using fast locals.

inspect.CO_NEWLOCALS[¶](https://docs.python.org/3/library/inspect.html#inspect.CO_NEWLOCALS "Link to this definition")

If set, a new dict will be created for the frame’s [`f_locals`](https://docs.python.org/3/reference/datamodel.html#frame.f_locals "frame.f_locals") when the code object is executed.

inspect.CO_VARARGS[¶](https://docs.python.org/3/library/inspect.html#inspect.CO_VARARGS "Link to this definition")

The code object has a variable positional parameter (`*args`-like).

inspect.CO_VARKEYWORDS[¶](https://docs.python.org/3/library/inspect.html#inspect.CO_VARKEYWORDS "Link to this definition")

The code object has a variable keyword parameter (`**kwargs`-like).

inspect.CO_NESTED[¶](https://docs.python.org/3/library/inspect.html#inspect.CO_NESTED "Link to this definition")

The flag is set when the code object is a nested function.

inspect.CO_GENERATOR[¶](https://docs.python.org/3/library/inspect.html#inspect.CO_GENERATOR "Link to this definition")

The flag is set when the code object is a generator function, i.e. a generator object is returned when the code object is executed.

inspect.CO_COROUTINE[¶](https://docs.python.org/3/library/inspect.html#inspect.CO_COROUTINE "Link to this definition")

The flag is set when the code object is a coroutine function. When the code object is executed it returns a coroutine object. See [**PEP 492**](https://peps.python.org/pep-0492/) for more details.
Added in version 3.5.

inspect.CO_ITERABLE_COROUTINE[¶](https://docs.python.org/3/library/inspect.html#inspect.CO_ITERABLE_COROUTINE "Link to this definition")

The flag is used to transform generators into generator-based coroutines. Generator objects with this flag can be used in `await` expression, and can `yield from` coroutine objects. See [**PEP 492**](https://peps.python.org/pep-0492/) for more details.
Added in version 3.5.

inspect.CO_ASYNC_GENERATOR[¶](https://docs.python.org/3/library/inspect.html#inspect.CO_ASYNC_GENERATOR "Link to this definition")

The flag is set when the code object is an asynchronous generator function. When the code object is executed it returns an asynchronous generator object. See [**PEP 525**](https://peps.python.org/pep-0525/) for more details.
Added in version 3.6.

inspect.CO_HAS_DOCSTRING[¶](https://docs.python.org/3/library/inspect.html#inspect.CO_HAS_DOCSTRING "Link to this definition")

The flag is set when there is a docstring for the code object in the source code. If set, it will be the first item in [`co_consts`](https://docs.python.org/3/reference/datamodel.html#codeobject.co_consts "codeobject.co_consts").
Added in version 3.14.

inspect.CO_METHOD[¶](https://docs.python.org/3/library/inspect.html#inspect.CO_METHOD "Link to this definition")

The flag is set when the code object is a function defined in class scope.
Added in version 3.14.
Note
The flags are specific to CPython, and may not be defined in other Python implementations. Furthermore, the flags are an implementation detail, and can be removed or deprecated in future Python releases. It’s recommended to use public APIs from the `inspect` module for any introspection needs.
## Buffer flags[¶](https://docs.python.org/3/library/inspect.html#buffer-flags "Link to this heading")

_class_ inspect.BufferFlags[¶](https://docs.python.org/3/library/inspect.html#inspect.BufferFlags "Link to this definition")

This is an [`enum.IntFlag`](https://docs.python.org/3/library/enum.html#enum.IntFlag "enum.IntFlag") that represents the flags that can be passed to the [`__buffer__()`](https://docs.python.org/3/reference/datamodel.html#object.__buffer__ "object.__buffer__") method of objects implementing the [buffer protocol](https://docs.python.org/3/c-api/buffer.html#bufferobjects).
The meaning of the flags is explained at [Buffer request types](https://docs.python.org/3/c-api/buffer.html#buffer-request-types).

SIMPLE[¶](https://docs.python.org/3/library/inspect.html#inspect.BufferFlags.SIMPLE "Link to this definition")


WRITABLE[¶](https://docs.python.org/3/library/inspect.html#inspect.BufferFlags.WRITABLE "Link to this definition")


FORMAT[¶](https://docs.python.org/3/library/inspect.html#inspect.BufferFlags.FORMAT "Link to this definition")


ND[¶](https://docs.python.org/3/library/inspect.html#inspect.BufferFlags.ND "Link to this definition")


STRIDES[¶](https://docs.python.org/3/library/inspect.html#inspect.BufferFlags.STRIDES "Link to this definition")


C_CONTIGUOUS[¶](https://docs.python.org/3/library/inspect.html#inspect.BufferFlags.C_CONTIGUOUS "Link to this definition")


F_CONTIGUOUS[¶](https://docs.python.org/3/library/inspect.html#inspect.BufferFlags.F_CONTIGUOUS "Link to this definition")


ANY_CONTIGUOUS[¶](https://docs.python.org/3/library/inspect.html#inspect.BufferFlags.ANY_CONTIGUOUS "Link to this definition")


INDIRECT[¶](https://docs.python.org/3/library/inspect.html#inspect.BufferFlags.INDIRECT "Link to this definition")


CONTIG[¶](https://docs.python.org/3/library/inspect.html#inspect.BufferFlags.CONTIG "Link to this definition")


CONTIG_RO[¶](https://docs.python.org/3/library/inspect.html#inspect.BufferFlags.CONTIG_RO "Link to this definition")


STRIDED[¶](https://docs.python.org/3/library/inspect.html#inspect.BufferFlags.STRIDED "Link to this definition")


STRIDED_RO[¶](https://docs.python.org/3/library/inspect.html#inspect.BufferFlags.STRIDED_RO "Link to this definition")


RECORDS[¶](https://docs.python.org/3/library/inspect.html#inspect.BufferFlags.RECORDS "Link to this definition")


RECORDS_RO[¶](https://docs.python.org/3/library/inspect.html#inspect.BufferFlags.RECORDS_RO "Link to this definition")


FULL[¶](https://docs.python.org/3/library/inspect.html#inspect.BufferFlags.FULL "Link to this definition")


FULL_RO[¶](https://docs.python.org/3/library/inspect.html#inspect.BufferFlags.FULL_RO "Link to this definition")


READ[¶](https://docs.python.org/3/library/inspect.html#inspect.BufferFlags.READ "Link to this definition")


WRITE[¶](https://docs.python.org/3/library/inspect.html#inspect.BufferFlags.WRITE "Link to this definition")

Added in version 3.12.
## Command-line interface[¶](https://docs.python.org/3/library/inspect.html#command-line-interface "Link to this heading")
The `inspect` module also provides a basic introspection capability from the command line.
By default, accepts the name of a module and prints the source of that module. A class or function within the module can be printed instead by appended a colon and the qualified name of the target object.

--details[¶](https://docs.python.org/3/library/inspect.html#cmdoption-inspect-details "Link to this definition")

Print information about the specified object rather than the source code
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`inspect` — Inspect live objects](https://docs.python.org/3/library/inspect.html)
    * [Types and members](https://docs.python.org/3/library/inspect.html#types-and-members)
    * [Retrieving source code](https://docs.python.org/3/library/inspect.html#retrieving-source-code)
    * [Introspecting callables with the Signature object](https://docs.python.org/3/library/inspect.html#introspecting-callables-with-the-signature-object)
    * [Classes and functions](https://docs.python.org/3/library/inspect.html#classes-and-functions)
    * [The interpreter stack](https://docs.python.org/3/library/inspect.html#the-interpreter-stack)
    * [Fetching attributes statically](https://docs.python.org/3/library/inspect.html#fetching-attributes-statically)
    * [Current State of Generators, Coroutines, and Asynchronous Generators](https://docs.python.org/3/library/inspect.html#current-state-of-generators-coroutines-and-asynchronous-generators)
    * [Code Objects Bit Flags](https://docs.python.org/3/library/inspect.html#code-objects-bit-flags)
    * [Buffer flags](https://docs.python.org/3/library/inspect.html#buffer-flags)
    * [Command-line interface](https://docs.python.org/3/library/inspect.html#command-line-interface)


#### Previous topic
[`gc` — Garbage Collector interface](https://docs.python.org/3/library/gc.html "previous chapter")
#### Next topic
[`annotationlib` — Functionality for introspecting annotations](https://docs.python.org/3/library/annotationlib.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=inspect+%E2%80%94+Inspect+live+objects&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Finspect.html&pagesource=library%2Finspect.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/annotationlib.html "annotationlib — Functionality for introspecting annotations") |
  * [previous](https://docs.python.org/3/library/gc.html "gc — Garbage Collector interface") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Python Runtime Services](https://docs.python.org/3/library/python.html) »
  * [`inspect` — Inspect live objects](https://docs.python.org/3/library/inspect.html)
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
