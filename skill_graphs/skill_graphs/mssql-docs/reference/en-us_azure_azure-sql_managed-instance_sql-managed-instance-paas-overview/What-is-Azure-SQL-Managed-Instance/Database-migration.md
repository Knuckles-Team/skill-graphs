## Database migration
SQL Managed Instance targets user scenarios with mass database migration from on-premises or IaaS database implementations. SQL Managed Instance supports several database migration options that the migration guides discuss. For more information, see [Migration overview: SQL Server to Azure SQL Managed Instance](https://learn.microsoft.com/en-us/azure/azure-sql/migration-guides/managed-instance/sql-server-to-managed-instance-overview?view=azuresql).
[](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/sql-managed-instance-paas-overview?view=azuresql#back-up-and-restore)
### Back up and restore
This migration approach uses SQL Server backups to Azure Blob storage. You can restore backups stored in Azure Blob Storage directly into a SQL managed instance by using the [T-SQL RESTORE command](https://learn.microsoft.com/en-us/sql/t-sql/statements/restore-statements-transact-sql?preserve-view=true&view=azuresqldb-mi-current).
  * For a quickstart that shows how to restore the Wide World Importers - Standard database backup file, see [Restore a backup file to a managed instance](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/restore-sample-database-quickstart?view=azuresql). This quickstart shows that you have to upload a backup file to Azure Blob Storage and secure it by using a shared access signature (SAS).
  * For information about restore from URL, see [Native RESTORE from URL](https://learn.microsoft.com/en-us/azure/azure-sql/migration-guides/managed-instance/sql-server-to-managed-instance-guide?view=azuresql#back-up-and-restore).


You can only restore backups from a SQL managed instance to other SQL managed instances or to either SQL Server 2022 or SQL Server 2025 (based on the [update policy](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/update-policy?view=azuresql)). You can't restore them to other versions of SQL Server or to Azure SQL Database.
[](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/sql-managed-instance-paas-overview?view=azuresql#database-migration-service)
### Database Migration Service
Azure Database Migration Service is a fully managed service designed to enable seamless migrations from multiple database sources to Azure data platforms with minimal downtime. This service streamlines the tasks required to move existing third-party and SQL Server databases to Azure SQL Database, Azure SQL Managed Instance, and SQL Server on Azure VM. See [How to migrate your on-premises database to SQL Managed Instance using Database Migration Service](https://learn.microsoft.com/en-us/azure/dms/tutorial-sql-server-to-managed-instance).
[](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/sql-managed-instance-paas-overview?view=azuresql#managed-instance-link-1)
### Managed Instance link
The [Managed Instance link](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/managed-instance-link-feature-overview?view=azuresql) uses distributed availability groups to extend your SQL Server on-premises Always On availability group hosted anywhere to Azure SQL Managed Instance in a safe and secure manner, replicating data in near real-time.
The link feature facilitates migrating from SQL Server to SQL Managed Instance, which enables:
  * The most performant, minimal downtime migration, compared to all other solutions available today.
  * True online migration to SQL Managed Instance in any service tier.


Because the link feature enables minimal downtime migration, you can migrate to your managed instance as you maintain your primary workload online. Although it's currently possible to achieve online migrations to the General Purpose service tier with other solutions, the link feature is the only solution that allows true online migrations to the Business Critical tier.
[](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/sql-managed-instance-paas-overview?view=azuresql#management-operations)
