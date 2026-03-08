# Data virtualization with PolyBase in SQL Server
Feedback
Summarize this article for me
##  In this article
  1. [What is PolyBase?](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-guide?view=sql-server-ver17#what-is-polybase)
  2. [Why use PolyBase?](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-guide?view=sql-server-ver17#why-use-polybase)
  3. [Performance](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-guide?view=sql-server-ver17#performance)
  4. [Upgrade to SQL Server 2022](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-guide?view=sql-server-ver17#upgrade-to-sql-server-2022)
  5. [Get started](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-guide?view=sql-server-ver17#get-started)
  6. [Related content](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-guide?view=sql-server-ver17#related-content)

Show 2 more
**Applies to:** ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure Synapse Analytics](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Analytics Platform System (PDW)](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to)
PolyBase enables data virtualization for SQL Server.
[](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-guide?view=sql-server-ver17#what-is-polybase)
## What is PolyBase?
PolyBase enables your SQL Server instance to query data with Transact-SQL (T-SQL) directly from SQL Server, Oracle, Teradata, MongoDB, Hadoop clusters, Cosmos DB, and S3-compatible object storage without separately installing client connection software. You can also use the generic ODBC connector to connect to additional providers using third-party ODBC drivers. PolyBase allows T-SQL queries to join the data from external sources to relational tables in an instance of SQL Server.
PolyBase also supports querying semi-structured and structured file-based data formats such as CSV, Parquet, JSON, and Delta Lake files. This enables seamless integration of file-based data into your T-SQL workflows.
A key use case for data virtualization with the PolyBase feature is to allow the data to stay in its original location and format. You can virtualize the external data through the SQL Server instance, so that it can be queried in place like any other table in SQL Server. This process minimizes the need for ETL processes for data movement. This data virtualization scenario is possible with the use of PolyBase connectors.
[](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-guide?view=sql-server-ver17#supported-sql-products-and-services)
### Supported SQL products and services
PolyBase provides these same functionalities for the following SQL products from Microsoft:
  * SQL Server 2016 (13.x) and later versions (Windows)
  * SQL Server 2019 (15.x) and later versions (Windows and Linux)
  * Azure SQL Managed Instance, for details, review [Data virtualization with Azure SQL Managed Instance](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/data-virtualization-overview)
  * Azure SQL Database, for details, review [Data virtualization with Azure SQL Database (Preview)](https://learn.microsoft.com/en-us/azure/azure-sql/database/data-virtualization-overview)
  * SQL Server Analytics Platform System (PDW)
  * Azure Synapse Analytics (for dedicated SQL pools)
    * Data virtualization in Azure Synapse Analytics is available in two modes, PolyBase and native. For more information, see [Use external tables with Synapse SQL](https://learn.microsoft.com/en-us/azure/synapse-analytics/sql/develop-tables-external-tables).


[](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-guide?view=sql-server-ver17#sql-server-2025-polybase-enhancements)
### SQL Server 2025 PolyBase enhancements
Expand table
New to SQL Server 2025 (17.x) | Details
---|---
Native support for CSV, Parquet, & Delta 1 | PolyBase Query Service for External Data installation is no longer required to use `OPENROWSET`, `CREATE EXTERNAL TABLE`, or `CREATE EXTERNAL TABLE AS SELECT` with the following types of external data: Parquet, Delta, Azure Blob Storage (ABS), Azure Data Lake Storage (ADLS), or S3-Compatible Object storage.
Use generic ODBC data sources on Linux | For more information, see [Configure PolyBase to access external data with ODBC generic types](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-configure-odbc-generic?view=sql-server-ver17).
[TDS 8.0 support](https://learn.microsoft.com/en-us/sql/relational-databases/security/networking/tds-8?view=sql-server-ver17) | PolyBase uses a secure-by-default configuration with ODBC Driver for SQL Server version 18 and `Encrypt=Yes` (Mandatory). Unlike other SQL Server features, PolyBase allows `TrustServerCertificate=True` for self-signed certificate scenarios. To enforce TLS 1.3 and strict encryption with TDS 8.0, set `Encrypt=Strict` and `TrustServerCertificate=No`. For more information, see [CREATE EXTERNAL DATA SOURCE - CONNECTION_OPTIONS](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-external-data-source-transact-sql?view=sql-server-ver17#connection_options--key_value_pair-2). Review [Breaking changes to Database Engine features in SQL Server 2025](https://learn.microsoft.com/en-us/sql/database-engine/breaking-changes-to-database-engine-features-in-sql-server-2025?view=sql-server-ver17).
Managed Identity | Managed Identity is available for SQL Server enabled by Azure Arc and SQL Server 2025 on Azure VMs.
1 On SQL Server 2025 (17.x), PolyBase Query Service for External Data is still required to connect with other databases. For example: SQL Server, Oracle, DB2, Teradata, MongoDB, or ODBC.
[](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-guide?view=sql-server-ver17#sql-server-2022-polybase-enhancements)
### SQL Server 2022 PolyBase enhancements
Expand table
New to SQL Server 2022 (16.x) | Details
---|---
S3-compatible object storage | SQL Server 2022 (16.x) adds new connector, S3-compatible object storage, using the S3 REST API. You can use both [OPENROWSET](https://learn.microsoft.com/en-us/sql/t-sql/functions/openrowset-transact-sql?view=sql-server-ver17) and [CREATE EXTERNAL TABLE](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-external-table-transact-sql?view=sql-server-ver17) to query data files in S3-compatible object storage.
Some connectors separate from PolyBase services | The S3-compatible object storage connector, ADSL Gen2, and Azure Blob Storage, are no longer dependent of PolyBase services. PolyBase services must still run to support connectivity with Oracle, Teradata, MongoDB, and Generic ODBC. The PolyBase feature must still be installed on your SQL Server instance.
Parquet file format | PolyBase is now capable of querying data from Parquet files stored on S3-compatible object storage. For more information, see to [Virtualize parquet file in a S3-compatible object storage with PolyBase](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-virtualize-parquet-file?view=sql-server-ver17).
Delta table format | PolyBase is now capable of querying (read-only) data from Delta Table format stored on S3-compatible object storage, Azure Storage Account V2, and Azure Data Lake Storage Gen2. For more information, see to [Virtualize delta table with PolyBase](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/virtualize-delta?view=sql-server-ver17)
Create External Table as Select (CETAS) | PolyBase can now use CETAS to create an external table and then export, in parallel, the result of a Transact-SQL `SELECT` statement to Azure Data Lake Storage Gen2, Azure Storage Account V2, and S3-compatible object storage. For more information, see [CREATE EXTERNAL TABLE AS SELECT (CETAS)](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-external-table-as-select-transact-sql?view=sql-server-ver17).
For more new features of SQL Server 2022 (16.x), see [What's new in SQL Server 2022](https://learn.microsoft.com/en-us/sql/sql-server/what-s-new-in-sql-server-2022?view=sql-server-ver17).
For a tutorial of PolyBase features and capabilities in SQL Server 2022 (16.x), see [Get started with PolyBase in SQL Server 2022](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-get-started?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-guide?view=sql-server-ver17#polybase-connectors)
### PolyBase connectors
The PolyBase feature provides connectivity to the following external data sources:
Expand table
External data sources | SQL Server 2016-2019 with PolyBase | SQL Server 2022 (16.x) with PolyBase | APS PDW | Azure Synapse Analytics
---|---|---|---|---
Oracle, MongoDB, Teradata | Read | Read | No | No
Generic ODBC | Read (Windows Only) | Read (Windows Only) | No | No
Azure Storage | Read/Write | Read/Write | Read/Write | Read/Write
Hadoop | Read/Write | No | Read/Write | No
SQL Server | Read | Read | No | No
S3-compatible object storage | No | Read/Write | No | No
  * SQL Server 2022 (16.x) and later versions don't support Hadoop.
  * SQL Server 2016 (13.x) introduced PolyBase with support for connections to Hadoop and Azure Blob Storage.
  * SQL Server 2019 (15.x) introduced more connectors, including SQL Server, Oracle, Teradata, and MongoDB.
  * SQL Server 2022 (16.x) introduced the S3-compatible storage connector.
  * SQL Server 2019 (15.x) Cumulative update 19 introduced support for Oracle TNS.
  * SQL Server 2022 (16.x) Cumulative update 2 introduced support for Oracle TNS.


Examples of external connectors include:
  * [SQL Server](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-configure-sql-server?view=sql-server-ver17)
  * [Oracle](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-configure-oracle?view=sql-server-ver17)
  * [Teradata](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-configure-teradata?view=sql-server-ver17)
  * [MongoDB](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-configure-mongodb?view=sql-server-ver17)
  * [Hadoop](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-configure-hadoop?view=sql-server-ver17) 1
  * [S3-compatible object storage](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-configure-s3-compatible?view=sql-server-ver17)
  * [CSV file](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/virtualize-csv?view=sql-server-ver17)


1 PolyBase supports two Hadoop providers, Hortonworks Data Platform (HDP) and Cloudera Distributed Hadoop (CDH), through SQL Server 2019. SQL Server support for HDFS Cloudera (CDP) and Hortonworks (HDP) external data sources has been retired, and isn't included in SQL Server 2022 (16.x) and later versions. For more information, see [Big data options on the Microsoft SQL Server platform](https://learn.microsoft.com/en-us/sql/big-data-cluster/big-data-options?view=sql-server-ver17).
To use PolyBase in an instance of SQL Server:
  1. [Install PolyBase on Windows](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-installation?view=sql-server-ver17) or [Install PolyBase on Linux](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-linux-setup?view=sql-server-ver17).
  2. Starting with SQL Server 2019 (15.x), [enable PolyBase in sp_configure](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-installation?view=sql-server-ver17#enable), if necessary.
  3. Create an [external data source](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-external-data-source-transact-sql?view=sql-server-ver17).
  4. Create an [external table](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-external-table-transact-sql?view=sql-server-ver17).


[](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-guide?view=sql-server-ver17#azure-integration)
### Azure integration
With the underlying help of PolyBase, T-SQL queries can also import and export data from Azure Blob Storage. Further, PolyBase enables Azure Synapse Analytics to import and export data from Azure Data Lake Store, and from Azure Blob Storage.
[](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-guide?view=sql-server-ver17#why-use-polybase)
## Why use PolyBase?
PolyBase lets you join data from a SQL Server instance with external data. Before PolyBase allowed joining data to external data sources, you could either:
  * Transfer half your data so that all the data was in one location.
  * Query both sources of data, then write custom query logic to join and integrate the data at the client level.


PolyBase lets you use Transact-SQL to join the data.
PolyBase doesn't require you to install extra software to your Hadoop environment. You query external data by using the same T-SQL syntax used to query a database table. The support actions implemented by PolyBase all happen transparently. The query author doesn't need any knowledge about the external source.
[](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-guide?view=sql-server-ver17#polybase-uses)
### PolyBase uses
PolyBase enables the following scenarios in SQL Server:
  * **Seamless data access:** Query other RDBMs or external files like CSV, Parquet, and Delta Lake tables using T-SQL as if they were native tables.
  * **Off-loading cold data:** While keeping it easily accessible.
  * **Enhanced productivity:** Reduce the time and effort required to integrate and analyze data from multiple sources.
  * **Cost efficiency:** Minimize the need for data replication and storage costs associated with traditional data integration methods.
  * **Real-time insights:** Enable real-time data querying and insights without delays caused by data movement or synchronization.
  * **Security:** Use SQL Server security features for granular permissions, credential management, and control.


[](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-guide?view=sql-server-ver17#performance)
## Performance
There's no hard limit to the number of files or the amount of data that can be queried. Query performance depends on the amount of data, data format, the way data is organized, and complexity of queries and joins.
For more information on performance guidance and recommendations for PolyBase, see [Performance considerations in PolyBase for SQL Server](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-performance?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-guide?view=sql-server-ver17#upgrade-to-sql-server-2022)
## Upgrade to SQL Server 2022
Starting in SQL Server 2022 (16.x) Hortonworks Data Platform (HDP) and Cloudera Distributed Hadoop (CDH) are no longer supported. Due to these changes, you must manually drop PolyBase external data sources created on previous versions of SQL Server that use `TYPE = HADOOP` or Azure Storage before migrating to SQL Server 2022 (16.x) or later. Dropping external data sources also requires dropping the associated database objects, such as database scoped credentials and external tables.
Azure Storage connectors must be changed based on the following reference table:
Expand table
External data source | From | To
---|---|---
Azure Blob Storage | `wasb[s]` | `abs`
ADLS Gen 2 | `abfs[s]` | `adls`
[](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-guide?view=sql-server-ver17#get-started)
## Get started
Before using PolyBase, you must [install PolyBase on Windows](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-installation?view=sql-server-ver17) or [install PolyBase on Linux](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-linux-setup?view=sql-server-ver17), and [enable PolyBase in sp_configure](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-installation?view=sql-server-ver17#enable) if necessary.
For a tutorial of PolyBase features and capabilities, see [Get started with PolyBase in SQL Server 2022](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-get-started?view=sql-server-ver17).
For more tutorials on various external data sources, review:
  * [Hadoop](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-configure-hadoop?view=sql-server-ver17)
  * [Azure Blob Storage](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-configure-azure-blob-storage?view=sql-server-ver17)
  * [SQL Server](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-configure-sql-server?view=sql-server-ver17)
  * [Oracle](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-configure-oracle?view=sql-server-ver17)
  * [Teradata](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-configure-teradata?view=sql-server-ver17)
  * [MongoDB](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-configure-mongodb?view=sql-server-ver17)
  * [ODBC generic types](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-configure-odbc-generic?view=sql-server-ver17)
  * [S3-compatible object storage](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-configure-s3-compatible?view=sql-server-ver17)
  * [CSV file](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/virtualize-csv?view=sql-server-ver17)
  * [Parquet file](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-virtualize-parquet-file?view=sql-server-ver17)
  * [Delta table](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/virtualize-delta?view=sql-server-ver17)


[](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-guide?view=sql-server-ver17#data-virtualization-on-other-platforms)
### Data virtualization on other platforms
Data virtualization features are also available on other platforms:
  * [Use external tables with Synapse SQL](https://learn.microsoft.com/en-us/azure/synapse-analytics/sql/develop-tables-external-tables)
  * [Data virtualization with Azure SQL Managed Instance](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/data-virtualization-overview)
  * [Data virtualization with Azure SQL Database (Preview)](https://learn.microsoft.com/en-us/azure/azure-sql/database/data-virtualization-overview)


[](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-guide?view=sql-server-ver17#related-content)
## Related content
  * [Get started with PolyBase in SQL Server 2022](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-get-started?view=sql-server-ver17)
  * [OPENROWSET (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/functions/openrowset-transact-sql?view=sql-server-ver17)
  * [CREATE EXTERNAL TABLE (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-external-table-transact-sql?view=sql-server-ver17)
  * [CREATE EXTERNAL TABLE AS SELECT (CETAS) (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-external-table-as-select-transact-sql?view=sql-server-ver17)
  * [Performance considerations in PolyBase for SQL Server](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-performance?view=sql-server-ver17)
  * [Frequently asked questions in PolyBase](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-faq?view=sql-server-ver17)
  * [Monitor and troubleshoot PolyBase](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-troubleshooting?view=sql-server-ver17)
  * [PolyBase Transact-SQL reference](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-t-sql-objects?view=sql-server-ver17)


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
  * [ Get started with PolyBase in SQL Server 2022 - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-get-started?source=recommendations)
A tutorial for getting started with PolyBase in SQL Server 2022.
  * [ PolyBase query scenarios - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-queries?source=recommendations)
See examples of queries using the PolyBase feature of SQL Server, including SELECT, JOIN external with local tables, import/export data, and new catalog views.
  * [ PolyBase features and limitations - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-versioned-feature-summary?source=recommendations)
PolyBase features available for SQL Server products and services, including a list of T-SQL operators supported for pushdown and known limitations.
  * [ Access external data: SQL Server - PolyBase - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-configure-sql-server?source=recommendations)
Learn how to use PolyBase on a SQL Server instance to query external data in another SQL Server instance. Create external tables to reference external data.
  * [ Virtualize a CSV file with PolyBase - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/virtualize-csv?source=recommendations)
Virtualize a CSV file with PolyBase starting with SQL Server 2022.
  * [ PolyBase Transact-SQL reference - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-t-sql-objects?source=recommendations)
Use PolyBase to query your external data in Hadoop, Azure Blob Storage, Azure Data Lake Store, SQL Server, Oracle, Teradata, MongoDB, or CSV files.
  * [ Access external data: Oracle - PolyBase - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-configure-oracle?source=recommendations)
This article demonstrates how to use PolyBase to create an external data source to access Oracle data.
  * [ Install PolyBase on Windows - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-installation?source=recommendations)
Learn to install PolyBase as a single node or PolyBase scale-out group. You can use an installation wizard or a command prompt. Finally, enable PolyBase.


Show 5 more
Module
[ Introduction to SQL Server 2025 Data Virtualization - Training ](https://learn.microsoft.com/en-us/training/modules/sql-server-2022-data-virtualization/?source=recommendations)
Learn about data virtualization, how to use Polybase to access and query external data, and enhanced Polybase features in SQL Server 2025.
Certification
[ Microsoft Certified: Azure Database Administrator Associate - Certifications ](https://learn.microsoft.com/en-us/credentials/certifications/azure-database-administrator-associate/?source=recommendations)
Administer an SQL Server database infrastructure for cloud, on-premises and hybrid relational databases using the Microsoft PaaS relational database offerings.
Mar 8, 4 PM - Mar 8, 4 PM
Experiment with what's next in AI-driven apps and agent design
* * *
  * Last updated on 11/18/2025


##  In this article
  1. [What is PolyBase?](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-guide?view=sql-server-ver17#what-is-polybase)
  2. [Why use PolyBase?](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-guide?view=sql-server-ver17#why-use-polybase)
  3. [Performance](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-guide?view=sql-server-ver17#performance)
  4. [Upgrade to SQL Server 2022](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-guide?view=sql-server-ver17#upgrade-to-sql-server-2022)
  5. [Get started](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-guide?view=sql-server-ver17#get-started)
  6. [Related content](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-guide?view=sql-server-ver17#related-content)


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
[ Sign in ](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-guide?view=sql-server-ver17)
[English (United States)](https://learn.microsoft.com/en-us/locale?target=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fsql%2Frelational-databases%2Fpolybase%2Fpolybase-guide%3Fview%3Dsql-server-ver17)
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
