## Advanced security and compliance
SQL Database provides a range of [built-in security and compliance features](https://learn.microsoft.com/en-us/azure/active-directory/identity-protection/concept-identity-protection-security-overview) to help your application meet various security and compliance requirements.
Microsoft has certified Azure SQL Database (all deployment options) against a number of compliance standards. For more information, see the [Microsoft Azure Trust Center](https://microsoft.com/trust-center/product-overview), where you can find the most current list of SQL Database compliance certifications.
[](https://learn.microsoft.com/en-us/azure/azure-sql/database/sql-database-paas-overview?view=azuresql#advance-threat-protection)
###  Advanced threat protection
Microsoft Defender for SQL is a unified package for advanced SQL security capabilities. It includes functionality for managing your database vulnerabilities, and detecting anomalous activities that might indicate a threat to your database. It provides a single location for enabling and managing these capabilities.
  * [Vulnerability assessment](https://learn.microsoft.com/en-us/azure/defender-for-cloud/sql-azure-vulnerability-assessment-overview):
This service can discover, track, and help you remediate potential database vulnerabilities. It provides visibility into your security state, and includes actionable steps to resolve security issues, and enhance your database fortifications.
  * [Threat detection](https://learn.microsoft.com/en-us/azure/azure-sql/database/threat-detection-configure?view=azuresql):
This feature detects anomalous activities that indicate unusual and potentially harmful attempts to access or exploit your database. It continuously monitors your database for suspicious activities, and provides immediate security alerts on potential vulnerabilities, SQL injection attacks, and anomalous database access patterns. Threat detection alerts provide details of the suspicious activity, and recommend action on how to investigate and mitigate the threat.


[](https://learn.microsoft.com/en-us/azure/azure-sql/database/sql-database-paas-overview?view=azuresql#auditing-for-compliance-and-security)
### Auditing for compliance and security
[Auditing](https://learn.microsoft.com/en-us/azure/azure-sql/database/auditing-overview?view=azuresql) tracks database events and writes them to an audit log in your Azure storage account. Auditing can help you maintain regulatory compliance, understand database activity, and gain insight into discrepancies and anomalies that might indicate business concerns or suspected security violations.
[](https://learn.microsoft.com/en-us/azure/azure-sql/database/sql-database-paas-overview?view=azuresql#data-encryption)
### Data encryption
SQL Database helps secure your data by providing encryption. For data in motion, it uses [transport layer security](https://learn.microsoft.com/en-us/troubleshoot/sql/database-engine/connect/tls-1-2-support-microsoft-sql-server). For data at rest, it uses [transparent data encryption](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption-azure-sql). For data in use, it uses [Always Encrypted](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-database-engine).
[](https://learn.microsoft.com/en-us/azure/azure-sql/database/sql-database-paas-overview?view=azuresql#data-discovery-and-classification)
### Data discovery and classification
[Data discovery and classification](https://learn.microsoft.com/en-us/azure/azure-sql/database/data-discovery-and-classification-overview?view=azuresql) provides capabilities built into Azure SQL Database for discovering, classifying, labeling, and protecting the sensitive data in your databases. It provides visibility into your database classification state, and tracks the access to sensitive data within the database and beyond its borders.
[](https://learn.microsoft.com/en-us/azure/azure-sql/database/sql-database-paas-overview?view=azuresql#microsoft-entra-integration-and-multifactor-authentication)
### Microsoft Entra integration and multifactor authentication
SQL Database enables you to centrally manage identities of database user and other Microsoft services with [Microsoft Entra integration](https://learn.microsoft.com/en-us/azure/azure-sql/database/authentication-aad-overview?view=azuresql). This capability simplifies permission management and enhances security. Microsoft Entra ID ([formerly Azure Active Directory](https://learn.microsoft.com/en-us/entra/fundamentals/new-name)) supports [multifactor authentication](https://learn.microsoft.com/en-us/azure/azure-sql/database/authentication-mfa-ssms-overview?view=azuresql) to increase data and application security, while supporting a single sign-in process.
[](https://learn.microsoft.com/en-us/azure/azure-sql/database/sql-database-paas-overview?view=azuresql#easy-to-use-tools)
