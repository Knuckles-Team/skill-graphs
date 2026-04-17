# Extended Events overview
Feedback
Summarize this article for me
##  In this article
  1. [Benefits of Extended Events](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/extended-events?view=sql-server-ver17&tabs=sqldb#benefits-of-extended-events)
  2. [Extended Events concepts](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/extended-events?view=sql-server-ver17&tabs=sqldb#extended-events-concepts)
  3. [Extended Events architecture](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/extended-events?view=sql-server-ver17&tabs=sqldb#extended-events-architecture)
  4. [Extended Events tasks](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/extended-events?view=sql-server-ver17&tabs=sqldb#extended-events-tasks)
  5. [Extended Events catalog views](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/extended-events?view=sql-server-ver17&tabs=sqldb#extended-events-catalog-views)
  6. [Extended Events dynamic management views](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/extended-events?view=sql-server-ver17&tabs=sqldb#extended-events-dynamic-management-views)
  7. [Permissions](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/extended-events?view=sql-server-ver17&tabs=sqldb#permissions)
  8. [Code examples can differ for Azure SQL Database, SQL database in Fabric, and SQL Managed Instance](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/extended-events?view=sql-server-ver17&tabs=sqldb#code-examples-can-differ-for-azure-sql-database-sql-database-in-fabric-and-sql-managed-instance)
  9. [Related content](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/extended-events?view=sql-server-ver17&tabs=sqldb#related-content)

Show 5 more
**Applies to:** ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure SQL Database](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure SQL Managed Instance](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL database in Microsoft Fabric](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to)
The Extended Events (XEvents) architecture enables users to collect as much or as little data as is necessary to monitor, identify, or troubleshoot performance in SQL Server, Azure SQL Database, Azure SQL Managed Instance, and SQL database in Fabric. Extended Events is highly configurable, lightweight, and scales well. For more information, see [Extended Events Architecture](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/extended-events?view=sql-server-ver17&tabs=sqldb#extended-events-architecture).
Extended Events replace the deprecated [SQL Trace](https://learn.microsoft.com/en-us/sql/relational-databases/sql-trace/sql-trace?view=sql-server-ver17) and SQL Server Profiler features.
To get started with Extended Events, use [Quickstart: Extended Events](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/quick-start-extended-events-in-sql-server?view=sql-server-ver17).
For Azure SQL Database, SQL database in Fabric, and SQL Managed Instance, [code examples can differ](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/extended-events?view=sql-server-ver17&tabs=sqldb#code-examples-can-differ-for-azure-sql-database-and-sql-managed-instance) because the files for the `event_file` target are stored in Azure Storage. For more information, see [Extended Events in Azure SQL](https://learn.microsoft.com/en-us/azure/azure-sql/database/xevent-db-diff-from-svr).
[](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/extended-events?view=sql-server-ver17&tabs=sqldb#benefits-of-extended-events)
## Benefits of Extended Events
Extended Events is a lightweight performance monitoring system that uses minimal system resources while providing a detailed, in-depth view of the database engine. SQL Server Management Studio provides a graphical user interface for Extended Events to create, modify, and drop event sessions and to display and analyze session data. To learn more about Extended Events support in Management Studio, see:
  * [Manage Event Sessions in the Object Explorer](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/manage-event-sessions-in-the-object-explorer?view=sql-server-ver17)
  * [Use the SSMS XEvent Profiler](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/use-the-ssms-xe-profiler?view=sql-server-ver17)


[](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/extended-events?view=sql-server-ver17&tabs=sqldb#extended-events-concepts)
## Extended Events concepts
Extended Events builds on the existing concepts from Event Tracing for Windows (ETW), such as _event_ and _event consumer_ , and introduces new concepts such as _action_ and _predicate_.
The following table provides documentation references to understand the concepts in Extended Events.
Expand table
Article | Description
---|---
[Extended Events packages](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/sql-server-extended-events-packages?view=sql-server-ver17) | Describes the Extended Events packages that contain objects. These objects are used to obtain and process data when an Extended Events session is running.
[Extended Events targets](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/targets-for-extended-events-in-sql-server?view=sql-server-ver17) | Describes the event consumers that can receive data during an event session.
[Extended Events engine](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/sql-server-extended-events-engine?view=sql-server-ver17) | Describes the engine that implements and manages an Extended Events session.
[Extended Events sessions](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/sql-server-extended-events-sessions?view=sql-server-ver17) | Describes the Extended Events session.
[](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/extended-events?view=sql-server-ver17&tabs=sqldb#extended-events-architecture)
## Extended Events architecture
Extended Events is a name for a general event-handling system for server systems. The Extended Events infrastructure supports the correlation of data from the database engine, and under certain conditions, the correlation of data from the operating system and database applications. In the operating system case, Extended Events output must be directed to [Event Tracing for Windows (ETW)](https://learn.microsoft.com/en-us/windows/win32/etw/event-tracing-portal). ETW can correlate the event data with operating system or application event data.
All applications have execution points that are useful both inside and outside an application. Inside the application, asynchronous processing can be enqueued using information that is collected during the initial execution of a task. Outside the application, execution points provide monitoring utilities with information. The information is about the behavioral and performance characteristics of the monitored application.
Extended Events supports using event data outside a process. This data is typically used by users either administering or supporting a product by doing performance monitoring or by user developing applications on a product for debugging purposes. Data is consumed or analyzed using tools such as SQL Server Management Studio, XEvent Profiler and Performance Monitor, and T-SQL or Windows command line tools.
Extended Events has the following key design aspects:
  * The Extended Events engine is event agnostic. The engine can bind any event to any target, because the engine isn't constrained by event content. For more information about the Extended Events engine, see [Extended Events engine](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/sql-server-extended-events-engine?view=sql-server-ver17).
  * Events are separated from event consumers, which are called _targets_ in Extended Events. This means that any target can receive any event. In addition, any event that is raised can be automatically consumed by the target, which can log or provide additional event context. For more information, see [Extended Events targets](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/targets-for-extended-events-in-sql-server?view=sql-server-ver17).
  * Events are distinct from the action to take when an event occurs. Therefore, any action can be associated with any event.
  * Predicates can dynamically filter when event data should be captured. Dynamic filtering adds to the flexibility of the Extended Events infrastructure. For more information, see [Extended Events packages](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/sql-server-extended-events-packages?view=sql-server-ver17).


Extended Events can synchronously generate event data (and asynchronously process that data), which provides a flexible solution for event handling. In addition, Extended Events provides the following features:
  * A unified approach to handling events across the server system, while enabling users to isolate specific events for troubleshooting purposes.
  * Integration with, and support for existing ETW tools.
  * A fully configurable event handling mechanism that uses Transact-SQL.
  * The ability to dynamically monitor active processes, while having minimal effect on those processes.
  * A default system health session that runs without any noticeable performance effects. The session collects system data that you can use to help troubleshoot performance issues. For more information, see [Use the system_health session](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/use-the-system-health-session?view=sql-server-ver17).


[](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/extended-events?view=sql-server-ver17&tabs=sqldb#extended-events-tasks)
## Extended Events tasks
Using Management Studio or Transact-SQL to execute Transact-SQL Data Definition Language (DDL) statements, consume dynamic management views and functions, or catalog views, you can create simple or complex SQL Server Extended Events troubleshooting solutions for your SQL Server environment.
Expand table
Task description | Article
---|---
Use the **Object Explorer** to manage event sessions. | [Manage Event Sessions in the Object Explorer](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/manage-event-sessions-in-the-object-explorer?view=sql-server-ver17)
Describes how to use available Extended Events targets. | [Extended Events targets](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/targets-for-extended-events-in-sql-server?view=sql-server-ver17)
Describes how to view and refresh target data. | [View event data in SQL Server Management Studio](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/advanced-viewing-of-target-data-from-extended-events-in-sql-server?view=sql-server-ver17)
Describes the architecture of Extended Events sessions. | [Extended Events sessions](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/sql-server-extended-events-sessions?view=sql-server-ver17)
Describes how to use Extended Events tools to create and manage your Extended Events sessions. | [Extended Events Tools](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/extended-events-tools?view=sql-server-ver17)
Describes how to alter an Extended Events session. | [Alter an Extended Events Session](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/alter-an-extended-events-session?view=sql-server-ver17)
Describes how to get information about the fields associated with the events. | [Get the Fields for All Events](https://learn.microsoft.com/en-us/previous-versions/sql/sql-server-2016/bb677249\(v=sql.130\))
Describes how to find out what events are available in the registered packages. | [SELECTs and JOINs From System Views for Extended Events](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/selects-and-joins-from-system-views-for-extended-events-in-sql-server?view=sql-server-ver17)
Describes how to view the Extended Events events and actions that are equivalent to each SQL Trace event and its associated columns. | [View the Extended Events Equivalents to SQL Trace Event Classes](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/view-the-extended-events-equivalents-to-sql-trace-event-classes?view=sql-server-ver17)
Describes how to convert an existing SQL Trace script to an Extended Events session. | [Convert an Existing SQL Trace Script to an Extended Events Session](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/convert-an-existing-sql-trace-script-to-an-extended-events-session?view=sql-server-ver17)
Describes how to determine which queries are holding the lock, the plan of the query, and the Transact-SQL stack at the time the lock was taken. | [Determine Which Queries Are Holding Locks](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/determine-which-queries-are-holding-locks?view=sql-server-ver17)
Describes how to identify the source of locks. | [Find the Objects That Have the Most Locks Taken on Them](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/find-the-objects-that-have-the-most-locks-taken-on-them?view=sql-server-ver17)
Describes how to use Extended Events with Event Tracing for Windows to monitor system activity. | [Monitor System Activity Using Extended Events](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/monitor-system-activity-using-extended-events?view=sql-server-ver17)
Using Catalog Views and Dynamic Management Views (DMVs) for Extended Events | [SELECTs and JOINs From System Views for Extended Events](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/selects-and-joins-from-system-views-for-extended-events-in-sql-server?view=sql-server-ver17)
[](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/extended-events?view=sql-server-ver17&tabs=sqldb#extended-events-catalog-views)
## Extended Events catalog views
Extended Events provides several [catalog views](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/catalog-views-transact-sql?view=sql-server-ver17). Catalog views tell you about event session _metadata_ or _definition_. For information about instances of active event sessions, see [Extended Events dynamic management views](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/extended-events?view=sql-server-ver17&tabs=sqldb#extended-events-dynamic-management-views).
  * [Azure SQL Database and SQL database in Fabric](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/extended-events?view=sql-server-ver17&tabs=sqldb#tabpanel_1_sqldb)
  * [Azure SQL Managed Instance](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/extended-events?view=sql-server-ver17&tabs=sqldb#tabpanel_1_sqlmi)
  * [SQL Server](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/extended-events?view=sql-server-ver17&tabs=sqldb#tabpanel_1_sqlserver)


Expand table
Name of catalog view | Description
---|---
[sys.database_event_session_actions](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-database-event-session-actions-azure-sql-database?view=sql-server-ver17) | Returns a row for each action on each event of a database-scoped event session.
[sys.database_event_session_events](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-database-event-session-events-azure-sql-database?view=sql-server-ver17) | Returns a row for each event in a database-scoped event session.
[sys.database_event_session_fields](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-database-event-session-fields-azure-sql-database?view=sql-server-ver17) | Returns a row for each customizable column that was explicitly set on events and targets of a database-scoped session.
[sys.database_event_session_targets](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-database-event-session-targets-azure-sql-database?view=sql-server-ver17) | Returns a row for each event target for a database-scoped event session.
[sys.database_event_sessions](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-database-event-sessions-azure-sql-database?view=sql-server-ver17) | Returns a row for each database-scoped event session.
Expand table
Name of catalog view | Description
---|---
[sys.server_event_session_actions](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-server-event-session-actions-transact-sql?view=sql-server-ver17) | Returns a row for each action on each event of a server-scoped event session.
[sys.server_event_session_events](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-server-event-session-events-transact-sql?view=sql-server-ver17) | Returns a row for each event in a server-scoped event session.
[sys.server_event_session_fields](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-server-event-session-fields-transact-sql?view=sql-server-ver17) | Returns a row for each customizable column that was explicitly set on events and targets of a server-scoped event session.
[sys.server_event_session_targets](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-server-event-session-targets-transact-sql?view=sql-server-ver17) | Returns a row for each event target for a server-scoped event session.
[sys.server_event_sessions](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-server-event-sessions-transact-sql?view=sql-server-ver17) | Returns a row for each server-scoped event session.
[sys.database_event_session_actions](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-database-event-session-actions-azure-sql-database?view=sql-server-ver17) | Returns a row for each action on each event of a database-scoped event session.
[sys.database_event_session_events](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-database-event-session-events-azure-sql-database?view=sql-server-ver17) | Returns a row for each event in a database-scoped event session.
[sys.database_event_session_fields](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-database-event-session-fields-azure-sql-database?view=sql-server-ver17) | Returns a row for each customizable column that was explicitly set on events and targets of a database-scoped session.
[sys.database_event_session_targets](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-database-event-session-targets-azure-sql-database?view=sql-server-ver17) | Returns a row for each event target for a database-scoped event session.
[sys.database_event_sessions](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-database-event-sessions-azure-sql-database?view=sql-server-ver17) | Returns a row for each database-scoped event session.
Expand table
Name of catalog view | Description
---|---
[sys.server_event_session_actions](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-server-event-session-actions-transact-sql?view=sql-server-ver17) | Returns a row for each action on each event of a server-scoped event session.
[sys.server_event_session_events](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-server-event-session-events-transact-sql?view=sql-server-ver17) | Returns a row for each event in a server-scoped event session.
[sys.server_event_session_fields](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-server-event-session-fields-transact-sql?view=sql-server-ver17) | Returns a row for each customizable column that was explicitly set on events and targets of a server-scoped event session.
[sys.server_event_session_targets](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-server-event-session-targets-transact-sql?view=sql-server-ver17) | Returns a row for each event target for a server-scoped event session.
[sys.server_event_sessions](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-server-event-sessions-transact-sql?view=sql-server-ver17) | Returns a row for each server-scoped event session.
[](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/extended-events?view=sql-server-ver17&tabs=sqldb#extended-events-dynamic-management-views)
## Extended Events dynamic management views
Extended Events provides several [dynamic management views (DMVs)](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/extended-events-dynamic-management-views?view=sql-server-ver17). DMVs return information about _active_ (started) event sessions, such as session and target statistics.
  * [Azure SQL Database and SQL database in Fabric](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/extended-events?view=sql-server-ver17&tabs=sqldb#tabpanel_2_sqldb)
  * [Azure SQL Managed Instance](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/extended-events?view=sql-server-ver17&tabs=sqldb#tabpanel_2_sqlmi)
  * [SQL Server](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/extended-events?view=sql-server-ver17&tabs=sqldb#tabpanel_2_sqlserver)


Expand table
Name of DMV | Description
---|---
[sys.dm_xe_database_session_event_actions](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/sys-dm-xe-database-session-event-actions-azure-sql-database?view=sql-server-ver17) | Returns information about database-scoped event session actions.
[sys.dm_xe_database_session_events](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/sys-dm-xe-database-session-events-azure-sql-database?view=sql-server-ver17) | Returns information about database-scoped event session events.
[sys.dm_xe_database_session_object_columns](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/sys-dm-xe-database-session-object-columns-azure-sql-database?view=sql-server-ver17) | Shows the configuration values for objects that are bound to a database-scoped session.
[sys.dm_xe_database_session_targets](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/sys-dm-xe-database-session-targets-azure-sql-database?view=sql-server-ver17) | Returns information about database-scoped event session targets.
[sys.dm_xe_database_sessions](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/sys-dm-xe-database-sessions-azure-sql-database?view=sql-server-ver17) | Returns a row for each database-scoped event session running in the current database.
Expand table
Name of DMV | Description
---|---
[sys.dm_xe_session_event_actions](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/sys-dm-xe-session-event-actions-transact-sql?view=sql-server-ver17) | Returns information about server-scoped event session actions.
[sys.dm_xe_session_events](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/sys-dm-xe-session-events-transact-sql?view=sql-server-ver17) | Returns information about server-scoped event session events.
[sys.dm_xe_session_object_columns](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/sys-dm-xe-session-object-columns-transact-sql?view=sql-server-ver17) | Shows the configuration values for objects that are bound to a server-scoped session.
[sys.dm_xe_session_targets](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/sys-dm-xe-session-targets-transact-sql?view=sql-server-ver17) | Returns information about server-scoped event session targets.
[sys.dm_xe_sessions](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/sys-dm-xe-sessions-transact-sql?view=sql-server-ver17) | Returns a row for each server-scoped event session running on the server.
[sys.dm_xe_database_session_event_actions](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/sys-dm-xe-database-session-event-actions-azure-sql-database?view=sql-server-ver17) | Returns information about database-scoped event session actions.
[sys.dm_xe_database_session_events](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/sys-dm-xe-database-session-events-azure-sql-database?view=sql-server-ver17) | Returns information about database-scoped event session events.
[sys.dm_xe_database_session_object_columns](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/sys-dm-xe-database-session-object-columns-azure-sql-database?view=sql-server-ver17) | Shows the configuration values for objects that are bound to a database-scoped session.
[sys.dm_xe_database_session_targets](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/sys-dm-xe-database-session-targets-azure-sql-database?view=sql-server-ver17) | Returns information about database-scoped event session targets.
[sys.dm_xe_database_sessions](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/sys-dm-xe-database-sessions-azure-sql-database?view=sql-server-ver17) | Returns a row for each database-scoped event session running in the current database.
Expand table
Name of DMV | Description
---|---
[sys.dm_xe_session_event_actions](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/sys-dm-xe-session-event-actions-transact-sql?view=sql-server-ver17) | Returns information about server-scoped event session actions.
[sys.dm_xe_session_events](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/sys-dm-xe-session-events-transact-sql?view=sql-server-ver17) | Returns information about server-scoped event session events.
[sys.dm_xe_session_object_columns](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/sys-dm-xe-session-object-columns-transact-sql?view=sql-server-ver17) | Shows the configuration values for objects that are bound to a server-scoped session.
[sys.dm_xe_session_targets](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/sys-dm-xe-session-targets-transact-sql?view=sql-server-ver17) | Returns information about server-scoped event session targets.
[sys.dm_xe_sessions](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/sys-dm-xe-sessions-transact-sql?view=sql-server-ver17) | Returns a row for each server-scoped event session running on the server.
[](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/extended-events?view=sql-server-ver17&tabs=sqldb#permissions)
## Permissions
In Azure SQL Database, SQL database in Fabric, Azure SQL Managed Instance, and in SQL Server 2022 and later versions, Extended Events supports a granular permission model. The following permissions can be granted:
  * [Azure SQL Database and SQL database in Fabric](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/extended-events?view=sql-server-ver17&tabs=sqldb#tabpanel_3_sqldb)
  * [Azure SQL Managed Instance](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/extended-events?view=sql-server-ver17&tabs=sqldb#tabpanel_3_sqlmi)
  * [SQL Server](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/extended-events?view=sql-server-ver17&tabs=sqldb#tabpanel_3_sqlserver)


SQL
Copy
```
CREATE ANY DATABASE EVENT SESSION
DROP ANY DATABASE EVENT SESSION
ALTER ANY DATABASE EVENT SESSION
ALTER ANY DATABASE EVENT SESSION ADD EVENT
ALTER ANY DATABASE EVENT SESSION DROP EVENT
ALTER ANY DATABASE EVENT SESSION ADD TARGET
ALTER ANY DATABASE EVENT SESSION DROP TARGET
ALTER ANY DATABASE EVENT SESSION ENABLE
ALTER ANY DATABASE EVENT SESSION DISABLE
ALTER ANY DATABASE EVENT SESSION OPTION

```

SQL
Copy
```
CREATE ANY EVENT SESSION
DROP ANY EVENT SESSION
ALTER ANY EVENT SESSION
ALTER ANY EVENT SESSION ADD EVENT
ALTER ANY EVENT SESSION DROP EVENT
ALTER ANY EVENT SESSION ADD TARGET
ALTER ANY EVENT SESSION DROP TARGET
ALTER ANY EVENT SESSION ENABLE
ALTER ANY EVENT SESSION DISABLE
ALTER ANY EVENT SESSION OPTION

CREATE ANY DATABASE EVENT SESSION
DROP ANY DATABASE EVENT SESSION
ALTER ANY DATABASE EVENT SESSION
ALTER ANY DATABASE EVENT SESSION ADD EVENT
ALTER ANY DATABASE EVENT SESSION DROP EVENT
ALTER ANY DATABASE EVENT SESSION ADD TARGET
ALTER ANY DATABASE EVENT SESSION DROP TARGET
ALTER ANY DATABASE EVENT SESSION ENABLE
ALTER ANY DATABASE EVENT SESSION DISABLE
ALTER ANY DATABASE EVENT SESSION OPTION

```

SQL
Copy
```
CREATE ANY EVENT SESSION
DROP ANY EVENT SESSION
ALTER ANY EVENT SESSION
ALTER ANY EVENT SESSION ADD EVENT
ALTER ANY EVENT SESSION DROP EVENT
ALTER ANY EVENT SESSION ADD TARGET
ALTER ANY EVENT SESSION DROP TARGET
ALTER ANY EVENT SESSION ENABLE
ALTER ANY EVENT SESSION DISABLE
ALTER ANY EVENT SESSION OPTION

```

For information on what each of these permissions controls, see [CREATE EVENT SESSION](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-event-session-transact-sql?view=sql-server-ver17), [ALTER EVENT SESSION](https://learn.microsoft.com/en-us/sql/t-sql/statements/alter-event-session-transact-sql?view=sql-server-ver17), and [DROP EVENT SESSION](https://learn.microsoft.com/en-us/sql/t-sql/statements/drop-event-session-transact-sql?view=sql-server-ver17).
All of these permissions are included in the `CONTROL` permission on the database, SQL managed instance, or SQL Server instance. In Azure SQL Database, the database owner (`dbo`), members of the `db_owner` database role, and the administrators of the logical server hold the database `CONTROL` permission. In Azure SQL Managed Instance and in SQL Server, members of the `sysadmin` server role hold the `CONTROL` permission on the instance.
[](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/extended-events?view=sql-server-ver17&tabs=sqldb#code-examples-can-differ-for-azure-sql-database-sql-database-in-fabric-and-sql-managed-instance)
## Code examples can differ for Azure SQL Database, SQL database in Fabric, and SQL Managed Instance
Some Transact-SQL code examples written for SQL Server need small changes to run in Azure SQL Database or SQL database in Fabric. One category of such code examples involves catalog views whose name prefixes differ depending on the database engine type:
  * `server_` - _prefix for SQL Server and Azure SQL Managed Instance_
  * `database_` - _prefix for Azure SQL Database, SQL database in Fabric, and SQL Managed Instance_


Azure SQL Database and SQL database in Fabric support only database-scoped event sessions. [SQL Server Management Studio (SSMS)](https://learn.microsoft.com/en-us/ssms/sql-server-management-studio-ssms) supports database-scoped event sessions for Azure SQL Database: an **Extended Events** node containing database-scoped sessions appears under each database in [Object Explorer](https://learn.microsoft.com/en-us/ssms/object/object-explorer).
Azure SQL Managed Instance supports both database-scoped sessions and server-scoped sessions. SSMS fully supports server-scoped sessions for SQL Managed Instance: an **Extended Events** node containing all server-scoped sessions appears under the **Management** folder for each managed instance in Object Explorer.
Server-scoped event sessions are recommended for Azure SQL Managed Instance.
Database-scoped event sessions aren't displayed in Object Explorer in SSMS for Azure SQL Managed Instance. On a SQL managed instance, database-scoped event sessions can only be queried and managed with Transact-SQL.
For illustration, the following table lists and compares two subsets of catalog views. The subsets have differing name prefixes because they support different database engine types.
Expand table
Name in SQL Server and Azure SQL Managed Instance | Name in Azure SQL Database, SQL database in Fabric, and Azure SQL Managed Instance
---|---
`sys.server_event_session_actions`
`sys.server_event_session_events`
`sys.server_event_session_fields`
`sys.server_event_session_targets`
`sys.server_event_sessions`
|  `sys.database_event_session_actions`
`sys.database_event_session_events`
`sys.database_event_session_fields`
`sys.database_event_session_targets`
`sys.database_event_sessions`
[](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/extended-events?view=sql-server-ver17&tabs=sqldb#related-content)
## Related content
  * [Extended Events Dynamic Management Views](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/extended-events-dynamic-management-views?view=sql-server-ver17)
  * [Extended Events Catalog Views (Transact-SQL)](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/extended-events-catalog-views-transact-sql?view=sql-server-ver17)
  * [SQL Mysteries: Causality tracking vs Event Sequence for XEvent Sessions](https://techcommunity.microsoft.com/blog/sqlserver/sql-mysteries-causality-tracking-vs-event-sequence-for-xevent-sessions/3198826)
  * [Analyze and prevent deadlocks in Azure SQL Database and Fabric SQL database](https://learn.microsoft.com/en-us/azure/azure-sql/database/analyze-prevent-deadlocks)
  * [Quickstart: Extended Events](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/quick-start-extended-events-in-sql-server?view=sql-server-ver17)
  * [Create an event session with an event_file target in Azure Storage](https://learn.microsoft.com/en-us/azure/azure-sql/database/xevent-code-event-file)
  * [Extended Events in Azure SQL](https://learn.microsoft.com/en-us/azure/azure-sql/database/xevent-db-diff-from-svr)


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
  * [ Quickstart: Extended Events - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/quick-start-extended-events-in-sql-server?source=recommendations)
This quickstart helps you use Extended Events, a lightweight performance monitoring system, to collect data to monitor and troubleshoot problems.
  * [ View event data in SQL Server Management Studio - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/advanced-viewing-of-target-data-from-extended-events-in-sql-server?source=recommendations)
Use SQL Server Management Studio to view target data from Extended Events in detail. You can view, export, filter, and aggregate event data.
  * [ Extended Events Equivalents to SQL Trace Event Classes - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/view-the-extended-events-equivalents-to-sql-trace-event-classes?source=recommendations)
This article shows you how to view the Extended Events actions and events that are equivalent to each SQL Trace event and its associated columns.
  * [ Extended Events Targets - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/targets-for-extended-events-in-sql-server?source=recommendations)
This article explains different targets for Extended Events sessions. Learn about target abilities in gathering and reporting data.
  * [ SQL Trace - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/sql-trace/sql-trace?source=recommendations)
SQL Trace
  * [ Use the SSMS XEvent Profiler - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/use-the-ssms-xe-profiler?source=recommendations)
The XEvent Profiler displays a live viewer of extended events. Learn why to use this profiler, key features, and how to get started viewing extended events.
  * [ Manage Event Sessions in the Object Explorer - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/manage-event-sessions-in-the-object-explorer?source=recommendations)
You can take actions in Object Explorer that affect Extended Events, such as create, start or stop, export, import, edit, or delete Extended Events sessions.
  * [ Use the system_health session - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/use-the-system-health-session?source=recommendations)
The system_health Extended Events session is included with SQL Server. This session collects system data to troubleshoot database engine performance.


Show 5 more
Module
[ Manage and monitor Windows Server event logs - Training ](https://learn.microsoft.com/en-us/training/modules/manage-monitor-event-logs/?source=recommendations)
Learn how Event Viewer provides a convenient and accessible location for you to observe events that occur. Access event information quickly and conveniently. Learn how to interpret the data in the event log.
Certification
[ Microsoft Certified: Azure Database Administrator Associate - Certifications ](https://learn.microsoft.com/en-us/credentials/certifications/azure-database-administrator-associate/?source=recommendations)
Administer an SQL Server database infrastructure for cloud, on-premises and hybrid relational databases using the Microsoft PaaS relational database offerings.
Mar 8, 4 PM - Mar 8, 4 PM
Experiment with what's next in AI-driven apps and agent design
* * *
  * Last updated on 11/18/2025


##  In this article
  1. [Benefits of Extended Events](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/extended-events?view=sql-server-ver17&tabs=sqldb#benefits-of-extended-events)
  2. [Extended Events concepts](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/extended-events?view=sql-server-ver17&tabs=sqldb#extended-events-concepts)
  3. [Extended Events architecture](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/extended-events?view=sql-server-ver17&tabs=sqldb#extended-events-architecture)
  4. [Extended Events tasks](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/extended-events?view=sql-server-ver17&tabs=sqldb#extended-events-tasks)
  5. [Extended Events catalog views](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/extended-events?view=sql-server-ver17&tabs=sqldb#extended-events-catalog-views)
  6. [Extended Events dynamic management views](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/extended-events?view=sql-server-ver17&tabs=sqldb#extended-events-dynamic-management-views)
  7. [Permissions](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/extended-events?view=sql-server-ver17&tabs=sqldb#permissions)
  8. [Code examples can differ for Azure SQL Database, SQL database in Fabric, and SQL Managed Instance](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/extended-events?view=sql-server-ver17&tabs=sqldb#code-examples-can-differ-for-azure-sql-database-sql-database-in-fabric-and-sql-managed-instance)
  9. [Related content](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/extended-events?view=sql-server-ver17&tabs=sqldb#related-content)


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
[ Sign in ](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/extended-events?view=sql-server-ver17&tabs=sqldb)
[English (United States)](https://learn.microsoft.com/en-us/locale?target=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fsql%2Frelational-databases%2Fextended-events%2Fextended-events%3Fview%3Dsql-server-ver17)
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
