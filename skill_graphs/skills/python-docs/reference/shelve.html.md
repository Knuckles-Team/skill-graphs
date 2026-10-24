[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`shelve` — Python object persistence](https://docs.python.org/3/library/shelve.html)
    * [Restrictions](https://docs.python.org/3/library/shelve.html#restrictions)
    * [Example](https://docs.python.org/3/library/shelve.html#example)


#### Previous topic
[`copyreg` — Register `pickle` support functions](https://docs.python.org/3/library/copyreg.html "previous chapter")
#### Next topic
[`marshal` — Internal Python object serialization](https://docs.python.org/3/library/marshal.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=shelve+%E2%80%94+Python+object+persistence&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fshelve.html&pagesource=library%2Fshelve.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/marshal.html "marshal — Internal Python object serialization") |
  * [previous](https://docs.python.org/3/library/copyreg.html "copyreg — Register pickle support functions") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Data Persistence](https://docs.python.org/3/library/persistence.html) »
  * [`shelve` — Python object persistence](https://docs.python.org/3/library/shelve.html)
  * |
  * Theme  Auto Light Dark |


#  `shelve` — Python object persistence[¶](https://docs.python.org/3/library/shelve.html#module-shelve "Link to this heading")
**Source code:**
* * *
A “shelf” is a persistent, dictionary-like object. The difference with “dbm” databases is that the values (not the keys!) in a shelf can be essentially arbitrary Python objects — anything that the [`pickle`](https://docs.python.org/3/library/pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.") module can handle. This includes most class instances, recursive data types, and objects containing lots of shared sub-objects. The keys are ordinary strings.

shelve.open(_filename_ , _flag ='c'_, _protocol =None_, _writeback =False_)[¶](https://docs.python.org/3/library/shelve.html#shelve.open "Link to this definition")

Open a persistent dictionary. The filename specified is the base filename for the underlying database. As a side-effect, an extension may be added to the filename and more than one file may be created. By default, the underlying database file is opened for reading and writing. The optional _flag_ parameter has the same interpretation as the _flag_ parameter of [`dbm.open()`](https://docs.python.org/3/library/dbm.html#dbm.open "dbm.open").
By default, pickles created with [`pickle.DEFAULT_PROTOCOL`](https://docs.python.org/3/library/pickle.html#pickle.DEFAULT_PROTOCOL "pickle.DEFAULT_PROTOCOL") are used to serialize values. The version of the pickle protocol can be specified with the _protocol_ parameter.
Because of Python semantics, a shelf cannot know when a mutable persistent-dictionary entry is modified. By default modified objects are written _only_ when assigned to the shelf (see [Example](https://docs.python.org/3/library/shelve.html#shelve-example)). If the optional _writeback_ parameter is set to `True`, all entries accessed are also cached in memory, and written back on [`sync()`](https://docs.python.org/3/library/shelve.html#shelve.Shelf.sync "shelve.Shelf.sync") and [`close()`](https://docs.python.org/3/library/shelve.html#shelve.Shelf.close "shelve.Shelf.close"); this can make it handier to mutate mutable entries in the persistent dictionary, but, if many entries are accessed, it can consume vast amounts of memory for the cache, and it can make the close operation very slow since all accessed entries are written back (there is no way to determine which accessed entries are mutable, nor which ones were actually mutated).
Changed in version 3.10: [`pickle.DEFAULT_PROTOCOL`](https://docs.python.org/3/library/pickle.html#pickle.DEFAULT_PROTOCOL "pickle.DEFAULT_PROTOCOL") is now used as the default pickle protocol.
Changed in version 3.11: Accepts [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object) for filename.
Note
Do not rely on the shelf being closed automatically; always call [`close()`](https://docs.python.org/3/library/shelve.html#shelve.Shelf.close "shelve.Shelf.close") explicitly when you don’t need it any more, or use [`shelve.open()`](https://docs.python.org/3/library/shelve.html#shelve.open "shelve.open") as a context manager:
Copy```
with shelve.open('spam') as db:
    db['eggs'] = 'eggs'

```

Warning
Because the `shelve` module is backed by [`pickle`](https://docs.python.org/3/library/pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back."), it is insecure to load a shelf from an untrusted source. Like with pickle, loading a shelf can execute arbitrary code.
Shelf objects support most of the methods and operations supported by dictionaries (except copying, constructors and operators `|` and `|=`). This eases the transition from dictionary based scripts to those requiring persistent storage.
Two additional methods are supported:

Shelf.sync()[¶](https://docs.python.org/3/library/shelve.html#shelve.Shelf.sync "Link to this definition")

Write back all entries in the cache if the shelf was opened with _writeback_ set to [`True`](https://docs.python.org/3/library/constants.html#True "True"). Also empty the cache and synchronize the persistent dictionary on disk, if feasible. This is called automatically when the shelf is closed with [`close()`](https://docs.python.org/3/library/shelve.html#shelve.Shelf.close "shelve.Shelf.close").

Shelf.close()[¶](https://docs.python.org/3/library/shelve.html#shelve.Shelf.close "Link to this definition")

Synchronize and close the persistent _dict_ object. Operations on a closed shelf will fail with a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError").
See also
## Restrictions[¶](https://docs.python.org/3/library/shelve.html#restrictions "Link to this heading")
  * The choice of which database package will be used (such as [`dbm.ndbm`](https://docs.python.org/3/library/dbm.html#module-dbm.ndbm "dbm.ndbm: The New Database Manager") or [`dbm.gnu`](https://docs.python.org/3/library/dbm.html#module-dbm.gnu "dbm.gnu: GNU database manager")) depends on which interface is available. Therefore it is not safe to open the database directly using [`dbm`](https://docs.python.org/3/library/dbm.html#module-dbm "dbm: Interfaces to various Unix "database" formats."). The database is also (unfortunately) subject to the limitations of `dbm`, if it is used — this means that (the pickled representation of) the objects stored in the database should be fairly small, and in rare cases key collisions may cause the database to refuse updates.
  * The `shelve` module does not support _concurrent_ read/write access to shelved objects. (Multiple simultaneous read accesses are safe.) When a program has a shelf open for writing, no other program should have it open for reading or writing. Unix file locking can be used to solve this, but this differs across Unix versions and requires knowledge about the database implementation used.
  * On macOS [`dbm.ndbm`](https://docs.python.org/3/library/dbm.html#module-dbm.ndbm "dbm.ndbm: The New Database Manager") can silently corrupt the database file on updates, which can cause hard crashes when trying to read from the database.



_class_ shelve.Shelf(_dict_ , _protocol =None_, _writeback =False_, _keyencoding ='utf-8'_)[¶](https://docs.python.org/3/library/shelve.html#shelve.Shelf "Link to this definition")

A subclass of [`collections.abc.MutableMapping`](https://docs.python.org/3/library/collections.abc.html#collections.abc.MutableMapping "collections.abc.MutableMapping") which stores pickled values in the _dict_ object.
By default, pickles created with [`pickle.DEFAULT_PROTOCOL`](https://docs.python.org/3/library/pickle.html#pickle.DEFAULT_PROTOCOL "pickle.DEFAULT_PROTOCOL") are used to serialize values. The version of the pickle protocol can be specified with the _protocol_ parameter. See the [`pickle`](https://docs.python.org/3/library/pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.") documentation for a discussion of the pickle protocols.
If the _writeback_ parameter is `True`, the object will hold a cache of all entries accessed and write them back to the _dict_ at sync and close times. This allows natural operations on mutable entries, but can consume much more memory and make sync and close take a long time.
The _keyencoding_ parameter is the encoding used to encode keys before they are used with the underlying dict.
A `Shelf` object can also be used as a context manager, in which case it will be automatically closed when the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) block ends.
Changed in version 3.2: Added the _keyencoding_ parameter; previously, keys were always encoded in UTF-8.
Changed in version 3.4: Added context manager support.
Changed in version 3.10: [`pickle.DEFAULT_PROTOCOL`](https://docs.python.org/3/library/pickle.html#pickle.DEFAULT_PROTOCOL "pickle.DEFAULT_PROTOCOL") is now used as the default pickle protocol.

_class_ shelve.BsdDbShelf(_dict_ , _protocol =None_, _writeback =False_, _keyencoding ='utf-8'_)[¶](https://docs.python.org/3/library/shelve.html#shelve.BsdDbShelf "Link to this definition")

A subclass of [`Shelf`](https://docs.python.org/3/library/shelve.html#shelve.Shelf "shelve.Shelf") which exposes `first()`, `next()`, `previous()`, `last()` and `set_location()` methods. These are available in the third-party `bsddb` module from _dict_ object passed to the constructor must support those methods. This is generally accomplished by calling one of `bsddb.hashopen()`, `bsddb.btopen()` or `bsddb.rnopen()`. The optional _protocol_ , _writeback_ , and _keyencoding_ parameters have the same interpretation as for the `Shelf` class.

_class_ shelve.DbfilenameShelf(_filename_ , _flag ='c'_, _protocol =None_, _writeback =False_)[¶](https://docs.python.org/3/library/shelve.html#shelve.DbfilenameShelf "Link to this definition")

A subclass of [`Shelf`](https://docs.python.org/3/library/shelve.html#shelve.Shelf "shelve.Shelf") which accepts a _filename_ instead of a dict-like object. The underlying file will be opened using [`dbm.open()`](https://docs.python.org/3/library/dbm.html#dbm.open "dbm.open"). By default, the file will be created and opened for both read and write. The optional _flag_ parameter has the same interpretation as for the [`open()`](https://docs.python.org/3/library/shelve.html#shelve.open "shelve.open") function. The optional _protocol_ and _writeback_ parameters have the same interpretation as for the `Shelf` class.
## Example[¶](https://docs.python.org/3/library/shelve.html#example "Link to this heading")
To summarize the interface (`key` is a string, `data` is an arbitrary object):
Copy```
import shelve

d = shelve.open(filename)  # open -- file may get suffix added by low-level
                           # library

d[key] = data              # store data at key (overwrites old data if
                           # using an existing key)
data = d[key]              # retrieve a COPY of data at key (raise KeyError
                           # if no such key)
del d[key]                 # delete data stored at key (raises KeyError
                           # if no such key)

flag = key in d            # true if the key exists
klist = list(d.keys())     # a list of all existing keys (slow!)

# as d was opened WITHOUT writeback=True, beware:
d['xx'] = [0, 1, 2]        # this works as expected, but...
d['xx'].append(3)          # *this doesn't!* -- d['xx'] is STILL [0, 1, 2]!

# having opened d without writeback=True, you need to code carefully:
temp = d['xx']             # extracts the copy
temp.append(5)             # mutates the copy
d['xx'] = temp             # stores the copy right back, to persist it

# or, d=shelve.open(filename,writeback=True) would let you just code
# d['xx'].append(5) and have it work as expected, BUT it would also
# consume more memory and make the d.close() operation slower.

d.close()                  # close it

```

See also

Module [`dbm`](https://docs.python.org/3/library/dbm.html#module-dbm "dbm: Interfaces to various Unix "database" formats.")

Generic interface to `dbm`-style databases.

Module [`pickle`](https://docs.python.org/3/library/pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.")

Object serialization used by `shelve`.
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`shelve` — Python object persistence](https://docs.python.org/3/library/shelve.html)
    * [Restrictions](https://docs.python.org/3/library/shelve.html#restrictions)
    * [Example](https://docs.python.org/3/library/shelve.html#example)


#### Previous topic
[`copyreg` — Register `pickle` support functions](https://docs.python.org/3/library/copyreg.html "previous chapter")
#### Next topic
[`marshal` — Internal Python object serialization](https://docs.python.org/3/library/marshal.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=shelve+%E2%80%94+Python+object+persistence&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fshelve.html&pagesource=library%2Fshelve.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/marshal.html "marshal — Internal Python object serialization") |
  * [previous](https://docs.python.org/3/library/copyreg.html "copyreg — Register pickle support functions") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Data Persistence](https://docs.python.org/3/library/persistence.html) »
  * [`shelve` — Python object persistence](https://docs.python.org/3/library/shelve.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
