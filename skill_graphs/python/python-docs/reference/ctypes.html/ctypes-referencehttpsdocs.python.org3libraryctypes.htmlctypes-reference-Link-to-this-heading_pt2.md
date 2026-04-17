>>> paramflags = (1, "hwnd", 0), (1, "text", "Hi"), (1, "caption", "Hello from ctypes"), (1, "flags", 0)
>>> MessageBox = prototype(("MessageBoxW", windll.user32), paramflags)

```

The `MessageBox` foreign function can now be called in these ways:
Copy```
>>> MessageBox()
>>> MessageBox(text="Spam, spam, spam")
>>> MessageBox(flags=2, text="foo bar")

```

A second example demonstrates output parameters. The win32 `GetWindowRect` function retrieves the dimensions of a specified window by copying them into `RECT` structure that the caller has to supply. Here is the C declaration:
Copy```
WINUSERAPI BOOL WINAPI
GetWindowRect(
     HWND hWnd,
     LPRECT lpRect);

```

Here is the wrapping with `ctypes`:
Copy```
>>> from ctypes import POINTER, WINFUNCTYPE, windll, WinError
>>> from ctypes.wintypes import BOOL, HWND, RECT
>>> prototype = WINFUNCTYPE(BOOL, HWND, POINTER(RECT))
>>> paramflags = (1, "hwnd"), (2, "lprect")
>>> GetWindowRect = prototype(("GetWindowRect", windll.user32), paramflags)
>>>

```

Functions with output parameters will automatically return the output parameter value if there is a single one, or a tuple containing the output parameter values when there are more than one, so the GetWindowRect function now returns a RECT instance, when called.
Output parameters can be combined with the [`errcheck`](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr.errcheck "ctypes._CFuncPtr.errcheck") protocol to do further output processing and error checking. The win32 `GetWindowRect` api function returns a `BOOL` to signal success or failure, so this function could do the error checking, and raises an exception when the api call failed:
Copy```
>>> def errcheck(result, func, args):
...     if not result:
...         raise WinError()
...     return args
...
>>> GetWindowRect.errcheck = errcheck
>>>

```

If the [`errcheck`](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr.errcheck "ctypes._CFuncPtr.errcheck") function returns the argument tuple it receives unchanged, `ctypes` continues the normal processing it does on the output parameters. If you want to return a tuple of window coordinates instead of a `RECT` instance, you can retrieve the fields in the function and return them instead, the normal processing will no longer take place:
Copy```
>>> def errcheck(result, func, args):
...     if not result:
...         raise WinError()
...     rc = args[1]
...     return rc.left, rc.top, rc.bottom, rc.right
...
>>> GetWindowRect.errcheck = errcheck
>>>

```

### Utility functions[¶](https://docs.python.org/3/library/ctypes.html#utility-functions "Link to this heading")

ctypes.addressof(_obj_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.addressof "Link to this definition")

Returns the address of the memory buffer as integer. _obj_ must be an instance of a ctypes type.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `ctypes.addressof` with argument `obj`.

ctypes.alignment(_obj_or_type_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.alignment "Link to this definition")

Returns the alignment requirements of a ctypes type. _obj_or_type_ must be a ctypes type or instance.

ctypes.byref(_obj_[, _offset_])[¶](https://docs.python.org/3/library/ctypes.html#ctypes.byref "Link to this definition")

Returns a light-weight pointer to _obj_ , which must be an instance of a ctypes type. _offset_ defaults to zero, and must be an integer that will be added to the internal pointer value.
`byref(obj, offset)` corresponds to this C code:
Copy```
(((char *)&obj) + offset)

