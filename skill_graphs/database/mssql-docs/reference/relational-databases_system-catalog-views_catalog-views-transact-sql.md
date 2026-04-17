Version SQL Server 2025
  * Analytics Platform System (PDW)
    * [2016-AU7](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/catalog-views-transact-sql?view=aps-pdw-2016-au7)
    * [2016-AU6](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/catalog-views-transact-sql?view=aps-pdw-2016)
  * [Azure SQL Database](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/catalog-views-transact-sql?view=azuresqldb-current)
  * [Azure SQL Managed Instance](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/catalog-views-transact-sql?view=azuresqldb-mi-current)
  * [Azure Synapse Analytics](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/catalog-views-transact-sql?view=azure-sqldw-latest)
  * [Fabric Data Warehouse](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/catalog-views-transact-sql?view=fabric)
  * [Fabric SQL database](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/catalog-views-transact-sql?view=fabric-sqldb)
  * SQL Server
    * [2025](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/catalog-views-transact-sql?view=sql-server-ver17)
    * [2022](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/catalog-views-transact-sql?view=sql-server-ver16)
    * [2019](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/catalog-views-transact-sql?view=sql-server-ver15)
    * [2017](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/catalog-views-transact-sql?view=sql-server-2017)
    * [2016](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/catalog-views-transact-sql?view=sql-server-2016)
  * SQL Server on Linux
    * [2025](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/catalog-views-transact-sql?view=sql-server-linux-ver17)
    * [2022](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/catalog-views-transact-sql?view=sql-server-linux-ver16)
    * [2019](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/catalog-views-transact-sql?view=sql-server-linux-ver15)
    * [2017](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/catalog-views-transact-sql?view=sql-server-linux-2017)


