[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
#### Previous topic
[Audit events table](https://docs.python.org/3/library/audit_events.html "previous chapter")
#### Next topic
[`faulthandler` — Dump the Python traceback](https://docs.python.org/3/library/faulthandler.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=bdb+%E2%80%94+Debugger+framework&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fbdb.html&pagesource=library%2Fbdb.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/faulthandler.html "faulthandler — Dump the Python traceback") |
  * [previous](https://docs.python.org/3/library/audit_events.html "Audit events table") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Debugging and Profiling](https://docs.python.org/3/library/debug.html) »
  * [`bdb` — Debugger framework](https://docs.python.org/3/library/bdb.html)
  * |
  * Theme  Auto Light Dark |


#  `bdb` — Debugger framework[¶](https://docs.python.org/3/library/bdb.html#module-bdb "Link to this heading")
**Source code:**
* * *
The `bdb` module handles basic debugger functions, like setting breakpoints or managing execution via the debugger.
The following exception is defined:

_exception_ bdb.BdbQuit[¶](https://docs.python.org/3/library/bdb.html#bdb.BdbQuit "Link to this definition")

Exception raised by the [`Bdb`](https://docs.python.org/3/library/bdb.html#bdb.Bdb "bdb.Bdb") class for quitting the debugger.
The `bdb` module also defines two classes:

_class_ bdb.Breakpoint(_self_ , _file_ , _line_ , _temporary =False_, _cond =None_, _funcname =None_)[¶](https://docs.python.org/3/library/bdb.html#bdb.Breakpoint "Link to this definition")

This class implements temporary breakpoints, ignore counts, disabling and (re-)enabling, and conditionals.
Breakpoints are indexed by number through a list called [`bpbynumber`](https://docs.python.org/3/library/bdb.html#bdb.Breakpoint.bpbynumber "bdb.Breakpoint.bpbynumber") and by `(file, line)` pairs through [`bplist`](https://docs.python.org/3/library/bdb.html#bdb.Breakpoint.bplist "bdb.Breakpoint.bplist"). The former points to a single instance of class `Breakpoint`. The latter points to a list of such instances since there may be more than one breakpoint per line.
When creating a breakpoint, its associated [`file name`](https://docs.python.org/3/library/bdb.html#bdb.Breakpoint.file "bdb.Breakpoint.file") should be in canonical form. If a [`funcname`](https://docs.python.org/3/library/bdb.html#bdb.Breakpoint.funcname "bdb.Breakpoint.funcname") is defined, a breakpoint [`hit`](https://docs.python.org/3/library/bdb.html#bdb.Breakpoint.hits "bdb.Breakpoint.hits") will be counted when the first line of that function is executed. A [`conditional`](https://docs.python.org/3/library/bdb.html#bdb.Breakpoint.cond "bdb.Breakpoint.cond") breakpoint always counts a `hit`.
`Breakpoint` instances have the following methods:

deleteMe()[¶](https://docs.python.org/3/library/bdb.html#bdb.Breakpoint.deleteMe "Link to this definition")

Delete the breakpoint from the list associated to a file/line. If it is the last breakpoint in that position, it also deletes the entry for the file/line.

enable()[¶](https://docs.python.org/3/library/bdb.html#bdb.Breakpoint.enable "Link to this definition")

Mark the breakpoint as enabled.

disable()[¶](https://docs.python.org/3/library/bdb.html#bdb.Breakpoint.disable "Link to this definition")

Mark the breakpoint as disabled.

bpformat()[¶](https://docs.python.org/3/library/bdb.html#bdb.Breakpoint.bpformat "Link to this definition")

Return a string with all the information about the breakpoint, nicely formatted:
  * Breakpoint number.
  * Temporary status (del or keep).
  * File/line position.
  * Break condition.
  * Number of times to ignore.
  * Number of times hit.


Added in version 3.2.

bpprint(_out =None_)[¶](https://docs.python.org/3/library/bdb.html#bdb.Breakpoint.bpprint "Link to this definition")

Print the output of [`bpformat()`](https://docs.python.org/3/library/bdb.html#bdb.Breakpoint.bpformat "bdb.Breakpoint.bpformat") to the file _out_ , or if it is `None`, to standard output.
`Breakpoint` instances have the following attributes:

file[¶](https://docs.python.org/3/library/bdb.html#bdb.Breakpoint.file "Link to this definition")

File name of the `Breakpoint`.

line[¶](https://docs.python.org/3/library/bdb.html#bdb.Breakpoint.line "Link to this definition")

Line number of the `Breakpoint` within [`file`](https://docs.python.org/3/library/bdb.html#bdb.Breakpoint.file "bdb.Breakpoint.file").

temporary[¶](https://docs.python.org/3/library/bdb.html#bdb.Breakpoint.temporary "Link to this definition")

`True` if a `Breakpoint` at (file, line) is temporary.

cond[¶](https://docs.python.org/3/library/bdb.html#bdb.Breakpoint.cond "Link to this definition")

Condition for evaluating a `Breakpoint` at (file, line).

funcname[¶](https://docs.python.org/3/library/bdb.html#bdb.Breakpoint.funcname "Link to this definition")

Function name that defines whether a `Breakpoint` is hit upon entering the function.

enabled[¶](https://docs.python.org/3/library/bdb.html#bdb.Breakpoint.enabled "Link to this definition")

`True` if `Breakpoint` is enabled.

bpbynumber[¶](https://docs.python.org/3/library/bdb.html#bdb.Breakpoint.bpbynumber "Link to this definition")

Numeric index for a single instance of a `Breakpoint`.

bplist[¶](https://docs.python.org/3/library/bdb.html#bdb.Breakpoint.bplist "Link to this definition")

Dictionary of `Breakpoint` instances indexed by ([`file`](https://docs.python.org/3/library/bdb.html#bdb.Breakpoint.file "bdb.Breakpoint.file"), [`line`](https://docs.python.org/3/library/bdb.html#bdb.Breakpoint.line "bdb.Breakpoint.line")) tuples.

ignore[¶](https://docs.python.org/3/library/bdb.html#bdb.Breakpoint.ignore "Link to this definition")

Number of times to ignore a `Breakpoint`.

hits[¶](https://docs.python.org/3/library/bdb.html#bdb.Breakpoint.hits "Link to this definition")

Count of the number of times a `Breakpoint` has been hit.

_class_ bdb.Bdb(_skip =None_, _backend ='settrace'_)[¶](https://docs.python.org/3/library/bdb.html#bdb.Bdb "Link to this definition")

The `Bdb` class acts as a generic Python debugger base class.
This class takes care of the details of the trace facility; a derived class should implement user interaction. The standard debugger class ([`pdb.Pdb`](https://docs.python.org/3/library/pdb.html#pdb.Pdb "pdb.Pdb")) is an example.
The _skip_ argument, if given, must be an iterable of glob-style module name patterns. The debugger will not step into frames that originate in a module that matches one of these patterns. Whether a frame is considered to originate in a certain module is determined by the `__name__` in the frame globals.
The _backend_ argument specifies the backend to use for `Bdb`. It can be either `'settrace'` or `'monitoring'`. `'settrace'` uses [`sys.settrace()`](https://docs.python.org/3/library/sys.html#sys.settrace "sys.settrace") which has the best backward compatibility. The `'monitoring'` backend uses the new [`sys.monitoring`](https://docs.python.org/3/library/sys.monitoring.html#module-sys.monitoring "sys.monitoring: Access and control event monitoring") that was introduced in Python 3.12, which can be much more efficient because it can disable unused events. We are trying to keep the exact interfaces for both backends, but there are some differences. The debugger developers are encouraged to use the `'monitoring'` backend to achieve better performance.
Changed in version 3.1: Added the _skip_ parameter.
Changed in version 3.14: Added the _backend_ parameter.
The following methods of `Bdb` normally don’t need to be overridden.

canonic(_filename_)[¶](https://docs.python.org/3/library/bdb.html#bdb.Bdb.canonic "Link to this definition")

Return canonical form of _filename_.
For real file names, the canonical form is an operating-system-dependent, [`case-normalized`](https://docs.python.org/3/library/os.path.html#os.path.normcase "os.path.normcase") [`absolute path`](https://docs.python.org/3/library/os.path.html#os.path.abspath "os.path.abspath"). A _filename_ with angle brackets, such as `"<stdin>"` generated in interactive mode, is returned unchanged.

start_trace(_self_)[¶](https://docs.python.org/3/library/bdb.html#bdb.Bdb.start_trace "Link to this definition")

Start tracing. For `'settrace'` backend, this method is equivalent to `sys.settrace(self.trace_dispatch)`
Added in version 3.14.

stop_trace(_self_)[¶](https://docs.python.org/3/library/bdb.html#bdb.Bdb.stop_trace "Link to this definition")

Stop tracing. For `'settrace'` backend, this method is equivalent to `sys.settrace(None)`
Added in version 3.14.

reset()[¶](https://docs.python.org/3/library/bdb.html#bdb.Bdb.reset "Link to this definition")

Set the `botframe`, `stopframe`, `returnframe` and [`quitting`](https://docs.python.org/3/library/bdb.html#bdb.Bdb.set_quit "bdb.Bdb.set_quit") attributes with values ready to start debugging.

trace_dispatch(_frame_ , _event_ , _arg_)[¶](https://docs.python.org/3/library/bdb.html#bdb.Bdb.trace_dispatch "Link to this definition")

This function is installed as the trace function of debugged frames. Its return value is the new trace function (in most cases, that is, itself).
The default implementation decides how to dispatch a frame, depending on the type of event (passed as a string) that is about to be executed. _event_ can be one of the following:
  * `"line"`: A new line of code is going to be executed.
  * `"call"`: A function is about to be called, or another code block entered.
  * `"return"`: A function or other code block is about to return.
  * `"exception"`: An exception has occurred.
  * `"c_call"`: A C function is about to be called.
  * `"c_return"`: A C function has returned.
  * `"c_exception"`: A C function has raised an exception.


For the Python events, specialized functions (see below) are called. For the C events, no action is taken.
The _arg_ parameter depends on the previous event.
See the documentation for [`sys.settrace()`](https://docs.python.org/3/library/sys.html#sys.settrace "sys.settrace") for more information on the trace function. For more information on code and frame objects, refer to [The standard type hierarchy](https://docs.python.org/3/reference/datamodel.html#types).

dispatch_line(_frame_)[¶](https://docs.python.org/3/library/bdb.html#bdb.Bdb.dispatch_line "Link to this definition")

If the debugger should stop on the current line, invoke the [`user_line()`](https://docs.python.org/3/library/bdb.html#bdb.Bdb.user_line "bdb.Bdb.user_line") method (which should be overridden in subclasses). Raise a [`BdbQuit`](https://docs.python.org/3/library/bdb.html#bdb.BdbQuit "bdb.BdbQuit") exception if the [`quitting`](https://docs.python.org/3/library/bdb.html#bdb.Bdb.set_quit "bdb.Bdb.set_quit") flag is set (which can be set from `user_line()`). Return a reference to the [`trace_dispatch()`](https://docs.python.org/3/library/bdb.html#bdb.Bdb.trace_dispatch "bdb.Bdb.trace_dispatch") method for further tracing in that scope.

dispatch_call(_frame_ , _arg_)[¶](https://docs.python.org/3/library/bdb.html#bdb.Bdb.dispatch_call "Link to this definition")

If the debugger should stop on this function call, invoke the [`user_call()`](https://docs.python.org/3/library/bdb.html#bdb.Bdb.user_call "bdb.Bdb.user_call") method (which should be overridden in subclasses). Raise a [`BdbQuit`](https://docs.python.org/3/library/bdb.html#bdb.BdbQuit "bdb.BdbQuit") exception if the [`quitting`](https://docs.python.org/3/library/bdb.html#bdb.Bdb.set_quit "bdb.Bdb.set_quit") flag is set (which can be set from `user_call()`). Return a reference to the [`trace_dispatch()`](https://docs.python.org/3/library/bdb.html#bdb.Bdb.trace_dispatch "bdb.Bdb.trace_dispatch") method for further tracing in that scope.

dispatch_return(_frame_ , _arg_)[¶](https://docs.python.org/3/library/bdb.html#bdb.Bdb.dispatch_return "Link to this definition")

If the debugger should stop on this function return, invoke the [`user_return()`](https://docs.python.org/3/library/bdb.html#bdb.Bdb.user_return "bdb.Bdb.user_return") method (which should be overridden in subclasses). Raise a [`BdbQuit`](https://docs.python.org/3/library/bdb.html#bdb.BdbQuit "bdb.BdbQuit") exception if the [`quitting`](https://docs.python.org/3/library/bdb.html#bdb.Bdb.set_quit "bdb.Bdb.set_quit") flag is set (which can be set from `user_return()`). Return a reference to the [`trace_dispatch()`](https://docs.python.org/3/library/bdb.html#bdb.Bdb.trace_dispatch "bdb.Bdb.trace_dispatch") method for further tracing in that scope.

dispatch_exception(_frame_ , _arg_)[¶](https://docs.python.org/3/library/bdb.html#bdb.Bdb.dispatch_exception "Link to this definition")

If the debugger should stop at this exception, invokes the [`user_exception()`](https://docs.python.org/3/library/bdb.html#bdb.Bdb.user_exception "bdb.Bdb.user_exception") method (which should be overridden in subclasses). Raise a [`BdbQuit`](https://docs.python.org/3/library/bdb.html#bdb.BdbQuit "bdb.BdbQuit") exception if the [`quitting`](https://docs.python.org/3/library/bdb.html#bdb.Bdb.set_quit "bdb.Bdb.set_quit") flag is set (which can be set from `user_exception()`). Return a reference to the [`trace_dispatch()`](https://docs.python.org/3/library/bdb.html#bdb.Bdb.trace_dispatch "bdb.Bdb.trace_dispatch") method for further tracing in that scope.
Normally derived classes don’t override the following methods, but they may if they want to redefine the definition of stopping and breakpoints.

is_skipped_module(_module_name_)[¶](https://docs.python.org/3/library/bdb.html#bdb.Bdb.is_skipped_module "Link to this definition")

Return `True` if _module_name_ matches any skip pattern.

stop_here(_frame_)[¶](https://docs.python.org/3/library/bdb.html#bdb.Bdb.stop_here "Link to this definition")

Return `True` if _frame_ is below the starting frame in the stack.

break_here(_frame_)[¶](https://docs.python.org/3/library/bdb.html#bdb.Bdb.break_here "Link to this definition")

Return `True` if there is an effective breakpoint for this line.
Check whether a line or function breakpoint exists and is in effect. Delete temporary breakpoints based on information from [`effective()`](https://docs.python.org/3/library/bdb.html#bdb.effective "bdb.effective").

break_anywhere(_frame_)[¶](https://docs.python.org/3/library/bdb.html#bdb.Bdb.break_anywhere "Link to this definition")

Return `True` if any breakpoint exists for _frame_ ’s filename.
Derived classes should override these methods to gain control over debugger operation.

user_call(_frame_ , _argument_list_)[¶](https://docs.python.org/3/library/bdb.html#bdb.Bdb.user_call "Link to this definition")

Called from [`dispatch_call()`](https://docs.python.org/3/library/bdb.html#bdb.Bdb.dispatch_call "bdb.Bdb.dispatch_call") if a break might stop inside the called function.
_argument_list_ is not used anymore and will always be `None`. The argument is kept for backwards compatibility.

user_line(_frame_)[¶](https://docs.python.org/3/library/bdb.html#bdb.Bdb.user_line "Link to this definition")

Called from [`dispatch_line()`](https://docs.python.org/3/library/bdb.html#bdb.Bdb.dispatch_line "bdb.Bdb.dispatch_line") when either [`stop_here()`](https://docs.python.org/3/library/bdb.html#bdb.Bdb.stop_here "bdb.Bdb.stop_here") or [`break_here()`](https://docs.python.org/3/library/bdb.html#bdb.Bdb.break_here "bdb.Bdb.break_here") returns `True`.

user_return(_frame_ , _return_value_)[¶](https://docs.python.org/3/library/bdb.html#bdb.Bdb.user_return "Link to this definition")

Called from [`dispatch_return()`](https://docs.python.org/3/library/bdb.html#bdb.Bdb.dispatch_return "bdb.Bdb.dispatch_return") when [`stop_here()`](https://docs.python.org/3/library/bdb.html#bdb.Bdb.stop_here "bdb.Bdb.stop_here") returns `True`.

user_exception(_frame_ , _exc_info_)[¶](https://docs.python.org/3/library/bdb.html#bdb.Bdb.user_exception "Link to this definition")

Called from [`dispatch_exception()`](https://docs.python.org/3/library/bdb.html#bdb.Bdb.dispatch_exception "bdb.Bdb.dispatch_exception") when [`stop_here()`](https://docs.python.org/3/library/bdb.html#bdb.Bdb.stop_here "bdb.Bdb.stop_here") returns `True`.

do_clear(_arg_)[¶](https://docs.python.org/3/library/bdb.html#bdb.Bdb.do_clear "Link to this definition")

Handle how a breakpoint must be removed when it is a temporary one.
This method must be implemented by derived classes.
Derived classes and clients can call the following methods to affect the stepping state.

set_step()[¶](https://docs.python.org/3/library/bdb.html#bdb.Bdb.set_step "Link to this definition")

Stop after one line of code.

set_next(_frame_)[¶](https://docs.python.org/3/library/bdb.html#bdb.Bdb.set_next "Link to this definition")

Stop on the next line in or below the given frame.

set_return(_frame_)[¶](https://docs.python.org/3/library/bdb.html#bdb.Bdb.set_return "Link to this definition")

Stop when returning from the given frame.

set_until(_frame_ , _lineno =None_)[¶](https://docs.python.org/3/library/bdb.html#bdb.Bdb.set_until "Link to this definition")

Stop when the line with the _lineno_ greater than the current one is reached or when returning from current frame.

set_trace([_frame_])[¶](https://docs.python.org/3/library/bdb.html#bdb.Bdb.set_trace "Link to this definition")

Start debugging from _frame_. If _frame_ is not specified, debugging starts from caller’s frame.
Changed in version 3.13: [`set_trace()`](https://docs.python.org/3/library/bdb.html#bdb.set_trace "bdb.set_trace") will enter the debugger immediately, rather than on the next line of code to be executed.

set_continue()[¶](https://docs.python.org/3/library/bdb.html#bdb.Bdb.set_continue "Link to this definition")

Stop only at breakpoints or when finished. If there are no breakpoints, set the system trace function to `None`.

set_quit()[¶](https://docs.python.org/3/library/bdb.html#bdb.Bdb.set_quit "Link to this definition")

Set the `quitting` attribute to `True`. This raises [`BdbQuit`](https://docs.python.org/3/library/bdb.html#bdb.BdbQuit "bdb.BdbQuit") in the next call to one of the `dispatch_*()` methods.
Derived classes and clients can call the following methods to manipulate breakpoints. These methods return a string containing an error message if something went wrong, or `None` if all is well.

set_break(_filename_ , _lineno_ , _temporary =False_, _cond =None_, _funcname =None_)[¶](https://docs.python.org/3/library/bdb.html#bdb.Bdb.set_break "Link to this definition")

Set a new breakpoint. If the _lineno_ line doesn’t exist for the _filename_ passed as argument, return an error message. The _filename_ should be in canonical form, as described in the [`canonic()`](https://docs.python.org/3/library/bdb.html#bdb.Bdb.canonic "bdb.Bdb.canonic") method.

clear_break(_filename_ , _lineno_)[¶](https://docs.python.org/3/library/bdb.html#bdb.Bdb.clear_break "Link to this definition")

Delete the breakpoints in _filename_ and _lineno_. If none were set, return an error message.

clear_bpbynumber(_arg_)[¶](https://docs.python.org/3/library/bdb.html#bdb.Bdb.clear_bpbynumber "Link to this definition")

Delete the breakpoint which has the index _arg_ in the [`Breakpoint.bpbynumber`](https://docs.python.org/3/library/bdb.html#bdb.Breakpoint.bpbynumber "bdb.Breakpoint.bpbynumber"). If _arg_ is not numeric or out of range, return an error message.

clear_all_file_breaks(_filename_)[¶](https://docs.python.org/3/library/bdb.html#bdb.Bdb.clear_all_file_breaks "Link to this definition")

Delete all breakpoints in _filename_. If none were set, return an error message.

clear_all_breaks()[¶](https://docs.python.org/3/library/bdb.html#bdb.Bdb.clear_all_breaks "Link to this definition")

Delete all existing breakpoints. If none were set, return an error message.

get_bpbynumber(_arg_)[¶](https://docs.python.org/3/library/bdb.html#bdb.Bdb.get_bpbynumber "Link to this definition")

Return a breakpoint specified by the given number. If _arg_ is a string, it will be converted to a number. If _arg_ is a non-numeric string, if the given breakpoint never existed or has been deleted, a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised.
Added in version 3.2.

get_break(_filename_ , _lineno_)[¶](https://docs.python.org/3/library/bdb.html#bdb.Bdb.get_break "Link to this definition")

Return `True` if there is a breakpoint for _lineno_ in _filename_.

get_breaks(_filename_ , _lineno_)[¶](https://docs.python.org/3/library/bdb.html#bdb.Bdb.get_breaks "Link to this definition")

Return all breakpoints for _lineno_ in _filename_ , or an empty list if none are set.

get_file_breaks(_filename_)[¶](https://docs.python.org/3/library/bdb.html#bdb.Bdb.get_file_breaks "Link to this definition")

Return all breakpoints in _filename_ , or an empty list if none are set.

get_all_breaks()[¶](https://docs.python.org/3/library/bdb.html#bdb.Bdb.get_all_breaks "Link to this definition")

Return all breakpoints that are set.
Derived classes and clients can call the following methods to disable and restart events to achieve better performance. These methods only work when using the `'monitoring'` backend.

disable_current_event()[¶](https://docs.python.org/3/library/bdb.html#bdb.Bdb.disable_current_event "Link to this definition")

Disable the current event until the next time [`restart_events()`](https://docs.python.org/3/library/bdb.html#bdb.Bdb.restart_events "bdb.Bdb.restart_events") is called. This is helpful when the debugger is not interested in the current line.
Added in version 3.14.

restart_events()[¶](https://docs.python.org/3/library/bdb.html#bdb.Bdb.restart_events "Link to this definition")

Restart all the disabled events. This function is automatically called in `dispatch_*` methods after `user_*` methods are called. If the `dispatch_*` methods are not overridden, the disabled events will be restarted after each user interaction.
Added in version 3.14.
Derived classes and clients can call the following methods to get a data structure representing a stack trace.

get_stack(_f_ , _t_)[¶](https://docs.python.org/3/library/bdb.html#bdb.Bdb.get_stack "Link to this definition")

Return a list of (frame, lineno) tuples in a stack trace, and a size.
The most recently called frame is last in the list. The size is the number of frames below the frame where the debugger was invoked.

format_stack_entry(_frame_lineno_ , _lprefix =': '_)[¶](https://docs.python.org/3/library/bdb.html#bdb.Bdb.format_stack_entry "Link to this definition")

Return a string with information about a stack entry, which is a `(frame, lineno)` tuple. The return string contains:
  * The canonical filename which contains the frame.
  * The function name or `"<lambda>"`.
  * The input arguments.
  * The return value.
  * The line of code (if it exists).


The following two methods can be called by clients to use a debugger to debug a [statement](https://docs.python.org/3/glossary.html#term-statement), given as a string.

run(_cmd_ , _globals =None_, _locals =None_)[¶](https://docs.python.org/3/library/bdb.html#bdb.Bdb.run "Link to this definition")

Debug a statement executed via the [`exec()`](https://docs.python.org/3/library/functions.html#exec "exec") function. _globals_ defaults to `__main__.__dict__`, _locals_ defaults to _globals_.

runeval(_expr_ , _globals =None_, _locals =None_)[¶](https://docs.python.org/3/library/bdb.html#bdb.Bdb.runeval "Link to this definition")

Debug an expression executed via the [`eval()`](https://docs.python.org/3/library/functions.html#eval "eval") function. _globals_ and _locals_ have the same meaning as in [`run()`](https://docs.python.org/3/library/bdb.html#bdb.Bdb.run "bdb.Bdb.run").

runctx(_cmd_ , _globals_ , _locals_)[¶](https://docs.python.org/3/library/bdb.html#bdb.Bdb.runctx "Link to this definition")

For backwards compatibility. Calls the [`run()`](https://docs.python.org/3/library/bdb.html#bdb.Bdb.run "bdb.Bdb.run") method.

runcall(_func_ , _/_ , _* args_, _** kwds_)[¶](https://docs.python.org/3/library/bdb.html#bdb.Bdb.runcall "Link to this definition")

Debug a single function call, and return its result.
Finally, the module defines the following functions:

bdb.checkfuncname(_b_ , _frame_)[¶](https://docs.python.org/3/library/bdb.html#bdb.checkfuncname "Link to this definition")

Return `True` if we should break here, depending on the way the [`Breakpoint`](https://docs.python.org/3/library/bdb.html#bdb.Breakpoint "bdb.Breakpoint") _b_ was set.
If it was set via line number, it checks if [`b.line`](https://docs.python.org/3/library/bdb.html#bdb.Breakpoint.line "bdb.Breakpoint.line") is the same as the one in _frame_. If the breakpoint was set via [`function name`](https://docs.python.org/3/library/bdb.html#bdb.Breakpoint.funcname "bdb.Breakpoint.funcname"), we have to check we are in the right _frame_ (the right function) and if we are on its first executable line.

bdb.effective(_file_ , _line_ , _frame_)[¶](https://docs.python.org/3/library/bdb.html#bdb.effective "Link to this definition")

Return `(active breakpoint, delete temporary flag)` or `(None, None)` as the breakpoint to act upon.
The _active breakpoint_ is the first entry in [`bplist`](https://docs.python.org/3/library/bdb.html#bdb.Breakpoint.bplist "bdb.Breakpoint.bplist") for the ([`file`](https://docs.python.org/3/library/bdb.html#bdb.Breakpoint.file "bdb.Breakpoint.file"), [`line`](https://docs.python.org/3/library/bdb.html#bdb.Breakpoint.line "bdb.Breakpoint.line")) (which must exist) that is [`enabled`](https://docs.python.org/3/library/bdb.html#bdb.Breakpoint.enabled "bdb.Breakpoint.enabled"), for which [`checkfuncname()`](https://docs.python.org/3/library/bdb.html#bdb.checkfuncname "bdb.checkfuncname") is true, and that has neither a false [`condition`](https://docs.python.org/3/library/bdb.html#bdb.Breakpoint.cond "bdb.Breakpoint.cond") nor positive [`ignore`](https://docs.python.org/3/library/bdb.html#bdb.Breakpoint.ignore "bdb.Breakpoint.ignore") count. The _flag_ , meaning that a temporary breakpoint should be deleted, is `False` only when the `cond` cannot be evaluated (in which case, `ignore` count is ignored).
If no such entry exists, then `(None, None)` is returned.

bdb.set_trace()[¶](https://docs.python.org/3/library/bdb.html#bdb.set_trace "Link to this definition")

Start debugging with a [`Bdb`](https://docs.python.org/3/library/bdb.html#bdb.Bdb "bdb.Bdb") instance from caller’s frame.
#### Previous topic
[Audit events table](https://docs.python.org/3/library/audit_events.html "previous chapter")
#### Next topic
[`faulthandler` — Dump the Python traceback](https://docs.python.org/3/library/faulthandler.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=bdb+%E2%80%94+Debugger+framework&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fbdb.html&pagesource=library%2Fbdb.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/faulthandler.html "faulthandler — Dump the Python traceback") |
  * [previous](https://docs.python.org/3/library/audit_events.html "Audit events table") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Debugging and Profiling](https://docs.python.org/3/library/debug.html) »
  * [`bdb` — Debugger framework](https://docs.python.org/3/library/bdb.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
  *[/]: Positional-only parameter separator (PEP 570)
