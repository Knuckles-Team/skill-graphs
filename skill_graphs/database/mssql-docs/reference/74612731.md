# Upgrade Analysis Services
Feedback
Summarize this article for me
##  In this article
  1. [Server upgrade](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/upgrade-analysis-services?view=sql-server-ver17#server-upgrade)
  2. [Database upgrade](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/upgrade-analysis-services?view=sql-server-ver17#database-upgrade)
  3. [Related content](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/upgrade-analysis-services?view=sql-server-ver17#related-content)


**Applies to:** ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) on Windows
Analysis Services instances can be upgraded to a SQL Server version of the same server mode to take advantage of features introduced in the current release, as described in [What's new in Analysis Services](https://learn.microsoft.com/en-us/analysis-services/what-s-new-in-analysis-services).
You can upgrade each instance in-place, independently of other instances running on the same hardware. However, most administrators choose to install a new instance of the new version for application testing before transferring production workloads onto the new server. But for development or test servers, an in-place upgrade might be more convenient.
[](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/upgrade-analysis-services?view=sql-server-ver17#server-upgrade)
## Server upgrade
There are two basic approaches for upgrading servers and databases:
The compatibility levels of databases that are attached to a given server remain the same unless you manually change them.
[](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/upgrade-analysis-services?view=sql-server-ver17#in-place-upgrade)
### In-place upgrade
The upgrade process automatically migrates existing databases from the old instance to the new instance. Because the metadata and binary data is compatible between the two versions, you'll retain the data after you upgrade and you don't have to manually migrate the data.
To upgrade an existing instance, run Setup and specify the name of the existing instance as the name of the new instance.
[](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/upgrade-analysis-services?view=sql-server-ver17#side-by-side-upgrade)
### Side-by-side upgrade
  * Backup all databases and verify that each can be restored. To learn more, see [Backup and restore Analysis Services databases](https://learn.microsoft.com/en-us/analysis-services/multidimensional-models/backup-and-restore-of-analysis-services-databases).
  * Identify a subset of reports, spreadsheets, or dashboard snapshots to use later as the basis for confirming post-upgrade server operations. If possible, collect performance measurements so that you can run comparisons against the same workloads on an upgraded server.
  * Install a new instance of Analysis Services, choosing the same server mode (tabular or multidimensional) as the server you intend to replace.
Follow post-installation tasks for configuring ports and adding server administrators. To learn more, see [Post-install configuration (Analysis Services)](https://learn.microsoft.com/en-us/analysis-services/instances/post-install-configuration-analysis-services).
  * Attach or restore each database.
  * Run DBCC to check for database integrity. Tabular models undergo more thorough checking, with tests for orphaned objects throughout the model hierarchy. For multidimensional models, only the partition indexes are checked. To learn more, see [Database Consistency Checker (DBCC) for Analysis Services tabular and multidimensional databases](https://learn.microsoft.com/en-us/analysis-services/instances/database-consistency-checker-dbcc-for-analysis-services).
  * Test reports, spreadsheets, and dashboards to confirm there's no adverse change to behavior or calculations. You should see faster performance for both multidimensional and tabular workloads.
  * Test processing operations, correcting any login or permission issues. If you're using default service account for connections, the new service runs under a different account. To learn more, see [Configure service accounts (Analysis Services)](https://learn.microsoft.com/en-us/analysis-services/instances/configure-service-accounts-analysis-services).
  * Test backup and restore operations on the upgraded server, adjusting scripts to use the new server name.


[](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/upgrade-analysis-services?view=sql-server-ver17#database-upgrade)
## Database upgrade
Databases that were created in previous versions run on the upgraded server with the original compatibility level setting. Generally, you can upgrade a database or model to operate at a higher compatibility level to gain access to new features, but doing so binds you to a specific server version.
To upgrade a database, you typically upgrade the model in SQL Server Data Tools (SSDT) and then deploy the solution to an upgraded server instance.
Tabular and multidimensional databases follow different version paths. It's coincidental that both multidimensional and tabular models have similarly numbered compatibility levels. Modes advance at different rates if feature changes affect only one of them.
For background purposes, the following table summarizes the compatibility levels, but you should review the detail articles to understand what each level provides.
Expand table
Database model | Compatibility level | Compatible versions
---|---|---
Tabular | 1500 | SQL Server 2019
Tabular | 1400 | SQL Server 2017
Tabular | 1200 | SQL Server 2016
Tabular | 1103 | SQL Server 2014
Tabular | 1100 | SQL Server 2012
Multidimensional | 1100 | SQL Server 2012 and later
Multidimensional | 1050 | SQL Server 2005, 2008, 2008 R2
For more information, see:
  * [Compatibility level of a multidimensional database (Analysis Services)](https://learn.microsoft.com/en-us/analysis-services/multidimensional-models/compatibility-level-of-a-multidimensional-database-analysis-services)
  * [Compatibility level for Analysis Services tabular models](https://learn.microsoft.com/en-us/analysis-services/tabular-models/compatibility-level-for-tabular-models-in-analysis-services)


[](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/upgrade-analysis-services?view=sql-server-ver17#related-content)
## Related content
  * [Plan a SQL Server installation](https://learn.microsoft.com/en-us/sql/sql-server/install/planning-a-sql-server-installation?view=sql-server-ver17)
  * [Upgrade Power Pivot for SharePoint](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/upgrade-power-pivot-for-sharepoint?view=sql-server-ver17)


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
  * [ Upgrade SQL Server - SQL Server ](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/upgrade-sql-server?source=recommendations)
This article provides links to resources that contain upgrade information for instances of different versions of SQL Server.
  * [ Upgrade: Installation Wizard (Setup) - SQL Server ](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/upgrade-sql-server-using-the-installation-wizard-setup?source=recommendations)
The SQL Server Installation Wizard provides a single feature tree for an in-place upgrade of SQL Server components to the latest version of SQL Server.
  * [ Upgrade SQL Server Management Tools - SQL Server ](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/upgrade-sql-server-management-tools?source=recommendations)
This article describes support for upgrading SQL Server Management Tools and management components, such as SQL Server Agent.
  * [ Upgrade the Database Engine - SQL Server ](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/upgrade-database-engine?source=recommendations)
The article provides links to resources that help you upgrade the SQL Server Database Engine from a prior release of SQL Server to the latest version.
  * [ Upgrade to a Different Edition of SQL Server - SQL Server ](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/upgrade-to-a-different-edition-of-sql-server-setup?source=recommendations)
SQL Server Setup supports edition upgrade among various editions of SQL Server. Before you begin an edition upgrade, review the resources in this article.
  * [ Choose a Database Engine Upgrade Method - SQL Server ](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/choose-a-database-engine-upgrade-method?source=recommendations)
This article describes upgrade paths for the Database Engine in SQL Server, including upgrade in-place, migrate to a new installation, and a rolling upgrade.
  * [ SQL Server 2022 Release Notes - SQL Server ](https://learn.microsoft.com/en-us/sql/sql-server/sql-server-2022-release-notes?source=recommendations)
Find information about SQL Server 2022 (16.x) limitations, known issues, help resources, and other release notes.
  * [ Supported Version and Edition Upgrades (SQL Server 2022) - SQL Server ](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/supported-version-and-edition-upgrades-2022?source=recommendations)
The supported version and edition upgrades for SQL Server 2022.


Show 5 more
Module
[ Evaluate strategies for migrating to Azure SQL - Training ](https://learn.microsoft.com/en-us/training/modules/evaluate-strategies-for-migrating-to-azure-sql/?source=recommendations)
Evaluate strategies for migrating to Azure SQL
Certification
[ Microsoft Certified: Azure Database Administrator Associate - Certifications ](https://learn.microsoft.com/en-us/credentials/certifications/azure-database-administrator-associate/?source=recommendations)
Administer an SQL Server database infrastructure for cloud, on-premises and hybrid relational databases using the Microsoft PaaS relational database offerings.
Mar 8, 4 PM - Mar 8, 4 PM
Experiment with what's next in AI-driven apps and agent design
* * *
  * Last updated on 06/04/2025


##  In this article
  1. [Server upgrade](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/upgrade-analysis-services?view=sql-server-ver17#server-upgrade)
  2. [Database upgrade](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/upgrade-analysis-services?view=sql-server-ver17#database-upgrade)
  3. [Related content](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/upgrade-analysis-services?view=sql-server-ver17#related-content)


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
[ Sign in ](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/upgrade-analysis-services?view=sql-server-ver17)
[English (United States)](https://learn.microsoft.com/en-us/locale?target=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fsql%2Fdatabase-engine%2Finstall-windows%2Fupgrade-analysis-services%3Fview%3Dsql-server-ver17)
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
