# The transaction log
Feedback
Summarize this article for me
##  In this article
  1. [Operations supported by the transaction log](https://learn.microsoft.com/en-us/sql/relational-databases/logs/the-transaction-log-sql-server?view=sql-server-ver17#operations-supported-by-the-transaction-log)
  2. [Transaction log characteristics](https://learn.microsoft.com/en-us/sql/relational-databases/logs/the-transaction-log-sql-server?view=sql-server-ver17#transaction-log-characteristics)
  3. [Transaction log truncation](https://learn.microsoft.com/en-us/sql/relational-databases/logs/the-transaction-log-sql-server?view=sql-server-ver17#transaction-log-truncation)
  4. [Factors that can delay log truncation](https://learn.microsoft.com/en-us/sql/relational-databases/logs/the-transaction-log-sql-server?view=sql-server-ver17#factors-that-can-delay-log-truncation)
  5. [Operations that can be minimally logged](https://learn.microsoft.com/en-us/sql/relational-databases/logs/the-transaction-log-sql-server?view=sql-server-ver17#operations-that-can-be-minimally-logged)
  6. [Related tasks](https://learn.microsoft.com/en-us/sql/relational-databases/logs/the-transaction-log-sql-server?view=sql-server-ver17#related-tasks)
  7. [Related content](https://learn.microsoft.com/en-us/sql/relational-databases/logs/the-transaction-log-sql-server?view=sql-server-ver17#related-content)

Show 3 more
**Applies to:** ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to)
Every SQL Server database has a transaction log that records all transactions and the database modifications made by each transaction.
The transaction log is a critical component of the database. If there's a system failure, you need this log to bring your database back to a consistent state.
Never delete or move this log unless you fully understand the ramifications of doing so.
For information about the physical and logical architecture of the transaction log, see the [SQL Server transaction log architecture and management guide](https://learn.microsoft.com/en-us/sql/relational-databases/sql-server-transaction-log-architecture-and-management-guide?view=sql-server-ver17).
Checkpoints create known good points from which to begin applying transaction logs during database recovery. For more information, see [Database checkpoints (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/logs/database-checkpoints-sql-server?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/relational-databases/logs/the-transaction-log-sql-server?view=sql-server-ver17#operations-supported-by-the-transaction-log)
## Operations supported by the transaction log
The transaction log supports the following operations:
  * Individual transaction recovery.
  * Recovery of all incomplete transactions when SQL Server is started.
  * Rolling a restored database, file, filegroup, or page forward to the point of failure.
  * Supporting transactional replication.
  * Supporting high availability and disaster recovery solutions: Always On availability groups, database mirroring, and log shipping.


[](https://learn.microsoft.com/en-us/sql/relational-databases/logs/the-transaction-log-sql-server?view=sql-server-ver17#individual-transaction-recovery)
### Individual transaction recovery
If an application issues a `ROLLBACK` statement, or if the Database Engine detects an error such as the loss of communication with a client, the log records are used to roll back the modifications made by an incomplete transaction.
[](https://learn.microsoft.com/en-us/sql/relational-databases/logs/the-transaction-log-sql-server?view=sql-server-ver17#recovery-of-all-incomplete-transactions-when--is-started)
### Recovery of all incomplete transactions when SQL Server is started
If a server fails, the databases might be left in a state where some modifications were never written from the buffer cache to the data files, and there might be some modifications from incomplete transactions in the data files. When an instance of SQL Server is started, it runs a recovery of each database. Every modification recorded in the log that might not have been written to the data files is rolled forward. Every incomplete transaction found in the transaction log is then rolled back to make sure the integrity of the database is preserved. For more information, see [Restore and recovery overview (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/restore-and-recovery-overview-sql-server?view=sql-server-ver17#TlogAndRecovery).
[](https://learn.microsoft.com/en-us/sql/relational-databases/logs/the-transaction-log-sql-server?view=sql-server-ver17#rolling-a-restored-database-file-filegroup-or-page-forward-to-the-point-of-failure)
### Rolling a restored database, file, filegroup, or page forward to the point of failure
After a hardware loss or disk failure affecting the database files, you can restore the database to the point of failure. You first restore the last full database backup and the last differential database backup, and then restore the subsequent sequence of the transaction log backups to the point of failure.
As you restore each log backup, the Database Engine reapplies all the modifications recorded in the log to roll forward all the transactions. When the last log backup is restored, the Database Engine then uses the log information to roll back all transactions that weren't complete at that point. For more information, see [Restore and recovery overview (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/restore-and-recovery-overview-sql-server?view=sql-server-ver17#TlogAndRecovery).
[](https://learn.microsoft.com/en-us/sql/relational-databases/logs/the-transaction-log-sql-server?view=sql-server-ver17#support-transactional-replication)
### Support transactional replication
The Log Reader Agent monitors the transaction log of each database configured for transactional replication and copies the transactions marked for replication from the transaction log into the distribution database. For more information, see [How transactional replication works](https://learn.microsoft.com/en-us/previous-versions/sql/sql-server-2008-r2/ms151706\(v=sql.105\)).
[](https://learn.microsoft.com/en-us/sql/relational-databases/logs/the-transaction-log-sql-server?view=sql-server-ver17#support-high-availability-and-disaster-recovery-solutions)
### Support high availability and disaster recovery solutions
The standby-server solutions, Always On availability groups, database mirroring, and log shipping, rely heavily on the transaction log.
In an **Always On availability groups scenario** , every update to a database on the primary replica is immediately reproduced in the separate copies of the database on all the secondary replicas. The primary replica sends each log record immediately to the secondary replicas, which apply the incoming log records to the availability databases, continually rolling forward the log. For more information, see [Always On failover cluster instances (SQL Server)](https://learn.microsoft.com/en-us/sql/sql-server/failover-clusters/windows/always-on-failover-cluster-instances-sql-server?view=sql-server-ver17).
In a **log shipping scenario** , the primary server sends the transaction log backups of the primary database to one or more destinations. Each secondary server restores the log backups to its local secondary database. For more information, see [About log shipping (SQL Server)](https://learn.microsoft.com/en-us/sql/database-engine/log-shipping/about-log-shipping-sql-server?view=sql-server-ver17).
In a **database mirroring scenario** , every update to a database, the principal database, is immediately reproduced in a separate, full copy of the database, the mirror database. The principal server instance sends each log record immediately to the mirror server instance, which applies the incoming log records to the mirror database, continually rolling it forward. For more information, see [Database mirroring (SQL Server)](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-sql-server?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/relational-databases/logs/the-transaction-log-sql-server?view=sql-server-ver17#transaction-log-characteristics)
## Transaction log characteristics
Characteristics of the SQL Server Database Engine transaction log:
  * The transaction log is implemented as a separate file or set of files in the database. The log cache is managed separately from the buffer cache for data pages. This separation results in simple, fast, and robust code within the SQL Server Database Engine. For more information, see [Transaction log physical architecture](https://learn.microsoft.com/en-us/sql/relational-databases/sql-server-transaction-log-architecture-and-management-guide?view=sql-server-ver17#physical_arch).
  * The format of log records and pages isn't constrained to follow the format of data pages.
  * The transaction log can be implemented in several files. You can configure the files to expand automatically by setting the `FILEGROWTH` value for the log. This configuration reduces the potential for running out of space in the transaction log, at the same time reducing administrative overhead. For more information, see [ALTER DATABASE (Transact-SQL) file and filegroup options](https://learn.microsoft.com/en-us/sql/t-sql/statements/alter-database-transact-sql-file-and-filegroup-options?view=sql-server-ver17).
  * The mechanism to reuse the space within the log files is quick and has minimal effect on transaction throughput.


For information about the physical and logical architecture of the transaction log, see the [SQL Server transaction log architecture and management guide](https://learn.microsoft.com/en-us/sql/relational-databases/sql-server-transaction-log-architecture-and-management-guide?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/relational-databases/logs/the-transaction-log-sql-server?view=sql-server-ver17#transaction-log-truncation)
## Transaction log truncation
Log truncation frees space in the log file for reuse by the transaction log. You must regularly truncate your transaction log to keep it from filling the allotted space. Several factors can delay log truncation, so monitoring log size matters. Some operations can be minimally logged to reduce their effect on transaction log size.
Log truncation deletes inactive [virtual log files (VLFs)](https://learn.microsoft.com/en-us/sql/relational-databases/sql-server-transaction-log-architecture-and-management-guide?view=sql-server-ver17#physical_arch) from the logical transaction log of a SQL Server database, freeing space in the logical log for reuse by the physical transaction log. If a transaction log is never truncated, it eventually fills all the disk space allocated to physical log files.
To avoid running out of space, unless log truncation is delayed for some reason, truncation occurs automatically after the following events:
  * Under the simple recovery model, after a checkpoint.
  * Under the full recovery model or bulk-logged recovery model, if a checkpoint has occurred since the previous backup, truncation occurs after a log backup (unless it's a copy-only log backup).
  * When you first create a database that uses the full recovery model, the transaction log is reused as needed (similar to a database using the simple recovery model), up until the time you create a full database backup.


For more information, see [Factors that can delay log truncation](https://learn.microsoft.com/en-us/sql/relational-databases/logs/the-transaction-log-sql-server?view=sql-server-ver17#factors-that-can-delay-log-truncation) later in this article.
Log truncation doesn't reduce the size of the physical log file. To reduce the physical size of a physical log file, you must shrink the log file. For information about shrinking the size of the physical log file, see [Manage the size of the transaction log file](https://learn.microsoft.com/en-us/sql/relational-databases/logs/manage-the-size-of-the-transaction-log-file?view=sql-server-ver17). However, keep in mind [factors that can delay log truncation](https://learn.microsoft.com/en-us/sql/relational-databases/logs/the-transaction-log-sql-server?view=sql-server-ver17#factors-that-can-delay-log-truncation). If the storage space is required again after a log shrink, the transaction log will grow again and, by doing that, introduce performance overhead during log grow operations.
[](https://learn.microsoft.com/en-us/sql/relational-databases/logs/the-transaction-log-sql-server?view=sql-server-ver17#factors-that-can-delay-log-truncation)
## Factors that can delay log truncation
When log records remain active for a long time, transaction log truncation is delayed, and the transaction log can fill up, as described earlier in this article.
For information about how to respond to a full transaction log, see [Troubleshoot a full transaction log (SQL Server error 9002)](https://learn.microsoft.com/en-us/sql/relational-databases/logs/troubleshoot-a-full-transaction-log-sql-server-error-9002?view=sql-server-ver17).
Log truncation can be delayed for various reasons. To learn what is preventing your log truncation, query the `log_reuse_wait` and `log_reuse_wait_desc` columns of the [sys.databases](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-databases-transact-sql?view=sql-server-ver17) catalog view. The following table describes the values of these columns.
Expand table
log_reuse_wait value | log_reuse_wait_desc value | Description
---|---|---
`0` | `NOTHING` | There are currently one or more reusable [virtual log files (VLFs)](https://learn.microsoft.com/en-us/sql/relational-databases/sql-server-transaction-log-architecture-and-management-guide?view=sql-server-ver17#physical_arch).
`1` | `CHECKPOINT` | No checkpoint has occurred since the last log truncation, or the head of the log hasn't yet moved beyond a [virtual log file (VLF)](https://learn.microsoft.com/en-us/sql/relational-databases/sql-server-transaction-log-architecture-and-management-guide?view=sql-server-ver17#physical_arch). (All recovery models.)

This scenario is a routine reason for delaying log truncation. For more information, see [Database checkpoints (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/logs/database-checkpoints-sql-server?view=sql-server-ver17).
`2` | `LOG_BACKUP` | A log backup is required before the transaction log can be truncated. (Full or bulk-logged recovery models only.)

When the next log backup is completed, some log space might become reusable.
`3` | `ACTIVE_BACKUP_OR_RESTORE` | A data backup or a restore is in progress. (All recovery models.)

If a data backup is preventing log truncation, canceling the backup operation might help the immediate problem.
`4` | `ACTIVE_TRANSACTION` | A transaction is active (all recovery models):

A long-running transaction might exist at the start of the log backup. In this case, freeing the space might require another log backup. Long-running transactions prevent log truncation under all recovery models, including the simple recovery model, under which the transaction log is generally truncated on each automatic checkpoint.

A transaction is deferred. A _deferred transaction_ is effectively an active transaction whose rollback is blocked because of some unavailable resource. For information about the causes of deferred transactions and how to move them out of the deferred state, see [Deferred transactions (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/deferred-transactions-sql-server?view=sql-server-ver17).

Long-running transactions might also fill up `tempdb`'s transaction log. `tempdb` is used implicitly by user transactions for internal objects such as work tables for sorting, work files for hashing, cursor work tables, and row versioning. Even if the user transaction includes only reading data (`SELECT` queries), internal objects might be created and used under user transactions. Then the `tempdb` transaction log can be filled.
`5` | `DATABASE_MIRRORING` | Database mirroring is paused, or under high-performance mode, the mirror database is significantly behind the principal database. (Full recovery model only.)

For more information, see [Database mirroring (SQL Server)](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-sql-server?view=sql-server-ver17).
`6` | `REPLICATION` | During transactional replications, transactions relevant to the publications are still undelivered to the distribution database. (Full recovery model only.)

For information about transactional replication, see [SQL Server replication](https://learn.microsoft.com/en-us/sql/relational-databases/replication/sql-server-replication?view=sql-server-ver17).
`7` | `DATABASE_SNAPSHOT_CREATION` | A database snapshot is being created. (All recovery models.)

This is a routine, and typically brief, cause of delayed log truncation.
`8` | `LOG_SCAN` | A log scan is occurring. (All recovery models.)

This is a routine, and typically brief, cause of delayed log truncation.
`9` | `AVAILABILITY_REPLICA` | A secondary replica of an availability group is applying transaction log records of this database to a corresponding secondary database. (Full recovery model only.)

For more information, see [What is an Always On availability group?](https://learn.microsoft.com/en-us/sql/database-engine/availability-groups/windows/overview-of-always-on-availability-groups-sql-server?view=sql-server-ver17).
`10` | - | For internal use only.
`11` | - | For internal use only.
`12` | - | For internal use only.
`13` | `OLDEST_PAGE` | If a database is configured to use indirect checkpoints, the oldest page on the database might be older than the checkpoint [log sequence number (LSN)](https://learn.microsoft.com/en-us/sql/relational-databases/sql-server-transaction-log-architecture-and-management-guide?view=sql-server-ver17#Logical_Arch). In this case, the oldest page can delay log truncation. (All recovery models.)

For information about indirect checkpoints, see [Database checkpoints (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/logs/database-checkpoints-sql-server?view=sql-server-ver17).
`14` | `OTHER_TRANSIENT` | This value is currently not used.
`16` | `XTP_CHECKPOINT` | An In-Memory OLTP checkpoint needs to be performed. For memory-optimized tables, an automatic checkpoint is taken when the transaction log file becomes bigger than 1.5 GB since the last checkpoint. (Includes both disk-based and memory-optimized tables.)

For more information, see [Checkpoint operation for memory-optimized tables](https://learn.microsoft.com/en-us/sql/relational-databases/in-memory-oltp/checkpoint-operation-for-memory-optimized-tables?view=sql-server-ver17) and [Logging and checkpoint process for memory optimized tables](https://blogs.msdn.microsoft.com/sqlcat/2016/05/20/logging-and-checkpoint-process-for-memory-optimized-tables-2/).
[](https://learn.microsoft.com/en-us/sql/relational-databases/logs/the-transaction-log-sql-server?view=sql-server-ver17#operations-that-can-be-minimally-logged)
## Operations that can be minimally logged
_Minimal logging_ involves logging only the information that's required to recover the transaction without supporting point-in-time recovery. This article identifies the operations that are minimally logged under the bulk-logged [recovery model](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/recovery-models-sql-server?view=sql-server-ver17) (and also under the simple recovery model, except when a backup is running).
Minimal logging isn't supported for memory-optimized tables.
Under the full [recovery model](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/recovery-models-sql-server?view=sql-server-ver17), all bulk operations are fully logged. However, you can minimize logging for a set of bulk operations by switching the database to the bulk-logged recovery model temporarily for bulk operations. Minimal logging is more efficient than full logging, and it reduces the possibility of a large-scale bulk operation filling the available transaction log space during a bulk transaction. However, if the database is damaged or lost when minimal logging is in effect, you can't recover the database to the point of failure.
The following operations, which are fully logged under the full recovery model, are minimally logged under the simple and bulk-logged recovery model:
  * Bulk import operations ([bcp](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17), [BULK INSERT](https://learn.microsoft.com/en-us/sql/t-sql/statements/bulk-insert-transact-sql?view=sql-server-ver17), and [INSERT](https://learn.microsoft.com/en-us/sql/t-sql/statements/insert-transact-sql?view=sql-server-ver17)). For more information about when bulk import into a table is minimally logged, see [Prerequisites for minimal logging in bulk import](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/prerequisites-for-minimal-logging-in-bulk-import?view=sql-server-ver17).
When transactional replication is enabled, `BULK INSERT` operations are fully logged even under the bulk-logged recovery model.
  * [SELECT - INTO clause](https://learn.microsoft.com/en-us/sql/t-sql/queries/select-into-clause-transact-sql?view=sql-server-ver17) operations.
When transactional replication is enabled, `SELECT INTO` operations are fully logged even under the bulk-logged recovery model.
  * Partial updates to large value data types, using the `.WRITE` clause in the [UPDATE](https://learn.microsoft.com/en-us/sql/t-sql/queries/update-transact-sql?view=sql-server-ver17) statement when inserting or appending new data. Minimal logging isn't used when existing values are updated. For more information about large value data types, see [Data types](https://learn.microsoft.com/en-us/sql/t-sql/data-types/data-types-transact-sql?view=sql-server-ver17).
  * [WRITETEXT](https://learn.microsoft.com/en-us/sql/t-sql/queries/writetext-transact-sql?view=sql-server-ver17) and [UPDATETEXT](https://learn.microsoft.com/en-us/sql/t-sql/queries/updatetext-transact-sql?view=sql-server-ver17) statements when inserting or appending new data into the **text** , **ntext** , and **image** data type columns. Minimal logging isn't used when existing values are updated.
The `WRITETEXT` and `UPDATETEXT` statements are deprecated. Avoid using them in new applications.
  * If the database is set to the simple or bulk-logged recovery model, some index DDL operations are minimally logged, whether the operation is run offline or online. The minimally logged index operations are:
    * [CREATE INDEX](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-index-transact-sql?view=sql-server-ver17) operations (including indexed views).
    * [ALTER INDEX REBUILD](https://learn.microsoft.com/en-us/sql/t-sql/statements/alter-index-transact-sql?view=sql-server-ver17) or `DBCC DBREINDEX` operation.
Index build operations use minimal logging but might be delayed when there's a concurrently running backup. This delay is caused by the synchronization requirements of minimally logged buffer pool pages when you're using the simple or bulk-logged recovery model.
The `DBCC DBREINDEX` statement is deprecated. Avoid using it in new applications.
    * [DROP INDEX](https://learn.microsoft.com/en-us/sql/t-sql/statements/drop-index-transact-sql?view=sql-server-ver17) new heap rebuild (if applicable). Index page deallocation during a `DROP INDEX` operation is always fully logged.


[](https://learn.microsoft.com/en-us/sql/relational-databases/logs/the-transaction-log-sql-server?view=sql-server-ver17#related-tasks)
## Related tasks
Expand table
Task | Article
---|---
Manage the transaction log |  [Manage the size of the transaction log file](https://learn.microsoft.com/en-us/sql/relational-databases/logs/manage-the-size-of-the-transaction-log-file?view=sql-server-ver17)

[Troubleshoot a full transaction log (SQL Server error 9002)](https://learn.microsoft.com/en-us/sql/relational-databases/logs/troubleshoot-a-full-transaction-log-sql-server-error-9002?view=sql-server-ver17)
Back up the transaction log (full recovery model only) |  [Back up a transaction log](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-a-transaction-log-sql-server?view=sql-server-ver17)

[Back up the transaction log when the database is damaged (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-the-transaction-log-when-the-database-is-damaged-sql-server?view=sql-server-ver17)
Restore the transaction log (full recovery model only) | [Restore a transaction log backup (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/restore-a-transaction-log-backup-sql-server?view=sql-server-ver17)
[](https://learn.microsoft.com/en-us/sql/relational-databases/logs/the-transaction-log-sql-server?view=sql-server-ver17#related-content)
## Related content
  * [SQL Server transaction log architecture and management guide](https://learn.microsoft.com/en-us/sql/relational-databases/sql-server-transaction-log-architecture-and-management-guide?view=sql-server-ver17)
  * [Control transaction durability](https://learn.microsoft.com/en-us/sql/relational-databases/logs/control-transaction-durability?view=sql-server-ver17)
  * [Prerequisites for minimal logging in bulk import](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/prerequisites-for-minimal-logging-in-bulk-import?view=sql-server-ver17)
  * [Back up and restore of SQL Server databases](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver17)
  * [Restore and recovery overview (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/restore-and-recovery-overview-sql-server?view=sql-server-ver17#TlogAndRecovery)
  * [Database checkpoints (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/logs/database-checkpoints-sql-server?view=sql-server-ver17)
  * [View or change the properties of a database](https://learn.microsoft.com/en-us/sql/relational-databases/databases/view-or-change-the-properties-of-a-database?view=sql-server-ver17)
  * [Recovery models (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/recovery-models-sql-server?view=sql-server-ver17)
  * [Transaction log backups (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/transaction-log-backups-sql-server?view=sql-server-ver17)
  * [sys.dm_db_log_info (Transact-SQL)](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/sys-dm-db-log-info-transact-sql?view=sql-server-ver17)
  * [sys.dm_db_log_space_usage (Transact-SQL)](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/sys-dm-db-log-space-usage-transact-sql?view=sql-server-ver17)


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
  * [ Troubleshoot Full Transaction Log Error 9002 - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/logs/troubleshoot-a-full-transaction-log-sql-server-error-9002?source=recommendations)
Learn how to resolve a full SQL Server transaction log, and how to avoid the problem in the future.
  * [ Manage Transaction Log File Size - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/logs/manage-the-size-of-the-transaction-log-file?source=recommendations)
Learn how to monitor SQL Server transaction log size, shrink the log, enlarge a log, optimize the tempdb log growth rate, and control transaction log growth.
  * [ sys.dm_db_log_info (Transact-SQL) - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/sys-dm-db-log-info-transact-sql?source=recommendations)
The sys.dm_db_log_info (Transact-SQL) dynamic management function returns virtual log file (VLF) information from the transaction log.
  * [ SQL Server Transaction Log Architecture and Management Guide - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/sql-server-transaction-log-architecture-and-management-guide?source=recommendations)
The SQL Server transaction log is a critical component. Learn about its architecture and how to manage it.
  * [ sys.dm_db_log_space_usage (Transact-SQL) - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/sys-dm-db-log-space-usage-transact-sql?source=recommendations)
The sys.dm_db_log_space_usage dynamic management view returns space usage information for the transaction log.
  * [ DBCC SHRINKFILE (Transact-SQL) - SQL Server ](https://learn.microsoft.com/en-us/sql/t-sql/database-console-commands/dbcc-shrinkfile-transact-sql?source=recommendations)
DBCC SHRINKFILE shrinks the size of a database file.
  * [ Recovery Models (SQL Server) - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/recovery-models-sql-server?source=recommendations)
Learn about SQL Server recovery models, which control how to log transactions, whether the transaction log requires backing up, and what restore operations are available.
  * [ Considerations for the autogrow and autoshrink - SQL Server ](https://learn.microsoft.com/en-us/troubleshoot/sql/database-engine/database-file-operations/considerations-autogrow-autoshrink?source=recommendations)
This article provides information regarding what happens when you select the autogrow and autoshrink for your environment.


Show 5 more
Module
[ Implement transactions with Transact-SQL - Training ](https://learn.microsoft.com/en-us/training/modules/implement-transactions-transact-sql/?source=recommendations)
Implement transactions with Transact-SQL
Mar 8, 4 PM - Mar 8, 4 PM
Experiment with what's next in AI-driven apps and agent design
* * *
  * Last updated on 08/26/2025


##  In this article
  1. [Operations supported by the transaction log](https://learn.microsoft.com/en-us/sql/relational-databases/logs/the-transaction-log-sql-server?view=sql-server-ver17#operations-supported-by-the-transaction-log)
  2. [Transaction log characteristics](https://learn.microsoft.com/en-us/sql/relational-databases/logs/the-transaction-log-sql-server?view=sql-server-ver17#transaction-log-characteristics)
  3. [Transaction log truncation](https://learn.microsoft.com/en-us/sql/relational-databases/logs/the-transaction-log-sql-server?view=sql-server-ver17#transaction-log-truncation)
  4. [Factors that can delay log truncation](https://learn.microsoft.com/en-us/sql/relational-databases/logs/the-transaction-log-sql-server?view=sql-server-ver17#factors-that-can-delay-log-truncation)
  5. [Operations that can be minimally logged](https://learn.microsoft.com/en-us/sql/relational-databases/logs/the-transaction-log-sql-server?view=sql-server-ver17#operations-that-can-be-minimally-logged)
  6. [Related tasks](https://learn.microsoft.com/en-us/sql/relational-databases/logs/the-transaction-log-sql-server?view=sql-server-ver17#related-tasks)
  7. [Related content](https://learn.microsoft.com/en-us/sql/relational-databases/logs/the-transaction-log-sql-server?view=sql-server-ver17#related-content)


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
[ Sign in ](https://learn.microsoft.com/en-us/sql/relational-databases/logs/the-transaction-log-sql-server?view=sql-server-ver17)
[English (United States)](https://learn.microsoft.com/en-us/locale?target=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fsql%2Frelational-databases%2Flogs%2Fthe-transaction-log-sql-server%3Fview%3Dsql-server-ver17)
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
