# Performance Center for SQL Server Database Engine and Azure SQL Database
Feedback
Summarize this article for me
##  In this article
  1. [Configuration options for performance](https://learn.microsoft.com/en-us/sql/relational-databases/performance/performance-center-for-sql-server-database-engine-and-azure-sql-database?view=sql-server-ver17#configuration-options-for-performance)
  2. [Query Performance Options](https://learn.microsoft.com/en-us/sql/relational-databases/performance/performance-center-for-sql-server-database-engine-and-azure-sql-database?view=sql-server-ver17#query-performance-options)
  3. [See also](https://learn.microsoft.com/en-us/sql/relational-databases/performance/performance-center-for-sql-server-database-engine-and-azure-sql-database?view=sql-server-ver17#see-also)


**Applies to:** ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure SQL Database](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to)
This page provides links to help you locate the information that you need about performance in the SQL Server Database Engine and Azure SQL Database.
**Legend**
![Screenshot of the legend that explains the feature availability icons.](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/performance-center-for-sql-server-database-engine-and-azure-sql-database/security-center-legend.png?view=sql-server-ver17)
[](https://learn.microsoft.com/en-us/sql/relational-databases/performance/performance-center-for-sql-server-database-engine-and-azure-sql-database?view=sql-server-ver17#configuration-options-for-performance)
## Configuration options for performance
SQL Server provides the ability to affect database engine performance through a number of configuration options at the SQL Server Database Engine level. With Azure SQL Database, Microsoft performs most, but not all, of these optimizations for you.
Expand table
Options | Description
---|---
**Disk configuration options** |  ![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-sqlserver.png?view=sql-server-ver17) [Disk striping and RAID](https://technet.microsoft.com/library/ms190764\(v=sql.105\).aspx)
**Data and log file configuration options** |  ![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-sqlserver.png?view=sql-server-ver17) [Place Data and Log Files on Separate Drives](https://learn.microsoft.com/en-us/sql/relational-databases/policy-based-management/place-data-and-log-files-on-separate-drives?view=sql-server-ver17)
![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-sqlserver.png?view=sql-server-ver17) [View or Change the Default Locations for Data and Log Files (SQL Server Management Studio)](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/view-or-change-the-default-locations-for-data-and-log-files?view=sql-server-ver17)
`tempdb` configuration options** |  ![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-sqlserver.png?view=sql-server-ver17) [Performance Improvements in TempDB](https://learn.microsoft.com/en-us/sql/relational-databases/databases/tempdb-database?view=sql-server-ver17)
![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-sqlserver.png?view=sql-server-ver17) [Database Engine Configuration - TempDB](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/install-sql-server?view=sql-server-ver17)
![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-sqlserver.png?view=sql-server-ver17) [Using SSDs in Azure VMs to store SQL Server TempDB and Buffer Pool Extensions](https://cloudblogs.microsoft.com/sqlserver/2014/09/25/using-ssds-in-azure-vms-to-store-sql-server-tempdb-and-buffer-pool-extensions/)
![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-sqlserver.png?view=sql-server-ver17) [Disk and performance best practices for temporary disk for SQL Server in Azure Virtual Machines](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/performance-guidelines-best-practices-storage)
**(server configuration option)s** |  **Processor configuration options**

![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-sqlserver.png?view=sql-server-ver17) [affinity mask (server configuration option)](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/affinity-mask-server-configuration-option?view=sql-server-ver17)
![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-sqlserver.png?view=sql-server-ver17) [affinity Input-Output mask (server configuration option)](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/affinity-input-output-mask-server-configuration-option?view=sql-server-ver17)
![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-sqlserver.png?view=sql-server-ver17) [affinity64 mask (server configuration option)](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/affinity64-mask-server-configuration-option?view=sql-server-ver17)
![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-sqlserver.png?view=sql-server-ver17) [affinity64 Input-Output mask (server configuration option)](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/affinity64-input-output-mask-server-configuration-option?view=sql-server-ver17)
![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-sqlserver.png?view=sql-server-ver17) [Configure the max worker threads (server configuration option)](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/configure-the-max-worker-threads-server-configuration-option?view=sql-server-ver17)

**Memory configuration options**

![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-sqlserver.png?view=sql-server-ver17) [Server Memory (server configuration option)s](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/server-memory-server-configuration-options?view=sql-server-ver17)

**Index configuration options**

![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-sqlserver.png?view=sql-server-ver17) [Configure the fill factor (server configuration option)](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/configure-the-fill-factor-server-configuration-option?view=sql-server-ver17)

**Query configuration options**

![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-sqlserver.png?view=sql-server-ver17) [Configure the min memory per query (server configuration option)](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/configure-the-min-memory-per-query-server-configuration-option?view=sql-server-ver17)
![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-sqlserver.png?view=sql-server-ver17) [Configure the query governor cost limit (server configuration option)](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/configure-the-query-governor-cost-limit-server-configuration-option?view=sql-server-ver17)
![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-sqlserver.png?view=sql-server-ver17) [Configure the max degree of parallelism (server configuration option)](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/configure-the-max-degree-of-parallelism-server-configuration-option?view=sql-server-ver17)
![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-sqlserver.png?view=sql-server-ver17) [Configure the cost threshold for parallelism (server configuration option)](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/configure-the-cost-threshold-for-parallelism-server-configuration-option?view=sql-server-ver17)
![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-sqlserver.png?view=sql-server-ver17) [optimize for ad hoc workloads (server configuration option)](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/optimize-for-ad-hoc-workloads-server-configuration-option?view=sql-server-ver17)

**Backup configuration options**

![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-sqlserver.png?view=sql-server-ver17) [View or Configure the backup compression default (server configuration option)](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/view-or-configure-the-backup-compression-default-server-configuration-option?view=sql-server-ver17)
**Database configuration optimization options** |  ![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-sqlserver.png?view=sql-server-ver17) [Data Compression](https://learn.microsoft.com/en-us/sql/relational-databases/data-compression/data-compression?view=sql-server-ver17)
![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-both.png?view=sql-server-ver17) [View or Change the Compatibility Level of a Database](https://learn.microsoft.com/en-us/sql/relational-databases/databases/view-or-change-the-compatibility-level-of-a-database?view=sql-server-ver17)
![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-both.png?view=sql-server-ver17) [ALTER DATABASE SCOPED CONFIGURATION (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/statements/alter-database-scoped-configuration-transact-sql?view=sql-server-ver17)
**Table configuration optimization** |  ![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-sqlserver.png?view=sql-server-ver17) [Partitioned Tables and Indexes](https://learn.microsoft.com/en-us/sql/relational-databases/partitions/partitioned-tables-and-indexes?view=sql-server-ver17)
**Database Engine Performance in an Azure Virtual Machine** |  ![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-sqlserver.png?view=sql-server-ver17) [Quick check list](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/performance-guidelines-best-practices-checklist)
![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-sqlserver.png?view=sql-server-ver17) [Virtual machine size and storage account considerations](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/performance-guidelines-best-practices-vm-size)
![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-sqlserver.png?view=sql-server-ver17) [Disks and performance considerations](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/performance-guidelines-best-practices-storage)
![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-sqlserver.png?view=sql-server-ver17) [Collect baseline: Performance best practices](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/performance-guidelines-best-practices-collect-baseline)
![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-sqlserver.png?view=sql-server-ver17) [Feature specific performance considerations](https://techcommunity.microsoft.com/t5/fasttrack-for-azure/feature-comparison-of-azure-sql-database-azure-sql-managed/ba-p/3154789)
**Performance best practices and configuration guidelines for SQL Server on Linux** |  ![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-sqlserver.png?view=sql-server-ver17) [SQL Server configuration](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-performance-best-practices?view=sql-server-ver17#sql-server-configuration)
![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-sqlserver.png?view=sql-server-ver17) [Linux OS Configuration](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-performance-best-practices?view=sql-server-ver17)
Additional considerations are available in:
  * [Recommended updates and configuration options for SQL Server 2012 and SQL Server 2014 with high-performance workloads](https://support.microsoft.com/help/2964518)
  * [Recommended updates and configuration options for SQL Server 2017 and 2016 with high-performance workloads](https://support.microsoft.com/help/4465518)


[](https://learn.microsoft.com/en-us/sql/relational-databases/performance/performance-center-for-sql-server-database-engine-and-azure-sql-database?view=sql-server-ver17#query-performance-options)
## Query Performance Options
Expand table
Option | Description
---|---
![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-both.png?view=sql-server-ver17) **[Indexes](https://learn.microsoft.com/en-us/sql/relational-databases/indexes/indexes?view=sql-server-ver17)** |  [Reorganize and Rebuild Indexes](https://learn.microsoft.com/en-us/sql/relational-databases/indexes/reorganize-and-rebuild-indexes?view=sql-server-ver17)
[Specify Fill Factor for an Index](https://learn.microsoft.com/en-us/sql/relational-databases/indexes/specify-fill-factor-for-an-index?view=sql-server-ver17)
[Configure Parallel Index Operations](https://learn.microsoft.com/en-us/sql/relational-databases/indexes/configure-parallel-index-operations?view=sql-server-ver17)
[SORT_IN_TEMPDB Option For Indexes](https://learn.microsoft.com/en-us/sql/relational-databases/indexes/sort-in-tempdb-option-for-indexes?view=sql-server-ver17)
[Improve the Performance of Full-Text Indexes](https://learn.microsoft.com/en-us/sql/relational-databases/search/improve-the-performance-of-full-text-indexes?view=sql-server-ver17)
[Configure the min memory per query (server configuration option)](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/configure-the-min-memory-per-query-server-configuration-option?view=sql-server-ver17)
[Configure the index create memory (server configuration option)](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/configure-the-index-create-memory-server-configuration-option?view=sql-server-ver17)
![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-both.png?view=sql-server-ver17) **[Partitioned Tables and Indexes](https://learn.microsoft.com/en-us/sql/relational-databases/partitions/partitioned-tables-and-indexes?view=sql-server-ver17)** | [Benefits of Partitioning](https://learn.microsoft.com/en-us/sql/relational-databases/partitions/partitioned-tables-and-indexes?view=sql-server-ver17)
![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-both.png?view=sql-server-ver17) **[Joins](https://learn.microsoft.com/en-us/sql/relational-databases/performance/joins?view=sql-server-ver17)** |  [Join Fundamentals](https://learn.microsoft.com/en-us/sql/relational-databases/performance/joins?view=sql-server-ver17#fundamentals)
[Nested Loops join](https://learn.microsoft.com/en-us/sql/relational-databases/performance/joins?view=sql-server-ver17#nested_loops)
[Merge join](https://learn.microsoft.com/en-us/sql/relational-databases/performance/joins?view=sql-server-ver17#merge)
[Hash join](https://learn.microsoft.com/en-us/sql/relational-databases/performance/joins?view=sql-server-ver17#hash)
![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-both.png?view=sql-server-ver17) **[Subqueries](https://learn.microsoft.com/en-us/sql/relational-databases/performance/subqueries?view=sql-server-ver17)** |  [Subquery Fundamentals](https://learn.microsoft.com/en-us/sql/relational-databases/performance/subqueries?view=sql-server-ver17#fundamentals)
[Correlated subqueries](https://learn.microsoft.com/en-us/sql/relational-databases/performance/subqueries?view=sql-server-ver17#correlated)
[Subquery types](https://learn.microsoft.com/en-us/sql/relational-databases/performance/subqueries?view=sql-server-ver17#types)
![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-both.png?view=sql-server-ver17) **[Stored Procedures](https://learn.microsoft.com/en-us/sql/relational-databases/stored-procedures/stored-procedures-database-engine?view=sql-server-ver17)** | [CREATE PROCEDURE (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-procedure-transact-sql?view=sql-server-ver17#best-practices)
![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-both.png?view=sql-server-ver17) **[User-Defined Functions](https://learn.microsoft.com/en-us/sql/relational-databases/user-defined-functions/user-defined-functions?view=sql-server-ver17)** |  [CREATE FUNCTION (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-function-transact-sql?view=sql-server-ver17#best-practices)
[Create User-defined Functions (Database Engine)](https://learn.microsoft.com/en-us/sql/relational-databases/user-defined-functions/create-user-defined-functions-database-engine?view=sql-server-ver17)
![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-both.png?view=sql-server-ver17) **Parallelism optimization** |  [Configure the max worker threads (server configuration option)](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/configure-the-max-worker-threads-server-configuration-option?view=sql-server-ver17)
[ALTER DATABASE SCOPED CONFIGURATION (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/statements/alter-database-scoped-configuration-transact-sql?view=sql-server-ver17)
![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-both.png?view=sql-server-ver17) **Query optimizer optimization** |  [ALTER DATABASE SCOPED CONFIGURATION (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/statements/alter-database-scoped-configuration-transact-sql?view=sql-server-ver17)
[USE HINT query hint](https://learn.microsoft.com/en-us/sql/t-sql/queries/hints-transact-sql-query?view=sql-server-ver17#use_hint)
![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-both.png?view=sql-server-ver17) **[Statistics](https://learn.microsoft.com/en-us/sql/relational-databases/statistics/statistics?view=sql-server-ver17)** |  [When to Update Statistics](https://learn.microsoft.com/en-us/sql/relational-databases/statistics/statistics?view=sql-server-ver17)
[Update Statistics](https://learn.microsoft.com/en-us/sql/relational-databases/statistics/update-statistics?view=sql-server-ver17)
![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-both.png?view=sql-server-ver17) **[In-Memory OLTP (In-Memory Optimization)](https://learn.microsoft.com/en-us/sql/relational-databases/in-memory-oltp/overview-and-usage-scenarios?view=sql-server-ver17)** |  [Memory-Optimized Tables](https://learn.microsoft.com/en-us/sql/relational-databases/in-memory-oltp/sample-database-for-in-memory-oltp?view=sql-server-ver17)
[Natively Compiled Stored Procedures](https://learn.microsoft.com/en-us/sql/relational-databases/in-memory-oltp/a-guide-to-query-processing-for-memory-optimized-tables?view=sql-server-ver17)
[Create and Access Tables in TempDB from Stored Procedures](https://learn.microsoft.com/en-us/sql/relational-databases/in-memory-oltp/create-and-access-tables-in-tempdb-from-stored-procedures?view=sql-server-ver17)
[Troubleshooting Common Performance Problems with Memory-Optimized Hash Indexes](https://learn.microsoft.com/en-us/previous-versions/sql/sql-server-2016/dn589805\(v=sql.130\))
[Demonstration: Performance Improvement of In-Memory OLTP](https://learn.microsoft.com/en-us/sql/relational-databases/in-memory-oltp/demonstration-performance-improvement-of-in-memory-oltp?view=sql-server-ver17)
![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-both.png?view=sql-server-ver17) **[Intelligent query processing](https://learn.microsoft.com/en-us/sql/relational-databases/performance/intelligent-query-processing?view=sql-server-ver17)** | [Intelligent query processing](https://learn.microsoft.com/en-us/sql/relational-databases/performance/intelligent-query-processing?view=sql-server-ver17)
[](https://learn.microsoft.com/en-us/sql/relational-databases/performance/performance-center-for-sql-server-database-engine-and-azure-sql-database?view=sql-server-ver17#see-also)
## See also
  * [Monitor and Tune for Performance](https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitor-and-tune-for-performance?view=sql-server-ver17)
  * [Monitoring Performance By Using the Query Store](https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitoring-performance-by-using-the-query-store?view=sql-server-ver17)
  * [Azure SQL Database performance guidance for single databases](https://learn.microsoft.com/en-us/azure/azure-sql/database/performance-guidance)
  * [Optimizing Azure SQL Database Performance using Elastic Pools](https://learn.microsoft.com/en-us/azure/azure-sql/database/elastic-pool-overview)
  * [Query Performance Insight for Azure SQL Database](https://learn.microsoft.com/en-us/azure/azure-sql/database/query-performance-insight-use)
  * [Index Design Guide](https://learn.microsoft.com/en-us/sql/relational-databases/sql-server-index-design-guide?view=sql-server-ver17)
  * [Memory Management Architecture Guide](https://learn.microsoft.com/en-us/sql/relational-databases/memory-management-architecture-guide?view=sql-server-ver17)
  * [Pages and Extents Architecture Guide](https://learn.microsoft.com/en-us/sql/relational-databases/pages-and-extents-architecture-guide?view=sql-server-ver17)
  * [Post-migration Validation and Optimization Guide](https://learn.microsoft.com/en-us/sql/relational-databases/post-migration-validation-and-optimization-guide?view=sql-server-ver17)
  * [Query Processing Architecture Guide](https://learn.microsoft.com/en-us/sql/relational-databases/query-processing-architecture-guide?view=sql-server-ver17)
  * [SQL Server Transaction Locking and Row Versioning Guide](https://learn.microsoft.com/en-us/sql/relational-databases/sql-server-transaction-locking-and-row-versioning-guide?view=sql-server-ver17)
  * [SQL Server Transaction Log Architecture and Management Guide](https://learn.microsoft.com/en-us/sql/relational-databases/sql-server-transaction-log-architecture-and-management-guide?view=sql-server-ver17)
  * [Thread and Task Architecture Guide](https://learn.microsoft.com/en-us/sql/relational-databases/thread-and-task-architecture-guide?view=sql-server-ver17)


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
  * [ SQL Server Guides - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/sql-server-guides?source=recommendations)
SQL Server internals and architecture guides.
  * [ Database Engine Tuning Advisor (DTA) Command-Line Utility - SQL Server ](https://learn.microsoft.com/en-us/sql/tools/dta/dta-utility?source=recommendations)
The dta utility is a command prompt version of Database Engine Tuning Advisor that allows you to use functionality in applications and scripts.
  * [ Automatic tuning - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/automatic-tuning/automatic-tuning?source=recommendations)
Learn about automatic tuning in SQL Server and Azure SQL Database
  * [ SQL Server I/O Fundamentals - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/sql-server-storage-guide?source=recommendations)
Learn about how storage choice and caching affect SQL Server performance.
  * [ Intelligent Query Processing - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/performance/intelligent-query-processing?source=recommendations)
Intelligent query processing features to improve query performance in SQL Server, Azure SQL Managed Instance, and Azure SQL Database.
  * [ Monitor and Tune for Performance - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitor-and-tune-for-performance?source=recommendations)
Learn about monitoring databases to assess server performance, using periodic snapshots and gathering data continuously to track performance trends.
  * [ Parameter Sensitive Plan Optimization - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/performance/parameter-sensitive-plan-optimization?source=recommendations)
Learn about Parameter Sensitive Plan Optimization in the Query Store.


Show 4 more
Learning path
[ Optimize query performance in Azure SQL - Training ](https://learn.microsoft.com/en-us/training/paths/optimize-query-performance-sql-server/?source=recommendations)
Optimize query performance in Azure SQL
Certification
[ Microsoft Certified: Azure Database Administrator Associate - Certifications ](https://learn.microsoft.com/en-us/credentials/certifications/azure-database-administrator-associate/?source=recommendations)
Administer an SQL Server database infrastructure for cloud, on-premises and hybrid relational databases using the Microsoft PaaS relational database offerings.
Mar 8, 4 PM - Mar 8, 4 PM
Experiment with what's next in AI-driven apps and agent design
* * *
  * Last updated on 08/27/2024


##  In this article
  1. [Configuration options for performance](https://learn.microsoft.com/en-us/sql/relational-databases/performance/performance-center-for-sql-server-database-engine-and-azure-sql-database?view=sql-server-ver17#configuration-options-for-performance)
  2. [Query Performance Options](https://learn.microsoft.com/en-us/sql/relational-databases/performance/performance-center-for-sql-server-database-engine-and-azure-sql-database?view=sql-server-ver17#query-performance-options)
  3. [See also](https://learn.microsoft.com/en-us/sql/relational-databases/performance/performance-center-for-sql-server-database-engine-and-azure-sql-database?view=sql-server-ver17#see-also)


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
[ Sign in ](https://learn.microsoft.com/en-us/sql/relational-databases/performance/performance-center-for-sql-server-database-engine-and-azure-sql-database?view=sql-server-ver17)
[English (United States)](https://learn.microsoft.com/en-us/locale?target=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fsql%2Frelational-databases%2Fperformance%2Fperformance-center-for-sql-server-database-engine-and-azure-sql-database%3Fview%3Dsql-server-ver17)
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
