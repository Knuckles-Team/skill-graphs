# Upgrade SQL Server
Feedback
Summarize this article for me
##  In this article
  1. [Upgrade documentation](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/upgrade-sql-server?view=sql-server-ver17#upgrade-documentation)
  2. [Related content](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/upgrade-sql-server?view=sql-server-ver17#related-content)


**Applies to:** ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) on Windows
You can upgrade instances of SQL Server 2012 (11.x), SQL Server 2014 (12.x), SQL Server 2016 (13.x), SQL Server 2017 (14.x), or SQL Server 2019 (15.x) directly to SQL Server 2022 (16.x). For SQL Server 2008 (10.0.x) and SQL Server 2008 R2 (10.50.x), you need to either do a side-by-side upgrade, or a migration, to move to SQL Server 2022 (16.x) as there's no common overlap between a supported mainstream operating system. Before running setup to upgrade, review the following articles about the upgrade process and the release notes.
Check out what's new in each version of the product:
  * [SQL Server 2025 release notes](https://learn.microsoft.com/en-us/sql/sql-server/sql-server-2025-release-notes?view=sql-server-ver17)
  * [SQL Server 2022 release notes](https://learn.microsoft.com/en-us/sql/sql-server/sql-server-2022-release-notes?view=sql-server-ver17)
  * [SQL Server 2019 release notes](https://learn.microsoft.com/en-us/sql/sql-server/sql-server-2019-release-notes?view=sql-server-ver17)
  * [SQL Server 2017 release notes](https://learn.microsoft.com/en-us/sql/sql-server/sql-server-2017-release-notes?view=sql-server-ver17)
  * [SQL Server 2016 release notes](https://learn.microsoft.com/en-us/sql/sql-server/sql-server-2016-release-notes?view=sql-server-ver17)


Support for SQL Server 2014 (12.x) ended on July 9, 2024. For new end of support options, see [End of Support for Windows Server and SQL Server](https://www.microsoft.com/sql-server/end-of-support).
If you're upgrading from an end-of-support version of SQL Server, see the [end of support options](https://learn.microsoft.com/en-us/sql/sql-server/end-of-support/sql-server-end-of-support-overview?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/upgrade-sql-server?view=sql-server-ver17#upgrade-documentation)
## Upgrade documentation
If you want to install or upgrade SQL Server to SQL Server 2022 (16.x) or a later version, on Windows Server 2022 or greater, make sure there are no restarts pending. You should restart Windows first, and then run the SQL Server installation or upgrade.
For a list of features supported by the editions of SQL Server on Windows, see:
  * [Editions and supported features of SQL Server 2025](https://learn.microsoft.com/en-us/sql/sql-server/editions-and-components-of-sql-server-2025?view=sql-server-ver17)
  * [Editions and supported features of SQL Server 2022](https://learn.microsoft.com/en-us/sql/sql-server/editions-and-components-of-sql-server-2022?view=sql-server-ver17)
  * [Editions and supported features of SQL Server 2019](https://learn.microsoft.com/en-us/sql/sql-server/editions-and-components-of-sql-server-2019?view=sql-server-ver17)
  * [Editions and supported features of SQL Server 2017](https://learn.microsoft.com/en-us/sql/sql-server/editions-and-components-of-sql-server-2017?view=sql-server-ver17)
  * [Editions and supported features of SQL Server 2016](https://learn.microsoft.com/en-us/sql/sql-server/editions-and-components-of-sql-server-2016?view=sql-server-ver17)


The following articles help you upgrade components of SQL Server:
  * [Upgrade Analysis Services](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/upgrade-analysis-services?view=sql-server-ver17)
  * [Upgrade the Database Engine](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/upgrade-database-engine?view=sql-server-ver17)
  * [Upgrade Data Quality Services](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/upgrade-data-quality-services?view=sql-server-ver17) 1
  * [Upgrade Integration Services](https://learn.microsoft.com/en-us/sql/integration-services/install-windows/upgrade-integration-services?view=sql-server-ver17)
  * [Upgrade Master Data Services](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/upgrade-master-data-services?view=sql-server-ver17) 1
  * [Upgrade Power Pivot for SharePoint](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/upgrade-power-pivot-for-sharepoint?view=sql-server-ver17)
  * [Upgrade or patch replicated databases](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/upgrade-replicated-databases?view=sql-server-ver17)
  * [Upgrade and migrate Reporting Services](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/upgrade-and-migrate-reporting-services?view=sql-server-ver17) 1
  * [Upgrade SQL Server Management Tools](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/upgrade-sql-server-management-tools?view=sql-server-ver17)
  * [Upgrade SQL Server Using the Installation Wizard (Setup)](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/upgrade-sql-server-using-the-installation-wizard-setup?view=sql-server-ver17)
  * [Upgrade to a different edition of SQL Server (Setup)](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/upgrade-downgrade-sql-server-edition-setup?view=sql-server-ver17)
  * [SQL Server end of support options](https://learn.microsoft.com/en-us/sql/sql-server/end-of-support/sql-server-end-of-support-overview?view=sql-server-ver17)


1 DQS, MDS, and Reporting Services upgrades aren't supported on SQL Server 2025 (17.x).
[](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/upgrade-sql-server?view=sql-server-ver17#related-content)
## Related content
  * [Upgrade the Database Engine](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/upgrade-database-engine?view=sql-server-ver17)
  * [Upgrade Analysis Services](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/upgrade-analysis-services?view=sql-server-ver17)
  * [Upgrade and migrate Reporting Services](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/upgrade-and-migrate-reporting-services?view=sql-server-ver17)
  * [Upgrade Integration Services](https://learn.microsoft.com/en-us/sql/integration-services/install-windows/upgrade-integration-services?view=sql-server-ver17)
  * [Upgrade or patch replicated databases](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/upgrade-replicated-databases?view=sql-server-ver17)
  * [Upgrade Master Data Services](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/upgrade-master-data-services?view=sql-server-ver17)
  * [SQL Server 2008 R2 Best Practices Analyzer](https://www.microsoft.com/download/details.aspx?id=436)
  * [Discontinued Database Engine functionality in SQL Server](https://learn.microsoft.com/en-us/sql/database-engine/discontinued-database-engine-functionality-in-sql-server?view=sql-server-ver17)
  * [Upgrade to a different edition of SQL Server (Setup)](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/upgrade-downgrade-sql-server-edition-setup?view=sql-server-ver17)


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
  * [ SQL Server 2022 Release Notes - SQL Server ](https://learn.microsoft.com/en-us/sql/sql-server/sql-server-2022-release-notes?source=recommendations)
Find information about SQL Server 2022 (16.x) limitations, known issues, help resources, and other release notes.
  * [ Upgrade: Installation Wizard (Setup) - SQL Server ](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/upgrade-sql-server-using-the-installation-wizard-setup?source=recommendations)
The SQL Server Installation Wizard provides a single feature tree for an in-place upgrade of SQL Server components to the latest version of SQL Server.
  * [ Upgrade SQL Server Management Tools - SQL Server ](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/upgrade-sql-server-management-tools?source=recommendations)
This article describes support for upgrading SQL Server Management Tools and management components, such as SQL Server Agent.
  * [ Upgrade to a Different Edition of SQL Server - SQL Server ](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/upgrade-to-a-different-edition-of-sql-server-setup?source=recommendations)
SQL Server Setup supports edition upgrade among various editions of SQL Server. Before you begin an edition upgrade, review the resources in this article.
  * [ SQL Server 2022: Hardware and Software Requirements - SQL Server ](https://learn.microsoft.com/en-us/sql/sql-server/install/hardware-and-software-requirements-for-installing-sql-server-2022?source=recommendations)
A list of hardware, software, and operating system requirements for installing and running SQL Server 2022.
  * [ Upgrade Analysis Services - SQL Server ](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/upgrade-analysis-services?source=recommendations)
Upgrade Analysis Services
  * [ Supported Version and Edition Upgrades (SQL Server 2022) - SQL Server ](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/supported-version-and-edition-upgrades-2022?source=recommendations)
The supported version and edition upgrades for SQL Server 2022.
  * [ SQL Server 2016 Release Notes - SQL Server ](https://learn.microsoft.com/en-us/sql/sql-server/sql-server-2016-release-notes?source=recommendations)
This Release Notes document describes known issues that you should read about before you install or troubleshoot Microsoft SQL Server 2016 releases.


Show 5 more
Learning path
[ Explore SQL Server 2025 capabilities - Training ](https://learn.microsoft.com/en-us/training/paths/explore-sql-server-2022-capabilities/?source=recommendations)
Explore SQL Server 2025 capabilities
Certification
[ Microsoft Certified: Azure Database Administrator Associate - Certifications ](https://learn.microsoft.com/en-us/credentials/certifications/azure-database-administrator-associate/?source=recommendations)
Administer an SQL Server database infrastructure for cloud, on-premises and hybrid relational databases using the Microsoft PaaS relational database offerings.
Mar 8, 4 PM - Mar 8, 4 PM
Experiment with what's next in AI-driven apps and agent design
* * *
  * Last updated on 11/18/2025


##  In this article
  1. [Upgrade documentation](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/upgrade-sql-server?view=sql-server-ver17#upgrade-documentation)
  2. [Related content](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/upgrade-sql-server?view=sql-server-ver17#related-content)


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
[ Sign in ](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/upgrade-sql-server?view=sql-server-ver17)
[English (United States)](https://learn.microsoft.com/en-us/locale?target=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fsql%2Fdatabase-engine%2Finstall-windows%2Fupgrade-sql-server%3Fview%3Dsql-server-ver17)
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
