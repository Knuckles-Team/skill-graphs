#  `sys` — System-specific parameters and functions[¶](https://docs.python.org/3/library/sys.html#module-sys "Link to this heading")
* * *
This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. It is always available. Unless explicitly noted otherwise, all variables are read-only.

sys.abiflags[¶](https://docs.python.org/3/library/sys.html#sys.abiflags "Link to this definition")

On POSIX systems where Python was built with the standard `configure` script, this contains the ABI flags as specified by [**PEP 3149**](https://peps.python.org/pep-3149/).
Added in version 3.2.
Changed in version 3.8: Default flags became an empty string (`m` flag for pymalloc has been removed).
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.

sys.addaudithook(_hook_)[¶](https://docs.python.org/3/library/sys.html#sys.addaudithook "Link to this definition")

Append the callable _hook_ to the list of active auditing hooks for the current (sub)interpreter.
When an auditing event is raised through the [`sys.audit()`](https://docs.python.org/3/library/sys.html#sys.audit "sys.audit") function, each hook will be called in the order it was added with the event name and the tuple of arguments. Native hooks added by [`PySys_AddAuditHook()`](https://docs.python.org/3/c-api/sys.html#c.PySys_AddAuditHook "PySys_AddAuditHook") are called first, followed by hooks added in the current (sub)interpreter. Hooks can then log the event, raise an exception to abort the operation, or terminate the process entirely.
Note that audit hooks are primarily for collecting information about internal or otherwise unobservable actions, whether by Python or libraries written in Python. They are not suitable for implementing a “sandbox”. In particular, malicious code can trivially disable or bypass hooks added using this function. At a minimum, any security-sensitive hooks must be added using the C API [`PySys_AddAuditHook()`](https://docs.python.org/3/c-api/sys.html#c.PySys_AddAuditHook "PySys_AddAuditHook") before initialising the runtime, and any modules allowing arbitrary memory modification (such as [`ctypes`](https://docs.python.org/3/library/ctypes.html#module-ctypes "ctypes: A foreign function library for Python.")) should be completely removed or closely monitored.
Calling [`sys.addaudithook()`](https://docs.python.org/3/library/sys.html#sys.addaudithook "sys.addaudithook") will itself raise an auditing event named `sys.addaudithook` with no arguments. If any existing hooks raise an exception derived from [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError"), the new hook will not be added and the exception suppressed. As a result, callers cannot assume that their hook has been added unless they control all existing hooks.
See the [audit events table](https://docs.python.org/3/library/audit_events.html#audit-events) for all events raised by CPython, and [**PEP 578**](https://peps.python.org/pep-0578/) for the original design discussion.
Added in version 3.8.
Changed in version 3.8.1: Exceptions derived from [`Exception`](https://docs.python.org/3/library/exceptions.html#Exception "Exception") but not [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError") are no longer suppressed.
**CPython implementation detail:** When tracing is enabled (see [`settrace()`](https://docs.python.org/3/library/sys.html#sys.settrace "sys.settrace")), Python hooks are only traced if the callable has a `__cantrace__` member that is set to a true value. Otherwise, trace functions will skip the hook.

sys.argv[¶](https://docs.python.org/3/library/sys.html#sys.argv "Link to this definition")

The list of command line arguments passed to a Python script. `argv[0]` is the script name (it is operating system dependent whether this is a full pathname or not). If the command was executed using the [`-c`](https://docs.python.org/3/using/cmdline.html#cmdoption-c) command line option to the interpreter, `argv[0]` is set to the string `'-c'`. If no script name was passed to the Python interpreter, `argv[0]` is the empty string.
To loop over the standard input, or the list of files given on the command line, see the [`fileinput`](https://docs.python.org/3/library/fileinput.html#module-fileinput "fileinput: Loop over standard input or a list of files.") module.
See also [`sys.orig_argv`](https://docs.python.org/3/library/sys.html#sys.orig_argv "sys.orig_argv").
Note
On Unix, command line arguments are passed by bytes from OS. Python decodes them with filesystem encoding and “surrogateescape” error handler. When you need original bytes, you can get it by `[os.fsencode(arg) for arg in sys.argv]`.

sys.audit(_event_ , _* args_)[¶](https://docs.python.org/3/library/sys.html#sys.audit "Link to this definition")

Raise an auditing event and trigger any active auditing hooks. _event_ is a string identifying the event, and _args_ may contain optional arguments with more information about the event. The number and types of arguments for a given event are considered a public and stable API and should not be modified between releases.
For example, one auditing event is named `os.chdir`. This event has one argument called _path_ that will contain the requested new working directory.
[`sys.audit()`](https://docs.python.org/3/library/sys.html#sys.audit "sys.audit") will call the existing auditing hooks, passing the event name and arguments, and will re-raise the first exception from any hook. In general, if an exception is raised, it should not be handled and the process should be terminated as quickly as possible. This allows hook implementations to decide how to respond to particular events: they can merely log the event or abort the operation by raising an exception.
Hooks are added using the [`sys.addaudithook()`](https://docs.python.org/3/library/sys.html#sys.addaudithook "sys.addaudithook") or [`PySys_AddAuditHook()`](https://docs.python.org/3/c-api/sys.html#c.PySys_AddAuditHook "PySys_AddAuditHook") functions.
The native equivalent of this function is [`PySys_Audit()`](https://docs.python.org/3/c-api/sys.html#c.PySys_Audit "PySys_Audit"). Using the native function is preferred when possible.
See the [audit events table](https://docs.python.org/3/library/audit_events.html#audit-events) for all events raised by CPython.
Added in version 3.8.

sys.base_exec_prefix[¶](https://docs.python.org/3/library/sys.html#sys.base_exec_prefix "Link to this definition")

Equivalent to [`exec_prefix`](https://docs.python.org/3/library/sys.html#sys.exec_prefix "sys.exec_prefix"), but referring to the base Python installation.
When running under [Virtual Environments](https://docs.python.org/3/library/sys_path_init.html#sys-path-init-virtual-environments), [`exec_prefix`](https://docs.python.org/3/library/sys.html#sys.exec_prefix "sys.exec_prefix") gets overwritten to the virtual environment prefix. `base_exec_prefix`, conversely, does not change, and always points to the base Python installation. Refer to sys-path-init-virtual-environments for more information.
Added in version 3.3.

sys.base_prefix[¶](https://docs.python.org/3/library/sys.html#sys.base_prefix "Link to this definition")

Equivalent to [`prefix`](https://docs.python.org/3/library/sys.html#sys.prefix "sys.prefix"), but referring to the base Python installation.
When running under [virtual environment](https://docs.python.org/3/library/venv.html#venv-def), [`prefix`](https://docs.python.org/3/library/sys.html#sys.prefix "sys.prefix") gets overwritten to the virtual environment prefix. `base_prefix`, conversely, does not change, and always points to the base Python installation. Refer to [Virtual Environments](https://docs.python.org/3/library/sys_path_init.html#sys-path-init-virtual-environments) for more information.
Added in version 3.3.

sys.byteorder[¶](https://docs.python.org/3/library/sys.html#sys.byteorder "Link to this definition")

An indicator of the native byte order. This will have the value `'big'` on big-endian (most-significant byte first) platforms, and `'little'` on little-endian (least-significant byte first) platforms.

sys.builtin_module_names[¶](https://docs.python.org/3/library/sys.html#sys.builtin_module_names "Link to this definition")

A tuple of strings containing the names of all modules that are compiled into this Python interpreter. (This information is not available in any other way — `modules.keys()` only lists the imported modules.)
See also the [`sys.stdlib_module_names`](https://docs.python.org/3/library/sys.html#sys.stdlib_module_names "sys.stdlib_module_names") list.

sys.call_tracing(_func_ , _args_)[¶](https://docs.python.org/3/library/sys.html#sys.call_tracing "Link to this definition")

Call `func(*args)`, while tracing is enabled. The tracing state is saved, and restored afterwards. This is intended to be called from a debugger from a checkpoint, to recursively debug or profile some other code.
Tracing is suspended while calling a tracing function set by [`settrace()`](https://docs.python.org/3/library/sys.html#sys.settrace "sys.settrace") or [`setprofile()`](https://docs.python.org/3/library/sys.html#sys.setprofile "sys.setprofile") to avoid infinite recursion. `call_tracing()` enables explicit recursion of the tracing function.

sys.copyright[¶](https://docs.python.org/3/library/sys.html#sys.copyright "Link to this definition")

A string containing the copyright pertaining to the Python interpreter.

sys._clear_type_cache()[¶](https://docs.python.org/3/library/sys.html#sys._clear_type_cache "Link to this definition")

Clear the internal type cache. The type cache is used to speed up attribute and method lookups. Use the function _only_ to drop unnecessary references during reference leak debugging.
This function should be used for internal and specialized purposes only.
Deprecated since version 3.13: Use the more general [`_clear_internal_caches()`](https://docs.python.org/3/library/sys.html#sys._clear_internal_caches "sys._clear_internal_caches") function instead.

sys._clear_internal_caches()[¶](https://docs.python.org/3/library/sys.html#sys._clear_internal_caches "Link to this definition")

Clear all internal performance-related caches. Use this function _only_ to release unnecessary references and memory blocks when hunting for leaks.
Added in version 3.13.

sys._current_frames()[¶](https://docs.python.org/3/library/sys.html#sys._current_frames "Link to this definition")

Return a dictionary mapping each thread’s identifier to the topmost stack frame currently active in that thread at the time the function is called. Note that functions in the [`traceback`](https://docs.python.org/3/library/traceback.html#module-traceback "traceback: Print or retrieve a stack traceback.") module can build the call stack given such a frame.
This is most useful for debugging deadlock: this function does not require the deadlocked threads’ cooperation, and such threads’ call stacks are frozen for as long as they remain deadlocked. The frame returned for a non-deadlocked thread may bear no relationship to that thread’s current activity by the time calling code examines the frame.
This function should be used for internal and specialized purposes only.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `sys._current_frames` with no arguments.

sys._current_exceptions()[¶](https://docs.python.org/3/library/sys.html#sys._current_exceptions "Link to this definition")

Return a dictionary mapping each thread’s identifier to the topmost exception currently active in that thread at the time the function is called. If a thread is not currently handling an exception, it is not included in the result dictionary.
This is most useful for statistical profiling.
This function should be used for internal and specialized purposes only.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `sys._current_exceptions` with no arguments.
Changed in version 3.12: Each value in the dictionary is now a single exception instance, rather than a 3-tuple as returned from `sys.exc_info()`.

sys.breakpointhook()[¶](https://docs.python.org/3/library/sys.html#sys.breakpointhook "Link to this definition")

This hook function is called by built-in [`breakpoint()`](https://docs.python.org/3/library/functions.html#breakpoint "breakpoint"). By default, it drops you into the [`pdb`](https://docs.python.org/3/library/pdb.html#module-pdb "pdb: The Python debugger for interactive interpreters.") debugger, but it can be set to any other function so that you can choose which debugger gets used.
The signature of this function is dependent on what it calls. For example, the default binding (e.g. `pdb.set_trace()`) expects no arguments, but you might bind it to a function that expects additional arguments (positional and/or keyword). The built-in `breakpoint()` function passes its `*args` and `**kws` straight through. Whatever `breakpointhooks()` returns is returned from `breakpoint()`.
The default implementation first consults the environment variable [`PYTHONBREAKPOINT`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONBREAKPOINT). If that is set to `"0"` then this function returns immediately; i.e. it is a no-op. If the environment variable is not set, or is set to the empty string, `pdb.set_trace()` is called. Otherwise this variable should name a function to run, using Python’s dotted-import nomenclature, e.g. `package.subpackage.module.function`. In this case, `package.subpackage.module` would be imported and the resulting module must have a callable named `function()`. This is run, passing in `*args` and `**kws`, and whatever `function()` returns, `sys.breakpointhook()` returns to the built-in [`breakpoint()`](https://docs.python.org/3/library/functions.html#breakpoint "breakpoint") function.
Note that if anything goes wrong while importing the callable named by [`PYTHONBREAKPOINT`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONBREAKPOINT), a [`RuntimeWarning`](https://docs.python.org/3/library/exceptions.html#RuntimeWarning "RuntimeWarning") is reported and the breakpoint is ignored.
Also note that if `sys.breakpointhook()` is overridden programmatically, [`PYTHONBREAKPOINT`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONBREAKPOINT) is _not_ consulted.
Added in version 3.7.

sys._debugmallocstats()[¶](https://docs.python.org/3/library/sys.html#sys._debugmallocstats "Link to this definition")

Print low-level information to stderr about the state of CPython’s memory allocator.
If Python is [built in debug mode](https://docs.python.org/3/using/configure.html#debug-build) ([`configure --with-pydebug option`](https://docs.python.org/3/using/configure.html#cmdoption-with-pydebug)), it also performs some expensive internal consistency checks.
Added in version 3.3.
**CPython implementation detail:** This function is specific to CPython. The exact output format is not defined here, and may change.

sys.dllhandle[¶](https://docs.python.org/3/library/sys.html#sys.dllhandle "Link to this definition")

Integer specifying the handle of the Python DLL.
[Availability](https://docs.python.org/3/library/intro.html#availability): Windows.

sys.displayhook(_value_)[¶](https://docs.python.org/3/library/sys.html#sys.displayhook "Link to this definition")

If _value_ is not `None`, this function prints `repr(value)` to `sys.stdout`, and saves _value_ in `builtins._`. If `repr(value)` is not encodable to `sys.stdout.encoding` with `sys.stdout.errors` error handler (which is probably `'strict'`), encode it to `sys.stdout.encoding` with `'backslashreplace'` error handler.
`sys.displayhook` is called on the result of evaluating an [expression](https://docs.python.org/3/glossary.html#term-expression) entered in an interactive Python session. The display of these values can be customized by assigning another one-argument function to `sys.displayhook`.
Pseudo-code:
Copy```
def displayhook(value):
    if value is None:
        return
    # Set '_' to None to avoid recursion
    builtins._ = None
    text = repr(value)
    try:
        sys.stdout.write(text)
    except UnicodeEncodeError:
        bytes = text.encode(sys.stdout.encoding, 'backslashreplace')
        if hasattr(sys.stdout, 'buffer'):
            sys.stdout.buffer.write(bytes)
        else:
            text = bytes.decode(sys.stdout.encoding, 'strict')
            sys.stdout.write(text)
    sys.stdout.write("\n")
    builtins._ = value

```

Changed in version 3.2: Use `'backslashreplace'` error handler on [`UnicodeEncodeError`](https://docs.python.org/3/library/exceptions.html#UnicodeEncodeError "UnicodeEncodeError").

sys.dont_write_bytecode[¶](https://docs.python.org/3/library/sys.html#sys.dont_write_bytecode "Link to this definition")

If this is true, Python won’t try to write `.pyc` files on the import of source modules. This value is initially set to `True` or `False` depending on the [`-B`](https://docs.python.org/3/using/cmdline.html#cmdoption-B) command line option and the [`PYTHONDONTWRITEBYTECODE`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONDONTWRITEBYTECODE) environment variable, but you can set it yourself to control bytecode file generation.

sys._emscripten_info[¶](https://docs.python.org/3/library/sys.html#sys._emscripten_info "Link to this definition")

A [named tuple](https://docs.python.org/3/glossary.html#term-named-tuple) holding information about the environment on the _wasm32-emscripten_ platform. The named tuple is provisional and may change in the future.

_emscripten_info.emscripten_version[¶](https://docs.python.org/3/library/sys.html#sys._emscripten_info.emscripten_version "Link to this definition")

Emscripten version as tuple of ints (major, minor, micro), e.g. `(3, 1, 8)`.

_emscripten_info.runtime[¶](https://docs.python.org/3/library/sys.html#sys._emscripten_info.runtime "Link to this definition")

Runtime string, e.g. browser user agent, `'Node.js v14.18.2'`, or `'UNKNOWN'`.

_emscripten_info.pthreads[¶](https://docs.python.org/3/library/sys.html#sys._emscripten_info.pthreads "Link to this definition")

`True` if Python is compiled with Emscripten pthreads support.

_emscripten_info.shared_memory[¶](https://docs.python.org/3/library/sys.html#sys._emscripten_info.shared_memory "Link to this definition")

`True` if Python is compiled with shared memory support.
[Availability](https://docs.python.org/3/library/intro.html#availability): Emscripten.
Added in version 3.11.

sys.pycache_prefix[¶](https://docs.python.org/3/library/sys.html#sys.pycache_prefix "Link to this definition")

If this is set (not `None`), Python will write bytecode-cache `.pyc` files to (and read them from) a parallel directory tree rooted at this directory, rather than from `__pycache__` directories in the source code tree. Any `__pycache__` directories in the source code tree will be ignored and new `.pyc` files written within the pycache prefix. Thus if you use [`compileall`](https://docs.python.org/3/library/compileall.html#module-compileall "compileall: Tools for byte-compiling all Python source files in a directory tree.") as a pre-build step, you must ensure you run it with the same pycache prefix (if any) that you will use at runtime.
A relative path is interpreted relative to the current working directory.
This value is initially set based on the value of the [`-X`](https://docs.python.org/3/using/cmdline.html#cmdoption-X) `pycache_prefix=PATH` command-line option or the [`PYTHONPYCACHEPREFIX`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPYCACHEPREFIX) environment variable (command-line takes precedence). If neither are set, it is `None`.
Added in version 3.8.

sys.excepthook(_type_ , _value_ , _traceback_)[¶](https://docs.python.org/3/library/sys.html#sys.excepthook "Link to this definition")

This function prints out a given traceback and exception to `sys.stderr`.
When an exception other than [`SystemExit`](https://docs.python.org/3/library/exceptions.html#SystemExit "SystemExit") is raised and uncaught, the interpreter calls `sys.excepthook` with three arguments, the exception class, exception instance, and a traceback object. In an interactive session this happens just before control is returned to the prompt; in a Python program this happens just before the program exits. The handling of such top-level exceptions can be customized by assigning another three-argument function to `sys.excepthook`.
Raise an auditing event `sys.excepthook` with arguments `hook`, `type`, `value`, `traceback` when an uncaught exception occurs. If no hook has been set, `hook` may be `None`. If any hook raises an exception derived from [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError") the call to the hook will be suppressed. Otherwise, the audit hook exception will be reported as unraisable and `sys.excepthook` will be called.
See also
The [`sys.unraisablehook()`](https://docs.python.org/3/library/sys.html#sys.unraisablehook "sys.unraisablehook") function handles unraisable exceptions and the [`threading.excepthook()`](https://docs.python.org/3/library/threading.html#threading.excepthook "threading.excepthook") function handles exception raised by [`threading.Thread.run()`](https://docs.python.org/3/library/threading.html#threading.Thread.run "threading.Thread.run").

sys.__breakpointhook__[¶](https://docs.python.org/3/library/sys.html#sys.__breakpointhook__ "Link to this definition")


sys.__displayhook__[¶](https://docs.python.org/3/library/sys.html#sys.__displayhook__ "Link to this definition")


sys.__excepthook__[¶](https://docs.python.org/3/library/sys.html#sys.__excepthook__ "Link to this definition")


sys.__unraisablehook__[¶](https://docs.python.org/3/library/sys.html#sys.__unraisablehook__ "Link to this definition")

These objects contain the original values of `breakpointhook`, `displayhook`, `excepthook`, and `unraisablehook` at the start of the program. They are saved so that `breakpointhook`, `displayhook` and `excepthook`, `unraisablehook` can be restored in case they happen to get replaced with broken or alternative objects.
Added in version 3.7: __breakpointhook__
Added in version 3.8: __unraisablehook__

sys.exception()[¶](https://docs.python.org/3/library/sys.html#sys.exception "Link to this definition")

This function, when called while an exception handler is executing (such as an `except` or `except*` clause), returns the exception instance that was caught by this handler. When exception handlers are nested within one another, only the exception handled by the innermost handler is accessible.
If no exception handler is executing, this function returns `None`.
Added in version 3.11.

sys.exc_info()[¶](https://docs.python.org/3/library/sys.html#sys.exc_info "Link to this definition")

This function returns the old-style representation of the handled exception. If an exception `e` is currently handled (so [`exception()`](https://docs.python.org/3/library/sys.html#sys.exception "sys.exception") would return `e`), `exc_info()` returns the tuple `(type(e), e, e.__traceback__)`. That is, a tuple containing the type of the exception (a subclass of [`BaseException`](https://docs.python.org/3/library/exceptions.html#BaseException "BaseException")), the exception itself, and a [traceback object](https://docs.python.org/3/reference/datamodel.html#traceback-objects) which typically encapsulates the call stack at the point where the exception last occurred.
If no exception is being handled anywhere on the stack, this function return a tuple containing three `None` values.
Changed in version 3.11: The `type` and `traceback` fields are now derived from the `value` (the exception instance), so when an exception is modified while it is being handled, the changes are reflected in the results of subsequent calls to `exc_info()`.

sys.exec_prefix[¶](https://docs.python.org/3/library/sys.html#sys.exec_prefix "Link to this definition")

A string giving the site-specific directory prefix where the platform-dependent Python files are installed; by default, this is also `'/usr/local'`. This can be set at build time with the `--exec-prefix` argument to the **configure** script. Specifically, all configuration files (e.g. the `pyconfig.h` header file) are installed in the directory `_exec_prefix_/lib/python_X.Y_/config`, and shared library modules are installed in` _exec_prefix_/lib/python_X.Y_/lib-dynload`, where _X.Y_ is the version number of Python, for example `3.2`.
Note
If a [virtual environment](https://docs.python.org/3/library/venv.html#venv-def) is in effect, this `exec_prefix` will point to the virtual environment. The value for the Python installation will still be available, via [`base_exec_prefix`](https://docs.python.org/3/library/sys.html#sys.base_exec_prefix "sys.base_exec_prefix"). Refer to [Virtual Environments](https://docs.python.org/3/library/sys_path_init.html#sys-path-init-virtual-environments) for more information.
Changed in version 3.14: When running under a [virtual environment](https://docs.python.org/3/library/venv.html#venv-def), [`prefix`](https://docs.python.org/3/library/sys.html#sys.prefix "sys.prefix") and `exec_prefix` are now set to the virtual environment prefix by the [path initialization](https://docs.python.org/3/library/sys_path_init.html#sys-path-init), instead of [`site`](https://docs.python.org/3/library/site.html#module-site "site: Module responsible for site-specific configuration."). This means that `prefix` and `exec_prefix` always point to the virtual environment, even when `site` is disabled ([`-S`](https://docs.python.org/3/using/cmdline.html#cmdoption-S)).
