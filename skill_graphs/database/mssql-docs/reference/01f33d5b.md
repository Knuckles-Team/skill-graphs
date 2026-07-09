# Database Engine Tuning Advisor
Feedback
Summarize this article for me
##  In this article
  1. [Database Engine Tuning Advisor benefits](https://learn.microsoft.com/en-us/sql/relational-databases/performance/database-engine-tuning-advisor?view=sql-server-ver17#database-engine-tuning-advisor-benefits)
  2. [DTA Components and Concepts](https://learn.microsoft.com/en-us/sql/relational-databases/performance/database-engine-tuning-advisor?view=sql-server-ver17#dta-components-and-concepts)
  3. [Limitations and Restrictions](https://learn.microsoft.com/en-us/sql/relational-databases/performance/database-engine-tuning-advisor?view=sql-server-ver17#limitations-and-restrictions)
  4. [Performance Considerations](https://learn.microsoft.com/en-us/sql/relational-databases/performance/database-engine-tuning-advisor?view=sql-server-ver17#performance-considerations)
  5. [Dependency on xp_msver extended stored procedure](https://learn.microsoft.com/en-us/sql/relational-databases/performance/database-engine-tuning-advisor?view=sql-server-ver17#dependency-on-xp_msver-extended-stored-procedure)
  6. [Database Engine Tuning Advisor tasks](https://learn.microsoft.com/en-us/sql/relational-databases/performance/database-engine-tuning-advisor?view=sql-server-ver17#database-engine-tuning-advisor-tasks)

Show 2 more
**Applies to:** ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to)
The Microsoft Database Engine Tuning Advisor (DTA) analyzes databases and makes recommendations that you can use to optimize query performance. You can use the Database Engine Tuning Advisor to select and create an optimal set of indexes, indexed views, or table partitions without having an expert understanding of the database structure or the internals of SQL Server. Using the DTA, you can perform the following tasks:
  * Troubleshoot the performance of a specific problem query
  * Tune a large set of queries across one or more databases
  * Perform an exploratory what-if analysis of potential physical design changes
  * Manage storage space


The Database Engine Tuning Advisor is not supported for Azure SQL Database or Azure SQL Managed Instance. Instead, consider the strategies recommended in [Monitoring and performance tuning in Azure SQL Database and Azure SQL Managed Instance](https://learn.microsoft.com/en-us/azure/azure-sql/database/monitor-tune-overview). For Azure SQL Database, see also the [Database Advisor performance recommendations for Azure SQL Database](https://learn.microsoft.com/en-us/azure/azure-sql/database/database-advisor-implement-performance-recommendations).
[](https://learn.microsoft.com/en-us/sql/relational-databases/performance/database-engine-tuning-advisor?view=sql-server-ver17#database-engine-tuning-advisor-benefits)
## Database Engine Tuning Advisor benefits
Optimizing query performance can be difficult without a full understanding the database structure and the queries that are run against the database. The **Database Engine Tuning Advisor (DTA)** can make this task easier by analyzing the current query plan cache or by analyzing a workload of Transact-SQL queries that you create and recommending an appropriate physical design. For more advanced database administrators, DTA exposes a powerful mechanism to perform exploratory what-if analysis of different physical design alternatives. The DTA can provide the following information.
  * Recommend the best mix of rowstore and [columnstore](https://learn.microsoft.com/en-us/sql/relational-databases/performance/columnstore-index-recommendations-in-database-engine-tuning-advisor-dta?view=sql-server-ver17) indexes for databases by using the query optimizer to analyze queries in a workload.
  * Recommend aligned or non-aligned partitions for databases referenced in a workload.
  * Recommend indexed views for databases referenced in a workload.
  * Analyze the effects of the proposed changes, including index usage, query distribution among tables, and query performance in the workload.
  * Recommend ways to tune the database for a small set of problem queries.
  * Allow you to customize the recommendation by specifying advanced options such as disk space constraints.
  * Provide reports that summarize the effects of implementing the recommendations for a given workload.
  * Consider alternatives in which you supply possible design choices in the form of hypothetical configurations for Database Engine Tuning Advisor to evaluate.
  * Tune workloads from a variety of sources including SQL Server Query Store, Plan Cache, SQL Server Profiler Trace file or table, or a .SQL file.


The Database Engine Tuning Advisor is designed to handle the following types of query workloads:
  * Online transaction processing (OLTP) queries only
  * Online analytical processing (OLAP) queries only
  * Mixed OLTP and OLAP queries
  * Query-heavy workloads (more queries than data modifications)
  * Update-heavy workloads (more data modifications than queries)


[](https://learn.microsoft.com/en-us/sql/relational-databases/performance/database-engine-tuning-advisor?view=sql-server-ver17#dta-components-and-concepts)
## DTA Components and Concepts
**Database Engine Tuning Advisor Graphical User Interface**
An easy-to-use interface in which you can specify the workload and select various tuning options.
**dta** Utility
The command prompt version of Database Engine Tuning Advisor. The **dta** utility is designed to allow you to use Database Engine Tuning Advisor functionality in applications and scripts.
**workload**
A Transact-SQL script file, trace file, or trace table that contains a representative workload for the databases you want to tune. Beginning with SQL Server 2012 (11.x), you can specify the plan cache as the workload. Beginning with SQL Server 2016 (13.x), you can [specify the Query Store as the workload](https://learn.microsoft.com/en-us/sql/relational-databases/performance/tuning-database-using-workload-from-query-store?view=sql-server-ver17).
**XML input file**
A XML-formatted file that Database Engine Tuning Advisor can use to tune workloads. The XML input file supports advanced tuning options that are not available in either the GUI or **dta** utility.
[](https://learn.microsoft.com/en-us/sql/relational-databases/performance/database-engine-tuning-advisor?view=sql-server-ver17#limitations-and-restrictions)
## Limitations and Restrictions
The Database Engine Tuning Advisor has the following limitations and restrictions.
  * It cannot add or drop unique indexes or indexes that enforce `PRIMARY KEY` or `UNIQUE` constraints.
  * It cannot analyze a database that is set to single-user mode.
  * If you specify a maximum disk space for tuning recommendations that exceeds the actual available space, Database Engine Tuning Advisor uses the value you specify. However, when you execute the recommendation script to implement it, the script may fail if more disk space is not added first. Maximum disk space can be specified with the **-B** option of the **dta** utility, or by entering a value in the **Advanced Tuning Options** dialog box.
  * For security reasons, Database Engine Tuning Advisor cannot tune a workload in a trace table that resides on a remote server. To work around this limitation, you can use a trace file instead of a trace table or copy the trace table to the remote server.
  * When you impose constraints, such as those imposed when you specify a maximum disk space for tuning recommendations (by using the **-B** option or the **Advanced Tuning Options** dialog box), Database Engine Tuning Advisor may be forced to drop certain existing indexes. In this case, the resulting Database Engine Tuning Advisor recommendation may produce a negative expected improvement.
  * When you specify a constraint to limit tuning time (by using the **-A** option with the **dta** utility or by checking **Limit tuning time** on the **Tuning Options** tab), Database Engine Tuning Advisor may exceed that time limit to produce an accurate expected improvement and the analysis reports for whatever portion of the workload has been consumed so far.
  * Database Engine Tuning Advisor might not make recommendations under the following circumstances:
    1. The table being tuned contains less than 10 data pages.
    2. The recommended indexes would not offer enough improvement in query performance over the current physical database design.
    3. The user who runs Database Engine Tuning Advisor is not a member of the **db_owner** database role or the **sysadmin** fixed server role. The queries in the workload are analyzed in the security context of the user who runs the Database Engine Tuning Advisor. The user must be a member of the **db_owner** database role.
  * Database Engine Tuning Advisor stores tuning session data and other information in the `msdb` database. If changes are made to the `msdb` database, you may risk losing tuning session data. To eliminate this risk, implement an appropriate backup strategy for the `msdb` database.


[](https://learn.microsoft.com/en-us/sql/relational-databases/performance/database-engine-tuning-advisor?view=sql-server-ver17#performance-considerations)
## Performance Considerations
Database Engine Tuning Advisor can consume significant processor and memory resources during analysis. To avoid slowing down your production server, follow one of these strategies:
  * Tune your databases when your server is free. Database Engine Tuning Advisor can affect maintenance task performance.
  * Use the test server/production server feature. For more information, see [Reduce the Production Server Tuning Load](https://learn.microsoft.com/en-us/sql/relational-databases/performance/reduce-the-production-server-tuning-load?view=sql-server-ver17).
  * Specify only the physical database design structures you want Database Engine Tuning Advisor to analyze. Database Engine Tuning Advisor provides many options, but specifies only those that are necessary.


[](https://learn.microsoft.com/en-us/sql/relational-databases/performance/database-engine-tuning-advisor?view=sql-server-ver17#dependency-on-xp_msver-extended-stored-procedure)
## Dependency on xp_msver extended stored procedure
Database Engine Tuning Advisor depends on the **xp_msver** extended stored procedure to provide full functionality. This extended stored procedure is turned on by default. Database Engine Tuning Advisor uses this extended stored procedure to fetch the number of processors and available memory on the computer where the database that you are tuning resides. If **xp_msver** is unavailable, Database Engine Tuning Advisor assumes the hardware characteristics of the computer where Database Engine Tuning Advisor is running. If the hardware characteristics of the computer where Database Engine Tuning Advisor is running are not available, one processor and 1024 megabytes (MBs) of memory are assumed.
This dependency affects partitioning recommendations because the number of partitions recommended depends on these two values (number of processors and available memory). The dependency also affects your tuning results when you use a test server to tune your production server. In this scenario, Database Engine Tuning Advisor uses **xp_msver** to fetch hardware properties from the production server. After tuning the workload on the test server, Database Engine Tuning Advisor uses these hardware properties to generate a recommendation. For more information, see [xp_msver (Transact-SQL)](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/xp-msver-transact-sql?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/relational-databases/performance/database-engine-tuning-advisor?view=sql-server-ver17#database-engine-tuning-advisor-tasks)
## Database Engine Tuning Advisor tasks
The following table lists common Database Engine Tuning Advisor tasks and the articles that describe how to perform them.
Expand table
Database Engine Tuning Advisor task | article
---|---
Initialize and start the Database Engine Tuning Advisor.

Create a workload by specifying the plan cache, by creating a script, or by generating a trace file or trace table.

Tune a database by using the Database Engine Tuning Advisor graphical user interface tool.

Create XML input files to tune workloads.

View descriptions of the Database Engine Tuning Advisor user interface options. | [Start and Use the Database Engine Tuning Advisor](https://learn.microsoft.com/en-us/sql/relational-databases/performance/start-and-use-the-database-engine-tuning-advisor?view=sql-server-ver17)
View the results of the database tuning operation.

Select and implement tuning recommendations.

Perform what-if exploratory analysis against the workload.

Review existing tuning sessions, clone sessions based on existing ones
or edit existing tuning recommendations for further evaluation or implementation.

View descriptions of the Database Engine Tuning Advisor user interface options. | [View and Work with the Output from the Database Engine Tuning Advisor](https://learn.microsoft.com/en-us/sql/relational-databases/performance/view-and-work-with-the-output-from-the-database-engine-tuning-advisor?view=sql-server-ver17)
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
  * [ Start and Use the Database Engine Tuning Advisor - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/performance/start-and-use-the-database-engine-tuning-advisor?source=recommendations)
Learn how to start and use Database Engine Tuning Advisor in SQL Server to create workloads, tune databases, and create XML input files.
  * [ Output from DTA - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/performance/view-and-work-with-the-output-from-the-database-engine-tuning-advisor?source=recommendations)
Learn about how to use the summaries, recommendations, reports, and tuning logs that the Database Engine Tuning Advisor creates in your SQL Server installation.
  * [ Tuning Database Using Workload from Query Store - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/performance/tuning-database-using-workload-from-query-store?source=recommendations)
The Database Engine Tuning Advisor supports the option to use the Query Store to automatically select an appropriate workload for tuning.
  * [ Performance Monitoring and Tuning Tools - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/performance/performance-monitoring-and-tuning-tools?source=recommendations)
Learn about SQL Server monitoring and tuning tools and how to choose the right one depending on the type of monitoring and the events to monitor.
  * [ Monitor and Tune for Performance - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitor-and-tune-for-performance?source=recommendations)
Learn about monitoring databases to assess server performance, using periodic snapshots and gathering data continuously to track performance trends.
  * [ Columnstore index recommendations-Database Engine Tuning Advisor (DTA) - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/performance/columnstore-index-recommendations-in-database-engine-tuning-advisor-dta?source=recommendations)
Learn how the Database Engine Tuning Advisor can analyze your workload and recommend rowstore and columnstore indexes to build on the database in SQL Server.
  * [ Live Query Statistics - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/performance/live-query-statistics?source=recommendations)
Learn how to view the live execution plan of an active query in SQL Server Management Studio. Use the execution statistics to debug query performance issues.
  * [ Database Engine Tuning Advisor (DTA) Command-Line Utility - SQL Server ](https://learn.microsoft.com/en-us/sql/tools/dta/dta-utility?source=recommendations)
The dta utility is a command prompt version of Database Engine Tuning Advisor that allows you to use functionality in applications and scripts.


Show 5 more
Certification
[ Microsoft Certified: Azure Database Administrator Associate - Certifications ](https://learn.microsoft.com/en-us/credentials/certifications/azure-database-administrator-associate/?source=recommendations)
Administer an SQL Server database infrastructure for cloud, on-premises and hybrid relational databases using the Microsoft PaaS relational database offerings.
Mar 8, 4 PM - Mar 8, 4 PM
Experiment with what's next in AI-driven apps and agent design
* * *
  * Last updated on 08/27/2024


##  In this article
  1. [Database Engine Tuning Advisor benefits](https://learn.microsoft.com/en-us/sql/relational-databases/performance/database-engine-tuning-advisor?view=sql-server-ver17#database-engine-tuning-advisor-benefits)
  2. [DTA Components and Concepts](https://learn.microsoft.com/en-us/sql/relational-databases/performance/database-engine-tuning-advisor?view=sql-server-ver17#dta-components-and-concepts)
  3. [Limitations and Restrictions](https://learn.microsoft.com/en-us/sql/relational-databases/performance/database-engine-tuning-advisor?view=sql-server-ver17#limitations-and-restrictions)
  4. [Performance Considerations](https://learn.microsoft.com/en-us/sql/relational-databases/performance/database-engine-tuning-advisor?view=sql-server-ver17#performance-considerations)
  5. [Dependency on xp_msver extended stored procedure](https://learn.microsoft.com/en-us/sql/relational-databases/performance/database-engine-tuning-advisor?view=sql-server-ver17#dependency-on-xp_msver-extended-stored-procedure)
  6. [Database Engine Tuning Advisor tasks](https://learn.microsoft.com/en-us/sql/relational-databases/performance/database-engine-tuning-advisor?view=sql-server-ver17#database-engine-tuning-advisor-tasks)


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
[ Sign in ](https://learn.microsoft.com/en-us/sql/relational-databases/performance/database-engine-tuning-advisor?view=sql-server-ver17)
[English (United States)](https://learn.microsoft.com/en-us/locale?target=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fsql%2Frelational-databases%2Fperformance%2Fdatabase-engine-tuning-advisor%3Fview%3Dsql-server-ver17)
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
