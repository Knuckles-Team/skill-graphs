  * The encoding and error handling are is initialized from [`PyConfig.stdio_encoding`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.stdio_encoding "PyConfig.stdio_encoding") and [`PyConfig.stdio_errors`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.stdio_errors "PyConfig.stdio_errors").
On Windows, UTF-8 is used for the console device. Non-character devices such as disk files and pipes use the system locale encoding (i.e. the ANSI codepage). Non-console character devices such as NUL (i.e. where `isatty()` returns `True`) use the value of the console input and output codepages at startup, respectively for stdin and stdout/stderr. This defaults to the system [locale encoding](https://docs.python.org/3/glossary.html#term-locale-encoding) if the process is not initially attached to a console.
The special behaviour of the console can be overridden by setting the environment variable PYTHONLEGACYWINDOWSSTDIO before starting Python. In that case, the console codepages are used as for any other character device.
Under all platforms, you can override the character encoding by setting the [`PYTHONIOENCODING`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONIOENCODING) environment variable before starting Python or by using the new [`-X`](https://docs.python.org/3/using/cmdline.html#cmdoption-X) `utf8` command line option and [`PYTHONUTF8`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONUTF8) environment variable. However, for the Windows console, this only applies when [`PYTHONLEGACYWINDOWSSTDIO`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONLEGACYWINDOWSSTDIO) is also set.
  * When interactive, the `stdout` stream is line-buffered. Otherwise, it is block-buffered like regular text files. The `stderr` stream is line-buffered in both cases. You can make both streams unbuffered by passing the [`-u`](https://docs.python.org/3/using/cmdline.html#cmdoption-u) command-line option or setting the [`PYTHONUNBUFFERED`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONUNBUFFERED) environment variable.


Changed in version 3.9: Non-interactive `stderr` is now line-buffered instead of fully buffered.
Note
To write or read binary data from/to the standard streams, use the underlying binary [`buffer`](https://docs.python.org/3/library/io.html#io.TextIOBase.buffer "io.TextIOBase.buffer") object. For example, to write bytes to `stdout`, use `sys.stdout.buffer.write(b'abc')`.
However, if you are writing a library (and do not control in which context its code will be executed), be aware that the standard streams may be replaced with file-like objects like [`io.StringIO`](https://docs.python.org/3/library/io.html#io.StringIO "io.StringIO") which do not support the `buffer` attribute.

sys.__stdin__[¶](https://docs.python.org/3/library/sys.html#sys.__stdin__ "Link to this definition")


sys.__stdout__[¶](https://docs.python.org/3/library/sys.html#sys.__stdout__ "Link to this definition")


sys.__stderr__[¶](https://docs.python.org/3/library/sys.html#sys.__stderr__ "Link to this definition")

These objects contain the original values of `stdin`, `stderr` and `stdout` at the start of the program. They are used during finalization, and could be useful to print to the actual standard stream no matter if the `sys.std*` object has been redirected.
It can also be used to restore the actual files to known working file objects in case they have been overwritten with a broken object. However, the preferred way to do this is to explicitly save the previous stream before replacing it, and restore the saved object.
Note
Under some conditions `stdin`, `stdout` and `stderr` as well as the original values `__stdin__`, `__stdout__` and `__stderr__` can be `None`. It is usually the case for Windows GUI apps that aren’t connected to a console and Python apps started with **pythonw**.

sys.stdlib_module_names[¶](https://docs.python.org/3/library/sys.html#sys.stdlib_module_names "Link to this definition")

A frozenset of strings containing the names of standard library modules.
It is the same on all platforms. Modules which are not available on some platforms and modules disabled at Python build are also listed. All module kinds are listed: pure Python, built-in, frozen and extension modules. Test modules are excluded.
For packages, only the main package is listed: sub-packages and sub-modules are not listed. For example, the `email` package is listed, but the `email.mime` sub-package and the `email.message` sub-module are not listed.
See also the [`sys.builtin_module_names`](https://docs.python.org/3/library/sys.html#sys.builtin_module_names "sys.builtin_module_names") list.
Added in version 3.10.

sys.thread_info[¶](https://docs.python.org/3/library/sys.html#sys.thread_info "Link to this definition")

A [named tuple](https://docs.python.org/3/glossary.html#term-named-tuple) holding information about the thread implementation.

thread_info.name[¶](https://docs.python.org/3/library/sys.html#sys.thread_info.name "Link to this definition")

The name of the thread implementation:
  * `"nt"`: Windows threads
  * `"pthread"`: POSIX threads
  * `"pthread-stubs"`: stub POSIX threads (on WebAssembly platforms without threading support)
  * `"solaris"`: Solaris threads



thread_info.lock[¶](https://docs.python.org/3/library/sys.html#sys.thread_info.lock "Link to this definition")

The name of the lock implementation:
  * `"semaphore"`: a lock uses a semaphore
  * `"mutex+cond"`: a lock uses a mutex and a condition variable
  * `None` if this information is unknown



thread_info.version[¶](https://docs.python.org/3/library/sys.html#sys.thread_info.version "Link to this definition")

The name and version of the thread library. It is a string, or `None` if this information is unknown.
Added in version 3.3.

sys.tracebacklimit[¶](https://docs.python.org/3/library/sys.html#sys.tracebacklimit "Link to this definition")

When this variable is set to an integer value, it determines the maximum number of levels of traceback information printed when an unhandled exception occurs. The default is `1000`. When set to `0` or less, all traceback information is suppressed and only the exception type and value are printed.

sys.unraisablehook(_unraisable_ , _/_)[¶](https://docs.python.org/3/library/sys.html#sys.unraisablehook "Link to this definition")

Handle an unraisable exception.
Called when an exception has occurred but there is no way for Python to handle it. For example, when a destructor raises an exception or during garbage collection ([`gc.collect()`](https://docs.python.org/3/library/gc.html#gc.collect "gc.collect")).
The _unraisable_ argument has the following attributes:
  * `exc_type`: Exception type.
  * `exc_value`: Exception value, can be `None`.
  * `exc_traceback`: Exception traceback, can be `None`.
  * `err_msg`: Error message, can be `None`.
  * `object`: Object causing the exception, can be `None`.


The default hook formats `err_msg` and `object` as: `f'{err_msg}: {object!r}'`; use “Exception ignored in” error message if `err_msg` is `None`.
[`sys.unraisablehook()`](https://docs.python.org/3/library/sys.html#sys.unraisablehook "sys.unraisablehook") can be overridden to control how unraisable exceptions are handled.
See also
[`excepthook()`](https://docs.python.org/3/library/sys.html#sys.excepthook "sys.excepthook") which handles uncaught exceptions.
Warning
Storing `exc_value` using a custom hook can create a reference cycle. It should be cleared explicitly to break the reference cycle when the exception is no longer needed.
Storing `object` using a custom hook can resurrect it if it is set to an object which is being finalized. Avoid storing `object` after the custom hook completes to avoid resurrecting objects.
Raise an auditing event `sys.unraisablehook` with arguments _hook_ , _unraisable_ when an exception that cannot be handled occurs. The _unraisable_ object is the same as what will be passed to the hook. If no hook has been set, _hook_ may be `None`.
Added in version 3.8.

sys.version[¶](https://docs.python.org/3/library/sys.html#sys.version "Link to this definition")

A string containing the version number of the Python interpreter plus additional information on the build number and compiler used. This string is displayed when the interactive interpreter is started. Do not extract version information out of it, rather, use [`version_info`](https://docs.python.org/3/library/sys.html#sys.version_info "sys.version_info") and the functions provided by the [`platform`](https://docs.python.org/3/library/platform.html#module-platform "platform: Retrieves as much platform identifying data as possible.") module.

sys.api_version[¶](https://docs.python.org/3/library/sys.html#sys.api_version "Link to this definition")

The C API version, equivalent to the C macro [`PYTHON_API_VERSION`](https://docs.python.org/3/c-api/module.html#c.PYTHON_API_VERSION "PYTHON_API_VERSION"). Defined for backwards compatibility.
Currently, this constant is not updated in new Python versions, and is not useful for versioning. This may change in the future.

sys.version_info[¶](https://docs.python.org/3/library/sys.html#sys.version_info "Link to this definition")

A tuple containing the five components of the version number: _major_ , _minor_ , _micro_ , _releaselevel_ , and _serial_. All values except _releaselevel_ are integers; the release level is `'alpha'`, `'beta'`, `'candidate'`, or `'final'`. The `version_info` value corresponding to the Python version 2.0 is `(2, 0, 0, 'final', 0)`. The components can also be accessed by name, so `sys.version_info[0]` is equivalent to `sys.version_info.major` and so on.
Changed in version 3.1: Added named component attributes.

sys.warnoptions[¶](https://docs.python.org/3/library/sys.html#sys.warnoptions "Link to this definition")

This is an implementation detail of the warnings framework; do not modify this value. Refer to the [`warnings`](https://docs.python.org/3/library/warnings.html#module-warnings "warnings: Issue warning messages and control their disposition.") module for more information on the warnings framework.

sys.winver[¶](https://docs.python.org/3/library/sys.html#sys.winver "Link to this definition")

The version number used to form registry keys on Windows platforms. This is stored as string resource 1000 in the Python DLL. The value is normally the major and minor versions of the running Python interpreter. It is provided in the `sys` module for informational purposes; modifying this value has no effect on the registry keys used by Python.
[Availability](https://docs.python.org/3/library/intro.html#availability): Windows.

sys.monitoring

Namespace containing functions and constants for register callbacks and controlling monitoring events. See [`sys.monitoring`](https://docs.python.org/3/library/sys.monitoring.html#module-sys.monitoring "sys.monitoring: Access and control event monitoring") for details.

sys._xoptions[¶](https://docs.python.org/3/library/sys.html#sys._xoptions "Link to this definition")

A dictionary of the various implementation-specific flags passed through the [`-X`](https://docs.python.org/3/using/cmdline.html#cmdoption-X) command-line option. Option names are either mapped to their values, if given explicitly, or to [`True`](https://docs.python.org/3/library/constants.html#True "True"). Example:
Copy```
$ ./python -Xa=b -Xc
Python 3.2a3+ (py3k, Oct 16 2010, 20:14:50)
[GCC 4.4.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> sys._xoptions
{'a': 'b', 'c': True}

```

**CPython implementation detail:** This is a CPython-specific way of accessing options passed through [`-X`](https://docs.python.org/3/using/cmdline.html#cmdoption-X). Other implementations may export them through other means, or not at all.
Added in version 3.2.
Citations
[[C99](https://docs.python.org/3/library/sys.html#id1)]
ISO/IEC 9899:1999. “Programming languages – C.” A public draft of this standard is available at
#### Previous topic
[Python Runtime Services](https://docs.python.org/3/library/python.html "previous chapter")
#### Next topic
[`sys.monitoring` — Execution event monitoring](https://docs.python.org/3/library/sys.monitoring.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=sys+%E2%80%94+System-specific+parameters+and+functions&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fsys.html&pagesource=library%2Fsys.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/sys.monitoring.html "sys.monitoring — Execution event monitoring") |
  * [previous](https://docs.python.org/3/library/python.html "Python Runtime Services") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Python Runtime Services](https://docs.python.org/3/library/python.html) »
  * [`sys` — System-specific parameters and functions](https://docs.python.org/3/library/sys.html)
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
