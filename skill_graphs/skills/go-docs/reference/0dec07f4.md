```
func (tx *Tx[](https://pkg.go.dev/database/sql#Tx)) PrepareContext(ctx context[](https://pkg.go.dev/context).Context[](https://pkg.go.dev/context#Context), query string[](https://pkg.go.dev/builtin#string)) (*Stmt[](https://pkg.go.dev/database/sql#Stmt), error[](https://pkg.go.dev/builtin#error))
```

PrepareContext creates a prepared statement for use within a transaction.
The returned statement operates within the transaction and will be closed when the transaction has been committed or rolled back.
To use an existing prepared statement on this transaction, see [Tx.Stmt](https://pkg.go.dev/database/sql#Tx.Stmt).
The provided context will be used for the preparation of the context, not for the execution of the returned statement. The returned statement will run in the transaction context.
####  func (*Tx) [¶](https://pkg.go.dev/database/sql#Tx.Query "Go to Tx.Query")
```
func (tx *Tx[](https://pkg.go.dev/database/sql#Tx)) Query(query string[](https://pkg.go.dev/builtin#string), args ...any[](https://pkg.go.dev/builtin#any)) (*Rows[](https://pkg.go.dev/database/sql#Rows), error[](https://pkg.go.dev/builtin#error))
```

Query executes a query that returns rows, typically a SELECT.
Query uses [context.Background](https://pkg.go.dev/context#Background) internally; to specify the context, use [Tx.QueryContext](https://pkg.go.dev/database/sql#Tx.QueryContext).
####  func (*Tx) [¶](https://pkg.go.dev/database/sql#Tx.QueryContext "Go to Tx.QueryContext") added in go1.8
```
func (tx *Tx[](https://pkg.go.dev/database/sql#Tx)) QueryContext(ctx context[](https://pkg.go.dev/context).Context[](https://pkg.go.dev/context#Context), query string[](https://pkg.go.dev/builtin#string), args ...any[](https://pkg.go.dev/builtin#any)) (*Rows[](https://pkg.go.dev/database/sql#Rows), error[](https://pkg.go.dev/builtin#error))
```

QueryContext executes a query that returns rows, typically a SELECT.
####  func (*Tx) [¶](https://pkg.go.dev/database/sql#Tx.QueryRow "Go to Tx.QueryRow")
```
func (tx *Tx[](https://pkg.go.dev/database/sql#Tx)) QueryRow(query string[](https://pkg.go.dev/builtin#string), args ...any[](https://pkg.go.dev/builtin#any)) *Row[](https://pkg.go.dev/database/sql#Row)
```

QueryRow executes a query that is expected to return at most one row. QueryRow always returns a non-nil value. Errors are deferred until [Row](https://pkg.go.dev/database/sql#Row)'s Scan method is called. If the query selects no rows, the [*Row.Scan](https://pkg.go.dev/database/sql#Row.Scan) will return [ErrNoRows](https://pkg.go.dev/database/sql#ErrNoRows). Otherwise, the [*Row.Scan](https://pkg.go.dev/database/sql#Row.Scan) scans the first selected row and discards the rest.
QueryRow uses [context.Background](https://pkg.go.dev/context#Background) internally; to specify the context, use [Tx.QueryRowContext](https://pkg.go.dev/database/sql#Tx.QueryRowContext).
####  func (*Tx) [¶](https://pkg.go.dev/database/sql#Tx.QueryRowContext "Go to Tx.QueryRowContext") added in go1.8
```
func (tx *Tx[](https://pkg.go.dev/database/sql#Tx)) QueryRowContext(ctx context[](https://pkg.go.dev/context).Context[](https://pkg.go.dev/context#Context), query string[](https://pkg.go.dev/builtin#string), args ...any[](https://pkg.go.dev/builtin#any)) *Row[](https://pkg.go.dev/database/sql#Row)
```

QueryRowContext executes a query that is expected to return at most one row. QueryRowContext always returns a non-nil value. Errors are deferred until [Row](https://pkg.go.dev/database/sql#Row)'s Scan method is called. If the query selects no rows, the [*Row.Scan](https://pkg.go.dev/database/sql#Row.Scan) will return [ErrNoRows](https://pkg.go.dev/database/sql#ErrNoRows). Otherwise, the [*Row.Scan](https://pkg.go.dev/database/sql#Row.Scan) scans the first selected row and discards the rest.
####  func (*Tx) [¶](https://pkg.go.dev/database/sql#Tx.Rollback "Go to Tx.Rollback")
```
func (tx *Tx[](https://pkg.go.dev/database/sql#Tx)) Rollback() error[](https://pkg.go.dev/builtin#error)
```

Rollback aborts the transaction.
Example [¶](https://pkg.go.dev/database/sql#example-Tx.Rollback "Go to Example")
Share Format Run
####  func (*Tx) [¶](https://pkg.go.dev/database/sql#Tx.Stmt "Go to Tx.Stmt")
```
func (tx *Tx[](https://pkg.go.dev/database/sql#Tx)) Stmt(stmt *Stmt[](https://pkg.go.dev/database/sql#Stmt)) *Stmt[](https://pkg.go.dev/database/sql#Stmt)
```

Stmt returns a transaction-specific prepared statement from an existing statement.
Example:
```
updateMoney, err := db.Prepare("UPDATE balance SET money=money+? WHERE id=?")
...
tx, err := db.Begin()
...
res, err := tx.Stmt(updateMoney).Exec(123.45, 98293203)

```

The returned statement operates within the transaction and will be closed when the transaction has been committed or rolled back.
Stmt uses [context.Background](https://pkg.go.dev/context#Background) internally; to specify the context, use [Tx.StmtContext](https://pkg.go.dev/database/sql#Tx.StmtContext).
####  func (*Tx) [¶](https://pkg.go.dev/database/sql#Tx.StmtContext "Go to Tx.StmtContext") added in go1.8
```
func (tx *Tx[](https://pkg.go.dev/database/sql#Tx)) StmtContext(ctx context[](https://pkg.go.dev/context).Context[](https://pkg.go.dev/context#Context), stmt *Stmt[](https://pkg.go.dev/database/sql#Stmt)) *Stmt[](https://pkg.go.dev/database/sql#Stmt)
```

StmtContext returns a transaction-specific prepared statement from an existing statement.
Example:
```
updateMoney, err := db.Prepare("UPDATE balance SET money=money+? WHERE id=?")
...
tx, err := db.Begin()
...
res, err := tx.StmtContext(ctx, updateMoney).Exec(123.45, 98293203)

```

The provided context is used for the preparation of the statement, not for the execution of the statement.
The returned statement operates within the transaction and will be closed when the transaction has been committed or rolled back.
####  type [¶](https://pkg.go.dev/database/sql#TxOptions "Go to TxOptions") added in go1.8
```
type TxOptions struct {
	// Isolation is the transaction isolation level.
	// If zero, the driver or database's default level is used.
	Isolation IsolationLevel[](https://pkg.go.dev/database/sql#IsolationLevel)
	ReadOnly  bool[](https://pkg.go.dev/builtin#bool)
}
```

TxOptions holds the transaction options to be used in [DB.BeginTx](https://pkg.go.dev/database/sql#DB.BeginTx).
