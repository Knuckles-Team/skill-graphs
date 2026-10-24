[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
#### Previous topic
[`sysconfig` — Provide access to Python’s configuration information](https://docs.python.org/3/library/sysconfig.html "previous chapter")
#### Next topic
[`__main__` — Top-level code environment](https://docs.python.org/3/library/__main__.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=builtins+%E2%80%94+Built-in+objects&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fbuiltins.html&pagesource=library%2Fbuiltins.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/__main__.html "__main__ — Top-level code environment") |
  * [previous](https://docs.python.org/3/library/sysconfig.html "sysconfig — Provide access to Python’s configuration information") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Python Runtime Services](https://docs.python.org/3/library/python.html) »
  * [`builtins` — Built-in objects](https://docs.python.org/3/library/builtins.html)
  * |
  * Theme  Auto Light Dark |


#  `builtins` — Built-in objects[¶](https://docs.python.org/3/library/builtins.html#module-builtins "Link to this heading")
* * *
This module provides direct access to all ‘built-in’ identifiers of Python; for example, `builtins.open` is the full name for the built-in function [`open()`](https://docs.python.org/3/library/functions.html#open "open").
This module is not normally accessed explicitly by most applications, but can be useful in modules that provide objects with the same name as a built-in value, but in which the built-in of that name is also needed. For example, in a module that wants to implement an [`open()`](https://docs.python.org/3/library/functions.html#open "open") function that wraps the built-in `open()`, this module can be used directly:
Copy```
import builtins

def open(path):
    f = builtins.open(path, 'r')
    return UpperCaser(f)

class UpperCaser:
    '''Wrapper around a file that converts output to uppercase.'''

    def __init__(self, f):
        self._f = f

    def read(self, count=-1):
        return self._f.read(count).upper()

    # ...

```

As an implementation detail, most modules have the name `__builtins__` made available as part of their globals. The value of `__builtins__` is normally either this module or the value of this module’s [`__dict__`](https://docs.python.org/3/reference/datamodel.html#object.__dict__ "object.__dict__") attribute. Since this is an implementation detail, it may not be used by alternate implementations of Python.
See also
  * [Built-in Constants](https://docs.python.org/3/library/constants.html#built-in-consts)
  * [Built-in Exceptions](https://docs.python.org/3/library/exceptions.html#bltin-exceptions)
  * [Built-in Functions](https://docs.python.org/3/library/functions.html#built-in-funcs)
  * [Built-in Types](https://docs.python.org/3/library/stdtypes.html#bltin-types)


#### Previous topic
[`sysconfig` — Provide access to Python’s configuration information](https://docs.python.org/3/library/sysconfig.html "previous chapter")
#### Next topic
[`__main__` — Top-level code environment](https://docs.python.org/3/library/__main__.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=builtins+%E2%80%94+Built-in+objects&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fbuiltins.html&pagesource=library%2Fbuiltins.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/__main__.html "__main__ — Top-level code environment") |
  * [previous](https://docs.python.org/3/library/sysconfig.html "sysconfig — Provide access to Python’s configuration information") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Python Runtime Services](https://docs.python.org/3/library/python.html) »
  * [`builtins` — Built-in objects](https://docs.python.org/3/library/builtins.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
