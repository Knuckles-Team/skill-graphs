#  `test.support` — Utilities for the Python test suite[¶](https://docs.python.org/3/library/test.html#module-test.support "Link to this heading")
The `test.support` module provides support for Python’s regression test suite.
Note
`test.support` is not a public module. It is documented here to help Python developers write tests. The API of this module is subject to change without backwards compatibility concerns between releases.
This module defines the following exceptions:

_exception_ test.support.TestFailed[¶](https://docs.python.org/3/library/test.html#test.support.TestFailed "Link to this definition")

Exception to be raised when a test fails. This is deprecated in favor of [`unittest`](https://docs.python.org/3/library/unittest.html#module-unittest "unittest: Unit testing framework for Python.")-based tests and [`unittest.TestCase`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase")’s assertion methods.

_exception_ test.support.ResourceDenied[¶](https://docs.python.org/3/library/test.html#test.support.ResourceDenied "Link to this definition")

Subclass of [`unittest.SkipTest`](https://docs.python.org/3/library/unittest.html#unittest.SkipTest "unittest.SkipTest"). Raised when a resource (such as a network connection) is not available. Raised by the [`requires()`](https://docs.python.org/3/library/test.html#test.support.requires "test.support.requires") function.
The `test.support` module defines the following constants:

test.support.verbose[¶](https://docs.python.org/3/library/test.html#test.support.verbose "Link to this definition")

`True` when verbose output is enabled. Should be checked when more detailed information is desired about a running test. _verbose_ is set by [`test.regrtest`](https://docs.python.org/3/library/test.html#module-test.regrtest "test.regrtest: Drives the regression test suite.").

test.support.is_jython[¶](https://docs.python.org/3/library/test.html#test.support.is_jython "Link to this definition")

`True` if the running interpreter is Jython.

test.support.is_android[¶](https://docs.python.org/3/library/test.html#test.support.is_android "Link to this definition")

`True` if `sys.platform` is `android`.

test.support.is_emscripten[¶](https://docs.python.org/3/library/test.html#test.support.is_emscripten "Link to this definition")

`True` if `sys.platform` is `emscripten`.

test.support.is_wasi[¶](https://docs.python.org/3/library/test.html#test.support.is_wasi "Link to this definition")

`True` if `sys.platform` is `wasi`.

test.support.is_apple_mobile[¶](https://docs.python.org/3/library/test.html#test.support.is_apple_mobile "Link to this definition")

`True` if `sys.platform` is `ios`, `tvos`, or `watchos`.

test.support.is_apple[¶](https://docs.python.org/3/library/test.html#test.support.is_apple "Link to this definition")

`True` if `sys.platform` is `darwin` or `is_apple_mobile` is `True`.

test.support.unix_shell[¶](https://docs.python.org/3/library/test.html#test.support.unix_shell "Link to this definition")

Path for shell if not on Windows; otherwise `None`.

test.support.LOOPBACK_TIMEOUT[¶](https://docs.python.org/3/library/test.html#test.support.LOOPBACK_TIMEOUT "Link to this definition")

Timeout in seconds for tests using a network server listening on the network local loopback interface like `127.0.0.1`.
The timeout is long enough to prevent test failure: it takes into account that the client and the server can run in different threads or even different processes.
The timeout should be long enough for [`connect()`](https://docs.python.org/3/library/socket.html#socket.socket.connect "socket.socket.connect"), [`recv()`](https://docs.python.org/3/library/socket.html#socket.socket.recv "socket.socket.recv") and [`send()`](https://docs.python.org/3/library/socket.html#socket.socket.send "socket.socket.send") methods of [`socket.socket`](https://docs.python.org/3/library/socket.html#socket.socket "socket.socket").
Its default value is 5 seconds.
See also [`INTERNET_TIMEOUT`](https://docs.python.org/3/library/test.html#test.support.INTERNET_TIMEOUT "test.support.INTERNET_TIMEOUT").

test.support.INTERNET_TIMEOUT[¶](https://docs.python.org/3/library/test.html#test.support.INTERNET_TIMEOUT "Link to this definition")

Timeout in seconds for network requests going to the internet.
The timeout is short enough to prevent a test to wait for too long if the internet request is blocked for whatever reason.
Usually, a timeout using `INTERNET_TIMEOUT` should not mark a test as failed, but skip the test instead: see [`transient_internet()`](https://docs.python.org/3/library/test.html#test.support.socket_helper.transient_internet "test.support.socket_helper.transient_internet").
Its default value is 1 minute.
See also [`LOOPBACK_TIMEOUT`](https://docs.python.org/3/library/test.html#test.support.LOOPBACK_TIMEOUT "test.support.LOOPBACK_TIMEOUT").

test.support.SHORT_TIMEOUT[¶](https://docs.python.org/3/library/test.html#test.support.SHORT_TIMEOUT "Link to this definition")

Timeout in seconds to mark a test as failed if the test takes “too long”.
The timeout value depends on the regrtest `--timeout` command line option.
If a test using `SHORT_TIMEOUT` starts to fail randomly on slow buildbots, use [`LONG_TIMEOUT`](https://docs.python.org/3/library/test.html#test.support.LONG_TIMEOUT "test.support.LONG_TIMEOUT") instead.
Its default value is 30 seconds.

test.support.LONG_TIMEOUT[¶](https://docs.python.org/3/library/test.html#test.support.LONG_TIMEOUT "Link to this definition")

Timeout in seconds to detect when a test hangs.
It is long enough to reduce the risk of test failure on the slowest Python buildbots. It should not be used to mark a test as failed if the test takes “too long”. The timeout value depends on the regrtest `--timeout` command line option.
Its default value is 5 minutes.
See also [`LOOPBACK_TIMEOUT`](https://docs.python.org/3/library/test.html#test.support.LOOPBACK_TIMEOUT "test.support.LOOPBACK_TIMEOUT"), [`INTERNET_TIMEOUT`](https://docs.python.org/3/library/test.html#test.support.INTERNET_TIMEOUT "test.support.INTERNET_TIMEOUT") and [`SHORT_TIMEOUT`](https://docs.python.org/3/library/test.html#test.support.SHORT_TIMEOUT "test.support.SHORT_TIMEOUT").

test.support.PGO[¶](https://docs.python.org/3/library/test.html#test.support.PGO "Link to this definition")

Set when tests can be skipped when they are not useful for PGO.

test.support.PIPE_MAX_SIZE[¶](https://docs.python.org/3/library/test.html#test.support.PIPE_MAX_SIZE "Link to this definition")

A constant that is likely larger than the underlying OS pipe buffer size, to make writes blocking.

test.support.Py_DEBUG[¶](https://docs.python.org/3/library/test.html#test.support.Py_DEBUG "Link to this definition")

`True` if Python was built with the [`Py_DEBUG`](https://docs.python.org/3/c-api/intro.html#c.Py_DEBUG "Py_DEBUG") macro defined, that is, if Python was [built in debug mode](https://docs.python.org/3/using/configure.html#debug-build).
Added in version 3.12.

test.support.SOCK_MAX_SIZE[¶](https://docs.python.org/3/library/test.html#test.support.SOCK_MAX_SIZE "Link to this definition")

A constant that is likely larger than the underlying OS socket buffer size, to make writes blocking.

test.support.TEST_SUPPORT_DIR[¶](https://docs.python.org/3/library/test.html#test.support.TEST_SUPPORT_DIR "Link to this definition")

Set to the top level directory that contains `test.support`.

test.support.TEST_HOME_DIR[¶](https://docs.python.org/3/library/test.html#test.support.TEST_HOME_DIR "Link to this definition")

Set to the top level directory for the test package.

test.support.TEST_DATA_DIR[¶](https://docs.python.org/3/library/test.html#test.support.TEST_DATA_DIR "Link to this definition")

Set to the `data` directory within the test package.

test.support.MAX_Py_ssize_t[¶](https://docs.python.org/3/library/test.html#test.support.MAX_Py_ssize_t "Link to this definition")

Set to [`sys.maxsize`](https://docs.python.org/3/library/sys.html#sys.maxsize "sys.maxsize") for big memory tests.

test.support.max_memuse[¶](https://docs.python.org/3/library/test.html#test.support.max_memuse "Link to this definition")

Set by [`set_memlimit()`](https://docs.python.org/3/library/test.html#test.support.set_memlimit "test.support.set_memlimit") as the memory limit for big memory tests. Limited by [`MAX_Py_ssize_t`](https://docs.python.org/3/library/test.html#test.support.MAX_Py_ssize_t "test.support.MAX_Py_ssize_t").

test.support.real_max_memuse[¶](https://docs.python.org/3/library/test.html#test.support.real_max_memuse "Link to this definition")

Set by [`set_memlimit()`](https://docs.python.org/3/library/test.html#test.support.set_memlimit "test.support.set_memlimit") as the memory limit for big memory tests. Not limited by [`MAX_Py_ssize_t`](https://docs.python.org/3/library/test.html#test.support.MAX_Py_ssize_t "test.support.MAX_Py_ssize_t").

test.support.MISSING_C_DOCSTRINGS[¶](https://docs.python.org/3/library/test.html#test.support.MISSING_C_DOCSTRINGS "Link to this definition")

Set to `True` if Python is built without docstrings (the `WITH_DOC_STRINGS` macro is not defined). See the [`configure --without-doc-strings`](https://docs.python.org/3/using/configure.html#cmdoption-without-doc-strings) option.
See also the [`HAVE_DOCSTRINGS`](https://docs.python.org/3/library/test.html#test.support.HAVE_DOCSTRINGS "test.support.HAVE_DOCSTRINGS") variable.

test.support.HAVE_DOCSTRINGS[¶](https://docs.python.org/3/library/test.html#test.support.HAVE_DOCSTRINGS "Link to this definition")

Set to `True` if function docstrings are available. See the [`python -OO`](https://docs.python.org/3/using/cmdline.html#cmdoption-O) option, which strips docstrings of functions implemented in Python.
See also the [`MISSING_C_DOCSTRINGS`](https://docs.python.org/3/library/test.html#test.support.MISSING_C_DOCSTRINGS "test.support.MISSING_C_DOCSTRINGS") variable.

test.support.TEST_HTTP_URL[¶](https://docs.python.org/3/library/test.html#test.support.TEST_HTTP_URL "Link to this definition")

Define the URL of a dedicated HTTP server for the network tests.

test.support.ALWAYS_EQ[¶](https://docs.python.org/3/library/test.html#test.support.ALWAYS_EQ "Link to this definition")

Object that is equal to anything. Used to test mixed type comparison.

test.support.NEVER_EQ[¶](https://docs.python.org/3/library/test.html#test.support.NEVER_EQ "Link to this definition")

Object that is not equal to anything (even to [`ALWAYS_EQ`](https://docs.python.org/3/library/test.html#test.support.ALWAYS_EQ "test.support.ALWAYS_EQ")). Used to test mixed type comparison.

test.support.LARGEST[¶](https://docs.python.org/3/library/test.html#test.support.LARGEST "Link to this definition")

Object that is greater than anything (except itself). Used to test mixed type comparison.

test.support.SMALLEST[¶](https://docs.python.org/3/library/test.html#test.support.SMALLEST "Link to this definition")

Object that is less than anything (except itself). Used to test mixed type comparison.
The `test.support` module defines the following functions:

test.support.busy_retry(_timeout_ , _err_msg =None_, _/_ , _*_ , _error =True_)[¶](https://docs.python.org/3/library/test.html#test.support.busy_retry "Link to this definition")

Run the loop body until `break` stops the loop.
After _timeout_ seconds, raise an [`AssertionError`](https://docs.python.org/3/library/exceptions.html#AssertionError "AssertionError") if _error_ is true, or just stop the loop if _error_ is false.
Example:
Copy```
for _ in support.busy_retry(support.SHORT_TIMEOUT):
    if check():
        break

```

Example of error=False usage:
Copy```
for _ in support.busy_retry(support.SHORT_TIMEOUT, error=False):
    if check():
        break
else:
    raise RuntimeError('my custom error')

```


test.support.sleeping_retry(_timeout_ , _err_msg =None_, _/_ , _*_ , _init_delay =0.010_, _max_delay =1.0_, _error =True_)[¶](https://docs.python.org/3/library/test.html#test.support.sleeping_retry "Link to this definition")

Wait strategy that applies exponential backoff.
Run the loop body until `break` stops the loop. Sleep at each loop iteration, but not at the first iteration. The sleep delay is doubled at each iteration (up to _max_delay_ seconds).
See [`busy_retry()`](https://docs.python.org/3/library/test.html#test.support.busy_retry "test.support.busy_retry") documentation for the parameters usage.
Example raising an exception after SHORT_TIMEOUT seconds:
Copy```
for _ in support.sleeping_retry(support.SHORT_TIMEOUT):
    if check():
        break

```

Example of error=False usage:
Copy```
for _ in support.sleeping_retry(support.SHORT_TIMEOUT, error=False):
    if check():
        break
else:
    raise RuntimeError('my custom error')

```


test.support.is_resource_enabled(_resource_)[¶](https://docs.python.org/3/library/test.html#test.support.is_resource_enabled "Link to this definition")

Return `True` if _resource_ is enabled and available. The list of available resources is only set when [`test.regrtest`](https://docs.python.org/3/library/test.html#module-test.regrtest "test.regrtest: Drives the regression test suite.") is executing the tests.

test.support.get_resource_value(_resource_)[¶](https://docs.python.org/3/library/test.html#test.support.get_resource_value "Link to this definition")

Return the value specified for _resource_ (as `-u _resource_=_value_`). Return`None` if _resource_ is disabled or no value is specified.

test.support.python_is_optimized()[¶](https://docs.python.org/3/library/test.html#test.support.python_is_optimized "Link to this definition")

Return `True` if Python was not built with `-O0` or `-Og`.

test.support.with_pymalloc()[¶](https://docs.python.org/3/library/test.html#test.support.with_pymalloc "Link to this definition")

Return `_testcapi.WITH_PYMALLOC`.

test.support.requires(_resource_ , _msg =None_)[¶](https://docs.python.org/3/library/test.html#test.support.requires "Link to this definition")

Raise [`ResourceDenied`](https://docs.python.org/3/library/test.html#test.support.ResourceDenied "test.support.ResourceDenied") if _resource_ is not available. _msg_ is the argument to `ResourceDenied` if it is raised. Always returns `True` if called by a function whose `__name__` is `'__main__'`. Used when tests are executed by [`test.regrtest`](https://docs.python.org/3/library/test.html#module-test.regrtest "test.regrtest: Drives the regression test suite.").

test.support.sortdict(_dict_)[¶](https://docs.python.org/3/library/test.html#test.support.sortdict "Link to this definition")

Return a repr of _dict_ with keys sorted.

test.support.findfile(_filename_ , _subdir =None_)[¶](https://docs.python.org/3/library/test.html#test.support.findfile "Link to this definition")

Return the path to the file named _filename_. If no match is found _filename_ is returned. This does not equal a failure since it could be the path to the file.
Setting _subdir_ indicates a relative path to use to find the file rather than looking directly in the path directories.

test.support.get_pagesize()[¶](https://docs.python.org/3/library/test.html#test.support.get_pagesize "Link to this definition")

Get size of a page in bytes.
Added in version 3.12.

test.support.setswitchinterval(_interval_)[¶](https://docs.python.org/3/library/test.html#test.support.setswitchinterval "Link to this definition")

Set the [`sys.setswitchinterval()`](https://docs.python.org/3/library/sys.html#sys.setswitchinterval "sys.setswitchinterval") to the given _interval_. Defines a minimum interval for Android systems to prevent the system from hanging.

test.support.check_impl_detail(_** guards_)[¶](https://docs.python.org/3/library/test.html#test.support.check_impl_detail "Link to this definition")

Use this check to guard CPython’s implementation-specific tests or to run them only on the implementations guarded by the arguments. This function returns `True` or `False` depending on the host platform. Example usage:
Copy```
check_impl_detail()               # Only on CPython (default).
check_impl_detail(jython=True)    # Only on Jython.
check_impl_detail(cpython=False)  # Everywhere except CPython.

```


test.support.set_memlimit(_limit_)[¶](https://docs.python.org/3/library/test.html#test.support.set_memlimit "Link to this definition")

Set the values for [`max_memuse`](https://docs.python.org/3/library/test.html#test.support.max_memuse "test.support.max_memuse") and [`real_max_memuse`](https://docs.python.org/3/library/test.html#test.support.real_max_memuse "test.support.real_max_memuse") for big memory tests.

test.support.record_original_stdout(_stdout_)[¶](https://docs.python.org/3/library/test.html#test.support.record_original_stdout "Link to this definition")

Store the value from _stdout_. It is meant to hold the stdout at the time the regrtest began.

test.support.get_original_stdout()[¶](https://docs.python.org/3/library/test.html#test.support.get_original_stdout "Link to this definition")

Return the original stdout set by [`record_original_stdout()`](https://docs.python.org/3/library/test.html#test.support.record_original_stdout "test.support.record_original_stdout") or `sys.stdout` if it’s not set.

test.support.args_from_interpreter_flags()[¶](https://docs.python.org/3/library/test.html#test.support.args_from_interpreter_flags "Link to this definition")

Return a list of command line arguments reproducing the current settings in `sys.flags` and `sys.warnoptions`.

test.support.optim_args_from_interpreter_flags()[¶](https://docs.python.org/3/library/test.html#test.support.optim_args_from_interpreter_flags "Link to this definition")

Return a list of command line arguments reproducing the current optimization settings in `sys.flags`.

test.support.captured_stdin()[¶](https://docs.python.org/3/library/test.html#test.support.captured_stdin "Link to this definition")


test.support.captured_stdout()[¶](https://docs.python.org/3/library/test.html#test.support.captured_stdout "Link to this definition")


test.support.captured_stderr()[¶](https://docs.python.org/3/library/test.html#test.support.captured_stderr "Link to this definition")

A context managers that temporarily replaces the named stream with [`io.StringIO`](https://docs.python.org/3/library/io.html#io.StringIO "io.StringIO") object.
Example use with output streams:
Copy```
with captured_stdout() as stdout, captured_stderr() as stderr:
    print("hello")
    print("error", file=sys.stderr)
assert stdout.getvalue() == "hello\n"
assert stderr.getvalue() == "error\n"

```

Example use with input stream:
Copy```
with captured_stdin() as stdin:
    stdin.write('hello\n')
    stdin.seek(0)
    # call test code that consumes from sys.stdin
    captured = input()
self.assertEqual(captured, "hello")

```


test.support.disable_faulthandler()[¶](https://docs.python.org/3/library/test.html#test.support.disable_faulthandler "Link to this definition")

A context manager that temporary disables [`faulthandler`](https://docs.python.org/3/library/faulthandler.html#module-faulthandler "faulthandler: Dump the Python traceback.").

test.support.gc_collect()[¶](https://docs.python.org/3/library/test.html#test.support.gc_collect "Link to this definition")

Force as many objects as possible to be collected. This is needed because timely deallocation is not guaranteed by the garbage collector. This means that `__del__` methods may be called later than expected and weakrefs may remain alive for longer than expected.

test.support.disable_gc()[¶](https://docs.python.org/3/library/test.html#test.support.disable_gc "Link to this definition")

A context manager that disables the garbage collector on entry. On exit, the garbage collector is restored to its prior state.

test.support.swap_attr(_obj_ , _attr_ , _new_val_)[¶](https://docs.python.org/3/library/test.html#test.support.swap_attr "Link to this definition")

Context manager to swap out an attribute with a new object.
Usage:
Copy```
with swap_attr(obj, "attr", 5):
    ...

```

This will set `obj.attr` to 5 for the duration of the `with` block, restoring the old value at the end of the block. If `attr` doesn’t exist on `obj`, it will be created and then deleted at the end of the block.
The old value (or `None` if it doesn’t exist) will be assigned to the target of the “as” clause, if there is one.

test.support.swap_item(_obj_ , _attr_ , _new_val_)[¶](https://docs.python.org/3/library/test.html#test.support.swap_item "Link to this definition")

Context manager to swap out an item with a new object.
Usage:
Copy```
with swap_item(obj, "item", 5):
    ...

```

This will set `obj["item"]` to 5 for the duration of the `with` block, restoring the old value at the end of the block. If `item` doesn’t exist on `obj`, it will be created and then deleted at the end of the block.
The old value (or `None` if it doesn’t exist) will be assigned to the target of the “as” clause, if there is one.

test.support.flush_std_streams()[¶](https://docs.python.org/3/library/test.html#test.support.flush_std_streams "Link to this definition")

Call the `flush()` method on [`sys.stdout`](https://docs.python.org/3/library/sys.html#sys.stdout "sys.stdout") and then on [`sys.stderr`](https://docs.python.org/3/library/sys.html#sys.stderr "sys.stderr"). It can be used to make sure that the logs order is consistent before writing into stderr.
Added in version 3.11.

test.support.print_warning(_msg_)[¶](https://docs.python.org/3/library/test.html#test.support.print_warning "Link to this definition")

Print a warning into [`sys.__stderr__`](https://docs.python.org/3/library/sys.html#sys.__stderr__ "sys.__stderr__"). Format the message as: `f"Warning -- {msg}"`. If _msg_ is made of multiple lines, add `"Warning -- "` prefix to each line.
Added in version 3.9.

test.support.wait_process(_pid_ , _*_ , _exitcode_ , _timeout =None_)[¶](https://docs.python.org/3/library/test.html#test.support.wait_process "Link to this definition")

Wait until process _pid_ completes and check that the process exit code is _exitcode_.
Raise an [`AssertionError`](https://docs.python.org/3/library/exceptions.html#AssertionError "AssertionError") if the process exit code is not equal to _exitcode_.
If the process runs longer than _timeout_ seconds ([`SHORT_TIMEOUT`](https://docs.python.org/3/library/test.html#test.support.SHORT_TIMEOUT "test.support.SHORT_TIMEOUT") by default), kill the process and raise an [`AssertionError`](https://docs.python.org/3/library/exceptions.html#AssertionError "AssertionError"). The timeout feature is not available on Windows.
Added in version 3.9.

test.support.calcobjsize(_fmt_)[¶](https://docs.python.org/3/library/test.html#test.support.calcobjsize "Link to this definition")

Return the size of the [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject") whose structure members are defined by _fmt_. The returned value includes the size of the Python object header and alignment.

test.support.calcvobjsize(_fmt_)[¶](https://docs.python.org/3/library/test.html#test.support.calcvobjsize "Link to this definition")

Return the size of the [`PyVarObject`](https://docs.python.org/3/c-api/structures.html#c.PyVarObject "PyVarObject") whose structure members are defined by _fmt_. The returned value includes the size of the Python object header and alignment.

test.support.checksizeof(_test_ , _o_ , _size_)[¶](https://docs.python.org/3/library/test.html#test.support.checksizeof "Link to this definition")

For testcase _test_ , assert that the `sys.getsizeof` for _o_ plus the GC header size equals _size_.

@test.support.anticipate_failure(_condition_)[¶](https://docs.python.org/3/library/test.html#test.support.anticipate_failure "Link to this definition")

A decorator to conditionally mark tests with [`unittest.expectedFailure()`](https://docs.python.org/3/library/unittest.html#unittest.expectedFailure "unittest.expectedFailure"). Any use of this decorator should have an associated comment identifying the relevant tracker issue.

test.support.system_must_validate_cert(_f_)[¶](https://docs.python.org/3/library/test.html#test.support.system_must_validate_cert "Link to this definition")

A decorator that skips the decorated test on TLS certification validation failures.

@test.support.run_with_locale(_catstr_ , _* locales_)[¶](https://docs.python.org/3/library/test.html#test.support.run_with_locale "Link to this definition")

A decorator for running a function in a different locale, correctly resetting it after it has finished. _catstr_ is the locale category as a string (for example `"LC_ALL"`). The _locales_ passed will be tried sequentially, and the first valid locale will be used.

@test.support.run_with_tz(_tz_)[¶](https://docs.python.org/3/library/test.html#test.support.run_with_tz "Link to this definition")

A decorator for running a function in a specific timezone, correctly resetting it after it has finished.

@test.support.requires_freebsd_version(_* min_version_)[¶](https://docs.python.org/3/library/test.html#test.support.requires_freebsd_version "Link to this definition")

Decorator for the minimum version when running test on FreeBSD. If the FreeBSD version is less than the minimum, the test is skipped.

@test.support.requires_linux_version(_* min_version_)[¶](https://docs.python.org/3/library/test.html#test.support.requires_linux_version "Link to this definition")

Decorator for the minimum version when running test on Linux. If the Linux version is less than the minimum, the test is skipped.

@test.support.requires_mac_version(_* min_version_)[¶](https://docs.python.org/3/library/test.html#test.support.requires_mac_version "Link to this definition")

Decorator for the minimum version when running test on macOS. If the macOS version is less than the minimum, the test is skipped.

@test.support.requires_gil_enabled[¶](https://docs.python.org/3/library/test.html#test.support.requires_gil_enabled "Link to this definition")

Decorator for skipping tests on the free-threaded build. If the [GIL](https://docs.python.org/3/glossary.html#term-GIL) is disabled, the test is skipped.

@test.support.requires_IEEE_754[¶](https://docs.python.org/3/library/test.html#test.support.requires_IEEE_754 "Link to this definition")

Decorator for skipping tests on non-IEEE 754 platforms.

@test.support.requires_zlib[¶](https://docs.python.org/3/library/test.html#test.support.requires_zlib "Link to this definition")

Decorator for skipping tests if [`zlib`](https://docs.python.org/3/library/zlib.html#module-zlib "zlib: Low-level interface to compression and decompression routines compatible with gzip.") doesn’t exist.

@test.support.requires_gzip[¶](https://docs.python.org/3/library/test.html#test.support.requires_gzip "Link to this definition")

Decorator for skipping tests if [`gzip`](https://docs.python.org/3/library/gzip.html#module-gzip "gzip: Interfaces for gzip compression and decompression using file objects.") doesn’t exist.

@test.support.requires_bz2[¶](https://docs.python.org/3/library/test.html#test.support.requires_bz2 "Link to this definition")

Decorator for skipping tests if [`bz2`](https://docs.python.org/3/library/bz2.html#module-bz2 "bz2: Interfaces for bzip2 compression and decompression.") doesn’t exist.

@test.support.requires_lzma[¶](https://docs.python.org/3/library/test.html#test.support.requires_lzma "Link to this definition")

Decorator for skipping tests if [`lzma`](https://docs.python.org/3/library/lzma.html#module-lzma "lzma: A Python wrapper for the liblzma compression library.") doesn’t exist.

@test.support.requires_resource(_resource_)[¶](https://docs.python.org/3/library/test.html#test.support.requires_resource "Link to this definition")

Decorator for skipping tests if _resource_ is not available.

@test.support.requires_docstrings[¶](https://docs.python.org/3/library/test.html#test.support.requires_docstrings "Link to this definition")

Decorator for only running the test if [`HAVE_DOCSTRINGS`](https://docs.python.org/3/library/test.html#test.support.HAVE_DOCSTRINGS "test.support.HAVE_DOCSTRINGS").

@test.support.requires_limited_api[¶](https://docs.python.org/3/library/test.html#test.support.requires_limited_api "Link to this definition")

Decorator for only running the test if [Limited C API](https://docs.python.org/3/c-api/stable.html#limited-c-api) is available.

@test.support.cpython_only[¶](https://docs.python.org/3/library/test.html#test.support.cpython_only "Link to this definition")

Decorator for tests only applicable to CPython.

@test.support.impl_detail(_msg =None_, _** guards_)[¶](https://docs.python.org/3/library/test.html#test.support.impl_detail "Link to this definition")

Decorator for invoking [`check_impl_detail()`](https://docs.python.org/3/library/test.html#test.support.check_impl_detail "test.support.check_impl_detail") on _guards_. If that returns `False`, then uses _msg_ as the reason for skipping the test.

@test.support.thread_unsafe(_reason =None_)[¶](https://docs.python.org/3/library/test.html#test.support.thread_unsafe "Link to this definition")

Decorator for marking tests as thread-unsafe. This test always runs in one thread even when invoked with `--parallel-threads`.

@test.support.no_tracing[¶](https://docs.python.org/3/library/test.html#test.support.no_tracing "Link to this definition")

Decorator to temporarily turn off tracing for the duration of the test.

@test.support.refcount_test[¶](https://docs.python.org/3/library/test.html#test.support.refcount_test "Link to this definition")

Decorator for tests which involve reference counting. The decorator does not run the test if it is not run by CPython. Any trace function is unset for the duration of the test to prevent unexpected refcounts caused by the trace function.

@test.support.bigmemtest(_size_ , _memuse_ , _dry_run =True_)[¶](https://docs.python.org/3/library/test.html#test.support.bigmemtest "Link to this definition")

Decorator for bigmem tests.
_size_ is a requested size for the test (in arbitrary, test-interpreted units.) _memuse_ is the number of bytes per unit for the test, or a good estimate of it. For example, a test that needs two byte buffers, of 4 GiB each, could be decorated with `@bigmemtest(size=_4G, memuse=2)`.
The _size_ argument is normally passed to the decorated test method as an extra argument. If _dry_run_ is `True`, the value passed to the test method may be less than the requested value. If _dry_run_ is `False`, it means the test doesn’t support dummy runs when `-M` is not specified.

@test.support.bigaddrspacetest[¶](https://docs.python.org/3/library/test.html#test.support.bigaddrspacetest "Link to this definition")

Decorator for tests that fill the address space.

test.support.linked_to_musl()[¶](https://docs.python.org/3/library/test.html#test.support.linked_to_musl "Link to this definition")

Return `False` if there is no evidence the interpreter was compiled with `musl`, otherwise return a version triple, either `(0, 0, 0)` if the version is unknown, or the actual version if it is known. Intended for use in `skip` decorators. `emscripten` and `wasi` are assumed to be compiled with `musl`; otherwise `platform.libc_ver` is checked.

test.support.check_syntax_error(_testcase_ , _statement_ , _errtext =''_, _*_ , _lineno =None_, _offset =None_)[¶](https://docs.python.org/3/library/test.html#test.support.check_syntax_error "Link to this definition")

Test for syntax errors in _statement_ by attempting to compile _statement_. _testcase_ is the [`unittest`](https://docs.python.org/3/library/unittest.html#module-unittest "unittest: Unit testing framework for Python.") instance for the test. _errtext_ is the regular expression which should match the string representation of the raised [`SyntaxError`](https://docs.python.org/3/library/exceptions.html#SyntaxError "SyntaxError"). If _lineno_ is not `None`, compares to the line of the exception. If _offset_ is not `None`, compares to the offset of the exception.

test.support.open_urlresource(_url_ , _* args_, _** kw_)[¶](https://docs.python.org/3/library/test.html#test.support.open_urlresource "Link to this definition")

Open _url_. If open fails, raises [`TestFailed`](https://docs.python.org/3/library/test.html#test.support.TestFailed "test.support.TestFailed").

test.support.reap_children()[¶](https://docs.python.org/3/library/test.html#test.support.reap_children "Link to this definition")

Use this at the end of `test_main` whenever sub-processes are started. This will help ensure that no extra children (zombies) stick around to hog resources and create problems when looking for refleaks.

test.support.get_attribute(_obj_ , _name_)[¶](https://docs.python.org/3/library/test.html#test.support.get_attribute "Link to this definition")

Get an attribute, raising [`unittest.SkipTest`](https://docs.python.org/3/library/unittest.html#unittest.SkipTest "unittest.SkipTest") if [`AttributeError`](https://docs.python.org/3/library/exceptions.html#AttributeError "AttributeError") is raised.

test.support.catch_unraisable_exception()[¶](https://docs.python.org/3/library/test.html#test.support.catch_unraisable_exception "Link to this definition")

Context manager catching unraisable exception using [`sys.unraisablehook()`](https://docs.python.org/3/library/sys.html#sys.unraisablehook "sys.unraisablehook").
Storing the exception value (`cm.unraisable.exc_value`) creates a reference cycle. The reference cycle is broken explicitly when the context manager exits.
Storing the object (`cm.unraisable.object`) can resurrect it if it is set to an object which is being finalized. Exiting the context manager clears the stored object.
Usage:
Copy```
with support.catch_unraisable_exception() as cm:
    # code creating an "unraisable exception"
    ...

    # check the unraisable exception: use cm.unraisable
    ...

# cm.unraisable attribute no longer exists at this point
# (to break a reference cycle)

```

Added in version 3.8.

test.support.load_package_tests(_pkg_dir_ , _loader_ , _standard_tests_ , _pattern_)[¶](https://docs.python.org/3/library/test.html#test.support.load_package_tests "Link to this definition")

Generic implementation of the [`unittest`](https://docs.python.org/3/library/unittest.html#module-unittest "unittest: Unit testing framework for Python.") `load_tests` protocol for use in test packages. _pkg_dir_ is the root directory of the package; _loader_ , _standard_tests_ , and _pattern_ are the arguments expected by `load_tests`. In simple cases, the test package’s `__init__.py` can be the following:
Copy```
import os
from test.support import load_package_tests

def load_tests(*args):
    return load_package_tests(os.path.dirname(__file__), *args)

```


test.support.detect_api_mismatch(_ref_api_ , _other_api_ , _*_ , _ignore =()_)[¶](https://docs.python.org/3/library/test.html#test.support.detect_api_mismatch "Link to this definition")

Returns the set of attributes, functions or methods of _ref_api_ not found on _other_api_ , except for a defined list of items to be ignored in this check specified in _ignore_.
By default this skips private attributes beginning with ‘_’ but includes all magic methods, i.e. those starting and ending in ‘__’.
Added in version 3.5.

test.support.patch(_test_instance_ , _object_to_patch_ , _attr_name_ , _new_value_)[¶](https://docs.python.org/3/library/test.html#test.support.patch "Link to this definition")

Override _object_to_patch.attr_name_ with _new_value_. Also add cleanup procedure to _test_instance_ to restore _object_to_patch_ for _attr_name_. The _attr_name_ should be a valid attribute for _object_to_patch_.

test.support.run_in_subinterp(_code_)[¶](https://docs.python.org/3/library/test.html#test.support.run_in_subinterp "Link to this definition")

Run _code_ in subinterpreter. Raise [`unittest.SkipTest`](https://docs.python.org/3/library/unittest.html#unittest.SkipTest "unittest.SkipTest") if [`tracemalloc`](https://docs.python.org/3/library/tracemalloc.html#module-tracemalloc "tracemalloc: Trace memory allocations.") is enabled.

test.support.check_free_after_iterating(_test_ , _iter_ , _cls_ , _args =()_)[¶](https://docs.python.org/3/library/test.html#test.support.check_free_after_iterating "Link to this definition")

Assert instances of _cls_ are deallocated after iterating.

test.support.missing_compiler_executable(_cmd_names =[]_)[¶](https://docs.python.org/3/library/test.html#test.support.missing_compiler_executable "Link to this definition")

Check for the existence of the compiler executables whose names are listed in _cmd_names_ or all the compiler executables when _cmd_names_ is empty and return the first missing executable or `None` when none is found missing.

test.support.check__all__(_test_case_ , _module_ , _name_of_module =None_, _extra =()_, _not_exported =()_)[¶](https://docs.python.org/3/library/test.html#test.support.check__all__ "Link to this definition")

Assert that the `__all__` variable of _module_ contains all public names.
The module’s public names (its API) are detected automatically based on whether they match the public name convention and were defined in _module_.
The _name_of_module_ argument can specify (as a string or tuple thereof) what module(s) an API could be defined in order to be detected as a public API. One case for this is when _module_ imports part of its public API from other modules, possibly a C backend (like `csv` and its `_csv`).
The _extra_ argument can be a set of names that wouldn’t otherwise be automatically detected as “public”, like objects without a proper [`__module__`](https://docs.python.org/3/library/stdtypes.html#definition.__module__ "definition.__module__") attribute. If provided, it will be added to the automatically detected ones.
The _not_exported_ argument can be a set of names that must not be treated as part of the public API even though their names indicate otherwise.
Example use:
Copy```
import bar
import foo
import unittest
from test import support

class MiscTestCase(unittest.TestCase):
    def test__all__(self):
        support.check__all__(self, foo)

class OtherTestCase(unittest.TestCase):
    def test__all__(self):
        extra = {'BAR_CONST', 'FOO_CONST'}
        not_exported = {'baz'}  # Undocumented name.
        # bar imports part of its API from _bar.
        support.check__all__(self, bar, ('bar', '_bar'),
                             extra=extra, not_exported=not_exported)

```

Added in version 3.6.

test.support.skip_if_broken_multiprocessing_synchronize()[¶](https://docs.python.org/3/library/test.html#test.support.skip_if_broken_multiprocessing_synchronize "Link to this definition")

Skip tests if the `multiprocessing.synchronize` module is missing, if there is no available semaphore implementation, or if creating a lock raises an [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError").
Added in version 3.10.

test.support.check_disallow_instantiation(_test_case_ , _tp_ , _* args_, _** kwds_)[¶](https://docs.python.org/3/library/test.html#test.support.check_disallow_instantiation "Link to this definition")

Assert that type _tp_ cannot be instantiated using _args_ and _kwds_.
Added in version 3.10.

test.support.adjust_int_max_str_digits(_max_digits_)[¶](https://docs.python.org/3/library/test.html#test.support.adjust_int_max_str_digits "Link to this definition")

This function returns a context manager that will change the global [`sys.set_int_max_str_digits()`](https://docs.python.org/3/library/sys.html#sys.set_int_max_str_digits "sys.set_int_max_str_digits") setting for the duration of the context to allow execution of test code that needs a different limit on the number of digits when converting between an integer and string.
Added in version 3.11.
The `test.support` module defines the following classes:

_class_ test.support.SuppressCrashReport[¶](https://docs.python.org/3/library/test.html#test.support.SuppressCrashReport "Link to this definition")

A context manager used to try to prevent crash dialog popups on tests that are expected to crash a subprocess.
On Windows, it disables Windows Error Reporting dialogs using
On UNIX, [`resource.setrlimit()`](https://docs.python.org/3/library/resource.html#resource.setrlimit "resource.setrlimit") is used to set [`resource.RLIMIT_CORE`](https://docs.python.org/3/library/resource.html#resource.RLIMIT_CORE "resource.RLIMIT_CORE")’s soft limit to 0 to prevent coredump file creation.
On both platforms, the old value is restored by [`__exit__()`](https://docs.python.org/3/reference/datamodel.html#object.__exit__ "object.__exit__").

_class_ test.support.SaveSignals[¶](https://docs.python.org/3/library/test.html#test.support.SaveSignals "Link to this definition")

Class to save and restore signal handlers registered by the Python signal handler.

save(_self_)[¶](https://docs.python.org/3/library/test.html#test.support.SaveSignals.save "Link to this definition")

Save the signal handlers to a dictionary mapping signal numbers to the current signal handler.

restore(_self_)[¶](https://docs.python.org/3/library/test.html#test.support.SaveSignals.restore "Link to this definition")

Set the signal numbers from the [`save()`](https://docs.python.org/3/library/test.html#test.support.SaveSignals.save "test.support.SaveSignals.save") dictionary to the saved handler.

_class_ test.support.Matcher[¶](https://docs.python.org/3/library/test.html#test.support.Matcher "Link to this definition")


matches(_self_ , _d_ , _** kwargs_)[¶](https://docs.python.org/3/library/test.html#test.support.Matcher.matches "Link to this definition")

Try to match a single dict with the supplied arguments.

match_value(_self_ , _k_ , _dv_ , _v_)[¶](https://docs.python.org/3/library/test.html#test.support.Matcher.match_value "Link to this definition")

Try to match a single stored value (_dv_) with a supplied value (_v_).
