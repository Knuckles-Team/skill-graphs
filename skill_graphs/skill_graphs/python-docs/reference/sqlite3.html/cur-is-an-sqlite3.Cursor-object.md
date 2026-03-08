# cur is an sqlite3.Cursor object
cur.executescript("""
    BEGIN;
    CREATE TABLE person(firstname, lastname, age);
    CREATE TABLE book(title, author, published);
    CREATE TABLE publisher(name, address);
    COMMIT;
""")

```


fetchone()[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.fetchone "Link to this definition")

If [`row_factory`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.row_factory "sqlite3.Cursor.row_factory") is `None`, return the next row query result set as a [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "tuple"). Else, pass it to the row factory and return its result. Return `None` if no more data is available.

fetchmany(_size =cursor.arraysize_)[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.fetchmany "Link to this definition")

Return the next set of rows of a query result as a [`list`](https://docs.python.org/3/library/stdtypes.html#list "list"). Return an empty list if no more rows are available.
The number of rows to fetch per call is specified by the _size_ parameter. If _size_ is not given, [`arraysize`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.arraysize "sqlite3.Cursor.arraysize") determines the number of rows to be fetched. If fewer than _size_ rows are available, as many rows as are available are returned.
Note there are performance considerations involved with the _size_ parameter. For optimal performance, it is usually best to use the arraysize attribute. If the _size_ parameter is used, then it is best for it to retain the same value from one `fetchmany()` call to the next.
Changed in version 3.14.1: Negative _size_ values are rejected by raising [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError").

fetchall()[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.fetchall "Link to this definition")

Return all (remaining) rows of a query result as a [`list`](https://docs.python.org/3/library/stdtypes.html#list "list"). Return an empty list if no rows are available. Note that the [`arraysize`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.arraysize "sqlite3.Cursor.arraysize") attribute can affect the performance of this operation.

close()[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.close "Link to this definition")

Close the cursor now (rather than whenever `__del__` is called).
The cursor will be unusable from this point forward; a [`ProgrammingError`](https://docs.python.org/3/library/sqlite3.html#sqlite3.ProgrammingError "sqlite3.ProgrammingError") exception will be raised if any operation is attempted with the cursor.

setinputsizes(_sizes_ , _/_)[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.setinputsizes "Link to this definition")

Required by the DB-API. Does nothing in `sqlite3`.

setoutputsize(_size_ , _column =None_, _/_)[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.setoutputsize "Link to this definition")

Required by the DB-API. Does nothing in `sqlite3`.

arraysize[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.arraysize "Link to this definition")

Read/write attribute that controls the number of rows returned by [`fetchmany()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.fetchmany "sqlite3.Cursor.fetchmany"). The default value is 1 which means a single row would be fetched per call.
Changed in version 3.14.1: Negative values are rejected by raising [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError").

connection[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.connection "Link to this definition")

Read-only attribute that provides the SQLite database [`Connection`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection "sqlite3.Connection") belonging to the cursor. A `Cursor` object created by calling [`con.cursor()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.cursor "sqlite3.Connection.cursor") will have a [`connection`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.connection "sqlite3.Cursor.connection") attribute that refers to _con_ :
Copy```
>>> con = sqlite3.connect(":memory:")
>>> cur = con.cursor()
>>> cur.connection == con
True
>>> con.close()

```


description[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.description "Link to this definition")

Read-only attribute that provides the column names of the last query. To remain compatible with the Python DB API, it returns a 7-tuple for each column where the last six items of each tuple are `None`.
It is set for `SELECT` statements without any matching rows as well.

lastrowid[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.lastrowid "Link to this definition")

Read-only attribute that provides the row id of the last inserted row. It is only updated after successful `INSERT` or `REPLACE` statements using the [`execute()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.execute "sqlite3.Cursor.execute") method. For other statements, after [`executemany()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.executemany "sqlite3.Cursor.executemany") or [`executescript()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.executescript "sqlite3.Cursor.executescript"), or if the insertion failed, the value of `lastrowid` is left unchanged. The initial value of `lastrowid` is `None`.
Note
Inserts into `WITHOUT ROWID` tables are not recorded.
Changed in version 3.6: Added support for the `REPLACE` statement.

rowcount[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.rowcount "Link to this definition")

Read-only attribute that provides the number of modified rows for `INSERT`, `UPDATE`, `DELETE`, and `REPLACE` statements; is `-1` for other statements, including CTE queries. It is only updated by the [`execute()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.execute "sqlite3.Cursor.execute") and [`executemany()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.executemany "sqlite3.Cursor.executemany") methods, after the statement has run to completion. This means that any resulting rows must be fetched in order for `rowcount` to be updated.

row_factory[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.row_factory "Link to this definition")

Control how a row fetched from this `Cursor` is represented. If `None`, a row is represented as a [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "tuple"). Can be set to the included [`sqlite3.Row`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Row "sqlite3.Row"); or a [callable](https://docs.python.org/3/glossary.html#term-callable) that accepts two arguments, a `Cursor` object and the `tuple` of row values, and returns a custom object representing an SQLite row.
Defaults to what [`Connection.row_factory`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.row_factory "sqlite3.Connection.row_factory") was set to when the `Cursor` was created. Assigning to this attribute does not affect `Connection.row_factory` of the parent connection.
See [How to create and use row factories](https://docs.python.org/3/library/sqlite3.html#sqlite3-howto-row-factory) for more details.
### Row objects[¶](https://docs.python.org/3/library/sqlite3.html#row-objects "Link to this heading")

_class_ sqlite3.Row[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Row "Link to this definition")

A `Row` instance serves as a highly optimized [`row_factory`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.row_factory "sqlite3.Connection.row_factory") for [`Connection`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection "sqlite3.Connection") objects. It supports iteration, equality testing, [`len()`](https://docs.python.org/3/library/functions.html#len "len"), and [mapping](https://docs.python.org/3/glossary.html#term-mapping) access by column name and index.
Two `Row` objects compare equal if they have identical column names and values.
See [How to create and use row factories](https://docs.python.org/3/library/sqlite3.html#sqlite3-howto-row-factory) for more details.

keys()[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Row.keys "Link to this definition")

Return a [`list`](https://docs.python.org/3/library/stdtypes.html#list "list") of column names as [`strings`](https://docs.python.org/3/library/stdtypes.html#str "str"). Immediately after a query, it is the first member of each tuple in [`Cursor.description`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.description "sqlite3.Cursor.description").
Changed in version 3.5: Added support of slicing.
### Blob objects[¶](https://docs.python.org/3/library/sqlite3.html#blob-objects "Link to this heading")

_class_ sqlite3.Blob[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Blob "Link to this definition")

Added in version 3.11.
A `Blob` instance is a [file-like object](https://docs.python.org/3/glossary.html#term-file-like-object) that can read and write data in an SQLite BLOB. Call [`len(blob)`](https://docs.python.org/3/library/functions.html#len "len") to get the size (number of bytes) of the blob. Use indices and [slices](https://docs.python.org/3/glossary.html#term-slice) for direct access to the blob data.
Use the `Blob` as a [context manager](https://docs.python.org/3/glossary.html#term-context-manager) to ensure that the blob handle is closed after use.
Copy```
con = sqlite3.connect(":memory:")
con.execute("CREATE TABLE test(blob_col blob)")
con.execute("INSERT INTO test(blob_col) VALUES(zeroblob(13))")
