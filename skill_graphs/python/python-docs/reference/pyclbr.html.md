[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`pyclbr` — Python module browser support](https://docs.python.org/3/library/pyclbr.html)
    * [Function Objects](https://docs.python.org/3/library/pyclbr.html#function-objects)
    * [Class Objects](https://docs.python.org/3/library/pyclbr.html#class-objects)


#### Previous topic
[`tabnanny` — Detection of ambiguous indentation](https://docs.python.org/3/library/tabnanny.html "previous chapter")
#### Next topic
[`py_compile` — Compile Python source files](https://docs.python.org/3/library/py_compile.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=pyclbr+%E2%80%94+Python+module+browser+support&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fpyclbr.html&pagesource=library%2Fpyclbr.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/py_compile.html "py_compile — Compile Python source files") |
  * [previous](https://docs.python.org/3/library/tabnanny.html "tabnanny — Detection of ambiguous indentation") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Python Language Services](https://docs.python.org/3/library/language.html) »
  * [`pyclbr` — Python module browser support](https://docs.python.org/3/library/pyclbr.html)
  * |
  * Theme  Auto Light Dark |


#  `pyclbr` — Python module browser support[¶](https://docs.python.org/3/library/pyclbr.html#module-pyclbr "Link to this heading")
**Source code:**
* * *
The `pyclbr` module provides limited information about the functions, classes, and methods defined in a Python-coded module. The information is sufficient to implement a module browser. The information is extracted from the Python source code rather than by importing the module, so this module is safe to use with untrusted code. This restriction makes it impossible to use this module with modules not implemented in Python, including all standard and optional extension modules.

pyclbr.readmodule(_module_ , _path =None_)[¶](https://docs.python.org/3/library/pyclbr.html#pyclbr.readmodule "Link to this definition")

Return a dictionary mapping module-level class names to class descriptors. If possible, descriptors for imported base classes are included. Parameter _module_ is a string with the name of the module to read; it may be the name of a module within a package. If given, _path_ is a sequence of directory paths prepended to `sys.path`, which is used to locate the module source code.
This function is the original interface and is only kept for back compatibility. It returns a filtered version of the following.

pyclbr.readmodule_ex(_module_ , _path =None_)[¶](https://docs.python.org/3/library/pyclbr.html#pyclbr.readmodule_ex "Link to this definition")

Return a dictionary-based tree containing a function or class descriptors for each function and class defined in the module with a `def` or `class` statement. The returned dictionary maps module-level function and class names to their descriptors. Nested objects are entered into the children dictionary of their parent. As with readmodule, _module_ names the module to be read and _path_ is prepended to sys.path. If the module being read is a package, the returned dictionary has a key `'__path__'` whose value is a list containing the package search path.
Added in version 3.7: Descriptors for nested definitions. They are accessed through the new children attribute. Each has a new parent attribute.
The descriptors returned by these functions are instances of Function and Class classes. Users are not expected to create instances of these classes.
## Function Objects[¶](https://docs.python.org/3/library/pyclbr.html#function-objects "Link to this heading")

_class_ pyclbr.Function[¶](https://docs.python.org/3/library/pyclbr.html#pyclbr.Function "Link to this definition")

Class `Function` instances describe functions defined by def statements. They have the following attributes:

file[¶](https://docs.python.org/3/library/pyclbr.html#pyclbr.Function.file "Link to this definition")

Name of the file in which the function is defined.

module[¶](https://docs.python.org/3/library/pyclbr.html#pyclbr.Function.module "Link to this definition")

The name of the module defining the function described.

name[¶](https://docs.python.org/3/library/pyclbr.html#pyclbr.Function.name "Link to this definition")

The name of the function.

lineno[¶](https://docs.python.org/3/library/pyclbr.html#pyclbr.Function.lineno "Link to this definition")

The line number in the file where the definition starts.

parent[¶](https://docs.python.org/3/library/pyclbr.html#pyclbr.Function.parent "Link to this definition")

For top-level functions, `None`. For nested functions, the parent.
Added in version 3.7.

children[¶](https://docs.python.org/3/library/pyclbr.html#pyclbr.Function.children "Link to this definition")

A [`dictionary`](https://docs.python.org/3/library/stdtypes.html#dict "dict") mapping names to descriptors for nested functions and classes.
Added in version 3.7.

is_async[¶](https://docs.python.org/3/library/pyclbr.html#pyclbr.Function.is_async "Link to this definition")

`True` for functions that are defined with the [`async`](https://docs.python.org/3/reference/compound_stmts.html#async-def) prefix, `False` otherwise.
Added in version 3.10.
## Class Objects[¶](https://docs.python.org/3/library/pyclbr.html#class-objects "Link to this heading")

_class_ pyclbr.Class[¶](https://docs.python.org/3/library/pyclbr.html#pyclbr.Class "Link to this definition")

Class `Class` instances describe classes defined by class statements. They have the same attributes as [`Functions`](https://docs.python.org/3/library/pyclbr.html#pyclbr.Function "pyclbr.Function") and two more.

file[¶](https://docs.python.org/3/library/pyclbr.html#pyclbr.Class.file "Link to this definition")

Name of the file in which the class is defined.

module[¶](https://docs.python.org/3/library/pyclbr.html#pyclbr.Class.module "Link to this definition")

The name of the module defining the class described.

name[¶](https://docs.python.org/3/library/pyclbr.html#pyclbr.Class.name "Link to this definition")

The name of the class.

lineno[¶](https://docs.python.org/3/library/pyclbr.html#pyclbr.Class.lineno "Link to this definition")

The line number in the file where the definition starts.

parent[¶](https://docs.python.org/3/library/pyclbr.html#pyclbr.Class.parent "Link to this definition")

For top-level classes, `None`. For nested classes, the parent.
Added in version 3.7.

children[¶](https://docs.python.org/3/library/pyclbr.html#pyclbr.Class.children "Link to this definition")

A dictionary mapping names to descriptors for nested functions and classes.
Added in version 3.7.

super[¶](https://docs.python.org/3/library/pyclbr.html#pyclbr.Class.super "Link to this definition")

A list of `Class` objects which describe the immediate base classes of the class being described. Classes which are named as superclasses but which are not discoverable by [`readmodule_ex()`](https://docs.python.org/3/library/pyclbr.html#pyclbr.readmodule_ex "pyclbr.readmodule_ex") are listed as a string with the class name instead of as `Class` objects.

methods[¶](https://docs.python.org/3/library/pyclbr.html#pyclbr.Class.methods "Link to this definition")

A [`dictionary`](https://docs.python.org/3/library/stdtypes.html#dict "dict") mapping method names to line numbers. This can be derived from the newer [`children`](https://docs.python.org/3/library/pyclbr.html#pyclbr.Class.children "pyclbr.Class.children") dictionary, but remains for back-compatibility.
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`pyclbr` — Python module browser support](https://docs.python.org/3/library/pyclbr.html)
    * [Function Objects](https://docs.python.org/3/library/pyclbr.html#function-objects)
    * [Class Objects](https://docs.python.org/3/library/pyclbr.html#class-objects)


#### Previous topic
[`tabnanny` — Detection of ambiguous indentation](https://docs.python.org/3/library/tabnanny.html "previous chapter")
#### Next topic
[`py_compile` — Compile Python source files](https://docs.python.org/3/library/py_compile.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=pyclbr+%E2%80%94+Python+module+browser+support&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fpyclbr.html&pagesource=library%2Fpyclbr.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/py_compile.html "py_compile — Compile Python source files") |
  * [previous](https://docs.python.org/3/library/tabnanny.html "tabnanny — Detection of ambiguous indentation") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Python Language Services](https://docs.python.org/3/library/language.html) »
  * [`pyclbr` — Python module browser support](https://docs.python.org/3/library/pyclbr.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
