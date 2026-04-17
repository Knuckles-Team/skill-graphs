Version SQL Server 2025
  * Analytics Platform System (PDW)
    * [2016-AU7](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/system-dynamic-management-views?view=aps-pdw-2016-au7)
    * [2016-AU6](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/system-dynamic-management-views?view=aps-pdw-2016)
  * [Azure SQL Database](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/system-dynamic-management-views?view=azuresqldb-current)
  * [Azure SQL Managed Instance](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/system-dynamic-management-views?view=azuresqldb-mi-current)
  * [Azure Synapse Analytics](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/system-dynamic-management-views?view=azure-sqldw-latest)
  * [Fabric Data Warehouse](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/system-dynamic-management-views?view=fabric)
  * [Fabric SQL database](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/system-dynamic-management-views?view=fabric-sqldb)
  * SQL Server
    * [2025](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/system-dynamic-management-views?view=sql-server-ver17)
    * [2022](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/system-dynamic-management-views?view=sql-server-ver16)
    * [2019](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/system-dynamic-management-views?view=sql-server-ver15)
    * [2017](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/system-dynamic-management-views?view=sql-server-2017)
    * [2016](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/system-dynamic-management-views?view=sql-server-2016)
  * SQL Server on Linux
    * [2025](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/system-dynamic-management-views?view=sql-server-linux-ver17)
    * [2022](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/system-dynamic-management-views?view=sql-server-linux-ver16)
    * [2019](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/system-dynamic-management-views?view=sql-server-linux-ver15)
    * [2017](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/system-dynamic-management-views?view=sql-server-linux-2017)


Search
Suggestions will filter as you type
  * [SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/?view=sql-server-ver17)
  * [Docs navigation tips](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17)
  * [Previous versions 2005-2014](https://learn.microsoft.com/en-us/sql/sql-server/previous-versions-sql-server?view=sql-server-ver17)
  *     * [What is SQL Server?](https://learn.microsoft.com/en-us/sql/sql-server/what-is-sql-server?view=sql-server-ver17)
    * [Connect to the Database Engine](https://learn.microsoft.com/en-us/sql/sql-server/connect-to-database-engine?view=sql-server-ver17)
  *     *       * [Overview](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/system-dynamic-management-views?view=sql-server-ver17)


Download PDF
Table of contents  Exit editor mode
  1. [ Learn ](https://learn.microsoft.com/en-us/?view=sql-server-ver17)
  2. [ SQL ](https://learn.microsoft.com/en-us/sql/?view=sql-server-ver17)
  3. [ SQL Server ](https://learn.microsoft.com/en-us/sql/sql-server/?view=sql-server-ver17)


  1. [Learn](https://learn.microsoft.com/en-us/?view=sql-server-ver17)
  2. [SQL](https://learn.microsoft.com/en-us/sql/?view=sql-server-ver17)
  3. [SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/?view=sql-server-ver17)


Ask Learn Ask Learn Focus mode
Table of contents [ Read in English ](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/system-dynamic-management-views?view=sql-server-ver17) Add to Collections Add to plan
* * *
#### Share via
* * *
Copy Markdown Print
* * *
Note
Access to this page requires authorization. You can try [signing in](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/system-dynamic-management-views?view=sql-server-ver17) or changing directories.
Access to this page requires authorization. You can try changing directories.
# System dynamic management views
Feedback
Summarize this article for me
##  In this article
  1. [Query dynamic management views](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/system-dynamic-management-views?view=sql-server-ver17#query-dynamic-management-views)
  2. [Related content](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/system-dynamic-management-views?view=sql-server-ver17#related-content)


**Applies to:** ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure SQL Database](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure SQL Managed Instance](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure Synapse Analytics](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Analytics Platform System (PDW)](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL analytics endpoint in Microsoft Fabric](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Warehouse in Microsoft Fabric](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL database in Microsoft Fabric](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to)
Dynamic management views (DMVs) and dynamic management functions (DMFs) return server state information that can be used to monitor the health of a server instance, diagnose problems, and tune performance.
Dynamic management views and functions return internal, implementation-specific state data. Their schemas and the data they return might change in future releases of SQL Server. Therefore, dynamic management views and functions in future releases might not be compatible with the dynamic management views and functions in this release. For example, in future releases of SQL Server, Microsoft might augment the definition of any dynamic management view by adding columns to the end of the column list. We recommend against using the syntax `SELECT * FROM dynamic_management_view_name` in production code because the number of columns returned might change and break your application.
There are two types of dynamic management views and functions:
  * Server-scoped dynamic management views and functions. These require VIEW SERVER STATE permission on the server. For SQL Server 2022 and later, VIEW SERVER PERFORMANCE STATE is required, or VIEW SERVER SECURITY STATE is required for a few DMVs that are security related.
  * Database-scoped dynamic management views and functions. These require VIEW DATABASE STATE permission on the database. For SQL Server 2022 and later, VIEW DATABASE PERFORMANCE STATE is required, or VIEW DATABASE SECURITY STATE is required for a few DMVs that are security related.


[](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/system-dynamic-management-views?view=sql-server-ver17#query-dynamic-management-views)
## Query dynamic management views
Dynamic management views can be referenced in Transact-SQL statements by using two-part, three-part, or four-part names. Dynamic management functions on the other hand can be referenced in Transact-SQL statements by using either two-part or three-part names. Dynamic management views and functions can't be referenced in Transact-SQL statements by using one-part names.
All dynamic management views and functions exist in the sys schema and follow this naming convention dm_*. When you use a dynamic management view or function, you must prefix the name of the view or function by using the sys schema. For example, to query the dm_os_wait_stats dynamic management view, run the following query:
SQL
Copy
```
SELECT wait_type,
       wait_time_ms
FROM sys.dm_os_wait_stats;

```

[](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/system-dynamic-management-views?view=sql-server-ver17#required-permissions)
### Required permissions
To query a dynamic management view or function requires `SELECT` permission on object and `VIEW SERVER STATE` or `VIEW DATABASE STATE` permission. This lets you selectively restrict access of a user or login to dynamic management views and functions. To do this, first create the user in `master` and then deny the user `SELECT` permission on the dynamic management views or functions that you don't want them to access. After this, the user can't select from these dynamic management views or functions, regardless of database context of the user.
Because `DENY` takes precedence, if a user has been granted VIEW SERVER STATE permissions but denied `VIEW DATABASE STATE` permission, the user can see server-level information, but not database-level information.
[](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/system-dynamic-management-views?view=sql-server-ver17#related-content)
## Related content
  * [GRANT Server Permissions (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/statements/grant-server-permissions-transact-sql?view=sql-server-ver17)
  * [GRANT Database Permissions (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/statements/grant-database-permissions-transact-sql?view=sql-server-ver17)
  * [Transact-SQL reference (Database Engine)](https://learn.microsoft.com/en-us/sql/t-sql/language-reference?view=sql-server-ver17)


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
Mar 8, 4 PM - Mar 8, 4 PM
Experiment with what's next in AI-driven apps and agent design
* * *
  * Last updated on 02/10/2026


Ask Learn is an AI assistant that can answer questions, clarify concepts, and define terms using trusted Microsoft documentation.
Please sign in to use Ask Learn.
[ Sign in ](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/system-dynamic-management-views?view=sql-server-ver17)
