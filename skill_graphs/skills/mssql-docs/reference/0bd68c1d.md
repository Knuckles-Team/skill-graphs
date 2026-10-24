## When to update statistics
The Query Optimizer determines when statistics might be out-of-date and then updates them when they're needed for a query plan. In some cases, you can improve the query plan and therefore improve query performance by updating statistics more frequently than occur when [AUTO_UPDATE_STATISTICS](https://learn.microsoft.com/en-us/sql/t-sql/statements/alter-database-transact-sql-set-options?view=sql-server-ver17#auto_update_statistics) is on. You can update statistics with the `UPDATE STATISTICS` statement or the stored procedure `sp_updatestats`.
Updating statistics ensures that queries compile with up-to-date statistics. Updating statistics via any process can cause query plans to recompile automatically. We recommend not manually updating statistics too frequently because there's a performance tradeoff between improving query plans and the time it takes to recompile queries. The specific tradeoffs depend on your application.
When updating statistics with `UPDATE STATISTICS` or `sp_updatestats`, we recommend keeping AUTO_UPDATE_STATISTICS set to ON so that the Query Optimizer routinely updates statistics.
  * For more information about how to update statistics on a column, an index, a table, or an indexed view, see [UPDATE STATISTICS](https://learn.microsoft.com/en-us/sql/t-sql/statements/update-statistics-transact-sql?view=sql-server-ver17).
  * For information about how to update statistics for all user-defined and internal tables in the database, see the stored procedure [sp_updatestats](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-updatestats-transact-sql?view=sql-server-ver17).
  * For more information on the thresholds for automatic statistics updates, see [AUTO_UPDATE_STATISTICS Option](https://learn.microsoft.com/en-us/sql/relational-databases/statistics/statistics?view=sql-server-ver17#auto_update_statistics-option).


When `AUTO_UPDATE_STATISTICS` is set to OFF, plan recompilation can still occur for various other reasons, but don't occur automatically due to out-of-date statistics updates. When `AUTO_UPDATE_STATISTICS` is set to OFF, statistics updates only occur via other manually scheduled processes, such as maintenance plans. Setting `AUTO_UPDATE_STATISTICS` to OFF can therefore cause suboptimal query plans and degraded query performance.
[](https://learn.microsoft.com/en-us/sql/relational-databases/statistics/statistics?view=sql-server-ver17#detect-out-of-date-statistics)
### Detect out-of-date statistics
To determine when statistics were last updated, use the [sys.dm_db_stats_properties](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/sys-dm-db-stats-properties-transact-sql?view=sql-server-ver17) or [STATS_DATE](https://learn.microsoft.com/en-us/sql/t-sql/functions/stats-date-transact-sql?view=sql-server-ver17) functions.
Consider updating statistics for the following conditions:
  * Query execution times are slow.
  * Insert operations occur on ascending or descending key columns.
  * After maintenance operations.


For examples updating statistics manually, see [UPDATE STATISTICS](https://learn.microsoft.com/en-us/sql/t-sql/statements/update-statistics-transact-sql?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/relational-databases/statistics/statistics?view=sql-server-ver17#query-execution-times-are-slow)
### Query execution times are slow
If query response times are slow or unpredictable, ensure that queries have up-to-date statistics before performing additional troubleshooting steps.
[](https://learn.microsoft.com/en-us/sql/relational-databases/statistics/statistics?view=sql-server-ver17#insert-operations-occur-on-ascending-or-descending-key-columns)
### Insert operations occur on ascending or descending key columns
Statistics on ascending or descending key columns, such as IDENTITY or real-time timestamp columns, might require more frequent statistics updates than the Query Optimizer performs. Insert operations append new values to ascending or descending columns. The number of rows added might be too small to trigger a statistics update. If statistics aren't up-to-date and queries select from the most recently added rows, the current statistics don't have cardinality estimates for these new values. This can result in inaccurate cardinality estimates and slow query performance.
For example, a query that selects from the most recent sales order dates have inaccurate cardinality estimates if the statistics aren't updated to include cardinality estimates for the most recent sales order dates.
[](https://learn.microsoft.com/en-us/sql/relational-databases/statistics/statistics?view=sql-server-ver17#after-maintenance-operations)
### After maintenance operations
Consider updating statistics after performing maintenance procedures that change the distribution of data, such as truncating a table or performing a bulk insert of a large percentage of the rows. This can avoid future delays in query processing while queries wait for automatic statistics updates.
Operations such as rebuilding, defragmenting, or reorganizing an index don't change the distribution of data. Therefore, you don't need to update statistics after performing [ALTER INDEX REBUILD](https://learn.microsoft.com/en-us/sql/t-sql/statements/alter-index-transact-sql?view=sql-server-ver17#rebuilding-indexes), [DBCC DBREINDEX](https://learn.microsoft.com/en-us/sql/t-sql/database-console-commands/dbcc-dbreindex-transact-sql?view=sql-server-ver17), [DBCC INDEXDEFRAG](https://learn.microsoft.com/en-us/sql/t-sql/database-console-commands/dbcc-indexdefrag-transact-sql?view=sql-server-ver17), or [ALTER INDEX REORGANIZE](https://learn.microsoft.com/en-us/sql/t-sql/statements/alter-index-transact-sql?view=sql-server-ver17#reorganizing-indexes) operations. The Query Optimizer updates statistics when you rebuild an index on a table or view with `ALTER INDEX REBUILD` or `DBCC DBREINDEX`, however this statistics update is a byproduct of re-creating the index. The Query Optimizer doesn't update statistics after `DBCC INDEXDEFRAG` or `ALTER INDEX REORGANIZE` operations.
Starting with SQL Server 2016 (13.x) SP1 CU4, use the PERSIST_SAMPLE_PERCENT option of [CREATE STATISTICS](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-statistics-transact-sql?view=sql-server-ver17) or [UPDATE STATISTICS](https://learn.microsoft.com/en-us/sql/t-sql/statements/update-statistics-transact-sql?view=sql-server-ver17), to set and retain a specific sampling percentage for subsequent statistic updates that don't explicitly specify a sampling percentage.
[](https://learn.microsoft.com/en-us/sql/relational-databases/statistics/statistics?view=sql-server-ver17#automatic-index-and-statistics-management)
### Automatic index and statistics management
Use smart solutions such as
[](https://learn.microsoft.com/en-us/sql/relational-databases/statistics/statistics?view=sql-server-ver17#queries-that-use-statistics-effectively)
