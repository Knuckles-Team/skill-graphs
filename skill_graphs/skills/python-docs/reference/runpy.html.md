[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
#### Previous topic
[`modulefinder` — Find modules used by a script](https://docs.python.org/3/library/modulefinder.html "previous chapter")
#### Next topic
[`importlib` — The implementation of `import`](https://docs.python.org/3/library/importlib.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=runpy+%E2%80%94+Locating+and+executing+Python+modules&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Frunpy.html&pagesource=library%2Frunpy.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/importlib.html "importlib — The implementation of import") |
  * [previous](https://docs.python.org/3/library/modulefinder.html "modulefinder — Find modules used by a script") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Importing Modules](https://docs.python.org/3/library/modules.html) »
  * [`runpy` — Locating and executing Python modules](https://docs.python.org/3/library/runpy.html)
  * |
  * Theme  Auto Light Dark |


#  `runpy` — Locating and executing Python modules[¶](https://docs.python.org/3/library/runpy.html#module-runpy "Link to this heading")
**Source code:**
* * *
The `runpy` module is used to locate and run Python modules without importing them first. Its main use is to implement the [`-m`](https://docs.python.org/3/using/cmdline.html#cmdoption-m) command line switch that allows scripts to be located using the Python module namespace rather than the filesystem.
Note that this is _not_ a sandbox module - all code is executed in the current process, and any side effects (such as cached imports of other modules) will remain in place after the functions have returned.
Furthermore, any functions and classes defined by the executed code are not guaranteed to work correctly after a `runpy` function has returned. If that limitation is not acceptable for a given use case, [`importlib`](https://docs.python.org/3/library/importlib.html#module-importlib "importlib: The implementation of the import machinery.") is likely to be a more suitable choice than this module.
The `runpy` module provides two functions:

runpy.run_module(_mod_name_ , _init_globals =None_, _run_name =None_, _alter_sys =False_)[¶](https://docs.python.org/3/library/runpy.html#runpy.run_module "Link to this definition")

Execute the code of the specified module and return the resulting module’s globals dictionary. The module’s code is first located using the standard import mechanism (refer to [**PEP 302**](https://peps.python.org/pep-0302/) for details) and then executed in a fresh module namespace.
The _mod_name_ argument should be an absolute module name. If the module name refers to a package rather than a normal module, then that package is imported and the [`__main__`](https://docs.python.org/3/library/__main__.html#module-__main__ "__main__: The environment where top-level code is run. Covers command-line interfaces, import-time behavior, and ``__name__ == '__main__'``.") submodule within that package is then executed and the resulting module globals dictionary returned.
The optional dictionary argument _init_globals_ may be used to pre-populate the module’s globals dictionary before the code is executed. _init_globals_ will not be modified. If any of the special global variables below are defined in _init_globals_ , those definitions are overridden by `run_module()`.
The special global variables `__name__`, `__spec__`, `__file__`, `__cached__`, `__loader__` and `__package__` are set in the globals dictionary before the module code is executed. (Note that this is a minimal set of variables - other variables may be set implicitly as an interpreter implementation detail.)
`__name__` is set to _run_name_ if this optional argument is not [`None`](https://docs.python.org/3/library/constants.html#None "None"), to `mod_name + '.__main__'` if the named module is a package and to the _mod_name_ argument otherwise.
`__spec__` will be set appropriately for the _actually_ imported module (that is, `__spec__.name` will always be _mod_name_ or `mod_name + '.__main__'`, never _run_name_).
`__file__`, `__cached__`, `__loader__` and `__package__` are [set as normal](https://docs.python.org/3/reference/datamodel.html#import-mod-attrs) based on the module spec.
If the argument _alter_sys_ is supplied and evaluates to [`True`](https://docs.python.org/3/library/constants.html#True "True"), then `sys.argv[0]` is updated with the value of `__file__` and `sys.modules[__name__]` is updated with a temporary module object for the module being executed. Both `sys.argv[0]` and `sys.modules[__name__]` are restored to their original values before the function returns.
Note that this manipulation of [`sys`](https://docs.python.org/3/library/sys.html#module-sys "sys: Access system-specific parameters and functions.") is not thread-safe. Other threads may see the partially initialised module, as well as the altered list of arguments. It is recommended that the `sys` module be left alone when invoking this function from threaded code.
See also
The [`-m`](https://docs.python.org/3/using/cmdline.html#cmdoption-m) option offering equivalent functionality from the command line.
Changed in version 3.1: Added ability to execute packages by looking for a [`__main__`](https://docs.python.org/3/library/__main__.html#module-__main__ "__main__: The environment where top-level code is run. Covers command-line interfaces, import-time behavior, and ``__name__ == '__main__'``.") submodule.
Changed in version 3.2: Added `__cached__` global variable (see [**PEP 3147**](https://peps.python.org/pep-3147/)).
Changed in version 3.4: Updated to take advantage of the module spec feature added by [**PEP 451**](https://peps.python.org/pep-0451/). This allows `__cached__` to be set correctly for modules run this way, as well as ensuring the real module name is always accessible as `__spec__.name`.
Changed in version 3.12: The setting of `__cached__`, `__loader__`, and `__package__` are deprecated. See [`ModuleSpec`](https://docs.python.org/3/library/importlib.html#importlib.machinery.ModuleSpec "importlib.machinery.ModuleSpec") for alternatives.

runpy.run_path(_path_name_ , _init_globals =None_, _run_name =None_)[¶](https://docs.python.org/3/library/runpy.html#runpy.run_path "Link to this definition")

Execute the code at the named filesystem location and return the resulting module’s globals dictionary. As with a script name supplied to the CPython command line, _file_path_ may refer to a Python source file, a compiled bytecode file or a valid [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path") entry containing a [`__main__`](https://docs.python.org/3/library/__main__.html#module-__main__ "__main__: The environment where top-level code is run. Covers command-line interfaces, import-time behavior, and ``__name__ == '__main__'``.") module (e.g. a zipfile containing a top-level `__main__.py` file).
For a simple script, the specified code is simply executed in a fresh module namespace. For a valid [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path") entry (typically a zipfile or directory), the entry is first added to the beginning of `sys.path`. The function then looks for and executes a [`__main__`](https://docs.python.org/3/library/__main__.html#module-__main__ "__main__: The environment where top-level code is run. Covers command-line interfaces, import-time behavior, and ``__name__ == '__main__'``.") module using the updated path. Note that there is no special protection against invoking an existing `__main__` entry located elsewhere on `sys.path` if there is no such module at the specified location.
The optional dictionary argument _init_globals_ may be used to pre-populate the module’s globals dictionary before the code is executed. _init_globals_ will not be modified. If any of the special global variables below are defined in _init_globals_ , those definitions are overridden by `run_path()`.
The special global variables `__name__`, `__spec__`, `__file__`, `__cached__`, `__loader__` and `__package__` are set in the globals dictionary before the module code is executed. (Note that this is a minimal set of variables - other variables may be set implicitly as an interpreter implementation detail.)
`__name__` is set to _run_name_ if this optional argument is not [`None`](https://docs.python.org/3/library/constants.html#None "None") and to `'<run_path>'` otherwise.
If _file_path_ directly references a script file (whether as source or as precompiled byte code), then `__file__` will be set to _file_path_ , and `__spec__`, `__cached__`, `__loader__` and `__package__` will all be set to [`None`](https://docs.python.org/3/library/constants.html#None "None").
If _file_path_ is a reference to a valid [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path") entry, then `__spec__` will be set appropriately for the imported [`__main__`](https://docs.python.org/3/library/__main__.html#module-__main__ "__main__: The environment where top-level code is run. Covers command-line interfaces, import-time behavior, and ``__name__ == '__main__'``.") module (that is, `__spec__.name` will always be `__main__`). `__file__`, `__cached__`, `__loader__` and `__package__` will be [set as normal](https://docs.python.org/3/reference/datamodel.html#import-mod-attrs) based on the module spec.
A number of alterations are also made to the [`sys`](https://docs.python.org/3/library/sys.html#module-sys "sys: Access system-specific parameters and functions.") module. Firstly, [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path") may be altered as described above. `sys.argv[0]` is updated with the value of _file_path_ and `sys.modules[__name__]` is updated with a temporary module object for the module being executed. All modifications to items in `sys` are reverted before the function returns.
Note that, unlike [`run_module()`](https://docs.python.org/3/library/runpy.html#runpy.run_module "runpy.run_module"), the alterations made to [`sys`](https://docs.python.org/3/library/sys.html#module-sys "sys: Access system-specific parameters and functions.") are not optional in this function as these adjustments are essential to allowing the execution of [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path") entries. As the thread-safety limitations still apply, use of this function in threaded code should be either serialised with the import lock or delegated to a separate process.
See also
[Interface options](https://docs.python.org/3/using/cmdline.html#using-on-interface-options) for equivalent functionality on the command line (`python path/to/script`).
Added in version 3.2.
Changed in version 3.4: Updated to take advantage of the module spec feature added by [**PEP 451**](https://peps.python.org/pep-0451/). This allows `__cached__` to be set correctly in the case where `__main__` is imported from a valid [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path") entry rather than being executed directly.
Changed in version 3.12: The setting of `__cached__`, `__loader__`, and `__package__` are deprecated.
See also

[**PEP 338**](https://peps.python.org/pep-0338/) – Executing modules as scripts

PEP written and implemented by Nick Coghlan.

[**PEP 366**](https://peps.python.org/pep-0366/) – Main module explicit relative imports

PEP written and implemented by Nick Coghlan.

[**PEP 451**](https://peps.python.org/pep-0451/) – A ModuleSpec Type for the Import System

PEP written and implemented by Eric Snow
[Command line and environment](https://docs.python.org/3/using/cmdline.html#using-on-general) - CPython command line details
The [`importlib.import_module()`](https://docs.python.org/3/library/importlib.html#importlib.import_module "importlib.import_module") function
#### Previous topic
[`modulefinder` — Find modules used by a script](https://docs.python.org/3/library/modulefinder.html "previous chapter")
#### Next topic
[`importlib` — The implementation of `import`](https://docs.python.org/3/library/importlib.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=runpy+%E2%80%94+Locating+and+executing+Python+modules&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Frunpy.html&pagesource=library%2Frunpy.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/importlib.html "importlib — The implementation of import") |
  * [previous](https://docs.python.org/3/library/modulefinder.html "modulefinder — Find modules used by a script") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Importing Modules](https://docs.python.org/3/library/modules.html) »
  * [`runpy` — Locating and executing Python modules](https://docs.python.org/3/library/runpy.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
