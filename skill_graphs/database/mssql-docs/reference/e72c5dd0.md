## Developer
Expand table
New feature or update | Details
---|---
[Change event streaming](https://learn.microsoft.com/en-us/sql/relational-databases/track-changes/change-event-streaming/overview?view=sql-server-ver17) | Capture and publish incremental DML changes of data (such as updates, inserts, and deletes) in near real-time. Change event streaming sends details of data changes such as the schema, previous values, and new values to Azure Event Hubs in a simple _CloudEvent_ , serialized as either native JSON or Avro Binary. Requires [PREVIEW_FEATURES database scoped configuration](https://learn.microsoft.com/en-us/sql/t-sql/statements/alter-database-scoped-configuration-transact-sql?view=sql-server-ver17#preview-features).
[Fuzzy string matching](https://learn.microsoft.com/en-us/sql/relational-databases/fuzzy-string-match/overview?view=sql-server-ver17) | Check if two strings are similar, and calculate the difference between two strings. Requires [PREVIEW_FEATURES database scoped configuration](https://learn.microsoft.com/en-us/sql/t-sql/statements/alter-database-scoped-configuration-transact-sql?view=sql-server-ver17#preview-features).
[Regular expressions](https://learn.microsoft.com/en-us/sql/relational-databases/regular-expressions/overview?view=sql-server-ver17) | Define a search pattern for text with a sequence of characters. Query SQL Server with regex to find, replace, or validate text data.
[Regular expressions functions](https://learn.microsoft.com/en-us/sql/t-sql/functions/regular-expressions-functions-transact-sql?view=sql-server-ver17) | Match complex patterns and manipulate data in SQL Server with regular expressions.
[External REST endpoint invocation](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-invoke-external-rest-endpoint-transact-sql?view=sql-server-ver17) | With a call to the system stored procedure [sp_invoke_external_rest_endpoint](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-invoke-external-rest-endpoint-transact-sql?view=sql-server-ver17), you can:

- Call REST/GraphQL endpoints from other Azure services
- Have data processed via an Azure Function
- Update a Power BI dashboard
- Call an on-premises REST endpoint
- Talk to Azure OpenAI services
[JSON data in SQL Server](https://learn.microsoft.com/en-us/sql/relational-databases/json/json-data-sql-server?view=sql-server-ver17#sql-server-2025-changes) | Use SQL Server built-in functions and operators with JSON data stored in a native binary format:

- Parse JSON text and read or modify values.
- Transform arrays of JSON objects into table format.
- Run any Transact-SQL query on the converted JSON objects.
- Format the results of Transact-SQL queries in JSON format.
- For more information and examples, see [JSON data type](https://learn.microsoft.com/en-us/sql/t-sql/data-types/json-data-type?view=sql-server-ver17).
Batch mode optimizations for built-in functions | Performance improvements for the following built-in functions:

- [Mathematical functions](https://learn.microsoft.com/en-us/sql/t-sql/functions/mathematical-functions-transact-sql?view=sql-server-ver17)
- [DATETRUNC](https://learn.microsoft.com/en-us/sql/t-sql/functions/datetrunc-transact-sql?view=sql-server-ver17)
New Chinese collations | Version 160 to support GB18030-2022 standard.
[](https://learn.microsoft.com/en-us/sql/sql-server/what-s-new-in-sql-server-2025?view=sql-server-ver17#analytics)
