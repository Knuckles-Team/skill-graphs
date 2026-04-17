[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`faulthandler` — Dump the Python traceback](https://docs.python.org/3/library/faulthandler.html)
    * [Dumping the traceback](https://docs.python.org/3/library/faulthandler.html#dumping-the-traceback)
    * [Dumping the C stack](https://docs.python.org/3/library/faulthandler.html#dumping-the-c-stack)
      * [C Stack Compatibility](https://docs.python.org/3/library/faulthandler.html#c-stack-compatibility)
    * [Fault handler state](https://docs.python.org/3/library/faulthandler.html#fault-handler-state)
    * [Dumping the tracebacks after a timeout](https://docs.python.org/3/library/faulthandler.html#dumping-the-tracebacks-after-a-timeout)
    * [Dumping the traceback on a user signal](https://docs.python.org/3/library/faulthandler.html#dumping-the-traceback-on-a-user-signal)
    * [Issue with file descriptors](https://docs.python.org/3/library/faulthandler.html#issue-with-file-descriptors)
    * [Example](https://docs.python.org/3/library/faulthandler.html#example)


#### Previous topic
[`bdb` — Debugger framework](https://docs.python.org/3/library/bdb.html "previous chapter")
#### Next topic
[`pdb` — The Python Debugger](https://docs.python.org/3/library/pdb.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=faulthandler+%E2%80%94+Dump+the+Python+traceback&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ffaulthandler.html&pagesource=library%2Ffaulthandler.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/pdb.html "pdb — The Python Debugger") |
  * [previous](https://docs.python.org/3/library/bdb.html "bdb — Debugger framework") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Debugging and Profiling](https://docs.python.org/3/library/debug.html) »
  * [`faulthandler` — Dump the Python traceback](https://docs.python.org/3/library/faulthandler.html)
  * |
  * Theme  Auto Light Dark |


#  `faulthandler` — Dump the Python traceback[¶](https://docs.python.org/3/library/faulthandler.html#module-faulthandler "Link to this heading")
Added in version 3.3.
* * *
This module contains functions to dump Python tracebacks explicitly, on a fault, after a timeout, or on a user signal. Call [`faulthandler.enable()`](https://docs.python.org/3/library/faulthandler.html#faulthandler.enable "faulthandler.enable") to install fault handlers for the [`SIGSEGV`](https://docs.python.org/3/library/signal.html#signal.SIGSEGV "signal.SIGSEGV"), [`SIGFPE`](https://docs.python.org/3/library/signal.html#signal.SIGFPE "signal.SIGFPE"), [`SIGABRT`](https://docs.python.org/3/library/signal.html#signal.SIGABRT "signal.SIGABRT"), [`SIGBUS`](https://docs.python.org/3/library/signal.html#signal.SIGBUS "signal.SIGBUS"), and [`SIGILL`](https://docs.python.org/3/library/signal.html#signal.SIGILL "signal.SIGILL") signals. You can also enable them at startup by setting the [`PYTHONFAULTHANDLER`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONFAULTHANDLER) environment variable or by using the [`-X`](https://docs.python.org/3/using/cmdline.html#cmdoption-X) `faulthandler` command line option.
The fault handler is compatible with system fault handlers like Apport or the Windows fault handler. The module uses an alternative stack for signal handlers if the `sigaltstack()` function is available. This allows it to dump the traceback even on a stack overflow.
The fault handler is called on catastrophic cases and therefore can only use signal-safe functions (e.g. it cannot allocate memory on the heap). Because of this limitation traceback dumping is minimal compared to normal Python tracebacks:
  * Only ASCII is supported. The `backslashreplace` error handler is used on encoding.
  * Each string is limited to 500 characters.
  * Only the filename, the function name and the line number are displayed. (no source code)
  * It is limited to 100 frames and 100 threads.
  * The order is reversed: the most recent call is shown first.


By default, the Python traceback is written to [`sys.stderr`](https://docs.python.org/3/library/sys.html#sys.stderr "sys.stderr"). To see tracebacks, applications must be run in the terminal. A log file can alternatively be passed to [`faulthandler.enable()`](https://docs.python.org/3/library/faulthandler.html#faulthandler.enable "faulthandler.enable").
The module is implemented in C, so tracebacks can be dumped on a crash or when Python is deadlocked.
The [Python Development Mode](https://docs.python.org/3/library/devmode.html#devmode) calls [`faulthandler.enable()`](https://docs.python.org/3/library/faulthandler.html#faulthandler.enable "faulthandler.enable") at Python startup.
See also

Module [`pdb`](https://docs.python.org/3/library/pdb.html#module-pdb "pdb: The Python debugger for interactive interpreters.")

Interactive source code debugger for Python programs.

Module [`traceback`](https://docs.python.org/3/library/traceback.html#module-traceback "traceback: Print or retrieve a stack traceback.")

Standard interface to extract, format and print stack traces of Python programs.
## Dumping the traceback[¶](https://docs.python.org/3/library/faulthandler.html#dumping-the-traceback "Link to this heading")

faulthandler.dump_traceback(_file =sys.stderr_, _all_threads =True_)[¶](https://docs.python.org/3/library/faulthandler.html#faulthandler.dump_traceback "Link to this definition")

Dump the tracebacks of all threads into _file_. If _all_threads_ is `False`, dump only the current thread.
See also
[`traceback.print_tb()`](https://docs.python.org/3/library/traceback.html#traceback.print_tb "traceback.print_tb"), which can be used to print a traceback object.
Changed in version 3.5: Added support for passing file descriptor to this function.
## Dumping the C stack[¶](https://docs.python.org/3/library/faulthandler.html#dumping-the-c-stack "Link to this heading")
Added in version 3.14.

faulthandler.dump_c_stack(_file =sys.stderr_)[¶](https://docs.python.org/3/library/faulthandler.html#faulthandler.dump_c_stack "Link to this definition")

Dump the C stack trace of the current thread into _file_.
If the Python build does not support it or the operating system does not provide a stack trace, then this prints an error in place of a dumped C stack.
### C Stack Compatibility[¶](https://docs.python.org/3/library/faulthandler.html#c-stack-compatibility "Link to this heading")
If the system does not support the C-level
Additionally, some compilers do not support [CPython’s](https://docs.python.org/3/glossary.html#term-CPython) implementation of C stack dumps. As a result, a different error may be printed instead of the stack, even if the operating system supports dumping stacks.
Note
Dumping C stacks can be arbitrarily slow, depending on the DWARF level of the binaries in the call stack.
## Fault handler state[¶](https://docs.python.org/3/library/faulthandler.html#fault-handler-state "Link to this heading")

faulthandler.enable(_file =sys.stderr_, _all_threads =True_, _c_stack =True_)[¶](https://docs.python.org/3/library/faulthandler.html#faulthandler.enable "Link to this definition")

Enable the fault handler: install handlers for the [`SIGSEGV`](https://docs.python.org/3/library/signal.html#signal.SIGSEGV "signal.SIGSEGV"), [`SIGFPE`](https://docs.python.org/3/library/signal.html#signal.SIGFPE "signal.SIGFPE"), [`SIGABRT`](https://docs.python.org/3/library/signal.html#signal.SIGABRT "signal.SIGABRT"), [`SIGBUS`](https://docs.python.org/3/library/signal.html#signal.SIGBUS "signal.SIGBUS") and [`SIGILL`](https://docs.python.org/3/library/signal.html#signal.SIGILL "signal.SIGILL") signals to dump the Python traceback. If _all_threads_ is `True`, produce tracebacks for every running thread. Otherwise, dump only the current thread.
The _file_ must be kept open until the fault handler is disabled: see [issue with file descriptors](https://docs.python.org/3/library/faulthandler.html#faulthandler-fd).
If _c_stack_ is `True`, then the C stack trace is printed after the Python traceback, unless the system does not support it. See [`dump_c_stack()`](https://docs.python.org/3/library/faulthandler.html#faulthandler.dump_c_stack "faulthandler.dump_c_stack") for more information on compatibility.
Changed in version 3.5: Added support for passing file descriptor to this function.
Changed in version 3.6: On Windows, a handler for Windows exception is also installed.
Changed in version 3.10: The dump now mentions if a garbage collector collection is running if _all_threads_ is true.
Changed in version 3.14: Only the current thread is dumped if the [GIL](https://docs.python.org/3/glossary.html#term-GIL) is disabled to prevent the risk of data races.
Changed in version 3.14: The dump now displays the C stack trace if _c_stack_ is true.

faulthandler.disable()[¶](https://docs.python.org/3/library/faulthandler.html#faulthandler.disable "Link to this definition")

Disable the fault handler: uninstall the signal handlers installed by [`enable()`](https://docs.python.org/3/library/faulthandler.html#faulthandler.enable "faulthandler.enable").

faulthandler.is_enabled()[¶](https://docs.python.org/3/library/faulthandler.html#faulthandler.is_enabled "Link to this definition")

Check if the fault handler is enabled.
## Dumping the tracebacks after a timeout[¶](https://docs.python.org/3/library/faulthandler.html#dumping-the-tracebacks-after-a-timeout "Link to this heading")

faulthandler.dump_traceback_later(_timeout_ , _repeat =False_, _file =sys.stderr_, _exit =False_)[¶](https://docs.python.org/3/library/faulthandler.html#faulthandler.dump_traceback_later "Link to this definition")

Dump the tracebacks of all threads, after a timeout of _timeout_ seconds, or every _timeout_ seconds if _repeat_ is `True`. If _exit_ is `True`, call `_exit()` with status=1 after dumping the tracebacks. (Note `_exit()` exits the process immediately, which means it doesn’t do any cleanup like flushing file buffers.) If the function is called twice, the new call replaces previous parameters and resets the timeout. The timer has a sub-second resolution.
The _file_ must be kept open until the traceback is dumped or [`cancel_dump_traceback_later()`](https://docs.python.org/3/library/faulthandler.html#faulthandler.cancel_dump_traceback_later "faulthandler.cancel_dump_traceback_later") is called: see [issue with file descriptors](https://docs.python.org/3/library/faulthandler.html#faulthandler-fd).
This function is implemented using a watchdog thread.
Changed in version 3.5: Added support for passing file descriptor to this function.
Changed in version 3.7: This function is now always available.

faulthandler.cancel_dump_traceback_later()[¶](https://docs.python.org/3/library/faulthandler.html#faulthandler.cancel_dump_traceback_later "Link to this definition")

Cancel the last call to [`dump_traceback_later()`](https://docs.python.org/3/library/faulthandler.html#faulthandler.dump_traceback_later "faulthandler.dump_traceback_later").
## Dumping the traceback on a user signal[¶](https://docs.python.org/3/library/faulthandler.html#dumping-the-traceback-on-a-user-signal "Link to this heading")

faulthandler.register(_signum_ , _file =sys.stderr_, _all_threads =True_, _chain =False_)[¶](https://docs.python.org/3/library/faulthandler.html#faulthandler.register "Link to this definition")

Register a user signal: install a handler for the _signum_ signal to dump the traceback of all threads, or of the current thread if _all_threads_ is `False`, into _file_. Call the previous handler if chain is `True`.
The _file_ must be kept open until the signal is unregistered by [`unregister()`](https://docs.python.org/3/library/faulthandler.html#faulthandler.unregister "faulthandler.unregister"): see [issue with file descriptors](https://docs.python.org/3/library/faulthandler.html#faulthandler-fd).
Not available on Windows.
Changed in version 3.5: Added support for passing file descriptor to this function.

faulthandler.unregister(_signum_)[¶](https://docs.python.org/3/library/faulthandler.html#faulthandler.unregister "Link to this definition")

Unregister a user signal: uninstall the handler of the _signum_ signal installed by [`register()`](https://docs.python.org/3/library/faulthandler.html#faulthandler.register "faulthandler.register"). Return `True` if the signal was registered, `False` otherwise.
Not available on Windows.
## Issue with file descriptors[¶](https://docs.python.org/3/library/faulthandler.html#issue-with-file-descriptors "Link to this heading")
[`enable()`](https://docs.python.org/3/library/faulthandler.html#faulthandler.enable "faulthandler.enable"), [`dump_traceback_later()`](https://docs.python.org/3/library/faulthandler.html#faulthandler.dump_traceback_later "faulthandler.dump_traceback_later") and [`register()`](https://docs.python.org/3/library/faulthandler.html#faulthandler.register "faulthandler.register") keep the file descriptor of their _file_ argument. If the file is closed and its file descriptor is reused by a new file, or if [`os.dup2()`](https://docs.python.org/3/library/os.html#os.dup2 "os.dup2") is used to replace the file descriptor, the traceback will be written into a different file. Call these functions again each time that the file is replaced.
## Example[¶](https://docs.python.org/3/library/faulthandler.html#example "Link to this heading")
Example of a segmentation fault on Linux with and without enabling the fault handler:
Copy```
$ python -c "import ctypes; ctypes.string_at(0)"
Segmentation fault

$ python -q -X faulthandler
>>> import ctypes
>>> ctypes.string_at(0)
Fatal Python error: Segmentation fault

Current thread 0x00007fb899f39700 (most recent call first):
  File "/opt/python/Lib/ctypes/__init__.py", line 486 in string_at
  File "<stdin>", line 1 in <module>

Current thread's C stack trace (most recent call first):
  Binary file "/opt/python/python", at _Py_DumpStack+0x42 [0x5b27f7d7147e]
  Binary file "/opt/python/python", at +0x32dcbd [0x5b27f7d85cbd]
  Binary file "/opt/python/python", at +0x32df8a [0x5b27f7d85f8a]
  Binary file "/usr/lib/libc.so.6", at +0x3def0 [0x77b73226bef0]
  Binary file "/usr/lib/libc.so.6", at +0x17ef9c [0x77b7323acf9c]
  Binary file "/opt/python/build/lib.linux-x86_64-3.14/_ctypes.cpython-314d-x86_64-linux-gnu.so", at +0xcdf6 [0x77b7315dddf6]
  Binary file "/usr/lib/libffi.so.8", at +0x7976 [0x77b73158f976]
  Binary file "/usr/lib/libffi.so.8", at +0x413c [0x77b73158c13c]
  Binary file "/usr/lib/libffi.so.8", at ffi_call+0x12e [0x77b73158ef0e]
  Binary file "/opt/python/build/lib.linux-x86_64-3.14/_ctypes.cpython-314d-x86_64-linux-gnu.so", at +0x15a33 [0x77b7315e6a33]
  Binary file "/opt/python/build/lib.linux-x86_64-3.14/_ctypes.cpython-314d-x86_64-linux-gnu.so", at +0x164fa [0x77b7315e74fa]
  Binary file "/opt/python/build/lib.linux-x86_64-3.14/_ctypes.cpython-314d-x86_64-linux-gnu.so", at +0xc624 [0x77b7315dd624]
  Binary file "/opt/python/python", at _PyObject_MakeTpCall+0xce [0x5b27f7b73883]
  Binary file "/opt/python/python", at +0x11bab6 [0x5b27f7b73ab6]
  Binary file "/opt/python/python", at PyObject_Vectorcall+0x23 [0x5b27f7b73b04]
  Binary file "/opt/python/python", at _PyEval_EvalFrameDefault+0x490c [0x5b27f7cbb302]
  Binary file "/opt/python/python", at +0x2818e6 [0x5b27f7cd98e6]
  Binary file "/opt/python/python", at +0x281aab [0x5b27f7cd9aab]
  Binary file "/opt/python/python", at PyEval_EvalCode+0xc5 [0x5b27f7cd9ba3]
  Binary file "/opt/python/python", at +0x255957 [0x5b27f7cad957]
  Binary file "/opt/python/python", at +0x255ab4 [0x5b27f7cadab4]
  Binary file "/opt/python/python", at _PyEval_EvalFrameDefault+0x6c3e [0x5b27f7cbd634]
  Binary file "/opt/python/python", at +0x2818e6 [0x5b27f7cd98e6]
  Binary file "/opt/python/python", at +0x281aab [0x5b27f7cd9aab]
  Binary file "/opt/python/python", at +0x11b6e1 [0x5b27f7b736e1]
  Binary file "/opt/python/python", at +0x11d348 [0x5b27f7b75348]
  Binary file "/opt/python/python", at +0x11d626 [0x5b27f7b75626]
  Binary file "/opt/python/python", at PyObject_Call+0x20 [0x5b27f7b7565e]
  Binary file "/opt/python/python", at +0x32a67a [0x5b27f7d8267a]
  Binary file "/opt/python/python", at +0x32a7f8 [0x5b27f7d827f8]
  Binary file "/opt/python/python", at +0x32ac1b [0x5b27f7d82c1b]
  Binary file "/opt/python/python", at Py_RunMain+0x31 [0x5b27f7d82ebe]
  <truncated rest of calls>
Segmentation fault

```

### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`faulthandler` — Dump the Python traceback](https://docs.python.org/3/library/faulthandler.html)
    * [Dumping the traceback](https://docs.python.org/3/library/faulthandler.html#dumping-the-traceback)
    * [Dumping the C stack](https://docs.python.org/3/library/faulthandler.html#dumping-the-c-stack)
      * [C Stack Compatibility](https://docs.python.org/3/library/faulthandler.html#c-stack-compatibility)
    * [Fault handler state](https://docs.python.org/3/library/faulthandler.html#fault-handler-state)
    * [Dumping the tracebacks after a timeout](https://docs.python.org/3/library/faulthandler.html#dumping-the-tracebacks-after-a-timeout)
    * [Dumping the traceback on a user signal](https://docs.python.org/3/library/faulthandler.html#dumping-the-traceback-on-a-user-signal)
    * [Issue with file descriptors](https://docs.python.org/3/library/faulthandler.html#issue-with-file-descriptors)
    * [Example](https://docs.python.org/3/library/faulthandler.html#example)


#### Previous topic
[`bdb` — Debugger framework](https://docs.python.org/3/library/bdb.html "previous chapter")
#### Next topic
[`pdb` — The Python Debugger](https://docs.python.org/3/library/pdb.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=faulthandler+%E2%80%94+Dump+the+Python+traceback&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ffaulthandler.html&pagesource=library%2Ffaulthandler.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/pdb.html "pdb — The Python Debugger") |
  * [previous](https://docs.python.org/3/library/bdb.html "bdb — Debugger framework") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Debugging and Profiling](https://docs.python.org/3/library/debug.html) »
  * [`faulthandler` — Dump the Python traceback](https://docs.python.org/3/library/faulthandler.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
