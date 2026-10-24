## Key features and capabilities
SQL Managed Instance runs with all of the features of the most recent version of SQL Server, including online operations, automatic plan corrections, and other enterprise performance enhancements. For details about the SQL Server features available in Azure SQL Managed Instance, review [feature comparison](https://learn.microsoft.com/en-us/azure/azure-sql/database/features-comparison?view=azuresql).
The following table provides key capabilities of Azure SQL Managed Instance:
Expand table
**PaaS benefits** | **Business continuity**
---|---
No purchasing or managing hardware
No management overhead to manage underlying infrastructure
Quick provisioning and service scaling
Automated patching and version upgrade
You can [stop and start](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/instance-stop-start-how-to?view=azuresql) the instance to save on costs
Integration with other PaaS data services | 99.99% uptime SLA
Built-in [high availability through zone redundancy](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/high-availability-sla-local-zone-redundancy?view=azuresql)
[Overview of the Managed Instance link](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/managed-instance-link-feature-overview?view=azuresql)
Data protected with [automated backups](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/automated-backups-overview?view=azuresql)
Customer configurable backup retention period
User-initiated [backups](https://learn.microsoft.com/en-us/sql/t-sql/statements/backup-transact-sql?preserve-view=true&view=azuresqldb-mi-current) that can be [restored to SQL Server 2022](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/restore-database-to-sql-server?view=azuresql)
[Point-in-time database restore](https://learn.microsoft.com/en-us/azure/azure-sql/database/recovery-using-backups?view=azuresql#point-in-time-restore) capability
**Security and compliance** | **Management**
Isolated environment ([Connectivity architecture for Azure SQL Managed Instance](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/connectivity-architecture-overview?view=azuresql), single tenant service, dedicated compute and storage)
Adheres to the same compliance standards as Azure SQL Database
[Transparent data encryption (TDE)](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption-azure-sql)
[Use Microsoft Entra authentication](https://learn.microsoft.com/en-us/azure/azure-sql/database/authentication-aad-overview?view=azuresql), single sign-on support
[Microsoft Entra server principals (logins)](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-login-transact-sql?view=azuresqldb-mi-current&preserve-view=true)
[What is Windows Authentication for Microsoft Entra principals on Azure SQL Managed Instance?](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/winauth-azuread-overview?view=azuresql)
[Get started with Azure SQL Managed Instance auditing](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/auditing-configure?view=azuresql)
[Configure Advanced Threat Protection in Azure SQL Managed Instance](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/threat-detection-configure?view=azuresql) | Azure Resource Manager API for automating service provisioning and scaling
Azure portal functionality for manual service provisioning and scaling
Data Migration Service
Azure SQL Managed Instance is certified against a number of compliance standards. For more information, see the [Microsoft Trust Center](https://www.microsoft.com/trust-center/compliance/compliance-overview), where you can find the most current list of Azure SQL Managed Instance compliance certifications. The following table shows characteristics of SQL Managed Instance:
Expand table
Feature | Description
---|---
Azure portal management | Yes
SQL Server version/build | The latest stable SQL Server Database Engine 1
Managed automated backups | Yes
Automatic software patching | Yes
The latest database engine features | Yes
Built-in instance and database monitoring and metrics | Yes
SQL Server Agent jobs | Yes
Number of data files (ROWS) per the database | Multiple
Number of log files (LOG) per database | 1
VNet - Azure Resource Manager deployment | Yes
VNet - Classic deployment model | No
1 Based on the [**Always-up-to-date** update policy](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/update-policy?view=azuresql#always-up-to-date-update-policy). Instances configured with the **SQL Server 2022** update policy have updates from the latest stable SQL Server 2022 Database Engine. Instances configured with the **SQL Server 2025** update policy have updates from the latest stable SQL Server 2025 Database Engine.
[](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/sql-managed-instance-paas-overview?view=azuresql#supported-sql-features)
