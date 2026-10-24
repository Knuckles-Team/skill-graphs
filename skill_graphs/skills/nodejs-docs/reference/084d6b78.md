## SQLite[#](https://nodejs.org/docs/latest/api/sqlite.html#sqlite)
**Source Code:** Added in: v22.5.0History Version | Changes
---|---
v25.7.0 | SQLite is now a release candidate.
v23.4.0, v22.13.0 | SQLite is no longer behind `--experimental-sqlite` but still experimental.
[Stability: 1.2](https://nodejs.org/docs/latest/api/documentation.html#stability-index) - Release candidate.
The `node:sqlite` module facilitates working with SQLite databases. To access it:
```
import sqlite from 'node:sqlite';
const sqlite = require('node:sqlite');
copy
```

This module is only available under the `node:` scheme.
The following example shows the basic usage of the `node:sqlite` module to open an in-memory database, write data to the database, and then read the data back.
```
import { DatabaseSync } from 'node:sqlite';
const database = new DatabaseSync(':memory:');

// Execute SQL statements from strings.
database.exec(`
  CREATE TABLE data(
    key INTEGER PRIMARY KEY,
    value TEXT
  ) STRICT
`);
// Create a prepared statement to insert data into the database.
const insert = database.prepare('INSERT INTO data (key, value) VALUES (?, ?)');
// Execute the prepared statement with bound values.
insert.run(1, 'hello');
insert.run(2, 'world');
// Create a prepared statement to read data from the database.
const query = database.prepare('SELECT * FROM data ORDER BY key');
// Execute the prepared statement and log the result set.
console.log(query.all());
// Prints: [ { key: 1, value: 'hello' }, { key: 2, value: 'world' } ]
'use strict';
const { DatabaseSync } = require('node:sqlite');
const database = new DatabaseSync(':memory:');

// Execute SQL statements from strings.
database.exec(`
  CREATE TABLE data(
    key INTEGER PRIMARY KEY,
    value TEXT
  ) STRICT
`);
// Create a prepared statement to insert data into the database.
const insert = database.prepare('INSERT INTO data (key, value) VALUES (?, ?)');
// Execute the prepared statement with bound values.
insert.run(1, 'hello');
insert.run(2, 'world');
// Create a prepared statement to read data from the database.
const query = database.prepare('SELECT * FROM data ORDER BY key');
// Execute the prepared statement and log the result set.
console.log(query.all());
// Prints: [ { key: 1, value: 'hello' }, { key: 2, value: 'world' } ]
copy
```

### Class: `DatabaseSync`[#](https://nodejs.org/docs/latest/api/sqlite.html#class-databasesync)
Added in: v22.5.0History Version | Changes
---|---
v24.0.0, v22.16.0 | Add `timeout` option.
v23.10.0, v22.15.0 | The `path` argument now supports Buffer and URL objects.
This class represents a single
####  `new DatabaseSync(path[, options])`[#](https://nodejs.org/docs/latest/api/sqlite.html#new-databasesyncpath-options)
Added in: v22.5.0History Version | Changes
---|---
v25.5.0 | Enable `defensive` by default.
v25.1.0 | Add `defensive` option.
v24.4.0, v22.18.0 | Add new SQLite database options.
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api) The path of the database. A SQLite database can be stored in a file or completely `':memory:'`.
  * `options`
    * `open` `true`, the database is opened by the constructor. When this value is `false`, the database must be opened via the `open()` method. **Default:** `true`.
    * `readOnly` `true`, the database is opened in read-only mode. If the database does not exist, opening it will fail. **Default:** `false`.
    * `enableForeignKeyConstraints` `true`, foreign key constraints are enabled. This is recommended but can be disabled for compatibility with legacy database schemas. The enforcement of foreign key constraints can be enabled and disabled after opening the database using **Default:** `true`.
    * `enableDoubleQuotedStringLiterals` `true`, SQLite will accept **Default:** `false`.
    * `allowExtension` `true`, the `loadExtension` SQL function and the `loadExtension()` method are enabled. You can call `enableLoadExtension(false)` later to disable this feature. **Default:** `false`.
    * `timeout` **Default:** `0`.
    * `readBigInts` `true`, integer fields are read as JavaScript `BigInt` values. If `false`, integer fields are read as JavaScript numbers. **Default:** `false`.
    * `returnArrays` `true`, query results are returned as arrays instead of objects. **Default:** `false`.
    * `allowBareNamedParameters` `true`, allows binding named parameters without the prefix character (e.g., `foo` instead of `:foo`). **Default:** `true`.
    * `allowUnknownNamedParameters` `true`, unknown named parameters are ignored when binding. If `false`, an exception is thrown for unknown named parameters. **Default:** `false`.
    * `defensive` `true`, enables the defensive flag. When the defensive flag is enabled, language features that allow ordinary SQL to deliberately corrupt the database file are disabled. The defensive flag can also be set using `enableDefensive()`. **Default:** `true`.
    * `limits`
      * `length`
      * `sqlLength`
      * `column`
      * `exprDepth`
      * `compoundSelect`
      * `vdbeOp`
      * `functionArg`
      * `attach`
      * `likePatternLength`
      * `variableNumber`
      * `triggerDepth`


