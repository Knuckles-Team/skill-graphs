# Back up and restore of SQL Server databases
Feedback
Summarize this article for me
##  In this article
  1. [Why back up?](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver17#why-back-up)
  2. [Glossary of backup terms](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver17#glossary-of-backup-terms)
  3. [Backup and restore strategies](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver17#backup-and-restore-strategies)
  4. [Best practice recommendations](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver17#best-practice-recommendations)
  5. [Security risk of restoring backups from untrusted sources](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver17#security-risk-of-restoring-backups-from-untrusted-sources)
  6. [Monitor progress with XEvent](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver17#monitor-progress-with-xevent)
  7. [More about backup tasks](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver17#more-about-backup-tasks)
  8. [Work with backup devices and backup media](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver17#work-with-backup-devices-and-backup-media)
  9. [Create backups](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver17#create-backups)
  10. [Restore data backups](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver17#restore-data-backups)
  11. [Restore transaction logs (full recovery model)](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver17#restore-transaction-logs-full-recovery-model)
  12. [Related content](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver17#related-content)

Show 8 more
**Applies to:** ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to)
This article describes the benefits of backing up SQL Server databases, describes basic backup and restore terms, and introduces backup and restore strategies for SQL Server and security considerations for SQL Server backup and restore.
> This article introduces SQL Server backups. For specific steps to back up SQL Server databases, see [Creating backups](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver17#creating-backups).
The SQL Server backup and restore component provides an essential safeguard for protecting critical data stored in your SQL Server databases. To minimize the risk of catastrophic data loss, you need to back up your databases to preserve modifications to your data on a regular basis. A well-planned backup and restore strategy helps protect databases against data loss caused by a variety of failures. Test your strategy by restoring a set of backups and then recovering your database to prepare you to respond effectively to a disaster.
In addition to local storage for storing the backups, SQL Server also supports backup to and restore from Azure Blob Storage. For more information, see [SQL Server backup and restore with Microsoft Azure Blob Storage](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/sql-server-backup-and-restore-with-microsoft-azure-blob-storage-service?view=sql-server-ver17). For database files stored using Azure Blob Storage, SQL Server 2016 (13.x) provides the option to use Azure snapshots for nearly instantaneous backups and faster restores. For more information, see [File-snapshot backups for database files in Azure](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/file-snapshot-backups-for-database-files-in-azure?view=sql-server-ver17). Azure also offers an enterprise-class backup solution for SQL Server running in Azure VMs. A fully managed backup solution, it supports Always On availability groups, long-term retention, point-in-time recovery, and central management and monitoring. For more information, see [About SQL Server backup on Azure VMs](https://learn.microsoft.com/en-us/azure/backup/backup-azure-sql-database).
[](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver17#why-back-up)
## Why back up?
  * Backing up your SQL Server databases, running test restores procedures on your backups, and storing copies of backups in a safe, off-site location protects you from potentially catastrophic data loss. **Backing up is the only way to protect your data.**
With valid backups of a database, you can recover your data from many failures, such as:
    * Media failure.
    * User errors, for example, dropping a table by mistake.
    * Hardware failures, for example, a damaged disk drive or permanent loss of a server.
    * Natural disasters. By using SQL Server Backup to Azure Blob Storage, you can create an off-site backup in a different region than your on-premises location, to use in the event of a natural disaster affecting your on-premises location.
  * Additionally, backups of a database are useful for routine administrative purposes, such as copying a database from one server to another, setting up Always On availability groups or database mirroring, and archiving.


[](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver17#glossary-of-backup-terms)
## Glossary of backup terms
**back up** [verb]
The process of creating a **backup [noun]** by copying data records from a SQL Server database or log records from its transaction log.
**backup** [noun]
A copy of data that you can use to restore and recover the data after a failure. Backups of a database can also be used to restore a copy the database to a new location.
**backup** device
A disk or tape device to which SQL Server backups are written and from which they can be restored. SQL Server backups can also be written to an Azure Blob Storage, and **URL** format is used to specify the destination and the name of the backup file. For more information, see [SQL Server backup and restore with Microsoft Azure Blob Storage](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/sql-server-backup-and-restore-with-microsoft-azure-blob-storage-service?view=sql-server-ver17).
**backup media**
One or more tapes or disk files to which one or more backups have been written.
**data backup**
A backup of data in a complete database (a database backup), a partial database (a partial backup), or a set of data files or filegroups (a file backup).
**database backup**
A backup of a database. Full database backups represent the whole database at the time the backup finished. Differential database backups contain only changes made to the database since its most recent full database backup.
**differential backup**
A data backup that is based on the latest full backup of a complete or partial database or a set of data files or filegroups (the differential base) and that contains only the data that has changed since that base.
**full backup**
A data backup that contains all the data in a specific database or set of filegroups or files, and also enough log to allow for recovering that data.
**log backup**
A backup of transaction logs that includes all log records that weren't backed up in a previous log backup (full recovery model).
**recover**
To return a database to a stable and consistent state.
**recovery**
A phase of database startup or of a restore with recovery that brings the database into a transaction-consistent state.
**recovery model**
A database property that controls transaction log maintenance on a database. There are three recovery models: simple, full, and bulk-logged. A database's recovery model determines its backup and restore requirements.
**restore**
A multiphase process that copies all the data and log pages from a specified SQL Server backup to a specified database, and then rolls forward all the transactions that are logged in the backup by applying logged changes to bring the data forward in time.
[](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver17#backup-and-restore-strategies)
## Backup and restore strategies
Backing up and restoring data must be customized to a particular environment and must work with the available resources. Therefore, a reliable use of backup and restore for recovery requires a backup and restore strategy. A well-designed backup and restore strategy balances the business requirements for maximum data availability and minimum data loss while considering the cost of maintaining and storing backups.
A backup and restore strategy contains a backup portion and a restore portion. The backup part of the strategy defines the type and frequency of backups, the nature and speed of the hardware they require, how backups are to be tested, and where and how backup media is to be stored (including security considerations). The restore part of the strategy defines who's responsible for performing restores, how restores should be performed to meet your goals for database availability and minimizing data loss, and how restores are tested.
Designing an effective backup and restore strategy requires careful planning, implementation, and testing. Testing is required: you don't have a backup strategy until you've successfully restored backups in all the combinations that are included in your restore strategy and have tested the restored database for physical consistency. You must consider a variety of factors. These include:
  * Your organization's goals regarding your production databases, especially the requirements for availability and protecting data from loss or damage.
  * The nature of each database: its size, its usage patterns, the nature of its content, the requirements for its data, and so on.
  * Constraints on resources, such as hardware, personnel, space for storing backup media, the physical security of the stored media, and so on.


[](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver17#best-practice-recommendations)
## Best practice recommendations
The accounts that perform backup or restore operations shouldn't be granted more privileges than necessary. Review [backup](https://learn.microsoft.com/en-us/sql/t-sql/statements/backup-transact-sql?view=sql-server-ver17#permissions) and [restore](https://learn.microsoft.com/en-us/sql/t-sql/statements/restore-statements-transact-sql?view=sql-server-ver17#permissions) for specific permission details. It's recommended that backups are [encrypted](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver17) and, if possible, [compressed](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/backup-compression-sql-server?view=sql-server-ver17).
To ensure security, backup files should have extensions that follow proper conventions:
  * Database backup files should have the `.BAK` extension
  * Log backup files should have the `.TRN` extension.


[](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver17#use-separate-storage)
### Use Separate Storage
Ensure that you place your database backups on a separate physical location or device from the database files. When your physical drive that stores your databases malfunctions or crashes, recoverability depends on the ability to access the separate drive or remote device that stored the backups in order to perform a restore. Keep in mind that you could create several logical volumes or partitions from a same physical disk drive. Carefully study the disk partition and logical volume layouts before choosing a storage location for the backups.
[](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver17#choose-appropriate-recovery-model)
### Choose appropriate recovery model
Backup and restore operations occur within the context of a [recovery model](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/recovery-models-sql-server?view=sql-server-ver17). A recovery model is a database property that controls how the transaction log is managed. Thus, a database's recovery model determines what types of backups and restore scenarios are supported for the database, and what size the transaction log backups would be. Typically, a database uses either the simple recovery model or the full recovery model. You can augment the full recovery model by switching to the bulk-logged recovery model before bulk operations. For an introduction to these recovery models and how they affect transaction log management, see [the transaction log](https://learn.microsoft.com/en-us/sql/relational-databases/logs/the-transaction-log-sql-server?view=sql-server-ver17).
The best choice of recovery model for the database depends on your business requirements. To avoid transaction log management and simplify backup and restore, use the simple recovery model. To minimize work-loss exposure at the cost of administrative overhead, use the full recovery model. To minimize impact on log size during bulk-logged operations while at the same time allowing for recoverability of those operations, use bulk-logged recovery model. For information about the effect of recovery models on backup and restore, see [Backup overview](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/backup-overview-sql-server?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver17#design-your-backup-strategy)
### Design your backup strategy
After you've selected a recovery model that meets your business requirements for a specific database, you have to plan and implement a corresponding backup strategy. The optimal backup strategy depends on a variety of factors, of which the following are especially significant:
  * How many hours a day do applications have to access the database?
If there's a predictable off-peak period, we recommend that you schedule full database backups for that period.
  * How frequently are changes and updates likely to occur?
If changes are frequent, consider the following:
    * Under the simple recovery model, consider scheduling differential backups between full database backups. A differential backup captures only the changes since the last full database backup.
    * Under the full recovery model, you should schedule frequent log backups. Scheduling differential backups between full backups can reduce restore time by reducing the number of log backups you have to restore after restoring the data.
  * Are changes likely to occur in only a small part of the database or in a large part of the database?
For a large database in which changes are concentrated in a part of the files or filegroups, partial backups and or full file backups can be useful. For more information, see [Partial backups (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/partial-backups-sql-server?view=sql-server-ver17) and [Full file backups (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/full-file-backups-sql-server?view=sql-server-ver17).
  * How much disk space will a full database backup require?
  * How far in the past does your business require to maintain backups?
Make sure you have a proper backup schedule established according to the needs of the application and business requirements. As the backups get old, the risk of data loss is higher unless you have a way to regenerate all the data till the point of failure. Before you choose to dispose of old backups due to storage resource limitations, consider if recoverability is required that far in the past.


[](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver17#estimate-the-size-of-a-full-database-backup)
### Estimate the size of a full database backup
Before you implement a backup and restore strategy, you should estimate how much disk space a full database backup will use. The backup operation copies the data in the database to the backup file. The backup contains only the actual data in the database and not any unused space. Therefore, the backup is usually smaller than the database itself. You can estimate the size of a full database backup by using the `sp_spaceused` system stored procedure. For more information, see [sp_spaceused (Transact-SQL)](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-spaceused-transact-sql?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver17#schedule-backups)
### Schedule backups
Performing a backup operation has minimal effect on transactions that are running; therefore, you can run backup operations during regular operations. You can perform a SQL Server backup with minimal effect on production workloads.
> For information about concurrency restrictions during backup, see [Backup overview (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/backup-overview-sql-server?view=sql-server-ver17).
After you decide what types of backups you require and how frequently you have to perform each type, we recommend that you schedule regular backups as part of a database maintenance plan for the database. For information about maintenance plans and how to create them for database backups and log backups, see [Use the Maintenance Plan Wizard](https://learn.microsoft.com/en-us/sql/relational-databases/maintenance-plans/use-the-maintenance-plan-wizard?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver17#test-your-backups)
### Test your backups
You don't have a restore strategy until you test your backups. It's very important to thoroughly test your backup strategy for each of your databases by restoring a copy of the database onto a test system. You must test restoring every type of backup that you intend to use. We also recommend that once you restore the backup, you perform database consistency checks via DBCC CHECKDB of the database to validate the backup media wasn't damaged.
[](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver17#verify-media-stability-and-consistency)
### Verify media stability and consistency
Use the verification options provided by the backup utilities (`BACKUP` T-SQL command, SQL Server Maintenance Plans, your backup software or solution, etc.). For an example, see [RESTORE statements - VERIFYONLY](https://learn.microsoft.com/en-us/sql/t-sql/statements/restore-statements-verifyonly-transact-sql?view=sql-server-ver17).
Use advanced features like `BACKUP CHECKSUM` to detect problems with the backup media itself. For more information, see [Possible media errors during backup and restore (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/possible-media-errors-during-backup-and-restore-sql-server?view=sql-server-ver17)
[](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver17#document-backuprestore-strategy)
### Document backup/restore strategy
We recommend that you document your backup and restore procedures and keep a copy of the documentation in your run book. We also recommend that you maintain an operations manual for each database. This operations manual should document the location of the backups, backup device names (if any), and the amount of time that is required to restore the test backups.
[](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver17#security-risk-of-restoring-backups-from-untrusted-sources)
## Security risk of restoring backups from untrusted sources
This section outlines the security risk associated with restoring backups from untrusted sources to any SQL Server environment, including on-premises, Azure SQL Managed Instance, SQL Server on Azure Virtual Machines (VMs) and any other environment.
[](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver17#why-this-matters)
### Why this matters
Restoring SQL backup files (`.bak`) introduces a potential risk if the backup originates from an untrusted source. The security risk is exacerbated further when a SQL Server environment has multiple instances, as it amplifies the area of threat. While backups that remain within a trusted boundary pose no security issue, restoring a malicious backup can compromise the security of the entire environment.
A malicious `.bak` file can:
  * Take over the entire SQL Server instance.
  * Escalate privileges and gain unauthorized access to the underlying host or virtual machine.


This attack occurs before any validating scripts or security checks can execute, which makes it extremely dangerous. Restoring an untrusted backup is equivalent to running untrusted applications on a critical server or virtual machine, and introducing arbitrary code execution into your environment.
[](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver17#best-practices)
### Best practices
Follow these backup security best practices to reduce the threat to your SQL Server environments:
  * Treat restoring backups as a high-risk operation.
  * Reduce the threat service area by using isolated instances.
  * Only allow trusted backups: never restore backups from unknown or external sources.
  * Only allow backups that have remained within a trusted boundary: ensure backups originate from within the trusted boundary.
  * Do not bypass security controls for convenience.
  * Enable [server-level auditing](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-server-audit-specification-transact-sql) to capture backup and restore events and mitigate audit evasion.


[](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver17#monitor-progress-with-xevent)
## Monitor progress with XEvent
Backup and restore operations can take a considerable amount of time due to the size of a database and the complexity of the operations involved. When issues arise with either operation, you can use the `backup_restore_progress_trace` extended event to monitor progress live. For more information about extended events, see [Extended Events overview](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/extended-events?view=sql-server-ver17).
Using the `backup_restore_progress_trace` extended event can cause a performance issue and consume a significant amount of disk space. Use for short periods of time, exercise caution, and test thoroughly before implementing in production.
SQL
Copy
```
-- Create the backup_restore_progress_trace extended event session
CREATE EVENT SESSION [BackupRestoreTrace] ON SERVER
ADD EVENT sqlserver.backup_restore_progress_trace
ADD TARGET package0.event_file(SET filename=N'BackupRestoreTrace')
WITH (MAX_MEMORY=4096 KB,EVENT_RETENTION_MODE=ALLOW_SINGLE_EVENT_LOSS,MAX_DISPATCH_LATENCY=5 SECONDS,MAX_EVENT_SIZE=0 KB,MEMORY_PARTITION_MODE=NONE,TRACK_CAUSALITY=OFF,STARTUP_STATE=OFF)
GO

-- Start the event session
ALTER EVENT SESSION [BackupRestoreTrace]
ON SERVER
STATE = start;
GO

-- Stop the event session
ALTER EVENT SESSION [BackupRestoreTrace]
ON SERVER
STATE = stop;
GO

```

[](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver17#sample-output-from-extended-event)
### Sample output from extended event
![Screenshot of an example of back up xevent output.](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/media/back-up-and-restore-of-sql-server-databases/backup-xevent-example.png?view=sql-server-ver17) ![Screenshot of an example of back up xevent output, continued.](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/media/back-up-and-restore-of-sql-server-databases/restore-xevent-example.png?view=sql-server-ver17)
[](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver17#more-about-backup-tasks)
## More about backup tasks
  * [Create a maintenance plan](https://learn.microsoft.com/en-us/sql/relational-databases/maintenance-plans/create-a-maintenance-plan?view=sql-server-ver17)
  * [Create a SQL Server Agent job in SQL Server Management Studio](https://learn.microsoft.com/en-us/ssms/agent/create-a-job)
  * [Configure schedule for SQL Server Agent job](https://learn.microsoft.com/en-us/ssms/agent/schedule-a-job)


[](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver17#work-with-backup-devices-and-backup-media)
## Work with backup devices and backup media
  * [Define a logical backup device for a disk file (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/define-a-logical-backup-device-for-a-disk-file-sql-server?view=sql-server-ver17)
  * [Define a logical backup device for a tape drive (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/define-a-logical-backup-device-for-a-tape-drive-sql-server?view=sql-server-ver17)
  * [Specify a disk or tape backup destination (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/specify-a-disk-or-tape-as-a-backup-destination-sql-server?view=sql-server-ver17)
  * [Delete a backup device (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/delete-a-backup-device-sql-server?view=sql-server-ver17)
  * [Set the expiration date on a backup (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/set-the-expiration-date-on-a-backup-sql-server?view=sql-server-ver17)
  * [View the contents of a backup tape or file (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/view-the-contents-of-a-backup-tape-or-file-sql-server?view=sql-server-ver17)
  * [View the data and log files in a backup set (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/view-the-data-and-log-files-in-a-backup-set-sql-server?view=sql-server-ver17)
  * [View the properties and contents of a logical backup device (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/view-the-properties-and-contents-of-a-logical-backup-device-sql-server?view=sql-server-ver17)
  * [Restore a backup from a device (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/restore-a-backup-from-a-device-sql-server?view=sql-server-ver17)


[](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver17#create-backups)
## Create backups
For partial or copy-only backups, you must use the Transact-SQL [BACKUP](https://learn.microsoft.com/en-us/sql/t-sql/statements/backup-transact-sql?view=sql-server-ver17) statement with the `PARTIAL` or `COPY_ONLY` option, respectively.
[](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver17#use-ssms)
### Use SSMS
  * [Create a Full Database Backup (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/create-a-full-database-backup-sql-server?view=sql-server-ver17)
  * [Back up a transaction log](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-a-transaction-log-sql-server?view=sql-server-ver17)
  * [Back Up Files and Filegroups](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-files-and-filegroups-sql-server?view=sql-server-ver17)
  * [Create a Differential Database Backup (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/create-a-differential-database-backup-sql-server?view=sql-server-ver17)


[](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver17#use-t-sql)
### Use T-SQL
  * [Use Resource Governor to Limit CPU Usage by Backup Compression (Transact-SQL)](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/use-resource-governor-to-limit-cpu-usage-by-backup-compression-transact-sql?view=sql-server-ver17)
  * [Back Up the Transaction Log When the Database Is Damaged (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-the-transaction-log-when-the-database-is-damaged-sql-server?view=sql-server-ver17)
  * [Enable or disable backup checksums during backup or restore (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/enable-or-disable-backup-checksums-during-backup-or-restore-sql-server?view=sql-server-ver17)
  * [Specify backup or restore to continue or stop after error](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/specify-if-backup-or-restore-continues-or-stops-after-error?view=sql-server-ver17)


[](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver17#restore-data-backups)
## Restore data backups
[](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver17#use-ssms-1)
### Use SSMS
  * [Restore a Database Backup Using SSMS](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/restore-a-database-backup-using-ssms?view=sql-server-ver17)
  * [Restore a database to a new location (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/restore-a-database-to-a-new-location-sql-server?view=sql-server-ver17)
  * [Restore a differential database backup (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/restore-a-differential-database-backup-sql-server?view=sql-server-ver17)
  * [Restore Files and Filegroups (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/restore-files-and-filegroups-sql-server?view=sql-server-ver17)


[](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver17#use-t-sql-1)
### Use T-SQL
  * [Restore a database backup under the simple recovery model (Transact-SQL)](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/restore-a-database-backup-under-the-simple-recovery-model-transact-sql?view=sql-server-ver17)
  * [Restore Database to Point of Failure - Full Recovery](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/restore-database-to-point-of-failure-full-recovery?view=sql-server-ver17)
  * [Restore Files and Filegroups over Existing Files (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/restore-files-and-filegroups-over-existing-files-sql-server?view=sql-server-ver17)
  * [Restore Files to a New Location (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/restore-files-to-a-new-location-sql-server?view=sql-server-ver17)
  * [Restore the master database (Transact-SQL)](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/restore-the-master-database-transact-sql?view=sql-server-ver17)


[](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver17#restore-transaction-logs-full-recovery-model)
## Restore transaction logs (full recovery model)
[](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver17#use-ssms-2)
### Use SSMS
  * [Restore a database to a marked transaction (SQL Server Management Studio)](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/restore-a-database-to-a-marked-transaction-sql-server-management-studio?view=sql-server-ver17)
  * [Restore a Transaction Log Backup (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/restore-a-transaction-log-backup-sql-server?view=sql-server-ver17)
  * [Restore a SQL Server Database to a Point in Time (Full Recovery Model)](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/restore-a-sql-server-database-to-a-point-in-time-full-recovery-model?view=sql-server-ver17)


[](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver17#using-t-sql)
### Using T-SQL
  * [Restore a SQL Server Database to a Point in Time (Full Recovery Model)](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/restore-a-sql-server-database-to-a-point-in-time-full-recovery-model?view=sql-server-ver17)
  * [Restart an interrupted restore operation (Transact-SQL)](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/restart-an-interrupted-restore-operation-transact-sql?view=sql-server-ver17)
  * [Recover a database without restoring data (Transact-SQL)](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/recover-a-database-without-restoring-data-transact-sql?view=sql-server-ver17)


[](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver17#related-content)
## Related content
  * [Backup overview (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/backup-overview-sql-server?view=sql-server-ver17)
  * [Restore and recovery overview (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/restore-and-recovery-overview-sql-server?view=sql-server-ver17)
  * [BACKUP (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/statements/backup-transact-sql?view=sql-server-ver17)
  * [RESTORE Statements (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/statements/restore-statements-transact-sql?view=sql-server-ver17)
  * [Backup and Restore of Analysis Services Databases](https://learn.microsoft.com/en-us/analysis-services/multidimensional-models/backup-and-restore-of-analysis-services-databases)
  * [Back Up and Restore Full-Text Catalogs and Indexes](https://learn.microsoft.com/en-us/sql/relational-databases/search/back-up-and-restore-full-text-catalogs-and-indexes?view=sql-server-ver17)
  * [Back Up and Restore Replicated Databases](https://learn.microsoft.com/en-us/sql/relational-databases/replication/administration/back-up-and-restore-replicated-databases?view=sql-server-ver17)
  * [The transaction log](https://learn.microsoft.com/en-us/sql/relational-databases/logs/the-transaction-log-sql-server?view=sql-server-ver17)
  * [Recovery models (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/recovery-models-sql-server?view=sql-server-ver17)
  * [Media sets, media families, and backup sets (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/media-sets-media-families-and-backup-sets-sql-server?view=sql-server-ver17)


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
  * [ Back Up Files and Filegroups - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-files-and-filegroups-sql-server?source=recommendations)
This article describes how to back up files and filegroups in SQL Server by using SQL Server Management Studio, Transact-SQL, or PowerShell.
  * [ Create a Full Database Backup - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/create-a-full-database-backup-sql-server?source=recommendations)
Learn how to create a full database backup in SQL Server by using SQL Server Management Studio, Transact-SQL, or PowerShell.
  * [ BACKUP (Transact-SQL) - SQL Server ](https://learn.microsoft.com/en-us/sql/t-sql/statements/backup-transact-sql?source=recommendations)
BACKUP (Transact-SQL) backs up a SQL database.
  * [ Backup overview (SQL Server) - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/backup-overview-sql-server?source=recommendations)
Learn about the SQL Server backup component, including backup types and restrictions, and also backup devices and backup media.
  * [ Restore and Recovery Overview (SQL Server) - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/restore-and-recovery-overview-sql-server?source=recommendations)
Learn about the operations involved in recovering a SQL Server database from a failure by restoring a set of SQL Server backups in sequence.
  * [ Backup Devices (SQL Server) - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/backup-devices-sql-server?source=recommendations)
This article describes backup devices for a SQL Server database, including terminology and working with backup devices.
  * [ Restore a SQL Server Database to a Point in Time (Full Recovery Model) - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/restore-a-sql-server-database-to-a-point-in-time-full-recovery-model?source=recommendations)
Restore a SQL Server Database to a Point in Time (Full Recovery Model)
  * [ Restore a Database to a New Location (SQL Server) - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/restore-a-database-to-a-new-location-sql-server?source=recommendations)
Restore a SQL Server database to a new location by using SQL Server Management Studio or Transact-SQL.


Show 5 more
Module
[ Back up and restore databases - Training ](https://learn.microsoft.com/en-us/training/modules/backup-restore-databases/?source=recommendations)
Back up and restore databases
Certification
[ Microsoft Certified: Azure Database Administrator Associate - Certifications ](https://learn.microsoft.com/en-us/credentials/certifications/azure-database-administrator-associate/?source=recommendations)
Administer an SQL Server database infrastructure for cloud, on-premises and hybrid relational databases using the Microsoft PaaS relational database offerings.
Mar 8, 4 PM - Mar 8, 4 PM
Experiment with what's next in AI-driven apps and agent design
* * *
  * Last updated on 12/05/2025


##  In this article
  1. [Why back up?](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver17#why-back-up)
  2. [Glossary of backup terms](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver17#glossary-of-backup-terms)
  3. [Backup and restore strategies](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver17#backup-and-restore-strategies)
  4. [Best practice recommendations](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver17#best-practice-recommendations)
  5. [Security risk of restoring backups from untrusted sources](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver17#security-risk-of-restoring-backups-from-untrusted-sources)
  6. [Monitor progress with XEvent](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver17#monitor-progress-with-xevent)
  7. [More about backup tasks](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver17#more-about-backup-tasks)
  8. [Work with backup devices and backup media](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver17#work-with-backup-devices-and-backup-media)
  9. [Create backups](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver17#create-backups)
  10. [Restore data backups](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver17#restore-data-backups)
  11. [Restore transaction logs (full recovery model)](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver17#restore-transaction-logs-full-recovery-model)
  12. [Related content](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver17#related-content)

Show 3 more
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
[ Sign in ](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver17)
[English (United States)](https://learn.microsoft.com/en-us/locale?target=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fsql%2Frelational-databases%2Fbackup-restore%2Fback-up-and-restore-of-sql-server-databases%3Fview%3Dsql-server-ver17)
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
