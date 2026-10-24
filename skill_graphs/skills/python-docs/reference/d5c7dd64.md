
sys.executable[¶](https://docs.python.org/3/library/sys.html#sys.executable "Link to this definition")

A string giving the absolute path of the executable binary for the Python interpreter, on systems where this makes sense. If Python is unable to retrieve the real path to its executable, [`sys.executable`](https://docs.python.org/3/library/sys.html#sys.executable "sys.executable") will be an empty string or `None`.

sys.exit([_arg_])[¶](https://docs.python.org/3/library/sys.html#sys.exit "Link to this definition")

Raise a [`SystemExit`](https://docs.python.org/3/library/exceptions.html#SystemExit "SystemExit") exception, signaling an intention to exit the interpreter.
The optional argument _arg_ can be an integer giving the exit status (defaulting to zero), or another type of object. If it is an integer, zero is considered “successful termination” and any nonzero value is considered “abnormal termination” by shells and the like. Most systems require it to be in the range 0–127, and produce undefined results otherwise. Some systems have a convention for assigning specific meanings to specific exit codes, but these are generally underdeveloped; Unix programs generally use 2 for command line syntax errors and 1 for all other kinds of errors. If another type of object is passed, `None` is equivalent to passing zero, and any other object is printed to [`stderr`](https://docs.python.org/3/library/sys.html#sys.stderr "sys.stderr") and results in an exit code of 1. In particular, `sys.exit("some error message")` is a quick way to exit a program when an error occurs.
Since `exit()` ultimately “only” raises an exception, it will only exit the process when called from the main thread, and the exception is not intercepted. Cleanup actions specified by finally clauses of [`try`](https://docs.python.org/3/reference/compound_stmts.html#try) statements are honored, and it is possible to intercept the exit attempt at an outer level.
Changed in version 3.6: If an error occurs in the cleanup after the Python interpreter has caught [`SystemExit`](https://docs.python.org/3/library/exceptions.html#SystemExit "SystemExit") (such as an error flushing buffered data in the standard streams), the exit status is changed to 120.

sys.flags[¶](https://docs.python.org/3/library/sys.html#sys.flags "Link to this definition")

The [named tuple](https://docs.python.org/3/glossary.html#term-named-tuple) _flags_ exposes the status of command line flags. Flags should only be accessed only by name and not by index. The attributes are read only.

flags.debug[¶](https://docs.python.org/3/library/sys.html#sys.flags.debug "Link to this definition")
| [`-d`](https://docs.python.org/3/using/cmdline.html#cmdoption-d)
---|---

flags.inspect[¶](https://docs.python.org/3/library/sys.html#sys.flags.inspect "Link to this definition")
| [`-i`](https://docs.python.org/3/using/cmdline.html#cmdoption-i)

flags.interactive[¶](https://docs.python.org/3/library/sys.html#sys.flags.interactive "Link to this definition")
| [`-i`](https://docs.python.org/3/using/cmdline.html#cmdoption-i)

flags.isolated[¶](https://docs.python.org/3/library/sys.html#sys.flags.isolated "Link to this definition")
| [`-I`](https://docs.python.org/3/using/cmdline.html#cmdoption-I)

flags.optimize[¶](https://docs.python.org/3/library/sys.html#sys.flags.optimize "Link to this definition")
| [`-O`](https://docs.python.org/3/using/cmdline.html#cmdoption-O) or [`-OO`](https://docs.python.org/3/using/cmdline.html#cmdoption-OO)

flags.dont_write_bytecode[¶](https://docs.python.org/3/library/sys.html#sys.flags.dont_write_bytecode "Link to this definition")
| [`-B`](https://docs.python.org/3/using/cmdline.html#cmdoption-B)

flags.no_user_site[¶](https://docs.python.org/3/library/sys.html#sys.flags.no_user_site "Link to this definition")
| [`-s`](https://docs.python.org/3/using/cmdline.html#cmdoption-s)

flags.no_site[¶](https://docs.python.org/3/library/sys.html#sys.flags.no_site "Link to this definition")
| [`-S`](https://docs.python.org/3/using/cmdline.html#cmdoption-S)

flags.ignore_environment[¶](https://docs.python.org/3/library/sys.html#sys.flags.ignore_environment "Link to this definition")
| [`-E`](https://docs.python.org/3/using/cmdline.html#cmdoption-E)

flags.verbose[¶](https://docs.python.org/3/library/sys.html#sys.flags.verbose "Link to this definition")
| [`-v`](https://docs.python.org/3/using/cmdline.html#cmdoption-v)

flags.bytes_warning[¶](https://docs.python.org/3/library/sys.html#sys.flags.bytes_warning "Link to this definition")
| [`-b`](https://docs.python.org/3/using/cmdline.html#cmdoption-b)

flags.quiet[¶](https://docs.python.org/3/library/sys.html#sys.flags.quiet "Link to this definition")
| [`-q`](https://docs.python.org/3/using/cmdline.html#cmdoption-q)

flags.hash_randomization[¶](https://docs.python.org/3/library/sys.html#sys.flags.hash_randomization "Link to this definition")
| [`-R`](https://docs.python.org/3/using/cmdline.html#cmdoption-R)

flags.dev_mode[¶](https://docs.python.org/3/library/sys.html#sys.flags.dev_mode "Link to this definition")
| [`-X dev`](https://docs.python.org/3/using/cmdline.html#cmdoption-X) ([Python Development Mode](https://docs.python.org/3/library/devmode.html#devmode))

flags.utf8_mode[¶](https://docs.python.org/3/library/sys.html#sys.flags.utf8_mode "Link to this definition")
| [`-X utf8`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)

flags.safe_path[¶](https://docs.python.org/3/library/sys.html#sys.flags.safe_path "Link to this definition")
| [`-P`](https://docs.python.org/3/using/cmdline.html#cmdoption-P)

flags.int_max_str_digits[¶](https://docs.python.org/3/library/sys.html#sys.flags.int_max_str_digits "Link to this definition")
| [`-X int_max_str_digits`](https://docs.python.org/3/using/cmdline.html#cmdoption-X) ([integer string conversion length limitation](https://docs.python.org/3/library/stdtypes.html#int-max-str-digits))

flags.warn_default_encoding[¶](https://docs.python.org/3/library/sys.html#sys.flags.warn_default_encoding "Link to this definition")
| [`-X warn_default_encoding`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)

flags.gil[¶](https://docs.python.org/3/library/sys.html#sys.flags.gil "Link to this definition")
| [`-X gil`](https://docs.python.org/3/using/cmdline.html#cmdoption-X) and [`PYTHON_GIL`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_GIL)

flags.thread_inherit_context[¶](https://docs.python.org/3/library/sys.html#sys.flags.thread_inherit_context "Link to this definition")
| [`-X thread_inherit_context`](https://docs.python.org/3/using/cmdline.html#cmdoption-X) and [`PYTHON_THREAD_INHERIT_CONTEXT`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_THREAD_INHERIT_CONTEXT)

flags.context_aware_warnings[¶](https://docs.python.org/3/library/sys.html#sys.flags.context_aware_warnings "Link to this definition")
| [`-X context_aware_warnings`](https://docs.python.org/3/using/cmdline.html#cmdoption-X) and [`PYTHON_CONTEXT_AWARE_WARNINGS`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_CONTEXT_AWARE_WARNINGS)
Changed in version 3.2: Added `quiet` attribute for the new [`-q`](https://docs.python.org/3/using/cmdline.html#cmdoption-q) flag.
Added in version 3.2.3: The `hash_randomization` attribute.
Changed in version 3.3: Removed obsolete `division_warning` attribute.
Changed in version 3.4: Added `isolated` attribute for [`-I`](https://docs.python.org/3/using/cmdline.html#cmdoption-I) `isolated` flag.
Changed in version 3.7: Added the `dev_mode` attribute for the new [Python Development Mode](https://docs.python.org/3/library/devmode.html#devmode) and the `utf8_mode` attribute for the new [`-X`](https://docs.python.org/3/using/cmdline.html#cmdoption-X) `utf8` flag.
Changed in version 3.10: Added `warn_default_encoding` attribute for [`-X`](https://docs.python.org/3/using/cmdline.html#cmdoption-X) `warn_default_encoding` flag.
Changed in version 3.11: Added the `safe_path` attribute for [`-P`](https://docs.python.org/3/using/cmdline.html#cmdoption-P) option.
Changed in version 3.11: Added the `int_max_str_digits` attribute.
Changed in version 3.13: Added the `gil` attribute.
Changed in version 3.14: Added the `thread_inherit_context` attribute.
Changed in version 3.14: Added the `context_aware_warnings` attribute.

sys.float_info[¶](https://docs.python.org/3/library/sys.html#sys.float_info "Link to this definition")

A [named tuple](https://docs.python.org/3/glossary.html#term-named-tuple) holding information about the float type. It contains low level information about the precision and internal representation. The values correspond to the various floating-point constants defined in the standard header file `float.h` for the ‘C’ programming language; see section 5.2.4.2.2 of the 1999 ISO/IEC C standard [[C99]](https://docs.python.org/3/library/sys.html#c99), ‘Characteristics of floating types’, for details.
Attributes of the `float_info` [named tuple](https://docs.python.org/3/glossary.html#term-named-tuple)[¶](https://docs.python.org/3/library/sys.html#id2 "Link to this table") attribute | float.h macro | explanation
---|---|---

float_info.epsilon[¶](https://docs.python.org/3/library/sys.html#sys.float_info.epsilon "Link to this definition")
| `DBL_EPSILON` |  difference between 1.0 and the least value greater than 1.0 that is representable as a float. See also [`math.ulp()`](https://docs.python.org/3/library/math.html#math.ulp "math.ulp").

float_info.dig[¶](https://docs.python.org/3/library/sys.html#sys.float_info.dig "Link to this definition")
| `DBL_DIG` | The maximum number of decimal digits that can be faithfully represented in a float; see below.

float_info.mant_dig[¶](https://docs.python.org/3/library/sys.html#sys.float_info.mant_dig "Link to this definition")
| `DBL_MANT_DIG` | Float precision: the number of base-`radix` digits in the significand of a float.

float_info.max[¶](https://docs.python.org/3/library/sys.html#sys.float_info.max "Link to this definition")
| `DBL_MAX` | The maximum representable positive finite float.

float_info.max_exp[¶](https://docs.python.org/3/library/sys.html#sys.float_info.max_exp "Link to this definition")
| `DBL_MAX_EXP` | The maximum integer _e_ such that `radix**(e-1)` is a representable finite float.

float_info.max_10_exp[¶](https://docs.python.org/3/library/sys.html#sys.float_info.max_10_exp "Link to this definition")
| `DBL_MAX_10_EXP` | The maximum integer _e_ such that `10**e` is in the range of representable finite floats.

float_info.min[¶](https://docs.python.org/3/library/sys.html#sys.float_info.min "Link to this definition")
| `DBL_MIN` |  The minimum representable positive _normalized_ float. Use [`math.ulp(0.0)`](https://docs.python.org/3/library/math.html#math.ulp "math.ulp") to get the smallest positive _denormalized_ representable float.

float_info.min_exp[¶](https://docs.python.org/3/library/sys.html#sys.float_info.min_exp "Link to this definition")
| `DBL_MIN_EXP` | The minimum integer _e_ such that `radix**(e-1)` is a normalized float.

float_info.min_10_exp[¶](https://docs.python.org/3/library/sys.html#sys.float_info.min_10_exp "Link to this definition")
| `DBL_MIN_10_EXP` | The minimum integer _e_ such that `10**e` is a normalized float.

float_info.radix[¶](https://docs.python.org/3/library/sys.html#sys.float_info.radix "Link to this definition")
| `FLT_RADIX` | The radix of exponent representation.

float_info.rounds[¶](https://docs.python.org/3/library/sys.html#sys.float_info.rounds "Link to this definition")
| `FLT_ROUNDS` |  An integer representing the rounding mode for floating-point arithmetic. This reflects the value of the system `FLT_ROUNDS` macro at interpreter startup time:
  * `-1`: indeterminable
  * `0`: toward zero
  * `1`: to nearest
  * `2`: toward positive infinity
  * `3`: toward negative infinity

All other values for `FLT_ROUNDS` characterize implementation-defined rounding behavior.
The attribute [`sys.float_info.dig`](https://docs.python.org/3/library/sys.html#sys.float_info.dig "sys.float_info.dig") needs further explanation. If `s` is any string representing a decimal number with at most `sys.float_info.dig` significant digits, then converting `s` to a float and back again will recover a string representing the same decimal value:
Copy```
>>> import sys
>>> sys.float_info.dig
15
>>> s = '3.14159265358979'    # decimal string with 15 significant digits
>>> format(float(s), '.15g')  # convert to float and back -> same value
'3.14159265358979'

```

But for strings with more than [`sys.float_info.dig`](https://docs.python.org/3/library/sys.html#sys.float_info.dig "sys.float_info.dig") significant digits, this isn’t always true:
Copy```
>>> s = '9876543211234567'    # 16 significant digits is too many!
>>> format(float(s), '.16g')  # conversion changes value
'9876543211234568'

```


sys.float_repr_style[¶](https://docs.python.org/3/library/sys.html#sys.float_repr_style "Link to this definition")

A string indicating how the [`repr()`](https://docs.python.org/3/library/functions.html#repr "repr") function behaves for floats. If the string has value `'short'` then for a finite float `x`, `repr(x)` aims to produce a short string with the property that `float(repr(x)) == x`. This is the usual behaviour in Python 3.1 and later. Otherwise, `float_repr_style` has value `'legacy'` and `repr(x)` behaves in the same way as it did in versions of Python prior to 3.1.
Added in version 3.1.

sys.getallocatedblocks()[¶](https://docs.python.org/3/library/sys.html#sys.getallocatedblocks "Link to this definition")

Return the number of memory blocks currently allocated by the interpreter, regardless of their size. This function is mainly useful for tracking and debugging memory leaks. Because of the interpreter’s internal caches, the result can vary from call to call; you may have to call [`_clear_internal_caches()`](https://docs.python.org/3/library/sys.html#sys._clear_internal_caches "sys._clear_internal_caches") and [`gc.collect()`](https://docs.python.org/3/library/gc.html#gc.collect "gc.collect") to get more predictable results.
If a Python build or implementation cannot reasonably compute this information, `getallocatedblocks()` is allowed to return 0 instead.
Added in version 3.4.

sys.getunicodeinternedsize()[¶](https://docs.python.org/3/library/sys.html#sys.getunicodeinternedsize "Link to this definition")

Return the number of unicode objects that have been interned.
Added in version 3.12.

sys.getandroidapilevel()[¶](https://docs.python.org/3/library/sys.html#sys.getandroidapilevel "Link to this definition")

Return the build-time API level of Android as an integer. This represents the minimum version of Android this build of Python can run on. For runtime version information, see [`platform.android_ver()`](https://docs.python.org/3/library/platform.html#platform.android_ver "platform.android_ver").
[Availability](https://docs.python.org/3/library/intro.html#availability): Android.
Added in version 3.7.

sys.getdefaultencoding()[¶](https://docs.python.org/3/library/sys.html#sys.getdefaultencoding "Link to this definition")

Return `'utf-8'`. This is the name of the default string encoding, used in methods like [`str.encode()`](https://docs.python.org/3/library/stdtypes.html#str.encode "str.encode").

sys.getdlopenflags()[¶](https://docs.python.org/3/library/sys.html#sys.getdlopenflags "Link to this definition")

Return the current value of the flags that are used for `dlopen()` calls. Symbolic names for the flag values can be found in the [`os`](https://docs.python.org/3/library/os.html#module-os "os: Miscellaneous operating system interfaces.") module (`RTLD__xxx_`constants, e.g.[`os.RTLD_LAZY`](https://docs.python.org/3/library/os.html#os.RTLD_LAZY "os.RTLD_LAZY")).
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.

sys.getfilesystemencoding()[¶](https://docs.python.org/3/library/sys.html#sys.getfilesystemencoding "Link to this definition")

Get the [filesystem encoding](https://docs.python.org/3/glossary.html#term-filesystem-encoding-and-error-handler): the encoding used with the filesystem error handler to convert between Unicode filenames and bytes filenames. The filesystem error handler is returned from [`getfilesystemencodeerrors()`](https://docs.python.org/3/library/sys.html#sys.getfilesystemencodeerrors "sys.getfilesystemencodeerrors").
For best compatibility, str should be used for filenames in all cases, although representing filenames as bytes is also supported. Functions accepting or returning filenames should support either str or bytes and internally convert to the system’s preferred representation.
[`os.fsencode()`](https://docs.python.org/3/library/os.html#os.fsencode "os.fsencode") and [`os.fsdecode()`](https://docs.python.org/3/library/os.html#os.fsdecode "os.fsdecode") should be used to ensure that the correct encoding and errors mode are used.
The [filesystem encoding and error handler](https://docs.python.org/3/glossary.html#term-filesystem-encoding-and-error-handler) are configured at Python startup by the [`PyConfig_Read()`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Read "PyConfig_Read") function: see [`filesystem_encoding`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.filesystem_encoding "PyConfig.filesystem_encoding") and [`filesystem_errors`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.filesystem_errors "PyConfig.filesystem_errors") members of [`PyConfig`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig "PyConfig").
Changed in version 3.2: `getfilesystemencoding()` result cannot be `None` anymore.
Changed in version 3.6: Windows is no longer guaranteed to return `'mbcs'`. See [**PEP 529**](https://peps.python.org/pep-0529/) and [`_enablelegacywindowsfsencoding()`](https://docs.python.org/3/library/sys.html#sys._enablelegacywindowsfsencoding "sys._enablelegacywindowsfsencoding") for more information.
Changed in version 3.7: Return `'utf-8'` if the [Python UTF-8 Mode](https://docs.python.org/3/library/os.html#utf8-mode) is enabled.

sys.getfilesystemencodeerrors()[¶](https://docs.python.org/3/library/sys.html#sys.getfilesystemencodeerrors "Link to this definition")

Get the [filesystem error handler](https://docs.python.org/3/glossary.html#term-filesystem-encoding-and-error-handler): the error handler used with the filesystem encoding to convert between Unicode filenames and bytes filenames. The filesystem encoding is returned from [`getfilesystemencoding()`](https://docs.python.org/3/library/sys.html#sys.getfilesystemencoding "sys.getfilesystemencoding").
[`os.fsencode()`](https://docs.python.org/3/library/os.html#os.fsencode "os.fsencode") and [`os.fsdecode()`](https://docs.python.org/3/library/os.html#os.fsdecode "os.fsdecode") should be used to ensure that the correct encoding and errors mode are used.
The [filesystem encoding and error handler](https://docs.python.org/3/glossary.html#term-filesystem-encoding-and-error-handler) are configured at Python startup by the [`PyConfig_Read()`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Read "PyConfig_Read") function: see [`filesystem_encoding`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.filesystem_encoding "PyConfig.filesystem_encoding") and [`filesystem_errors`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.filesystem_errors "PyConfig.filesystem_errors") members of [`PyConfig`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig "PyConfig").
Added in version 3.6.

sys.get_int_max_str_digits()[¶](https://docs.python.org/3/library/sys.html#sys.get_int_max_str_digits "Link to this definition")

Returns the current value for the [integer string conversion length limitation](https://docs.python.org/3/library/stdtypes.html#int-max-str-digits). See also [`set_int_max_str_digits()`](https://docs.python.org/3/library/sys.html#sys.set_int_max_str_digits "sys.set_int_max_str_digits").
Added in version 3.11.

sys.getrefcount(_object_)[¶](https://docs.python.org/3/library/sys.html#sys.getrefcount "Link to this definition")

Return the reference count of the _object_. The count returned is generally one higher than you might expect, because it includes the (temporary) reference as an argument to `getrefcount()`.
Note that the returned value may not actually reflect how many references to the object are actually held. For example, some objects are [immortal](https://docs.python.org/3/glossary.html#term-immortal) and have a very high refcount that does not reflect the actual number of references. Consequently, do not rely on the returned value to be accurate, other than a value of 0 or 1.
**CPython implementation detail:** [Immortal](https://docs.python.org/3/glossary.html#term-immortal) objects with a large reference count can be identified via [`_is_immortal()`](https://docs.python.org/3/library/sys.html#sys._is_immortal "sys._is_immortal").
Changed in version 3.12: Immortal objects have very large refcounts that do not match the actual number of references to the object.

sys.getrecursionlimit()[¶](https://docs.python.org/3/library/sys.html#sys.getrecursionlimit "Link to this definition")

Return the current value of the recursion limit, the maximum depth of the Python interpreter stack. This limit prevents infinite recursion from causing an overflow of the C stack and crashing Python. It can be set by [`setrecursionlimit()`](https://docs.python.org/3/library/sys.html#sys.setrecursionlimit "sys.setrecursionlimit").

sys.getsizeof(_object_[, _default_])[¶](https://docs.python.org/3/library/sys.html#sys.getsizeof "Link to this definition")

Return the size of an object in bytes. The object can be any type of object. All built-in objects will return correct results, but this does not have to hold true for third-party extensions as it is implementation specific.
Only the memory consumption directly attributed to the object is accounted for, not the memory consumption of objects it refers to.
If given, _default_ will be returned if the object does not provide means to retrieve the size. Otherwise a [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") will be raised.
`getsizeof()` calls the object’s `__sizeof__` method and adds an additional garbage collector overhead if the object is managed by the garbage collector.
See `getsizeof()` recursively to find the size of containers and all their contents.

sys.getswitchinterval()[¶](https://docs.python.org/3/library/sys.html#sys.getswitchinterval "Link to this definition")

Return the interpreter’s “thread switch interval” in seconds; see [`setswitchinterval()`](https://docs.python.org/3/library/sys.html#sys.setswitchinterval "sys.setswitchinterval").
Added in version 3.2.

sys._getframe([_depth_])[¶](https://docs.python.org/3/library/sys.html#sys._getframe "Link to this definition")

Return a frame object from the call stack. If optional integer _depth_ is given, return the frame object that many calls below the top of the stack. If that is deeper than the call stack, [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised. The default for _depth_ is zero, returning the frame at the top of the call stack.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `sys._getframe` with argument `frame`.
**CPython implementation detail:** This function should be used for internal and specialized purposes only. It is not guaranteed to exist in all implementations of Python.

sys._getframemodulename([_depth_])[¶](https://docs.python.org/3/library/sys.html#sys._getframemodulename "Link to this definition")

Return the name of a module from the call stack. If optional integer _depth_ is given, return the module that many calls below the top of the stack. If that is deeper than the call stack, or if the module is unidentifiable, `None` is returned. The default for _depth_ is zero, returning the module at the top of the call stack.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `sys._getframemodulename` with argument `depth`.
**CPython implementation detail:** This function should be used for internal and specialized purposes only. It is not guaranteed to exist in all implementations of Python.
Added in version 3.12.

sys.getobjects(_limit_[, _type_])[¶](https://docs.python.org/3/library/sys.html#sys.getobjects "Link to this definition")

This function only exists if CPython was built using the specialized configure option [`--with-trace-refs`](https://docs.python.org/3/using/configure.html#cmdoption-with-trace-refs). It is intended only for debugging garbage-collection issues.
Return a list of up to _limit_ dynamically allocated Python objects. If _type_ is given, only objects of that exact type (not subtypes) are included.
Objects from the list are not safe to use. Specifically, the result will include objects from all interpreters that share their object allocator state (that is, ones created with [`PyInterpreterConfig.use_main_obmalloc`](https://docs.python.org/3/c-api/subinterpreters.html#c.PyInterpreterConfig.use_main_obmalloc "PyInterpreterConfig.use_main_obmalloc") set to 1 or using [`Py_NewInterpreter()`](https://docs.python.org/3/c-api/subinterpreters.html#c.Py_NewInterpreter "Py_NewInterpreter"), and the [main interpreter](https://docs.python.org/3/c-api/subinterpreters.html#sub-interpreter-support)). Mixing objects from different interpreters may lead to crashes or other unexpected behavior.
