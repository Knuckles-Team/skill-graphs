## Exception context[¶](https://docs.python.org/3/library/exceptions.html#exception-context "Link to this heading")
Three attributes on exception objects provide information about the context in which the exception was raised:

BaseException.__context__[¶](https://docs.python.org/3/library/exceptions.html#BaseException.__context__ "Link to this definition")


BaseException.__cause__[¶](https://docs.python.org/3/library/exceptions.html#BaseException.__cause__ "Link to this definition")


BaseException.__suppress_context__[¶](https://docs.python.org/3/library/exceptions.html#BaseException.__suppress_context__ "Link to this definition")

When raising a new exception while another exception is already being handled, the new exception’s `__context__` attribute is automatically set to the handled exception. An exception may be handled when an [`except`](https://docs.python.org/3/reference/compound_stmts.html#except) or [`finally`](https://docs.python.org/3/reference/compound_stmts.html#finally) clause, or a [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) statement, is used.
This implicit exception context can be supplemented with an explicit cause by using `from` with [`raise`](https://docs.python.org/3/reference/simple_stmts.html#raise):
Copy```
raise new_exc from original_exc

```

The expression following [`from`](https://docs.python.org/3/reference/simple_stmts.html#raise) must be an exception or `None`. It will be set as `__cause__` on the raised exception. Setting `__cause__` also implicitly sets the `__suppress_context__` attribute to `True`, so that using `raise new_exc from None` effectively replaces the old exception with the new one for display purposes (e.g. converting [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError "KeyError") to [`AttributeError`](https://docs.python.org/3/library/exceptions.html#AttributeError "AttributeError")), while leaving the old exception available in `__context__` for introspection when debugging.
The default traceback display code shows these chained exceptions in addition to the traceback for the exception itself. An explicitly chained exception in `__cause__` is always shown when present. An implicitly chained exception in `__context__` is shown only if `__cause__` is [`None`](https://docs.python.org/3/library/constants.html#None "None") and `__suppress_context__` is false.
In either case, the exception itself is always shown after any chained exceptions so that the final line of the traceback always shows the last exception that was raised.
## Inheriting from built-in exceptions[¶](https://docs.python.org/3/library/exceptions.html#inheriting-from-built-in-exceptions "Link to this heading")
User code can create subclasses that inherit from an exception type. It’s recommended to only subclass one exception type at a time to avoid any possible conflicts between how the bases handle the `args` attribute, as well as due to possible memory layout incompatibilities.
**CPython implementation detail:** Most built-in exceptions are implemented in C for efficiency, see:
## Base classes[¶](https://docs.python.org/3/library/exceptions.html#base-classes "Link to this heading")
The following exceptions are used mostly as base classes for other exceptions.

_exception_ BaseException[¶](https://docs.python.org/3/library/exceptions.html#BaseException "Link to this definition")

The base class for all built-in exceptions. It is not meant to be directly inherited by user-defined classes (for that, use [`Exception`](https://docs.python.org/3/library/exceptions.html#Exception "Exception")). If [`str()`](https://docs.python.org/3/library/stdtypes.html#str "str") is called on an instance of this class, the representation of the argument(s) to the instance are returned, or the empty string when there were no arguments.

args[¶](https://docs.python.org/3/library/exceptions.html#BaseException.args "Link to this definition")

The tuple of arguments given to the exception constructor. Some built-in exceptions (like [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError")) expect a certain number of arguments and assign a special meaning to the elements of this tuple, while others are usually called only with a single string giving an error message.

with_traceback(_tb_)[¶](https://docs.python.org/3/library/exceptions.html#BaseException.with_traceback "Link to this definition")

This method sets _tb_ as the new traceback for the exception and returns the exception object. It was more commonly used before the exception chaining features of [**PEP 3134**](https://peps.python.org/pep-3134/) became available. The following example shows how we can convert an instance of `SomeException` into an instance of `OtherException` while preserving the traceback. Once raised, the current frame is pushed onto the traceback of the `OtherException`, as would have happened to the traceback of the original `SomeException` had we allowed it to propagate to the caller.
Copy```
try:
    ...
except SomeException:
    tb = sys.exception().__traceback__
    raise OtherException(...).with_traceback(tb)

```


__traceback__[¶](https://docs.python.org/3/library/exceptions.html#BaseException.__traceback__ "Link to this definition")

A writable field that holds the [traceback object](https://docs.python.org/3/reference/datamodel.html#traceback-objects) associated with this exception. See also: [The raise statement](https://docs.python.org/3/reference/simple_stmts.html#raise).

add_note(_note_)[¶](https://docs.python.org/3/library/exceptions.html#BaseException.add_note "Link to this definition")

Add the string `note` to the exception’s notes which appear in the standard traceback after the exception string. A [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") is raised if `note` is not a string.
Added in version 3.11.

__notes__[¶](https://docs.python.org/3/library/exceptions.html#BaseException.__notes__ "Link to this definition")

A list of the notes of this exception, which were added with [`add_note()`](https://docs.python.org/3/library/exceptions.html#BaseException.add_note "BaseException.add_note"). This attribute is created when `add_note()` is called.
Added in version 3.11.

_exception_ Exception[¶](https://docs.python.org/3/library/exceptions.html#Exception "Link to this definition")

All built-in, non-system-exiting exceptions are derived from this class. All user-defined exceptions should also be derived from this class.

_exception_ ArithmeticError[¶](https://docs.python.org/3/library/exceptions.html#ArithmeticError "Link to this definition")

The base class for those built-in exceptions that are raised for various arithmetic errors: [`OverflowError`](https://docs.python.org/3/library/exceptions.html#OverflowError "OverflowError"), [`ZeroDivisionError`](https://docs.python.org/3/library/exceptions.html#ZeroDivisionError "ZeroDivisionError"), [`FloatingPointError`](https://docs.python.org/3/library/exceptions.html#FloatingPointError "FloatingPointError").

_exception_ BufferError[¶](https://docs.python.org/3/library/exceptions.html#BufferError "Link to this definition")

Raised when a [buffer](https://docs.python.org/3/c-api/buffer.html#bufferobjects) related operation cannot be performed.

_exception_ LookupError[¶](https://docs.python.org/3/library/exceptions.html#LookupError "Link to this definition")

The base class for the exceptions that are raised when a key or index used on a mapping or sequence is invalid: [`IndexError`](https://docs.python.org/3/library/exceptions.html#IndexError "IndexError"), [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError "KeyError"). This can be raised directly by [`codecs.lookup()`](https://docs.python.org/3/library/codecs.html#codecs.lookup "codecs.lookup").
