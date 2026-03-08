# In-Memory OLTP overview and usage scenarios
Feedback
Summarize this article for me
##  In this article
  1. [In-Memory OLTP overview](https://learn.microsoft.com/en-us/sql/relational-databases/in-memory-oltp/overview-and-usage-scenarios?view=sql-server-ver17#-overview)
  2. [Usage scenarios for In-Memory OLTP](https://learn.microsoft.com/en-us/sql/relational-databases/in-memory-oltp/overview-and-usage-scenarios?view=sql-server-ver17#usage-scenarios-for-)
  3. [Sample script](https://learn.microsoft.com/en-us/sql/relational-databases/in-memory-oltp/overview-and-usage-scenarios?view=sql-server-ver17#sample-script)
  4. [Related content](https://learn.microsoft.com/en-us/sql/relational-databases/in-memory-oltp/overview-and-usage-scenarios?view=sql-server-ver17#related-content)


**Applies to:** ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure SQL Database](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure SQL Managed Instance](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to)
In-Memory OLTP is the premier technology available in SQL Server and SQL Database for optimizing performance of transaction processing, data ingestion, data load, and transient data scenarios. This article includes an overview of the technology and outlines usage scenarios for In-Memory OLTP. Use this information to determine whether In-Memory OLTP is right for your application. The article concludes with an example that shows In-Memory OLTP objects, reference to a perf demo, and references to resources you can use for next steps.
  * This article covers the In-Memory OLTP technology in both SQL Server and SQL Database.
  * For more information specific to in-memory data in Azure SQL Database, see [Optimize performance by using in-memory technologies in Azure SQL Database](https://learn.microsoft.com/en-us/azure/azure-sql/database/in-memory-oltp-overview?view=azuresql-db&preserve-view=true) and [Blog: In-Memory OLTP in Azure SQL Database](https://azure.microsoft.com/blog/in-memory-oltp-in-azure-sql-database/).
  * For more information specific to in-memory data in Azure SQL Managed Instance, see [Optimize performance by using in-memory technologies in Azure SQL Managed Instance](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/in-memory-oltp-overview?view=azuresql-mi&preserve-view=true).


[](https://learn.microsoft.com/en-us/sql/relational-databases/in-memory-oltp/overview-and-usage-scenarios?view=sql-server-ver17#-overview)
## In-Memory OLTP overview
In-Memory OLTP can provide great performance gains, for the right workloads. While customers have seen up to 30X performance gain in some cases, how much gain you see depends on the workload.
Now, where does this performance gain come from? In essence, In-Memory OLTP improves performance of transaction processing by making data access and transaction execution more efficient, and by removing lock and latch contention between concurrently executing transactions. In-Memory OLTP isn't fast because it's in-memory; it's fast because of optimization around in-memory data. Data storage, access, and processing algorithms were redesigned from the ground up to take advantage of the latest enhancements in in-memory and high concurrency computing.
Now, just because data lives in-memory doesn't mean you lose it when there's a failure. By default, all transactions are fully durable, meaning that you have the same durability guarantees you get for any other table in SQL Server: as part of transaction commit, all changes are written to the transaction log, on disk. If there's a failure at any time after the transaction commits, your data is there when the database comes back online. In addition, In-Memory OLTP works with all high availability and disaster recovery capabilities of SQL Server, like [availability groups](https://learn.microsoft.com/en-us/sql/database-engine/availability-groups/windows/overview-of-always-on-availability-groups-sql-server?view=sql-server-ver17), [failover cluster instances](https://learn.microsoft.com/en-us/sql/sql-server/failover-clusters/windows/always-on-failover-cluster-instances-sql-server?view=sql-server-ver17), backup/restore, and so on.
To use In-Memory OLTP in your database, you use one or more of the following types of objects:
  * _Memory-optimized tables_ are used for storing user data. You declare a table to be memory-optimized at create time.
  * _Non-durable tables_ are used for transient data, either for caching or for intermediate result set (replacing traditional temp tables). A non-durable table is a memory-optimized table that is declared with DURABILITY=SCHEMA_ONLY, meaning that changes to these tables don't incur any IO. This avoids consuming log IO resources for cases where durability isn't a concern.
  * _Memory-optimized table types_ are used for table-valued parameters (TVPs) and intermediate result sets in stored procedures. Memory-optimized table types can be used instead of traditional table types. Table variables and TVPs that are declared using a memory-optimized table type inherit the benefits of non-durable memory-optimized tables: efficient data access, and no IO.
  * _Natively compiled T-SQL modules_ are used to further reduce the time taken for an individual transaction by reducing CPU cycles required to process the operations. You declare a Transact-SQL module to be natively compiled at create time. At this time, the following T-SQL modules can be natively compiled: stored procedures, triggers, and scalar user-defined functions.


In-Memory OLTP is built into SQL Server and SQL Database. Because these objects behave in a similar way to their traditional counterparts, you can often gain performance benefits while making only minimal changes to the database and the application. Plus, you can have both memory-optimized and traditional disk-based tables in the same database, and run queries across the two. See the [sample Transact-SQL script](https://learn.microsoft.com/en-us/sql/relational-databases/in-memory-oltp/overview-and-usage-scenarios?view=sql-server-ver17#sample-script) for each of these types of objects later in this article.
[](https://learn.microsoft.com/en-us/sql/relational-databases/in-memory-oltp/overview-and-usage-scenarios?view=sql-server-ver17#usage-scenarios-for-)
## Usage scenarios for In-Memory OLTP
In-Memory OLTP isn't a magic go-fast button, and isn't suitable for all workloads. For example, memory-optimized tables don't bring down your CPU utilization if most of the queries are performing aggregation over large ranges of data. Columnstore indexes help with that scenario.
**Known issue** : For databases with memory-optimized tables, performing a transactional log backup with no recovery, and later executing a transaction log restore with recovery, could result in an unresponsive database restore process. This issue can also affect log shipping functionality. To work around this problem, the SQL Server instance can be restarted before initiating the restore process.
Here's a list of scenarios and application patterns where we have seen customers be successful with In-Memory OLTP.
[](https://learn.microsoft.com/en-us/sql/relational-databases/in-memory-oltp/overview-and-usage-scenarios?view=sql-server-ver17#high-throughput-and-low-latency-transaction-processing)
### High-throughput and low-latency transaction processing
This is the core scenario for which we built In-Memory OLTP: support large volumes of transactions, with consistent low latency for individual transactions.
Common workload scenarios are: trading of financial instruments, sports betting, mobile gaming, and ad delivery. Another common pattern is a "catalog" that is frequently read and/or updated. One example is where you have large files, each distributed over multiple cluster nodes, and you catalog the location of each shard of each file in a memory-optimized table.
[](https://learn.microsoft.com/en-us/sql/relational-databases/in-memory-oltp/overview-and-usage-scenarios?view=sql-server-ver17#implementation-considerations)
#### Implementation considerations
Use memory-optimized tables for your core transaction tables, that is, the tables with the most performance-critical transactions. Use natively compiled stored procedures to optimize execution of the logic associated with the business transaction. The more of the logic you can push down into stored procedures in the database, the more benefit you see from In-Memory OLTP.
To get started in an existing application:
  1. Use the [transaction performance analysis report](https://learn.microsoft.com/en-us/sql/relational-databases/in-memory-oltp/determining-if-a-table-or-stored-procedure-should-be-ported-to-in-memory-oltp?view=sql-server-ver17) to identify the objects you want to migrate.
  2. Use the [Memory Optimization Advisor](https://learn.microsoft.com/en-us/sql/relational-databases/in-memory-oltp/memory-optimization-advisor?view=sql-server-ver17) and [Native Compilation Advisor](https://learn.microsoft.com/en-us/sql/relational-databases/in-memory-oltp/native-compilation-advisor?view=sql-server-ver17) to help with migration.


[](https://learn.microsoft.com/en-us/sql/relational-databases/in-memory-oltp/overview-and-usage-scenarios?view=sql-server-ver17#data-ingestion-including-iot-internet-of-things)
### Data ingestion, including IoT (Internet-of-Things)
In-Memory OLTP is good at ingesting large volumes of data from many different sources at the same time. And it's often beneficial to ingest data into a SQL Server database compared with other destinations, because SQL Server makes running queries against the data fast, and allows you to get real-time insights.
Common application patterns are:
  * Ingesting sensor readings and events, and allow notifications as well as historical analysis.
  * Managing batch updates, even from multiple sources, while minimizing the impact on the concurrent read workload.


[](https://learn.microsoft.com/en-us/sql/relational-databases/in-memory-oltp/overview-and-usage-scenarios?view=sql-server-ver17#implementation-considerations-1)
#### Implementation considerations
Use a memory-optimized table for the data ingestion. If the ingestion consists mostly of inserts (rather than updates) and In-Memory OLTP storage footprint of the data is a concern, either
  * Use a job to regularly batch-offload data to a disk-based table with a [clustered columnstore index](https://learn.microsoft.com/en-us/sql/relational-databases/indexes/columnstore-indexes-overview?view=sql-server-ver17), using a job that does `INSERT INTO <disk-based table> SELECT FROM <memory-optimized table>`; or
  * Use a [temporal memory-optimized table](https://learn.microsoft.com/en-us/sql/relational-databases/tables/system-versioned-temporal-tables-with-memory-optimized-tables?view=sql-server-ver17) to manage historical data - in this mode, historical data lives on disk, and data movement is managed by the system.


The SQL Server samples repository contains a smart grid application that uses a temporal memory-optimized table, a memory-optimized table type, and a natively compiled stored procedure, to speed up data ingestion, while managing the In-Memory OLTP storage footprint of the sensor data:
[](https://learn.microsoft.com/en-us/sql/relational-databases/in-memory-oltp/overview-and-usage-scenarios?view=sql-server-ver17#caching-and-session-state)
### Caching and session state
The In-Memory OLTP technology makes the database engine in SQL Server or Azure SQL databases an attractive platform for maintaining session state (for example, for an ASP.NET application) and for caching.
ASP.NET session state is a successful use case for In-Memory OLTP. With SQL Server, one customer was about to achieve 1.2 Million requests per second. In the meantime, they have started using In-Memory OLTP for the caching needs of all mid-tier applications in the enterprise. Details: [How bwin is using SQL Server 2016 (13.x) In-Memory OLTP to achieve unprecedented performance and scale](https://blogs.msdn.microsoft.com/sqlcat/2016/10/26/how-bwin-is-using-sql-server-2016-in-memory-oltp-to-achieve-unprecedented-performance-and-scale/)
[](https://learn.microsoft.com/en-us/sql/relational-databases/in-memory-oltp/overview-and-usage-scenarios?view=sql-server-ver17#implementation-considerations-2)
#### Implementation considerations
You can use non-durable memory-optimized tables as a simple key-value store by storing a BLOB in a varbinary(max) column. Alternatively, you can implement a semi-structured cache with [JSON support](https://azure.microsoft.com/blog/json-support-is-generally-available-in-azure-sql-database/) in SQL Server and SQL Database. Finally, you can create a full relational cache through non-durable tables with a full relational schema, including various data types and constraints.
Get started with memory-optimizing ASP.NET session state by using the scripts published on GitHub to replace the objects created by the built-in SQL Server session state provider:
[](https://learn.microsoft.com/en-us/sql/relational-databases/in-memory-oltp/overview-and-usage-scenarios?view=sql-server-ver17#customer-case-study)
#### Customer case study
  * bwin increased throughput with ASP.NET session state even further and implemented an enterprise-wide mid-tier caching system, with In-Memory OLTP in SQL Server 2016 (13.x): [How bwin is using SQL Server 2016 (13.x) In-Memory OLTP to achieve unprecedented performance and scale](https://blogs.msdn.microsoft.com/sqlcat/2016/10/26/how-bwin-is-using-sql-server-2016-in-memory-oltp-to-achieve-unprecedented-performance-and-scale/).


[](https://learn.microsoft.com/en-us/sql/relational-databases/in-memory-oltp/overview-and-usage-scenarios?view=sql-server-ver17#tempdb-object-replacement)
### tempdb object replacement
Use non-durable tables and memory-optimized table types to replace your traditional `tempdb` based structures, such as temporary tables, table variables, and table-valued parameters (TVPs).
Memory-optimized table variables and non-durable tables typically reduce CPU and completely remove log IO, when compared with traditional table variables and #temp table.
[](https://learn.microsoft.com/en-us/sql/relational-databases/in-memory-oltp/overview-and-usage-scenarios?view=sql-server-ver17#implementation-considerations-3)
#### Implementation considerations
To get started: [Improving temp table and table variable performance using memory optimization.](https://learn.microsoft.com/en-us/archive/blogs/sqlserverstorageengine/improving-temp-table-and-table-variable-performance-using-memory-optimization)
[](https://learn.microsoft.com/en-us/sql/relational-databases/in-memory-oltp/overview-and-usage-scenarios?view=sql-server-ver17#customer-case-study-1)
#### Customer case study
  * One customer was able to improve performance by 40%, just by replacing traditional TVPs with memory-optimized TVPs: [High Speed IoT Data Ingestion Using In-Memory OLTP in Azure](https://learn.microsoft.com/en-us/archive/blogs/sqlserverstorageengine/a-technical-case-study-high-speed-iot-data-ingestion-using-in-memory-oltp-in-azure)


[](https://learn.microsoft.com/en-us/sql/relational-databases/in-memory-oltp/overview-and-usage-scenarios?view=sql-server-ver17#etl-extract-transform-load)
### ETL (Extract Transform Load)
ETL workflows often include load of data into a staging table, transformations of the data, and load into the final tables.
Use non-durable memory-optimized tables for the data staging. They completely remove all IO, and make data access more efficient.
[](https://learn.microsoft.com/en-us/sql/relational-databases/in-memory-oltp/overview-and-usage-scenarios?view=sql-server-ver17#implementation-considerations-4)
#### Implementation considerations
If you perform transformations on the staging table as part of the workflow, you can use natively compiled stored procedures to speed up these transformations. If you can do these transformations in parallel, you get additional scaling benefits from the memory-optimization.
[](https://learn.microsoft.com/en-us/sql/relational-databases/in-memory-oltp/overview-and-usage-scenarios?view=sql-server-ver17#sample-script)
## Sample script
Before you can start using In-Memory OLTP, you need to create a MEMORY_OPTIMIZED_DATA filegroup. In addition, we recommend using database compatibility level 130 (or higher), and set the database option MEMORY_OPTIMIZED_ELEVATE_TO_SNAPSHOT to ON.
You can use the script at the following location to create the filegroup in the default data folder, and configure the recommended settings:
The following sample script illustrates In-Memory OLTP objects you can create in your database.
First start by configuring the database for In-Memory OLTP.
SQL
Copy
```
-- configure recommended DB option
ALTER DATABASE CURRENT SET MEMORY_OPTIMIZED_ELEVATE_TO_SNAPSHOT=ON;
GO

```

You can create tables with different durability:
SQL
Copy
```
-- memory-optimized table
CREATE TABLE dbo.table1
( c1 INT IDENTITY PRIMARY KEY NONCLUSTERED,
  c2 NVARCHAR(MAX))
WITH (MEMORY_OPTIMIZED=ON);
GO
-- non-durable table
CREATE TABLE dbo.temp_table1
( c1 INT IDENTITY PRIMARY KEY NONCLUSTERED,
  c2 NVARCHAR(MAX))
WITH (MEMORY_OPTIMIZED=ON,
      DURABILITY=SCHEMA_ONLY);
GO

```

You can create a [table type](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-type-transact-sql?view=sql-server-ver17) as an in-memory table.
SQL
Copy
```
-- memory-optimized table type
CREATE TYPE dbo.tt_table1 AS TABLE
( c1 INT IDENTITY,
  c2 NVARCHAR(MAX),
  is_transient BIT NOT NULL DEFAULT (0),
  INDEX ix_c1 HASH (c1) WITH (BUCKET_COUNT=1024))
WITH (MEMORY_OPTIMIZED=ON);
GO

```

You can create a [natively compiled stored procedure](https://learn.microsoft.com/en-us/sql/relational-databases/in-memory-oltp/creating-natively-compiled-stored-procedures?view=sql-server-ver17). For more information, see [Calling Natively Compiled Stored Procedures from Data Access Applications](https://learn.microsoft.com/en-us/sql/relational-databases/in-memory-oltp/calling-natively-compiled-stored-procedures-from-data-access-applications?view=sql-server-ver17).
SQL
Copy
```
-- natively compiled stored procedure
CREATE PROCEDURE dbo.usp_ingest_table1
  @table1 dbo.tt_table1 READONLY
WITH NATIVE_COMPILATION, SCHEMABINDING
AS
BEGIN ATOMIC
    WITH (TRANSACTION ISOLATION LEVEL=SNAPSHOT,
          LANGUAGE=N'us_english')

  DECLARE @i INT = 1

  WHILE @i > 0
  BEGIN
    INSERT dbo.table1
    SELECT c2
    FROM @table1
    WHERE c1 = @i AND is_transient=0

    IF @@ROWCOUNT > 0
      SET @i += 1
    ELSE
    BEGIN
      INSERT dbo.temp_table1
      SELECT c2
      FROM @table1
      WHERE c1 = @i AND is_transient=1

      IF @@ROWCOUNT > 0
        SET @i += 1
      ELSE
        SET @i = 0
    END
  END

END
GO
-- sample execution of the proc
DECLARE @table1 dbo.tt_table1;
INSERT @table1 (c2, is_transient) VALUES (N'sample durable', 0);
INSERT @table1 (c2, is_transient) VALUES (N'sample non-durable', 1);
EXECUTE dbo.usp_ingest_table1 @table1=@table1;
SELECT c1, c2 from dbo.table1;
SELECT c1, c2 from dbo.temp_table1;
GO

```

[](https://learn.microsoft.com/en-us/sql/relational-databases/in-memory-oltp/overview-and-usage-scenarios?view=sql-server-ver17#related-content)
## Related content
  * [In-Memory OLTP Technologies for Faster T-SQL Performance](https://learn.microsoft.com/en-us/sql/relational-databases/in-memory-oltp/survey-of-initial-areas-in-in-memory-oltp?view=sql-server-ver17)
  * [Performance and resource utilization benefits of In-Memory OLTP in Azure SQL Database](https://azure.microsoft.com/blog/in-memory-oltp-in-azure-sql-database/)
  * [Improving temp table and table variable performance using memory optimization](https://learn.microsoft.com/en-us/archive/blogs/sqlserverstorageengine/improving-temp-table-and-table-variable-performance-using-memory-optimization)
  * [Demonstration: Performance Improvement of In-Memory OLTP](https://learn.microsoft.com/en-us/sql/relational-databases/in-memory-oltp/demonstration-performance-improvement-of-in-memory-oltp?view=sql-server-ver17)
  * [Sample Database for In-Memory OLTP](https://learn.microsoft.com/en-us/sql/relational-databases/in-memory-oltp/sample-database-for-in-memory-oltp?view=sql-server-ver17)
  * Perf demo using In-Memory OLTP can be found at:
  * [In-Memory OLTP overview and usage scenarios](https://learn.microsoft.com/en-us/sql/relational-databases/in-memory-oltp/overview-and-usage-scenarios?view=sql-server-ver17)
  * [Optimize Performance using In-Memory Technologies in Azure SQL](https://learn.microsoft.com/en-us/azure/sql-database/sql-database-in-memory)
  * [System-Versioned Temporal Tables with Memory-Optimized Tables](https://learn.microsoft.com/en-us/sql/relational-databases/tables/system-versioned-temporal-tables-with-memory-optimized-tables?view=sql-server-ver17)
  * [The Memory Optimized Filegroup](https://learn.microsoft.com/en-us/sql/relational-databases/in-memory-oltp/the-memory-optimized-filegroup?view=sql-server-ver17)


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
  * [ Introduction to Memory-Optimized Tables - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/in-memory-oltp/introduction-to-memory-optimized-tables?source=recommendations)
Learn about memory-optimized tables, which are durable and support transactions that are atomic, consistent, isolated, and durable.
  * [ In-memory OLTP for faster T-SQL Performance - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/in-memory-oltp/survey-of-initial-areas-in-in-memory-oltp?source=recommendations)
Learn the basics of the In-Memory OLTP performance features of SQL Server and Azure SQL Database with quick explanations and core code samples for developers.
  * [ Requirements for using memory-optimized tables - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/in-memory-oltp/requirements-for-using-memory-optimized-tables?source=recommendations)
Learn about the requirements for using In-Memory OLTP, including SQL Database version, memory & storage considerations, and installation.
  * [ Memory requirements - memory-optimized tables - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/in-memory-oltp/estimate-memory-requirements-for-memory-optimized-tables?source=recommendations)
Learn about memory use and management scenarios for memory-optimized tables in SQL Server, which require sufficient memory for all the rows and indexes.
  * [ Should Table or Stored Procedure Be Ported to In-Memory OLTP? - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/in-memory-oltp/determining-if-a-table-or-stored-procedure-should-be-ported-to-in-memory-oltp?source=recommendations)
Use the Transaction Performance Analysis report in SQL Server Management Studio to evaluate whether In-Memory OLTP can improve database application performance.
  * [ Defining Durability for Memory-Optimized Objects - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/in-memory-oltp/defining-durability-for-memory-optimized-objects?source=recommendations)
Learn about the durability options for memory-optimized tables in SQL Server: the default SCHEMA_AND_DATA and SCHEMA_ONLY.
  * [ Hardware for SQL In-Memory OLTP - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/in-memory-oltp/blog-hardware-in-memory-oltp?source=recommendations)
Learn about hardware considerations for In-Memory OLTP performance in SQL Server. In-Memory OLTP uses memory and disk in different ways than disk-based tables.
  * [ Durability for Memory-Optimized Tables - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/in-memory-oltp/durability-for-memory-optimized-tables?source=recommendations)
Learn how In-Memory OLTP provides full durability for memory-optimized tables, by using transaction logging and by saving data changes to on-disk storage.


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
  * Last updated on 03/05/2024


##  In this article
  1. [In-Memory OLTP overview](https://learn.microsoft.com/en-us/sql/relational-databases/in-memory-oltp/overview-and-usage-scenarios?view=sql-server-ver17#-overview)
  2. [Usage scenarios for In-Memory OLTP](https://learn.microsoft.com/en-us/sql/relational-databases/in-memory-oltp/overview-and-usage-scenarios?view=sql-server-ver17#usage-scenarios-for-)
  3. [Sample script](https://learn.microsoft.com/en-us/sql/relational-databases/in-memory-oltp/overview-and-usage-scenarios?view=sql-server-ver17#sample-script)
  4. [Related content](https://learn.microsoft.com/en-us/sql/relational-databases/in-memory-oltp/overview-and-usage-scenarios?view=sql-server-ver17#related-content)


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
[ Sign in ](https://learn.microsoft.com/en-us/sql/relational-databases/in-memory-oltp/overview-and-usage-scenarios?view=sql-server-ver17)
[English (United States)](https://learn.microsoft.com/en-us/locale?target=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fsql%2Frelational-databases%2Fin-memory-oltp%2Foverview-and-usage-scenarios%3Fview%3Dsql-server-ver17)
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
