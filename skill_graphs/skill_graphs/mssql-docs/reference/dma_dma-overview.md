Version SQL Server 2022
  * Analytics Platform System (PDW)
    * [2016-AU7](https://learn.microsoft.com/en-us/previous-versions/sql/dma/dma-overview?view=aps-pdw-2016-au7)
    * [2016-AU6](https://learn.microsoft.com/en-us/previous-versions/sql/dma/dma-overview?view=aps-pdw-2016)
  * [Azure SQL Database](https://learn.microsoft.com/en-us/previous-versions/sql/dma/dma-overview?view=azuresqldb-current)
  * [Azure SQL Managed Instance](https://learn.microsoft.com/en-us/previous-versions/sql/dma/dma-overview?view=azuresqldb-mi-current)
  * [Azure Synapse Analytics](https://learn.microsoft.com/en-us/previous-versions/sql/dma/dma-overview?view=azure-sqldw-latest)
  * [Fabric Data Warehouse](https://learn.microsoft.com/en-us/previous-versions/sql/dma/dma-overview?view=fabric)
  * [Fabric SQL database](https://learn.microsoft.com/en-us/previous-versions/sql/dma/dma-overview?view=fabric-sqldb)
  * SQL Server
    * [2025](https://learn.microsoft.com/en-us/previous-versions/sql/dma/dma-overview?view=sql-server-ver17)
    * [2022](https://learn.microsoft.com/en-us/previous-versions/sql/dma/dma-overview?view=sql-server-ver16)
    * [2019](https://learn.microsoft.com/en-us/previous-versions/sql/dma/dma-overview?view=sql-server-ver15)
    * [2017](https://learn.microsoft.com/en-us/previous-versions/sql/dma/dma-overview?view=sql-server-2017)
    * [2016](https://learn.microsoft.com/en-us/previous-versions/sql/dma/dma-overview?view=sql-server-2016)
  * SQL Server on Linux
    * [2025](https://learn.microsoft.com/en-us/previous-versions/sql/dma/dma-overview?view=sql-server-linux-ver17)
    * [2022](https://learn.microsoft.com/en-us/previous-versions/sql/dma/dma-overview?view=sql-server-linux-ver16)
    * [2019](https://learn.microsoft.com/en-us/previous-versions/sql/dma/dma-overview?view=sql-server-linux-ver15)
    * [2017](https://learn.microsoft.com/en-us/previous-versions/sql/dma/dma-overview?view=sql-server-linux-2017)


Search
Suggestions will filter as you type
  * [SQL Server](https://learn.microsoft.com/en-us/previous-versions/sql/?view=sql-server-ver16)
  * [SQL Server - Current Version](https://learn.microsoft.com/en-us/sql?view=sql-server-ver16)
  * [SQL Server 2014](https://learn.microsoft.com/en-us/previous-versions/sql/2014/?view=sql-server-ver16)
  * [SQL Server 2012](https://learn.microsoft.com/en-us/previous-versions/sql/sql-server-2012/ms130214\(v=sql.110\)?view=sql-server-ver16)
  * [SQL Server 2008 R2](https://learn.microsoft.com/en-us/previous-versions/sql/sql-server-2008-r2?view=sql-server-ver16)
  * [SQL Server 2008](https://learn.microsoft.com/en-us/previous-versions/sql/sql-server-2008?view=sql-server-ver16)
  * [SQL Server 2005](https://learn.microsoft.com/en-us/previous-versions/sql/sql-server-2005?view=sql-server-ver16)
  * [SQL Server Compact](https://learn.microsoft.com/en-us/previous-versions/sql/compact?view=sql-server-ver16)
  * [Microsoft StreamInsight](https://learn.microsoft.com/en-us/previous-versions/sql/streaminsight?view=sql-server-ver16)


Table of contents  Exit editor mode
  1. [ Learn ](https://learn.microsoft.com/en-us/?view=sql-server-ver16)
  2. [ SQL Server ](https://learn.microsoft.com/en-us/previous-versions/sql/?view=sql-server-ver16)


  1. [Learn](https://learn.microsoft.com/en-us/?view=sql-server-ver16)
  2. [SQL Server](https://learn.microsoft.com/en-us/previous-versions/sql/?view=sql-server-ver16)


Ask Learn Ask Learn Focus mode
Table of contents [ Read in English ](https://learn.microsoft.com/en-us/previous-versions/sql/dma/dma-overview?view=sql-server-ver16) Add to Collections Add to plan
* * *
#### Share via
* * *
Copy Markdown Print
* * *
Note
Access to this page requires authorization. You can try [signing in](https://learn.microsoft.com/en-us/previous-versions/sql/dma/dma-overview?view=sql-server-ver16) or changing directories.
Access to this page requires authorization. You can try changing directories.
# Overview of Data Migration Assistant
Feedback
Summarize this article for me
##  In this article
  1. [Get Data Migration Assistant](https://learn.microsoft.com/en-us/previous-versions/sql/dma/dma-overview?view=sql-server-ver16#get-data-migration-assistant)
  2. [Capabilities](https://learn.microsoft.com/en-us/previous-versions/sql/dma/dma-overview?view=sql-server-ver16#capabilities)
  3. [Permissions](https://learn.microsoft.com/en-us/previous-versions/sql/dma/dma-overview?view=sql-server-ver16#permissions)
  4. [Supported source and target versions](https://learn.microsoft.com/en-us/previous-versions/sql/dma/dma-overview?view=sql-server-ver16#supported-source-and-target-versions)
  5. [Related content](https://learn.microsoft.com/en-us/previous-versions/sql/dma/dma-overview?view=sql-server-ver16#related-content)


Data Migration Assistant (DMA) is [retired](https://learn.microsoft.com/en-us/lifecycle/definitions#retirement) from **July 16, 2025**. For migration options from SQL Server to Azure SQL, see [Migration overview: From SQL Server](https://learn.microsoft.com/en-us/data-migration/sql-server/overview). For more information, see [Announcing retirement of Microsoft Data Migration Assistant (DMA) Tool](https://techcommunity.microsoft.com/blog/MicrosoftDataMigration/announcing-retirement-of-microsoft-data-migration-assistant-dma-tool/4424400).
The Data Migration Assistant (DMA) helps you upgrade to a modern data platform by detecting compatibility issues that can affect database functionality when you:
  * Upgrade to a new version of SQL Server
  * Migrate to [Azure SQL Database](https://learn.microsoft.com/en-us/azure/azure-sql/database/sql-database-paas-overview)
  * Migrate to [Azure SQL Managed Instance](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/sql-managed-instance-paas-overview)


DMA recommends performance and reliability improvements for your target environment and allows you to move your schema, data, and uncontained objects from your source server to your target server.
For SQL Server large migrations (in terms of number and size of databases) to Azure, we recommend that you use the [Azure Database Migration Service](https://learn.microsoft.com/en-us/azure/dms/dms-overview), which can migrate databases at scale.
DMA doesn't support database migrations to [Azure SQL Managed Instance](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/sql-managed-instance-paas-overview). Use the [Azure SQL migration extension for Azure Data Studio](https://learn.microsoft.com/en-us/azure/dms/migration-using-azure-data-studio) instead, which supports both online and offline database migrations to Azure SQL Managed Instance.
[](https://learn.microsoft.com/en-us/previous-versions/sql/dma/dma-overview?view=sql-server-ver16#get-data-migration-assistant)
## Get Data Migration Assistant
To install DMA, download the latest version of the tool from the [Microsoft Download Center](https://www.microsoft.com/download/details.aspx?id=53595), and then run the `DataMigrationAssistant.msi` file.
[](https://learn.microsoft.com/en-us/previous-versions/sql/dma/dma-overview?view=sql-server-ver16#capabilities)
## Capabilities
DMA brings you the following capabilities:
[](https://learn.microsoft.com/en-us/previous-versions/sql/dma/dma-overview?view=sql-server-ver16#assess-on-premises-sql-server-instances-migrating-to-azure)
#### Assess on-premises SQL Server Instances migrating to Azure
Assess on-premises SQL Server instances migrating to Azure SQL Database or Azure SQL Managed Instance. The assessment workflow helps you to detect the following issues, which might affect your Azure SQL migration and provides detailed guidance on how to resolve them.
  * Migration blocking issues: Discovers the compatibility issues that block migrating on-premises SQL Server database to Azure SQL Database or Azure SQL Managed Instance. DMA provides recommendations to help you address those issues.
  * Partially supported or unsupported features: Detects partially supported or unsupported features that are currently in use by the source SQL Server instance. DMA provides a comprehensive set of recommendations, alternative approaches available in Azure, and mitigating steps so that you can incorporate them into your migration projects.


[](https://learn.microsoft.com/en-us/previous-versions/sql/dma/dma-overview?view=sql-server-ver16#discover-issues-that-affect-an-upgrade)
#### Discover issues that affect an upgrade
Discover issues that can affect an upgrade to an on-premises SQL Server. These are described as compatibility issues and are organized in the following categories:
  * Breaking changes
  * Behavior changes
  * Deprecated features


[](https://learn.microsoft.com/en-us/previous-versions/sql/dma/dma-overview?view=sql-server-ver16#discover-new-features)
#### Discover new features
Discover new features in the target SQL Server platform that the database can benefit from after an upgrade. These are described as feature recommendations and are organized in the following categories:
  * Performance
  * Security
  * Storage


[](https://learn.microsoft.com/en-us/previous-versions/sql/dma/dma-overview?view=sql-server-ver16#migrate-on-premises-instances-to-sql-server-on-azure-vms)
#### Migrate on-premises instances to SQL Server on Azure VMs
Migrate an on-premises SQL Server instance to a modern SQL Server instance hosted on-premises or on an Azure virtual machine (VM) that is accessible from your on-premises network. The Azure VM can be accessed using VPN or other technologies. The migration workflow helps you to migrate the following components:
  * Schema of databases
  * Data and users
  * Server roles
  * SQL Server and Windows logins


[](https://learn.microsoft.com/en-us/previous-versions/sql/dma/dma-overview?view=sql-server-ver16#assess-on-premises-ssis-packages-migration-to-azure)
#### Assess on-premises SSIS packages migration to Azure
Assess on-premises SQL Server Integration Services (SSIS) packages migrating to Azure SQL Database or Azure SQL Managed Instance. The assessment helps to discover issues that can affect the migration. These are described as compatibility issues and are organized in the following categories:
  * Migration blockers: discovers the compatibility issues that block migrating source packages to Azure. DMA provides recommendations to help you address those issues.
  * Information issues: detects partially supported or deprecated features that are used in source packages.


[](https://learn.microsoft.com/en-us/previous-versions/sql/dma/dma-overview?view=sql-server-ver16#connect-to-databases-after-migration)
#### Connect to databases after migration
After a successful migration, applications can connect to the target SQL databases seamlessly.
[](https://learn.microsoft.com/en-us/previous-versions/sql/dma/dma-overview?view=sql-server-ver16#permissions)
## Permissions
To run an assessment, you have to be a member of the SQL Server **sysadmin** role. The recommended display resolution is 1024x756.
[](https://learn.microsoft.com/en-us/previous-versions/sql/dma/dma-overview?view=sql-server-ver16#supported-source-and-target-versions)
## Supported source and target versions
DMA replaces all previous versions of SQL Server Upgrade Advisor and should be used for upgrades for most SQL Server versions. The following list shows the supported source and target versions for assessment:
**Supported sources**
  * SQL Server 2005 (deprecated)
  * SQL Server 2008
  * SQL Server 2008 R2
  * SQL Server 2012
  * SQL Server 2014
  * SQL Server 2016
  * SQL Server 2017
  * SQL Server 2019
  * SQL Server 2022
  * Amazon RDS for SQL Server


**Supported targets**
  * SQL Server 2012
  * SQL Server 2014
  * SQL Server 2016
  * SQL Server 2017 on Windows and Linux
  * SQL Server 2019 on Windows and Linux
  * SQL Server 2022 on Windows and Linux
  * [Azure SQL Database](https://learn.microsoft.com/en-us/azure/azure-sql/database/sql-database-paas-overview)
  * [Azure SQL Managed Instance](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/sql-managed-instance-paas-overview) (assessment only)
  * [SQL Server on Azure Virtual Machines](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/sql-server-on-azure-vm-iaas-what-is-overview)


[](https://learn.microsoft.com/en-us/previous-versions/sql/dma/dma-overview?view=sql-server-ver16#related-content)
## Related content
  * [Perform a SQL Server migration assessment with Data Migration Assistant](https://learn.microsoft.com/en-us/previous-versions/sql/dma/dma-assesssqlonprem?view=sql-server-ver16)
  * [Configure settings for Data Migration Assistant](https://learn.microsoft.com/en-us/previous-versions/sql/dma/dma-configurationsettings?view=sql-server-ver16)
  * [Upgrade SQL Server using the Data Migration Assistant](https://learn.microsoft.com/en-us/previous-versions/sql/dma/dma-migrateonpremsql?view=sql-server-ver16)
  * [Best practices for running Data Migration Assistant](https://learn.microsoft.com/en-us/previous-versions/sql/dma/dma-bestpractices?view=sql-server-ver16)


* * *
##  Additional resources
* * *
  * Last updated on 06/15/2025


Ask Learn is an AI assistant that can answer questions, clarify concepts, and define terms using trusted Microsoft documentation.
Please sign in to use Ask Learn.
[ Sign in ](https://learn.microsoft.com/en-us/previous-versions/sql/dma/dma-overview?view=sql-server-ver16)
