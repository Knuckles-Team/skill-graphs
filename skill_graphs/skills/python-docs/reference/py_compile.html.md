[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`py_compile` — Compile Python source files](https://docs.python.org/3/library/py_compile.html)
    * [Command-Line Interface](https://docs.python.org/3/library/py_compile.html#command-line-interface)


#### Previous topic
[`pyclbr` — Python module browser support](https://docs.python.org/3/library/pyclbr.html "previous chapter")
#### Next topic
[`compileall` — Byte-compile Python libraries](https://docs.python.org/3/library/compileall.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=py_compile+%E2%80%94+Compile+Python+source+files&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fpy_compile.html&pagesource=library%2Fpy_compile.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/compileall.html "compileall — Byte-compile Python libraries") |
  * [previous](https://docs.python.org/3/library/pyclbr.html "pyclbr — Python module browser support") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Python Language Services](https://docs.python.org/3/library/language.html) »
  * [`py_compile` — Compile Python source files](https://docs.python.org/3/library/py_compile.html)
  * |
  * Theme  Auto Light Dark |


#  `py_compile` — Compile Python source files[¶](https://docs.python.org/3/library/py_compile.html#module-py_compile "Link to this heading")
**Source code:**
* * *
The `py_compile` module provides a function to generate a byte-code file from a source file, and another function used when the module source file is invoked as a script.
Though not often needed, this function can be useful when installing modules for shared use, especially if some of the users may not have permission to write the byte-code cache files in the directory containing the source code.

_exception_ py_compile.PyCompileError[¶](https://docs.python.org/3/library/py_compile.html#py_compile.PyCompileError "Link to this definition")

Exception raised when an error occurs while attempting to compile the file.

py_compile.compile(_file_ , _cfile =None_, _dfile =None_, _doraise =False_, _optimize =-1_, _invalidation_mode =PycInvalidationMode.TIMESTAMP_, _quiet =0_)[¶](https://docs.python.org/3/library/py_compile.html#py_compile.compile "Link to this definition")

Compile a source file to byte-code and write out the byte-code cache file. The source code is loaded from the file named _file_. The byte-code is written to _cfile_ , which defaults to the [**PEP 3147**](https://peps.python.org/pep-3147/)/[**PEP 488**](https://peps.python.org/pep-0488/) path, ending in `.pyc`. For example, if _file_ is `/foo/bar/baz.py` _cfile_ will default to `/foo/bar/__pycache__/baz.cpython-32.pyc` for Python 3.2. If _dfile_ is specified, it is used instead of _file_ as the name of the source file from which source lines are obtained for display in exception tracebacks. If _doraise_ is true, a [`PyCompileError`](https://docs.python.org/3/library/py_compile.html#py_compile.PyCompileError "py_compile.PyCompileError") is raised when an error is encountered while compiling _file_. If _doraise_ is false (the default), an error string is written to `sys.stderr`, but no exception is raised. This function returns the path to byte-compiled file, i.e. whatever _cfile_ value was used.
The _doraise_ and _quiet_ arguments determine how errors are handled while compiling file. If _quiet_ is 0 or 1, and _doraise_ is false, the default behaviour is enabled: an error string is written to `sys.stderr`, and the function returns `None` instead of a path. If _doraise_ is true, a [`PyCompileError`](https://docs.python.org/3/library/py_compile.html#py_compile.PyCompileError "py_compile.PyCompileError") is raised instead. However if _quiet_ is 2, no message is written, and _doraise_ has no effect.
If the path that _cfile_ becomes (either explicitly specified or computed) is a symlink or non-regular file, [`FileExistsError`](https://docs.python.org/3/library/exceptions.html#FileExistsError "FileExistsError") will be raised. This is to act as a warning that import will turn those paths into regular files if it is allowed to write byte-compiled files to those paths. This is a side-effect of import using file renaming to place the final byte-compiled file into place to prevent concurrent file writing issues.
_optimize_ controls the optimization level and is passed to the built-in `compile()` function. The default of `-1` selects the optimization level of the current interpreter.
_invalidation_mode_ should be a member of the [`PycInvalidationMode`](https://docs.python.org/3/library/py_compile.html#py_compile.PycInvalidationMode "py_compile.PycInvalidationMode") enum and controls how the generated bytecode cache is invalidated at runtime. The default is [`PycInvalidationMode.CHECKED_HASH`](https://docs.python.org/3/library/py_compile.html#py_compile.PycInvalidationMode.CHECKED_HASH "py_compile.PycInvalidationMode.CHECKED_HASH") if the `SOURCE_DATE_EPOCH` environment variable is set, otherwise the default is [`PycInvalidationMode.TIMESTAMP`](https://docs.python.org/3/library/py_compile.html#py_compile.PycInvalidationMode.TIMESTAMP "py_compile.PycInvalidationMode.TIMESTAMP").
Changed in version 3.2: Changed default value of _cfile_ to be [**PEP 3147**](https://peps.python.org/pep-3147/)-compliant. Previous default was _file_ + `'c'` (`'o'` if optimization was enabled). Also added the _optimize_ parameter.
Changed in version 3.4: Changed code to use [`importlib`](https://docs.python.org/3/library/importlib.html#module-importlib "importlib: The implementation of the import machinery.") for the byte-code cache file writing. This means file creation/writing semantics now match what `importlib` does, e.g. permissions, write-and-move semantics, etc. Also added the caveat that [`FileExistsError`](https://docs.python.org/3/library/exceptions.html#FileExistsError "FileExistsError") is raised if _cfile_ is a symlink or non-regular file.
Changed in version 3.7: The _invalidation_mode_ parameter was added as specified in [**PEP 552**](https://peps.python.org/pep-0552/). If the `SOURCE_DATE_EPOCH` environment variable is set, _invalidation_mode_ will be forced to [`PycInvalidationMode.CHECKED_HASH`](https://docs.python.org/3/library/py_compile.html#py_compile.PycInvalidationMode.CHECKED_HASH "py_compile.PycInvalidationMode.CHECKED_HASH").
Changed in version 3.7.2: The `SOURCE_DATE_EPOCH` environment variable no longer overrides the value of the _invalidation_mode_ argument, and determines its default value instead.
Changed in version 3.8: The _quiet_ parameter was added.

_class_ py_compile.PycInvalidationMode[¶](https://docs.python.org/3/library/py_compile.html#py_compile.PycInvalidationMode "Link to this definition")

An enumeration of possible methods the interpreter can use to determine whether a bytecode file is up to date with a source file. The `.pyc` file indicates the desired invalidation mode in its header. See [Cached bytecode invalidation](https://docs.python.org/3/reference/import.html#pyc-invalidation) for more information on how Python invalidates `.pyc` files at runtime.
Added in version 3.7.

TIMESTAMP[¶](https://docs.python.org/3/library/py_compile.html#py_compile.PycInvalidationMode.TIMESTAMP "Link to this definition")

The `.pyc` file includes the timestamp and size of the source file, which Python will compare against the metadata of the source file at runtime to determine if the `.pyc` file needs to be regenerated.

CHECKED_HASH[¶](https://docs.python.org/3/library/py_compile.html#py_compile.PycInvalidationMode.CHECKED_HASH "Link to this definition")

The `.pyc` file includes a hash of the source file content, which Python will compare against the source at runtime to determine if the `.pyc` file needs to be regenerated.

UNCHECKED_HASH[¶](https://docs.python.org/3/library/py_compile.html#py_compile.PycInvalidationMode.UNCHECKED_HASH "Link to this definition")

Like [`CHECKED_HASH`](https://docs.python.org/3/library/py_compile.html#py_compile.PycInvalidationMode.CHECKED_HASH "py_compile.PycInvalidationMode.CHECKED_HASH"), the `.pyc` file includes a hash of the source file content. However, Python will at runtime assume the `.pyc` file is up to date and not validate the `.pyc` against the source file at all.
This option is useful when the `.pycs` are kept up to date by some system external to Python like a build system.
## Command-Line Interface[¶](https://docs.python.org/3/library/py_compile.html#command-line-interface "Link to this heading")
This module can be invoked as a script to compile several source files. The files named in _filenames_ are compiled and the resulting bytecode is cached in the normal manner. This program does not search a directory structure to locate source files; it only compiles files named explicitly. The exit status is nonzero if one of the files could not be compiled.

<file> ... <fileN>[¶](https://docs.python.org/3/library/py_compile.html#cmdoption-python-m-py_compile-arg-file "Link to this definition")


-[¶](https://docs.python.org/3/library/py_compile.html#cmdoption-python-m-py_compile "Link to this definition")

Positional arguments are files to compile. If `-` is the only parameter, the list of files is taken from standard input.

-q, --quiet[¶](https://docs.python.org/3/library/py_compile.html#cmdoption-python-m-py_compile-q "Link to this definition")

Suppress errors output.
Changed in version 3.2: Added support for `-`.
Changed in version 3.10: Added support for [`-q`](https://docs.python.org/3/library/py_compile.html#cmdoption-python-m-py_compile-q).
See also

Module [`compileall`](https://docs.python.org/3/library/compileall.html#module-compileall "compileall: Tools for byte-compiling all Python source files in a directory tree.")

Utilities to compile all Python source files in a directory tree.
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`py_compile` — Compile Python source files](https://docs.python.org/3/library/py_compile.html)
    * [Command-Line Interface](https://docs.python.org/3/library/py_compile.html#command-line-interface)


#### Previous topic
[`pyclbr` — Python module browser support](https://docs.python.org/3/library/pyclbr.html "previous chapter")
#### Next topic
[`compileall` — Byte-compile Python libraries](https://docs.python.org/3/library/compileall.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=py_compile+%E2%80%94+Compile+Python+source+files&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fpy_compile.html&pagesource=library%2Fpy_compile.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/compileall.html "compileall — Byte-compile Python libraries") |
  * [previous](https://docs.python.org/3/library/pyclbr.html "pyclbr — Python module browser support") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Python Language Services](https://docs.python.org/3/library/language.html) »
  * [`py_compile` — Compile Python source files](https://docs.python.org/3/library/py_compile.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
