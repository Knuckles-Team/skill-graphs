## ctypes reference[¶](https://docs.python.org/3/library/ctypes.html#ctypes-reference "Link to this heading")
### Finding shared libraries[¶](https://docs.python.org/3/library/ctypes.html#finding-shared-libraries "Link to this heading")
When programming in a compiled language, shared libraries are accessed when compiling/linking a program, and when the program is run.
The purpose of the [`find_library()`](https://docs.python.org/3/library/ctypes.html#ctypes.util.find_library "ctypes.util.find_library") function is to locate a library in a way similar to what the compiler or runtime loader does (on platforms with several versions of a shared library the most recent should be loaded), while the ctypes library loaders act like when a program is run, and call the runtime loader directly.
The `ctypes.util` module provides a function which can help to determine the library to load.

ctypes.util.find_library(_name_)

Try to find a library and return a pathname. _name_ is the library name without any prefix like _lib_ , suffix like `.so`, `.dylib` or version number (this is the form used for the posix linker option `-l`). If no library can be found, returns `None`.
The exact functionality is system dependent.
On Linux, [`find_library()`](https://docs.python.org/3/library/ctypes.html#ctypes.util.find_library "ctypes.util.find_library") tries to run external programs (`/sbin/ldconfig`, `gcc`, `objdump` and `ld`) to find the library file. It returns the filename of the library file.
Note that if the output of these programs does not correspond to the dynamic linker used by Python, the result of this function may be misleading.
Changed in version 3.6: On Linux, the value of the environment variable `LD_LIBRARY_PATH` is used when searching for libraries, if a library cannot be found by any other means.
Here are some examples:
Copy```
>>> from ctypes.util import find_library
>>> find_library("m")
'libm.so.6'
>>> find_library("c")
'libc.so.6'
>>> find_library("bz2")
'libbz2.so.1.0'
>>>

```

On macOS and Android, [`find_library()`](https://docs.python.org/3/library/ctypes.html#ctypes.util.find_library "ctypes.util.find_library") uses the system’s standard naming schemes and paths to locate the library, and returns a full pathname if successful:
Copy```
>>> from ctypes.util import find_library
>>> find_library("c")
'/usr/lib/libc.dylib'
>>> find_library("m")
'/usr/lib/libm.dylib'
>>> find_library("bz2")
'/usr/lib/libbz2.dylib'
>>> find_library("AGL")
'/System/Library/Frameworks/AGL.framework/AGL'
>>>

```

On Windows, [`find_library()`](https://docs.python.org/3/library/ctypes.html#ctypes.util.find_library "ctypes.util.find_library") searches along the system search path, and returns the full pathname, but since there is no predefined naming scheme a call like `find_library("c")` will fail and return `None`.
If wrapping a shared library with `ctypes`, it _may_ be better to determine the shared library name at development time, and hardcode that into the wrapper module instead of using [`find_library()`](https://docs.python.org/3/library/ctypes.html#ctypes.util.find_library "ctypes.util.find_library") to locate the library at runtime.
### Listing loaded shared libraries[¶](https://docs.python.org/3/library/ctypes.html#listing-loaded-shared-libraries "Link to this heading")
When writing code that relies on code loaded from shared libraries, it can be useful to know which shared libraries have already been loaded into the current process.
The `ctypes.util` module provides the [`dllist()`](https://docs.python.org/3/library/ctypes.html#ctypes.util.dllist "ctypes.util.dllist") function, which calls the different APIs provided by the various platforms to help determine which shared libraries have already been loaded into the current process.
The exact output of this function will be system dependent. On most platforms, the first entry of this list represents the current process itself, which may be an empty string. For example, on glibc-based Linux, the return may look like:
Copy```
>>> from ctypes.util import dllist
>>> dllist()
['', 'linux-vdso.so.1', '/lib/x86_64-linux-gnu/libm.so.6', '/lib/x86_64-linux-gnu/libc.so.6', ... ]

```

### Loading shared libraries[¶](https://docs.python.org/3/library/ctypes.html#loading-shared-libraries "Link to this heading")
There are several ways to load shared libraries into the Python process. One way is to instantiate one of the following classes:

_class_ ctypes.CDLL(_name_ , _mode =DEFAULT_MODE_, _handle =None_, _use_errno =False_, _use_last_error =False_, _winmode =None_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.CDLL "Link to this definition")

Instances of this class represent loaded shared libraries. Functions in these libraries use the standard C calling convention, and are assumed to return int.
On Windows creating a `CDLL` instance may fail even if the DLL name exists. When a dependent DLL of the loaded DLL is not found, a [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") error is raised with the message _“[WinError 126] The specified module could not be found”._ This error message does not contain the name of the missing DLL because the Windows API does not return this information making this error hard to diagnose. To resolve this error and determine which DLL is not found, you need to find the list of dependent DLLs and determine which one is not found using Windows debugging and tracing tools.
Changed in version 3.12: The _name_ parameter can now be a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).
See also

_class_ ctypes.OleDLL(_name_ , _mode =DEFAULT_MODE_, _handle =None_, _use_errno =False_, _use_last_error =False_, _winmode =None_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.OleDLL "Link to this definition")

Instances of this class represent loaded shared libraries, functions in these libraries use the `stdcall` calling convention, and are assumed to return the windows specific [`HRESULT`](https://docs.python.org/3/library/ctypes.html#ctypes.HRESULT "ctypes.HRESULT") code. `HRESULT` values contain information specifying whether the function call failed or succeeded, together with additional error code. If the return value signals a failure, an [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") is automatically raised.
[Availability](https://docs.python.org/3/library/intro.html#availability): Windows
Changed in version 3.3: [`WindowsError`](https://docs.python.org/3/library/exceptions.html#WindowsError "WindowsError") used to be raised, which is now an alias of [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError").
Changed in version 3.12: The _name_ parameter can now be a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).

_class_ ctypes.WinDLL(_name_ , _mode =DEFAULT_MODE_, _handle =None_, _use_errno =False_, _use_last_error =False_, _winmode =None_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.WinDLL "Link to this definition")

Instances of this class represent loaded shared libraries, functions in these libraries use the `stdcall` calling convention, and are assumed to return int by default.
[Availability](https://docs.python.org/3/library/intro.html#availability): Windows
Changed in version 3.12: The _name_ parameter can now be a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).
The Python [global interpreter lock](https://docs.python.org/3/glossary.html#term-global-interpreter-lock) is released before calling any function exported by these libraries, and reacquired afterwards.

_class_ ctypes.PyDLL(_name_ , _mode =DEFAULT_MODE_, _handle =None_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.PyDLL "Link to this definition")

Instances of this class behave like [`CDLL`](https://docs.python.org/3/library/ctypes.html#ctypes.CDLL "ctypes.CDLL") instances, except that the Python GIL is _not_ released during the function call, and after the function execution the Python error flag is checked. If the error flag is set, a Python exception is raised.
Thus, this is only useful to call Python C api functions directly.
Changed in version 3.12: The _name_ parameter can now be a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).
All these classes can be instantiated by calling them with at least one argument, the pathname of the shared library. If you have an existing handle to an already loaded shared library, it can be passed as the `handle` named parameter, otherwise the underlying platform’s `dlopen()` or `LoadLibrary()` function is used to load the library into the process, and to get a handle to it.
The _mode_ parameter can be used to specify how the library is loaded. For details, consult the _mode_ is ignored. On posix systems, RTLD_NOW is always added, and is not configurable.
The _use_errno_ parameter, when set to true, enables a ctypes mechanism that allows accessing the system [`errno`](https://docs.python.org/3/library/errno.html#module-errno "errno: Standard errno system symbols.") error number in a safe way. `ctypes` maintains a thread-local copy of the system’s `errno` variable; if you call foreign functions created with `use_errno=True` then the `errno` value before the function call is swapped with the ctypes private copy, the same happens immediately after the function call.
The function [`ctypes.get_errno()`](https://docs.python.org/3/library/ctypes.html#ctypes.get_errno "ctypes.get_errno") returns the value of the ctypes private copy, and the function [`ctypes.set_errno()`](https://docs.python.org/3/library/ctypes.html#ctypes.set_errno "ctypes.set_errno") changes the ctypes private copy to a new value and returns the former value.
The _use_last_error_ parameter, when set to true, enables the same mechanism for the Windows error code which is managed by the [`GetLastError()`](https://docs.python.org/3/library/ctypes.html#ctypes.GetLastError "ctypes.GetLastError") and `SetLastError()` Windows API functions; [`ctypes.get_last_error()`](https://docs.python.org/3/library/ctypes.html#ctypes.get_last_error "ctypes.get_last_error") and [`ctypes.set_last_error()`](https://docs.python.org/3/library/ctypes.html#ctypes.set_last_error "ctypes.set_last_error") are used to request and change the ctypes private copy of the windows error code.
The _winmode_ parameter is used on Windows to specify how the library is loaded (since _mode_ is ignored). It takes any value that is valid for the Win32 API `LoadLibraryEx` flags parameter. When omitted, the default is to use the flags that result in the most secure DLL load, which avoids issues such as DLL hijacking. Passing the full path to the DLL is the safest way to ensure the correct library and dependencies are loaded.
Changed in version 3.8: Added _winmode_ parameter.

ctypes.RTLD_GLOBAL

Flag to use as _mode_ parameter. On platforms where this flag is not available, it is defined as the integer zero.

ctypes.RTLD_LOCAL

Flag to use as _mode_ parameter. On platforms where this is not available, it is the same as _RTLD_GLOBAL_.

ctypes.DEFAULT_MODE

The default mode which is used to load shared libraries. On OSX 10.3, this is _RTLD_GLOBAL_ , otherwise it is the same as _RTLD_LOCAL_.
Instances of these classes have no public methods. Functions exported by the shared library can be accessed as attributes or by index. Please note that accessing the function through an attribute caches the result and therefore accessing it repeatedly returns the same object each time. On the other hand, accessing it through an index returns a new object each time:
Copy```
>>> from ctypes import CDLL
>>> libc = CDLL("libc.so.6")  # On Linux
>>> libc.time == libc.time
True
>>> libc['time'] == libc['time']
False

```

The following public attributes are available, their name starts with an underscore to not clash with exported function names:

PyDLL._handle[¶](https://docs.python.org/3/library/ctypes.html#ctypes.PyDLL._handle "Link to this definition")

The system handle used to access the library.

PyDLL._name[¶](https://docs.python.org/3/library/ctypes.html#ctypes.PyDLL._name "Link to this definition")

The name of the library passed in the constructor.
Shared libraries can also be loaded by using one of the prefabricated objects, which are instances of the [`LibraryLoader`](https://docs.python.org/3/library/ctypes.html#ctypes.LibraryLoader "ctypes.LibraryLoader") class, either by calling the [`LoadLibrary()`](https://docs.python.org/3/library/ctypes.html#ctypes.LibraryLoader.LoadLibrary "ctypes.LibraryLoader.LoadLibrary") method, or by retrieving the library as attribute of the loader instance.

_class_ ctypes.LibraryLoader(_dlltype_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.LibraryLoader "Link to this definition")

Class which loads shared libraries. _dlltype_ should be one of the [`CDLL`](https://docs.python.org/3/library/ctypes.html#ctypes.CDLL "ctypes.CDLL"), [`PyDLL`](https://docs.python.org/3/library/ctypes.html#ctypes.PyDLL "ctypes.PyDLL"), [`WinDLL`](https://docs.python.org/3/library/ctypes.html#ctypes.WinDLL "ctypes.WinDLL"), or [`OleDLL`](https://docs.python.org/3/library/ctypes.html#ctypes.OleDLL "ctypes.OleDLL") types.
`__getattr__()` has special behavior: It allows loading a shared library by accessing it as attribute of a library loader instance. The result is cached, so repeated attribute accesses return the same library each time.

LoadLibrary(_name_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.LibraryLoader.LoadLibrary "Link to this definition")

Load a shared library into the process and return it. This method always returns a new instance of the library.
These prefabricated library loaders are available:

ctypes.cdll

Creates [`CDLL`](https://docs.python.org/3/library/ctypes.html#ctypes.CDLL "ctypes.CDLL") instances.

ctypes.windll

Creates [`WinDLL`](https://docs.python.org/3/library/ctypes.html#ctypes.WinDLL "ctypes.WinDLL") instances.
[Availability](https://docs.python.org/3/library/intro.html#availability): Windows

ctypes.oledll

Creates [`OleDLL`](https://docs.python.org/3/library/ctypes.html#ctypes.OleDLL "ctypes.OleDLL") instances.
[Availability](https://docs.python.org/3/library/intro.html#availability): Windows

ctypes.pydll

Creates [`PyDLL`](https://docs.python.org/3/library/ctypes.html#ctypes.PyDLL "ctypes.PyDLL") instances.
For accessing the C Python api directly, a ready-to-use Python shared library object is available:

ctypes.pythonapi

An instance of [`PyDLL`](https://docs.python.org/3/library/ctypes.html#ctypes.PyDLL "ctypes.PyDLL") that exposes Python C API functions as attributes. Note that all these functions are assumed to return C int, which is of course not always the truth, so you have to assign the correct `restype` attribute to use these functions.
Loading a library through any of these objects raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `ctypes.dlopen` with string argument `name`, the name used to load the library.
Accessing a function on a loaded library raises an auditing event `ctypes.dlsym` with arguments `library` (the library object) and `name` (the symbol’s name as a string or integer).
In cases when only the library handle is available rather than the object, accessing a function raises an auditing event `ctypes.dlsym/handle` with arguments `handle` (the raw library handle) and `name`.
### Foreign functions[¶](https://docs.python.org/3/library/ctypes.html#foreign-functions "Link to this heading")
As explained in the previous section, foreign functions can be accessed as attributes of loaded shared libraries. The function objects created in this way by default accept any number of arguments, accept any ctypes data instances as arguments, and return the default result type specified by the library loader.
They are instances of a private local class `_FuncPtr` (not exposed in `ctypes`) which inherits from the private [`_CFuncPtr`](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr "ctypes._CFuncPtr") class:
Copy```
>>> import ctypes
>>> lib = ctypes.CDLL(None)
>>> issubclass(lib._FuncPtr, ctypes._CFuncPtr)
True
>>> lib._FuncPtr is ctypes._CFuncPtr
False

```


_class_ ctypes._CFuncPtr[¶](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr "Link to this definition")

Base class for C callable foreign functions.
Instances of foreign functions are also C compatible data types; they represent C function pointers.
This behavior can be customized by assigning to special attributes of the foreign function object.

restype[¶](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr.restype "Link to this definition")

Assign a ctypes type to specify the result type of the foreign function. Use `None` for void, a function not returning anything.
It is possible to assign a callable Python object that is not a ctypes type, in this case the function is assumed to return a C int, and the callable will be called with this integer, allowing further processing or error checking. Using this is deprecated, for more flexible post processing or error checking use a ctypes data type as `restype` and assign a callable to the [`errcheck`](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr.errcheck "ctypes._CFuncPtr.errcheck") attribute.

argtypes[¶](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr.argtypes "Link to this definition")

Assign a tuple of ctypes types to specify the argument types that the function accepts. Functions using the `stdcall` calling convention can only be called with the same number of arguments as the length of this tuple; functions using the C calling convention accept additional, unspecified arguments as well.
When a foreign function is called, each actual argument is passed to the [`from_param()`](https://docs.python.org/3/library/ctypes.html#ctypes._CData.from_param "ctypes._CData.from_param") class method of the items in the [`argtypes`](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr.argtypes "ctypes._CFuncPtr.argtypes") tuple, this method allows adapting the actual argument to an object that the foreign function accepts. For example, a [`c_char_p`](https://docs.python.org/3/library/ctypes.html#ctypes.c_char_p "ctypes.c_char_p") item in the `argtypes` tuple will convert a string passed as argument into a bytes object using ctypes conversion rules.
New: It is now possible to put items in argtypes which are not ctypes types, but each item must have a [`from_param()`](https://docs.python.org/3/library/ctypes.html#ctypes._CData.from_param "ctypes._CData.from_param") method which returns a value usable as argument (integer, string, ctypes instance). This allows defining adapters that can adapt custom objects as function parameters.

errcheck[¶](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr.errcheck "Link to this definition")

Assign a Python function or another callable to this attribute. The callable will be called with three or more arguments:

callable(_result_ , _func_ , _arguments_)

_result_ is what the foreign function returns, as specified by the `restype` attribute.
_func_ is the foreign function object itself, this allows reusing the same callable object to check or post process the results of several functions.
_arguments_ is a tuple containing the parameters originally passed to the function call, this allows specializing the behavior on the arguments used.
The object that this function returns will be returned from the foreign function call, but it can also check the result value and raise an exception if the foreign function call failed.
On Windows, when a foreign function call raises a system exception (for example, due to an access violation), it will be captured and replaced with a suitable Python exception. Further, an auditing event `ctypes.set_exception` with argument `code` will be raised, allowing an audit hook to replace the exception with its own.
Some ways to invoke foreign function calls as well as some of the functions in this module may raise an auditing event `ctypes.call_function` with arguments `function pointer` and `arguments`.
### Function prototypes[¶](https://docs.python.org/3/library/ctypes.html#function-prototypes "Link to this heading")
Foreign functions can also be created by instantiating function prototypes. Function prototypes are similar to function prototypes in C; they describe a function (return type, argument types, calling convention) without defining an implementation. The factory functions must be called with the desired result type and the argument types of the function, and can be used as decorator factories, and as such, be applied to functions through the `@wrapper` syntax. See [Callback functions](https://docs.python.org/3/library/ctypes.html#ctypes-callback-functions) for examples.

ctypes.CFUNCTYPE(_restype_ , _* argtypes_, _use_errno =False_, _use_last_error =False_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.CFUNCTYPE "Link to this definition")

The returned function prototype creates functions that use the standard C calling convention. The function will release the GIL during the call. If _use_errno_ is set to true, the ctypes private copy of the system [`errno`](https://docs.python.org/3/library/errno.html#module-errno "errno: Standard errno system symbols.") variable is exchanged with the real `errno` value before and after the call; _use_last_error_ does the same for the Windows error code.

ctypes.WINFUNCTYPE(_restype_ , _* argtypes_, _use_errno =False_, _use_last_error =False_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.WINFUNCTYPE "Link to this definition")

The returned function prototype creates functions that use the `stdcall` calling convention. The function will release the GIL during the call. _use_errno_ and _use_last_error_ have the same meaning as above.
[Availability](https://docs.python.org/3/library/intro.html#availability): Windows

ctypes.PYFUNCTYPE(_restype_ , _* argtypes_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.PYFUNCTYPE "Link to this definition")

The returned function prototype creates functions that use the Python calling convention. The function will _not_ release the GIL during the call.
Function prototypes created by these factory functions can be instantiated in different ways, depending on the type and number of the parameters in the call:

prototype(_address_)

Returns a foreign function at the specified address which must be an integer.

prototype(_callable_)

Create a C callable function (a callback function) from a Python _callable_.

prototype(_func_spec_[, _paramflags_])

Returns a foreign function exported by a shared library. _func_spec_ must be a 2-tuple `(name_or_ordinal, library)`. The first item is the name of the exported function as string, or the ordinal of the exported function as small integer. The second item is the shared library instance.

prototype(_vtbl_index_ , _name_[, _paramflags_[, _iid_]])

Returns a foreign function that will call a COM method. _vtbl_index_ is the index into the virtual function table, a small non-negative integer. _name_ is name of the COM method. _iid_ is an optional pointer to the interface identifier which is used in extended error reporting.
If _iid_ is not specified, an [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") is raised if the COM method call fails. If _iid_ is specified, a [`COMError`](https://docs.python.org/3/library/ctypes.html#ctypes.COMError "ctypes.COMError") is raised instead.
COM methods use a special calling convention: They require a pointer to the COM interface as first argument, in addition to those parameters that are specified in the `argtypes` tuple.
[Availability](https://docs.python.org/3/library/intro.html#availability): Windows
The optional _paramflags_ parameter creates foreign function wrappers with much more functionality than the features described above.
_paramflags_ must be a tuple of the same length as [`argtypes`](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr.argtypes "ctypes._CFuncPtr.argtypes").
Each item in this tuple contains further information about a parameter, it must be a tuple containing one, two, or three items.
The first item is an integer containing a combination of direction flags for the parameter:
>

1

> Specifies an input parameter to the function.

2

> Output parameter. The foreign function fills in a value.

4

> Input parameter which defaults to the integer zero.
The optional second item is the parameter name as string. If this is specified, the foreign function can be called with named parameters.
The optional third item is the default value for this parameter.
The following example demonstrates how to wrap the Windows `MessageBoxW` function so that it supports default parameters and named arguments. The C declaration from the windows header file is this:
Copy```
WINUSERAPI int WINAPI
MessageBoxW(
    HWND hWnd,
    LPCWSTR lpText,
    LPCWSTR lpCaption,
    UINT uType);

```

Here is the wrapping with `ctypes`:
Copy```
>>> from ctypes import c_int, WINFUNCTYPE, windll
>>> from ctypes.wintypes import HWND, LPCWSTR, UINT
>>> prototype = WINFUNCTYPE(c_int, HWND, LPCWSTR, LPCWSTR, UINT)
