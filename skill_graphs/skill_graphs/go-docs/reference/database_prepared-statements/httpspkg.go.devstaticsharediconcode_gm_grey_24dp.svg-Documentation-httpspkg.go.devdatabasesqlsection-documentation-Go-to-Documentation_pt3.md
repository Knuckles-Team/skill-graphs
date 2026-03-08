	Valid bool[](https://pkg.go.dev/builtin#bool) // Valid is true if Int32 is not NULL
}
```

NullInt32 represents an int32 that may be null. NullInt32 implements the [Scanner](https://pkg.go.dev/database/sql#Scanner) interface so it can be used as a scan destination, similar to [NullString](https://pkg.go.dev/database/sql#NullString).
####  func (*NullInt32) [¶](https://pkg.go.dev/database/sql#NullInt32.Scan "Go to NullInt32.Scan") added in go1.13
```
func (n *NullInt32[](https://pkg.go.dev/database/sql#NullInt32)) Scan(value any[](https://pkg.go.dev/builtin#any)) error[](https://pkg.go.dev/builtin#error)
```

Scan implements the [Scanner](https://pkg.go.dev/database/sql#Scanner) interface.
####  func (NullInt32) [¶](https://pkg.go.dev/database/sql#NullInt32.Value "Go to NullInt32.Value") added in go1.13
```
func (n NullInt32[](https://pkg.go.dev/database/sql#NullInt32)) Value() (driver[](https://pkg.go.dev/database/sql/driver).Value[](https://pkg.go.dev/database/sql/driver#Value), error[](https://pkg.go.dev/builtin#error))
```

Value implements the [driver.Valuer](https://pkg.go.dev/database/sql/driver#Valuer) interface.
####  type [¶](https://pkg.go.dev/database/sql#NullInt64 "Go to NullInt64")
```
type NullInt64 struct {
	Int64 int64[](https://pkg.go.dev/builtin#int64)
	Valid bool[](https://pkg.go.dev/builtin#bool) // Valid is true if Int64 is not NULL
}
```

NullInt64 represents an int64 that may be null. NullInt64 implements the [Scanner](https://pkg.go.dev/database/sql#Scanner) interface so it can be used as a scan destination, similar to [NullString](https://pkg.go.dev/database/sql#NullString).
####  func (*NullInt64) [¶](https://pkg.go.dev/database/sql#NullInt64.Scan "Go to NullInt64.Scan")
```
func (n *NullInt64[](https://pkg.go.dev/database/sql#NullInt64)) Scan(value any[](https://pkg.go.dev/builtin#any)) error[](https://pkg.go.dev/builtin#error)
```

Scan implements the [Scanner](https://pkg.go.dev/database/sql#Scanner) interface.
####  func (NullInt64) [¶](https://pkg.go.dev/database/sql#NullInt64.Value "Go to NullInt64.Value")
```
func (n NullInt64[](https://pkg.go.dev/database/sql#NullInt64)) Value() (driver[](https://pkg.go.dev/database/sql/driver).Value[](https://pkg.go.dev/database/sql/driver#Value), error[](https://pkg.go.dev/builtin#error))
```

Value implements the [driver.Valuer](https://pkg.go.dev/database/sql/driver#Valuer) interface.
####  type [¶](https://pkg.go.dev/database/sql#NullString "Go to NullString")
```
type NullString struct {
	String string[](https://pkg.go.dev/builtin#string)
	Valid  bool[](https://pkg.go.dev/builtin#bool) // Valid is true if String is not NULL
}
```

NullString represents a string that may be null. NullString implements the [Scanner](https://pkg.go.dev/database/sql#Scanner) interface so it can be used as a scan destination:
```
var s NullString
err := db.QueryRow("SELECT name FROM foo WHERE id=?", id).Scan(&s)
...
if s.Valid {
   // use s.String
} else {
   // NULL value
}

```

####  func (*NullString) [¶](https://pkg.go.dev/database/sql#NullString.Scan "Go to NullString.Scan")
```
func (ns *NullString[](https://pkg.go.dev/database/sql#NullString)) Scan(value any[](https://pkg.go.dev/builtin#any)) error[](https://pkg.go.dev/builtin#error)
```

Scan implements the [Scanner](https://pkg.go.dev/database/sql#Scanner) interface.
####  func (NullString) [¶](https://pkg.go.dev/database/sql#NullString.Value "Go to NullString.Value")
```
func (ns NullString[](https://pkg.go.dev/database/sql#NullString)) Value() (driver[](https://pkg.go.dev/database/sql/driver).Value[](https://pkg.go.dev/database/sql/driver#Value), error[](https://pkg.go.dev/builtin#error))
```

Value implements the [driver.Valuer](https://pkg.go.dev/database/sql/driver#Valuer) interface.
####  type [¶](https://pkg.go.dev/database/sql#NullTime "Go to NullTime") added in go1.13
```
type NullTime struct {
	Time  time[](https://pkg.go.dev/time).Time[](https://pkg.go.dev/time#Time)
	Valid bool[](https://pkg.go.dev/builtin#bool) // Valid is true if Time is not NULL
}
```

NullTime represents a [time.Time](https://pkg.go.dev/time#Time) that may be null. NullTime implements the [Scanner](https://pkg.go.dev/database/sql#Scanner) interface so it can be used as a scan destination, similar to [NullString](https://pkg.go.dev/database/sql#NullString).
####  func (*NullTime) [¶](https://pkg.go.dev/database/sql#NullTime.Scan "Go to NullTime.Scan") added in go1.13
```
func (n *NullTime[](https://pkg.go.dev/database/sql#NullTime)) Scan(value any[](https://pkg.go.dev/builtin#any)) error[](https://pkg.go.dev/builtin#error)
```

Scan implements the [Scanner](https://pkg.go.dev/database/sql#Scanner) interface.
####  func (NullTime) [¶](https://pkg.go.dev/database/sql#NullTime.Value "Go to NullTime.Value") added in go1.13
```
func (n NullTime[](https://pkg.go.dev/database/sql#NullTime)) Value() (driver[](https://pkg.go.dev/database/sql/driver).Value[](https://pkg.go.dev/database/sql/driver#Value), error[](https://pkg.go.dev/builtin#error))
```

Value implements the [driver.Valuer](https://pkg.go.dev/database/sql/driver#Valuer) interface.
####  type [¶](https://pkg.go.dev/database/sql#Out "Go to Out") added in go1.9
```
type Out struct {

	// Dest is a pointer to the value that will be set to the result of the
	// stored procedure's OUTPUT parameter.
	Dest any[](https://pkg.go.dev/builtin#any)

	// In is whether the parameter is an INOUT parameter. If so, the input value to the stored
	// procedure is the dereferenced value of Dest's pointer, which is then replaced with
	// the output value.
	In bool[](https://pkg.go.dev/builtin#bool)
	// contains filtered or unexported fields
}
```

Out may be used to retrieve OUTPUT value parameters from stored procedures.
Not all drivers and databases support OUTPUT value parameters.
Example usage:
```
var outArg string
_, err := db.ExecContext(ctx, "ProcName", sql.Named("Arg1", sql.Out{Dest: &outArg}))

```

####  type [¶](https://pkg.go.dev/database/sql#RawBytes "Go to RawBytes")
```
type RawBytes []byte[](https://pkg.go.dev/builtin#byte)
```

RawBytes is a byte slice that holds a reference to memory owned by the database itself. After a [Rows.Scan](https://pkg.go.dev/database/sql#Rows.Scan) into a RawBytes, the slice is only valid until the next call to [Rows.Next](https://pkg.go.dev/database/sql#Rows.Next), [Rows.Scan](https://pkg.go.dev/database/sql#Rows.Scan), or [Rows.Close](https://pkg.go.dev/database/sql#Rows.Close).
####  type [¶](https://pkg.go.dev/database/sql#Result "Go to Result")
```
type Result interface {
	// LastInsertId returns the integer generated by the database
	// in response to a command. Typically this will be from an
	// "auto increment" column when inserting a new row. Not all
	// databases support this feature, and the syntax of such
	// statements varies.
	LastInsertId() (int64[](https://pkg.go.dev/builtin#int64), error[](https://pkg.go.dev/builtin#error))

	// RowsAffected returns the number of rows affected by an
	// update, insert, or delete. Not every database or database
	// driver may support this.
	RowsAffected() (int64[](https://pkg.go.dev/builtin#int64), error[](https://pkg.go.dev/builtin#error))
}
```

A Result summarizes an executed SQL command.
####  type [¶](https://pkg.go.dev/database/sql#Row "Go to Row")
```
type Row struct {
	// contains filtered or unexported fields
}
```

Row is the result of calling [DB.QueryRow](https://pkg.go.dev/database/sql#DB.QueryRow) to select a single row.
####  func (*Row) [¶](https://pkg.go.dev/database/sql#Row.Err "Go to Row.Err") added in go1.15
```
func (r *Row[](https://pkg.go.dev/database/sql#Row)) Err() error[](https://pkg.go.dev/builtin#error)
```

Err provides a way for wrapping packages to check for query errors without calling [Row.Scan](https://pkg.go.dev/database/sql#Row.Scan). Err returns the error, if any, that was encountered while running the query. If this error is not nil, this error will also be returned from [Row.Scan](https://pkg.go.dev/database/sql#Row.Scan).
####  func (*Row) [¶](https://pkg.go.dev/database/sql#Row.Scan "Go to Row.Scan")
```
func (r *Row[](https://pkg.go.dev/database/sql#Row)) Scan(dest ...any[](https://pkg.go.dev/builtin#any)) error[](https://pkg.go.dev/builtin#error)
```

Scan copies the columns from the matched row into the values pointed at by dest. See the documentation on [Rows.Scan](https://pkg.go.dev/database/sql#Rows.Scan) for details. If more than one row matches the query, Scan uses the first row and discards the rest. If no row matches the query, Scan returns [ErrNoRows](https://pkg.go.dev/database/sql#ErrNoRows).
####  type [¶](https://pkg.go.dev/database/sql#Rows "Go to Rows")
```
type Rows struct {
	// contains filtered or unexported fields
}
```

Rows is the result of a query. Its cursor starts before the first row of the result set. Use [Rows.Next](https://pkg.go.dev/database/sql#Rows.Next) to advance from row to row.
Example [¶](https://pkg.go.dev/database/sql#example-Rows "Go to Example")
Share Format Run
####  func (*Rows) [¶](https://pkg.go.dev/database/sql#Rows.Close "Go to Rows.Close")
```
func (rs *Rows[](https://pkg.go.dev/database/sql#Rows)) Close() error[](https://pkg.go.dev/builtin#error)
```

Close closes the [Rows](https://pkg.go.dev/database/sql#Rows), preventing further enumeration. If [Rows.Next](https://pkg.go.dev/database/sql#Rows.Next) is called and returns false and there are no further result sets, the [Rows](https://pkg.go.dev/database/sql#Rows) are closed automatically and it will suffice to check the result of [Rows.Err](https://pkg.go.dev/database/sql#Rows.Err). Close is idempotent and does not affect the result of [Rows.Err](https://pkg.go.dev/database/sql#Rows.Err).
####  func (*Rows) [¶](https://pkg.go.dev/database/sql#Rows.ColumnTypes "Go to Rows.ColumnTypes") added in go1.8
```
func (rs *Rows[](https://pkg.go.dev/database/sql#Rows)) ColumnTypes() ([]*ColumnType[](https://pkg.go.dev/database/sql#ColumnType), error[](https://pkg.go.dev/builtin#error))
```

ColumnTypes returns column information such as column type, length, and nullable. Some information may not be available from some drivers.
####  func (*Rows) [¶](https://pkg.go.dev/database/sql#Rows.Columns "Go to Rows.Columns")
```
func (rs *Rows[](https://pkg.go.dev/database/sql#Rows)) Columns() ([]string[](https://pkg.go.dev/builtin#string), error[](https://pkg.go.dev/builtin#error))
```

Columns returns the column names. Columns returns an error if the rows are closed.
####  func (*Rows) [¶](https://pkg.go.dev/database/sql#Rows.Err "Go to Rows.Err")
```
func (rs *Rows[](https://pkg.go.dev/database/sql#Rows)) Err() error[](https://pkg.go.dev/builtin#error)
```

Err returns the error, if any, that was encountered during iteration. Err may be called after an explicit or implicit [Rows.Close](https://pkg.go.dev/database/sql#Rows.Close).
####  func (*Rows) [¶](https://pkg.go.dev/database/sql#Rows.Next "Go to Rows.Next")
```
func (rs *Rows[](https://pkg.go.dev/database/sql#Rows)) Next() bool[](https://pkg.go.dev/builtin#bool)
```

Next prepares the next result row for reading with the [Rows.Scan](https://pkg.go.dev/database/sql#Rows.Scan) method. It returns true on success, or false if there is no next result row or an error happened while preparing it. [Rows.Err](https://pkg.go.dev/database/sql#Rows.Err) should be consulted to distinguish between the two cases.
Every call to [Rows.Scan](https://pkg.go.dev/database/sql#Rows.Scan), even the first one, must be preceded by a call to [Rows.Next](https://pkg.go.dev/database/sql#Rows.Next).
####  func (*Rows) [¶](https://pkg.go.dev/database/sql#Rows.NextResultSet "Go to Rows.NextResultSet") added in go1.8
```
func (rs *Rows[](https://pkg.go.dev/database/sql#Rows)) NextResultSet() bool[](https://pkg.go.dev/builtin#bool)
```

NextResultSet prepares the next result set for reading. It reports whether there is further result sets, or false if there is no further result set or if there is an error advancing to it. The [Rows.Err](https://pkg.go.dev/database/sql#Rows.Err) method should be consulted to distinguish between the two cases.
After calling NextResultSet, the [Rows.Next](https://pkg.go.dev/database/sql#Rows.Next) method should always be called before scanning. If there are further result sets they may not have rows in the result set.
####  func (*Rows) [¶](https://pkg.go.dev/database/sql#Rows.Scan "Go to Rows.Scan")
```
func (rs *Rows[](https://pkg.go.dev/database/sql#Rows)) Scan(dest ...any[](https://pkg.go.dev/builtin#any)) error[](https://pkg.go.dev/builtin#error)
```

Scan copies the columns in the current row into the values pointed at by dest. The number of values in dest must be the same as the number of columns in [Rows](https://pkg.go.dev/database/sql#Rows).
Scan converts columns read from the database into the following common Go types and special types provided by the sql package:
```
*string
*[]byte
*int, *int8, *int16, *int32, *int64
*uint, *uint8, *uint16, *uint32, *uint64
*bool
*float32, *float64
*interface{}
*RawBytes
*Rows (cursor value)
any type implementing Scanner (see Scanner docs)

```

In the most simple case, if the type of the value from the source column is an integer, bool or string type T and dest is of type *T, Scan simply assigns the value through the pointer.
Scan also converts between string and numeric types, as long as no information would be lost. While Scan stringifies all numbers scanned from numeric database columns into *string, scans into numeric types are checked for overflow. For example, a float64 with value 300 or a string with value "300" can scan into a uint16, but not into a uint8, though float64(255) or "255" can scan into a uint8. One exception is that scans of some float64 numbers to strings may lose information when stringifying. In general, scan floating point columns into *float64.
If a dest argument has type *[]byte, Scan saves in that argument a copy of the corresponding data. The copy is owned by the caller and can be modified and held indefinitely. The copy can be avoided by using an argument of type [*RawBytes](https://pkg.go.dev/database/sql#RawBytes) instead; see the documentation for [RawBytes](https://pkg.go.dev/database/sql#RawBytes) for restrictions on its use.
If an argument has type *interface{}, Scan copies the value provided by the underlying driver without conversion. When scanning from a source value of type []byte to *interface{}, a copy of the slice is made and the caller owns the result.
Source values of type [time.Time](https://pkg.go.dev/time#Time) may be scanned into values of type *time.Time, *interface{}, *string, or *[]byte. When converting to the latter two, [time.RFC3339Nano](https://pkg.go.dev/time#RFC3339Nano) is used.
Source values of type bool may be scanned into types *bool, *interface{}, *string, *[]byte, or [*RawBytes](https://pkg.go.dev/database/sql#RawBytes).
For scanning into *bool, the source may be true, false, 1, 0, or string inputs parseable by [strconv.ParseBool](https://pkg.go.dev/strconv#ParseBool).
Scan can also convert a cursor returned from a query, such as "select cursor(select * from my_table) from dual", into a [*Rows](https://pkg.go.dev/database/sql#Rows) value that can itself be scanned from. The parent select query will close any cursor [*Rows](https://pkg.go.dev/database/sql#Rows) if the parent [*Rows](https://pkg.go.dev/database/sql#Rows) is closed.
If any of the first arguments implementing [Scanner](https://pkg.go.dev/database/sql#Scanner) returns an error, that error will be wrapped in the returned error.
####  type [¶](https://pkg.go.dev/database/sql#Scanner "Go to Scanner")
```
type Scanner interface {
	// Scan assigns a value from a database driver.
	//
	// The src value will be of one of the following types:
	//
	//    int64
	//    float64
	//    bool
	//    []byte
	//    string
	//    time.Time
	//    nil - for NULL values
	//
	// An error should be returned if the value cannot be stored
	// without loss of information.
	//
	// Reference types such as []byte are only valid until the next call to Scan
	// and should not be retained. Their underlying memory is owned by the driver.
	// If retention is necessary, copy their values before the next call to Scan.
	Scan(src any[](https://pkg.go.dev/builtin#any)) error[](https://pkg.go.dev/builtin#error)
}
```

Scanner is an interface used by [Rows.Scan](https://pkg.go.dev/database/sql#Rows.Scan).
####  type [¶](https://pkg.go.dev/database/sql#Stmt "Go to Stmt")
```
type Stmt struct {
	// contains filtered or unexported fields
}
```

Stmt is a prepared statement. A Stmt is safe for concurrent use by multiple goroutines.
If a Stmt is prepared on a [Tx](https://pkg.go.dev/database/sql#Tx) or [Conn](https://pkg.go.dev/database/sql#Conn), it will be bound to a single underlying connection forever. If the [Tx](https://pkg.go.dev/database/sql#Tx) or [Conn](https://pkg.go.dev/database/sql#Conn) closes, the Stmt will become unusable and all operations will return an error. If a Stmt is prepared on a [DB](https://pkg.go.dev/database/sql#DB), it will remain usable for the lifetime of the [DB](https://pkg.go.dev/database/sql#DB). When the Stmt needs to execute on a new underlying connection, it will prepare itself on the new connection automatically.
Example [¶](https://pkg.go.dev/database/sql#example-Stmt "Go to Example")
Share Format Run
####  func (*Stmt) [¶](https://pkg.go.dev/database/sql#Stmt.Close "Go to Stmt.Close")
```
func (s *Stmt[](https://pkg.go.dev/database/sql#Stmt)) Close() error[](https://pkg.go.dev/builtin#error)
```

Close closes the statement.
####  func (*Stmt) [¶](https://pkg.go.dev/database/sql#Stmt.Exec "Go to Stmt.Exec")
```
func (s *Stmt[](https://pkg.go.dev/database/sql#Stmt)) Exec(args ...any[](https://pkg.go.dev/builtin#any)) (Result[](https://pkg.go.dev/database/sql#Result), error[](https://pkg.go.dev/builtin#error))
```

Exec executes a prepared statement with the given arguments and returns a [Result](https://pkg.go.dev/database/sql#Result) summarizing the effect of the statement.
Exec uses [context.Background](https://pkg.go.dev/context#Background) internally; to specify the context, use [Stmt.ExecContext](https://pkg.go.dev/database/sql#Stmt.ExecContext).
####  func (*Stmt) [¶](https://pkg.go.dev/database/sql#Stmt.ExecContext "Go to Stmt.ExecContext") added in go1.8
```
func (s *Stmt[](https://pkg.go.dev/database/sql#Stmt)) ExecContext(ctx context[](https://pkg.go.dev/context).Context[](https://pkg.go.dev/context#Context), args ...any[](https://pkg.go.dev/builtin#any)) (Result[](https://pkg.go.dev/database/sql#Result), error[](https://pkg.go.dev/builtin#error))
```

ExecContext executes a prepared statement with the given arguments and returns a [Result](https://pkg.go.dev/database/sql#Result) summarizing the effect of the statement.
####  func (*Stmt) [¶](https://pkg.go.dev/database/sql#Stmt.Query "Go to Stmt.Query")
```
func (s *Stmt[](https://pkg.go.dev/database/sql#Stmt)) Query(args ...any[](https://pkg.go.dev/builtin#any)) (*Rows[](https://pkg.go.dev/database/sql#Rows), error[](https://pkg.go.dev/builtin#error))
```

Query executes a prepared query statement with the given arguments and returns the query results as a *Rows.
Query uses [context.Background](https://pkg.go.dev/context#Background) internally; to specify the context, use [Stmt.QueryContext](https://pkg.go.dev/database/sql#Stmt.QueryContext).
####  func (*Stmt) [¶](https://pkg.go.dev/database/sql#Stmt.QueryContext "Go to Stmt.QueryContext") added in go1.8
```
func (s *Stmt[](https://pkg.go.dev/database/sql#Stmt)) QueryContext(ctx context[](https://pkg.go.dev/context).Context[](https://pkg.go.dev/context#Context), args ...any[](https://pkg.go.dev/builtin#any)) (*Rows[](https://pkg.go.dev/database/sql#Rows), error[](https://pkg.go.dev/builtin#error))
```

QueryContext executes a prepared query statement with the given arguments and returns the query results as a [*Rows](https://pkg.go.dev/database/sql#Rows).
####  func (*Stmt) [¶](https://pkg.go.dev/database/sql#Stmt.QueryRow "Go to Stmt.QueryRow")
```
func (s *Stmt[](https://pkg.go.dev/database/sql#Stmt)) QueryRow(args ...any[](https://pkg.go.dev/builtin#any)) *Row[](https://pkg.go.dev/database/sql#Row)
```

QueryRow executes a prepared query statement with the given arguments. If an error occurs during the execution of the statement, that error will be returned by a call to Scan on the returned [*Row](https://pkg.go.dev/database/sql#Row), which is always non-nil. If the query selects no rows, the [*Row.Scan](https://pkg.go.dev/database/sql#Row.Scan) will return [ErrNoRows](https://pkg.go.dev/database/sql#ErrNoRows). Otherwise, the [*Row.Scan](https://pkg.go.dev/database/sql#Row.Scan) scans the first selected row and discards the rest.
Example usage:
```
var name string
err := nameByUseridStmt.QueryRow(id).Scan(&name)

```

QueryRow uses [context.Background](https://pkg.go.dev/context#Background) internally; to specify the context, use [Stmt.QueryRowContext](https://pkg.go.dev/database/sql#Stmt.QueryRowContext).
####  func (*Stmt) [¶](https://pkg.go.dev/database/sql#Stmt.QueryRowContext "Go to Stmt.QueryRowContext") added in go1.8
```
func (s *Stmt[](https://pkg.go.dev/database/sql#Stmt)) QueryRowContext(ctx context[](https://pkg.go.dev/context).Context[](https://pkg.go.dev/context#Context), args ...any[](https://pkg.go.dev/builtin#any)) *Row[](https://pkg.go.dev/database/sql#Row)
```

QueryRowContext executes a prepared query statement with the given arguments. If an error occurs during the execution of the statement, that error will be returned by a call to Scan on the returned [*Row](https://pkg.go.dev/database/sql#Row), which is always non-nil. If the query selects no rows, the [*Row.Scan](https://pkg.go.dev/database/sql#Row.Scan) will return [ErrNoRows](https://pkg.go.dev/database/sql#ErrNoRows). Otherwise, the [*Row.Scan](https://pkg.go.dev/database/sql#Row.Scan) scans the first selected row and discards the rest.
Example [¶](https://pkg.go.dev/database/sql#example-Stmt.QueryRowContext "Go to Example")
Share Format Run
####  type [¶](https://pkg.go.dev/database/sql#Tx "Go to Tx")
```
type Tx struct {
	// contains filtered or unexported fields
}
```

Tx is an in-progress database transaction.
A transaction must end with a call to [Tx.Commit](https://pkg.go.dev/database/sql#Tx.Commit) or [Tx.Rollback](https://pkg.go.dev/database/sql#Tx.Rollback).
After a call to [Tx.Commit](https://pkg.go.dev/database/sql#Tx.Commit) or [Tx.Rollback](https://pkg.go.dev/database/sql#Tx.Rollback), all operations on the transaction fail with [ErrTxDone](https://pkg.go.dev/database/sql#ErrTxDone).
The statements prepared for a transaction by calling the transaction's [Tx.Prepare](https://pkg.go.dev/database/sql#Tx.Prepare) or [Tx.Stmt](https://pkg.go.dev/database/sql#Tx.Stmt) methods are closed by the call to [Tx.Commit](https://pkg.go.dev/database/sql#Tx.Commit) or [Tx.Rollback](https://pkg.go.dev/database/sql#Tx.Rollback).
####  func (*Tx) [¶](https://pkg.go.dev/database/sql#Tx.Commit "Go to Tx.Commit")
```
func (tx *Tx[](https://pkg.go.dev/database/sql#Tx)) Commit() error[](https://pkg.go.dev/builtin#error)
```

Commit commits the transaction.
####  func (*Tx) [¶](https://pkg.go.dev/database/sql#Tx.Exec "Go to Tx.Exec")
```
func (tx *Tx[](https://pkg.go.dev/database/sql#Tx)) Exec(query string[](https://pkg.go.dev/builtin#string), args ...any[](https://pkg.go.dev/builtin#any)) (Result[](https://pkg.go.dev/database/sql#Result), error[](https://pkg.go.dev/builtin#error))
```

Exec executes a query that doesn't return rows. For example: an INSERT and UPDATE.
Exec uses [context.Background](https://pkg.go.dev/context#Background) internally; to specify the context, use [Tx.ExecContext](https://pkg.go.dev/database/sql#Tx.ExecContext).
####  func (*Tx) [¶](https://pkg.go.dev/database/sql#Tx.ExecContext "Go to Tx.ExecContext") added in go1.8
```
func (tx *Tx[](https://pkg.go.dev/database/sql#Tx)) ExecContext(ctx context[](https://pkg.go.dev/context).Context[](https://pkg.go.dev/context#Context), query string[](https://pkg.go.dev/builtin#string), args ...any[](https://pkg.go.dev/builtin#any)) (Result[](https://pkg.go.dev/database/sql#Result), error[](https://pkg.go.dev/builtin#error))
```

ExecContext executes a query that doesn't return rows. For example: an INSERT and UPDATE.
Example [¶](https://pkg.go.dev/database/sql#example-Tx.ExecContext "Go to Example")
Share Format Run
####  func (*Tx) [¶](https://pkg.go.dev/database/sql#Tx.Prepare "Go to Tx.Prepare")
```
func (tx *Tx[](https://pkg.go.dev/database/sql#Tx)) Prepare(query string[](https://pkg.go.dev/builtin#string)) (*Stmt[](https://pkg.go.dev/database/sql#Stmt), error[](https://pkg.go.dev/builtin#error))
```

Prepare creates a prepared statement for use within a transaction.
The returned statement operates within the transaction and will be closed when the transaction has been committed or rolled back.
To use an existing prepared statement on this transaction, see [Tx.Stmt](https://pkg.go.dev/database/sql#Tx.Stmt).
Prepare uses [context.Background](https://pkg.go.dev/context#Background) internally; to specify the context, use [Tx.PrepareContext](https://pkg.go.dev/database/sql#Tx.PrepareContext).
Example [¶](https://pkg.go.dev/database/sql#example-Tx.Prepare "Go to Example")
Share Format Run
####  func (*Tx) [¶](https://pkg.go.dev/database/sql#Tx.PrepareContext "Go to Tx.PrepareContext") added in go1.8
