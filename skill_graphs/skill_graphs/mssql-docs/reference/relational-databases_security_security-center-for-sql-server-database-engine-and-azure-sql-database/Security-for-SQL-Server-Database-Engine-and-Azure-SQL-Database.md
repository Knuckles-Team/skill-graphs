# Security for SQL Server Database Engine and Azure SQL Database
Feedback
Summarize this article for me
##  In this article
  1. [Authentication: Who are you?](https://learn.microsoft.com/en-us/sql/relational-databases/security/security-center-for-sql-server-database-engine-and-azure-sql-database?view=sql-server-ver17#authentication-who-are-you)
  2. [Authorization: What can you do?](https://learn.microsoft.com/en-us/sql/relational-databases/security/security-center-for-sql-server-database-engine-and-azure-sql-database?view=sql-server-ver17#authorization-what-can-you-do)
  3. [Encryption: Storing Secret Data](https://learn.microsoft.com/en-us/sql/relational-databases/security/security-center-for-sql-server-database-engine-and-azure-sql-database?view=sql-server-ver17#encryption-storing-secret-data)
  4. [Connection Security: Restricting and Securing](https://learn.microsoft.com/en-us/sql/relational-databases/security/security-center-for-sql-server-database-engine-and-azure-sql-database?view=sql-server-ver17#connection-security-restricting-and-securing)
  5. [Auditing: Recording Access](https://learn.microsoft.com/en-us/sql/relational-databases/security/security-center-for-sql-server-database-engine-and-azure-sql-database?view=sql-server-ver17#auditing-recording-access)
  6. [SQL Injection](https://learn.microsoft.com/en-us/sql/relational-databases/security/security-center-for-sql-server-database-engine-and-azure-sql-database?view=sql-server-ver17#sql-injection)
  7. [Related content](https://learn.microsoft.com/en-us/sql/relational-databases/security/security-center-for-sql-server-database-engine-and-azure-sql-database?view=sql-server-ver17#related-content)
  8. [Get help](https://learn.microsoft.com/en-us/sql/relational-databases/security/security-center-for-sql-server-database-engine-and-azure-sql-database?view=sql-server-ver17#-get-help)

Show 4 more
**Applies to:** ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure SQL Database](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure SQL Managed Instance](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure Synapse Analytics](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Analytics Platform System (PDW)](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to)
This page provides links to help you locate the information that you need about security and protection in the SQL Server Database Engine and Azure SQL Database.
**Legend**
![Screenshot of the legend that explains the feature availability icons.](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-legend.png?view=sql-server-ver17)
[](https://learn.microsoft.com/en-us/sql/relational-databases/security/security-center-for-sql-server-database-engine-and-azure-sql-database?view=sql-server-ver17#authentication-who-are-you)
## Authentication: Who are you?
Expand table
Feature | Link
---|---
**Who Authenticates?**

![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-sqlserver.png?view=sql-server-ver17) Windows Authentication
![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-both.png?view=sql-server-ver17) SQL Server Authentication
![](https://learn.microsoft.com/en-us/sql/relational-databases/security/media/security-center-both.png?view=sql-server-ver17) Microsoft Entra ID ([formerly Azure Active Directory](https://learn.microsoft.com/en-us/entra/fundamentals/new-name)) | Who Authenticates? (Windows or SQL Server)
[Choose an authentication mode](https://learn.microsoft.com/en-us/sql/relational-databases/security/choose-an-authentication-mode?view=sql-server-ver17)
[Connect to Azure SQL with Microsoft Entra authentication](https://learn.microsoft.com/en-us/azure/azure-sql/database/authentication-aad-overview)
**Where Authenticated?**

![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-both.png?view=sql-server-ver17) At `master` database: Logins and Database Users
![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-both.png?view=sql-server-ver17) At User Database: Contained DB Users | Authenticate at the `master` database (Logins and database users)
[Create a login](https://learn.microsoft.com/en-us/sql/relational-databases/security/authentication-access/create-a-login?view=sql-server-ver17)
[Managing Databases and Logins in Azure SQL Database](https://learn.microsoft.com/en-us/previous-versions/azure/ee336235\(v=azure.100\))
[Create a database user](https://learn.microsoft.com/en-us/sql/relational-databases/security/authentication-access/create-a-database-user?view=sql-server-ver17)
Authenticate at a user database
[Make your database portable by using contained databases](https://learn.microsoft.com/en-us/sql/relational-databases/security/contained-database-users-making-your-database-portable?view=sql-server-ver17)
**Using Other Identities**

![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-both.png?view=sql-server-ver17) Credentials
![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-sqlserver.png?view=sql-server-ver17) Execute as Another Login
![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-both.png?view=sql-server-ver17) Execute as Another Database User |  [Credentials (Database Engine)](https://learn.microsoft.com/en-us/sql/relational-databases/security/authentication-access/credentials-database-engine?view=sql-server-ver17)
[EXECUTE AS](https://learn.microsoft.com/en-us/sql/t-sql/statements/execute-as-transact-sql?view=sql-server-ver17)
[EXECUTE AS](https://learn.microsoft.com/en-us/sql/t-sql/statements/execute-as-transact-sql?view=sql-server-ver17)
[](https://learn.microsoft.com/en-us/sql/relational-databases/security/security-center-for-sql-server-database-engine-and-azure-sql-database?view=sql-server-ver17#authorization-what-can-you-do)
## Authorization: What can you do?
Expand table
Feature | Link
---|---
**Granting, Revoking, and Denying Permissions**

![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-both.png?view=sql-server-ver17) Securable Classes
![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-sqlserver.png?view=sql-server-ver17) Granular Server Permissions
![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-both.png?view=sql-server-ver17) Granular Database Permissions |  [Permissions Hierarchy (Database Engine)](https://learn.microsoft.com/en-us/sql/relational-databases/security/permissions-hierarchy-database-engine?view=sql-server-ver17)
[Permissions (Database Engine)](https://learn.microsoft.com/en-us/sql/relational-databases/security/permissions-database-engine?view=sql-server-ver17)
[Securables](https://learn.microsoft.com/en-us/sql/relational-databases/security/securables?view=sql-server-ver17)
[Get started with Database Engine permissions](https://learn.microsoft.com/en-us/sql/relational-databases/security/authentication-access/getting-started-with-database-engine-permissions?view=sql-server-ver17)
**Security by Roles**

![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-sqlserver.png?view=sql-server-ver17) Server Level Roles
![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-both.png?view=sql-server-ver17) Database Level Roles |  [Server-level roles](https://learn.microsoft.com/en-us/sql/relational-databases/security/authentication-access/server-level-roles?view=sql-server-ver17)
[Database-level roles](https://learn.microsoft.com/en-us/sql/relational-databases/security/authentication-access/database-level-roles?view=sql-server-ver17)
**Restricting Data Access to Selected Data Elements**

![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-both.png?view=sql-server-ver17) Restrict Data Access With Views/Procedures
![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-both.png?view=sql-server-ver17) Row-Level Security
![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-both.png?view=sql-server-ver17) Dynamic Data Masking
![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-both.png?view=sql-server-ver17) Signed Objects | Restrict Data Access Using [Views](https://learn.microsoft.com/en-us/sql/relational-databases/views/views?view=sql-server-ver17) and [Stored procedures (Database Engine)](https://learn.microsoft.com/en-us/sql/relational-databases/stored-procedures/stored-procedures-database-engine?view=sql-server-ver17)
[Row-level security](https://learn.microsoft.com/en-us/sql/relational-databases/security/row-level-security?view=sql-server-ver17)
[Row-level security](https://learn.microsoft.com/en-us/sql/relational-databases/security/row-level-security?view=sql-server-ver17)
[Dynamic data masking](https://learn.microsoft.com/en-us/sql/relational-databases/security/dynamic-data-masking?view=sql-server-ver17)
[Dynamic Data Masking (Azure SQL Database)](https://learn.microsoft.com/en-us/azure/azure-sql/database/dynamic-data-masking-overview)
[ADD SIGNATURE](https://learn.microsoft.com/en-us/sql/t-sql/statements/add-signature-transact-sql?view=sql-server-ver17)
[](https://learn.microsoft.com/en-us/sql/relational-databases/security/security-center-for-sql-server-database-engine-and-azure-sql-database?view=sql-server-ver17#encryption-storing-secret-data)
## Encryption: Storing Secret Data
Expand table
Feature | Link
---|---
**Encrypting Files**

![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-sqlserver.png?view=sql-server-ver17) BitLocker Encryption (Drive Level)
![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-sqlserver.png?view=sql-server-ver17) NTFS Encryption (Folder Level)
![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-both.png?view=sql-server-ver17) Transparent Data Encryption (File Level)
![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-both.png?view=sql-server-ver17) Backup Encryption (File Level) |  [BitLocker (Drive Level)](https://learn.microsoft.com/en-us/troubleshoot/windows-client/windows-security/enable-bitlocker-device-encryption-local-hard-disk)
[NTFS Encryption (Folder Level)](https://learn.microsoft.com/en-us/previous-versions/tn-archive/dd163562\(v=technet.10\))
[Transparent data encryption (TDE)](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver17)
[Backup encryption](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/backup-encryption?view=sql-server-ver17)
**Encrypting Sources**

![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-sqlserver.png?view=sql-server-ver17) Extensible Key Management Module
![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-sqlserver.png?view=sql-server-ver17) Keys Stored in the Azure Key Vault
![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-both.png?view=sql-server-ver17) Always Encrypted |  [Extensible Key Management (EKM)](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/extensible-key-management-ekm?view=sql-server-ver17)
[Extensible Key Management Using Azure Key Vault (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/extensible-key-management-using-azure-key-vault-sql-server?view=sql-server-ver17)
[Always Encrypted](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-database-engine?view=sql-server-ver17)
**Column, Data, & Key Encryption**

![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-both.png?view=sql-server-ver17) Encrypt by Certificate
![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-both.png?view=sql-server-ver17) Encrypt by Symmetric Key
![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-both.png?view=sql-server-ver17) Encrypt by Asymmetric Key
![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-both.png?view=sql-server-ver17) Encrypt by Passphrase |  [ENCRYPTBYCERT](https://learn.microsoft.com/en-us/sql/t-sql/functions/encryptbycert-transact-sql?view=sql-server-ver17)
[ENCRYPTBYASYMKEY](https://learn.microsoft.com/en-us/sql/t-sql/functions/encryptbyasymkey-transact-sql?view=sql-server-ver17)
[ENCRYPTBYKEY](https://learn.microsoft.com/en-us/sql/t-sql/functions/encryptbykey-transact-sql?view=sql-server-ver17)
[ENCRYPTBYPASSPHRASE](https://learn.microsoft.com/en-us/sql/t-sql/functions/encryptbypassphrase-transact-sql?view=sql-server-ver17)
[Encrypt a Column of Data](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/encrypt-a-column-of-data?view=sql-server-ver17)
[](https://learn.microsoft.com/en-us/sql/relational-databases/security/security-center-for-sql-server-database-engine-and-azure-sql-database?view=sql-server-ver17#connection-security-restricting-and-securing)
## Connection Security: Restricting and Securing
Expand table
Feature | Link
---|---
**Firewall Protection**

![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-sqlserver.png?view=sql-server-ver17) Windows Firewall Settings
![](https://learn.microsoft.com/en-us/sql/relational-databases/security/media/security-center-sqldb.png?view=sql-server-ver17) Azure Service Firewall Settings
![](https://learn.microsoft.com/en-us/sql/relational-databases/security/media/security-center-sqldb.png?view=sql-server-ver17) Database Firewall Settings |  [Configure Windows Firewall for Database Engine access](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/configure-a-windows-firewall-for-database-engine-access?view=sql-server-ver17)
[sp_set_database_firewall_rule (Azure SQL Database)](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-set-database-firewall-rule-azure-sql-database?view=sql-server-ver17)
[sp_set_firewall_rule (Azure SQL Database)](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-set-firewall-rule-azure-sql-database?view=sql-server-ver17)
**Encrypting Data in Transit**

![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-both.png?view=sql-server-ver17) Forced TLS/SSL Connections
![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-sqlserver.png?view=sql-server-ver17) Optional SSL Connections |  [Configure SQL Server Database Engine for encrypting connections](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/configure-sql-server-encryption?view=sql-server-ver17)
[Configure SQL Server Database Engine for encrypting connections](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/configure-sql-server-encryption?view=sql-server-ver17), [Network security](https://learn.microsoft.com/en-us/azure/sql-database/sql-database-security-best-practice#network-security)
[TLS 1.2 support for Microsoft SQL Server](https://learn.microsoft.com/en-us/troubleshoot/sql/database-engine/connect/tls-1-2-support-microsoft-sql-server)
[](https://learn.microsoft.com/en-us/sql/relational-databases/security/security-center-for-sql-server-database-engine-and-azure-sql-database?view=sql-server-ver17#auditing-recording-access)
## Auditing: Recording Access
Expand table
Feature | Link
---|---
**Automated Auditing**

![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-sqlserver.png?view=sql-server-ver17) SQL Server Audit (Server and DB Level)
![](https://learn.microsoft.com/en-us/sql/relational-databases/security/media/security-center-sqldb.png?view=sql-server-ver17) SQL Database Audit (Database Level)
![](https://learn.microsoft.com/en-us/sql/relational-databases/security/media/security-center-sqldb.png?view=sql-server-ver17) Detect threats |
[SQL Server Audit (Database Engine)](https://learn.microsoft.com/en-us/sql/relational-databases/security/auditing/sql-server-audit-database-engine?view=sql-server-ver17)
[SQL Database Auditing](https://learn.microsoft.com/en-us/azure/azure-sql/database/auditing-overview)
[Get started with SQL Database Advanced Threat Protection](https://learn.microsoft.com/en-us/azure/azure-sql/database/threat-detection-configure)
[SQL Database Vulnerability Assessment](https://learn.microsoft.com/en-us/azure/sql-database/sql-vulnerability-assessment)
**Custom Audit**

![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-both.png?view=sql-server-ver17) Triggers | Custom Audit Implementation: Creating [DDL Triggers](https://learn.microsoft.com/en-us/sql/relational-databases/triggers/ddl-triggers?view=sql-server-ver17) and [DML Triggers](https://learn.microsoft.com/en-us/sql/relational-databases/triggers/dml-triggers?view=sql-server-ver17)
**Compliance**

![](https://learn.microsoft.com/en-us/sql/relational-databases/performance/media/security-center-both.png?view=sql-server-ver17) Compliance | SQL Server:
[Common Criteria](https://go.microsoft.com/fwlink/?LinkId=616319)
SQL Database:
[Microsoft Azure Trust Center: Compliance by Feature](https://azure.microsoft.com/support/trust-center/services/)
[](https://learn.microsoft.com/en-us/sql/relational-databases/security/security-center-for-sql-server-database-engine-and-azure-sql-database?view=sql-server-ver17#sql-injection)
## SQL Injection
SQL injection is an attack in which malicious code is inserted into strings that are later passed to the Database Engine for parsing and execution. Any procedure that constructs SQL statements should be reviewed for injection vulnerabilities because SQL Server will execute all syntactically valid queries that it receives. All database systems have some risk of SQL Injection, and many of the vulnerabilities are introduced in the application that is querying the Database Engine. You can thwart SQL injection attacks by using stored procedures and parameterized commands, avoiding dynamic SQL, and restricting permissions on all users. For more information, see [SQL injection](https://learn.microsoft.com/en-us/sql/relational-databases/security/sql-injection?view=sql-server-ver17).
Additional links for application programmers:
  * [Application Security Scenarios in SQL Server](https://learn.microsoft.com/en-us/dotnet/framework/data/adonet/sql/application-security-scenarios-in-sql-server)
  * [Writing Secure Dynamic SQL in SQL Server](https://learn.microsoft.com/en-us/dotnet/framework/data/adonet/sql/writing-secure-dynamic-sql-in-sql-server)
  * [How To: Protect From SQL Injection in ASP.NET](https://learn.microsoft.com/en-us/previous-versions/msp-n-p/ff648339\(v=pandp.10\))


[](https://learn.microsoft.com/en-us/sql/relational-databases/security/security-center-for-sql-server-database-engine-and-azure-sql-database?view=sql-server-ver17#related-content)
## Related content
  * [Get started with Database Engine permissions](https://learn.microsoft.com/en-us/sql/relational-databases/security/authentication-access/getting-started-with-database-engine-permissions?view=sql-server-ver17)
  * [Securing SQL Server](https://learn.microsoft.com/en-us/sql/relational-databases/security/securing-sql-server?view=sql-server-ver17)
  * [Principals (Database Engine)](https://learn.microsoft.com/en-us/sql/relational-databases/security/authentication-access/principals-database-engine?view=sql-server-ver17)
  * [SQL Server Certificates and Asymmetric Keys](https://learn.microsoft.com/en-us/sql/relational-databases/security/sql-server-certificates-and-asymmetric-keys?view=sql-server-ver17)
  * [SQL Server encryption](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/sql-server-encryption?view=sql-server-ver17)
  * [Surface area configuration](https://learn.microsoft.com/en-us/sql/relational-databases/security/surface-area-configuration?view=sql-server-ver17)
  * [Strong Passwords](https://learn.microsoft.com/en-us/sql/relational-databases/security/strong-passwords?view=sql-server-ver17)
  * [TRUSTWORTHY database property](https://learn.microsoft.com/en-us/sql/relational-databases/security/trustworthy-database-property?view=sql-server-ver17)
  * [What's new in SQL Server 2019](https://learn.microsoft.com/en-us/sql/sql-server/what-s-new-in-sql-server-2019?view=sql-server-ver17)
  * [Protecting Your SQL Server Intellectual Property](https://learn.microsoft.com/en-us/sql/relational-databases/security/protecting-your-sql-server-intellectual-property?view=sql-server-ver17)


[](https://learn.microsoft.com/en-us/sql/relational-databases/security/security-center-for-sql-server-database-engine-and-azure-sql-database?view=sql-server-ver17#-get-help)
##  ![](https://learn.microsoft.com/en-us/sql/includes/media/info-tip.svg?view=sql-server-ver17) Get help
  * [Microsoft Q & A (SQL Server)](https://learn.microsoft.com/en-us/answers/products/sql-server)
  * [Microsoft SQL Server License Terms and Information](https://www.microsoft.com/download/details.aspx?id=39299)
  * [Support options for business users](https://support.serviceshub.microsoft.com/supportforbusiness)
  * [Contact Microsoft](https://support.microsoft.com/contactus/)


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
  * [ Securing SQL Server - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/security/securing-sql-server?source=recommendations)
Use these articles to create and implement an effective security plan in SQL Server. Learn about the platform, authentication, objects, and applications.
  * [ SQL Server security best practices - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/security/sql-server-security-best-practices?source=recommendations)
This article provides general guidance for securing SQL Server running in an Azure virtual machine.
  * [ Secure your SQL Server - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/security/secure-sql-server?source=recommendations)
Learn how to secure SQL Server, with best practices for protecting data, manage access, and defend against common threats.
  * [ Vulnerability assessment for SQL Server - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/security/sql-vulnerability-assessment?source=recommendations)
Use the vulnerability assessment scanner to discover, track, and remediate potential database vulnerabilities in SQL Server.
  * [ What's New in SQL Server 2022 - SQL Server ](https://learn.microsoft.com/en-us/sql/sql-server/what-s-new-in-sql-server-2022?source=recommendations)
Learn about new features for SQL Server 2022 (16.x), which gives you choices of development languages, data types, environments, and operating systems.
  * [ Surface area configuration - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/security/surface-area-configuration?source=recommendations)
Learn how to change feature defaults for SQL Server installation and selectively enable or disable features of a running instance of SQL Server.
  * [ Determine effective Database Engine permissions - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/security/authentication-access/determining-effective-database-engine-permissions?source=recommendations)
Learn how to determine who has permissions to various objects in the SQL Server Database Engine, including the current and previous permissions systems.


Show 4 more
Learning path
[ Implement a secure environment for a database service - Training ](https://learn.microsoft.com/en-us/training/paths/implement-secure-environment-database-service/?source=recommendations)
Implement a secure environment for a database service
Certification
[ Microsoft Certified: Information Security Administrator Associate - Certifications ](https://learn.microsoft.com/en-us/credentials/certifications/information-security-administrator/?source=recommendations)
As an Information Security Administrator, you plan and implement information security of sensitive data by using Microsoft Purview and related services.
Mar 8, 4 PM - Mar 8, 4 PM
Experiment with what's next in AI-driven apps and agent design
* * *
  * Last updated on 06/30/2025


##  In this article
  1. [Authentication: Who are you?](https://learn.microsoft.com/en-us/sql/relational-databases/security/security-center-for-sql-server-database-engine-and-azure-sql-database?view=sql-server-ver17#authentication-who-are-you)
  2. [Authorization: What can you do?](https://learn.microsoft.com/en-us/sql/relational-databases/security/security-center-for-sql-server-database-engine-and-azure-sql-database?view=sql-server-ver17#authorization-what-can-you-do)
  3. [Encryption: Storing Secret Data](https://learn.microsoft.com/en-us/sql/relational-databases/security/security-center-for-sql-server-database-engine-and-azure-sql-database?view=sql-server-ver17#encryption-storing-secret-data)
  4. [Connection Security: Restricting and Securing](https://learn.microsoft.com/en-us/sql/relational-databases/security/security-center-for-sql-server-database-engine-and-azure-sql-database?view=sql-server-ver17#connection-security-restricting-and-securing)
  5. [Auditing: Recording Access](https://learn.microsoft.com/en-us/sql/relational-databases/security/security-center-for-sql-server-database-engine-and-azure-sql-database?view=sql-server-ver17#auditing-recording-access)
  6. [SQL Injection](https://learn.microsoft.com/en-us/sql/relational-databases/security/security-center-for-sql-server-database-engine-and-azure-sql-database?view=sql-server-ver17#sql-injection)
  7. [Related content](https://learn.microsoft.com/en-us/sql/relational-databases/security/security-center-for-sql-server-database-engine-and-azure-sql-database?view=sql-server-ver17#related-content)
  8. [Get help](https://learn.microsoft.com/en-us/sql/relational-databases/security/security-center-for-sql-server-database-engine-and-azure-sql-database?view=sql-server-ver17#-get-help)


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
[ Sign in ](https://learn.microsoft.com/en-us/sql/relational-databases/security/security-center-for-sql-server-database-engine-and-azure-sql-database?view=sql-server-ver17)
[English (United States)](https://learn.microsoft.com/en-us/locale?target=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fsql%2Frelational-databases%2Fsecurity%2Fsecurity-center-for-sql-server-database-engine-and-azure-sql-database%3Fview%3Dsql-server-ver17)
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
