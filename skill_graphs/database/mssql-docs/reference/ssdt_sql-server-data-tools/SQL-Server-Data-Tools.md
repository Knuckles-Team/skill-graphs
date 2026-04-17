# SQL Server Data Tools
Feedback
Summarize this article for me
##  In this article
  1. [Release notes](https://learn.microsoft.com/en-us/sql/ssdt/sql-server-data-tools?view=sql-server-ver17#release-notes)
  2. [Core SQL Server Data Tools](https://learn.microsoft.com/en-us/sql/ssdt/sql-server-data-tools?view=sql-server-ver17#core-sql-server-data-tools)
  3. [SDK-style SQL projects (preview)](https://learn.microsoft.com/en-us/sql/ssdt/sql-server-data-tools?view=sql-server-ver17#sdk-style-sql-projects-preview)
  4. [Related content](https://learn.microsoft.com/en-us/sql/ssdt/sql-server-data-tools?view=sql-server-ver17#related-content)


**SQL Server Data Tools (SSDT)** is a set of development tools in Visual Studio with focus on building SQL Server databases and Azure SQL databases. SSDT can be extended to Analysis Services (AS) data models, Integration Services (IS) packages, and Reporting Services (RS) reports with their corresponding extensions. SSDT allows you to design and deploy SQL objects with the same project concept as other application development tools. The **SQL projects** capability extends to CI/CD pipelines, enabling you to automate the build and deployment of your database projects with the [SqlPackage CLI](https://learn.microsoft.com/en-us/sql/tools/sqlpackage/sqlpackage?view=sql-server-ver17).
![Screenshot of graphic with SQL Server Data Tools component and three extensions.](https://learn.microsoft.com/en-us/sql/ssdt/media/sql-server-data-tools/install-layout.png?view=sql-server-ver17)
The core of SQL Server Data Tools functionality is available as a workload component with Visual Studio. The Visual Studio extensions are available from the Visual Studio Marketplace and more information on installing SSDT can be found at [Install SQL Server Data Tools (SSDT) for Visual Studio](https://learn.microsoft.com/en-us/sql/ssdt/download-sql-server-data-tools-ssdt?view=sql-server-ver17).
SDK-style SQL projects in Visual Studio are available as part of the **SQL Server Data Tools, SDK-style (preview)** feature for Visual Studio 2022, separate from the original SSDT. The SDK-style project format is based on the new SDK-style projects introduced in .NET Core and is the format used by the SQL Database Projects extension for Visual Studio Code. For more information, see [SQL Server Data Tools, SDK-style (preview)](https://learn.microsoft.com/en-us/sql/ssdt/sql-server-data-tools-sdk-style?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/ssdt/sql-server-data-tools?view=sql-server-ver17#release-notes)
## Release notes
The latest release notes for SQL Server Data Tools with Visual Studio 2022 and Visual Studio 2026 can be found in the following locations:
  * SQL Server Data Tools (SSDT) release notes are listed with the release notes for [Visual Studio 2022](https://learn.microsoft.com/en-us/visualstudio/releases/2022/release-notes) and [Visual Studio 2026](https://learn.microsoft.com/en-us/visualstudio/releases/2026/release-notes).
  * Analysis Services (SSAS) extension release notes are listed on the
  * Integration Services (SSIS) extension release notes are listed on the
  * Reporting Services (SSRS) extension release notes are listed on the


The release notes for SQL Server Data Tools with Visual Studio 2019 can be found in the following locations:
  * SQL Server Data Tools (SSDT) release notes are listed with the [release notes for Visual Studio 2019](https://learn.microsoft.com/en-us/visualstudio/releases/2019/release-notes)
  * Analysis Services (SSAS) extension release notes are listed on the
  * Integration Services (SSIS) extension release notes are listed on the
  * Reporting Services (SSRS) extension release notes are listed on the


For information about SQL Server Data Tools with Visual Studio 2017, see [Previous releases of SQL Server Data Tools (SSDT and SSDT-BI)](https://learn.microsoft.com/en-us/sql/ssdt/previous-releases-of-sql-server-data-tools-ssdt-and-ssdt-bi?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/ssdt/sql-server-data-tools?view=sql-server-ver17#core-sql-server-data-tools)
## Core SQL Server Data Tools
SQL Server Data Tools (SSDT) transforms database development by introducing a ubiquitous, declarative model (SQL database projects) that spans all the phases of database development inside Visual Studio. SSDT Transact-SQL design capabilities can be used to build, debug, maintain, and refactor databases. You can work with a database project or directly connect to a database instance on or off-premises.
Developers can use the familiar Visual Studio environment for comprehensive database development. The suite of tools includes code navigation, IntelliSense, and language support akin to what is available for C# and Visual Basic, along with specialized validation, debugging, and declarative editing within the Transact-SQL editor. SQL Server Data Tools (SSDT) also offers a visual table designer for streamlined creation and modification of tables in database projects or connected instances. In team-based settings, version control is available for all project files, enhancing collaboration. When it's time to deploy, projects can be published across all supported SQL platforms, such as SQL Database and SQL Server.
The SQL Server Object Explorer in Visual Studio offers a view of your database objects like SQL Server Management Studio. SQL Server Object Explorer lets you do light-duty database administration and design work. You can easily create, edit, rename, and delete tables, stored procedures, types, and functions. You can also edit table data, compare schemas, or execute queries using contextual menus from the SQL Server Object Explorer.
For more information about SQL projects and database development tasks that you can accomplish with SQL Server Data Tools, see [What are SQL database projects?](https://learn.microsoft.com/en-us/sql/tools/sql-database-projects/sql-database-projects?view=sql-server-ver17)
[](https://learn.microsoft.com/en-us/sql/ssdt/sql-server-data-tools?view=sql-server-ver17#sdk-style-sql-projects-preview)
## SDK-style SQL projects (preview)
Support for the Microsoft.Build.Sql project SDK is available in preview in Visual Studio 2022 as the next generation of SQL projects. The SDK-style SQL projects are based on the .NET SDK-style project format and are designed to be more flexible and extensible than the original SQL projects. The SDK-style SQL projects are available in Visual Studio 2022 as an optional component "SQL Server Data Tools, SDK-style (preview)" and aren't available in Visual Studio 2026. For more information about the SDK-style SQL projects and Visual Studio, see [SQL Server Data Tools, SDK-style (preview)](https://learn.microsoft.com/en-us/sql/ssdt/sql-server-data-tools-sdk-style?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/ssdt/sql-server-data-tools?view=sql-server-ver17#related-content)
## Related content
  * [What are SQL database projects?](https://learn.microsoft.com/en-us/sql/tools/sql-database-projects/sql-database-projects?view=sql-server-ver17)
  * [SQL Server Analysis Services tutorials](https://learn.microsoft.com/en-us/analysis-services/analysis-services-tutorials-ssas)
  * [SQL Server Reporting Services tools](https://learn.microsoft.com/en-us/sql/reporting-services/tools/reporting-services-tools?view=sql-server-ver17)
  * [Integration Services (SSIS) Projects and Solutions](https://learn.microsoft.com/en-us/sql/integration-services/integration-services-ssis-projects-and-solutions?view=sql-server-ver17)


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
  * [ Previous Releases of SQL Server Data Tools (SSDT) - SQL Server Data Tools (SSDT) ](https://learn.microsoft.com/en-us/sql/ssdt/previous-releases-of-sql-server-data-tools-ssdt-and-ssdt-bi?source=recommendations)
See how to install 2017 and earlier versions of SSDT and SSDT-BI. View the release notes for all versions of SQL Server Data Tools (SSDT) that work with Visual Studio 2017 and earlier Visual Studio versions.
  * [ Connect to an Existing Database in SSDT - SQL Server Data Tools (SSDT) ](https://learn.microsoft.com/en-us/sql/ssdt/connect-to-an-existing-database-in-sql-server-data-tools?source=recommendations)
Connect to an existing database in SSDT using SQL Server Object Explorer.
  * [ Install SQL Server Data Tools (SSDT) - SQL Server Data Tools (SSDT) ](https://learn.microsoft.com/en-us/sql/ssdt/download-sql-server-data-tools-ssdt?source=recommendations)
Learn about SQL Server Data Tools (SSDT). See how to install this database development tool set with Visual Studio 2019 and 2022.
  * [ SQL Server Data Tools, SDK-Style (Preview) - SQL Server Data Tools (SSDT) ](https://learn.microsoft.com/en-us/sql/ssdt/sql-server-data-tools-sdk-style?source=recommendations)
SDK-style SQL projects in Visual Studio enable the next generation of SQL projects.
  * [ SSIS Projects Extension for Visual Studio 2022+ Troubleshooting Guide - SQL Server Data Tools (SSDT) ](https://learn.microsoft.com/en-us/sql/ssdt/ssis-vs2022-troubleshooting-guide?source=recommendations)
SSIS Projects extension for Visual Studio 2022+ troubleshooting guide


Show 2 more
Module
[ Develop for Azure SQL Database - Training ](https://learn.microsoft.com/en-us/training/modules/develop-azure-sql-database/?source=recommendations)
Learn how to create and configure an Azure SQL Database. You'll use SQL Database Projects in VS Code, including installing the extension, importing, and modifying a schema. Additionally, you'll build and deploy database projects in GitHub Actions and Azure Pipelines, and automate and invoke the publishing of a database.
Mar 8, 4 PM - Mar 8, 4 PM
Experiment with what's next in AI-driven apps and agent design
* * *
  * Last updated on 12/03/2025


##  In this article
  1. [Release notes](https://learn.microsoft.com/en-us/sql/ssdt/sql-server-data-tools?view=sql-server-ver17#release-notes)
  2. [Core SQL Server Data Tools](https://learn.microsoft.com/en-us/sql/ssdt/sql-server-data-tools?view=sql-server-ver17#core-sql-server-data-tools)
  3. [SDK-style SQL projects (preview)](https://learn.microsoft.com/en-us/sql/ssdt/sql-server-data-tools?view=sql-server-ver17#sdk-style-sql-projects-preview)
  4. [Related content](https://learn.microsoft.com/en-us/sql/ssdt/sql-server-data-tools?view=sql-server-ver17#related-content)


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
[ Sign in ](https://learn.microsoft.com/en-us/sql/ssdt/sql-server-data-tools?view=sql-server-ver17)
[English (United States)](https://learn.microsoft.com/en-us/locale?target=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fsql%2Fssdt%2Fsql-server-data-tools%3Fview%3Dsql-server-ver17)
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
