####  func [¶](https://pkg.go.dev/database/sql#Open "Go to Open")
```
func Open(driverName, dataSourceName string[](https://pkg.go.dev/builtin#string)) (*DB[](https://pkg.go.dev/database/sql#DB), error[](https://pkg.go.dev/builtin#error))
```

Open opens a database specified by its database driver name and a driver-specific data source name, usually consisting of at least a database name and connection information.
Most users will open a database via a driver-specific connection helper function that returns a [*DB](https://pkg.go.dev/database/sql#DB). No database drivers are included in the Go standard library. See
Open may just validate its arguments without creating a connection to the database. To verify that the data source name is valid, call [DB.Ping](https://pkg.go.dev/database/sql#DB.Ping).
The returned [DB](https://pkg.go.dev/database/sql#DB) is safe for concurrent use by multiple goroutines and maintains its own pool of idle connections. Thus, the Open function should be called just once. It is rarely necessary to close a [DB](https://pkg.go.dev/database/sql#DB).
####  func [¶](https://pkg.go.dev/database/sql#OpenDB "Go to OpenDB") added in go1.10
```
func OpenDB(c driver[](https://pkg.go.dev/database/sql/driver).Connector[](https://pkg.go.dev/database/sql/driver#Connector)) *DB[](https://pkg.go.dev/database/sql#DB)
```

OpenDB opens a database using a [driver.Connector](https://pkg.go.dev/database/sql/driver#Connector), allowing drivers to bypass a string based data source name.
Most users will open a database via a driver-specific connection helper function that returns a [*DB](https://pkg.go.dev/database/sql#DB). No database drivers are included in the Go standard library. See
OpenDB may just validate its arguments without creating a connection to the database. To verify that the data source name is valid, call [DB.Ping](https://pkg.go.dev/database/sql#DB.Ping).
The returned [DB](https://pkg.go.dev/database/sql#DB) is safe for concurrent use by multiple goroutines and maintains its own pool of idle connections. Thus, the OpenDB function should be called just once. It is rarely necessary to close a [DB](https://pkg.go.dev/database/sql#DB).
####  func (*DB) [¶](https://pkg.go.dev/database/sql#DB.Begin "Go to DB.Begin")
```
func (db *DB[](https://pkg.go.dev/database/sql#DB)) Begin() (*Tx[](https://pkg.go.dev/database/sql#Tx), error[](https://pkg.go.dev/builtin#error))
```

Begin starts a transaction. The default isolation level is dependent on the driver.
Begin uses [context.Background](https://pkg.go.dev/context#Background) internally; to specify the context, use [DB.BeginTx](https://pkg.go.dev/database/sql#DB.BeginTx).
####  func (*DB) [¶](https://pkg.go.dev/database/sql#DB.BeginTx "Go to DB.BeginTx") added in go1.8
```
func (db *DB[](https://pkg.go.dev/database/sql#DB)) BeginTx(ctx context[](https://pkg.go.dev/context).Context[](https://pkg.go.dev/context#Context), opts *TxOptions[](https://pkg.go.dev/database/sql#TxOptions)) (*Tx[](https://pkg.go.dev/database/sql#Tx), error[](https://pkg.go.dev/builtin#error))
```

BeginTx starts a transaction.
The provided context is used until the transaction is committed or rolled back. If the context is canceled, the sql package will roll back the transaction. [Tx.Commit](https://pkg.go.dev/database/sql#Tx.Commit) will return an error if the context provided to BeginTx is canceled.
The provided [TxOptions](https://pkg.go.dev/database/sql#TxOptions) is optional and may be nil if defaults should be used. If a non-default isolation level is used that the driver doesn't support, an error will be returned.
Example [¶](https://pkg.go.dev/database/sql#example-DB.BeginTx "Go to Example")
Share Format Run
####  func (*DB) [¶](https://pkg.go.dev/database/sql#DB.Close "Go to DB.Close")
```
func (db *DB[](https://pkg.go.dev/database/sql#DB)) Close() error[](https://pkg.go.dev/builtin#error)
```

Close closes the database and prevents new queries from starting. Close then waits for all queries that have started processing on the server to finish.
It is rare to Close a [DB](https://pkg.go.dev/database/sql#DB), as the [DB](https://pkg.go.dev/database/sql#DB) handle is meant to be long-lived and shared between many goroutines.
####  func (*DB) [¶](https://pkg.go.dev/database/sql#DB.Conn "Go to DB.Conn") added in go1.9
```
func (db *DB[](https://pkg.go.dev/database/sql#DB)) Conn(ctx context[](https://pkg.go.dev/context).Context[](https://pkg.go.dev/context#Context)) (*Conn[](https://pkg.go.dev/database/sql#Conn), error[](https://pkg.go.dev/builtin#error))
```

Conn returns a single connection by either opening a new connection or returning an existing connection from the connection pool. Conn will block until either a connection is returned or ctx is canceled. Queries run on the same Conn will be run in the same database session.
Every Conn must be returned to the database pool after use by calling [Conn.Close](https://pkg.go.dev/database/sql#Conn.Close).
####  func (*DB) [¶](https://pkg.go.dev/database/sql#DB.Driver "Go to DB.Driver")
```
func (db *DB[](https://pkg.go.dev/database/sql#DB)) Driver() driver[](https://pkg.go.dev/database/sql/driver).Driver[](https://pkg.go.dev/database/sql/driver#Driver)
```

Driver returns the database's underlying driver.
####  func (*DB) [¶](https://pkg.go.dev/database/sql#DB.Exec "Go to DB.Exec")
```
func (db *DB[](https://pkg.go.dev/database/sql#DB)) Exec(query string[](https://pkg.go.dev/builtin#string), args ...any[](https://pkg.go.dev/builtin#any)) (Result[](https://pkg.go.dev/database/sql#Result), error[](https://pkg.go.dev/builtin#error))
```

Exec executes a query without returning any rows. The args are for any placeholder parameters in the query.
Exec uses [context.Background](https://pkg.go.dev/context#Background) internally; to specify the context, use [DB.ExecContext](https://pkg.go.dev/database/sql#DB.ExecContext).
####  func (*DB) [¶](https://pkg.go.dev/database/sql#DB.ExecContext "Go to DB.ExecContext") added in go1.8
```
func (db *DB[](https://pkg.go.dev/database/sql#DB)) ExecContext(ctx context[](https://pkg.go.dev/context).Context[](https://pkg.go.dev/context#Context), query string[](https://pkg.go.dev/builtin#string), args ...any[](https://pkg.go.dev/builtin#any)) (Result[](https://pkg.go.dev/database/sql#Result), error[](https://pkg.go.dev/builtin#error))
```

ExecContext executes a query without returning any rows. The args are for any placeholder parameters in the query.
Example [¶](https://pkg.go.dev/database/sql#example-DB.ExecContext "Go to Example")
Share Format Run
####  func (*DB) [¶](https://pkg.go.dev/database/sql#DB.Ping "Go to DB.Ping") added in go1.1
```
func (db *DB[](https://pkg.go.dev/database/sql#DB)) Ping() error[](https://pkg.go.dev/builtin#error)
```

Ping verifies a connection to the database is still alive, establishing a connection if necessary.
Ping uses [context.Background](https://pkg.go.dev/context#Background) internally; to specify the context, use [DB.PingContext](https://pkg.go.dev/database/sql#DB.PingContext).
####  func (*DB) [¶](https://pkg.go.dev/database/sql#DB.PingContext "Go to DB.PingContext") added in go1.8
```
func (db *DB[](https://pkg.go.dev/database/sql#DB)) PingContext(ctx context[](https://pkg.go.dev/context).Context[](https://pkg.go.dev/context#Context)) error[](https://pkg.go.dev/builtin#error)
```

PingContext verifies a connection to the database is still alive, establishing a connection if necessary.
Example [¶](https://pkg.go.dev/database/sql#example-DB.PingContext "Go to Example")
Share Format Run
####  func (*DB) [¶](https://pkg.go.dev/database/sql#DB.Prepare "Go to DB.Prepare")
```
func (db *DB[](https://pkg.go.dev/database/sql#DB)) Prepare(query string[](https://pkg.go.dev/builtin#string)) (*Stmt[](https://pkg.go.dev/database/sql#Stmt), error[](https://pkg.go.dev/builtin#error))
```

Prepare creates a prepared statement for later queries or executions. Multiple queries or executions may be run concurrently from the returned statement. The caller must call the statement's [*Stmt.Close](https://pkg.go.dev/database/sql#Stmt.Close) method when the statement is no longer needed.
Prepare uses [context.Background](https://pkg.go.dev/context#Background) internally; to specify the context, use [DB.PrepareContext](https://pkg.go.dev/database/sql#DB.PrepareContext).
Example [¶](https://pkg.go.dev/database/sql#example-DB.Prepare "Go to Example")
Share Format Run
####  func (*DB) [¶](https://pkg.go.dev/database/sql#DB.PrepareContext "Go to DB.PrepareContext") added in go1.8
```
func (db *DB[](https://pkg.go.dev/database/sql#DB)) PrepareContext(ctx context[](https://pkg.go.dev/context).Context[](https://pkg.go.dev/context#Context), query string[](https://pkg.go.dev/builtin#string)) (*Stmt[](https://pkg.go.dev/database/sql#Stmt), error[](https://pkg.go.dev/builtin#error))
```

PrepareContext creates a prepared statement for later queries or executions. Multiple queries or executions may be run concurrently from the returned statement. The caller must call the statement's [*Stmt.Close](https://pkg.go.dev/database/sql#Stmt.Close) method when the statement is no longer needed.
The provided context is used for the preparation of the statement, not for the execution of the statement.
####  func (*DB) [¶](https://pkg.go.dev/database/sql#DB.Query "Go to DB.Query")
```
func (db *DB[](https://pkg.go.dev/database/sql#DB)) Query(query string[](https://pkg.go.dev/builtin#string), args ...any[](https://pkg.go.dev/builtin#any)) (*Rows[](https://pkg.go.dev/database/sql#Rows), error[](https://pkg.go.dev/builtin#error))
```

Query executes a query that returns rows, typically a SELECT. The args are for any placeholder parameters in the query.
Query uses [context.Background](https://pkg.go.dev/context#Background) internally; to specify the context, use [DB.QueryContext](https://pkg.go.dev/database/sql#DB.QueryContext).
Example (MultipleResultSets) [¶](https://pkg.go.dev/database/sql#example-DB.Query-MultipleResultSets "Go to Example \(MultipleResultSets\)")
Share Format Run
####  func (*DB) [¶](https://pkg.go.dev/database/sql#DB.QueryContext "Go to DB.QueryContext") added in go1.8
```
func (db *DB[](https://pkg.go.dev/database/sql#DB)) QueryContext(ctx context[](https://pkg.go.dev/context).Context[](https://pkg.go.dev/context#Context), query string[](https://pkg.go.dev/builtin#string), args ...any[](https://pkg.go.dev/builtin#any)) (*Rows[](https://pkg.go.dev/database/sql#Rows), error[](https://pkg.go.dev/builtin#error))
```

QueryContext executes a query that returns rows, typically a SELECT. The args are for any placeholder parameters in the query.
Example [¶](https://pkg.go.dev/database/sql#example-DB.QueryContext "Go to Example")
Share Format Run
####  func (*DB) [¶](https://pkg.go.dev/database/sql#DB.QueryRow "Go to DB.QueryRow")
```
func (db *DB[](https://pkg.go.dev/database/sql#DB)) QueryRow(query string[](https://pkg.go.dev/builtin#string), args ...any[](https://pkg.go.dev/builtin#any)) *Row[](https://pkg.go.dev/database/sql#Row)
```

QueryRow executes a query that is expected to return at most one row. QueryRow always returns a non-nil value. Errors are deferred until [Row](https://pkg.go.dev/database/sql#Row)'s Scan method is called. If the query selects no rows, the [*Row.Scan](https://pkg.go.dev/database/sql#Row.Scan) will return [ErrNoRows](https://pkg.go.dev/database/sql#ErrNoRows). Otherwise, [*Row.Scan](https://pkg.go.dev/database/sql#Row.Scan) scans the first selected row and discards the rest.
QueryRow uses [context.Background](https://pkg.go.dev/context#Background) internally; to specify the context, use [DB.QueryRowContext](https://pkg.go.dev/database/sql#DB.QueryRowContext).
####  func (*DB) [¶](https://pkg.go.dev/database/sql#DB.QueryRowContext "Go to DB.QueryRowContext") added in go1.8
```
func (db *DB[](https://pkg.go.dev/database/sql#DB)) QueryRowContext(ctx context[](https://pkg.go.dev/context).Context[](https://pkg.go.dev/context#Context), query string[](https://pkg.go.dev/builtin#string), args ...any[](https://pkg.go.dev/builtin#any)) *Row[](https://pkg.go.dev/database/sql#Row)
```

QueryRowContext executes a query that is expected to return at most one row. QueryRowContext always returns a non-nil value. Errors are deferred until [Row](https://pkg.go.dev/database/sql#Row)'s Scan method is called. If the query selects no rows, the [*Row.Scan](https://pkg.go.dev/database/sql#Row.Scan) will return [ErrNoRows](https://pkg.go.dev/database/sql#ErrNoRows). Otherwise, [*Row.Scan](https://pkg.go.dev/database/sql#Row.Scan) scans the first selected row and discards the rest.
Example [¶](https://pkg.go.dev/database/sql#example-DB.QueryRowContext "Go to Example")
Share Format Run
####  func (*DB) [¶](https://pkg.go.dev/database/sql#DB.SetConnMaxIdleTime "Go to DB.SetConnMaxIdleTime") added in go1.15
```
func (db *DB[](https://pkg.go.dev/database/sql#DB)) SetConnMaxIdleTime(d time[](https://pkg.go.dev/time).Duration[](https://pkg.go.dev/time#Duration))
```

SetConnMaxIdleTime sets the maximum amount of time a connection may be idle.
Expired connections may be closed lazily before reuse.
If d <= 0, connections are not closed due to a connection's idle time.
####  func (*DB) [¶](https://pkg.go.dev/database/sql#DB.SetConnMaxLifetime "Go to DB.SetConnMaxLifetime") added in go1.6
```
func (db *DB[](https://pkg.go.dev/database/sql#DB)) SetConnMaxLifetime(d time[](https://pkg.go.dev/time).Duration[](https://pkg.go.dev/time#Duration))
```

SetConnMaxLifetime sets the maximum amount of time a connection may be reused.
Expired connections may be closed lazily before reuse.
If d <= 0, connections are not closed due to a connection's age.
####  func (*DB) [¶](https://pkg.go.dev/database/sql#DB.SetMaxIdleConns "Go to DB.SetMaxIdleConns") added in go1.1
```
func (db *DB[](https://pkg.go.dev/database/sql#DB)) SetMaxIdleConns(n int[](https://pkg.go.dev/builtin#int))
```

SetMaxIdleConns sets the maximum number of connections in the idle connection pool.
If MaxOpenConns is greater than 0 but less than the new MaxIdleConns, then the new MaxIdleConns will be reduced to match the MaxOpenConns limit.
If n <= 0, no idle connections are retained.
The default max idle connections is currently 2. This may change in a future release.
####  func (*DB) [¶](https://pkg.go.dev/database/sql#DB.SetMaxOpenConns "Go to DB.SetMaxOpenConns") added in go1.2
```
func (db *DB[](https://pkg.go.dev/database/sql#DB)) SetMaxOpenConns(n int[](https://pkg.go.dev/builtin#int))
```

SetMaxOpenConns sets the maximum number of open connections to the database.
If MaxIdleConns is greater than 0 and the new MaxOpenConns is less than MaxIdleConns, then MaxIdleConns will be reduced to match the new MaxOpenConns limit.
If n <= 0, then there is no limit on the number of open connections. The default is 0 (unlimited).
####  func (*DB) [¶](https://pkg.go.dev/database/sql#DB.Stats "Go to DB.Stats") added in go1.5
```
func (db *DB[](https://pkg.go.dev/database/sql#DB)) Stats() DBStats[](https://pkg.go.dev/database/sql#DBStats)
```

Stats returns database statistics.
####  type [¶](https://pkg.go.dev/database/sql#DBStats "Go to DBStats") added in go1.5
```
type DBStats struct {
	MaxOpenConnections int[](https://pkg.go.dev/builtin#int) // Maximum number of open connections to the database.

	// Pool Status
	OpenConnections int[](https://pkg.go.dev/builtin#int) // The number of established connections both in use and idle.
	InUse           int[](https://pkg.go.dev/builtin#int) // The number of connections currently in use.
	Idle            int[](https://pkg.go.dev/builtin#int) // The number of idle connections.

	// Counters
	WaitCount         int64[](https://pkg.go.dev/builtin#int64)         // The total number of connections waited for.
	WaitDuration      time[](https://pkg.go.dev/time).Duration[](https://pkg.go.dev/time#Duration) // The total time blocked waiting for a new connection.
	MaxIdleClosed     int64[](https://pkg.go.dev/builtin#int64)         // The total number of connections closed due to SetMaxIdleConns.
	MaxIdleTimeClosed int64[](https://pkg.go.dev/builtin#int64)         // The total number of connections closed due to SetConnMaxIdleTime.
	MaxLifetimeClosed int64[](https://pkg.go.dev/builtin#int64)         // The total number of connections closed due to SetConnMaxLifetime.
}
```

DBStats contains database statistics.
####  type [¶](https://pkg.go.dev/database/sql#IsolationLevel "Go to IsolationLevel") added in go1.8
```
type IsolationLevel int[](https://pkg.go.dev/builtin#int)
```

IsolationLevel is the transaction isolation level used in [TxOptions](https://pkg.go.dev/database/sql#TxOptions).
```
const (
	LevelDefault IsolationLevel[](https://pkg.go.dev/database/sql#IsolationLevel) = iota[](https://pkg.go.dev/builtin#iota)
	LevelReadUncommitted
	LevelReadCommitted
	LevelWriteCommitted
	LevelRepeatableRead
	LevelSnapshot
	LevelSerializable
	LevelLinearizable
)
```

Various isolation levels that drivers may support in [DB.BeginTx](https://pkg.go.dev/database/sql#DB.BeginTx). If a driver does not support a given isolation level an error may be returned.
See
####  func (IsolationLevel) [¶](https://pkg.go.dev/database/sql#IsolationLevel.String "Go to IsolationLevel.String") added in go1.11
```
func (i IsolationLevel[](https://pkg.go.dev/database/sql#IsolationLevel)) String() string[](https://pkg.go.dev/builtin#string)
```

String returns the name of the transaction isolation level.
####  type [¶](https://pkg.go.dev/database/sql#NamedArg "Go to NamedArg") added in go1.8
```
type NamedArg struct {

	// Name is the name of the parameter placeholder.
	//
	// If empty, the ordinal position in the argument list will be
	// used.
	//
	// Name must omit any symbol prefix.
	Name string[](https://pkg.go.dev/builtin#string)

	// Value is the value of the parameter.
	// It may be assigned the same value types as the query
	// arguments.
	Value any[](https://pkg.go.dev/builtin#any)
	// contains filtered or unexported fields
}
```

A NamedArg is a named argument. NamedArg values may be used as arguments to [DB.Query](https://pkg.go.dev/database/sql#DB.Query) or [DB.Exec](https://pkg.go.dev/database/sql#DB.Exec) and bind to the corresponding named parameter in the SQL statement.
For a more concise way to create NamedArg values, see the [Named](https://pkg.go.dev/database/sql#Named) function.
####  func [¶](https://pkg.go.dev/database/sql#Named "Go to Named") added in go1.8
```
func Named(name string[](https://pkg.go.dev/builtin#string), value any[](https://pkg.go.dev/builtin#any)) NamedArg[](https://pkg.go.dev/database/sql#NamedArg)
```

Named provides a more concise way to create [NamedArg](https://pkg.go.dev/database/sql#NamedArg) values.
Example usage:
```
db.ExecContext(ctx, `
    delete from Invoice
    where
        TimeCreated < @end
        and TimeCreated >= @start;`,
    sql.Named("start", startTime),
    sql.Named("end", endTime),
)

```

####  type [¶](https://pkg.go.dev/database/sql#Null "Go to Null") added in go1.22.0
```
type Null[T any[](https://pkg.go.dev/builtin#any)] struct {
	V     T
	Valid bool[](https://pkg.go.dev/builtin#bool)
}
```

Null represents a value that may be null. Null implements the [Scanner](https://pkg.go.dev/database/sql#Scanner) interface so it can be used as a scan destination:
```
var s Null[string]
err := db.QueryRow("SELECT name FROM foo WHERE id=?", id).Scan(&s)
...
if s.Valid {
   // use s.V
} else {
   // NULL value
}

```

T should be one of the types accepted by [driver.Value](https://pkg.go.dev/database/sql/driver#Value).
####  func (*Null[T]) [¶](https://pkg.go.dev/database/sql#Null.Scan "Go to Null.Scan") added in go1.22.0
```
func (n *Null[](https://pkg.go.dev/database/sql#Null)[T]) Scan(value any[](https://pkg.go.dev/builtin#any)) error[](https://pkg.go.dev/builtin#error)
```

####  func (Null[T]) [¶](https://pkg.go.dev/database/sql#Null.Value "Go to Null.Value") added in go1.22.0
```
func (n Null[](https://pkg.go.dev/database/sql#Null)[T]) Value() (driver[](https://pkg.go.dev/database/sql/driver).Value[](https://pkg.go.dev/database/sql/driver#Value), error[](https://pkg.go.dev/builtin#error))
```

####  type [¶](https://pkg.go.dev/database/sql#NullBool "Go to NullBool")
```
type NullBool struct {
	Bool  bool[](https://pkg.go.dev/builtin#bool)
	Valid bool[](https://pkg.go.dev/builtin#bool) // Valid is true if Bool is not NULL
}
```

NullBool represents a bool that may be null. NullBool implements the [Scanner](https://pkg.go.dev/database/sql#Scanner) interface so it can be used as a scan destination, similar to [NullString](https://pkg.go.dev/database/sql#NullString).
####  func (*NullBool) [¶](https://pkg.go.dev/database/sql#NullBool.Scan "Go to NullBool.Scan")
```
func (n *NullBool[](https://pkg.go.dev/database/sql#NullBool)) Scan(value any[](https://pkg.go.dev/builtin#any)) error[](https://pkg.go.dev/builtin#error)
```

Scan implements the [Scanner](https://pkg.go.dev/database/sql#Scanner) interface.
####  func (NullBool) [¶](https://pkg.go.dev/database/sql#NullBool.Value "Go to NullBool.Value")
```
func (n NullBool[](https://pkg.go.dev/database/sql#NullBool)) Value() (driver[](https://pkg.go.dev/database/sql/driver).Value[](https://pkg.go.dev/database/sql/driver#Value), error[](https://pkg.go.dev/builtin#error))
```

Value implements the [driver.Valuer](https://pkg.go.dev/database/sql/driver#Valuer) interface.
####  type [¶](https://pkg.go.dev/database/sql#NullByte "Go to NullByte") added in go1.17
```
type NullByte struct {
	Byte  byte[](https://pkg.go.dev/builtin#byte)
	Valid bool[](https://pkg.go.dev/builtin#bool) // Valid is true if Byte is not NULL
}
```

NullByte represents a byte that may be null. NullByte implements the [Scanner](https://pkg.go.dev/database/sql#Scanner) interface so it can be used as a scan destination, similar to [NullString](https://pkg.go.dev/database/sql#NullString).
####  func (*NullByte) [¶](https://pkg.go.dev/database/sql#NullByte.Scan "Go to NullByte.Scan") added in go1.17
```
func (n *NullByte[](https://pkg.go.dev/database/sql#NullByte)) Scan(value any[](https://pkg.go.dev/builtin#any)) error[](https://pkg.go.dev/builtin#error)
```

Scan implements the [Scanner](https://pkg.go.dev/database/sql#Scanner) interface.
####  func (NullByte) [¶](https://pkg.go.dev/database/sql#NullByte.Value "Go to NullByte.Value") added in go1.17
```
func (n NullByte[](https://pkg.go.dev/database/sql#NullByte)) Value() (driver[](https://pkg.go.dev/database/sql/driver).Value[](https://pkg.go.dev/database/sql/driver#Value), error[](https://pkg.go.dev/builtin#error))
```

Value implements the [driver.Valuer](https://pkg.go.dev/database/sql/driver#Valuer) interface.
####  type [¶](https://pkg.go.dev/database/sql#NullFloat64 "Go to NullFloat64")
```
type NullFloat64 struct {
	Float64 float64[](https://pkg.go.dev/builtin#float64)
	Valid   bool[](https://pkg.go.dev/builtin#bool) // Valid is true if Float64 is not NULL
}
```

NullFloat64 represents a float64 that may be null. NullFloat64 implements the [Scanner](https://pkg.go.dev/database/sql#Scanner) interface so it can be used as a scan destination, similar to [NullString](https://pkg.go.dev/database/sql#NullString).
####  func (*NullFloat64) [¶](https://pkg.go.dev/database/sql#NullFloat64.Scan "Go to NullFloat64.Scan")
```
func (n *NullFloat64[](https://pkg.go.dev/database/sql#NullFloat64)) Scan(value any[](https://pkg.go.dev/builtin#any)) error[](https://pkg.go.dev/builtin#error)
```

Scan implements the [Scanner](https://pkg.go.dev/database/sql#Scanner) interface.
####  func (NullFloat64) [¶](https://pkg.go.dev/database/sql#NullFloat64.Value "Go to NullFloat64.Value")
```
func (n NullFloat64[](https://pkg.go.dev/database/sql#NullFloat64)) Value() (driver[](https://pkg.go.dev/database/sql/driver).Value[](https://pkg.go.dev/database/sql/driver#Value), error[](https://pkg.go.dev/builtin#error))
```

Value implements the [driver.Valuer](https://pkg.go.dev/database/sql/driver#Valuer) interface.
####  type [¶](https://pkg.go.dev/database/sql#NullInt16 "Go to NullInt16") added in go1.17
```
type NullInt16 struct {
	Int16 int16[](https://pkg.go.dev/builtin#int16)
	Valid bool[](https://pkg.go.dev/builtin#bool) // Valid is true if Int16 is not NULL
}
```

NullInt16 represents an int16 that may be null. NullInt16 implements the [Scanner](https://pkg.go.dev/database/sql#Scanner) interface so it can be used as a scan destination, similar to [NullString](https://pkg.go.dev/database/sql#NullString).
####  func (*NullInt16) [¶](https://pkg.go.dev/database/sql#NullInt16.Scan "Go to NullInt16.Scan") added in go1.17
```
func (n *NullInt16[](https://pkg.go.dev/database/sql#NullInt16)) Scan(value any[](https://pkg.go.dev/builtin#any)) error[](https://pkg.go.dev/builtin#error)
```

Scan implements the [Scanner](https://pkg.go.dev/database/sql#Scanner) interface.
####  func (NullInt16) [¶](https://pkg.go.dev/database/sql#NullInt16.Value "Go to NullInt16.Value") added in go1.17
```
func (n NullInt16[](https://pkg.go.dev/database/sql#NullInt16)) Value() (driver[](https://pkg.go.dev/database/sql/driver).Value[](https://pkg.go.dev/database/sql/driver#Value), error[](https://pkg.go.dev/builtin#error))
```

Value implements the [driver.Valuer](https://pkg.go.dev/database/sql/driver#Valuer) interface.
####  type [¶](https://pkg.go.dev/database/sql#NullInt32 "Go to NullInt32") added in go1.13
```
type NullInt32 struct {
	Int32 int32[](https://pkg.go.dev/builtin#int32)
