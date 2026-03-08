[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`dbm` — Interfaces to Unix “databases”](https://docs.python.org/3/library/dbm.html)
    * [`dbm.sqlite3` — SQLite backend for dbm](https://docs.python.org/3/library/dbm.html#module-dbm.sqlite3)
    * [`dbm.gnu` — GNU database manager](https://docs.python.org/3/library/dbm.html#module-dbm.gnu)
    * [`dbm.ndbm` — New Database Manager](https://docs.python.org/3/library/dbm.html#module-dbm.ndbm)
    * [`dbm.dumb` — Portable DBM implementation](https://docs.python.org/3/library/dbm.html#module-dbm.dumb)


#### Previous topic
[`marshal` — Internal Python object serialization](https://docs.python.org/3/library/marshal.html "previous chapter")
#### Next topic
[`sqlite3` — DB-API 2.0 interface for SQLite databases](https://docs.python.org/3/library/sqlite3.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=dbm+%E2%80%94+Interfaces+to+Unix+%E2%80%9Cdatabases%E2%80%9D&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fdbm.html&pagesource=library%2Fdbm.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/sqlite3.html "sqlite3 — DB-API 2.0 interface for SQLite databases") |
  * [previous](https://docs.python.org/3/library/marshal.html "marshal — Internal Python object serialization") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Data Persistence](https://docs.python.org/3/library/persistence.html) »
  * [`dbm` — Interfaces to Unix “databases”](https://docs.python.org/3/library/dbm.html)
  * |
  * Theme  Auto Light Dark |


#  `dbm` — Interfaces to Unix “databases”[¶](https://docs.python.org/3/library/dbm.html#module-dbm "Link to this heading")
**Source code:**
* * *
`dbm` is a generic interface to variants of the DBM database:
  * [`dbm.sqlite3`](https://docs.python.org/3/library/dbm.html#module-dbm.sqlite3 "dbm.sqlite3: SQLite backend for dbm")
  * [`dbm.gnu`](https://docs.python.org/3/library/dbm.html#module-dbm.gnu "dbm.gnu: GNU database manager")
  * [`dbm.ndbm`](https://docs.python.org/3/library/dbm.html#module-dbm.ndbm "dbm.ndbm: The New Database Manager")


If none of these modules are installed, the slow-but-simple implementation in module [`dbm.dumb`](https://docs.python.org/3/library/dbm.html#module-dbm.dumb "dbm.dumb: Portable implementation of the simple DBM interface.") will be used. There is a

_exception_ dbm.error[¶](https://docs.python.org/3/library/dbm.html#dbm.error "Link to this definition")

A tuple containing the exceptions that can be raised by each of the supported modules, with a unique exception also named [`dbm.error`](https://docs.python.org/3/library/dbm.html#dbm.error "dbm.error") as the first item — the latter is used when `dbm.error` is raised.

dbm.whichdb(_filename_)[¶](https://docs.python.org/3/library/dbm.html#dbm.whichdb "Link to this definition")

This function attempts to guess which of the several simple database modules available — [`dbm.sqlite3`](https://docs.python.org/3/library/dbm.html#module-dbm.sqlite3 "dbm.sqlite3: SQLite backend for dbm"), [`dbm.gnu`](https://docs.python.org/3/library/dbm.html#module-dbm.gnu "dbm.gnu: GNU database manager"), [`dbm.ndbm`](https://docs.python.org/3/library/dbm.html#module-dbm.ndbm "dbm.ndbm: The New Database Manager"), or [`dbm.dumb`](https://docs.python.org/3/library/dbm.html#module-dbm.dumb "dbm.dumb: Portable implementation of the simple DBM interface.") — should be used to open a given file.
Return one of the following values:
  * `None` if the file can’t be opened because it’s unreadable or doesn’t exist
  * the empty string (`''`) if the file’s format can’t be guessed
  * a string containing the required module name, such as `'dbm.ndbm'` or `'dbm.gnu'`


Changed in version 3.11: _filename_ accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).

dbm.open(_file_ , _flag ='r'_, _mode =0o666_)[¶](https://docs.python.org/3/library/dbm.html#dbm.open "Link to this definition")

Open a database and return the corresponding database object.

Parameters:

  * **file** ([path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)) –
The database file to open.
If the database file already exists, the [`whichdb()`](https://docs.python.org/3/library/dbm.html#dbm.whichdb "dbm.whichdb") function is used to determine its type and the appropriate module is used; if it does not exist, the first submodule listed above that can be imported is used.
  * **flag** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "str")) –
    * `'r'` (default): Open existing database for reading only.
    * `'w'`: Open existing database for reading and writing.
    * `'c'`: Open database for reading and writing, creating it if it doesn’t exist.
    * `'n'`: Always create a new, empty database, open for reading and writing.
  * **mode** ([_int_](https://docs.python.org/3/library/functions.html#int "int")) – The Unix file access mode of the file (default: octal `0o666`), used only when the database has to be created.


Changed in version 3.11: _file_ accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).
The object returned by [`open()`](https://docs.python.org/3/library/dbm.html#dbm.open "dbm.open") supports the basic functionality of mutable [mappings](https://docs.python.org/3/glossary.html#term-mapping); keys and their corresponding values can be stored, retrieved, and deleted, and iteration, the [`in`](https://docs.python.org/3/reference/expressions.html#in) operator and methods `keys()`, `get()`, `setdefault()` and `clear()` are available. The `keys()` method returns a list instead of a view object. The `setdefault()` method requires two arguments.
Key and values are always stored as [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes"). This means that when strings are used they are implicitly converted to the default encoding before being stored.
These objects also support being used in a [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) statement, which will automatically close them when done.
Changed in version 3.2: `get()` and `setdefault()` methods are now available for all `dbm` backends.
Changed in version 3.4: Added native support for the context management protocol to the objects returned by [`open()`](https://docs.python.org/3/library/dbm.html#dbm.open "dbm.open").
Changed in version 3.8: Deleting a key from a read-only database raises a database module specific exception instead of [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError "KeyError").
Changed in version 3.13: `clear()` methods are now available for all `dbm` backends.
The following example records some hostnames and a corresponding title, and then prints out the contents of the database:
Copy```
import dbm

# Open database, creating it if necessary.
with dbm.open('cache', 'c') as db:

    # Record some values
    db[b'hello'] = b'there'
    db['www.python.org'] = 'Python Website'
    db['www.cnn.com'] = 'Cable News Network'

    # Note that the keys are considered bytes now.
    assert db[b'www.python.org'] == b'Python Website'
    # Notice how the value is now in bytes.
    assert db['www.cnn.com'] == b'Cable News Network'

    # Often-used methods of the dict interface work too.
    print(db.get('python.org', b'not present'))

    # Storing a non-string key or value will raise an exception (most
    # likely a TypeError).
    db['www.yahoo.com'] = 4

# db is automatically closed when leaving the with statement.

```

See also

Module [`shelve`](https://docs.python.org/3/library/shelve.html#module-shelve "shelve: Python object persistence.")

Persistence module which stores non-string data.
The individual submodules are described in the following sections.
##  `dbm.sqlite3` — SQLite backend for dbm[¶](https://docs.python.org/3/library/dbm.html#module-dbm.sqlite3 "Link to this heading")
Added in version 3.13.
**Source code:**
* * *
This module uses the standard library [`sqlite3`](https://docs.python.org/3/library/sqlite3.html#module-sqlite3 "sqlite3: A DB-API 2.0 implementation using SQLite 3.x.") module to provide an SQLite backend for the `dbm` module. The files created by `dbm.sqlite3` can thus be opened by `sqlite3`, or any other SQLite browser, including the SQLite CLI.
[Availability](https://docs.python.org/3/library/intro.html#availability): not WASI.
This module does not work or is not available on WebAssembly. See [WebAssembly platforms](https://docs.python.org/3/library/intro.html#wasm-availability) for more information.

dbm.sqlite3.open(_filename_ , _/_ , _flag ='r'_, _mode =0o666_)[¶](https://docs.python.org/3/library/dbm.html#dbm.sqlite3.open "Link to this definition")

Open an SQLite database.

Parameters:

  * **filename** ([path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)) – The path to the database to be opened.
  * **flag** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "str")) –
    * `'r'` (default): Open existing database for reading only.
    * `'w'`: Open existing database for reading and writing.
    * `'c'`: Open database for reading and writing, creating it if it doesn’t exist.
    * `'n'`: Always create a new, empty database, open for reading and writing.
  * **mode** – The Unix file access mode of the file (default: octal `0o666`), used only when the database has to be created.


The returned database object behaves similar to a mutable [mapping](https://docs.python.org/3/glossary.html#term-mapping), but the `keys()` method returns a list, and the `setdefault()` method requires two arguments. It also supports a “closing” context manager via the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) keyword.
The following method is also provided:

sqlite3.close()[¶](https://docs.python.org/3/library/dbm.html#dbm.sqlite3.sqlite3.close "Link to this definition")

Close the SQLite database.
##  `dbm.gnu` — GNU database manager[¶](https://docs.python.org/3/library/dbm.html#module-dbm.gnu "Link to this heading")
**Source code:**
* * *
The `dbm.gnu` module provides an interface to the GDBM library, similar to the [`dbm.ndbm`](https://docs.python.org/3/library/dbm.html#module-dbm.ndbm "dbm.ndbm: The New Database Manager") module, but with additional functionality like crash tolerance.
Note
The file formats created by `dbm.gnu` and [`dbm.ndbm`](https://docs.python.org/3/library/dbm.html#module-dbm.ndbm "dbm.ndbm: The New Database Manager") are incompatible and can not be used interchangeably.
[Availability](https://docs.python.org/3/library/intro.html#availability): not Android, not iOS, not WASI.
This module is not supported on [mobile platforms](https://docs.python.org/3/library/intro.html#mobile-availability) or [WebAssembly platforms](https://docs.python.org/3/library/intro.html#wasm-availability).
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.

_exception_ dbm.gnu.error[¶](https://docs.python.org/3/library/dbm.html#dbm.gnu.error "Link to this definition")

Raised on `dbm.gnu`-specific errors, such as I/O errors. [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError "KeyError") is raised for general mapping errors like specifying an incorrect key.

dbm.gnu.open_flags[¶](https://docs.python.org/3/library/dbm.html#dbm.gnu.open_flags "Link to this definition")

A string of characters the _flag_ parameter of [`open()`](https://docs.python.org/3/library/dbm.html#dbm.gnu.open "dbm.gnu.open") supports.

dbm.gnu.open(_filename_ , _flag ='r'_, _mode =0o666_, _/_)[¶](https://docs.python.org/3/library/dbm.html#dbm.gnu.open "Link to this definition")

Open a GDBM database and return a `gdbm` object.

Parameters:

  * **filename** ([path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)) – The database file to open.
  * **flag** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "str")) –
    * `'r'` (default): Open existing database for reading only.
    * `'w'`: Open existing database for reading and writing.
    * `'c'`: Open database for reading and writing, creating it if it doesn’t exist.
    * `'n'`: Always create a new, empty database, open for reading and writing.
The following additional characters may be appended to control how the database is opened:
    * `'f'`: Open the database in fast mode. Writes to the database will not be synchronized.
    * `'s'`: Synchronized mode. Changes to the database will be written immediately to the file.
    * `'u'`: Do not lock database.
Not all flags are valid for all versions of GDBM. See the [`open_flags`](https://docs.python.org/3/library/dbm.html#dbm.gnu.open_flags "dbm.gnu.open_flags") member for a list of supported flag characters.
  * **mode** ([_int_](https://docs.python.org/3/library/functions.html#int "int")) – The Unix file access mode of the file (default: octal `0o666`), used only when the database has to be created.



Raises:

[**error**](https://docs.python.org/3/library/dbm.html#dbm.gnu.error "dbm.gnu.error") – If an invalid _flag_ argument is passed.
Changed in version 3.11: _filename_ accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).
`gdbm` objects behave similar to mutable [mappings](https://docs.python.org/3/glossary.html#term-mapping), but methods `items()`, `values()`, `pop()`, `popitem()`, and `update()` are not supported, the `keys()` method returns a list, and the `setdefault()` method requires two arguments. It also supports a “closing” context manager via the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) keyword.
Changed in version 3.2: Added the `get()` and `setdefault()` methods.
Changed in version 3.13: Added the `clear()` method.
The following methods are also provided:

gdbm.close()[¶](https://docs.python.org/3/library/dbm.html#dbm.gnu.gdbm.close "Link to this definition")

Close the GDBM database.

gdbm.firstkey()[¶](https://docs.python.org/3/library/dbm.html#dbm.gnu.gdbm.firstkey "Link to this definition")

It’s possible to loop over every key in the database using this method and the [`nextkey()`](https://docs.python.org/3/library/dbm.html#dbm.gnu.gdbm.nextkey "dbm.gnu.gdbm.nextkey") method. The traversal is ordered by GDBM’s internal hash values, and won’t be sorted by the key values. This method returns the starting key.

gdbm.nextkey(_key_)[¶](https://docs.python.org/3/library/dbm.html#dbm.gnu.gdbm.nextkey "Link to this definition")

Returns the key that follows _key_ in the traversal. The following code prints every key in the database `db`, without having to create a list in memory that contains them all:
Copy```
k = db.firstkey()
while k is not None:
    print(k)
    k = db.nextkey(k)

```


gdbm.reorganize()[¶](https://docs.python.org/3/library/dbm.html#dbm.gnu.gdbm.reorganize "Link to this definition")

If you have carried out a lot of deletions and would like to shrink the space used by the GDBM file, this routine will reorganize the database. `gdbm` objects will not shorten the length of a database file except by using this reorganization; otherwise, deleted file space will be kept and reused as new (key, value) pairs are added.

gdbm.sync()[¶](https://docs.python.org/3/library/dbm.html#dbm.gnu.gdbm.sync "Link to this definition")

When the database has been opened in fast mode, this method forces any unwritten data to be written to the disk.
##  `dbm.ndbm` — New Database Manager[¶](https://docs.python.org/3/library/dbm.html#module-dbm.ndbm "Link to this heading")
**Source code:**
* * *
The `dbm.ndbm` module provides an interface to the NDBM library. This module can be used with the “classic” NDBM interface or the GDBM compatibility interface.
Note
The file formats created by [`dbm.gnu`](https://docs.python.org/3/library/dbm.html#module-dbm.gnu "dbm.gnu: GNU database manager") and `dbm.ndbm` are incompatible and can not be used interchangeably.
Warning
The NDBM library shipped as part of macOS has an undocumented limitation on the size of values, which can result in corrupted database files when storing values larger than this limit. Reading such corrupted files can result in a hard crash (segmentation fault).
[Availability](https://docs.python.org/3/library/intro.html#availability): not Android, not iOS, not WASI.
This module is not supported on [mobile platforms](https://docs.python.org/3/library/intro.html#mobile-availability) or [WebAssembly platforms](https://docs.python.org/3/library/intro.html#wasm-availability).
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.

_exception_ dbm.ndbm.error[¶](https://docs.python.org/3/library/dbm.html#dbm.ndbm.error "Link to this definition")

Raised on `dbm.ndbm`-specific errors, such as I/O errors. [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError "KeyError") is raised for general mapping errors like specifying an incorrect key.

dbm.ndbm.library[¶](https://docs.python.org/3/library/dbm.html#dbm.ndbm.library "Link to this definition")

Name of the NDBM implementation library used.

dbm.ndbm.open(_filename_ , _flag ='r'_, _mode =0o666_, _/_)[¶](https://docs.python.org/3/library/dbm.html#dbm.ndbm.open "Link to this definition")

Open an NDBM database and return an `ndbm` object.

Parameters:

  * **filename** ([path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)) – The basename of the database file (without the `.dir` or `.pag` extensions).
  * **flag** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "str")) –
    * `'r'` (default): Open existing database for reading only.
    * `'w'`: Open existing database for reading and writing.
    * `'c'`: Open database for reading and writing, creating it if it doesn’t exist.
    * `'n'`: Always create a new, empty database, open for reading and writing.
  * **mode** ([_int_](https://docs.python.org/3/library/functions.html#int "int")) – The Unix file access mode of the file (default: octal `0o666`), used only when the database has to be created.


Changed in version 3.11: Accepts [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object) for filename.
`ndbm` objects behave similar to mutable [mappings](https://docs.python.org/3/glossary.html#term-mapping), but methods `items()`, `values()`, `pop()`, `popitem()`, and `update()` are not supported, the `keys()` method returns a list, and the `setdefault()` method requires two arguments. It also supports a “closing” context manager via the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) keyword.
Changed in version 3.2: Added the `get()` and `setdefault()` methods.
Changed in version 3.13: Added the `clear()` method.
The following method is also provided:

ndbm.close()[¶](https://docs.python.org/3/library/dbm.html#dbm.ndbm.ndbm.close "Link to this definition")

Close the NDBM database.
##  `dbm.dumb` — Portable DBM implementation[¶](https://docs.python.org/3/library/dbm.html#module-dbm.dumb "Link to this heading")
**Source code:**
Note
The `dbm.dumb` module is intended as a last resort fallback for the `dbm` module when a more robust module is not available. The `dbm.dumb` module is not written for speed and is not nearly as heavily used as the other database modules.
* * *
The `dbm.dumb` module provides a persistent [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict")-like interface which is written entirely in Python. Unlike other `dbm` backends, such as [`dbm.gnu`](https://docs.python.org/3/library/dbm.html#module-dbm.gnu "dbm.gnu: GNU database manager"), no external library is required.
The `dbm.dumb` module defines the following:

_exception_ dbm.dumb.error[¶](https://docs.python.org/3/library/dbm.html#dbm.dumb.error "Link to this definition")

Raised on `dbm.dumb`-specific errors, such as I/O errors. [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError "KeyError") is raised for general mapping errors like specifying an incorrect key.

dbm.dumb.open(_filename_ , _flag ='c'_, _mode =0o666_)[¶](https://docs.python.org/3/library/dbm.html#dbm.dumb.open "Link to this definition")

Open a `dbm.dumb` database.

Parameters:

  * **filename** –
The basename of the database file (without extensions). A new database creates the following files:
    * `_filename_.dat`
    * `_filename_.dir`
  * **flag** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "str")) –
    * `'r'`: Open existing database for reading only.
    * `'w'`: Open existing database for reading and writing.
    * `'c'` (default): Open database for reading and writing, creating it if it doesn’t exist.
    * `'n'`: Always create a new, empty database, open for reading and writing.
  * **mode** ([_int_](https://docs.python.org/3/library/functions.html#int "int")) – The Unix file access mode of the file (default: octal `0o666`), used only when the database has to be created.


Warning
It is possible to crash the Python interpreter when loading a database with a sufficiently large/complex entry due to stack depth limitations in Python’s AST compiler.
Changed in version 3.5: [`open()`](https://docs.python.org/3/library/dbm.html#dbm.dumb.open "dbm.dumb.open") always creates a new database when _flag_ is `'n'`.
Changed in version 3.8: A database opened read-only if _flag_ is `'r'`. A database is not created if it does not exist if _flag_ is `'r'` or `'w'`.
Changed in version 3.11: _filename_ accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).
The returned database object behaves similar to a mutable [mapping](https://docs.python.org/3/glossary.html#term-mapping), but the `keys()` and `items()` methods return lists, and the `setdefault()` method requires two arguments. It also supports a “closing” context manager via the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) keyword.
The following methods are also provided:

dumbdbm.close()[¶](https://docs.python.org/3/library/dbm.html#dbm.dumb.dumbdbm.close "Link to this definition")

Close the database.

dumbdbm.sync()[¶](https://docs.python.org/3/library/dbm.html#dbm.dumb.dumbdbm.sync "Link to this definition")

Synchronize the on-disk directory and data files. This method is called by the [`shelve.Shelf.sync()`](https://docs.python.org/3/library/shelve.html#shelve.Shelf.sync "shelve.Shelf.sync") method.
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`dbm` — Interfaces to Unix “databases”](https://docs.python.org/3/library/dbm.html)
    * [`dbm.sqlite3` — SQLite backend for dbm](https://docs.python.org/3/library/dbm.html#module-dbm.sqlite3)
    * [`dbm.gnu` — GNU database manager](https://docs.python.org/3/library/dbm.html#module-dbm.gnu)
    * [`dbm.ndbm` — New Database Manager](https://docs.python.org/3/library/dbm.html#module-dbm.ndbm)
    * [`dbm.dumb` — Portable DBM implementation](https://docs.python.org/3/library/dbm.html#module-dbm.dumb)


#### Previous topic
[`marshal` — Internal Python object serialization](https://docs.python.org/3/library/marshal.html "previous chapter")
#### Next topic
[`sqlite3` — DB-API 2.0 interface for SQLite databases](https://docs.python.org/3/library/sqlite3.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=dbm+%E2%80%94+Interfaces+to+Unix+%E2%80%9Cdatabases%E2%80%9D&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fdbm.html&pagesource=library%2Fdbm.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/sqlite3.html "sqlite3 — DB-API 2.0 interface for SQLite databases") |
  * [previous](https://docs.python.org/3/library/marshal.html "marshal — Internal Python object serialization") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Data Persistence](https://docs.python.org/3/library/persistence.html) »
  * [`dbm` — Interfaces to Unix “databases”](https://docs.python.org/3/library/dbm.html)
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
  *[GDBM]: GNU dbm
  *[NDBM]: New Database Manager