Search
Suggestions will filter as you type
  * [SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/?view=sql-server-ver17)
  * [Docs navigation tips](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17)
  * [Previous versions 2005-2014](https://learn.microsoft.com/en-us/sql/sql-server/previous-versions-sql-server?view=sql-server-ver17)
  *     * [What is SQL Server?](https://learn.microsoft.com/en-us/sql/sql-server/what-is-sql-server?view=sql-server-ver17)
    * [Connect to the Database Engine](https://learn.microsoft.com/en-us/sql/sql-server/connect-to-database-engine?view=sql-server-ver17)
  *     *       * [System catalog views](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/catalog-views-transact-sql?view=sql-server-ver17)
      * [Querying the SQL Server System Catalog FAQ](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/querying-the-sql-server-system-catalog-faq?view=sql-server-ver17)
      * [Schemas - sys.schemas](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/schemas-catalog-views-sys-schemas?view=sql-server-ver17)
      * [Messages (for errors) - sys.messages](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/messages-for-errors-catalog-views-sys-messages?view=sql-server-ver17)
      * [Extended Properties - sys.extended_properties](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/extended-properties-catalog-views-sys-extended-properties?view=sql-server-ver17)


Download PDF
Table of contents  Exit editor mode
  1. [ Learn ](https://learn.microsoft.com/en-us/?view=sql-server-ver17)
  2. [ SQL ](https://learn.microsoft.com/en-us/sql/?view=sql-server-ver17)
  3. [ SQL Server ](https://learn.microsoft.com/en-us/sql/sql-server/?view=sql-server-ver17)


  1. [Learn](https://learn.microsoft.com/en-us/?view=sql-server-ver17)
  2. [SQL](https://learn.microsoft.com/en-us/sql/?view=sql-server-ver17)
  3. [SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/?view=sql-server-ver17)


Ask Learn Ask Learn Focus mode
Table of contents [ Read in English ](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/catalog-views-transact-sql?view=sql-server-ver17) Add to Collections Add to plan
* * *
#### Share via
* * *
Copy Markdown Print
* * *
Note
Access to this page requires authorization. You can try [signing in](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/catalog-views-transact-sql?view=sql-server-ver17) or changing directories.
Access to this page requires authorization. You can try changing directories.
# System catalog views (Transact-SQL)
Feedback
Summarize this article for me
##  In this article
  1. [Remarks](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/catalog-views-transact-sql?view=sql-server-ver17#remarks)
  2. [Related content](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/catalog-views-transact-sql?view=sql-server-ver17#related-content)


**Applies to:** ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure SQL Database](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure SQL Managed Instance](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure Synapse Analytics](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Analytics Platform System (PDW)](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL analytics endpoint in Microsoft Fabric](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Warehouse in Microsoft Fabric](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL database in Microsoft Fabric](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to)
Catalog views return information that is used by the SQL Server Database Engine. We recommend that you use catalog views because they are the most general interface to the catalog metadata, and provide the most efficient way to obtain, transform, and present customized forms of this information. All user-available catalog metadata is exposed through catalog views.
Catalog views do not contain information about replication, backup, database maintenance plan, or SQL Server Agent catalog data.
[](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/catalog-views-transact-sql?view=sql-server-ver17#remarks)
## Remarks
Some catalog views inherit rows from other catalog views. For example, the [sys.tables](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-tables-transact-sql?view=sql-server-ver17) catalog view inherits from the [sys.objects](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-objects-transact-sql?view=sql-server-ver17) catalog view. The `sys.objects` catalog view is referred to as the base view, and the `sys.tables` view is called the derived view. The `sys.tables` catalog view returns the columns that are specific to tables and also all the columns that the `sys.objects` catalog view returns. The `sys.objects` catalog view returns rows for objects other than tables, such as stored procedures and views. After a table is created, the metadata for the table is returned in both views. Although the two catalog views return different levels of information about the table, there is only one entry in metadata for this table with one name and one `object_id`. This can be summarized as follows:
  * The base view contains a subset of columns and a superset of rows.
  * The derived view contains a superset of columns and a subset of rows.


In future releases of SQL Server, Microsoft may augment the definition of any system catalog view by adding columns to the end of the column list. We recommend against using the syntax `SELECT * FROM sys.<catalog_view_name>` in production code because the number of columns returned might change and break your application.
The catalog views in SQL Server have been organized into the following categories:
[Always On Availability Groups Catalog Views (Transact-SQL)](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/always-on-availability-groups-catalog-views-transact-sql?view=sql-server-ver17)
[Azure SQL Database Catalog Views](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/azure-sql-database-catalog-views?view=sql-server-ver17)
[Change Tracking Catalog Views - sys.change_tracking_databases](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/change-tracking-catalog-views-sys-change-tracking-databases?view=sql-server-ver17)
[CLR Assembly Catalog Views (Transact-SQL)](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/clr-assembly-catalog-views-transact-sql?view=sql-server-ver17)
[Data Collector Views (Transact-SQL)](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/data-collector-views-transact-sql?view=sql-server-ver17)
[Data Spaces (Transact-SQL)](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/data-spaces-transact-sql?view=sql-server-ver17)
[Database Mail Views (Transact-SQL)](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/database-mail-views-transact-sql?view=sql-server-ver17)
[Database Mirroring Witness Catalog Views - sys.database_mirroring_witnesses](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/database-mirroring-witness-catalog-views-sys-database-mirroring-witnesses?view=sql-server-ver17)
[Databases and Files Catalog Views (Transact-SQL)](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/databases-and-files-catalog-views-transact-sql?view=sql-server-ver17)
[Endpoints Catalog Views (Transact-SQL)](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/endpoints-catalog-views-transact-sql?view=sql-server-ver17)
[Extended Events Catalog Views (Transact-SQL)](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/extended-events-catalog-views-transact-sql?view=sql-server-ver17)
[Extended Properties Catalog Views - sys.extended_properties](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/extended-properties-catalog-views-sys-extended-properties?view=sql-server-ver17)
[External Operations Catalog Views (Transact-SQL)](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/external-operations-catalog-views-transact-sql?view=sql-server-ver17)
[FILESTREAM and FileTable Catalog Views (Transact-SQL)](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/filestream-and-filetable-catalog-views-transact-sql?view=sql-server-ver17)
[Full-Text Search and Semantic Search Catalog Views (Transact-SQL)](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/full-text-search-and-semantic-search-catalog-views-transact-sql?view=sql-server-ver17)
[Linked Servers Catalog Views (Transact-SQL)](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/linked-servers-catalog-views-transact-sql?view=sql-server-ver17)
[Messages (for errors) Catalog Views - sys.messages](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/messages-for-errors-catalog-views-sys-messages?view=sql-server-ver17)
[Object Catalog Views (Transact-SQL)](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/object-catalog-views-transact-sql?view=sql-server-ver17)
[Partition Function Catalog Views (Transact-SQL)](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/partition-function-catalog-views-transact-sql?view=sql-server-ver17)
[Policy-Based Management Views (Transact-SQL)](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/policy-based-management-views-transact-sql?view=sql-server-ver17)
[Resource Governor Catalog Views (Transact-SQL)](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/resource-governor-catalog-views-transact-sql?view=sql-server-ver17)
[Query Store catalog views (Transact-SQL)](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/query-store-catalog-views-transact-sql?view=sql-server-ver17)
[Scalar Types Catalog Views (Transact-SQL)](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/scalar-types-catalog-views-transact-sql?view=sql-server-ver17)
[Schemas Catalog Views - sys.schemas](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/schemas-catalog-views-sys-schemas?view=sql-server-ver17)
[Security Catalog Views (Transact-SQL)](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/security-catalog-views-transact-sql?view=sql-server-ver17)
[Service Broker Catalog Views (Transact-SQL)](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/service-broker-catalog-views-transact-sql?view=sql-server-ver17)
[Server-wide Configuration Catalog Views (Transact-SQL)](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/server-wide-configuration-catalog-views-transact-sql?view=sql-server-ver17)
[Spatial Data Catalog Views](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/spatial-data-catalog-views?view=sql-server-ver17)
[Azure Synapse Analytics and Analytics Platform System (PDW) catalog views](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sql-data-warehouse-and-parallel-data-warehouse-catalog-views?view=sql-server-ver17)
[Stretch Database Catalog Views - sys.remote_data_archive_databases](https://learn.microsoft.com/en-us/previous-versions/sql/relational-databases/system-catalog-views/stretch-database-catalog-views-sys-remote-data-archive-databases)
[XML Schemas (XML Type System) Catalog Views (Transact-SQL)](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/xml-schemas-xml-type-system-catalog-views-transact-sql?view=sql-server-ver17)
[](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/catalog-views-transact-sql?view=sql-server-ver17#related-content)
## Related content
  * [System Information Schema Views (Transact-SQL)](https://learn.microsoft.com/en-us/sql/relational-databases/system-information-schema-views/system-information-schema-views-transact-sql?view=sql-server-ver17)
  * [System Tables (Transact-SQL)](https://learn.microsoft.com/en-us/sql/relational-databases/system-tables/system-tables-transact-sql?view=sql-server-ver17)
  * [Querying the SQL Server System Catalog FAQ](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/querying-the-sql-server-system-catalog-faq?view=sql-server-ver17)


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
Mar 8, 4 PM - Mar 8, 4 PM
Experiment with what's next in AI-driven apps and agent design
* * *
  * Last updated on 11/18/2025


Ask Learn is an AI assistant that can answer questions, clarify concepts, and define terms using trusted Microsoft documentation.
Please sign in to use Ask Learn.
[ Sign in ](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/catalog-views-transact-sql?view=sql-server-ver17)
