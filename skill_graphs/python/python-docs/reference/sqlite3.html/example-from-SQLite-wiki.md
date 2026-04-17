# example from SQLite wiki
con.execute("CREATE VIRTUAL TABLE recipe USING fts3(name, ingredients)")
con.executescript("""
    INSERT INTO recipe (name, ingredients) VALUES('broccoli stew', 'broccoli peppers cheese tomatoes');
    INSERT INTO recipe (name, ingredients) VALUES('pumpkin stew', 'pumpkin onions garlic celery');
    INSERT INTO recipe (name, ingredients) VALUES('broccoli pie', 'broccoli cheese onions flour');
    INSERT INTO recipe (name, ingredients) VALUES('pumpkin pie', 'pumpkin sugar flour butter');
    """)
for row in con.execute("SELECT rowid, name, ingredients FROM recipe WHERE name MATCH 'pie'"):
    print(row)

```


load_extension(_path_ , _/_ , _*_ , _entrypoint =None_)[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.load_extension "Link to this definition")

Load an SQLite extension from a shared library. Enable extension loading with [`enable_load_extension()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.enable_load_extension "sqlite3.Connection.enable_load_extension") before calling this method.

Parameters:

  * **path** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "str")) – The path to the SQLite extension.
  * **entrypoint** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "str") _|__None_) – Entry point name. If `None` (the default), SQLite will come up with an entry point name of its own; see the SQLite docs


Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `sqlite3.load_extension` with arguments `connection`, `path`.
Added in version 3.2.
Changed in version 3.10: Added the `sqlite3.load_extension` auditing event.
Changed in version 3.12: Added the _entrypoint_ parameter.

iterdump(_*_ , _filter =None_)[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.iterdump "Link to this definition")

Return an [iterator](https://docs.python.org/3/glossary.html#term-iterator) to dump the database as SQL source code. Useful when saving an in-memory database for later restoration. Similar to the `.dump` command in the **sqlite3** shell.

Parameters:

**filter** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "str") _|__None_) – An optional `LIKE` pattern for database objects to dump, e.g. `prefix_%`. If `None` (the default), all database objects will be included.
Example:
Copy```
# Convert file example.db to SQL dump file dump.sql
con = sqlite3.connect('example.db')
with open('dump.sql', 'w') as f:
    for line in con.iterdump():
        f.write('%s\n' % line)
con.close()

```

