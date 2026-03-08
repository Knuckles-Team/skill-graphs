## Queries that use statistics effectively
Certain query implementations, such as local variables and complex expressions in the query predicate, can lead to suboptimal query plans. Following query design guidelines for using statistics effectively can help to avoid this. For more information about query predicates, see [Search condition](https://learn.microsoft.com/en-us/sql/t-sql/queries/search-condition-transact-sql?view=sql-server-ver17).
You can improve query plans by applying query design guidelines that use statistics effectively to improve _cardinality estimates_ for expressions, variables, and functions used in query predicates. When the Query Optimizer doesn't know the value of an expression, variable, or function, it doesn't know which value to look up in the histogram and therefore can't retrieve the best cardinality estimate from the histogram. Instead, the Query Optimizer bases the cardinality estimate on the average number of rows per distinct value for all of the sampled rows in the histogram. This leads to suboptimal cardinality estimates and can hurt query performance. For more information about histograms, see [histogram](https://learn.microsoft.com/en-us/sql/relational-databases/statistics/statistics?view=sql-server-ver17#histogram) section in this page or [sys.dm_db_stats_histogram](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/sys-dm-db-stats-histogram-transact-sql?view=sql-server-ver17).
The following guidelines describe how to write queries to improve query plans by improving cardinality estimates.
[](https://learn.microsoft.com/en-us/sql/relational-databases/statistics/statistics?view=sql-server-ver17#improve-cardinality-estimates-for-expressions)
### Improve cardinality estimates for expressions
To improve cardinality estimates for expressions, follow these guidelines:
  * Whenever possible, simplify expressions with constants in them. The Query Optimizer doesn't evaluate all functions and expressions containing constants prior to determining cardinality estimates. For example, simplify the expression `ABS(-100)` to `100`.
  * If the expression uses multiple variables, consider creating a computed column for the expression, and then create statistics or an index on the computed column. For example, the query predicate `WHERE PRICE + Tax > 100` might have a better cardinality estimate if you create a computed column for the expression `Price + Tax`.


[](https://learn.microsoft.com/en-us/sql/relational-databases/statistics/statistics?view=sql-server-ver17#improve-cardinality-estimates-for-variables-and-functions)
### Improve cardinality estimates for variables and functions
To improve the cardinality estimates for variables and functions, follow these guidelines:
  * If the query predicate uses a local variable, consider rewriting the query to use a parameter instead of a local variable. The value of a local variable isn't known when the Query Optimizer creates the query execution plan. When a query uses a parameter, the Query Optimizer uses the cardinality estimate for the first actual parameter value that is passed to the stored procedure.
  * Consider using a standard table or temporary table to hold the results of multi-statement table-valued functions (mstvf). The Query Optimizer doesn't create statistics for multi-statement table-valued functions. With this approach, the Query Optimizer can create statistics on the table columns and use them to create a better query plan.
  * Consider using a standard table or temporary table as a replacement for table variables. The Query Optimizer doesn't create statistics for table variables. With this approach, the Query Optimizer can create statistics on the table columns and use them to create a better query plan. There are tradeoffs in determining whether to use a temporary table or a table variable; Table variables used in stored procedures cause fewer recompilations of the stored procedure than temporary tables. Depending on the application, using a temporary table instead of a table variable might not improve performance.
  * If a stored procedure contains a query that uses a passed-in parameter, avoid changing the parameter value within the stored procedure before using it in the query. The cardinality estimates for the query are based on the passed-in parameter value and not the updated value. To avoid changing the parameter value, you can rewrite the query to use two stored procedures.
For example, the following stored procedure `Sales.GetRecentSales` changes the value of the parameter `@date` when `@date` is `NULL`.
SQL
Copy
```
USE AdventureWorks2022;
GO

IF OBJECT_ID('Sales.GetRecentSales', 'P') IS NOT NULL
    DROP PROCEDURE Sales.GetRecentSales;
GO

CREATE PROCEDURE Sales.GetRecentSales
@date DATETIME
AS
BEGIN
    IF @date IS NULL
        SET @date = DATEADD(MONTH, -3,
            (SELECT MAX(ORDERDATE)
            FROM Sales.SalesOrderHeader));
    SELECT *
    FROM Sales.SalesOrderHeader AS h, Sales.SalesOrderDetail AS d
    WHERE h.SalesOrderID = d.SalesOrderID
        AND h.OrderDate > @date;
END
GO

```

If the first call to the stored procedure `Sales.GetRecentSales` passes a `NULL` for the `@date` parameter, the Query Optimizer compiles the stored procedure with the cardinality estimate for `@date = NULL` even though the query predicate isn't called with `@date = NULL`. This cardinality estimate might be significantly different than the number of rows in the actual query result. As a result, the Query Optimizer might choose a suboptimal query plan. To help avoid this, you can rewrite the stored procedure into two procedures as follows:
SQL
Copy
```
USE AdventureWorks2022;
GO

IF OBJECT_ID('Sales.GetNullRecentSales', 'P') IS NOT NULL
    DROP PROCEDURE Sales.GetNullRecentSales;
GO

CREATE PROCEDURE Sales.GetNullRecentSales
@date DATETIME
AS
BEGIN
    IF @date IS NULL
        SET @date = DATEADD(MONTH, -3,
            (SELECT MAX(ORDERDATE)
            FROM Sales.SalesOrderHeader));
    EXECUTE Sales.GetNonNullRecentSales @date;
END
GO

IF OBJECT_ID('Sales.GetNonNullRecentSales', 'P') IS NOT NULL
    DROP PROCEDURE Sales.GetNonNullRecentSales;
GO

CREATE PROCEDURE Sales.GetNonNullRecentSales
@date DATETIME
AS
BEGIN
    SELECT *
    FROM Sales.SalesOrderHeader AS h, Sales.SalesOrderDetail AS d
    WHERE h.SalesOrderID = d.SalesOrderID
        AND h.OrderDate > @date;
END
GO

```



[](https://learn.microsoft.com/en-us/sql/relational-databases/statistics/statistics?view=sql-server-ver17#improve-cardinality-estimates-with-query-hints)
### Improve cardinality estimates with query hints
To improve cardinality estimates for local variables, you can use the `OPTIMIZE FOR <value>` or `OPTIMIZE FOR UNKNOWN` query hints with `RECOMPILE`. For more information, see [Query hints](https://learn.microsoft.com/en-us/sql/t-sql/queries/hints-transact-sql-query?view=sql-server-ver17).
For some applications, recompiling the query each time it executes might take too much time. The `OPTIMIZE FOR` query hint can help even if you don't use the `RECOMPILE` option. For example, you could add an `OPTIMIZE FOR` option to the stored procedure `Sales.GetRecentSales` to specify a specific date. The following example adds the `OPTIMIZE FOR` option to the `Sales.GetRecentSales` procedure.
SQL
Copy
```
USE AdventureWorks2022;
GO

IF OBJECT_ID('Sales.GetRecentSales', 'P') IS NOT NULL
    DROP PROCEDURE Sales.GetRecentSales;
GO

CREATE PROCEDURE Sales.GetRecentSales
@date DATETIME
AS
BEGIN
    IF @date IS NULL
        SET @date = DATEADD(MONTH, -3,
            (SELECT MAX(ORDERDATE)
            FROM Sales.SalesOrderHeader));
    SELECT *
    FROM Sales.SalesOrderHeader AS h, Sales.SalesOrderDetail AS d
    WHERE h.SalesOrderID = d.SalesOrderID AND h.OrderDate > @date
    OPTION (OPTIMIZE FOR (@date = '2004-05-01 00:00:00.000'));
END
GO

```

[](https://learn.microsoft.com/en-us/sql/relational-databases/statistics/statistics?view=sql-server-ver17#improve-cardinality-estimates-with-plan-guides)
### Improve cardinality estimates with plan guides
For some applications, query design guidelines might not apply because you can't change the query or the `RECOMPILE` query hint might cause too many recompiles. You can use plan guides to specify other hints, such as USE PLAN, to control the behavior of the query while investigating application changes with the application vendor. For more information about plan guides, see [Plan Guides](https://learn.microsoft.com/en-us/sql/relational-databases/performance/plan-guides?view=sql-server-ver17).
In Azure SQL Database, consider Query Store hints to force plans, instead of plan guides. For more information, see [Query Store hints](https://learn.microsoft.com/en-us/sql/relational-databases/performance/query-store-hints?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/relational-databases/statistics/statistics?view=sql-server-ver17#related-content)
