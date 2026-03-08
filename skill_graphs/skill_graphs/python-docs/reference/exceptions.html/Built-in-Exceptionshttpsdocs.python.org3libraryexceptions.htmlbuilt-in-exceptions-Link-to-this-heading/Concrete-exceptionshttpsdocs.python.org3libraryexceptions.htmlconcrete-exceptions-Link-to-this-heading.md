## Concrete exceptions[¶](https://docs.python.org/3/library/exceptions.html#concrete-exceptions "Link to this heading")
The following exceptions are the exceptions that are usually raised.

_exception_ AssertionError[¶](https://docs.python.org/3/library/exceptions.html#AssertionError "Link to this definition")

Raised when an [`assert`](https://docs.python.org/3/reference/simple_stmts.html#assert) statement fails.

_exception_ AttributeError[¶](https://docs.python.org/3/library/exceptions.html#AttributeError "Link to this definition")

Raised when an attribute reference (see [Attribute references](https://docs.python.org/3/reference/expressions.html#attribute-references)) or assignment fails. (When an object does not support attribute references or attribute assignments at all, [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") is raised.)
The optional _name_ and _obj_ keyword-only arguments set the corresponding attributes:

name[¶](https://docs.python.org/3/library/exceptions.html#AttributeError.name "Link to this definition")

The name of the attribute that was attempted to be accessed.

obj[¶](https://docs.python.org/3/library/exceptions.html#AttributeError.obj "Link to this definition")

The object that was accessed for the named attribute.
Changed in version 3.10: Added the [`name`](https://docs.python.org/3/library/exceptions.html#AttributeError.name "AttributeError.name") and [`obj`](https://docs.python.org/3/library/exceptions.html#AttributeError.obj "AttributeError.obj") attributes.

_exception_ EOFError[¶](https://docs.python.org/3/library/exceptions.html#EOFError "Link to this definition")

Raised when the [`input()`](https://docs.python.org/3/library/functions.html#input "input") function hits an end-of-file condition (EOF) without reading any data. (Note: the `io.IOBase.read()` and [`io.IOBase.readline()`](https://docs.python.org/3/library/io.html#io.IOBase.readline "io.IOBase.readline") methods return an empty string when they hit EOF.)

_exception_ FloatingPointError[¶](https://docs.python.org/3/library/exceptions.html#FloatingPointError "Link to this definition")

Not currently used.

_exception_ GeneratorExit[¶](https://docs.python.org/3/library/exceptions.html#GeneratorExit "Link to this definition")

Raised when a [generator](https://docs.python.org/3/glossary.html#term-generator) or [coroutine](https://docs.python.org/3/glossary.html#term-coroutine) is closed; see [`generator.close()`](https://docs.python.org/3/reference/expressions.html#generator.close "generator.close") and [`coroutine.close()`](https://docs.python.org/3/reference/datamodel.html#coroutine.close "coroutine.close"). It directly inherits from [`BaseException`](https://docs.python.org/3/library/exceptions.html#BaseException "BaseException") instead of [`Exception`](https://docs.python.org/3/library/exceptions.html#Exception "Exception") since it is technically not an error.

_exception_ ImportError[¶](https://docs.python.org/3/library/exceptions.html#ImportError "Link to this definition")

Raised when the [`import`](https://docs.python.org/3/reference/simple_stmts.html#import) statement has troubles trying to load a module. Also raised when the “from list” in `from ... import` has a name that cannot be found.
The optional _name_ and _path_ keyword-only arguments set the corresponding attributes:

name[¶](https://docs.python.org/3/library/exceptions.html#ImportError.name "Link to this definition")

The name of the module that was attempted to be imported.

path[¶](https://docs.python.org/3/library/exceptions.html#ImportError.path "Link to this definition")

The path to any file which triggered the exception.
Changed in version 3.3: Added the [`name`](https://docs.python.org/3/library/exceptions.html#ImportError.name "ImportError.name") and [`path`](https://docs.python.org/3/library/exceptions.html#ImportError.path "ImportError.path") attributes.

_exception_ ModuleNotFoundError[¶](https://docs.python.org/3/library/exceptions.html#ModuleNotFoundError "Link to this definition")

A subclass of [`ImportError`](https://docs.python.org/3/library/exceptions.html#ImportError "ImportError") which is raised by [`import`](https://docs.python.org/3/reference/simple_stmts.html#import) when a module could not be located. It is also raised when `None` is found in [`sys.modules`](https://docs.python.org/3/library/sys.html#sys.modules "sys.modules").
Added in version 3.6.

_exception_ IndexError[¶](https://docs.python.org/3/library/exceptions.html#IndexError "Link to this definition")

Raised when a sequence subscript is out of range. (Slice indices are silently truncated to fall in the allowed range; if an index is not an integer, [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") is raised.)

_exception_ KeyError[¶](https://docs.python.org/3/library/exceptions.html#KeyError "Link to this definition")

Raised when a mapping (dictionary) key is not found in the set of existing keys.

_exception_ KeyboardInterrupt[¶](https://docs.python.org/3/library/exceptions.html#KeyboardInterrupt "Link to this definition")

Raised when the user hits the interrupt key (normally `Control`-`C` or `Delete`). During execution, a check for interrupts is made regularly. The exception inherits from [`BaseException`](https://docs.python.org/3/library/exceptions.html#BaseException "BaseException") so as to not be accidentally caught by code that catches [`Exception`](https://docs.python.org/3/library/exceptions.html#Exception "Exception") and thus prevent the interpreter from exiting.
Note
Catching a `KeyboardInterrupt` requires special consideration. Because it can be raised at unpredictable points, it may, in some circumstances, leave the running program in an inconsistent state. It is generally best to allow `KeyboardInterrupt` to end the program as quickly as possible or avoid raising it entirely. (See [Note on Signal Handlers and Exceptions](https://docs.python.org/3/library/signal.html#handlers-and-exceptions).)

_exception_ MemoryError[¶](https://docs.python.org/3/library/exceptions.html#MemoryError "Link to this definition")

Raised when an operation runs out of memory but the situation may still be rescued (by deleting some objects). The associated value is a string indicating what kind of (internal) operation ran out of memory. Note that because of the underlying memory management architecture (C’s `malloc()` function), the interpreter may not always be able to completely recover from this situation; it nevertheless raises an exception so that a stack traceback can be printed, in case a run-away program was the cause.

_exception_ NameError[¶](https://docs.python.org/3/library/exceptions.html#NameError "Link to this definition")

Raised when a local or global name is not found. This applies only to unqualified names. The associated value is an error message that includes the name that could not be found.
The optional _name_ keyword-only argument sets the attribute:

name[¶](https://docs.python.org/3/library/exceptions.html#NameError.name "Link to this definition")

The name of the variable that was attempted to be accessed.
Changed in version 3.10: Added the [`name`](https://docs.python.org/3/library/exceptions.html#NameError.name "NameError.name") attribute.

_exception_ NotImplementedError[¶](https://docs.python.org/3/library/exceptions.html#NotImplementedError "Link to this definition")

This exception is derived from [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError"). In user defined base classes, abstract methods should raise this exception when they require derived classes to override the method, or while the class is being developed to indicate that the real implementation still needs to be added.
Note
It should not be used to indicate that an operator or method is not meant to be supported at all – in that case either leave the operator / method undefined or, if a subclass, set it to [`None`](https://docs.python.org/3/library/constants.html#None "None").
Caution
`NotImplementedError` and `NotImplemented` are not interchangeable. This exception should only be used as described above; see [`NotImplemented`](https://docs.python.org/3/library/constants.html#NotImplemented "NotImplemented") for details on correct usage of the built-in constant.

_exception_ OSError([_arg_])[¶](https://docs.python.org/3/library/exceptions.html#OSError "Link to this definition")


_exception_ OSError(_errno_ , _strerror_[, _filename_[, _winerror_[, _filename2_]]])

This exception is raised when a system function returns a system-related error, including I/O failures such as “file not found” or “disk full” (not for illegal argument types or other incidental errors).
The second form of the constructor sets the corresponding attributes, described below. The attributes default to [`None`](https://docs.python.org/3/library/constants.html#None "None") if not specified. For backwards compatibility, if three arguments are passed, the [`args`](https://docs.python.org/3/library/exceptions.html#BaseException.args "BaseException.args") attribute contains only a 2-tuple of the first two constructor arguments.
The constructor often actually returns a subclass of `OSError`, as described in [OS exceptions](https://docs.python.org/3/library/exceptions.html#os-exceptions) below. The particular subclass depends on the final [`errno`](https://docs.python.org/3/library/exceptions.html#OSError.errno "OSError.errno") value. This behaviour only occurs when constructing `OSError` directly or via an alias, and is not inherited when subclassing.

errno[¶](https://docs.python.org/3/library/exceptions.html#OSError.errno "Link to this definition")

A numeric error code from the C variable `errno`.

winerror[¶](https://docs.python.org/3/library/exceptions.html#OSError.winerror "Link to this definition")

Under Windows, this gives you the native Windows error code. The [`errno`](https://docs.python.org/3/library/exceptions.html#OSError.errno "OSError.errno") attribute is then an approximate translation, in POSIX terms, of that native error code.
Under Windows, if the _winerror_ constructor argument is an integer, the [`errno`](https://docs.python.org/3/library/exceptions.html#OSError.errno "OSError.errno") attribute is determined from the Windows error code, and the _errno_ argument is ignored. On other platforms, the _winerror_ argument is ignored, and the [`winerror`](https://docs.python.org/3/library/exceptions.html#OSError.winerror "OSError.winerror") attribute does not exist.

strerror[¶](https://docs.python.org/3/library/exceptions.html#OSError.strerror "Link to this definition")

The corresponding error message, as provided by the operating system. It is formatted by the C functions `perror()` under POSIX, and `FormatMessage()` under Windows.

filename[¶](https://docs.python.org/3/library/exceptions.html#OSError.filename "Link to this definition")


filename2[¶](https://docs.python.org/3/library/exceptions.html#OSError.filename2 "Link to this definition")

For exceptions that involve a file system path (such as [`open()`](https://docs.python.org/3/library/functions.html#open "open") or [`os.unlink()`](https://docs.python.org/3/library/os.html#os.unlink "os.unlink")), [`filename`](https://docs.python.org/3/library/exceptions.html#OSError.filename "OSError.filename") is the file name passed to the function. For functions that involve two file system paths (such as [`os.rename()`](https://docs.python.org/3/library/os.html#os.rename "os.rename")), [`filename2`](https://docs.python.org/3/library/exceptions.html#OSError.filename2 "OSError.filename2") corresponds to the second file name passed to the function.
Changed in version 3.3: [`EnvironmentError`](https://docs.python.org/3/library/exceptions.html#EnvironmentError "EnvironmentError"), [`IOError`](https://docs.python.org/3/library/exceptions.html#IOError "IOError"), [`WindowsError`](https://docs.python.org/3/library/exceptions.html#WindowsError "WindowsError"), [`socket.error`](https://docs.python.org/3/library/socket.html#socket.error "socket.error"), [`select.error`](https://docs.python.org/3/library/select.html#select.error "select.error") and `mmap.error` have been merged into `OSError`, and the constructor may return a subclass.
Changed in version 3.4: The [`filename`](https://docs.python.org/3/library/exceptions.html#OSError.filename "OSError.filename") attribute is now the original file name passed to the function, instead of the name encoded to or decoded from the [filesystem encoding and error handler](https://docs.python.org/3/glossary.html#term-filesystem-encoding-and-error-handler). Also, the _filename2_ constructor argument and attribute was added.

_exception_ OverflowError[¶](https://docs.python.org/3/library/exceptions.html#OverflowError "Link to this definition")

Raised when the result of an arithmetic operation is too large to be represented. This cannot occur for integers (which would rather raise [`MemoryError`](https://docs.python.org/3/library/exceptions.html#MemoryError "MemoryError") than give up). However, for historical reasons, OverflowError is sometimes raised for integers that are outside a required range. Because of the lack of standardization of floating-point exception handling in C, most floating-point operations are not checked.

_exception_ PythonFinalizationError[¶](https://docs.python.org/3/library/exceptions.html#PythonFinalizationError "Link to this definition")

This exception is derived from [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError"). It is raised when an operation is blocked during interpreter shutdown also known as [Python finalization](https://docs.python.org/3/glossary.html#term-interpreter-shutdown).
Examples of operations which can be blocked with a `PythonFinalizationError` during the Python finalization:
  * Creating a new Python thread.
  * [`Joining`](https://docs.python.org/3/library/threading.html#threading.Thread.join "threading.Thread.join") a running daemon thread.
  * [`os.fork()`](https://docs.python.org/3/library/os.html#os.fork "os.fork").


See also the [`sys.is_finalizing()`](https://docs.python.org/3/library/sys.html#sys.is_finalizing "sys.is_finalizing") function.
Added in version 3.13: Previously, a plain [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError") was raised.
Changed in version 3.14: [`threading.Thread.join()`](https://docs.python.org/3/library/threading.html#threading.Thread.join "threading.Thread.join") can now raise this exception.

_exception_ RecursionError[¶](https://docs.python.org/3/library/exceptions.html#RecursionError "Link to this definition")

This exception is derived from [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError"). It is raised when the interpreter detects that the maximum recursion depth (see [`sys.getrecursionlimit()`](https://docs.python.org/3/library/sys.html#sys.getrecursionlimit "sys.getrecursionlimit")) is exceeded.
Added in version 3.5: Previously, a plain [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError") was raised.

_exception_ ReferenceError[¶](https://docs.python.org/3/library/exceptions.html#ReferenceError "Link to this definition")

This exception is raised when a weak reference proxy, created by the [`weakref.proxy()`](https://docs.python.org/3/library/weakref.html#weakref.proxy "weakref.proxy") function, is used to access an attribute of the referent after it has been garbage collected. For more information on weak references, see the [`weakref`](https://docs.python.org/3/library/weakref.html#module-weakref "weakref: Support for weak references and weak dictionaries.") module.

_exception_ RuntimeError[¶](https://docs.python.org/3/library/exceptions.html#RuntimeError "Link to this definition")

Raised when an error is detected that doesn’t fall in any of the other categories. The associated value is a string indicating what precisely went wrong.

_exception_ StopIteration[¶](https://docs.python.org/3/library/exceptions.html#StopIteration "Link to this definition")

Raised by built-in function [`next()`](https://docs.python.org/3/library/functions.html#next "next") and an [iterator](https://docs.python.org/3/glossary.html#term-iterator)'s [`__next__()`](https://docs.python.org/3/library/stdtypes.html#iterator.__next__ "iterator.__next__") method to signal that there are no further items produced by the iterator.

value[¶](https://docs.python.org/3/library/exceptions.html#StopIteration.value "Link to this definition")

The exception object has a single attribute `value`, which is given as an argument when constructing the exception, and defaults to [`None`](https://docs.python.org/3/library/constants.html#None "None").
When a [generator](https://docs.python.org/3/glossary.html#term-generator) or [coroutine](https://docs.python.org/3/glossary.html#term-coroutine) function returns, a new `StopIteration` instance is raised, and the value returned by the function is used as the [`value`](https://docs.python.org/3/library/exceptions.html#StopIteration.value "StopIteration.value") parameter to the constructor of the exception.
If a generator code directly or indirectly raises `StopIteration`, it is converted into a [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError") (retaining the `StopIteration` as the new exception’s cause).
Changed in version 3.3: Added `value` attribute and the ability for generator functions to use it to return a value.
Changed in version 3.5: Introduced the RuntimeError transformation via `from __future__ import generator_stop`, see [**PEP 479**](https://peps.python.org/pep-0479/).
Changed in version 3.7: Enable [**PEP 479**](https://peps.python.org/pep-0479/) for all code by default: a `StopIteration` error raised in a generator is transformed into a [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError").

_exception_ StopAsyncIteration[¶](https://docs.python.org/3/library/exceptions.html#StopAsyncIteration "Link to this definition")

Must be raised by [`__anext__()`](https://docs.python.org/3/reference/datamodel.html#object.__anext__ "object.__anext__") method of an [asynchronous iterator](https://docs.python.org/3/glossary.html#term-asynchronous-iterator) object to stop the iteration.
Added in version 3.5.

_exception_ SyntaxError(_message_ , _details_)[¶](https://docs.python.org/3/library/exceptions.html#SyntaxError "Link to this definition")

Raised when the parser encounters a syntax error. This may occur in an [`import`](https://docs.python.org/3/reference/simple_stmts.html#import) statement, in a call to the built-in functions [`compile()`](https://docs.python.org/3/library/functions.html#compile "compile"), [`exec()`](https://docs.python.org/3/library/functions.html#exec "exec"), or [`eval()`](https://docs.python.org/3/library/functions.html#eval "eval"), or when reading the initial script or standard input (also interactively).
The [`str()`](https://docs.python.org/3/library/stdtypes.html#str "str") of the exception instance returns only the error message. Details is a tuple whose members are also available as separate attributes.

filename[¶](https://docs.python.org/3/library/exceptions.html#SyntaxError.filename "Link to this definition")

The name of the file the syntax error occurred in.

lineno[¶](https://docs.python.org/3/library/exceptions.html#SyntaxError.lineno "Link to this definition")

Which line number in the file the error occurred in. This is 1-indexed: the first line in the file has a `lineno` of 1.

offset[¶](https://docs.python.org/3/library/exceptions.html#SyntaxError.offset "Link to this definition")

The column in the line where the error occurred. This is 1-indexed: the first character in the line has an `offset` of 1.

text[¶](https://docs.python.org/3/library/exceptions.html#SyntaxError.text "Link to this definition")

The source code text involved in the error.

end_lineno[¶](https://docs.python.org/3/library/exceptions.html#SyntaxError.end_lineno "Link to this definition")

Which line number in the file the error occurred ends in. This is 1-indexed: the first line in the file has a `lineno` of 1.

end_offset[¶](https://docs.python.org/3/library/exceptions.html#SyntaxError.end_offset "Link to this definition")

The column in the end line where the error occurred finishes. This is 1-indexed: the first character in the line has an `offset` of 1.
For errors in f-string fields, the message is prefixed by “f-string: ” and the offsets are offsets in a text constructed from the replacement expression. For example, compiling f’Bad {a b} field’ results in this args attribute: (‘f-string: …’, (‘’, 1, 2, ‘(a b)n’, 1, 5)).
Changed in version 3.10: Added the [`end_lineno`](https://docs.python.org/3/library/exceptions.html#SyntaxError.end_lineno "SyntaxError.end_lineno") and [`end_offset`](https://docs.python.org/3/library/exceptions.html#SyntaxError.end_offset "SyntaxError.end_offset") attributes.

_exception_ IndentationError[¶](https://docs.python.org/3/library/exceptions.html#IndentationError "Link to this definition")

Base class for syntax errors related to incorrect indentation. This is a subclass of [`SyntaxError`](https://docs.python.org/3/library/exceptions.html#SyntaxError "SyntaxError").

_exception_ TabError[¶](https://docs.python.org/3/library/exceptions.html#TabError "Link to this definition")

Raised when indentation contains an inconsistent use of tabs and spaces. This is a subclass of [`IndentationError`](https://docs.python.org/3/library/exceptions.html#IndentationError "IndentationError").

_exception_ SystemError[¶](https://docs.python.org/3/library/exceptions.html#SystemError "Link to this definition")

Raised when the interpreter finds an internal error, but the situation does not look so serious to cause it to abandon all hope. The associated value is a string indicating what went wrong (in low-level terms). In [CPython](https://docs.python.org/3/glossary.html#term-CPython), this could be raised by incorrectly using Python’s C API, such as returning a `NULL` value without an exception set.
If you’re confident that this exception wasn’t your fault, or the fault of a package you’re using, you should report this to the author or maintainer of your Python interpreter. Be sure to report the version of the Python interpreter (`sys.version`; it is also printed at the start of an interactive Python session), the exact error message (the exception’s associated value) and if possible the source of the program that triggered the error.

_exception_ SystemExit[¶](https://docs.python.org/3/library/exceptions.html#SystemExit "Link to this definition")

This exception is raised by the [`sys.exit()`](https://docs.python.org/3/library/sys.html#sys.exit "sys.exit") function. It inherits from [`BaseException`](https://docs.python.org/3/library/exceptions.html#BaseException "BaseException") instead of [`Exception`](https://docs.python.org/3/library/exceptions.html#Exception "Exception") so that it is not accidentally caught by code that catches `Exception`. This allows the exception to properly propagate up and cause the interpreter to exit. When it is not handled, the Python interpreter exits; no stack traceback is printed. The constructor accepts the same optional argument passed to `sys.exit()`. If the value is an integer, it specifies the system exit status (passed to C’s `exit()` function); if it is `None`, the exit status is zero; if it has another type (such as a string), the object’s value is printed and the exit status is one.
A call to [`sys.exit()`](https://docs.python.org/3/library/sys.html#sys.exit "sys.exit") is translated into an exception so that clean-up handlers ([`finally`](https://docs.python.org/3/reference/compound_stmts.html#finally) clauses of [`try`](https://docs.python.org/3/reference/compound_stmts.html#try) statements) can be executed, and so that a debugger can execute a script without running the risk of losing control. The [`os._exit()`](https://docs.python.org/3/library/os.html#os._exit "os._exit") function can be used if it is absolutely positively necessary to exit immediately (for example, in the child process after a call to [`os.fork()`](https://docs.python.org/3/library/os.html#os.fork "os.fork")).

code[¶](https://docs.python.org/3/library/exceptions.html#SystemExit.code "Link to this definition")

The exit status or error message that is passed to the constructor. (Defaults to `None`.)

_exception_ TypeError[¶](https://docs.python.org/3/library/exceptions.html#TypeError "Link to this definition")

Raised when an operation or function is applied to an object of inappropriate type. The associated value is a string giving details about the type mismatch.
This exception may be raised by user code to indicate that an attempted operation on an object is not supported, and is not meant to be. If an object is meant to support a given operation but has not yet provided an implementation, [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "NotImplementedError") is the proper exception to raise.
Passing arguments of the wrong type (e.g. passing a [`list`](https://docs.python.org/3/library/stdtypes.html#list "list") when an [`int`](https://docs.python.org/3/library/functions.html#int "int") is expected) should result in a `TypeError`, but passing arguments with the wrong value (e.g. a number outside expected boundaries) should result in a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError").

_exception_ UnboundLocalError[¶](https://docs.python.org/3/library/exceptions.html#UnboundLocalError "Link to this definition")

Raised when a reference is made to a local variable in a function or method, but no value has been bound to that variable. This is a subclass of [`NameError`](https://docs.python.org/3/library/exceptions.html#NameError "NameError").

_exception_ UnicodeError[¶](https://docs.python.org/3/library/exceptions.html#UnicodeError "Link to this definition")

Raised when a Unicode-related encoding or decoding error occurs. It is a subclass of [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError").
`UnicodeError` has attributes that describe the encoding or decoding error. For example, `err.object[err.start:err.end]` gives the particular invalid input that the codec failed on.

encoding[¶](https://docs.python.org/3/library/exceptions.html#UnicodeError.encoding "Link to this definition")

The name of the encoding that raised the error.

reason[¶](https://docs.python.org/3/library/exceptions.html#UnicodeError.reason "Link to this definition")

A string describing the specific codec error.

object[¶](https://docs.python.org/3/library/exceptions.html#UnicodeError.object "Link to this definition")

The object the codec was attempting to encode or decode.

start[¶](https://docs.python.org/3/library/exceptions.html#UnicodeError.start "Link to this definition")

The first index of invalid data in [`object`](https://docs.python.org/3/library/functions.html#object "object").
This value should not be negative as it is interpreted as an absolute offset but this constraint is not enforced at runtime.

end[¶](https://docs.python.org/3/library/exceptions.html#UnicodeError.end "Link to this definition")

The index after the last invalid data in [`object`](https://docs.python.org/3/library/functions.html#object "object").
This value should not be negative as it is interpreted as an absolute offset but this constraint is not enforced at runtime.

_exception_ UnicodeEncodeError[¶](https://docs.python.org/3/library/exceptions.html#UnicodeEncodeError "Link to this definition")

Raised when a Unicode-related error occurs during encoding. It is a subclass of [`UnicodeError`](https://docs.python.org/3/library/exceptions.html#UnicodeError "UnicodeError").

_exception_ UnicodeDecodeError[¶](https://docs.python.org/3/library/exceptions.html#UnicodeDecodeError "Link to this definition")

Raised when a Unicode-related error occurs during decoding. It is a subclass of [`UnicodeError`](https://docs.python.org/3/library/exceptions.html#UnicodeError "UnicodeError").

_exception_ UnicodeTranslateError[¶](https://docs.python.org/3/library/exceptions.html#UnicodeTranslateError "Link to this definition")

Raised when a Unicode-related error occurs during translating. It is a subclass of [`UnicodeError`](https://docs.python.org/3/library/exceptions.html#UnicodeError "UnicodeError").

_exception_ ValueError[¶](https://docs.python.org/3/library/exceptions.html#ValueError "Link to this definition")

Raised when an operation or function receives an argument that has the right type but an inappropriate value, and the situation is not described by a more precise exception such as [`IndexError`](https://docs.python.org/3/library/exceptions.html#IndexError "IndexError").

_exception_ ZeroDivisionError[¶](https://docs.python.org/3/library/exceptions.html#ZeroDivisionError "Link to this definition")

Raised when the second argument of a division or modulo operation is zero. The associated value is a string indicating the type of the operands and the operation.
The following exceptions are kept for compatibility with previous versions; starting from Python 3.3, they are aliases of [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError").

_exception_ EnvironmentError[¶](https://docs.python.org/3/library/exceptions.html#EnvironmentError "Link to this definition")


_exception_ IOError[¶](https://docs.python.org/3/library/exceptions.html#IOError "Link to this definition")


_exception_ WindowsError[¶](https://docs.python.org/3/library/exceptions.html#WindowsError "Link to this definition")

Only available on Windows.
### OS exceptions[¶](https://docs.python.org/3/library/exceptions.html#os-exceptions "Link to this heading")
The following exceptions are subclasses of [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError"), they get raised depending on the system error code.

_exception_ BlockingIOError[¶](https://docs.python.org/3/library/exceptions.html#BlockingIOError "Link to this definition")

Raised when an operation would block on an object (e.g. socket) set for non-blocking operation. Corresponds to `errno` [`EAGAIN`](https://docs.python.org/3/library/errno.html#errno.EAGAIN "errno.EAGAIN"), [`EALREADY`](https://docs.python.org/3/library/errno.html#errno.EALREADY "errno.EALREADY"), [`EWOULDBLOCK`](https://docs.python.org/3/library/errno.html#errno.EWOULDBLOCK "errno.EWOULDBLOCK") and [`EINPROGRESS`](https://docs.python.org/3/library/errno.html#errno.EINPROGRESS "errno.EINPROGRESS").
In addition to those of [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError"), `BlockingIOError` can have one more attribute:

characters_written[¶](https://docs.python.org/3/library/exceptions.html#BlockingIOError.characters_written "Link to this definition")

An integer containing the number of **bytes** written to the stream before it blocked. This attribute is available when using the buffered I/O classes from the [`io`](https://docs.python.org/3/library/io.html#module-io "io: Core tools for working with streams.") module.

_exception_ ChildProcessError[¶](https://docs.python.org/3/library/exceptions.html#ChildProcessError "Link to this definition")

Raised when an operation on a child process failed. Corresponds to `errno` [`ECHILD`](https://docs.python.org/3/library/errno.html#errno.ECHILD "errno.ECHILD").

_exception_ ConnectionError[¶](https://docs.python.org/3/library/exceptions.html#ConnectionError "Link to this definition")

A base class for connection-related issues.
Subclasses are [`BrokenPipeError`](https://docs.python.org/3/library/exceptions.html#BrokenPipeError "BrokenPipeError"), [`ConnectionAbortedError`](https://docs.python.org/3/library/exceptions.html#ConnectionAbortedError "ConnectionAbortedError"), [`ConnectionRefusedError`](https://docs.python.org/3/library/exceptions.html#ConnectionRefusedError "ConnectionRefusedError") and [`ConnectionResetError`](https://docs.python.org/3/library/exceptions.html#ConnectionResetError "ConnectionResetError").

_exception_ BrokenPipeError[¶](https://docs.python.org/3/library/exceptions.html#BrokenPipeError "Link to this definition")

A subclass of [`ConnectionError`](https://docs.python.org/3/library/exceptions.html#ConnectionError "ConnectionError"), raised when trying to write on a pipe while the other end has been closed, or trying to write on a socket which has been shutdown for writing. Corresponds to `errno` [`EPIPE`](https://docs.python.org/3/library/errno.html#errno.EPIPE "errno.EPIPE") and [`ESHUTDOWN`](https://docs.python.org/3/library/errno.html#errno.ESHUTDOWN "errno.ESHUTDOWN").

_exception_ ConnectionAbortedError[¶](https://docs.python.org/3/library/exceptions.html#ConnectionAbortedError "Link to this definition")

A subclass of [`ConnectionError`](https://docs.python.org/3/library/exceptions.html#ConnectionError "ConnectionError"), raised when a connection attempt is aborted by the peer. Corresponds to `errno` [`ECONNABORTED`](https://docs.python.org/3/library/errno.html#errno.ECONNABORTED "errno.ECONNABORTED").

_exception_ ConnectionRefusedError[¶](https://docs.python.org/3/library/exceptions.html#ConnectionRefusedError "Link to this definition")

A subclass of [`ConnectionError`](https://docs.python.org/3/library/exceptions.html#ConnectionError "ConnectionError"), raised when a connection attempt is refused by the peer. Corresponds to `errno` [`ECONNREFUSED`](https://docs.python.org/3/library/errno.html#errno.ECONNREFUSED "errno.ECONNREFUSED").

_exception_ ConnectionResetError[¶](https://docs.python.org/3/library/exceptions.html#ConnectionResetError "Link to this definition")

A subclass of [`ConnectionError`](https://docs.python.org/3/library/exceptions.html#ConnectionError "ConnectionError"), raised when a connection is reset by the peer. Corresponds to `errno` [`ECONNRESET`](https://docs.python.org/3/library/errno.html#errno.ECONNRESET "errno.ECONNRESET").

_exception_ FileExistsError[¶](https://docs.python.org/3/library/exceptions.html#FileExistsError "Link to this definition")

Raised when trying to create a file or directory which already exists. Corresponds to `errno` [`EEXIST`](https://docs.python.org/3/library/errno.html#errno.EEXIST "errno.EEXIST").

_exception_ FileNotFoundError[¶](https://docs.python.org/3/library/exceptions.html#FileNotFoundError "Link to this definition")

Raised when a file or directory is requested but doesn’t exist. Corresponds to `errno` [`ENOENT`](https://docs.python.org/3/library/errno.html#errno.ENOENT "errno.ENOENT").

_exception_ InterruptedError[¶](https://docs.python.org/3/library/exceptions.html#InterruptedError "Link to this definition")

Raised when a system call is interrupted by an incoming signal. Corresponds to `errno` [`EINTR`](https://docs.python.org/3/library/errno.html#errno.EINTR "errno.EINTR").
Changed in version 3.5: Python now retries system calls when a syscall is interrupted by a signal, except if the signal handler raises an exception (see [**PEP 475**](https://peps.python.org/pep-0475/) for the rationale), instead of raising `InterruptedError`.

_exception_ IsADirectoryError[¶](https://docs.python.org/3/library/exceptions.html#IsADirectoryError "Link to this definition")

Raised when a file operation (such as [`os.remove()`](https://docs.python.org/3/library/os.html#os.remove "os.remove")) is requested on a directory. Corresponds to `errno` [`EISDIR`](https://docs.python.org/3/library/errno.html#errno.EISDIR "errno.EISDIR").

_exception_ NotADirectoryError[¶](https://docs.python.org/3/library/exceptions.html#NotADirectoryError "Link to this definition")

Raised when a directory operation (such as [`os.listdir()`](https://docs.python.org/3/library/os.html#os.listdir "os.listdir")) is requested on something which is not a directory. On most POSIX platforms, it may also be raised if an operation attempts to open or traverse a non-directory file as if it were a directory. Corresponds to `errno` [`ENOTDIR`](https://docs.python.org/3/library/errno.html#errno.ENOTDIR "errno.ENOTDIR").

_exception_ PermissionError[¶](https://docs.python.org/3/library/exceptions.html#PermissionError "Link to this definition")

Raised when trying to run an operation without the adequate access rights - for example filesystem permissions. Corresponds to `errno` [`EACCES`](https://docs.python.org/3/library/errno.html#errno.EACCES "errno.EACCES"), [`EPERM`](https://docs.python.org/3/library/errno.html#errno.EPERM "errno.EPERM"), and [`ENOTCAPABLE`](https://docs.python.org/3/library/errno.html#errno.ENOTCAPABLE "errno.ENOTCAPABLE").
Changed in version 3.11.1: WASI’s [`ENOTCAPABLE`](https://docs.python.org/3/library/errno.html#errno.ENOTCAPABLE "errno.ENOTCAPABLE") is now mapped to `PermissionError`.

_exception_ ProcessLookupError[¶](https://docs.python.org/3/library/exceptions.html#ProcessLookupError "Link to this definition")

Raised when a given process doesn’t exist. Corresponds to `errno` [`ESRCH`](https://docs.python.org/3/library/errno.html#errno.ESRCH "errno.ESRCH").

_exception_ TimeoutError[¶](https://docs.python.org/3/library/exceptions.html#TimeoutError "Link to this definition")

Raised when a system function timed out at the system level. Corresponds to `errno` [`ETIMEDOUT`](https://docs.python.org/3/library/errno.html#errno.ETIMEDOUT "errno.ETIMEDOUT").
Added in version 3.3: All the above [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") subclasses were added.
See also
[**PEP 3151**](https://peps.python.org/pep-3151/) - Reworking the OS and IO exception hierarchy
