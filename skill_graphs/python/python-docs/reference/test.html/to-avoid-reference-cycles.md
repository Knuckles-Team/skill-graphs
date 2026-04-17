# (to avoid reference cycles)

```

Added in version 3.8.

test.support.threading_helper.run_concurrently(_worker_func_ , _nthreads_ , _args =()_, _kwargs ={}_)[¶](https://docs.python.org/3/library/test.html#test.support.threading_helper.run_concurrently "Link to this definition")

Run the worker function concurrently in multiple threads. Re-raises an exception if any thread raises one, after all threads have finished.
#  `test.support.os_helper` — Utilities for os tests[¶](https://docs.python.org/3/library/test.html#module-test.support.os_helper "Link to this heading")
The `test.support.os_helper` module provides support for os tests.
Added in version 3.10.

test.support.os_helper.FS_NONASCII[¶](https://docs.python.org/3/library/test.html#test.support.os_helper.FS_NONASCII "Link to this definition")

A non-ASCII character encodable by [`os.fsencode()`](https://docs.python.org/3/library/os.html#os.fsencode "os.fsencode").

test.support.os_helper.SAVEDCWD[¶](https://docs.python.org/3/library/test.html#test.support.os_helper.SAVEDCWD "Link to this definition")

Set to [`os.getcwd()`](https://docs.python.org/3/library/os.html#os.getcwd "os.getcwd").

test.support.os_helper.TESTFN[¶](https://docs.python.org/3/library/test.html#test.support.os_helper.TESTFN "Link to this definition")

Set to a name that is safe to use as the name of a temporary file. Any temporary file that is created should be closed and unlinked (removed).

test.support.os_helper.TESTFN_NONASCII[¶](https://docs.python.org/3/library/test.html#test.support.os_helper.TESTFN_NONASCII "Link to this definition")

Set to a filename containing the [`FS_NONASCII`](https://docs.python.org/3/library/test.html#test.support.os_helper.FS_NONASCII "test.support.os_helper.FS_NONASCII") character, if it exists. This guarantees that if the filename exists, it can be encoded and decoded with the default filesystem encoding. This allows tests that require a non-ASCII filename to be easily skipped on platforms where they can’t work.

test.support.os_helper.TESTFN_UNENCODABLE[¶](https://docs.python.org/3/library/test.html#test.support.os_helper.TESTFN_UNENCODABLE "Link to this definition")

Set to a filename (str type) that should not be able to be encoded by file system encoding in strict mode. It may be `None` if it’s not possible to generate such a filename.

test.support.os_helper.TESTFN_UNDECODABLE[¶](https://docs.python.org/3/library/test.html#test.support.os_helper.TESTFN_UNDECODABLE "Link to this definition")

Set to a filename (bytes type) that should not be able to be decoded by file system encoding in strict mode. It may be `None` if it’s not possible to generate such a filename.

test.support.os_helper.TESTFN_UNICODE[¶](https://docs.python.org/3/library/test.html#test.support.os_helper.TESTFN_UNICODE "Link to this definition")

Set to a non-ASCII name for a temporary file.

_class_ test.support.os_helper.EnvironmentVarGuard[¶](https://docs.python.org/3/library/test.html#test.support.os_helper.EnvironmentVarGuard "Link to this definition")

Class used to temporarily set or unset environment variables. Instances can be used as a context manager and have a complete dictionary interface for querying/modifying the underlying `os.environ`. After exit from the context manager all changes to environment variables done through this instance will be rolled back.
Changed in version 3.1: Added dictionary interface.

_class_ test.support.os_helper.FakePath(_path_)[¶](https://docs.python.org/3/library/test.html#test.support.os_helper.FakePath "Link to this definition")

Simple [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object). It implements the [`__fspath__()`](https://docs.python.org/3/library/os.html#os.PathLike.__fspath__ "os.PathLike.__fspath__") method which just returns the _path_ argument. If _path_ is an exception, it will be raised in `__fspath__()`.

EnvironmentVarGuard.set(_envvar_ , _value_)[¶](https://docs.python.org/3/library/test.html#test.support.os_helper.EnvironmentVarGuard.set "Link to this definition")

Temporarily set the environment variable `envvar` to the value of `value`.

EnvironmentVarGuard.unset(_envvar_ , _* others_)[¶](https://docs.python.org/3/library/test.html#test.support.os_helper.EnvironmentVarGuard.unset "Link to this definition")

Temporarily unset one or more environment variables.
Changed in version 3.14: More than one environment variable can be unset.

test.support.os_helper.can_symlink()[¶](https://docs.python.org/3/library/test.html#test.support.os_helper.can_symlink "Link to this definition")

Return `True` if the OS supports symbolic links, `False` otherwise.

test.support.os_helper.can_xattr()[¶](https://docs.python.org/3/library/test.html#test.support.os_helper.can_xattr "Link to this definition")

Return `True` if the OS supports xattr, `False` otherwise.

test.support.os_helper.change_cwd(_path_ , _quiet =False_)[¶](https://docs.python.org/3/library/test.html#test.support.os_helper.change_cwd "Link to this definition")

A context manager that temporarily changes the current working directory to _path_ and yields the directory.
If _quiet_ is `False`, the context manager raises an exception on error. Otherwise, it issues only a warning and keeps the current working directory the same.

test.support.os_helper.create_empty_file(_filename_)[¶](https://docs.python.org/3/library/test.html#test.support.os_helper.create_empty_file "Link to this definition")

Create an empty file with _filename_. If it already exists, truncate it.

test.support.os_helper.fd_count()[¶](https://docs.python.org/3/library/test.html#test.support.os_helper.fd_count "Link to this definition")

Count the number of open file descriptors.

test.support.os_helper.fs_is_case_insensitive(_directory_)[¶](https://docs.python.org/3/library/test.html#test.support.os_helper.fs_is_case_insensitive "Link to this definition")

Return `True` if the file system for _directory_ is case-insensitive.

test.support.os_helper.make_bad_fd()[¶](https://docs.python.org/3/library/test.html#test.support.os_helper.make_bad_fd "Link to this definition")

Create an invalid file descriptor by opening and closing a temporary file, and returning its descriptor.

test.support.os_helper.rmdir(_filename_)[¶](https://docs.python.org/3/library/test.html#test.support.os_helper.rmdir "Link to this definition")

Call [`os.rmdir()`](https://docs.python.org/3/library/os.html#os.rmdir "os.rmdir") on _filename_. On Windows platforms, this is wrapped with a wait loop that checks for the existence of the file, which is needed due to antivirus programs that can hold files open and prevent deletion.

test.support.os_helper.rmtree(_path_)[¶](https://docs.python.org/3/library/test.html#test.support.os_helper.rmtree "Link to this definition")

Call [`shutil.rmtree()`](https://docs.python.org/3/library/shutil.html#shutil.rmtree "shutil.rmtree") on _path_ or call [`os.lstat()`](https://docs.python.org/3/library/os.html#os.lstat "os.lstat") and [`os.rmdir()`](https://docs.python.org/3/library/os.html#os.rmdir "os.rmdir") to remove a path and its contents. As with [`rmdir()`](https://docs.python.org/3/library/test.html#test.support.os_helper.rmdir "test.support.os_helper.rmdir"), on Windows platforms this is wrapped with a wait loop that checks for the existence of the files.

@test.support.os_helper.skip_unless_symlink[¶](https://docs.python.org/3/library/test.html#test.support.os_helper.skip_unless_symlink "Link to this definition")

A decorator for running tests that require support for symbolic links.

@test.support.os_helper.skip_unless_xattr[¶](https://docs.python.org/3/library/test.html#test.support.os_helper.skip_unless_xattr "Link to this definition")

A decorator for running tests that require support for xattr.

test.support.os_helper.temp_cwd(_name ='tempcwd'_, _quiet =False_)[¶](https://docs.python.org/3/library/test.html#test.support.os_helper.temp_cwd "Link to this definition")

A context manager that temporarily creates a new directory and changes the current working directory (CWD).
The context manager creates a temporary directory in the current directory with name _name_ before temporarily changing the current working directory. If _name_ is `None`, the temporary directory is created using [`tempfile.mkdtemp()`](https://docs.python.org/3/library/tempfile.html#tempfile.mkdtemp "tempfile.mkdtemp").
If _quiet_ is `False` and it is not possible to create or change the CWD, an error is raised. Otherwise, only a warning is raised and the original CWD is used.

test.support.os_helper.temp_dir(_path =None_, _quiet =False_)[¶](https://docs.python.org/3/library/test.html#test.support.os_helper.temp_dir "Link to this definition")

A context manager that creates a temporary directory at _path_ and yields the directory.
If _path_ is `None`, the temporary directory is created using [`tempfile.mkdtemp()`](https://docs.python.org/3/library/tempfile.html#tempfile.mkdtemp "tempfile.mkdtemp"). If _quiet_ is `False`, the context manager raises an exception on error. Otherwise, if _path_ is specified and cannot be created, only a warning is issued.

test.support.os_helper.temp_umask(_umask_)[¶](https://docs.python.org/3/library/test.html#test.support.os_helper.temp_umask "Link to this definition")

A context manager that temporarily sets the process umask.

test.support.os_helper.unlink(_filename_)[¶](https://docs.python.org/3/library/test.html#test.support.os_helper.unlink "Link to this definition")

Call [`os.unlink()`](https://docs.python.org/3/library/os.html#os.unlink "os.unlink") on _filename_. As with [`rmdir()`](https://docs.python.org/3/library/test.html#test.support.os_helper.rmdir "test.support.os_helper.rmdir"), on Windows platforms, this is wrapped with a wait loop that checks for the existence of the file.
#  `test.support.import_helper` — Utilities for import tests[¶](https://docs.python.org/3/library/test.html#module-test.support.import_helper "Link to this heading")
The `test.support.import_helper` module provides support for import tests.
Added in version 3.10.

test.support.import_helper.forget(_module_name_)[¶](https://docs.python.org/3/library/test.html#test.support.import_helper.forget "Link to this definition")

Remove the module named _module_name_ from `sys.modules` and delete any byte-compiled files of the module.

test.support.import_helper.import_fresh_module(_name_ , _fresh =()_, _blocked =()_, _deprecated =False_)[¶](https://docs.python.org/3/library/test.html#test.support.import_helper.import_fresh_module "Link to this definition")

This function imports and returns a fresh copy of the named Python module by removing the named module from `sys.modules` before doing the import. Note that unlike `reload()`, the original module is not affected by this operation.
_fresh_ is an iterable of additional module names that are also removed from the `sys.modules` cache before doing the import.
_blocked_ is an iterable of module names that are replaced with `None` in the module cache during the import to ensure that attempts to import them raise [`ImportError`](https://docs.python.org/3/library/exceptions.html#ImportError "ImportError").
The named module and any modules named in the _fresh_ and _blocked_ parameters are saved before starting the import and then reinserted into `sys.modules` when the fresh import is complete.
Module and package deprecation messages are suppressed during this import if _deprecated_ is `True`.
This function will raise [`ImportError`](https://docs.python.org/3/library/exceptions.html#ImportError "ImportError") if the named module cannot be imported.
Example use:
Copy```
# Get copies of the warnings module for testing without affecting the
# version being used by the rest of the test suite. One copy uses the
# C implementation, the other is forced to use the pure Python fallback
# implementation
py_warnings = import_fresh_module('warnings', blocked=['_warnings'])
c_warnings = import_fresh_module('warnings', fresh=['_warnings'])

