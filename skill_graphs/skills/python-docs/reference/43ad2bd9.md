# Example taken from https://www.sqlite.org/windowfunctions.html#udfwinfunc
class WindowSumInt:
    def __init__(self):
        self.count = 0

    def step(self, value):
        """Add a row to the current window."""
        self.count += value

    def value(self):
        """Return the current value of the aggregate."""
        return self.count

    def inverse(self, value):
        """Remove a row from the current window."""
        self.count -= value

    def finalize(self):
        """Return the final value of the aggregate.

        Any clean-up actions should be placed here.
        """
        return self.count


con = sqlite3.connect(":memory:")
cur = con.execute("CREATE TABLE test(x, y)")
values = [
    ("a", 4),
    ("b", 5),
    ("c", 3),
    ("d", 8),
    ("e", 1),
]
cur.executemany("INSERT INTO test VALUES(?, ?)", values)
con.create_window_function("sumint", 1, WindowSumInt)
cur.execute("""
    SELECT x, sumint(y) OVER (
        ORDER BY x ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING
    ) AS sum_y
    FROM test ORDER BY x
""")
print(cur.fetchall())
con.close()

```


create_collation(_name_ , _callable_ , _/_)[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.create_collation "Link to this definition")

Create a collation named _name_ using the collating function _callable_. _callable_ is passed two [`string`](https://docs.python.org/3/library/stdtypes.html#str "str") arguments, and it should return an [`integer`](https://docs.python.org/3/library/functions.html#int "int"):
  * `1` if the first is ordered higher than the second
  * `-1` if the first is ordered lower than the second
  * `0` if they are ordered equal


The following example shows a reverse sorting collation:
Copy```
def collate_reverse(string1, string2):
    if string1 == string2:
        return 0
    elif string1 < string2:
        return 1
    else:
        return -1

con = sqlite3.connect(":memory:")
con.create_collation("reverse", collate_reverse)

cur = con.execute("CREATE TABLE test(x)")
cur.executemany("INSERT INTO test(x) VALUES(?)", [("a",), ("b",)])
cur.execute("SELECT x FROM test ORDER BY x COLLATE reverse")
for row in cur:
    print(row)
con.close()

```

Remove a collation function by setting _callable_ to `None`.
Changed in version 3.11: The collation name can contain any Unicode character. Earlier, only ASCII characters were allowed.

interrupt()[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.interrupt "Link to this definition")

Call this method from a different thread to abort any queries that might be executing on the connection. Aborted queries will raise an [`OperationalError`](https://docs.python.org/3/library/sqlite3.html#sqlite3.OperationalError "sqlite3.OperationalError").

set_authorizer(_authorizer_callback_)[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.set_authorizer "Link to this definition")

Register [callable](https://docs.python.org/3/glossary.html#term-callable) _authorizer_callback_ to be invoked for each attempt to access a column of a table in the database. The callback should return one of [`SQLITE_OK`](https://docs.python.org/3/library/sqlite3.html#sqlite3.SQLITE_OK "sqlite3.SQLITE_OK"), [`SQLITE_DENY`](https://docs.python.org/3/library/sqlite3.html#sqlite3.SQLITE_DENY "sqlite3.SQLITE_DENY"), or [`SQLITE_IGNORE`](https://docs.python.org/3/library/sqlite3.html#sqlite3.SQLITE_IGNORE "sqlite3.SQLITE_IGNORE") to signal how access to the column should be handled by the underlying SQLite library.
The first argument to the callback signifies what kind of operation is to be authorized. The second and third argument will be arguments or `None` depending on the first argument. The 4th argument is the name of the database (“main”, “temp”, etc.) if applicable. The 5th argument is the name of the inner-most trigger or view that is responsible for the access attempt or `None` if this access attempt is directly from input SQL code.
Please consult the SQLite documentation about the possible values for the first argument and the meaning of the second and third argument depending on the first one. All necessary constants are available in the `sqlite3` module.
Passing `None` as _authorizer_callback_ will disable the authorizer.
Changed in version 3.11: Added support for disabling the authorizer using `None`.
Changed in version 3.13: Passing _authorizer_callback_ as a keyword argument is deprecated. The parameter will become positional-only in Python 3.15.

set_progress_handler(_progress_handler_ , _n_)[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.set_progress_handler "Link to this definition")

Register [callable](https://docs.python.org/3/glossary.html#term-callable) _progress_handler_ to be invoked for every _n_ instructions of the SQLite virtual machine. This is useful if you want to get called from SQLite during long-running operations, for example to update a GUI.
If you want to clear any previously installed progress handler, call the method with `None` for _progress_handler_.
Returning a non-zero value from the handler function will terminate the currently executing query and cause it to raise a [`DatabaseError`](https://docs.python.org/3/library/sqlite3.html#sqlite3.DatabaseError "sqlite3.DatabaseError") exception.
Changed in version 3.13: Passing _progress_handler_ as a keyword argument is deprecated. The parameter will become positional-only in Python 3.15.

set_trace_callback(_trace_callback_)[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.set_trace_callback "Link to this definition")

Register [callable](https://docs.python.org/3/glossary.html#term-callable) _trace_callback_ to be invoked for each SQL statement that is actually executed by the SQLite backend.
The only argument passed to the callback is the statement (as [`str`](https://docs.python.org/3/library/stdtypes.html#str "str")) that is being executed. The return value of the callback is ignored. Note that the backend does not only run statements passed to the [`Cursor.execute()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.execute "sqlite3.Cursor.execute") methods. Other sources include the [transaction management](https://docs.python.org/3/library/sqlite3.html#sqlite3-controlling-transactions) of the `sqlite3` module and the execution of triggers defined in the current database.
Passing `None` as _trace_callback_ will disable the trace callback.
Note
Exceptions raised in the trace callback are not propagated. As a development and debugging aid, use [`enable_callback_tracebacks()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.enable_callback_tracebacks "sqlite3.enable_callback_tracebacks") to enable printing tracebacks from exceptions raised in the trace callback.
Added in version 3.3.
Changed in version 3.13: Passing _trace_callback_ as a keyword argument is deprecated. The parameter will become positional-only in Python 3.15.

enable_load_extension(_enabled_ , _/_)[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.enable_load_extension "Link to this definition")

Enable the SQLite engine to load SQLite extensions from shared libraries if _enabled_ is `True`; else, disallow loading SQLite extensions. SQLite extensions can define new functions, aggregates or whole new virtual table implementations. One well-known extension is the fulltext-search extension distributed with SQLite.
Note
The `sqlite3` module is not built with loadable extension support by default, because some platforms (notably macOS) have SQLite libraries which are compiled without this feature. To get loadable extension support, you must pass the [`--enable-loadable-sqlite-extensions`](https://docs.python.org/3/using/configure.html#cmdoption-enable-loadable-sqlite-extensions) option to **configure**.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `sqlite3.enable_load_extension` with arguments `connection`, `enabled`.
Added in version 3.2.
Changed in version 3.10: Added the `sqlite3.enable_load_extension` auditing event.
Copy```
con.enable_load_extension(True)
