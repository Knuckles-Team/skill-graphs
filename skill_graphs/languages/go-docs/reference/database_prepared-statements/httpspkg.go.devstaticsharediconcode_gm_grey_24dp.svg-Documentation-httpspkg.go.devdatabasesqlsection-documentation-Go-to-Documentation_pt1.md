##  ![](https://pkg.go.dev/static/shared/icon/code_gm_grey_24dp.svg) Documentation [¶](https://pkg.go.dev/database/sql#section-documentation "Go to Documentation")
### Overview [¶](https://pkg.go.dev/database/sql#pkg-overview "Go to Overview")
Package sql provides a generic interface around SQL (or SQL-like) databases.
The sql package must be used in conjunction with a database driver. See
Drivers that do not support context cancellation will not return until after the query is completed.
For usage examples, see the wiki page at
Example (OpenDBCLI) [¶](https://pkg.go.dev/database/sql#example-package-OpenDBCLI "Go to Example \(OpenDBCLI\)")
Share Format Run
Example (OpenDBService) [¶](https://pkg.go.dev/database/sql#example-package-OpenDBService "Go to Example \(OpenDBService\)")
Share Format Run
### Index [¶](https://pkg.go.dev/database/sql#pkg-index "Go to Index")
  * [Variables](https://pkg.go.dev/database/sql#pkg-variables)
  * [func Drivers() []string](https://pkg.go.dev/database/sql#Drivers)
  * [func Register(name string, driver driver.Driver)](https://pkg.go.dev/database/sql#Register)
  * [type ColumnType](https://pkg.go.dev/database/sql#ColumnType)
  *     * [func (ci *ColumnType) DatabaseTypeName() string](https://pkg.go.dev/database/sql#ColumnType.DatabaseTypeName)
    * [func (ci *ColumnType) DecimalSize() (precision, scale int64, ok bool)](https://pkg.go.dev/database/sql#ColumnType.DecimalSize)
    * [func (ci *ColumnType) Length() (length int64, ok bool)](https://pkg.go.dev/database/sql#ColumnType.Length)
    * [func (ci *ColumnType) Name() string](https://pkg.go.dev/database/sql#ColumnType.Name)
    * [func (ci *ColumnType) Nullable() (nullable, ok bool)](https://pkg.go.dev/database/sql#ColumnType.Nullable)
    * [func (ci *ColumnType) ScanType() reflect.Type](https://pkg.go.dev/database/sql#ColumnType.ScanType)
  * [type Conn](https://pkg.go.dev/database/sql#Conn)
  *     * [func (c *Conn) BeginTx(ctx context.Context, opts *TxOptions) (*Tx, error)](https://pkg.go.dev/database/sql#Conn.BeginTx)
    * [func (c *Conn) Close() error](https://pkg.go.dev/database/sql#Conn.Close)
    * [func (c *Conn) ExecContext(ctx context.Context, query string, args ...any) (Result, error)](https://pkg.go.dev/database/sql#Conn.ExecContext)
    * [func (c *Conn) PingContext(ctx context.Context) error](https://pkg.go.dev/database/sql#Conn.PingContext)
    * [func (c *Conn) PrepareContext(ctx context.Context, query string) (*Stmt, error)](https://pkg.go.dev/database/sql#Conn.PrepareContext)
    * [func (c *Conn) QueryContext(ctx context.Context, query string, args ...any) (*Rows, error)](https://pkg.go.dev/database/sql#Conn.QueryContext)
    * [func (c *Conn) QueryRowContext(ctx context.Context, query string, args ...any) *Row](https://pkg.go.dev/database/sql#Conn.QueryRowContext)
    * [func (c *Conn) Raw(f func(driverConn any) error) (err error)](https://pkg.go.dev/database/sql#Conn.Raw)
  * [type DB](https://pkg.go.dev/database/sql#DB)
  *     * [func Open(driverName, dataSourceName string) (*DB, error)](https://pkg.go.dev/database/sql#Open)
    * [func OpenDB(c driver.Connector) *DB](https://pkg.go.dev/database/sql#OpenDB)
  *     * [func (db *DB) Begin() (*Tx, error)](https://pkg.go.dev/database/sql#DB.Begin)
    * [func (db *DB) BeginTx(ctx context.Context, opts *TxOptions) (*Tx, error)](https://pkg.go.dev/database/sql#DB.BeginTx)
    * [func (db *DB) Close() error](https://pkg.go.dev/database/sql#DB.Close)
    * [func (db *DB) Conn(ctx context.Context) (*Conn, error)](https://pkg.go.dev/database/sql#DB.Conn)
    * [func (db *DB) Driver() driver.Driver](https://pkg.go.dev/database/sql#DB.Driver)
    * [func (db *DB) Exec(query string, args ...any) (Result, error)](https://pkg.go.dev/database/sql#DB.Exec)
    * [func (db *DB) ExecContext(ctx context.Context, query string, args ...any) (Result, error)](https://pkg.go.dev/database/sql#DB.ExecContext)
    * [func (db *DB) Ping() error](https://pkg.go.dev/database/sql#DB.Ping)
    * [func (db *DB) PingContext(ctx context.Context) error](https://pkg.go.dev/database/sql#DB.PingContext)
    * [func (db *DB) Prepare(query string) (*Stmt, error)](https://pkg.go.dev/database/sql#DB.Prepare)
    * [func (db *DB) PrepareContext(ctx context.Context, query string) (*Stmt, error)](https://pkg.go.dev/database/sql#DB.PrepareContext)
    * [func (db *DB) Query(query string, args ...any) (*Rows, error)](https://pkg.go.dev/database/sql#DB.Query)
    * [func (db *DB) QueryContext(ctx context.Context, query string, args ...any) (*Rows, error)](https://pkg.go.dev/database/sql#DB.QueryContext)
    * [func (db *DB) QueryRow(query string, args ...any) *Row](https://pkg.go.dev/database/sql#DB.QueryRow)
    * [func (db *DB) QueryRowContext(ctx context.Context, query string, args ...any) *Row](https://pkg.go.dev/database/sql#DB.QueryRowContext)
    * [func (db *DB) SetConnMaxIdleTime(d time.Duration)](https://pkg.go.dev/database/sql#DB.SetConnMaxIdleTime)
    * [func (db *DB) SetConnMaxLifetime(d time.Duration)](https://pkg.go.dev/database/sql#DB.SetConnMaxLifetime)
    * [func (db *DB) SetMaxIdleConns(n int)](https://pkg.go.dev/database/sql#DB.SetMaxIdleConns)
    * [func (db *DB) SetMaxOpenConns(n int)](https://pkg.go.dev/database/sql#DB.SetMaxOpenConns)
    * [func (db *DB) Stats() DBStats](https://pkg.go.dev/database/sql#DB.Stats)
  * [type DBStats](https://pkg.go.dev/database/sql#DBStats)
  * [type IsolationLevel](https://pkg.go.dev/database/sql#IsolationLevel)
  *     * [func (i IsolationLevel) String() string](https://pkg.go.dev/database/sql#IsolationLevel.String)
  * [type NamedArg](https://pkg.go.dev/database/sql#NamedArg)
  *     * [func Named(name string, value any) NamedArg](https://pkg.go.dev/database/sql#Named)
  * [type Null](https://pkg.go.dev/database/sql#Null)
  *     * [func (n *Null[T]) Scan(value any) error](https://pkg.go.dev/database/sql#Null.Scan)
    * [func (n Null[T]) Value() (driver.Value, error)](https://pkg.go.dev/database/sql#Null.Value)
  * [type NullBool](https://pkg.go.dev/database/sql#NullBool)
  *     * [func (n *NullBool) Scan(value any) error](https://pkg.go.dev/database/sql#NullBool.Scan)
    * [func (n NullBool) Value() (driver.Value, error)](https://pkg.go.dev/database/sql#NullBool.Value)
  * [type NullByte](https://pkg.go.dev/database/sql#NullByte)
  *     * [func (n *NullByte) Scan(value any) error](https://pkg.go.dev/database/sql#NullByte.Scan)
    * [func (n NullByte) Value() (driver.Value, error)](https://pkg.go.dev/database/sql#NullByte.Value)
  * [type NullFloat64](https://pkg.go.dev/database/sql#NullFloat64)
  *     * [func (n *NullFloat64) Scan(value any) error](https://pkg.go.dev/database/sql#NullFloat64.Scan)
    * [func (n NullFloat64) Value() (driver.Value, error)](https://pkg.go.dev/database/sql#NullFloat64.Value)
  * [type NullInt16](https://pkg.go.dev/database/sql#NullInt16)
  *     * [func (n *NullInt16) Scan(value any) error](https://pkg.go.dev/database/sql#NullInt16.Scan)
    * [func (n NullInt16) Value() (driver.Value, error)](https://pkg.go.dev/database/sql#NullInt16.Value)
  * [type NullInt32](https://pkg.go.dev/database/sql#NullInt32)
  *     * [func (n *NullInt32) Scan(value any) error](https://pkg.go.dev/database/sql#NullInt32.Scan)
    * [func (n NullInt32) Value() (driver.Value, error)](https://pkg.go.dev/database/sql#NullInt32.Value)
  * [type NullInt64](https://pkg.go.dev/database/sql#NullInt64)
  *     * [func (n *NullInt64) Scan(value any) error](https://pkg.go.dev/database/sql#NullInt64.Scan)
    * [func (n NullInt64) Value() (driver.Value, error)](https://pkg.go.dev/database/sql#NullInt64.Value)
  * [type NullString](https://pkg.go.dev/database/sql#NullString)
  *     * [func (ns *NullString) Scan(value any) error](https://pkg.go.dev/database/sql#NullString.Scan)
    * [func (ns NullString) Value() (driver.Value, error)](https://pkg.go.dev/database/sql#NullString.Value)
  * [type NullTime](https://pkg.go.dev/database/sql#NullTime)
  *     * [func (n *NullTime) Scan(value any) error](https://pkg.go.dev/database/sql#NullTime.Scan)
    * [func (n NullTime) Value() (driver.Value, error)](https://pkg.go.dev/database/sql#NullTime.Value)
  * [type Out](https://pkg.go.dev/database/sql#Out)
  * [type RawBytes](https://pkg.go.dev/database/sql#RawBytes)
  * [type Result](https://pkg.go.dev/database/sql#Result)
  * [type Row](https://pkg.go.dev/database/sql#Row)
  *     * [func (r *Row) Err() error](https://pkg.go.dev/database/sql#Row.Err)
    * [func (r *Row) Scan(dest ...any) error](https://pkg.go.dev/database/sql#Row.Scan)
  * [type Rows](https://pkg.go.dev/database/sql#Rows)
  *     * [func (rs *Rows) Close() error](https://pkg.go.dev/database/sql#Rows.Close)
    * [func (rs *Rows) ColumnTypes() ([]*ColumnType, error)](https://pkg.go.dev/database/sql#Rows.ColumnTypes)
    * [func (rs *Rows) Columns() ([]string, error)](https://pkg.go.dev/database/sql#Rows.Columns)
    * [func (rs *Rows) Err() error](https://pkg.go.dev/database/sql#Rows.Err)
    * [func (rs *Rows) Next() bool](https://pkg.go.dev/database/sql#Rows.Next)
    * [func (rs *Rows) NextResultSet() bool](https://pkg.go.dev/database/sql#Rows.NextResultSet)
    * [func (rs *Rows) Scan(dest ...any) error](https://pkg.go.dev/database/sql#Rows.Scan)
  * [type Scanner](https://pkg.go.dev/database/sql#Scanner)
  * [type Stmt](https://pkg.go.dev/database/sql#Stmt)
  *     * [func (s *Stmt) Close() error](https://pkg.go.dev/database/sql#Stmt.Close)
    * [func (s *Stmt) Exec(args ...any) (Result, error)](https://pkg.go.dev/database/sql#Stmt.Exec)
    * [func (s *Stmt) ExecContext(ctx context.Context, args ...any) (Result, error)](https://pkg.go.dev/database/sql#Stmt.ExecContext)
    * [func (s *Stmt) Query(args ...any) (*Rows, error)](https://pkg.go.dev/database/sql#Stmt.Query)
    * [func (s *Stmt) QueryContext(ctx context.Context, args ...any) (*Rows, error)](https://pkg.go.dev/database/sql#Stmt.QueryContext)
    * [func (s *Stmt) QueryRow(args ...any) *Row](https://pkg.go.dev/database/sql#Stmt.QueryRow)
    * [func (s *Stmt) QueryRowContext(ctx context.Context, args ...any) *Row](https://pkg.go.dev/database/sql#Stmt.QueryRowContext)
  * [type Tx](https://pkg.go.dev/database/sql#Tx)
  *     * [func (tx *Tx) Commit() error](https://pkg.go.dev/database/sql#Tx.Commit)
    * [func (tx *Tx) Exec(query string, args ...any) (Result, error)](https://pkg.go.dev/database/sql#Tx.Exec)
    * [func (tx *Tx) ExecContext(ctx context.Context, query string, args ...any) (Result, error)](https://pkg.go.dev/database/sql#Tx.ExecContext)
    * [func (tx *Tx) Prepare(query string) (*Stmt, error)](https://pkg.go.dev/database/sql#Tx.Prepare)
    * [func (tx *Tx) PrepareContext(ctx context.Context, query string) (*Stmt, error)](https://pkg.go.dev/database/sql#Tx.PrepareContext)
    * [func (tx *Tx) Query(query string, args ...any) (*Rows, error)](https://pkg.go.dev/database/sql#Tx.Query)
    * [func (tx *Tx) QueryContext(ctx context.Context, query string, args ...any) (*Rows, error)](https://pkg.go.dev/database/sql#Tx.QueryContext)
    * [func (tx *Tx) QueryRow(query string, args ...any) *Row](https://pkg.go.dev/database/sql#Tx.QueryRow)
    * [func (tx *Tx) QueryRowContext(ctx context.Context, query string, args ...any) *Row](https://pkg.go.dev/database/sql#Tx.QueryRowContext)
    * [func (tx *Tx) Rollback() error](https://pkg.go.dev/database/sql#Tx.Rollback)
    * [func (tx *Tx) Stmt(stmt *Stmt) *Stmt](https://pkg.go.dev/database/sql#Tx.Stmt)
    * [func (tx *Tx) StmtContext(ctx context.Context, stmt *Stmt) *Stmt](https://pkg.go.dev/database/sql#Tx.StmtContext)
  * [type TxOptions](https://pkg.go.dev/database/sql#TxOptions)


### Examples [¶](https://pkg.go.dev/database/sql#pkg-examples "Go to Examples")
  * [Package (OpenDBCLI)](https://pkg.go.dev/database/sql#example-package-OpenDBCLI)
  * [Package (OpenDBService)](https://pkg.go.dev/database/sql#example-package-OpenDBService)
  * [Conn.ExecContext](https://pkg.go.dev/database/sql#example-Conn.ExecContext)
  * [DB.BeginTx](https://pkg.go.dev/database/sql#example-DB.BeginTx)
  * [DB.ExecContext](https://pkg.go.dev/database/sql#example-DB.ExecContext)
  * [DB.PingContext](https://pkg.go.dev/database/sql#example-DB.PingContext)
  * [DB.Prepare](https://pkg.go.dev/database/sql#example-DB.Prepare)
  * [DB.Query (MultipleResultSets)](https://pkg.go.dev/database/sql#example-DB.Query-MultipleResultSets)
  * [DB.QueryContext](https://pkg.go.dev/database/sql#example-DB.QueryContext)
  * [DB.QueryRowContext](https://pkg.go.dev/database/sql#example-DB.QueryRowContext)
  * [Rows](https://pkg.go.dev/database/sql#example-Rows)
  * [Stmt](https://pkg.go.dev/database/sql#example-Stmt)
  * [Stmt.QueryRowContext](https://pkg.go.dev/database/sql#example-Stmt.QueryRowContext)
  * [Tx.ExecContext](https://pkg.go.dev/database/sql#example-Tx.ExecContext)
  * [Tx.Prepare](https://pkg.go.dev/database/sql#example-Tx.Prepare)
  * [Tx.Rollback](https://pkg.go.dev/database/sql#example-Tx.Rollback)


### Constants [¶](https://pkg.go.dev/database/sql#pkg-constants "Go to Constants")
This section is empty.
### Variables [¶](https://pkg.go.dev/database/sql#pkg-variables "Go to Variables")
```
var ErrConnDone = errors[](https://pkg.go.dev/errors).New[](https://pkg.go.dev/errors#New)("sql: connection is already closed")
```

ErrConnDone is returned by any operation that is performed on a connection that has already been returned to the connection pool.
```
var ErrNoRows = errors[](https://pkg.go.dev/errors).New[](https://pkg.go.dev/errors#New)("sql: no rows in result set")
```

ErrNoRows is returned by [Row.Scan](https://pkg.go.dev/database/sql#Row.Scan) when [DB.QueryRow](https://pkg.go.dev/database/sql#DB.QueryRow) doesn't return a row. In such a case, QueryRow returns a placeholder [*Row](https://pkg.go.dev/database/sql#Row) value that defers this error until a Scan.
```
var ErrTxDone = errors[](https://pkg.go.dev/errors).New[](https://pkg.go.dev/errors#New)("sql: transaction has already been committed or rolled back")
```

ErrTxDone is returned by any operation that is performed on a transaction that has already been committed or rolled back.
### Functions [¶](https://pkg.go.dev/database/sql#pkg-functions "Go to Functions")
####  func [¶](https://pkg.go.dev/database/sql#Drivers "Go to Drivers") added in go1.4
```
func Drivers() []string[](https://pkg.go.dev/builtin#string)
```

Drivers returns a sorted list of the names of the registered drivers.
####  func [¶](https://pkg.go.dev/database/sql#Register "Go to Register")
```
func Register(name string[](https://pkg.go.dev/builtin#string), driver driver[](https://pkg.go.dev/database/sql/driver).Driver[](https://pkg.go.dev/database/sql/driver#Driver))
```

Register makes a database driver available by the provided name. If Register is called twice with the same name or if driver is nil, it panics.
### Types [¶](https://pkg.go.dev/database/sql#pkg-types "Go to Types")
####  type [¶](https://pkg.go.dev/database/sql#ColumnType "Go to ColumnType") added in go1.8
```
type ColumnType struct {
	// contains filtered or unexported fields
}
```

ColumnType contains the name and type of a column.
####  func (*ColumnType) [¶](https://pkg.go.dev/database/sql#ColumnType.DatabaseTypeName "Go to ColumnType.DatabaseTypeName") added in go1.8
```
func (ci *ColumnType[](https://pkg.go.dev/database/sql#ColumnType)) DatabaseTypeName() string[](https://pkg.go.dev/builtin#string)
```

DatabaseTypeName returns the database system name of the column type. If an empty string is returned, then the driver type name is not supported. Consult your driver documentation for a list of driver data types. [ColumnType.Length](https://pkg.go.dev/database/sql#ColumnType.Length) specifiers are not included. Common type names include "VARCHAR", "TEXT", "NVARCHAR", "DECIMAL", "BOOL", "INT", and "BIGINT".
####  func (*ColumnType) [¶](https://pkg.go.dev/database/sql#ColumnType.DecimalSize "Go to ColumnType.DecimalSize") added in go1.8
```
func (ci *ColumnType[](https://pkg.go.dev/database/sql#ColumnType)) DecimalSize() (precision, scale int64[](https://pkg.go.dev/builtin#int64), ok bool[](https://pkg.go.dev/builtin#bool))
```

DecimalSize returns the scale and precision of a decimal type. If not applicable or if not supported ok is false.
####  func (*ColumnType) [¶](https://pkg.go.dev/database/sql#ColumnType.Length "Go to ColumnType.Length") added in go1.8
```
func (ci *ColumnType[](https://pkg.go.dev/database/sql#ColumnType)) Length() (length int64[](https://pkg.go.dev/builtin#int64), ok bool[](https://pkg.go.dev/builtin#bool))
```

Length returns the column type length for variable length column types such as text and binary field types. If the type length is unbounded the value will be [math.MaxInt64](https://pkg.go.dev/math#MaxInt64) (any database limits will still apply). If the column type is not variable length, such as an int, or if not supported by the driver ok is false.
####  func (*ColumnType) [¶](https://pkg.go.dev/database/sql#ColumnType.Name "Go to ColumnType.Name") added in go1.8
```
func (ci *ColumnType[](https://pkg.go.dev/database/sql#ColumnType)) Name() string[](https://pkg.go.dev/builtin#string)
```

Name returns the name or alias of the column.
####  func (*ColumnType) [¶](https://pkg.go.dev/database/sql#ColumnType.Nullable "Go to ColumnType.Nullable") added in go1.8
```
func (ci *ColumnType[](https://pkg.go.dev/database/sql#ColumnType)) Nullable() (nullable, ok bool[](https://pkg.go.dev/builtin#bool))
```

Nullable reports whether the column may be null. If a driver does not support this property ok will be false.
####  func (*ColumnType) [¶](https://pkg.go.dev/database/sql#ColumnType.ScanType "Go to ColumnType.ScanType") added in go1.8
```
func (ci *ColumnType[](https://pkg.go.dev/database/sql#ColumnType)) ScanType() reflect[](https://pkg.go.dev/reflect).Type[](https://pkg.go.dev/reflect#Type)
```

ScanType returns a Go type suitable for scanning into using [Rows.Scan](https://pkg.go.dev/database/sql#Rows.Scan). If a driver does not support this property ScanType will return the type of an empty interface.
####  type [¶](https://pkg.go.dev/database/sql#Conn "Go to Conn") added in go1.9
```
type Conn struct {
	// contains filtered or unexported fields
}
```

Conn represents a single database connection rather than a pool of database connections. Prefer running queries from [DB](https://pkg.go.dev/database/sql#DB) unless there is a specific need for a continuous single database connection.
A Conn must call [Conn.Close](https://pkg.go.dev/database/sql#Conn.Close) to return the connection to the database pool and may do so concurrently with a running query.
After a call to [Conn.Close](https://pkg.go.dev/database/sql#Conn.Close), all operations on the connection fail with [ErrConnDone](https://pkg.go.dev/database/sql#ErrConnDone).
####  func (*Conn) [¶](https://pkg.go.dev/database/sql#Conn.BeginTx "Go to Conn.BeginTx") added in go1.9
```
func (c *Conn[](https://pkg.go.dev/database/sql#Conn)) BeginTx(ctx context[](https://pkg.go.dev/context).Context[](https://pkg.go.dev/context#Context), opts *TxOptions[](https://pkg.go.dev/database/sql#TxOptions)) (*Tx[](https://pkg.go.dev/database/sql#Tx), error[](https://pkg.go.dev/builtin#error))
```

BeginTx starts a transaction.
The provided context is used until the transaction is committed or rolled back. If the context is canceled, the sql package will roll back the transaction. [Tx.Commit](https://pkg.go.dev/database/sql#Tx.Commit) will return an error if the context provided to BeginTx is canceled.
The provided [TxOptions](https://pkg.go.dev/database/sql#TxOptions) is optional and may be nil if defaults should be used. If a non-default isolation level is used that the driver doesn't support, an error will be returned.
####  func (*Conn) [¶](https://pkg.go.dev/database/sql#Conn.Close "Go to Conn.Close") added in go1.9
```
func (c *Conn[](https://pkg.go.dev/database/sql#Conn)) Close() error[](https://pkg.go.dev/builtin#error)
```

Close returns the connection to the connection pool. All operations after a Close will return with [ErrConnDone](https://pkg.go.dev/database/sql#ErrConnDone). Close is safe to call concurrently with other operations and will block until all other operations finish. It may be useful to first cancel any used context and then call close directly after.
####  func (*Conn) [¶](https://pkg.go.dev/database/sql#Conn.ExecContext "Go to Conn.ExecContext") added in go1.9
```
func (c *Conn[](https://pkg.go.dev/database/sql#Conn)) ExecContext(ctx context[](https://pkg.go.dev/context).Context[](https://pkg.go.dev/context#Context), query string[](https://pkg.go.dev/builtin#string), args ...any[](https://pkg.go.dev/builtin#any)) (Result[](https://pkg.go.dev/database/sql#Result), error[](https://pkg.go.dev/builtin#error))
```

ExecContext executes a query without returning any rows. The args are for any placeholder parameters in the query.
Example [¶](https://pkg.go.dev/database/sql#example-Conn.ExecContext "Go to Example")
Share Format Run
####  func (*Conn) [¶](https://pkg.go.dev/database/sql#Conn.PingContext "Go to Conn.PingContext") added in go1.9
```
func (c *Conn[](https://pkg.go.dev/database/sql#Conn)) PingContext(ctx context[](https://pkg.go.dev/context).Context[](https://pkg.go.dev/context#Context)) error[](https://pkg.go.dev/builtin#error)
```

PingContext verifies the connection to the database is still alive.
####  func (*Conn) [¶](https://pkg.go.dev/database/sql#Conn.PrepareContext "Go to Conn.PrepareContext") added in go1.9
```
func (c *Conn[](https://pkg.go.dev/database/sql#Conn)) PrepareContext(ctx context[](https://pkg.go.dev/context).Context[](https://pkg.go.dev/context#Context), query string[](https://pkg.go.dev/builtin#string)) (*Stmt[](https://pkg.go.dev/database/sql#Stmt), error[](https://pkg.go.dev/builtin#error))
```

PrepareContext creates a prepared statement for later queries or executions. Multiple queries or executions may be run concurrently from the returned statement. The caller must call the statement's [*Stmt.Close](https://pkg.go.dev/database/sql#Stmt.Close) method when the statement is no longer needed.
The provided context is used for the preparation of the statement, not for the execution of the statement.
####  func (*Conn) [¶](https://pkg.go.dev/database/sql#Conn.QueryContext "Go to Conn.QueryContext") added in go1.9
```
func (c *Conn[](https://pkg.go.dev/database/sql#Conn)) QueryContext(ctx context[](https://pkg.go.dev/context).Context[](https://pkg.go.dev/context#Context), query string[](https://pkg.go.dev/builtin#string), args ...any[](https://pkg.go.dev/builtin#any)) (*Rows[](https://pkg.go.dev/database/sql#Rows), error[](https://pkg.go.dev/builtin#error))
```

QueryContext executes a query that returns rows, typically a SELECT. The args are for any placeholder parameters in the query.
####  func (*Conn) [¶](https://pkg.go.dev/database/sql#Conn.QueryRowContext "Go to Conn.QueryRowContext") added in go1.9
```
func (c *Conn[](https://pkg.go.dev/database/sql#Conn)) QueryRowContext(ctx context[](https://pkg.go.dev/context).Context[](https://pkg.go.dev/context#Context), query string[](https://pkg.go.dev/builtin#string), args ...any[](https://pkg.go.dev/builtin#any)) *Row[](https://pkg.go.dev/database/sql#Row)
```

QueryRowContext executes a query that is expected to return at most one row. QueryRowContext always returns a non-nil value. Errors are deferred until the [*Row.Scan](https://pkg.go.dev/database/sql#Row.Scan) method is called. If the query selects no rows, the [*Row.Scan](https://pkg.go.dev/database/sql#Row.Scan) will return [ErrNoRows](https://pkg.go.dev/database/sql#ErrNoRows). Otherwise, the [*Row.Scan](https://pkg.go.dev/database/sql#Row.Scan) scans the first selected row and discards the rest.
####  func (*Conn) [¶](https://pkg.go.dev/database/sql#Conn.Raw "Go to Conn.Raw") added in go1.13
```
func (c *Conn[](https://pkg.go.dev/database/sql#Conn)) Raw(f func(driverConn any[](https://pkg.go.dev/builtin#any)) error[](https://pkg.go.dev/builtin#error)) (err error[](https://pkg.go.dev/builtin#error))
```

Raw executes f exposing the underlying driver connection for the duration of f. The driverConn must not be used outside of f.
Once f returns and err is not [driver.ErrBadConn](https://pkg.go.dev/database/sql/driver#ErrBadConn), the [Conn](https://pkg.go.dev/database/sql#Conn) will continue to be usable until [Conn.Close](https://pkg.go.dev/database/sql#Conn.Close) is called.
####  type [¶](https://pkg.go.dev/database/sql#DB "Go to DB")
```
type DB struct {
	// contains filtered or unexported fields
}
```

DB is a database handle representing a pool of zero or more underlying connections. It's safe for concurrent use by multiple goroutines.
The sql package creates and frees connections automatically; it also maintains a free pool of idle connections. If the database has a concept of per-connection state, such state can be reliably observed within a transaction ([Tx](https://pkg.go.dev/database/sql#Tx)) or connection ([Conn](https://pkg.go.dev/database/sql#Conn)). Once [DB.Begin](https://pkg.go.dev/database/sql#DB.Begin) is called, the returned [Tx](https://pkg.go.dev/database/sql#Tx) is bound to a single connection. Once [Tx.Commit](https://pkg.go.dev/database/sql#Tx.Commit) or [Tx.Rollback](https://pkg.go.dev/database/sql#Tx.Rollback) is called on the transaction, that transaction's connection is returned to [DB](https://pkg.go.dev/database/sql#DB)'s idle connection pool. The pool size can be controlled with [DB.SetMaxIdleConns](https://pkg.go.dev/database/sql#DB.SetMaxIdleConns).
