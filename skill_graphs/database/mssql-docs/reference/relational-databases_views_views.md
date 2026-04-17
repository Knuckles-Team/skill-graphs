Version SQL Server 2025
  * Analytics Platform System (PDW)
    * [2016-AU7](https://learn.microsoft.com/en-us/sql/relational-databases/views/views?view=aps-pdw-2016-au7)
    * [2016-AU6](https://learn.microsoft.com/en-us/sql/relational-databases/views/views?view=aps-pdw-2016)
  * [Azure SQL Database](https://learn.microsoft.com/en-us/sql/relational-databases/views/views?view=azuresqldb-current)
  * [Azure SQL Managed Instance](https://learn.microsoft.com/en-us/sql/relational-databases/views/views?view=azuresqldb-mi-current)
  * [Azure Synapse Analytics](https://learn.microsoft.com/en-us/sql/relational-databases/views/views?view=azure-sqldw-latest)
  * [Fabric Data Warehouse](https://learn.microsoft.com/en-us/sql/relational-databases/views/views?view=fabric)
  * [Fabric SQL database](https://learn.microsoft.com/en-us/sql/relational-databases/views/views?view=fabric-sqldb)
  * SQL Server
    * [2025](https://learn.microsoft.com/en-us/sql/relational-databases/views/views?view=sql-server-ver17)
    * [2022](https://learn.microsoft.com/en-us/sql/relational-databases/views/views?view=sql-server-ver16)
    * [2019](https://learn.microsoft.com/en-us/sql/relational-databases/views/views?view=sql-server-ver15)
    * [2017](https://learn.microsoft.com/en-us/sql/relational-databases/views/views?view=sql-server-2017)
    * [2016](https://learn.microsoft.com/en-us/sql/relational-databases/views/views?view=sql-server-2016)
  * SQL Server on Linux
    * [2025](https://learn.microsoft.com/en-us/sql/relational-databases/views/views?view=sql-server-linux-ver17)
    * [2022](https://learn.microsoft.com/en-us/sql/relational-databases/views/views?view=sql-server-linux-ver16)
    * [2019](https://learn.microsoft.com/en-us/sql/relational-databases/views/views?view=sql-server-linux-ver15)
    * [2017](https://learn.microsoft.com/en-us/sql/relational-databases/views/views?view=sql-server-linux-2017)


Search
Suggestions will filter as you type
  * [SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/?view=sql-server-ver17)
  * [Docs navigation tips](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17)
  * [Previous versions 2005-2014](https://learn.microsoft.com/en-us/sql/sql-server/previous-versions-sql-server?view=sql-server-ver17)
  *     * [What is SQL Server?](https://learn.microsoft.com/en-us/sql/sql-server/what-is-sql-server?view=sql-server-ver17)
    * [Connect to the Database Engine](https://learn.microsoft.com/en-us/sql/sql-server/connect-to-database-engine?view=sql-server-ver17)
  *     * [Hierarchical Data](https://learn.microsoft.com/en-us/sql/relational-databases/hierarchical-data-sql-server?view=sql-server-ver17)
    *       * [Views](https://learn.microsoft.com/en-us/sql/relational-databases/views/views?view=sql-server-ver17)
      * [Create](https://learn.microsoft.com/en-us/sql/relational-databases/views/create-views?view=sql-server-ver17)
      * [Create Indexed Views](https://learn.microsoft.com/en-us/sql/relational-databases/views/create-indexed-views?view=sql-server-ver17)
      * [Modify](https://learn.microsoft.com/en-us/sql/relational-databases/views/modify-views?view=sql-server-ver17)
      * [Modify Data Through a View](https://learn.microsoft.com/en-us/sql/relational-databases/views/modify-data-through-a-view?view=sql-server-ver17)
      * [Get Information](https://learn.microsoft.com/en-us/sql/relational-databases/views/get-information-about-a-view?view=sql-server-ver17)
      * [Rename](https://learn.microsoft.com/en-us/sql/relational-databases/views/rename-views?view=sql-server-ver17)
      * [Delete](https://learn.microsoft.com/en-us/sql/relational-databases/views/delete-views?view=sql-server-ver17)
      * [Use DMVs to determine performance of Views](https://learn.microsoft.com/en-us/sql/relational-databases/performance/use-dmvs-determine-usage-performance-views?view=sql-server-ver17)


Download PDF
Table of contents  Exit editor mode
  1. [ Learn ](https://learn.microsoft.com/en-us/?view=sql-server-ver17)
  2. [ SQL ](https://learn.microsoft.com/en-us/sql/?view=sql-server-ver17)
  3. [ SQL Server ](https://learn.microsoft.com/en-us/sql/sql-server/?view=sql-server-ver17)


  1. [Learn](https://learn.microsoft.com/en-us/?view=sql-server-ver17)
  2. [SQL](https://learn.microsoft.com/en-us/sql/?view=sql-server-ver17)
  3. [SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/?view=sql-server-ver17)


Ask Learn Ask Learn Focus mode
Table of contents [ Read in English ](https://learn.microsoft.com/en-us/sql/relational-databases/views/views?view=sql-server-ver17) Add to Collections Add to plan
* * *
#### Share via
* * *
Copy Markdown Print
* * *
Note
Access to this page requires authorization. You can try [signing in](https://learn.microsoft.com/en-us/sql/relational-databases/views/views?view=sql-server-ver17) or changing directories.
Access to this page requires authorization. You can try changing directories.
# Views
Feedback
Summarize this article for me
##  In this article
  1. [Types of views](https://learn.microsoft.com/en-us/sql/relational-databases/views/views?view=sql-server-ver17#types-of-views)
  2. [Common view tasks](https://learn.microsoft.com/en-us/sql/relational-databases/views/views?view=sql-server-ver17#common-view-tasks)
  3. [Related content](https://learn.microsoft.com/en-us/sql/relational-databases/views/views?view=sql-server-ver17#related-content)


**Applies to:** ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure SQL Database](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure SQL Managed Instance](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure Synapse Analytics](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Analytics Platform System (PDW)](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL analytics endpoint in Microsoft Fabric](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Warehouse in Microsoft Fabric](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL database in Microsoft Fabric](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to)
A view is a virtual table whose contents are defined by a query. Like a table, a view consists of a set of named columns and rows of data. Unless indexed, a view does not exist as a stored set of data values in a database. The rows and columns of data come from tables referenced in the query defining the view and are produced dynamically when the view is referenced.
A view acts as a filter on the underlying tables referenced in the view. The query that defines the view can be from one or more tables or from other views in the current or other databases. Distributed queries can also be used to define views that use data from multiple heterogeneous sources. This is useful, for example, if you want to combine similarly structured data from different servers, each of which stores data for a different region of your organization.
Views are generally used to focus, simplify, and customize the perception each user has of the database. Views can be used as security mechanisms by letting users access data through the view, without granting users permissions to directly access the underlying tables of the query. Views can be used to provide a backward compatible interface to emulate a table that used to exist but whose schema has changed. Views can also be used when you copy data to and from SQL Server to improve performance and to partition data.
[](https://learn.microsoft.com/en-us/sql/relational-databases/views/views?view=sql-server-ver17#types-of-views)
## Types of views
Besides the standard role of basic user-defined views, SQL Server provides the following types of views that serve special purposes in a database.
[](https://learn.microsoft.com/en-us/sql/relational-databases/views/views?view=sql-server-ver17#indexed-views)
### Indexed views
An indexed view is a materialized view. This means the view definition has been computed and the resulting data stored just like a table. You index a view by creating a unique clustered index on it. Indexed views can dramatically improve the performance of some types of queries. Indexed views work best for queries that aggregate many rows. They are not well-suited for underlying data sets that are frequently updated.
[](https://learn.microsoft.com/en-us/sql/relational-databases/views/views?view=sql-server-ver17#partitioned-views)
### Partitioned views
A partitioned view joins horizontally partitioned data from a set of member tables across one or more servers. A partitioned view makes the data appear as if from one table. A view that joins member tables on the same instance of SQL Server is a local partitioned view.
[](https://learn.microsoft.com/en-us/sql/relational-databases/views/views?view=sql-server-ver17#system-views)
### System views
System views expose catalog metadata. You can use system views to return information about the instance of SQL Server or the objects defined in the instance. For example, you can query the `sys.databases` catalog view to return information about the user-defined databases available in the instance. For more information, see [System Views (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/language-reference?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/relational-databases/views/views?view=sql-server-ver17#common-view-tasks)
## Common view tasks
The following table provides links to common tasks associated with creating or modifying a view.
Expand table
View Tasks | Article
---|---
Describes how to create a view. | [Create Views](https://learn.microsoft.com/en-us/sql/relational-databases/views/create-views?view=sql-server-ver17)
Describes how to create an indexed view. | [Create Indexed Views](https://learn.microsoft.com/en-us/sql/relational-databases/views/create-indexed-views?view=sql-server-ver17)
Describes how to modify the view definition. | [Modify Views](https://learn.microsoft.com/en-us/sql/relational-databases/views/modify-views?view=sql-server-ver17)
Describes how to modify data through a view. | [Modify Data Through a View](https://learn.microsoft.com/en-us/sql/relational-databases/views/modify-data-through-a-view?view=sql-server-ver17)
Describes how to delete a view. | [Delete Views](https://learn.microsoft.com/en-us/sql/relational-databases/views/delete-views?view=sql-server-ver17)
Describes how to return information about a view such as the view definition. | [Get Information About a View](https://learn.microsoft.com/en-us/sql/relational-databases/views/get-information-about-a-view?view=sql-server-ver17)
Describes how to rename a view. | [Rename Views](https://learn.microsoft.com/en-us/sql/relational-databases/views/rename-views?view=sql-server-ver17)
[](https://learn.microsoft.com/en-us/sql/relational-databases/views/views?view=sql-server-ver17#related-content)
## Related content
  * [Create Views over XML Columns](https://learn.microsoft.com/en-us/sql/relational-databases/xml/create-views-over-xml-columns?view=sql-server-ver17)
  * [CREATE VIEW (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-view-transact-sql?view=sql-server-ver17)
  * [GRANT Object Permissions (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/statements/grant-object-permissions-transact-sql?view=sql-server-ver17)
  * [Row-level security](https://learn.microsoft.com/en-us/sql/relational-databases/security/row-level-security?view=sql-server-ver17)


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
  * [ Create views - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/views/create-views?source=recommendations)
Create views in the Database Engine with SQL Server Management Studio or Transact-SQL.
  * [ CREATE VIEW (Transact-SQL) - SQL Server ](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-view-transact-sql?source=recommendations)
CREATE VIEW creates a virtual table whose contents are defined by a query.
  * [ Modify Data Through a View - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/views/modify-data-through-a-view?source=recommendations)
Learn how to modify data through a view.
  * [ Create Indexed Views - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/views/create-indexed-views?source=recommendations)
Creating a unique clustered index on a view improves query performance, because the view is stored in the same way as a clustered index is stored.
  * [ Get information about a view - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/views/get-information-about-a-view?source=recommendations)
Learn how to view information about a view from SSMS or T-SQL.
  * [ Delete views - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/views/delete-views?source=recommendations)
Delete (drop) views in the Database Engine using SQL Server Management Studio or Transact-SQL.
  * [ Modify views - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/views/modify-views?source=recommendations)
After you define a view, you can modify its definition in the Database Engine without dropping and re-creating the view.
  * [ DROP VIEW (Transact-SQL) - SQL Server ](https://learn.microsoft.com/en-us/sql/t-sql/statements/drop-view-transact-sql?source=recommendations)
DROP VIEW (Transact-SQL)


Show 5 more
Module
[ Create tables, views, and temporary objects - Training ](https://learn.microsoft.com/en-us/training/modules/create-tables-views-temporary-objects/?source=recommendations)
This content is a part of Create tables, views, and temporary objects.
Certification
[ Microsoft Certified: Azure Database Administrator Associate - Certifications ](https://learn.microsoft.com/en-us/credentials/certifications/azure-database-administrator-associate/?source=recommendations)
Administer an SQL Server database infrastructure for cloud, on-premises and hybrid relational databases using the Microsoft PaaS relational database offerings.
Mar 8, 4 PM - Mar 8, 4 PM
Experiment with what's next in AI-driven apps and agent design
* * *
  * Last updated on 11/18/2025


Ask Learn is an AI assistant that can answer questions, clarify concepts, and define terms using trusted Microsoft documentation.
Please sign in to use Ask Learn.
[ Sign in ](https://learn.microsoft.com/en-us/sql/relational-databases/views/views?view=sql-server-ver17)