See also
[How to handle non-UTF-8 text encodings](https://docs.python.org/3/library/sqlite3.html#sqlite3-howto-encoding)
Changed in version 3.13: Added the _filter_ parameter.

backup(_target_ , _*_ , _pages =-1_, _progress =None_, _name ='main'_, _sleep =0.250_)[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.backup "Link to this definition")

Create a backup of an SQLite database.
Works even if the database is being accessed by other clients or concurrently by the same connection.

Parameters:

  * **target** ([_Connection_](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection "sqlite3.Connection")) – The database connection to save the backup to.
  * **pages** ([_int_](https://docs.python.org/3/library/functions.html#int "int")) – The number of pages to copy at a time. If equal to or less than `0`, the entire database is copied in a single step. Defaults to `-1`.
  * **progress** ([callback](https://docs.python.org/3/glossary.html#term-callback) | None) – If set to a [callable](https://docs.python.org/3/glossary.html#term-callable), it is invoked with three integer arguments for every backup iteration: the _status_ of the last iteration, the _remaining_ number of pages still to be copied, and the _total_ number of pages. Defaults to `None`.
  * **name** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "str")) – The name of the database to back up. Either `"main"` (the default) for the main database, `"temp"` for the temporary database, or the name of a custom database as attached using the `ATTACH DATABASE` SQL statement.
  * **sleep** ([_float_](https://docs.python.org/3/library/functions.html#float "float")) – The number of seconds to sleep between successive attempts to back up remaining pages.


Example 1, copy an existing database into another:
Copy```
def progress(status, remaining, total):
    print(f'Copied {total-remaining} of {total} pages...')

src = sqlite3.connect('example.db')
dst = sqlite3.connect('backup.db')
with dst:
    src.backup(dst, pages=1, progress=progress)
dst.close()
src.close()

```

Example 2, copy an existing database into a transient copy:
Copy```
src = sqlite3.connect('example.db')
dst = sqlite3.connect(':memory:')
src.backup(dst)
dst.close()
src.close()

```

Added in version 3.7.
See also
[How to handle non-UTF-8 text encodings](https://docs.python.org/3/library/sqlite3.html#sqlite3-howto-encoding)

getlimit(_category_ , _/_)[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.getlimit "Link to this definition")

Get a connection runtime limit.

Parameters:

**category** ([_int_](https://docs.python.org/3/library/functions.html#int "int")) – The

Return type:

[int](https://docs.python.org/3/library/functions.html#int "int")

Raises:

[**ProgrammingError**](https://docs.python.org/3/library/sqlite3.html#sqlite3.ProgrammingError "sqlite3.ProgrammingError") – If _category_ is not recognised by the underlying SQLite library.
Example, query the maximum length of an SQL statement for `Connection` `con` (the default is 1000000000):
Copy```
>>> con.getlimit(sqlite3.SQLITE_LIMIT_SQL_LENGTH)
1000000000

```

Added in version 3.11.

setlimit(_category_ , _limit_ , _/_)[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.setlimit "Link to this definition")

Set a connection runtime limit. Attempts to increase a limit above its hard upper bound are silently truncated to the hard upper bound. Regardless of whether or not the limit was changed, the prior value of the limit is returned.

Parameters:

  * **category** ([_int_](https://docs.python.org/3/library/functions.html#int "int")) – The
  * **limit** ([_int_](https://docs.python.org/3/library/functions.html#int "int")) – The value of the new limit. If negative, the current limit is unchanged.



Return type:

[int](https://docs.python.org/3/library/functions.html#int "int")

Raises:

[**ProgrammingError**](https://docs.python.org/3/library/sqlite3.html#sqlite3.ProgrammingError "sqlite3.ProgrammingError") – If _category_ is not recognised by the underlying SQLite library.
Example, limit the number of attached databases to 1 for `Connection` `con` (the default limit is 10):
Copy```
>>> con.setlimit(sqlite3.SQLITE_LIMIT_ATTACHED, 1)
10
>>> con.getlimit(sqlite3.SQLITE_LIMIT_ATTACHED)
1

```

Added in version 3.11.

getconfig(_op_ , _/_)[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.getconfig "Link to this definition")

Query a boolean connection configuration option.

Parameters:

**op** ([_int_](https://docs.python.org/3/library/functions.html#int "int")) – A [SQLITE_DBCONFIG code](https://docs.python.org/3/library/sqlite3.html#sqlite3-dbconfig-constants).

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool "bool")
Added in version 3.12.

setconfig(_op_ , _enable =True_, _/_)[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.setconfig "Link to this definition")

Set a boolean connection configuration option.

Parameters:

  * **op** ([_int_](https://docs.python.org/3/library/functions.html#int "int")) – A [SQLITE_DBCONFIG code](https://docs.python.org/3/library/sqlite3.html#sqlite3-dbconfig-constants).
  * **enable** ([_bool_](https://docs.python.org/3/library/functions.html#bool "bool")) – `True` if the configuration option should be enabled (default); `False` if it should be disabled.


Added in version 3.12.

serialize(_*_ , _name ='main'_)[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.serialize "Link to this definition")

Serialize a database into a [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") object. For an ordinary on-disk database file, the serialization is just a copy of the disk file. For an in-memory database or a “temp” database, the serialization is the same sequence of bytes which would be written to disk if that database were backed up to disk.

Parameters:

**name** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "str")) – The database name to be serialized. Defaults to `"main"`.

Return type:

[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "bytes")
Note
This method is only available if the underlying SQLite library has the serialize API.
Added in version 3.11.

deserialize(_data_ , _/_ , _*_ , _name ='main'_)[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.deserialize "Link to this definition")

Deserialize a [`serialized`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.serialize "sqlite3.Connection.serialize") database into a `Connection`. This method causes the database connection to disconnect from database _name_ , and reopen _name_ as an in-memory database based on the serialization contained in _data_.

Parameters:

  * **data** ([_bytes_](https://docs.python.org/3/library/stdtypes.html#bytes "bytes")) – A serialized database.
  * **name** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "str")) – The database name to deserialize into. Defaults to `"main"`.



Raises:

  * [**OperationalError**](https://docs.python.org/3/library/sqlite3.html#sqlite3.OperationalError "sqlite3.OperationalError") – If the database connection is currently involved in a read transaction or a backup operation.
  * [**DatabaseError**](https://docs.python.org/3/library/sqlite3.html#sqlite3.DatabaseError "sqlite3.DatabaseError") – If _data_ does not contain a valid SQLite database.
  * [**OverflowError**](https://docs.python.org/3/library/exceptions.html#OverflowError "OverflowError") – If [`len(data)`](https://docs.python.org/3/library/functions.html#len "len") is larger than `2**63 - 1`.


Note
This method is only available if the underlying SQLite library has the deserialize API.
Added in version 3.11.

autocommit[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.autocommit "Link to this definition")

This attribute controls [**PEP 249**](https://peps.python.org/pep-0249/)-compliant transaction behaviour. `autocommit` has three allowed values:
  * `False`: Select [**PEP 249**](https://peps.python.org/pep-0249/)-compliant transaction behaviour, implying that `sqlite3` ensures a transaction is always open. Use [`commit()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.commit "sqlite3.Connection.commit") and [`rollback()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.rollback "sqlite3.Connection.rollback") to close transactions.
This is the recommended value of `autocommit`.
  * `True`: Use SQLite’s [`commit()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.commit "sqlite3.Connection.commit") and [`rollback()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.rollback "sqlite3.Connection.rollback") have no effect in this mode.
  * [`LEGACY_TRANSACTION_CONTROL`](https://docs.python.org/3/library/sqlite3.html#sqlite3.LEGACY_TRANSACTION_CONTROL "sqlite3.LEGACY_TRANSACTION_CONTROL"): Pre-Python 3.12 (non-[**PEP 249**](https://peps.python.org/pep-0249/)-compliant) transaction control. See [`isolation_level`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.isolation_level "sqlite3.Connection.isolation_level") for more details.
This is currently the default value of `autocommit`.


Changing `autocommit` to `False` will open a new transaction, and changing it to `True` will commit any pending transaction.
See [Transaction control via the autocommit attribute](https://docs.python.org/3/library/sqlite3.html#sqlite3-transaction-control-autocommit) for more details.
Note
The [`isolation_level`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.isolation_level "sqlite3.Connection.isolation_level") attribute has no effect unless [`autocommit`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.autocommit "sqlite3.Connection.autocommit") is [`LEGACY_TRANSACTION_CONTROL`](https://docs.python.org/3/library/sqlite3.html#sqlite3.LEGACY_TRANSACTION_CONTROL "sqlite3.LEGACY_TRANSACTION_CONTROL").
Added in version 3.12.

in_transaction[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.in_transaction "Link to this definition")

This read-only attribute corresponds to the low-level SQLite
`True` if a transaction is active (there are uncommitted changes), `False` otherwise.
Added in version 3.2.

isolation_level[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.isolation_level "Link to this definition")

Controls the [legacy transaction handling mode](https://docs.python.org/3/library/sqlite3.html#sqlite3-transaction-control-isolation-level) of `sqlite3`. If set to `None`, transactions are never implicitly opened. If set to one of `"DEFERRED"`, `"IMMEDIATE"`, or `"EXCLUSIVE"`, corresponding to the underlying implicit transaction management is performed.
If not overridden by the _isolation_level_ parameter of [`connect()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.connect "sqlite3.connect"), the default is `""`, which is an alias for `"DEFERRED"`.
Note
Using [`autocommit`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.autocommit "sqlite3.Connection.autocommit") to control transaction handling is recommended over using `isolation_level`. `isolation_level` has no effect unless `autocommit` is set to [`LEGACY_TRANSACTION_CONTROL`](https://docs.python.org/3/library/sqlite3.html#sqlite3.LEGACY_TRANSACTION_CONTROL "sqlite3.LEGACY_TRANSACTION_CONTROL") (the default).

row_factory[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.row_factory "Link to this definition")

The initial [`row_factory`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.row_factory "sqlite3.Cursor.row_factory") for [`Cursor`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor "sqlite3.Cursor") objects created from this connection. Assigning to this attribute does not affect the `row_factory` of existing cursors belonging to this connection, only new ones. Is `None` by default, meaning each row is returned as a [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "tuple").
See [How to create and use row factories](https://docs.python.org/3/library/sqlite3.html#sqlite3-howto-row-factory) for more details.

text_factory[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.text_factory "Link to this definition")

A [callable](https://docs.python.org/3/glossary.html#term-callable) that accepts a [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") parameter and returns a text representation of it. The callable is invoked for SQLite values with the `TEXT` data type. By default, this attribute is set to [`str`](https://docs.python.org/3/library/stdtypes.html#str "str").
See [How to handle non-UTF-8 text encodings](https://docs.python.org/3/library/sqlite3.html#sqlite3-howto-encoding) for more details.

total_changes[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.total_changes "Link to this definition")

Return the total number of database rows that have been modified, inserted, or deleted since the database connection was opened.
### Cursor objects[¶](https://docs.python.org/3/library/sqlite3.html#cursor-objects "Link to this heading")
> A `Cursor` object represents a [`Connection.cursor()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.cursor "sqlite3.Connection.cursor"), or by using any of the [connection shortcut methods](https://docs.python.org/3/library/sqlite3.html#sqlite3-connection-shortcuts).
> Cursor objects are [iterators](https://docs.python.org/3/glossary.html#term-iterator), meaning that if you [`execute()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.execute "sqlite3.Cursor.execute") a `SELECT` query, you can simply iterate over the cursor to fetch the resulting rows:
> Copy```
for row in cur.execute("SELECT t FROM data"):
    print(row)

```


_class_ sqlite3.Cursor[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor "Link to this definition")

A `Cursor` instance has the following attributes and methods.

execute(_sql_ , _parameters =()_, _/_)[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.execute "Link to this definition")

Execute a single SQL statement, optionally binding Python values using [placeholders](https://docs.python.org/3/library/sqlite3.html#sqlite3-placeholders).

Parameters:

  * **sql** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "str")) – A single SQL statement.
  * **parameters** ([`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict") | [sequence](https://docs.python.org/3/glossary.html#term-sequence)) – Python values to bind to placeholders in _sql_. A `dict` if named placeholders are used. A sequence if unnamed placeholders are used. See [How to use placeholders to bind values in SQL queries](https://docs.python.org/3/library/sqlite3.html#sqlite3-placeholders).



Raises:

[**ProgrammingError**](https://docs.python.org/3/library/sqlite3.html#sqlite3.ProgrammingError "sqlite3.ProgrammingError") – When _sql_ contains more than one SQL statement. When [named placeholders](https://docs.python.org/3/library/sqlite3.html#sqlite3-placeholders) are used and _parameters_ is a sequence instead of a [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict").
If [`autocommit`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.autocommit "sqlite3.Connection.autocommit") is [`LEGACY_TRANSACTION_CONTROL`](https://docs.python.org/3/library/sqlite3.html#sqlite3.LEGACY_TRANSACTION_CONTROL "sqlite3.LEGACY_TRANSACTION_CONTROL"), [`isolation_level`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.isolation_level "sqlite3.Connection.isolation_level") is not `None`, _sql_ is an `INSERT`, `UPDATE`, `DELETE`, or `REPLACE` statement, and there is no open transaction, a transaction is implicitly opened before executing _sql_.
Changed in version 3.14: [`ProgrammingError`](https://docs.python.org/3/library/sqlite3.html#sqlite3.ProgrammingError "sqlite3.ProgrammingError") is emitted if [named placeholders](https://docs.python.org/3/library/sqlite3.html#sqlite3-placeholders) are used and _parameters_ is a sequence instead of a [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict").
Use [`executescript()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.executescript "sqlite3.Cursor.executescript") to execute multiple SQL statements.

executemany(_sql_ , _parameters_ , _/_)[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.executemany "Link to this definition")

For every item in _parameters_ , repeatedly execute the [parameterized](https://docs.python.org/3/library/sqlite3.html#sqlite3-placeholders) DML SQL statement _sql_.
Uses the same implicit transaction handling as [`execute()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.execute "sqlite3.Cursor.execute").

Parameters:

  * **sql** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "str")) – A single SQL DML statement.
  * **parameters** ([iterable](https://docs.python.org/3/glossary.html#term-iterable)) – An iterable of parameters to bind with the placeholders in _sql_. See [How to use placeholders to bind values in SQL queries](https://docs.python.org/3/library/sqlite3.html#sqlite3-placeholders).



Raises:

[**ProgrammingError**](https://docs.python.org/3/library/sqlite3.html#sqlite3.ProgrammingError "sqlite3.ProgrammingError") – When _sql_ contains more than one SQL statement or is not a DML statement, When [named placeholders](https://docs.python.org/3/library/sqlite3.html#sqlite3-placeholders) are used and the items in _parameters_ are sequences instead of [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict")s.
Example:
Copy```
rows = [
    ("row1",),
    ("row2",),
]
# cur is an sqlite3.Cursor object
cur.executemany("INSERT INTO data VALUES(?)", rows)

```

Note
Any resulting rows are discarded, including DML statements with
Changed in version 3.14: [`ProgrammingError`](https://docs.python.org/3/library/sqlite3.html#sqlite3.ProgrammingError "sqlite3.ProgrammingError") is emitted if [named placeholders](https://docs.python.org/3/library/sqlite3.html#sqlite3-placeholders) are used and the items in _parameters_ are sequences instead of [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict")s.

executescript(_sql_script_ , _/_)[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.executescript "Link to this definition")

Execute the SQL statements in _sql_script_. If the [`autocommit`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.autocommit "sqlite3.Connection.autocommit") is [`LEGACY_TRANSACTION_CONTROL`](https://docs.python.org/3/library/sqlite3.html#sqlite3.LEGACY_TRANSACTION_CONTROL "sqlite3.LEGACY_TRANSACTION_CONTROL") and there is a pending transaction, an implicit `COMMIT` statement is executed first. No other implicit transaction control is performed; any transaction control must be added to _sql_script_.
_sql_script_ must be a [`string`](https://docs.python.org/3/library/stdtypes.html#str "str").
Example:
Copy```
