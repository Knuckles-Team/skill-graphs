# Stored procedures (Database Engine)
Feedback
Summarize this article for me
##  In this article
  1. [Benefits of using stored procedures](https://learn.microsoft.com/en-us/sql/relational-databases/stored-procedures/stored-procedures-database-engine?view=sql-server-ver17#benefits-of-using-stored-procedures)
  2. [Types of stored procedures](https://learn.microsoft.com/en-us/sql/relational-databases/stored-procedures/stored-procedures-database-engine?view=sql-server-ver17#types-of-stored-procedures)
  3. [Related tasks](https://learn.microsoft.com/en-us/sql/relational-databases/stored-procedures/stored-procedures-database-engine?view=sql-server-ver17#related-tasks)
  4. [Related content](https://learn.microsoft.com/en-us/sql/relational-databases/stored-procedures/stored-procedures-database-engine?view=sql-server-ver17#related-content)


**Applies to:** ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure SQL Database](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure SQL Managed Instance](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure Synapse Analytics](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Analytics Platform System (PDW)](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL database in Microsoft Fabric](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to)
A stored procedure in SQL Server is a group of one or more Transact-SQL statements, or a reference to a Microsoft .NET Framework common runtime language (CLR) method. Procedures resemble constructs in other programming languages because they can:
  * Accept input parameters and return multiple values in the form of output parameters to the calling program.
  * Contain programming statements that perform operations in the database. These statements include calling other procedures.
  * Return a status value to a calling program to indicate success or failure (and the reason for failure).


[](https://learn.microsoft.com/en-us/sql/relational-databases/stored-procedures/stored-procedures-database-engine?view=sql-server-ver17#benefits-of-using-stored-procedures)
## Benefits of using stored procedures
The following list describes some benefits of using procedures.
[](https://learn.microsoft.com/en-us/sql/relational-databases/stored-procedures/stored-procedures-database-engine?view=sql-server-ver17#reduced-serverclient-network-traffic)
### Reduced server/client network traffic
The commands in a procedure are executed as a single batch of code. This approach can significantly reduce network traffic between the server and client because only the call to execute the procedure is sent across the network. Without the code encapsulation provided by a procedure, every individual line of code would have to cross the network.
[](https://learn.microsoft.com/en-us/sql/relational-databases/stored-procedures/stored-procedures-database-engine?view=sql-server-ver17#stronger-security)
### Stronger security
Multiple users and client programs can perform operations on underlying database objects through a procedure, even if the users and programs don't have direct permissions on those underlying objects. The procedure controls what processes and activities are performed and protects the underlying database objects. This approach eliminates the requirement to grant permissions at the individual object level and simplifies the security layers.
The [EXECUTE AS](https://learn.microsoft.com/en-us/sql/t-sql/statements/execute-as-clause-transact-sql?view=sql-server-ver17) clause can be specified in the `CREATE PROCEDURE` statement to enable impersonating another user, or enable users or applications to perform certain database activities without needing direct permissions on the underlying objects and commands. For example, some actions such as `TRUNCATE TABLE` don't have grantable permissions. To execute `TRUNCATE TABLE`, the user must have `ALTER` permissions on the specified table. Granting a user `ALTER` permissions on a table might not be ideal, because the user effectively has permissions well beyond the ability to truncate a table. By incorporating the `TRUNCATE TABLE` statement in a module and specifying that module execute as a user who has permissions to modify the table, you can extend the permissions to truncate the table to the user that you grant `EXECUTE` permissions on the module.
When an application calls a procedure over the network, only the call to execute the procedure is visible. Therefore, malicious users can't see table and database object names, embed Transact-SQL statements of their own, or search for critical data.
Using procedure parameters helps guard against SQL injection attacks. Since parameter input is treated as a literal value and not as executable code, it's more difficult for an attacker to insert a command into the Transact-SQL statements inside the procedure and compromise security.
You can encrypt procedures to help obfuscate the source code. For more information, see [SQL Server encryption](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/sql-server-encryption?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/relational-databases/stored-procedures/stored-procedures-database-engine?view=sql-server-ver17#reuse-of-code)
### Reuse of code
The code for any repetitious database operation is a perfect candidate for encapsulation in procedures. This approach eliminates needless rewrites of the same code, decreases code inconsistency, and allows any user or application with the necessary permissions to access and execute the code.
[](https://learn.microsoft.com/en-us/sql/relational-databases/stored-procedures/stored-procedures-database-engine?view=sql-server-ver17#easier-maintenance)
### Easier maintenance
When client applications call procedures and keep database operations in the data tier, you only need to update the procedures for any changes in the underlying database. The application tier remains separate and doesn't have to know about any changes to database layouts, relationships, or processes.
[](https://learn.microsoft.com/en-us/sql/relational-databases/stored-procedures/stored-procedures-database-engine?view=sql-server-ver17#improved-performance)
### Improved performance
By default, a procedure compiles the first time it's executed, and creates an execution plan that it reuses for subsequent executions. Since the query processor doesn't have to create a new plan, it typically takes less time to process the procedure.
If there are significant changes to the tables or data referenced by the procedure, the precompiled plan might actually cause the procedure to perform slower. In this case, recompiling the procedure and forcing a new execution plan can improve performance.
[](https://learn.microsoft.com/en-us/sql/relational-databases/stored-procedures/stored-procedures-database-engine?view=sql-server-ver17#types-of-stored-procedures)
## Types of stored procedures
[](https://learn.microsoft.com/en-us/sql/relational-databases/stored-procedures/stored-procedures-database-engine?view=sql-server-ver17#user-defined)
### User-defined
A user-defined procedure can be created in a user-defined database or in all system databases except the `Resource` database. The procedure can be developed in either Transact-SQL, or as a reference to a .NET Framework common runtime language (CLR) method.
[](https://learn.microsoft.com/en-us/sql/relational-databases/stored-procedures/stored-procedures-database-engine?view=sql-server-ver17#temporary)
### Temporary
Temporary procedures are a form of user-defined procedures. Temporary procedures are like a permanent procedure, except that they're stored in `tempdb`. There are two types of temporary procedures: _local_ and _global_. They differ from each other in their names, their visibility, and their availability. Local temporary procedures have a single number sign (`#`) as the first character of their names. They're visible only to the current user connection, and they're deleted when the connection is closed. Global temporary procedures have two number signs (`##`) as the first two characters of their names. They're visible to any user after they're created, and they're deleted at the end of the last session using the procedure.
[](https://learn.microsoft.com/en-us/sql/relational-databases/stored-procedures/stored-procedures-database-engine?view=sql-server-ver17#system)
### System
System procedures are included with the Database Engine. They're physically stored in the internal, hidden `Resource` database and logically appear in the `sys` schema of every system-defined and user-defined database. In addition, the `msdb` database also contains system stored procedures in the `dbo` schema that are used for scheduling alerts and jobs. Because system procedures start with the prefix `sp_`, don't use this prefix when naming user-defined procedures. For a complete list of system procedures, see [System stored procedures](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/system-stored-procedures-transact-sql?view=sql-server-ver17).
SQL Server supports the system procedures that provide an interface from SQL Server to external programs for various maintenance activities. These extended procedures use the `xp_` prefix. For a complete list of extended procedures, see [General extended stored procedures](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/general-extended-stored-procedures-transact-sql?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/relational-databases/stored-procedures/stored-procedures-database-engine?view=sql-server-ver17#extended-user-defined)
### Extended user-defined
Extended procedures enable creating external routines in a programming language such as C. These procedures are DLLs that an instance of SQL Server can dynamically load and run.
Extended stored procedures will be removed in a future version of SQL Server. Don't use this feature in new development work, and modify applications that currently use this feature as soon as possible. Create CLR procedures instead. This method provides a more robust and secure alternative to writing extended procedures.
[](https://learn.microsoft.com/en-us/sql/relational-databases/stored-procedures/stored-procedures-database-engine?view=sql-server-ver17#related-tasks)
## Related tasks
Expand table
Task description | Article
---|---
Describes how to create a stored procedure. | [Create a stored procedure](https://learn.microsoft.com/en-us/sql/relational-databases/stored-procedures/create-a-stored-procedure?view=sql-server-ver17)
Describes how to modify a stored procedure. | [Modify a stored procedure](https://learn.microsoft.com/en-us/sql/relational-databases/stored-procedures/modify-a-stored-procedure?view=sql-server-ver17)
Describes how to delete a stored procedure. | [Delete a stored procedure](https://learn.microsoft.com/en-us/sql/relational-databases/stored-procedures/delete-a-stored-procedure?view=sql-server-ver17)
Describes how to execute a stored procedure. | [Execute a stored procedure](https://learn.microsoft.com/en-us/sql/relational-databases/stored-procedures/execute-a-stored-procedure?view=sql-server-ver17)
Describes how to grant permissions on a stored procedure. | [Grant Permissions on a stored procedure](https://learn.microsoft.com/en-us/sql/relational-databases/stored-procedures/grant-permissions-on-a-stored-procedure?view=sql-server-ver17)
Describes how to return data from a stored procedure to an application. | [Return data from a stored procedure](https://learn.microsoft.com/en-us/sql/relational-databases/stored-procedures/return-data-from-a-stored-procedure?view=sql-server-ver17)
Describes how to recompile a stored procedure. | [Recompile a stored procedure](https://learn.microsoft.com/en-us/sql/relational-databases/stored-procedures/recompile-a-stored-procedure?view=sql-server-ver17)
Describes how to rename a stored procedure. | [Rename a stored procedure](https://learn.microsoft.com/en-us/sql/relational-databases/stored-procedures/rename-a-stored-procedure?view=sql-server-ver17)
Describes how to view the definition of a stored procedure. | [View the definition of a stored procedure](https://learn.microsoft.com/en-us/sql/relational-databases/stored-procedures/view-the-definition-of-a-stored-procedure?view=sql-server-ver17)
Describes how to view the dependencies on a stored procedure. | [View the dependencies of a stored procedure](https://learn.microsoft.com/en-us/sql/relational-databases/stored-procedures/view-the-dependencies-of-a-stored-procedure?view=sql-server-ver17)
Describes how parameters are used in a stored procedure. | [Parameters](https://learn.microsoft.com/en-us/sql/relational-databases/stored-procedures/parameters?view=sql-server-ver17)
[](https://learn.microsoft.com/en-us/sql/relational-databases/stored-procedures/stored-procedures-database-engine?view=sql-server-ver17#related-content)
## Related content
  * [CLR Stored Procedures](https://learn.microsoft.com/en-us/dotnet/framework/data/adonet/sql/clr-stored-procedures)
  * [Deferred name resolution](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-trigger-transact-sql?view=sql-server-ver17#deferred-name-resolution)


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
  * [ Create a stored procedure - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/stored-procedures/create-a-stored-procedure?source=recommendations)
Learn how to create a Transact-SQL stored procedure by using SQL Server Management Studio and by using the Transact-SQL CREATE PROCEDURE statement.
  * [ Modify a stored procedure - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/stored-procedures/modify-a-stored-procedure?source=recommendations)
Learn how to modify a stored procedure in SQL Server by using SQL Server Management Studio or Transact-SQL.
  * [ CREATE PROCEDURE (Transact-SQL) - SQL Server ](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-procedure-transact-sql?source=recommendations)
CREATE PROCEDURE creates a Transact-SQL or common language runtime (CLR) stored procedure.
  * [ Parameters - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/stored-procedures/parameters?source=recommendations)
Learn how to use parameters to exchange data between stored procedures and functions and the application or tool that called the stored procedure or function.
  * [ FILESTREAM, functions, stored procedures, views - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/blob/filestream-ddl-functions-stored-procedures-and-views?source=recommendations)
FILESTREAM works with specific Transact-SQL statements, APIs, functions, stored procedures, and views. Learn which statements and objects support FILESTREAM.
  * [ Execute a Stored Procedure - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/stored-procedures/execute-a-stored-procedure?source=recommendations)
Learn how to execute a stored procedure by using SQL Server Management Studio or Transact-SQL.
  * [ Specify Parameters in a Stored Procedure - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/stored-procedures/specify-parameters?source=recommendations)
Learn how to pass values into parameters and about how each of the parameter attributes is used during a procedure call.
  * [ Stored Procedure Properties (General Page) - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/stored-procedures/stored-procedure-properties-general-page?source=recommendations)
Learn how to use the Stored Properties (General Page) to view read-only information about a stored procedure.


Show 5 more
Module
[ Create stored procedures and user-defined functions - Training ](https://learn.microsoft.com/en-us/training/modules/create-stored-procedures-table-valued-functions/?source=recommendations)
This content is a part of Create stored procedures and user-defined functions.
Certification
[ Microsoft Certified: Azure Database Administrator Associate - Certifications ](https://learn.microsoft.com/en-us/credentials/certifications/azure-database-administrator-associate/?source=recommendations)
Administer an SQL Server database infrastructure for cloud, on-premises and hybrid relational databases using the Microsoft PaaS relational database offerings.
Mar 8, 4 PM - Mar 8, 4 PM
Experiment with what's next in AI-driven apps and agent design
* * *
  * Last updated on 11/20/2025


##  In this article
  1. [Benefits of using stored procedures](https://learn.microsoft.com/en-us/sql/relational-databases/stored-procedures/stored-procedures-database-engine?view=sql-server-ver17#benefits-of-using-stored-procedures)
  2. [Types of stored procedures](https://learn.microsoft.com/en-us/sql/relational-databases/stored-procedures/stored-procedures-database-engine?view=sql-server-ver17#types-of-stored-procedures)
  3. [Related tasks](https://learn.microsoft.com/en-us/sql/relational-databases/stored-procedures/stored-procedures-database-engine?view=sql-server-ver17#related-tasks)
  4. [Related content](https://learn.microsoft.com/en-us/sql/relational-databases/stored-procedures/stored-procedures-database-engine?view=sql-server-ver17#related-content)


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
[ Sign in ](https://learn.microsoft.com/en-us/sql/relational-databases/stored-procedures/stored-procedures-database-engine?view=sql-server-ver17)
[English (United States)](https://learn.microsoft.com/en-us/locale?target=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fsql%2Frelational-databases%2Fstored-procedures%2Fstored-procedures-database-engine%3Fview%3Dsql-server-ver17)
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