```

Added in version 3.1.

test.support.import_helper.import_module(_name_ , _deprecated =False_, _*_ , _required_on =()_)[¶](https://docs.python.org/3/library/test.html#test.support.import_helper.import_module "Link to this definition")

This function imports and returns the named module. Unlike a normal import, this function raises [`unittest.SkipTest`](https://docs.python.org/3/library/unittest.html#unittest.SkipTest "unittest.SkipTest") if the module cannot be imported.
Module and package deprecation messages are suppressed during this import if _deprecated_ is `True`. If a module is required on a platform but optional for others, set _required_on_ to an iterable of platform prefixes which will be compared against [`sys.platform`](https://docs.python.org/3/library/sys.html#sys.platform "sys.platform").
Added in version 3.1.

test.support.import_helper.modules_setup()[¶](https://docs.python.org/3/library/test.html#test.support.import_helper.modules_setup "Link to this definition")

Return a copy of [`sys.modules`](https://docs.python.org/3/library/sys.html#sys.modules "sys.modules").

test.support.import_helper.modules_cleanup(_oldmodules_)[¶](https://docs.python.org/3/library/test.html#test.support.import_helper.modules_cleanup "Link to this definition")

Remove modules except for _oldmodules_ and `encodings` in order to preserve internal cache.

test.support.import_helper.unload(_name_)[¶](https://docs.python.org/3/library/test.html#test.support.import_helper.unload "Link to this definition")

Delete _name_ from `sys.modules`.

test.support.import_helper.make_legacy_pyc(_source_)[¶](https://docs.python.org/3/library/test.html#test.support.import_helper.make_legacy_pyc "Link to this definition")

Move a [**PEP 3147**](https://peps.python.org/pep-3147/)/[**PEP 488**](https://peps.python.org/pep-0488/) pyc file to its legacy pyc location and return the file system path to the legacy pyc file. The _source_ value is the file system path to the source file. It does not need to exist, however the PEP 3147/488 pyc file must exist.

_class_ test.support.import_helper.CleanImport(_* module_names_)[¶](https://docs.python.org/3/library/test.html#test.support.import_helper.CleanImport "Link to this definition")

A context manager to force import to return a new module reference. This is useful for testing module-level behaviors, such as the emission of a [`DeprecationWarning`](https://docs.python.org/3/library/exceptions.html#DeprecationWarning "DeprecationWarning") on import. Example usage:
Copy```
with CleanImport('foo'):
    importlib.import_module('foo')  # New reference.

