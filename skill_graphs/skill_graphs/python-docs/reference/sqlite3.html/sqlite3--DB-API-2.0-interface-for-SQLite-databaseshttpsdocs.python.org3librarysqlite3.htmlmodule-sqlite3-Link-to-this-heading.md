#  `sqlite3` — DB-API 2.0 interface for SQLite databases[¶](https://docs.python.org/3/library/sqlite3.html#module-sqlite3 "Link to this heading")
**Source code:**
SQLite is a C library that provides a lightweight disk-based database that doesn’t require a separate server process and allows accessing the database using a nonstandard variant of the SQL query language. Some applications can use SQLite for internal data storage. It’s also possible to prototype an application using SQLite and then port the code to a larger database such as PostgreSQL or Oracle.
The `sqlite3` module was written by Gerhard Häring. It provides an SQL interface compliant with the DB-API 2.0 specification described by [**PEP 249**](https://peps.python.org/pep-0249/), and requires the third-party
This is an [optional module](https://docs.python.org/3/glossary.html#term-optional-module). If it is missing from your copy of CPython, look for documentation from your distributor (that is, whoever provided Python to you). If you are the distributor, see [Requirements for optional modules](https://docs.python.org/3/using/configure.html#optional-module-requirements).
This document includes four main sections:
  * [Tutorial](https://docs.python.org/3/library/sqlite3.html#sqlite3-tutorial) teaches how to use the `sqlite3` module.
  * [Reference](https://docs.python.org/3/library/sqlite3.html#sqlite3-reference) describes the classes and functions this module defines.
  * [How-to guides](https://docs.python.org/3/library/sqlite3.html#sqlite3-howtos) details how to handle specific tasks.
  * [Explanation](https://docs.python.org/3/library/sqlite3.html#sqlite3-explanation) provides in-depth background on transaction control.


See also
The SQLite web page; the documentation describes the syntax and the available data types for the supported SQL dialect.
Tutorial, reference and examples for learning SQL syntax.

[**PEP 249**](https://peps.python.org/pep-0249/) - Database API Specification 2.0

PEP written by Marc-André Lemburg.
## Tutorial[¶](https://docs.python.org/3/library/sqlite3.html#tutorial "Link to this heading")
In this tutorial, you will create a database of Monty Python movies using basic `sqlite3` functionality. It assumes a fundamental understanding of database concepts, including
First, we need to create a new database and open a database connection to allow `sqlite3` to work with it. Call [`sqlite3.connect()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.connect "sqlite3.connect") to create a connection to the database `tutorial.db` in the current working directory, implicitly creating it if it does not exist:
Copy```
import sqlite3
con = sqlite3.connect("tutorial.db")

```

The returned [`Connection`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection "sqlite3.Connection") object `con` represents the connection to the on-disk database.
In order to execute SQL statements and fetch results from SQL queries, we will need to use a database cursor. Call [`con.cursor()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.cursor "sqlite3.Connection.cursor") to create the [`Cursor`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor "sqlite3.Cursor"):
Copy```
cur = con.cursor()

```

Now that we’ve got a database connection and a cursor, we can create a database table `movie` with columns for title, release year, and review score. For simplicity, we can just use column names in the table declaration – thanks to the `CREATE TABLE` statement by calling [`cur.execute(...)`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.execute "sqlite3.Cursor.execute"):
Copy```
cur.execute("CREATE TABLE movie(title, year, score)")

```

We can verify that the new table has been created by querying the `sqlite_master` table built-in to SQLite, which should now contain an entry for the `movie` table definition (see [`cur.execute(...)`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.execute "sqlite3.Cursor.execute"), assign the result to `res`, and call [`res.fetchone()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.fetchone "sqlite3.Cursor.fetchone") to fetch the resulting row:
Copy```
>>> res = cur.execute("SELECT name FROM sqlite_master")
>>> res.fetchone()
('movie',)

```

We can see that the table has been created, as the query returns a [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "tuple") containing the table’s name. If we query `sqlite_master` for a non-existent table `spam`, `res.fetchone()` will return `None`:
Copy```
>>> res = cur.execute("SELECT name FROM sqlite_master WHERE name='spam'")
>>> res.fetchone() is None
True

```

Now, add two rows of data supplied as SQL literals by executing an `INSERT` statement, once again by calling [`cur.execute(...)`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.execute "sqlite3.Cursor.execute"):
Copy```
cur.execute("""
    INSERT INTO movie VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
""")

```

The `INSERT` statement implicitly opens a transaction, which needs to be committed before changes are saved in the database (see [Transaction control](https://docs.python.org/3/library/sqlite3.html#sqlite3-controlling-transactions) for details). Call [`con.commit()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.commit "sqlite3.Connection.commit") on the connection object to commit the transaction:
Copy```
con.commit()

```

We can verify that the data was inserted correctly by executing a `SELECT` query. Use the now-familiar [`cur.execute(...)`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.execute "sqlite3.Cursor.execute") to assign the result to `res`, and call [`res.fetchall()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.fetchall "sqlite3.Cursor.fetchall") to return all resulting rows:
Copy```
>>> res = cur.execute("SELECT score FROM movie")
>>> res.fetchall()
[(8.2,), (7.5,)]

```

The result is a [`list`](https://docs.python.org/3/library/stdtypes.html#list "list") of two `tuple`s, one per row, each containing that row’s `score` value.
Now, insert three more rows by calling [`cur.executemany(...)`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.executemany "sqlite3.Cursor.executemany"):
Copy```
data = [
    ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
    ("Monty Python's The Meaning of Life", 1983, 7.5),
    ("Monty Python's Life of Brian", 1979, 8.0),
]
cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
con.commit()  # Remember to commit the transaction after executing INSERT.

```

Notice that `?` placeholders are used to bind `data` to the query. Always use placeholders instead of [string formatting](https://docs.python.org/3/tutorial/inputoutput.html#tut-formatting) to bind Python values to SQL statements, to avoid [How to use placeholders to bind values in SQL queries](https://docs.python.org/3/library/sqlite3.html#sqlite3-placeholders) for more details).
We can verify that the new rows were inserted by executing a `SELECT` query, this time iterating over the results of the query:
Copy```
>>> for row in cur.execute("SELECT year, title FROM movie ORDER BY year"):
...     print(row)
(1971, 'And Now for Something Completely Different')
(1975, 'Monty Python and the Holy Grail')
(1979, "Monty Python's Life of Brian")
(1982, 'Monty Python Live at the Hollywood Bowl')
(1983, "Monty Python's The Meaning of Life")

```

Each row is a two-item [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "tuple") of `(year, title)`, matching the columns selected in the query.
Finally, verify that the database has been written to disk by calling [`con.close()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.close "sqlite3.Connection.close") to close the existing connection, opening a new one, creating a new cursor, then querying the database:
Copy```
>>> con.close()
>>> new_con = sqlite3.connect("tutorial.db")
>>> new_cur = new_con.cursor()
>>> res = new_cur.execute("SELECT title, year FROM movie ORDER BY score DESC")
>>> title, year = res.fetchone()
>>> print(f'The highest scoring Monty Python movie is {title!r}, released in {year}')
The highest scoring Monty Python movie is 'Monty Python and the Holy Grail', released in 1975
>>> new_con.close()

```

You’ve now created an SQLite database using the `sqlite3` module, inserted data and retrieved values from it in multiple ways.
See also
  * [How-to guides](https://docs.python.org/3/library/sqlite3.html#sqlite3-howtos) for further reading:
    * [How to use placeholders to bind values in SQL queries](https://docs.python.org/3/library/sqlite3.html#sqlite3-placeholders)
    * [How to adapt custom Python types to SQLite values](https://docs.python.org/3/library/sqlite3.html#sqlite3-adapters)
    * [How to convert SQLite values to custom Python types](https://docs.python.org/3/library/sqlite3.html#sqlite3-converters)
    * [How to use the connection context manager](https://docs.python.org/3/library/sqlite3.html#sqlite3-connection-context-manager)
    * [How to create and use row factories](https://docs.python.org/3/library/sqlite3.html#sqlite3-howto-row-factory)
  * [Explanation](https://docs.python.org/3/library/sqlite3.html#sqlite3-explanation) for in-depth background on transaction control.


## Reference[¶](https://docs.python.org/3/library/sqlite3.html#reference "Link to this heading")
### Module functions[¶](https://docs.python.org/3/library/sqlite3.html#module-functions "Link to this heading")

sqlite3.connect(_database_ , _timeout =5.0_, _detect_types =0_, _isolation_level ='DEFERRED'_, _check_same_thread =True_, _factory =sqlite3.Connection_, _cached_statements =128_, _uri =False_, _*_ , _autocommit =sqlite3.LEGACY_TRANSACTION_CONTROL_)[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.connect "Link to this definition")

Open a connection to an SQLite database.

Parameters:

  * **database** ([path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)) – The path to the database file to be opened. You can pass `":memory:"` to create an
  * **timeout** ([_float_](https://docs.python.org/3/library/functions.html#float "float")) – How many seconds the connection should wait before raising an [`OperationalError`](https://docs.python.org/3/library/sqlite3.html#sqlite3.OperationalError "sqlite3.OperationalError") when a table is locked. If another connection opens a transaction to modify a table, that table will be locked until the transaction is committed. Default five seconds.
  * **detect_types** ([_int_](https://docs.python.org/3/library/functions.html#int "int")) – Control whether and how data types not [natively supported by SQLite](https://docs.python.org/3/library/sqlite3.html#sqlite3-types) are looked up to be converted to Python types, using the converters registered with [`register_converter()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.register_converter "sqlite3.register_converter"). Set it to any combination (using `|`, bitwise or) of [`PARSE_DECLTYPES`](https://docs.python.org/3/library/sqlite3.html#sqlite3.PARSE_DECLTYPES "sqlite3.PARSE_DECLTYPES") and [`PARSE_COLNAMES`](https://docs.python.org/3/library/sqlite3.html#sqlite3.PARSE_COLNAMES "sqlite3.PARSE_COLNAMES") to enable this. Column names take precedence over declared types if both flags are set. By default (`0`), type detection is disabled.
  * **isolation_level** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "str") _|__None_) – Control legacy transaction handling behaviour. See [`Connection.isolation_level`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.isolation_level "sqlite3.Connection.isolation_level") and [Transaction control via the isolation_level attribute](https://docs.python.org/3/library/sqlite3.html#sqlite3-transaction-control-isolation-level) for more information. Can be `"DEFERRED"` (default), `"EXCLUSIVE"` or `"IMMEDIATE"`; or `None` to disable opening transactions implicitly. Has no effect unless [`Connection.autocommit`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.autocommit "sqlite3.Connection.autocommit") is set to [`LEGACY_TRANSACTION_CONTROL`](https://docs.python.org/3/library/sqlite3.html#sqlite3.LEGACY_TRANSACTION_CONTROL "sqlite3.LEGACY_TRANSACTION_CONTROL") (the default).
  * **check_same_thread** ([_bool_](https://docs.python.org/3/library/functions.html#bool "bool")) – If `True` (default), [`ProgrammingError`](https://docs.python.org/3/library/sqlite3.html#sqlite3.ProgrammingError "sqlite3.ProgrammingError") will be raised if the database connection is used by a thread other than the one that created it. If `False`, the connection may be accessed in multiple threads; write operations may need to be serialized by the user to avoid data corruption. See [`threadsafety`](https://docs.python.org/3/library/sqlite3.html#sqlite3.threadsafety "sqlite3.threadsafety") for more information.
  * **factory** ([_Connection_](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection "sqlite3.Connection")) – A custom subclass of [`Connection`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection "sqlite3.Connection") to create the connection with, if not the default `Connection` class.
  * **cached_statements** ([_int_](https://docs.python.org/3/library/functions.html#int "int")) – The number of statements that `sqlite3` should internally cache for this connection, to avoid parsing overhead. By default, 128 statements.
  * **uri** ([_bool_](https://docs.python.org/3/library/functions.html#bool "bool")) – If set to `True`, _database_ is interpreted as a URI with a file path and an optional query string. The scheme part _must_ be `"file:"`, and the path can be relative or absolute. The query string allows passing parameters to SQLite, enabling various [How to work with SQLite URIs](https://docs.python.org/3/library/sqlite3.html#sqlite3-uri-tricks).
  * **autocommit** ([_bool_](https://docs.python.org/3/library/functions.html#bool "bool")) – Control [**PEP 249**](https://peps.python.org/pep-0249/) transaction handling behaviour. See [`Connection.autocommit`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.autocommit "sqlite3.Connection.autocommit") and [Transaction control via the autocommit attribute](https://docs.python.org/3/library/sqlite3.html#sqlite3-transaction-control-autocommit) for more information. _autocommit_ currently defaults to [`LEGACY_TRANSACTION_CONTROL`](https://docs.python.org/3/library/sqlite3.html#sqlite3.LEGACY_TRANSACTION_CONTROL "sqlite3.LEGACY_TRANSACTION_CONTROL"). The default will change to `False` in a future Python release.



Return type:

[_Connection_](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection "sqlite3.Connection")
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `sqlite3.connect` with argument `database`.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `sqlite3.connect/handle` with argument `connection_handle`.
Changed in version 3.4: Added the _uri_ parameter.
Changed in version 3.7: _database_ can now also be a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object), not only a string.
Changed in version 3.10: Added the `sqlite3.connect/handle` auditing event.
Changed in version 3.12: Added the _autocommit_ parameter.
Changed in version 3.13: Positional use of the parameters _timeout_ , _detect_types_ , _isolation_level_ , _check_same_thread_ , _factory_ , _cached_statements_ , and _uri_ is deprecated. They will become keyword-only parameters in Python 3.15.

sqlite3.complete_statement(_statement_)[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.complete_statement "Link to this definition")

Return `True` if the string _statement_ appears to contain one or more complete SQL statements. No syntactic verification or parsing of any kind is performed, other than checking that there are no unclosed string literals and the statement is terminated by a semicolon.
For example:
Copy```
>>> sqlite3.complete_statement("SELECT foo FROM bar;")
True
>>> sqlite3.complete_statement("SELECT foo")
False

```

This function may be useful during command-line input to determine if the entered text seems to form a complete SQL statement, or if additional input is needed before calling [`execute()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.execute "sqlite3.Cursor.execute").
See `runsource()` in

sqlite3.enable_callback_tracebacks(_flag_ , _/_)[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.enable_callback_tracebacks "Link to this definition")

Enable or disable callback tracebacks. By default you will not get any tracebacks in user-defined functions, aggregates, converters, authorizer callbacks etc. If you want to debug them, you can call this function with _flag_ set to `True`. Afterwards, you will get tracebacks from callbacks on [`sys.stderr`](https://docs.python.org/3/library/sys.html#sys.stderr "sys.stderr"). Use `False` to disable the feature again.
Note
Errors in user-defined function callbacks are logged as unraisable exceptions. Use an [`unraisable hook handler`](https://docs.python.org/3/library/sys.html#sys.unraisablehook "sys.unraisablehook") for introspection of the failed callback.

sqlite3.register_adapter(_type_ , _adapter_ , _/_)[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.register_adapter "Link to this definition")

Register an _adapter_ [callable](https://docs.python.org/3/glossary.html#term-callable) to adapt the Python type _type_ into an SQLite type. The adapter is called with a Python object of type _type_ as its sole argument, and must return a value of a [type that SQLite natively understands](https://docs.python.org/3/library/sqlite3.html#sqlite3-types).

sqlite3.register_converter(_typename_ , _converter_ , _/_)[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.register_converter "Link to this definition")

Register the _converter_ [callable](https://docs.python.org/3/glossary.html#term-callable) to convert SQLite objects of type _typename_ into a Python object of a specific type. The converter is invoked for all SQLite values of type _typename_ ; it is passed a [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") object and should return an object of the desired Python type. Consult the parameter _detect_types_ of [`connect()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.connect "sqlite3.connect") for information regarding how type detection works.
Note: _typename_ and the name of the type in your query are matched case-insensitively.
### Module constants[¶](https://docs.python.org/3/library/sqlite3.html#module-constants "Link to this heading")

sqlite3.LEGACY_TRANSACTION_CONTROL[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.LEGACY_TRANSACTION_CONTROL "Link to this definition")

Set [`autocommit`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.autocommit "sqlite3.Connection.autocommit") to this constant to select old style (pre-Python 3.12) transaction control behaviour. See [Transaction control via the isolation_level attribute](https://docs.python.org/3/library/sqlite3.html#sqlite3-transaction-control-isolation-level) for more information.

sqlite3.PARSE_DECLTYPES[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.PARSE_DECLTYPES "Link to this definition")

Pass this flag value to the _detect_types_ parameter of [`connect()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.connect "sqlite3.connect") to look up a converter function using the declared types for each column. The types are declared when the database table is created. `sqlite3` will look up a converter function using the first word of the declared type as the converter dictionary key. For example:
```
CREATE TABLE test(
   i integer primary key,  ! will look up a converter named "integer"
   p point,                ! will look up a converter named "point"
   n number(10)            ! will look up a converter named "number"
 )

```

This flag may be combined with [`PARSE_COLNAMES`](https://docs.python.org/3/library/sqlite3.html#sqlite3.PARSE_COLNAMES "sqlite3.PARSE_COLNAMES") using the `|` (bitwise or) operator.
Note
Generated fields (for example `MAX(p)`) are returned as [`str`](https://docs.python.org/3/library/stdtypes.html#str "str"). Use `PARSE_COLNAMES` to enforce types for such queries.

sqlite3.PARSE_COLNAMES[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.PARSE_COLNAMES "Link to this definition")

Pass this flag value to the _detect_types_ parameter of [`connect()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.connect "sqlite3.connect") to look up a converter function by using the type name, parsed from the query column name, as the converter dictionary key. The query column name must be wrapped in double quotes (`"`) and the type name must be wrapped in square brackets (`[]`).
```
SELECT MAX(p) as "p [point]" FROM test;  ! will look up converter "point"

```

This flag may be combined with [`PARSE_DECLTYPES`](https://docs.python.org/3/library/sqlite3.html#sqlite3.PARSE_DECLTYPES "sqlite3.PARSE_DECLTYPES") using the `|` (bitwise or) operator.

sqlite3.SQLITE_OK[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.SQLITE_OK "Link to this definition")


sqlite3.SQLITE_DENY[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.SQLITE_DENY "Link to this definition")


sqlite3.SQLITE_IGNORE[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.SQLITE_IGNORE "Link to this definition")

Flags that should be returned by the _authorizer_callback_ [callable](https://docs.python.org/3/glossary.html#term-callable) passed to [`Connection.set_authorizer()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.set_authorizer "sqlite3.Connection.set_authorizer"), to indicate whether:
  * Access is allowed (`SQLITE_OK`),
  * The SQL statement should be aborted with an error (`SQLITE_DENY`)
  * The column should be treated as a `NULL` value (`SQLITE_IGNORE`)



sqlite3.apilevel[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.apilevel "Link to this definition")

String constant stating the supported DB-API level. Required by the DB-API. Hard-coded to `"2.0"`.

sqlite3.paramstyle[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.paramstyle "Link to this definition")

String constant stating the type of parameter marker formatting expected by the `sqlite3` module. Required by the DB-API. Hard-coded to `"qmark"`.
Note
The `named` DB-API parameter style is also supported.

sqlite3.sqlite_version[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.sqlite_version "Link to this definition")

Version number of the runtime SQLite library as a [`string`](https://docs.python.org/3/library/stdtypes.html#str "str").

sqlite3.sqlite_version_info[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.sqlite_version_info "Link to this definition")

Version number of the runtime SQLite library as a [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "tuple") of [`integers`](https://docs.python.org/3/library/functions.html#int "int").

sqlite3.threadsafety[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.threadsafety "Link to this definition")

Integer constant required by the DB-API 2.0, stating the level of thread safety the `sqlite3` module supports. This attribute is set based on the default
  1. **Single-thread** : In this mode, all mutexes are disabled and SQLite is unsafe to use in more than a single thread at once.
  2. **Multi-thread** : In this mode, SQLite can be safely used by multiple threads provided that no single database connection is used simultaneously in two or more threads.
  3. **Serialized** : In serialized mode, SQLite can be safely used by multiple threads with no restriction.


The mappings from SQLite threading modes to DB-API 2.0 threadsafety levels are as follows:
SQLite threading mode | [**threadsafety**](https://peps.python.org/pep-0249/#threadsafety) |  | DB-API 2.0 meaning
---|---|---|---
single-thread | 0 | 0 | Threads may not share the module
multi-thread | 1 | 2 | Threads may share the module, but not connections
serialized | 3 | 1 | Threads may share the module, connections and cursors
Changed in version 3.11: Set _threadsafety_ dynamically instead of hard-coding it to `1`.

sqlite3.SQLITE_DBCONFIG_DEFENSIVE[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.SQLITE_DBCONFIG_DEFENSIVE "Link to this definition")


sqlite3.SQLITE_DBCONFIG_DQS_DDL[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.SQLITE_DBCONFIG_DQS_DDL "Link to this definition")


sqlite3.SQLITE_DBCONFIG_DQS_DML[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.SQLITE_DBCONFIG_DQS_DML "Link to this definition")


sqlite3.SQLITE_DBCONFIG_ENABLE_FKEY[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.SQLITE_DBCONFIG_ENABLE_FKEY "Link to this definition")


sqlite3.SQLITE_DBCONFIG_ENABLE_FTS3_TOKENIZER[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.SQLITE_DBCONFIG_ENABLE_FTS3_TOKENIZER "Link to this definition")


sqlite3.SQLITE_DBCONFIG_ENABLE_LOAD_EXTENSION[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.SQLITE_DBCONFIG_ENABLE_LOAD_EXTENSION "Link to this definition")


sqlite3.SQLITE_DBCONFIG_ENABLE_QPSG[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.SQLITE_DBCONFIG_ENABLE_QPSG "Link to this definition")


sqlite3.SQLITE_DBCONFIG_ENABLE_TRIGGER[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.SQLITE_DBCONFIG_ENABLE_TRIGGER "Link to this definition")


sqlite3.SQLITE_DBCONFIG_ENABLE_VIEW[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.SQLITE_DBCONFIG_ENABLE_VIEW "Link to this definition")


sqlite3.SQLITE_DBCONFIG_LEGACY_ALTER_TABLE[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.SQLITE_DBCONFIG_LEGACY_ALTER_TABLE "Link to this definition")


sqlite3.SQLITE_DBCONFIG_LEGACY_FILE_FORMAT[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.SQLITE_DBCONFIG_LEGACY_FILE_FORMAT "Link to this definition")


sqlite3.SQLITE_DBCONFIG_NO_CKPT_ON_CLOSE[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.SQLITE_DBCONFIG_NO_CKPT_ON_CLOSE "Link to this definition")


sqlite3.SQLITE_DBCONFIG_RESET_DATABASE[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.SQLITE_DBCONFIG_RESET_DATABASE "Link to this definition")


sqlite3.SQLITE_DBCONFIG_TRIGGER_EQP[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.SQLITE_DBCONFIG_TRIGGER_EQP "Link to this definition")


sqlite3.SQLITE_DBCONFIG_TRUSTED_SCHEMA[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.SQLITE_DBCONFIG_TRUSTED_SCHEMA "Link to this definition")


sqlite3.SQLITE_DBCONFIG_WRITABLE_SCHEMA[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.SQLITE_DBCONFIG_WRITABLE_SCHEMA "Link to this definition")

These constants are used for the [`Connection.setconfig()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.setconfig "sqlite3.Connection.setconfig") and [`getconfig()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.getconfig "sqlite3.Connection.getconfig") methods.
The availability of these constants varies depending on the version of SQLite Python was compiled with.
Added in version 3.12.
See also
SQLite docs: Database Connection Configuration Options
Deprecated since version 3.12, removed in version 3.14: The `version` and `version_info` constants.
### Connection objects[¶](https://docs.python.org/3/library/sqlite3.html#connection-objects "Link to this heading")

_class_ sqlite3.Connection[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection "Link to this definition")

Each open SQLite database is represented by a `Connection` object, which is created using [`sqlite3.connect()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.connect "sqlite3.connect"). Their main purpose is creating [`Cursor`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor "sqlite3.Cursor") objects, and [Transaction control](https://docs.python.org/3/library/sqlite3.html#sqlite3-controlling-transactions).
See also
  * [How to use connection shortcut methods](https://docs.python.org/3/library/sqlite3.html#sqlite3-connection-shortcuts)
  * [How to use the connection context manager](https://docs.python.org/3/library/sqlite3.html#sqlite3-connection-context-manager)


Changed in version 3.13: A [`ResourceWarning`](https://docs.python.org/3/library/exceptions.html#ResourceWarning "ResourceWarning") is emitted if [`close()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.close "sqlite3.Connection.close") is not called before a `Connection` object is deleted.
An SQLite database connection has the following attributes and methods:

cursor(_factory =Cursor_)[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.cursor "Link to this definition")

Create and return a [`Cursor`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor "sqlite3.Cursor") object. The cursor method accepts a single optional parameter _factory_. If supplied, this must be a [callable](https://docs.python.org/3/glossary.html#term-callable) returning an instance of `Cursor` or its subclasses.

blobopen(_table_ , _column_ , _rowid_ , _/_ , _*_ , _readonly =False_, _name ='main'_)[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.blobopen "Link to this definition")

Open a [`Blob`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Blob "sqlite3.Blob") handle to an existing BLOB.

Parameters:

  * **table** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "str")) – The name of the table where the blob is located.
  * **column** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "str")) – The name of the column where the blob is located.
  * **rowid** ([_int_](https://docs.python.org/3/library/functions.html#int "int")) – The row id where the blob is located.
  * **readonly** ([_bool_](https://docs.python.org/3/library/functions.html#bool "bool")) – Set to `True` if the blob should be opened without write permissions. Defaults to `False`.
  * **name** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "str")) – The name of the database where the blob is located. Defaults to `"main"`.



Raises:

[**OperationalError**](https://docs.python.org/3/library/sqlite3.html#sqlite3.OperationalError "sqlite3.OperationalError") – When trying to open a blob in a `WITHOUT ROWID` table.

Return type:

[Blob](https://docs.python.org/3/library/sqlite3.html#sqlite3.Blob "sqlite3.Blob")
Note
The blob size cannot be changed using the [`Blob`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Blob "sqlite3.Blob") class. Use the SQL function `zeroblob` to create a blob with a fixed size.
Added in version 3.11.

commit()[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.commit "Link to this definition")

Commit any pending transaction to the database. If [`autocommit`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.autocommit "sqlite3.Connection.autocommit") is `True`, or there is no open transaction, this method does nothing. If `autocommit` is `False`, a new transaction is implicitly opened if a pending transaction was committed by this method.

rollback()[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.rollback "Link to this definition")

Roll back to the start of any pending transaction. If [`autocommit`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.autocommit "sqlite3.Connection.autocommit") is `True`, or there is no open transaction, this method does nothing. If `autocommit` is `False`, a new transaction is implicitly opened if a pending transaction was rolled back by this method.

close()[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.close "Link to this definition")

Close the database connection. If [`autocommit`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.autocommit "sqlite3.Connection.autocommit") is `False`, any pending transaction is implicitly rolled back. If `autocommit` is `True` or [`LEGACY_TRANSACTION_CONTROL`](https://docs.python.org/3/library/sqlite3.html#sqlite3.LEGACY_TRANSACTION_CONTROL "sqlite3.LEGACY_TRANSACTION_CONTROL"), no implicit transaction control is executed. Make sure to [`commit()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.commit "sqlite3.Connection.commit") before closing to avoid losing pending changes.

execute(_sql_ , _parameters =()_, _/_)[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.execute "Link to this definition")

Create a new [`Cursor`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor "sqlite3.Cursor") object and call [`execute()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.execute "sqlite3.Cursor.execute") on it with the given _sql_ and _parameters_. Return the new cursor object.

executemany(_sql_ , _parameters_ , _/_)[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.executemany "Link to this definition")

Create a new [`Cursor`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor "sqlite3.Cursor") object and call [`executemany()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.executemany "sqlite3.Cursor.executemany") on it with the given _sql_ and _parameters_. Return the new cursor object.

executescript(_sql_script_ , _/_)[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.executescript "Link to this definition")

Create a new [`Cursor`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor "sqlite3.Cursor") object and call [`executescript()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.executescript "sqlite3.Cursor.executescript") on it with the given _sql_script_. Return the new cursor object.

create_function(_name_ , _narg_ , _func_ , _*_ , _deterministic =False_)[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.create_function "Link to this definition")

Create or remove a user-defined SQL function.

Parameters:

  * **name** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "str")) – The name of the SQL function.
  * **narg** ([_int_](https://docs.python.org/3/library/functions.html#int "int")) – The number of arguments the SQL function can accept. If `-1`, it may take any number of arguments.
  * **func** ([callback](https://docs.python.org/3/glossary.html#term-callback) | None) – A [callable](https://docs.python.org/3/glossary.html#term-callable) that is called when the SQL function is invoked. The callable must return [a type natively supported by SQLite](https://docs.python.org/3/library/sqlite3.html#sqlite3-types). Set to `None` to remove an existing SQL function.
  * **deterministic** ([_bool_](https://docs.python.org/3/library/functions.html#bool "bool")) – If `True`, the created SQL function is marked as


Changed in version 3.8: Added the _deterministic_ parameter.
Example:
Copy```
>>> import hashlib
>>> def md5sum(t):
...     return hashlib.md5(t).hexdigest()
>>> con = sqlite3.connect(":memory:")
>>> con.create_function("md5", 1, md5sum)
>>> for row in con.execute("SELECT md5(?)", (b"foo",)):
...     print(row)
('acbd18db4cc2f85cedef654fccc4a4d8',)
>>> con.close()

```

Changed in version 3.13: Passing _name_ , _narg_ , and _func_ as keyword arguments is deprecated. These parameters will become positional-only in Python 3.15.

create_aggregate(_name_ , _n_arg_ , _aggregate_class_)[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.create_aggregate "Link to this definition")

Create or remove a user-defined SQL aggregate function.

Parameters:

  * **name** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "str")) – The name of the SQL aggregate function.
  * **n_arg** ([_int_](https://docs.python.org/3/library/functions.html#int "int")) – The number of arguments the SQL aggregate function can accept. If `-1`, it may take any number of arguments.
  * **aggregate_class** ([class](https://docs.python.org/3/glossary.html#term-class) | None) –
A class must implement the following methods:
    * `step()`: Add a row to the aggregate.
    * `finalize()`: Return the final result of the aggregate as [a type natively supported by SQLite](https://docs.python.org/3/library/sqlite3.html#sqlite3-types).
The number of arguments that the `step()` method must accept is controlled by _n_arg_.
Set to `None` to remove an existing SQL aggregate function.


Example:
Copy```
class MySum:
    def __init__(self):
        self.count = 0

    def step(self, value):
        self.count += value

    def finalize(self):
        return self.count

con = sqlite3.connect(":memory:")
con.create_aggregate("mysum", 1, MySum)
cur = con.execute("CREATE TABLE test(i)")
cur.execute("INSERT INTO test(i) VALUES(1)")
cur.execute("INSERT INTO test(i) VALUES(2)")
cur.execute("SELECT mysum(i) FROM test")
print(cur.fetchone()[0])

con.close()

```

Changed in version 3.13: Passing _name_ , _n_arg_ , and _aggregate_class_ as keyword arguments is deprecated. These parameters will become positional-only in Python 3.15.

create_window_function(_name_ , _num_params_ , _aggregate_class_ , _/_)[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.create_window_function "Link to this definition")

Create or remove a user-defined aggregate window function.

Parameters:

  * **name** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "str")) – The name of the SQL aggregate window function to create or remove.
  * **num_params** ([_int_](https://docs.python.org/3/library/functions.html#int "int")) – The number of arguments the SQL aggregate window function can accept. If `-1`, it may take any number of arguments.
  * **aggregate_class** ([class](https://docs.python.org/3/glossary.html#term-class) | None) –
A class that must implement the following methods:
    * `step()`: Add a row to the current window.
    * `value()`: Return the current value of the aggregate.
    * `inverse()`: Remove a row from the current window.
    * `finalize()`: Return the final result of the aggregate as [a type natively supported by SQLite](https://docs.python.org/3/library/sqlite3.html#sqlite3-types).
The number of arguments that the `step()` and `value()` methods must accept is controlled by _num_params_.
Set to `None` to remove an existing SQL aggregate window function.



Raises:

[**NotSupportedError**](https://docs.python.org/3/library/sqlite3.html#sqlite3.NotSupportedError "sqlite3.NotSupportedError") – If used with a version of SQLite older than 3.25.0, which does not support aggregate window functions.
Added in version 3.11.
Example:
Copy```
