**CPython implementation detail:** This function should be used for specialized purposes only. It is not guaranteed to exist in all implementations of Python.
Changed in version 3.14: The result may include objects from other interpreters.

sys.getprofile()[¶](https://docs.python.org/3/library/sys.html#sys.getprofile "Link to this definition")

Get the profiler function as set by [`setprofile()`](https://docs.python.org/3/library/sys.html#sys.setprofile "sys.setprofile").

sys.gettrace()[¶](https://docs.python.org/3/library/sys.html#sys.gettrace "Link to this definition")

Get the trace function as set by [`settrace()`](https://docs.python.org/3/library/sys.html#sys.settrace "sys.settrace").
**CPython implementation detail:** The `gettrace()` function is intended only for implementing debuggers, profilers, coverage tools and the like. Its behavior is part of the implementation platform, rather than part of the language definition, and thus may not be available in all Python implementations.

sys.getwindowsversion()[¶](https://docs.python.org/3/library/sys.html#sys.getwindowsversion "Link to this definition")

Return a named tuple describing the Windows version currently running. The named elements are _major_ , _minor_ , _build_ , _platform_ , _service_pack_ , _service_pack_minor_ , _service_pack_major_ , _suite_mask_ , _product_type_ and _platform_version_. _service_pack_ contains a string, _platform_version_ a 3-tuple and all other values are integers. The components can also be accessed by name, so `sys.getwindowsversion()[0]` is equivalent to `sys.getwindowsversion().major`. For compatibility with prior versions, only the first 5 elements are retrievable by indexing.
_platform_ will be `2` (VER_PLATFORM_WIN32_NT).
_product_type_ may be one of the following values:
Constant | Meaning
---|---
`1` (VER_NT_WORKSTATION) | The system is a workstation.
`2` (VER_NT_DOMAIN_CONTROLLER) | The system is a domain controller.
`3` (VER_NT_SERVER) | The system is a server, but not a domain controller.
This function wraps the Win32 `GetVersionEx()` function; see the Microsoft documentation on `OSVERSIONINFOEX()` for more information about these fields.
_platform_version_ returns the major version, minor version and build number of the current operating system, rather than the version that is being emulated for the process. It is intended for use in logging rather than for feature detection.
Note
_platform_version_ derives the version from kernel32.dll which can be of a different version than the OS version. Please use [`platform`](https://docs.python.org/3/library/platform.html#module-platform "platform: Retrieves as much platform identifying data as possible.") module for achieving accurate OS version.
[Availability](https://docs.python.org/3/library/intro.html#availability): Windows.
Changed in version 3.2: Changed to a named tuple and added _service_pack_minor_ , _service_pack_major_ , _suite_mask_ , and _product_type_.
Changed in version 3.6: Added _platform_version_

sys.get_asyncgen_hooks()[¶](https://docs.python.org/3/library/sys.html#sys.get_asyncgen_hooks "Link to this definition")

Returns an _asyncgen_hooks_ object, which is similar to a [`namedtuple`](https://docs.python.org/3/library/collections.html#collections.namedtuple "collections.namedtuple") of the form `(firstiter, finalizer)`, where _firstiter_ and _finalizer_ are expected to be either `None` or functions which take an [asynchronous generator iterator](https://docs.python.org/3/glossary.html#term-asynchronous-generator-iterator) as an argument, and are used to schedule finalization of an asynchronous generator by an event loop.
Added in version 3.6: See [**PEP 525**](https://peps.python.org/pep-0525/) for more details.
Note
This function has been added on a provisional basis (see [**PEP 411**](https://peps.python.org/pep-0411/) for details.)

sys.get_coroutine_origin_tracking_depth()[¶](https://docs.python.org/3/library/sys.html#sys.get_coroutine_origin_tracking_depth "Link to this definition")

Get the current coroutine origin tracking depth, as set by [`set_coroutine_origin_tracking_depth()`](https://docs.python.org/3/library/sys.html#sys.set_coroutine_origin_tracking_depth "sys.set_coroutine_origin_tracking_depth").
Added in version 3.7.
Note
This function has been added on a provisional basis (see [**PEP 411**](https://peps.python.org/pep-0411/) for details.) Use it only for debugging purposes.

sys.hash_info[¶](https://docs.python.org/3/library/sys.html#sys.hash_info "Link to this definition")

A [named tuple](https://docs.python.org/3/glossary.html#term-named-tuple) giving parameters of the numeric hash implementation. For more details about hashing of numeric types, see [Hashing of numeric types](https://docs.python.org/3/library/stdtypes.html#numeric-hash).

hash_info.width[¶](https://docs.python.org/3/library/sys.html#sys.hash_info.width "Link to this definition")

The width in bits used for hash values

hash_info.modulus[¶](https://docs.python.org/3/library/sys.html#sys.hash_info.modulus "Link to this definition")

The prime modulus P used for numeric hash scheme

hash_info.inf[¶](https://docs.python.org/3/library/sys.html#sys.hash_info.inf "Link to this definition")

The hash value returned for a positive infinity

hash_info.nan[¶](https://docs.python.org/3/library/sys.html#sys.hash_info.nan "Link to this definition")

(This attribute is no longer used)

hash_info.imag[¶](https://docs.python.org/3/library/sys.html#sys.hash_info.imag "Link to this definition")

The multiplier used for the imaginary part of a complex number

hash_info.algorithm[¶](https://docs.python.org/3/library/sys.html#sys.hash_info.algorithm "Link to this definition")

The name of the algorithm for hashing of str, bytes, and memoryview

hash_info.hash_bits[¶](https://docs.python.org/3/library/sys.html#sys.hash_info.hash_bits "Link to this definition")

The internal output size of the hash algorithm

hash_info.seed_bits[¶](https://docs.python.org/3/library/sys.html#sys.hash_info.seed_bits "Link to this definition")

The size of the seed key of the hash algorithm

hash_info.cutoff[¶](https://docs.python.org/3/library/sys.html#sys.hash_info.cutoff "Link to this definition")

Cutoff for small string DJBX33A optimization in range `[1, cutoff)`.
Added in version 3.2.
Changed in version 3.4: Added _algorithm_ , _hash_bits_ , _seed_bits_ , and _cutoff_.

sys.hexversion[¶](https://docs.python.org/3/library/sys.html#sys.hexversion "Link to this definition")

The version number encoded as a single integer. This is guaranteed to increase with each version, including proper support for non-production releases. For example, to test that the Python interpreter is at least version 1.5.2, use:
Copy```
if sys.hexversion >= 0x010502F0:
    # use some advanced feature
    ...
else:
    # use an alternative implementation or warn the user
    ...

```

This is called `hexversion` since it only really looks meaningful when viewed as the result of passing it to the built-in [`hex()`](https://docs.python.org/3/library/functions.html#hex "hex") function. The [named tuple](https://docs.python.org/3/glossary.html#term-named-tuple) [`sys.version_info`](https://docs.python.org/3/library/sys.html#sys.version_info "sys.version_info") may be used for a more human-friendly encoding of the same information.
More details of `hexversion` can be found at [API and ABI Versioning](https://docs.python.org/3/c-api/apiabiversion.html#apiabiversion).

sys.implementation[¶](https://docs.python.org/3/library/sys.html#sys.implementation "Link to this definition")

An object containing information about the implementation of the currently running Python interpreter. The following attributes are required to exist in all Python implementations.
_name_ is the implementation’s identifier, e.g. `'cpython'`. The actual string is defined by the Python implementation, but it is guaranteed to be lower case.
_version_ is a named tuple, in the same format as [`sys.version_info`](https://docs.python.org/3/library/sys.html#sys.version_info "sys.version_info"). It represents the version of the Python _implementation_. This has a distinct meaning from the specific version of the Python _language_ to which the currently running interpreter conforms, which `sys.version_info` represents. For example, for PyPy 1.8 `sys.implementation.version` might be `sys.version_info(1, 8, 0, 'final', 0)`, whereas `sys.version_info` would be `sys.version_info(2, 7, 2, 'final', 0)`. For CPython they are the same value, since it is the reference implementation.
_hexversion_ is the implementation version in hexadecimal format, like [`sys.hexversion`](https://docs.python.org/3/library/sys.html#sys.hexversion "sys.hexversion").
_cache_tag_ is the tag used by the import machinery in the filenames of cached modules. By convention, it would be a composite of the implementation’s name and version, like `'cpython-33'`. However, a Python implementation may use some other value if appropriate. If `cache_tag` is set to `None`, it indicates that module caching should be disabled.
_supports_isolated_interpreters_ is a boolean value, whether this implementation supports multiple isolated interpreters. It is `True` for CPython on most platforms. Platforms with this support implement the low-level `_interpreters` module.
See also
[**PEP 684**](https://peps.python.org/pep-0684/), [**PEP 734**](https://peps.python.org/pep-0734/), and [`concurrent.interpreters`](https://docs.python.org/3/library/concurrent.interpreters.html#module-concurrent.interpreters "concurrent.interpreters: Multiple interpreters in the same process").
[`sys.implementation`](https://docs.python.org/3/library/sys.html#sys.implementation "sys.implementation") may contain additional attributes specific to the Python implementation. These non-standard attributes must start with an underscore, and are not described here. Regardless of its contents, `sys.implementation` will not change during a run of the interpreter, nor between implementation versions. (It may change between Python language versions, however.) See [**PEP 421**](https://peps.python.org/pep-0421/) for more information.
Added in version 3.3.
Changed in version 3.14: Added `supports_isolated_interpreters` field.
Note
The addition of new required attributes must go through the normal PEP process. See [**PEP 421**](https://peps.python.org/pep-0421/) for more information.

sys.int_info[¶](https://docs.python.org/3/library/sys.html#sys.int_info "Link to this definition")

A [named tuple](https://docs.python.org/3/glossary.html#term-named-tuple) that holds information about Python’s internal representation of integers. The attributes are read only.

int_info.bits_per_digit[¶](https://docs.python.org/3/library/sys.html#sys.int_info.bits_per_digit "Link to this definition")

The number of bits held in each digit. Python integers are stored internally in base `2**int_info.bits_per_digit`.

int_info.sizeof_digit[¶](https://docs.python.org/3/library/sys.html#sys.int_info.sizeof_digit "Link to this definition")

The size in bytes of the C type used to represent a digit.

int_info.default_max_str_digits[¶](https://docs.python.org/3/library/sys.html#sys.int_info.default_max_str_digits "Link to this definition")

The default value for [`sys.get_int_max_str_digits()`](https://docs.python.org/3/library/sys.html#sys.get_int_max_str_digits "sys.get_int_max_str_digits") when it is not otherwise explicitly configured.

int_info.str_digits_check_threshold[¶](https://docs.python.org/3/library/sys.html#sys.int_info.str_digits_check_threshold "Link to this definition")

The minimum non-zero value for [`sys.set_int_max_str_digits()`](https://docs.python.org/3/library/sys.html#sys.set_int_max_str_digits "sys.set_int_max_str_digits"), [`PYTHONINTMAXSTRDIGITS`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONINTMAXSTRDIGITS), or [`-X int_max_str_digits`](https://docs.python.org/3/using/cmdline.html#cmdoption-X).
Added in version 3.1.
Changed in version 3.11: Added [`default_max_str_digits`](https://docs.python.org/3/library/sys.html#sys.int_info.default_max_str_digits "sys.int_info.default_max_str_digits") and [`str_digits_check_threshold`](https://docs.python.org/3/library/sys.html#sys.int_info.str_digits_check_threshold "sys.int_info.str_digits_check_threshold").

sys.__interactivehook__[¶](https://docs.python.org/3/library/sys.html#sys.__interactivehook__ "Link to this definition")

When this attribute exists, its value is automatically called (with no arguments) when the interpreter is launched in [interactive mode](https://docs.python.org/3/tutorial/interpreter.html#tut-interactive). This is done after the [`PYTHONSTARTUP`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONSTARTUP) file is read, so that you can set this hook there. The [`site`](https://docs.python.org/3/library/site.html#module-site "site: Module responsible for site-specific configuration.") module [sets this](https://docs.python.org/3/library/site.html#rlcompleter-config).
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `cpython.run_interactivehook` with the hook object as the argument when the hook is called on startup.
Added in version 3.4.

sys.intern(_string_)[¶](https://docs.python.org/3/library/sys.html#sys.intern "Link to this definition")

Enter _string_ in the table of “interned” strings and return the interned string – which is _string_ itself or a copy. Interning strings is useful to gain a little performance on dictionary lookup – if the keys in a dictionary are interned, and the lookup key is interned, the key comparisons (after hashing) can be done by a pointer compare instead of a string compare. Normally, the names used in Python programs are automatically interned, and the dictionaries used to hold module, class or instance attributes have interned keys.
Interned strings are not [immortal](https://docs.python.org/3/glossary.html#term-immortal); you must keep a reference to the return value of `intern()` around to benefit from it.

sys._is_gil_enabled()[¶](https://docs.python.org/3/library/sys.html#sys._is_gil_enabled "Link to this definition")

Return [`True`](https://docs.python.org/3/library/constants.html#True "True") if the [GIL](https://docs.python.org/3/glossary.html#term-GIL) is enabled and [`False`](https://docs.python.org/3/library/constants.html#False "False") if it is disabled.
Added in version 3.13.
**CPython implementation detail:** It is not guaranteed to exist in all implementations of Python.

sys.is_finalizing()[¶](https://docs.python.org/3/library/sys.html#sys.is_finalizing "Link to this definition")

Return [`True`](https://docs.python.org/3/library/constants.html#True "True") if the main Python interpreter is [shutting down](https://docs.python.org/3/glossary.html#term-interpreter-shutdown). Return [`False`](https://docs.python.org/3/library/constants.html#False "False") otherwise.
See also the [`PythonFinalizationError`](https://docs.python.org/3/library/exceptions.html#PythonFinalizationError "PythonFinalizationError") exception.
Added in version 3.5.

sys._jit[¶](https://docs.python.org/3/library/sys.html#sys._jit "Link to this definition")

Utilities for observing just-in-time compilation.
**CPython implementation detail:** JIT compilation is an _experimental implementation detail_ of CPython. `sys._jit` is not guaranteed to exist or behave the same way in all Python implementations, versions, or build configurations.
Added in version 3.14.

_jit.is_available()[¶](https://docs.python.org/3/library/sys.html#sys._jit.is_available "Link to this definition")

Return `True` if the current Python executable supports JIT compilation, and `False` otherwise. This can be controlled by building CPython with the `--experimental-jit` option on Windows, and the [`--enable-experimental-jit`](https://docs.python.org/3/using/configure.html#cmdoption-enable-experimental-jit) option on all other platforms.

_jit.is_enabled()[¶](https://docs.python.org/3/library/sys.html#sys._jit.is_enabled "Link to this definition")

Return `True` if JIT compilation is enabled for the current Python process (implies [`sys._jit.is_available()`](https://docs.python.org/3/library/sys.html#sys._jit.is_available "sys._jit.is_available")), and `False` otherwise. If JIT compilation is available, this can be controlled by setting the [`PYTHON_JIT`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_JIT) environment variable to `0` (disabled) or `1` (enabled) at interpreter startup.

_jit.is_active()[¶](https://docs.python.org/3/library/sys.html#sys._jit.is_active "Link to this definition")

Return `True` if the topmost Python frame is currently executing JIT code (implies [`sys._jit.is_enabled()`](https://docs.python.org/3/library/sys.html#sys._jit.is_enabled "sys._jit.is_enabled")), and `False` otherwise.
Note
This function is intended for testing and debugging the JIT itself. It should be avoided for any other purpose.
Note
Due to the nature of tracing JIT compilers, repeated calls to this function may give surprising results. For example, branching on its return value will likely lead to unexpected behavior (if doing so causes JIT code to be entered or exited):
Copy```
>>> for warmup in range(BIG_NUMBER):
...     # This line is "hot", and is eventually JIT-compiled:
...     if sys._jit.is_active():
...         # This line is "cold", and is run in the interpreter:
...         assert sys._jit.is_active()
...
Traceback (most recent call last):
  File "<stdin>", line 5, in <module>
    assert sys._jit.is_active()
           ~~~~~~~~~~~~~~~~~~^^
AssertionError

```


sys.last_exc[¶](https://docs.python.org/3/library/sys.html#sys.last_exc "Link to this definition")

This variable is not always defined; it is set to the exception instance when an exception is not handled and the interpreter prints an error message and a stack traceback. Its intended use is to allow an interactive user to import a debugger module and engage in post-mortem debugging without having to re-execute the command that caused the error. (Typical use is `import pdb; pdb.pm()` to enter the post-mortem debugger; see [`pdb`](https://docs.python.org/3/library/pdb.html#module-pdb "pdb: The Python debugger for interactive interpreters.") module for more information.)
Added in version 3.12.

sys._is_immortal(_op_)[¶](https://docs.python.org/3/library/sys.html#sys._is_immortal "Link to this definition")

Return [`True`](https://docs.python.org/3/library/constants.html#True "True") if the given object is [immortal](https://docs.python.org/3/glossary.html#term-immortal), [`False`](https://docs.python.org/3/library/constants.html#False "False") otherwise.
Note
Objects that are immortal (and thus return `True` upon being passed to this function) are not guaranteed to be immortal in future versions, and vice versa for mortal objects.
Added in version 3.14.
**CPython implementation detail:** This function should be used for specialized purposes only. It is not guaranteed to exist in all implementations of Python.

sys._is_interned(_string_)[¶](https://docs.python.org/3/library/sys.html#sys._is_interned "Link to this definition")

Return [`True`](https://docs.python.org/3/library/constants.html#True "True") if the given string is “interned”, [`False`](https://docs.python.org/3/library/constants.html#False "False") otherwise.
Added in version 3.13.
**CPython implementation detail:** It is not guaranteed to exist in all implementations of Python.

sys.last_type[¶](https://docs.python.org/3/library/sys.html#sys.last_type "Link to this definition")


sys.last_value[¶](https://docs.python.org/3/library/sys.html#sys.last_value "Link to this definition")


sys.last_traceback[¶](https://docs.python.org/3/library/sys.html#sys.last_traceback "Link to this definition")

These three variables are deprecated; use [`sys.last_exc`](https://docs.python.org/3/library/sys.html#sys.last_exc "sys.last_exc") instead. They hold the legacy representation of `sys.last_exc`, as returned from [`exc_info()`](https://docs.python.org/3/library/sys.html#sys.exc_info "sys.exc_info") above.

sys.maxsize[¶](https://docs.python.org/3/library/sys.html#sys.maxsize "Link to this definition")

An integer giving the maximum value a variable of type [`Py_ssize_t`](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t") can take. It’s usually `2**31 - 1` on a 32-bit platform and `2**63 - 1` on a 64-bit platform.

sys.maxunicode[¶](https://docs.python.org/3/library/sys.html#sys.maxunicode "Link to this definition")

An integer giving the value of the largest Unicode code point, i.e. `1114111` (`0x10FFFF` in hexadecimal).
Changed in version 3.3: Before [**PEP 393**](https://peps.python.org/pep-0393/), `sys.maxunicode` used to be either `0xFFFF` or `0x10FFFF`, depending on the configuration option that specified whether Unicode characters were stored as UCS-2 or UCS-4.

sys.meta_path[¶](https://docs.python.org/3/library/sys.html#sys.meta_path "Link to this definition")

A list of [meta path finder](https://docs.python.org/3/glossary.html#term-meta-path-finder) objects that have their [`find_spec()`](https://docs.python.org/3/library/importlib.html#importlib.abc.MetaPathFinder.find_spec "importlib.abc.MetaPathFinder.find_spec") methods called to see if one of the objects can find the module to be imported. By default, it holds entries that implement Python’s default import semantics. The `find_spec()` method is called with at least the absolute name of the module being imported. If the module to be imported is contained in a package, then the parent package’s [`__path__`](https://docs.python.org/3/reference/datamodel.html#module.__path__ "module.__path__") attribute is passed in as a second argument. The method returns a [module spec](https://docs.python.org/3/glossary.html#term-module-spec), or `None` if the module cannot be found.
See also

[`importlib.abc.MetaPathFinder`](https://docs.python.org/3/library/importlib.html#importlib.abc.MetaPathFinder "importlib.abc.MetaPathFinder")

The abstract base class defining the interface of finder objects on `meta_path`.

[`importlib.machinery.ModuleSpec`](https://docs.python.org/3/library/importlib.html#importlib.machinery.ModuleSpec "importlib.machinery.ModuleSpec")

The concrete class which [`find_spec()`](https://docs.python.org/3/library/importlib.html#importlib.abc.MetaPathFinder.find_spec "importlib.abc.MetaPathFinder.find_spec") should return instances of.
Changed in version 3.4: [Module specs](https://docs.python.org/3/glossary.html#term-module-spec) were introduced in Python 3.4, by [**PEP 451**](https://peps.python.org/pep-0451/).
Changed in version 3.12: Removed the fallback that looked for a `find_module()` method if a `meta_path` entry didn’t have a [`find_spec()`](https://docs.python.org/3/library/importlib.html#importlib.abc.MetaPathFinder.find_spec "importlib.abc.MetaPathFinder.find_spec") method.

sys.modules[¶](https://docs.python.org/3/library/sys.html#sys.modules "Link to this definition")

This is a dictionary that maps module names to modules which have already been loaded. This can be manipulated to force reloading of modules and other tricks. However, replacing the dictionary will not necessarily work as expected and deleting essential items from the dictionary may cause Python to fail. If you want to iterate over this global dictionary always use `sys.modules.copy()` or `tuple(sys.modules)` to avoid exceptions as its size may change during iteration as a side effect of code or activity in other threads.

sys.orig_argv[¶](https://docs.python.org/3/library/sys.html#sys.orig_argv "Link to this definition")

The list of the original command line arguments passed to the Python executable.
The elements of [`sys.orig_argv`](https://docs.python.org/3/library/sys.html#sys.orig_argv "sys.orig_argv") are the arguments to the Python interpreter, while the elements of [`sys.argv`](https://docs.python.org/3/library/sys.html#sys.argv "sys.argv") are the arguments to the user’s program. Arguments consumed by the interpreter itself will be present in `sys.orig_argv` and missing from `sys.argv`.
Added in version 3.10.

sys.path[¶](https://docs.python.org/3/library/sys.html#sys.path "Link to this definition")

A list of strings that specifies the search path for modules. Initialized from the environment variable [`PYTHONPATH`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH), plus an installation-dependent default.
By default, as initialized upon program startup, a potentially unsafe path is prepended to [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path") (_before_ the entries inserted as a result of [`PYTHONPATH`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH)):
  * `python -m module` command line: prepend the current working directory.
  * `python script.py` command line: prepend the script’s directory. If it’s a symbolic link, resolve symbolic links.
  * `python -c code` and `python` (REPL) command lines: prepend an empty string, which means the current working directory.


To not prepend this potentially unsafe path, use the [`-P`](https://docs.python.org/3/using/cmdline.html#cmdoption-P) command line option or the [`PYTHONSAFEPATH`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONSAFEPATH) environment variable.