```


_class_ test.support.import_helper.DirsOnSysPath(_* paths_)[¶](https://docs.python.org/3/library/test.html#test.support.import_helper.DirsOnSysPath "Link to this definition")

A context manager to temporarily add directories to [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path").
This makes a copy of [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path"), appends any directories given as positional arguments, then reverts `sys.path` to the copied settings when the context ends.
Note that _all_ [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path") modifications in the body of the context manager, including replacement of the object, will be reverted at the end of the block.
#  `test.support.warnings_helper` — Utilities for warnings tests[¶](https://docs.python.org/3/library/test.html#module-test.support.warnings_helper "Link to this heading")
The `test.support.warnings_helper` module provides support for warnings tests.
Added in version 3.10.

test.support.warnings_helper.ignore_warnings(_*_ , _category_)[¶](https://docs.python.org/3/library/test.html#test.support.warnings_helper.ignore_warnings "Link to this definition")

Suppress warnings that are instances of _category_ , which must be [`Warning`](https://docs.python.org/3/library/exceptions.html#Warning "Warning") or a subclass. Roughly equivalent to [`warnings.catch_warnings()`](https://docs.python.org/3/library/warnings.html#warnings.catch_warnings "warnings.catch_warnings") with [`warnings.simplefilter('ignore', category=category)`](https://docs.python.org/3/library/warnings.html#warnings.simplefilter "warnings.simplefilter"). For example:
Copy```
@warning_helper.ignore_warnings(category=DeprecationWarning)
def test_suppress_warning():
    # do something

