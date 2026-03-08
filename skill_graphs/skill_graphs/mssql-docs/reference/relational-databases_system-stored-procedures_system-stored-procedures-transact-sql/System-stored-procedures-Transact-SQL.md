# System stored procedures (Transact-SQL)
Feedback
Summarize this article for me
##  In this article
  1. [Stored procedure categories](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/system-stored-procedures-transact-sql?view=sql-server-ver17#stored-procedure-categories)
  2. [API system stored procedures](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/system-stored-procedures-transact-sql?view=sql-server-ver17#api-system-stored-procedures)
  3. [Related content](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/system-stored-procedures-transact-sql?view=sql-server-ver17#related-content)


**Applies to:** ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) SQL Server 2016 (13.x) and later versions ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure SQL Database](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure SQL Managed Instance](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure Synapse Analytics](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL analytics endpoint in Microsoft Fabric](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Warehouse in Microsoft Fabric](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL database in Microsoft Fabric](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to)
In SQL Server, many administrative and informational activities can be performed by using system stored procedures. The system stored procedures are grouped into the categories shown in the following table.
[](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/system-stored-procedures-transact-sql?view=sql-server-ver17#stored-procedure-categories)
## Stored procedure categories
Expand table
Category | Description
---|---
[Active Geo-Replication stored procedures (Azure SQL Database)](https://learn.microsoft.com/en-us/azure/azure-sql/database/active-geo-replication-overview) | Manage Active Geo-Replication and Auto-Failover Group configurations in Azure SQL Database.
[Catalog stored procedures](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/catalog-stored-procedures-transact-sql?view=sql-server-ver17) | Implement ODBC data dictionary functions and isolate ODBC applications from changes to underlying system tables.
[Change Data Capture stored procedures](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/change-data-capture-stored-procedures-transact-sql?view=sql-server-ver17) | Enable, disable, or report on change data capture objects.
[Cursor stored procedures](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/cursor-stored-procedures-transact-sql?view=sql-server-ver17) | Implement cursor variable functionality.
[Data collector stored procedures](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/data-collector-stored-procedures-transact-sql?view=sql-server-ver17) | Work with the data collector and its components: collection sets, collection items, and collection types.
[Database Engine stored procedures](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/database-engine-stored-procedures-transact-sql?view=sql-server-ver17) | Perform general maintenance of the SQL Server Database Engine.
[Database Mail stored procedures](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/database-mail-stored-procedures-transact-sql?view=sql-server-ver17) | Perform e-mail operations from within an instance of SQL Server.
[Database Maintenance Plan stored procedures](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/database-maintenance-plan-stored-procedures-transact-sql?view=sql-server-ver17) | Set up core maintenance tasks that are required to manage database performance.
[Distributed Queries stored procedures](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/distributed-queries-stored-procedures-transact-sql?view=sql-server-ver17) | Implement and manage distributed queries.
[FILESTREAM and FileTable stored procedures](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/filestream-and-filetable-sp-filestream-force-garbage-collection?view=sql-server-ver17) | Configure and manage the FILESTREAM and FileTable features.
[Firewall Rules stored procedures (Azure SQL Database)](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/firewall-rules-stored-procedures-azure-sql-database?view=sql-server-ver17) | Configure the Azure SQL Database firewall.
[Full-Text Search and Semantic Search stored procedures](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/full-text-search-and-semantic-search-stored-procedures-transact-sql?view=sql-server-ver17) | Implement and query full-text indexes.
[General extended stored procedures](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/general-extended-stored-procedures-transact-sql?view=sql-server-ver17) | Provide an interface from an instance of SQL Server to external programs for various maintenance activities.
[Log Shipping stored procedures](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/log-shipping-stored-procedures-transact-sql?view=sql-server-ver17) | Configure, modify, and monitor log shipping configurations.
[Management Data Warehouse stored procedures](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/management-data-warehouse-stored-procedures-transact-sql?view=sql-server-ver17) | Configure the management data warehouse.
[MSDTC stored procedures](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/msdtc-stored-procedures-transact-sql?view=sql-server-ver17) | Reset the Microsoft Distributed Transaction Coordinator (MSDTC) log or look at MSDTC statistics.
[OLE Automation stored procedures](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/ole-automation-stored-procedures-transact-sql?view=sql-server-ver17) | Enable standard Automation objects for use within a standard Transact-SQL batch.
[Policy-Based Management stored procedures](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/policy-based-management-stored-procedures-transact-sql?view=sql-server-ver17) | Manage Policy-Based Management configurations.
[PolyBase stored procedures](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/polybase-stored-procedures-sp-polybase-join-group?view=sql-server-ver17) | Add or remove a computer from a PolyBase scale-out group.
[Query Store stored procedures](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/query-store-stored-procedures-transact-sql?view=sql-server-ver17) | Tune performance using Query Store data.
[Replication stored procedures](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/replication-stored-procedures-transact-sql?view=sql-server-ver17) | Manage replication configurations and operations.
[Security stored procedures](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/security-stored-procedures-transact-sql?view=sql-server-ver17) | Manage security settings and permissions.
[Snapshot Backup stored procedures](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/snapshot-backup-sp-delete-backup?view=sql-server-ver17) | Delete the FILE_SNAPSHOT backup along with all of its snapshots or delete an individual backup file snapshot.
[Spatial Index stored procedures](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/spatial-index-stored-procedures-arguments-and-properties?view=sql-server-ver17) | Analyze and improve the indexing performance of spatial indexes.
[SQL Server Agent stored procedures](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sql-server-agent-stored-procedures-transact-sql?view=sql-server-ver17) | Manage scheduled and event-driven activities for SQL Server Agent.
[SQL Server Profiler stored procedures](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sql-server-profiler-stored-procedures-transact-sql?view=sql-server-ver17) | Monitor performance and activity using SQL Server Profiler.
[XML stored procedures](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/xml-stored-procedures-transact-sql?view=sql-server-ver17) | Manage XML text processing.
Unless specifically documented otherwise, all system stored procedures return a value of `0` to indicate success. To indicate failure, a nonzero value is returned.
[](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/system-stored-procedures-transact-sql?view=sql-server-ver17#api-system-stored-procedures)
## API system stored procedures
Users that run SQL Server Profiler against ADO, OLE DB, and ODBC applications might notice these applications using system stored procedures that aren't covered in the Transact-SQL Reference. These stored procedures are used by the SQL Server Native Client OLE DB Provider and the SQL Server Native Client ODBC driver to implement the functionality of a database API. These stored procedures are the mechanism the provider or driver uses to communicate user requests to an instance of SQL Server. They are intended only for the internal use of the provider or the driver. Calling them explicitly from a SQL Server-based application isn't supported.
The `sp_createorphan` and `sp_droporphans` stored procedures are used for ODBC **ntext** , **text** , and **image** processing.
The `sp_reset_connection` stored procedure is used by SQL Server to support remote stored procedure calls in a transaction. This stored procedure also causes Audit Login and Audit Logout events to fire when a connection is reused from a connection pool.
The system stored procedures in the following tables are used only within an instance of SQL Server or through client APIs and aren't intended for general customer use. They are subject to change and compatibility isn't guaranteed.
[](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/system-stored-procedures-transact-sql?view=sql-server-ver17#documented-api-stored-procedures)
### Documented API stored procedures
Expand table
Stored procedure | Stored procedure
---|---
[sp_catalogs](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-catalogs-transact-sql?view=sql-server-ver17) | [sp_column_privileges](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-column-privileges-transact-sql?view=sql-server-ver17)
[sp_column_privileges_ex](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-column-privileges-ex-transact-sql?view=sql-server-ver17) | [sp_columns](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-columns-transact-sql?view=sql-server-ver17)
[sp_columns_ex](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-columns-ex-transact-sql?view=sql-server-ver17) | [sp_databases](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-databases-transact-sql?view=sql-server-ver17)
[sp_cursor](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-cursor-transact-sql?view=sql-server-ver17) | [sp_cursorclose](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-cursorclose-transact-sql?view=sql-server-ver17)
[sp_cursorexecute](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-cursorexecute-transact-sql?view=sql-server-ver17) | [sp_cursorfetch](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-cursorfetch-transact-sql?view=sql-server-ver17)
[sp_cursoroption](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-cursoroption-transact-sql?view=sql-server-ver17) | [sp_cursoropen](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-cursoropen-transact-sql?view=sql-server-ver17)
[sp_cursorprepare](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-cursorprepare-transact-sql?view=sql-server-ver17) | [sp_cursorprepexec](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-cursorprepexec-transact-sql?view=sql-server-ver17)
[sp_cursorunprepare](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-cursorunprepare-transact-sql?view=sql-server-ver17) | [sp_execute](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-execute-transact-sql?view=sql-server-ver17)
[sp_datatype_info](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-datatype-info-transact-sql?view=sql-server-ver17) | [sp_fkeys](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-fkeys-transact-sql?view=sql-server-ver17)
[sp_foreignkeys](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-foreignkeys-transact-sql?view=sql-server-ver17) | [sp_indexes](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-indexes-transact-sql?view=sql-server-ver17)
[sp_pkeys](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-pkeys-transact-sql?view=sql-server-ver17) | [sp_primarykeys](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-primarykeys-transact-sql?view=sql-server-ver17)
[sp_prepare (Transact SQL)](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-prepare-transact-sql?view=sql-server-ver17) | [sp_prepexec](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-prepexec-transact-sql?view=sql-server-ver17)
[sp_prepexecrpc](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-prepexecrpc-transact-sql?view=sql-server-ver17) | [sp_unprepare](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-unprepare-transact-sql?view=sql-server-ver17)
[sp_server_info](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-server-info-transact-sql?view=sql-server-ver17) | [sp_special_columns](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-special-columns-transact-sql?view=sql-server-ver17)
[sp_sproc_columns](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-sproc-columns-transact-sql?view=sql-server-ver17) | [sp_statistics](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-statistics-transact-sql?view=sql-server-ver17)
[sp_table_privileges](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-table-privileges-transact-sql?view=sql-server-ver17) | [sp_table_privileges_ex](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-table-privileges-ex-transact-sql?view=sql-server-ver17)
[sp_tables](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-tables-transact-sql?view=sql-server-ver17) | [sp_tables_ex](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-tables-ex-transact-sql?view=sql-server-ver17)
[](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/system-stored-procedures-transact-sql?view=sql-server-ver17#undocumented-api-stored-procedures)
### Undocumented API stored procedures
The following stored procedures aren't documented and are for internal use only:
Expand table
Stored procedure | Stored procedure
---|---
`sp_assemblies_rowset` | `sp_assemblies_rowset_rmt`
`sp_assemblies_rowset2` | `sp_assembly_dependencies_rowset`
`sp_assembly_dependencies_rowset_rmt` | `sp_assembly_dependencies_rowset2`
`sp_bcp_dbcmptlevel` | `sp_catalogs_rowset`
`sp_catalogs_rowset;2` | `sp_catalogs_rowset;5`
`sp_catalogs_rowset_rmt` | `sp_catalogs_rowset2`
`sp_check_constbytable_rowset` | `sp_check_constbytable_rowset;2`
`sp_check_constbytable_rowset2` | `sp_check_constraints_rowset`
`sp_check_constraints_rowset;2` | `sp_check_constraints_rowset2`
`sp_column_privileges_rowset` | `sp_column_privileges_rowset;2`
`sp_column_privileges_rowset;5` | `sp_column_privileges_rowset_rmt`
`sp_column_privileges_rowset2` | `sp_columns_90`
`sp_columns_90_rowset` | `sp_columns_90_rowset_rmt`
`sp_columns_90_rowset2` | `sp_columns_ex_90`
`sp_columns_rowset` | `sp_columns_rowset;2`
`sp_columns_rowset;5` | `sp_columns_rowset_rmt`
`sp_columns_rowset2` | `sp_constr_col_usage_rowset`
`sp_datatype_info_90` | `sp_ddopen;1`
`sp_ddopen;10` | `sp_ddopen;11`
`sp_ddopen;12` | `sp_ddopen;13`
`sp_ddopen;2` | `sp_ddopen;3`
`sp_ddopen;4` | `sp_ddopen;5`
`sp_ddopen;6` | `sp_ddopen;7`
`sp_ddopen;8` | `sp_ddopen;9`
`sp_foreign_keys_rowset` | `sp_foreign_keys_rowset;2`
`sp_foreign_keys_rowset;3` | `sp_foreign_keys_rowset;5`
`sp_foreign_keys_rowset_rmt` | `sp_foreign_keys_rowset2`
`sp_foreign_keys_rowset3` | `sp_indexes_90_rowset`
`sp_indexes_90_rowset_rmt` | `sp_indexes_90_rowset2`
`sp_indexes_rowset` | `sp_indexes_rowset;2`
`sp_indexes_rowset;5` | `sp_indexes_rowset_rmt`
`sp_indexes_rowset2` | `sp_linkedservers_rowset`
`sp_linkedservers_rowset;2` | `sp_linkedservers_rowset2`
`sp_oledb_database` | `sp_oledb_defdb`
`sp_oledb_deflang` | `sp_oledb_language`
`sp_oledb_ro_usrname` | `sp_primary_keys_rowset`
`sp_primary_keys_rowset;2` | `sp_primary_keys_rowset;3`
`sp_primary_keys_rowset;5` | `sp_primary_keys_rowset_rmt`
`sp_primary_keys_rowset2` | `sp_procedure_params_90_rowset`
`sp_procedure_params_90_rowset2` | `sp_procedure_params_rowset`
`sp_procedure_params_rowset;2` | `sp_procedure_params_rowset2`
`sp_procedures_rowset` | `sp_procedures_rowset;2`
`sp_procedures_rowset2` | `sp_provider_types_90_rowset`
`sp_provider_types_rowset` | `sp_schemata_rowset`
`sp_schemata_rowset;3` | `sp_special_columns_90`
`sp_sproc_columns_90` | `sp_statistics_rowset`
`sp_statistics_rowset;2` | `sp_statistics_rowset2`
`sp_stored_procedures` | `sp_table_constraints_rowset`
`sp_table_constraints_rowset;2` | `sp_table_constraints_rowset2`
`sp_table_privileges_rowset` | `sp_table_privileges_rowset;2`
`sp_table_privileges_rowset;5` | `sp_table_privileges_rowset_rmt`
`sp_table_privileges_rowset2` | `sp_table_statistics_rowset`
`sp_table_statistics_rowset;2` | `sp_table_statistics2_rowset`
`sp_tablecollations` | `sp_tablecollations_90`
`sp_tables_info_90_rowset` | `sp_tables_info_90_rowset_64`
`sp_tables_info_90_rowset2` | `sp_tables_info_90_rowset2_64`
`sp_tables_info_rowset` | `sp_tables_info_rowset;2`
`sp_tables_info_rowset_64` | `sp_tables_info_rowset_64;2`
`sp_tables_info_rowset2` | `sp_tables_info_rowset2_64`
`sp_tables_rowset;2` | `sp_tables_rowset;5`
`sp_tables_rowset_rmt` | `sp_tables_rowset2`
`sp_usertypes_rowset` | `sp_usertypes_rowset_rmt`
`sp_usertypes_rowset2` | `sp_views_rowset`
`sp_views_rowset2` | `sp_xml_schema_rowset`
`sp_xml_schema_rowset2` |
[](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/system-stored-procedures-transact-sql?view=sql-server-ver17#related-content)
## Related content
  * [CREATE PROCEDURE (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-procedure-transact-sql?view=sql-server-ver17)
  * [Stored Procedures (Database Engine)](https://learn.microsoft.com/en-us/sql/relational-databases/stored-procedures/stored-procedures-database-engine?view=sql-server-ver17)
  * [Running stored procedures (OLE DB)](https://learn.microsoft.com/en-us/sql/relational-databases/native-client/ole-db/stored-procedures-running?view=sql-server-ver17)
  * [Running stored procedures](https://learn.microsoft.com/en-us/sql/relational-databases/native-client-odbc-stored-procedures/running-stored-procedures?view=sql-server-ver17)
  * [Database Engine stored procedures (Transact-SQL)](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/database-engine-stored-procedures-transact-sql?view=sql-server-ver17)


**Note:** The author created this article with assistance from AI. [Learn more](https://learn.microsoft.com/principles-for-ai-generated-content)
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
  * Last updated on 02/24/2026


##  In this article
  1. [Stored procedure categories](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/system-stored-procedures-transact-sql?view=sql-server-ver17#stored-procedure-categories)
  2. [API system stored procedures](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/system-stored-procedures-transact-sql?view=sql-server-ver17#api-system-stored-procedures)
  3. [Related content](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/system-stored-procedures-transact-sql?view=sql-server-ver17#related-content)


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
[ Sign in ](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/system-stored-procedures-transact-sql?view=sql-server-ver17)
[English (United States)](https://learn.microsoft.com/en-us/locale?target=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fsql%2Frelational-databases%2Fsystem-stored-procedures%2Fsystem-stored-procedures-transact-sql%3Fview%3Dsql-server-ver17)
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