```

The returned object can only be used as a foreign function call parameter. It behaves similar to `pointer(obj)`, but the construction is a lot faster.

ctypes.CopyComPointer(_src_ , _dst_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.CopyComPointer "Link to this definition")

Copies a COM pointer from _src_ to _dst_ and returns the Windows specific `HRESULT` value.
If _src_ is not `NULL`, its `AddRef` method is called, incrementing the reference count.
In contrast, the reference count of _dst_ will not be decremented before assigning the new value. Unless _dst_ is `NULL`, the caller is responsible for decrementing the reference count by calling its `Release` method when necessary.
[Availability](https://docs.python.org/3/library/intro.html#availability): Windows
Added in version 3.14.

ctypes.cast(_obj_ , _type_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.cast "Link to this definition")

This function is similar to the cast operator in C. It returns a new instance of _type_ which points to the same memory block as _obj_. _type_ must be a pointer type, and _obj_ must be an object that can be interpreted as a pointer.

ctypes.create_string_buffer(_init_ , _size =None_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.create_string_buffer "Link to this definition")


ctypes.create_string_buffer(_size_)

This function creates a mutable character buffer. The returned object is a ctypes array of [`c_char`](https://docs.python.org/3/library/ctypes.html#ctypes.c_char "ctypes.c_char").
If _size_ is given (and not `None`), it must be an [`int`](https://docs.python.org/3/library/functions.html#int "int"). It specifies the size of the returned array.
If the _init_ argument is given, it must be [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes"). It is used to initialize the array items. Bytes not initialized this way are set to zero (NUL).
If _size_ is not given (or if it is `None`), the buffer is made one element larger than _init_ , effectively adding a NUL terminator.
If both arguments are given, _size_ must not be less than `len(init)`.
Warning
If _size_ is equal to `len(init)`, a NUL terminator is not added. Do not treat such a buffer as a C string.
For example:
Copy```
>>> bytes(create_string_buffer(2))
b'\x00\x00'
>>> bytes(create_string_buffer(b'ab'))
b'ab\x00'
>>> bytes(create_string_buffer(b'ab', 2))
b'ab'
>>> bytes(create_string_buffer(b'ab', 4))
b'ab\x00\x00'
>>> bytes(create_string_buffer(b'abcdef', 2))
Traceback (most recent call last):
   ...
ValueError: byte string too long

