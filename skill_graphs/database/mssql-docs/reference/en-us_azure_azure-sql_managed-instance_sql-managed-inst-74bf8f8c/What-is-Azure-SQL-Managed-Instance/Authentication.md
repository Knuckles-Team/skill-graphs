## Authentication
SQL Managed Instance authentication refers to how users prove their identity when connecting to the database. SQL Managed Instance supports three types of authentication:
  * **SQL Authentication** : This authentication method uses a username and password.
  * **Microsoft Entra authentication** : This authentication method uses identities managed by Microsoft Entra ID and is supported for managed and integrated domains. Use Active Directory authentication (integrated security) [whenever possible](https://learn.microsoft.com/en-us/sql/relational-databases/security/choose-an-authentication-mode).
  * **Windows authentication for Microsoft Entra principals** : [Kerberos authentication for Microsoft Entra principals](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/winauth-azuread-overview?view=azuresql) enables Windows authentication for Azure SQL Managed Instance. Windows authentication for managed instances empowers customers to move existing services to the cloud while maintaining a seamless user experience and provides the basis for infrastructure modernization.


[](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/sql-managed-instance-paas-overview?view=azuresql#authorization)
### Authorization
Authorization refers to what a user can do within a database in Azure SQL Managed Instance. Your user account's database role memberships and object-level permissions control authorization. SQL Managed Instance has the same authorization capabilities as SQL Server 2022.
[](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/sql-managed-instance-paas-overview?view=azuresql#database-migration)
