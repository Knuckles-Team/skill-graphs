# What is SQL Server?
Feedback
Summarize this article for me
##  In this article
  1. [Deployment options](https://learn.microsoft.com/en-us/sql/sql-server/what-is-sql-server?view=sql-server-ver17#deployment-options)
  2. [SQL Server components and technologies](https://learn.microsoft.com/en-us/sql/sql-server/what-is-sql-server?view=sql-server-ver17#sql-server-components-and-technologies)
  3. [Fundamental concepts](https://learn.microsoft.com/en-us/sql/sql-server/what-is-sql-server?view=sql-server-ver17#fundamental-concepts)
  4. [Connect to SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/what-is-sql-server?view=sql-server-ver17#connect-to-sql-server)
  5. [Azure integration](https://learn.microsoft.com/en-us/sql/sql-server/what-is-sql-server?view=sql-server-ver17#azure-integration)
  6. [Migrate and move data](https://learn.microsoft.com/en-us/sql/sql-server/what-is-sql-server?view=sql-server-ver17#migrate-and-move-data)
  7. [Update your version of SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/what-is-sql-server?view=sql-server-ver17#update-your-version-of-sql-server)
  8. [Samples](https://learn.microsoft.com/en-us/sql/sql-server/what-is-sql-server?view=sql-server-ver17#samples)
  9. [Get help](https://learn.microsoft.com/en-us/sql/sql-server/what-is-sql-server?view=sql-server-ver17#-get-help)
  10. [Contribute to SQL documentation](https://learn.microsoft.com/en-us/sql/sql-server/what-is-sql-server?view=sql-server-ver17#-contribute-to-sql-documentation)
  11. [Related content](https://learn.microsoft.com/en-us/sql/sql-server/what-is-sql-server?view=sql-server-ver17#related-content)

Show 7 more
**Applies to:** ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to)
Microsoft SQL Server is a relational database management system (RDBMS). Applications and tools connect to a SQL Server _instance_ or _database_ , and communicate using [Transact-SQL](https://learn.microsoft.com/en-us/sql/t-sql/language-reference?view=sql-server-ver17) (T-SQL).
[](https://learn.microsoft.com/en-us/sql/sql-server/what-is-sql-server?view=sql-server-ver17#deployment-options)
## Deployment options
You can install SQL Server on Windows or [Linux](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-overview?view=sql-server-ver17), deploy it in [a Linux container](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-overview?view=sql-server-ver17#container-images), or deploy it on [Azure Virtual Machines](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/sql-server-on-azure-vm-iaas-what-is-overview) or other virtual machine platform. You previously might have referred to this as the _boxed product_.
Supported versions of SQL Server depend on your license agreement, but for the purposes of this documentation, we mean SQL Server 2016 (13.x) and later versions. Documentation for SQL Server 2014 (12.x) and previous versions is available at [Previous versions of SQL Server documentation](https://learn.microsoft.com/en-us/sql/sql-server/previous-versions-sql-server?view=sql-server-ver17). To find out which versions of SQL Server are currently supported, see [SQL Server end of support options](https://learn.microsoft.com/en-us/sql/sql-server/end-of-support/sql-server-end-of-support-overview?view=sql-server-ver17).
The underlying SQL Server Database Engine is also used by the following products and services:
  * [Azure SQL Database](https://learn.microsoft.com/en-us/azure/azure-sql/database/sql-database-paas-overview)
  * [Azure SQL Managed Instance](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/sql-managed-instance-paas-overview)
  * [Microsoft Analytics Platform System](https://learn.microsoft.com/en-us/sql/analytics-platform-system/home-analytics-platform-system-aps-pdw?view=sql-server-ver17) (PDW)
  * [Azure Synapse Analytics](https://learn.microsoft.com/en-us/azure/synapse-analytics/overview-what-is)
  * [Azure SQL Edge](https://learn.microsoft.com/en-us/azure/azure-sql-edge/overview)


For a list of features supported by the editions of SQL Server on Windows, see:
  * [Editions and supported features of SQL Server 2025](https://learn.microsoft.com/en-us/sql/sql-server/editions-and-components-of-sql-server-2025?view=sql-server-ver17)
  * [Editions and supported features of SQL Server 2022](https://learn.microsoft.com/en-us/sql/sql-server/editions-and-components-of-sql-server-2022?view=sql-server-ver17)
  * [Editions and supported features of SQL Server 2019](https://learn.microsoft.com/en-us/sql/sql-server/editions-and-components-of-sql-server-2019?view=sql-server-ver17)
  * [Editions and supported features of SQL Server 2017](https://learn.microsoft.com/en-us/sql/sql-server/editions-and-components-of-sql-server-2017?view=sql-server-ver17)
  * [Editions and supported features of SQL Server 2016](https://learn.microsoft.com/en-us/sql/sql-server/editions-and-components-of-sql-server-2016?view=sql-server-ver17)


[](https://learn.microsoft.com/en-us/sql/sql-server/what-is-sql-server?view=sql-server-ver17#sql-server-components-and-technologies)
## SQL Server components and technologies
This section describes some of the key technologies available in SQL Server.
Expand table
Component | Description
---|---
**Database Engine** | The Database Engine is the core service for storing, processing, and securing data. The Database Engine provides controlled access and transaction processing to meet the requirements of the most demanding data consuming applications within your enterprise. The Database Engine also provides rich support for sustaining business continuity through [Business continuity and database recovery](https://learn.microsoft.com/en-us/sql/database-engine/sql-server-business-continuity-dr?view=sql-server-ver17).
**Machine Learning Services (MLS)** |  [SQL Server Machine Learning Services](https://learn.microsoft.com/en-us/sql/machine-learning/sql-server-machine-learning-services?view=sql-server-ver17) supports integration of machine learning, using the popular R and Python languages, into enterprise workflows.

Machine Learning Services (In-Database) integrates R and Python with SQL Server, making it easy to build, retrain, and score models by calling stored procedures. Machine Learning Server provides enterprise-scale support for R and Python, without requiring SQL Server.
**Integration Services (SSIS)** |  [SQL Server Integration Services](https://learn.microsoft.com/en-us/sql/integration-services/sql-server-integration-services?view=sql-server-ver17) is a platform for building high performance data integration solutions, including packages that provide extract, transform, and load (ETL) processing for data warehousing.
**Analysis Services (SSAS)** |  [SQL Server Analysis Services](https://learn.microsoft.com/en-us/analysis-services/ssas-overview) is an analytical data platform and toolset for personal, team, and corporate business intelligence. Servers and client designers support traditional OLAP solutions, new tabular modeling solutions, as well as self-service analytics and collaboration using Power Pivot, Excel, and a SharePoint Server environment. Analysis Services also includes Data Mining so that you can uncover the patterns and relationships hidden inside large volumes of data.
**Reporting Services (SSRS)** |  [SQL Server Reporting Services](https://learn.microsoft.com/en-us/sql/reporting-services/create-deploy-and-manage-mobile-and-paginated-reports?view=sql-server-ver17) delivers enterprise, Web-enabled reporting functionality. You can create reports that draw content from various data sources, publish reports in various formats, and centrally manage security and subscriptions. Starting in SQL Server 2025 (17.x), on-premises reporting services is consolidated under [Power BI Report Server](https://learn.microsoft.com/en-us/power-bi/report-server/get-started). For more information, see [Reporting Services consolidation FAQ](https://learn.microsoft.com/en-us/sql/reporting-services/reporting-services-consolidation-faq?view=sql-server-ver17).
**Replication** |  [SQL Server Replication](https://learn.microsoft.com/en-us/sql/relational-databases/replication/sql-server-replication?view=sql-server-ver17) is a set of technologies for copying and distributing data and database objects from one database to another, and then synchronizing between databases to maintain consistency. By using replication, you can distribute data to different locations and to remote or mobile users with local and wide area networks, dial-up connections, wireless connections, and the Internet.
**Data Quality Services (DQS)** 1 |  [Data Quality Services](https://learn.microsoft.com/en-us/sql/data-quality-services/data-quality-services?view=sql-server-ver17) provides you with a knowledge-driven data cleansing solution. DQS enables you to build a knowledge base, and then use that knowledge base to perform data correction and deduplication on your data, using both computer-assisted and interactive means. You can use cloud-based reference data services, and you can build a data management solution that integrates DQS with SQL Server Integration Services and Master Data Services.
**Master Data Services (MDS)** 1 |  [Master Data Services](https://learn.microsoft.com/en-us/sql/master-data-services/master-data-services-overview-mds?view=sql-server-ver17) is the SQL Server solution for master data management. A solution built on Master Data Services helps ensure that reporting and analysis are based on the right information. Using Master Data Services, you create a central repository for your master data and maintain an auditable, securable record of that data as it changes over time.
1 This feature is [removed](https://learn.microsoft.com/en-us/lifecycle/definitions#removal) in SQL Server 2025 (17.x). We continue to support this feature in SQL Server 2022 (16.x) and earlier versions.
[](https://learn.microsoft.com/en-us/sql/sql-server/what-is-sql-server?view=sql-server-ver17#fundamental-concepts)
## Fundamental concepts
This table provides links to fundamental concepts in SQL Server and Azure SQL.
Expand table
Area | More information
---|---
**Data files** and the **transaction log** | - [Database files and filegroups](https://learn.microsoft.com/en-us/sql/relational-databases/databases/database-files-and-filegroups?view=sql-server-ver17)
- [System Databases](https://learn.microsoft.com/en-us/sql/relational-databases/databases/system-databases?view=sql-server-ver17)
- [The transaction log](https://learn.microsoft.com/en-us/sql/relational-databases/logs/the-transaction-log-sql-server?view=sql-server-ver17)
**Database compatibility levels** | - [Compatibility certification](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/compatibility-certification?view=sql-server-ver17)
- [View or change the compatibility level of a database](https://learn.microsoft.com/en-us/sql/relational-databases/databases/view-or-change-the-compatibility-level-of-a-database?view=sql-server-ver17)
- [ALTER DATABASE (Transact-SQL) compatibility level](https://learn.microsoft.com/en-us/sql/t-sql/statements/alter-database-transact-sql-compatibility-level?view=sql-server-ver17)
**Tables** and **views** | - [Tables](https://learn.microsoft.com/en-us/sql/relational-databases/tables/tables?view=sql-server-ver17)
- [Views](https://learn.microsoft.com/en-us/sql/relational-databases/views/views?view=sql-server-ver17)
**Functions** and **stored procedures** | - [What are the SQL database functions?](https://learn.microsoft.com/en-us/sql/t-sql/functions/functions?view=sql-server-ver17)
- [Stored procedures (Database Engine)](https://learn.microsoft.com/en-us/sql/relational-databases/stored-procedures/stored-procedures-database-engine?view=sql-server-ver17)
**Indexes** | - [Indexes](https://learn.microsoft.com/en-us/sql/relational-databases/indexes/indexes?view=sql-server-ver17)
- [Index architecture and design guide](https://learn.microsoft.com/en-us/sql/relational-databases/sql-server-index-design-guide?view=sql-server-ver17)
Configure **cost threshold for parallelism**
and **maximum degree of parallelism** | - [Server configuration: cost threshold for parallelism](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/configure-the-cost-threshold-for-parallelism-server-configuration-option?view=sql-server-ver17)
- [Server configuration: max degree of parallelism](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/configure-the-max-degree-of-parallelism-server-configuration-option?view=sql-server-ver17)
**Memory management** | - [Server memory configuration options](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/server-memory-server-configuration-options?view=sql-server-ver17)
- [Memory management architecture guide](https://learn.microsoft.com/en-us/sql/relational-databases/memory-management-architecture-guide?view=sql-server-ver17)
**Checkpoints** , **startup** , and **crash recovery** | - [Database checkpoints](https://learn.microsoft.com/en-us/sql/relational-databases/logs/database-checkpoints-sql-server?view=sql-server-ver17)
- [Accelerated database recovery](https://learn.microsoft.com/en-us/sql/relational-databases/accelerated-database-recovery-concepts?view=sql-server-ver17)
**Back up** and **restore** databases | - [Back up and restore of SQL Server databases](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver17)
- [Transaction log backups](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/transaction-log-backups-sql-server?view=sql-server-ver17)
**Manage SQL Server services** | - [Manage the Database Engine services](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/manage-the-database-engine-services?view=sql-server-ver17)
- [SQL Server Configuration Manager](https://learn.microsoft.com/en-us/sql/relational-databases/sql-server-configuration-manager?view=sql-server-ver17)
- [Start, stop, pause, resume, and restart SQL Server services](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/start-stop-pause-resume-restart-sql-server-services?view=sql-server-ver17)
- [Add Features to an Instance of SQL Server (Setup)](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/add-features-to-an-instance-of-sql-server-setup?view=sql-server-ver17)
**Database console commands** (DBCC) | - [DBCC](https://learn.microsoft.com/en-us/sql/t-sql/database-console-commands/dbcc-transact-sql?view=sql-server-ver17)
- [DBCC HELP](https://learn.microsoft.com/en-us/sql/t-sql/database-console-commands/dbcc-help-transact-sql?view=sql-server-ver17)
- [DBCC CHECKDB](https://learn.microsoft.com/en-us/sql/t-sql/database-console-commands/dbcc-checkdb-transact-sql?view=sql-server-ver17)
**High availability** (HA) and **disaster recovery** (DR) | - [Business continuity and database recovery](https://learn.microsoft.com/en-us/sql/database-engine/sql-server-business-continuity-dr?view=sql-server-ver17)
- [About log shipping](https://learn.microsoft.com/en-us/sql/database-engine/log-shipping/about-log-shipping-sql-server?view=sql-server-ver17)
- [Failover Clustering and Always On Availability Groups](https://learn.microsoft.com/en-us/sql/database-engine/availability-groups/windows/failover-clustering-and-always-on-availability-groups-sql-server?view=sql-server-ver17)
- [What is an Always On availability group?](https://learn.microsoft.com/en-us/sql/database-engine/availability-groups/windows/overview-of-always-on-availability-groups-sql-server?view=sql-server-ver17)
**Query processing** and **performance tuning** | - [Tune performance with the Query Store](https://learn.microsoft.com/en-us/sql/relational-databases/performance/tune-performance-with-the-query-store?view=sql-server-ver17)
- [Query processing architecture guide](https://learn.microsoft.com/en-us/sql/relational-databases/query-processing-architecture-guide?view=sql-server-ver17)
- [Optimized locking](https://learn.microsoft.com/en-us/sql/relational-databases/performance/optimized-locking?view=sql-server-ver17)
- [Transaction locking and row versioning guide](https://learn.microsoft.com/en-us/sql/relational-databases/sql-server-transaction-locking-and-row-versioning-guide?view=sql-server-ver17)
[](https://learn.microsoft.com/en-us/sql/sql-server/what-is-sql-server?view=sql-server-ver17#connect-to-sql-server)
## Connect to SQL Server
  * [Connect to the Database Engine](https://learn.microsoft.com/en-us/sql/sql-server/connect-to-database-engine?view=sql-server-ver17)
  * [SQL Server Management Studio (SSMS)](https://learn.microsoft.com/en-us/ssms/sql-server-management-studio-ssms)
  * [MSSQL extension for Visual Studio Code](https://learn.microsoft.com/en-us/sql/tools/visual-studio-code-extensions/mssql/mssql-extension-visual-studio-code?view=sql-server-ver17)


[](https://learn.microsoft.com/en-us/sql/sql-server/what-is-sql-server?view=sql-server-ver17#azure-integration)
## Azure integration
Although SQL Server is a standalone product, which can be installed on computers running Windows and Linux operating systems, you can integrate your SQL Server instances with several Azure services.
[](https://learn.microsoft.com/en-us/sql/sql-server/what-is-sql-server?view=sql-server-ver17#azure-virtual-machines)
### Azure Virtual Machines
[SQL Server on Azure Virtual Machines](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/sql-server-on-azure-vm-iaas-what-is-overview) enables you to use full versions of SQL Server in the cloud without having to manage any on-premises hardware. SQL Server virtual machines (VMs) also simplify licensing costs when you pay as you go.
Azure virtual machines run in many different geographic regions around the world. They also offer various machine sizes. The virtual machine image gallery allows you to create a SQL Server VM with the right version, edition, and operating system. This makes virtual machines a good option for many different SQL Server workloads.
[](https://learn.microsoft.com/en-us/sql/sql-server/what-is-sql-server?view=sql-server-ver17#azure-arc)
### Azure Arc
[SQL Server enabled by Azure Arc](https://learn.microsoft.com/en-us/sql/sql-server/azure-arc/overview?view=sql-server-ver17) simplifies governance and management by delivering a consistent multicloud and on-premises management platform. Azure Arc provides a centralized, unified way to manage your entire environment together, combining existing non-Azure and/or on-premises virtual machines, Kubernetes clusters, and databases into Azure Resource Manager.
You can use Azure services and management capabilities, introduce DevOps practices to support new cloud native patterns in your environment, and configure custom locations as an abstraction layer on top of Azure Arc-enabled Kubernetes clusters and cluster extensions, regardless of where your resources live.
[](https://learn.microsoft.com/en-us/sql/sql-server/what-is-sql-server?view=sql-server-ver17#azure-kubernetes-service-aks)
### Azure Kubernetes Service (ASK)
[Azure Kubernetes Service](https://learn.microsoft.com/en-us/azure/ask/intro-kubernetes) (ASK) is a managed Kubernetes service for deploying and managing container clusters. With SQL Server on Linux containers, you can [deploy a SQL Server Linux container to ASK using Helm charts](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-containers-deploy-helm-charts-kubernetes?view=sql-server-ver17).
You can also set up [SQL Managed Instance enabled by Azure Arc](https://learn.microsoft.com/en-us/azure/azure-arc/data/managed-instance-overview) on a Kubernetes infrastructure of your choice, which allows you to manage the service in Azure while your data stays in the location you prefer.
[](https://learn.microsoft.com/en-us/sql/sql-server/what-is-sql-server?view=sql-server-ver17#migrate-and-move-data)
## Migrate and move data
SQL Server provides many opportunities to migrate and modernize your data estate.
[](https://learn.microsoft.com/en-us/sql/sql-server/what-is-sql-server?view=sql-server-ver17#migrate-to-the-cloud)
### Migrate to the cloud
  * [Migrate SQL Server workloads (FAQ)](https://learn.microsoft.com/en-us/azure/azure-sql/migration-guides/modernization)
  * [Import and Export Data with the SQL Server Import and Export Wizard](https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/import-and-export-data-with-the-sql-server-import-and-export-wizard?view=sql-server-ver17)
  * [Azure Database Migration Guides](https://learn.microsoft.com/en-us/data-migration/)


[](https://learn.microsoft.com/en-us/sql/sql-server/what-is-sql-server?view=sql-server-ver17#migrate-to-sql-server)
### Migrate to SQL Server
  * [Migrate databases and structured data to SQL Server on Linux](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-migrate-overview?view=sql-server-ver17) 1
  * [SQL Server migration component in SQL Server Management Studio](https://learn.microsoft.com/en-us/ssms/migrate-sql-server-component)
  * [Import data from Excel to SQL Server or Azure SQL Database](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/import-data-from-excel-to-sql?view=sql-server-ver17)
  * [SQL Server Migration Assistant](https://learn.microsoft.com/en-us/sql/ssma/sql-server-migration-assistant?view=sql-server-ver17)


1 SQL Server 2017 (14.x) and later versions.
[](https://learn.microsoft.com/en-us/sql/sql-server/what-is-sql-server?view=sql-server-ver17#update-your-version-of-sql-server)
## Update your version of SQL Server
  * [Latest updates and version history for SQL Server](https://learn.microsoft.com/en-us/troubleshoot/sql/releases/download-and-install-latest-updates)


[](https://learn.microsoft.com/en-us/sql/sql-server/what-is-sql-server?view=sql-server-ver17#samples)
## Samples
  * [Wide World Importers sample databases](https://learn.microsoft.com/en-us/sql/samples/wide-world-importers-what-is?view=sql-server-ver17)
  * [AdventureWorks sample databases](https://learn.microsoft.com/en-us/sql/samples/adventureworks-install-configure?view=sql-server-ver17)


[](https://learn.microsoft.com/en-us/sql/sql-server/what-is-sql-server?view=sql-server-ver17#-get-help)
##  ![](https://learn.microsoft.com/en-us/sql/includes/media/info-tip.svg?view=sql-server-ver17) Get help
  * [Microsoft Q & A (SQL Server)](https://learn.microsoft.com/en-us/answers/products/sql-server)
  * [Microsoft SQL Server License Terms and Information](https://www.microsoft.com/licensing/product-licensing/sql-server)
  * [Support options for business users](https://support.microsoft.com/support-for-business)
  * [Additional SQL Server help and feedback](https://learn.microsoft.com/en-us/sql/sql-server/sql-server-get-help?view=sql-server-ver17)


[](https://learn.microsoft.com/en-us/sql/sql-server/what-is-sql-server?view=sql-server-ver17#-contribute-to-sql-documentation)
##  ![](https://learn.microsoft.com/en-us/sql/includes/media/edit-topic-pencil.svg?view=sql-server-ver17) Contribute to SQL documentation
Did you know that you can edit SQL content yourself? If you do so, not only do you help improve our documentation, but you also get credited as a contributor to the page.
For more information, see [Edit Microsoft Learn documentation](https://learn.microsoft.com/en-us/sql/sql-server/sql-server-docs-contribute?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/sql-server/what-is-sql-server?view=sql-server-ver17#related-content)
## Related content
  * [SQL Server installation guide](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/install-sql-server?view=sql-server-ver17)
  * [Installation guidance for SQL Server on Linux](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-setup?view=sql-server-ver17)
  * [Configure and customize SQL Server Linux containers](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-docker-container-configure?view=sql-server-ver17)
  * [Server configuration options](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/server-configuration-options-sql-server?view=sql-server-ver17)


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
  * [ Databases - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/databases/databases?source=recommendations)
Learn about database schemas, tables, filegroups, logins, and roles. See how you can use the SQL Server Management Studio tool to work with databases.
  * [ Tutorials for SQL Server - SQL Server ](https://learn.microsoft.com/en-us/sql/sql-server/tutorials-for-sql-server-2016?source=recommendations)
Use these SQL Server tutorials to learn new technologies and features. Tutorials for earlier versions of SQL Server usually work with more recent versions.
  * [ How to Contribute to SQL Server Documentation - SQL Server ](https://learn.microsoft.com/en-us/sql/sql-server/sql-server-docs-contribute?source=recommendations)
How to contribute to SQL Server Documentation
  * [ What's New in SQL Server 2022 - SQL Server ](https://learn.microsoft.com/en-us/sql/sql-server/what-s-new-in-sql-server-2022?source=recommendations)
Learn about new features for SQL Server 2022 (16.x), which gives you choices of development languages, data types, environments, and operating systems.
  * [ Intelligent Applications and AI - SQL Server ](https://learn.microsoft.com/en-us/sql/sql-server/ai/artificial-intelligence-intelligent-applications?source=recommendations)
Use AI options such as OpenAI and vectors to build intelligent applications with SQL Server and Azure SQL Managed Instance.
  * [ Connect to the SQL Server Database Engine - SQL Server ](https://learn.microsoft.com/en-us/sql/sql-server/connect-to-database-engine?source=recommendations)
Learn how to connect to the Database Engine used by SQL Server and Azure SQL services
  * [ Previous versions of SQL Server documentation - SQL Server ](https://learn.microsoft.com/en-us/sql/sql-server/previous-versions-sql-server?source=recommendations)
How to get online and offline documentation for previous versions of SQL Server, including 2005, 2008, 2012, and 2014.


Show 4 more
Learning path
[ Migrate SQL Server workloads to Azure SQL DP-3001 - Training ](https://learn.microsoft.com/en-us/training/paths/migrate-sql-workloads-azure/?source=recommendations)
Learn how to perform online and offline SQL Server migrations to Azure SQL. (DP-3001)
Certification
[ Microsoft Certified: Azure Database Administrator Associate - Certifications ](https://learn.microsoft.com/en-us/credentials/certifications/azure-database-administrator-associate/?source=recommendations)
Administer an SQL Server database infrastructure for cloud, on-premises and hybrid relational databases using the Microsoft PaaS relational database offerings.
Mar 8, 4 PM - Mar 8, 4 PM
Experiment with what's next in AI-driven apps and agent design
* * *
  * Last updated on 01/28/2026


##  In this article
  1. [Deployment options](https://learn.microsoft.com/en-us/sql/sql-server/what-is-sql-server?view=sql-server-ver17#deployment-options)
  2. [SQL Server components and technologies](https://learn.microsoft.com/en-us/sql/sql-server/what-is-sql-server?view=sql-server-ver17#sql-server-components-and-technologies)
  3. [Fundamental concepts](https://learn.microsoft.com/en-us/sql/sql-server/what-is-sql-server?view=sql-server-ver17#fundamental-concepts)
  4. [Connect to SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/what-is-sql-server?view=sql-server-ver17#connect-to-sql-server)
  5. [Azure integration](https://learn.microsoft.com/en-us/sql/sql-server/what-is-sql-server?view=sql-server-ver17#azure-integration)
  6. [Migrate and move data](https://learn.microsoft.com/en-us/sql/sql-server/what-is-sql-server?view=sql-server-ver17#migrate-and-move-data)
  7. [Update your version of SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/what-is-sql-server?view=sql-server-ver17#update-your-version-of-sql-server)
  8. [Samples](https://learn.microsoft.com/en-us/sql/sql-server/what-is-sql-server?view=sql-server-ver17#samples)
  9. [Get help](https://learn.microsoft.com/en-us/sql/sql-server/what-is-sql-server?view=sql-server-ver17#-get-help)
  10. [Contribute to SQL documentation](https://learn.microsoft.com/en-us/sql/sql-server/what-is-sql-server?view=sql-server-ver17#-contribute-to-sql-documentation)
  11. [Related content](https://learn.microsoft.com/en-us/sql/sql-server/what-is-sql-server?view=sql-server-ver17#related-content)

Show 2 more
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
[ Sign in ](https://learn.microsoft.com/en-us/sql/sql-server/what-is-sql-server?view=sql-server-ver17)
[English (United States)](https://learn.microsoft.com/en-us/locale?target=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fsql%2Fsql-server%2Fwhat-is-sql-server%3Fview%3Dsql-server-ver17)
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
