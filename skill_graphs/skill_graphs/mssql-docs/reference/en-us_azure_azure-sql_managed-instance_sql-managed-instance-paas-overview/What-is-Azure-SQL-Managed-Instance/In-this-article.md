##  In this article
  1. [Overview](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/sql-managed-instance-paas-overview?view=azuresql#overview)
  2. [Key features and capabilities](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/sql-managed-instance-paas-overview?view=azuresql#key-features-and-capabilities)
  3. [Supported SQL features](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/sql-managed-instance-paas-overview?view=azuresql#supported-sql-features)
  4. [Save on costs](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/sql-managed-instance-paas-overview?view=azuresql#save-on-costs)
  5. [vCore-based purchasing model](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/sql-managed-instance-paas-overview?view=azuresql#vcore-based-purchasing-model)
  6. [Service tiers](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/sql-managed-instance-paas-overview?view=azuresql#service-tiers)
  7. [High availability](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/sql-managed-instance-paas-overview?view=azuresql#high-availability)
  8. [Managed Instance link](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/sql-managed-instance-paas-overview?view=azuresql#managed-instance-link)
  9. [License-free DR benefit](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/sql-managed-instance-paas-overview?view=azuresql#license-free-dr-benefit)
  10. [Advanced security and compliance](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/sql-managed-instance-paas-overview?view=azuresql#advanced-security-and-compliance)
  11. [Microsoft Entra integration](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/sql-managed-instance-paas-overview?view=azuresql#microsoft-entra-integration)
  12. [Authentication](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/sql-managed-instance-paas-overview?view=azuresql#authentication)
  13. [Database migration](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/sql-managed-instance-paas-overview?view=azuresql#database-migration)
  14. [Management operations](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/sql-managed-instance-paas-overview?view=azuresql#management-operations)
  15. [Programmatically identify a SQL managed instance](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/sql-managed-instance-paas-overview?view=azuresql#programmatically-identify-a-sql-managed-instance)
  16. [Related content](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/sql-managed-instance-paas-overview?view=azuresql#related-content)

Show 12 more
**Applies to:** ![](https://learn.microsoft.com/en-us/azure/azure-sql/media/applies-to/yes-icon.svg?view=azuresql) [Azure SQL Managed Instance](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide#applies-to)
This article provides an overview of Azure SQL Managed Instance, a fully managed platform as a service (PaaS) database engine that handles most database management functions such as upgrading, patching, backups, and monitoring without user involvement.
[Try Azure SQL Managed Instance free of charge](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/free-offer?view=azuresql) and get 720 vCore hours on a General Purpose SQL Managed Instance with up to 100 databases per instance for the first 12 months.
Azure SQL Managed Instance is a scalable cloud database service that's always running on the latest stable version of the [SQL Server Database Engine](https://learn.microsoft.com/en-us/sql/sql-server/sql-server-technical-documentation) and a patched OS with [99.99% built-in high availability](https://azure.microsoft.com/support/legal/sla/azure-sql-database), offering close to 100% feature compatibility with SQL Server. PaaS capabilities built into Azure SQL Managed enable you to focus on domain-specific database administration and optimization activities that are critical for your business while Microsoft handles backups, as well as patching and updating of the SQL and operating system code, which removes the burden on managing the underlying infrastructure.
If you're new to Azure SQL Managed Instance, check out the _Azure SQL Managed Instance_ video from our in-depth [Azure SQL video series](https://learn.microsoft.com/en-us/shows/Azure-SQL-for-Beginners/?WT.mc_id=azuresql4beg_azuresql-ch9-niner):
[Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/fundamentals/new-name) was previously known as Azure Active Directory (Azure AD).
[](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/sql-managed-instance-paas-overview?view=azuresql#overview)
##  In this article
  1. [Overview](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/sql-managed-instance-paas-overview?view=azuresql#overview)
  2. [Key features and capabilities](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/sql-managed-instance-paas-overview?view=azuresql#key-features-and-capabilities)
  3. [Supported SQL features](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/sql-managed-instance-paas-overview?view=azuresql#supported-sql-features)
  4. [Save on costs](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/sql-managed-instance-paas-overview?view=azuresql#save-on-costs)
  5. [vCore-based purchasing model](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/sql-managed-instance-paas-overview?view=azuresql#vcore-based-purchasing-model)
  6. [Service tiers](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/sql-managed-instance-paas-overview?view=azuresql#service-tiers)
  7. [High availability](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/sql-managed-instance-paas-overview?view=azuresql#high-availability)
  8. [Managed Instance link](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/sql-managed-instance-paas-overview?view=azuresql#managed-instance-link)
  9. [License-free DR benefit](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/sql-managed-instance-paas-overview?view=azuresql#license-free-dr-benefit)
  10. [Advanced security and compliance](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/sql-managed-instance-paas-overview?view=azuresql#advanced-security-and-compliance)
  11. [Microsoft Entra integration](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/sql-managed-instance-paas-overview?view=azuresql#microsoft-entra-integration)
  12. [Authentication](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/sql-managed-instance-paas-overview?view=azuresql#authentication)
  13. [Database migration](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/sql-managed-instance-paas-overview?view=azuresql#database-migration)
  14. [Management operations](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/sql-managed-instance-paas-overview?view=azuresql#management-operations)
  15. [Programmatically identify a SQL managed instance](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/sql-managed-instance-paas-overview?view=azuresql#programmatically-identify-a-sql-managed-instance)
  16. [Related content](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/sql-managed-instance-paas-overview?view=azuresql#related-content)

Show 7 more
Was this page helpful?
Yes No No
Need help with this topic?
Want to try using Ask Learn to clarify or guide you through this topic?
Ask Learn Ask Learn
Suggest a fix?
