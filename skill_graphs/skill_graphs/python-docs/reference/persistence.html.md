[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
#### Previous topic
[`shutil` — High-level file operations](https://docs.python.org/3/library/shutil.html "previous chapter")
#### Next topic
[`pickle` — Python object serialization](https://docs.python.org/3/library/pickle.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Data+Persistence&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fpersistence.html&pagesource=library%2Fpersistence.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/pickle.html "pickle — Python object serialization") |
  * [previous](https://docs.python.org/3/library/shutil.html "shutil — High-level file operations") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Data Persistence](https://docs.python.org/3/library/persistence.html)
  * |
  * Theme  Auto Light Dark |


# Data Persistence[¶](https://docs.python.org/3/library/persistence.html#data-persistence "Link to this heading")
The modules described in this chapter support storing Python data in a persistent form on disk. The [`pickle`](https://docs.python.org/3/library/pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.") and [`marshal`](https://docs.python.org/3/library/marshal.html#module-marshal "marshal: Convert Python objects to streams of bytes and back \(with different constraints\).") modules can turn many Python data types into a stream of bytes and then recreate the objects from the bytes. The various DBM-related modules support a family of hash-based file formats that store a mapping of strings to other strings.
The list of modules described in this chapter is:
  * [`pickle` — Python object serialization](https://docs.python.org/3/library/pickle.html)
    * [Relationship to other Python modules](https://docs.python.org/3/library/pickle.html#relationship-to-other-python-modules)
      * [Comparison with `marshal`](https://docs.python.org/3/library/pickle.html#comparison-with-marshal)
      * [Comparison with `json`](https://docs.python.org/3/library/pickle.html#comparison-with-json)
    * [Data stream format](https://docs.python.org/3/library/pickle.html#data-stream-format)
    * [Module Interface](https://docs.python.org/3/library/pickle.html#module-interface)
    * [What can be pickled and unpickled?](https://docs.python.org/3/library/pickle.html#what-can-be-pickled-and-unpickled)
    * [Pickling Class Instances](https://docs.python.org/3/library/pickle.html#pickling-class-instances)
      * [Persistence of External Objects](https://docs.python.org/3/library/pickle.html#persistence-of-external-objects)
      * [Dispatch Tables](https://docs.python.org/3/library/pickle.html#dispatch-tables)
      * [Handling Stateful Objects](https://docs.python.org/3/library/pickle.html#handling-stateful-objects)
    * [Custom Reduction for Types, Functions, and Other Objects](https://docs.python.org/3/library/pickle.html#custom-reduction-for-types-functions-and-other-objects)
    * [Out-of-band Buffers](https://docs.python.org/3/library/pickle.html#out-of-band-buffers)
      * [Provider API](https://docs.python.org/3/library/pickle.html#provider-api)
      * [Consumer API](https://docs.python.org/3/library/pickle.html#consumer-api)
      * [Example](https://docs.python.org/3/library/pickle.html#example)
    * [Restricting Globals](https://docs.python.org/3/library/pickle.html#restricting-globals)
    * [Performance](https://docs.python.org/3/library/pickle.html#performance)
    * [Examples](https://docs.python.org/3/library/pickle.html#examples)
    * [Command-line interface](https://docs.python.org/3/library/pickle.html#command-line-interface)
  * [`copyreg` — Register `pickle` support functions](https://docs.python.org/3/library/copyreg.html)
    * [Example](https://docs.python.org/3/library/copyreg.html#example)
  * [`shelve` — Python object persistence](https://docs.python.org/3/library/shelve.html)
    * [Restrictions](https://docs.python.org/3/library/shelve.html#restrictions)
    * [Example](https://docs.python.org/3/library/shelve.html#example)
  * [`marshal` — Internal Python object serialization](https://docs.python.org/3/library/marshal.html)
  * [`dbm` — Interfaces to Unix “databases”](https://docs.python.org/3/library/dbm.html)
    * [`dbm.sqlite3` — SQLite backend for dbm](https://docs.python.org/3/library/dbm.html#module-dbm.sqlite3)
    * [`dbm.gnu` — GNU database manager](https://docs.python.org/3/library/dbm.html#module-dbm.gnu)
    * [`dbm.ndbm` — New Database Manager](https://docs.python.org/3/library/dbm.html#module-dbm.ndbm)
    * [`dbm.dumb` — Portable DBM implementation](https://docs.python.org/3/library/dbm.html#module-dbm.dumb)
  * [`sqlite3` — DB-API 2.0 interface for SQLite databases](https://docs.python.org/3/library/sqlite3.html)
    * [Tutorial](https://docs.python.org/3/library/sqlite3.html#tutorial)
    * [Reference](https://docs.python.org/3/library/sqlite3.html#reference)
      * [Module functions](https://docs.python.org/3/library/sqlite3.html#module-functions)
      * [Module constants](https://docs.python.org/3/library/sqlite3.html#module-constants)
      * [Connection objects](https://docs.python.org/3/library/sqlite3.html#connection-objects)
      * [Cursor objects](https://docs.python.org/3/library/sqlite3.html#cursor-objects)
      * [Row objects](https://docs.python.org/3/library/sqlite3.html#row-objects)
      * [Blob objects](https://docs.python.org/3/library/sqlite3.html#blob-objects)
      * [PrepareProtocol objects](https://docs.python.org/3/library/sqlite3.html#prepareprotocol-objects)
      * [Exceptions](https://docs.python.org/3/library/sqlite3.html#exceptions)
      * [SQLite and Python types](https://docs.python.org/3/library/sqlite3.html#sqlite-and-python-types)
      * [Default adapters and converters (deprecated)](https://docs.python.org/3/library/sqlite3.html#default-adapters-and-converters-deprecated)
      * [Command-line interface](https://docs.python.org/3/library/sqlite3.html#command-line-interface)
    * [How-to guides](https://docs.python.org/3/library/sqlite3.html#how-to-guides)
      * [How to use placeholders to bind values in SQL queries](https://docs.python.org/3/library/sqlite3.html#how-to-use-placeholders-to-bind-values-in-sql-queries)
      * [How to adapt custom Python types to SQLite values](https://docs.python.org/3/library/sqlite3.html#how-to-adapt-custom-python-types-to-sqlite-values)
        * [How to write adaptable objects](https://docs.python.org/3/library/sqlite3.html#how-to-write-adaptable-objects)
        * [How to register adapter callables](https://docs.python.org/3/library/sqlite3.html#how-to-register-adapter-callables)
      * [How to convert SQLite values to custom Python types](https://docs.python.org/3/library/sqlite3.html#how-to-convert-sqlite-values-to-custom-python-types)
      * [Adapter and converter recipes](https://docs.python.org/3/library/sqlite3.html#adapter-and-converter-recipes)
      * [How to use connection shortcut methods](https://docs.python.org/3/library/sqlite3.html#how-to-use-connection-shortcut-methods)
      * [How to use the connection context manager](https://docs.python.org/3/library/sqlite3.html#how-to-use-the-connection-context-manager)
      * [How to work with SQLite URIs](https://docs.python.org/3/library/sqlite3.html#how-to-work-with-sqlite-uris)
      * [How to create and use row factories](https://docs.python.org/3/library/sqlite3.html#how-to-create-and-use-row-factories)
      * [How to handle non-UTF-8 text encodings](https://docs.python.org/3/library/sqlite3.html#how-to-handle-non-utf-8-text-encodings)
    * [Explanation](https://docs.python.org/3/library/sqlite3.html#explanation)
      * [Transaction control](https://docs.python.org/3/library/sqlite3.html#transaction-control)
        * [Transaction control via the `autocommit` attribute](https://docs.python.org/3/library/sqlite3.html#transaction-control-via-the-autocommit-attribute)
        * [Transaction control via the `isolation_level` attribute](https://docs.python.org/3/library/sqlite3.html#transaction-control-via-the-isolation-level-attribute)


#### Previous topic
[`shutil` — High-level file operations](https://docs.python.org/3/library/shutil.html "previous chapter")
#### Next topic
[`pickle` — Python object serialization](https://docs.python.org/3/library/pickle.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Data+Persistence&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fpersistence.html&pagesource=library%2Fpersistence.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/pickle.html "pickle — Python object serialization") |
  * [previous](https://docs.python.org/3/library/shutil.html "shutil — High-level file operations") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Data Persistence](https://docs.python.org/3/library/persistence.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
