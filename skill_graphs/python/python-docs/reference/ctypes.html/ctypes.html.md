[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
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
