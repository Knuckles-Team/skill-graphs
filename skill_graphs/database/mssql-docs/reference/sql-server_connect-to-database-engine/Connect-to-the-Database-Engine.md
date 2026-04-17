# Connect to the Database Engine
Feedback
Summarize this article for me
##  In this article
  1. [Prerequisites](https://learn.microsoft.com/en-us/sql/sql-server/connect-to-database-engine?view=sql-server-ver17&tabs=sqldb#prerequisites)
  2. [Connection options](https://learn.microsoft.com/en-us/sql/sql-server/connect-to-database-engine?view=sql-server-ver17&tabs=sqldb#connection-options)
  3. [Network protocol considerations](https://learn.microsoft.com/en-us/sql/sql-server/connect-to-database-engine?view=sql-server-ver17&tabs=sqldb#network-protocol-considerations)
  4. [Connect to Azure SQL](https://learn.microsoft.com/en-us/sql/sql-server/connect-to-database-engine?view=sql-server-ver17&tabs=sqldb#connect-to-azure-sql)
  5. [Connect to SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/connect-to-database-engine?view=sql-server-ver17&tabs=sqldb#connect-to-sql-server)
  6. [Run a Transact-SQL query](https://learn.microsoft.com/en-us/sql/sql-server/connect-to-database-engine?view=sql-server-ver17&tabs=sqldb#run-a-transact-sql-query)
  7. [Get help](https://learn.microsoft.com/en-us/sql/sql-server/connect-to-database-engine?view=sql-server-ver17&tabs=sqldb#get-help)
  8. [Related content](https://learn.microsoft.com/en-us/sql/sql-server/connect-to-database-engine?view=sql-server-ver17&tabs=sqldb#related-content)

Show 4 more
This article provides a high level overview for connecting to the SQL Server Database Engine, used by the following products and services:
  * SQL Server
  * Azure SQL Database
  * Azure SQL Managed Instance
  * Analytics Platform System (PDW)
  * Azure Synapse Analytics
  * SQL database in Microsoft Fabric
  * [SQL analytics endpoint and Warehouse in Microsoft Fabric](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to)


[](https://learn.microsoft.com/en-us/sql/sql-server/connect-to-database-engine?view=sql-server-ver17&tabs=sqldb#prerequisites)
## Prerequisites
You connect to the Database Engine using a _client tool_ or _client library_. Client tools run in a graphical user interface (GUI), or a command-line interface (CLI).
The following table describes some of the more common client tools.
Expand table
Client tool | Type | Operating system
---|---|---
**[SQL Server Management Studio (SSMS)](https://learn.microsoft.com/en-us/ssms/sql-server-management-studio-ssms)** | GUI | Windows
**[MSSQL extension for Visual Studio Code](https://learn.microsoft.com/en-us/sql/tools/visual-studio-code-extensions/mssql/mssql-extension-visual-studio-code?view=sql-server-ver17)** | GUI | Windows, macOS, Linux
**[sqlcmd](https://learn.microsoft.com/en-us/sql/tools/sqlcmd/sqlcmd-utility?view=sql-server-ver17)** | CLI | Windows, macOS, Linux
**[bcp](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17)** | CLI | Windows, macOS, Linux
Client tools include at least one client library. For more information about connecting with a client library, see [Connection modules for Microsoft SQL Database](https://learn.microsoft.com/en-us/sql/connect/sql-connection-libraries?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/sql-server/connect-to-database-engine?view=sql-server-ver17&tabs=sqldb#connection-options)
## Connection options
When you connect to the Database Engine, you must provide an _instance_ name (that is, the server or instance where the Database Engine is installed), a network _protocol_ , and a connection _port_ , in the following format:
text
Copy
```
[<protocol>:]<instance>[,<port>]

```

The protocol and port are optional because they have default values. Depending on the client tool and client library, they can be skipped.
If you use a custom TCP port for connecting to the Database Engine, you must separate it with a comma (`,`), because the colon (`:`) is used to specify the protocol.
Expand table
Setting | Values | Default | Details
---|---|---|---
**Protocol** |  `tcp` (TCP/IP), `np` (named pipes), or `lpc` (shared memory). |  `np` is the default when connecting to SQL Server.

`tcp` is the default when connecting to Azure SQL services. |  **Protocol** is optional, and is frequently excluded when connecting to SQL Server on the same computer as the client tool.

For more information, see [Network protocol considerations](https://learn.microsoft.com/en-us/sql/sql-server/connect-to-database-engine?view=sql-server-ver17&tabs=sqldb#network-protocol-considerations) in the next section.
**Instance** | The name of the server or instance. For example, `MyServer` or `MyServer\MyInstance`. | `localhost` | If the Database Engine is located on the same computer as the client tool, you might be able to connect using `localhost`, `127.0.0.1`, or even `.` (a single period).

If you're connecting to a named instance, you must specify the server name and the instance name, separated by a slash. For example, `MyServer\MyInstance`. A named instance on the local machine is specified by `.\MyInstance`. SQL Server Express uses `MyServer\SQLEXPRESS`.
**Port** | Any TCP port. | `1433` | The default TCP port for connecting to the default instance of SQL Server is `1433`. However, your infrastructure team might configure custom ports.

SQL Server on Windows, including SQL Server Express edition, can be configured as a named instance and might also have a custom port.

For connecting to Azure SQL services, see the [Connect to Azure SQL](https://learn.microsoft.com/en-us/sql/sql-server/connect-to-database-engine?view=sql-server-ver17&tabs=sqldb#connect-to-azure-sql) section.

For more information about custom ports with SQL Server, see [SQL Server Configuration Manager](https://learn.microsoft.com/en-us/sql/relational-databases/sql-server-configuration-manager?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/sql-server/connect-to-database-engine?view=sql-server-ver17&tabs=sqldb#network-protocol-considerations)
## Network protocol considerations
For SQL Server on Windows, when you connect to an instance on the same machine as the client tool, and depending on which edition is installed, the default protocol can be configured with multiple protocols, including named pipes (`np`), TCP/IP (`tcp`), and shared memory (`lpc`). Use the shared memory protocol for troubleshooting when you suspect the other protocols are configured incorrectly.
If you connect to SQL Server over a TCP/IP network, make sure that TCP/IP is enabled on the server as well. TCP/IP might be disabled by default on installations of SQL Server. For more information, see [Default SQL Server Network Protocol Configuration](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/default-sql-server-network-protocol-configuration?view=sql-server-ver17#default-configuration).
Connections to Azure SQL services, SQL Server on Linux, and SQL Server in containers, all use TCP/IP.
For both Azure SQL Database and Azure SQL Managed Instance, see [Azure SQL Database and Azure SQL Managed Instance connect and query articles](https://learn.microsoft.com/en-us/azure/azure-sql/database/connect-query-content-reference-guide).
[](https://learn.microsoft.com/en-us/sql/sql-server/connect-to-database-engine?view=sql-server-ver17&tabs=sqldb#connect-to-azure-sql)
## Connect to Azure SQL
This section provides information on connecting to Azure SQL services.
  * [Azure SQL Database](https://learn.microsoft.com/en-us/sql/sql-server/connect-to-database-engine?view=sql-server-ver17&tabs=sqldb#tabpanel_1_sqldb)
  * [Azure SQL Managed Instance](https://learn.microsoft.com/en-us/sql/sql-server/connect-to-database-engine?view=sql-server-ver17&tabs=sqldb#tabpanel_1_sqlmi)
  * [SQL Server on Azure VM](https://learn.microsoft.com/en-us/sql/sql-server/connect-to-database-engine?view=sql-server-ver17&tabs=sqldb#tabpanel_1_sqlvm)


To quickly connect to and query an Azure SQL Database from the Azure portal, use the [Azure portal Query editor for Azure SQL Database](https://learn.microsoft.com/en-us/azure/azure-sql/database/query-editor?view=azuresql-db&preserve-view=true).
For external connections, be aware of the secure-by-default [Azure SQL Database database-level firewall](https://learn.microsoft.com/en-us/azure/azure-sql/database/firewall-configure?view=azuresql-db&preserve-view=true).
Examples for application connections are available:
  * [Use .NET and the Microsoft.Data.SqlClient library](https://learn.microsoft.com/en-us/azure/azure-sql/database/azure-sql-dotnet-quickstart?view=azuresql-db&preserve-view=true)
  * [Use .NET and EF Core](https://learn.microsoft.com/en-us/azure/azure-sql/database/azure-sql-dotnet-entity-framework-core-quickstart?view=azuresql-db&preserve-view=true)
  * [Use Python with mssql-python](https://learn.microsoft.com/en-us/azure/azure-sql/database/azure-sql-python-quickstart?view=azuresql-db&preserve-view=true)
  * [Use Node.js with mssql](https://learn.microsoft.com/en-us/azure/azure-sql/database/azure-sql-javascript-mssql-quickstart?view=azuresql-db&preserve-view=true)


Connect to an Azure SQL Managed Instance in the same ways you connect to a SQL Server instance. For more information, see [Connect your application to Azure SQL Managed Instance](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/connect-application-instance?view=azuresql-mi&preserve-view=true).
You can also [configure a point-to-site connection to Azure SQL Managed Instance from on-premises](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/point-to-site-p2s-configure?view=azuresql-mi&preserve-view=true) or [connect to Azure SQL Managed Instance from an Azure VM](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/connect-vm-instance-configure?view=azuresql-mi&preserve-view=true).
Azure SQL Managed Instance can enforce a minimum [Transport Layer Security (TLS)](https://learn.microsoft.com/en-us/troubleshoot/sql/database-engine/connect/tls-1-2-support-microsoft-sql-server) version for application connections. For more information, see [Configure minimal TLS version in Azure SQL Managed Instance](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/minimal-tls-version-configure?view=azuresql-mi&preserve-view=true).
Connect to the **Public IP address** of the VM. For an example, see [Connect to SQL Server on a Windows virtual machine in the Azure portal](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/sql-vm-create-portal-quickstart#connect-to-sql-server).
[](https://learn.microsoft.com/en-us/sql/sql-server/connect-to-database-engine?view=sql-server-ver17&tabs=sqldb#connect-to-sql-server)
## Connect to SQL Server
This section provides information on connecting to SQL Server.
[](https://learn.microsoft.com/en-us/sql/sql-server/connect-to-database-engine?view=sql-server-ver17&tabs=sqldb#connect-to-sql-server-on-the-same-machine-as-the-client)
### Connect to SQL Server on the same machine as the client
You can connect to the local machine using named pipes (`np`), shared memory (`lpc`), or TCP/IP (`tcp`). Shared memory is the fastest, because it doesn't use the network interface.
If you use an IP address for your instance name and don't specify `tcp`, the protocol defaults to `np` (named pipes) if it's a configured protocol.
A named instance has a dynamically assigned TCP port. If you want to connect to a named instance, the SQL Server Browser service must be running on the server.
[](https://learn.microsoft.com/en-us/sql/sql-server/connect-to-database-engine?view=sql-server-ver17&tabs=sqldb#connect-to-a-default-sql-server-instance-on-the-same-machine)
#### Connect to a default SQL Server instance on the same machine
  1. If you're connecting to a server configured with default settings, use one of the following options:
     * `localhost`
     * `127.0.0.1`
     * `.` (a single period)
  2. If you're connecting to a custom TCP port, such as `51433`, use one of the following options:
     * `tcp:localhost,51433`
     * `127.0.0.1,51433`


[](https://learn.microsoft.com/en-us/sql/sql-server/connect-to-database-engine?view=sql-server-ver17&tabs=sqldb#connect-to-a-sql-server-named-instance-on-the-same-machine)
#### Connect to a SQL Server named instance on the same machine
In this example, the named instance is called `MyInstance`. Make sure the SQL Server Browser service is running, and use one of the following options:
  * `localhost\MyInstance`
  * `127.0.0.1\MyInstance`
  * `.\MyInstance`


[](https://learn.microsoft.com/en-us/sql/sql-server/connect-to-database-engine?view=sql-server-ver17&tabs=sqldb#connect-to-sql-server-on-the-network)
### Connect to SQL Server on the network
You can connect using a server name or an IP address. In this example, the server name `MyServer` resolves to `192.10.1.128`.
[](https://learn.microsoft.com/en-us/sql/sql-server/connect-to-database-engine?view=sql-server-ver17&tabs=sqldb#connect-to-a-default-sql-server-instance-on-the-network-using-named-pipes)
#### Connect to a default SQL Server instance on the network, using named pipes
To connect to a server on the local network with named pipes, use one of the following options:
  * `MyServer`
  * `np:MyServer`


On a local area network, connecting with TCP/IP might be faster than with named pipes.
[](https://learn.microsoft.com/en-us/sql/sql-server/connect-to-database-engine?view=sql-server-ver17&tabs=sqldb#connect-to-a-default-sql-server-instance-on-the-network-using-tcpip)
#### Connect to a default SQL Server instance on the network, using TCP/IP
  1. If you're connecting to a server configured with default TCP port `1433`, use one of the following options:
     * `tcp:MyServer`
     * `tcp:192.10.1.128`
  2. If you're connecting to a server configured with a custom TCP port, such as `51433`, use one of the following options:
     * `MyServer,51433`
     * `tcp:MyServer,51433`
     * `192.10.1.128,51433`
     * `tcp:192.10.1.128,51433`


[](https://learn.microsoft.com/en-us/sql/sql-server/connect-to-database-engine?view=sql-server-ver17&tabs=sqldb#connect-to-a-sql-server-named-instance-on-the-network-using-tcpip)
#### Connect to a SQL Server named instance on the network, using TCP/IP
In this example, the named instance is called `MyInstance`. Make sure the SQL Server Browser service is running on the server, and use one of the following options:
  * `tcp:MyServer\MyInstance`
  * `tcp:192.10.1.128\MyInstance`


[](https://learn.microsoft.com/en-us/sql/sql-server/connect-to-database-engine?view=sql-server-ver17&tabs=sqldb#connect-to-data-in-microsoft-fabric)
#### Connect to data in Microsoft Fabric
You can connect to Fabric Data Warehouse and SQL database in Fabric in much the same way you connect to an Azure SQL Database.
For complete details, see:
  * [Connect to Fabric Data Warehouse](https://learn.microsoft.com/en-us/fabric/data-warehouse/how-to-connect)
  * [Connect to SQL database in Fabric](https://learn.microsoft.com/en-us/fabric/database/sql/connect)


[](https://learn.microsoft.com/en-us/sql/sql-server/connect-to-database-engine?view=sql-server-ver17&tabs=sqldb#run-a-transact-sql-query)
## Run a Transact-SQL query
Once you connect successfully to the Database Engine using a client tool, you can execute a Transact-SQL (T-SQL) query or script.
In SQL Server Management Studio and Visual Studio Code, paste or type the query into a new query window.
For more information about running T-SQL queries in client tools, see:
  * [SQL Server Management Studio (SSMS)](https://learn.microsoft.com/en-us/ssms/quickstarts/ssms-connect-query-sql-server)
  * [Quickstart: Connect to and query a database with the MSSQL extension for Visual Studio Code](https://learn.microsoft.com/en-us/sql/tools/visual-studio-code-extensions/mssql/connect-database-visual-studio-code?view=sql-server-ver17)
  * [sqlcmd utility](https://learn.microsoft.com/en-us/sql/tools/sqlcmd/sqlcmd-run-transact-sql-script-files?view=sql-server-ver17)
  * [Azure portal query editor for Azure SQL Database](https://learn.microsoft.com/en-us/azure/azure-sql/database/query-editor)
  * [Query with the SQL query editor](https://learn.microsoft.com/en-us/fabric/database/sql/query-editor)


Some tools require a _batch separator_ to know that a query is ready to be executed. For example, you might need to put the `GO` separator at the end of a T-SQL query in **sqlcmd** to make sure that the T-SQL query runs.
[](https://learn.microsoft.com/en-us/sql/sql-server/connect-to-database-engine?view=sql-server-ver17&tabs=sqldb#get-help)
## Get help
  * [Create a valid connection string using the shared memory protocol](https://learn.microsoft.com/en-us/sql/tools/configuration-manager/aliases-sql-server-configuration-manager?view=sql-server-ver17)
  * [Create a valid connection string using TCP/IP](https://learn.microsoft.com/en-us/sql/tools/configuration-manager/aliases-sql-server-configuration-manager?view=sql-server-ver17)
  * [Troubleshoot connectivity issues in SQL Server](https://learn.microsoft.com/en-us/troubleshoot/sql/database-engine/connect/resolve-connectivity-errors-overview)
  * [Trace the network authentication process to the Database Engine](https://learn.microsoft.com/en-us/sql/relational-databases/database-engine-connection-open-network-trace?view=sql-server-ver17)


[](https://learn.microsoft.com/en-us/sql/sql-server/connect-to-database-engine?view=sql-server-ver17&tabs=sqldb#related-content)
## Related content
  * [Sign in to SQL Server](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/logging-in-to-sql-server?view=sql-server-ver17)
  * [What is SQL Server Management Studio (SSMS)?](https://learn.microsoft.com/en-us/ssms/sql-server-management-studio-ssms)
  * [What is the MSSQL extension for Visual Studio Code?](https://learn.microsoft.com/en-us/sql/tools/visual-studio-code-extensions/mssql/mssql-extension-visual-studio-code?view=sql-server-ver17)
  * [Configure Database Engine Instances (SQL Server)](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/configure-database-engine-instances-sql-server?view=sql-server-ver17)
  * [sqlcmd utility](https://learn.microsoft.com/en-us/sql/tools/sqlcmd/sqlcmd-utility?view=sql-server-ver17)


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
  * [ Databases - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/databases/databases?source=recommendations)
Learn about database schemas, tables, filegroups, logins, and roles. See how you can use the SQL Server Management Studio tool to work with databases.
  * [ Lesson 1: Connecting to the Database Engine - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/lesson-1-connecting-to-the-database-engine?source=recommendations)
Learn about the main tools of the Database Engine and how to connect to the engine and authorize more users.
  * [ Create a Database - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/databases/create-a-database?source=recommendations)
Create a database in SQL Server by using SQL Server Management Studio or Transact-SQL. View recommendations for the procedure.
  * [ What Is SQL Server? - SQL Server ](https://learn.microsoft.com/en-us/sql/sql-server/what-is-sql-server?source=recommendations)
An overview of the relational database engine and components of SQL Server
  * [ SQL Tools Overview - SQL Server ](https://learn.microsoft.com/en-us/sql/tools/overview-sql-tools?source=recommendations)
SQL query and management tools for SQL Server, Azure SQL (Azure SQL database, Azure SQL managed instance, SQL virtual machines), and Azure Synapse Analytics.
  * [ SQL Server Help and Feedback - SQL Server ](https://learn.microsoft.com/en-us/sql/sql-server/sql-server-get-help?source=recommendations)
A resource for finding ways to get help with your issue or submit feedback for either the SQL Server product, or the SQL Server technical documentation.
  * [ What's New in SQL Server 2022 - SQL Server ](https://learn.microsoft.com/en-us/sql/sql-server/what-s-new-in-sql-server-2022?source=recommendations)
Learn about new features for SQL Server 2022 (16.x), which gives you choices of development languages, data types, environments, and operating systems.


Show 4 more
Module
[ Understand client-server communication in PostgreSQL - Training ](https://learn.microsoft.com/en-us/training/modules/understand-client-server-communication-postgresql/?source=recommendations)
PostgreSQL is a client-server system, which allows many clients to connect to a central server. In this module you learn how PostgreSQL manages connections from clients, and looking at some common PostgreSQL client tools.
Certification
[ Microsoft Certified: Azure Database Administrator Associate - Certifications ](https://learn.microsoft.com/en-us/credentials/certifications/azure-database-administrator-associate/?source=recommendations)
Administer an SQL Server database infrastructure for cloud, on-premises and hybrid relational databases using the Microsoft PaaS relational database offerings.
Mar 8, 4 PM - Mar 8, 4 PM
Experiment with what's next in AI-driven apps and agent design
* * *
  * Last updated on 01/29/2026


##  In this article
  1. [Prerequisites](https://learn.microsoft.com/en-us/sql/sql-server/connect-to-database-engine?view=sql-server-ver17&tabs=sqldb#prerequisites)
  2. [Connection options](https://learn.microsoft.com/en-us/sql/sql-server/connect-to-database-engine?view=sql-server-ver17&tabs=sqldb#connection-options)
  3. [Network protocol considerations](https://learn.microsoft.com/en-us/sql/sql-server/connect-to-database-engine?view=sql-server-ver17&tabs=sqldb#network-protocol-considerations)
  4. [Connect to Azure SQL](https://learn.microsoft.com/en-us/sql/sql-server/connect-to-database-engine?view=sql-server-ver17&tabs=sqldb#connect-to-azure-sql)
  5. [Connect to SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/connect-to-database-engine?view=sql-server-ver17&tabs=sqldb#connect-to-sql-server)
  6. [Run a Transact-SQL query](https://learn.microsoft.com/en-us/sql/sql-server/connect-to-database-engine?view=sql-server-ver17&tabs=sqldb#run-a-transact-sql-query)
  7. [Get help](https://learn.microsoft.com/en-us/sql/sql-server/connect-to-database-engine?view=sql-server-ver17&tabs=sqldb#get-help)
  8. [Related content](https://learn.microsoft.com/en-us/sql/sql-server/connect-to-database-engine?view=sql-server-ver17&tabs=sqldb#related-content)


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
[ Sign in ](https://learn.microsoft.com/en-us/sql/sql-server/connect-to-database-engine?view=sql-server-ver17&tabs=sqldb)
[English (United States)](https://learn.microsoft.com/en-us/locale?target=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fsql%2Fsql-server%2Fconnect-to-database-engine%3Fview%3Dsql-server-ver17)
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
