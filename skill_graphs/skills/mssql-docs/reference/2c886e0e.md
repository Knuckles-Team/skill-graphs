# Import and Export Data with the SQL Server Import and Export Wizard
Feedback
Summarize this article for me
##  In this article
  1. [Get the wizard](https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/import-and-export-data-with-the-sql-server-import-and-export-wizard?view=sql-server-ver17#get-the-wizard)
  2. [What happens when I run the wizard?](https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/import-and-export-data-with-the-sql-server-import-and-export-wizard?view=sql-server-ver17#what-happens-when-i-run-the-wizard)
  3. [What sources and destinations can I use?](https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/import-and-export-data-with-the-sql-server-import-and-export-wizard?view=sql-server-ver17#wizardSources)
  4. [How do I connect to my data?](https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/import-and-export-data-with-the-sql-server-import-and-export-wizard?view=sql-server-ver17#how-do-i-connect-to-my-data)
  5. [What permissions do I need?](https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/import-and-export-data-with-the-sql-server-import-and-export-wizard?view=sql-server-ver17#what-permissions-do-i-need)
  6. [Get help while the wizard is running](https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/import-and-export-data-with-the-sql-server-import-and-export-wizard?view=sql-server-ver17#get-help-while-the-wizard-is-running)
  7. [The wizard uses SQL Server Integration Services (SSIS)](https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/import-and-export-data-with-the-sql-server-import-and-export-wizard?view=sql-server-ver17#wizardSSIS)
  8. [What's next?](https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/import-and-export-data-with-the-sql-server-import-and-export-wizard?view=sql-server-ver17#whats-next)
  9. [See also](https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/import-and-export-data-with-the-sql-server-import-and-export-wizard?view=sql-server-ver17#see-also)

Show 5 more
**Applies to:** ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) SSIS Integration Runtime in Azure Data Factory
SQL Server Import and Export Wizard is a simple way to copy data from a source to a destination. This overview describes the data sources that the wizard can use as sources and destinations, as well as the permissions you need to run the wizard.
[](https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/import-and-export-data-with-the-sql-server-import-and-export-wizard?view=sql-server-ver17#get-the-wizard)
## Get the wizard
If you want to run the wizard, but you don't have Microsoft SQL Server installed on your computer, you can install the SQL Server Import and Export Wizard by installing SQL Server Data Tools (SSDT). For more info, see [Download SQL Server Data Tools (SSDT)](https://learn.microsoft.com/en-us/sql/ssdt/download-sql-server-data-tools-ssdt?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/import-and-export-data-with-the-sql-server-import-and-export-wizard?view=sql-server-ver17#what-happens-when-i-run-the-wizard)
## What happens when I run the wizard?
  * **See the list of steps.** For a description of the steps in the wizard, see [Steps in the SQL Server Import and Export Wizard](https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/steps-in-the-sql-server-import-and-export-wizard?view=sql-server-ver17). There's also a separate page of documentation for each page of the wizard.
- or -
  * **See an example.** For a quick look at the several screens you see in a typical session, take a look at this simple example on a single page - [Get started with this simple example of the Import and Export Wizard](https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/get-started-with-this-simple-example-of-the-import-and-export-wizard?view=sql-server-ver17).


[](https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/import-and-export-data-with-the-sql-server-import-and-export-wizard?view=sql-server-ver17#wizardSources)
##  What sources and destinations can I use?
The SQL Server Import and Export Wizard can copy data to and from the data sources listed in the following table. To connect to some of these data sources, you may have to download and install additional files.
Expand table
Data source | Do I have to download additional files?
---|---
**Enterprise databases**
SQL Server, Oracle, DB2, and others. | SQL Server or SQL Server Data Tools (SSDT) installs the files that you need to connect to SQL Server. But SSDT doesn't install all the files that you need to connect to other enterprise databases such as Oracle or IBM Db2.

To connect to an enterprise database, you typically have to have two things:

1. **Client software**. If you already have the client software installed for your enterprise database system, then you typically have what you need to make a connection. If you don't have the client software installed, ask the database administrator how to install a licensed copy.

2. **Drivers or providers**. Microsoft installs drivers and providers to connect to Oracle. To connect to IBM Db2, get the Microsoft OLEDB Provider for DB2 v5.0 for Microsoft SQL Server from the [Microsoft SQL Server 2016 Feature Pack](https://www.microsoft.com/download/details.aspx?id=56833).

For more info, see [Connect to a SQL Server Data Source](https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/connect-to-a-sql-server-data-source-sql-server-import-and-export-wizard?view=sql-server-ver17) or [Connect to an Oracle Data Source](https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/connect-to-an-oracle-data-source-sql-server-import-and-export-wizard?view=sql-server-ver17).
**Text files** (flat files) | No additional files required.

For more info, see [Connect to a Flat File Data Source](https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/connect-to-a-flat-file-data-source-sql-server-import-and-export-wizard?view=sql-server-ver17).
**Microsoft Excel and Microsoft Access files** | Microsoft Office doesn't install all the files that you need to connect to Excel and Access files as data sources. Get the following download - [Microsoft Access Database Engine 2016 Redistributable](https://www.microsoft.com/download/details.aspx?id=54920).

For more info, see [Connect to an Excel Data Source](https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/connect-to-an-excel-data-source-sql-server-import-and-export-wizard?view=sql-server-ver17) or [Connect to an Access Data Source](https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/connect-to-an-access-data-source-sql-server-import-and-export-wizard?view=sql-server-ver17).
**Azure data sources**
Currently only Azure Blob Storage. | SQL Server Data Tools don't install the files that you need to connect to Azure Blob Storage as a data source. Get the following download - [Microsoft SQL Server 2016 Integration Services Feature Pack for Azure](https://www.microsoft.com/download/details.aspx?id=49492).

For more info, see [Connect to Azure Blob Storage](https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/connect-to-azure-blob-storage-sql-server-import-and-export-wizard?view=sql-server-ver17).
**Open source databases**
PostgreSQL, MySQL, and others. | To connect to these data sources, you have to download additional files.

- For **PostgreSQL** , see [Connect to a PostgreSQL Data Source](https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/connect-to-a-postgresql-data-source-sql-server-import-and-export-wizard?view=sql-server-ver17).
- For **MySQL** , see [Connect to a MySQL Data Source](https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/connect-to-a-mysql-data-source-sql-server-import-and-export-wizard?view=sql-server-ver17).
**Any other data source for which a driver or provider is available** | You typically have to download additional files to connect to the following types of data sources.

- Any source for which an **ODBC driver** is available. For more info, see [Connect to an ODBC Data Source](https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/connect-to-an-odbc-data-source-sql-server-import-and-export-wizard?view=sql-server-ver17).
- Any source for which a **.Net Framework Data Provider** is available.
- Any source for which an **OLE DB Provider** is available.

Third-party components that provide source and destination capabilities for other data sources are sometimes marketed as add-on products for SQL Server Integration Services (SSIS).
[](https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/import-and-export-data-with-the-sql-server-import-and-export-wizard?view=sql-server-ver17#how-do-i-connect-to-my-data)
## How do I connect to my data?
For info about how to connect to a commonly used data source, see one of the following pages:
  * [Connect to SQL Server](https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/connect-to-a-sql-server-data-source-sql-server-import-and-export-wizard?view=sql-server-ver17)
  * [Connect to Oracle](https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/connect-to-an-oracle-data-source-sql-server-import-and-export-wizard?view=sql-server-ver17)
  * [Connect to flat files (text files)](https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/connect-to-a-flat-file-data-source-sql-server-import-and-export-wizard?view=sql-server-ver17)
  * [Connect to Excel](https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/connect-to-an-excel-data-source-sql-server-import-and-export-wizard?view=sql-server-ver17)
  * [Connect to Access](https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/connect-to-an-access-data-source-sql-server-import-and-export-wizard?view=sql-server-ver17)
  * [Connect to Azure Blob Storage](https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/connect-to-azure-blob-storage-sql-server-import-and-export-wizard?view=sql-server-ver17)
  * [Connect with ODBC](https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/connect-to-an-odbc-data-source-sql-server-import-and-export-wizard?view=sql-server-ver17)
  * [Connect to PostgreSQL](https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/connect-to-a-postgresql-data-source-sql-server-import-and-export-wizard?view=sql-server-ver17)
  * [Connect to MySQL](https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/connect-to-a-mysql-data-source-sql-server-import-and-export-wizard?view=sql-server-ver17)


For info about how to connect to a data source that's not listed here, see
[](https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/import-and-export-data-with-the-sql-server-import-and-export-wizard?view=sql-server-ver17#what-permissions-do-i-need)
## What permissions do I need?
To run the SQL Server Import and Export Wizard successfully, you have to have at least the following permissions. If you already work with your data source and destination, you probably already have the permissions that you need.
Expand table
You need permissions to do these things | If you're connecting to SQL Server, you need these specific permissions
---|---
Connect to the source and destination databases or file shares. | Server and database login rights.
Export or read data from the source database or file. | SELECT permissions on the source tables and views.
Import or write data to the destination database or file. | INSERT permissions on the destination tables.
Create the destination database or file, if applicable. | CREATE DATABASE or CREATE TABLE permissions.
Save the SSIS package created by the wizard, if applicable. | If you want to save the package to SQL Server, permissions sufficient to save the package to the **msdb** database.
[](https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/import-and-export-data-with-the-sql-server-import-and-export-wizard?view=sql-server-ver17#get-help-while-the-wizard-is-running)
## Get help while the wizard is running
Tap the F1 key from any page or dialog box of the wizard to see documentation for the current page.
[](https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/import-and-export-data-with-the-sql-server-import-and-export-wizard?view=sql-server-ver17#wizardSSIS)
##  The wizard uses SQL Server Integration Services (SSIS)
The wizard uses SQL Server Integration Services (SSIS) to copy data. SSIS is a tool for extracting, transforming, and loading data (ETL). The pages of the wizard use some of the language of SSIS.
In SSIS, the basic unit is the **package**. The wizard creates an SSIS package in memory as you move through the pages of the wizard and specify options.
At the end of the wizard, if you have SQL Server Standard Edition or higher installed, you can optionally save the SSIS package. Later you can reuse the package and extend it by using SSIS Designer to add tasks, transformations, and event-driven logic. The SQL Server Import and Export Wizard is the simplest way to create a basic Integration Services package that copies data from a source to a destination.
For more info about SSIS, see [SQL Server Integration Services](https://learn.microsoft.com/en-us/sql/integration-services/sql-server-integration-services?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/import-and-export-data-with-the-sql-server-import-and-export-wizard?view=sql-server-ver17#whats-next)
## What's next?
Start the wizard. For more info, see [Start the SQL Server Import and Export Wizard](https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/start-the-sql-server-import-and-export-wizard?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/import-and-export-data-with-the-sql-server-import-and-export-wizard?view=sql-server-ver17#see-also)
## See also
[Get started with this simple example of the Import and Export Wizard](https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/get-started-with-this-simple-example-of-the-import-and-export-wizard?view=sql-server-ver17)
[Data Type Mapping in the SQL Server Import and Export Wizard](https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/data-type-mapping-in-the-sql-server-import-and-export-wizard?view=sql-server-ver17)
* * *
##  Additional resources
  * [ Start the SQL Server Import and Export Wizard - Integration Services (SSIS) ](https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/start-the-sql-server-import-and-export-wizard?source=recommendations)
Start the SQL Server Import and Export Wizard
  * [ Welcome to SQL Server Import and Export Wizard - SQL Server Integration Services (SSIS) ](https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/welcome-to-sql-server-import-and-export-wizard?source=recommendations)
Welcome to SQL Server Import and Export Wizard
  * [ Steps in the SQL Server Import and Export Wizard - SQL Server Integration Services (SSIS) ](https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/steps-in-the-sql-server-import-and-export-wizard?source=recommendations)
Steps in the SQL Server Import and Export Wizard
  * [ Connect to Data Sources (SQL Server Import and Export Wizard) - SQL Server Integration Services (SSIS) ](https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/connect-to-data-sources-with-the-sql-server-import-and-export-wizard?source=recommendations)
Connect to Data Sources with the SQL Server Import and Export Wizard
  * [ Get started with this simple example of the Import and Export Wizard - SQL Server Integration Services (SSIS) ](https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/get-started-with-this-simple-example-of-the-import-and-export-wizard?source=recommendations)
Get started with this simple example of the Import and Export Wizard
  * [ Connect to a Flat File Data Source (SQL Server Import and Export Wizard) - SQL Server Integration Services (SSIS) ](https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/connect-to-a-flat-file-data-source-sql-server-import-and-export-wizard?source=recommendations)
Connect to a Flat File Data Source (SQL Server Import and Export Wizard)
  * [ Choose a Data Source (SQL Server Import and Export Wizard) - SQL Server Integration Services (SSIS) ](https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/choose-a-data-source-sql-server-import-and-export-wizard?source=recommendations)
Choose a Data Source (SQL Server Import and Export Wizard)
  * [ Choose a Destination (SQL Server Import and Export Wizard) - SQL Server Integration Services (SSIS) ](https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/choose-a-destination-sql-server-import-and-export-wizard?source=recommendations)
Choose a Destination (SQL Server Import and Export Wizard)


Show 5 more
Module
[ Explore data manipulation options in Azure SQL Database - Training ](https://learn.microsoft.com/en-us/training/modules/explore-data-manipulation-azure-sql-database/?source=recommendations)
Learn how to invoke REST endpoints in Azure SQL Database and manipulate data using Azure Functions. Also, explore various tools and options for importing and exporting data to and from Azure SQL Database.
Certification
[ Microsoft Certified: Azure Database Administrator Associate - Certifications ](https://learn.microsoft.com/en-us/credentials/certifications/azure-database-administrator-associate/?source=recommendations)
Administer an SQL Server database infrastructure for cloud, on-premises and hybrid relational databases using the Microsoft PaaS relational database offerings.
Mar 8, 4 PM - Mar 8, 4 PM
Experiment with what's next in AI-driven apps and agent design
* * *
  * Last updated on 09/04/2024


##  In this article
  1. [Get the wizard](https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/import-and-export-data-with-the-sql-server-import-and-export-wizard?view=sql-server-ver17#get-the-wizard)
  2. [What happens when I run the wizard?](https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/import-and-export-data-with-the-sql-server-import-and-export-wizard?view=sql-server-ver17#what-happens-when-i-run-the-wizard)
  3. [What sources and destinations can I use?](https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/import-and-export-data-with-the-sql-server-import-and-export-wizard?view=sql-server-ver17#wizardSources)
  4. [How do I connect to my data?](https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/import-and-export-data-with-the-sql-server-import-and-export-wizard?view=sql-server-ver17#how-do-i-connect-to-my-data)
  5. [What permissions do I need?](https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/import-and-export-data-with-the-sql-server-import-and-export-wizard?view=sql-server-ver17#what-permissions-do-i-need)
  6. [Get help while the wizard is running](https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/import-and-export-data-with-the-sql-server-import-and-export-wizard?view=sql-server-ver17#get-help-while-the-wizard-is-running)
  7. [The wizard uses SQL Server Integration Services (SSIS)](https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/import-and-export-data-with-the-sql-server-import-and-export-wizard?view=sql-server-ver17#wizardSSIS)
  8. [What's next?](https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/import-and-export-data-with-the-sql-server-import-and-export-wizard?view=sql-server-ver17#whats-next)
  9. [See also](https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/import-and-export-data-with-the-sql-server-import-and-export-wizard?view=sql-server-ver17#see-also)


##
Ask Learn
Preview
Ask Learn is an AI assistant that can answer questions, clarify concepts, and define terms using trusted Microsoft documentation.
Please sign in to use Ask Learn.
[ Sign in ](https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/import-and-export-data-with-the-sql-server-import-and-export-wizard?view=sql-server-ver17)
[English (United States)](https://learn.microsoft.com/en-us/locale?target=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fsql%2Fintegration-services%2Fimport-export-data%2Fimport-and-export-data-with-the-sql-server-import-and-export-wizard%3Fview%3Dsql-server-ver17)
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
