## Discontinued services and deprecated features
**Data Quality Services** (DQS) is discontinued in this version of SQL Server. We continue to support DQS in SQL Server 2022 (16.x) and earlier versions. For more information, including how to uninstall DQS during an upgrade, see [SQL Server 2025 known issues](https://learn.microsoft.com/en-us/sql/sql-server/sql-server-2025-known-issues?view=sql-server-ver17#upgrade-fails-if-data-quality-services-is-installed).
**Master Data Services** (MDS) is discontinued in this version of SQL Server. We continue to support MDS in SQL Server 2022 (16.x) and earlier versions.
**Synapse Link** is discontinued in this version of SQL Server. Use [Mirroring in Fabric](https://learn.microsoft.com/en-us/fabric/database/mirrored-database/overview) instead. For more information, see
**Purview access policies** (DevOps policies and data owner policies) are discontinued in this version of SQL Server. Use [Fixed server roles](https://learn.microsoft.com/en-us/sql/relational-databases/security/authentication-access/server-level-roles?view=sql-server-ver17#fixed-server-level-roles-introduced-in-sql-server-2022) instead.
  * In place of the **SQL Performance Monitoring** Purview policy action, use the `##MS_ServerPerformanceStateReader##` and/or `##MS_PerformanceDefinitionReader##` fixed server roles.
  * In place of **SQL Security Auditing** Purview policy action, use the `##MS_ServerSecurityStateReader##` and/or `##MS_SecurityDefinitionReader##` fixed server roles.
  * Use the `##MS_DatabaseConnector##` server role with existing logins, to connect to a database without the need to create a user in that database.


The [Hot add CPU](https://learn.microsoft.com/en-us/sql/relational-databases/thread-and-task-architecture-guide?view=sql-server-ver17#hot-add-cpu) feature is deprecated in this version of SQL Server, and is planned for removal in a future version.
The [lightweight pooling](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/lightweight-pooling-server-configuration-option?view=sql-server-ver17) configuration option and the corresponding **fiber mode** feature is deprecated in this version of SQL Server, and is planned for removal in a future version.
[](https://learn.microsoft.com/en-us/sql/sql-server/what-s-new-in-sql-server-2025?view=sql-server-ver17#breaking-changes)
