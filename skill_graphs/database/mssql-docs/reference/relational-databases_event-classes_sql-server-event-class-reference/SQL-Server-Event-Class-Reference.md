# SQL Server Event Class Reference
Feedback
Summarize this article for me
##  In this article
**Applies to:** ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure SQL Database](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure SQL Managed Instance](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL database in Microsoft Fabric](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to)
SQL Server Profiler lets you record events as they occur in an instance of the Microsoft SQL Server Database Engine. The recorded events are instances of the event classes in the trace definition. In SQL Server Profiler, event classes and their event categories are available on the **Events Selection** tab of the **Trace File Properties** dialog box.
The following table describes the event categories and lists their associated event classes.
Expand table
Event Category | Event Classes
---|---
The [Broker Event Category](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/broker-event-category?view=sql-server-ver17) includes event classes that are produced by the Service Broker. |  [Broker:Activation Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/broker-activation-event-class?view=sql-server-ver17)

[Broker:Connection Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/broker-connection-event-class?view=sql-server-ver17)

[Broker:Conversation Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/broker-conversation-event-class?view=sql-server-ver17)

[Broker:Conversation Group Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/broker-conversation-group-event-class?view=sql-server-ver17)

[Broker:Corrupted Message Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/broker-corrupted-message-event-class?view=sql-server-ver17)

[Broker:Forwarded Message Dropped Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/broker-forwarded-message-dropped-event-class?view=sql-server-ver17)

[Broker:Forwarded Message Sent Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/broker-forwarded-message-sent-event-class?view=sql-server-ver17)

[Broker:Message Classify Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/broker-message-classify-event-class?view=sql-server-ver17)

[Broker:Message Drop Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/broker-message-drop-event-class?view=sql-server-ver17)

[Broker:Remote Message Ack Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/broker-remote-message-ack-event-class?view=sql-server-ver17)
The [Cursors Event Category](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/cursors-event-category?view=sql-server-ver17) includes event classes that are produced by cursor operations. |  [CursorClose Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/cursorclose-event-class?view=sql-server-ver17)

[CursorExecute Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/cursorexecute-event-class?view=sql-server-ver17)

[CursorImplicitConversion Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/cursorimplicitconversion-event-class?view=sql-server-ver17)

[CursorOpen Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/cursoropen-event-class?view=sql-server-ver17)

[CursorPrepare Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/cursorprepare-event-class?view=sql-server-ver17)

[CursorRecompile Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/cursorrecompile-event-class?view=sql-server-ver17)