```

Added in version 3.8.

test.support.warnings_helper.check_no_resource_warning(_testcase_)[¶](https://docs.python.org/3/library/test.html#test.support.warnings_helper.check_no_resource_warning "Link to this definition")

Context manager to check that no [`ResourceWarning`](https://docs.python.org/3/library/exceptions.html#ResourceWarning "ResourceWarning") was raised. You must remove the object which may emit `ResourceWarning` before the end of the context manager.

test.support.warnings_helper.check_syntax_warning(_testcase_ , _statement_ , _errtext =''_, _*_ , _lineno =1_, _offset =None_)[¶](https://docs.python.org/3/library/test.html#test.support.warnings_helper.check_syntax_warning "Link to this definition")

Test for syntax warning in _statement_ by attempting to compile _statement_. Test also that the [`SyntaxWarning`](https://docs.python.org/3/library/exceptions.html#SyntaxWarning "SyntaxWarning") is emitted only once, and that it will be converted to a [`SyntaxError`](https://docs.python.org/3/library/exceptions.html#SyntaxError "SyntaxError") when turned into error. _testcase_ is the [`unittest`](https://docs.python.org/3/library/unittest.html#module-unittest "unittest: Unit testing framework for Python.") instance for the test. _errtext_ is the regular expression which should match the string representation of the emitted `SyntaxWarning` and raised `SyntaxError`. If _lineno_ is not `None`, compares to the line of the warning and exception. If _offset_ is not `None`, compares to the offset of the exception.
Added in version 3.8.

test.support.warnings_helper.check_warnings(_* filters_, _quiet =True_)[¶](https://docs.python.org/3/library/test.html#test.support.warnings_helper.check_warnings "Link to this definition")

A convenience wrapper for [`warnings.catch_warnings()`](https://docs.python.org/3/library/warnings.html#warnings.catch_warnings "warnings.catch_warnings") that makes it easier to test that a warning was correctly raised. It is approximately equivalent to calling `warnings.catch_warnings(record=True)` with [`warnings.simplefilter()`](https://docs.python.org/3/library/warnings.html#warnings.simplefilter "warnings.simplefilter") set to `always` and with the option to automatically validate the results that are recorded.
`check_warnings` accepts 2-tuples of the form `("message regexp", WarningCategory)` as positional arguments. If one or more _filters_ are provided, or if the optional keyword argument _quiet_ is `False`, it checks to make sure the warnings are as expected: each specified filter must match at least one of the warnings raised by the enclosed code or the test fails, and if any warnings are raised that do not match any of the specified filters the test fails. To disable the first of these checks, set _quiet_ to `True`.
If no arguments are specified, it defaults to:
Copy```
check_warnings(("", Warning), quiet=True)