Constructs a new `DatabaseSync` instance.
####  `database.aggregate(name, options)`[#](https://nodejs.org/docs/latest/api/sqlite.html#databaseaggregatename-options)
Added in: v24.0.0, v22.16.0
Registers a new aggregate function with the SQLite database. This method is a wrapper around
  * `name`
  * `options`
    * `deterministic` `true`, the **Default:** `false`.
    * `directOnly` `true`, the **Default:** `false`.
    * `useBigIntArguments` `true`, integer arguments to `options.step` and `options.inverse` are converted to `BigInt`s. If `false`, integer arguments are passed as JavaScript numbers. **Default:** `false`.
    * `varargs` `true`, `options.step` and `options.inverse` may be invoked with any number of arguments (between zero and `false`, `inverse` and `step` must be invoked with exactly `length` arguments. **Default:** `false`.
    * `start`
    * `step`
    * `result`
    * `inverse` `aggregate` method will work as a window function. The function receives the current state and the dropped row value. The return value of this function should be the new state.


When used as a window function, the `result` function will be called multiple times.
```
const { DatabaseSync } = require('node:sqlite');

const db = new DatabaseSync(':memory:');
db.exec(`
  CREATE TABLE t3(x, y);
  INSERT INTO t3 VALUES ('a', 4),
                        ('b', 5),
                        ('c', 3),
                        ('d', 8),
                        ('e', 1);
`);

db.aggregate('sumint', {
  start: 0,
  step: (acc, value) => acc + value,
});

db.prepare('SELECT sumint(y) as total FROM t3').get(); // { total: 21 }
import { DatabaseSync } from 'node:sqlite';

const db = new DatabaseSync(':memory:');
db.exec(`
  CREATE TABLE t3(x, y);
  INSERT INTO t3 VALUES ('a', 4),
                        ('b', 5),
                        ('c', 3),
                        ('d', 8),
                        ('e', 1);
`);

db.aggregate('sumint', {
  start: 0,
  step: (acc, value) => acc + value,
});

db.prepare('SELECT sumint(y) as total FROM t3').get(); // { total: 21 }
copy
```

####  `database.close()`[#](https://nodejs.org/docs/latest/api/sqlite.html#databaseclose)
Added in: v22.5.0
Closes the database connection. An exception is thrown if the database is not open. This method is a wrapper around
####  `database.loadExtension(path)`[#](https://nodejs.org/docs/latest/api/sqlite.html#databaseloadextensionpath)
Added in: v23.5.0, v22.13.0
  * `path`


Loads a shared library into the database connection. This method is a wrapper around `allowExtension` option when constructing the `DatabaseSync` instance.
####  `database.enableLoadExtension(allow)`[#](https://nodejs.org/docs/latest/api/sqlite.html#databaseenableloadextensionallow)
Added in: v23.5.0, v22.13.0
  * `allow`


Enables or disables the `loadExtension` SQL function, and the `loadExtension()` method. When `allowExtension` is `false` when constructing, you cannot enable loading extensions for security reasons.
####  `database.enableDefensive(active)`[#](https://nodejs.org/docs/latest/api/sqlite.html#databaseenabledefensiveactive)
Added in: v25.1.0
  * `active`


Enables or disables the defensive flag. When the defensive flag is active, language features that allow ordinary SQL to deliberately corrupt the database file are disabled. See
####  `database.location([dbName])`[#](https://nodejs.org/docs/latest/api/sqlite.html#databaselocationdbname)
Added in: v24.0.0, v22.16.0
  * `dbName` `'main'` (the default primary database) or any other database that has been added with **Default:** `'main'`.
  * Returns:


This method is a wrapper around
####  `database.exec(sql)`[#](https://nodejs.org/docs/latest/api/sqlite.html#databaseexecsql)
Added in: v22.5.0
  * `sql`


This method allows one or more SQL statements to be executed without returning any results. This method is useful when executing SQL statements read from a file. This method is a wrapper around
####  `database.function(name[, options], fn)`[#](https://nodejs.org/docs/latest/api/sqlite.html#databasefunctionname-options-fn)
Added in: v23.5.0, v22.13.0
  * `name`
  * `options`
    * `deterministic` `true`, the **Default:** `false`.
    * `directOnly` `true`, the **Default:** `false`.
    * `useBigIntArguments` `true`, integer arguments to `function` are converted to `BigInt`s. If `false`, integer arguments are passed as JavaScript numbers. **Default:** `false`.
    * `varargs` `true`, `function` may be invoked with any number of arguments (between zero and `false`, `function` must be invoked with exactly `function.length` arguments. **Default:** `false`.
  * `fn` [Type conversion between JavaScript and SQLite](https://nodejs.org/docs/latest/api/sqlite.html#type-conversion-between-javascript-and-sqlite). The result defaults to `NULL` if the return value is `undefined`.


This method is used to create SQLite user-defined functions. This method is a wrapper around
####  `database.setAuthorizer(callback)`[#](https://nodejs.org/docs/latest/api/sqlite.html#databasesetauthorizercallback)
Added in: v24.10.0
  * `callback` `null` to clear the current authorizer.


Sets an authorizer callback that SQLite will invoke whenever it attempts to access data or modify the database schema through prepared statements. This can be used to implement security policies, audit access, or restrict certain operations. This method is a wrapper around
When invoked, the callback receives five arguments:
  * `actionCode` `SQLITE_INSERT`, `SQLITE_UPDATE`, `SQLITE_SELECT`).
  * `arg1`
  * `arg2`
  * `dbName`
  * `triggerOrView`


The callback must return one of the following constants:
  * `SQLITE_OK` - Allow the operation.
  * `SQLITE_DENY` - Deny the operation (causes an error).
  * `SQLITE_IGNORE` - Ignore the operation (silently skip).

```
const { DatabaseSync, constants } = require('node:sqlite');
const db = new DatabaseSync(':memory:');

// Set up an authorizer that denies all table creation
db.setAuthorizer((actionCode) => {
  if (actionCode === constants.SQLITE_CREATE_TABLE) {
    return constants.SQLITE_DENY;
  }
  return constants.SQLITE_OK;
});

// This will work
db.prepare('SELECT 1').get();

// This will throw an error due to authorization denial
try {
  db.exec('CREATE TABLE blocked (id INTEGER)');
} catch (err) {
  console.log('Operation blocked:', err.message);
}
import { DatabaseSync, constants } from 'node:sqlite';
const db = new DatabaseSync(':memory:');

// Set up an authorizer that denies all table creation
db.setAuthorizer((actionCode) => {
  if (actionCode === constants.SQLITE_CREATE_TABLE) {
    return constants.SQLITE_DENY;
  }
  return constants.SQLITE_OK;
});

// This will work
db.prepare('SELECT 1').get();

// This will throw an error due to authorization denial
try {
  db.exec('CREATE TABLE blocked (id INTEGER)');
} catch (err) {
  console.log('Operation blocked:', err.message);
}
copy
```

####  `database.isOpen`[#](https://nodejs.org/docs/latest/api/sqlite.html#databaseisopen)
Added in: v23.11.0, v22.15.0
  * Type:


####  `database.isTransaction`[#](https://nodejs.org/docs/latest/api/sqlite.html#databaseistransaction)
Added in: v24.0.0, v22.16.0
  * Type:


####  `database.limits`[#](https://nodejs.org/docs/latest/api/sqlite.html#databaselimits)
Added in: v25.8.0
  * Type:


An object for getting and setting SQLite database limits at runtime. Each property corresponds to an SQLite limit and can be read or written.
```
const db = new DatabaseSync(':memory:');

// Read current limit
console.log(db.limits.length);

// Set a new limit
db.limits.sqlLength = 100000;

// Reset a limit to its compile-time maximum
db.limits.sqlLength = Infinity;
copy
```

Available properties: `length`, `sqlLength`, `column`, `exprDepth`, `compoundSelect`, `vdbeOp`, `functionArg`, `attach`, `likePatternLength`, `variableNumber`, `triggerDepth`.
Setting a property to `Infinity` resets the limit to its compile-time maximum value.
####  `database.open()`[#](https://nodejs.org/docs/latest/api/sqlite.html#databaseopen)
Added in: v22.5.0
Opens the database specified in the `path` argument of the `DatabaseSync` constructor. This method should only be used when the database is not opened via the constructor. An exception is thrown if the database is already open.
####  `database.prepare(sql[, options])`[#](https://nodejs.org/docs/latest/api/sqlite.html#databasepreparesql-options)
Added in: v22.5.0
  * `sql`
  * `options`
    * `readBigInts` `true`, integer fields are read as `BigInt`s. **Default:** inherited from database options or `false`.
    * `returnArrays` `true`, results are returned as arrays. **Default:** inherited from database options or `false`.
    * `allowBareNamedParameters` `true`, allows binding named parameters without the prefix character. **Default:** inherited from database options or `true`.
    * `allowUnknownNamedParameters` `true`, unknown named parameters are ignored. **Default:** inherited from database options or `false`.
  * Returns: [`<StatementSync>`](https://nodejs.org/docs/latest/api/sqlite.html#class-statementsync) The prepared statement.


Compiles a SQL statement into a
####  `database.createTagStore([maxSize])`[#](https://nodejs.org/docs/latest/api/sqlite.html#databasecreatetagstoremaxsize)
Added in: v24.9.0
  * `maxSize` **Default:** `1000`.
  * Returns: {SQLTagStore} A new SQL tag store for caching prepared statements.


Creates a new [`SQLTagStore`](https://nodejs.org/docs/latest/api/sqlite.html#class-sqltagstore), which is a Least Recently Used (LRU) cache for storing prepared statements. This allows for the efficient reuse of prepared statements by tagging them with a unique identifier.
When a tagged SQL literal is executed, the `SQLTagStore` checks if a prepared statement for the corresponding SQL query string already exists in the cache. If it does, the cached statement is used. If not, a new prepared statement is created, executed, and then stored in the cache for future use. This mechanism helps to avoid the overhead of repeatedly parsing and preparing the same SQL statements.
Tagged statements bind the placeholder values from the template literal as parameters to the underlying prepared statement. For example:
```
sqlTagStore.get`SELECT ${value}`;
copy
```

is equivalent to:
```
db.prepare('SELECT ?').get(value);
copy
```

However, in the first example, the tag store will cache the underlying prepared statement for future use.
> **Note:** The `${value}` syntax in tagged statements _binds_ a parameter to the prepared statement. This differs from its behavior in _untagged_ template literals, where it performs string interpolation.
> ```
// This a safe example of binding a parameter to a tagged statement.
sqlTagStore.run`INSERT INTO t1 (id) VALUES (${id})`;

// This is an *unsafe* example of an untagged template string.
// `id` is interpolated into the query text as a string.
// This can lead to SQL injection and data corruption.
db.run(`INSERT INTO t1 (id) VALUES (${id})`);
copy
```

The tag store will match a statement from the cache if the query strings (including the positions of any bound placeholders) are identical.
```
// The following statements will match in the cache:
sqlTagStore.get`SELECT * FROM t1 WHERE id = ${id} AND active = 1`;
sqlTagStore.get`SELECT * FROM t1 WHERE id = ${12345} AND active = 1`;

// The following statements will not match, as the query strings
// and bound placeholders differ:
sqlTagStore.get`SELECT * FROM t1 WHERE id = ${id} AND active = 1`;
sqlTagStore.get`SELECT * FROM t1 WHERE id = 12345 AND active = 1`;

// The following statements will not match, as matches are case-sensitive:
sqlTagStore.get`SELECT * FROM t1 WHERE id = ${id} AND active = 1`;
sqlTagStore.get`select * from t1 where id = ${id} and active = 1`;
copy
```

The only way of binding parameters in tagged statements is with the `${value}` syntax. Do not add parameter binding placeholders (`?` etc.) to the SQL query string itself.
```
import { DatabaseSync } from 'node:sqlite';

const db = new DatabaseSync(':memory:');
const sql = db.createTagStore();

db.exec('CREATE TABLE users (id INT, name TEXT)');

// Using the 'run' method to insert data.
// The tagged literal is used to identify the prepared statement.
sql.run`INSERT INTO users VALUES (1, 'Alice')`;
sql.run`INSERT INTO users VALUES (2, 'Bob')`;

// Using the 'get' method to retrieve a single row.
const name = 'Alice';
const user = sql.get`SELECT * FROM users WHERE name = ${name}`;
console.log(user); // { id: 1, name: 'Alice' }

// Using the 'all' method to retrieve all rows.
const allUsers = sql.all`SELECT * FROM users ORDER BY id`;
console.log(allUsers);
// [
//   { id: 1, name: 'Alice' },
//   { id: 2, name: 'Bob' }
// ]
const { DatabaseSync } = require('node:sqlite');

const db = new DatabaseSync(':memory:');
const sql = db.createTagStore();

db.exec('CREATE TABLE users (id INT, name TEXT)');

// Using the 'run' method to insert data.
// The tagged literal is used to identify the prepared statement.
sql.run`INSERT INTO users VALUES (1, 'Alice')`;
sql.run`INSERT INTO users VALUES (2, 'Bob')`;

// Using the 'get' method to retrieve a single row.
const name = 'Alice';
const user = sql.get`SELECT * FROM users WHERE name = ${name}`;
console.log(user); // { id: 1, name: 'Alice' }

// Using the 'all' method to retrieve all rows.
const allUsers = sql.all`SELECT * FROM users ORDER BY id`;
console.log(allUsers);
// [
//   { id: 1, name: 'Alice' },
//   { id: 2, name: 'Bob' }
// ]
copy
```

####  `database.createSession([options])`[#](https://nodejs.org/docs/latest/api/sqlite.html#databasecreatesessionoptions)
Added in: v23.3.0, v22.12.0
  * `options`
    * `table`
    * `db` **Default** : `'main'`.
  * Returns: [`<Session>`](https://nodejs.org/docs/latest/api/sqlite.html#class-session) A session handle.


Creates and attaches a session to the database. This method is a wrapper around
####  `database.applyChangeset(changeset[, options])`[#](https://nodejs.org/docs/latest/api/sqlite.html#databaseapplychangesetchangeset-options)
Added in: v23.3.0, v22.12.0
  * `changeset`
  * `options`
    * `filter`
    * `onConflict`
      * `SQLITE_CHANGESET_DATA`: A `DELETE` or `UPDATE` change does not contain the expected "before" values.
      * `SQLITE_CHANGESET_NOTFOUND`: A row matching the primary key of the `DELETE` or `UPDATE` change does not exist.
      * `SQLITE_CHANGESET_CONFLICT`: An `INSERT` change results in a duplicate primary key.
      * `SQLITE_CHANGESET_FOREIGN_KEY`: Applying a change would result in a foreign key violation.
      * `SQLITE_CHANGESET_CONSTRAINT`: Applying a change results in a `UNIQUE`, `CHECK`, or `NOT NULL` constraint violation.
The function should return one of the following values:
      * `SQLITE_CHANGESET_OMIT`: Omit conflicting changes.
      * `SQLITE_CHANGESET_REPLACE`: Replace existing values with conflicting changes (only valid with `SQLITE_CHANGESET_DATA` or `SQLITE_CHANGESET_CONFLICT` conflicts).
      * `SQLITE_CHANGESET_ABORT`: Abort on conflict and roll back the database.
When an error is thrown in the conflict handler or when any other value is returned from the handler, applying the changeset is aborted and the database is rolled back.
**Default** : A function that returns `SQLITE_CHANGESET_ABORT`.
  * Returns:


An exception is thrown if the database is not open. This method is a wrapper around
```
import { DatabaseSync } from 'node:sqlite';

const sourceDb = new DatabaseSync(':memory:');
const targetDb = new DatabaseSync(':memory:');

sourceDb.exec('CREATE TABLE data(key INTEGER PRIMARY KEY, value TEXT)');
targetDb.exec('CREATE TABLE data(key INTEGER PRIMARY KEY, value TEXT)');

const session = sourceDb.createSession();

const insert = sourceDb.prepare('INSERT INTO data (key, value) VALUES (?, ?)');
insert.run(1, 'hello');
insert.run(2, 'world');

const changeset = session.changeset();
targetDb.applyChangeset(changeset);
// Now that the changeset has been applied, targetDb contains the same data as sourceDb.
const { DatabaseSync } = require('node:sqlite');

const sourceDb = new DatabaseSync(':memory:');
const targetDb = new DatabaseSync(':memory:');

sourceDb.exec('CREATE TABLE data(key INTEGER PRIMARY KEY, value TEXT)');
targetDb.exec('CREATE TABLE data(key INTEGER PRIMARY KEY, value TEXT)');

const session = sourceDb.createSession();

const insert = sourceDb.prepare('INSERT INTO data (key, value) VALUES (?, ?)');
insert.run(1, 'hello');
insert.run(2, 'world');

const changeset = session.changeset();
targetDb.applyChangeset(changeset);
// Now that the changeset has been applied, targetDb contains the same data as sourceDb.
copy
```

####  `database[Symbol.dispose]()`[#](https://nodejs.org/docs/latest/api/sqlite.html#databasesymboldispose)
Added in: v23.11.0, v22.15.0History Version | Changes
---|---
v24.2.0 | No longer experimental.
Closes the database connection. If the database connection is already closed then this is a no-op.
### Class: `Session`[#](https://nodejs.org/docs/latest/api/sqlite.html#class-session)
Added in: v23.3.0, v22.12.0
####  `session.changeset()`[#](https://nodejs.org/docs/latest/api/sqlite.html#sessionchangeset)
Added in: v23.3.0, v22.12.0
  * Returns:


Retrieves a changeset containing all changes since the changeset was created. Can be called multiple times. An exception is thrown if the database or the session is not open. This method is a wrapper around
####  `session.patchset()`[#](https://nodejs.org/docs/latest/api/sqlite.html#sessionpatchset)
Added in: v23.3.0, v22.12.0
  * Returns:


Similar to the method above, but generates a more compact patchset. See
####  `session.close()`[#](https://nodejs.org/docs/latest/api/sqlite.html#sessionclose)
Closes the session. An exception is thrown if the database or the session is not open. This method is a wrapper around
####  `session[Symbol.dispose]()`[#](https://nodejs.org/docs/latest/api/sqlite.html#sessionsymboldispose)
Added in: v24.9.0
Closes the session. If the session is already closed, does nothing.
### Class: `StatementSync`[#](https://nodejs.org/docs/latest/api/sqlite.html#class-statementsync)
Added in: v22.5.0
This class represents a single `database.prepare()` method. All APIs exposed by this class execute synchronously.
A prepared statement is an efficient binary representation of the SQL used to create it. Prepared statements are parameterizable, and can be invoked multiple times with different bound values. Parameters also offer protection against
####  `statement.all([namedParameters][, ...anonymousParameters])`[#](https://nodejs.org/docs/latest/api/sqlite.html#statementallnamedparameters-anonymousparameters)
Added in: v22.5.0History Version | Changes
---|---
v23.7.0, v22.14.0 | Add support for `DataView` and typed array objects for `anonymousParameters`.
  * `namedParameters`
  * `...anonymousParameters` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * Returns:


This method executes a prepared statement and returns all results as an array of objects. If the prepared statement does not return any results, this method returns an empty array. The prepared statement `namedParameters` and `anonymousParameters`.
####  `statement.columns()`[#](https://nodejs.org/docs/latest/api/sqlite.html#statementcolumns)
Added in: v23.11.0, v22.16.0
  * Returns:
    * `column` `null` if the column is the result of an expression or subquery. This property is the result of
    * `database` `null` if the column is the result of an expression or subquery. This property is the result of
    * `name` `SELECT` statement. This property is the result of
    * `table` `null` if the column is the result of an expression or subquery. This property is the result of
    * `type` `null` if the column is the result of an expression or subquery. This property is the result of


This method is used to retrieve information about the columns returned by the prepared statement.
####  `statement.expandedSQL`[#](https://nodejs.org/docs/latest/api/sqlite.html#statementexpandedsql)
Added in: v22.5.0
  * Type:


The source SQL text of the prepared statement with parameter placeholders replaced by the values that were used during the most recent execution of this prepared statement. This property is a wrapper around
####  `statement.get([namedParameters][, ...anonymousParameters])`[#](https://nodejs.org/docs/latest/api/sqlite.html#statementgetnamedparameters-anonymousparameters)
Added in: v22.5.0History Version | Changes
---|---
v23.7.0, v22.14.0 | Add support for `DataView` and typed array objects for `anonymousParameters`.
  * `namedParameters`
  * `...anonymousParameters` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * Returns: `undefined`.


This method executes a prepared statement and returns the first result as an object. If the prepared statement does not return any results, this method returns `undefined`. The prepared statement `namedParameters` and `anonymousParameters`.
####  `statement.iterate([namedParameters][, ...anonymousParameters])`[#](https://nodejs.org/docs/latest/api/sqlite.html#statementiteratenamedparameters-anonymousparameters)
Added in: v23.4.0, v22.13.0History Version | Changes
---|---
v23.7.0, v22.14.0 | Add support for `DataView` and typed array objects for `anonymousParameters`.
  * `namedParameters`
  * `...anonymousParameters` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * Returns:


This method executes a prepared statement and returns an iterator of objects. If the prepared statement does not return any results, this method returns an empty iterator. The prepared statement `namedParameters` and `anonymousParameters`.
####  `statement.run([namedParameters][, ...anonymousParameters])`[#](https://nodejs.org/docs/latest/api/sqlite.html#statementrunnamedparameters-anonymousparameters)
Added in: v22.5.0History Version | Changes
---|---
v23.7.0, v22.14.0 | Add support for `DataView` and typed array objects for `anonymousParameters`.
  * `namedParameters`
  * `...anonymousParameters` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * Returns:
    * `changes` `INSERT`, `UPDATE`, or `DELETE` statement. This field is either a number or a `BigInt` depending on the prepared statement's configuration. This property is the result of
    * `lastInsertRowid` `BigInt` depending on the prepared statement's configuration. This property is the result of


This method executes a prepared statement and returns an object summarizing the resulting changes. The prepared statement `namedParameters` and `anonymousParameters`.
####  `statement.setAllowBareNamedParameters(enabled)`[#](https://nodejs.org/docs/latest/api/sqlite.html#statementsetallowbarenamedparametersenabled)
Added in: v22.5.0
  * `enabled`


The names of SQLite parameters begin with a prefix character. By default, `node:sqlite` requires that this prefix character is present when binding parameters. However, with the exception of dollar sign character, these prefix characters also require extra quoting when used in object keys.
To improve ergonomics, this method can be used to also allow bare named parameters, which do not require the prefix character in JavaScript code. There are several caveats to be aware of when enabling bare named parameters:
  * The prefix character is still required in SQL.
  * The prefix character is still allowed in JavaScript. In fact, prefixed names will have slightly better binding performance.
  * Using ambiguous named parameters, such as `$k` and `@k`, in the same prepared statement will result in an exception as it cannot be determined how to bind a bare name.


####  `statement.setAllowUnknownNamedParameters(enabled)`[#](https://nodejs.org/docs/latest/api/sqlite.html#statementsetallowunknownnamedparametersenabled)
Added in: v23.11.0, v22.15.0
  * `enabled`


By default, if an unknown name is encountered while binding parameters, an exception is thrown. This method allows unknown named parameters to be ignored.
####  `statement.setReturnArrays(enabled)`[#](https://nodejs.org/docs/latest/api/sqlite.html#statementsetreturnarraysenabled)
Added in: v24.0.0, v22.16.0
  * `enabled`


When enabled, query results returned by the `all()`, `get()`, and `iterate()` methods will be returned as arrays instead of objects.
####  `statement.setReadBigInts(enabled)`[#](https://nodejs.org/docs/latest/api/sqlite.html#statementsetreadbigintsenabled)
Added in: v22.5.0
  * `enabled` `BigInt`s when reading `INTEGER` fields from the database.


When reading from the database, SQLite `INTEGER`s are mapped to JavaScript numbers by default. However, SQLite `INTEGER`s can store values larger than JavaScript numbers are capable of representing. In such cases, this method can be used to read `INTEGER` data using JavaScript `BigInt`s. This method has no impact on database write operations where numbers and `BigInt`s are both supported at all times.
####  `statement.sourceSQL`[#](https://nodejs.org/docs/latest/api/sqlite.html#statementsourcesql)
Added in: v22.5.0
  * Type:


The source SQL text of the prepared statement. This property is a wrapper around
### Class: `SQLTagStore`[#](https://nodejs.org/docs/latest/api/sqlite.html#class-sqltagstore)
Added in: v24.9.0
This class represents a single LRU (Least Recently Used) cache for storing prepared statements.
Instances of this class are created via the [`database.createTagStore()`](https://nodejs.org/docs/latest/api/sqlite.html#databasecreatetagstoremaxsize) method, not by using a constructor. The store caches prepared statements based on the provided SQL query string. When the same query is seen again, the store retrieves the cached statement and safely applies the new values through parameter binding, thereby preventing attacks like SQL injection.
The cache has a maxSize that defaults to 1000 statements, but a custom size can be provided (e.g., `database.createTagStore(100)`). All APIs exposed by this class execute synchronously.
####  `sqlTagStore.all(stringElements[, ...boundParameters])`[#](https://nodejs.org/docs/latest/api/sqlite.html#sqltagstoreallstringelements-boundparameters)
Added in: v24.9.0
  * `stringElements`
  * `...boundParameters` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * Returns:


Executes the given SQL query and returns all resulting rows as an array of objects.
This function is intended to be used as a template literal tag, not to be called directly.
####  `sqlTagStore.get(stringElements[, ...boundParameters])`[#](https://nodejs.org/docs/latest/api/sqlite.html#sqltagstoregetstringelements-boundparameters)
Added in: v24.9.0
  * `stringElements`
  * `...boundParameters` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * Returns: `undefined` if no rows are returned.


Executes the given SQL query and returns the first resulting row as an object.
This function is intended to be used as a template literal tag, not to be called directly.
####  `sqlTagStore.iterate(stringElements[, ...boundParameters])`[#](https://nodejs.org/docs/latest/api/sqlite.html#sqltagstoreiteratestringelements-boundparameters)
Added in: v24.9.0
  * `stringElements`
  * `...boundParameters` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * Returns:


Executes the given SQL query and returns an iterator over the resulting rows.
This function is intended to be used as a template literal tag, not to be called directly.
####  `sqlTagStore.run(stringElements[, ...boundParameters])`[#](https://nodejs.org/docs/latest/api/sqlite.html#sqltagstorerunstringelements-boundparameters)
Added in: v24.9.0
  * `stringElements`
  * `...boundParameters` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * Returns: `changes` and `lastInsertRowid`.


Executes the given SQL query, which is expected to not return any rows (e.g., INSERT, UPDATE, DELETE).
This function is intended to be used as a template literal tag, not to be called directly.
####  `sqlTagStore.size`[#](https://nodejs.org/docs/latest/api/sqlite.html#sqltagstoresize)
Added in: v24.9.0History Version | Changes
---|---
v25.4.0 | Changed from a method to a getter.
  * Type:


A read-only property that returns the number of prepared statements currently in the cache.
####  `sqlTagStore.capacity`[#](https://nodejs.org/docs/latest/api/sqlite.html#sqltagstorecapacity)
Added in: v24.9.0
  * Type:


A read-only property that returns the maximum number of prepared statements the cache can hold.
####  `sqlTagStore.db`[#](https://nodejs.org/docs/latest/api/sqlite.html#sqltagstoredb)
Added in: v24.9.0
  * Type: [`<DatabaseSync>`](https://nodejs.org/docs/latest/api/sqlite.html#class-databasesync)


A read-only property that returns the `DatabaseSync` object associated with this `SQLTagStore`.
####  `sqlTagStore.clear()`[#](https://nodejs.org/docs/latest/api/sqlite.html#sqltagstoreclear)
Added in: v24.9.0
Resets the LRU cache, clearing all stored prepared statements.
#### Type conversion between JavaScript and SQLite[#](https://nodejs.org/docs/latest/api/sqlite.html#type-conversion-between-javascript-and-sqlite)
When Node.js writes to or reads from SQLite, it is necessary to convert between JavaScript data types and SQLite's
Storage class | JavaScript to SQLite | SQLite to JavaScript
---|---|---
`NULL` |  |
`INTEGER` |  | _(configurable)_
`REAL` |  |
`TEXT` |  |
`BLOB` |  |
APIs that read values from SQLite have a configuration option that determines whether `INTEGER` values are converted to `number` or `bigint` in JavaScript, such as the `readBigInts` option for statements and the `useBigIntArguments` option for user-defined functions. If Node.js reads an `INTEGER` value from SQLite that is outside the JavaScript `ERR_OUT_OF_RANGE` error will be thrown.
###  `sqlite.backup(sourceDb, path[, options])`[#](https://nodejs.org/docs/latest/api/sqlite.html#sqlitebackupsourcedb-path-options)
Added in: v23.8.0, v22.16.0History Version | Changes
---|---
v23.10.0 | The `path` argument now supports Buffer and URL objects.
  * `sourceDb` [`<DatabaseSync>`](https://nodejs.org/docs/latest/api/sqlite.html#class-databasesync) The database to backup. The source database must be open.
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api) The path where the backup will be created. If the file already exists, the contents will be overwritten.
  * `options`
    * `source` `'main'` (the default primary database) or any other database that have been added with **Default:** `'main'`.
    * `target` `'main'` (the default primary database) or any other database that have been added with **Default:** `'main'`.
    * `rate` **Default:** `100`.
    * `progress` `remainingPages` and `totalPages` properties, describing the current progress of the backup operation.
  * Returns:


This method makes a database backup. This method abstracts the
The backed-up database can be used normally during the backup process. Mutations coming from the same connection - same [`<DatabaseSync>`](https://nodejs.org/docs/latest/api/sqlite.html#class-databasesync) - object will be reflected in the backup right away. However, mutations from other connections will cause the backup process to restart.
```
const { backup, DatabaseSync } = require('node:sqlite');

(async () => {
  const sourceDb = new DatabaseSync('source.db');
  const totalPagesTransferred = await backup(sourceDb, 'backup.db', {
    rate: 1, // Copy one page at a time.
    progress: ({ totalPages, remainingPages }) => {
      console.log('Backup in progress', { totalPages, remainingPages });
    },
  });

  console.log('Backup completed', totalPagesTransferred);
})();
import { backup, DatabaseSync } from 'node:sqlite';

const sourceDb = new DatabaseSync('source.db');
const totalPagesTransferred = await backup(sourceDb, 'backup.db', {
  rate: 1, // Copy one page at a time.
  progress: ({ totalPages, remainingPages }) => {
    console.log('Backup in progress', { totalPages, remainingPages });
  },
});

console.log('Backup completed', totalPagesTransferred);
copy
```

###  `sqlite.constants`[#](https://nodejs.org/docs/latest/api/sqlite.html#sqliteconstants)
Added in: v23.5.0, v22.13.0
  * Type:


An object containing commonly used constants for SQLite operations.
#### SQLite constants[#](https://nodejs.org/docs/latest/api/sqlite.html#sqlite-constants)
The following constants are exported by the `sqlite.constants` object.
##### Conflict resolution constants[#](https://nodejs.org/docs/latest/api/sqlite.html#conflict-resolution-constants)
One of the following constants is available as an argument to the `onConflict` conflict resolution handler passed to [`database.applyChangeset()`](https://nodejs.org/docs/latest/api/sqlite.html#databaseapplychangesetchangeset-options). See also
Constant | Description
---|---
`SQLITE_CHANGESET_DATA` | The conflict handler is invoked with this constant when processing a DELETE or UPDATE change if a row with the required PRIMARY KEY fields is present in the database, but one or more other (non primary-key) fields modified by the update do not contain the expected "before" values.
`SQLITE_CHANGESET_NOTFOUND` | The conflict handler is invoked with this constant when processing a DELETE or UPDATE change if a row with the required PRIMARY KEY fields is not present in the database.
`SQLITE_CHANGESET_CONFLICT` | This constant is passed to the conflict handler while processing an INSERT change if the operation would result in duplicate primary key values.
`SQLITE_CHANGESET_CONSTRAINT` | If foreign key handling is enabled, and applying a changeset leaves the database in a state containing foreign key violations, the conflict handler is invoked with this constant exactly once before the changeset is committed. If the conflict handler returns `SQLITE_CHANGESET_OMIT`, the changes, including those that caused the foreign key constraint violation, are committed. Or, if it returns `SQLITE_CHANGESET_ABORT`, the changeset is rolled back.
`SQLITE_CHANGESET_FOREIGN_KEY` | If any other constraint violation occurs while applying a change (i.e. a UNIQUE, CHECK or NOT NULL constraint), the conflict handler is invoked with this constant.
One of the following constants must be returned from the `onConflict` conflict resolution handler passed to [`database.applyChangeset()`](https://nodejs.org/docs/latest/api/sqlite.html#databaseapplychangesetchangeset-options). See also
Constant | Description
---|---
`SQLITE_CHANGESET_OMIT` | Conflicting changes are omitted.
`SQLITE_CHANGESET_REPLACE` | Conflicting changes replace existing values. Note that this value can only be returned when the type of conflict is either `SQLITE_CHANGESET_DATA` or `SQLITE_CHANGESET_CONFLICT`.
`SQLITE_CHANGESET_ABORT` | Abort when a change encounters a conflict and roll back database.
##### Authorization constants[#](https://nodejs.org/docs/latest/api/sqlite.html#authorization-constants)
The following constants are used with the [`database.setAuthorizer()`](https://nodejs.org/docs/latest/api/sqlite.html#databasesetauthorizercallback) method.
###### Authorization result codes[#](https://nodejs.org/docs/latest/api/sqlite.html#authorization-result-codes)
One of the following constants must be returned from the authorizer callback function passed to [`database.setAuthorizer()`](https://nodejs.org/docs/latest/api/sqlite.html#databasesetauthorizercallback).
Constant | Description
---|---
`SQLITE_OK` | Allow the operation to proceed normally.
`SQLITE_DENY` | Deny the operation and cause an error to be returned.
`SQLITE_IGNORE` | Ignore the operation and continue as if it had never been requested.
###### Authorization action codes[#](https://nodejs.org/docs/latest/api/sqlite.html#authorization-action-codes)
The following constants are passed as the first argument to the authorizer callback function to indicate what type of operation is being authorized.
Constant | Description
---|---
`SQLITE_CREATE_INDEX` | Create an index
`SQLITE_CREATE_TABLE` | Create a table
`SQLITE_CREATE_TEMP_INDEX` | Create a temporary index
`SQLITE_CREATE_TEMP_TABLE` | Create a temporary table
`SQLITE_CREATE_TEMP_TRIGGER` | Create a temporary trigger
`SQLITE_CREATE_TEMP_VIEW` | Create a temporary view
`SQLITE_CREATE_TRIGGER` | Create a trigger
`SQLITE_CREATE_VIEW` | Create a view
`SQLITE_DELETE` | Delete from a table
`SQLITE_DROP_INDEX` | Drop an index
`SQLITE_DROP_TABLE` | Drop a table
`SQLITE_DROP_TEMP_INDEX` | Drop a temporary index
`SQLITE_DROP_TEMP_TABLE` | Drop a temporary table
`SQLITE_DROP_TEMP_TRIGGER` | Drop a temporary trigger
`SQLITE_DROP_TEMP_VIEW` | Drop a temporary view
`SQLITE_DROP_TRIGGER` | Drop a trigger
`SQLITE_DROP_VIEW` | Drop a view
`SQLITE_INSERT` | Insert into a table
`SQLITE_PRAGMA` | Execute a PRAGMA statement
`SQLITE_READ` | Read from a table
`SQLITE_SELECT` | Execute a SELECT statement
`SQLITE_TRANSACTION` | Begin, commit, or rollback a transaction
`SQLITE_UPDATE` | Update a table
`SQLITE_ATTACH` | Attach a database
`SQLITE_DETACH` | Detach a database
`SQLITE_ALTER_TABLE` | Alter a table
`SQLITE_REINDEX` | Reindex
`SQLITE_ANALYZE` | Analyze the database
`SQLITE_CREATE_VTABLE` | Create a virtual table
`SQLITE_DROP_VTABLE` | Drop a virtual table
`SQLITE_FUNCTION` | Use a function
`SQLITE_SAVEPOINT` | Create, release, or rollback a savepoint
`SQLITE_COPY` | Copy data (legacy)
`SQLITE_RECURSIVE` | Recursive query
