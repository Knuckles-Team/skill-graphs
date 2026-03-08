# SQLdiag utility
Feedback
Summarize this article for me
##  In this article
  1. [Syntax](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#syntax)
  2. [Arguments](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#arguments)
  3. [Security requirements](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#security-requirements)
  4. [Performance considerations](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#performance-considerations)
  5. [Required disk space](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#required-disk-space)
  6. [Configuration files](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#configuration-files)
  7. [Output folder](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#output-folder)
  8. [Data collection process](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#data-collection-process)
  9. [Stop data collection](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#stop-data-collection)
  10. [Stop SQLdiag using sqldiag.stop file](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#stop-sqldiag-using-sqldiagstop-file)
  11. [Automatically start and stop SQLdiag](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#automatically-start-and-stop-sqldiag)
  12. [Run SQLdiag as a service](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#run-sqldiag-as-a-service)
  13. [Run multiple instances of SQLdiag](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#run-multiple-instances-of-sqldiag)
  14. [Collect diagnostic data from clustered SQL Server instances](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#collect-diagnostic-data-from-clustered-sql-server-instances)
  15. [Related content](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#related-content)

Show 11 more
**Applies to:** ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to)
The **SQLdiag** utility is a general purpose diagnostics collection utility that can be run as a console application or as a service. You can use **SQLdiag** to collect logs and data files from SQL Server and other types of servers, and use it to monitor your servers over time or troubleshoot specific problems with your servers. **SQLdiag** is intended to expedite and simplify diagnostic information gathering for Microsoft Customer Support Services.
This utility might be changed, and applications or scripts that rely on its command line arguments or behavior might not work correctly in future releases.
**SQLdiag** can collect the following types of diagnostic information:
  * Windows performance logs
  * Windows event logs
  * SQL Server Profiler traces
  * SQL Server blocking information
  * SQL Server configuration information


You can specify what types of information you want **SQLdiag** to collect by editing the configuration file `SQLdiag.xml`, which is described in a following section.
[](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#syntax)
## Syntax
Console
Copy
```
sqldiag
    { [ /? ] }
    |
    {
      [ /I configuration_file ]
      [ /O output_folder_path ]
      [ /P support_folder_path ]
      [ /N output_folder_management_option ]
      [ /M machine1 [ machine2 machineN ] | @machinelistfile ]
      [ /C file_compression_type ]
      [ /B [+]start_time ]
      [ /E [+]stop_time ]
      [ /A SQLdiag_application_name ]
      [ /T { tcp [ ,port ] | np | lpc } ]
      [ /Q ] [ /G ] [ /R ] [ /U ] [ /L ] [ /X ]
    }
    |
    { [ START | STOP | STOP_ABORT ] }
    |
    { [ START | STOP | STOP_ABORT ] /A SQLdiag_application_name }

```

[](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#arguments)
## Arguments
[](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#section)
#### /?
Displays usage information.
[](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#i-configuration_file)
#### /I _configuration_file_
Sets the configuration file for **SQLdiag** to use. By default, `/I` is set to `SQLdiag.xml`.
[](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#o-output_folder_path)
#### /O _output_folder_path_
Redirects **SQLdiag** output to the specified folder. If the `/O` option isn't specified, **SQLdiag** output is written to a subfolder named `SQLDIAG` under the **SQLdiag** startup folder. If the `SQLDIAG` folder doesn't exist, **SQLdiag** attempts to create it.
The output folder location is relative to the support folder location that can be specified with `/P`. To set an entirely different location for the output folder, specify the full directory path for `/O`.
[](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#p-support_folder_path)
#### /P _support_folder_path_
Sets the support folder path. By default, `/P` is set to the folder where the **SQLdiag** executable resides. The support folder contains **SQLdiag** support files, such as the XML configuration file, Transact-SQL scripts, and other files that the utility uses during diagnostics collection. If you use this option to specify an alternate support files path, **SQLdiag** automatically copies the support files it requires to the specified folder if they don't already exist.
To set your current folder as the support path, specify `%cd%` on the command line as follows:
Console
Copy
```
sqldiag /P %cd%

```

[](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#n-output_folder_management_option)
#### /N _output_folder_management_option_
Sets whether **SQLdiag** overwrites or renames the output folder when it starts up. Available options:
  * 1 = Overwrites the output folder (default)
  * 2 = When **SQLdiag** starts up, it renames the output folder to `SQLDIAG_00001`, `SQLDIAG_00002`, and so on. After renaming the current output folder, **SQLdiag** writes output to the default output folder `SQLDIAG`.


**SQLdiag** doesn't append output to the current output folder when it starts up. It can only overwrite the default output folder (option 1) or rename the folder (option 2), and then it writes output to the new default output folder named `SQLDIAG`.
[](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#m-machine1--machine2-machinen---machinelistfile)
#### /M _machine1_ [ _machine2_ _machineN_ ] | _@machinelistfile_
Overrides the machines specified in the configuration file. By default the configuration file is `SQLdiag.xml`, or is set with the `/I` parameter. When specifying more than one machine, separate each machine name with a space.
The _@machinelistfile_ option specifies a machine list file name to be stored in the configuration file.
[](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#c-file_compression_type)
#### /C _file_compression_type_
Sets the type of file compression used on the **SQLdiag** output folder files. Available options:
  * 0 = none (default)
  * 1 = uses NTFS compression


[](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#b-start_time)
#### /B [+]_start_time_
Specifies the date and time to start collecting diagnostic data in the following format: `yyyyMMdd_HH:mm:ss`
The time is specified using 24-hour notation. For example, 2:00 P.M. should be specified as `14:00:00`.
Use `+` without the date (HH:mm:ss only) to specify a time that is relative to the current date and time. For example, if you specify `/B +02:00:00`, **SQLdiag** waits 2 hours before it starts collecting information.
Don't insert a space between `+` and the specified _start_time_.
If you specify a start time that is in the past, **SQLdiag** forcibly changes the start date so the start date and time are in the future. For example, if you specify `/B 01:00:00` and the current time is 08:00:00, **SQLdiag** forcibly changes the start date so that the start date is the next day.
**SQLdiag** uses the local time on the computer where the utility is running.
[](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#e-stop_time)
#### /E [+]_stop_time_
Specifies the date and time to stop collecting diagnostic data in the following format: `yyyyMMdd_HH:mm:ss`
The time is specified using 24-hour notation. For example, 2:00 P.M. should be specified as `14:00:00`.
Use `+` without the date (HH:mm:ss only) to specify a time that is relative to the _start_ date and time. For example, if you specify a start time and end time by using `/B +02:00:00 /E +03:00:00`, **SQLdiag** waits 2 hours before it starts collecting information, then collects information for 3 hours before it stops and exits. If `/B` isn't specified, **SQLdiag** starts collecting diagnostics immediately and ends at the date and time specified by `/E`.
Don't insert a space between `+` and the specified _start_time_ or _end_time_.
**SQLdiag** uses the local time on the computer where the utility is running.
[](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#a-sqldiag_application_name)
#### /A _SQLdiag_application_name_
Enables running multiple instances of the **SQLdiag** utility against the same SQL Server instance.
Each _SQLdiag_application_name_ identifies a different instance of **SQLdiag**. No relationship exists between a _SQLdiag_application_name_ instance and a SQL Server instance name.
_SQLdiag_application_name_ can be used to start or stop a specific instance of the **SQLdiag** service.
In this example, replace `<SQLdiag_application_name>` with the appropriate value for _SQLdiag_application_name_ :
Console
Copy
```
sqldiag START /A <SQLdiag_application_name>

```

It can also be used with the `/R` option to register a specific instance of **SQLdiag** as a service. In this example, replace `<SQLdiag_application_name>` with the appropriate value for _SQLdiag_application_name_ :
Console
Copy
```
sqldiag /R /A <SQLdiag_application_name>

```

**SQLdiag** automatically prefixes `DIAG$` to the instance name specified for _SQLdiag_application_name_. This provides a sensible service name if you register **SQLdiag** as a service.
[](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#t-protocol)
#### /T _protocol_
Connects to an instance of SQL Server using one of the following protocol values.
Expand table
Protocol (and port) | Description
---|---
**tcp [ ,_port_ ]** | Transmission Control Protocol/Internet Protocol (TCP/IP). You can optionally specify a port number for the connection.
**np** | Named pipes. By default, the default instance of SQL Server listens on named pipe `\\.\pipe\sql\query` and `\\.\pipe\MSSQL$<instancename>\sql\query` for a named instance. You can't connect to an instance of SQL Server by using an alternate pipe name.
**lpc** | Local procedure call. This shared memory protocol is available if the client is connecting to an instance of SQL Server on the same computer.
[](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#q)
#### /Q
Runs **SQLdiag** in quiet mode. `/Q` suppresses all prompts, such as password prompts.
[](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#g)
#### /G
Runs **SQLdiag** in generic mode. When `/G` is specified, on startup **SQLdiag** doesn't enforce SQL Server connectivity checks or verify that the user is a member of the **sysadmin** fixed server role. Instead, **SQLdiag** defers to Windows to determine whether a user has the appropriate rights to gather each requested diagnostic.
If `/G` isn't specified, **SQLdiag** checks to determine whether the user is a member of the Windows **Administrators** group, and doesn't collect SQL Server diagnostics if the user isn't an **Administrators** group member.
[](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#r)
#### /R
Registers **SQLdiag** as a service. Any command line arguments that are specified when you register **SQLdiag** as a service are preserved for future runs of the service.
When **SQLdiag** is registered as a service, the default service name is `SQLDIAG`. You can change the service name by using the `/A` argument.
Use the `START` command line argument to start the service:
Console
Copy
```
sqldiag START

```

You can also use the `net start` command to start the service:
Console
Copy
```
net start SQLDIAG

```

[](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#u)
#### /U
Unregisters **SQLdiag** as a service.
Use the `/A` argument also if unregistering a named **SQLdiag** instance.
[](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#l)
#### /L
Runs **SQLdiag** in continuous mode when a start time or end time is also specified with the `/B` or `/E` arguments, respectively. **SQLdiag** automatically restarts after diagnostics collection stops due to a scheduled shutdown. For example, by using the `/E` or the `/X` arguments.
**SQLdiag** ignores the `/L` argument if a start time or end time isn't specified by using the `/B` and `/E` command line arguments.
Using `/L` doesn't imply the service mode. To use `/L` when running **SQLdiag** as a service, specify it on the command line when you register the service.
[](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#x)
#### /X
Runs **SQLdiag** in snapshot mode. **SQLdiag** takes a snapshot of all configured diagnostics and then shuts down automatically.
[](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#start--stop--stop_abort)
#### START | STOP | STOP_ABORT
Starts or stops the **SQLdiag** service. `STOP_ABORT` forces the service to shut down as quickly as possible without finishing collection of diagnostics it's currently collecting.
When these service control arguments are used, they must be the first argument used on the command line. For example:
Console
Copy
```
sqldiag START

```

Only the `/A` argument, which specifies a named instance of **SQLdiag** , can be used with `START`, `STOP`, or `STOP_ABORT` to control a specific instance of the **SQLdiag** service. In this example, replace `<SQLdiag_application_name>` with the appropriate value for _SQLdiag_application_name_ :
Console
Copy
```
sqldiag START /A <SQLdiag_application_name>

```

[](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#security-requirements)
## Security requirements
Unless **SQLdiag** is run in generic mode (by specifying the `/G` command line argument), the user who runs **SQLdiag** must be a member of the Windows **Administrators** group and a member of the SQL Server **sysadmin** fixed server role. By default, **SQLdiag** connects to SQL Server by using Windows Authentication, but it also supports SQL Server Authentication.
[](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#performance-considerations)
## Performance considerations
The performance effects of running **SQLdiag** depend on the type of diagnostic data you have configured it to collect. For example, if you have configured **SQLdiag** to collect SQL Server Profiler tracing information, the more event classes you choose to trace, the more your server performance is affected.
The performance impact of running **SQLdiag** is approximately equivalent to the sum of the costs of collecting the configured diagnostics separately. For example, collecting a trace with **SQLdiag** incurs the same performance cost as collecting it with SQL Server Profiler. The performance impact of using **SQLdiag** is negligible.
[](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#required-disk-space)
## Required disk space
Because **SQLdiag** can collect different types of diagnostic information, the free disk space that is required to run **SQLdiag** varies. The amount of diagnostic information collected depends on the nature and volume of the workload that the server is processing and might range from a few megabytes to several gigabytes.
[](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#configuration-files)
## Configuration files
On startup, **SQLdiag** reads the configuration file and the command line arguments that have been specified. You specify the types of diagnostic information that **SQLdiag** collects in the configuration file. By default, **SQLdiag** uses the `SQLdiag.xml` configuration file, which is extracted each time the tool runs and is located in the **SQLdiag** utility startup folder. The configuration file uses the XML schema, SQLDiag_schema.xsd, which is also extracted into the utility startup directory from the executable file each time **SQLdiag** runs.
[](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#edit-the-configuration-files)
### Edit the configuration files
You can copy and edit `SQLdiag.xml` to change the types of diagnostic data that **SQLdiag** collects. When editing the configuration file always use an XML editor that can validate the configuration file against its XML schema, such as Management Studio. You shouldn't edit `SQLdiag.xml` directly. Instead, make a copy of `SQLdiag.xml` and rename it to a new file name in the same folder. Then edit the new file, and use the `/I` argument to pass it to **SQLdiag**.
[](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#edit-the-configuration-file-when-sqldiag-runs-as-a-service)
### Edit the configuration file when SQLdiag runs as a service
If you have already run **SQLdiag** as a service and need to edit the configuration file, unregister the `SQLDIAG` service by specifying the `/U` command line argument and then re-register the service by using the `/R` command line argument. Unregistering and re-registering the service removes old configuration information that was cached in the Windows registry.
[](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#output-folder)
## Output folder
If you don't specify an output folder with the `/O` argument, **SQLdiag** creates a subfolder named `SQLDIAG` under the **SQLdiag** startup folder. For diagnostic information collection that involves high volume tracing, such as SQL Server Profiler, make sure that the output folder is on a local drive with enough space to store the requested diagnostic output.
When **SQLdiag** is restarted, it overwrites the contents of the output folder. To avoid this, specify `/N 2` on the command line.
[](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#data-collection-process)
## Data collection process
When **SQLdiag** starts, it performs the initialization checks necessary to collect the diagnostic data that have been specified in `SQLdiag.xml`. This process might take several seconds. After **SQLdiag** has started collecting diagnostic data when it runs as a console application, a message displays informing you that **SQLdiag** collection has started and that you can press CTRL+C to stop it. When **SQLdiag** is run as a service, a similar message is written to the Windows event log.
If you're using **SQLdiag** to diagnose a problem that you can reproduce, wait until you receive this message before you reproduce the problem on your server.
**SQLdiag** collects most diagnostic data in parallel. All diagnostic information is collected by connecting to tools, such as the SQL Server **sqlcmd** utility or the Windows command processor, except when information is collected from Windows performance logs and event logs. **SQLdiag** uses one worker thread per computer to monitor the diagnostic data collection of these other tools, often simultaneously waiting for several tools to complete. During the collection process, **SQLdiag** routes the output from each diagnostic to the output folder.
[](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#stop-data-collection)
## Stop data collection
After **SQLdiag** starts collecting diagnostic data, it continues to do so unless you stop it manually via `Ctrl+C`, or you create a `sqldiag.stop` file, or you configure it to stop at a specified time. You can configure **SQLdiag** to stop at a specific time by using the `/E` argument, or by using the `/X` argument, which causes **SQLdiag** to run in snapshot mode.
When **SQLdiag** stops, it stops all diagnostics it has started. For example, it stops SQL Server Profiler traces it was collecting, it stops executing Transact-SQL scripts it was running, and it stops any sub processes it has spawned during data collection. After diagnostic data collection has completed, **SQLdiag** exits.
[](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#stop-sqldiag-when-running-as-a-console-application)
### Stop SQLdiag when running as a console application
If you're running **SQLdiag** as a console application, press CTRL+C in the console window where **SQLdiag** is running to stop it. After you press CTRL+C, a message displays in the console window informing you that **SQLdiag** data collection is ending, and that you should wait until the process shuts down, which might take several minutes.
Press Ctrl+C twice to terminate all child diagnostic processes and immediately terminate the application.
[](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#stop-sqldiag-when-running-as-a-service)
### Stop SQLdiag when running as a service
If you're running **SQLdiag** as a service, run `sqldiag STOP` in the **SQLdiag** startup folder to stop it. Or, you can stop the **SQLdiag** services in the **Services.msc** applet.
Pausing the **SQLdiag** service isn't supported. If you attempt to pause the **SQLdiag** service, it stops after it finishes collecting the diagnostics that it was collecting when you paused it. If you restart **SQLdiag** after stopping it, the application restarts and overwrites the output folder. To avoid overwriting the output folder, specify `/N 2` on the command line.
If you're running multiple instances of **SQLdiag** on the same computer, you can also pass the **SQLdiag** instance name to on the command line when you stop the service. For example, to stop a **SQLdiag** instance named Instance1, use the following syntax:
Console
Copy
```
sqldiag STOP /A Instance1

```

`/A` is the only command-line argument that can be used with `START`, `STOP`, or `STOP_ABORT`. If you need to specify a named instance of **SQLdiag** with one of the service control verbs, specify `/A` after the control verb on the command line as shown in the previous syntax example. When control verbs are used, they must be the first argument on the command line.
To stop the service as quickly as possible, run `sqldiag STOP_ABORT` in the utility startup folder. This command aborts any diagnostics collecting currently being performed without waiting for them to finish.
Use `sqldiag STOP` or `sqldiag STOP_ABORT` to stop the **SQLdiag** service. Don't use the Windows Services Console to stop **SQLdiag** or other SQL Server services.
[](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#stop-sqldiag-using-sqldiagstop-file)
## Stop SQLdiag using sqldiag.stop file
**SQLdiag** also shuts down automatically when it finds a file named `sqldiag.stop` in the utility's `\Output` folder. This option applies regardless if **SQLdiag** runs as a console app or as a service. Creating a `.stop` file can be useful when you want to programmatically shut down **SQLdiag** after some event occurs, but you don't know in advance the time that this event occurs. The contents of the `sqldiag.stop` file are irrelevant. One option, besides manually creating the file, is to use a command like the following in a batch file to create `sqldiag.stop`:
Console
Copy
```
ECHO stop > F:\PSSDIAG\Output\sqldiag.stop

```

Another option is to use PowerShell:
PowerShell
Copy
```
Set-Content -Value "stop" -Path "F:\PSSDIAG\Output\sqldiag.stop"

```

[](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#automatically-start-and-stop-sqldiag)
## Automatically start and stop SQLdiag
To automatically start and stop diagnostic data collection at a specified time, use the `/B <start_time>` and `/E <stop_time>` arguments, using 24-hour notation. For example, if you're troubleshooting a problem that consistently appears at approximately 02:00:00, you can configure **SQLdiag** to automatically start collecting diagnostic data at 01:45 and automatically stop at 03:00:00.
Use the `/B` and `/E` arguments to specify the start and stop time. Use 24-hour notation to specify an exact start and stop date and time with the general format yyyyMMdd_HH:mm:ss. The following example starts data collection at 01:45 and stops it at 3:00.
Console
Copy
```
sqldiag /B 01:45:00 /E 03:00:00

```

To specify a relative start or stop time, prefix the start and stop time with `+` and omit the date portion (yyyyMMdd_) as shown in the following example. This causes **SQLdiag** to wait one hour before it starts collecting information, then it collects information for two and a half hours before it stops and exits:
Console
Copy
```
sqldiag /B +01:00:00 /E +02:30:00

```

When a relative _start_time_ is specified, **SQLdiag** starts at a time that is relative to the current date and time. When a relative _end_time_ is specified, **SQLdiag** ends at a time that is relative to the specified _start_time_. If the start or end date and time that you have specified is in the past, **SQLdiag** forcibly changes the start date so that the start date and time are in the future.
This has important implications on the start and end dates you choose. Consider the following example:
Console
Copy
```
sqldiag /B +01:00:00 /E 08:30:00

```

If the current time is 08:00, the end time passes before diagnostic collection actually begins. Because **SQLdiag** automatically adjusts start and end dates to the next day when they occur in the past, in this example diagnostic collection starts at 09:00 today (a relative start time has been specified at 1 hour from now using `+`) and continues collecting until 08:30 the following morning.
[](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#stop-and-restart-sqldiag-to-collect-daily-diagnostics)
### Stop and restart SQLdiag to collect daily diagnostics
To collect a specified set of diagnostics on a daily basis without having to manually start and stop **SQLdiag** , use the `/L` argument. The `/L` argument causes **SQLdiag** to run continuously by automatically restarting itself after a scheduled shutdown. When `/L` is specified, and **SQLdiag** stops because it has reached the end time specified with the `/E` argument, or it stops because it's being run in snapshot mode by using the `/X` argument, **SQLdiag** restarts instead of exiting.
The following example specifies that **SQLdiag** run in continuous mode to automatically restart after diagnostic data collecting occurs between 03:00:00 and 05:00:00.
Console
Copy
```
sqldiag /B 03:00:00 /E 05:00:00 /L

```

The following example specifies that **SQLdiag** run in continuous mode to automatically restart after taking a diagnostic data snapshot at 03:00:00.
Console
Copy
```
sqldiag /B 03:00:00 /X /L

```

[](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#run-sqldiag-as-a-service)
## Run SQLdiag as a service
When you want to use **SQLdiag** to collect diagnostic data for long periods of time during which you might need to sign out of the computer on which **SQLdiag** is running, you can run it as a service.
[](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#register-sqldiag-to-run-as-a-service)
### Register SQLdiag to run as a service
You can register **SQLdiag** to run as a service by specifying the `/R` argument at the command line. This registers **SQLdiag** to run as a service. The **SQLdiag** service name is `SQLDIAG`. Any other arguments you specify on the command line when you register **SQLdiag** as a service are preserved and reused when the service is started.
To change the default `SQLDIAG` service name, use the `/A` command-line argument to specify another name. **SQLdiag** automatically prefixes DIAG$ to any **SQLdiag** instance name specified with `/A` to create sensible service names.
[](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#unregister-the-sqldiag-service)
### Unregister the SQLDIAG service
To unregister the service, specify the `/U` argument. Unregistering **SQLdiag** as a service also deletes the Windows registry keys of the service.
[](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#start-or-restart-the-sqldiag-service)
### Start or restart the SQLDIAG service
To start or restart the `SQLDIAG` service, run `sqldiag START` from the command line.
If you're running multiple instances of **SQLdiag** by using the `/A` argument, you can also pass the **SQLdiag** instance name on the command line when you start the service. For example, to start a **SQLdiag** instance named Instance1, use the following syntax:
Console
Copy
```
sqldiag START /A Instance1

```

You can also use the `net start` command to start the `SQLDIAG` service.
When you restart **SQLdiag** , it overwrites the contents in the current output folder. To avoid this, specify `/N 2` on the command line to rename the output folder when the utility starts.
Pausing the **SQLdiag** service isn't supported.
[](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#run-multiple-instances-of-sqldiag)
## Run multiple instances of SQLdiag
Run multiple instances of **SQLdiag** on the same computer by specifying `/A <SQLdiag_application_name>` on the command line. This is useful for collecting different sets of diagnostics simultaneously from the same SQL Server instance. For example, you can configure a named instance of **SQLdiag** to continuously perform lightweight data collection. Then, if a specific problem occurs on SQL Server, you can run the default **SQLdiag** instance to collect diagnostics for that problem, or to gather a set of diagnostics that Microsoft Customer Support Services asks you to gather to diagnose a problem.
[](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#collect-diagnostic-data-from-clustered-sql-server-instances)
## Collect diagnostic data from clustered SQL Server instances
**SQLdiag** supports collecting diagnostic data from clustered SQL Server instances. To gather diagnostics from clustered SQL Server instances, make sure that `"."` is specified for the `name` attribute of the `<Machine>` element in the configuration file `SQLdiag.xml` and don't specify the `/G` argument on the command line. By default, `"."` is specified for the `name` attribute in the configuration file and the `/G` argument is turned off. Typically, you don't need to edit the configuration file or change the command line arguments when collecting from a clustered SQL Server instance.
When `"."` is specified as the machine name, **SQLdiag** detects that it's running on a cluster, and simultaneously retrieves diagnostic information from all virtual instances of SQL Server that are installed on the cluster. If you want to collect diagnostic information from only one virtual instance of SQL Server that is running on a computer, specify that virtual SQL Server for the `name` attribute of the `<Machine>` element in `SQLdiag.xml`.
To collect SQL Server Profiler trace information from clustered SQL Server instances, administrative shares (ADMIN$) must be enabled on the cluster.
[](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#related-content)
## Related content
  * [SQL command-line utilities (Database Engine)](https://learn.microsoft.com/en-us/sql/tools/command-prompt-utility-reference-database-engine?view=sql-server-ver17)


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
  * [ Troubleshooting and diagnostic tools for on-premises and hybrid scenarios - SQL Server ](https://learn.microsoft.com/en-us/troubleshoot/sql/tools/sql-support-troubleshooting-diagnostic-tools?source=recommendations)
This article describes which tools Microsoft technical support uses for troubleshooting SQL Server hybrid issues.
  * [ sys.dm_os_cluster_nodes (Transact-SQL) - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/sys-dm-os-cluster-nodes-transact-sql?source=recommendations)
sys.dm_os_cluster_nodes (Transact-SQL)
  * [ sp_server_diagnostics (Transact-SQL) - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-server-diagnostics-transact-sql?source=recommendations)
sp_server_diagnostics captures diagnostic data and health information about SQL Server to detect potential failures.
  * [ log_shipping_monitor_primary (Transact-SQL) - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/system-tables/log-shipping-monitor-primary-transact-sql?source=recommendations)
log_shipping_monitor_primary (Transact-SQL)
  * [ Transactions: availability groups & database mirroring - SQL Server Always On ](https://learn.microsoft.com/en-us/sql/database-engine/availability-groups/windows/transactions-always-on-availability-and-database-mirroring?source=recommendations)
Transactions - availability groups and database mirroring


Show 2 more
Learning path
[ Run high-performance computing (HPC) applications on Azure - Training ](https://learn.microsoft.com/en-us/training/paths/run-high-performance-computing-applications-azure/?source=recommendations)
Azure HPC is a purpose-built cloud capability for HPC & AI workload, using leading-edge processors and HPC-class InfiniBand interconnect, to deliver the best application performance, scalability, and value. Azure HPC enables users to unlock innovation, productivity, and business agility, through a highly available range of HPC & AI technologies that can be dynamically allocated as your business and technical needs change. This learning path is a series of modules that help you get started on Azure HPC - you
Mar 8, 4 PM - Mar 8, 4 PM
Experiment with what's next in AI-driven apps and agent design
* * *
  * Last updated on 12/16/2025


##  In this article
  1. [Syntax](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#syntax)
  2. [Arguments](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#arguments)
  3. [Security requirements](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#security-requirements)
  4. [Performance considerations](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#performance-considerations)
  5. [Required disk space](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#required-disk-space)
  6. [Configuration files](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#configuration-files)
  7. [Output folder](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#output-folder)
  8. [Data collection process](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#data-collection-process)
  9. [Stop data collection](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#stop-data-collection)
  10. [Stop SQLdiag using sqldiag.stop file](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#stop-sqldiag-using-sqldiagstop-file)
  11. [Automatically start and stop SQLdiag](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#automatically-start-and-stop-sqldiag)
  12. [Run SQLdiag as a service](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#run-sqldiag-as-a-service)
  13. [Run multiple instances of SQLdiag](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#run-multiple-instances-of-sqldiag)
  14. [Collect diagnostic data from clustered SQL Server instances](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#collect-diagnostic-data-from-clustered-sql-server-instances)
  15. [Related content](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17#related-content)

Show 6 more
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
[ Sign in ](https://learn.microsoft.com/en-us/sql/tools/sqldiag-utility?view=sql-server-ver17)
[English (United States)](https://learn.microsoft.com/en-us/locale?target=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fsql%2Ftools%2Fsqldiag-utility%3Fview%3Dsql-server-ver17)
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
