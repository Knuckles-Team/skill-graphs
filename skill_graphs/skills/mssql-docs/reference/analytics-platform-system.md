Version Analytics Platform System 2016-AU7
  * Analytics Platform System (PDW)
    * [2016-AU7](https://learn.microsoft.com/en-us/sql/analytics-platform-system/home-analytics-platform-system-aps-pdw?view=aps-pdw-2016-au7)
    * [2016-AU6](https://learn.microsoft.com/en-us/sql/analytics-platform-system/home-analytics-platform-system-aps-pdw?view=aps-pdw-2016)
  * [Azure SQL Database](https://learn.microsoft.com/en-us/sql/analytics-platform-system/home-analytics-platform-system-aps-pdw?view=azuresqldb-current)
  * [Azure SQL Managed Instance](https://learn.microsoft.com/en-us/sql/analytics-platform-system/home-analytics-platform-system-aps-pdw?view=azuresqldb-mi-current)
  * [Azure Synapse Analytics](https://learn.microsoft.com/en-us/sql/analytics-platform-system/home-analytics-platform-system-aps-pdw?view=azure-sqldw-latest)
  * [Fabric Data Warehouse](https://learn.microsoft.com/en-us/sql/analytics-platform-system/home-analytics-platform-system-aps-pdw?view=fabric)
  * [Fabric SQL database](https://learn.microsoft.com/en-us/sql/analytics-platform-system/home-analytics-platform-system-aps-pdw?view=fabric-sqldb)
  * SQL Server
    * [2025](https://learn.microsoft.com/en-us/sql/analytics-platform-system/home-analytics-platform-system-aps-pdw?view=sql-server-ver17)
    * [2022](https://learn.microsoft.com/en-us/sql/analytics-platform-system/home-analytics-platform-system-aps-pdw?view=sql-server-ver16)
    * [2019](https://learn.microsoft.com/en-us/sql/analytics-platform-system/home-analytics-platform-system-aps-pdw?view=sql-server-ver15)
    * [2017](https://learn.microsoft.com/en-us/sql/analytics-platform-system/home-analytics-platform-system-aps-pdw?view=sql-server-2017)
    * [2016](https://learn.microsoft.com/en-us/sql/analytics-platform-system/home-analytics-platform-system-aps-pdw?view=sql-server-2016)
  * SQL Server on Linux
    * [2025](https://learn.microsoft.com/en-us/sql/analytics-platform-system/home-analytics-platform-system-aps-pdw?view=sql-server-linux-ver17)
    * [2022](https://learn.microsoft.com/en-us/sql/analytics-platform-system/home-analytics-platform-system-aps-pdw?view=sql-server-linux-ver16)
    * [2019](https://learn.microsoft.com/en-us/sql/analytics-platform-system/home-analytics-platform-system-aps-pdw?view=sql-server-linux-ver15)
    * [2017](https://learn.microsoft.com/en-us/sql/analytics-platform-system/home-analytics-platform-system-aps-pdw?view=sql-server-linux-2017)


Search
Suggestions will filter as you type
  * [SQL Server >>](https://learn.microsoft.com/en-us/sql/sql-server/?view=aps-pdw-2016-au7)
  * [Overview of APS](https://learn.microsoft.com/en-us/sql/analytics-platform-system/home-analytics-platform-system-aps-pdw?view=aps-pdw-2016-au7)


Download PDF
Table of contents  Exit editor mode
  1. [ Learn ](https://learn.microsoft.com/en-us/?view=aps-pdw-2016-au7)
  2. [ SQL ](https://learn.microsoft.com/en-us/sql/?view=aps-pdw-2016-au7)
  3. [ Analytics Platform System ](https://learn.microsoft.com/en-us/sql/analytics-platform-system/?view=aps-pdw-2016-au7)


  1. [Learn](https://learn.microsoft.com/en-us/?view=aps-pdw-2016-au7)
  2. [SQL](https://learn.microsoft.com/en-us/sql/?view=aps-pdw-2016-au7)
  3. [Analytics Platform System](https://learn.microsoft.com/en-us/sql/analytics-platform-system/?view=aps-pdw-2016-au7)


Ask Learn Ask Learn Focus mode
Table of contents [ Read in English ](https://learn.microsoft.com/en-us/sql/analytics-platform-system/home-analytics-platform-system-aps-pdw?view=aps-pdw-2016-au7) Add to Collections Add to plan
* * *
#### Share via
* * *
Copy Markdown Print
* * *
Note
Access to this page requires authorization. You can try [signing in](https://learn.microsoft.com/en-us/sql/analytics-platform-system/home-analytics-platform-system-aps-pdw?view=aps-pdw-2016-au7) or changing directories.
Access to this page requires authorization. You can try changing directories.
# Microsoft Analytics Platform System
Feedback
Summarize this article for me
##  In this article
  1. [Parallel Data Warehouse, software designed for massively parallel processing](https://learn.microsoft.com/en-us/sql/analytics-platform-system/home-analytics-platform-system-aps-pdw?view=aps-pdw-2016-au7#parallel-data-warehouse-software-designed-for-massively-parallel-processing)
  2. [T-SQL support](https://learn.microsoft.com/en-us/sql/analytics-platform-system/home-analytics-platform-system-aps-pdw?view=aps-pdw-2016-au7#t-sql-support)


Microsoft Analytics Platform System (APS), a data platform designed for data warehousing and Big Data analytics, offers deep data integration, high-speed query processing, highly scalable storage, and simple maintenance for your end-to-end business intelligence solutions.
![Appliance architecture](https://learn.microsoft.com/en-us/sql/analytics-platform-system/media/architecture-high-level.png?view=aps-pdw-2016-au7)
Analytics Platform System hosts SQL Server Parallel Data Warehouse (PDW), which is the software that runs the massively parallel processing (MPP) data warehouse.
PolyBase technology combines relational PDW data with Hadoop data from multiple sources including Hortonworks on Windows Server, Hortonworks on Linux, Cloudera on Linux and HDInsight's Azure Blob Storage. These advanced data integration abilities, plus deep integration with Business Intelligence tools, allow Analytics Platform System to return integrated analysis that enables your business decision makers to make better and more insightful business decisions.
Analytics Platform System ships to your data center as an appliance with hardware and software pre-installed and pre-configured to run multiple workloads. When you purchase Analytics Platform System, you purchase Compute nodes for PDW according to your business requirements.
Analytics Platform System is not only fast and scalable, it is designed with high redundancy and high availability, making it a reliable platform you can trust with your most business critical data. Analytics Platform System is designed for simplicity which makes it easy to learn and to manage. PDW's PolyBase technology for analyzing Hadoop data, and its deep integration with Business Intelligence tools make it a comprehensive platform for building end-to- end solutions.
[](https://learn.microsoft.com/en-us/sql/analytics-platform-system/home-analytics-platform-system-aps-pdw?view=aps-pdw-2016-au7#parallel-data-warehouse-software-designed-for-massively-parallel-processing)
## Parallel Data Warehouse, software designed for massively parallel processing
Use PDW as the core relational data warehousing component of your end-to-end business intelligence solutions. With PDW's massively parallel processing (MPP) design, queries commonly complete 50 times faster than traditional data warehouses built on symmetric multi-processing (SMP) database management systems.
50 times faster means that queries complete in minutes instead of hours, or seconds instead of minutes. With this breakthrough performance, your business analysts can generate more extensive results faster, and can easily perform ad hoc queries or drill down into the details. As a result, your business can make better decisions, faster.
In addition to achieving breakthrough query performance, PDW makes it easy to:
  * Grow your data warehouse to anywhere from a few terabytes to over 6 petabytes of data in a single appliance by adding "scale units" to your existing system.
  * Trust your data will be there when you need it because of the built-in high redundancy and high availability.
  * Solve modern data challenges of loading and consolidating data.
  * Integrate Hadoop data with relational data for fast analysis by using PDW's highly parallelized PolyBase technology.
  * Use Business Intelligence tools to build comprehensive end-to-end solutions.


[](https://learn.microsoft.com/en-us/sql/analytics-platform-system/home-analytics-platform-system-aps-pdw?view=aps-pdw-2016-au7#t-sql-support)
## T-SQL support
To view T-SQL reference articles for PDW, select the **Analytics Platform System (PDW)** product version from the version dropdown list.
![Screenshot from learn.microsoft.com of the product Version selector.](https://learn.microsoft.com/en-us/sql/analytics-platform-system/media/version-selector.png?view=aps-pdw-2016-au7)
For example, view the APS version of the [Collations and Unicode Support](https://learn.microsoft.com/en-us/sql/t-sql/statements/collations?view=aps-pdw-2016-au7&preserve-view=true) document.
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
  * [ How to Contribute to SQL Server Documentation - SQL Server ](https://learn.microsoft.com/en-us/sql/sql-server/sql-server-docs-contribute?source=recommendations)
How to contribute to SQL Server Documentation


Module
[ Explore Fundamentals Of Large-Scale Data Analytics - Training ](https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/?source=recommendations)
Organizations use analytics platforms to build large scale data analytics solutions that generate insights and drive success. Microsoft provides multiple technologies that you can combine to build a large scale data analytics solution.
Mar 8, 4 PM - Mar 8, 4 PM
Experiment with what's next in AI-driven apps and agent design
* * *
  * Last updated on 02/10/2026


Ask Learn is an AI assistant that can answer questions, clarify concepts, and define terms using trusted Microsoft documentation.
Please sign in to use Ask Learn.
[ Sign in ](https://learn.microsoft.com/en-us/sql/analytics-platform-system/home-analytics-platform-system-aps-pdw?view=aps-pdw-2016-au7)