```

In this case all warnings are caught and no errors are raised.
On entry to the context manager, a `WarningRecorder` instance is returned. The underlying warnings list from [`catch_warnings()`](https://docs.python.org/3/library/warnings.html#warnings.catch_warnings "warnings.catch_warnings") is available via the recorder object’s [`warnings`](https://docs.python.org/3/library/warnings.html#module-warnings "warnings: Issue warning messages and control their disposition.") attribute. As a convenience, the attributes of the object representing the most recent warning can also be accessed directly through the recorder object (see example below). If no warning has been raised, then any of the attributes that would otherwise be expected on an object representing a warning will return `None`.
The recorder object also has a `reset()` method, which clears the warnings list.
The context manager is designed to be used like this:
Copy```
with check_warnings(("assertion is always true", SyntaxWarning),
                    ("", UserWarning)):
    exec('assert(False, "Hey!")')
    warnings.warn(UserWarning("Hide me!"))

```

In this case if either warning was not raised, or some other warning was raised, `check_warnings()` would raise an error.
When a test needs to look more deeply into the warnings, rather than just checking whether or not they occurred, code like this can be used:
Copy```
with check_warnings(quiet=True) as w:
    warnings.warn("foo")
    assert str(w.args[0]) == "foo"
    warnings.warn("bar")
    assert str(w.args[0]) == "bar"
    assert str(w.warnings[0].args[0]) == "foo"
    assert str(w.warnings[1].args[0]) == "bar"
    w.reset()
    assert len(w.warnings) == 0

```

Here all warnings will be caught, and the test code tests the captured warnings directly.
Changed in version 3.2: New optional arguments _filters_ and _quiet_.

_class_ test.support.warnings_helper.WarningsRecorder[¶](https://docs.python.org/3/library/test.html#test.support.warnings_helper.WarningsRecorder "Link to this definition")

Class used to record warnings for unit tests. See documentation of [`check_warnings()`](https://docs.python.org/3/library/test.html#test.support.warnings_helper.check_warnings "test.support.warnings_helper.check_warnings") above for more details.
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`test` — Regression tests package for Python](https://docs.python.org/3/library/test.html)
    * [Writing Unit Tests for the `test` package](https://docs.python.org/3/library/test.html#writing-unit-tests-for-the-test-package)
    * [Running tests using the command-line interface](https://docs.python.org/3/library/test.html#module-test.regrtest)
  * [`test.support` — Utilities for the Python test suite](https://docs.python.org/3/library/test.html#module-test.support)
  * [`test.support.socket_helper` — Utilities for socket tests](https://docs.python.org/3/library/test.html#module-test.support.socket_helper)
  * [`test.support.script_helper` — Utilities for the Python execution tests](https://docs.python.org/3/library/test.html#module-test.support.script_helper)
  * [`test.support.bytecode_helper` — Support tools for testing correct bytecode generation](https://docs.python.org/3/library/test.html#module-test.support.bytecode_helper)
  * [`test.support.threading_helper` — Utilities for threading tests](https://docs.python.org/3/library/test.html#module-test.support.threading_helper)
  * [`test.support.os_helper` — Utilities for os tests](https://docs.python.org/3/library/test.html#module-test.support.os_helper)
  * [`test.support.import_helper` — Utilities for import tests](https://docs.python.org/3/library/test.html#module-test.support.import_helper)
  * [`test.support.warnings_helper` — Utilities for warnings tests](https://docs.python.org/3/library/test.html#module-test.support.warnings_helper)


#### Previous topic
[`unittest.mock` — getting started](https://docs.python.org/3/library/unittest.mock-examples.html "previous chapter")
#### Next topic
[Debugging and Profiling](https://docs.python.org/3/library/debug.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=test+%E2%80%94+Regression+tests+package+for+Python&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ftest.html&pagesource=library%2Ftest.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/debug.html "Debugging and Profiling") |
  * [previous](https://docs.python.org/3/library/unittest.mock-examples.html "unittest.mock — getting started") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Development Tools](https://docs.python.org/3/library/development.html) »
  * [`test` — Regression tests package for Python](https://docs.python.org/3/library/test.html)
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
  *[*]: Keyword-only parameters separator (PEP 3102)
