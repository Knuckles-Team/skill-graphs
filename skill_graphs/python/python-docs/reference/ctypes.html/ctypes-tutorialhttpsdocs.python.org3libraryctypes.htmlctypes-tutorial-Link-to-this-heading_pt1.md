## ctypes tutorial[¶](https://docs.python.org/3/library/ctypes.html#ctypes-tutorial "Link to this heading")
Note: The code samples in this tutorial use [`doctest`](https://docs.python.org/3/library/doctest.html#module-doctest "doctest: Test pieces of code within docstrings.") to make sure that they actually work. Since some code samples behave differently under Linux, Windows, or macOS, they contain doctest directives in comments.
Note: Some code samples reference the ctypes [`c_int`](https://docs.python.org/3/library/ctypes.html#ctypes.c_int "ctypes.c_int") type. On platforms where `sizeof(long) == sizeof(int)` it is an alias to [`c_long`](https://docs.python.org/3/library/ctypes.html#ctypes.c_long "ctypes.c_long"). So, you should not be confused if `c_long` is printed if you would expect `c_int` — they are actually the same type.
### Loading dynamic link libraries[¶](https://docs.python.org/3/library/ctypes.html#loading-dynamic-link-libraries "Link to this heading")
`ctypes` exports the _cdll_ , and on Windows _windll_ and _oledll_ objects, for loading dynamic link libraries.
You load libraries by accessing them as attributes of these objects. _cdll_ loads libraries which export functions using the standard `cdecl` calling convention, while _windll_ libraries call functions using the `stdcall` calling convention. _oledll_ also uses the `stdcall` calling convention, and assumes the functions return a Windows `HRESULT` error code. The error code is used to automatically raise an [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") exception when the function call fails.
Changed in version 3.3: Windows errors used to raise [`WindowsError`](https://docs.python.org/3/library/exceptions.html#WindowsError "WindowsError"), which is now an alias of [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError").
Here are some examples for Windows. Note that `msvcrt` is the MS standard C library containing most standard C functions, and uses the `cdecl` calling convention:
Copy```
>>> from ctypes import *
>>> print(windll.kernel32)
<WinDLL 'kernel32', handle ... at ...>
>>> print(cdll.msvcrt)
<CDLL 'msvcrt', handle ... at ...>
>>> libc = cdll.msvcrt
>>>

```

Windows appends the usual `.dll` file suffix automatically.
Note
Accessing the standard C library through `cdll.msvcrt` will use an outdated version of the library that may be incompatible with the one being used by Python. Where possible, use native Python functionality, or else import and use the `msvcrt` module.
On Linux, it is required to specify the filename _including_ the extension to load a library, so attribute access can not be used to load libraries. Either the [`LoadLibrary()`](https://docs.python.org/3/library/ctypes.html#ctypes.LibraryLoader.LoadLibrary "ctypes.LibraryLoader.LoadLibrary") method of the dll loaders should be used, or you should load the library by creating an instance of CDLL by calling the constructor:
Copy```
>>> cdll.LoadLibrary("libc.so.6")
<CDLL 'libc.so.6', handle ... at ...>
>>> libc = CDLL("libc.so.6")
>>> libc
<CDLL 'libc.so.6', handle ... at ...>
>>>

```

### Accessing functions from loaded dlls[¶](https://docs.python.org/3/library/ctypes.html#accessing-functions-from-loaded-dlls "Link to this heading")
Functions are accessed as attributes of dll objects:
Copy```
>>> libc.printf
<_FuncPtr object at 0x...>
>>> print(windll.kernel32.GetModuleHandleA)
<_FuncPtr object at 0x...>
>>> print(windll.kernel32.MyOwnFunction)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "ctypes.py", line 239, in __getattr__
    func = _StdcallFuncPtr(name, self)
AttributeError: function 'MyOwnFunction' not found
>>>

```

Note that win32 system dlls like `kernel32` and `user32` often export ANSI as well as UNICODE versions of a function. The UNICODE version is exported with a `W` appended to the name, while the ANSI version is exported with an `A` appended to the name. The win32 `GetModuleHandle` function, which returns a _module handle_ for a given module name, has the following C prototype, and a macro is used to expose one of them as `GetModuleHandle` depending on whether UNICODE is defined or not:
Copy```
/* ANSI version */
HMODULE GetModuleHandleA(LPCSTR lpModuleName);
/* UNICODE version */
HMODULE GetModuleHandleW(LPCWSTR lpModuleName);

```

_windll_ does not try to select one of them by magic, you must access the version you need by specifying `GetModuleHandleA` or `GetModuleHandleW` explicitly, and then call it with bytes or string objects respectively.
Sometimes, dlls export functions with names which aren’t valid Python identifiers, like `"??2@YAPAXI@Z"`. In this case you have to use [`getattr()`](https://docs.python.org/3/library/functions.html#getattr "getattr") to retrieve the function:
Copy```
>>> getattr(cdll.msvcrt, "??2@YAPAXI@Z")
<_FuncPtr object at 0x...>
>>>

```

On Windows, some dlls export functions not by name but by ordinal. These functions can be accessed by indexing the dll object with the ordinal number:
Copy```
>>> cdll.kernel32[1]
<_FuncPtr object at 0x...>
>>> cdll.kernel32[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "ctypes.py", line 310, in __getitem__
    func = _StdcallFuncPtr(name, self)
AttributeError: function ordinal 0 not found
>>>

```

### Calling functions[¶](https://docs.python.org/3/library/ctypes.html#calling-functions "Link to this heading")
You can call these functions like any other Python callable. This example uses the `rand()` function, which takes no arguments and returns a pseudo-random integer:
Copy```
>>> print(libc.rand())
1804289383

```

On Windows, you can call the `GetModuleHandleA()` function, which returns a win32 module handle (passing `None` as single argument to call it with a `NULL` pointer):
Copy```
>>> print(hex(windll.kernel32.GetModuleHandleA(None)))
0x1d000000
>>>

```

[`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised when you call an `stdcall` function with the `cdecl` calling convention, or vice versa:
Copy```
>>> cdll.kernel32.GetModuleHandleA(None)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: Procedure probably called with not enough arguments (4 bytes missing)
>>>

>>> windll.msvcrt.printf(b"spam")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: Procedure probably called with too many arguments (4 bytes in excess)
>>>

```

To find out the correct calling convention you have to look into the C header file or the documentation for the function you want to call.
On Windows, `ctypes` uses win32 structured exception handling to prevent crashes from general protection faults when functions are called with invalid argument values:
Copy```
>>> windll.kernel32.GetModuleHandleA(32)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
OSError: exception: access violation reading 0x00000020
>>>

```

There are, however, enough ways to crash Python with `ctypes`, so you should be careful anyway. The [`faulthandler`](https://docs.python.org/3/library/faulthandler.html#module-faulthandler "faulthandler: Dump the Python traceback.") module can be helpful in debugging crashes (e.g. from segmentation faults produced by erroneous C library calls).
`None`, integers, bytes objects and (unicode) strings are the only native Python objects that can directly be used as parameters in these function calls. `None` is passed as a C `NULL` pointer, bytes objects and strings are passed as pointer to the memory block that contains their data (char* or wchar_t*). Python integers are passed as the platform’s default C int type, their value is masked to fit into the C type.
Before we move on calling functions with other parameter types, we have to learn more about `ctypes` data types.
### Fundamental data types[¶](https://docs.python.org/3/library/ctypes.html#fundamental-data-types "Link to this heading")
`ctypes` defines a number of primitive C compatible data types:
ctypes type | C type | Python type
---|---|---
[`c_bool`](https://docs.python.org/3/library/ctypes.html#ctypes.c_bool "ctypes.c_bool") | _Bool | bool (1)
[`c_char`](https://docs.python.org/3/library/ctypes.html#ctypes.c_char "ctypes.c_char") | char | 1-character bytes object
[`c_wchar`](https://docs.python.org/3/library/ctypes.html#ctypes.c_wchar "ctypes.c_wchar") | `wchar_t` | 1-character string
[`c_byte`](https://docs.python.org/3/library/ctypes.html#ctypes.c_byte "ctypes.c_byte") | char | int
[`c_ubyte`](https://docs.python.org/3/library/ctypes.html#ctypes.c_ubyte "ctypes.c_ubyte") | unsignedchar | int
[`c_short`](https://docs.python.org/3/library/ctypes.html#ctypes.c_short "ctypes.c_short") | short | int
[`c_ushort`](https://docs.python.org/3/library/ctypes.html#ctypes.c_ushort "ctypes.c_ushort") | unsignedshort | int
[`c_int`](https://docs.python.org/3/library/ctypes.html#ctypes.c_int "ctypes.c_int") | int | int
[`c_int8`](https://docs.python.org/3/library/ctypes.html#ctypes.c_int8 "ctypes.c_int8") | `int8_t` | int
[`c_int16`](https://docs.python.org/3/library/ctypes.html#ctypes.c_int16 "ctypes.c_int16") | `int16_t` | int
[`c_int32`](https://docs.python.org/3/library/ctypes.html#ctypes.c_int32 "ctypes.c_int32") | `int32_t` | int
[`c_int64`](https://docs.python.org/3/library/ctypes.html#ctypes.c_int64 "ctypes.c_int64") | `int64_t` | int
[`c_uint`](https://docs.python.org/3/library/ctypes.html#ctypes.c_uint "ctypes.c_uint") | unsignedint | int
[`c_uint8`](https://docs.python.org/3/library/ctypes.html#ctypes.c_uint8 "ctypes.c_uint8") | `uint8_t` | int
[`c_uint16`](https://docs.python.org/3/library/ctypes.html#ctypes.c_uint16 "ctypes.c_uint16") | `uint16_t` | int
[`c_uint32`](https://docs.python.org/3/library/ctypes.html#ctypes.c_uint32 "ctypes.c_uint32") | `uint32_t` | int
[`c_uint64`](https://docs.python.org/3/library/ctypes.html#ctypes.c_uint64 "ctypes.c_uint64") | `uint64_t` | int
[`c_long`](https://docs.python.org/3/library/ctypes.html#ctypes.c_long "ctypes.c_long") | long | int
[`c_ulong`](https://docs.python.org/3/library/ctypes.html#ctypes.c_ulong "ctypes.c_ulong") | unsignedlong | int
[`c_longlong`](https://docs.python.org/3/library/ctypes.html#ctypes.c_longlong "ctypes.c_longlong") | __int64 or longlong | int
[`c_ulonglong`](https://docs.python.org/3/library/ctypes.html#ctypes.c_ulonglong "ctypes.c_ulonglong") | unsigned__int64 or unsignedlonglong | int
[`c_size_t`](https://docs.python.org/3/library/ctypes.html#ctypes.c_size_t "ctypes.c_size_t") | `size_t` | int
[`c_ssize_t`](https://docs.python.org/3/library/ctypes.html#ctypes.c_ssize_t "ctypes.c_ssize_t") | `ssize_t` or [Py_ssize_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t") | int
[`c_time_t`](https://docs.python.org/3/library/ctypes.html#ctypes.c_time_t "ctypes.c_time_t") | `time_t` | int
[`c_float`](https://docs.python.org/3/library/ctypes.html#ctypes.c_float "ctypes.c_float") | float | float
[`c_double`](https://docs.python.org/3/library/ctypes.html#ctypes.c_double "ctypes.c_double") | double | float
[`c_longdouble`](https://docs.python.org/3/library/ctypes.html#ctypes.c_longdouble "ctypes.c_longdouble") | longdouble | float
[`c_char_p`](https://docs.python.org/3/library/ctypes.html#ctypes.c_char_p "ctypes.c_char_p") | char* (NUL terminated) | bytes object or `None`
[`c_wchar_p`](https://docs.python.org/3/library/ctypes.html#ctypes.c_wchar_p "ctypes.c_wchar_p") | wchar_t* (NUL terminated) | string or `None`
[`c_void_p`](https://docs.python.org/3/library/ctypes.html#ctypes.c_void_p "ctypes.c_void_p") | void* | int or `None`
  1. The constructor accepts any object with a truth value.


Additionally, if IEC 60559 compatible complex arithmetic (Annex G) is supported in both C and `libffi`, the following complex types are available:
ctypes type | C type | Python type
---|---|---
[`c_float_complex`](https://docs.python.org/3/library/ctypes.html#ctypes.c_float_complex "ctypes.c_float_complex") | floatcomplex | complex
[`c_double_complex`](https://docs.python.org/3/library/ctypes.html#ctypes.c_double_complex "ctypes.c_double_complex") | doublecomplex | complex
[`c_longdouble_complex`](https://docs.python.org/3/library/ctypes.html#ctypes.c_longdouble_complex "ctypes.c_longdouble_complex") | longdoublecomplex | complex
All these types can be created by calling them with an optional initializer of the correct type and value:
Copy```
>>> c_int()
c_long(0)
>>> c_wchar_p("Hello, World")
c_wchar_p(140018365411392)
>>> c_ushort(-3)
c_ushort(65533)
>>>

```

Since these types are mutable, their value can also be changed afterwards:
Copy```
>>> i = c_int(42)
>>> print(i)
c_long(42)
>>> print(i.value)
42
>>> i.value = -99
>>> print(i.value)
-99
>>>

```

Assigning a new value to instances of the pointer types [`c_char_p`](https://docs.python.org/3/library/ctypes.html#ctypes.c_char_p "ctypes.c_char_p"), [`c_wchar_p`](https://docs.python.org/3/library/ctypes.html#ctypes.c_wchar_p "ctypes.c_wchar_p"), and [`c_void_p`](https://docs.python.org/3/library/ctypes.html#ctypes.c_void_p "ctypes.c_void_p") changes the _memory location_ they point to, _not the contents_ of the memory block (of course not, because Python string objects are immutable):
Copy```
>>> s = "Hello, World"
>>> c_s = c_wchar_p(s)
>>> print(c_s)
c_wchar_p(139966785747344)
>>> print(c_s.value)
Hello World
>>> c_s.value = "Hi, there"
>>> print(c_s)              # the memory location has changed
c_wchar_p(139966783348904)
>>> print(c_s.value)
Hi, there
>>> print(s)                # first object is unchanged
Hello, World
>>>

```

You should be careful, however, not to pass them to functions expecting pointers to mutable memory. If you need mutable memory blocks, ctypes has a [`create_string_buffer()`](https://docs.python.org/3/library/ctypes.html#ctypes.create_string_buffer "ctypes.create_string_buffer") function which creates these in various ways. The current memory block contents can be accessed (or changed) with the `raw` property; if you want to access it as NUL terminated string, use the `value` property:
Copy```
>>> from ctypes import *
>>> p = create_string_buffer(3)            # create a 3 byte buffer, initialized to NUL bytes
>>> print(sizeof(p), repr(p.raw))
3 b'\x00\x00\x00'
>>> p = create_string_buffer(b"Hello")     # create a buffer containing a NUL terminated string
>>> print(sizeof(p), repr(p.raw))
6 b'Hello\x00'
>>> print(repr(p.value))
b'Hello'
>>> p = create_string_buffer(b"Hello", 10) # create a 10 byte buffer
>>> print(sizeof(p), repr(p.raw))
10 b'Hello\x00\x00\x00\x00\x00'
>>> p.value = b"Hi"
>>> print(sizeof(p), repr(p.raw))
10 b'Hi\x00lo\x00\x00\x00\x00\x00'
>>>

```

The [`create_string_buffer()`](https://docs.python.org/3/library/ctypes.html#ctypes.create_string_buffer "ctypes.create_string_buffer") function replaces the old `c_buffer()` function (which is still available as an alias). To create a mutable memory block containing unicode characters of the C type `wchar_t`, use the [`create_unicode_buffer()`](https://docs.python.org/3/library/ctypes.html#ctypes.create_unicode_buffer "ctypes.create_unicode_buffer") function.
### Calling functions, continued[¶](https://docs.python.org/3/library/ctypes.html#calling-functions-continued "Link to this heading")
Note that printf prints to the real standard output channel, _not_ to [`sys.stdout`](https://docs.python.org/3/library/sys.html#sys.stdout "sys.stdout"), so these examples will only work at the console prompt, not from within _IDLE_ or _PythonWin_ :
Copy```
>>> printf = libc.printf
>>> printf(b"Hello, %s\n", b"World!")
Hello, World!
14
>>> printf(b"Hello, %S\n", "World!")
Hello, World!
14
>>> printf(b"%d bottles of beer\n", 42)
42 bottles of beer
19
>>> printf(b"%f bottles of beer\n", 42.5)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ctypes.ArgumentError: argument 2: TypeError: Don't know how to convert parameter 2
>>>

```

As has been mentioned before, all Python types except integers, strings, and bytes objects have to be wrapped in their corresponding `ctypes` type, so that they can be converted to the required C data type:
Copy```
>>> printf(b"An int %d, a double %f\n", 1234, c_double(3.14))
An int 1234, a double 3.140000
31
>>>

```

### Calling variadic functions[¶](https://docs.python.org/3/library/ctypes.html#calling-variadic-functions "Link to this heading")
On a lot of platforms calling variadic functions through ctypes is exactly the same as calling functions with a fixed number of parameters. On some platforms, and in particular ARM64 for Apple Platforms, the calling convention for variadic functions is different than that for regular functions.
On those platforms it is required to specify the [`argtypes`](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr.argtypes "ctypes._CFuncPtr.argtypes") attribute for the regular, non-variadic, function arguments:
Copy```
libc.printf.argtypes = [ctypes.c_char_p]

```

Because specifying the attribute does not inhibit portability it is advised to always specify [`argtypes`](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr.argtypes "ctypes._CFuncPtr.argtypes") for all variadic functions.
### Calling functions with your own custom data types[¶](https://docs.python.org/3/library/ctypes.html#calling-functions-with-your-own-custom-data-types "Link to this heading")
You can also customize `ctypes` argument conversion to allow instances of your own classes be used as function arguments. `ctypes` looks for an `_as_parameter_` attribute and uses this as the function argument. The attribute must be an integer, string, bytes, a `ctypes` instance, or an object with an `_as_parameter_` attribute:
Copy```
>>> class Bottles:
...     def __init__(self, number):
...         self._as_parameter_ = number
...
>>> bottles = Bottles(42)
>>> printf(b"%d bottles of beer\n", bottles)
42 bottles of beer
19
>>>

```

If you don’t want to store the instance’s data in the `_as_parameter_` instance variable, you could define a [`property`](https://docs.python.org/3/library/functions.html#property "property") which makes the attribute available on request.
### Specifying the required argument types (function prototypes)[¶](https://docs.python.org/3/library/ctypes.html#specifying-the-required-argument-types-function-prototypes "Link to this heading")
It is possible to specify the required argument types of functions exported from DLLs by setting the [`argtypes`](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr.argtypes "ctypes._CFuncPtr.argtypes") attribute.
[`argtypes`](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr.argtypes "ctypes._CFuncPtr.argtypes") must be a sequence of C data types (the `printf()` function is probably not a good example here, because it takes a variable number and different types of parameters depending on the format string, on the other hand this is quite handy to experiment with this feature):
Copy```
>>> printf.argtypes = [c_char_p, c_char_p, c_int, c_double]
>>> printf(b"String '%s', Int %d, Double %f\n", b"Hi", 10, 2.2)
String 'Hi', Int 10, Double 2.200000
37
>>>

```

Specifying a format protects against incompatible argument types (just as a prototype for a C function), and tries to convert the arguments to valid types:
Copy```
>>> printf(b"%d %d %d", 1, 2, 3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ctypes.ArgumentError: argument 2: TypeError: 'int' object cannot be interpreted as ctypes.c_char_p
>>> printf(b"%s %d %f\n", b"X", 2, 3)
X 2 3.000000
13
>>>

```

If you have defined your own classes which you pass to function calls, you have to implement a [`from_param()`](https://docs.python.org/3/library/ctypes.html#ctypes._CData.from_param "ctypes._CData.from_param") class method for them to be able to use them in the [`argtypes`](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr.argtypes "ctypes._CFuncPtr.argtypes") sequence. The `from_param()` class method receives the Python object passed to the function call, it should do a typecheck or whatever is needed to make sure this object is acceptable, and then return the object itself, its `_as_parameter_` attribute, or whatever you want to pass as the C function argument in this case. Again, the result should be an integer, string, bytes, a `ctypes` instance, or an object with an `_as_parameter_` attribute.
### Return types[¶](https://docs.python.org/3/library/ctypes.html#return-types "Link to this heading")
By default functions are assumed to return the C int type. Other return types can be specified by setting the [`restype`](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr.restype "ctypes._CFuncPtr.restype") attribute of the function object.
The C prototype of `time()` is `time_t time(time_t *)`. Because `time_t` might be of a different type than the default return type int, you should specify the `restype` attribute:
Copy```
>>> libc.time.restype = c_time_t

```

The argument types can be specified using [`argtypes`](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr.argtypes "ctypes._CFuncPtr.argtypes"):
Copy```
>>> libc.time.argtypes = (POINTER(c_time_t),)

```

To call the function with a `NULL` pointer as first argument, use `None`:
Copy```
>>> print(libc.time(None))
1150640792

```

Here is a more advanced example, it uses the `strchr()` function, which expects a string pointer and a char, and returns a pointer to a string:
Copy```
>>> strchr = libc.strchr
>>> strchr(b"abcdef", ord("d"))
8059983
>>> strchr.restype = c_char_p    # c_char_p is a pointer to a string
>>> strchr(b"abcdef", ord("d"))
b'def'
>>> print(strchr(b"abcdef", ord("x")))
None
>>>

```

If you want to avoid the [`ord("x")`](https://docs.python.org/3/library/functions.html#ord "ord") calls above, you can set the [`argtypes`](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr.argtypes "ctypes._CFuncPtr.argtypes") attribute, and the second argument will be converted from a single character Python bytes object into a C char:
Copy```
>>> strchr.restype = c_char_p
>>> strchr.argtypes = [c_char_p, c_char]
>>> strchr(b"abcdef", b"d")
b'def'
>>> strchr(b"abcdef", b"def")
Traceback (most recent call last):
ctypes.ArgumentError: argument 2: TypeError: one character bytes, bytearray or integer expected
>>> print(strchr(b"abcdef", b"x"))
None
>>> strchr(b"abcdef", b"d")
b'def'
>>>

```

You can also use a callable Python object (a function or a class for example) as the [`restype`](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr.restype "ctypes._CFuncPtr.restype") attribute, if the foreign function returns an integer. The callable will be called with the _integer_ the C function returns, and the result of this call will be used as the result of your function call. This is useful to check for error return values and automatically raise an exception:
Copy```
>>> GetModuleHandle = windll.kernel32.GetModuleHandleA
>>> def ValidHandle(value):
...     if value == 0:
...         raise WinError()
...     return value
...
>>>
>>> GetModuleHandle.restype = ValidHandle
>>> GetModuleHandle(None)
486539264
>>> GetModuleHandle("something silly")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in ValidHandle
OSError: [Errno 126] The specified module could not be found.
>>>

```

`WinError` is a function which will call Windows `FormatMessage()` api to get the string representation of an error code, and _returns_ an exception. `WinError` takes an optional error code parameter, if no one is used, it calls [`GetLastError()`](https://docs.python.org/3/library/ctypes.html#ctypes.GetLastError "ctypes.GetLastError") to retrieve it.
Please note that a much more powerful error checking mechanism is available through the [`errcheck`](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr.errcheck "ctypes._CFuncPtr.errcheck") attribute; see the reference manual for details.
### Passing pointers (or: passing parameters by reference)[¶](https://docs.python.org/3/library/ctypes.html#passing-pointers-or-passing-parameters-by-reference "Link to this heading")
Sometimes a C api function expects a _pointer_ to a data type as parameter, probably to write into the corresponding location, or if the data is too large to be passed by value. This is also known as _passing parameters by reference_.
`ctypes` exports the [`byref()`](https://docs.python.org/3/library/ctypes.html#ctypes.byref "ctypes.byref") function which is used to pass parameters by reference. The same effect can be achieved with the [`pointer()`](https://docs.python.org/3/library/ctypes.html#ctypes.pointer "ctypes.pointer") function, although `pointer()` does a lot more work since it constructs a real pointer object, so it is faster to use `byref()` if you don’t need the pointer object in Python itself:
Copy```
>>> i = c_int()
>>> f = c_float()
>>> s = create_string_buffer(b'\000' * 32)
>>> print(i.value, f.value, repr(s.value))
0 0.0 b''
>>> libc.sscanf(b"1 3.14 Hello", b"%d %f %s",
...             byref(i), byref(f), s)
3
>>> print(i.value, f.value, repr(s.value))
1 3.1400001049 b'Hello'
>>>

```

### Structures and unions[¶](https://docs.python.org/3/library/ctypes.html#structures-and-unions "Link to this heading")
Structures and unions must derive from the [`Structure`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure "ctypes.Structure") and [`Union`](https://docs.python.org/3/library/ctypes.html#ctypes.Union "ctypes.Union") base classes which are defined in the `ctypes` module. Each subclass must define a [`_fields_`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._fields_ "ctypes.Structure._fields_") attribute. `_fields_` must be a list of _2-tuples_ , containing a _field name_ and a _field type_.
