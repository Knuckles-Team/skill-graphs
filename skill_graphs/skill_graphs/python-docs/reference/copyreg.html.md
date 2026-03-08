[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`copyreg` — Register `pickle` support functions](https://docs.python.org/3/library/copyreg.html)
    * [Example](https://docs.python.org/3/library/copyreg.html#example)


#### Previous topic
[`pickle` — Python object serialization](https://docs.python.org/3/library/pickle.html "previous chapter")
#### Next topic
[`shelve` — Python object persistence](https://docs.python.org/3/library/shelve.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=copyreg+%E2%80%94+Register+pickle+support+functions&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fcopyreg.html&pagesource=library%2Fcopyreg.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/shelve.html "shelve — Python object persistence") |
  * [previous](https://docs.python.org/3/library/pickle.html "pickle — Python object serialization") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Data Persistence](https://docs.python.org/3/library/persistence.html) »
  * [`copyreg` — Register `pickle` support functions](https://docs.python.org/3/library/copyreg.html)
  * |
  * Theme  Auto Light Dark |


#  `copyreg` — Register `pickle` support functions[¶](https://docs.python.org/3/library/copyreg.html#module-copyreg "Link to this heading")
**Source code:**
* * *
The `copyreg` module offers a way to define functions used while pickling specific objects. The [`pickle`](https://docs.python.org/3/library/pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.") and [`copy`](https://docs.python.org/3/library/copy.html#module-copy "copy: Shallow and deep copy operations.") modules use those functions when pickling/copying those objects. The module provides configuration information about object constructors which are not classes. Such constructors may be factory functions or class instances.

copyreg.constructor(_object_)[¶](https://docs.python.org/3/library/copyreg.html#copyreg.constructor "Link to this definition")

Declares _object_ to be a valid constructor. If _object_ is not callable (and hence not valid as a constructor), raises [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError").

copyreg.pickle(_type_ , _function_ , _constructor_ob =None_)[¶](https://docs.python.org/3/library/copyreg.html#copyreg.pickle "Link to this definition")

Declares that _function_ should be used as a “reduction” function for objects of type _type_. _function_ must return either a string or a tuple containing between two and six elements. See the [`dispatch_table`](https://docs.python.org/3/library/pickle.html#pickle.Pickler.dispatch_table "pickle.Pickler.dispatch_table") for more details on the interface of _function_.
The _constructor_ob_ parameter is a legacy feature and is now ignored, but if passed it must be a callable.
Note that the [`dispatch_table`](https://docs.python.org/3/library/pickle.html#pickle.Pickler.dispatch_table "pickle.Pickler.dispatch_table") attribute of a pickler object or subclass of [`pickle.Pickler`](https://docs.python.org/3/library/pickle.html#pickle.Pickler "pickle.Pickler") can also be used for declaring reduction functions.
## Example[¶](https://docs.python.org/3/library/copyreg.html#example "Link to this heading")
The example below would like to show how to register a pickle function and how it will be used:
Copy```
>>> import copyreg, copy, pickle
>>> class C:
...     def __init__(self, a):
...         self.a = a
...
>>> def pickle_c(c):
...     print("pickling a C instance...")
...     return C, (c.a,)
...
>>> copyreg.pickle(C, pickle_c)
>>> c = C(1)
>>> d = copy.copy(c)
pickling a C instance...
>>> p = pickle.dumps(c)
pickling a C instance...

```

### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`copyreg` — Register `pickle` support functions](https://docs.python.org/3/library/copyreg.html)
    * [Example](https://docs.python.org/3/library/copyreg.html#example)


#### Previous topic
[`pickle` — Python object serialization](https://docs.python.org/3/library/pickle.html "previous chapter")
#### Next topic
[`shelve` — Python object persistence](https://docs.python.org/3/library/shelve.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=copyreg+%E2%80%94+Register+pickle+support+functions&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fcopyreg.html&pagesource=library%2Fcopyreg.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/shelve.html "shelve — Python object persistence") |
  * [previous](https://docs.python.org/3/library/pickle.html "pickle — Python object serialization") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Data Persistence](https://docs.python.org/3/library/persistence.html) »
  * [`copyreg` — Register `pickle` support functions](https://docs.python.org/3/library/copyreg.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
