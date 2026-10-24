## Security
Expand table
New feature or update | Details
---|---
[Security cache improvements](https://learn.microsoft.com/en-us/sql/relational-databases/security-cache?view=sql-server-ver17) | Invalidates caches for only a specific login. When security cache entries are invalidated, only those entries belonging to the affected login are affected. This improvement minimizes the impact of non-cache permissions validation for unaffected login users.
[OAEP padding mode support for RSA encryption](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/encryption-hierarchy?view=sql-server-ver17) | Support for certificates and asymmetric keys, adding security layers to encryption and decryption processes.
[PBKDF for password hashes on by default](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-application-role-transact-sql?view=sql-server-ver17#remarks) | Uses **PBKDF2** for password hashes by default, enhancing password security and helping customers comply with NIST SP 800-63b.
[Managed identity with Microsoft Entra authentication](https://learn.microsoft.com/en-us/sql/sql-server/azure-arc/managed-identity?view=sql-server-ver17) | Can use the Arc-enabled server managed identity in outbound connections to communicate with Azure resources, and inbound connections for external users to connect to SQL Server. Requires SQL Server enabled by Azure Arc.
[Back up to/restore from URL with managed identity](https://learn.microsoft.com/en-us/sql/sql-server/azure-arc/backup-to-url?view=sql-server-ver17) | Back up to, or restore from, URL with a managed identity. Requires SQL Server enabled by Azure Arc.
[Managed Identity support for Extensible Key Management with Azure Key Vault](https://learn.microsoft.com/en-us/sql/sql-server/azure-arc/managed-identity-extensible-key-management?view=sql-server-ver17) | Supported for EKM with AKV and Managed Hardware Security Modules (HSM). Requires SQL Server enabled by Azure Arc.
[Create Microsoft Entra logins and users with nonunique display names](https://learn.microsoft.com/en-us/azure/azure-sql/database/authentication-microsoft-entra-create-users-with-nonunique-names) | Support for the T-SQL syntax `WITH OBJECT_ID` when using the [CREATE LOGIN](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-login-transact-sql?view=sql-server-ver17&preserve-view=true#with-object_id--objectid) or [CREATE USER](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-user-transact-sql?view=sql-server-ver17#with-object_id--objectid) statement.
[Support custom password policy on Linux](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-custom-password-policy?view=sql-server-ver17) | Enforce a custom password policy for SQL authentication logins on SQL Server on Linux.
[Configure TLS 1.3 encryption with TDS 8.0 support](https://learn.microsoft.com/en-us/sql/relational-databases/security/networking/tds-8?view=sql-server-ver17#sql-server-2025-support) | TLS 1.3 encryption added with TDS 8 for the following features:
- [SQL Server Agent](https://learn.microsoft.com/en-us/ssms/agent/sql-server-agent#tds-80-and-strict-encryption-support)
- [sqlcmd utility](https://learn.microsoft.com/en-us/sql/tools/sqlcmd/sqlcmd-utility?view=sql-server-ver17#tds-80-support)
- [bcp utility](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17#tds-80-support)
- [SQL Writer service](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/sql-writer-service?view=sql-server-ver17)
- [Configure usage and diagnostic data collection for SQL Server (CEIP)](https://learn.microsoft.com/en-us/sql/sql-server/usage-and-diagnostic-data-configuration-for-sql-server?view=sql-server-ver17)
- [Data virtualization with PolyBase in SQL Server](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-guide?view=sql-server-ver17#sql-server-2025-polybase-enhancements)
- [Always On availability groups](https://learn.microsoft.com/en-us/sql/relational-databases/security/networking/connect-with-strict-encryption?view=sql-server-ver17#connect-to-an-always-on-availability-group)
- [Always On failover cluster instances (FCI)](https://learn.microsoft.com/en-us/sql/relational-databases/security/networking/connect-with-strict-encryption?view=sql-server-ver17#connect-to-a-failover-cluster-instance)
- [Linked servers](https://learn.microsoft.com/en-us/sql/relational-databases/linked-servers/linked-servers-database-engine?view=sql-server-ver17#related-content)
- [Transactional replication](https://learn.microsoft.com/en-us/sql/relational-databases/replication/transactional/transactional-replication?view=sql-server-ver17#configure-tls-13-encryption)
- [Merge replication](https://learn.microsoft.com/en-us/sql/relational-databases/replication/merge/merge-replication?view=sql-server-ver17#configure-tls-13-encryption)
- [Peer-to-peer](https://learn.microsoft.com/en-us/sql/relational-databases/replication/transactional/peer-to-peer-transactional-replication?view=sql-server-ver17#configure-tls-13-encryption)
- [Snapshot replication](https://learn.microsoft.com/en-us/sql/relational-databases/replication/snapshot-replication?view=sql-server-ver17#configure-tls-13-encryption)
- [Log shipping](https://learn.microsoft.com/en-us/sql/database-engine/log-shipping/about-log-shipping-sql-server?view=sql-server-ver17#enforce-tls-13-encryption)

Review [Breaking changes](https://learn.microsoft.com/en-us/sql/database-engine/breaking-changes-to-database-engine-features-in-sql-server-2025?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/sql-server/what-s-new-in-sql-server-2025?view=sql-server-ver17#database-engine)
