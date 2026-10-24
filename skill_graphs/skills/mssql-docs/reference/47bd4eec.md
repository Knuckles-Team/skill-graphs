# Transparent data encryption (TDE)
Feedback
Summarize this article for me
##  In this article
  1. [About TDE](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver17#about-tde)
  2. [Enable TDE](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver17#enable-tde)
  3. [Commands and functions](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver17#commands-and-functions)
  4. [Catalog views and dynamic management views](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver17#catalog-views-and-dynamic-management-views)
  5. [Permissions](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver17#permissions)
  6. [Considerations](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver17#considerations)
  7. [Limitations](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver17#limitations)
  8. [TDE scan](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver17#tde-scan)
  9. [TDE and transaction logs](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver17#tde-and-transaction-logs)
  10. [TDE and the tempdb system database](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver17#tde-and-the-tempdb-system-database)
  11. [TDE and replication](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver17#tde-and-replication)
  12. [TDE and availability groups](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver17#tde-and-availability-groups)
  13. [TDE and FILESTREAM data](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver17#tde-and-filestream-data)
  14. [TDE and backups](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver17#tde-and-backups)
  15. [Remove TDE](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver17#remove-tde)
  16. [TDE and the buffer pool extension](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver17#tde-and-the-buffer-pool-extension)
  17. [TDE and In-Memory OLTP](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver17#tde-and-in-memory-oltp)
  18. [Guidelines on managing certificates used in TDE](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver17#guidelines-on-managing-certificates-used-in-tde)
  19. [Related content](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver17#related-content)

Show 15 more
**Applies to:** ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure SQL Database](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure SQL Managed Instance](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure Synapse Analytics](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Analytics Platform System (PDW)](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to)
Transparent data encryption (TDE) encrypts SQL Server, Azure SQL Database, and Azure Synapse Analytics data files. This encryption is known as encrypting data at rest.
To help secure a user database, you can take precautions like:
  * Designing a secure system.
  * Encrypting confidential assets.
  * Building a firewall around the database servers.


However, a malicious party who steals physical media like drives or backup tapes can restore or attach the database and browse its data.
One solution is to encrypt sensitive data in a database and use a certificate to protect the keys that encrypt the data. This solution prevents anyone without the keys from using the data. But you must plan this kind of protection in advance.
TDE does real-time I/O encryption and decryption of data and log files. The encryption uses a database encryption key (DEK). The database boot record stores the key for availability during recovery. The DEK is a symmetric key, and is secured by a certificate that the server's `master` database stores or by an asymmetric key that an EKM module protects.
TDE protects data at rest, which is the data and log files. It lets you follow many laws, regulations, and guidelines established in various industries. This ability lets software developers encrypt data by using AES and 3DES encryption algorithms without changing existing applications.
TDE isn't available for system databases. It can't be used to encrypt `master`, `model`, or `msdb`. `tempdb` is automatically encrypted when a user database enabled TDE, but can't be encrypted directly.
TDE doesn't provide encryption across communication channels. For more information about how to encrypt data across communication channels, see [Encrypt connections to SQL Server by importing a certificate](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/configure-sql-server-encryption?view=sql-server-ver17).
**Related topics:**
  * [Transparent data encryption for SQL Database, SQL Managed Instance, and Azure Synapse Analytics](https://learn.microsoft.com/en-us/azure/azure-sql/database/transparent-data-encryption-tde-overview)
  * [Get started with transparent data encryption (TDE) in Azure Synapse Analytics](https://learn.microsoft.com/en-us/azure/synapse-analytics/sql-data-warehouse/sql-data-warehouse-encryption-tde-tsql)
  * [Move a TDE protected database to another SQL Server](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/move-a-tde-protected-database-to-another-sql-server?view=sql-server-ver17)
  * [Enable TDE on SQL Server Using EKM](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/enable-tde-on-sql-server-using-ekm?view=sql-server-ver17)
  * [Use SQL Server Connector with SQL Encryption Features](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/use-sql-server-connector-with-sql-encryption-features?view=sql-server-ver17)
  * [The SQL Server Security Blog on TDE with FAQ](https://learn.microsoft.com/en-us/archive/blogs/sqlsecurity/feature-spotlight-transparent-data-encryption-tde)


[](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver17#about-tde)
## About TDE
Encryption of a database file is done at the page level. The pages in an encrypted database are encrypted before they're written to disk and are decrypted when read into memory. TDE doesn't increase the size of the encrypted database.
[](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver17#information-applicable-to-sql-database)
### Information applicable to SQL Database
When you use TDE with Azure SQL Database, SQL Database automatically creates the server-level certificate stored in the `master` database. To move a TDE database on SQL Database, you don't have to decrypt the database for the move operation. For more information on using TDE with SQL Database, see [transparent data encryption with Azure SQL Database](https://learn.microsoft.com/en-us/azure/azure-sql/database/transparent-data-encryption-tde-overview).
[](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver17#information-applicable-to-sql-server)
### Information applicable to SQL Server
After you secure a database, you can restore it by using the correct certificate. For more information about certificates, see [SQL Server Certificates and Asymmetric Keys](https://learn.microsoft.com/en-us/sql/relational-databases/security/sql-server-certificates-and-asymmetric-keys?view=sql-server-ver17).
After you enable TDE, immediately back up the certificate and its associated private key. If the certificate becomes unavailable, or if you restore or attach the database on another server, you need backups of the certificate and private key. Otherwise, you can't open the database. Certificates stored in a [contained system database](https://learn.microsoft.com/en-us/sql/database-engine/availability-groups/windows/contained-availability-groups-overview?view=sql-server-ver17) should also be backed up.
Keep the encrypting certificate even if you've disabled TDE on the database. Although the database isn't encrypted, parts of the transaction log might remain protected. You also might need the certificate for some operations until you do a full database backup.
You can still use a certificate that exceeds its expiration date to encrypt and decrypt data with TDE.
[](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver17#encryption-hierarchy)
### Encryption hierarchy
The Windows Data Protection API (DPAPI) is at the root of the encryption tree, secures the key hierarchy at the machine level, and is used to protect the service master key (SMK) for the database server instance. The SMK protects the database master key (DMK), which is stored at the user database level and protects certificates and asymmetric keys. These keys, in turn, protect symmetric keys, which protect the data. TDE uses a similar hierarchy down to the certificate. When you use TDE, the DMK and certificate must be stored in the `master` database. A new key, used only for TDE and referred to as the database encryption key (DEK), is created and stored in the user database.
The following illustration shows the architecture of TDE encryption. Only the database-level items (the database encryption key and `ALTER DATABASE` portions) are user-configurable when you use TDE on SQL Database.
[ ![Diagram showing the transparent data encryption architecture.](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/media/transparent-data-encryption/tde-architecture.png?view=sql-server-ver17) ](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/media/transparent-data-encryption/tde-architecture.png?view=sql-server-ver17#lightbox)
[](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver17#enable-tde)
## Enable TDE
To use TDE, follow these steps.
**Applies to** : SQL Server.
  1. Create a master key.
  2. Create or obtain a certificate protected by the master key.
  3. Create a database encryption key and protect it by using the certificate.
  4. Set the database to use encryption.


The following example shows encryption and decryption of the `AdventureWorks2025` database using a certificate named `MyServerCert` that's installed on the server.
SQL
Copy
```
USE master;
GO

CREATE MASTER KEY ENCRYPTION BY PASSWORD= '<password>';
GO

CREATE CERTIFICATE MyServerCert
    WITH SUBJECT = 'My DEK Certificate';
GO

USE AdventureWorks2022;
GO

CREATE DATABASE ENCRYPTION KEY WITH ALGORITHM = AES_256
    ENCRYPTION BY SERVER CERTIFICATE MyServerCert;
GO

ALTER DATABASE AdventureWorks2022
    SET ENCRYPTION ON;
GO

```

The encryption and decryption operations are scheduled on background threads by SQL Server. To view the status of these operations, use the catalog views and dynamic management views in the table that appears later in this article.
Backup files for databases that have TDE enabled are also encrypted with the DEK. As a result, when you restore these backups, the certificate that protects the DEK must be available. Therefore, in addition to backing up the database, make sure to maintain backups of the server certificates. Data loss results if the certificates are no longer available.
For more information, see [SQL Server Certificates and Asymmetric Keys](https://learn.microsoft.com/en-us/sql/relational-databases/security/sql-server-certificates-and-asymmetric-keys?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver17#commands-and-functions)
## Commands and functions
For the following statements to accept TDE certificates, use a database master key to encrypt them. If you encrypt them by password only, the statements reject them as encryptors.
If you make the certificates password protected after TDE uses them, the database becomes inaccessible after a restart.
The following table provides links and explanations of TDE commands and functions:
Expand table
Command or function | Purpose
---|---
[CREATE DATABASE ENCRYPTION KEY](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-database-encryption-key-transact-sql?view=sql-server-ver17) | Creates a key that encrypts a database
[ALTER DATABASE ENCRYPTION KEY](https://learn.microsoft.com/en-us/sql/t-sql/statements/alter-database-encryption-key-transact-sql?view=sql-server-ver17) | Changes the key that encrypts a database
[DROP DATABASE ENCRYPTION KEY](https://learn.microsoft.com/en-us/sql/t-sql/statements/drop-database-encryption-key-transact-sql?view=sql-server-ver17) | Removes the key that encrypts a database
[ALTER DATABASE SET options](https://learn.microsoft.com/en-us/sql/t-sql/statements/alter-database-transact-sql-set-options?view=sql-server-ver17) | Explains the `ALTER DATABASE` option that is used to enable TDE
[](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver17#catalog-views-and-dynamic-management-views)
## Catalog views and dynamic management views
The following table shows TDE catalog views and dynamic management views (DMV).
Expand table
Catalog view or dynamic management view | Purpose
---|---
[sys.databases](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-databases-transact-sql?view=sql-server-ver17) | Catalog view that displays database information
[sys.certificates](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-certificates-transact-sql?view=sql-server-ver17) | Catalog view that shows the certificates in a database
[sys.dm_database_encryption_keys](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/sys-dm-database-encryption-keys-transact-sql?view=sql-server-ver17) | Dynamic management view that provides information about a database's encryption keys and state of encryption
[](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver17#permissions)
## Permissions
Each TDE feature and command has individual permission requirements as described in the tables shown earlier.
Viewing the metadata involved with TDE requires the `VIEW DEFINITION` permission on a certificate.
[](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver17#considerations)
## Considerations
While a re-encryption scan for a database encryption operation is in progress, maintenance operations to the database are disabled. You can use the single-user mode setting for the database to do maintenance operations. For more information, see [Set a database to single-user mode](https://learn.microsoft.com/en-us/sql/relational-databases/databases/set-a-database-to-single-user-mode?view=sql-server-ver17).
Use the `sys.dm_database_encryption_keys` dynamic management view to find the state of database encryption. For more information, see the [Catalog views and dynamic management views](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver17#catalog-views-and-dynamic-management-views) section earlier in this article.
In TDE, all files and filegroups in a database are encrypted. If any filegroup in a database is marked `READ ONLY`, the database encryption operation fails.
If you use a database in database mirroring or log shipping, both databases are encrypted. The log transactions are encrypted when sent between them.
Full-text indexes are encrypted when a database is set for encryption. Such indexes created in SQL Server 2005 (9.x) and earlier versions, are imported into the database by SQL Server 2008 (10.0.x) and later versions, and are encrypted by TDE.
To monitor changes in the TDE status of a database, use SQL Server Audit or Azure SQL Database auditing. For SQL Server, TDE is tracked under the audit action group `DATABASE_OBJECT_CHANGE_GROUP`, which you can find in [SQL Server Audit action groups and actions](https://learn.microsoft.com/en-us/sql/relational-databases/security/auditing/sql-server-audit-action-groups-and-actions?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver17#limitations)
## Limitations
The following operations are disallowed during initial database encryption, key change, or database decryption:
  * Dropping a file from a filegroup in a database
  * Dropping a database
  * Taking a database offline
  * Detaching a database
  * Transitioning a database or filegroup into a `READ ONLY` state


The following operations are disallowed during the `CREATE DATABASE ENCRYPTION KEY`, `ALTER DATABASE ENCRYPTION KEY`, `DROP DATABASE ENCRYPTION KEY`, and `ALTER DATABASE...SET ENCRYPTION` statements:
  * Dropping a file from a filegroup in a database
  * Dropping a database
  * Taking a database offline
  * Detaching a database
  * Transitioning a database or filegroup into a `READ ONLY` state
  * Using an `ALTER DATABASE` command
  * Starting a database or database-file backup
  * Starting a database or database-file restore
  * Creating a snapshot


The following operations or conditions prevent the `CREATE DATABASE ENCRYPTION KEY`, `ALTER DATABASE ENCRYPTION KEY`, `DROP DATABASE ENCRYPTION KEY`, and `ALTER DATABASE...SET ENCRYPTION` statements:
  * A database is read-only or has read-only filegroups.
  * An `ALTER DATABASE` command is running.
  * A data backup is running.
  * A database is in an offline or restore condition.
  * A snapshot is in progress.
  * Database maintenance tasks are running.


When database files are created, instant file initialization is unavailable when TDE is enabled.
To encrypt a DEK with an asymmetric key, the asymmetric key must be on an extensible key-management provider.
[](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver17#tde-scan)
## TDE scan
To enable TDE on a database, SQL Server must do an encryption scan. The scan reads each page from the data files into the buffer pool and then writes the encrypted pages back out to disk.
To give you more control over the encryption scan, SQL Server 2019 (15.x) introduces TDE scan, which has a suspend and resume syntax. You can pause the scan while the workload on the system is heavy or during business-critical hours and then resume the scan later.
Use the following syntax to pause the TDE encryption scan:
SQL
Copy
```
ALTER DATABASE <db_name> SET ENCRYPTION SUSPEND;

```

Similarly, use the following syntax to resume the TDE encryption scan:
SQL
Copy
```
ALTER DATABASE <db_name> SET ENCRYPTION RESUME;

```

The encryption_scan_state column has been added to the `sys.dm_database_encryption_keys` dynamic management view. It shows the current state of the encryption scan. There's also a new column called encryption_scan_modify_date, which contains the date and time of the last encryption-scan state change.
If the SQL Server instance restarts while its encryption scan is suspended, a message is logged in the error log during startup. The message indicates that an existing scan has been paused.
Suspend and Resume TDE scan feature isn't currently available in Azure SQL Database, Azure SQL Managed Instance, and Azure Synapse Analytics.
[](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver17#tde-and-transaction-logs)
## TDE and transaction logs
TDE protects data files and log files at rest. Encrypting the entire database after enabling TDE on an unencrypted database is a sizable data operation and the time it takes depends on the system resources on which this database is running. The [sys.dm_database_encryption_keys](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/sys-dm-database-encryption-keys-transact-sql?view=sql-server-ver17) DMV can be used to determine the encryption state of a database.
When TDE is turned on, the Database Engine forces the creation of a new transaction log, which will be encrypted by the database encryption key. Any log generated by previous transactions or current long running transactions interleaved between the TDE state change isn't encrypted.
The transaction logs can be monitored using the [sys.dm_db_log_info](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/sys-dm-db-log-info-transact-sql?view=sql-server-ver17) DMV, which also shows whether the log file is encrypted or not using the `vlf_encryptor_thumbprint` column that is available in Azure SQL, and SQL Server 2019 (15.x) and later versions. To find the encryption status of the log file using the `encryption_state` column in the `sys.dm_database_encryption_keys` view, here's a sample query:
SQL
Copy
```
USE AdventureWorks2022;
GO

/* The value 3 represents an encrypted state
   on the database and transaction logs. */
SELECT *
FROM sys.dm_database_encryption_keys
WHERE encryption_state = 3;
GO

```

For more information about the SQL Server log-file architecture, see [The transaction log](https://learn.microsoft.com/en-us/sql/relational-databases/logs/the-transaction-log-sql-server?view=sql-server-ver17).
Before a DEK changes, the previous DEK encrypts all data written to the transaction log.
If you change a DEK twice, you must do a log backup before you can change the DEK again.
[](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver17#tde-and-the-tempdb-system-database)
## TDE and the tempdb system database
The `tempdb` system database is encrypted if any other database on the SQL Server instance is encrypted by using TDE. This encryption might have a performance effect for unencrypted databases on the same SQL Server instance. For more information about the `tempdb` system database, see [tempdb Database](https://learn.microsoft.com/en-us/sql/relational-databases/databases/tempdb-database?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver17#tde-and-replication)
## TDE and replication
Replication doesn't automatically replicate data from a TDE-enabled database in an encrypted form. Separately enable TDE if you want to protect distribution and subscriber databases.
Snapshot replication can store data in unencrypted intermediate files like BCP files. The initial data distribution for transactional and merge replication can too. During such replication, you can enable encryption to protect the communication channel.
For more information, see [Encrypt connections to SQL Server by importing a certificate](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/configure-sql-server-encryption?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver17#tde-and-availability-groups)
## TDE and availability groups
You can [add an encrypted database to an Always On availability group](https://learn.microsoft.com/en-us/sql/database-engine/availability-groups/windows/encrypted-databases-with-always-on-availability-groups-sql-server?view=sql-server-ver17).
To encrypt databases that are part of an availability group, create the master key and certificates, or asymmetric key (EKM) on all secondary replicas before creating the [database encryption key](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-database-encryption-key-transact-sql?view=sql-server-ver17) on the primary replica.
If a certificate is used to protect the DEK, [back up the certificate](https://learn.microsoft.com/en-us/sql/t-sql/statements/backup-certificate-transact-sql?view=sql-server-ver17) created on the primary replica, and then [create the certificate from a file](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-certificate-transact-sql?view=sql-server-ver17) on all secondary replicas before creating the DEK on the primary replica.
[](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver17#tde-and-filestream-data)
## TDE and FILESTREAM data
FILESTREAM data isn't encrypted, even when you enable TDE.
[](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver17#tde-and-backups)
## TDE and backups
Certificates are commonly used in Transparent Data Encryption to protect the DEK. The certificate must be created in the `master` database. Backup files of databases that have TDE enabled, are also encrypted by using the DEK. As a result, when you restore from these backups, the certificate protecting the DEK must be available. This means that in addition to backing up the database, you must maintain backups of the server certificates to prevent data loss. Data loss occurs if the certificate is no longer available.
[](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver17#remove-tde)
## Remove TDE
Remove encryption from the database by using the `ALTER DATABASE` statement.
SQL
Copy
```
ALTER DATABASE <db_name> SET ENCRYPTION OFF;

```

To view the state of the database, use the [sys.dm_database_encryption_keys](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/sys-dm-database-encryption-keys-transact-sql?view=sql-server-ver17) dynamic management view.
While the encryption process is in progress, `ALTER DATABASE` statements aren't allowed on the database. Until the encryption process is finished, you can't start decrypting the database.
Wait for decryption to finish before removing the DEK by using [DROP DATABASE ENCRYPTION KEY](https://learn.microsoft.com/en-us/sql/t-sql/statements/drop-database-encryption-key-transact-sql?view=sql-server-ver17).
Back up the master key and certificate that are used for TDE to a safe location. The master key and certificate are required to restore backups that were taken when the database was encrypted with TDE. After you remove the DEK, take a log backup followed by a fresh full backup of the decrypted database.
[](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver17#tde-and-the-buffer-pool-extension)
## TDE and the buffer pool extension
When you encrypt a database using TDE, files related to buffer pool extension (BPE) aren't encrypted. For those files, use encryption tools like BitLocker or EFS at the file-system level.
[](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver17#tde-and-in-memory-oltp)
## TDE and In-Memory OLTP
You can enable TDE on a database that has In-Memory OLTP objects. In SQL Server 2016 (13.x) and Azure SQL Database, In-Memory OLTP log records and data are encrypted if you enable TDE. In SQL Server 2014 (12.x), In-Memory OLTP log records are encrypted if you enable TDE, but files in the `MEMORY_OPTIMIZED_DATA` filegroup are unencrypted.
[](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver17#guidelines-on-managing-certificates-used-in-tde)
## Guidelines on managing certificates used in TDE
You must back up the certificate and database master key when the database is enabled for TDE and is used in log shipping or database mirroring. Certificates stored in a contained system database should also be backed up.
The certificate used to protect the DEK should never be dropped from the `master` database. Doing so causes the encrypted database to become inaccessible.
A message like the following one (error 33091) is raised after executing `CREATE DATABASE ENCRYPTION KEY` if the certificate used in the command hasn't been backed up already.
The certificate used for encrypting the database encryption key hasn't been backed up. You should immediately back up the certificate and the private key associated with the certificate. If the certificate ever becomes unavailable or if you must restore or attach the database on another server, you must have backups of both the certificate and the private key or you'll not be able to open the database.
The following query can be used to identify the certificates used in TDE that haven't been backed up from the time it was created.
SQL
Copy
```
SELECT pvt_key_last_backup_date,
       Db_name(dek.database_id) AS encrypteddatabase,
       c.name AS Certificate_Name
FROM sys.certificates AS c
     INNER JOIN sys.dm_database_encryption_keys AS dek
         ON c.thumbprint = dek.encryptor_thumbprint;

```

If the column `pvt_key_last_backup_date` is `NULL`, the database corresponding to that row has been enabled for TDE, but the certificate used to protect its DEK hasn't been backed up. For more information on backing up a certificate, see [BACKUP CERTIFICATE](https://learn.microsoft.com/en-us/sql/t-sql/statements/backup-certificate-transact-sql?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver17#related-content)
## Related content
  * [Security for SQL Server Database Engine and Azure SQL Database](https://learn.microsoft.com/en-us/sql/relational-databases/security/security-center-for-sql-server-database-engine-and-azure-sql-database?view=sql-server-ver17)
  * [FILESTREAM (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/blob/filestream-sql-server?view=sql-server-ver17)
  * [SQL Server encryption](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/sql-server-encryption?view=sql-server-ver17)
  * [SQL Server and Database Encryption Keys (Database Engine)](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/sql-server-and-database-encryption-keys-database-engine?view=sql-server-ver17)


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
  * [ sys.dm_database_encryption_keys (Transact-SQL) - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/sys-dm-database-encryption-keys-transact-sql?source=recommendations)
sys.dm_database_encryption_keys (Transact-SQL)
  * [ CREATE DATABASE ENCRYPTION KEY (Transact-SQL) - SQL Server ](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-database-encryption-key-transact-sql?source=recommendations)
CREATE DATABASE ENCRYPTION KEY (Transact-SQL)
  * [ Move a TDE-Protected Database to Another SQL Server - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/move-a-tde-protected-database-to-another-sql-server?source=recommendations)
Describes how to protect a database using transparent data encryption (TDE) and then move the database to another instance of SQL Server using SQL Server Management Studio (SSMS) or Transact-SQL (T-SQL).
  * [ SQL Server Certificates and Asymmetric Keys - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/security/sql-server-certificates-and-asymmetric-keys?source=recommendations)
Learn about certificates and asymmetric keys in SQL Server, including externally generated or SQL Server generated certificates, tools, and related tasks.
  * [ SQL Server encryption - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/sql-server-encryption?source=recommendations)
Use these resources to understand how SQL Server uses encryption to enhance security for your databases.
  * [ ALTER DATABASE ENCRYPTION KEY (Transact-SQL) - SQL Server ](https://learn.microsoft.com/en-us/sql/t-sql/statements/alter-database-encryption-key-transact-sql?source=recommendations)
ALTER DATABASE ENCRYPTION KEY (Transact-SQL)
  * [ SQL Server & database encryption keys - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/sql-server-and-database-encryption-keys-database-engine?source=recommendations)
Learn about the service master key and database master key used by the SQL Server database engine to encrypt and secure data.


Show 4 more
Module
[ Protect data in-transit and at rest - Training ](https://learn.microsoft.com/en-us/training/modules/protect-data-transit-rest/?source=recommendations)
Protect data in-transit and at rest
Certification
[ Microsoft Certified: Azure Database Administrator Associate - Certifications ](https://learn.microsoft.com/en-us/credentials/certifications/azure-database-administrator-associate/?source=recommendations)
Administer an SQL Server database infrastructure for cloud, on-premises and hybrid relational databases using the Microsoft PaaS relational database offerings.
Mar 8, 4 PM - Mar 8, 4 PM
Experiment with what's next in AI-driven apps and agent design
* * *
  * Last updated on 09/07/2025


##  In this article
  1. [About TDE](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver17#about-tde)
  2. [Enable TDE](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver17#enable-tde)
  3. [Commands and functions](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver17#commands-and-functions)
  4. [Catalog views and dynamic management views](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver17#catalog-views-and-dynamic-management-views)
  5. [Permissions](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver17#permissions)
  6. [Considerations](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver17#considerations)
  7. [Limitations](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver17#limitations)
  8. [TDE scan](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver17#tde-scan)
  9. [TDE and transaction logs](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver17#tde-and-transaction-logs)
  10. [TDE and the tempdb system database](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver17#tde-and-the-tempdb-system-database)
  11. [TDE and replication](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver17#tde-and-replication)
  12. [TDE and availability groups](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver17#tde-and-availability-groups)
  13. [TDE and FILESTREAM data](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver17#tde-and-filestream-data)
  14. [TDE and backups](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver17#tde-and-backups)
  15. [Remove TDE](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver17#remove-tde)
  16. [TDE and the buffer pool extension](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver17#tde-and-the-buffer-pool-extension)
  17. [TDE and In-Memory OLTP](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver17#tde-and-in-memory-oltp)
  18. [Guidelines on managing certificates used in TDE](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver17#guidelines-on-managing-certificates-used-in-tde)
  19. [Related content](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver17#related-content)

Show 10 more
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
[ Sign in ](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver17)
[English (United States)](https://learn.microsoft.com/en-us/locale?target=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fsql%2Frelational-databases%2Fsecurity%2Fencryption%2Ftransparent-data-encryption%3Fview%3Dsql-server-ver17)
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
