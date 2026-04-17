A program is free to modify this list for its own purposes. Only strings should be added to [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path"); all other data types are ignored during import.
See also
  * Module [`site`](https://docs.python.org/3/library/site.html#module-site "site: Module responsible for site-specific configuration.") This describes how to use .pth files to extend [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path").



sys.path_hooks[¶](https://docs.python.org/3/library/sys.html#sys.path_hooks "Link to this definition")

A list of callables that take a path argument to try to create a [finder](https://docs.python.org/3/glossary.html#term-finder) for the path. If a finder can be created, it is to be returned by the callable, else raise [`ImportError`](https://docs.python.org/3/library/exceptions.html#ImportError "ImportError").
Originally specified in [**PEP 302**](https://peps.python.org/pep-0302/).

sys.path_importer_cache[¶](https://docs.python.org/3/library/sys.html#sys.path_importer_cache "Link to this definition")

A dictionary acting as a cache for [finder](https://docs.python.org/3/glossary.html#term-finder) objects. The keys are paths that have been passed to [`sys.path_hooks`](https://docs.python.org/3/library/sys.html#sys.path_hooks "sys.path_hooks") and the values are the finders that are found. If a path is a valid file system path but no finder is found on `sys.path_hooks` then `None` is stored.
Originally specified in [**PEP 302**](https://peps.python.org/pep-0302/).

sys.platform[¶](https://docs.python.org/3/library/sys.html#sys.platform "Link to this definition")

A string containing a platform identifier. Known values are:
System | `platform` value
---|---
AIX | `'aix'`
Android | `'android'`
Emscripten | `'emscripten'`
FreeBSD | `'freebsd'`
iOS | `'ios'`
Linux | `'linux'`
macOS | `'darwin'`
Windows | `'win32'`
Windows/Cygwin | `'cygwin'`
WASI | `'wasi'`
On Unix systems not listed in the table, the value is the lowercased OS name as returned by `uname -s`, with the first part of the version as returned by `uname -r` appended, e.g. `'sunos5'`, _at the time when Python was built_. Unless you want to test for a specific system version, it is therefore recommended to use the following idiom:
Copy```
if sys.platform.startswith('sunos'):
    # SunOS-specific code here...

```

Changed in version 3.3: On Linux, [`sys.platform`](https://docs.python.org/3/library/sys.html#sys.platform "sys.platform") doesn’t contain the major version anymore. It is always `'linux'`, instead of `'linux2'` or `'linux3'`.
Changed in version 3.8: On AIX, [`sys.platform`](https://docs.python.org/3/library/sys.html#sys.platform "sys.platform") doesn’t contain the major version anymore. It is always `'aix'`, instead of `'aix5'` or `'aix7'`.
Changed in version 3.13: On Android, [`sys.platform`](https://docs.python.org/3/library/sys.html#sys.platform "sys.platform") now returns `'android'` rather than `'linux'`.
Changed in version 3.14: On FreeBSD, [`sys.platform`](https://docs.python.org/3/library/sys.html#sys.platform "sys.platform") doesn’t contain the major version anymore. It is always `'freebsd'`, instead of `'freebsd13'` or `'freebsd14'`.
See also
[`os.name`](https://docs.python.org/3/library/os.html#os.name "os.name") has a coarser granularity. [`os.uname()`](https://docs.python.org/3/library/os.html#os.uname "os.uname") gives system-dependent version information.
The [`platform`](https://docs.python.org/3/library/platform.html#module-platform "platform: Retrieves as much platform identifying data as possible.") module provides detailed checks for the system’s identity.

sys.platlibdir[¶](https://docs.python.org/3/library/sys.html#sys.platlibdir "Link to this definition")

Name of the platform-specific library directory. It is used to build the path of standard library and the paths of installed extension modules.
It is equal to `"lib"` on most platforms. On Fedora and SuSE, it is equal to `"lib64"` on 64-bit platforms which gives the following `sys.path` paths (where `X.Y` is the Python `major.minor` version):
  * `/usr/lib64/pythonX.Y/`: Standard library (like `os.py` of the [`os`](https://docs.python.org/3/library/os.html#module-os "os: Miscellaneous operating system interfaces.") module)
  * `/usr/lib64/pythonX.Y/lib-dynload/`: C extension modules of the standard library (like the [`errno`](https://docs.python.org/3/library/errno.html#module-errno "errno: Standard errno system symbols.") module, the exact filename is platform specific)
  * `/usr/lib/pythonX.Y/site-packages/` (always use `lib`, not [`sys.platlibdir`](https://docs.python.org/3/library/sys.html#sys.platlibdir "sys.platlibdir")): Third-party modules
  * `/usr/lib64/pythonX.Y/site-packages/`: C extension modules of third-party packages


Added in version 3.9.

sys.prefix[¶](https://docs.python.org/3/library/sys.html#sys.prefix "Link to this definition")

A string giving the site-specific directory prefix where the platform independent Python files are installed; on Unix, the default is `/usr/local`. This can be set at build time with the [`--prefix`](https://docs.python.org/3/using/configure.html#cmdoption-prefix) argument to the **configure** script. See [Installation paths](https://docs.python.org/3/library/sysconfig.html#installation-paths) for derived paths.
Note
If a [virtual environment](https://docs.python.org/3/library/venv.html#venv-def) is in effect, this `prefix` will point to the virtual environment. The value for the Python installation will still be available, via [`base_prefix`](https://docs.python.org/3/library/sys.html#sys.base_prefix "sys.base_prefix"). Refer to [Virtual Environments](https://docs.python.org/3/library/sys_path_init.html#sys-path-init-virtual-environments) for more information.
Changed in version 3.14: When running under a [virtual environment](https://docs.python.org/3/library/venv.html#venv-def), `prefix` and [`exec_prefix`](https://docs.python.org/3/library/sys.html#sys.exec_prefix "sys.exec_prefix") are now set to the virtual environment prefix by the [path initialization](https://docs.python.org/3/library/sys_path_init.html#sys-path-init), instead of [`site`](https://docs.python.org/3/library/site.html#module-site "site: Module responsible for site-specific configuration."). This means that `prefix` and `exec_prefix` always point to the virtual environment, even when `site` is disabled ([`-S`](https://docs.python.org/3/using/cmdline.html#cmdoption-S)).

sys.ps1[¶](https://docs.python.org/3/library/sys.html#sys.ps1 "Link to this definition")


sys.ps2[¶](https://docs.python.org/3/library/sys.html#sys.ps2 "Link to this definition")

Strings specifying the primary and secondary prompt of the interpreter. These are only defined if the interpreter is in interactive mode. Their initial values in this case are `'>>> '` and `'... '`. If a non-string object is assigned to either variable, its [`str()`](https://docs.python.org/3/library/stdtypes.html#str "str") is re-evaluated each time the interpreter prepares to read a new interactive command; this can be used to implement a dynamic prompt.

sys.setdlopenflags(_n_)[¶](https://docs.python.org/3/library/sys.html#sys.setdlopenflags "Link to this definition")

Set the flags used by the interpreter for `dlopen()` calls, such as when the interpreter loads extension modules. Among other things, this will enable a lazy resolving of symbols when importing a module, if called as `sys.setdlopenflags(0)`. To share symbols across extension modules, call as `sys.setdlopenflags(os.RTLD_GLOBAL)`. Symbolic names for the flag values can be found in the [`os`](https://docs.python.org/3/library/os.html#module-os "os: Miscellaneous operating system interfaces.") module (`RTLD__xxx_`constants, e.g.[`os.RTLD_LAZY`](https://docs.python.org/3/library/os.html#os.RTLD_LAZY "os.RTLD_LAZY")).
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.

sys.set_int_max_str_digits(_maxdigits_)[¶](https://docs.python.org/3/library/sys.html#sys.set_int_max_str_digits "Link to this definition")

Set the [integer string conversion length limitation](https://docs.python.org/3/library/stdtypes.html#int-max-str-digits) used by this interpreter. See also [`get_int_max_str_digits()`](https://docs.python.org/3/library/sys.html#sys.get_int_max_str_digits "sys.get_int_max_str_digits").
Added in version 3.11.

sys.setprofile(_profilefunc_)[¶](https://docs.python.org/3/library/sys.html#sys.setprofile "Link to this definition")

Set the system’s profile function, which allows you to implement a Python source code profiler in Python. See chapter [The Python Profilers](https://docs.python.org/3/library/profile.html#profile) for more information on the Python profiler. The system’s profile function is called similarly to the system’s trace function (see [`settrace()`](https://docs.python.org/3/library/sys.html#sys.settrace "sys.settrace")), but it is called with different events, for example it isn’t called for each executed line of code (only on call and return, but the return event is reported even when an exception has been set). The function is thread-specific, but there is no way for the profiler to know about context switches between threads, so it does not make sense to use this in the presence of multiple threads. Also, its return value is not used, so it can simply return `None`. Error in the profile function will cause itself unset.
Note
The same tracing mechanism is used for `setprofile()` as [`settrace()`](https://docs.python.org/3/library/sys.html#sys.settrace "sys.settrace"). To trace calls with `setprofile()` inside a tracing function (e.g. in a debugger breakpoint), see [`call_tracing()`](https://docs.python.org/3/library/sys.html#sys.call_tracing "sys.call_tracing").
Profile functions should have three arguments: _frame_ , _event_ , and _arg_. _frame_ is the current stack frame. _event_ is a string: `'call'`, `'return'`, `'c_call'`, `'c_return'`, or `'c_exception'`. _arg_ depends on the event type.
The events have the following meaning:

`'call'`

A function is called (or some other code block entered). The profile function is called; _arg_ is `None`.

`'return'`

A function (or other code block) is about to return. The profile function is called; _arg_ is the value that will be returned, or `None` if the event is caused by an exception being raised.

`'c_call'`

A C function is about to be called. This may be an extension function or a built-in. _arg_ is the C function object.

`'c_return'`

A C function has returned. _arg_ is the C function object.

`'c_exception'`

A C function has raised an exception. _arg_ is the C function object.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `sys.setprofile` with no arguments.

sys.setrecursionlimit(_limit_)[¶](https://docs.python.org/3/library/sys.html#sys.setrecursionlimit "Link to this definition")

Set the maximum depth of the Python interpreter stack to _limit_. This limit prevents infinite recursion from causing an overflow of the C stack and crashing Python.
The highest possible limit is platform-dependent. A user may need to set the limit higher when they have a program that requires deep recursion and a platform that supports a higher limit. This should be done with care, because a too-high limit can lead to a crash.
If the new limit is too low at the current recursion depth, a [`RecursionError`](https://docs.python.org/3/library/exceptions.html#RecursionError "RecursionError") exception is raised.
Changed in version 3.5.1: A [`RecursionError`](https://docs.python.org/3/library/exceptions.html#RecursionError "RecursionError") exception is now raised if the new limit is too low at the current recursion depth.

sys.setswitchinterval(_interval_)[¶](https://docs.python.org/3/library/sys.html#sys.setswitchinterval "Link to this definition")

Set the interpreter’s thread switch interval (in seconds). This floating-point value determines the ideal duration of the “timeslices” allocated to concurrently running Python threads. Please note that the actual value can be higher, especially if long-running internal functions or methods are used. Also, which thread becomes scheduled at the end of the interval is the operating system’s decision. The interpreter doesn’t have its own scheduler.
Added in version 3.2.

sys.settrace(_tracefunc_)[¶](https://docs.python.org/3/library/sys.html#sys.settrace "Link to this definition")

Set the system’s trace function, which allows you to implement a Python source code debugger in Python. The function is thread-specific; for a debugger to support multiple threads, it must register a trace function using `settrace()` for each thread being debugged or use [`threading.settrace()`](https://docs.python.org/3/library/threading.html#threading.settrace "threading.settrace").
Trace functions should have three arguments: _frame_ , _event_ , and _arg_. _frame_ is the [current stack frame](https://docs.python.org/3/reference/datamodel.html#frame-objects). _event_ is a string: `'call'`, `'line'`, `'return'`, `'exception'` or `'opcode'`. _arg_ depends on the event type.
The trace function is invoked (with _event_ set to `'call'`) whenever a new local scope is entered; it should return a reference to a local trace function to be used for the new scope, or `None` if the scope shouldn’t be traced.
The local trace function should return a reference to itself, or to another function which would then be used as the local trace function for the scope.
If there is any error occurred in the trace function, it will be unset, just like `settrace(None)` is called.
Note
Tracing is disabled while calling the trace function (e.g. a function set by `settrace()`). For recursive tracing see [`call_tracing()`](https://docs.python.org/3/library/sys.html#sys.call_tracing "sys.call_tracing").
The events have the following meaning:

`'call'`

A function is called (or some other code block entered). The global trace function is called; _arg_ is `None`; the return value specifies the local trace function.

`'line'`

The interpreter is about to execute a new line of code or re-execute the condition of a loop. The local trace function is called; _arg_ is `None`; the return value specifies the new local trace function. See `Objects/lnotab_notes.txt` for a detailed explanation of how this works. Per-line events may be disabled for a frame by setting [`f_trace_lines`](https://docs.python.org/3/reference/datamodel.html#frame.f_trace_lines "frame.f_trace_lines") to [`False`](https://docs.python.org/3/library/constants.html#False "False") on that [frame](https://docs.python.org/3/reference/datamodel.html#frame-objects).

`'return'`

A function (or other code block) is about to return. The local trace function is called; _arg_ is the value that will be returned, or `None` if the event is caused by an exception being raised. The trace function’s return value is ignored.

`'exception'`

An exception has occurred. The local trace function is called; _arg_ is a tuple `(exception, value, traceback)`; the return value specifies the new local trace function.

`'opcode'`

The interpreter is about to execute a new opcode (see [`dis`](https://docs.python.org/3/library/dis.html#module-dis "dis: Disassembler for Python bytecode.") for opcode details). The local trace function is called; _arg_ is `None`; the return value specifies the new local trace function. Per-opcode events are not emitted by default: they must be explicitly requested by setting [`f_trace_opcodes`](https://docs.python.org/3/reference/datamodel.html#frame.f_trace_opcodes "frame.f_trace_opcodes") to [`True`](https://docs.python.org/3/library/constants.html#True "True") on the [frame](https://docs.python.org/3/reference/datamodel.html#frame-objects).
Note that as an exception is propagated down the chain of callers, an `'exception'` event is generated at each level.
For more fine-grained usage, it’s possible to set a trace function by assigning `frame.f_trace = tracefunc` explicitly, rather than relying on it being set indirectly via the return value from an already installed trace function. This is also required for activating the trace function on the current frame, which `settrace()` doesn’t do. Note that in order for this to work, a global tracing function must have been installed with `settrace()` in order to enable the runtime tracing machinery, but it doesn’t need to be the same tracing function (e.g. it could be a low overhead tracing function that simply returns `None` to disable itself immediately on each frame).
For more information on code and frame objects, refer to [The standard type hierarchy](https://docs.python.org/3/reference/datamodel.html#types).
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `sys.settrace` with no arguments.
**CPython implementation detail:** The `settrace()` function is intended only for implementing debuggers, profilers, coverage tools and the like. Its behavior is part of the implementation platform, rather than part of the language definition, and thus may not be available in all Python implementations.
Changed in version 3.7: `'opcode'` event type added; [`f_trace_lines`](https://docs.python.org/3/reference/datamodel.html#frame.f_trace_lines "frame.f_trace_lines") and [`f_trace_opcodes`](https://docs.python.org/3/reference/datamodel.html#frame.f_trace_opcodes "frame.f_trace_opcodes") attributes added to frames

sys.set_asyncgen_hooks(_[firstiter] [, finalizer]_)[¶](https://docs.python.org/3/library/sys.html#sys.set_asyncgen_hooks "Link to this definition")

Accepts two optional keyword arguments which are callables that accept an [asynchronous generator iterator](https://docs.python.org/3/glossary.html#term-asynchronous-generator-iterator) as an argument. The _firstiter_ callable will be called when an asynchronous generator is iterated for the first time. The _finalizer_ will be called when an asynchronous generator is about to be garbage collected.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `sys.set_asyncgen_hooks_firstiter` with no arguments.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `sys.set_asyncgen_hooks_finalizer` with no arguments.
Two auditing events are raised because the underlying API consists of two calls, each of which must raise its own event.
Added in version 3.6: See [**PEP 525**](https://peps.python.org/pep-0525/) for more details, and for a reference example of a _finalizer_ method see the implementation of `asyncio.Loop.shutdown_asyncgens` in
Note
This function has been added on a provisional basis (see [**PEP 411**](https://peps.python.org/pep-0411/) for details.)

sys.set_coroutine_origin_tracking_depth(_depth_)[¶](https://docs.python.org/3/library/sys.html#sys.set_coroutine_origin_tracking_depth "Link to this definition")

Allows enabling or disabling coroutine origin tracking. When enabled, the `cr_origin` attribute on coroutine objects will contain a tuple of (filename, line number, function name) tuples describing the traceback where the coroutine object was created, with the most recent call first. When disabled, `cr_origin` will be `None`.
To enable, pass a _depth_ value greater than zero; this sets the number of frames whose information will be captured. To disable, set _depth_ to zero.
This setting is thread-specific.
Added in version 3.7.
Note
This function has been added on a provisional basis (see [**PEP 411**](https://peps.python.org/pep-0411/) for details.) Use it only for debugging purposes.

sys.activate_stack_trampoline(_backend_ , _/_)[¶](https://docs.python.org/3/library/sys.html#sys.activate_stack_trampoline "Link to this definition")

Activate the stack profiler trampoline _backend_. The only supported backend is `"perf"`.
Stack trampolines cannot be activated if the JIT is active.
[Availability](https://docs.python.org/3/library/intro.html#availability): Linux.
Added in version 3.12.
See also
  * [Python support for the Linux perf profiler](https://docs.python.org/3/howto/perf_profiling.html#perf-profiling)



sys.deactivate_stack_trampoline()[¶](https://docs.python.org/3/library/sys.html#sys.deactivate_stack_trampoline "Link to this definition")

Deactivate the current stack profiler trampoline backend.
If no stack profiler is activated, this function has no effect.
[Availability](https://docs.python.org/3/library/intro.html#availability): Linux.
Added in version 3.12.

sys.is_stack_trampoline_active()[¶](https://docs.python.org/3/library/sys.html#sys.is_stack_trampoline_active "Link to this definition")

Return `True` if a stack profiler trampoline is active.
[Availability](https://docs.python.org/3/library/intro.html#availability): Linux.
Added in version 3.12.

sys.remote_exec(_pid_ , _script_)[¶](https://docs.python.org/3/library/sys.html#sys.remote_exec "Link to this definition")

Executes _script_ , a file containing Python code in the remote process with the given _pid_.
This function returns immediately, and the code will be executed by the target process’s main thread at the next available opportunity, similarly to how signals are handled. There is no interface to determine when the code has been executed. The caller is responsible for making sure that the file still exists whenever the remote process tries to read it and that it hasn’t been overwritten.
The remote process must be running a CPython interpreter of the same major and minor version as the local process. If either the local or remote interpreter is pre-release (alpha, beta, or release candidate) then the local and remote interpreters must be the same exact version.
See [Remote debugging attachment protocol](https://docs.python.org/3/howto/remote_debugging.html#remote-debugging) for more information about the remote debugging mechanism.
When the code is executed in the remote process, an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `sys.remote_exec` is raised with the _pid_ and the path to the script file. This event is raised in the process that called [`sys.remote_exec()`](https://docs.python.org/3/library/sys.html#sys.remote_exec "sys.remote_exec").
When the script is executed in the remote process, an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `cpython.remote_debugger_script` is raised with the path in the remote process. This event is raised in the remote process, not the one that called [`sys.remote_exec()`](https://docs.python.org/3/library/sys.html#sys.remote_exec "sys.remote_exec").
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, Windows.
Added in version 3.14: See [**PEP 768**](https://peps.python.org/pep-0768/) for more details.

sys._enablelegacywindowsfsencoding()[¶](https://docs.python.org/3/library/sys.html#sys._enablelegacywindowsfsencoding "Link to this definition")

Changes the [filesystem encoding and error handler](https://docs.python.org/3/glossary.html#term-filesystem-encoding-and-error-handler) to ‘mbcs’ and ‘replace’ respectively, for consistency with versions of Python prior to 3.6.
This is equivalent to defining the [`PYTHONLEGACYWINDOWSFSENCODING`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONLEGACYWINDOWSFSENCODING) environment variable before launching Python.
See also [`sys.getfilesystemencoding()`](https://docs.python.org/3/library/sys.html#sys.getfilesystemencoding "sys.getfilesystemencoding") and [`sys.getfilesystemencodeerrors()`](https://docs.python.org/3/library/sys.html#sys.getfilesystemencodeerrors "sys.getfilesystemencodeerrors").
[Availability](https://docs.python.org/3/library/intro.html#availability): Windows.
Note
Changing the filesystem encoding after Python startup is risky because the old fsencoding or paths encoded by the old fsencoding may be cached somewhere. Use [`PYTHONLEGACYWINDOWSFSENCODING`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONLEGACYWINDOWSFSENCODING) instead.
Added in version 3.6: See [**PEP 529**](https://peps.python.org/pep-0529/) for more details.
Deprecated since version 3.13, will be removed in version 3.16: Use [`PYTHONLEGACYWINDOWSFSENCODING`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONLEGACYWINDOWSFSENCODING) instead.

sys.stdin[¶](https://docs.python.org/3/library/sys.html#sys.stdin "Link to this definition")


sys.stdout[¶](https://docs.python.org/3/library/sys.html#sys.stdout "Link to this definition")


sys.stderr[¶](https://docs.python.org/3/library/sys.html#sys.stderr "Link to this definition")

[File objects](https://docs.python.org/3/glossary.html#term-file-object) used by the interpreter for standard input, output and errors:
  * `stdin` is used for all interactive input (including calls to [`input()`](https://docs.python.org/3/library/functions.html#input "input"));
  * `stdout` is used for the output of [`print()`](https://docs.python.org/3/library/functions.html#print "print") and [expression](https://docs.python.org/3/glossary.html#term-expression) statements and for the prompts of [`input()`](https://docs.python.org/3/library/functions.html#input "input");
  * The interpreter’s own prompts and its error messages go to `stderr`.


These streams are regular [text files](https://docs.python.org/3/glossary.html#term-text-file) like those returned by the [`open()`](https://docs.python.org/3/library/functions.html#open "open") function. Their parameters are chosen as follows:
