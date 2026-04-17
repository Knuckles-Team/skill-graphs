# so the connection object should be closed manually
con.close()

```

### How to work with SQLite URIs[¶](https://docs.python.org/3/library/sqlite3.html#how-to-work-with-sqlite-uris "Link to this heading")
Some useful URI tricks include:
  * Open a database in read-only mode:


Copy```
>>> con = sqlite3.connect("file:tutorial.db?mode=ro", uri=True)
>>> con.execute("CREATE TABLE readonly(data)")
Traceback (most recent call last):
OperationalError: attempt to write a readonly database
>>> con.close()

```

  * Do not implicitly create a new database file if it does not already exist; will raise [`OperationalError`](https://docs.python.org/3/library/sqlite3.html#sqlite3.OperationalError "sqlite3.OperationalError") if unable to create a new file:


Copy```
>>> con = sqlite3.connect("file:nosuchdb.db?mode=rw", uri=True)
Traceback (most recent call last):
OperationalError: unable to open database file

```

  * Create a shared named in-memory database:


Copy```
db = "file:mem1?mode=memory&cache=shared"
con1 = sqlite3.connect(db, uri=True)
con2 = sqlite3.connect(db, uri=True)
with con1:
    con1.execute("CREATE TABLE shared(data)")
    con1.execute("INSERT INTO shared VALUES(28)")
res = con2.execute("SELECT data FROM shared")
assert res.fetchone() == (28,)

con1.close()
con2.close()

```

More information about this feature, including a list of parameters, can be found in the
### How to create and use row factories[¶](https://docs.python.org/3/library/sqlite3.html#how-to-create-and-use-row-factories "Link to this heading")
By default, `sqlite3` represents each row as a [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "tuple"). If a `tuple` does not suit your needs, you can use the [`sqlite3.Row`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Row "sqlite3.Row") class or a custom [`row_factory`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.row_factory "sqlite3.Cursor.row_factory").
While `row_factory` exists as an attribute both on the [`Cursor`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor "sqlite3.Cursor") and the [`Connection`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection "sqlite3.Connection"), it is recommended to set [`Connection.row_factory`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.row_factory "sqlite3.Connection.row_factory"), so all cursors created from the connection will use the same row factory.
`Row` provides indexed and case-insensitive named access to columns, with minimal memory overhead and performance impact over a `tuple`. To use `Row` as a row factory, assign it to the `row_factory` attribute:
Copy```
>>> con = sqlite3.connect(":memory:")
>>> con.row_factory = sqlite3.Row

```

Queries now return `Row` objects:
Copy```
>>> res = con.execute("SELECT 'Earth' AS name, 6378 AS radius")
>>> row = res.fetchone()
>>> row.keys()
['name', 'radius']
>>> row[0]         # Access by index.
'Earth'
>>> row["name"]    # Access by name.
'Earth'
>>> row["RADIUS"]  # Column names are case-insensitive.
6378
>>> con.close()

```

Note
The `FROM` clause can be omitted in the `SELECT` statement, as in the above example. In such cases, SQLite returns a single row with columns defined by expressions, e.g. literals, with the given aliases `expr AS alias`.
You can create a custom [`row_factory`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.row_factory "sqlite3.Cursor.row_factory") that returns each row as a [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict"), with column names mapped to values:
Copy```
def dict_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}

```

Using it, queries now return a `dict` instead of a `tuple`:
Copy```
>>> con = sqlite3.connect(":memory:")
>>> con.row_factory = dict_factory
>>> for row in con.execute("SELECT 1 AS a, 2 AS b"):
...     print(row)
{'a': 1, 'b': 2}
>>> con.close()

```

The following row factory returns a [named tuple](https://docs.python.org/3/glossary.html#term-named-tuple):
Copy```
from collections import namedtuple

def namedtuple_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    cls = namedtuple("Row", fields)
    return cls._make(row)

```

`namedtuple_factory()` can be used as follows:
Copy```
>>> con = sqlite3.connect(":memory:")
>>> con.row_factory = namedtuple_factory
>>> cur = con.execute("SELECT 1 AS a, 2 AS b")
>>> row = cur.fetchone()
>>> row
Row(a=1, b=2)
>>> row[0]  # Indexed access.
1
>>> row.b   # Attribute access.
2
>>> con.close()

```

With some adjustments, the above recipe can be adapted to use a [`dataclass`](https://docs.python.org/3/library/dataclasses.html#dataclasses.dataclass "dataclasses.dataclass"), or any other custom class, instead of a [`namedtuple`](https://docs.python.org/3/library/collections.html#collections.namedtuple "collections.namedtuple").
### How to handle non-UTF-8 text encodings[¶](https://docs.python.org/3/library/sqlite3.html#how-to-handle-non-utf-8-text-encodings "Link to this heading")
By default, `sqlite3` uses [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") to adapt SQLite values with the `TEXT` data type. This works well for UTF-8 encoded text, but it might fail for other encodings and invalid UTF-8. You can use a custom [`text_factory`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.text_factory "sqlite3.Connection.text_factory") to handle such cases.
Because of SQLite’s `TEXT` data type containing non-UTF-8 encodings, or even arbitrary data. To demonstrate, let’s assume we have a database with ISO-8859-2 (Latin-2) encoded text, for example a table of Czech-English dictionary entries. Assuming we now have a [`Connection`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection "sqlite3.Connection") instance `con` connected to this database, we can decode the Latin-2 encoded text using this [`text_factory`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.text_factory "sqlite3.Connection.text_factory"):
Copy```
con.text_factory = lambda data: str(data, encoding="latin2")

```

For invalid UTF-8 or arbitrary data in stored in `TEXT` table columns, you can use the following technique, borrowed from the [Unicode HOWTO](https://docs.python.org/3/howto/unicode.html#unicode-howto):
Copy```
con.text_factory = lambda data: str(data, errors="surrogateescape")