[CursorUnprepare Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/cursorunprepare-event-class?view=sql-server-ver17)
The [CLR Event Category](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/clr-event-category?view=sql-server-ver17) includes event classes that are produced by the execution of .NET common language runtime (CLR) objects. | [Assembly Load Event Class](https://learn.microsoft.com/en-us/dotnet/api/system.appdomain.assemblyload)
The [Database Event Category](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/database-event-category?view=sql-server-ver17) includes event classes that are produced when data or log files grow or shrink automatically. |  [Data File Auto Grow Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/data-file-auto-grow-event-class?view=sql-server-ver17)

[Data File Auto Shrink Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/data-file-auto-shrink-event-class?view=sql-server-ver17)

[Database Mirroring State Change Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/database-mirroring-state-change-event-class?view=sql-server-ver17)

[Log File Auto Grow Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/log-file-auto-grow-event-class?view=sql-server-ver17)

[Log File Auto Shrink Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/log-file-auto-shrink-event-class?view=sql-server-ver17)
The [Deprecation Event Category](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/deprecation-event-category?view=sql-server-ver17) includes deprecation related events. |  [Deprecation Announcement Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/deprecation-announcement-event-class?view=sql-server-ver17)

[Deprecation Final Support Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/deprecation-final-support-event-class?view=sql-server-ver17)
The [Errors and Warnings Event Category (Database Engine)](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/errors-and-warnings-event-category-database-engine?view=sql-server-ver17) includes event classes that are produced when a SQL Server error or warning is returned, for example, if an error occurs during the compilation of a stored procedure or an exception occurs in SQL Server. |  [Attention Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/attention-event-class?view=sql-server-ver17)

[Background Job Error Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/background-job-error-event-class?view=sql-server-ver17)

[Blocked Process Report Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/blocked-process-report-event-class?view=sql-server-ver17)

[CPU Threshold Exceeded Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/cpu-threshold-exceeded-event-class?view=sql-server-ver17)

[ErrorLog Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/errorlog-event-class?view=sql-server-ver17)

[EventLog Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/eventlog-event-class?view=sql-server-ver17)

[Exception Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/exception-event-class?view=sql-server-ver17)

[Exchange Spill Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/exchange-spill-event-class?view=sql-server-ver17)

[Execution Warnings Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/execution-warnings-event-class?view=sql-server-ver17)

[Hash Warning Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/hash-warning-event-class?view=sql-server-ver17)

[Missing Column Statistics Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/missing-column-statistics-event-class?view=sql-server-ver17)

[Missing Join Predicate Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/missing-join-predicate-event-class?view=sql-server-ver17)

[Sort Warnings Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/sort-warnings-event-class?view=sql-server-ver17)

[User Error Message Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/user-error-message-event-class?view=sql-server-ver17)
The [Full Text Event Category](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/full-text-event-category?view=sql-server-ver17) includes event classes that are produced when full-text searches are started, interrupted, or stopped. |  [FT:Crawl Aborted Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/ft-crawl-aborted-event-class?view=sql-server-ver17)

[FT:Crawl Started Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/ft-crawl-started-event-class?view=sql-server-ver17)

[FT:Crawl Stopped Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/ft-crawl-stopped-event-class?view=sql-server-ver17)
The [Locks Event Category](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/locks-event-category?view=sql-server-ver17) includes event classes that are produced when a lock is acquired, cancelled, released, or has some other action performed on it. |  [Deadlock Graph Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/deadlock-graph-event-class?view=sql-server-ver17)

[Lock:Acquired Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/lock-acquired-event-class?view=sql-server-ver17)

[Lock:Cancel Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/lock-cancel-event-class?view=sql-server-ver17)

[Lock:Deadlock Chain Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/lock-deadlock-chain-event-class?view=sql-server-ver17)

[Lock:Deadlock Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/lock-deadlock-event-class?view=sql-server-ver17)

[Lock:Escalation Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/lock-escalation-event-class?view=sql-server-ver17)

[Lock:Released Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/lock-released-event-class?view=sql-server-ver17)

[Lock:Timeout (timeout > 0) Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/lock-timeout-timeout-0-event-class?view=sql-server-ver17)

[Lock:Timeout Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/lock-timeout-event-class?view=sql-server-ver17)
The [Objects Event Category](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/objects-event-category?view=sql-server-ver17) includes event classes that are produced when database objects are created, opened, closed, dropped, or deleted. |  [Auto Stats Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/auto-stats-event-class?view=sql-server-ver17)

[Object:Altered Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/object-altered-event-class?view=sql-server-ver17)

[Object:Created Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/object-created-event-class?view=sql-server-ver17)

[Object:Deleted Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/object-deleted-event-class?view=sql-server-ver17)
The [OLEDB Event Category](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/oledb-event-category?view=sql-server-ver17) includes event classes that are produced by OLE DB calls. |  [OLEDB Call Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/oledb-call-event-class?view=sql-server-ver17)

[OLEDB DataRead Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/oledb-dataread-event-class?view=sql-server-ver17)

[OLEDB Errors Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/oledb-errors-event-class?view=sql-server-ver17)

[OLEDB Provider Information Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/oledb-provider-information-event-class?view=sql-server-ver17)

[OLEDB QueryInterface Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/oledb-queryinterface-event-class?view=sql-server-ver17)
The [Performance Event Category](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/performance-event-category?view=sql-server-ver17) includes event classes that are produced when SQL data manipulation language (DML) operators execute. |  [Degree of Parallelism (7.0 Insert) Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/degree-of-parallelism-7-0-insert-event-class?view=sql-server-ver17)

[Performance Statistics Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/performance-statistics-event-class?view=sql-server-ver17)

[Showplan All Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/showplan-all-event-class?view=sql-server-ver17)

[Showplan All for Query Compile Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/showplan-all-for-query-compile-event-class?view=sql-server-ver17)

[Showplan Statistics Profile Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/showplan-statistics-profile-event-class?view=sql-server-ver17)

[Showplan Text Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/showplan-text-event-class?view=sql-server-ver17)

[Showplan Text (Unencoded) Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/showplan-text-unencoded-event-class?view=sql-server-ver17)

[Showplan XML Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/showplan-xml-event-class?view=sql-server-ver17)

[Showplan XML for Query Compile Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/showplan-xml-for-query-compile-event-class?view=sql-server-ver17)

[Showplan XML Statistics Profile Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/showplan-xml-statistics-profile-event-class?view=sql-server-ver17)

[SQL:FullTextQuery Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/sql-fulltextquery-event-class?view=sql-server-ver17)
The [Progress Report Event Category](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/progress-report-event-category?view=sql-server-ver17) includes the **Progress Report: Online Index Operation** event class. | [Progress Report: Online Index Operation Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/progress-report-online-index-operation-event-class?view=sql-server-ver17)
The [Scans Event Category](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/scans-event-category?view=sql-server-ver17) includes event classes that are produced when tables and indexes are scanned. |  [Scan:Started Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/scan-started-event-class?view=sql-server-ver17)

[Scan:Stopped Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/scan-stopped-event-class?view=sql-server-ver17)
The [Security Audit Event Category](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/security-audit-event-category-sql-server-profiler?view=sql-server-ver17) includes event classes that are used to audit server activity. |  [Audit Add DB User Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/audit-add-db-user-event-class?view=sql-server-ver17)

[Audit Add Login to Server Role Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/audit-add-login-to-server-role-event-class?view=sql-server-ver17)

[Audit Add Member to DB Role Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/audit-add-member-to-db-role-event-class?view=sql-server-ver17)

[Audit Add Role Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/audit-add-role-event-class?view=sql-server-ver17)

[Audit Addlogin Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/audit-addlogin-event-class?view=sql-server-ver17)

[Audit App Role Change Password Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/audit-app-role-change-password-event-class?view=sql-server-ver17)

[Audit Backup and Restore Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/audit-backup-and-restore-event-class?view=sql-server-ver17)

[Audit Broker Conversation Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/audit-broker-conversation-event-class?view=sql-server-ver17)

[Audit Broker Login Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/audit-broker-login-event-class?view=sql-server-ver17)

[Audit Change Audit Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/audit-change-audit-event-class?view=sql-server-ver17)

[Audit Change Database Owner Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/audit-change-database-owner-event-class?view=sql-server-ver17)

[Audit Database Management Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/audit-database-management-event-class?view=sql-server-ver17)

[Audit Database Object Access Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/audit-database-object-access-event-class?view=sql-server-ver17)

[Audit Database Object GDR Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/audit-database-object-gdr-event-class?view=sql-server-ver17)

[Audit Database Object Management Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/audit-database-object-management-event-class?view=sql-server-ver17)

[Audit Database Object Take Ownership Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/audit-database-object-take-ownership-event-class?view=sql-server-ver17)

[Audit Database Operation Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/audit-database-operation-event-class?view=sql-server-ver17)

[Audit Database Principal Impersonation Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/audit-database-principal-impersonation-event-class?view=sql-server-ver17)

[Audit Database Principal Management Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/audit-database-principal-management-event-class?view=sql-server-ver17)

[Audit Database Scope GDR Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/audit-database-scope-gdr-event-class?view=sql-server-ver17)

[Audit DBCC Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/audit-dbcc-event-class?view=sql-server-ver17)

[Audit Login Change Password Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/audit-login-change-password-event-class?view=sql-server-ver17)

[Audit Login Change Property Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/audit-login-change-property-event-class?view=sql-server-ver17)

[Audit Login Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/audit-login-event-class?view=sql-server-ver17)

[Audit Login Failed Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/audit-login-failed-event-class?view=sql-server-ver17)

[Audit Login GDR Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/audit-login-gdr-event-class?view=sql-server-ver17)

[Audit Logout Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/audit-logout-event-class?view=sql-server-ver17)

[Audit Object Derived Permission Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/audit-object-derived-permission-event-class?view=sql-server-ver17)

[Audit Schema Object Access Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/audit-schema-object-access-event-class?view=sql-server-ver17)

[Audit Schema Object GDR Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/audit-schema-object-gdr-event-class?view=sql-server-ver17)

[Audit Schema Object Management Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/audit-schema-object-management-event-class?view=sql-server-ver17)

[Audit Schema Object Take Ownership Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/audit-schema-object-take-ownership-event-class?view=sql-server-ver17)

[Audit Server Alter Trace Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/audit-server-alter-trace-event-class?view=sql-server-ver17)

[Audit Server Object GDR Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/audit-server-object-gdr-event-class?view=sql-server-ver17)

[Audit Server Object Management Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/audit-server-object-management-event-class?view=sql-server-ver17)

[Audit Server Object Take Ownership Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/audit-server-object-take-ownership-event-class?view=sql-server-ver17)

[Audit Server Operation Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/audit-server-operation-event-class?view=sql-server-ver17)

[Audit Server Principal Impersonation Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/audit-server-principal-impersonation-event-class?view=sql-server-ver17)

[Audit Server Principal Management Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/audit-server-principal-management-event-class?view=sql-server-ver17)

[Audit Server Scope GDR Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/audit-server-scope-gdr-event-class?view=sql-server-ver17)

[Audit Server Starts and Stops Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/audit-server-starts-and-stops-event-class?view=sql-server-ver17)

[Audit Statement Permission Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/audit-statement-permission-event-class?view=sql-server-ver17)
The [Server Event Category](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/server-event-category?view=sql-server-ver17) contains general server events. |  [Mount Tape Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/mount-tape-event-class?view=sql-server-ver17)

[Server Memory Change Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/server-memory-change-event-class?view=sql-server-ver17)

[Trace File Close Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/trace-file-close-event-class?view=sql-server-ver17)
The [Sessions Event Category](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/sessions-event-category?view=sql-server-ver17) includes event classes produced by clients connecting to and disconnecting from an instance of SQL Server. | [ExistingConnection Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/existingconnection-event-class?view=sql-server-ver17)
The [Stored Procedures Event Category](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/stored-procedures-event-category?view=sql-server-ver17) includes event classes produced by the execution of stored procedures. |  [PreConnect:Completed Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/preconnect-completed-event-class?view=sql-server-ver17)

[PreConnect:Starting Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/preconnect-starting-event-class?view=sql-server-ver17)

[RPC:Completed Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/rpc-completed-event-class?view=sql-server-ver17)

[RPC Output Parameter Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/rpc-output-parameter-event-class?view=sql-server-ver17)

[RPC:Starting Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/rpc-starting-event-class?view=sql-server-ver17)

[SP:CacheHit Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/sp-cachehit-event-class?view=sql-server-ver17)

[SP:CacheInsert Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/sp-cacheinsert-event-class?view=sql-server-ver17)

[SP:CacheMiss Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/sp-cachemiss-event-class?view=sql-server-ver17)

[SP:CacheRemove Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/sp-cacheremove-event-class?view=sql-server-ver17)

[SP:Completed Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/sp-completed-event-class?view=sql-server-ver17)

[SP:Recompile Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/sp-recompile-event-class?view=sql-server-ver17)

[SP:Starting Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/sp-starting-event-class?view=sql-server-ver17)

[SP:StmtCompleted Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/sp-stmtcompleted-event-class?view=sql-server-ver17)

[SP:StmtStarting Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/sp-stmtstarting-event-class?view=sql-server-ver17)
The [Transactions Event Category](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/transactions-event-category?view=sql-server-ver17) includes event classes produced by the execution of Microsoft Distributed Transaction Coordinator transactions or by writing to the transaction log. |  [DTCTransaction Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/dtctransaction-event-class?view=sql-server-ver17)

[SQLTransaction Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/sqltransaction-event-class?view=sql-server-ver17)

[TM: Begin Tran Completed Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/tm-begin-tran-completed-event-class?view=sql-server-ver17)

[TM: Begin Tran Starting Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/tm-begin-tran-starting-event-class?view=sql-server-ver17)

[TM: Commit Tran Completed Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/tm-commit-tran-completed-event-class?view=sql-server-ver17)

[TM: Commit Tran Starting Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/tm-commit-tran-starting-event-class?view=sql-server-ver17)

[TM: Promote Tran Completed Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/tm-promote-tran-completed-event-class?view=sql-server-ver17)

[TM: Promote Tran Starting Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/tm-promote-tran-starting-event-class?view=sql-server-ver17)

[TM: Rollback Tran Completed Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/tm-rollback-tran-completed-event-class?view=sql-server-ver17)

[TM: Rollback Tran Starting Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/tm-rollback-tran-starting-event-class?view=sql-server-ver17)

[TM: Save Tran Completed Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/tm-save-tran-completed-event-class?view=sql-server-ver17)

[TM: Save Tran Starting Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/tm-save-tran-starting-event-class?view=sql-server-ver17)

[TransactionLog Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/transactionlog-event-class?view=sql-server-ver17)
The [TSQL Event Category](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/tsql-event-category?view=sql-server-ver17) includes event classes produced by the execution of Transact-SQL statements passed to an instance of SQL Server from the client. |  [Exec Prepared SQL Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/exec-prepared-sql-event-class?view=sql-server-ver17)

[Prepare SQL Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/prepare-sql-event-class?view=sql-server-ver17)

[SQL:BatchCompleted Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/sql-batchcompleted-event-class?view=sql-server-ver17)

[SQL:BatchStarting Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/sql-batchstarting-event-class?view=sql-server-ver17)

[SQL:StmtCompleted Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/sql-stmtcompleted-event-class?view=sql-server-ver17)

[SQL:StmtRecompile Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/sql-stmtrecompile-event-class?view=sql-server-ver17)

[SQL:StmtStarting Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/sql-stmtstarting-event-class?view=sql-server-ver17)

[Unprepare SQL Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/unprepare-sql-event-class?view=sql-server-ver17)

[XQuery Static Type Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/xquery-static-type-event-class?view=sql-server-ver17)
The [User-Configurable Event Category](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/user-configurable-event-category?view=sql-server-ver17) includes event classes that you can define. | [User-Configurable Event Class](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/user-configurable-event-class?view=sql-server-ver17)
[](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/sql-server-event-class-reference?view=sql-server-ver17#see-also)
## See Also
[SQL Server Profiler](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/sql-server-profiler?view=sql-server-ver17)
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
Mar 8, 4 PM - Mar 8, 4 PM
Experiment with what's next in AI-driven apps and agent design
* * *
  * Last updated on 11/18/2025


### In this article
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
[ Sign in ](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/sql-server-event-class-reference?view=sql-server-ver17)
[English (United States)](https://learn.microsoft.com/en-us/locale?target=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fsql%2Frelational-databases%2Fevent-classes%2Fsql-server-event-class-reference%3Fview%3Dsql-server-ver17)
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
