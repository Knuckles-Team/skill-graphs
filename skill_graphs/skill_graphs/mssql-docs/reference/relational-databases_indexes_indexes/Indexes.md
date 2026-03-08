# Indexes
Feedback
Summarize this article for me
##  In this article
  1. [Available index types](https://learn.microsoft.com/en-us/sql/relational-databases/indexes/indexes?view=sql-server-ver17#available-index-types)
  2. [Related content](https://learn.microsoft.com/en-us/sql/relational-databases/indexes/indexes?view=sql-server-ver17#related-content)


**Applies to:** ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure SQL Database](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure SQL Managed Instance](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL database in Microsoft Fabric](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to)
[](https://learn.microsoft.com/en-us/sql/relational-databases/indexes/indexes?view=sql-server-ver17#available-index-types)
## Available index types
The following table lists the types of indexes available in SQL Server and provides links to additional information.
Expand table
Index type | Description | Additional information
---|---|---
Hash | With a hash index, data is accessed through an in-memory hash table. Hash indexes consume a fixed amount of memory, which is a function of the bucket count. |  [Indexes on Memory-Optimized Tables](https://learn.microsoft.com/en-us/sql/relational-databases/in-memory-oltp/indexes-for-memory-optimized-tables?view=sql-server-ver17)

[Hash Index Design Guidelines](https://learn.microsoft.com/en-us/sql/relational-databases/sql-server-index-design-guide?view=sql-server-ver17#hash_index)
memory-optimized Nonclustered | For memory-optimized nonclustered indexes, memory consumption is a function of the row count and the size of the index key columns |  [Indexes on Memory-Optimized Tables](https://learn.microsoft.com/en-us/sql/relational-databases/in-memory-oltp/indexes-for-memory-optimized-tables?view=sql-server-ver17)

[Memory-Optimized Nonclustered Index Design Guidelines](https://learn.microsoft.com/en-us/sql/relational-databases/sql-server-index-design-guide?view=sql-server-ver17#inmem_nonclustered_index)
Clustered | A clustered index sorts and stores the data rows of the table or view in order based on the clustered index key. The clustered index is implemented as a B-tree index structure that supports fast retrieval of the rows, based on their clustered index key values. |  [Clustered and nonclustered indexes](https://learn.microsoft.com/en-us/sql/relational-databases/indexes/clustered-and-nonclustered-indexes-described?view=sql-server-ver17)

[Create a clustered index](https://learn.microsoft.com/en-us/sql/relational-databases/indexes/create-clustered-indexes?view=sql-server-ver17)

[Clustered Index Design Guidelines](https://learn.microsoft.com/en-us/sql/relational-databases/sql-server-index-design-guide?view=sql-server-ver17#Clustered)
Nonclustered | A nonclustered index can be defined on a table or view with a clustered index or on a heap. Each index row in the nonclustered index contains the nonclustered key value and a row locator. This locator points to the data row in the clustered index or heap having the key value. The rows in the index are stored in the order of the index key values, but the data rows aren't guaranteed to be in any particular order unless a clustered index is created on the table. |  [Clustered and nonclustered indexes](https://learn.microsoft.com/en-us/sql/relational-databases/indexes/clustered-and-nonclustered-indexes-described?view=sql-server-ver17)

[Create nonclustered indexes](https://learn.microsoft.com/en-us/sql/relational-databases/indexes/create-nonclustered-indexes?view=sql-server-ver17)

[Nonclustered Index Design Guidelines](https://learn.microsoft.com/en-us/sql/relational-databases/sql-server-index-design-guide?view=sql-server-ver17#Nonclustered)
Unique | A unique index ensures that the index key contains no duplicate values and therefore every row in the table or view is in some way unique.

Uniqueness can be a property of both clustered and nonclustered indexes. |  [Create a unique index](https://learn.microsoft.com/en-us/sql/relational-databases/indexes/create-unique-indexes?view=sql-server-ver17)

[Unique Index Design Guidelines](https://learn.microsoft.com/en-us/sql/relational-databases/sql-server-index-design-guide?view=sql-server-ver17#Unique)
Columnstore | An in-memory columnstore index stores and manages data by using column-based data storage and column-based query processing.

Columnstore indexes work well for data warehousing workloads that primarily perform bulk loads and read-only queries. Use the columnstore index to achieve up to **10x query performance** gains over traditional row-oriented storage, and up to **7x data compression** over the uncompressed data size. |  [Columnstore indexes: overview](https://learn.microsoft.com/en-us/sql/relational-databases/indexes/columnstore-indexes-overview?view=sql-server-ver17)

[Columnstore Index Design Guidelines](https://learn.microsoft.com/en-us/sql/relational-databases/sql-server-index-design-guide?view=sql-server-ver17#columnstore_index)
Index with included columns | A nonclustered index that is extended to include nonkey columns in addition to the key columns. | [Create indexes with included columns](https://learn.microsoft.com/en-us/sql/relational-databases/indexes/create-indexes-with-included-columns?view=sql-server-ver17)
Index on computed columns | An index on a column that is derived from the value of one or more other columns, or certain deterministic inputs. | [Indexes on computed columns](https://learn.microsoft.com/en-us/sql/relational-databases/indexes/indexes-on-computed-columns?view=sql-server-ver17)
Filtered | An optimized nonclustered index, especially suited to cover queries that select from a well-defined subset of data. It uses a filter predicate to index a portion of rows in the table. A well-designed filtered index can improve query performance, reduce index maintenance costs, and reduce index storage costs compared with full-table indexes. |  [Create filtered indexes](https://learn.microsoft.com/en-us/sql/relational-databases/indexes/create-filtered-indexes?view=sql-server-ver17)

[Filtered Index Design Guidelines](https://learn.microsoft.com/en-us/sql/relational-databases/sql-server-index-design-guide?view=sql-server-ver17#Filtered)
Spatial | A spatial index provides the ability to perform certain operations more efficiently on spatial objects (_spatial data_) in a column of the **geometry** data type. The spatial index reduces the number of objects on which relatively costly spatial operations need to be applied. | [Spatial Indexes Overview](https://learn.microsoft.com/en-us/sql/relational-databases/spatial/spatial-indexes-overview?view=sql-server-ver17)
XML | A shredded, and persisted, representation of the XML binary large objects (BLOBs) in the **xml** data type column. | [XML indexes (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/xml/xml-indexes-sql-server?view=sql-server-ver17)
Full-text | A special type of token-based functional index that is built and maintained by the Microsoft Full-Text Engine for SQL Server. It provides efficient support for sophisticated word searches in character string data. | [Populate Full-Text Indexes](https://learn.microsoft.com/en-us/sql/relational-databases/search/populate-full-text-indexes?view=sql-server-ver17)
Documentation uses the term B-tree generally in reference to indexes. In rowstore indexes, the Database Engine implements a B+ tree. This does not apply to columnstore indexes or indexes on memory-optimized tables. For more information, see the [SQL Server and Azure SQL index architecture and design guide](https://learn.microsoft.com/en-us/sql/relational-databases/sql-server-index-design-guide?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/relational-databases/indexes/indexes?view=sql-server-ver17#related-content)
## Related content
  * [SQL Server and Azure SQL index architecture and design guide](https://learn.microsoft.com/en-us/sql/relational-databases/sql-server-index-design-guide?view=sql-server-ver17)
  * [SORT_IN_TEMPDB Option For Indexes](https://learn.microsoft.com/en-us/sql/relational-databases/indexes/sort-in-tempdb-option-for-indexes?view=sql-server-ver17)
  * [Disable indexes and constraints](https://learn.microsoft.com/en-us/sql/relational-databases/indexes/disable-indexes-and-constraints?view=sql-server-ver17)
  * [Enable indexes and constraints](https://learn.microsoft.com/en-us/sql/relational-databases/indexes/enable-indexes-and-constraints?view=sql-server-ver17)
  * [Rename Indexes](https://learn.microsoft.com/en-us/sql/relational-databases/indexes/rename-indexes?view=sql-server-ver17)
  * [Set Index Options](https://learn.microsoft.com/en-us/sql/relational-databases/indexes/set-index-options?view=sql-server-ver17)
  * [Disk Space Requirements for Index DDL Operations](https://learn.microsoft.com/en-us/sql/relational-databases/indexes/disk-space-requirements-for-index-ddl-operations?view=sql-server-ver17)
  * [Optimize index maintenance to improve query performance and reduce resource consumption](https://learn.microsoft.com/en-us/sql/relational-databases/indexes/reorganize-and-rebuild-indexes?view=sql-server-ver17)
  * [Specify Fill Factor for an Index](https://learn.microsoft.com/en-us/sql/relational-databases/indexes/specify-fill-factor-for-an-index?view=sql-server-ver17)
  * [Pages and extents architecture guide](https://learn.microsoft.com/en-us/sql/relational-databases/pages-and-extents-architecture-guide?view=sql-server-ver17)
  * [Clustered and nonclustered indexes](https://learn.microsoft.com/en-us/sql/relational-databases/indexes/clustered-and-nonclustered-indexes-described?view=sql-server-ver17)


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
  * [ Clustered and Nonclustered Indexes - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/indexes/clustered-and-nonclustered-indexes-described?source=recommendations)
Describes clustered and nonclustered indexes.
  * [ Index Architecture and Design Guide - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/sql-server-index-design-guide?source=recommendations)
Learn about designing efficient indexes in SQL Server and Azure SQL to achieve good database and application performance. Read about index architecture and best practices.
  * [ Create a Clustered Index - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/indexes/create-clustered-indexes?source=recommendations)
Create a clustered index in SQL Server and Azure SQL.
  * [ Create Indexes with Included Columns - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/indexes/create-indexes-with-included-columns?source=recommendations)
Create indexes with included columns
  * [ Create Nonclustered Indexes - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/indexes/create-nonclustered-indexes?source=recommendations)
This article shows you how to create nonclustered indexes by using SQL Server Management Studio or Transact-SQL.
  * [ Create Filtered Indexes - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/indexes/create-filtered-indexes?source=recommendations)
A filtered index is an optimized disk-based rowstore nonclustered index especially suited to cover queries that select from a well-defined subset of data.
  * [ Heaps (Tables without clustered indexes) - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/indexes/heaps-tables-without-clustered-indexes?source=recommendations)
Heaps (tables without clustered indexes)
  * [ CREATE INDEX (Transact-SQL) - SQL Server ](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-index-transact-sql?source=recommendations)
The CREATE INDEX statement creates a relational index on a table or view.


Show 5 more
Certification
[ Microsoft Certified: Azure Database Administrator Associate - Certifications ](https://learn.microsoft.com/en-us/credentials/certifications/azure-database-administrator-associate/?source=recommendations)
Administer an SQL Server database infrastructure for cloud, on-premises and hybrid relational databases using the Microsoft PaaS relational database offerings.
Mar 8, 4 PM - Mar 8, 4 PM
Experiment with what's next in AI-driven apps and agent design
* * *
  * Last updated on 11/18/2025


##  In this article
  1. [Available index types](https://learn.microsoft.com/en-us/sql/relational-databases/indexes/indexes?view=sql-server-ver17#available-index-types)
  2. [Related content](https://learn.microsoft.com/en-us/sql/relational-databases/indexes/indexes?view=sql-server-ver17#related-content)


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
[ Sign in ](https://learn.microsoft.com/en-us/sql/relational-databases/indexes/indexes?view=sql-server-ver17)
[English (United States)](https://learn.microsoft.com/en-us/locale?target=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fsql%2Frelational-databases%2Findexes%2Findexes%3Fview%3Dsql-server-ver17)
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
