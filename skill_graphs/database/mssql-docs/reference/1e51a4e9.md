# FILESTREAM (SQL Server)
Feedback
Summarize this article for me
##  In this article
  1. [When to Use FILESTREAM](https://learn.microsoft.com/en-us/sql/relational-databases/blob/filestream-sql-server?view=sql-server-ver17#when-to-use-filestream)
  2. [FILESTREAM Storage](https://learn.microsoft.com/en-us/sql/relational-databases/blob/filestream-sql-server?view=sql-server-ver17#filestream-storage)
  3. [Access BLOB Data with Transact-SQL and File System Streaming Access](https://learn.microsoft.com/en-us/sql/relational-databases/blob/filestream-sql-server?view=sql-server-ver17#access-blob-data-with-transact-sql-and-file-system-streaming-access)
  4. [Recommendations and guidelines for improving FILESTREAM performance](https://learn.microsoft.com/en-us/sql/relational-databases/blob/filestream-sql-server?view=sql-server-ver17#recommendations-and-guidelines-for-improving-filestream-performance)
  5. [Related tasks](https://learn.microsoft.com/en-us/sql/relational-databases/blob/filestream-sql-server?view=sql-server-ver17#related-tasks)
  6. [Related content](https://learn.microsoft.com/en-us/sql/relational-databases/blob/filestream-sql-server?view=sql-server-ver17#related-content)

Show 2 more
**Applies to:** ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) on Windows
FILESTREAM enables SQL Server-based applications to store unstructured data, such as documents and images, on the file system. Applications can use the rich streaming APIs and performance of the file system and at the same time maintain transactional consistency between the unstructured data and corresponding structured data.
FILESTREAM integrates the SQL Server Database Engine with an NTFS or ReFS file systems by storing **varbinary(max)** binary large object (BLOB) data as files on the file system. Transact-SQL statements can insert, update, query, search, and back up FILESTREAM data. Win32 file system interfaces provide streaming access to the data.
FILESTREAM uses the NT system cache for caching file data. Caching files in the system cache helps reduce any impact that FILESTREAM data might have on Database Engine performance. The SQL Server buffer pool isn't used; therefore, this memory is available for query processing.
FILESTREAM isn't automatically enabled when you install or upgrade SQL Server. You must enable FILESTREAM by using SQL Server Configuration Manager and SQL Server Management Studio. To use FILESTREAM, you must create or modify a database to contain a special type of filegroup. Then, create or modify a table so that it contains a **varbinary(max)** column with the FILESTREAM attribute. After you complete these tasks, you can use Transact-SQL and Win32 to manage the FILESTREAM data.
[](https://learn.microsoft.com/en-us/sql/relational-databases/blob/filestream-sql-server?view=sql-server-ver17#when-to-use-filestream)
## When to Use FILESTREAM
In SQL Server, BLOBs can be standard **varbinary(max)** data that stores the data in tables, or FILESTREAM **varbinary(max)** objects that store the data in the file system. The size and use of the data determines whether you should use database storage or file system storage. If the following conditions are true, you should consider using FILESTREAM:
  * Objects that are being stored are, on average, larger than 1 MB.
  * Fast read access is important.
  * You're developing applications that use a middle tier for application logic.


For smaller objects, storing **varbinary(max)** BLOBs in the database often provides better streaming performance.
[](https://learn.microsoft.com/en-us/sql/relational-databases/blob/filestream-sql-server?view=sql-server-ver17#filestream-storage)
## FILESTREAM Storage
FILESTREAM storage is implemented as a **varbinary(max)** column in which the data is stored as BLOBs in the file system. The sizes of the BLOBs are limited only by the volume size of the file system. The standard **varbinary(max)** limitation of 2-GB file sizes doesn't apply to BLOBs that are stored in the file system.
To specify that a column should store data on the file system, specify the FILESTREAM attribute on a **varbinary(max)** column. This attribute causes the Database Engine to store all data for that column on the file system, but not in the database file.
FILESTREAM data must be stored in FILESTREAM filegroups. A FILESTREAM filegroup is a special filegroup that contains file system directories instead of the files themselves. These file system directories are called _data containers_. Data containers are the interface between Database Engine storage and file system storage.
When you use FILESTREAM storage, consider the following:
  * When a table contains a FILESTREAM column, each row must have a non-null unique row ID.
  * Multiple data containers can be added to a FILESTREAM filegroup.
  * FILESTREAM data containers can't be nested.
  * When you're using failover clustering, the FILESTREAM filegroups must be on shared disk resources.
  * FILESTREAM filegroups can be on compressed volumes.


[](https://learn.microsoft.com/en-us/sql/relational-databases/blob/filestream-sql-server?view=sql-server-ver17#integrated-management)
### Integrated Management
Because FILESTREAM is implemented as a **varbinary(max)** column and integrated directly into the Database Engine, most SQL Server management tools and functions work without modification for FILESTREAM data. For example, you can use all backup and recovery models with FILESTREAM data, and the FILESTREAM data is backed up with the structured data in the database. If you don't want to back up FILESTREAM data with relational data, you can use a partial backup to exclude FILESTREAM filegroups.
[](https://learn.microsoft.com/en-us/sql/relational-databases/blob/filestream-sql-server?view=sql-server-ver17#integrated-security)
### Integrated Security
In SQL Server, FILESTREAM data is secured just like other data is secured: by granting permissions at the table or column levels. If a user has permission to the FILESTREAM column in a table, the user can open the associated files.
Encryption isn't supported on FILESTREAM data.
Only the account under which the SQL Server service account runs is granted permissions to the FILESTREAM container. We recommend that no other account is granted permissions on the data container.
SQL logins will not work with FILESTREAM containers. Only NTFS or ReFS authentication will work with FILESTREAM containers.
[](https://learn.microsoft.com/en-us/sql/relational-databases/blob/filestream-sql-server?view=sql-server-ver17#access-blob-data-with-transact-sql-and-file-system-streaming-access)
## Access BLOB Data with Transact-SQL and File System Streaming Access
After you store data in a FILESTREAM column, you can access the files by using Transact-SQL transactions or by using Win32 APIs.
[](https://learn.microsoft.com/en-us/sql/relational-databases/blob/filestream-sql-server?view=sql-server-ver17#transact-sql-access)
### Transact-SQL Access
By using Transact-SQL, you can insert, update, and delete FILESTREAM data:
  * You can use an insert operation to prepopulate a FILESTREAM field with a null value, empty value, or relatively short inline data. However, a large amount of data is more efficiently streamed into a file that uses Win32 interfaces.
  * When you update a FILESTREAM field, you modify the underlying BLOB data in the file system. When a FILESTREAM field is set to `NULL`, the BLOB data associated with the field is deleted. You can't use a Transact-SQL chunked update, implemented as `UPDATE`.**Write(), to perform partial updates to the data.
  * When you delete a row or delete or truncate a table that contains FILESTREAM data, you delete the underlying BLOB data in the file system.


[](https://learn.microsoft.com/en-us/sql/relational-databases/blob/filestream-sql-server?view=sql-server-ver17#file-system-streaming-access)
### File System Streaming Access
The Win32 streaming support works in the context of a SQL Server transaction. Within a transaction, you can use FILESTREAM functions to obtain a logical UNC file system path of a file. You then use the OpenSqlFilestream API to obtain a file handle. This handle can then be used by Win32 file streaming interfaces, such as ReadFile() and WriteFile(), to access and update the file by way of the file system.
Because file operations are transactional, you can't delete or rename FILESTREAM files through the file system.
The FILESTREAM container is a folder managed by SQL Server. Don't add or remove files in the FILESTREAM folder manually or through other applications. If you do, this will result in backup and inconsistency errors. For more information, see [MSSQLSERVER_3056](https://learn.microsoft.com/en-us/sql/relational-databases/errors-events/mssqlserver-3056-database-engine-error?view=sql-server-ver17), [MSSQLSERVER_7908](https://learn.microsoft.com/en-us/sql/relational-databases/errors-events/mssqlserver-7908-database-engine-error?view=sql-server-ver17), and [MSSQLSERVER_7906](https://learn.microsoft.com/en-us/sql/relational-databases/errors-events/mssqlserver-7906-database-engine-error?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/relational-databases/blob/filestream-sql-server?view=sql-server-ver17#statement-model)
#### Statement model
The FILESTREAM file system access models a Transact-SQL statement by using file open and close. The statement starts when a file handle is opened and ends when the handle is closed. For example, when a write handle is closed, any possible `AFTER` trigger that is registered on the table, fires as if an `UPDATE` statement is completed.
[](https://learn.microsoft.com/en-us/sql/relational-databases/blob/filestream-sql-server?view=sql-server-ver17#storage-namespace)
#### Storage namespace
In FILESTREAM, the Database Engine controls the BLOB physical file system namespace. A new intrinsic function, [PathName](https://learn.microsoft.com/en-us/sql/relational-databases/system-functions/pathname-transact-sql?view=sql-server-ver17), provides the logical UNC path of the BLOB that corresponds to each FILESTREAM cell in the table. The application uses this logical path to obtain the Win32 handle and operate on the BLOB data by using regular Win32 file system interfaces. The function returns `NULL` if the value of the FILESTREAM column is `NULL`.
[](https://learn.microsoft.com/en-us/sql/relational-databases/blob/filestream-sql-server?view=sql-server-ver17#transacted-file-system-access)
#### Transacted file system access
A new intrinsic function, [GET_FILESTREAM_TRANSACTION_CONTEXT](https://learn.microsoft.com/en-us/sql/t-sql/functions/get-filestream-transaction-context-transact-sql?view=sql-server-ver17), provides the token that represents the current transaction that the session is associated with. The transaction must have been started and not yet aborted or committed. By obtaining a token, the application binds the FILESTREAM file system streaming operations with a started transaction. The function returns `NULL` in case of no explicitly started transaction.
All file handles must be closed before the transaction commits or aborts. If a handle is left open beyond the transaction scope, additional reads against the handle cause a failure; additional writes against the handle succeed, but the actual data isn't be written to disk. Similarly, if the database or instance of the Database Engine shuts down, all open handles are invalidated.
[](https://learn.microsoft.com/en-us/sql/relational-databases/blob/filestream-sql-server?view=sql-server-ver17#transactional-durability)
#### Transactional durability
With FILESTREAM, upon transaction commit, the Database Engine ensures transaction durability for FILESTREAM BLOB data that is modified from the file system streaming access.
[](https://learn.microsoft.com/en-us/sql/relational-databases/blob/filestream-sql-server?view=sql-server-ver17#isolation-semantics)
#### Isolation semantics
The isolation semantics are governed by Database Engine transaction isolation levels. Read-committed isolation level is supported for Transact-SQL and file system access. Repeatable read operations, serializable, and snapshot isolation levels are supported. Dirty read isn't supported.
The file system access open operations don't wait for any locks. Instead, the open operations fail immediately if they can't access the data because of transaction isolation. The streaming API calls fail with ERROR_SHARING_VIOLATION if the open operation can't continue because of isolation violation.
To allow for partial updates to be made, the application can issue a device FS control (FSCTL_SQL_FILESTREAM_FETCH_OLD_CONTENT) to fetch the old content into the file that the opened handle references. This triggers a server-side old content copy. For better application performance and to avoid running into potential time-outs when you work with very large files, we recommend that you use asynchronous I/O.
If the FSCTL is issued after the handle has been written to, the last write operation will persist, and prior writes that were made to the handle are lost.
[](https://learn.microsoft.com/en-us/sql/relational-databases/blob/filestream-sql-server?view=sql-server-ver17#file-system-apis-and-supported-isolation-levels)
#### File system APIs and supported isolation levels
When a file system API can't open a file because of an isolation violation, an ERROR_SHARING_VIOLATION exception is returned. This isolation violation occurs when two transactions try to access the same file. The outcome of the access operation depends on the mode the file was opened in and the version of SQL Server that the transaction is running on. The following table outlines the possible outcomes for two transactions that are accessing the same file.
Expand table
Transaction 1 | Transaction 2 | Outcome on SQL Server 2008 (10.0.x) | Outcome on SQL Server 2008 R2 (10.50.x) and later versions
---|---|---|---
Open for read. | Open for read. | Both succeed. | Both succeed.
Open for read. | Open for write. | Both succeed. Write operations under transaction 2 don't affect read operations performed in transaction 1. | Both succeed. Write operations under transaction 2 don't affect read operations performed in transaction 1.
Open for write. | Open for read. | Open for transaction 2 fails with an ERROR_SHARING_VIOLATION exception. | Both succeed.
Open for write. | Open for write. | Open for transaction 2 fails with an ERROR_SHARING_VIOLATION exception. | Open for transaction 2 fails with an ERROR_SHARING_VIOLATION exception.
Open for read. | Open for `SELECT`. | Both succeed. | Both succeed.
Open for read. | Open for `UPDATE` or `DELETE`. | Both succeed. Write operations under transaction 2 don't affect read operations performed in transaction 1. | Both succeed. Write operations under transaction 2 don't affect read operations performed in transaction 1.
Open for write. | open for `SELECT`. | Transaction 2 blocks until transaction 1 commits or ends the transaction, or the transaction lock times out. | Both succeed.
Open for write. | Open for `UPDATE` or `DELETE`. | Transaction 2 blocks until transaction 1 commits or ends the transaction, or the transaction lock times out. | Transaction 2 blocks until transaction 1 commits or ends the transaction, or the transaction lock times out.
Open for `SELECT`. | Open for read. | Both succeed. | Both succeed.
Open for `SELECT`. | Open for write. | Both succeed. Write operations under transaction 2 don't affect transaction 1. | Both succeed. Write operations under transaction 2 don't affect transaction 1.
Open for `UPDATE` or `DELETE`. | Open for read. | The open operation on transaction 2 fails with an ERROR_SHARING_VIOLATION exception. | Both succeed.
Open for `UPDATE` or `DELETE`. | Open for write. | The open operation on transaction 2 fails with an ERROR_SHARING_VIOLATION exception. | The open operation on transaction 2 fails with an ERROR_SHARING_VIOLATION exception.
Open for `SELECT` with repeatable read. | Open for read. | Both succeed. | Both succeed.
Open for `SELECT` with repeatable read. | Open for write. | The open operation on transaction 2 fails with an ERROR_SHARING_VIOLATION exception. | The open operation on transaction 2 fails with an ERROR_SHARING_VIOLATION exception.
[](https://learn.microsoft.com/en-us/sql/relational-databases/blob/filestream-sql-server?view=sql-server-ver17#write-through-from-remote-clients)
#### Write-through from remote clients
Remote file system access to FILESTREAM data is enabled over the Server Message Block (SMB) protocol. If the client is remote, no write operations are cached by the client side. The write operations will always be sent to the server. The data can be cached on the server side. We recommend that applications that are running on remote clients consolidate small write operations into larger size operations. The goal is to perform fewer writes.
Creating memory mapped views (memory mapped I/O) by using a FILESTREAM handle isn't supported. If memory mapping is used for FILESTREAM data, the Database Engine can't guarantee consistency and durability of the data or the integrity of the database.
[](https://learn.microsoft.com/en-us/sql/relational-databases/blob/filestream-sql-server?view=sql-server-ver17#recommendations-and-guidelines-for-improving-filestream-performance)
## Recommendations and guidelines for improving FILESTREAM performance
The SQL Server FILESTREAM feature allows you to store varbinary(max) binary large object data as files in the file system. When you have a large number of rows in FILESTREAM containers, which are the underlying storage for both FILESTREAM columns and FileTables, you can end up with a file system volume that contains large number of files. To achieve best performance when processing the integrated data from the database and the file system, it's important to ensure the file system is tuned optimally. The following are some of the tuning options that are available from a file system perspective:
  * Altitude check for the SQL Server FILESTREAM filter driver (for example, `rsfx0100.sys`). Evaluate all the filter drivers loaded for the storage stack associated with a volume where the FILESTREAM feature stores files and make sure that rsfx driver is located at the bottom of the stack. You can use the FLTMC.EXE control program to enumerate the filter drivers for a specific volume. Here's a sample output from the FLTMC utility: `C:\Windows\System32>fltMC.exe` filters
Expand table
Filter Name | Num Instances | Altitude | Frame
---|---|---|---
Sftredir | 1 | 406000 | 0
MpFilter | 9 | 328000 | 0
luafv | 1 | 135000 | 0
FileInfo | 9 | 45000 | 0
RsFx0103 | 1 | 41001.03 | 0
  * Check that the server has the "last access time" property disabled for the files. This file system attribute is maintained in the registry: Key Name: `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem` Name: NtfsDisableLastAccessUpdate Type: REG_DWORD Value: 1
  * Check that the server has 8.3 naming disabled. This file system attribute is maintained in the registry: Key Name: `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem` Name: NtfsDisable8dot3NameCreation Type: REG_DWORD Value: 1
  * Check that the FILESTREAM directory containers don't have file system encryption or file system compression enabled, as these can introduce a level of overhead when accessing these files.
  * From an elevated command prompt, run fltmc instances and make sure that no filter drivers are attached to the volume where you try to restore.
  * Check that FILESTREAM directory containers don't have more than 300,000 files. You can use the information from `sys.database_files` catalog view to find out which directories in the file system store `FILESTREAM-related` files. This can be prevented by having multiple containers. (See the next bullet item for more information.)
  * With only one FILESTREAM filegroup, all data files are created under the same folder. File creation of very large numbers of files might be affected by large NTFS indices, which can also become fragmented.
    * Having multiple filegroups generally should help with this (the application uses partitioning or has multiple tables, each going to its own filegroup).
    * With SQL Server 2012 (11.x) and later versions, you can have multiple containers or files under a FILESTREAM filegroup, and a round-robin allocation scheme will apply. Therefore the number of NTFS files per directory gets smaller.
  * Backup and restore can become faster with multiple FILESTREAM containers, if multiple volumes storing containers are used.
SQL Server 2012 (11.x) supports multiple containers per filegroup and can make things easier. No complicated partitioning schemes might be needed to manage larger number of files.
  * When there are a very large number of FILESTREAM containers in a SQL instance, starting the databases with many FILESTREAM containers might take a long time to register them in the FILESTREAM filter driver. Spreading them in multiple different volumes helps with improving database startup time.
  * The NTFS MFT might become fragmented, and that can cause performance issues. The MFT reserved size does depend on volume size, so you might or might not encounter this.
    * You can check the MFT fragmentation with `defrag /A /V C:` (change C: to the actual volume name).
    * You can reserve more MFT space by using fsutil behavior set mftzone 2.
    * FILESTREAM data files should be excluded from antivirus software scanning.
Windows Server 2016 automatically enables Windows Defender. Make sure that Windows Defender is configured to exclude Filestream files. Failure to do this can result in decreased performance for backup and restore operations.
For more information, see [Configure and validate exclusions for Windows Defender Antivirus scans](https://learn.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-antivirus/configure-exclusions-microsoft-defender-antivirus).


[](https://learn.microsoft.com/en-us/sql/relational-databases/blob/filestream-sql-server?view=sql-server-ver17#related-tasks)
## Related tasks
  * [Enable and configure FILESTREAM](https://learn.microsoft.com/en-us/sql/relational-databases/blob/enable-and-configure-filestream?view=sql-server-ver17)
  * [Create a FILESTREAM-Enabled Database](https://learn.microsoft.com/en-us/sql/relational-databases/blob/create-a-filestream-enabled-database?view=sql-server-ver17)
  * [Create a Table for Storing FILESTREAM Data](https://learn.microsoft.com/en-us/sql/relational-databases/blob/create-a-table-for-storing-filestream-data?view=sql-server-ver17)
  * [Access FILESTREAM data with Transact-SQL](https://learn.microsoft.com/en-us/sql/relational-databases/blob/access-filestream-data-with-transact-sql?view=sql-server-ver17)
  * [Create Client Applications for FILESTREAM Data](https://learn.microsoft.com/en-us/sql/relational-databases/blob/create-client-applications-for-filestream-data?view=sql-server-ver17)
  * [Access FILESTREAM Data with OpenSqlFilestream](https://learn.microsoft.com/en-us/sql/relational-databases/blob/access-filestream-data-with-opensqlfilestream?view=sql-server-ver17)
  * [Make Partial Updates to FILESTREAM Data](https://learn.microsoft.com/en-us/sql/relational-databases/blob/make-partial-updates-to-filestream-data?view=sql-server-ver17)
  * [Avoid conflicts with database operations in FILESTREAM applications](https://learn.microsoft.com/en-us/sql/relational-databases/blob/avoid-conflicts-with-database-operations-in-filestream-applications?view=sql-server-ver17)
  * [Move a FILESTREAM-enabled database](https://learn.microsoft.com/en-us/sql/relational-databases/blob/move-a-filestream-enabled-database?view=sql-server-ver17)
  * [Set Up FILESTREAM on a Failover Cluster](https://learn.microsoft.com/en-us/sql/relational-databases/blob/set-up-filestream-on-a-failover-cluster?view=sql-server-ver17)
  * [Configure a Firewall for FILESTREAM Access](https://learn.microsoft.com/en-us/sql/relational-databases/blob/configure-a-firewall-for-filestream-access?view=sql-server-ver17)


[](https://learn.microsoft.com/en-us/sql/relational-databases/blob/filestream-sql-server?view=sql-server-ver17#related-content)
## Related content
  * [FILESTREAM compatibility with other SQL Server features](https://learn.microsoft.com/en-us/sql/relational-databases/blob/filestream-compatibility-with-other-sql-server-features?view=sql-server-ver17)
  * [FILESTREAM and FileTable dynamic management views (Transact-SQL)](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/filestream-and-filetable-dynamic-management-views-transact-sql?view=sql-server-ver17)
  * [FILESTREAM and FileTable catalog views (Transact-SQL)](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/filestream-and-filetable-catalog-views-transact-sql?view=sql-server-ver17)
  * [FILESTREAM and FileTable system stored procedures (Transact-SQL)](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/filestream-and-filetable-system-stored-procedures?view=sql-server-ver17)


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
  * [ Access FILESTREAM data with Transact-SQL - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/blob/access-filestream-data-with-transact-sql?source=recommendations)
Learn how to use the Transact-SQL INSERT, UPDATE, and DELETE statements to access and manage FILESTREAM data.
  * [ Create a FILESTREAM-Enabled Database - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/blob/create-a-filestream-enabled-database?source=recommendations)
Configure a database to support FILESTREAM by using the CONTAINS FILESTREAM clause when you create or alter the database.
  * [ Enable and configure FILESTREAM - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/blob/enable-and-configure-filestream?source=recommendations)
To use FILESTREAM, first enable it on the SQL Server Database Engine instance. Learn how to enable FILESTREAM by using SQL Server Configuration Manager.
  * [ Create a Table for Storing FILESTREAM Data - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/blob/create-a-table-for-storing-filestream-data?source=recommendations)
Learn how to create a table for storing FILESTREAM data in SQL Server. See which columns and attributes to use in the Transact-SQL code.
  * [ FILESTREAM compatibility - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/blob/filestream-compatibility-with-other-sql-server-features?source=recommendations)
FILESTREAM stores data in the file system. Read about guidelines, limitations, and tips to keep in mind when using FILESTREAM with various SQL Server features.
  * [ FileTables (SQL Server) - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/blob/filetables-sql-server?source=recommendations)
Explore the benefits and functionality of FileTables, the SQL Server feature that uses a directory structure to store files. Learn how to work with FileTables.
  * [ Server Configuration: filestream access level - SQL Server ](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/filestream-access-level-server-configuration-option?source=recommendations)
Become familiar with the filestream_access_level option. See how it changes the FILESTREAM access level for an instance of SQL Server.
  * [ Access FILESTREAM Data with OpenSqlFilestream - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/blob/access-filestream-data-with-opensqlfilestream?source=recommendations)
Find out how to access FILESTREAM data with OpenSqlFilestream. View examples demonstrating how to use this API to obtain a Win32 handle.


Show 5 more
Module
[ Implement a hybrid file server infrastructure - Training ](https://learn.microsoft.com/en-us/training/modules/implement-hybrid-file-server-infrastructure/?source=recommendations)
Implement a hybrid file server infrastructure using Azure Files and Azure File Sync, and migrate SMB file servers to Azure.
Certification
[ Microsoft Certified: Azure Database Administrator Associate - Certifications ](https://learn.microsoft.com/en-us/credentials/certifications/azure-database-administrator-associate/?source=recommendations)
Administer an SQL Server database infrastructure for cloud, on-premises and hybrid relational databases using the Microsoft PaaS relational database offerings.
Mar 8, 4 PM - Mar 8, 4 PM
Experiment with what's next in AI-driven apps and agent design
* * *
  * Last updated on 09/03/2025


##  In this article
  1. [When to Use FILESTREAM](https://learn.microsoft.com/en-us/sql/relational-databases/blob/filestream-sql-server?view=sql-server-ver17#when-to-use-filestream)
  2. [FILESTREAM Storage](https://learn.microsoft.com/en-us/sql/relational-databases/blob/filestream-sql-server?view=sql-server-ver17#filestream-storage)
  3. [Access BLOB Data with Transact-SQL and File System Streaming Access](https://learn.microsoft.com/en-us/sql/relational-databases/blob/filestream-sql-server?view=sql-server-ver17#access-blob-data-with-transact-sql-and-file-system-streaming-access)
  4. [Recommendations and guidelines for improving FILESTREAM performance](https://learn.microsoft.com/en-us/sql/relational-databases/blob/filestream-sql-server?view=sql-server-ver17#recommendations-and-guidelines-for-improving-filestream-performance)
  5. [Related tasks](https://learn.microsoft.com/en-us/sql/relational-databases/blob/filestream-sql-server?view=sql-server-ver17#related-tasks)
  6. [Related content](https://learn.microsoft.com/en-us/sql/relational-databases/blob/filestream-sql-server?view=sql-server-ver17#related-content)


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
[ Sign in ](https://learn.microsoft.com/en-us/sql/relational-databases/blob/filestream-sql-server?view=sql-server-ver17)
[English (United States)](https://learn.microsoft.com/en-us/locale?target=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fsql%2Frelational-databases%2Fblob%2Ffilestream-sql-server%3Fview%3Dsql-server-ver17)
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
