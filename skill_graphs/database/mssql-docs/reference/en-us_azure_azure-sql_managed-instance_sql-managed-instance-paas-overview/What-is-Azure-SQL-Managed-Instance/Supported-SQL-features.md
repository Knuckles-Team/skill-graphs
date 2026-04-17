## Supported SQL features
Azure SQL Managed Instance aims to deliver close to 100% surface area compatibility with the latest SQL Server version through a staged release plan. This goal means that most features of SQL Server are also compatible with SQL Managed Instance.
SQL Managed Instance supports backward compatibility to SQL Server 2008 databases. Direct migration from SQL Server 2005 is supported, and the compatibility level for migrated SQL Server 2005 databases is updated to SQL Server 2008.
The following list shows SQL Server features that are compatible with Azure SQL Managed Instance:
**Data migration**
  * [Native backup and restore](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/restore-sample-database-quickstart?view=azuresql)
  * Configurable database file layout
  * [SQL migration experience in Azure Arc portal](https://learn.microsoft.com/en-us/sql/sql-server/azure-arc/migrate-to-azure-sql-managed-instance)
  * [Migrate with Managed Instance link](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/managed-instance-link-migrate?view=azuresql)
  * Automated migrations at scale with [Azure Database Migration Service](https://learn.microsoft.com/en-us/azure/dms/migration-dms-powershell-cli)


**Operational**
  * [DMVs](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/monitoring-with-dmvs?view=azuresql) and [Extended events](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/extended-events)
  * [Query store](https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitoring-performance-by-using-the-query-store)
  * [SQL Server Agent](https://learn.microsoft.com/en-us/sql/ssms/agent/sql-server-agent)
  * [Database mail (external SMTP)](https://learn.microsoft.com/en-us/sql/relational-databases/database-mail/database-mail)


**Scenario enablers**
  * [Synchronize data with the Managed Instance link](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/managed-instance-link-feature-overview?view=azuresql)
  * [Service Broker](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/sql-server-service-broker)
  * [Transactional replication](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/replication-transactional-overview?view=azuresql)
  * [Change Data Capture](https://learn.microsoft.com/en-us/sql/relational-databases/track-changes/about-change-data-capture-sql-server)


**Programmability**
  * [Global temporal tables](https://learn.microsoft.com/en-us/azure/azure-sql/temporal-tables?view=azuresql)
  * [Cross-database queries and transactions](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/distributed-transaction-coordinator-dtc?view=azuresql)
  * [Linked servers](https://learn.microsoft.com/en-us/sql/relational-databases/linked-servers/linked-servers-database-engine)
  * [CLR modules](https://learn.microsoft.com/en-us/sql/relational-databases/clr-integration/common-language-runtime-clr-integration-programming-concepts)


**Security**
  * [Microsoft Entra authentication](https://learn.microsoft.com/en-us/azure/azure-sql/database/authentication-aad-overview?view=azuresql)
  * [TDE](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption-azure-sql)
  * [Always Encrypted](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-database-engine)
  * [SQL Auditing](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/auditing-configure?view=azuresql)
  * [Row-Level Security (RLS)](https://learn.microsoft.com/en-us/sql/relational-databases/security/row-level-security)
  * [Dynamic Data Masking](https://learn.microsoft.com/en-us/sql/relational-databases/security/dynamic-data-masking)


For a comprehensive list of SQL Server and Azure SQL Managed Instance features, review [features comparison](https://learn.microsoft.com/en-us/azure/azure-sql/database/features-comparison?view=azuresql).
For a list of T-SQL differences between SQL Managed Instance and SQL Server, review [SQL Managed Instance T-SQL differences from SQL Server](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/transact-sql-tsql-differences-sql-server?view=azuresql).
Some SQL Managed Instance feature availability depends on the configured [update policy](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/update-policy?view=azuresql).
[](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/sql-managed-instance-paas-overview?view=azuresql#key-differences-between-sql-server-on-premises-and-sql-managed-instance)
### Key differences between SQL Server on-premises and SQL Managed Instance
SQL Managed Instance benefits from being always-up-to-date in the cloud, which means that some features in SQL Server might be obsolete, retired, or have alternatives. There are specific cases when tools need to recognize that a particular feature works in a slightly different way or that the service is running in an environment you don't fully control.
Some key differences include:
  * High availability is built in and preconfigured by using technology similar to [Always On availability groups](https://learn.microsoft.com/en-us/sql/database-engine/availability-groups/windows/always-on-availability-groups-sql-server).
  * There are only automated backups and point-in-time restore. You can initiate `copy-only` backups that don't interfere with the automatic backup chain.
  * Specifying full physical paths is unsupported, so all corresponding scenarios have to be supported differently: RESTORE DB doesn't support WITH MOVE, CREATE DB doesn't allow physical paths, BULK INSERT works with Azure blobs only, and so on.
  * SQL Managed Instance supports [Microsoft Entra authentication](https://learn.microsoft.com/en-us/azure/azure-sql/database/authentication-aad-overview?view=azuresql) and [Windows Authentication for Microsoft Entra principals (Preview)](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/winauth-azuread-overview?view=azuresql).
  * SQL Managed Instance automatically manages XTP filegroups and files for databases containing In-Memory OLTP objects.
  * SQL Managed Instance supports SQL Server Integration Services (SSIS) and can host an SSIS catalog (SSISDB) that stores SSIS packages, but they're executed on a managed Azure-SSIS Integration Runtime (IR) in Azure Data Factory. See [Create Azure-SSIS IR in Data Factory](https://learn.microsoft.com/en-us/azure/data-factory/create-azure-ssis-integration-runtime). To compare the SSIS features, see [Compare SQL Database to SQL Managed Instance](https://learn.microsoft.com/en-us/azure/data-factory/create-azure-ssis-integration-runtime#comparison-of-sql-database-and-sql-managed-instance).
  * SQL Managed Instance supports connectivity only through the TCP protocol. It doesn't support connectivity through named pipes.
  * You can [stop and start](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/instance-stop-start-how-to?view=azuresql) the instance to save on costs.


[](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/sql-managed-instance-paas-overview?view=azuresql#business-intelligence)
### Business intelligence
Azure SQL Managed Instance doesn't have the Business Intelligence suite natively built-in, but you can use the following services:
  * **SQL Server Integration Services (SSIS)** is part of [Azure Data Factory PaaS](https://learn.microsoft.com/en-us/azure/data-factory/tutorial-deploy-ssis-packages-azure).
  * **SQL Server Analysis Services (SSAS)** is a separate [PaaS](https://learn.microsoft.com/en-us/azure/analysis-services/analysis-services-overview) service in Azure.
  * **SQL Server Reporting Services (SSRS)** , you can use [Power BI paginated reports](https://learn.microsoft.com/en-us/power-bi/paginated-reports/paginated-reports-report-builder-power-bi) instead or host SSRS on an Azure Virtual Machine. While SQL Managed Instance can't run SSRS as a service, it can host [SSRS catalog databases](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/ssrs-report-server-create-a-report-server-database#database-server-version-requirements) for a reporting server installed on Azure Virtual Machine, by using SQL Server authentication.


[](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/sql-managed-instance-paas-overview?view=azuresql#administration-features)
### Administration features
SQL Managed Instance enables system administrators to spend less time on administrative tasks because the service either performs them for you or greatly simplifies those tasks. For example, [OS/RDBMS installation and patching](https://learn.microsoft.com/en-us/azure/azure-sql/database/high-availability-sla-local-zone-redundancy?view=azuresql), [dynamic instance resizing and configuration](https://learn.microsoft.com/en-us/azure/azure-sql/database/single-database-scale?view=azuresql), [backups](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/automated-backups-overview?view=azuresql), [database replication](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/replication-between-two-instances-configure-tutorial?view=azuresql) (including system databases), [high availability configuration](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/high-availability-sla-local-zone-redundancy?view=azuresql), and configuration of health and [performance monitoring](https://learn.microsoft.com/en-us/azure/azure-monitor/insights/azure-sql) data streams.
For more information, see [a list of supported and unsupported SQL Managed Instance features](https://learn.microsoft.com/en-us/azure/azure-sql/database/features-comparison?view=azuresql), and [T-SQL differences between SQL Managed Instance and SQL Server](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/transact-sql-tsql-differences-sql-server?view=azuresql).
[](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/sql-managed-instance-paas-overview?view=azuresql#save-on-costs)