```

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `ctypes.create_string_buffer` with arguments `init`, `size`.

ctypes.create_unicode_buffer(_init_ , _size =None_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.create_unicode_buffer "Link to this definition")


ctypes.create_unicode_buffer(_size_)

This function creates a mutable unicode character buffer. The returned object is a ctypes array of [`c_wchar`](https://docs.python.org/3/library/ctypes.html#ctypes.c_wchar "ctypes.c_wchar").
The function takes the same arguments as [`create_string_buffer()`](https://docs.python.org/3/library/ctypes.html#ctypes.create_string_buffer "ctypes.create_string_buffer") except _init_ must be a string and _size_ counts [`c_wchar`](https://docs.python.org/3/library/ctypes.html#ctypes.c_wchar "ctypes.c_wchar").
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `ctypes.create_unicode_buffer` with arguments `init`, `size`.

ctypes.DllCanUnloadNow()[¶](https://docs.python.org/3/library/ctypes.html#ctypes.DllCanUnloadNow "Link to this definition")

This function is a hook which allows implementing in-process COM servers with ctypes. It is called from the DllCanUnloadNow function that the _ctypes extension dll exports.
[Availability](https://docs.python.org/3/library/intro.html#availability): Windows

ctypes.DllGetClassObject()[¶](https://docs.python.org/3/library/ctypes.html#ctypes.DllGetClassObject "Link to this definition")

This function is a hook which allows implementing in-process COM servers with ctypes. It is called from the DllGetClassObject function that the `_ctypes` extension dll exports.
[Availability](https://docs.python.org/3/library/intro.html#availability): Windows

ctypes.util.find_library(_name_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.util.find_library "Link to this definition")

Try to find a library and return a pathname. _name_ is the library name without any prefix like `lib`, suffix like `.so`, `.dylib` or version number (this is the form used for the posix linker option `-l`). If no library can be found, returns `None`.
The exact functionality is system dependent.
See [Finding shared libraries](https://docs.python.org/3/library/ctypes.html#ctypes-finding-shared-libraries) for complete documentation.

ctypes.util.find_msvcrt()[¶](https://docs.python.org/3/library/ctypes.html#ctypes.util.find_msvcrt "Link to this definition")

Returns the filename of the VC runtime library used by Python, and by the extension modules. If the name of the library cannot be determined, `None` is returned.
If you need to free memory, for example, allocated by an extension module with a call to the `free(void *)`, it is important that you use the function in the same library that allocated the memory.
[Availability](https://docs.python.org/3/library/intro.html#availability): Windows

ctypes.util.dllist()[¶](https://docs.python.org/3/library/ctypes.html#ctypes.util.dllist "Link to this definition")

Try to provide a list of paths of the shared libraries loaded into the current process. These paths are not normalized or processed in any way. The function can raise [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") if the underlying platform APIs fail. The exact functionality is system dependent.
On most platforms, the first element of the list represents the current executable file. It may be an empty string.
[Availability](https://docs.python.org/3/library/intro.html#availability): Windows, macOS, iOS, glibc, BSD libc, musl
Added in version 3.14.

ctypes.FormatError([_code_])[¶](https://docs.python.org/3/library/ctypes.html#ctypes.FormatError "Link to this definition")

Returns a textual description of the error code _code_. If no error code is specified, the last error code is used by calling the Windows API function [`GetLastError()`](https://docs.python.org/3/library/ctypes.html#ctypes.GetLastError "ctypes.GetLastError").
[Availability](https://docs.python.org/3/library/intro.html#availability): Windows

ctypes.GetLastError()[¶](https://docs.python.org/3/library/ctypes.html#ctypes.GetLastError "Link to this definition")

Returns the last error code set by Windows in the calling thread. This function calls the Windows `GetLastError()` function directly, it does not return the ctypes-private copy of the error code.
[Availability](https://docs.python.org/3/library/intro.html#availability): Windows

ctypes.get_errno()[¶](https://docs.python.org/3/library/ctypes.html#ctypes.get_errno "Link to this definition")

Returns the current value of the ctypes-private copy of the system [`errno`](https://docs.python.org/3/library/errno.html#module-errno "errno: Standard errno system symbols.") variable in the calling thread.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `ctypes.get_errno` with no arguments.

ctypes.get_last_error()[¶](https://docs.python.org/3/library/ctypes.html#ctypes.get_last_error "Link to this definition")

Returns the current value of the ctypes-private copy of the system `LastError` variable in the calling thread.
[Availability](https://docs.python.org/3/library/intro.html#availability): Windows
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `ctypes.get_last_error` with no arguments.

ctypes.memmove(_dst_ , _src_ , _count_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.memmove "Link to this definition")

Same as the standard C memmove library function: copies _count_ bytes from _src_ to _dst_. _dst_ and _src_ must be integers or ctypes instances that can be converted to pointers.

ctypes.memset(_dst_ , _c_ , _count_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.memset "Link to this definition")

Same as the standard C memset library function: fills the memory block at address _dst_ with _count_ bytes of value _c_. _dst_ must be an integer specifying an address, or a ctypes instance.

ctypes.POINTER(_type_ , _/_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.POINTER "Link to this definition")

Create or return a ctypes pointer type. Pointer types are cached and reused internally, so calling this function repeatedly is cheap. _type_ must be a ctypes type.
**CPython implementation detail:** The resulting pointer type is cached in the `__pointer_type__` attribute of _type_. It is possible to set this attribute before the first call to `POINTER` in order to set a custom pointer type. However, doing this is discouraged: manually creating a suitable pointer type is difficult without relying on implementation details that may change in future Python versions.

ctypes.pointer(_obj_ , _/_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.pointer "Link to this definition")

Create a new pointer instance, pointing to _obj_. The returned object is of the type `POINTER(type(obj))`.
Note: If you just want to pass a pointer to an object to a foreign function call, you should use `byref(obj)` which is much faster.

ctypes.resize(_obj_ , _size_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.resize "Link to this definition")

This function resizes the internal memory buffer of _obj_ , which must be an instance of a ctypes type. It is not possible to make the buffer smaller than the native size of the objects type, as given by `sizeof(type(obj))`, but it is possible to enlarge the buffer.

ctypes.set_errno(_value_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.set_errno "Link to this definition")

Set the current value of the ctypes-private copy of the system [`errno`](https://docs.python.org/3/library/errno.html#module-errno "errno: Standard errno system symbols.") variable in the calling thread to _value_ and return the previous value.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `ctypes.set_errno` with argument `errno`.

ctypes.set_last_error(_value_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.set_last_error "Link to this definition")

Sets the current value of the ctypes-private copy of the system `LastError` variable in the calling thread to _value_ and return the previous value.
[Availability](https://docs.python.org/3/library/intro.html#availability): Windows
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `ctypes.set_last_error` with argument `error`.

ctypes.sizeof(_obj_or_type_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.sizeof "Link to this definition")

Returns the size in bytes of a ctypes type or instance memory buffer. Does the same as the C `sizeof` operator.

ctypes.string_at(_ptr_ , _size =-1_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.string_at "Link to this definition")

Return the byte string at _void *ptr_. If _size_ is specified, it is used as size, otherwise the string is assumed to be zero-terminated.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `ctypes.string_at` with arguments `ptr`, `size`.

ctypes.WinError(_code =None_, _descr =None_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.WinError "Link to this definition")

Creates an instance of [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError"). If _code_ is not specified, [`GetLastError()`](https://docs.python.org/3/library/ctypes.html#ctypes.GetLastError "ctypes.GetLastError") is called to determine the error code. If _descr_ is not specified, [`FormatError()`](https://docs.python.org/3/library/ctypes.html#ctypes.FormatError "ctypes.FormatError") is called to get a textual description of the error.
[Availability](https://docs.python.org/3/library/intro.html#availability): Windows
Changed in version 3.3: An instance of [`WindowsError`](https://docs.python.org/3/library/exceptions.html#WindowsError "WindowsError") used to be created, which is now an alias of [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError").

ctypes.wstring_at(_ptr_ , _size =-1_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wstring_at "Link to this definition")

Return the wide-character string at _void *ptr_. If _size_ is specified, it is used as the number of characters of the string, otherwise the string is assumed to be zero-terminated.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `ctypes.wstring_at` with arguments `ptr`, `size`.

ctypes.memoryview_at(_ptr_ , _size_ , _readonly =False_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.memoryview_at "Link to this definition")

Return a [`memoryview`](https://docs.python.org/3/library/stdtypes.html#memoryview "memoryview") object of length _size_ that references memory starting at _void *ptr_.
If _readonly_ is true, the returned `memoryview` object can not be used to modify the underlying memory. (Changes made by other means will still be reflected in the returned object.)
This function is similar to [`string_at()`](https://docs.python.org/3/library/ctypes.html#ctypes.string_at "ctypes.string_at") with the key difference of not making a copy of the specified memory. It is a semantically equivalent (but more efficient) alternative to `memoryview((c_byte * size).from_address(ptr))`. (While [`from_address()`](https://docs.python.org/3/library/ctypes.html#ctypes._CData.from_address "ctypes._CData.from_address") only takes integers, _ptr_ can also be given as a [`ctypes.POINTER`](https://docs.python.org/3/library/ctypes.html#ctypes.POINTER "ctypes.POINTER") or a [`byref()`](https://docs.python.org/3/library/ctypes.html#ctypes.byref "ctypes.byref") object.)
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `ctypes.memoryview_at` with arguments `address`, `size`, `readonly`.
Added in version 3.14.
### Data types[¶](https://docs.python.org/3/library/ctypes.html#data-types "Link to this heading")

_class_ ctypes._CData[¶](https://docs.python.org/3/library/ctypes.html#ctypes._CData "Link to this definition")

This non-public class is the common base class of all ctypes data types. Among other things, all ctypes type instances contain a memory block that hold C compatible data; the address of the memory block is returned by the [`addressof()`](https://docs.python.org/3/library/ctypes.html#ctypes.addressof "ctypes.addressof") helper function. Another instance variable is exposed as [`_objects`](https://docs.python.org/3/library/ctypes.html#ctypes._CData._objects "ctypes._CData._objects"); this contains other Python objects that need to be kept alive in case the memory block contains pointers.
Common methods of ctypes data types, these are all class methods (to be exact, they are methods of the [metaclass](https://docs.python.org/3/glossary.html#term-metaclass)):

from_buffer(_source_[, _offset_])[¶](https://docs.python.org/3/library/ctypes.html#ctypes._CData.from_buffer "Link to this definition")

This method returns a ctypes instance that shares the buffer of the _source_ object. The _source_ object must support the writeable buffer interface. The optional _offset_ parameter specifies an offset into the source buffer in bytes; the default is zero. If the source buffer is not large enough a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `ctypes.cdata/buffer` with arguments `pointer`, `size`, `offset`.

from_buffer_copy(_source_[, _offset_])[¶](https://docs.python.org/3/library/ctypes.html#ctypes._CData.from_buffer_copy "Link to this definition")

This method creates a ctypes instance, copying the buffer from the _source_ object buffer which must be readable. The optional _offset_ parameter specifies an offset into the source buffer in bytes; the default is zero. If the source buffer is not large enough a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `ctypes.cdata/buffer` with arguments `pointer`, `size`, `offset`.

from_address(_address_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes._CData.from_address "Link to this definition")

This method returns a ctypes type instance using the memory specified by _address_ which must be an integer.
This method, and others that indirectly call this method, raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `ctypes.cdata` with argument `address`.

from_param(_obj_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes._CData.from_param "Link to this definition")

This method adapts _obj_ to a ctypes type. It is called with the actual object used in a foreign function call when the type is present in the foreign function’s [`argtypes`](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr.argtypes "ctypes._CFuncPtr.argtypes") tuple; it must return an object that can be used as a function call parameter.
All ctypes data types have a default implementation of this classmethod that normally returns _obj_ if that is an instance of the type. Some types accept other objects as well.

in_dll(_library_ , _name_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes._CData.in_dll "Link to this definition")

This method returns a ctypes type instance exported by a shared library. _name_ is the name of the symbol that exports the data, _library_ is the loaded shared library.
Common class variables of ctypes data types:

__pointer_type__[¶](https://docs.python.org/3/library/ctypes.html#ctypes._CData.__pointer_type__ "Link to this definition")

The pointer type that was created by calling [`POINTER()`](https://docs.python.org/3/library/ctypes.html#ctypes.POINTER "ctypes.POINTER") for corresponding ctypes data type. If a pointer type was not yet created, the attribute is missing.
Added in version 3.14.
Common instance variables of ctypes data types:

_b_base_[¶](https://docs.python.org/3/library/ctypes.html#ctypes._CData._b_base_ "Link to this definition")

Sometimes ctypes data instances do not own the memory block they contain, instead they share part of the memory block of a base object. The [`_b_base_`](https://docs.python.org/3/library/ctypes.html#ctypes._CData._b_base_ "ctypes._CData._b_base_") read-only member is the root ctypes object that owns the memory block.

_b_needsfree_[¶](https://docs.python.org/3/library/ctypes.html#ctypes._CData._b_needsfree_ "Link to this definition")

This read-only variable is true when the ctypes data instance has allocated the memory block itself, false otherwise.

_objects[¶](https://docs.python.org/3/library/ctypes.html#ctypes._CData._objects "Link to this definition")

This member is either `None` or a dictionary containing Python objects that need to be kept alive so that the memory block contents is kept valid. This object is only exposed for debugging; never modify the contents of this dictionary.
### Fundamental data types[¶](https://docs.python.org/3/library/ctypes.html#ctypes-fundamental-data-types-2 "Link to this heading")

_class_ ctypes._SimpleCData[¶](https://docs.python.org/3/library/ctypes.html#ctypes._SimpleCData "Link to this definition")

This non-public class is the base class of all fundamental ctypes data types. It is mentioned here because it contains the common attributes of the fundamental ctypes data types. `_SimpleCData` is a subclass of [`_CData`](https://docs.python.org/3/library/ctypes.html#ctypes._CData "ctypes._CData"), so it inherits their methods and attributes. ctypes data types that are not and do not contain pointers can now be pickled.
Instances have a single attribute:

value[¶](https://docs.python.org/3/library/ctypes.html#ctypes._SimpleCData.value "Link to this definition")

This attribute contains the actual value of the instance. For integer and pointer types, it is an integer, for character types, it is a single character bytes object or string, for character pointer types it is a Python bytes object or string.
When the `value` attribute is retrieved from a ctypes instance, usually a new object is returned each time. `ctypes` does _not_ implement original object return, always a new object is constructed. The same is true for all other ctypes object instances.
Fundamental data types, when returned as foreign function call results, or, for example, by retrieving structure field members or array items, are transparently converted to native Python types. In other words, if a foreign function has a [`restype`](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr.restype "ctypes._CFuncPtr.restype") of [`c_char_p`](https://docs.python.org/3/library/ctypes.html#ctypes.c_char_p "ctypes.c_char_p"), you will always receive a Python bytes object, _not_ a `c_char_p` instance.
Subclasses of fundamental data types do _not_ inherit this behavior. So, if a foreign functions `restype` is a subclass of [`c_void_p`](https://docs.python.org/3/library/ctypes.html#ctypes.c_void_p "ctypes.c_void_p"), you will receive an instance of this subclass from the function call. Of course, you can get the value of the pointer by accessing the `value` attribute.
