##  In this article
  1. [Collation terms](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#collation-terms)
  2. [Unicode support](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#unicode-support)
  3. [Supplementary characters](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#supplementary-characters)
  4. [GB18030 support](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#gb18030-support)
  5. [Complex script support](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#complex-script-support)
  6. [Collations in Azure SQL Database](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#collations-in-azure-sql-database)
  7. [Collations in Azure SQL Managed Instance](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#collations-in-azure-sql-managed-instance)
  8. [Collation in Microsoft Fabric](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#collation-in-microsoft-fabric)
  9. [UTF-8 support](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#utf-8-support)
  10. [Related tasks](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#related-tasks)
  11. [Related content](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#related-content)

Show 7 more
**Applies to:** ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure SQL Database](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure SQL Managed Instance](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure Synapse Analytics](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Analytics Platform System (PDW)](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL analytics endpoint in Microsoft Fabric](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Warehouse in Microsoft Fabric](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL database in Microsoft Fabric](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to)
Collations in the SQL Server Database Engine provide sorting rules, case, and accent sensitivity properties for your data. Collations that are used with character data types, such as **char** and **varchar** , dictate the code page and corresponding characters that can be represented for that data type.
Whether you're installing a new instance of SQL Server, restoring a database backup, or connecting server to client databases, it's important to understand the locale requirements, sorting order, and case and accent sensitivity of the data that you're working with. To list the collations that are available on your instance of SQL Server, see [sys.fn_helpcollations](https://learn.microsoft.com/en-us/sql/relational-databases/system-functions/sys-fn-helpcollations-transact-sql?view=sql-server-ver17).
When you select a collation for your server, database, column, or expression, you're assigning certain characteristics to your data. These characteristics affect the results of many operations in the database. For example, when you construct a query by using `ORDER BY`, the sort order of your result set might depend on the collation applied to the database, or dictated in a `COLLATE` clause at the expression level of the query.
To best use collation support in SQL Server, you should understand the terms that are defined in this article and how they relate to the characteristics of your data.
[](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#collation-terms)
##  In this article
  1. [Collation terms](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#collation-terms)
  2. [Unicode support](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#unicode-support)
  3. [Supplementary characters](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#supplementary-characters)
  4. [GB18030 support](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#gb18030-support)
  5. [Complex script support](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#complex-script-support)
  6. [Collations in Azure SQL Database](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#collations-in-azure-sql-database)
  7. [Collations in Azure SQL Managed Instance](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#collations-in-azure-sql-managed-instance)
  8. [Collation in Microsoft Fabric](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#collation-in-microsoft-fabric)
  9. [UTF-8 support](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#utf-8-support)
  10. [Related tasks](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#related-tasks)
  11. [Related content](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#related-content)

Show 2 more
Was this page helpful?
Yes No No
Need help with this topic?
Want to try using Ask Learn to clarify or guide you through this topic?
Ask Learn Ask Learn
Suggest a fix?
