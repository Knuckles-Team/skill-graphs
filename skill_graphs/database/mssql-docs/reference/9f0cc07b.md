# SQL Server Profiler
Feedback
Summarize this article for me
##  In this article
  1. [Deprecation notice](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/sql-server-profiler?view=sql-server-ver17#deprecation-notice)
  2. [Where's the Profiler?](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/sql-server-profiler?view=sql-server-ver17#wheres-the-profiler)
  3. [Capture and replay trace data](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/sql-server-profiler?view=sql-server-ver17#capture-and-replay-trace-data)
  4. [Use SQL Server Profiler](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/sql-server-profiler?view=sql-server-ver17#use-sql-server-profiler)
  5. [SQL Server Profiler concepts](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/sql-server-profiler?view=sql-server-ver17#sql-server-profiler-concepts)
  6. [SQL Server Profiler tasks](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/sql-server-profiler?view=sql-server-ver17#sql-server-profiler-tasks)
  7. [Extended Events vs. SQL Server Profiler](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/sql-server-profiler?view=sql-server-ver17#extended-events-vs-sql-server-profiler)
  8. [Extended Events tool](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/sql-server-profiler?view=sql-server-ver17#extended-events-tool)
  9. [SQL Server Profiler tool](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/sql-server-profiler?view=sql-server-ver17#sql-server-profiler-tool)
  10. [Related content](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/sql-server-profiler?view=sql-server-ver17#related-content)

Show 6 more
**Applies to:** ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure SQL Managed Instance](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to)
SQL Server Profiler is an interface to create and manage traces and analyze and replay trace results. Events are saved in a trace file that you can later analyze or use to replay a specific series of steps when diagnosing a problem.
When you try to connect to an Azure SQL Database from the SQL Server Profiler, it incorrectly throws a misleading error message as follows:
Output
Copy
```
To run a trace against SQL Server, you must be a sysadmin fixed server role member or have the ALTER TRACE permission.

```

The message should state that Azure SQL Database isn't supported by SQL Server Profiler.
[](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/sql-server-profiler?view=sql-server-ver17#deprecation-notice)
## Deprecation notice
SQL Trace and SQL Server Profiler are deprecated. Use [Extended Events](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/extended-events?view=sql-server-ver17) instead. This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature.
The `Microsoft.SqlServer.Management.Trace` namespace that contains the SQL Server Trace and Replay objects is also deprecated. However, Analysis Services workloads are supported.
For more information on [Extended Events](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/extended-events?view=sql-server-ver17), see the following articles:
  * [Quickstart: Extended Events](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/quick-start-extended-events-in-sql-server?view=sql-server-ver17)
  * For SQL Server Management Studio, use [XEvent Profiler](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/use-the-ssms-xe-profiler?view=sql-server-ver17)
  * For the [MSSQL extension for Visual Studio Code](https://learn.microsoft.com/en-us/sql/tools/visual-studio-code-extensions/mssql/mssql-extension-visual-studio-code?view=sql-server-ver17), use [Query Profiler (Preview)](https://learn.microsoft.com/en-us/sql/tools/visual-studio-code-extensions/mssql/mssql-query-profiler?view=sql-server-ver17).


[](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/sql-server-profiler?view=sql-server-ver17#wheres-the-profiler)
## Where's the Profiler?
You can start the Profiler within [Run SQL Server Profiler](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/start-sql-server-profiler?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/sql-server-profiler?view=sql-server-ver17#capture-and-replay-trace-data)
## Capture and replay trace data
The following table shows the features you can use in SQL Server to capture and replay your trace data.
Expand table
Feature / target workload | Relational Engine | Analysis Services
---|---|---
**Trace Capture** |  [Extended Events overview](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/extended-events?view=sql-server-ver17) graphical user interface in SQL Server Management Studio | SQL Server Profiler
**Trace Replay** | [SQL Server Distributed Replay overview](https://learn.microsoft.com/en-us/sql/tools/distributed-replay/sql-server-distributed-replay?view=sql-server-ver17) | SQL Server Profiler
[](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/sql-server-profiler?view=sql-server-ver17#use-sql-server-profiler)
## Use SQL Server Profiler
Microsoft SQL Server Profiler is a graphical user interface to SQL Trace for monitoring an instance of the Database Engine or Analysis Services. You can capture and save data about each event to a file or table to analyze later. For example, you can monitor a production environment to see which stored procedures affect performance by executing too slowly. Use SQL Server Profiler for activities such as:
  * Stepping through problem queries to find the cause of the problem.
  * Finding and diagnosing slow-running queries.
  * Capturing the series of Transact-SQL statements that lead to a problem. The saved trace can then replicate the problem on a test server where the problem can be diagnosed.
  * Monitoring the performance of SQL Server to tune workloads. For information about tuning the physical database design for database workloads, see [Database Engine Tuning Advisor](https://learn.microsoft.com/en-us/sql/relational-databases/performance/database-engine-tuning-advisor?view=sql-server-ver17).
  * Correlating performance counters to diagnose problems.


SQL Server Profiler also supports auditing the actions performed on instances of SQL Server. Audits record security-related actions for later review by a security administrator.
[](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/sql-server-profiler?view=sql-server-ver17#sql-server-profiler-concepts)
## SQL Server Profiler concepts
To use SQL Server Profiler, you need to understand the terms that describe the way the tool functions.
Understanding SQL Trace helps when working with SQL Server Profiler. For more information, see [SQL Trace](https://learn.microsoft.com/en-us/sql/relational-databases/sql-trace/sql-trace?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/sql-server-profiler?view=sql-server-ver17#event)
### Event
An event is an action generated within an instance of SQL Server Database Engine. Examples of these events include:
  * Login connections, failures, and disconnections.
  * Transact-SQL `SELECT`, `INSERT`, `UPDATE`, and `DELETE` statements.
  * Remote procedure call (RPC) batch status.
  * The start or end of a stored procedure.
  * The start or end of statements within stored procedures.
  * The start or end of a SQL batch.
  * An error written to the SQL Server error log.
  * A lock acquired or released on a database object.
  * An opened cursor.
  * Security permission checks.


The trace displays all of the data generated by an event in a single row. Data columns that describe the event in detail intersect this row.
[](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/sql-server-profiler?view=sql-server-ver17#eventclass)
### EventClass
An event class is a type of event that you can trace. The event class contains all of the data that an event can report. The following list shows examples of event classes:
  * **SQL:BatchCompleted**
  * **Audit Login**
  * **Audit Logout**
  * **Lock: Acquired**
  * **Lock: Released**


[](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/sql-server-profiler?view=sql-server-ver17#eventcategory)
### EventCategory
An event category defines how SQL Server Profiler groups events. For example, the **Locks** event category groups all lock event classes. However, event categories exist only within SQL Server Profiler. This term doesn't reflect how Engine events are grouped.
[](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/sql-server-profiler?view=sql-server-ver17#datacolumn)
### DataColumn
A data column is an attribute of an event class captured in the trace. Because the event class determines the type of data that can be collected, not all data columns apply to all event classes. For example, in a trace that captures the **Lock: Acquired** event class, the **BinaryData** data column contains the value of the locked page ID or row, but the **Integer Data** data column doesn't contain any value because it doesn't apply to the event class being captured.
[](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/sql-server-profiler?view=sql-server-ver17#template)
### Template
A template defines the default configuration for a trace. Specifically, it includes the event classes you want to monitor with SQL Server Profiler. For example, you can create a template specifying the events, data columns, and filters. You can't execute a template directly. Instead, you save it as a file with a `.tdf` extension. Once saved, the template controls the trace data captured when a trace based on the template is launched.
[](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/sql-server-profiler?view=sql-server-ver17#trace)
### Trace
A trace captures data based on selected event classes, data columns, and filters. For example, you can create a trace to monitor exception errors. You select the **Exception** event class and the **Error** , **State** , and **Severity** data columns to do this. The trace results provide meaningful data only if data is collected from these three columns. You can run a trace configured in such a manner and collect data on any **Exception** events in the server. Save the trace data, or use it immediately for analysis. You can replay traces later, although certain events, such as **Exception** events, are never replayed. You can also save the trace as a template to build similar traces.
SQL Server provides two ways to trace an instance of SQL Server: you can trace with SQL Server Profiler, or you can trace using system stored procedures.
[](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/sql-server-profiler?view=sql-server-ver17#filter)
### Filter
When you create a trace or template, you can define criteria to filter the data that the event collects. To keep traces from becoming too large, filter them so that you collect only a subset of the event data. For example, limiting the Microsoft Windows user names in the trace to specific users reduces the output data.
If you don't set a filter, the trace output returns all events of the selected event classes.
[](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/sql-server-profiler?view=sql-server-ver17#sql-server-profiler-tasks)
## SQL Server Profiler tasks
Expand table
Task description | Article
---|---
Lists the predefined templates that SQL Server provides for monitoring certain events and the permissions required to use replay traces. | [SQL Server Profiler templates and permissions](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/sql-server-profiler-templates-and-permissions?view=sql-server-ver17)
Describes how to run SQL Server Profiler. | [Permissions required to run SQL Server Profiler](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/permissions-required-to-run-sql-server-profiler?view=sql-server-ver17)
Describes how to create a trace. | [Create a trace (SQL Server Profiler)](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/create-a-trace-sql-server-profiler?view=sql-server-ver17)
Describes how to specify events and data columns for a trace file. | [Specify events and data columns for a trace file (SQL Server Profiler)](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/specify-events-and-data-columns-for-a-trace-file-sql-server-profiler?view=sql-server-ver17)
Describes how to save trace results to a file. | [Save trace results to a file (SQL Server Profiler)](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/save-trace-results-to-a-file-sql-server-profiler?view=sql-server-ver17)
Describes how to save trace results to a table. | [Save trace results to a table (SQL Server Profiler)](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/save-trace-results-to-a-table-sql-server-profiler?view=sql-server-ver17)
Describes how to filter events in a trace. | [Filter events in a trace (SQL Server Profiler)](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/filter-events-in-a-trace-sql-server-profiler?view=sql-server-ver17)
Describes how to view filter information. | [View filter information (SQL Server Profiler)](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/view-filter-information-sql-server-profiler?view=sql-server-ver17)
Describes how to modify a filter. | [Modify a filter (SQL Server Profiler)](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/modify-a-filter-sql-server-profiler?view=sql-server-ver17)
Describes how to set a maximum file size for a trace file (SQL Server Profiler). |  [Set a maximum file size for a trace file (SQL Server Profiler)](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/set-a-maximum-file-size-for-a-trace-file-sql-server-profiler?view=sql-server-ver17).
Describes how to set a maximum table size for a trace table. | [Set a maximum table size for a trace table (SQL Server Profiler)](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/set-a-maximum-table-size-for-a-trace-table-sql-server-profiler?view=sql-server-ver17)
Describes how to start a trace. | [Start a trace (SQL Server Profiler)](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/start-a-trace?view=sql-server-ver17)
Describes how to start a trace automatically after connecting to a server. | [Start a trace automatically after connecting to a server (SQL Server Profiler)](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/start-a-trace-automatically-after-connecting-to-a-server-sql-server-profiler?view=sql-server-ver17)
Describes how to filter events based on the event start time. | [Filter events based on the event start time (SQL Server Profiler)](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/filter-events-based-on-the-event-start-time-sql-server-profiler?view=sql-server-ver17)
Describes how to filter events based on the event end time. | [Filter events based on the event end Time (SQL Server Profiler)](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/filter-events-based-on-the-event-end-time-sql-server-profiler?view=sql-server-ver17)
Describes how to filter session IDs in a trace. | [Filter session IDs in a trace (SQL Server Profiler)](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/filter-server-process-ids-spids-in-a-trace-sql-server-profiler?view=sql-server-ver17)
Describes how to pause a trace. | [Pause a trace (SQL Server Profiler)](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/pause-a-trace-sql-server-profiler?view=sql-server-ver17)
Describes how to stop a trace. | [Stop a trace (SQL Server Profiler)](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/stop-a-trace-sql-server-profiler?view=sql-server-ver17)
Describes how to run a trace after it has been paused or stopped. | [Run a trace after it has been paused or stopped (SQL Server Profiler)](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/run-a-trace-after-it-has-been-paused-or-stopped-sql-server-profiler?view=sql-server-ver17)
Describes how to clear a trace window. | [Clear a trace window (SQL Server Profiler)](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/clear-a-trace-window-sql-server-profiler?view=sql-server-ver17)
Describes how to close a trace window. | [Close a trace window (SQL Server Profiler)](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/close-a-trace-window-sql-server-profiler?view=sql-server-ver17)
Describes how to set trace definition defaults. | [Set trace definition defaults (SQL Server Profiler)](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/set-trace-definition-defaults-sql-server-profiler?view=sql-server-ver17)
Describes how to set trace display defaults. | [Set trace display defaults (SQL Server Profiler)](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/set-trace-display-defaults-sql-server-profiler?view=sql-server-ver17)
Describes how to open a trace file. | [Open a trace file (SQL Server Profiler)](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/open-a-trace-file-sql-server-profiler?view=sql-server-ver17)
Describes how to open a trace table. | [Open a trace table (SQL Server Profiler)](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/open-a-trace-table-sql-server-profiler?view=sql-server-ver17)
Describes how to replay a trace table. | [Replay a trace table (SQL Server Profiler)](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/replay-a-trace-table-sql-server-profiler?view=sql-server-ver17)
Describes how to replay a trace file. | [Replay a trace file (SQL Server Profiler)](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/replay-a-trace-file-sql-server-profiler?view=sql-server-ver17)
Describes how to replay a single event at a time. | [Replay a single event at a time (SQL Server Profiler)](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/replay-a-single-event-at-a-time-sql-server-profiler?view=sql-server-ver17)
Describes how to replay to a breakpoint. | [Replay to a breakpoint (SQL Server Profiler)](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/replay-to-a-breakpoint-sql-server-profiler?view=sql-server-ver17)
Describes how to replay to a cursor. | [Replay to a cursor (SQL Server Profiler)](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/replay-to-a-cursor-sql-server-profiler?view=sql-server-ver17)
Describes how to replay a Transact-SQL script. | [Replay a Transact-SQL script (SQL Server Profiler)](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/replay-a-transact-sql-script-sql-server-profiler?view=sql-server-ver17)
Describes how to create a trace template. | [Create a trace template (SQL Server Profiler)](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/create-a-trace-template-sql-server-profiler?view=sql-server-ver17)
Describes how to modify a trace template. | [Modify trace templates](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/modify-trace-templates?view=sql-server-ver17)
Describes how to set global trace options. | [Set global trace options (SQL Server Profiler)](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/set-global-trace-options-sql-server-profiler?view=sql-server-ver17)
Describes how to find a value or data column while tracing. | [Find a value or data column while tracing (SQL Server Profiler)](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/find-a-value-or-data-column-while-tracing-sql-server-profiler?view=sql-server-ver17)
Describes how to derive a template from a running trace. | [Derive a template from a running trace (SQL Server Profiler)](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/derive-a-template-from-a-running-trace-sql-server-profiler?view=sql-server-ver17)
Describes how to derive a template from a trace file or trace table. | [Derive a template from a trace file or trace table (SQL Server Profiler)](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/derive-a-template-from-a-trace-file-or-trace-table-sql-server-profiler?view=sql-server-ver17)
Describes how to create a Transact-SQL script for running a trace. | [Create a Transact-SQL script for running a trace (SQL Server Profiler)](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/create-a-transact-sql-script-for-running-a-trace-sql-server-profiler?view=sql-server-ver17)
Describes how to export a trace template. | [Export a trace template (SQL Server Profiler)](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/export-a-trace-template-sql-server-profiler?view=sql-server-ver17)
Describes how to import a trace template. | [Import a trace template (SQL Server Profiler)](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/import-a-trace-template-sql-server-profiler?view=sql-server-ver17)
Describes how to extract a script from a trace. | [Extract a script from a trace (SQL Server Profiler)](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/extract-a-script-from-a-trace-sql-server-profiler?view=sql-server-ver17)
Describes how to correlate a trace with Windows performance log data. | [Correlate a trace with Windows performance log data](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/correlate-a-trace-with-windows-performance-log-data?view=sql-server-ver17)
Describes how to organize columns displayed in a trace. | [Organize columns displayed in a trace (SQL Server Profiler)](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/organize-columns-displayed-in-a-trace-sql-server-profiler?view=sql-server-ver17)
Describes how to start SQL Server Profiler. | [Run SQL Server Profiler](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/start-sql-server-profiler?view=sql-server-ver17)
Describes how to save traces and trace templates. | [Save traces and trace templates](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/save-traces-and-trace-templates?view=sql-server-ver17)
Describes how to modify trace templates. | [Modify trace templates](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/modify-trace-templates?view=sql-server-ver17)
Describes how to correlate a trace with Windows performance log data. | [Correlate a trace with Windows performance log data](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/correlate-a-trace-with-windows-performance-log-data?view=sql-server-ver17)
Describes how to view and analyze traces with SQL Server Profiler. | [View and analyze traces with SQL Server Profiler](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/view-and-analyze-traces-with-sql-server-profiler?view=sql-server-ver17)
Describes how to analyze deadlocks with SQL Server Profiler. | [Analyze deadlocks with SQL Server Profiler](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/analyze-deadlocks-with-sql-server-profiler?view=sql-server-ver17)
Describes how to analyze queries with SHOWPLAN results in SQL Server Profiler. | [Analyze queries with SHOWPLAN results in SQL Server Profiler](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/analyze-queries-with-showplan-results-in-sql-server-profiler?view=sql-server-ver17)
Describes how to filter traces with SQL Server Profiler. | [Filter traces with SQL Server Profiler](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/filter-traces-with-sql-server-profiler?view=sql-server-ver17)
Describes how to use the replay features of SQL Server Profiler. | [Replay Traces](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/replay-traces?view=sql-server-ver17)
Lists the context-sensitive help articles for SQL Server Profiler. | [SQL Server Profiler F1 Help](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/sql-server-profiler-f1-help?view=sql-server-ver17)
Lists the system stored procedures that are used by SQL Server Profiler to monitor performance and activity. | [SQL Server Profiler stored procedures](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sql-server-profiler-stored-procedures-transact-sql?view=sql-server-ver17)
[](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/sql-server-profiler?view=sql-server-ver17#extended-events-vs-sql-server-profiler)
## Extended Events vs. SQL Server Profiler
[Extended Events overview](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/extended-events?view=sql-server-ver17) and SQL Server Profiler are tools for monitoring and troubleshooting SQL Server performance. **SQL Server Profiler is deprecated and should only be used with Analysis Services**. Extended Events is the replacement for SQL Server Profiler and provides advanced troubleshooting capabilities not available elsewhere. The key differences are noted here to help with the migration from SQL Server Profiler to Extended Events.
[](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/sql-server-profiler?view=sql-server-ver17#extended-events-tool)
## Extended Events tool
[Extended Events overview](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/extended-events?view=sql-server-ver17) is a lightweight, highly scalable, and flexible event-handling system built into SQL Server.
Extended Events sessions typically consume fewer resources than SQL Trace and SQL Server Profiler, making them more suitable for production environments. Extended Events supports capturing events that are available in modern versions of SQL.
In contrast, the events available in SQL Trace/SQL Server Profiler are limited to features available in SQL Server 2008R2 and earlier. Extended Events provides superior filtering capabilities, a smaller default payload, and features not offered in Profiler, such as in-memory and aggregate targets and multi-target support.
For more information about Extended Events, see [Extended Events overview](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/extended-events?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/sql-server-profiler?view=sql-server-ver17#sql-server-profiler-tool)
## SQL Server Profiler tool
SQL Server Profiler is a graphical user interface that uses SQL Trace to capture activity for an instance of SQL Server or Analysis Services.
SQL Server Profiler can be resource-intensive if improperly configured, affecting server performance, especially when used on production servers. It has built-in templates to support quick tracing.
In summary, though SQL Server Profiler is an older tool that might be familiar to many users, Extended Events is a modern alternative that offers better performance, more detailed event information, and capabilities for troubleshooting and monitoring SQL Server instances not available elsewhere. Due to its advantages over Profiler, Extended Events is recommended for new tracing and monitoring work.
[](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/sql-server-profiler?view=sql-server-ver17#related-content)
## Related content
  * [Locks Event Category](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/locks-event-category?view=sql-server-ver17)
  * [Sessions Event Category](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/sessions-event-category?view=sql-server-ver17)
  * [Stored Procedures Event Category](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/stored-procedures-event-category?view=sql-server-ver17)
  * [TSQL Event Category](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/tsql-event-category?view=sql-server-ver17)
  * [Server Performance and Activity Monitoring](https://learn.microsoft.com/en-us/sql/relational-databases/performance/server-performance-and-activity-monitoring?view=sql-server-ver17)


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
  * [ Create a Trace - SQL Server Profiler ](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/create-a-trace-sql-server-profiler?source=recommendations)
Learn how to capture event data in SQL Server Profiler by creating a trace. Read about the various options you can specify for traces.
  * [ Templates - SQL Server Profiler ](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/sql-server-profiler-templates?source=recommendations)
Learn about the predefined templates SQL Server Profiler provides and how to use them. See how to create user-defined templates and change the default template.
  * [ Run SQL Server Profiler - SQL Server Profiler ](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/start-sql-server-profiler?source=recommendations)
Learn which programs and menus you can start SQL Server Profiler from and which connection contexts, templates, and filters are used with trace output.
  * [ Profiler Utility - SQL Server ](https://learn.microsoft.com/en-us/sql/tools/profiler-utility?source=recommendations)
The profiler utility launches the SQL Server Profiler tool. Optional arguments allow you to control how the application starts.
  * [ Use the SSMS XEvent Profiler - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/use-the-ssms-xe-profiler?source=recommendations)
The XEvent Profiler displays a live viewer of extended events. Learn why to use this profiler, key features, and how to get started viewing extended events.
  * [ View and Analyze Traces - SQL Server ](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/view-and-analyze-traces-with-sql-server-profiler?source=recommendations)
Find out how to use SQL Server Profiler to view trace data, find specific events, display object names, and troubleshoot problems.
  * [ SQL Trace - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/sql-trace/sql-trace?source=recommendations)
SQL Trace
  * [ Permissions Required - SQL Server Profiler ](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/permissions-required-to-run-sql-server-profiler?source=recommendations)
Find out which permissions you need to run SQL Server Profiler and replay traces, and learn which checks are performed during replays.


Show 5 more
Module
[ Describe performance monitoring - Training ](https://learn.microsoft.com/en-us/training/modules/describe-performance-monitoring/?source=recommendations)
Describe performance monitoring
Certification
[ Microsoft Certified: Azure Database Administrator Associate - Certifications ](https://learn.microsoft.com/en-us/credentials/certifications/azure-database-administrator-associate/?source=recommendations)
Administer an SQL Server database infrastructure for cloud, on-premises and hybrid relational databases using the Microsoft PaaS relational database offerings.
Mar 8, 4 PM - Mar 8, 4 PM
Experiment with what's next in AI-driven apps and agent design
* * *
  * Last updated on 02/21/2026


##  In this article
  1. [Deprecation notice](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/sql-server-profiler?view=sql-server-ver17#deprecation-notice)
  2. [Where's the Profiler?](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/sql-server-profiler?view=sql-server-ver17#wheres-the-profiler)
  3. [Capture and replay trace data](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/sql-server-profiler?view=sql-server-ver17#capture-and-replay-trace-data)
  4. [Use SQL Server Profiler](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/sql-server-profiler?view=sql-server-ver17#use-sql-server-profiler)
  5. [SQL Server Profiler concepts](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/sql-server-profiler?view=sql-server-ver17#sql-server-profiler-concepts)
  6. [SQL Server Profiler tasks](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/sql-server-profiler?view=sql-server-ver17#sql-server-profiler-tasks)
  7. [Extended Events vs. SQL Server Profiler](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/sql-server-profiler?view=sql-server-ver17#extended-events-vs-sql-server-profiler)
  8. [Extended Events tool](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/sql-server-profiler?view=sql-server-ver17#extended-events-tool)
  9. [SQL Server Profiler tool](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/sql-server-profiler?view=sql-server-ver17#sql-server-profiler-tool)
  10. [Related content](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/sql-server-profiler?view=sql-server-ver17#related-content)


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
[ Sign in ](https://learn.microsoft.com/en-us/sql/tools/sql-server-profiler/sql-server-profiler?view=sql-server-ver17)
[English (United States)](https://learn.microsoft.com/en-us/locale?target=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fsql%2Ftools%2Fsql-server-profiler%2Fsql-server-profiler%3Fview%3Dsql-server-ver17)
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
