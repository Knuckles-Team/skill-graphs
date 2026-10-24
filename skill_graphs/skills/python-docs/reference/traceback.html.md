[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`traceback` — Print or retrieve a stack traceback](https://docs.python.org/3/library/traceback.html)
    * [Module-Level Functions](https://docs.python.org/3/library/traceback.html#module-level-functions)
    * [`TracebackException` Objects](https://docs.python.org/3/library/traceback.html#tracebackexception-objects)
    * [`StackSummary` Objects](https://docs.python.org/3/library/traceback.html#stacksummary-objects)
    * [`FrameSummary` Objects](https://docs.python.org/3/library/traceback.html#framesummary-objects)
    * [Examples of Using the Module-Level Functions](https://docs.python.org/3/library/traceback.html#examples-of-using-the-module-level-functions)
    * [Examples of Using `TracebackException`](https://docs.python.org/3/library/traceback.html#examples-of-using-tracebackexception)


#### Previous topic
[`atexit` — Exit handlers](https://docs.python.org/3/library/atexit.html "previous chapter")
#### Next topic
[`__future__` — Future statement definitions](https://docs.python.org/3/library/__future__.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=traceback+%E2%80%94+Print+or+retrieve+a+stack+traceback&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ftraceback.html&pagesource=library%2Ftraceback.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/__future__.html "__future__ — Future statement definitions") |
  * [previous](https://docs.python.org/3/library/atexit.html "atexit — Exit handlers") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Python Runtime Services](https://docs.python.org/3/library/python.html) »
  * [`traceback` — Print or retrieve a stack traceback](https://docs.python.org/3/library/traceback.html)
  * |
  * Theme  Auto Light Dark |


#  `traceback` — Print or retrieve a stack traceback[¶](https://docs.python.org/3/library/traceback.html#module-traceback "Link to this heading")
**Source code:**
* * *
This module provides a standard interface to extract, format and print stack traces of Python programs. It is more flexible than the interpreter’s default traceback display, and therefore makes it possible to configure certain aspects of the output. Finally, it contains a utility for capturing enough information about an exception to print it later, without the need to save a reference to the actual exception. Since exceptions can be the roots of large objects graph, this utility can significantly improve memory management.
The module uses [traceback objects](https://docs.python.org/3/reference/datamodel.html#traceback-objects) — these are objects of type [`types.TracebackType`](https://docs.python.org/3/library/types.html#types.TracebackType "types.TracebackType"), which are assigned to the [`__traceback__`](https://docs.python.org/3/library/exceptions.html#BaseException.__traceback__ "BaseException.__traceback__") field of [`BaseException`](https://docs.python.org/3/library/exceptions.html#BaseException "BaseException") instances.
See also

Module [`faulthandler`](https://docs.python.org/3/library/faulthandler.html#module-faulthandler "faulthandler: Dump the Python traceback.")

Used to dump Python tracebacks explicitly, on a fault, after a timeout, or on a user signal.

Module [`pdb`](https://docs.python.org/3/library/pdb.html#module-pdb "pdb: The Python debugger for interactive interpreters.")

Interactive source code debugger for Python programs.
The module’s API can be divided into two parts:
  * Module-level functions offering basic functionality, which are useful for interactive inspection of exceptions and tracebacks.
  * [`TracebackException`](https://docs.python.org/3/library/traceback.html#traceback.TracebackException "traceback.TracebackException") class and its helper classes [`StackSummary`](https://docs.python.org/3/library/traceback.html#traceback.StackSummary "traceback.StackSummary") and [`FrameSummary`](https://docs.python.org/3/library/traceback.html#traceback.FrameSummary "traceback.FrameSummary"). These offer both more flexibility in the output generated and the ability to store the information necessary for later formatting without holding references to actual exception and traceback objects.


Added in version 3.13: Output is colorized by default and can be [controlled using environment variables](https://docs.python.org/3/using/cmdline.html#using-on-controlling-color).
## Module-Level Functions[¶](https://docs.python.org/3/library/traceback.html#module-level-functions "Link to this heading")

traceback.print_tb(_tb_ , _limit =None_, _file =None_)[¶](https://docs.python.org/3/library/traceback.html#traceback.print_tb "Link to this definition")

Print up to _limit_ stack trace entries from [traceback object](https://docs.python.org/3/reference/datamodel.html#traceback-objects) _tb_ (starting from the caller’s frame) if _limit_ is positive. Otherwise, print the last `abs(limit)` entries. If _limit_ is omitted or `None`, all entries are printed. If _file_ is omitted or `None`, the output goes to [`sys.stderr`](https://docs.python.org/3/library/sys.html#sys.stderr "sys.stderr"); otherwise it should be an open [file](https://docs.python.org/3/glossary.html#term-file-object) or [file-like object](https://docs.python.org/3/glossary.html#term-file-like-object) to receive the output.
Note
The meaning of the _limit_ parameter is different than the meaning of [`sys.tracebacklimit`](https://docs.python.org/3/library/sys.html#sys.tracebacklimit "sys.tracebacklimit"). A negative _limit_ value corresponds to a positive value of `sys.tracebacklimit`, whereas the behaviour of a positive _limit_ value cannot be achieved with `sys.tracebacklimit`.
Changed in version 3.5: Added negative _limit_ support.

traceback.print_exception(_exc_ , _/_ , [_value_ , _tb_ , ]_limit=None_ , _file=None_ , _chain=True_)[¶](https://docs.python.org/3/library/traceback.html#traceback.print_exception "Link to this definition")

Print exception information and stack trace entries from [traceback object](https://docs.python.org/3/reference/datamodel.html#traceback-objects) _tb_ to _file_. This differs from [`print_tb()`](https://docs.python.org/3/library/traceback.html#traceback.print_tb "traceback.print_tb") in the following ways:
  * if _tb_ is not `None`, it prints a header `Traceback (most recent call last):`
  * it prints the exception type and _value_ after the stack trace


  * if _type(value)_ is [`SyntaxError`](https://docs.python.org/3/library/exceptions.html#SyntaxError "SyntaxError") and _value_ has the appropriate format, it prints the line where the syntax error occurred with a caret indicating the approximate position of the error.


Since Python 3.10, instead of passing _value_ and _tb_ , an exception object can be passed as the first argument. If _value_ and _tb_ are provided, the first argument is ignored in order to provide backwards compatibility.
The optional _limit_ argument has the same meaning as for [`print_tb()`](https://docs.python.org/3/library/traceback.html#traceback.print_tb "traceback.print_tb"). If _chain_ is true (the default), then chained exceptions (the [`__cause__`](https://docs.python.org/3/library/exceptions.html#BaseException.__cause__ "BaseException.__cause__") or [`__context__`](https://docs.python.org/3/library/exceptions.html#BaseException.__context__ "BaseException.__context__") attributes of the exception) will be printed as well, like the interpreter itself does when printing an unhandled exception.
Changed in version 3.5: The _etype_ argument is ignored and inferred from the type of _value_.
Changed in version 3.10: The _etype_ parameter has been renamed to _exc_ and is now positional-only.

traceback.print_exc(_limit =None_, _file =None_, _chain =True_)[¶](https://docs.python.org/3/library/traceback.html#traceback.print_exc "Link to this definition")

This is a shorthand for `print_exception(sys.exception(), limit=limit, file=file, chain=chain)`.

traceback.print_last(_limit =None_, _file =None_, _chain =True_)[¶](https://docs.python.org/3/library/traceback.html#traceback.print_last "Link to this definition")

This is a shorthand for `print_exception(sys.last_exc, limit=limit, file=file, chain=chain)`. In general it will work only after an exception has reached an interactive prompt (see [`sys.last_exc`](https://docs.python.org/3/library/sys.html#sys.last_exc "sys.last_exc")).

traceback.print_stack(_f =None_, _limit =None_, _file =None_)[¶](https://docs.python.org/3/library/traceback.html#traceback.print_stack "Link to this definition")

Print up to _limit_ stack trace entries (starting from the invocation point) if _limit_ is positive. Otherwise, print the last `abs(limit)` entries. If _limit_ is omitted or `None`, all entries are printed. The optional _f_ argument can be used to specify an alternate [stack frame](https://docs.python.org/3/reference/datamodel.html#frame-objects) to start. The optional _file_ argument has the same meaning as for [`print_tb()`](https://docs.python.org/3/library/traceback.html#traceback.print_tb "traceback.print_tb").
Changed in version 3.5: Added negative _limit_ support.

traceback.extract_tb(_tb_ , _limit =None_)[¶](https://docs.python.org/3/library/traceback.html#traceback.extract_tb "Link to this definition")

Return a [`StackSummary`](https://docs.python.org/3/library/traceback.html#traceback.StackSummary "traceback.StackSummary") object representing a list of “pre-processed” stack trace entries extracted from the [traceback object](https://docs.python.org/3/reference/datamodel.html#traceback-objects) _tb_. It is useful for alternate formatting of stack traces. The optional _limit_ argument has the same meaning as for [`print_tb()`](https://docs.python.org/3/library/traceback.html#traceback.print_tb "traceback.print_tb"). A “pre-processed” stack trace entry is a [`FrameSummary`](https://docs.python.org/3/library/traceback.html#traceback.FrameSummary "traceback.FrameSummary") object containing attributes [`filename`](https://docs.python.org/3/library/traceback.html#traceback.FrameSummary.filename "traceback.FrameSummary.filename"), [`lineno`](https://docs.python.org/3/library/traceback.html#traceback.FrameSummary.lineno "traceback.FrameSummary.lineno"), [`name`](https://docs.python.org/3/library/traceback.html#traceback.FrameSummary.name "traceback.FrameSummary.name"), and [`line`](https://docs.python.org/3/library/traceback.html#traceback.FrameSummary.line "traceback.FrameSummary.line") representing the information that is usually printed for a stack trace.

traceback.extract_stack(_f =None_, _limit =None_)[¶](https://docs.python.org/3/library/traceback.html#traceback.extract_stack "Link to this definition")

Extract the raw traceback from the current [stack frame](https://docs.python.org/3/reference/datamodel.html#frame-objects). The return value has the same format as for [`extract_tb()`](https://docs.python.org/3/library/traceback.html#traceback.extract_tb "traceback.extract_tb"). The optional _f_ and _limit_ arguments have the same meaning as for [`print_stack()`](https://docs.python.org/3/library/traceback.html#traceback.print_stack "traceback.print_stack").

traceback.print_list(_extracted_list_ , _file =None_)[¶](https://docs.python.org/3/library/traceback.html#traceback.print_list "Link to this definition")

Print the list of tuples as returned by [`extract_tb()`](https://docs.python.org/3/library/traceback.html#traceback.extract_tb "traceback.extract_tb") or [`extract_stack()`](https://docs.python.org/3/library/traceback.html#traceback.extract_stack "traceback.extract_stack") as a formatted stack trace to the given file. If _file_ is `None`, the output is written to [`sys.stderr`](https://docs.python.org/3/library/sys.html#sys.stderr "sys.stderr").

traceback.format_list(_extracted_list_)[¶](https://docs.python.org/3/library/traceback.html#traceback.format_list "Link to this definition")

Given a list of tuples or [`FrameSummary`](https://docs.python.org/3/library/traceback.html#traceback.FrameSummary "traceback.FrameSummary") objects as returned by [`extract_tb()`](https://docs.python.org/3/library/traceback.html#traceback.extract_tb "traceback.extract_tb") or [`extract_stack()`](https://docs.python.org/3/library/traceback.html#traceback.extract_stack "traceback.extract_stack"), return a list of strings ready for printing. Each string in the resulting list corresponds to the item with the same index in the argument list. Each string ends in a newline; the strings may contain internal newlines as well, for those items whose source text line is not `None`.

traceback.format_exception_only(_exc_ , _/_ , [_value_ , ]_*_ , _show_group=False_)[¶](https://docs.python.org/3/library/traceback.html#traceback.format_exception_only "Link to this definition")

Format the exception part of a traceback using an exception value such as given by [`sys.last_value`](https://docs.python.org/3/library/sys.html#sys.last_value "sys.last_value"). The return value is a list of strings, each ending in a newline. The list contains the exception’s message, which is normally a single string; however, for [`SyntaxError`](https://docs.python.org/3/library/exceptions.html#SyntaxError "SyntaxError") exceptions, it contains several lines that (when printed) display detailed information about where the syntax error occurred. Following the message, the list contains the exception’s [`notes`](https://docs.python.org/3/library/exceptions.html#BaseException.__notes__ "BaseException.__notes__").
Since Python 3.10, instead of passing _value_ , an exception object can be passed as the first argument. If _value_ is provided, the first argument is ignored in order to provide backwards compatibility.
When _show_group_ is `True`, and the exception is an instance of [`BaseExceptionGroup`](https://docs.python.org/3/library/exceptions.html#BaseExceptionGroup "BaseExceptionGroup"), the nested exceptions are included as well, recursively, with indentation relative to their nesting depth.
Changed in version 3.10: The _etype_ parameter has been renamed to _exc_ and is now positional-only.
Changed in version 3.11: The returned list now includes any [`notes`](https://docs.python.org/3/library/exceptions.html#BaseException.__notes__ "BaseException.__notes__") attached to the exception.
Changed in version 3.13: _show_group_ parameter was added.

traceback.format_exception(_exc_ , _/_ , [_value_ , _tb_ , ]_limit=None_ , _chain=True_)[¶](https://docs.python.org/3/library/traceback.html#traceback.format_exception "Link to this definition")

Format a stack trace and the exception information. The arguments have the same meaning as the corresponding arguments to [`print_exception()`](https://docs.python.org/3/library/traceback.html#traceback.print_exception "traceback.print_exception"). The return value is a list of strings, each ending in a newline and some containing internal newlines. When these lines are concatenated and printed, exactly the same text is printed as does `print_exception()`.
Changed in version 3.5: The _etype_ argument is ignored and inferred from the type of _value_.
Changed in version 3.10: This function’s behavior and signature were modified to match [`print_exception()`](https://docs.python.org/3/library/traceback.html#traceback.print_exception "traceback.print_exception").

traceback.format_exc(_limit =None_, _chain =True_)[¶](https://docs.python.org/3/library/traceback.html#traceback.format_exc "Link to this definition")

This is like `print_exc(limit)` but returns a string instead of printing to a file.

traceback.format_tb(_tb_ , _limit =None_)[¶](https://docs.python.org/3/library/traceback.html#traceback.format_tb "Link to this definition")

A shorthand for `format_list(extract_tb(tb, limit))`.

traceback.format_stack(_f =None_, _limit =None_)[¶](https://docs.python.org/3/library/traceback.html#traceback.format_stack "Link to this definition")

A shorthand for `format_list(extract_stack(f, limit))`.

traceback.clear_frames(_tb_)[¶](https://docs.python.org/3/library/traceback.html#traceback.clear_frames "Link to this definition")

Clears the local variables of all the stack frames in a [traceback](https://docs.python.org/3/reference/datamodel.html#traceback-objects) _tb_ by calling the [`clear()`](https://docs.python.org/3/reference/datamodel.html#frame.clear "frame.clear") method of each [frame object](https://docs.python.org/3/reference/datamodel.html#frame-objects).
Added in version 3.4.

traceback.walk_stack(_f_)[¶](https://docs.python.org/3/library/traceback.html#traceback.walk_stack "Link to this definition")

Walk a stack following [`f.f_back`](https://docs.python.org/3/reference/datamodel.html#frame.f_back "frame.f_back") from the given frame, yielding the frame and line number for each frame. If _f_ is `None`, the current stack is used. This helper is used with [`StackSummary.extract()`](https://docs.python.org/3/library/traceback.html#traceback.StackSummary.extract "traceback.StackSummary.extract").
Added in version 3.5.
Changed in version 3.14: This function previously returned a generator that would walk the stack when first iterated over. The generator returned now is the state of the stack when `walk_stack` is called.

traceback.walk_tb(_tb_)[¶](https://docs.python.org/3/library/traceback.html#traceback.walk_tb "Link to this definition")

Walk a traceback following [`tb_next`](https://docs.python.org/3/reference/datamodel.html#traceback.tb_next "traceback.tb_next") yielding the frame and line number for each frame. This helper is used with [`StackSummary.extract()`](https://docs.python.org/3/library/traceback.html#traceback.StackSummary.extract "traceback.StackSummary.extract").
Added in version 3.5.
##  `TracebackException` Objects[¶](https://docs.python.org/3/library/traceback.html#tracebackexception-objects "Link to this heading")
Added in version 3.5.
`TracebackException` objects are created from actual exceptions to capture data for later printing. They offer a more lightweight method of storing this information by avoiding holding references to [traceback](https://docs.python.org/3/reference/datamodel.html#traceback-objects) and [frame](https://docs.python.org/3/reference/datamodel.html#frame-objects) objects. In addition, they expose more options to configure the output compared to the module-level functions described above.

_class_ traceback.TracebackException(_exc_type_ , _exc_value_ , _exc_traceback_ , _*_ , _limit =None_, _lookup_lines =True_, _capture_locals =False_, _compact =False_, _max_group_width =15_, _max_group_depth =10_)[¶](https://docs.python.org/3/library/traceback.html#traceback.TracebackException "Link to this definition")

Capture an exception for later rendering. The meaning of _limit_ , _lookup_lines_ and _capture_locals_ are as for the [`StackSummary`](https://docs.python.org/3/library/traceback.html#traceback.StackSummary "traceback.StackSummary") class.
If _compact_ is true, only data that is required by `TracebackException`’s [`format()`](https://docs.python.org/3/library/functions.html#format "format") method is saved in the class attributes. In particular, the [`__context__`](https://docs.python.org/3/library/traceback.html#traceback.TracebackException.__context__ "traceback.TracebackException.__context__") field is calculated only if [`__cause__`](https://docs.python.org/3/library/traceback.html#traceback.TracebackException.__cause__ "traceback.TracebackException.__cause__") is `None` and [`__suppress_context__`](https://docs.python.org/3/library/traceback.html#traceback.TracebackException.__suppress_context__ "traceback.TracebackException.__suppress_context__") is false.
Note that when locals are captured, they are also shown in the traceback.
_max_group_width_ and _max_group_depth_ control the formatting of exception groups (see [`BaseExceptionGroup`](https://docs.python.org/3/library/exceptions.html#BaseExceptionGroup "BaseExceptionGroup")). The depth refers to the nesting level of the group, and the width refers to the size of a single exception group’s exceptions array. The formatted output is truncated when either limit is exceeded.
Changed in version 3.10: Added the _compact_ parameter.
Changed in version 3.11: Added the _max_group_width_ and _max_group_depth_ parameters.

__cause__[¶](https://docs.python.org/3/library/traceback.html#traceback.TracebackException.__cause__ "Link to this definition")

A `TracebackException` of the original [`__cause__`](https://docs.python.org/3/library/exceptions.html#BaseException.__cause__ "BaseException.__cause__").

__context__[¶](https://docs.python.org/3/library/traceback.html#traceback.TracebackException.__context__ "Link to this definition")

A `TracebackException` of the original [`__context__`](https://docs.python.org/3/library/exceptions.html#BaseException.__context__ "BaseException.__context__").

exceptions[¶](https://docs.python.org/3/library/traceback.html#traceback.TracebackException.exceptions "Link to this definition")

If `self` represents an [`ExceptionGroup`](https://docs.python.org/3/library/exceptions.html#ExceptionGroup "ExceptionGroup"), this field holds a list of `TracebackException` instances representing the nested exceptions. Otherwise it is `None`.
Added in version 3.11.

__suppress_context__[¶](https://docs.python.org/3/library/traceback.html#traceback.TracebackException.__suppress_context__ "Link to this definition")

The [`__suppress_context__`](https://docs.python.org/3/library/exceptions.html#BaseException.__suppress_context__ "BaseException.__suppress_context__") value from the original exception.

__notes__[¶](https://docs.python.org/3/library/traceback.html#traceback.TracebackException.__notes__ "Link to this definition")

The [`__notes__`](https://docs.python.org/3/library/exceptions.html#BaseException.__notes__ "BaseException.__notes__") value from the original exception, or `None` if the exception does not have any notes. If it is not `None` is it formatted in the traceback after the exception string.
Added in version 3.11.

stack[¶](https://docs.python.org/3/library/traceback.html#traceback.TracebackException.stack "Link to this definition")

A [`StackSummary`](https://docs.python.org/3/library/traceback.html#traceback.StackSummary "traceback.StackSummary") representing the traceback.

exc_type[¶](https://docs.python.org/3/library/traceback.html#traceback.TracebackException.exc_type "Link to this definition")

The class of the original traceback.
Deprecated since version 3.13.

exc_type_str[¶](https://docs.python.org/3/library/traceback.html#traceback.TracebackException.exc_type_str "Link to this definition")

String display of the class of the original exception.
Added in version 3.13.

filename[¶](https://docs.python.org/3/library/traceback.html#traceback.TracebackException.filename "Link to this definition")

For syntax errors - the file name where the error occurred.

lineno[¶](https://docs.python.org/3/library/traceback.html#traceback.TracebackException.lineno "Link to this definition")

For syntax errors - the line number where the error occurred.

end_lineno[¶](https://docs.python.org/3/library/traceback.html#traceback.TracebackException.end_lineno "Link to this definition")

For syntax errors - the end line number where the error occurred. Can be `None` if not present.
Added in version 3.10.

text[¶](https://docs.python.org/3/library/traceback.html#traceback.TracebackException.text "Link to this definition")

For syntax errors - the text where the error occurred.

offset[¶](https://docs.python.org/3/library/traceback.html#traceback.TracebackException.offset "Link to this definition")

For syntax errors - the offset into the text where the error occurred.

end_offset[¶](https://docs.python.org/3/library/traceback.html#traceback.TracebackException.end_offset "Link to this definition")

For syntax errors - the end offset into the text where the error occurred. Can be `None` if not present.
Added in version 3.10.

msg[¶](https://docs.python.org/3/library/traceback.html#traceback.TracebackException.msg "Link to this definition")

For syntax errors - the compiler error message.

_classmethod_ from_exception(_exc_ , _*_ , _limit =None_, _lookup_lines =True_, _capture_locals =False_)[¶](https://docs.python.org/3/library/traceback.html#traceback.TracebackException.from_exception "Link to this definition")

Capture an exception for later rendering. _limit_ , _lookup_lines_ and _capture_locals_ are as for the [`StackSummary`](https://docs.python.org/3/library/traceback.html#traceback.StackSummary "traceback.StackSummary") class.
Note that when locals are captured, they are also shown in the traceback.

print(_*_ , _file =None_, _chain =True_)[¶](https://docs.python.org/3/library/traceback.html#traceback.TracebackException.print "Link to this definition")

Print to _file_ (default `sys.stderr`) the exception information returned by [`format()`](https://docs.python.org/3/library/functions.html#format "format").
Added in version 3.11.

format(_*_ , _chain =True_)[¶](https://docs.python.org/3/library/traceback.html#traceback.TracebackException.format "Link to this definition")

Format the exception.
If _chain_ is not `True`, [`__cause__`](https://docs.python.org/3/library/traceback.html#traceback.TracebackException.__cause__ "traceback.TracebackException.__cause__") and [`__context__`](https://docs.python.org/3/library/traceback.html#traceback.TracebackException.__context__ "traceback.TracebackException.__context__") will not be formatted.
The return value is a generator of strings, each ending in a newline and some containing internal newlines. [`print_exception()`](https://docs.python.org/3/library/traceback.html#traceback.print_exception "traceback.print_exception") is a wrapper around this method which just prints the lines to a file.

format_exception_only(_*_ , _show_group =False_)[¶](https://docs.python.org/3/library/traceback.html#traceback.TracebackException.format_exception_only "Link to this definition")

Format the exception part of the traceback.
The return value is a generator of strings, each ending in a newline.
When _show_group_ is `False`, the generator emits the exception’s message followed by its notes (if it has any). The exception message is normally a single string; however, for [`SyntaxError`](https://docs.python.org/3/library/exceptions.html#SyntaxError "SyntaxError") exceptions, it consists of several lines that (when printed) display detailed information about where the syntax error occurred.
When _show_group_ is `True`, and the exception is an instance of [`BaseExceptionGroup`](https://docs.python.org/3/library/exceptions.html#BaseExceptionGroup "BaseExceptionGroup"), the nested exceptions are included as well, recursively, with indentation relative to their nesting depth.
Changed in version 3.11: The exception’s [`notes`](https://docs.python.org/3/library/exceptions.html#BaseException.__notes__ "BaseException.__notes__") are now included in the output.
Changed in version 3.13: Added the _show_group_ parameter.
##  `StackSummary` Objects[¶](https://docs.python.org/3/library/traceback.html#stacksummary-objects "Link to this heading")
Added in version 3.5.
`StackSummary` objects represent a call stack ready for formatting.

_class_ traceback.StackSummary[¶](https://docs.python.org/3/library/traceback.html#traceback.StackSummary "Link to this definition")


_classmethod_ extract(_frame_gen_ , _*_ , _limit =None_, _lookup_lines =True_, _capture_locals =False_)[¶](https://docs.python.org/3/library/traceback.html#traceback.StackSummary.extract "Link to this definition")

Construct a `StackSummary` object from a frame generator (such as is returned by [`walk_stack()`](https://docs.python.org/3/library/traceback.html#traceback.walk_stack "traceback.walk_stack") or [`walk_tb()`](https://docs.python.org/3/library/traceback.html#traceback.walk_tb "traceback.walk_tb")).
If _limit_ is supplied, only this many frames are taken from _frame_gen_. If _lookup_lines_ is `False`, the returned [`FrameSummary`](https://docs.python.org/3/library/traceback.html#traceback.FrameSummary "traceback.FrameSummary") objects will not have read their lines in yet, making the cost of creating the `StackSummary` cheaper (which may be valuable if it may not actually get formatted). If _capture_locals_ is `True` the local variables in each `FrameSummary` are captured as object representations.
Changed in version 3.12: Exceptions raised from [`repr()`](https://docs.python.org/3/library/functions.html#repr "repr") on a local variable (when _capture_locals_ is `True`) are no longer propagated to the caller.

_classmethod_ from_list(_a_list_)[¶](https://docs.python.org/3/library/traceback.html#traceback.StackSummary.from_list "Link to this definition")

Construct a `StackSummary` object from a supplied list of [`FrameSummary`](https://docs.python.org/3/library/traceback.html#traceback.FrameSummary "traceback.FrameSummary") objects or old-style list of tuples. Each tuple should be a 4-tuple with _filename_ , _lineno_ , _name_ , _line_ as the elements.

format()[¶](https://docs.python.org/3/library/traceback.html#traceback.StackSummary.format "Link to this definition")

Returns a list of strings ready for printing. Each string in the resulting list corresponds to a single [frame](https://docs.python.org/3/reference/datamodel.html#frame-objects) from the stack. Each string ends in a newline; the strings may contain internal newlines as well, for those items with source text lines.
For long sequences of the same frame and line, the first few repetitions are shown, followed by a summary line stating the exact number of further repetitions.
Changed in version 3.6: Long sequences of repeated frames are now abbreviated.

format_frame_summary(_frame_summary_)[¶](https://docs.python.org/3/library/traceback.html#traceback.StackSummary.format_frame_summary "Link to this definition")

Returns a string for printing one of the [frames](https://docs.python.org/3/reference/datamodel.html#frame-objects) involved in the stack. This method is called for each [`FrameSummary`](https://docs.python.org/3/library/traceback.html#traceback.FrameSummary "traceback.FrameSummary") object to be printed by [`StackSummary.format()`](https://docs.python.org/3/library/traceback.html#traceback.StackSummary.format "traceback.StackSummary.format"). If it returns `None`, the frame is omitted from the output.
Added in version 3.11.
##  `FrameSummary` Objects[¶](https://docs.python.org/3/library/traceback.html#framesummary-objects "Link to this heading")
Added in version 3.5.
A `FrameSummary` object represents a single [frame](https://docs.python.org/3/reference/datamodel.html#frame-objects) in a [traceback](https://docs.python.org/3/reference/datamodel.html#traceback-objects).

_class_ traceback.FrameSummary(_filename_ , _lineno_ , _name_ , _*_ , _lookup_line =True_, _locals =None_, _line =None_, _end_lineno =None_, _colno =None_, _end_colno =None_)[¶](https://docs.python.org/3/library/traceback.html#traceback.FrameSummary "Link to this definition")

Represents a single [frame](https://docs.python.org/3/reference/datamodel.html#frame-objects) in the [traceback](https://docs.python.org/3/reference/datamodel.html#traceback-objects) or stack that is being formatted or printed. It may optionally have a stringified version of the frame’s locals included in it. If _lookup_line_ is `False`, the source code is not looked up until the `FrameSummary` has the [`line`](https://docs.python.org/3/library/traceback.html#traceback.FrameSummary.line "traceback.FrameSummary.line") attribute accessed (which also happens when casting it to a [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "tuple")). `line` may be directly provided, and will prevent line lookups happening at all. _locals_ is an optional local variable mapping, and if supplied the variable representations are stored in the summary for later display.
`FrameSummary` instances have the following attributes:

filename[¶](https://docs.python.org/3/library/traceback.html#traceback.FrameSummary.filename "Link to this definition")

The filename of the source code for this frame. Equivalent to accessing [`f.f_code.co_filename`](https://docs.python.org/3/reference/datamodel.html#codeobject.co_filename "codeobject.co_filename") on a [frame object](https://docs.python.org/3/reference/datamodel.html#frame-objects) _f_.

lineno[¶](https://docs.python.org/3/library/traceback.html#traceback.FrameSummary.lineno "Link to this definition")

The line number of the source code for this frame.

name[¶](https://docs.python.org/3/library/traceback.html#traceback.FrameSummary.name "Link to this definition")

Equivalent to accessing [`f.f_code.co_name`](https://docs.python.org/3/reference/datamodel.html#codeobject.co_name "codeobject.co_name") on a [frame object](https://docs.python.org/3/reference/datamodel.html#frame-objects) _f_.

line[¶](https://docs.python.org/3/library/traceback.html#traceback.FrameSummary.line "Link to this definition")

A string representing the source code for this frame, with leading and trailing whitespace stripped. If the source is not available, it is `None`.

end_lineno[¶](https://docs.python.org/3/library/traceback.html#traceback.FrameSummary.end_lineno "Link to this definition")

The last line number of the source code for this frame. By default, it is set to `lineno` and indexation starts from 1.
Changed in version 3.13: The default value changed from `None` to `lineno`.

colno[¶](https://docs.python.org/3/library/traceback.html#traceback.FrameSummary.colno "Link to this definition")

The column number of the source code for this frame. By default, it is `None` and indexation starts from 0.

end_colno[¶](https://docs.python.org/3/library/traceback.html#traceback.FrameSummary.end_colno "Link to this definition")

The last column number of the source code for this frame. By default, it is `None` and indexation starts from 0.
## Examples of Using the Module-Level Functions[¶](https://docs.python.org/3/library/traceback.html#examples-of-using-the-module-level-functions "Link to this heading")
This simple example implements a basic read-eval-print loop, similar to (but less useful than) the standard Python interactive interpreter loop. For a more complete implementation of the interpreter loop, refer to the [`code`](https://docs.python.org/3/library/code.html#module-code "code: Facilities to implement read-eval-print loops.") module.
Copy```
import sys, traceback

def run_user_code(envdir):
    source = input(">>> ")
    try:
        exec(source, envdir)
    except Exception:
        print("Exception in user code:")
        print("-"*60)
        traceback.print_exc(file=sys.stdout)
        print("-"*60)

envdir = {}
while True:
    run_user_code(envdir)

```

The following example demonstrates the different ways to print and format the exception and traceback:
Copy```
import sys, traceback

def lumberjack():
    bright_side_of_life()

def bright_side_of_life():
    return tuple()[0]

try:
    lumberjack()
except IndexError as exc:
    print("*** print_tb:")
    traceback.print_tb(exc.__traceback__, limit=1, file=sys.stdout)
    print("*** print_exception:")
    traceback.print_exception(exc, limit=2, file=sys.stdout)
    print("*** print_exc:")
    traceback.print_exc(limit=2, file=sys.stdout)
    print("*** format_exc, first and last line:")
    formatted_lines = traceback.format_exc().splitlines()
    print(formatted_lines[0])
    print(formatted_lines[-1])
    print("*** format_exception:")
    print(repr(traceback.format_exception(exc)))
    print("*** extract_tb:")
    print(repr(traceback.extract_tb(exc.__traceback__)))
    print("*** format_tb:")
    print(repr(traceback.format_tb(exc.__traceback__)))
    print("*** tb_lineno:", exc.__traceback__.tb_lineno)

```

The output for the example would look similar to this:
```
*** print_tb:
  File "<doctest...>", line 10, in <module>
    lumberjack()
    ~~~~~~~~~~^^
*** print_exception:
Traceback (most recent call last):
  File "<doctest...>", line 10, in <module>
    lumberjack()
    ~~~~~~~~~~^^
  File "<doctest...>", line 4, in lumberjack
    bright_side_of_life()
    ~~~~~~~~~~~~~~~~~~~^^
IndexError: tuple index out of range
*** print_exc:
Traceback (most recent call last):
  File "<doctest...>", line 10, in <module>
    lumberjack()
    ~~~~~~~~~~^^
  File "<doctest...>", line 4, in lumberjack
    bright_side_of_life()
    ~~~~~~~~~~~~~~~~~~~^^
IndexError: tuple index out of range
*** format_exc, first and last line:
Traceback (most recent call last):
IndexError: tuple index out of range
*** format_exception:
['Traceback (most recent call last):\n',
 '  File "<doctest default[0]>", line 10, in <module>\n    lumberjack()\n    ~~~~~~~~~~^^\n',
 '  File "<doctest default[0]>", line 4, in lumberjack\n    bright_side_of_life()\n    ~~~~~~~~~~~~~~~~~~~^^\n',
 '  File "<doctest default[0]>", line 7, in bright_side_of_life\n    return tuple()[0]\n           ~~~~~~~^^^\n',
 'IndexError: tuple index out of range\n']
*** extract_tb:
[<FrameSummary file <doctest...>, line 10 in <module>>,
 <FrameSummary file <doctest...>, line 4 in lumberjack>,
 <FrameSummary file <doctest...>, line 7 in bright_side_of_life>]
*** format_tb:
['  File "<doctest default[0]>", line 10, in <module>\n    lumberjack()\n    ~~~~~~~~~~^^\n',
 '  File "<doctest default[0]>", line 4, in lumberjack\n    bright_side_of_life()\n    ~~~~~~~~~~~~~~~~~~~^^\n',
 '  File "<doctest default[0]>", line 7, in bright_side_of_life\n    return tuple()[0]\n           ~~~~~~~^^^\n']
*** tb_lineno: 10

```

The following example shows the different ways to print and format the stack:
Copy```
>>> import traceback
>>> def another_function():
...     lumberstack()
...
>>> def lumberstack():
...     traceback.print_stack()
...     print(repr(traceback.extract_stack()))
...     print(repr(traceback.format_stack()))
...
>>> another_function()
  File "<doctest>", line 10, in <module>
    another_function()
  File "<doctest>", line 3, in another_function
    lumberstack()
  File "<doctest>", line 6, in lumberstack
    traceback.print_stack()
[('<doctest>', 10, '<module>', 'another_function()'),
 ('<doctest>', 3, 'another_function', 'lumberstack()'),
 ('<doctest>', 7, 'lumberstack', 'print(repr(traceback.extract_stack()))')]
['  File "<doctest>", line 10, in <module>\n    another_function()\n',
 '  File "<doctest>", line 3, in another_function\n    lumberstack()\n',
 '  File "<doctest>", line 8, in lumberstack\n    print(repr(traceback.format_stack()))\n']

```

This last example demonstrates the final few formatting functions:
Copy```
>>> import traceback
>>> traceback.format_list([('spam.py', 3, '<module>', 'spam.eggs()'),
...                        ('eggs.py', 42, 'eggs', 'return "bacon"')])
['  File "spam.py", line 3, in <module>\n    spam.eggs()\n',
 '  File "eggs.py", line 42, in eggs\n    return "bacon"\n']
>>> an_error = IndexError('tuple index out of range')
>>> traceback.format_exception_only(an_error)
['IndexError: tuple index out of range\n']

```

## Examples of Using [`TracebackException`](https://docs.python.org/3/library/traceback.html#traceback.TracebackException "traceback.TracebackException")[¶](https://docs.python.org/3/library/traceback.html#examples-of-using-tracebackexception "Link to this heading")
With the helper class, we have more options:
Copy```
>>> import sys
>>> from traceback import TracebackException
>>>
>>> def lumberjack():
...     bright_side_of_life()
...
>>> def bright_side_of_life():
...     t = "bright", "side", "of", "life"
...     return t[5]
...
>>> try:
...     lumberjack()
... except IndexError as e:
...     exc = e
...
>>> try:
...     try:
...         lumberjack()
...     except:
...         1/0
... except Exception as e:
...     chained_exc = e
...
>>> # limit works as with the module-level functions
>>> TracebackException.from_exception(exc, limit=-2).print()
Traceback (most recent call last):
  File "<python-input-1>", line 6, in lumberjack
    bright_side_of_life()
    ~~~~~~~~~~~~~~~~~~~^^
  File "<python-input-1>", line 10, in bright_side_of_life
    return t[5]
           ~^^^
IndexError: tuple index out of range

>>> # capture_locals adds local variables in frames
>>> TracebackException.from_exception(exc, limit=-2, capture_locals=True).print()
Traceback (most recent call last):
  File "<python-input-1>", line 6, in lumberjack
    bright_side_of_life()
    ~~~~~~~~~~~~~~~~~~~^^
  File "<python-input-1>", line 10, in bright_side_of_life
    return t[5]
           ~^^^
    t = ("bright", "side", "of", "life")
IndexError: tuple index out of range

>>> # The *chain* kwarg to print() controls whether chained
>>> # exceptions are displayed
>>> TracebackException.from_exception(chained_exc).print()
Traceback (most recent call last):
  File "<python-input-19>", line 4, in <module>
    lumberjack()
    ~~~~~~~~~~^^
  File "<python-input-8>", line 7, in lumberjack
    bright_side_of_life()
    ~~~~~~~~~~~~~~~~~~~^^
  File "<python-input-8>", line 11, in bright_side_of_life
    return t[5]
           ~^^^
IndexError: tuple index out of range

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<python-input-19>", line 6, in <module>
    1/0
    ~^~
ZeroDivisionError: division by zero

>>> TracebackException.from_exception(chained_exc).print(chain=False)
Traceback (most recent call last):
  File "<python-input-19>", line 6, in <module>
    1/0
    ~^~
ZeroDivisionError: division by zero

```

### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`traceback` — Print or retrieve a stack traceback](https://docs.python.org/3/library/traceback.html)
    * [Module-Level Functions](https://docs.python.org/3/library/traceback.html#module-level-functions)
    * [`TracebackException` Objects](https://docs.python.org/3/library/traceback.html#tracebackexception-objects)
    * [`StackSummary` Objects](https://docs.python.org/3/library/traceback.html#stacksummary-objects)
    * [`FrameSummary` Objects](https://docs.python.org/3/library/traceback.html#framesummary-objects)
    * [Examples of Using the Module-Level Functions](https://docs.python.org/3/library/traceback.html#examples-of-using-the-module-level-functions)
    * [Examples of Using `TracebackException`](https://docs.python.org/3/library/traceback.html#examples-of-using-tracebackexception)


#### Previous topic
[`atexit` — Exit handlers](https://docs.python.org/3/library/atexit.html "previous chapter")
#### Next topic
[`__future__` — Future statement definitions](https://docs.python.org/3/library/__future__.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=traceback+%E2%80%94+Print+or+retrieve+a+stack+traceback&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ftraceback.html&pagesource=library%2Ftraceback.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/__future__.html "__future__ — Future statement definitions") |
  * [previous](https://docs.python.org/3/library/atexit.html "atexit — Exit handlers") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Python Runtime Services](https://docs.python.org/3/library/python.html) »
  * [`traceback` — Print or retrieve a stack traceback](https://docs.python.org/3/library/traceback.html)
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
