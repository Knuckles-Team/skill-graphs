# Tables
Feedback
Summarize this article for me
##  In this article
  1. [Types of tables](https://learn.microsoft.com/en-us/sql/relational-databases/tables/tables?view=sql-server-ver17#types-of-tables)
  2. [Common table tasks](https://learn.microsoft.com/en-us/sql/relational-databases/tables/tables?view=sql-server-ver17#common-table-tasks)
  3. [Related content](https://learn.microsoft.com/en-us/sql/relational-databases/tables/tables?view=sql-server-ver17#related-content)


**Applies to:** ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) SQL Server 2016 (13.x) and later versions ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure SQL Database](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure SQL Managed Instance](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure Synapse Analytics](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Analytics Platform System (PDW)](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL analytics endpoint in Microsoft Fabric](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Warehouse in Microsoft Fabric](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL database in Microsoft Fabric](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to)
Tables are database objects that contain all the data in a database. In tables, data is logically organized in a row-and-column format similar to a spreadsheet. Each row represents a unique record, and each column represents a field in the record. For example, a table that contains employee data for a company might contain a row for each employee and columns representing employee information such as employee number, name, address, job title, and home telephone number.
  * The number of tables in a database is limited only by the number of objects allowed in a database (2,147,483,647). A standard user-defined table can have up to 1,024 columns. The number of rows in the table is limited only by the storage capacity of the server.
  * You can assign properties to the table and to each column in the table to control the data that is allowed and other properties. For example, you can create constraints on a column to disallow null values or provide a default value if a value is not specified, or you can assign a key constraint on the table that enforces uniqueness or defines a relationship between tables.
  * The data in the table can be compressed either by row or by page. Data compression can allow more rows to be stored on a page. For more information, see [Data compression](https://learn.microsoft.com/en-us/sql/relational-databases/data-compression/data-compression?view=sql-server-ver17).


[](https://learn.microsoft.com/en-us/sql/relational-databases/tables/tables?view=sql-server-ver17#types-of-tables)
## Types of tables
Besides the standard role of basic user-defined tables, SQL Server provides the following types of tables that serve special purposes in a database.
[](https://learn.microsoft.com/en-us/sql/relational-databases/tables/tables?view=sql-server-ver17#partitioned-tables)
### Partitioned tables
Partitioned tables are tables whose data is horizontally divided into units which might be spread across more than one filegroup in a database. Partitioning makes large tables or indexes more manageable by letting you access or manage subsets of data quickly and efficiently, while maintaining the integrity of the overall collection. By default, SQL Server supports up to 15,000 partitions. For more information, see [Partitioned tables and indexes](https://learn.microsoft.com/en-us/sql/relational-databases/partitions/partitioned-tables-and-indexes?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/relational-databases/tables/tables?view=sql-server-ver17#temporary-tables)
### Temporary tables
Temporary tables are stored in `tempdb`. There are two types of temporary tables: **local** and **global**. They differ from each other in their names, their visibility, and their availability.
  * Local temporary tables, also known as session-scoped temporary tables, have a single number sign (`#`) as the first character of their names; they are visible only to the current connection for the user, and they are deleted when the user disconnects from the instance of SQL Server.
  * Global temporary tables have two number signs (`##`) as the first characters of their names; they are visible to any user after they are created, and they are deleted when all users referencing the table disconnect from the instance of SQL Server.


In Fabric Data Warehouse, only session-scoped temp tables are supported, and are not affected by [Time travel hints](https://learn.microsoft.com/en-us/fabric/data-warehouse/time-travel).
[](https://learn.microsoft.com/en-us/sql/relational-databases/tables/tables?view=sql-server-ver17#reduced-recompilations-for-workloads-using-temporary-tables-across-multiple-scopes)
#### Reduced recompilations for workloads using temporary tables across multiple scopes
SQL Server 2019 (15.x) under all database compatibility levels reduces recompilations for workloads using temporary tables across multiple scopes. This feature is also enabled in Azure SQL Database under database compatibility level 150 for all deployment models. Prior to this feature, when referencing a temporary table with a data manipulation language (DML) statement (`SELECT`, `INSERT`, `UPDATE`, `DELETE`), if the temporary table was created by an outer scope batch, this would result in a recompile of the DML statement each time it is executed. With this improvement, SQL Server performs additional lightweight checks to avoid unnecessary recompilations:
  * Check if the outer-scope module used for creating the temporary table at compile time is the same one used for consecutive executions.
  * Keep track of any data definition language (DDL) changes made at initial compilation and compare them with DDL operations for consecutive executions.


The end result is a reduction in extraneous recompilations and CPU-overhead.
[](https://learn.microsoft.com/en-us/sql/relational-databases/tables/tables?view=sql-server-ver17#system-tables)
### System tables
SQL Server stores the data that defines the configuration of the server and all its tables in a special set of tables known as system tables. Users cannot directly query or update the system tables. The information in the system tables is made available through the system views. For a list, see [System Tables (Transact-SQL)](https://learn.microsoft.com/en-us/sql/relational-databases/system-tables/system-tables-transact-sql?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/relational-databases/tables/tables?view=sql-server-ver17#wide-tables)
### Wide tables
Wide tables use [sparse columns](https://learn.microsoft.com/en-us/sql/relational-databases/tables/use-sparse-columns?view=sql-server-ver17) to increase the total of columns that a table can have to 30,000. Sparse columns are ordinary columns that have an optimized storage for null values. Sparse columns reduce the space requirements for null values at the cost of more overhead to retrieve nonnull values. A wide table has defined a [column set](https://learn.microsoft.com/en-us/sql/relational-databases/tables/use-column-sets?view=sql-server-ver17), which is an untyped XML representation that combines all the sparse columns of a table into a structured output. The number of indexes and statistics is also increased to 1,000 and 30,000, respectively. The maximum size of a wide table row is 8,019 bytes. Therefore, most of the data in any particular row should be `NULL`. The maximum number of nonsparse columns plus computed columns in a wide table remains 1,024.
Wide tables have the following performance implications.
  * Wide tables can increase the cost to maintain indexes on the table. We recommend that the number of indexes on a wide table be limited to the indexes that are required by the business logic. As the number of indexes increases, so does the DML compile-time and memory requirement. Nonclustered indexes should be filtered indexes that are applied to data subsets. For more information, see [Create filtered indexes](https://learn.microsoft.com/en-us/sql/relational-databases/indexes/create-filtered-indexes?view=sql-server-ver17).
  * Applications can dynamically add and remove columns from wide tables. When columns are added or removed, compiled query plans are also invalidated. We recommend that you design an application to match the projected workload so that schema changes are minimized.
  * When data is added and removed from a wide table, performance can be affected. Applications must be designed for the projected workload so that changes to the table data are minimized.
  * Limit the execution of DML statements on a wide table that update multiple rows of a clustering key. These statements can require significant memory resources to compile and execute.
  * Switch partition operations on wide tables can be slow and might require large amounts of memory to process. The performance and memory requirements are proportional to the total number of columns in both the source and target partitions.
  * Update cursors that update specific columns in a wide table should list the columns explicitly in the FOR UPDATE clause. This will help optimize performance when you use cursors.


[](https://learn.microsoft.com/en-us/sql/relational-databases/tables/tables?view=sql-server-ver17#common-table-tasks)
## Common table tasks
The following table provides links to common tasks associated with creating or modifying a table.
Expand table
Table Tasks | Topic
---|---
Describes how to create a table. | [Create tables (Database Engine)](https://learn.microsoft.com/en-us/sql/relational-databases/tables/create-tables-database-engine?view=sql-server-ver17)
Describes how to delete a table. | [Delete Tables (Database Engine)](https://learn.microsoft.com/en-us/sql/relational-databases/tables/delete-tables-database-engine?view=sql-server-ver17)
Describes how to create a new table that contains some or all of the columns in an existing table. | [Duplicate tables](https://learn.microsoft.com/en-us/sql/relational-databases/tables/duplicate-tables?view=sql-server-ver17)
Describes how to rename a table. | [Rename tables (Database Engine)](https://learn.microsoft.com/en-us/sql/relational-databases/tables/rename-tables-database-engine?view=sql-server-ver17)
Describes how to view the properties of the table. | [View the Table Definition](https://learn.microsoft.com/en-us/sql/relational-databases/tables/view-the-table-definition?view=sql-server-ver17)
Describes how to determine whether other objects such as a view or stored procedure depend on a table. | [View the dependencies of a table](https://learn.microsoft.com/en-us/sql/relational-databases/tables/view-the-dependencies-of-a-table?view=sql-server-ver17)
The following table provides links to common tasks associated with creating or modifying columns in a table.
Expand table
Column Tasks | Topic
---|---
Describes how to add columns to an existing table. | [Add Columns to a Table (Database Engine)](https://learn.microsoft.com/en-us/sql/relational-databases/tables/add-columns-to-a-table-database-engine?view=sql-server-ver17)
Describes how to delete columns from a table. | [Delete columns from a table](https://learn.microsoft.com/en-us/sql/relational-databases/tables/delete-columns-from-a-table?view=sql-server-ver17)
Describes how to change the name of a column. | [Rename columns (Database Engine)](https://learn.microsoft.com/en-us/sql/relational-databases/tables/rename-columns-database-engine?view=sql-server-ver17)
Describes how to copy columns from one table to another, copying either just the column definition, or the definition and data. | [Copy Columns from One Table to Another (Database Engine)](https://learn.microsoft.com/en-us/sql/relational-databases/tables/copy-columns-from-one-table-to-another-database-engine?view=sql-server-ver17)
Describes how to modify a column definition, by changing the data type or other property. | [Modify columns](https://learn.microsoft.com/en-us/sql/relational-databases/tables/modify-columns-database-engine?view=sql-server-ver17)
Describes how to change the order in which the columns appear. | [Change Column Order in a Table](https://learn.microsoft.com/en-us/sql/relational-databases/tables/change-column-order-in-a-table?view=sql-server-ver17)
Describes how to create a computed column in a table. | [Specify computed columns in a table](https://learn.microsoft.com/en-us/sql/relational-databases/tables/specify-computed-columns-in-a-table?view=sql-server-ver17)
Describes how to specify a default value for a column. This value is used if another value is not supplied. | [Specify default values for columns](https://learn.microsoft.com/en-us/sql/relational-databases/tables/specify-default-values-for-columns?view=sql-server-ver17)
[](https://learn.microsoft.com/en-us/sql/relational-databases/tables/tables?view=sql-server-ver17#related-content)
## Related content
  * [Primary and foreign key constraints](https://learn.microsoft.com/en-us/sql/relational-databases/tables/primary-and-foreign-key-constraints?view=sql-server-ver17)
  * [Unique constraints and check constraints](https://learn.microsoft.com/en-us/sql/relational-databases/tables/unique-constraints-and-check-constraints?view=sql-server-ver17)


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
  * [ Create tables (Database Engine) - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/tables/create-tables-database-engine?source=recommendations)
Create a new table, name it, and add it to an existing database using the Database Engine.
  * [ Transact-SQL Reference (Database Engine) - SQL Server ](https://learn.microsoft.com/en-us/sql/t-sql/language-reference?source=recommendations)
This article gives the basics about how to find and use Transact-SQL (T-SQL) reference articles.
  * [ Hierarchical Data (SQL Server) - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/hierarchical-data-sql-server?source=recommendations)
The built-in hierarchyid data type makes it easier to store and query hierarchical data. It's optimized for representing trees, which are the most common type of hierarchical data.
  * [ Primary and foreign key constraints - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/tables/primary-and-foreign-key-constraints?source=recommendations)
Learn about primary and foreign key constraints, important objects used to enforce data integrity in database tables.
  * [ Transact-SQL statements - SQL Server ](https://learn.microsoft.com/en-us/sql/t-sql/statements/statements?source=recommendations)
Transact-SQL statements
  * [ Joins (SQL Server) - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/performance/joins?source=recommendations)
Learn about the types of join operations that SQL Server employs. SQL Server supports vertical table partitioning, or columnar storage, using join operations.
  * [ Database identifiers - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/databases/database-identifiers?source=recommendations)
Get acquainted with database identifiers. Learn about their collation, various classes, delimiting requirements, and naming rules.
  * [ CREATE TABLE (Transact-SQL) - SQL Server ](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-table-transact-sql?source=recommendations)
CREATE TABLE creates a new table in the database.


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


##  In this article
  1. [Types of tables](https://learn.microsoft.com/en-us/sql/relational-databases/tables/tables?view=sql-server-ver17#types-of-tables)
  2. [Common table tasks](https://learn.microsoft.com/en-us/sql/relational-databases/tables/tables?view=sql-server-ver17#common-table-tasks)
  3. [Related content](https://learn.microsoft.com/en-us/sql/relational-databases/tables/tables?view=sql-server-ver17#related-content)


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
[ Sign in ](https://learn.microsoft.com/en-us/sql/relational-databases/tables/tables?view=sql-server-ver17)
[English (United States)](https://learn.microsoft.com/en-us/locale?target=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fsql%2Frelational-databases%2Ftables%2Ftables%3Fview%3Dsql-server-ver17)
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
