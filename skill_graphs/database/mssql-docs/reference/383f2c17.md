## When to create statistics
The Query Optimizer already creates statistics in the following ways:
  1. The Query Optimizer creates statistics for indexes on tables or views when the index is created. These statistics are created on the key columns of the index. If the index is a filtered index, the Query Optimizer creates filtered statistics on the same subset of rows specified for the filtered index. For more information about filtered indexes, see [Create filtered indexes](https://learn.microsoft.com/en-us/sql/relational-databases/indexes/create-filtered-indexes?view=sql-server-ver17) and [CREATE INDEX](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-index-transact-sql?view=sql-server-ver17).
In SQL Server 2014 (12.x) and later versions, statistics aren't created by scanning all rows in the table when a partitioned index is created or rebuilt. Instead, the Query Optimizer uses the default sampling algorithm to generate statistics. After upgrading a database with partitioned indexes, you might notice a difference in the histogram data for these indexes. This change in behavior might not affect query performance. To obtain statistics on partitioned indexes by scanning all the rows in the table, use `CREATE STATISTICS` or `UPDATE STATISTICS` with the `FULLSCAN` clause.
  2. The Query Optimizer creates statistics for single columns in query predicates when [AUTO_CREATE_STATISTICS](https://learn.microsoft.com/en-us/sql/t-sql/statements/alter-database-transact-sql-set-options?view=sql-server-ver17#auto_create_statistics) is on.


For most queries, these two methods for creating statistics ensure a high-quality query plan; in a few cases, you can improve query plans by creating additional statistics with the [CREATE STATISTICS](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-statistics-transact-sql?view=sql-server-ver17) statement. These additional statistics can capture statistical correlations that the Query Optimizer doesn't account for when it creates statistics for indexes or single columns. Your application might have additional statistical correlations in the table data that, if calculated into a statistics object, could enable the Query Optimizer to improve query plans. For example, filtered statistics on a subset of data rows or multicolumn statistics on query predicate columns might improve the query plan.
When creating statistics with the CREATE STATISTICS statement, we recommend keeping the AUTO_CREATE_STATISTICS option ON so that the Query Optimizer continues to routinely create single-column statistics for query predicate columns. For more information about query predicates, see [Search condition](https://learn.microsoft.com/en-us/sql/t-sql/queries/search-condition-transact-sql?view=sql-server-ver17).
Consider creating statistics with the CREATE STATISTICS statement when any of the following applies:
  * The Database Engine Tuning Advisor suggests creating statistics.
  * The query predicate contains multiple correlated columns that aren't already keys in the same index.
  * The query selects from a subset of data.
  * The query has missing statistics.


For information specific to In-Memory OLTP related tables and statistics, see [Statistics for Memory-Optimized Tables](https://learn.microsoft.com/en-us/sql/relational-databases/in-memory-oltp/statistics-for-memory-optimized-tables?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/relational-databases/statistics/statistics?view=sql-server-ver17#query-predicate-contains-multiple-correlated-columns)
### Query Predicate contains multiple correlated columns
When a query predicate contains multiple columns that have cross-column relationships and dependencies, statistics on the multiple columns might improve the query plan. Statistics on multiple columns contain cross-column correlation statistics, called _densities_ , that aren't available in single-column statistics. Densities can improve cardinality estimates when query results depend on data relationships among multiple columns.
If the columns are already in the same index, the multicolumn statistics object already exists and it isn't necessary to create it manually. If the columns aren't already in the same index, you can create multicolumn statistics by creating an index on the columns or by using the [CREATE STATISTICS](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-statistics-transact-sql?view=sql-server-ver17) statement. It requires more system resources to maintain an index than a statistics object. If the application doesn't require the multicolumn index, you can economize on system resources by creating the statistics object without creating the index.
When you create multicolumn statistics, the order of the columns in the statistics object definition affects the effectiveness of densities for making cardinality estimates. The statistics object stores densities for each prefix of key columns in the statistics object definition. For more information about densities, see [Density](https://learn.microsoft.com/en-us/sql/relational-databases/statistics/statistics?view=sql-server-ver17#density) section in this page.
To create densities that are useful for cardinality estimates, the columns in the query predicate must match one of the prefixes of columns in the statistics object definition. For example, the following example creates a multicolumn statistics object on the columns `LastName`, `MiddleName`, and `FirstName`.
SQL
Copy
```
USE AdventureWorks2022;
GO

IF EXISTS (SELECT name
           FROM sys.stats
           WHERE name = 'LastFirst'
                 AND object_ID = OBJECT_ID('Person.Person'))
    DROP STATISTICS Person.Person.LastFirst;
GO

CREATE STATISTICS LastFirst
    ON Person.Person(LastName, MiddleName, FirstName);
GO

```

In this example, the statistics object `LastFirst` has densities for the following column prefixes: `(LastName)`, `(LastName, MiddleName)`, and `(LastName, MiddleName, FirstName)`. The density isn't available for `(LastName, FirstName)`. If the query uses `LastName` and `FirstName` without using `MiddleName`, the density isn't available for cardinality estimates.
[](https://learn.microsoft.com/en-us/sql/relational-databases/statistics/statistics?view=sql-server-ver17#query-selects-from-a-subset-of-data)
### Query Selects from a subset of data
When the Query Optimizer creates statistics for single columns and indexes, it creates the statistics for the values in all rows. When queries select from a subset of rows, and that subset of rows has a unique data distribution, filtered statistics can improve query plans. You can create filtered statistics by using the [CREATE STATISTICS](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-statistics-transact-sql?view=sql-server-ver17) statement with the [WHERE](https://learn.microsoft.com/en-us/sql/t-sql/queries/where-transact-sql?view=sql-server-ver17) clause to define the filter predicate expression.
For example, using AdventureWorks2025, each product in the `Production.Product` table belongs to one of four categories in the `Production.ProductCategory` table: `Bikes`, `Components`, `Clothing`, and `Accessories`. Each of the categories has a different data distribution for weight: bike weights range from 13.77 to 30.0, component weights range from 2.12 to 1050.00 with some `NULL` values, clothing weights are all `NULL`, and accessory weights are also `NULL`.
Using `Bikes` as an example, filtered statistics on all bike weights provide more accurate statistics to the Query Optimizer and can improve the query plan quality compared with full-table statistics or nonexistent statistics on the Weight column. The bike weight column is a good candidate for filtered statistics but not necessarily a good candidate for a filtered index if the number of weight lookups is relatively small. The performance gain for lookups that a filtered index provides might not outweigh the additional maintenance and storage cost for adding a filtered index to the database.
The following statement creates the `BikeWeights` filtered statistics on all of the subcategories for `Bikes`. The filtered predicate expression defines bikes by enumerating all of the bike subcategories with the comparison `Production.ProductSubcategoryID IN (1,2,3)`. The predicate can't use the `Bikes` category name because it's stored in the `Production.ProductCategory` table, and all columns in the filter expression must be in the same table.
SQL
Copy
```
USE AdventureWorks2022;
GO
IF EXISTS ( SELECT name FROM sys.stats
    WHERE name = 'BikeWeights'
    AND object_ID = OBJECT_ID ('Production.Product'))
DROP STATISTICS Production.Product.BikeWeights;
GO
CREATE STATISTICS BikeWeights
    ON Production.Product (Weight)
WHERE ProductSubcategoryID IN (1,2,3);
GO

```

The Query Optimizer can use the `BikeWeights` filtered statistics to improve the query plan for the following query that selects all of the bikes that weigh more than `25`.
SQL
Copy
```
SELECT P.Weight AS Weight,
       S.Name AS BikeName
FROM Production.Product AS P
     INNER JOIN Production.ProductSubcategory AS S
         ON P.ProductSubcategoryID = S.ProductSubcategoryID
WHERE P.ProductSubcategoryID IN (1, 2, 3)
      AND P.Weight > 25
ORDER BY P.Weight;
GO

```

[](https://learn.microsoft.com/en-us/sql/relational-databases/statistics/statistics?view=sql-server-ver17#query-identifies-missing-statistics)
### Query identifies missing statistics
If an error or other event prevents the Query Optimizer from creating statistics, the Query Optimizer creates the query plan without using statistics. The Query Optimizer marks the statistics as missing and attempts to regenerate the statistics the next time the query is executed.
Missing statistics are indicated as warnings (table name in red text) when the execution plan of a query is graphically displayed using SQL Server Management Studio. Additionally, monitoring the **Missing Column Statistics** event class by using SQL Server Profiler indicates when statistics are missing. For more information, see [Errors and Warnings Event Category (Database Engine)](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/errors-and-warnings-event-category-database-engine?view=sql-server-ver17).
If statistics are missing, perform the following steps:
  * Verify that [AUTO_CREATE_STATISTICS](https://learn.microsoft.com/en-us/sql/t-sql/statements/alter-database-transact-sql-set-options?view=sql-server-ver17#auto_create_statistics) and [AUTO_UPDATE_STATISTICS](https://learn.microsoft.com/en-us/sql/t-sql/statements/alter-database-transact-sql-set-options?view=sql-server-ver17#auto_update_statistics) are ON.
  * Verify that the database isn't read-only. If the database is read-only, a new statistics object can't be saved.
  * Create the missing statistics by using the [CREATE STATISTICS](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-statistics-transact-sql?view=sql-server-ver17) statement.


[](https://learn.microsoft.com/en-us/sql/relational-databases/statistics/statistics?view=sql-server-ver17#temporary-statistics)
#### Temporary statistics
When statistics on a read-only database or read-only snapshot are missing or stale, the Database Engine creates and maintains temporary statistics in `tempdb`. When the Database Engine creates temporary statistics, the statistics name is appended with the suffix __readonly_database_statistic_ to differentiate the temporary statistics from the permanent statistics. The suffix __readonly_database_statistic_ is reserved for statistics generated by the Database Engine. Scripts for the temporary statistics can be created and executed on a read-write database. When scripted, Management Studio changes the suffix of the statistics name from __readonly_database_statistic_ to __readonly_database_statistic_scripted_.
Only the Database Engine can create and update temporary statistics. However, you can delete temporary statistics and monitor statistics properties using the same tools that you use for permanent statistics:
  * Delete temporary statistics using the [DROP STATISTICS](https://learn.microsoft.com/en-us/sql/t-sql/statements/drop-statistics-transact-sql?view=sql-server-ver17) statement.
  * Monitor statistics using the [sys.stats](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-stats-transact-sql?view=sql-server-ver17) and [sys.stats_columns](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-stats-columns-transact-sql?view=sql-server-ver17) catalog views. The `sys.stats` system catalog view includes the `is_temporary` column, to indicate which statistics are permanent and which are temporary.


Because temporary statistics are stored in `tempdb`, a restart of the Database Engine removes all temporary statistics.
Just like for all statistics, creating and updating temporary statistics requires a schema modification (`Sch-M`) lock on the object. This lock might block other queries and processes, including the system redo process on secondary replicas that applies transactions from the primary replica. If this blocking affects query workloads or data propagation, you can disable the automatic creation and update of temporary statistics using the `READABLE_SECONDARY_TEMPORARY_STATS_AUTO_CREATE` and `READABLE_SECONDARY_TEMPORARY_STATS_AUTO_UPDATE` [database-scoped configurations](https://learn.microsoft.com/en-us/sql/t-sql/statements/alter-database-scoped-configuration-transact-sql?view=sql-server-ver17) respectively.
[](https://learn.microsoft.com/en-us/sql/relational-databases/statistics/statistics?view=sql-server-ver17#when-to-update-statistics)
