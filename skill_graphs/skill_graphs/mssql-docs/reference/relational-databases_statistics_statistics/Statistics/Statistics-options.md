## Statistics options
There are options that affect when and how statistics are created and updated. These options are configurable at the database level only.
[](https://learn.microsoft.com/en-us/sql/relational-databases/statistics/statistics?view=sql-server-ver17#auto_create_statistics-option)
### AUTO_CREATE_STATISTICS option
When the automatic create statistics option, [AUTO_CREATE_STATISTICS](https://learn.microsoft.com/en-us/sql/t-sql/statements/alter-database-transact-sql-set-options?view=sql-server-ver17#auto_create_statistics) is ON, the Query Optimizer creates statistics on individual columns in the query predicate, as necessary, to improve cardinality estimates for the query plan. These single-column statistics are created on columns that don't already have a [histogram](https://learn.microsoft.com/en-us/sql/relational-databases/statistics/statistics?view=sql-server-ver17#histogram) in an existing statistics object. The `AUTO_CREATE_STATISTICS` option doesn't determine whether statistics get created for indexes. This option also doesn't generate filtered statistics. It applies strictly to single-column statistics for the full table.
When the Query Optimizer creates statistics as a result of using the `AUTO_CREATE_STATISTICS` option, the statistics name starts with `_WA`. You can use the following query to determine if the Query Optimizer has created statistics for a query predicate column.
SQL
Copy
```
SELECT OBJECT_NAME(s.object_id) AS object_name,
    COL_NAME(sc.object_id, sc.column_id) AS column_name,
    s.name AS statistics_name
FROM sys.stats AS s
    INNER JOIN sys.stats_columns AS sc
        ON s.stats_id = sc.stats_id
        AND s.object_id = sc.object_id
WHERE s.name LIKE '_WA%'
ORDER BY s.name;

```

[](https://learn.microsoft.com/en-us/sql/relational-databases/statistics/statistics?view=sql-server-ver17#auto_update_statistics-option)
### AUTO_UPDATE_STATISTICS option
When the automatic update statistics option, [AUTO_UPDATE_STATISTICS](https://learn.microsoft.com/en-us/sql/t-sql/statements/alter-database-transact-sql-set-options?view=sql-server-ver17#auto_update_statistics) is ON, the Query Optimizer determines when statistics might be out-of-date and then updates them when they're used by a query. This action is also known as statistics recompilation. Statistics become out-of-date after modifications from insert, update, delete, or merge operations change the data distribution in the table or indexed view. The Query Optimizer determines when statistics might be out-of-date by counting the number of row modifications since the last statistics update and comparing the number of row modifications to a threshold. The threshold is based on the table cardinality, which can be defined as the number of rows in the table or indexed view.
Marking statistics as out-of-date based on row modifications occurs even when the `AUTO_UPDATE_STATISTICS` option is OFF. When the `AUTO_UPDATE_STATISTICS` option is OFF, statistics aren't updated, even when they're marked as out-of-date. Plans continue to use the out-of-date statistics objects. Setting `AUTO_UPDATE_STATISTICS` to OFF can cause suboptimal query plans and degraded query performance. Setting the `AUTO_UPDATE STATISTICS` option to ON is recommended.
  * Up to SQL Server 2014 (12.x), the Database Engine uses a recompilation threshold based on the number of rows in the table or indexed view at the time statistics were evaluated. The threshold is different whether a table is temporary or permanent.
Expand table
Table type | Table cardinality (_n_) | Recompilation threshold (# modifications)
---|---|---
Temporary |  _n_ < 6 | 6
Temporary | 6 <= _n_ <= 500 | 500
Permanent |  _n_ <= 500 | 500
Temporary or permanent |  _n_ > 500 | 500 + (0.20 * _n_)
For example if your table contains 20 thousand rows, then the calculation is `500 + (0.2 * 20,000) = 4,500` and the statistics are updated every 4,500 modifications.
  * Starting with SQL Server 2016 (13.x) and with the [database compatibility level](https://learn.microsoft.com/en-us/sql/relational-databases/databases/view-or-change-the-compatibility-level-of-a-database?view=sql-server-ver17) 130, the Database Engine also uses a decreasing, dynamic statistics recompilation threshold that adjusts according to the table cardinality at the time statistics were evaluated. With this change, statistics on large tables are updated more frequently. However, if a database has a compatibility level below 130, then the SQL Server 2014 (12.x) thresholds apply.
Expand table
Table type | Table cardinality (_n_) | Recompilation threshold (# modifications)
---|---|---
Temporary | `n < 6` | 6
Temporary | `6 <= n <= 500` | 500
Permanent | `n <= 500` | 500
Temporary or permanent | `n > 500` | `MIN ( 500 + (0.20 * n), SQRT(1,000 * n) )`
For example if your table contains 2 million rows, then the calculation is the minimum of `500 + (0.20 * 2,000,000) = 400,500` and `SQRT(1,000 * 2,000,000) = 44,721`. This means the statistics are updated every 44,721 modifications.


In SQL Server 2008 R2 (10.50.x) through SQL Server 2014 (12.x), or in SQL Server 2016 (13.x) and later versions with [database compatibility level](https://learn.microsoft.com/en-us/sql/relational-databases/databases/view-or-change-the-compatibility-level-of-a-database?view=sql-server-ver17) 120 and lower versions, enable [trace flag 2371](https://learn.microsoft.com/en-us/sql/t-sql/database-console-commands/dbcc-traceon-trace-flags-transact-sql?view=sql-server-ver17) so that SQL Server uses a decreasing, dynamic statistics update threshold.
While recommended for all scenarios, enabling trace flag 2371 is optional. However, you can use the following guidance for enabling the trace flag 2371 in your pre-SQL Server 2016 (13.x) environment:
  * If you're on an SAP system, enable this trace. For more information, see this [blog on trace flag 2371](https://learn.microsoft.com/en-us/archive/blogs/saponsqlserver/changes-to-automatic-update-statistics-in-sql-server-traceflag-2371).
  * If you have to rely on nightly job to update statistics because current automatic update isn't triggered frequently enough, consider enabling trace flag 2371 to adjust the threshold to table cardinality.


The Query Optimizer checks for out-of-date statistics before compiling a query and before executing a cached query plan. Before it compiles a query, the Query Optimizer uses the columns, tables, and indexed views in the query predicate to determine which statistics might be out-of-date. Before it executes a cached query plan, the Database Engine verifies that the query plan references up-to-date statistics.
The AUTO_UPDATE_STATISTICS option applies to statistics objects created for indexes, single-columns in query predicates, and statistics created with the [CREATE STATISTICS](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-statistics-transact-sql?view=sql-server-ver17) statement. This option also applies to filtered statistics.
You can use the [sys.dm_db_stats_properties](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/sys-dm-db-stats-properties-transact-sql?view=sql-server-ver17) to accurately track the number of rows changed in a table and decide if you wish to update statistics manually.
AUTO_UPDATE_STATISTICS is always OFF for memory-optimized tables.
[](https://learn.microsoft.com/en-us/sql/relational-databases/statistics/statistics?view=sql-server-ver17#auto_update_statistics_async)
### AUTO_UPDATE_STATISTICS_ASYNC
The asynchronous statistics update option, [AUTO_UPDATE_STATISTICS_ASYNC](https://learn.microsoft.com/en-us/sql/t-sql/statements/alter-database-transact-sql-set-options?view=sql-server-ver17#auto_update_statistics_async), determines whether the Query Optimizer uses synchronous or asynchronous statistics updates. By default, the asynchronous statistics update option is OFF, and the Query Optimizer updates statistics synchronously. The AUTO_UPDATE_STATISTICS_ASYNC option applies to statistics objects created for indexes, single columns in query predicates, and statistics created with the [CREATE STATISTICS](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-statistics-transact-sql?view=sql-server-ver17) statement.
To set the asynchronous statistics update option in SQL Server Management Studio, in the _Options_ page of the _Database Properties_ window, both _Auto Update Statistics_ and _Auto Update Statistics Asynchronously_ options need to be set to **True**.
Statistics updates can be either synchronous (the default) or asynchronous.
  * With synchronous statistics updates, queries always compile and execute with up-to-date statistics. When statistics are out-of-date, the Query Optimizer waits for updated statistics before compiling and executing the query.
  * With asynchronous statistics updates, queries compile with existing statistics even if the existing statistics are out-of-date. The Query Optimizer could choose a suboptimal query plan if statistics are out-of-date when the query compiles. Statistics are typically updated soon thereafter. Queries that compile after the stats updates complete benefit from using the updated statistics.


Consider using synchronous statistics when you perform operations that change the distribution of data, such as truncating a table or performing a bulk update of a large percentage of the rows. If you don't manually update the statistics after completing the operation, using synchronous statistics will ensure statistics are up-to-date before queries are executed on the changed data.
Consider using asynchronous statistics to achieve more predictable query response times for the following scenarios:
  * Your application frequently executes the same query, similar queries, or similar cached query plans. Your query response times might be more predictable with asynchronous statistics updates than with synchronous statistics updates because the Query Optimizer can execute incoming queries without waiting for up-to-date statistics. This avoids delaying some queries and not others.
  * Your application has experienced client request time outs caused by one or more queries waiting for updated statistics. In some cases, waiting for synchronous statistics could cause applications with aggressive time outs to fail.


Statistics on local temporary tables are always updated synchronously regardless of AUTO_UPDATE_STATISTICS_ASYNC option. Statistics on global temporary tables are updated synchronously or asynchronously according to the AUTO_UPDATE_STATISTICS_ASYNC option set for the user database.
Asynchronous statistics update is performed by a background request. When the request is ready to write updated statistics to the database, it attempts to acquire a schema modification lock on the statistics metadata object. If a different session is already holding a lock on the same object, asynchronous statistics update is blocked until the schema modification lock can be acquired. Similarly, sessions that need to acquire a schema stability (Sch-S) lock on the statistics metadata object to compile a query can be blocked by the asynchronous statistics update background session, which is already holding or waiting to acquire the schema modification lock. Therefore, for workloads with very frequent query compilations and frequent statistics updates, using asynchronous statistics can increase the likelihood of concurrency issues due to lock blocking.
In Azure SQL Database, Azure SQL Managed Instance, and beginning in SQL Server 2022 (16.x), you can avoid potential concurrency issues using asynchronous statistics update if you enable the ASYNC_STATS_UPDATE_WAIT_AT_LOW_PRIORITY [database-scoped configuration](https://learn.microsoft.com/en-us/sql/t-sql/statements/alter-database-scoped-configuration-transact-sql?view=sql-server-ver17). With this configuration enabled, the background request waits to acquire the schema modification (Sch-M) lock and persist the updated statistics on a separate low-priority queue, allowing other requests to continue compiling queries with existing statistics. Once no other session is holding a lock on the statistics metadata object, the background request acquires its schema modification lock and update statistics. In the unlikely event that the background request can't acquire the lock within a timeout period of several minutes, the asynchronous statistics update will be aborted, and the statistics aren't updated until another automatic statistics update is triggered, or until statistics are [updated manually](https://learn.microsoft.com/en-us/sql/relational-databases/statistics/update-statistics?view=sql-server-ver17).
The ASYNC_STATS_UPDATE_WAIT_AT_LOW_PRIORITY database scoped configuration option is available in Azure SQL Database, Azure SQL Managed Instance, and in SQL Server beginning with SQL Server 2022 (16.x).
[](https://learn.microsoft.com/en-us/sql/relational-databases/statistics/statistics?view=sql-server-ver17#auto_drop-option)
### AUTO_DROP option
**Applies to** : Azure SQL Database, Azure SQL Managed Instance, and starting with SQL Server 2022 (16.x)
In SQL Server prior to SQL Server 2022 (16.x), if statistics are manually created by a user or third party tool on a user database, those statistics objects can block or interfere with schema changes you might desire.
Starting with SQL Server 2022 (16.x), the auto drop option is enabled by default on all new and migrated databases. The `AUTO_DROP` property allows the creation of statistics objects in a mode such that a subsequent schema change _isn't_ blocked by the statistic object, but instead the statistics are dropped as necessary. In this way, manually created statistics with auto drop enabled behave like auto-created statistics.
In Azure SQL Database, Azure SQL Managed Instance, and SQL Server 2022 (16.x) and later versions, automatically created statistics always behave as though the [AUTO_DROP](https://learn.microsoft.com/en-us/sql/relational-databases/statistics/statistics?view=sql-server-ver17#auto_drop-option) has been set.
Trying to set or unset the auto drop property on auto-created statistics can raise errors. Auto-created statistics always uses auto drop. Some backups, when restored, can have this property set incorrectly until the next time the statistics object is updated (manually or automatically). However, auto-created statistics always behave like auto drop statistics. When restoring a database to SQL Server 2022 (16.x) from a previous version, it's recommended to execute `sp_updatestats` on the database, setting the proper metadata for the statistics auto drop feature.
For example, to manually create a statistics object on the `dbo.DatabaseLog` table:
SQL
Copy
```
CREATE STATISTICS [mystats]
    ON [dbo].[DatabaseLog]([DatabaseLogID], [PostTime], [DatabaseUser])
    WITH AUTO_DROP = ON;

```

For example, to update a statistics object auto drop setting on the `dbo.DatabaseLog` table:
SQL
Copy
```
UPDATE STATISTICS [dbo].[DatabaseLog] ([mystats])
    WITH AUTO_DROP = ON;

```

To evaluate the auto drop setting on existing statistics, use the `auto_drop` column in `sys.stats`:
SQL
Copy
```
SELECT object_id,
       [name],
       auto_drop
FROM sys.stats;

```

For more information, see [AUTO_DROP](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-statistics-transact-sql?view=sql-server-ver17#auto_drop---on--off-).
[](https://learn.microsoft.com/en-us/sql/relational-databases/statistics/statistics?view=sql-server-ver17#incremental)
### INCREMENTAL
**Applies to** : SQL Server 2014 (12.x) and later versions.
When INCREMENTAL option of CREATE STATISTICS is ON, the statistics created are per partition statistics. When OFF, the statistics tree is dropped and SQL Server recomputes the statistics. The default is OFF. This setting overrides the database level INCREMENTAL property. For more information about creating incremental statistics, see [CREATE STATISTICS](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-statistics-transact-sql?view=sql-server-ver17). For more information about creating per partition statistics automatically, see [Database Properties (Options Page)](https://learn.microsoft.com/en-us/sql/relational-databases/databases/database-properties-options-page?view=sql-server-ver17#automatic) and [ALTER DATABASE SET options](https://learn.microsoft.com/en-us/sql/t-sql/statements/alter-database-transact-sql-set-options?view=sql-server-ver17).
When new partitions are added to a large table, statistics should be updated to include the new partitions. However the time required to scan the entire table (`FULLSCAN` or `SAMPLE` options) might be quite long. Also, scanning the entire table isn't necessary because only the statistics on the new partitions might be needed. The incremental option creates and stores statistics on a per partition basis, and when updated, only refreshes statistics on those partitions that need new statistics
If per partition statistics aren't supported, the option is ignored and a warning is generated. Incremental stats aren't supported for following statistics types:
  * Statistics created with indexes that aren't partition-aligned with the base table.
  * Statistics created on Always On readable secondary databases.
  * Statistics created on read-only databases.
  * Statistics created on filtered indexes.
  * Statistics created on views.
  * Statistics created on internal tables.
  * Statistics created with spatial indexes or XML indexes.


[](https://learn.microsoft.com/en-us/sql/relational-databases/statistics/statistics?view=sql-server-ver17#when-to-create-statistics)
