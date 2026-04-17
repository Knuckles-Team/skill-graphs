# Database Mirroring (SQL Server)
Feedback
Summarize this article for me
##  In this article
  1. [Benefits of Database Mirroring](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-sql-server?view=sql-server-ver17#benefits-of-database-mirroring)
  2. [Database Mirroring Terms and Definitions](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-sql-server?view=sql-server-ver17#database-mirroring-terms-and-definitions)
  3. [Overview of Database Mirroring](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-sql-server?view=sql-server-ver17#overview-of-database-mirroring)
  4. [Set Up Database Mirroring Session](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-sql-server?view=sql-server-ver17#set-up-database-mirroring-session)
  5. [Interoperability and Coexistence with Other Database Engine Features](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-sql-server?view=sql-server-ver17#interoperability-and-coexistence-with-other-database-engine-features)
  6. [In this section](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-sql-server?view=sql-server-ver17#in-this-section)
  7. [Related tasks](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-sql-server?view=sql-server-ver17#related-tasks)
  8. [Related content](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-sql-server?view=sql-server-ver17#related-content)

Show 4 more
**Applies to:** ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to)
This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature. For high availability, use Always On availability groups instead.
Database Mirroring in SQL Server is a distinct technology from [Microsoft Fabric Database Mirroring](https://learn.microsoft.com/en-us/fabric/database/mirrored-database/overview). Mirroring to Fabric provides better analytical performance, the ability to unify your data estate with OneLake in Fabric, and open access to your data in Delta Parquet format.
With Mirroring to Microsoft Fabric, you can continuously replicate your existing data estate directly into OneLake in Fabric, including data from SQL Server 2016+, Azure SQL Database, Azure SQL Managed Instance, Cosmos DB, Oracle, Snowflake, and more.
_Database mirroring_ is a solution for increasing the availability of a SQL Server database. Mirroring is implemented on a per-database basis and works only with databases that use the full recovery model.
For information about support for database mirroring, restrictions, prerequisites, recommendations for configuring partner servers, and recommendations for deploying database mirroring, see [Prerequisites, Restrictions, and Recommendations for Database Mirroring](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/prerequisites-restrictions-and-recommendations-for-database-mirroring?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-sql-server?view=sql-server-ver17#benefits-of-database-mirroring)
## Benefits of Database Mirroring
Database mirroring is a simple strategy that offers the following benefits:
  * Increases availability of a database.
In the event of a disaster, in high-safety mode with automatic failover, failover quickly brings the standby copy of the database online (without data loss). In the other operating modes, the database administrator has the alternative of forcing service (with possible data loss) to the standby copy of the database. For more information, see [Role Switching](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-sql-server?view=sql-server-ver17#RoleSwitching), later in this topic.
  * Increases data protection.
Database mirroring provides complete or almost complete redundancy of the data, depending on whether the operating mode is high-safety or high-performance. For more information, see [Operating Modes](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-sql-server?view=sql-server-ver17#OperatingModes), later in this topic.
A database mirroring partner running on SQL Server 2008 (10.0.x) Enterprise or later versions automatically tries to resolve certain types of errors that prevent reading a data page. The partner that is unable to read a page requests a fresh copy from the other partner. If this request succeeds, the unreadable page is replaced by the copy, which usually resolves the error. For more information, see [Automatic Page Repair (Availability Groups: Database Mirroring)](https://learn.microsoft.com/en-us/sql/sql-server/failover-clusters/automatic-page-repair-availability-groups-database-mirroring?view=sql-server-ver17).
  * Improves the availability of the production database during upgrades.
To minimize downtime for a mirrored database, you can sequentially upgrade the instances of SQL Server that are hosting the failover partners. This will incur the downtime of only a single failover. This form of upgrade is known as a _rolling upgrade_. For more information, see [Upgrading Mirrored Instances](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/upgrading-mirrored-instances?view=sql-server-ver17).


[](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-sql-server?view=sql-server-ver17#database-mirroring-terms-and-definitions)
## Database Mirroring Terms and Definitions
[](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-sql-server?view=sql-server-ver17#automatic-failover)
### Automatic failover
The process by which, when the principal server becomes unavailable, the mirror server to take over the role of principal server and brings its copy of the database online as the principal database.
[](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-sql-server?view=sql-server-ver17#failover-partners)
### Failover partners
The two server instances (the principal server or the mirror server) that act as role-switching partners for a mirrored database.
[](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-sql-server?view=sql-server-ver17#forced-service)
### Forced service
A failover initiated by the database owner upon the failure of the principal server that transfers service to the mirror database while it's in an unknown state.
[](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-sql-server?view=sql-server-ver17#high-performance-mode)
### High-performance mode
The database mirroring session operates asynchronously and uses only the principal server and mirror server. The only form of role switching is forced service (with possible data loss).
[](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-sql-server?view=sql-server-ver17#high-safety-mode)
### High-safety mode
The database mirroring session operates synchronously and, optionally, uses a witness, as well as the principal server and mirror server.
[](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-sql-server?view=sql-server-ver17#manual-failover)
### Manual failover
A failover initiated by the database owner, while the principal server is still running, that transfers service from the principal database to the mirror database while they are in a synchronized state.
[](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-sql-server?view=sql-server-ver17#mirror-database)
### Mirror database
The copy of the database that is typically fully synchronized with the principal database.
[](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-sql-server?view=sql-server-ver17#mirror-server)
### Mirror server
In a database mirroring configuration, the server instance on which the mirror database resides.
[](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-sql-server?view=sql-server-ver17#principal-database)
### Principal database
In database mirroring, a read-write database whose transaction log records are applied to a read-only copy of the database (a mirror database).
[](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-sql-server?view=sql-server-ver17#principal-server)
### Principal server
In database mirroring, the partner whose database is currently the principal database.
[](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-sql-server?view=sql-server-ver17#redo-queue)
### Redo queue
Received transaction log records that are waiting on the disk of a mirror server.
[](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-sql-server?view=sql-server-ver17#role)
### Role
The principal server and mirror server perform complementary principal and mirror roles. Optionally, the role of witness is performed by a third server instance.
[](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-sql-server?view=sql-server-ver17#role-switching)
### Role switching
The taking over of the principal role by the mirror.
[](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-sql-server?view=sql-server-ver17#send-queue)
### Send queue
Unsent transaction log records that have accumulated on the log disk of the principal server.
[](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-sql-server?view=sql-server-ver17#session)
### Session
The relationship that occurs during database mirroring among the principal server, mirror server, and witness server (if present).
After a mirroring session starts or resumes, the process by which log records of the principal database that have accumulated on the principal server are sent to the mirror server, which writes these log records to disk as quickly as possible to catch up with the principal server.
[](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-sql-server?view=sql-server-ver17#transaction-safety)
### Transaction safety
A mirroring-specific database property that determines whether a database mirroring session operates synchronously or asynchronously. There are two safety levels: FULL and `OFF`.
[](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-sql-server?view=sql-server-ver17#witness)
### Witness
For use only with high-safety mode, an optional instance of SQL Server that enables the mirror server to recognize when to initiate an automatic failover. Unlike the two failover partners, the witness doesn't serve the database. Supporting automatic failover is the only role of the witness.
[](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-sql-server?view=sql-server-ver17#overview-of-database-mirroring)
## Overview of Database Mirroring
Database mirroring maintains two copies of a single database that reside on different instances of SQL Server Database Engine. Typically, these instances reside on computers in different locations. When database mirroring starts, one instance initiates a relationship, known as a _database mirroring session_ , with another instance.
One server instance serves the database to clients (the _principal server_). The other instance acts as a hot or warm standby server (the _mirror server_), depending on the configuration and state of the mirroring session. When a database mirroring session is synchronized, database mirroring provides a hot standby server that supports rapid failover without a loss of data from committed transactions. When the session isn't synchronized, the mirror server is typically available as a warm standby server (with possible data loss).
The principal and mirror servers communicate and cooperate as _partners_ in a _database mirroring session_. The two partners perform complementary roles in the session: the _principal role_ and the _mirror role_. At any given time, one partner performs the principal role, and the other partner performs the mirror role. Each partner is described as _owning_ its current role. The partner that owns the principal role is known as the _principal server_ , and its copy of the database is the current principal database. The partner that owns the mirror role is known as the _mirror server_ , and its copy of the database is the current mirror database. When database mirroring is deployed in a production environment, the principal database is the _production database_.
Database mirroring involves _redoing_ every insert, update, and delete operation that occurs on the principal database onto the mirror database as quickly as possible. Redoing is accomplished by sending a stream of active transaction log records to the mirror server, which applies log records to the mirror database, in sequence, as quickly as possible. Unlike replication, which works at the logical level, database mirroring works at the level of the physical log record. Beginning in SQL Server 2008 (10.0.x), the principal server compresses the stream of transaction log records before sending it to the mirror server. This log compression occurs in all mirroring sessions.
A given server instance can participate in multiple concurrent database mirroring sessions with the same or different partners. A server instance can be a partner in some sessions and a witness in other sessions. The mirror server instance must be running the same edition of SQL Server.
**In This Section:**
  * [Operating Modes](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-sql-server?view=sql-server-ver17#OperatingModes)
  * [Role Switching](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-sql-server?view=sql-server-ver17#RoleSwitching)
  * [Concurrent Sessions](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-sql-server?view=sql-server-ver17#ConcurrentSessions)
  * [Client Connections](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-sql-server?view=sql-server-ver17#ClientConnections)
  * [Impact of Pausing a Session on the Principal Transaction Log](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-sql-server?view=sql-server-ver17#ImpactOfPausing)


[](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-sql-server?view=sql-server-ver17#operating-modes)
### Operating Modes
A database mirroring session runs with either synchronous or asynchronous operation. Under asynchronous operation, the transactions commit without waiting for the mirror server to write the log to disk, which maximizes performance. Under synchronous operation, a transaction is committed on both partners, but at the cost of increased transaction latency.
There are two mirroring operating modes. One of them, _high-safety mode_ supports synchronous operation. Under high-safety mode, when a session starts, the mirror server synchronizes the mirror database together with the principal database as quickly as possible. As soon as the databases are synchronized, a transaction is committed on both partners, at the cost of increased transaction latency.
The second operating mode, _high-performance mode_ , runs asynchronously. The mirror server tries to keep up with the log records sent by the principal server. The mirror database might lag somewhat behind the principal database. However, typically, the gap between the databases is small. However, the gap can become significant if the principal server is under a heavy work load or the system of the mirror server is overloaded.
In high-performance mode, as soon as the principal server sends a log record to the mirror server, the principal server sends a confirmation to the client. It doesn't wait for an acknowledgment from the mirror server. This means that transactions commit without waiting for the mirror server to write the log to disk. Such asynchronous operation enables the principal server to run with minimum transaction latency, at the potential risk of some data loss.
All database mirroring sessions support only one principal server and one mirror server. This configuration is shown in the following illustration.
![Screenshot of Partners in a database mirroring session.](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/media/dbm-2-way-session-intro.png?view=sql-server-ver17)
High-safety mode with automatic failover requires a third server instance, known as a _witness_. Unlike the two partners, the witness doesn't serve the database. The witness supports automatic failover by verifying whether the principal server is up and functioning. The mirror server initiates automatic failover only if the mirror and the witness remain connected to each other after both have been disconnected from the principal server.
The following illustration shows a configuration that includes a witness.
![Screenshot of A mirroring session that includes a witness.](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/media/dbm-3-way-session-intro-ov.png?view=sql-server-ver17)
For more information, see [Role Switching](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-sql-server?view=sql-server-ver17#RoleSwitching), later in this topic.
Establishing a new mirroring session or adding a witness to an existing mirroring configuration requires that all involved server instances run the same version of SQL Server. However, when you're upgrading to SQL Server 2008 (10.0.x) or a later version, the versions of the involved instances can vary. For more information, see [Upgrading Mirrored Instances](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/upgrading-mirrored-instances?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-sql-server?view=sql-server-ver17#transaction-safety-and-operating-modes)
#### Transaction Safety and Operating Modes
Whether an operating mode is asynchronous or synchronous depends on the transaction safety setting. If you exclusively use SQL Server Management Studio to configure database mirroring, transaction safety settings are configured automatically when you select the operation mode.
If you use Transact-SQL to configure database mirroring, you must understand how to set transaction safety. Transaction safety is controlled by the `SAFETY` property of the `ALTER DATABASE` statement. On a database that is being mirrored, `SAFETY` is either FULL or `OFF`.
  * If the `SAFETY` option is set to FULL, database mirroring operation is synchronous, after the initial synchronizing phase. If a witness is set in high-safety mode, the session supports automatic failover.
  * If the `SAFETY` option is set to `OFF`, database mirroring operation is asynchronous. The session runs in high-performance mode, and the `WITNESS` option should also be `OFF`.


For more information, see [Database Mirroring Operating Modes](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-operating-modes?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-sql-server?view=sql-server-ver17#role-switching-1)
### Role Switching
Within the context of a database mirroring session, the principal and mirror roles are typically interchangeable in a process known as _role switching_. Role switching involves transferring the principal role to the mirror server. In role switching, the mirror server acts as the _failover partner_ for the principal server. When a role switch occurs, the mirror server takes over the principal role and brings its copy of the database online as the new principal database. The former principal server, if available, assumes the mirror role, and its database becomes the new mirror database. Potentially, the roles can switch back and forth repeatedly.
The following three forms of role switching exist.
  * _Automatic failover_
This requires high-safety mode and the presence of the mirror server and a witness. The database must already be synchronized, and the witness must be connected to the mirror server.
The role of the witness is to verify whether a given partner server is up and functioning. If the mirror server loses its connection to the principal server but the witness is still connected to the principal server, the mirror server doesn't initiate a failover. For more information, see [Database Mirroring Witness](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-witness?view=sql-server-ver17).
  * _Manual failover_
This requires high-safety mode. The partners must be connected to each other, and the database must already be synchronized.
  * _Forced service_ (with possible data loss)
Under high-performance mode and high-safety mode without automatic failover, forcing service is possible if the principal server has failed and the mirror server is available.
High-performance mode is intended to run without a witness. But if a witness exists, forcing service requires that the witness is connected to the mirror server.


In any role-switching scenario, as soon as the new principal database comes online, the client applications can recover quickly by reconnecting to the database.
[](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-sql-server?view=sql-server-ver17#concurrent-sessions)
### Concurrent Sessions
A given server instance can participate in multiple, concurrent database mirroring sessions (once per mirrored database) with the same or different server instances. Often, a server instance serves exclusively as a partner or a witness in all of its database mirroring sessions. However, because each session is independent of the other sessions, a server instance can act as a partner in some sessions and as a witness in other sessions. For example, consider the following four sessions among three server instances (`SSInstance_1`, `SSInstance_2`, and `SSInstance_3`). Each server instance serves as a partner in some sessions and as a witness in others:
Expand table
Server instance | Session for database A | Session for database B | Session for database C | Session for database D
---|---|---|---|---
`SSInstance_1` | Witness | Partner | Partner | Partner
`SSInstance_2` | Partner | Witness | Partner | Partner
`SSInstance_3` | Partner | Partner | Witness | Witness
The following figure illustrates two server instances that are participating as partners together in two mirroring sessions. One session is for a database named **Db_1** , and the other session is for a database named **Db_2**.
![Screenshot of Two server instances in two concurrent sessions.](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/media/dbm-concurrent-sessions.png?view=sql-server-ver17)
Each of the databases is independent of the others. For example, a server instance might initially be the mirror server for two databases. If one of those databases fails over, the server instance becomes the principal server for the failed-over database while remaining the mirror server for the other database.
As another example, consider a server instance that is the principal server for two or more databases running in high-safety mode with automatic failover, If the server instance fails, all of the databases automatically failover to their respective mirror databases.
When setting up a server instance to operate both as a partner and a witness, be sure that the database mirroring endpoint supports both roles (for more information, see [The database mirroring endpoint (SQL Server)](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/the-database-mirroring-endpoint-sql-server?view=sql-server-ver17)). Also, ensure that the system has sufficient resources to reduce resource contention.
Because mirrored databases are independent of each other, databases can't fail over as a group.
[](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-sql-server?view=sql-server-ver17#client-connections)
### Client Connections
Client-connection support for database mirroring sessions is provided by the Microsoft .NET Data Provider for SQL Server. For more information, see [Connect Clients to a Database Mirroring Session (SQL Server)](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/connect-clients-to-a-database-mirroring-session-sql-server?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-sql-server?view=sql-server-ver17#impact-of-pausing-a-session-on-the-principal-transaction-log)
### Impact of Pausing a Session on the Principal Transaction Log
At any time, the database owner can pause a session. Pausing preserves the session state while removing mirroring. When a session is paused, the principal server doesn't send any new log records to the mirror server. All of these records remain active and accumulate in the transaction log of the principal database. As long as a database mirroring session remains paused, the transaction log can't be truncated. Therefore, if the database mirroring session is paused for too long, the log can fill up.
For more information, see [Pausing and Resuming Database Mirroring (SQL Server)](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/pausing-and-resuming-database-mirroring-sql-server?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-sql-server?view=sql-server-ver17#set-up-database-mirroring-session)
## Set Up Database Mirroring Session
Before a mirroring session can begin, the database owner or system administrator must create the mirror database, set up endpoints and logins, and, in some cases, create and set up certificates. For more information, see [Setting Up Database Mirroring (SQL Server)](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/setting-up-database-mirroring-sql-server?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-sql-server?view=sql-server-ver17#interoperability-and-coexistence-with-other-database-engine-features)
## Interoperability and Coexistence with Other Database Engine Features
Database mirroring can be used with the following features or components of SQL Server.
  * [Database Mirroring and Log Shipping (SQL Server)](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-and-log-shipping-sql-server?view=sql-server-ver17)
  * [Database mirroring and full-text catalogs (SQL Server)](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-and-full-text-catalogs-sql-server?view=sql-server-ver17)
  * [Database Mirroring and Database Snapshots (SQL Server)](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-and-database-snapshots-sql-server?view=sql-server-ver17)
  * [Database Mirroring and Replication (SQL Server)](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-and-replication-sql-server?view=sql-server-ver17)


[](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-sql-server?view=sql-server-ver17#in-this-section)
## In this section
[Prerequisites, Restrictions, and Recommendations for Database Mirroring](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/prerequisites-restrictions-and-recommendations-for-database-mirroring?view=sql-server-ver17) Describes the prerequisites and recommendations for setting up database mirroring.
[Database Mirroring Operating Modes](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-operating-modes?view=sql-server-ver17) Contains information about the synchronous and asynchronous operating modes for database mirroring sessions, and about switching partner roles during a database mirroring session.
[Database Mirroring Witness](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-witness?view=sql-server-ver17) Describes the role of a witness in database mirroring, how to use a single witness in multiple mirroring sessions, software and hardware recommendations for witnesses, and the role of the witness in automatic failover. It also contains information about adding or removing a witness.
[Role Switching During a Database Mirroring Session (SQL Server)](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/role-switching-during-a-database-mirroring-session-sql-server?view=sql-server-ver17) Contains information about switching partner roles during a database mirroring session, including automatic failover, manual failover, and forced service (with possible data loss). Also, contains information about estimating the interruption of service during role switching.
[Possible Failures During Database Mirroring](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/possible-failures-during-database-mirroring?view=sql-server-ver17) Discusses physical, operating system, and SQL Server problems, including hard errors and soft errors, that can cause a failure in a database mirroring session. Discusses how the mirroring time-out mechanism responds to soft errors.
[The database mirroring endpoint (SQL Server)](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/the-database-mirroring-endpoint-sql-server?view=sql-server-ver17) Discusses how the database mirroring endpoint functions.
[Setting Up Database Mirroring (SQL Server)](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/setting-up-database-mirroring-sql-server?view=sql-server-ver17) Contains topics about the prerequisites, recommendations, and steps for setting up database mirroring.
[Connect Clients to a Database Mirroring Session (SQL Server)](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/connect-clients-to-a-database-mirroring-session-sql-server?view=sql-server-ver17) Contains topics covering client connection-string attributes and the algorithms for connecting and reconnecting a client to a mirrored database.
[Pausing and Resuming Database Mirroring (SQL Server)](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/pausing-and-resuming-database-mirroring-sql-server?view=sql-server-ver17) Discusses what happens while database mirroring is paused, including the impact on transaction log truncation, and contains descriptions about how to pause and resume database mirroring.
[Removing Database Mirroring (SQL Server)](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/removing-database-mirroring-sql-server?view=sql-server-ver17) Discusses the impact of removing mirroring and contains descriptions about how to end a session
[Monitoring Database Mirroring (SQL Server)](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/monitoring-database-mirroring-sql-server?view=sql-server-ver17) Contains information about using Database Mirroring Monitor or the **dbmmonitor** stored procedures to monitor database mirroring or sessions.
[](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-sql-server?view=sql-server-ver17#related-tasks)
## Related tasks
[](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-sql-server?view=sql-server-ver17#configuration-tasks)
### Configuration Tasks
**Using SQL Server Management Studio**
  * [Start the Configuring Database Mirroring Security Wizard](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/start-the-configuring-database-mirroring-security-wizard?view=sql-server-ver17)
  * [Establish Database Mirroring Session - Windows Authentication](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/establish-database-mirroring-session-windows-authentication?view=sql-server-ver17)


**Using Transact-SQL**
  * [Database Mirroring - Allow Network Access - Windows Authentication](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-allow-network-access-windows-authentication?view=sql-server-ver17)
  * [Database Mirroring - Use Certificates for Outbound Connections](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-use-certificates-for-outbound-connections?view=sql-server-ver17)
  * [Database Mirroring - Use Certificates for Inbound Connections](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-use-certificates-for-inbound-connections?view=sql-server-ver17)
  * [Create a Database Mirroring Endpoint for Windows Authentication (Transact-SQL)](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/create-a-database-mirroring-endpoint-for-windows-authentication-transact-sql?view=sql-server-ver17)
  * [Configure database mirroring](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-establish-session-windows-authentication?view=sql-server-ver17)
  * [Add a Database Mirroring Witness Using Windows Authentication (Transact-SQL)](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/add-a-database-mirroring-witness-using-windows-authentication-transact-sql?view=sql-server-ver17)
  * [Set Up a Mirror Database to Use the Trustworthy Property (Transact-SQL)](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/set-up-a-mirror-database-to-use-the-trustworthy-property-transact-sql?view=sql-server-ver17)


**Using Transact-SQL or SQL Server Management Studio**
  * [Upgrading Mirrored Instances](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/upgrading-mirrored-instances?view=sql-server-ver17)
  * [Prepare a Mirror Database for Mirroring (SQL Server)](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/prepare-a-mirror-database-for-mirroring-sql-server?view=sql-server-ver17)


[](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-sql-server?view=sql-server-ver17#administrative-tasks)
### Administrative Tasks
**Transact-SQL**
  * [Change Transaction Safety in a Database Mirroring Session (Transact-SQL)](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/change-transaction-safety-in-a-database-mirroring-session-transact-sql?view=sql-server-ver17)
  * [Manually Fail Over a Database Mirroring Session (Transact-SQL)](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/manually-fail-over-a-database-mirroring-session-transact-sql?view=sql-server-ver17)
  * [Force Service in a Database Mirroring Session (Transact-SQL)](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/force-service-in-a-database-mirroring-session-transact-sql?view=sql-server-ver17)
  * [Pause or Resume a Database Mirroring Session (SQL Server)](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/pause-or-resume-a-database-mirroring-session-sql-server?view=sql-server-ver17)
  * [Remove the Witness from a Database Mirroring Session (SQL Server)](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/remove-the-witness-from-a-database-mirroring-session-sql-server?view=sql-server-ver17)
  * [Remove Database Mirroring (SQL Server)](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/remove-database-mirroring-sql-server?view=sql-server-ver17)


**SQL Server Management Studio**
  * [Add or Replace a Database Mirroring Witness (SQL Server Management Studio)](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/add-or-replace-a-database-mirroring-witness-sql-server-management-studio?view=sql-server-ver17)
  * [Manually Fail Over a Database Mirroring Session (SQL Server Management Studio)](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/manually-fail-over-a-database-mirroring-session-sql-server-management-studio?view=sql-server-ver17)
  * [Pause or Resume a Database Mirroring Session (SQL Server)](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/pause-or-resume-a-database-mirroring-session-sql-server?view=sql-server-ver17)
  * [Remove the Witness from a Database Mirroring Session (SQL Server)](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/remove-the-witness-from-a-database-mirroring-session-sql-server?view=sql-server-ver17)
  * [Remove Database Mirroring (SQL Server)](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/remove-database-mirroring-sql-server?view=sql-server-ver17)


[](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-sql-server?view=sql-server-ver17#related-content)
## Related content
  * [The database mirroring endpoint (SQL Server)](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/the-database-mirroring-endpoint-sql-server?view=sql-server-ver17)
  * [Automatic Page Repair (Availability Groups: Database Mirroring)](https://learn.microsoft.com/en-us/sql/sql-server/failover-clusters/automatic-page-repair-availability-groups-database-mirroring?view=sql-server-ver17)
  * [Troubleshoot Database Mirroring Configuration (SQL Server)](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/troubleshoot-database-mirroring-configuration-sql-server?view=sql-server-ver17)
  * [Database Mirroring: Interoperability and Coexistence (SQL Server)](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-interoperability-and-coexistence-sql-server?view=sql-server-ver17)
  * [Prerequisites, Restrictions, and Recommendations for Database Mirroring](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/prerequisites-restrictions-and-recommendations-for-database-mirroring?view=sql-server-ver17)
  * [What is an Always On availability group?](https://learn.microsoft.com/en-us/sql/database-engine/availability-groups/windows/overview-of-always-on-availability-groups-sql-server?view=sql-server-ver17)
  * [About log shipping (SQL Server)](https://learn.microsoft.com/en-us/sql/database-engine/log-shipping/about-log-shipping-sql-server?view=sql-server-ver17)


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
  * [ Database Mirroring: Prerequisites, restrictions, & recommendations - SQL Server Database Mirroring ](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/prerequisites-restrictions-and-recommendations-for-database-mirroring?source=recommendations)
Learn about the prerequisites, restrictions, and recommendations for configuring database mirroring with SQL Server.
  * [ Microsoft Fabric mirrored databases - SQL Server ](https://learn.microsoft.com/en-us/sql/sql-server/fabric-database/fabric-mirrored-databases?source=recommendations)
Learn about the mirrored databases in Microsoft Fabric from SQL Server, Azure SQL Database and Azure SQL Managed Instance.
  * [ Database Mirroring and Replication (SQL Server) - SQL Server Database Mirroring ](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-and-replication-sql-server?source=recommendations)
Learn how to use database mirroring in conjunction with replication to improve availability for the publication database in SQL Server.
  * [ Setting Up Database Mirroring (SQL Server) - SQL Server Database Mirroring ](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/setting-up-database-mirroring-sql-server?source=recommendations)
Learn about prerequisites, recommendations, and steps for setting up database mirroring in SQL Server, including an overview of a database mirroring session.
  * [ Database Mirroring Operating Modes - SQL Server Database Mirroring ](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-operating-modes?source=recommendations)
Learn about the synchronous and asynchronous operating modes for database mirroring sessions in SQL Server.
  * [ Common issues when configuring database mirroring - SQL Server Database Mirroring ](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/troubleshoot-database-mirroring-configuration-sql-server?source=recommendations)
Provides information to help troubleshoot problems setting up a database mirroring session.
  * [ The Database Mirroring Endpoint (SQL Server) - SQL Server Database Mirroring ](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/the-database-mirroring-endpoint-sql-server?source=recommendations)
Learn about a dedicated database mirroring endpoint, which is required for each server to participate in Always On availability groups or database mirroring.
  * [ Prepare a database for mirroring - SQL Server Database Mirroring ](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/prepare-a-mirror-database-for-mirroring-sql-server?source=recommendations)
Learn how to prepare a SQL Server database for database mirroring by using SQL Server Management Studio or Transact-SQL in SQL Server.


Show 5 more
Module
[ Get started with SQL Database in Microsoft Fabric - Training ](https://learn.microsoft.com/en-us/training/modules/get-started-sql-database-microsoft-fabric/?source=recommendations)
Learn how SQL Database in Microsoft Fabric works, the key concepts, and practical examples to help users SQL Database effectively as part of their analytics solutions.
Certification
[ Microsoft Certified: Azure Database Administrator Associate - Certifications ](https://learn.microsoft.com/en-us/credentials/certifications/azure-database-administrator-associate/?source=recommendations)
Administer an SQL Server database infrastructure for cloud, on-premises and hybrid relational databases using the Microsoft PaaS relational database offerings.
Mar 8, 4 PM - Mar 8, 4 PM
Experiment with what's next in AI-driven apps and agent design
* * *
  * Last updated on 09/02/2025


##  In this article
  1. [Benefits of Database Mirroring](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-sql-server?view=sql-server-ver17#benefits-of-database-mirroring)
  2. [Database Mirroring Terms and Definitions](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-sql-server?view=sql-server-ver17#database-mirroring-terms-and-definitions)
  3. [Overview of Database Mirroring](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-sql-server?view=sql-server-ver17#overview-of-database-mirroring)
  4. [Set Up Database Mirroring Session](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-sql-server?view=sql-server-ver17#set-up-database-mirroring-session)
  5. [Interoperability and Coexistence with Other Database Engine Features](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-sql-server?view=sql-server-ver17#interoperability-and-coexistence-with-other-database-engine-features)
  6. [In this section](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-sql-server?view=sql-server-ver17#in-this-section)
  7. [Related tasks](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-sql-server?view=sql-server-ver17#related-tasks)
  8. [Related content](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-sql-server?view=sql-server-ver17#related-content)


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
[ Sign in ](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-sql-server?view=sql-server-ver17)
[English (United States)](https://learn.microsoft.com/en-us/locale?target=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fsql%2Fdatabase-engine%2Fdatabase-mirroring%2Fdatabase-mirroring-sql-server%3Fview%3Dsql-server-ver17)
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
