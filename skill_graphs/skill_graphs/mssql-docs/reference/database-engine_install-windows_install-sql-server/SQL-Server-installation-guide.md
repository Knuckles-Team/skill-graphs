# SQL Server installation guide
Feedback
Summarize this article for me
##  In this article
  1. [Get started](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/install-sql-server?view=sql-server-ver17#get-started)
  2. [Installation media](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/install-sql-server?view=sql-server-ver17#installation-media)
  3. [Considerations](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/install-sql-server?view=sql-server-ver17#considerations)
  4. [SQL Server installation](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/install-sql-server?view=sql-server-ver17#sql-server-installation)
  5. [Individual component installation](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/install-sql-server?view=sql-server-ver17#individual-component-installation)
  6. [SQL Server configuration](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/install-sql-server?view=sql-server-ver17#sql-server-configuration)
  7. [Related content](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/install-sql-server?view=sql-server-ver17#related-content)

Show 3 more
**Applies to:** ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) on Windows
This article is an index of content that provides guidance for installing SQL Server on Windows.
For other deployment scenarios, see:
  * [Installation guidance for SQL Server on Linux](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-setup?view=sql-server-ver17)
  * [Deploy and connect to SQL Server Linux containers](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-docker-container-deployment?view=sql-server-ver17)
  * [Kubernetes - Big Data Clusters](https://learn.microsoft.com/en-us/sql/big-data-cluster/deploy-get-started?view=sql-server-ver17) (SQL Server 2019 (15.x) only)


Beginning with SQL Server 2016 (13.x), SQL Server is only available as a 64-bit application. Here are important details about how to get SQL Server and how to install it.
[](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/install-sql-server?view=sql-server-ver17#get-started)
## Get started
Beginning with SQL Server 2025 (17.x), Data Quality Services (DQS), Master Data Services (MDS), Azure Synapse Link, and Reporting Services are removed. Azure Synapse Link and Reporting Services were deprecated in previous versions.
  * **Editions and features** : Review the supported features for the different editions and versions of SQL Server to determine which best suits your business needs.
    * [SQL Server 2025](https://learn.microsoft.com/en-us/sql/sql-server/editions-and-components-of-sql-server-2025?view=sql-server-ver17)
    * [SQL Server 2022](https://learn.microsoft.com/en-us/sql/sql-server/editions-and-components-of-sql-server-2022?view=sql-server-ver17)
    * [SQL Server 2019](https://learn.microsoft.com/en-us/sql/sql-server/editions-and-components-of-sql-server-2019?view=sql-server-ver17)
    * [SQL Server 2017](https://learn.microsoft.com/en-us/sql/sql-server/editions-and-components-of-sql-server-2017?view=sql-server-ver17)
    * [SQL Server 2016](https://learn.microsoft.com/en-us/sql/sql-server/editions-and-components-of-sql-server-2016?view=sql-server-ver17)
  * **Requirements** : Review hardware and software installation requirements:
    * [SQL Server 2025](https://learn.microsoft.com/en-us/sql/sql-server/install/hardware-and-software-requirements-for-installing-sql-server-2025?view=sql-server-ver17)
    * [SQL Server 2022](https://learn.microsoft.com/en-us/sql/sql-server/install/hardware-and-software-requirements-for-installing-sql-server-2022?view=sql-server-ver17)
    * [SQL Server 2019](https://learn.microsoft.com/en-us/sql/sql-server/install/hardware-and-software-requirements-for-installing-sql-server-2019?view=sql-server-ver17)
    * [SQL Server 2016 and 2017](https://learn.microsoft.com/en-us/sql/sql-server/install/hardware-and-software-requirements-for-installing-sql-server?view=sql-server-ver17)
    * [SQL Server on Linux](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-setup?view=sql-server-ver17)
You must also review system configuration checks, and security considerations in [Plan a SQL Server installation](https://learn.microsoft.com/en-us/sql/sql-server/install/planning-a-sql-server-installation?view=sql-server-ver17).
  * **Sample databases and sample code** aren't installed as part of SQL Server Setup by default, but can be installed for non-Express editions of SQL Server. For more information, see [SQL samples](https://learn.microsoft.com/en-us/sql/samples/sql-samples-where-are?view=sql-server-ver17).


[](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/install-sql-server?view=sql-server-ver17#installation-media)
## Installation media
The download location for SQL Server depends on the edition:
  * **SQL Server Enterprise, Standard, and Express editions** are licensed for production use. For the Enterprise and Standard Editions, contact your software vendor for the installation media. You can find purchasing information and a directory of Microsoft partners on the [Microsoft licensing page](https://www.microsoft.com/licensing/product-licensing/sql-server).
  * If you have a volume licensing agreement, for example an [Enterprise Agreement](https://www.microsoft.com/licensing/licensing-programs/enterprise), you can download software from the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339). The software's activation wizard automatically detects an embedded product key during installation.
  * [Free versions](https://www.microsoft.com/sql-server/sql-server-downloads).


Other SQL Server components can be found here:
  * [Latest updates and version history for SQL Server](https://learn.microsoft.com/en-us/troubleshoot/sql/releases/download-and-install-latest-updates)
  * [SQL Server Reporting Services](https://www.microsoft.com/download/details.aspx?id=104502).
  * [SQL Server Management Studio](https://learn.microsoft.com/en-us/ssms/sql-server-management-studio-ssms)
  * [MSSQL extension for Visual Studio Code](https://learn.microsoft.com/en-us/sql/tools/visual-studio-code-extensions/mssql/mssql-extension-visual-studio-code?view=sql-server-ver17)


[](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/install-sql-server?view=sql-server-ver17#considerations)
## Considerations
If you want to install or upgrade SQL Server to SQL Server 2022 (16.x) or a later version, on Windows Server 2022 or greater, make sure there are no restarts pending. You should restart Windows first, and then run the SQL Server installation or upgrade.
  * Installation fails if you launch setup through Remote Desktop Connection with the media on a local resource in the RDC client. To install remotely the media must be on a network share or local to the physical or virtual machine. SQL Server installation media could be either on a network share, a mapped drive, a local drive, or presented as an ISO to a virtual machine.
  * SQL Server Setup installs the following software components required by the product:
    * SQL Server Native Client
    * SQL Server Setup support files


[](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/install-sql-server?view=sql-server-ver17#sql-server-installation)
## SQL Server installation
Expand table
Article | Description
---|---
[Install SQL Server from the Installation Wizard (Setup)](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/install-sql-server-from-the-installation-wizard-setup?view=sql-server-ver17) | Install SQL Server using the Installation Wizard GUI launched from the setup.exe setup media.
[Install, configure, or uninstall SQL Server on Windows from the command prompt](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/install-sql-server-from-the-command-prompt?view=sql-server-ver17) | Sample syntax and installation parameters for running a SQL Server installation from the command prompt.
[Install SQL Server on Server Core](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/install-sql-server-on-server-core?view=sql-server-ver17) | Install SQL Server on Windows Server Core.
[Check parameters for the System Configuration Checker](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/check-parameters-for-the-system-configuration-checker?view=sql-server-ver17) | Discusses the function of the System Configuration Checker (SCC).
[Install SQL Server using a configuration file](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/install-sql-server-using-a-configuration-file?view=sql-server-ver17) | Sample syntax and installation parameters for running Setup through a configuration file.
[Slipstream installation for SQL Server](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/install-sql-server-using-slipstream?view=sql-server-ver17) | Sample syntax and installation parameters for installing SQL Server with the latest cumulative update.
[Install SQL Server with SysPrep](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/install-sql-server-using-sysprep?view=sql-server-ver17) | Sample syntax and installation parameters for running Setup through SysPrep.
[Add Features to an Instance of SQL Server (Setup)](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/add-features-to-an-instance-of-sql-server-setup?view=sql-server-ver17) | Update components of an existing instance of SQL Server.
[SQL Server failover cluster installation](https://learn.microsoft.com/en-us/sql/sql-server/failover-clusters/install/sql-server-failover-cluster-installation?view=sql-server-ver17) | Install a SQL Server failover cluster instance.
[Repair a failed SQL Server installation](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/repair-a-failed-sql-server-installation?view=sql-server-ver17) | Repair a corrupt SQL Server installation.
[Rename a computer that hosts a stand-alone instance of SQL Server](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/rename-a-computer-that-hosts-a-stand-alone-instance-of-sql-server?view=sql-server-ver17) | Update system metadata that is stored in `sys.servers` after the hostname of a computer hosting a stand-alone instance of SQL Server has been renamed.
[Install SQL Server servicing updates](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/install-sql-server-servicing-updates?view=sql-server-ver17) | Install updates for SQL Server.
[View and read SQL Server Setup log files](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/view-and-read-sql-server-setup-log-files?view=sql-server-ver17) | View and read the errors in the SQL Server setup log files.
[Validate a SQL Server installation](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/validate-a-sql-server-installation?view=sql-server-ver17) | Review the use of the SQL Discovery report to verify the version of SQL Server and the SQL Server features installed on the computer.
[](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/install-sql-server?view=sql-server-ver17#individual-component-installation)
## Individual component installation
Expand table
Article | Description
---|---
[Install SQL Server Database Engine](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/install-sql-server-database-engine?view=sql-server-ver17) | Install and configure the SQL Server Database Engine.
[Install SQL Server replication](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/install-sql-server-replication?view=sql-server-ver17) | Install and configure SQL Server Replication.
[Install Distributed Replay](https://learn.microsoft.com/en-us/sql/tools/distributed-replay/install-distributed-replay?view=sql-server-ver17)1 | Lists articles to install the Distributed Replay feature.
[SQL Server Management Tools](https://learn.microsoft.com/en-us/ssms/install/install) | Install and configure SQL Server management tools.
[SQL Server PowerShell](https://learn.microsoft.com/en-us/powershell/sql-server/download-sql-server-ps-module) | Considerations for installing SQL Server PowerShell components.
1 Distributed Replay is deprecated in SQL Server 2022 (16.x).
[](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/install-sql-server?view=sql-server-ver17#sql-server-configuration)
## SQL Server configuration
Expand table
Article | Description
---|---
[Configure the Windows Firewall to allow SQL Server access](https://learn.microsoft.com/en-us/sql/sql-server/install/configure-the-windows-firewall-to-allow-sql-server-access?view=sql-server-ver17) | Overview of firewall configuration and how to configure the Windows Firewall to allow access to SQL Server.
[Configure the Windows Firewall (SSAS)](https://learn.microsoft.com/en-us/analysis-services/instances/configure-the-windows-firewall-to-allow-analysis-services-access) | Configure both port and firewall settings to allow access to Analysis Services or Power Pivot for SharePoint.
[Configure a multi-homed computer for SQL Server access](https://learn.microsoft.com/en-us/sql/sql-server/install/configure-a-multi-homed-computer-for-sql-server-access?view=sql-server-ver17) | Configure SQL Server and Windows Firewall with Advanced Security to provide for network connections to an instance of SQL Server in a multi-homed environment.
[](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/install-sql-server?view=sql-server-ver17#related-content)
## Related content
  * [Upgrade SQL Server](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/upgrade-sql-server?view=sql-server-ver17)
  * [Uninstall SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/install/uninstall-sql-server?view=sql-server-ver17)
  * [Install and configure SQL Server Reporting Services](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/install-reporting-services?view=sql-server-ver17)
  * [Install SQL Server Analysis Services (SSAS)](https://learn.microsoft.com/en-us/analysis-services/instances/install-windows/install-analysis-services)
  * [Install SQL Server Business Intelligence Features](https://learn.microsoft.com/en-us/sql/sql-server/install/install-sql-server-business-intelligence-features?view=sql-server-ver17)
  * [Business continuity and database recovery - SQL Server](https://learn.microsoft.com/en-us/sql/database-engine/sql-server-business-continuity-dr?view=sql-server-ver17)


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
  * [ Editions and Supported Features of SQL Server 2019 - SQL Server ](https://learn.microsoft.com/en-us/sql/sql-server/editions-and-components-of-sql-server-2019?source=recommendations)
Editions and supported features of SQL Server 2019
  * [ Install SQL Server Database Engine - SQL Server ](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/install-sql-server-database-engine?source=recommendations)
Learn about features that can be installed when you select SQL Server Database Engine from Components to Install of the SQL Server Installation Wizard.
  * [ Install Using Graphical User Interface - SQL Server ](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/install-sql-server-from-the-installation-wizard-setup?source=recommendations)
This article provides a step-by-step procedure for installing a new instance of SQL Server by using the SQL Server Setup Installation Wizard.
  * [ Editions and Supported Features of SQL Server 2022 - SQL Server ](https://learn.microsoft.com/en-us/sql/sql-server/editions-and-components-of-sql-server-2022?source=recommendations)
Learn details of the features supported by the various editions of SQL Server 2022.
  * [ Optimize download-only article performance (Merge) - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/replication/merge/optimize-merge-replication-performance-with-download-only-articles?source=recommendations)
Describes how to optimize the performance of download-only articles used by Merge Replication.
  * [ SQL Server 2022: Hardware and Software Requirements - SQL Server ](https://learn.microsoft.com/en-us/sql/sql-server/install/hardware-and-software-requirements-for-installing-sql-server-2022?source=recommendations)
A list of hardware, software, and operating system requirements for installing and running SQL Server 2022.
  * [ SQL Server Docs Navigation Tips - SQL Server ](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?source=recommendations)
Tips and tricks for navigating the SQL Server technical documentation - explains such things as the hub page, the table of contents, the header, as well as how to use the breadcrumbs and how to use the version filter.
  * [ Editions and Supported Features of SQL Server 2025 - SQL Server ](https://learn.microsoft.com/en-us/sql/sql-server/editions-and-components-of-sql-server-2025?source=recommendations)
Learn details of the features supported by the various editions of SQL Server 2025.


Show 5 more
Module
[ Perform post-installation configuration of Windows Server - Training ](https://learn.microsoft.com/en-us/training/modules/perform-post-installation-configuration-of-windows-server/?source=recommendations)
Perform post-installation configuration of Windows Server
Certification
[ Microsoft Certified: Azure Database Administrator Associate - Certifications ](https://learn.microsoft.com/en-us/credentials/certifications/azure-database-administrator-associate/?source=recommendations)
Administer an SQL Server database infrastructure for cloud, on-premises and hybrid relational databases using the Microsoft PaaS relational database offerings.
Mar 8, 4 PM - Mar 8, 4 PM
Experiment with what's next in AI-driven apps and agent design
* * *
  * Last updated on 01/30/2026


##  In this article
  1. [Get started](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/install-sql-server?view=sql-server-ver17#get-started)
  2. [Installation media](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/install-sql-server?view=sql-server-ver17#installation-media)
  3. [Considerations](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/install-sql-server?view=sql-server-ver17#considerations)
  4. [SQL Server installation](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/install-sql-server?view=sql-server-ver17#sql-server-installation)
  5. [Individual component installation](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/install-sql-server?view=sql-server-ver17#individual-component-installation)
  6. [SQL Server configuration](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/install-sql-server?view=sql-server-ver17#sql-server-configuration)
  7. [Related content](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/install-sql-server?view=sql-server-ver17#related-content)


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
[ Sign in ](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/install-sql-server?view=sql-server-ver17)
[English (United States)](https://learn.microsoft.com/en-us/locale?target=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fsql%2Fdatabase-engine%2Finstall-windows%2Finstall-sql-server%3Fview%3Dsql-server-ver17)
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
