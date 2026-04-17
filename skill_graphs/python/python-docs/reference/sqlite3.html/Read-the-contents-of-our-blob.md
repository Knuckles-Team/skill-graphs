# Read the contents of our blob
with con.blobopen("test", "blob_col", 1) as blob:
    greeting = blob.read()

print(greeting)  # outputs "b'Hello, world!'"
con.close()

```


close()[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Blob.close "Link to this definition")

Close the blob.
The blob will be unusable from this point onward. An [`Error`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Error "sqlite3.Error") (or subclass) exception will be raised if any further operation is attempted with the blob.

read(_length =-1_, _/_)[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Blob.read "Link to this definition")

Read _length_ bytes of data from the blob at the current offset position. If the end of the blob is reached, the data up to EOF will be returned. When _length_ is not specified, or is negative, `read()` will read until the end of the blob.

write(_data_ , _/_)[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Blob.write "Link to this definition")

Write _data_ to the blob at the current offset. This function cannot change the blob length. Writing beyond the end of the blob will raise [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError").

tell()[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Blob.tell "Link to this definition")

Return the current access position of the blob.

seek(_offset_ , _origin =os.SEEK_SET_, _/_)[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Blob.seek "Link to this definition")

Set the current access position of the blob to _offset_. The _origin_ argument defaults to [`os.SEEK_SET`](https://docs.python.org/3/library/os.html#os.SEEK_SET "os.SEEK_SET") (absolute blob positioning). Other values for _origin_ are [`os.SEEK_CUR`](https://docs.python.org/3/library/os.html#os.SEEK_CUR "os.SEEK_CUR") (seek relative to the current position) and [`os.SEEK_END`](https://docs.python.org/3/library/os.html#os.SEEK_END "os.SEEK_END") (seek relative to the blob’s end).
### PrepareProtocol objects[¶](https://docs.python.org/3/library/sqlite3.html#prepareprotocol-objects "Link to this heading")

_class_ sqlite3.PrepareProtocol[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.PrepareProtocol "Link to this definition")

The PrepareProtocol type’s single purpose is to act as a [**PEP 246**](https://peps.python.org/pep-0246/) style adaption protocol for objects that can [adapt themselves](https://docs.python.org/3/library/sqlite3.html#sqlite3-conform) to [native SQLite types](https://docs.python.org/3/library/sqlite3.html#sqlite3-types).
### Exceptions[¶](https://docs.python.org/3/library/sqlite3.html#exceptions "Link to this heading")
The exception hierarchy is defined by the DB-API 2.0 ([**PEP 249**](https://peps.python.org/pep-0249/)).

_exception_ sqlite3.Warning[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Warning "Link to this definition")

This exception is not currently raised by the `sqlite3` module, but may be raised by applications using `sqlite3`, for example if a user-defined function truncates data while inserting. `Warning` is a subclass of [`Exception`](https://docs.python.org/3/library/exceptions.html#Exception "Exception").

_exception_ sqlite3.Error[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Error "Link to this definition")

The base class of the other exceptions in this module. Use this to catch all errors with one single [`except`](https://docs.python.org/3/reference/compound_stmts.html#except) statement. `Error` is a subclass of [`Exception`](https://docs.python.org/3/library/exceptions.html#Exception "Exception").
If the exception originated from within the SQLite library, the following two attributes are added to the exception:

sqlite_errorcode[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Error.sqlite_errorcode "Link to this definition")

The numeric error code from the
Added in version 3.11.

sqlite_errorname[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Error.sqlite_errorname "Link to this definition")

The symbolic name of the numeric error code from the
Added in version 3.11.

_exception_ sqlite3.InterfaceError[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.InterfaceError "Link to this definition")

Exception raised for misuse of the low-level SQLite C API. In other words, if this exception is raised, it probably indicates a bug in the `sqlite3` module. `InterfaceError` is a subclass of [`Error`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Error "sqlite3.Error").

_exception_ sqlite3.DatabaseError[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.DatabaseError "Link to this definition")

Exception raised for errors that are related to the database. This serves as the base exception for several types of database errors. It is only raised implicitly through the specialised subclasses. `DatabaseError` is a subclass of [`Error`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Error "sqlite3.Error").

_exception_ sqlite3.DataError[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.DataError "Link to this definition")

Exception raised for errors caused by problems with the processed data, like numeric values out of range, and strings which are too long. `DataError` is a subclass of [`DatabaseError`](https://docs.python.org/3/library/sqlite3.html#sqlite3.DatabaseError "sqlite3.DatabaseError").

_exception_ sqlite3.OperationalError[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.OperationalError "Link to this definition")

Exception raised for errors that are related to the database’s operation, and not necessarily under the control of the programmer. For example, the database path is not found, or a transaction could not be processed. `OperationalError` is a subclass of [`DatabaseError`](https://docs.python.org/3/library/sqlite3.html#sqlite3.DatabaseError "sqlite3.DatabaseError").

_exception_ sqlite3.IntegrityError[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.IntegrityError "Link to this definition")

Exception raised when the relational integrity of the database is affected, e.g. a foreign key check fails. It is a subclass of [`DatabaseError`](https://docs.python.org/3/library/sqlite3.html#sqlite3.DatabaseError "sqlite3.DatabaseError").

_exception_ sqlite3.InternalError[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.InternalError "Link to this definition")

Exception raised when SQLite encounters an internal error. If this is raised, it may indicate that there is a problem with the runtime SQLite library. `InternalError` is a subclass of [`DatabaseError`](https://docs.python.org/3/library/sqlite3.html#sqlite3.DatabaseError "sqlite3.DatabaseError").

_exception_ sqlite3.ProgrammingError[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.ProgrammingError "Link to this definition")

Exception raised for `sqlite3` API programming errors, for example supplying the wrong number of bindings to a query, or trying to operate on a closed [`Connection`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection "sqlite3.Connection"). `ProgrammingError` is a subclass of [`DatabaseError`](https://docs.python.org/3/library/sqlite3.html#sqlite3.DatabaseError "sqlite3.DatabaseError").

_exception_ sqlite3.NotSupportedError[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.NotSupportedError "Link to this definition")

Exception raised in case a method or database API is not supported by the underlying SQLite library. For example, setting _deterministic_ to `True` in [`create_function()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.create_function "sqlite3.Connection.create_function"), if the underlying SQLite library does not support deterministic functions. `NotSupportedError` is a subclass of [`DatabaseError`](https://docs.python.org/3/library/sqlite3.html#sqlite3.DatabaseError "sqlite3.DatabaseError").
### SQLite and Python types[¶](https://docs.python.org/3/library/sqlite3.html#sqlite-and-python-types "Link to this heading")
SQLite natively supports the following types: `NULL`, `INTEGER`, `REAL`, `TEXT`, `BLOB`.
The following Python types can thus be sent to SQLite without any problem:
Python type | SQLite type
---|---
`None` | `NULL`
[`int`](https://docs.python.org/3/library/functions.html#int "int") | `INTEGER`
[`float`](https://docs.python.org/3/library/functions.html#float "float") | `REAL`
[`str`](https://docs.python.org/3/library/stdtypes.html#str "str") | `TEXT`
[`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") | `BLOB`
This is how SQLite types are converted to Python types by default:
SQLite type | Python type
---|---
`NULL` | `None`
`INTEGER` | [`int`](https://docs.python.org/3/library/functions.html#int "int")
`REAL` | [`float`](https://docs.python.org/3/library/functions.html#float "float")
`TEXT` | depends on [`text_factory`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.text_factory "sqlite3.Connection.text_factory"), [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") by default
`BLOB` | [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes")
The type system of the `sqlite3` module is extensible in two ways: you can store additional Python types in an SQLite database via [object adapters](https://docs.python.org/3/library/sqlite3.html#sqlite3-adapters), and you can let the `sqlite3` module convert SQLite types to Python types via [converters](https://docs.python.org/3/library/sqlite3.html#sqlite3-converters).
### Default adapters and converters (deprecated)[¶](https://docs.python.org/3/library/sqlite3.html#default-adapters-and-converters-deprecated "Link to this heading")
Note
The default adapters and converters are deprecated as of Python 3.12. Instead, use the [Adapter and converter recipes](https://docs.python.org/3/library/sqlite3.html#sqlite3-adapter-converter-recipes) and tailor them to your needs.
The deprecated default adapters and converters consist of:
  * An adapter for [`datetime.date`](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date") objects to [`strings`](https://docs.python.org/3/library/stdtypes.html#str "str") in
  * An adapter for [`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") objects to strings in ISO 8601 format.
  * A converter for [declared](https://docs.python.org/3/library/sqlite3.html#sqlite3-converters) “date” types to [`datetime.date`](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date") objects.
  * A converter for declared “timestamp” types to [`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") objects. Fractional parts will be truncated to 6 digits (microsecond precision).


Note
The default “timestamp” converter ignores UTC offsets in the database and always returns a naive [`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") object. To preserve UTC offsets in timestamps, either leave converters disabled, or register an offset-aware converter with [`register_converter()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.register_converter "sqlite3.register_converter").
Deprecated since version 3.12.
### Command-line interface[¶](https://docs.python.org/3/library/sqlite3.html#command-line-interface "Link to this heading")
The `sqlite3` module can be invoked as a script, using the interpreter’s [`-m`](https://docs.python.org/3/using/cmdline.html#cmdoption-m) switch, in order to provide a simple SQLite shell. The argument signature is as follows:
Copy```
python -m sqlite3 [-h] [-v] [filename] [sql]

```

Type `.quit` or CTRL-D to exit the shell.

-h, --help[¶](https://docs.python.org/3/library/sqlite3.html#cmdoption-python-m-sqlite3-h-v-filename-sql-h "Link to this definition")

Print CLI help.

-v, --version[¶](https://docs.python.org/3/library/sqlite3.html#cmdoption-python-m-sqlite3-h-v-filename-sql-v "Link to this definition")

Print underlying SQLite library version.
Added in version 3.12.
## How-to guides[¶](https://docs.python.org/3/library/sqlite3.html#how-to-guides "Link to this heading")
### How to use placeholders to bind values in SQL queries[¶](https://docs.python.org/3/library/sqlite3.html#how-to-use-placeholders-to-bind-values-in-sql-queries "Link to this heading")
SQL operations usually need to use values from Python variables. However, beware of using Python’s string operations to assemble queries, as they are vulnerable to `OR TRUE` to select all rows:
Copy```
>>> # Never do this -- insecure!
>>> symbol = input()
' OR TRUE; --
>>> sql = "SELECT * FROM stocks WHERE symbol = '%s'" % symbol
>>> print(sql)
SELECT * FROM stocks WHERE symbol = '' OR TRUE; --'
>>> cur.execute(sql)

```

Instead, use the DB-API’s parameter substitution. To insert a variable into a query string, use a placeholder in the string, and substitute the actual values into the query by providing them as a [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "tuple") of values to the second argument of the cursor’s [`execute()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.execute "sqlite3.Cursor.execute") method.
An SQL statement may use one of two kinds of placeholders: question marks (qmark style) or named placeholders (named style). For the qmark style, _parameters_ must be a [sequence](https://docs.python.org/3/glossary.html#term-sequence) whose length must match the number of placeholders, or a [`ProgrammingError`](https://docs.python.org/3/library/sqlite3.html#sqlite3.ProgrammingError "sqlite3.ProgrammingError") is raised. For the named style, _parameters_ must be an instance of a [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict") (or a subclass), which must contain keys for all named parameters; any extra items are ignored. Here’s an example of both styles:
Copy```
con = sqlite3.connect(":memory:")
cur = con.execute("CREATE TABLE lang(name, first_appeared)")

# This is the named style used with executemany():
data = (
    {"name": "C", "year": 1972},
    {"name": "Fortran", "year": 1957},
    {"name": "Python", "year": 1991},
    {"name": "Go", "year": 2009},
)
cur.executemany("INSERT INTO lang VALUES(:name, :year)", data)

# This is the qmark style used in a SELECT query:
params = (1972,)
cur.execute("SELECT * FROM lang WHERE first_appeared = ?", params)
print(cur.fetchall())
con.close()

```

Note
[**PEP 249**](https://peps.python.org/pep-0249/) numeric placeholders are _not_ supported. If used, they will be interpreted as named placeholders.
### How to adapt custom Python types to SQLite values[¶](https://docs.python.org/3/library/sqlite3.html#how-to-adapt-custom-python-types-to-sqlite-values "Link to this heading")
SQLite supports only a limited set of data types natively. To store custom Python types in SQLite databases, _adapt_ them to one of the [Python types SQLite natively understands](https://docs.python.org/3/library/sqlite3.html#sqlite3-types).
There are two ways to adapt Python objects to SQLite types: letting your object adapt itself, or using an _adapter callable_. The latter will take precedence above the former. For a library that exports a custom type, it may make sense to enable that type to adapt itself. As an application developer, it may make more sense to take direct control by registering custom adapter functions.
#### How to write adaptable objects[¶](https://docs.python.org/3/library/sqlite3.html#how-to-write-adaptable-objects "Link to this heading")
Suppose we have a `Point` class that represents a pair of coordinates, `x` and `y`, in a Cartesian coordinate system. The coordinate pair will be stored as a text string in the database, using a semicolon to separate the coordinates. This can be implemented by adding a `__conform__(self, protocol)` method which returns the adapted value. The object passed to _protocol_ will be of type [`PrepareProtocol`](https://docs.python.org/3/library/sqlite3.html#sqlite3.PrepareProtocol "sqlite3.PrepareProtocol").
Copy```
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __conform__(self, protocol):
        if protocol is sqlite3.PrepareProtocol:
            return f"{self.x};{self.y}"

con = sqlite3.connect(":memory:")
cur = con.cursor()

cur.execute("SELECT ?", (Point(4.0, -3.2),))
print(cur.fetchone()[0])
con.close()

```

#### How to register adapter callables[¶](https://docs.python.org/3/library/sqlite3.html#how-to-register-adapter-callables "Link to this heading")
The other possibility is to create a function that converts the Python object to an SQLite-compatible type. This function can then be registered using [`register_adapter()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.register_adapter "sqlite3.register_adapter").
Copy```
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

def adapt_point(point):
    return f"{point.x};{point.y}"

sqlite3.register_adapter(Point, adapt_point)

con = sqlite3.connect(":memory:")
cur = con.cursor()

cur.execute("SELECT ?", (Point(1.0, 2.5),))
print(cur.fetchone()[0])
con.close()

```

### How to convert SQLite values to custom Python types[¶](https://docs.python.org/3/library/sqlite3.html#how-to-convert-sqlite-values-to-custom-python-types "Link to this heading")
Writing an adapter lets you convert _from_ custom Python types _to_ SQLite values. To be able to convert _from_ SQLite values _to_ custom Python types, we use _converters_.
Let’s go back to the `Point` class. We stored the x and y coordinates separated via semicolons as strings in SQLite.
First, we’ll define a converter function that accepts the string as a parameter and constructs a `Point` object from it.
Note
Converter functions are **always** passed a [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") object, no matter the underlying SQLite data type.
Copy```
def convert_point(s):
    x, y = map(float, s.split(b";"))
    return Point(x, y)

```

We now need to tell `sqlite3` when it should convert a given SQLite value. This is done when connecting to a database, using the _detect_types_ parameter of [`connect()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.connect "sqlite3.connect"). There are three options:
  * Implicit: set _detect_types_ to [`PARSE_DECLTYPES`](https://docs.python.org/3/library/sqlite3.html#sqlite3.PARSE_DECLTYPES "sqlite3.PARSE_DECLTYPES")
  * Explicit: set _detect_types_ to [`PARSE_COLNAMES`](https://docs.python.org/3/library/sqlite3.html#sqlite3.PARSE_COLNAMES "sqlite3.PARSE_COLNAMES")
  * Both: set _detect_types_ to `sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES`. Column names take precedence over declared types.


The following example illustrates the implicit and explicit approaches:
Copy```
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

def adapt_point(point):
    return f"{point.x};{point.y}"

def convert_point(s):
    x, y = list(map(float, s.split(b";")))
    return Point(x, y)

# Register the adapter and converter
sqlite3.register_adapter(Point, adapt_point)
sqlite3.register_converter("point", convert_point)

# 1) Parse using declared types
p = Point(4.0, -3.2)
con = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES)
cur = con.execute("CREATE TABLE test(p point)")

cur.execute("INSERT INTO test(p) VALUES(?)", (p,))
cur.execute("SELECT p FROM test")
print("with declared types:", cur.fetchone()[0])
cur.close()
con.close()

# 2) Parse using column names
con = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_COLNAMES)
cur = con.execute("CREATE TABLE test(p)")

cur.execute("INSERT INTO test(p) VALUES(?)", (p,))
cur.execute('SELECT p AS "p [point]" FROM test')
print("with column names:", cur.fetchone()[0])
cur.close()
con.close()

```

### Adapter and converter recipes[¶](https://docs.python.org/3/library/sqlite3.html#adapter-and-converter-recipes "Link to this heading")
This section shows recipes for common adapters and converters.
Copy```
import datetime
import sqlite3

def adapt_date_iso(val):
    """Adapt datetime.date to ISO 8601 date."""
    return val.isoformat()

def adapt_datetime_iso(val):
    """Adapt datetime.datetime to timezone-naive ISO 8601 date."""
    return val.replace(tzinfo=None).isoformat()

def adapt_datetime_epoch(val):
    """Adapt datetime.datetime to Unix timestamp."""
    return int(val.timestamp())

sqlite3.register_adapter(datetime.date, adapt_date_iso)
sqlite3.register_adapter(datetime.datetime, adapt_datetime_iso)
sqlite3.register_adapter(datetime.datetime, adapt_datetime_epoch)

def convert_date(val):
    """Convert ISO 8601 date to datetime.date object."""
    return datetime.date.fromisoformat(val.decode())

def convert_datetime(val):
    """Convert ISO 8601 datetime to datetime.datetime object."""
    return datetime.datetime.fromisoformat(val.decode())

def convert_timestamp(val):
    """Convert Unix epoch timestamp to datetime.datetime object."""
    return datetime.datetime.fromtimestamp(int(val))

sqlite3.register_converter("date", convert_date)
sqlite3.register_converter("datetime", convert_datetime)
sqlite3.register_converter("timestamp", convert_timestamp)

```

### How to use connection shortcut methods[¶](https://docs.python.org/3/library/sqlite3.html#how-to-use-connection-shortcut-methods "Link to this heading")
Using the [`execute()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.execute "sqlite3.Connection.execute"), [`executemany()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.executemany "sqlite3.Connection.executemany"), and [`executescript()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.executescript "sqlite3.Connection.executescript") methods of the [`Connection`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection "sqlite3.Connection") class, your code can be written more concisely because you don’t have to create the (often superfluous) [`Cursor`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor "sqlite3.Cursor") objects explicitly. Instead, the `Cursor` objects are created implicitly and these shortcut methods return the cursor objects. This way, you can execute a `SELECT` statement and iterate over it directly using only a single call on the `Connection` object.
Copy```
# Create and fill the table.
con = sqlite3.connect(":memory:")
con.execute("CREATE TABLE lang(name, first_appeared)")
data = [
    ("C++", 1985),
    ("Objective-C", 1984),
]
con.executemany("INSERT INTO lang(name, first_appeared) VALUES(?, ?)", data)

# Print the table contents
for row in con.execute("SELECT name, first_appeared FROM lang"):
    print(row)

print("I just deleted", con.execute("DELETE FROM lang").rowcount, "rows")

# close() is not a shortcut method and it's not called automatically;
# the connection object should be closed manually
con.close()

```

### How to use the connection context manager[¶](https://docs.python.org/3/library/sqlite3.html#how-to-use-the-connection-context-manager "Link to this heading")
A [`Connection`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection "sqlite3.Connection") object can be used as a context manager that automatically commits or rolls back open transactions when leaving the body of the context manager. If the body of the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) statement finishes without exceptions, the transaction is committed. If this commit fails, or if the body of the `with` statement raises an uncaught exception, the transaction is rolled back. If [`autocommit`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.autocommit "sqlite3.Connection.autocommit") is `False`, a new transaction is implicitly opened after committing or rolling back.
If there is no open transaction upon leaving the body of the `with` statement, or if [`autocommit`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.autocommit "sqlite3.Connection.autocommit") is `True`, the context manager does nothing.
Note
The context manager neither implicitly opens a new transaction nor closes the connection. If you need a closing context manager, consider using [`contextlib.closing()`](https://docs.python.org/3/library/contextlib.html#contextlib.closing "contextlib.closing").
Copy```
con = sqlite3.connect(":memory:")
con.execute("CREATE TABLE lang(id INTEGER PRIMARY KEY, name VARCHAR UNIQUE)")
