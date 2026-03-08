
A positive integer specifying the number of elements in the array. Out-of-range subscripts result in an [`IndexError`](https://docs.python.org/3/library/exceptions.html#IndexError "IndexError"). Will be returned by [`len()`](https://docs.python.org/3/library/functions.html#len "len").

_type_[¶](https://docs.python.org/3/library/ctypes.html#ctypes.Array._type_ "Link to this definition")

Specifies the type of each element in the array.
Array subclass constructors accept positional arguments, used to initialize the elements in order.

ctypes.ARRAY(_type_ , _length_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.ARRAY "Link to this definition")

Create an array. Equivalent to `type * length`, where _type_ is a `ctypes` data type and _length_ an integer.
This function is [soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated) in favor of multiplication. There are no plans to remove it.

_class_ ctypes._Pointer[¶](https://docs.python.org/3/library/ctypes.html#ctypes._Pointer "Link to this definition")

Private, abstract base class for pointers.
Concrete pointer types are created by calling [`POINTER()`](https://docs.python.org/3/library/ctypes.html#ctypes.POINTER "ctypes.POINTER") with the type that will be pointed to; this is done automatically by [`pointer()`](https://docs.python.org/3/library/ctypes.html#ctypes.pointer "ctypes.pointer").
If a pointer points to an array, its elements can be read and written using standard subscript and slice accesses. Pointer objects have no size, so [`len()`](https://docs.python.org/3/library/functions.html#len "len") will raise [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError"). Negative subscripts will read from the memory _before_ the pointer (as in C), and out-of-range subscripts will probably crash with an access violation (if you’re lucky).

_type_[¶](https://docs.python.org/3/library/ctypes.html#ctypes._Pointer._type_ "Link to this definition")

Specifies the type pointed to.

contents[¶](https://docs.python.org/3/library/ctypes.html#ctypes._Pointer.contents "Link to this definition")

Returns the object to which to pointer points. Assigning to this attribute changes the pointer to point to the assigned object.
### Exceptions[¶](https://docs.python.org/3/library/ctypes.html#exceptions "Link to this heading")

_exception_ ctypes.ArgumentError[¶](https://docs.python.org/3/library/ctypes.html#ctypes.ArgumentError "Link to this definition")

This exception is raised when a foreign function call cannot convert one of the passed arguments.

_exception_ ctypes.COMError(_hresult_ , _text_ , _details_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.COMError "Link to this definition")

This exception is raised when a COM method call failed.

hresult[¶](https://docs.python.org/3/library/ctypes.html#ctypes.COMError.hresult "Link to this definition")

The integer value representing the error code.

text[¶](https://docs.python.org/3/library/ctypes.html#ctypes.COMError.text "Link to this definition")

The error message.

details[¶](https://docs.python.org/3/library/ctypes.html#ctypes.COMError.details "Link to this definition")

The 5-tuple `(descr, source, helpfile, helpcontext, progid)`.
_descr_ is the textual description. _source_ is the language-dependent `ProgID` for the class or application that raised the error. _helpfile_ is the path of the help file. _helpcontext_ is the help context identifier. _progid_ is the `ProgID` of the interface that defined the error.
[Availability](https://docs.python.org/3/library/intro.html#availability): Windows
Added in version 3.14.
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`ctypes` — A foreign function library for Python](https://docs.python.org/3/library/ctypes.html)
    * [ctypes tutorial](https://docs.python.org/3/library/ctypes.html#ctypes-tutorial)
      * [Loading dynamic link libraries](https://docs.python.org/3/library/ctypes.html#loading-dynamic-link-libraries)
      * [Accessing functions from loaded dlls](https://docs.python.org/3/library/ctypes.html#accessing-functions-from-loaded-dlls)
      * [Calling functions](https://docs.python.org/3/library/ctypes.html#calling-functions)
      * [Fundamental data types](https://docs.python.org/3/library/ctypes.html#fundamental-data-types)
      * [Calling functions, continued](https://docs.python.org/3/library/ctypes.html#calling-functions-continued)
      * [Calling variadic functions](https://docs.python.org/3/library/ctypes.html#calling-variadic-functions)
      * [Calling functions with your own custom data types](https://docs.python.org/3/library/ctypes.html#calling-functions-with-your-own-custom-data-types)
      * [Specifying the required argument types (function prototypes)](https://docs.python.org/3/library/ctypes.html#specifying-the-required-argument-types-function-prototypes)
      * [Return types](https://docs.python.org/3/library/ctypes.html#return-types)
      * [Passing pointers (or: passing parameters by reference)](https://docs.python.org/3/library/ctypes.html#passing-pointers-or-passing-parameters-by-reference)
      * [Structures and unions](https://docs.python.org/3/library/ctypes.html#structures-and-unions)
      * [Structure/union layout, alignment and byte order](https://docs.python.org/3/library/ctypes.html#structure-union-layout-alignment-and-byte-order)
      * [Bit fields in structures and unions](https://docs.python.org/3/library/ctypes.html#bit-fields-in-structures-and-unions)
      * [Arrays](https://docs.python.org/3/library/ctypes.html#arrays)
      * [Pointers](https://docs.python.org/3/library/ctypes.html#pointers)
      * [Thread safety without the GIL](https://docs.python.org/3/library/ctypes.html#thread-safety-without-the-gil)
      * [Type conversions](https://docs.python.org/3/library/ctypes.html#type-conversions)
      * [Incomplete Types](https://docs.python.org/3/library/ctypes.html#incomplete-types)
      * [Callback functions](https://docs.python.org/3/library/ctypes.html#callback-functions)
      * [Accessing values exported from dlls](https://docs.python.org/3/library/ctypes.html#accessing-values-exported-from-dlls)
      * [Surprises](https://docs.python.org/3/library/ctypes.html#surprises)
      * [Variable-sized data types](https://docs.python.org/3/library/ctypes.html#variable-sized-data-types)
    * [ctypes reference](https://docs.python.org/3/library/ctypes.html#ctypes-reference)
      * [Finding shared libraries](https://docs.python.org/3/library/ctypes.html#finding-shared-libraries)
      * [Listing loaded shared libraries](https://docs.python.org/3/library/ctypes.html#listing-loaded-shared-libraries)
      * [Loading shared libraries](https://docs.python.org/3/library/ctypes.html#loading-shared-libraries)
      * [Foreign functions](https://docs.python.org/3/library/ctypes.html#foreign-functions)
      * [Function prototypes](https://docs.python.org/3/library/ctypes.html#function-prototypes)
      * [Utility functions](https://docs.python.org/3/library/ctypes.html#utility-functions)
      * [Data types](https://docs.python.org/3/library/ctypes.html#data-types)
      * [Fundamental data types](https://docs.python.org/3/library/ctypes.html#ctypes-fundamental-data-types-2)
      * [Structured data types](https://docs.python.org/3/library/ctypes.html#structured-data-types)
      * [Arrays and pointers](https://docs.python.org/3/library/ctypes.html#arrays-and-pointers)
      * [Exceptions](https://docs.python.org/3/library/ctypes.html#exceptions)


#### Previous topic
[`errno` — Standard errno system symbols](https://docs.python.org/3/library/errno.html "previous chapter")
#### Next topic
[Command-line interface libraries](https://docs.python.org/3/library/cmdlinelibs.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=ctypes+%E2%80%94+A+foreign+function+library+for+Python&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fctypes.html&pagesource=library%2Fctypes.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/cmdlinelibs.html "Command-line interface libraries") |
  * [previous](https://docs.python.org/3/library/errno.html "errno — Standard errno system symbols") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Generic Operating System Services](https://docs.python.org/3/library/allows.html) »
  * [`ctypes` — A foreign function library for Python](https://docs.python.org/3/library/ctypes.html)
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
