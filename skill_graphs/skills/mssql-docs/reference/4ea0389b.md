# What are the SQL database functions?
Feedback
Summarize this article for me
##  In this article
  1. [Aggregate functions](https://learn.microsoft.com/en-us/sql/t-sql/functions/functions?view=sql-server-ver17#aggregate-functions)
  2. [Analytic functions](https://learn.microsoft.com/en-us/sql/t-sql/functions/functions?view=sql-server-ver17#analytic-functions)
  3. [Bit manipulation functions](https://learn.microsoft.com/en-us/sql/t-sql/functions/functions?view=sql-server-ver17#bit-manipulation-functions)
  4. [Configuration functions](https://learn.microsoft.com/en-us/sql/t-sql/functions/functions?view=sql-server-ver17#configuration-functions)
  5. [Ranking functions](https://learn.microsoft.com/en-us/sql/t-sql/functions/functions?view=sql-server-ver17#ranking-functions)
  6. [Rowset functions](https://learn.microsoft.com/en-us/sql/t-sql/functions/functions?view=sql-server-ver17#rowset-functions)
  7. [Scalar functions](https://learn.microsoft.com/en-us/sql/t-sql/functions/functions?view=sql-server-ver17#scalar-functions)
  8. [String functions](https://learn.microsoft.com/en-us/sql/t-sql/functions/functions?view=sql-server-ver17#string-functions)
  9. [Function determinism](https://learn.microsoft.com/en-us/sql/t-sql/functions/functions?view=sql-server-ver17#function-determinism)
  10. [Function collation](https://learn.microsoft.com/en-us/sql/t-sql/functions/functions?view=sql-server-ver17#function-collation)
  11. [Limitations](https://learn.microsoft.com/en-us/sql/t-sql/functions/functions?view=sql-server-ver17#limitations)
  12. [Related content](https://learn.microsoft.com/en-us/sql/t-sql/functions/functions?view=sql-server-ver17#related-content)

Show 8 more
**Applies to:** ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure SQL Database](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure SQL Managed Instance](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure Synapse Analytics](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Analytics Platform System (PDW)](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL analytics endpoint in Microsoft Fabric](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Warehouse in Microsoft Fabric](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL database in Microsoft Fabric](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to)
Learn about the categories of built-in functions you can use with SQL databases. You can use the built-in functions or create your own user-defined functions.
[](https://learn.microsoft.com/en-us/sql/t-sql/functions/functions?view=sql-server-ver17#aggregate-functions)
## Aggregate functions
Aggregate functions perform a calculation on a set of values and return a single value. They're allowed in the select list or the `HAVING` clause of a `SELECT` statement. You can use an aggregation in combination with the `GROUP BY` clause to calculate the aggregation on categories of rows. Use the `OVER` clause to calculate the aggregation on a specific range of value. The `OVER` clause can't follow the `GROUPING` or `GROUPING_ID` aggregations.
All aggregate functions are deterministic, which means they always return the same value when they run on the same input values. For more information, see [Deterministic and nondeterministic functions](https://learn.microsoft.com/en-us/sql/relational-databases/user-defined-functions/deterministic-and-nondeterministic-functions?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/t-sql/functions/functions?view=sql-server-ver17#analytic-functions)
## Analytic functions
Analytic functions compute an aggregate value based on a group of rows. However, unlike aggregate functions, analytic functions can return multiple rows for each group. You can use analytic functions to compute moving averages, running totals, percentages, or top-N results within a group.
[](https://learn.microsoft.com/en-us/sql/t-sql/functions/functions?view=sql-server-ver17#bit-manipulation-functions)
## Bit manipulation functions
**Applies to:** SQL Server 2022 (16.x) and later versions, Azure SQL Managed Instance, Azure SQL Database, SQL database in Microsoft Fabric
Bit manipulation functions allow you to process and store data more efficiently than with individual bits. For more information, see [Bit manipulation functions](https://learn.microsoft.com/en-us/sql/t-sql/functions/bit-manipulation-functions-overview?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/t-sql/functions/functions?view=sql-server-ver17#configuration-functions)
## Configuration functions
Configuration functions are scalar functions that return information about current configuration option settings, for example, [@@SERVERNAME (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/functions/servername-transact-sql?view=sql-server-ver17).
All configuration functions operate in a nondeterministic way. In other words, these functions do not always return the same results every time they are called, even with the same set of input values. For more information about function determinism, see [Deterministic and Nondeterministic Functions](https://learn.microsoft.com/en-us/sql/relational-databases/user-defined-functions/deterministic-and-nondeterministic-functions?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/t-sql/functions/functions?view=sql-server-ver17#ranking-functions)
## Ranking functions
Ranking functions return a ranking value for each row in a partition. Depending on the function that is used, some rows might receive the same value as other rows. Ranking functions are nondeterministic.
[](https://learn.microsoft.com/en-us/sql/t-sql/functions/functions?view=sql-server-ver17#rowset-functions)
## Rowset functions
Rowset functions Return an object that can be used like table references in a SQL statement.
[](https://learn.microsoft.com/en-us/sql/t-sql/functions/functions?view=sql-server-ver17#scalar-functions)
## Scalar functions
Operate on a single value and then return a single value. Scalar functions can be used wherever an expression is valid.
[](https://learn.microsoft.com/en-us/sql/t-sql/functions/functions?view=sql-server-ver17#categories-of-scalar-functions)
### Categories of scalar functions
Expand table
Function category | Description
---|---
[Configuration Functions](https://learn.microsoft.com/en-us/sql/t-sql/functions/functions?view=sql-server-ver17#configuration-functions) | Return information about the current configuration.
[Conversion Functions](https://learn.microsoft.com/en-us/sql/t-sql/functions/conversion-functions-transact-sql?view=sql-server-ver17) | Support data type casting and converting.
[Cursor Functions](https://learn.microsoft.com/en-us/sql/t-sql/functions/cursor-functions-transact-sql?view=sql-server-ver17) | Return information about cursors.
[Date and Time Data Types and Functions](https://learn.microsoft.com/en-us/sql/t-sql/functions/date-and-time-data-types-and-functions-transact-sql?view=sql-server-ver17) | Perform operations on a date and time input values and return string, numeric, or date and time values.
[Graph Functions](https://learn.microsoft.com/en-us/sql/t-sql/functions/graph-functions-transact-sql?view=sql-server-ver17) | Perform operations to convert to and from character representations of graph node and edge IDs.
[JSON Functions](https://learn.microsoft.com/en-us/sql/t-sql/functions/json-functions-transact-sql?view=sql-server-ver17) | Validate, query, or change JSON data.
[Logical Functions](https://learn.microsoft.com/en-us/sql/t-sql/functions/logical-functions-choose-transact-sql?view=sql-server-ver17) | Perform logical operations.
[Mathematical Functions](https://learn.microsoft.com/en-us/sql/t-sql/functions/mathematical-functions-transact-sql?view=sql-server-ver17) | Perform calculations based on input values provided as parameters to the functions, and return numeric values.
[Metadata Functions](https://learn.microsoft.com/en-us/sql/t-sql/functions/metadata-functions-transact-sql?view=sql-server-ver17) | Return information about the database and database objects.
[Security Functions](https://learn.microsoft.com/en-us/sql/t-sql/functions/security-functions-transact-sql?view=sql-server-ver17) | Return information about users and roles.
[String Functions](https://learn.microsoft.com/en-us/sql/t-sql/functions/functions?view=sql-server-ver17#string-functions) | Perform operations on a string (**char** or **varchar**) input value and return a string or numeric value.
[System Functions](https://learn.microsoft.com/en-us/sql/relational-databases/system-functions/system-functions-category-transact-sql?view=sql-server-ver17) | Perform operations and return information about values, objects, and settings in an instance of SQL Server.
[System Statistical Functions](https://learn.microsoft.com/en-us/sql/t-sql/functions/system-statistical-functions-transact-sql?view=sql-server-ver17) | Return statistical information about the system.
[Text and Image Functions](https://learn.microsoft.com/en-us/sql/t-sql/functions/text-and-image-functions-textptr-transact-sql?view=sql-server-ver17) | Perform operations on text or image input values or columns, and return information about the value.
[](https://learn.microsoft.com/en-us/sql/t-sql/functions/functions?view=sql-server-ver17#string-functions)
## String functions
Scalar functions perform an operation on a string input value and return a string or numeric value, for example, [ASCII (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/functions/ascii-transact-sql?view=sql-server-ver17).
All built-in string functions except `FORMAT` are deterministic. This means they return the same value any time they are called with a specific set of input values. For more information about function determinism, see [Deterministic and Nondeterministic Functions](https://learn.microsoft.com/en-us/sql/relational-databases/user-defined-functions/deterministic-and-nondeterministic-functions?view=sql-server-ver17).
When string functions are passed arguments that are not string values, the input type is implicitly converted to a text data type. For more information, see [Data Type Conversion (Database Engine)](https://learn.microsoft.com/en-us/sql/t-sql/data-types/data-type-conversion-database-engine?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/t-sql/functions/functions?view=sql-server-ver17#function-determinism)
## Function determinism
SQL Server built-in functions are either deterministic or nondeterministic. Functions are deterministic when they always return the same result anytime they're called by using a specific set of input values. Functions are nondeterministic when they could return different results every time they're called, even with the same specific set of input values. For more information, see [Deterministic and nondeterministic functions](https://learn.microsoft.com/en-us/sql/relational-databases/user-defined-functions/deterministic-and-nondeterministic-functions?view=sql-server-ver17)
[](https://learn.microsoft.com/en-us/sql/t-sql/functions/functions?view=sql-server-ver17#function-collation)
## Function collation
Functions that take a character string input and return a character string output use the collation of the input string for the output.
Functions that take non-character inputs and return a character string use the default collation of the current database for the output.
Functions that take multiple character string inputs and return a character string use the rules of collation precedence to set the collation of the output string. For more information, see [Collation precedence](https://learn.microsoft.com/en-us/sql/t-sql/statements/collation-precedence-transact-sql?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/t-sql/functions/functions?view=sql-server-ver17#limitations)
## Limitations
For information on limitations of function types and platforms, see [CREATE FUNCTION (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-function-transact-sql?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/t-sql/functions/functions?view=sql-server-ver17#related-content)
## Related content
  * [CREATE FUNCTION (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-function-transact-sql?view=sql-server-ver17)
  * [Deterministic and nondeterministic functions](https://learn.microsoft.com/en-us/sql/relational-databases/user-defined-functions/deterministic-and-nondeterministic-functions?view=sql-server-ver17)


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
  * Last updated on 02/10/2026


##  In this article
  1. [Aggregate functions](https://learn.microsoft.com/en-us/sql/t-sql/functions/functions?view=sql-server-ver17#aggregate-functions)
  2. [Analytic functions](https://learn.microsoft.com/en-us/sql/t-sql/functions/functions?view=sql-server-ver17#analytic-functions)
  3. [Bit manipulation functions](https://learn.microsoft.com/en-us/sql/t-sql/functions/functions?view=sql-server-ver17#bit-manipulation-functions)
  4. [Configuration functions](https://learn.microsoft.com/en-us/sql/t-sql/functions/functions?view=sql-server-ver17#configuration-functions)
  5. [Ranking functions](https://learn.microsoft.com/en-us/sql/t-sql/functions/functions?view=sql-server-ver17#ranking-functions)
  6. [Rowset functions](https://learn.microsoft.com/en-us/sql/t-sql/functions/functions?view=sql-server-ver17#rowset-functions)
  7. [Scalar functions](https://learn.microsoft.com/en-us/sql/t-sql/functions/functions?view=sql-server-ver17#scalar-functions)
  8. [String functions](https://learn.microsoft.com/en-us/sql/t-sql/functions/functions?view=sql-server-ver17#string-functions)
  9. [Function determinism](https://learn.microsoft.com/en-us/sql/t-sql/functions/functions?view=sql-server-ver17#function-determinism)
  10. [Function collation](https://learn.microsoft.com/en-us/sql/t-sql/functions/functions?view=sql-server-ver17#function-collation)
  11. [Limitations](https://learn.microsoft.com/en-us/sql/t-sql/functions/functions?view=sql-server-ver17#limitations)
  12. [Related content](https://learn.microsoft.com/en-us/sql/t-sql/functions/functions?view=sql-server-ver17#related-content)

Show 3 more
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
[ Sign in ](https://learn.microsoft.com/en-us/sql/t-sql/functions/functions?view=sql-server-ver17)
[English (United States)](https://learn.microsoft.com/en-us/locale?target=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fsql%2Ft-sql%2Ffunctions%2Ffunctions%3Fview%3Dsql-server-ver17)
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
