##  In this article
  1. [Components and concepts](https://learn.microsoft.com/en-us/sql/relational-databases/statistics/statistics?view=sql-server-ver17#components-and-concepts)
  2. [Statistics options](https://learn.microsoft.com/en-us/sql/relational-databases/statistics/statistics?view=sql-server-ver17#statistics-options)
  3. [When to create statistics](https://learn.microsoft.com/en-us/sql/relational-databases/statistics/statistics?view=sql-server-ver17#when-to-create-statistics)
  4. [When to update statistics](https://learn.microsoft.com/en-us/sql/relational-databases/statistics/statistics?view=sql-server-ver17#when-to-update-statistics)
  5. [Queries that use statistics effectively](https://learn.microsoft.com/en-us/sql/relational-databases/statistics/statistics?view=sql-server-ver17#queries-that-use-statistics-effectively)
  6. [Related content](https://learn.microsoft.com/en-us/sql/relational-databases/statistics/statistics?view=sql-server-ver17#related-content)

Show 2 more
**Applies to:** ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure SQL Database](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure SQL Managed Instance](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure Synapse Analytics](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL database in Microsoft Fabric](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to)
The Query Optimizer uses statistics to create query plans that improve query performance. For most queries, the Query Optimizer already generates the necessary statistics for a high-quality query plan; in some cases, you need to create extra statistics or modify the query design for best results. This article discusses statistics concepts and provides guidelines for using query optimization statistics effectively.
[](https://learn.microsoft.com/en-us/sql/relational-databases/statistics/statistics?view=sql-server-ver17#components-and-concepts)
##  In this article
  1. [Components and concepts](https://learn.microsoft.com/en-us/sql/relational-databases/statistics/statistics?view=sql-server-ver17#components-and-concepts)
  2. [Statistics options](https://learn.microsoft.com/en-us/sql/relational-databases/statistics/statistics?view=sql-server-ver17#statistics-options)
  3. [When to create statistics](https://learn.microsoft.com/en-us/sql/relational-databases/statistics/statistics?view=sql-server-ver17#when-to-create-statistics)
  4. [When to update statistics](https://learn.microsoft.com/en-us/sql/relational-databases/statistics/statistics?view=sql-server-ver17#when-to-update-statistics)
  5. [Queries that use statistics effectively](https://learn.microsoft.com/en-us/sql/relational-databases/statistics/statistics?view=sql-server-ver17#queries-that-use-statistics-effectively)
  6. [Related content](https://learn.microsoft.com/en-us/sql/relational-databases/statistics/statistics?view=sql-server-ver17#related-content)


Was this page helpful?
Yes No No
Need help with this topic?
Want to try using Ask Learn to clarify or guide you through this topic?
Ask Learn Ask Learn
Suggest a fix?
