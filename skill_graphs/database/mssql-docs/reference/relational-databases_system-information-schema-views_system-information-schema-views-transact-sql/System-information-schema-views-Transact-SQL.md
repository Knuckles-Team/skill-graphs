# System information schema views (Transact-SQL)
Feedback
Summarize this article for me
##  In this article
  1. [Permissions](https://learn.microsoft.com/en-us/sql/relational-databases/system-information-schema-views/system-information-schema-views-transact-sql?view=sql-server-ver17#permissions)
  2. [Related content](https://learn.microsoft.com/en-us/sql/relational-databases/system-information-schema-views/system-information-schema-views-transact-sql?view=sql-server-ver17#related-content)


**Applies to:** ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure SQL Database](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure SQL Managed Instance](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL database in Microsoft Fabric](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to)
An information schema view is one of several methods SQL Server provides for obtaining metadata. Information schema views provide an internal, system table-independent view of the SQL Server metadata. Information schema views enable applications to work correctly, although significant changes were made to the underlying system tables. The information schema views included in SQL Server comply with the ISO standard definition for the `INFORMATION_SCHEMA`.
Some changes were made to the information schema views that break backward compatibility. These changes are described in the articles for the specific views.
SQL Server supports a three-part naming convention when you refer to the current server. The ISO standard also supports a three-part naming convention. However, the names used in both naming conventions are different. The information schema views are defined in a special schema named `INFORMATION_SCHEMA`. This schema is contained in each database. Each information schema view contains metadata for all data objects stored in that particular database. The following table shows the relationships between the SQL Server names and the SQL standard names.
Expand table
SQL Server name | Maps to this equivalent SQL standard name
---|---
Database | Catalog
Schema | Schema
Object | Object
User-defined data type | Domain
This name-mapping convention applies to the following SQL Server ISO-compatible views.
  * [CHECK_CONSTRAINTS](https://learn.microsoft.com/en-us/sql/relational-databases/system-information-schema-views/check-constraints-transact-sql?view=sql-server-ver17)
  * [COLUMN_DOMAIN_USAGE](https://learn.microsoft.com/en-us/sql/relational-databases/system-information-schema-views/column-domain-usage-transact-sql?view=sql-server-ver17)
  * [COLUMN_PRIVILEGES](https://learn.microsoft.com/en-us/sql/relational-databases/system-information-schema-views/column-privileges-transact-sql?view=sql-server-ver17)
  * [COLUMNS](https://learn.microsoft.com/en-us/sql/relational-databases/system-information-schema-views/columns-transact-sql?view=sql-server-ver17)
  * [CONSTRAINT_COLUMN_USAGE](https://learn.microsoft.com/en-us/sql/relational-databases/system-information-schema-views/constraint-column-usage-transact-sql?view=sql-server-ver17)
  * [CONSTRAINT_TABLE_USAGE](https://learn.microsoft.com/en-us/sql/relational-databases/system-information-schema-views/constraint-table-usage-transact-sql?view=sql-server-ver17)
  * [DOMAIN_CONSTRAINTS](https://learn.microsoft.com/en-us/sql/relational-databases/system-information-schema-views/domain-constraints-transact-sql?view=sql-server-ver17)
  * [DOMAINS](https://learn.microsoft.com/en-us/sql/relational-databases/system-information-schema-views/domains-transact-sql?view=sql-server-ver17)
  * [KEY_COLUMN_USAGE](https://learn.microsoft.com/en-us/sql/relational-databases/system-information-schema-views/key-column-usage-transact-sql?view=sql-server-ver17)
  * [PARAMETERS](https://learn.microsoft.com/en-us/sql/relational-databases/system-information-schema-views/parameters-transact-sql?view=sql-server-ver17)
  * [REFERENTIAL_CONSTRAINTS](https://learn.microsoft.com/en-us/sql/relational-databases/system-information-schema-views/referential-constraints-transact-sql?view=sql-server-ver17)
  * [ROUTINE_COLUMNS](https://learn.microsoft.com/en-us/sql/relational-databases/system-information-schema-views/routine-columns-transact-sql?view=sql-server-ver17)
  * [ROUTINES](https://learn.microsoft.com/en-us/sql/relational-databases/system-information-schema-views/routines-transact-sql?view=sql-server-ver17)
  * [SCHEMATA](https://learn.microsoft.com/en-us/sql/relational-databases/system-information-schema-views/schemata-transact-sql?view=sql-server-ver17)
  * [TABLE_CONSTRAINTS](https://learn.microsoft.com/en-us/sql/relational-databases/system-information-schema-views/table-constraints-transact-sql?view=sql-server-ver17)
  * [TABLE_PRIVILEGES](https://learn.microsoft.com/en-us/sql/relational-databases/system-information-schema-views/table-privileges-transact-sql?view=sql-server-ver17)
  * [TABLES](https://learn.microsoft.com/en-us/sql/relational-databases/system-information-schema-views/tables-transact-sql?view=sql-server-ver17)
  * [VIEW_COLUMN_USAGE](https://learn.microsoft.com/en-us/sql/relational-databases/system-information-schema-views/view-column-usage-transact-sql?view=sql-server-ver17)
  * [VIEW_TABLE_USAGE](https://learn.microsoft.com/en-us/sql/relational-databases/system-information-schema-views/view-table-usage-transact-sql?view=sql-server-ver17)
  * [VIEWS](https://learn.microsoft.com/en-us/sql/relational-databases/system-information-schema-views/views-transact-sql?view=sql-server-ver17)


Also, some views contain references to different classes of data such as character data or binary data.
When you reference the information schema views, you must use a qualified name that includes the `INFORMATION_SCHEMA` schema name. For example:
SQL
Copy
```
USE AdventureWorks2022;
GO

SELECT TABLE_CATALOG,
       TABLE_SCHEMA,
       TABLE_NAME,
       COLUMN_NAME,
       COLUMN_DEFAULT
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = N'Product';

```

[](https://learn.microsoft.com/en-us/sql/relational-databases/system-information-schema-views/system-information-schema-views-transact-sql?view=sql-server-ver17#permissions)
## Permissions
The visibility of the metadata in information schema views is limited to securables that a user either owns or on which the user is granted some permission. For more information, see [Metadata Visibility Configuration](https://learn.microsoft.com/en-us/sql/relational-databases/security/metadata-visibility-configuration?view=sql-server-ver17).
Information schema views are defined server-wide and therefore can't be denied within the context of a user database. To `REVOKE` or `DENY` access (`SELECT`), the `master` database must be used. By default the public role has `SELECT`-permission to all information schema views but the content is limited with metadata visibility rules.
You can't deny access to information schema views in Azure SQL Database.
[](https://learn.microsoft.com/en-us/sql/relational-databases/system-information-schema-views/system-information-schema-views-transact-sql?view=sql-server-ver17#related-content)
## Related content
  * [Replication Views (Transact-SQL)](https://learn.microsoft.com/en-us/sql/relational-databases/system-views/replication-views-transact-sql?view=sql-server-ver17)
  * [Data types (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/data-types/data-types-transact-sql?view=sql-server-ver17)
  * [System stored procedures (Transact-SQL)](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/system-stored-procedures-transact-sql?view=sql-server-ver17)


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
  * Last updated on 11/18/2025


##  In this article
  1. [Permissions](https://learn.microsoft.com/en-us/sql/relational-databases/system-information-schema-views/system-information-schema-views-transact-sql?view=sql-server-ver17#permissions)
  2. [Related content](https://learn.microsoft.com/en-us/sql/relational-databases/system-information-schema-views/system-information-schema-views-transact-sql?view=sql-server-ver17#related-content)


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
[ Sign in ](https://learn.microsoft.com/en-us/sql/relational-databases/system-information-schema-views/system-information-schema-views-transact-sql?view=sql-server-ver17)
[English (United States)](https://learn.microsoft.com/en-us/locale?target=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fsql%2Frelational-databases%2Fsystem-information-schema-views%2Fsystem-information-schema-views-transact-sql%3Fview%3Dsql-server-ver17)
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
