# Monitor and Tune for Performance
Feedback
Summarize this article for me
##  In this article
  1. [Monitor and tuning databases for performance](https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitor-and-tune-for-performance?view=sql-server-ver17#monitor-and-tuning-databases-for-performance)
  2. [Monitor in a dynamic environment](https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitor-and-tune-for-performance?view=sql-server-ver17#monitor-in-a-dynamic-environment)
  3. [Monitor and performance tuning tasks](https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitor-and-tune-for-performance?view=sql-server-ver17#monitor-and-performance-tuning-tasks)
  4. [Related content](https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitor-and-tune-for-performance?view=sql-server-ver17#related-content)


**Applies to:** ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure SQL Database](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure SQL Managed Instance](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL database in Microsoft Fabric](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to)
The goal of monitoring databases is to assess how a server is performing. Effective monitoring involves taking periodic snapshots of current performance to isolate processes that are causing problems, and gathering data continuously over time to track performance trends.
Ongoing evaluation of the database performance helps you minimize response times and maximize throughput, yielding optimal performance. Efficient network traffic, disk I/O, and CPU usage are key to peak performance. You need to thoroughly analyze the application requirements, understand the logical and physical structure of the data, assess database usage, and negotiate tradeoffs between conflicting uses such as online transaction processing (OLTP) versus decision support.
[](https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitor-and-tune-for-performance?view=sql-server-ver17#monitor-and-tuning-databases-for-performance)
## Monitor and tuning databases for performance
Microsoft SQL Server and the Microsoft Windows operating system provide utilities to view the current condition of the database and track performance as conditions change. There are a variety of tools and techniques you can use to monitor Microsoft SQL Server. Monitoring SQL Server helps you:
  * Determine whether you can improve performance. For example, by monitoring the response times for frequently used queries, you can determine whether changes to the query or indexes on the tables are required.
  * Evaluate user activity. For example, by monitoring users trying to connect to an instance of SQL Server, you can determine whether security is set up adequately and test applications or development systems. For example, by monitoring SQL queries as they are executed, you can determine whether they are written correctly and producing the expected results.
  * Troubleshoot problems or debug application components, such as stored procedures.


[](https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitor-and-tune-for-performance?view=sql-server-ver17#monitor-in-a-dynamic-environment)
## Monitor in a dynamic environment
Changing conditions result in changing performance. In your evaluations, you can see performance changes as the number of users increases, user access and connection methods change, database contents grow, client applications change, data in the applications changes, queries become more complex, and network traffic rises. Using tools to monitor performance helps you associate changes in performance with changing conditions and complex queries. **Examples:**
  * By monitoring the response times for frequently used queries, you can determine whether changes to the query or indexes on the tables where the queries execute are required.
  * By monitoring Transact-SQL queries as they are executed, you can determine whether the queries are written correctly and producing the expected results.
  * By monitoring users that try to connect to an instance of SQL Server, you can determine whether security is set up adequately and test applications or development systems.


Response time is the length of time required for the first row of the result set to be returned to the user in the form of visual confirmation that a query is being processed. Throughput is the total number of queries handled by the server during a specified period of time.
As the number of users increases, so does the competition for a server's resources, which in turn increases response time and decreases overall throughput.
[](https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitor-and-tune-for-performance?view=sql-server-ver17#monitor-and-performance-tuning-tasks)
## Monitor and performance tuning tasks
Expand table
Topic | Task
---|---
[Monitor SQL Server Components](https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitor-sql-server-components?view=sql-server-ver17) | Required steps to monitor any SQL Server component, such as Activity Monitor, Extended Events, and Dynamic Management Views and Functions, etc.
[Performance monitoring and tuning tools](https://learn.microsoft.com/en-us/sql/relational-databases/performance/performance-monitoring-and-tuning-tools?view=sql-server-ver17) | Lists the monitoring and tuning tools available with SQL Server, such as Live Query Statistics, and the Database Engine Tuning Advisor.
[Upgrade databases using the Query Tuning Assistant](https://learn.microsoft.com/en-us/sql/relational-databases/performance/upgrade-dbcompat-using-qta?view=sql-server-ver17) | Keep workload performance stability during the upgrade to newer database compatibility level.
[Monitor performance by using the Query Store](https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitoring-performance-by-using-the-query-store?view=sql-server-ver17) | Use Query Store to automatically capture a history of queries, plans, and runtime statistics, and retain these for your review.
[Establish a Performance Baseline](https://learn.microsoft.com/en-us/sql/relational-databases/performance/establish-a-performance-baseline?view=sql-server-ver17) | How to establish a performance baseline.
[Isolate Performance Problems](https://learn.microsoft.com/en-us/sql/relational-databases/performance/isolate-performance-problems?view=sql-server-ver17) | Isolate database performance problems.
[Identify Bottlenecks](https://learn.microsoft.com/en-us/sql/relational-databases/performance/identify-bottlenecks?view=sql-server-ver17) | Monitor and track server performance to identify bottlenecks.
[Use DMVs to Determine Usage Statistics and Performance of Views](https://learn.microsoft.com/en-us/sql/relational-databases/performance/use-dmvs-determine-usage-performance-views?view=sql-server-ver17) | Covers methodology and scripts used to get information about the performance of queries.
[Server Performance and Activity Monitoring](https://learn.microsoft.com/en-us/sql/relational-databases/performance/server-performance-and-activity-monitoring?view=sql-server-ver17) | Use SQL Server and Windows performance and activity monitoring tools.
[Monitor Resource Usage (Performance Monitor)](https://learn.microsoft.com/en-us/sql/relational-databases/performance-monitor/monitor-resource-usage-system-monitor?view=sql-server-ver17) | Using System Monitor (also known as perfmon) to measure the performance of SQL Server using performance counters.
[](https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitor-and-tune-for-performance?view=sql-server-ver17#related-content)
## Related content
  * [Automated Administration Across an Enterprise](https://learn.microsoft.com/en-us/ssms/agent/automated-administration-across-an-enterprise)
  * [Compare and Analyze Execution Plans](https://learn.microsoft.com/en-us/sql/relational-databases/performance/compare-and-analyze-execution-plans?view=sql-server-ver17)
  * [Display and save execution plans](https://learn.microsoft.com/en-us/sql/relational-databases/performance/display-and-save-execution-plans?view=sql-server-ver17)


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
  * [ Performance Dashboard - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/performance/performance-dashboard?source=recommendations)
Learn about SQL Server Management Studio Performance Dashboard, which provides fast insight into SQL Server and Azure SQL Managed Instance.
  * [ Performance Monitoring and Tuning Tools - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/performance/performance-monitoring-and-tuning-tools?source=recommendations)
Learn about SQL Server monitoring and tuning tools and how to choose the right one depending on the type of monitoring and the events to monitor.
  * [ Live Query Statistics - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/performance/live-query-statistics?source=recommendations)
Learn how to view the live execution plan of an active query in SQL Server Management Studio. Use the execution statistics to debug query performance issues.
  * [ Monitor SQL Server Components - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitor-sql-server-components?source=recommendations)
Learn how monitoring lets you identify performance trends. SQL Server provides a service in a dynamic environment, so changes may be necessary over time.
  * [ Server Performance and Activity Monitoring - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/performance/server-performance-and-activity-monitoring?source=recommendations)
Use these resources to learn how to use SQL Server and Windows performance and activity monitoring tools to assess how a server is performing.
  * [ Identify Bottlenecks - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/performance/identify-bottlenecks?source=recommendations)
Learn about the causes of bottlenecks, such as insufficient resources and malfunctioning/incorrectly configured resources in SQL Server.
  * [ Establish a Performance Baseline - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/performance/establish-a-performance-baseline?source=recommendations)
Take performance measurements at regular intervals over time, even when no problems occur, to establish a server performance baseline in SQL Server.


Show 4 more
Module
[ Describe performance monitoring - Training ](https://learn.microsoft.com/en-us/training/modules/describe-performance-monitoring/?source=recommendations)
Describe performance monitoring
Certification
[ Microsoft Certified: Azure Database Administrator Associate - Certifications ](https://learn.microsoft.com/en-us/credentials/certifications/azure-database-administrator-associate/?source=recommendations)
Administer an SQL Server database infrastructure for cloud, on-premises and hybrid relational databases using the Microsoft PaaS relational database offerings.
Mar 8, 4 PM - Mar 8, 4 PM
Experiment with what's next in AI-driven apps and agent design
* * *
  * Last updated on 11/18/2025


##  In this article
  1. [Monitor and tuning databases for performance](https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitor-and-tune-for-performance?view=sql-server-ver17#monitor-and-tuning-databases-for-performance)
  2. [Monitor in a dynamic environment](https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitor-and-tune-for-performance?view=sql-server-ver17#monitor-in-a-dynamic-environment)
  3. [Monitor and performance tuning tasks](https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitor-and-tune-for-performance?view=sql-server-ver17#monitor-and-performance-tuning-tasks)
  4. [Related content](https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitor-and-tune-for-performance?view=sql-server-ver17#related-content)


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
[ Sign in ](https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitor-and-tune-for-performance?view=sql-server-ver17)
[English (United States)](https://learn.microsoft.com/en-us/locale?target=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fsql%2Frelational-databases%2Fperformance%2Fmonitor-and-tune-for-performance%3Fview%3Dsql-server-ver17)
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
