[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
#### Previous topic
[`shelve` — Python object persistence](https://docs.python.org/3/library/shelve.html "previous chapter")
#### Next topic
[`dbm` — Interfaces to Unix “databases”](https://docs.python.org/3/library/dbm.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=marshal+%E2%80%94+Internal+Python+object+serialization&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fmarshal.html&pagesource=library%2Fmarshal.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/dbm.html "dbm — Interfaces to Unix “databases”") |
  * [previous](https://docs.python.org/3/library/shelve.html "shelve — Python object persistence") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Data Persistence](https://docs.python.org/3/library/persistence.html) »
  * [`marshal` — Internal Python object serialization](https://docs.python.org/3/library/marshal.html)
  * |
  * Theme  Auto Light Dark |


#  `marshal` — Internal Python object serialization[¶](https://docs.python.org/3/library/marshal.html#module-marshal "Link to this heading")
* * *
This module contains functions that can read and write Python values in a binary format. The format is specific to Python, but independent of machine architecture issues (e.g., you can write a Python value to a file on a PC, transport the file to a Mac, and read it back there). Details of the format are undocumented on purpose; it may change between Python versions (although it rarely does). [[1]](https://docs.python.org/3/library/marshal.html#id2)
This is not a general “persistence” module. For general persistence and transfer of Python objects through RPC calls, see the modules [`pickle`](https://docs.python.org/3/library/pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.") and [`shelve`](https://docs.python.org/3/library/shelve.html#module-shelve "shelve: Python object persistence."). The `marshal` module exists mainly to support reading and writing the “pseudo-compiled” code for Python modules of `.pyc` files. Therefore, the Python maintainers reserve the right to modify the marshal format in backward incompatible ways should the need arise. The format of code objects is not compatible between Python versions, even if the version of the format is the same. De-serializing a code object in the incorrect Python version has undefined behavior. If you’re serializing and de-serializing Python objects, use the `pickle` module instead – the performance is comparable, version independence is guaranteed, and pickle supports a substantially wider range of objects than marshal.
Warning
The `marshal` module is not intended to be secure against erroneous or maliciously constructed data. Never unmarshal data received from an untrusted or unauthenticated source.
There are functions that read/write files as well as functions operating on bytes-like objects.
Not all Python object types are supported; in general, only objects whose value is independent from a particular invocation of Python can be written and read by this module. The following types are supported:
  * Numeric types: [`int`](https://docs.python.org/3/library/functions.html#int "int"), [`bool`](https://docs.python.org/3/library/functions.html#bool "bool"), [`float`](https://docs.python.org/3/library/functions.html#float "float"), [`complex`](https://docs.python.org/3/library/functions.html#complex "complex").
  * Strings ([`str`](https://docs.python.org/3/library/stdtypes.html#str "str")) and [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes"). [Bytes-like objects](https://docs.python.org/3/glossary.html#term-bytes-like-object) like [`bytearray`](https://docs.python.org/3/library/stdtypes.html#bytearray "bytearray") are marshalled as `bytes`.
  * Containers: [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "tuple"), [`list`](https://docs.python.org/3/library/stdtypes.html#list "list"), [`set`](https://docs.python.org/3/library/stdtypes.html#set "set"), [`frozenset`](https://docs.python.org/3/library/stdtypes.html#frozenset "frozenset"), and (since [`version`](https://docs.python.org/3/library/marshal.html#marshal.version "marshal.version") 5), [`slice`](https://docs.python.org/3/library/functions.html#slice "slice"). It should be understood that these are supported only if the values contained therein are themselves supported. Recursive containers are supported since `version` 3.
  * The singletons [`None`](https://docs.python.org/3/library/constants.html#None "None"), [`Ellipsis`](https://docs.python.org/3/library/constants.html#Ellipsis "Ellipsis") and [`StopIteration`](https://docs.python.org/3/library/exceptions.html#StopIteration "StopIteration").
  * [`code`](https://docs.python.org/3/library/code.html#module-code "code: Facilities to implement read-eval-print loops.") objects, if _allow_code_ is true. See note above about version dependence.


Changed in version 3.4:
  * Added format version 3, which supports marshalling recursive lists, sets and dictionaries.
  * Added format version 4, which supports efficient representations of short strings.


Changed in version 3.14: Added format version 5, which allows marshalling slices.
The module defines these functions:

marshal.dump(_value_ , _file_ , _version =version_, _/_ , _*_ , _allow_code =True_)[¶](https://docs.python.org/3/library/marshal.html#marshal.dump "Link to this definition")

Write the value on the open file. The value must be a supported type. The file must be a writeable [binary file](https://docs.python.org/3/glossary.html#term-binary-file).
If the value has (or contains an object that has) an unsupported type, a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") exception is raised — but garbage data will also be written to the file. The object will not be properly read back by [`load()`](https://docs.python.org/3/library/marshal.html#marshal.load "marshal.load"). [Code objects](https://docs.python.org/3/reference/datamodel.html#code-objects) are only supported if _allow_code_ is true.
The _version_ argument indicates the data format that `dump` should use (see below).
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `marshal.dumps` with arguments `value`, `version`.
Changed in version 3.13: Added the _allow_code_ parameter.

marshal.load(_file_ , _/_ , _*_ , _allow_code =True_)[¶](https://docs.python.org/3/library/marshal.html#marshal.load "Link to this definition")

Read one value from the open file and return it. If no valid value is read (e.g. because the data has a different Python version’s incompatible marshal format), raise [`EOFError`](https://docs.python.org/3/library/exceptions.html#EOFError "EOFError"), [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") or [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError"). [Code objects](https://docs.python.org/3/reference/datamodel.html#code-objects) are only supported if _allow_code_ is true. The file must be a readable [binary file](https://docs.python.org/3/glossary.html#term-binary-file).
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `marshal.load` with no arguments.
Note
If an object containing an unsupported type was marshalled with [`dump()`](https://docs.python.org/3/library/marshal.html#marshal.dump "marshal.dump"), `load()` will substitute `None` for the unmarshallable type.
Changed in version 3.10: This call used to raise a `code.__new__` audit event for each code object. Now it raises a single `marshal.load` event for the entire load operation.
Changed in version 3.13: Added the _allow_code_ parameter.

marshal.dumps(_value_ , _version =version_, _/_ , _*_ , _allow_code =True_)[¶](https://docs.python.org/3/library/marshal.html#marshal.dumps "Link to this definition")

Return the bytes object that would be written to a file by `dump(value, file)`. The value must be a supported type. Raise a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") exception if value has (or contains an object that has) an unsupported type. [Code objects](https://docs.python.org/3/reference/datamodel.html#code-objects) are only supported if _allow_code_ is true.
The _version_ argument indicates the data format that `dumps` should use (see below).
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `marshal.dumps` with arguments `value`, `version`.
Changed in version 3.13: Added the _allow_code_ parameter.

marshal.loads(_bytes_ , _/_ , _*_ , _allow_code =True_)[¶](https://docs.python.org/3/library/marshal.html#marshal.loads "Link to this definition")

Convert the [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object) to a value. If no valid value is found, raise [`EOFError`](https://docs.python.org/3/library/exceptions.html#EOFError "EOFError"), [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") or [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError"). [Code objects](https://docs.python.org/3/reference/datamodel.html#code-objects) are only supported if _allow_code_ is true. Extra bytes in the input are ignored.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `marshal.loads` with argument `bytes`.
Changed in version 3.10: This call used to raise a `code.__new__` audit event for each code object. Now it raises a single `marshal.loads` event for the entire load operation.
Changed in version 3.13: Added the _allow_code_ parameter.
In addition, the following constants are defined:

marshal.version[¶](https://docs.python.org/3/library/marshal.html#marshal.version "Link to this definition")

Indicates the format that the module uses. Version 0 is the historical first version; subsequent versions add new features. Generally, a new version becomes the default when it is introduced.
Version | Available since | New features
---|---|---
1 | Python 2.4 | Sharing interned strings
2 | Python 2.5 | Binary representation of floats
3 | Python 3.4 | Support for object instancing and recursion
4 | Python 3.4 | Efficient representation of short strings
5 | Python 3.14 | Support for [`slice`](https://docs.python.org/3/library/functions.html#slice "slice") objects
Footnotes
[[1](https://docs.python.org/3/library/marshal.html#id1)]
The name of this module stems from a bit of terminology used by the designers of Modula-3 (amongst others), who use the term “marshalling” for shipping of data around in a self-contained form. Strictly speaking, “to marshal” means to convert some data from internal to external form (in an RPC buffer for instance) and “unmarshalling” for the reverse process.
#### Previous topic
[`shelve` — Python object persistence](https://docs.python.org/3/library/shelve.html "previous chapter")
#### Next topic
[`dbm` — Interfaces to Unix “databases”](https://docs.python.org/3/library/dbm.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=marshal+%E2%80%94+Internal+Python+object+serialization&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fmarshal.html&pagesource=library%2Fmarshal.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/dbm.html "dbm — Interfaces to Unix “databases”") |
  * [previous](https://docs.python.org/3/library/shelve.html "shelve — Python object persistence") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Data Persistence](https://docs.python.org/3/library/persistence.html) »
  * [`marshal` — Internal Python object serialization](https://docs.python.org/3/library/marshal.html)
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
  *[*]: Keyword-only parameters separator (PEP 3102)
