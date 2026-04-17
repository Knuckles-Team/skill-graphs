[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`modulefinder` — Find modules used by a script](https://docs.python.org/3/library/modulefinder.html)
    * [Example usage of `ModuleFinder`](https://docs.python.org/3/library/modulefinder.html#example-usage-of-modulefinder)


#### Previous topic
[`pkgutil` — Package extension utility](https://docs.python.org/3/library/pkgutil.html "previous chapter")
#### Next topic
[`runpy` — Locating and executing Python modules](https://docs.python.org/3/library/runpy.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=modulefinder+%E2%80%94+Find+modules+used+by+a+script&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fmodulefinder.html&pagesource=library%2Fmodulefinder.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/runpy.html "runpy — Locating and executing Python modules") |
  * [previous](https://docs.python.org/3/library/pkgutil.html "pkgutil — Package extension utility") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Importing Modules](https://docs.python.org/3/library/modules.html) »
  * [`modulefinder` — Find modules used by a script](https://docs.python.org/3/library/modulefinder.html)
  * |
  * Theme  Auto Light Dark |


#  `modulefinder` — Find modules used by a script[¶](https://docs.python.org/3/library/modulefinder.html#module-modulefinder "Link to this heading")
**Source code:**
* * *
This module provides a [`ModuleFinder`](https://docs.python.org/3/library/modulefinder.html#modulefinder.ModuleFinder "modulefinder.ModuleFinder") class that can be used to determine the set of modules imported by a script. `modulefinder.py` can also be run as a script, giving the filename of a Python script as its argument, after which a report of the imported modules will be printed.

modulefinder.AddPackagePath(_pkg_name_ , _path_)[¶](https://docs.python.org/3/library/modulefinder.html#modulefinder.AddPackagePath "Link to this definition")

Record that the package named _pkg_name_ can be found in the specified _path_.

modulefinder.ReplacePackage(_oldname_ , _newname_)[¶](https://docs.python.org/3/library/modulefinder.html#modulefinder.ReplacePackage "Link to this definition")

Allows specifying that the module named _oldname_ is in fact the package named _newname_.

_class_ modulefinder.ModuleFinder(_path =None_, _debug =0_, _excludes =[]_, _replace_paths =[]_)[¶](https://docs.python.org/3/library/modulefinder.html#modulefinder.ModuleFinder "Link to this definition")

This class provides [`run_script()`](https://docs.python.org/3/library/modulefinder.html#modulefinder.ModuleFinder.run_script "modulefinder.ModuleFinder.run_script") and [`report()`](https://docs.python.org/3/library/modulefinder.html#modulefinder.ModuleFinder.report "modulefinder.ModuleFinder.report") methods to determine the set of modules imported by a script. _path_ can be a list of directories to search for modules; if not specified, `sys.path` is used. _debug_ sets the debugging level; higher values make the class print debugging messages about what it’s doing. _excludes_ is a list of module names to exclude from the analysis. _replace_paths_ is a list of `(oldpath, newpath)` tuples that will be replaced in module paths.

report()[¶](https://docs.python.org/3/library/modulefinder.html#modulefinder.ModuleFinder.report "Link to this definition")

Print a report to standard output that lists the modules imported by the script and their paths, as well as modules that are missing or seem to be missing.

run_script(_pathname_)[¶](https://docs.python.org/3/library/modulefinder.html#modulefinder.ModuleFinder.run_script "Link to this definition")

Analyze the contents of the _pathname_ file, which must contain Python code.

modules[¶](https://docs.python.org/3/library/modulefinder.html#modulefinder.ModuleFinder.modules "Link to this definition")

A dictionary mapping module names to modules. See [Example usage of ModuleFinder](https://docs.python.org/3/library/modulefinder.html#modulefinder-example).
## Example usage of [`ModuleFinder`](https://docs.python.org/3/library/modulefinder.html#modulefinder.ModuleFinder "modulefinder.ModuleFinder")[¶](https://docs.python.org/3/library/modulefinder.html#example-usage-of-modulefinder "Link to this heading")
The script that is going to get analyzed later on (bacon.py):
Copy```
import re, itertools

try:
    import baconhameggs
except ImportError:
    pass

try:
    import guido.python.ham
except ImportError:
    pass

```

The script that will output the report of bacon.py:
Copy```
from modulefinder import ModuleFinder

finder = ModuleFinder()
finder.run_script('bacon.py')

print('Loaded modules:')
for name, mod in finder.modules.items():
    print('%s: ' % name, end='')
    print(','.join(list(mod.globalnames.keys())[:3]))

print('-'*50)
print('Modules not imported:')
print('\n'.join(finder.badmodules.keys()))

```

Sample output (may vary depending on the architecture):
Copy```
Loaded modules:
_types:
copyreg:  _inverted_registry,_slotnames,__all__
re._compiler:  isstring,_sre,_optimize_unicode
_sre:
re._constants:  REPEAT_ONE,makedict,AT_END_LINE
sys:
re:  __module__,finditer,_expand
itertools:
__main__:  re,itertools,baconhameggs
re._parser:  _PATTERNENDERS,SRE_FLAG_UNICODE
array:
types:  __module__,IntType,TypeType
---------------------------------------------------
Modules not imported:
guido.python.ham
baconhameggs

```

### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`modulefinder` — Find modules used by a script](https://docs.python.org/3/library/modulefinder.html)
    * [Example usage of `ModuleFinder`](https://docs.python.org/3/library/modulefinder.html#example-usage-of-modulefinder)


#### Previous topic
[`pkgutil` — Package extension utility](https://docs.python.org/3/library/pkgutil.html "previous chapter")
#### Next topic
[`runpy` — Locating and executing Python modules](https://docs.python.org/3/library/runpy.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=modulefinder+%E2%80%94+Find+modules+used+by+a+script&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fmodulefinder.html&pagesource=library%2Fmodulefinder.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/runpy.html "runpy — Locating and executing Python modules") |
  * [previous](https://docs.python.org/3/library/pkgutil.html "pkgutil — Package extension utility") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Importing Modules](https://docs.python.org/3/library/modules.html) »
  * [`modulefinder` — Find modules used by a script](https://docs.python.org/3/library/modulefinder.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
