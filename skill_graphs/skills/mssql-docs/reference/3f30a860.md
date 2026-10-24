# Install SQL Server Data Tools (SSDT) for Visual Studio
Feedback
Summarize this article for me
##  In this article
  1. [Install SSDT with Visual Studio](https://learn.microsoft.com/en-us/sql/ssdt/download-sql-server-data-tools-ssdt?view=sql-server-ver17&tabs=vs2026#install-ssdt-with-visual-studio)
  2. [Install extensions for Analysis Services, Integration Services, and Reporting Services](https://learn.microsoft.com/en-us/sql/ssdt/download-sql-server-data-tools-ssdt?view=sql-server-ver17&tabs=vs2026#install-extensions-for-analysis-services-integration-services-and-reporting-services)
  3. [Supported SQL versions](https://learn.microsoft.com/en-us/sql/ssdt/download-sql-server-data-tools-ssdt?view=sql-server-ver17&tabs=vs2026#supported-sql-versions)
  4. [Offline installation](https://learn.microsoft.com/en-us/sql/ssdt/download-sql-server-data-tools-ssdt?view=sql-server-ver17&tabs=vs2026#offline-installation)
  5. [License terms for Visual Studio](https://learn.microsoft.com/en-us/sql/ssdt/download-sql-server-data-tools-ssdt?view=sql-server-ver17&tabs=vs2026#license-terms-for-visual-studio)
  6. [Previous versions](https://learn.microsoft.com/en-us/sql/ssdt/download-sql-server-data-tools-ssdt?view=sql-server-ver17&tabs=vs2026#previous-versions)
  7. [Related content](https://learn.microsoft.com/en-us/sql/ssdt/download-sql-server-data-tools-ssdt?view=sql-server-ver17&tabs=vs2026#related-content)
  8. [Get help](https://learn.microsoft.com/en-us/sql/ssdt/download-sql-server-data-tools-ssdt?view=sql-server-ver17&tabs=vs2026#-get-help)
  9. [Contribute to SQL documentation](https://learn.microsoft.com/en-us/sql/ssdt/download-sql-server-data-tools-ssdt?view=sql-server-ver17&tabs=vs2026#-contribute-to-sql-documentation)

Show 5 more
**Applies to:** ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure SQL Database](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure SQL Managed Instance](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure Synapse Analytics](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL database in Microsoft Fabric](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to)
**SQL Server Data Tools (SSDT)** is a set of development tooling for building SQL Server databases, Azure SQL databases, Analysis Services (AS) data models, Integration Services (IS) packages, and Reporting Services (RS) reports. With SSDT, you can design and deploy SQL objects with the same project concept as other application development tools. The **SQL projects** capability extends to CI/CD pipelines, enabling you to automate the build and deployment of your database projects with the [SqlPackage CLI](https://learn.microsoft.com/en-us/sql/tools/sqlpackage/sqlpackage?view=sql-server-ver17).
The release notes for SSDT and its components are available for [Visual Studio 2017, 2019, 2022, and 2026](https://learn.microsoft.com/en-us/sql/ssdt/sql-server-data-tools?view=sql-server-ver17#release-notes). An overview of the core SSDT functionality is provided in the [SSDT Overview](https://learn.microsoft.com/en-us/sql/ssdt/sql-server-data-tools?view=sql-server-ver17#core-sql-server-data-tools).
![Screenshot of graphic with SQL Server Data Tools component and three extensions.](https://learn.microsoft.com/en-us/sql/ssdt/media/download-sql-server-data-tools-ssdt/install-layout.png?view=sql-server-ver17)
SSDT is installed as a Visual Studio component, both for [online installation](https://learn.microsoft.com/en-us/sql/ssdt/download-sql-server-data-tools-ssdt?view=sql-server-ver17&tabs=vs2026#install-ssdt-with-visual-studio) and [offline installation](https://learn.microsoft.com/en-us/sql/ssdt/download-sql-server-data-tools-ssdt?view=sql-server-ver17&tabs=vs2026#offline-installation). Analysis Services, Integration Services, and Reporting Services projects are available as separate extensions for each version.
SDK-style SQL projects in Visual Studio are available as part of the **SQL Server Data Tools, SDK-style (preview)** feature for Visual Studio 2022, separate from the original SSDT. The SDK-style project format is based on the new SDK-style projects introduced in .NET Core and is the format used by the SQL Database Projects extension for Visual Studio Code. For more information, see [SQL Server Data Tools, SDK-style (preview)](https://learn.microsoft.com/en-us/sql/ssdt/sql-server-data-tools-sdk-style?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/ssdt/download-sql-server-data-tools-ssdt?view=sql-server-ver17&tabs=vs2026#install-ssdt-with-visual-studio)
## Install SSDT with Visual Studio
If [Visual Studio 2026](https://learn.microsoft.com/en-us/visualstudio/install/install-visual-studio?preserve-view=true&view=vs-2026) or [Visual Studio 2022](https://learn.microsoft.com/en-us/visualstudio/install/install-visual-studio?preserve-view=true&view=vs-2022) is already installed, you can edit the list of workloads to include SSDT. If you don't have Visual Studio 2022 or 2026 installed, then you can download and install [Visual Studio 2026](https://visualstudio.microsoft.com/downloads/).
To modify the installed Visual Studio workloads to include SSDT, use the Visual Studio Installer.
  1. Launch the Visual Studio Installer. In the Windows Start menu, you can search for "installer."
  2. In the installer, select **Modify** for the version of Visual Studio to which you want to add SSDT.
  3. Select **SQL Server Data Tools** under **Data storage and processing** in the list of workloads.
[ ![Screenshot of Data storage and processing workload 2022.](https://learn.microsoft.com/en-us/sql/ssdt/media/download-sql-server-data-tools-ssdt/data-workload-2022.png?view=sql-server-ver17) ](https://learn.microsoft.com/en-us/sql/ssdt/media/download-sql-server-data-tools-ssdt/data-workload-2022.png?view=sql-server-ver17#lightbox)


[](https://learn.microsoft.com/en-us/sql/ssdt/download-sql-server-data-tools-ssdt?view=sql-server-ver17&tabs=vs2026#visual-studio-for-arm64)
### Visual Studio for Arm64
Visual Studio is available as a [native Arm64 application](https://learn.microsoft.com/en-us/visualstudio/install/visual-studio-on-arm-devices) on Windows 11 Arm64. In Visual Studio 2026, SSDT is available for Arm64 with some limitations:
  * IntelliSense and code completion aren't available for T-SQL files in SQL projects
  * The T-SQL debugger isn't available
  * Visual Studio can't connect to LocalDB


To install or configure Visual Studio to include SSDT on an Arm64 device:
  1. Install Visual Studio 2026 or later on your Arm64 device.
  2. In the installer, select the **Individual components** tab and search for **SQL Server Data Tools**.
[ ![Screenshot of SQL Server Data Tools for Arm64.](https://learn.microsoft.com/en-us/sql/ssdt/media/download-sql-server-data-tools-ssdt/ssdt-component-install.png?view=sql-server-ver17) ](https://learn.microsoft.com/en-us/sql/ssdt/media/download-sql-server-data-tools-ssdt/ssdt-component-install.png?view=sql-server-ver17#lightbox)
  3. Select **SQL Server Data Tools** and then choose **Modify**.


[](https://learn.microsoft.com/en-us/sql/ssdt/download-sql-server-data-tools-ssdt?view=sql-server-ver17&tabs=vs2026#install-extensions-for-analysis-services-integration-services-and-reporting-services)
## Install extensions for Analysis Services, Integration Services, and Reporting Services
For Analysis Services (SSAS), Integration Services (SSIS), or Reporting Services (SSRS) projects, you can install the appropriate [extensions](https://learn.microsoft.com/en-us/visualstudio/ide/finding-and-using-visual-studio-extensions) from within Visual Studio with **Extensions** > **Manage Extensions** or from the
  * [Visual Studio 2026 extensions](https://learn.microsoft.com/en-us/sql/ssdt/download-sql-server-data-tools-ssdt?view=sql-server-ver17&tabs=vs2026#tabpanel_1_vs2026)
  * [Visual Studio 2022 extensions](https://learn.microsoft.com/en-us/sql/ssdt/download-sql-server-data-tools-ssdt?view=sql-server-ver17&tabs=vs2026#tabpanel_1_vs2022)
  * [Visual Studio 2019 extensions](https://learn.microsoft.com/en-us/sql/ssdt/download-sql-server-data-tools-ssdt?view=sql-server-ver17&tabs=vs2026#tabpanel_1_vs2019)


The extensions for Visual Studio 2022 and 2026 are shared:
The extensions for Visual Studio 2022 and 2026 are shared:
Extensions for Visual Studio 2019:
[](https://learn.microsoft.com/en-us/sql/ssdt/download-sql-server-data-tools-ssdt?view=sql-server-ver17&tabs=vs2026#supported-sql-versions)
## Supported SQL versions
  * [Supported SQL versions in Visual Studio 2026](https://learn.microsoft.com/en-us/sql/ssdt/download-sql-server-data-tools-ssdt?view=sql-server-ver17&tabs=vs2026#tabpanel_2_vs2026)
  * [Supported SQL versions in Visual Studio 2022](https://learn.microsoft.com/en-us/sql/ssdt/download-sql-server-data-tools-ssdt?view=sql-server-ver17&tabs=vs2026#tabpanel_2_vs2022)
  * [Supported SQL versions in Visual Studio 2019](https://learn.microsoft.com/en-us/sql/ssdt/download-sql-server-data-tools-ssdt?view=sql-server-ver17&tabs=vs2026#tabpanel_2_vs2019)


Supported SQL versions in Visual Studio 2026:
Expand table
Project templates | SQL platforms supported
---|---
Relational databases | SQL Server 2016 (13.x) - SQL Server 2025 (17.x)

Azure SQL Database, Azure SQL Managed Instance

Azure Synapse Analytics Dedicated Pools
Azure Synapse Analytics Serverless Pools

Warehouse in Microsoft Fabric
SQL database in Microsoft Fabric
Analysis Services models

Reporting Services reports | SQL Server 2016 (13.x) - SQL Server 2025 (17.x)
Integration Services packages | SQL Server 2019 (15.x) - SQL Server 2025 (17.x)
Supported SQL versions in Visual Studio 2022:
Expand table
Project templates | SQL platforms supported
---|---
Relational databases | SQL Server 2016 (13.x) - SQL Server 2022 (16.x)

Azure SQL Database, Azure SQL Managed Instance

Azure Synapse Analytics Dedicated Pools
Azure Synapse Analytics Serverless Pools (requires VS2022 17.7)
Analysis Services models

Reporting Services reports | SQL Server 2016 (13.x) - SQL Server 2022 (16.x)
Integration Services packages | SQL Server 2019 (15.x) - SQL Server 2022 (16.x)
Supported SQL versions in Visual Studio 2019:
Expand table
Project templates | SQL platforms supported
---|---
Relational databases | SQL Server 2012 (11.x) - SQL Server 2019 (15.x)

Azure SQL Database, Azure SQL Managed Instance

Azure Synapse Analytics (dedicated pools only)
Analysis Services models

Reporting Services reports | SQL Server 2008 (10.0.x) - SQL Server 2019 (15.x)
Integration Services packages | SQL Server 2012 (11.x) - SQL Server 2022 (16.x)
[](https://learn.microsoft.com/en-us/sql/ssdt/download-sql-server-data-tools-ssdt?view=sql-server-ver17&tabs=vs2026#offline-installation)
## Offline installation
For scenarios where offline installation is required, such as low bandwidth or isolated networks, SSDT is available for offline installation. Two approaches are available:
  * For a single machine, [Download All, then install](https://learn.microsoft.com/en-us/visualstudio/install/create-an-offline-installation-of-visual-studio#use-the-download-all-then-install-feature)
  * For installation on one or more machines, [use the Visual Studio bootstrapper from the command line](https://learn.microsoft.com/en-us/visualstudio/install/create-an-offline-installation-of-visual-studio#use-the-command-line-to-create-a-local-layout)


For more details, you can follow the [Step-by-Step Guidelines for Offline Installation](https://learn.microsoft.com/en-us/visualstudio/install/create-an-offline-installation-of-visual-studio)
[](https://learn.microsoft.com/en-us/sql/ssdt/download-sql-server-data-tools-ssdt?view=sql-server-ver17&tabs=vs2026#license-terms-for-visual-studio)
## License terms for Visual Studio
To understand the license terms and use cases for Visual Studio, refer to [Visual Studio License Directory](https://visualstudio.microsoft.com/license-terms/). For example, if you're using the Community Edition of Visual Studio for SQL Server Data Tools, review the end user licensing agreement (EULA) for that specific edition of Visual Studio in the Visual Studio License Directory.
[](https://learn.microsoft.com/en-us/sql/ssdt/download-sql-server-data-tools-ssdt?view=sql-server-ver17&tabs=vs2026#previous-versions)
## Previous versions
To download and install SSDT for Visual Studio 2017, or an older version of SSDT, see [Previous releases of SQL Server Data Tools (SSDT and SSDT-BI)](https://learn.microsoft.com/en-us/sql/ssdt/previous-releases-of-sql-server-data-tools-ssdt-and-ssdt-bi?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/ssdt/download-sql-server-data-tools-ssdt?view=sql-server-ver17&tabs=vs2026#related-content)
## Related content
  * [SSDT Team Blog](https://learn.microsoft.com/en-us/archive/blogs/ssdt/)
  * [DACFx API Reference](https://learn.microsoft.com/en-us/dotnet/api/microsoft.sqlserver.dac)
  * [SQL Database Projects extension](https://learn.microsoft.com/en-us/sql/tools/visual-studio-code-extensions/sql-database-projects/sql-database-projects-extension?view=sql-server-ver17)
  * [What are SQL database projects?](https://learn.microsoft.com/en-us/sql/tools/sql-database-projects/sql-database-projects?view=sql-server-ver17)
  * [SSIS How to Create an ETL Package](https://learn.microsoft.com/en-us/sql/integration-services/ssis-how-to-create-an-etl-package?view=sql-server-ver17)
  * [Analysis Services tutorials](https://learn.microsoft.com/en-us/analysis-services/analysis-services-tutorials-ssas)
  * [Create a basic table report (SSRS tutorial)](https://learn.microsoft.com/en-us/sql/reporting-services/create-a-basic-table-report-ssrs-tutorial?view=sql-server-ver17)


[](https://learn.microsoft.com/en-us/sql/ssdt/download-sql-server-data-tools-ssdt?view=sql-server-ver17&tabs=vs2026#-get-help)
##  ![](https://learn.microsoft.com/en-us/sql/includes/media/info-tip.svg?view=sql-server-ver17) Get help
  * [Microsoft Q & A (SQL Server)](https://learn.microsoft.com/en-us/answers/products/sql-server)
  * [Microsoft SQL Server License Terms and Information](https://www.microsoft.com/licensing/product-licensing/sql-server)
  * [Support options for business users](https://support.microsoft.com/support-for-business)
  * [Additional SQL Server help and feedback](https://learn.microsoft.com/en-us/sql/sql-server/sql-server-get-help?view=sql-server-ver17)


[](https://learn.microsoft.com/en-us/sql/ssdt/download-sql-server-data-tools-ssdt?view=sql-server-ver17&tabs=vs2026#-contribute-to-sql-documentation)
##  ![](https://learn.microsoft.com/en-us/sql/includes/media/edit-topic-pencil.svg?view=sql-server-ver17) Contribute to SQL documentation
Did you know that you can edit SQL content yourself? If you do so, not only do you help improve our documentation, but you also get credited as a contributor to the page.
For more information, see [Edit Microsoft Learn documentation](https://learn.microsoft.com/en-us/sql/sql-server/sql-server-docs-contribute?view=sql-server-ver17).
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
  * [ SQL Server Data Tools - SQL Server Data Tools (SSDT) ](https://learn.microsoft.com/en-us/sql/ssdt/sql-server-data-tools?source=recommendations)
View resources on database development tasks that you can accomplish with SQL Server Data Tools, such as designing tables and creating feature extensions.
  * [ Previous Releases of SQL Server Data Tools (SSDT) - SQL Server Data Tools (SSDT) ](https://learn.microsoft.com/en-us/sql/ssdt/previous-releases-of-sql-server-data-tools-ssdt-and-ssdt-bi?source=recommendations)
See how to install 2017 and earlier versions of SSDT and SSDT-BI. View the release notes for all versions of SQL Server Data Tools (SSDT) that work with Visual Studio 2017 and earlier Visual Studio versions.
  * [ SSIS Projects Extension for Visual Studio 2022+ Troubleshooting Guide - SQL Server Data Tools (SSDT) ](https://learn.microsoft.com/en-us/sql/ssdt/ssis-vs2022-troubleshooting-guide?source=recommendations)
SSIS Projects extension for Visual Studio 2022+ troubleshooting guide
  * [ Install Business Intelligence Features - SQL Server ](https://learn.microsoft.com/en-us/sql/sql-server/install/install-sql-server-business-intelligence-features?source=recommendations)
This article provides links to information to install SQL Server features that are part of the Microsoft Business Intelligence platform.
  * [ SQL Server Data Tools and Visual Studio 2017 - License Terms ](https://learn.microsoft.com/en-us/legal/sql/sql-server-data-tools-license-terms-vs2017?source=recommendations)
Learn more about: SQL Server Data Tools & SQL Server Data Tools for Visual Studio 2017 - license terms
  * [ Connect to an Existing Database in SSDT - SQL Server Data Tools (SSDT) ](https://learn.microsoft.com/en-us/sql/ssdt/connect-to-an-existing-database-in-sql-server-data-tools?source=recommendations)
Connect to an existing database in SSDT using SQL Server Object Explorer.
  * [ SSIS Projects Extension for Visual Studio 2019 Troubleshooting Guide - SQL Server Data Tools (SSDT) ](https://learn.microsoft.com/en-us/sql/ssdt/ssis-vs2019-troubleshooting-guide?source=recommendations)
SSIS Projects extension for Visual Studio 2019 troubleshooting guide


Show 4 more
Module
[ Start developing for finance and operations apps by using Visual Studio - Training ](https://learn.microsoft.com/en-us/training/modules/customize-visual-studio-finance-operations/?source=recommendations)
Explore Visual Studio's capabilities for finance and operations app development, including project creation, data synchronization, and element design.
Certification
[ Microsoft Certified: Azure Database Administrator Associate - Certifications ](https://learn.microsoft.com/en-us/credentials/certifications/azure-database-administrator-associate/?source=recommendations)
Administer an SQL Server database infrastructure for cloud, on-premises and hybrid relational databases using the Microsoft PaaS relational database offerings.
Mar 8, 4 PM - Mar 8, 4 PM
Experiment with what's next in AI-driven apps and agent design
* * *
  * Last updated on 02/06/2026


##  In this article
  1. [Install SSDT with Visual Studio](https://learn.microsoft.com/en-us/sql/ssdt/download-sql-server-data-tools-ssdt?view=sql-server-ver17&tabs=vs2026#install-ssdt-with-visual-studio)
  2. [Install extensions for Analysis Services, Integration Services, and Reporting Services](https://learn.microsoft.com/en-us/sql/ssdt/download-sql-server-data-tools-ssdt?view=sql-server-ver17&tabs=vs2026#install-extensions-for-analysis-services-integration-services-and-reporting-services)
  3. [Supported SQL versions](https://learn.microsoft.com/en-us/sql/ssdt/download-sql-server-data-tools-ssdt?view=sql-server-ver17&tabs=vs2026#supported-sql-versions)
  4. [Offline installation](https://learn.microsoft.com/en-us/sql/ssdt/download-sql-server-data-tools-ssdt?view=sql-server-ver17&tabs=vs2026#offline-installation)
  5. [License terms for Visual Studio](https://learn.microsoft.com/en-us/sql/ssdt/download-sql-server-data-tools-ssdt?view=sql-server-ver17&tabs=vs2026#license-terms-for-visual-studio)
  6. [Previous versions](https://learn.microsoft.com/en-us/sql/ssdt/download-sql-server-data-tools-ssdt?view=sql-server-ver17&tabs=vs2026#previous-versions)
  7. [Related content](https://learn.microsoft.com/en-us/sql/ssdt/download-sql-server-data-tools-ssdt?view=sql-server-ver17&tabs=vs2026#related-content)
  8. [Get help](https://learn.microsoft.com/en-us/sql/ssdt/download-sql-server-data-tools-ssdt?view=sql-server-ver17&tabs=vs2026#-get-help)
  9. [Contribute to SQL documentation](https://learn.microsoft.com/en-us/sql/ssdt/download-sql-server-data-tools-ssdt?view=sql-server-ver17&tabs=vs2026#-contribute-to-sql-documentation)


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
[ Sign in ](https://learn.microsoft.com/en-us/sql/ssdt/download-sql-server-data-tools-ssdt?view=sql-server-ver17&tabs=vs2026)
[English (United States)](https://learn.microsoft.com/en-us/locale?target=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fsql%2Fssdt%2Fdownload-sql-server-data-tools-ssdt%3Fview%3Dsql-server-ver17)
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
