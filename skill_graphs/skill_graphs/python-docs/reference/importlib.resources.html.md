[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`importlib.resources` – Package resource reading, opening and access](https://docs.python.org/3/library/importlib.resources.html)
    * [Functional API](https://docs.python.org/3/library/importlib.resources.html#functional-api)


#### Previous topic
[`importlib` — The implementation of `import`](https://docs.python.org/3/library/importlib.html "previous chapter")
#### Next topic
[`importlib.resources.abc` – Abstract base classes for resources](https://docs.python.org/3/library/importlib.resources.abc.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=importlib.resources+%E2%80%93+Package+resource+reading%2C+opening+and+access&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fimportlib.resources.html&pagesource=library%2Fimportlib.resources.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/importlib.resources.abc.html "importlib.resources.abc – Abstract base classes for resources") |
  * [previous](https://docs.python.org/3/library/importlib.html "importlib — The implementation of import") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Importing Modules](https://docs.python.org/3/library/modules.html) »
  * [`importlib.resources` – Package resource reading, opening and access](https://docs.python.org/3/library/importlib.resources.html)
  * |
  * Theme  Auto Light Dark |


#  `importlib.resources` – Package resource reading, opening and access[¶](https://docs.python.org/3/library/importlib.resources.html#module-importlib.resources "Link to this heading")
**Source code:**
* * *
Added in version 3.7.
This module leverages Python’s import system to provide access to _resources_ within _packages_.
“Resources” are file-like resources associated with a module or package in Python. The resources may be contained directly in a package, within a subdirectory contained in that package, or adjacent to modules outside a package. Resources may be text or binary. As a result, a package’s Python module sources (.py), compilation artifacts (pycache), and installation artifacts (like [`reserved filenames`](https://docs.python.org/3/library/os.path.html#os.path.isreserved "os.path.isreserved") in directories) are technically de-facto resources of that package. In practice, however, resources are primarily those non-Python artifacts exposed specifically by the package author.
Resources can be opened or read in either binary or text mode.
Resources are roughly akin to files inside directories, though it’s important to keep in mind that this is just a metaphor. Resources and packages **do not** have to exist as physical files and directories on the file system: for example, a package and its resources can be imported from a zip file using [`zipimport`](https://docs.python.org/3/library/zipimport.html#module-zipimport "zipimport: Support for importing Python modules from ZIP archives.").
Note
This module provides functionality similar to
The standalone backport of this module provides more information on
[`Loaders`](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader "importlib.abc.Loader") that wish to support resource reading should implement a `get_resource_reader(fullname)` method as specified by [`importlib.resources.abc.ResourceReader`](https://docs.python.org/3/library/importlib.resources.abc.html#importlib.resources.abc.ResourceReader "importlib.resources.abc.ResourceReader").

_class_ importlib.resources.Anchor[¶](https://docs.python.org/3/library/importlib.resources.html#importlib.resources.Anchor "Link to this definition")

Represents an anchor for resources, either a [`module object`](https://docs.python.org/3/library/types.html#types.ModuleType "types.ModuleType") or a module name as a string. Defined as `Union[str, ModuleType]`.

importlib.resources.files(_anchor :[Anchor](https://docs.python.org/3/library/importlib.resources.html#importlib.resources.Anchor "importlib.resources.Anchor")|[None](https://docs.python.org/3/library/constants.html#None "None")=None_)[¶](https://docs.python.org/3/library/importlib.resources.html#importlib.resources.files "Link to this definition")

Returns a [`Traversable`](https://docs.python.org/3/library/importlib.resources.abc.html#importlib.resources.abc.Traversable "importlib.resources.abc.Traversable") object representing the resource container (think directory) and its resources (think files). A Traversable may contain other containers (think subdirectories).
_anchor_ is an optional [`Anchor`](https://docs.python.org/3/library/importlib.resources.html#importlib.resources.Anchor "importlib.resources.Anchor"). If the anchor is a package, resources are resolved from that package. If a module, resources are resolved adjacent to that module (in the same package or the package root). If the anchor is omitted, the caller’s module is used.
Added in version 3.9.
Changed in version 3.12: _package_ parameter was renamed to _anchor_. _anchor_ can now be a non-package module and if omitted will default to the caller’s module. _package_ is still accepted for compatibility but will raise a [`DeprecationWarning`](https://docs.python.org/3/library/exceptions.html#DeprecationWarning "DeprecationWarning"). Consider passing the anchor positionally or using `importlib_resources >= 5.10` for a compatible interface on older Pythons.

importlib.resources.as_file(_traversable_)[¶](https://docs.python.org/3/library/importlib.resources.html#importlib.resources.as_file "Link to this definition")

Given a [`Traversable`](https://docs.python.org/3/library/importlib.resources.abc.html#importlib.resources.abc.Traversable "importlib.resources.abc.Traversable") object representing a file or directory, typically from [`importlib.resources.files()`](https://docs.python.org/3/library/importlib.resources.html#importlib.resources.files "importlib.resources.files"), return a context manager for use in a [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) statement. The context manager provides a [`pathlib.Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path") object.
Exiting the context manager cleans up any temporary file or directory created when the resource was extracted from e.g. a zip file.
Use `as_file` when the Traversable methods (`read_text`, etc) are insufficient and an actual file or directory on the file system is required.
Added in version 3.9.
Changed in version 3.12: Added support for _traversable_ representing a directory.
## Functional API[¶](https://docs.python.org/3/library/importlib.resources.html#functional-api "Link to this heading")
A set of simplified, backwards-compatible helpers is available. These allow common operations in a single function call.
For all the following functions:
  * _anchor_ is an [`Anchor`](https://docs.python.org/3/library/importlib.resources.html#importlib.resources.Anchor "importlib.resources.Anchor"), as in [`files()`](https://docs.python.org/3/library/importlib.resources.html#importlib.resources.files "importlib.resources.files"). Unlike in `files`, it may not be omitted.
  * _path_names_ are components of a resource’s path name, relative to the anchor. For example, to get the text of resource named `info.txt`, use:
Copy```
importlib.resources.read_text(my_module, "info.txt")

```

Like [`Traversable.joinpath`](https://docs.python.org/3/library/importlib.resources.abc.html#importlib.resources.abc.Traversable "importlib.resources.abc.Traversable"), The individual components should use forward slashes (`/`) as path separators. For example, the following are equivalent:
Copy```
importlib.resources.read_binary(my_module, "pics/painting.png")
importlib.resources.read_binary(my_module, "pics", "painting.png")

```

For backward compatibility reasons, functions that read text require an explicit _encoding_ argument if multiple _path_names_ are given. For example, to get the text of `info/chapter1.txt`, use:
Copy```
importlib.resources.read_text(my_module, "info", "chapter1.txt",
                              encoding='utf-8')

```




importlib.resources.open_binary(_anchor_ , _* path_names_)[¶](https://docs.python.org/3/library/importlib.resources.html#importlib.resources.open_binary "Link to this definition")

Open the named resource for binary reading.
See [the introduction](https://docs.python.org/3/library/importlib.resources.html#importlib-resources-functional) for details on _anchor_ and _path_names_.
This function returns a [`BinaryIO`](https://docs.python.org/3/library/typing.html#typing.BinaryIO "typing.BinaryIO") object, that is, a binary stream open for reading.
This function is roughly equivalent to:
Copy```
files(anchor).joinpath(*path_names).open('rb')

```

Changed in version 3.13: Multiple _path_names_ are accepted.

importlib.resources.open_text(_anchor_ , _* path_names_, _encoding ='utf-8'_, _errors ='strict'_)[¶](https://docs.python.org/3/library/importlib.resources.html#importlib.resources.open_text "Link to this definition")

Open the named resource for text reading. By default, the contents are read as strict UTF-8.
See [the introduction](https://docs.python.org/3/library/importlib.resources.html#importlib-resources-functional) for details on _anchor_ and _path_names_. _encoding_ and _errors_ have the same meaning as in built-in [`open()`](https://docs.python.org/3/library/functions.html#open "open").
For backward compatibility reasons, the _encoding_ argument must be given explicitly if there are multiple _path_names_. This limitation is scheduled to be removed in Python 3.15.
This function returns a [`TextIO`](https://docs.python.org/3/library/typing.html#typing.TextIO "typing.TextIO") object, that is, a text stream open for reading.
This function is roughly equivalent to:
Copy```
files(anchor).joinpath(*path_names).open('r', encoding=encoding)

```

Changed in version 3.13: Multiple _path_names_ are accepted. _encoding_ and _errors_ must be given as keyword arguments.

importlib.resources.read_binary(_anchor_ , _* path_names_)[¶](https://docs.python.org/3/library/importlib.resources.html#importlib.resources.read_binary "Link to this definition")

Read and return the contents of the named resource as [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes").
See [the introduction](https://docs.python.org/3/library/importlib.resources.html#importlib-resources-functional) for details on _anchor_ and _path_names_.
This function is roughly equivalent to:
Copy```
files(anchor).joinpath(*path_names).read_bytes()

```

Changed in version 3.13: Multiple _path_names_ are accepted.

importlib.resources.read_text(_anchor_ , _* path_names_, _encoding ='utf-8'_, _errors ='strict'_)[¶](https://docs.python.org/3/library/importlib.resources.html#importlib.resources.read_text "Link to this definition")

Read and return the contents of the named resource as [`str`](https://docs.python.org/3/library/stdtypes.html#str "str"). By default, the contents are read as strict UTF-8.
See [the introduction](https://docs.python.org/3/library/importlib.resources.html#importlib-resources-functional) for details on _anchor_ and _path_names_. _encoding_ and _errors_ have the same meaning as in built-in [`open()`](https://docs.python.org/3/library/functions.html#open "open").
For backward compatibility reasons, the _encoding_ argument must be given explicitly if there are multiple _path_names_. This limitation is scheduled to be removed in Python 3.15.
This function is roughly equivalent to:
Copy```
files(anchor).joinpath(*path_names).read_text(encoding=encoding)

```

Changed in version 3.13: Multiple _path_names_ are accepted. _encoding_ and _errors_ must be given as keyword arguments.

importlib.resources.path(_anchor_ , _* path_names_)[¶](https://docs.python.org/3/library/importlib.resources.html#importlib.resources.path "Link to this definition")

Provides the path to the _resource_ as an actual file system path. This function returns a context manager for use in a [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) statement. The context manager provides a [`pathlib.Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path") object.
Exiting the context manager cleans up any temporary files created, e.g. when the resource needs to be extracted from a zip file.
For example, the [`stat()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.stat "pathlib.Path.stat") method requires an actual file system path; it can be used like this:
Copy```
with importlib.resources.path(anchor, "resource.txt") as fspath:
    result = fspath.stat()

```

See [the introduction](https://docs.python.org/3/library/importlib.resources.html#importlib-resources-functional) for details on _anchor_ and _path_names_.
This function is roughly equivalent to:
Copy```
as_file(files(anchor).joinpath(*path_names))

```

Changed in version 3.13: Multiple _path_names_ are accepted. _encoding_ and _errors_ must be given as keyword arguments.

importlib.resources.is_resource(_anchor_ , _* path_names_)[¶](https://docs.python.org/3/library/importlib.resources.html#importlib.resources.is_resource "Link to this definition")

Return `True` if the named resource exists, otherwise `False`. This function does not consider directories to be resources.
See [the introduction](https://docs.python.org/3/library/importlib.resources.html#importlib-resources-functional) for details on _anchor_ and _path_names_.
This function is roughly equivalent to:
Copy```
files(anchor).joinpath(*path_names).is_file()

```

Changed in version 3.13: Multiple _path_names_ are accepted.

importlib.resources.contents(_anchor_ , _* path_names_)[¶](https://docs.python.org/3/library/importlib.resources.html#importlib.resources.contents "Link to this definition")

Return an iterable over the named items within the package or path. The iterable returns names of resources (e.g. files) and non-resources (e.g. directories) as [`str`](https://docs.python.org/3/library/stdtypes.html#str "str"). The iterable does not recurse into subdirectories.
See [the introduction](https://docs.python.org/3/library/importlib.resources.html#importlib-resources-functional) for details on _anchor_ and _path_names_.
This function is roughly equivalent to:
Copy```
for resource in files(anchor).joinpath(*path_names).iterdir():
    yield resource.name

```

Deprecated since version 3.11: Prefer `iterdir()` as above, which offers more control over the results and richer functionality.
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`importlib.resources` – Package resource reading, opening and access](https://docs.python.org/3/library/importlib.resources.html)
    * [Functional API](https://docs.python.org/3/library/importlib.resources.html#functional-api)


#### Previous topic
[`importlib` — The implementation of `import`](https://docs.python.org/3/library/importlib.html "previous chapter")
#### Next topic
[`importlib.resources.abc` – Abstract base classes for resources](https://docs.python.org/3/library/importlib.resources.abc.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=importlib.resources+%E2%80%93+Package+resource+reading%2C+opening+and+access&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fimportlib.resources.html&pagesource=library%2Fimportlib.resources.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/importlib.resources.abc.html "importlib.resources.abc – Abstract base classes for resources") |
  * [previous](https://docs.python.org/3/library/importlib.html "importlib — The implementation of import") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Importing Modules](https://docs.python.org/3/library/modules.html) »
  * [`importlib.resources` – Package resource reading, opening and access](https://docs.python.org/3/library/importlib.resources.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