```

Note
The `sqlite3` module API does not support strings containing surrogates.
See also
[Unicode HOWTO](https://docs.python.org/3/howto/unicode.html#unicode-howto)
## Explanation[¶](https://docs.python.org/3/library/sqlite3.html#explanation "Link to this heading")
### Transaction control[¶](https://docs.python.org/3/library/sqlite3.html#transaction-control "Link to this heading")
`sqlite3` offers multiple methods of controlling whether, when and how database transactions are opened and closed. [Transaction control via the autocommit attribute](https://docs.python.org/3/library/sqlite3.html#sqlite3-transaction-control-autocommit) is recommended, while [Transaction control via the isolation_level attribute](https://docs.python.org/3/library/sqlite3.html#sqlite3-transaction-control-isolation-level) retains the pre-Python 3.12 behaviour.
#### Transaction control via the `autocommit` attribute[¶](https://docs.python.org/3/library/sqlite3.html#transaction-control-via-the-autocommit-attribute "Link to this heading")
The recommended way of controlling transaction behaviour is through the [`Connection.autocommit`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.autocommit "sqlite3.Connection.autocommit") attribute, which should preferably be set using the _autocommit_ parameter of [`connect()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.connect "sqlite3.connect").
It is suggested to set _autocommit_ to `False`, which implies [**PEP 249**](https://peps.python.org/pep-0249/)-compliant transaction control. This means:
  * `sqlite3` ensures that a transaction is always open, so [`connect()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.connect "sqlite3.connect"), [`Connection.commit()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.commit "sqlite3.Connection.commit"), and [`Connection.rollback()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.rollback "sqlite3.Connection.rollback") will implicitly open a new transaction (immediately after closing the pending one, for the latter two). `sqlite3` uses `BEGIN DEFERRED` statements when opening transactions.
  * Transactions should be committed explicitly using `commit()`.
  * Transactions should be rolled back explicitly using `rollback()`.
  * An implicit rollback is performed if the database is [`close()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.close "sqlite3.Connection.close")-ed with pending changes.


Set _autocommit_ to `True` to enable SQLite’s [`Connection.commit()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.commit "sqlite3.Connection.commit") and [`Connection.rollback()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.rollback "sqlite3.Connection.rollback") have no effect. Note that SQLite’s autocommit mode is distinct from the [**PEP 249**](https://peps.python.org/pep-0249/)-compliant [`Connection.autocommit`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.autocommit "sqlite3.Connection.autocommit") attribute; use [`Connection.in_transaction`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.in_transaction "sqlite3.Connection.in_transaction") to query the low-level SQLite autocommit mode.
Set _autocommit_ to [`LEGACY_TRANSACTION_CONTROL`](https://docs.python.org/3/library/sqlite3.html#sqlite3.LEGACY_TRANSACTION_CONTROL "sqlite3.LEGACY_TRANSACTION_CONTROL") to leave transaction control behaviour to the [`Connection.isolation_level`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.isolation_level "sqlite3.Connection.isolation_level") attribute. See [Transaction control via the isolation_level attribute](https://docs.python.org/3/library/sqlite3.html#sqlite3-transaction-control-isolation-level) for more information.
#### Transaction control via the `isolation_level` attribute[¶](https://docs.python.org/3/library/sqlite3.html#transaction-control-via-the-isolation-level-attribute "Link to this heading")
Note
The recommended way of controlling transactions is via the [`autocommit`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.autocommit "sqlite3.Connection.autocommit") attribute. See [Transaction control via the autocommit attribute](https://docs.python.org/3/library/sqlite3.html#sqlite3-transaction-control-autocommit).
If [`Connection.autocommit`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.autocommit "sqlite3.Connection.autocommit") is set to [`LEGACY_TRANSACTION_CONTROL`](https://docs.python.org/3/library/sqlite3.html#sqlite3.LEGACY_TRANSACTION_CONTROL "sqlite3.LEGACY_TRANSACTION_CONTROL") (the default), transaction behaviour is controlled using the [`Connection.isolation_level`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.isolation_level "sqlite3.Connection.isolation_level") attribute. Otherwise, `isolation_level` has no effect.
If the connection attribute [`isolation_level`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.isolation_level "sqlite3.Connection.isolation_level") is not `None`, new transactions are implicitly opened before [`execute()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.execute "sqlite3.Cursor.execute") and [`executemany()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.executemany "sqlite3.Cursor.executemany") executes `INSERT`, `UPDATE`, `DELETE`, or `REPLACE` statements; for other statements, no implicit transaction handling is performed. Use the [`commit()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.commit "sqlite3.Connection.commit") and [`rollback()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.rollback "sqlite3.Connection.rollback") methods to respectively commit and roll back pending transactions. You can choose the underlying `BEGIN` statements `sqlite3` implicitly executes – via the `isolation_level` attribute.
If [`isolation_level`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.isolation_level "sqlite3.Connection.isolation_level") is set to `None`, no transactions are implicitly opened at all. This leaves the underlying SQLite library in [`in_transaction`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.in_transaction "sqlite3.Connection.in_transaction") attribute.
The [`executescript()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.executescript "sqlite3.Cursor.executescript") method implicitly commits any pending transaction before execution of the given SQL script, regardless of the value of [`isolation_level`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.isolation_level "sqlite3.Connection.isolation_level").
Changed in version 3.6: `sqlite3` used to implicitly commit an open transaction before DDL statements. This is no longer the case.
Changed in version 3.12: The recommended way of controlling transactions is now via the [`autocommit`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.autocommit "sqlite3.Connection.autocommit") attribute.
### [Table of Contents](https://docs.python.org/3/contents.html)
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
[`dbm` — Interfaces to Unix “databases”](https://docs.python.org/3/library/dbm.html "previous chapter")
#### Next topic
[Data Compression and Archiving](https://docs.python.org/3/library/archiving.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=sqlite3+%E2%80%94+DB-API+2.0+interface+for+SQLite+databases&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fsqlite3.html&pagesource=library%2Fsqlite3.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/archiving.html "Data Compression and Archiving") |
  * [previous](https://docs.python.org/3/library/dbm.html "dbm — Interfaces to Unix “databases”") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Data Persistence](https://docs.python.org/3/library/persistence.html) »
  * [`sqlite3` — DB-API 2.0 interface for SQLite databases](https://docs.python.org/3/library/sqlite3.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[URI]: Uniform Resource Identifier
  *[/]: Positional-only parameter separator (PEP 570)
  *[BLOB]: Binary Large OBject
  *[DML]: Data Manipulation Language
  *[CTE]: Common Table Expression
  *[EOF]: End of File
