# About log shipping (SQL Server)
Feedback
Summarize this article for me
##  In this article
  1. [Log shipping overview](https://learn.microsoft.com/en-us/sql/database-engine/log-shipping/about-log-shipping-sql-server?view=sql-server-ver17#log-shipping-overview)
  2. [Enforce TLS 1.3 encryption](https://learn.microsoft.com/en-us/sql/database-engine/log-shipping/about-log-shipping-sql-server?view=sql-server-ver17#enforce-tls-13-encryption)
  3. [Benefits](https://learn.microsoft.com/en-us/sql/database-engine/log-shipping/about-log-shipping-sql-server?view=sql-server-ver17#benefits)
  4. [Terms and definitions](https://learn.microsoft.com/en-us/sql/database-engine/log-shipping/about-log-shipping-sql-server?view=sql-server-ver17#terms-and-definitions)
  5. [Interoperability](https://learn.microsoft.com/en-us/sql/database-engine/log-shipping/about-log-shipping-sql-server?view=sql-server-ver17#interoperability)
  6. [Related tasks](https://learn.microsoft.com/en-us/sql/database-engine/log-shipping/about-log-shipping-sql-server?view=sql-server-ver17#related-tasks)
  7. [Related content](https://learn.microsoft.com/en-us/sql/database-engine/log-shipping/about-log-shipping-sql-server?view=sql-server-ver17#related-content)

Show 3 more
**Applies to:** ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to)
SQL Server Log shipping allows you to automatically send transaction log backups from a _primary database_ on a _primary server_ instance to one or more _secondary databases_ on separate _secondary server_ instances. The transaction log backups are applied to each of the secondary databases individually. An optional third server instance, known as the _monitor server_ , records the history and status of backup and restore operations and, optionally, raises alerts if these operations fail to occur as scheduled.
[](https://learn.microsoft.com/en-us/sql/database-engine/log-shipping/about-log-shipping-sql-server?view=sql-server-ver17#log-shipping-overview)
## Log shipping overview
Log shipping consists of three operations:
  1. Back up the transaction log at the primary server instance.
  2. Copy the transaction log file to the secondary server instance.
  3. Restore the log backup on the secondary server instance.


The log can be shipped to multiple secondary server instances. In such cases, operations 2 and 3 are duplicated for each secondary server instance.
A log shipping configuration doesn't automatically fail over from the primary server to the secondary server. If the primary database becomes unavailable, any of the secondary databases can be brought online manually.
You can use a secondary database for reporting purposes.
In addition, you can configure alerts for your log shipping configuration.
[](https://learn.microsoft.com/en-us/sql/database-engine/log-shipping/about-log-shipping-sql-server?view=sql-server-ver17#a-typical-log-shipping-configuration)
### A typical log shipping configuration
The following figure shows a log shipping configuration with the primary server instance, three secondary server instances, and a monitor server instance. The figure illustrates the steps performed by backup, copy, and restore jobs, as follows:
  1. The primary server instance runs the backup job to back up the transaction log on the primary database. This server instance then places the log backup into a primary log-backup file, which it sends to the backup folder. In this figure, the backup folder is on a shared directory-the _backup share_.
  2. Each of the three secondary server instances runs its own copy job to copy the primary log-backup file to its own local destination folder.
  3. Each secondary server instance runs its own restore job to restore the log backup from the local destination folder onto the local secondary database.


The primary and secondary server instances send their own history and status to the monitor server instance.
![Diagram of configuration showing backup, copy, and restore jobs.](https://learn.microsoft.com/en-us/sql/database-engine/log-shipping/media/about-log-shipping-sql-server/log-shipping-typical-configuration.png?view=sql-server-ver17)
[](https://learn.microsoft.com/en-us/sql/database-engine/log-shipping/about-log-shipping-sql-server?view=sql-server-ver17#enforce-tls-13-encryption)
## Enforce TLS 1.3 encryption
SQL Server 2025 (17.x) introduces [TDS 8.0](https://learn.microsoft.com/en-us/sql/relational-databases/security/networking/tds-8?view=sql-server-ver17) support for log shipping. The TDS 8.0 protocol provides enhanced security and encryption for data transmitted between the primary and secondary servers of a log shipping topology. Choose between enforcing mandatory or strict encryption for communication between servers.
In SQL Server 2025 (17.x), log shipping uses [Microsoft OLE DB Driver for SQL Server](https://learn.microsoft.com/en-us/sql/connect/oledb/oledb-driver-for-sql-server?view=sql-server-ver17) as the default version for linked servers, which has a default `Encrypt` value of `Mandatory`.
To use TLS 1.3 encryption in your existing log shipping configuration, drop and then recreate the topology using the new TLS 1.3 parameters in the [log shipping stored procedures](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/log-shipping-stored-procedures-transact-sql?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/database-engine/log-shipping/about-log-shipping-sql-server?view=sql-server-ver17#log-shipping-monitoring-can-break-if-the-monitor-is-a-remote-sql-server-2025-instance)
### Log shipping monitoring can break if the monitor is a remote SQL Server 2025 instance
Log shipping monitoring can break if the monitor is a remote SQL Server 2025 (17.x) instance, when other SQL Server instances in the log shipping topology use a previous version. You might get one of the following errors:
Output
Copy
```
OLE DB provider "MSOLEDBSQL19" for linked server "<server>" returned message "Client unable to establish connection. For solutions related to encryption errors, see https://go.microsoft.com/fwlink/?linkid=2227882.".

```

Or:
Output
Copy
```
Msg 32055, Level 16, State 2, Procedure master.dbo.sp_add_log_shipping_primary_database, Line 325 [Batch Start Line 10]
There was an error configuring the remote monitor server.

```

To work around this issue, drop and recreate the log shipping configuration on both the primary and secondary replicas. An example script is available at [Use a remote monitor with connectivity options](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-add-log-shipping-primary-database-transact-sql?view=sql-server-ver17#c-use-a-remote-monitor-with-connectivity-options).
For more information, see [Encryption and certificate validation behavior](https://learn.microsoft.com/en-us/sql/connect/oledb/features/encryption-and-certificate-validation?view=sql-server-ver17#encryption-and-certificate-validation-behavior).
[](https://learn.microsoft.com/en-us/sql/database-engine/log-shipping/about-log-shipping-sql-server?view=sql-server-ver17#benefits)
## Benefits
  * Provides a disaster-recovery solution for a single primary database and one or more secondary databases, each on a separate instance of SQL Server.
  * Supports limited read-only access to secondary databases (during the interval between restore jobs).
  * Allows a user-specified delay between when the primary server backs up the log of the primary database and when the secondary servers must restore (apply) the log backup. A longer delay can be useful, for example, if data is accidentally changed on the primary database. If the accidental change is noticed quickly, a delay can let you retrieve still unchanged data from a secondary database before the change is reflected there.


[](https://learn.microsoft.com/en-us/sql/database-engine/log-shipping/about-log-shipping-sql-server?view=sql-server-ver17#terms-and-definitions)
## Terms and definitions
  * **primary server** : The instance of SQL Server that is your production server.
  * **primary database** : The database on the primary server that you want to back up to another server. All administration of the log shipping configuration through SQL Server Management Studio is performed from the primary database.
  * **secondary server** : The instance of SQL Server where you want to keep a warm standby copy of your primary database.
  * **secondary database** : The warm standby copy of the primary database. The secondary database might be in either the RECOVERING state or the `STANDBY` state, which leaves the database available for limited read-only access.
  * **monitor server** : An optional instance of SQL Server that tracks all of the details of log shipping, including:
    * When the transaction log on the primary database was last backed up.
    * When the secondary servers last copied and restored the backup files.
    * Information about any backup failure alerts.
Once the monitor server has been configured, it can't be changed without removing log shipping first.
  * **backup job** : A SQL Server Agent job that performs the backup operation, logs history to the local server and the monitor server, and deletes old backup files and history information. When log shipping is enabled, the job category "Log Shipping Backup" is created on the primary server instance.
  * **copy job** : A SQL Server Agent job that copies the backup files from the primary server to a configurable destination on the secondary server and logs history on the secondary server and the monitor server. When log shipping is enabled on a database, the job category "Log Shipping Copy" is created on each secondary server in a log shipping configuration.
  * **restore job** : A SQL Server Agent job that restores the copied backup files to the secondary databases. It logs history on the local server and the monitor server, and deletes old files and old history information. When log shipping is enabled on a database, the job category "Log Shipping Restore" is created on the secondary server instance.
  * **alert job** : A SQL Server Agent job that raises alerts for primary and secondary databases when a backup or restore operation doesn't complete successfully within a specified threshold. When log shipping is enabled on a database, job category "Log Shipping Alert" is created on the monitor server instance.
For each alert, you need to specify an alert number. Also, be sure to configure the alert to notify an operator when an alert is raised.


[](https://learn.microsoft.com/en-us/sql/database-engine/log-shipping/about-log-shipping-sql-server?view=sql-server-ver17#interoperability)
## Interoperability
Log shipping can be used with the following features or components of SQL Server:
  * [Prerequisites to convert log shipping to Always On availability groups](https://learn.microsoft.com/en-us/sql/database-engine/availability-groups/windows/prereqs-migrating-log-shipping-to-always-on-availability-groups?view=sql-server-ver17)
  * [Database Mirroring and Log Shipping (SQL Server)](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-and-log-shipping-sql-server?view=sql-server-ver17)
  * [Log Shipping and Replication (SQL Server)](https://learn.microsoft.com/en-us/sql/database-engine/log-shipping/log-shipping-and-replication-sql-server?view=sql-server-ver17)


Always On availability groups and database mirroring are mutually exclusive. A database that is configured for one of these features can't be configured for the other.
**Known issue** : For databases with memory-optimized tables, performing a transactional log backup with no recovery, and later executing a transaction log restore with recovery, could result in an unresponsive database restore process. This issue can also affect log shipping functionality. To work around this problem, the SQL Server instance can be restarted before initiating the restore process.
[](https://learn.microsoft.com/en-us/sql/database-engine/log-shipping/about-log-shipping-sql-server?view=sql-server-ver17#related-tasks)
## Related tasks
  * [Upgrade SQL Server with log shipping (Transact-SQL)](https://learn.microsoft.com/en-us/sql/database-engine/log-shipping/upgrade-sql-server-log-shipping-transact-sql?view=sql-server-ver17)
  * [Configure Log Shipping (SQL Server)](https://learn.microsoft.com/en-us/sql/database-engine/log-shipping/configure-log-shipping-sql-server?view=sql-server-ver17)
  * [Add a Secondary Database to a Log Shipping Configuration (SQL Server)](https://learn.microsoft.com/en-us/sql/database-engine/log-shipping/add-a-secondary-database-to-a-log-shipping-configuration-sql-server?view=sql-server-ver17)
  * [Remove a Secondary Database from a Log Shipping Configuration (SQL Server)](https://learn.microsoft.com/en-us/sql/database-engine/log-shipping/remove-a-secondary-database-from-a-log-shipping-configuration-sql-server?view=sql-server-ver17)
  * [Remove Log Shipping (SQL Server)](https://learn.microsoft.com/en-us/sql/database-engine/log-shipping/remove-log-shipping-sql-server?view=sql-server-ver17)
  * [View the Log Shipping Report (SQL Server Management Studio)](https://learn.microsoft.com/en-us/sql/database-engine/log-shipping/view-the-log-shipping-report-sql-server-management-studio?view=sql-server-ver17)
  * [Monitor Log Shipping (Transact-SQL)](https://learn.microsoft.com/en-us/sql/database-engine/log-shipping/monitor-log-shipping-transact-sql?view=sql-server-ver17)
  * [Fail Over to a Log Shipping Secondary (SQL Server)](https://learn.microsoft.com/en-us/sql/database-engine/log-shipping/fail-over-to-a-log-shipping-secondary-sql-server?view=sql-server-ver17)
  * [Management of Logins and Jobs After Role Switching (SQL Server)](https://learn.microsoft.com/en-us/sql/sql-server/failover-clusters/management-of-logins-and-jobs-after-role-switching-sql-server?view=sql-server-ver17)


[](https://learn.microsoft.com/en-us/sql/database-engine/log-shipping/about-log-shipping-sql-server?view=sql-server-ver17#related-content)
## Related content
  * [What is an Always On availability group?](https://learn.microsoft.com/en-us/sql/database-engine/availability-groups/windows/overview-of-always-on-availability-groups-sql-server?view=sql-server-ver17)


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
  * [ Configure Log Shipping (SQL Server) - SQL Server ](https://learn.microsoft.com/en-us/sql/database-engine/log-shipping/configure-log-shipping-sql-server?source=recommendations)
Learn how to configure log shipping by using SQL Server Management Studio or Transact-SQL in SQL Server.
  * [ Log Shipping and Replication (SQL Server) - SQL Server ](https://learn.microsoft.com/en-us/sql/database-engine/log-shipping/log-shipping-and-replication-sql-server?source=recommendations)
Learn how log shipping applies the transaction log from every insertion, update, or deletion made on the primary database to the secondary database.
  * [ Database Mirroring and Log Shipping (SQL Server) - SQL Server Database Mirroring ](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-and-log-shipping-sql-server?source=recommendations)
Learn about the considerations for combining log shipping and database mirroring in SQL Server, including how many destination servers you need.
  * [ Prerequisites to convert log shipping to availability groups - SQL Server Always On ](https://learn.microsoft.com/en-us/sql/database-engine/availability-groups/windows/prereqs-migrating-log-shipping-to-always-on-availability-groups?source=recommendations)
A description of the prerequisites necessary to convert log shipping to an Always On availability group.
  * [ Upgrade SQL Server Log Shipping - SQL Server ](https://learn.microsoft.com/en-us/sql/database-engine/log-shipping/upgrade-sql-server-log-shipping-transact-sql?source=recommendations)
Learn the appropriate order to preserve your log shipping disaster recovery solution when upgrading SQL Server from a previous version.
  * [ Fail over to a log shipping secondary - SQL Server ](https://learn.microsoft.com/en-us/sql/database-engine/log-shipping/fail-over-to-a-log-shipping-secondary-sql-server?source=recommendations)
Learn how to fail over to a SQL Server log shipping secondary by using SQL Server Management Studio or Transact-SQL.
  * [ Add Log Shipping Secondary - SQL Server ](https://learn.microsoft.com/en-us/sql/database-engine/log-shipping/add-a-secondary-database-to-a-log-shipping-configuration-sql-server?source=recommendations)
Describes how to add a secondary database to an existing log shipping configuration by using SQL Server Management Studio or Transact-SQL in SQL Server.
  * [ Log Shipping Transaction Log Backup Settings - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/databases/log-shipping-transaction-log-backup-settings?source=recommendations)
Log Shipping Transaction Log Backup Settings


Show 5 more
Module
[ Monitor workload protection in Azure Backup - Training ](https://learn.microsoft.com/en-us/training/modules/monitor-protection-of-workloads-in-azure-backup/?source=recommendations)
Learn how to monitor Azure Backup-protected workloads by using Azure Monitor.
Certification
[ Microsoft Certified: Azure Database Administrator Associate - Certifications ](https://learn.microsoft.com/en-us/credentials/certifications/azure-database-administrator-associate/?source=recommendations)
Administer an SQL Server database infrastructure for cloud, on-premises and hybrid relational databases using the Microsoft PaaS relational database offerings.
Mar 8, 4 PM - Mar 8, 4 PM
Experiment with what's next in AI-driven apps and agent design
* * *
  * Last updated on 02/23/2026


##  In this article
  1. [Log shipping overview](https://learn.microsoft.com/en-us/sql/database-engine/log-shipping/about-log-shipping-sql-server?view=sql-server-ver17#log-shipping-overview)
  2. [Enforce TLS 1.3 encryption](https://learn.microsoft.com/en-us/sql/database-engine/log-shipping/about-log-shipping-sql-server?view=sql-server-ver17#enforce-tls-13-encryption)
  3. [Benefits](https://learn.microsoft.com/en-us/sql/database-engine/log-shipping/about-log-shipping-sql-server?view=sql-server-ver17#benefits)
  4. [Terms and definitions](https://learn.microsoft.com/en-us/sql/database-engine/log-shipping/about-log-shipping-sql-server?view=sql-server-ver17#terms-and-definitions)
  5. [Interoperability](https://learn.microsoft.com/en-us/sql/database-engine/log-shipping/about-log-shipping-sql-server?view=sql-server-ver17#interoperability)
  6. [Related tasks](https://learn.microsoft.com/en-us/sql/database-engine/log-shipping/about-log-shipping-sql-server?view=sql-server-ver17#related-tasks)
  7. [Related content](https://learn.microsoft.com/en-us/sql/database-engine/log-shipping/about-log-shipping-sql-server?view=sql-server-ver17#related-content)


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
[ Sign in ](https://learn.microsoft.com/en-us/sql/database-engine/log-shipping/about-log-shipping-sql-server?view=sql-server-ver17)
[English (United States)](https://learn.microsoft.com/en-us/locale?target=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fsql%2Fdatabase-engine%2Flog-shipping%2Fabout-log-shipping-sql-server%3Fview%3Dsql-server-ver17)
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
