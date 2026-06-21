# Monitor performance by using the Query Store
Feedback
Summarize this article for me
##  In this article
  1. [Enable the Query Store](https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitoring-performance-by-using-the-query-store?view=sql-server-ver17#enable-the-query-store)
  2. [Information in the Query Store](https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitoring-performance-by-using-the-query-store?view=sql-server-ver17#information-in-the-query-store)
  3. [Query Store for secondary replicas](https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitoring-performance-by-using-the-query-store?view=sql-server-ver17#query-store-for-secondary-replicas)
  4. [Use the Regressed Queries feature](https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitoring-performance-by-using-the-query-store?view=sql-server-ver17#use-the-regressed-queries-feature)
  5. [Find waiting queries](https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitoring-performance-by-using-the-query-store?view=sql-server-ver17#find-waiting-queries)
  6. [Configuration options](https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitoring-performance-by-using-the-query-store?view=sql-server-ver17#configuration-options)
  7. [Related views, functions, and procedures](https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitoring-performance-by-using-the-query-store?view=sql-server-ver17#related-views-functions-and-procedures)
  8. [Query Store maintenance](https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitoring-performance-by-using-the-query-store?view=sql-server-ver17#query-store-maintenance)
  9. [Performance auditing and troubleshooting](https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitoring-performance-by-using-the-query-store?view=sql-server-ver17#performance-auditing-and-troubleshooting)
  10. [Related content](https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitoring-performance-by-using-the-query-store?view=sql-server-ver17#related-content)

Show 6 more
**Applies to:** ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) SQL Server 2016 (13.x) and later versions ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure SQL Database](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure SQL Managed Instance](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure Synapse Analytics (dedicated SQL pool only)](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL database in Microsoft Fabric](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to)
The Query Store feature provides you with insight on query plan choice and performance for SQL Server, Azure SQL Database, Fabric SQL database, Azure SQL Managed Instance, and Azure Synapse Analytics. The Query Store simplifies performance troubleshooting by helping you quickly find performance differences caused by query plan changes. Query Store automatically captures a history of queries, plans, and runtime statistics, and retains these for your review. It separates data by time windows so you can see database usage patterns and understand when query plan changes happened on the server.
You can configure Query Store using the [ALTER DATABASE SET options](https://learn.microsoft.com/en-us/sql/t-sql/statements/alter-database-transact-sql-set-options?view=sql-server-ver17) option.
  * For information about operating the Query Store in Azure SQL Database, see [Operating the Query Store in Azure SQL Database](https://learn.microsoft.com/en-us/sql/relational-databases/performance/best-practice-with-the-query-store?view=sql-server-ver17#Insight).
  * For information on discovering actionable information and tune performance with the Query Store, see [Tune performance with the Query Store](https://learn.microsoft.com/en-us/sql/relational-databases/performance/tune-performance-with-the-query-store?view=sql-server-ver17).
  * For information on shaping query plans without changing application code, see [Query Store hints](https://learn.microsoft.com/en-us/sql/relational-databases/performance/query-store-hints?view=sql-server-ver17).


If you're using Query Store for just in time workload insights in SQL Server 2016 (13.x), plan to install the performance scalability fixes in [KB 4340759](https://support.microsoft.com/help/4340759) as soon as possible.
[](https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitoring-performance-by-using-the-query-store?view=sql-server-ver17#enable-the-query-store)
## Enable the Query Store
  * Query Store is enabled by default for new Azure SQL Database and Azure SQL Managed Instance databases.
  * Query Store isn't enabled by default for SQL Server 2016 (13.x), SQL Server 2017 (14.x), SQL Server 2019 (15.x). It's enabled by default in the `READ_WRITE` mode for new databases starting with SQL Server 2022 (16.x). To enable features to better track performance history, troubleshoot query plan related issues, and enable new capabilities in SQL Server 2022 (16.x), we recommend enabling Query Store on all databases.
  * Query Store isn't enabled by default for new Azure Synapse Analytics databases.


[](https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitoring-performance-by-using-the-query-store?view=sql-server-ver17#use-the-query-store-page-in-sql-server-management-studio)
### Use the Query Store page in SQL Server Management Studio
  1. In Object Explorer, right-click a database, and then select **Properties**.
Requires at least version 16 of Management Studio.
  2. In the **Database Properties** dialog box, select the **Query Store** page.
  3. In the **Operation Mode (Requested)** box, select **Read Write**.


[](https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitoring-performance-by-using-the-query-store?view=sql-server-ver17#use-transact-sql-statements)
### Use Transact-SQL statements
Use the `ALTER DATABASE` statement to enable the Query Store for a given database. For example:
SQL
Copy
```
ALTER DATABASE <database_name>
SET QUERY_STORE = ON (OPERATION_MODE = READ_WRITE);

```

Options to configure the Query Store in Fabric SQL database with `ALTER DATABASE` are currently limited.
In Azure Synapse Analytics, enable the Query Store without additional options, for example:
SQL
Copy
```
ALTER DATABASE <database_name>
SET QUERY_STORE = ON;

```

For more syntax options related to the Query Store, see [ALTER DATABASE SET options](https://learn.microsoft.com/en-us/sql/t-sql/statements/alter-database-transact-sql-set-options?view=sql-server-ver17).
Query Store can't be enabled for the `master` or `tempdb` databases.
For information on enabling Query Store and keeping it adjusted to your workload, refer to [Best Practice with the Query Store](https://learn.microsoft.com/en-us/sql/relational-databases/performance/best-practice-with-the-query-store?view=sql-server-ver17#Configure).
[](https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitoring-performance-by-using-the-query-store?view=sql-server-ver17#information-in-the-query-store)
## Information in the Query Store
Execution plans for any specific query in SQL Server typically evolve over time due to a number of different reasons such as statistics changes, schema changes, creation/deletion of indexes, etc. The procedure cache (where cached query plans are stored) only stores the latest execution plan. Plans also get evicted from the plan cache due to memory pressure. As a result, query performance regressions caused by execution plan changes can be non-trivial and time consuming to resolve.
Since the Query Store retains multiple execution plans per query, it can enforce policies to direct the Query Processor to use a specific execution plan for a query. This is referred to as plan forcing. Plan forcing in Query Store is provided by using a mechanism similar to the [Query hints](https://learn.microsoft.com/en-us/sql/t-sql/queries/hints-transact-sql-query?view=sql-server-ver17) query hint, but it doesn't require any change in user applications. Plan forcing can resolve a query performance regression caused by a plan change in a very short period of time.
Query Store collects plans for DML Statements such as `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `MERGE`, and `BULK INSERT`.
By design, Query Store doesn't collect plans for DDL statements such as `CREATE INDEX`, etc. Query Store captures cumulative resource consumption by collecting plans for the underlying DML statements. For example, Query Store might display the `SELECT` and `INSERT` statements executed internally to populate a new index.
Query Store doesn't collect data for natively compiled stored procedures by default. Use [sys.sp_xtp_control_query_exec_stats](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sys-sp-xtp-control-query-exec-stats-transact-sql?view=sql-server-ver17) to enable data collection for natively compiled stored procedures.
**Wait stats** are another source of information that helps to troubleshoot performance in the Database Engine. For a long time, wait statistics were available only on instance level, which made it hard to backtrack waits to a specific query. Starting with SQL Server 2017 (14.x) and Azure SQL Database, Query Store includes a dimension that tracks wait stats. The following example enables the Query Store to collect wait stats.
SQL
Copy
```
ALTER DATABASE <database_name>
SET QUERY_STORE = ON ( WAIT_STATS_CAPTURE_MODE = ON );

```

Common scenarios for using the Query Store feature are:
  * Quickly find and fix a plan performance regression by forcing the previous query plan. Fix queries that have recently regressed in performance due to execution plan changes.
  * Determine the number of times a query was executed in a given time window, assisting a DBA in troubleshooting performance resource problems.
  * Identify top _n_ queries (by execution time, memory consumption, etc.) in the past _x_ hours.
  * Audit the history of query plans for a given query.
  * Analyze the resource (CPU, I/O, and Memory) usage patterns for a particular database.
  * Identify top n queries that are waiting on resources.
  * Understand wait nature for a particular query or plan.


The Query Store contains three stores:
  * a **plan store** for persisting the execution plan information.
  * a **runtime stats store** for persisting the execution statistics information.
  * a **wait stats store** for persisting wait statistics information.


The number of unique plans that can be stored for a query in the plan store is limited by the **max_plans_per_query** configuration option. To enhance performance, the information is written to the stores asynchronously. To minimize space usage, the runtime execution statistics in the runtime stats store are aggregated over a fixed time window. The information in these stores is visible by querying the Query Store catalog views.
The following query returns information about queries, their plans, compile time and run-time statistics from the Query Store.
SQL
Copy
```
SELECT Txt.query_text_id, Txt.query_sql_text, Pln.plan_id, Qry.*, RtSt.*
FROM sys.query_store_plan AS Pln
INNER JOIN sys.query_store_query AS Qry
    ON Pln.query_id = Qry.query_id
INNER JOIN sys.query_store_query_text AS Txt
    ON Qry.query_text_id = Txt.query_text_id
INNER JOIN sys.query_store_runtime_stats RtSt
ON Pln.plan_id = RtSt.plan_id;

```

[](https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitoring-performance-by-using-the-query-store?view=sql-server-ver17#query-store-for-secondary-replicas)
## Query Store for secondary replicas
**Applies to:** SQL Server 2025 (17.x), Azure SQL Database
The Query Store for secondary replicas feature enables the same Query Store functionality on secondary replica workloads that is available for primary replicas. When Query Store for secondary replicas is enabled, replicas send the query execution information that would normally be stored in the Query Store back to the primary replica. The primary replica then persists the data to disk within its own Query Store. In essence, there's one Query Store shared between the primary and all secondary replicas. The Query Store exists on the primary replica and stores data for all replicas together.
For more information, see [Query Store for secondary replicas](https://learn.microsoft.com/en-us/sql/relational-databases/performance/query-store-for-secondary-replicas?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitoring-performance-by-using-the-query-store?view=sql-server-ver17#use-the-regressed-queries-feature)
## Use the Regressed Queries feature
After enabling the Query Store, refresh the database portion of the Object Explorer pane to add the **Query Store** section.
![Screenshot of the Query Store reporting tree in SSMS Object Explorer.](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/monitoring-performance-by-using-the-query-store/object-explorer-query-store.png?view=sql-server-ver17)
For Azure Synapse Analytics, Query Store views are available under **System Views** in the database portion of the Object Explorer pane.
Select **Regressed Queries** to open the **Regressed Queries** pane in SQL Server Management Studio. The Regressed Queries pane shows you the queries and plans in the Query Store. Use the dropdown list boxes at the top to filter queries based on various criteria: Duration (ms) (Default), CPU Time (ms), Logical Reads (KB), Logical Writes (KB), Physical Reads (KB), CLR Time (ms), DOP, Memory Consumption (KB), Row Count, Log Memory Used (KB), Temp DB Memory Used (KB), and Wait Time (ms).
Select a plan to see the graphical query plan. Buttons are available to view the source query, force and unforce a query plan, toggle between grid and chart formats, compare selected plans (if more than one is selected), and refresh the display.
![Screenshot of the SQL Server Regressed Queries report in SSMS Object Explorer.](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/monitoring-performance-by-using-the-query-store/object-explorer-regressed-queries.png?view=sql-server-ver17)
To force a plan, select a query and plan, then select **Force Plan**. You can only force plans that were saved by the query plan feature and are still retained in the query plan cache.
[](https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitoring-performance-by-using-the-query-store?view=sql-server-ver17#find-waiting-queries)
## Find waiting queries
Starting with SQL Server 2017 (14.x) and Azure SQL Database, wait statistics per query over time are available in Query Store.
In Query Store, wait types are combined into **wait categories**. The mapping of wait categories to wait types is available in [sys.query_store_wait_stats (Transact-SQL)](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-query-store-wait-stats-transact-sql?view=sql-server-ver17#wait-categories-mapping-table).
Select **Query Wait Statistics** to open the **Query Wait Statistics** pane in SQL Server Management Studio 18.0 or higher versions. The Query Wait Statistics pane shows you a bar chart containing the top wait categories in the Query Store. Use the dropdown list at the top to select an aggregate criteria for the wait time: avg, max, min, std dev, and **total** (default).
![Screenshot of the SQL Server Query Wait Statistics report in SSMS Object Explorer.](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/monitoring-performance-by-using-the-query-store/query-store-waits.png?view=sql-server-ver17)
Select a wait category by selecting on the bar and a detail view on the selected wait category displays. This new bar chart contains the queries that contributed to that wait category.
[ ![Screenshot of the SQL Server Query Wait Statistics detail view in SSMS Object Explorer.](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/monitoring-performance-by-using-the-query-store/query-store-waits-detail.png?view=sql-server-ver17) ](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/monitoring-performance-by-using-the-query-store/query-store-waits-detail.png?view=sql-server-ver17#lightbox)
Use the dropdown list box at the top to filter queries based on various wait time criteria for the selected wait category: avg, max, min, std dev, and **total** (default). Select a plan to see the graphical query plan. Buttons are available to view the source query, force, and unforce a query plan, and refresh the display.
**Wait categories** are combining different wait types into buckets similar by nature. Different wait categories require a different follow-up analysis to resolve the issue, but wait types from the same category lead to very similar troubleshooting experiences, and providing the affected query on top of waits would be the missing piece to complete most such investigations successfully.
Here are some examples how you can get more insights into your workload before and after introducing wait categories in Query Store:
Expand table
Previous experience | New experience | Action
---|---|---
High RESOURCE_SEMAPHORE waits per database | High Memory waits in Query Store for specific queries | Find the top memory consuming queries in Query Store. These queries are probably delaying further progress of the affected queries. Consider using MAX_GRANT_PERCENT query hint for these queries, or for the affected queries.
High LCK_M_X waits per database | High Lock waits in Query Store for specific queries | Check the query texts for the affected queries and identify the target entities. Look in Query Store for other queries modifying the same entity, which are executed frequently and/or have high duration. After identifying these queries, consider changing the application logic to improve concurrency, or use a less restrictive isolation level.
High PAGEIOLATCH_SH waits per database | High Buffer `IO` waits in Query Store for specific queries | Find the queries with a high number of physical reads in Query Store. If they match the queries with high `IO` waits, consider introducing an index on the underlying entity, in order to do seeks instead of scans, and thus minimize the `IO` overhead of the queries.
High SOS_SCHEDULER_YIELD waits per database | High CPU waits in Query Store for specific queries | Find the top CPU consuming queries in Query Store. Among them, identify the queries for which high CPU trend correlates with high CPU waits for the affected queries. Focus on optimizing those queries - there could be a plan regression, or perhaps a missing index.
[](https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitoring-performance-by-using-the-query-store?view=sql-server-ver17#configuration-options)
## Configuration options
For the available options to configure Query Store parameters, see [ALTER DATABASE SET options (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/statements/alter-database-transact-sql-set-options?view=sql-server-ver17#query-store).
Query the `sys.database_query_store_options` view to determine the current options of the Query Store. For more information about the values, see [sys.database_query_store_options](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-database-query-store-options-transact-sql?view=sql-server-ver17).
For examples about setting configuration options using Transact-SQL statements, see [Option Management](https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitoring-performance-by-using-the-query-store?view=sql-server-ver17#OptionMgmt).
For Azure Synapse Analytics, the Query Store can be enabled as on other platforms but additional configuration options aren't supported.
[](https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitoring-performance-by-using-the-query-store?view=sql-server-ver17#related-views-functions-and-procedures)
## Related views, functions, and procedures
View and manage Query Store through Management Studio or by using the following views and procedures.
[](https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitoring-performance-by-using-the-query-store?view=sql-server-ver17#query-store-functions)
### Query Store functions
Functions help operations with the Query Store.
[sys.fn_stmt_sql_handle_from_sql_stmt](https://learn.microsoft.com/en-us/sql/relational-databases/system-functions/sys-fn-stmt-sql-handle-from-sql-stmt-transact-sql?view=sql-server-ver17)
[](https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitoring-performance-by-using-the-query-store?view=sql-server-ver17#query-store-catalog-views)
### Query Store catalog views
Catalog views present information about the Query Store.
[sys.database_query_store_options](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-database-query-store-options-transact-sql?view=sql-server-ver17)
[sys.query_context_settings](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-query-context-settings-transact-sql?view=sql-server-ver17)
[sys.query_store_plan](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-query-store-plan-transact-sql?view=sql-server-ver17)
[sys.query_store_query](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-query-store-query-transact-sql?view=sql-server-ver17)
[sys.query_store_query_text](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-query-store-query-text-transact-sql?view=sql-server-ver17)
[sys.query_store_runtime_stats](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-query-store-runtime-stats-transact-sql?view=sql-server-ver17)
[sys.query_store_wait_stats](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-query-store-wait-stats-transact-sql?view=sql-server-ver17)
[sys.query_store_runtime_stats_interval](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-query-store-runtime-stats-interval-transact-sql?view=sql-server-ver17)
[sys.database_query_store_internal_state](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-database-query-store-internal-state-transact-sql?view=sql-server-ver17)
[](https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitoring-performance-by-using-the-query-store?view=sql-server-ver17#query-store-stored-procedures)
### Query Store stored procedures
Stored procedures configure the Query Store.
[sp_query_store_flush_db](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-query-store-flush-db-transact-sql?view=sql-server-ver17)
[sp_query_store_reset_exec_stats](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-query-store-reset-exec-stats-transact-sql?view=sql-server-ver17)
[sp_query_store_force_plan](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-query-store-force-plan-transact-sql?view=sql-server-ver17)
[sp_query_store_unforce_plan](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-query-store-unforce-plan-transact-sql?view=sql-server-ver17)
[sp_query_store_remove_plan](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-query-store-remove-plan-transact-sql?view=sql-server-ver17)
[sp_query_store_remove_query](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-query-store-remove-query-transact-sql?view=sql-server-ver17)
[sp_query_store_clear_message_queues](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-query-store-clear-message-queues-transact-sql?view=sql-server-ver17)
`sp_query_store_consistency_check` (Transact-SQL)1
1 In extreme scenarios Query Store can enter an ERROR state because of internal errors. Starting with SQL Server 2017 (14.x), if this happens, Query Store can be recovered by executing the `sp_query_store_consistency_check` stored procedure in the affected database. See [sys.database_query_store_options](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-database-query-store-options-transact-sql?view=sql-server-ver17) for more details described in the `actual_state_desc` column description.
[](https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitoring-performance-by-using-the-query-store?view=sql-server-ver17#query-store-maintenance)
## Query Store maintenance
Best practices and recommendations for maintenance and management of the Query Store have been expanded in this article: [Best practices for managing the Query Store](https://learn.microsoft.com/en-us/sql/relational-databases/performance/manage-the-query-store?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitoring-performance-by-using-the-query-store?view=sql-server-ver17#performance-auditing-and-troubleshooting)
## Performance auditing and troubleshooting
For more information about diving into performance tuning with Query Store, see [Tune performance with the Query Store](https://learn.microsoft.com/en-us/sql/relational-databases/performance/tune-performance-with-the-query-store?view=sql-server-ver17).
Other performance topics:
  * [Query Store Usage Scenarios](https://learn.microsoft.com/en-us/sql/relational-databases/performance/query-store-usage-scenarios?view=sql-server-ver17)


[](https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitoring-performance-by-using-the-query-store?view=sql-server-ver17#related-content)
## Related content
  * [Query Store stored procedures (Transact-SQL)](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/query-store-stored-procedures-transact-sql?view=sql-server-ver17)
  * [Query Store catalog views (Transact-SQL)](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/query-store-catalog-views-transact-sql?view=sql-server-ver17)
  * [sys.database_query_store_options (Transact-SQL)](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-database-query-store-options-transact-sql?view=sql-server-ver17)
  * [Live Query Statistics](https://learn.microsoft.com/en-us/sql/relational-databases/performance/live-query-statistics?view=sql-server-ver17)
  * [Activity Monitor](https://learn.microsoft.com/en-us/sql/relational-databases/performance-monitor/activity-monitor?view=sql-server-ver17)
  * [How Query Store collects data](https://learn.microsoft.com/en-us/sql/relational-databases/performance/how-query-store-collects-data?view=sql-server-ver17)
  * [Monitor and Tune for Performance](https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitor-and-tune-for-performance?view=sql-server-ver17)
  * [Performance monitoring and tuning tools](https://learn.microsoft.com/en-us/sql/relational-databases/performance/performance-monitoring-and-tuning-tools?view=sql-server-ver17)
  * [Use the Query Store with In-Memory OLTP](https://learn.microsoft.com/en-us/sql/relational-databases/performance/using-the-query-store-with-in-memory-oltp?view=sql-server-ver17)
  * [Best practices for monitoring workloads with Query Store](https://learn.microsoft.com/en-us/sql/relational-databases/performance/best-practice-with-the-query-store?view=sql-server-ver17)
  * [Best practices for managing the Query Store](https://learn.microsoft.com/en-us/sql/relational-databases/performance/manage-the-query-store?view=sql-server-ver17)
  * [Tune performance with the Query Store](https://learn.microsoft.com/en-us/sql/relational-databases/performance/tune-performance-with-the-query-store?view=sql-server-ver17)
  * [Query Store hints](https://learn.microsoft.com/en-us/sql/relational-databases/performance/query-store-hints?view=sql-server-ver17)
  * [Query Store Usage Scenarios](https://learn.microsoft.com/en-us/sql/relational-databases/performance/query-store-usage-scenarios?view=sql-server-ver17)
  * [Open Activity Monitor in SQL Server Management Studio (SSMS)](https://learn.microsoft.com/en-us/sql/relational-databases/performance-monitor/open-activity-monitor-sql-server-management-studio?view=sql-server-ver17)


* * *
## Feedback
Was this page helpful?
Yes No No
Need help with this topic?
Want to try using Ask Learn to clarify or guide you through this topic?
Ask Learn Ask Learn
Suggest a fix?
* * *
##  Additional resources
  * [ Best practices for managing the Query Store - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/performance/manage-the-query-store?source=recommendations)
Learn best practices for managing the SQL Server Query Store, including version specific details, managing custom capture policies, and other performance features.
  * [ Best Practices for Monitoring Workloads with Query Store - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/performance/best-practice-with-the-query-store?source=recommendations)
Learn best practices for using SQL Server Query Store with your workload, such as using the latest SQL Server Management Studio and Query Performance Insight.
  * [ How Query Store collects data - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/performance/how-query-store-collects-data?source=recommendations)
SQL Server Query Store persists query-related data in the internal tables and presents it to users through a set of views.
  * [ sys.database_query_store_options (Transact-SQL) - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-database-query-store-options-transact-sql?source=recommendations)
sys.database_query_store_options returns the Query Store options for this database.
  * [ Tune performance with the Query Store - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/performance/tune-performance-with-the-query-store?source=recommendations)
The Query Store can be used to discover and tune query performance in all SQL Server and Azure SQL platforms.
  * [ sys.query_store_runtime_stats (Transact-SQL) - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-query-store-runtime-stats-transact-sql?source=recommendations)
sys.query_store_runtime_stats (Transact-SQL)
  * [ Query Store for Secondary Replicas - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/performance/query-store-for-secondary-replicas?source=recommendations)
Query Store can be configured to monitor and tuning workloads on secondary read-only replicas.
  * [ sys.query_store_wait_stats (Transact-SQL) - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-query-store-wait-stats-transact-sql?source=recommendations)
sys.query_store_wait_stats (Transact-SQL)


Show 5 more
Module
[ Explore query performance optimization - Training ](https://learn.microsoft.com/en-us/training/modules/explore-query-performance-optimization/?source=recommendations)
Explore query performance optimization
Certification
[ Microsoft Certified: Azure Database Administrator Associate - Certifications ](https://learn.microsoft.com/en-us/credentials/certifications/azure-database-administrator-associate/?source=recommendations)
Administer an SQL Server database infrastructure for cloud, on-premises and hybrid relational databases using the Microsoft PaaS relational database offerings.
Mar 8, 4 PM - Mar 8, 4 PM
Experiment with what's next in AI-driven apps and agent design
* * *
  * Last updated on 11/18/2025


##  In this article
  1. [Enable the Query Store](https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitoring-performance-by-using-the-query-store?view=sql-server-ver17#enable-the-query-store)
  2. [Information in the Query Store](https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitoring-performance-by-using-the-query-store?view=sql-server-ver17#information-in-the-query-store)
  3. [Query Store for secondary replicas](https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitoring-performance-by-using-the-query-store?view=sql-server-ver17#query-store-for-secondary-replicas)
  4. [Use the Regressed Queries feature](https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitoring-performance-by-using-the-query-store?view=sql-server-ver17#use-the-regressed-queries-feature)
  5. [Find waiting queries](https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitoring-performance-by-using-the-query-store?view=sql-server-ver17#find-waiting-queries)
  6. [Configuration options](https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitoring-performance-by-using-the-query-store?view=sql-server-ver17#configuration-options)
  7. [Related views, functions, and procedures](https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitoring-performance-by-using-the-query-store?view=sql-server-ver17#related-views-functions-and-procedures)
  8. [Query Store maintenance](https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitoring-performance-by-using-the-query-store?view=sql-server-ver17#query-store-maintenance)
  9. [Performance auditing and troubleshooting](https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitoring-performance-by-using-the-query-store?view=sql-server-ver17#performance-auditing-and-troubleshooting)
  10. [Related content](https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitoring-performance-by-using-the-query-store?view=sql-server-ver17#related-content)


Was this page helpful?
Yes No No
Need help with this topic?
Want to try using Ask Learn to clarify or guide you through this topic?
Ask Learn Ask Learn
Suggest a fix?
##
Ask Learn
Preview
Ask Learn is an AI assistant that can answer questions, clarify concepts, and define terms using trusted Microsoft documentation.
Please sign in to use Ask Learn.
[ Sign in ](https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitoring-performance-by-using-the-query-store?view=sql-server-ver17)
[English (United States)](https://learn.microsoft.com/en-us/locale?target=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fsql%2Frelational-databases%2Fperformance%2Fmonitoring-performance-by-using-the-query-store%3Fview%3Dsql-server-ver17)
Theme
  * Light
  * Dark
  * High contrast


  * [AI Disclaimer](https://learn.microsoft.com/en-us/principles-for-ai-generated-content)
  * [Previous Versions](https://learn.microsoft.com/en-us/previous-versions/)
  * [Blog](https://techcommunity.microsoft.com/t5/microsoft-learn-blog/bg-p/MicrosoftLearnBlog)
  * [Contribute](https://learn.microsoft.com/en-us/contribute)
  * [Privacy](https://go.microsoft.com/fwlink/?LinkId=521839)
  * [Consumer Health Privacy](https://go.microsoft.com/fwlink/?linkid=2259814)
  * [Terms of Use](https://learn.microsoft.com/en-us/legal/termsofuse)
  * [Trademarks](https://www.microsoft.com/legal/intellectualproperty/Trademarks/)
  * © Microsoft 2026
