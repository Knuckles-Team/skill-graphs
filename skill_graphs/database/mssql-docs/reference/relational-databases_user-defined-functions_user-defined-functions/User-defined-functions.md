# User-defined functions
Feedback
Summarize this article for me
##  In this article
  1. [Benefits of user-defined functions](https://learn.microsoft.com/en-us/sql/relational-databases/user-defined-functions/user-defined-functions?view=sql-server-ver17#benefits-of-user-defined-functions)
  2. [Types of functions](https://learn.microsoft.com/en-us/sql/relational-databases/user-defined-functions/user-defined-functions?view=sql-server-ver17#types-of-functions)
  3. [Guidelines](https://learn.microsoft.com/en-us/sql/relational-databases/user-defined-functions/user-defined-functions?view=sql-server-ver17#guidelines)
  4. [Valid statements in a function](https://learn.microsoft.com/en-us/sql/relational-databases/user-defined-functions/user-defined-functions?view=sql-server-ver17#valid-statements-in-a-function)
  5. [Schema-bound functions](https://learn.microsoft.com/en-us/sql/relational-databases/user-defined-functions/user-defined-functions?view=sql-server-ver17#schema-bound-functions)
  6. [Specify parameters](https://learn.microsoft.com/en-us/sql/relational-databases/user-defined-functions/user-defined-functions?view=sql-server-ver17#specify-parameters)
  7. [Related content](https://learn.microsoft.com/en-us/sql/relational-databases/user-defined-functions/user-defined-functions?view=sql-server-ver17#related-content)

Show 3 more
**Applies to:** ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure SQL Database](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure SQL Managed Instance](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL analytics endpoint in Microsoft Fabric](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Warehouse in Microsoft Fabric](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL database in Microsoft Fabric](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to)
Like functions in programming languages, SQL Server user-defined functions are routines that accept parameters, perform an action, such as a complex calculation, and return the result of that action as a value. The return value can either be a single scalar value or a result set.
[](https://learn.microsoft.com/en-us/sql/relational-databases/user-defined-functions/user-defined-functions?view=sql-server-ver17#benefits-of-user-defined-functions)
## Benefits of user-defined functions
Why use user-defined functions (UDFs)?
  * **Modular programming.** You can create the function once, store it in the database, and call it any number of times in your program. User-defined functions can be modified independently of the program source code.
  * **Faster execution.** Similar to stored procedures, Transact-SQL user-defined functions reduce the compilation cost of Transact-SQL code by caching the plans and reusing them for repeated executions. This means the user-defined function doesn't need to be reparsed and reoptimized with each use, resulting in faster execution times.
Common language runtime (CLR) functions offer significant performance advantage over Transact-SQL functions for computational tasks, string manipulation, and business logic. Transact-SQL functions are better suited for data-access intensive logic.
  * **Reduce network traffic.** An operation that filters data based on some complex constraint that can't be expressed in a single scalar expression can be expressed as a function. The function can then be invoked in the WHERE clause to reduce the number of rows sent to the client.


Transact-SQL UDFs in queries can only be executed on a single thread (serial execution plan). Therefore using UDFs inhibits parallel query processing. For more information about parallel query processing, see the [Query Processing Architecture Guide](https://learn.microsoft.com/en-us/sql/relational-databases/query-processing-architecture-guide?view=sql-server-ver17#parallel-query-processing).
[](https://learn.microsoft.com/en-us/sql/relational-databases/user-defined-functions/user-defined-functions?view=sql-server-ver17#types-of-functions)
## Types of functions
This section describes the differences between [scalar functions](https://learn.microsoft.com/en-us/sql/relational-databases/user-defined-functions/user-defined-functions?view=sql-server-ver17#scalar-functions), [table-valued functions](https://learn.microsoft.com/en-us/sql/relational-databases/user-defined-functions/user-defined-functions?view=sql-server-ver17#table-valued-functions), and [system functions](https://learn.microsoft.com/en-us/sql/relational-databases/user-defined-functions/user-defined-functions?view=sql-server-ver17#system-functions).
[](https://learn.microsoft.com/en-us/sql/relational-databases/user-defined-functions/user-defined-functions?view=sql-server-ver17#scalar-functions)
### Scalar functions
User-defined scalar functions return a single data value of the type defined in the RETURNS clause. For an inline scalar function, the returned scalar value is the result of a single statement. For a multistatement scalar function, the function body can contain a series of Transact-SQL statements that return the single value. The return type can be any data type except **text** , **ntext** , **image** , **cursor** , and **timestamp**. For examples, see [Create user-defined functions (database engine)](https://learn.microsoft.com/en-us/sql/relational-databases/user-defined-functions/create-user-defined-functions-database-engine?view=sql-server-ver17#Scalar).
[](https://learn.microsoft.com/en-us/sql/relational-databases/user-defined-functions/user-defined-functions?view=sql-server-ver17#table-valued-functions)
### Table-valued functions
User-defined table-valued functions (TVFs) return a **table** data type. For an inline table-valued function, there's no function body; the table is the result set of a single SELECT statement. For examples, see [Create user-defined functions (database engine)](https://learn.microsoft.com/en-us/sql/relational-databases/user-defined-functions/create-user-defined-functions-database-engine?view=sql-server-ver17#TVF).
[](https://learn.microsoft.com/en-us/sql/relational-databases/user-defined-functions/user-defined-functions?view=sql-server-ver17#system-functions)
### System functions
SQL Server provides many system functions that you can use to perform various operations. They can't be modified. For more information, see [What are the SQL database functions?](https://learn.microsoft.com/en-us/sql/t-sql/functions/functions?view=sql-server-ver17), [System Functions by category for Transact-SQL](https://learn.microsoft.com/en-us/sql/relational-databases/system-functions/system-functions-category-transact-sql?view=sql-server-ver17), and [System dynamic management views](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/system-dynamic-management-views?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/relational-databases/user-defined-functions/user-defined-functions?view=sql-server-ver17#guidelines)
## Guidelines
Transact-SQL errors that cause a statement to be canceled and continue with the next statement in the module (such as triggers or stored procedures) are treated differently inside a function. In functions, such errors cause the execution of the function to stop. This in turn causes the statement that invoked the function to be canceled.
The statements in a `BEGIN...END` block can't have any side effects. Function side effects are any permanent changes to the state of a resource that has a scope outside the function such as a modification to a database table. The only changes that statements in the function can make, are changes to objects local to the function, such as local cursors or variables. Modifications to database tables, operations on cursors that aren't local to the function, such as sending e-mail, attempting a catalog modification, and generating a result set that is returned to the user, are examples of actions that can't be performed in a function.
If a `CREATE FUNCTION` statement produces side effects against resources that don't exist when the `CREATE FUNCTION` statement is issued, SQL Server executes the statement. However, SQL Server doesn't execute the function when it's invoked.
The number of times that a function specified in a query is executed can vary between execution plans built by the optimizer. An example is a function invoked by a subquery in a `WHERE` clause. The number of times the subquery and its function is executed can vary with different access paths chosen by the optimizer.
Deterministic functions must be [schema-bound](https://learn.microsoft.com/en-us/sql/relational-databases/user-defined-functions/user-defined-functions?view=sql-server-ver17#SchemaBound). Use the `SCHEMABINDING` clause when creating a deterministic function.
For more information and performance considerations on user-defined functions, see [Create user-defined functions (Database Engine)](https://learn.microsoft.com/en-us/sql/relational-databases/user-defined-functions/create-user-defined-functions-database-engine?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/relational-databases/user-defined-functions/user-defined-functions?view=sql-server-ver17#valid-statements-in-a-function)
## Valid statements in a function
The types of statements that are valid in a function include:
  * `DECLARE` statements can be used to define data variables and cursors that are local to the function.
  * Assignments of values to objects local to the function, such as using `SET` to assign values to scalar and table local variables.
  * Cursor operations that reference local cursors that are declared, opened, closed, and deallocated in the function. `FETCH` statements that return data to the client aren't allowed. Only `FETCH` statements that assign values to local variables using the `INTO` clause are allowed.
  * Control-of-flow statements except `TRY...CATCH` statements.
  * `SELECT` statements containing select lists with expressions that assign values to variables that are local to the function.
  * `UPDATE`, `INSERT`, and `DELETE` statements modifying table variables that are local to the function.
  * `EXECUTE` statements calling an extended stored procedure.


[](https://learn.microsoft.com/en-us/sql/relational-databases/user-defined-functions/user-defined-functions?view=sql-server-ver17#built-in-system-functions)
### Built-in system functions
The following nondeterministic built-in functions can be used in Transact-SQL user-defined functions.
  * `CURRENT_TIMESTAMP`
  * `GET_TRANSMISSION_STATUS`
  * `GETDATE`
  * `GETUTCDATE`
  * `@@CONNECTIONS`
  * `@@CPU_BUSY`
  * `@@DBTS`
  * `@@IDLE`
  * `@@IO_BUSY`
  * `@@MAX_CONNECTIONS`
  * `@@PACK_RECEIVED`
  * `@@PACK_SENT`
  * `@@PACKET_ERRORS`
  * `@@TIMETICKS`
  * `@@TOTAL_ERRORS`
  * `@@TOTAL_READ`
  * `@@TOTAL_WRITE`


The following nondeterministic built-in functions **cannot** be used in a Transact-SQL user-defined function (UDF).
  * `NEWID`
  * `NEWSEQUENTIALID`
  * `RAND`
  * `TEXTPTR`


If you reference one of these functions inside a UDF, you get the following error:
Output
Copy
```
Msg 443, Level 16, State 1
Invalid use of a side-effecting operator <operator> within a function.

```

For a list of deterministic and nondeterministic built-in system functions, see [Deterministic and nondeterministic functions](https://learn.microsoft.com/en-us/sql/relational-databases/user-defined-functions/deterministic-and-nondeterministic-functions?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/relational-databases/user-defined-functions/user-defined-functions?view=sql-server-ver17#schema-bound-functions)
## Schema-bound functions
`CREATE FUNCTION` supports a `SCHEMABINDING` clause that binds the function to the schema of any objects it references, such as tables, views, and other user-defined functions. An attempt to alter or drop any object referenced by a schema-bound function fails.
These conditions must be met before you can specify `SCHEMABINDING` in [CREATE FUNCTION](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-function-transact-sql?view=sql-server-ver17):
  * All views and user-defined functions referenced by the function must be schema-bound.
  * All objects referenced by the function must be in the same database as the function. The objects must be referenced using either one-part or two-part names.
  * You must have `REFERENCES` permission on all objects (tables, views, and user-defined functions) referenced in the function.


You can use `ALTER FUNCTION` to remove the schema binding. The `ALTER FUNCTION` statement should redefine the function without specifying `WITH SCHEMABINDING`.
[](https://learn.microsoft.com/en-us/sql/relational-databases/user-defined-functions/user-defined-functions?view=sql-server-ver17#specify-parameters)
## Specify parameters
A user-defined function takes zero or more input parameters and returns either a scalar value or a table. A function can have a maximum of 1,024 input parameters. When a parameter of the function has a default value, the keyword `DEFAULT` must be specified when calling the function to get the default value. This behavior is different from parameters with default values in user-defined stored procedures in which omitting the parameter also implies the default value. User-defined functions don't support output parameters.
[](https://learn.microsoft.com/en-us/sql/relational-databases/user-defined-functions/user-defined-functions?view=sql-server-ver17#related-content)
## Related content
  * [Create user-defined functions (Database Engine)](https://learn.microsoft.com/en-us/sql/relational-databases/user-defined-functions/create-user-defined-functions-database-engine?view=sql-server-ver17)
  * [Create CLR functions](https://learn.microsoft.com/en-us/sql/relational-databases/user-defined-functions/create-clr-functions?view=sql-server-ver17)
  * [Create user-defined aggregates](https://learn.microsoft.com/en-us/sql/relational-databases/user-defined-functions/create-user-defined-aggregates?view=sql-server-ver17)
  * [Modify user-defined functions](https://learn.microsoft.com/en-us/sql/relational-databases/user-defined-functions/modify-user-defined-functions?view=sql-server-ver17)
  * [Delete user-defined functions](https://learn.microsoft.com/en-us/sql/relational-databases/user-defined-functions/delete-user-defined-functions?view=sql-server-ver17)
  * [Execute user-defined functions](https://learn.microsoft.com/en-us/sql/relational-databases/user-defined-functions/execute-user-defined-functions?view=sql-server-ver17)
  * [Rename user-defined functions](https://learn.microsoft.com/en-us/sql/relational-databases/user-defined-functions/rename-user-defined-functions?view=sql-server-ver17)
  * [View user-defined functions](https://learn.microsoft.com/en-us/sql/relational-databases/user-defined-functions/view-user-defined-functions?view=sql-server-ver17)


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
  * [ CREATE FUNCTION (Transact-SQL) - SQL Server ](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-function-transact-sql?source=recommendations)
CREATE FUNCTION (Transact-SQL)
  * [ Create User-Defined Functions (Database Engine) - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/user-defined-functions/create-user-defined-functions-database-engine?source=recommendations)
Learn how to create user-defined functions with Transact-SQL.
  * [ Deterministic and Nondeterministic Functions - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/user-defined-functions/deterministic-and-nondeterministic-functions?source=recommendations)
Learn about deterministic and nondeterministic functions in the SQL Database Engine.
  * [ Execute user-defined functions - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/user-defined-functions/execute-user-defined-functions?source=recommendations)
Learn how to execute a user defined function using Transact-SQL.
  * [ ALTER FUNCTION (Transact-SQL) - SQL Server ](https://learn.microsoft.com/en-us/sql/t-sql/statements/alter-function-transact-sql?source=recommendations)
ALTER FUNCTION (Transact-SQL)
  * [ How to: Use Table-Valued User-Defined Functions - ADO.NET ](https://learn.microsoft.com/en-us/dotnet/framework/data/adonet/sql/linq/how-to-use-table-valued-user-defined-functions?source=recommendations)
Use these examples to learn how to create a table-valued function, which returns a single rowset. Use such a table-valued function just like a table.
  * [ View User-defined Functions - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/user-defined-functions/view-user-defined-functions?source=recommendations)
View User-defined Functions
  * [ Delete User-defined Functions - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/user-defined-functions/delete-user-defined-functions?source=recommendations)
Delete User-defined Functions


Show 5 more
Module
[ Create stored procedures and user-defined functions - Training ](https://learn.microsoft.com/en-us/training/modules/create-stored-procedures-table-valued-functions/?source=recommendations)
This content is a part of Create stored procedures and user-defined functions.
Mar 8, 4 PM - Mar 8, 4 PM
Experiment with what's next in AI-driven apps and agent design
* * *
  * Last updated on 11/18/2025


##  In this article
  1. [Benefits of user-defined functions](https://learn.microsoft.com/en-us/sql/relational-databases/user-defined-functions/user-defined-functions?view=sql-server-ver17#benefits-of-user-defined-functions)
  2. [Types of functions](https://learn.microsoft.com/en-us/sql/relational-databases/user-defined-functions/user-defined-functions?view=sql-server-ver17#types-of-functions)
  3. [Guidelines](https://learn.microsoft.com/en-us/sql/relational-databases/user-defined-functions/user-defined-functions?view=sql-server-ver17#guidelines)
  4. [Valid statements in a function](https://learn.microsoft.com/en-us/sql/relational-databases/user-defined-functions/user-defined-functions?view=sql-server-ver17#valid-statements-in-a-function)
  5. [Schema-bound functions](https://learn.microsoft.com/en-us/sql/relational-databases/user-defined-functions/user-defined-functions?view=sql-server-ver17#schema-bound-functions)
  6. [Specify parameters](https://learn.microsoft.com/en-us/sql/relational-databases/user-defined-functions/user-defined-functions?view=sql-server-ver17#specify-parameters)
  7. [Related content](https://learn.microsoft.com/en-us/sql/relational-databases/user-defined-functions/user-defined-functions?view=sql-server-ver17#related-content)


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
[ Sign in ](https://learn.microsoft.com/en-us/sql/relational-databases/user-defined-functions/user-defined-functions?view=sql-server-ver17)
[English (United States)](https://learn.microsoft.com/en-us/locale?target=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fsql%2Frelational-databases%2Fuser-defined-functions%2Fuser-defined-functions%3Fview%3Dsql-server-ver17)
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
