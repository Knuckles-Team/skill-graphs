# JSON data in SQL Server
Feedback
Summarize this article for me
##  In this article
  1. [Overview](https://learn.microsoft.com/en-us/sql/relational-databases/json/json-data-sql-server?view=sql-server-ver17#overview)
  2. [SQL Server 2025 changes](https://learn.microsoft.com/en-us/sql/relational-databases/json/json-data-sql-server?view=sql-server-ver17#sql-server-2025-changes)
  3. [Key JSON capabilities](https://learn.microsoft.com/en-us/sql/relational-databases/json/json-data-sql-server?view=sql-server-ver17#key-json-capabilities)
  4. [Use cases for JSON data in SQL Server](https://learn.microsoft.com/en-us/sql/relational-databases/json/json-data-sql-server?view=sql-server-ver17#use-cases-for-json-data-in-sql-server)
  5. [Combine relational and JSON data](https://learn.microsoft.com/en-us/sql/relational-databases/json/json-data-sql-server?view=sql-server-ver17#combine-relational-and-json-data)
  6. [Store and index JSON data in SQL Server](https://learn.microsoft.com/en-us/sql/relational-databases/json/json-data-sql-server?view=sql-server-ver17#store-and-index-json-data-in-sql-server)
  7. [Analyze JSON data with SQL queries](https://learn.microsoft.com/en-us/sql/relational-databases/json/json-data-sql-server?view=sql-server-ver17#analyze-json-data-with-sql-queries)
  8. [Return data from a SQL Server table formatted as JSON](https://learn.microsoft.com/en-us/sql/relational-databases/json/json-data-sql-server?view=sql-server-ver17#return-data-from-a-sql-server-table-formatted-as-json)
  9. [Test drive built-in JSON support with the AdventureWorks sample database](https://learn.microsoft.com/en-us/sql/relational-databases/json/json-data-sql-server?view=sql-server-ver17#test-drive-built-in-json-support-with-the-adventureworks-sample-database)
  10. [Related content](https://learn.microsoft.com/en-us/sql/relational-databases/json/json-data-sql-server?view=sql-server-ver17#related-content)

Show 6 more
**Applies to:** ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) SQL Server 2016 (13.x) and later versions ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure SQL Database](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure SQL Managed Instance](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure Synapse Analytics](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL database in Microsoft Fabric](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to)
This article provides an overview of the textual data format JSON in SQL Server, Azure SQL Database, Azure SQL Managed Instance, Azure Synapse Analytics, and SQL database in Microsoft Fabric.
JSON support requires [database compatibility level](https://learn.microsoft.com/en-us/sql/relational-databases/databases/view-or-change-the-compatibility-level-of-a-database?view=sql-server-ver17) 130 or higher.
[](https://learn.microsoft.com/en-us/sql/relational-databases/json/json-data-sql-server?view=sql-server-ver17#overview)
## Overview
JSON is a popular textual data format that's used for exchanging data in modern web and mobile applications. JSON is also used for storing unstructured data in log files or NoSQL databases such as Microsoft Azure Cosmos DB. Many REST web services return results that are formatted as JSON text or accept data that's formatted as JSON. For example, most Azure services, such as Azure Search, Azure Storage, and Azure Cosmos DB, have REST endpoints that return or consume JSON. JSON is also the main format for exchanging data between webpages and web servers by using AJAX calls.
JSON functions, first introduced in SQL Server 2016 (13.x), enable you to combine NoSQL and relational concepts in the same database. You can combine classic relational columns with columns that contain documents formatted as JSON text in the same table, parse and import JSON documents in relational structures, or format relational data to JSON text.
The following is an example of JSON text:
JSON
Copy
```
[
    {
        "name": "John",
        "skills": [ "SQL", "C#", "Azure" ]
    },
    {
        "name": "Jane",
        "surname": "Doe"
    }
]

```

By using SQL Server built-in functions and operators, you can do the following things with JSON text:
  * Parse JSON text and read or modify values.
  * Transform arrays of JSON objects into table format.
  * Run any Transact-SQL query on the converted JSON objects.
  * Format the results of Transact-SQL queries in JSON format.


![Diagram showing the overview of built-in JSON support.](https://learn.microsoft.com/en-us/sql/relational-databases/json/media/json-data-sql-server/json-slides-overview.png?view=sql-server-ver17)
[](https://learn.microsoft.com/en-us/sql/relational-databases/json/json-data-sql-server?view=sql-server-ver17#sql-server-2025-changes)
## SQL Server 2025 changes
SQL Server 2025 (17.x) introduces the following JSON enhancements, all currently in preview:
  * [Modify method for the **json** type](https://learn.microsoft.com/en-us/sql/t-sql/data-types/json-data-type?view=sql-server-ver17#modify-method)
  * [CREATE JSON INDEX](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-json-index-transact-sql?view=sql-server-ver17)
  * [JSON_CONTAINS](https://learn.microsoft.com/en-us/sql/t-sql/functions/json-contains-transact-sql?view=sql-server-ver17)
  * [ANSI SQL path expression array wildcard support](https://learn.microsoft.com/en-us/sql/relational-databases/json/json-path-expressions-sql-server?view=sql-server-ver17#array-wildcard-and-range-support)
  * [ANSI SQL WITH ARRAY WRAPPER clause in JSON_QUERY function](https://learn.microsoft.com/en-us/sql/t-sql/functions/json-query-transact-sql?view=sql-server-ver17#with-array-wrapper)


[](https://learn.microsoft.com/en-us/sql/relational-databases/json/json-data-sql-server?view=sql-server-ver17#key-json-capabilities)
## Key JSON capabilities
The next sections discuss the key capabilities that SQL Server provides with its built-in JSON support.
[](https://learn.microsoft.com/en-us/sql/relational-databases/json/json-data-sql-server?view=sql-server-ver17#json-data-type)
### JSON data type
The [JSON data type](https://learn.microsoft.com/en-us/sql/t-sql/data-types/json-data-type?view=sql-server-ver17):
  * is generally available for Azure SQL Database and Azure SQL Managed Instance with the **SQL Server 2025** or **Always-up-to-date** [update policy](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/update-policy#always-up-to-date-update-policy).
  * is in preview for SQL Server 2025 (17.x) and SQL database in Fabric.


The new **json** data type that stores JSON documents in a native binary format that provides the following benefits over storing JSON data in **varchar** /**nvarchar** :
  * More efficient reads, as the document is already parsed
  * More efficient writes, as the query can update individual values without accessing the entire document
  * More efficient storage, optimized for compression
  * No change in compatibility with existing code


Using the JSON same functions described in this article remain the most efficient way to query the **json** data type. For more information on the native **json** data type, see [JSON data type](https://learn.microsoft.com/en-us/sql/t-sql/data-types/json-data-type?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/relational-databases/json/json-data-sql-server?view=sql-server-ver17#extract-values-from-json-text-and-use-them-in-queries)
### Extract values from JSON text and use them in queries
If you have JSON text that's stored in database tables, you can read or modify values in the JSON text by using the following built-in functions:
  * [ISJSON](https://learn.microsoft.com/en-us/sql/t-sql/functions/isjson-transact-sql?view=sql-server-ver17) tests whether a string contains valid JSON.
  * [JSON_VALUE](https://learn.microsoft.com/en-us/sql/t-sql/functions/json-value-transact-sql?view=sql-server-ver17) extracts a scalar value from a JSON string.
  * [JSON_QUERY](https://learn.microsoft.com/en-us/sql/t-sql/functions/json-query-transact-sql?view=sql-server-ver17) extracts an object or an array from a JSON string.
  * [JSON_MODIFY](https://learn.microsoft.com/en-us/sql/t-sql/functions/json-modify-transact-sql?view=sql-server-ver17) changes a value in a JSON string.


**Example**
In the following example, the query uses both relational and JSON data (stored in a column named `jsonCol`) from a table called `People`:
SQL
Copy
```
SELECT Name,
       Surname,
       JSON_VALUE(jsonCol, '$.info.address.PostCode') AS PostCode,
       JSON_VALUE(jsonCol, '$.info.address."Address Line 1"') + ' ' +
           JSON_VALUE(jsonCol, '$.info.address."Address Line 2"') AS Address,
       JSON_QUERY(jsonCol, '$.info.skills') AS Skills
FROM People
WHERE ISJSON(jsonCol) > 0
      AND JSON_VALUE(jsonCol, '$.info.address.Town') = 'Belgrade'
      AND STATUS = 'Active'
ORDER BY JSON_VALUE(jsonCol, '$.info.address.PostCode');

```

Applications and tools see no difference between the values taken from scalar table columns and the values taken from JSON columns. You can use values from JSON text in any part of a Transact-SQL query (including WHERE, ORDER BY, or GROUP BY clauses, window aggregates, and so on). JSON functions use JavaScript-like syntax for referencing values inside JSON text.
For more information, see [Validate, query, and change JSON data with built-in functions](https://learn.microsoft.com/en-us/sql/relational-databases/json/validate-query-and-change-json-data-with-built-in-functions-sql-server?view=sql-server-ver17), [JSON_VALUE](https://learn.microsoft.com/en-us/sql/t-sql/functions/json-value-transact-sql?view=sql-server-ver17), and [JSON_QUERY](https://learn.microsoft.com/en-us/sql/t-sql/functions/json-query-transact-sql?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/relational-databases/json/json-data-sql-server?view=sql-server-ver17#change-json-values)
### Change JSON values
If you must modify parts of JSON text, you can use the [JSON_MODIFY](https://learn.microsoft.com/en-us/sql/t-sql/functions/json-modify-transact-sql?view=sql-server-ver17) function to update the value of a property in a JSON string and return the updated JSON string. The following example updates the value of a property in a variable that contains JSON:
SQL
Copy
```
DECLARE @json AS NVARCHAR (MAX);

SET @json = '{"info": {"address": [{"town": "Belgrade"}, {"town": "Paris"}, {"town":"Madrid"}]}}';
SET @json = JSON_MODIFY(@json, '$.info.address[1].town', 'London');

SELECT @json AS modifiedJson;

```

Here's the result set.
JSON
Copy
```
{"info":{"address":[{"town":"Belgrade"},{"town":"London"},{"town":"Madrid"}]}}

```

[](https://learn.microsoft.com/en-us/sql/relational-databases/json/json-data-sql-server?view=sql-server-ver17#convert-json-collections-to-a-rowset)
### Convert JSON collections to a rowset
You don't need a custom query language to query JSON in SQL Server. To query JSON data, you can use standard T-SQL. If you must create a query or report on JSON data, you can easily convert JSON data to rows and columns by calling the `OPENJSON` rowset function. For more information, see [Parse and transform JSON data with OPENJSON](https://learn.microsoft.com/en-us/sql/relational-databases/json/convert-json-data-to-rows-and-columns-with-openjson-sql-server?view=sql-server-ver17).
The following example calls `OPENJSON` and transforms the array of objects that is stored in the `@json` variable to a rowset that can be queried with a standard Transact-SQL `SELECT` statement:
SQL
Copy
```
DECLARE @json AS NVARCHAR (MAX);

SET @json = N'[
  {"id": 2, "info": {"name": "John", "surname": "Smith"}, "age": 25},
  {"id": 5, "info": {"name": "Jane", "surname": "Smith"}, "dob": "2005-11-04T12:00:00"}
]';

SELECT *
FROM OPENJSON (@json) WITH (
    id INT 'strict $.id',
    firstName NVARCHAR (50) '$.info.name',
    lastName NVARCHAR (50) '$.info.surname',
    age INT,
    dateOfBirth DATETIME2 '$.dob'
);

```

Here's the result set.
Expand table
ID | firstName | lastName | age | dateOfBirth
---|---|---|---|---
2 | John | Smith | 25 |
5 | Jane | Smith |  | 2005-11-04T12:00:00
`OPENJSON` transforms the array of JSON objects into a table in which each object is represented as one row, and key/value pairs are returned as cells. The output observes the following rules:
  * `OPENJSON` converts JSON values to the types that are specified in the `WITH` clause.
  * `OPENJSON` can handle both flat key/value pairs and nested, hierarchically organized objects.
  * You don't have to return all the fields that are contained in the JSON text.
  * If JSON values don't exist, `OPENJSON` returns `NULL` values.
  * You can optionally specify a path after the type specification to reference a nested property or to reference a property by a different name.
  * The optional `strict` prefix in the path specifies that values for the specified properties must exist in the JSON text.


For more information, see [Parse and transform JSON data with OPENJSON](https://learn.microsoft.com/en-us/sql/relational-databases/json/convert-json-data-to-rows-and-columns-with-openjson-sql-server?view=sql-server-ver17) and [OPENJSON](https://learn.microsoft.com/en-us/sql/t-sql/functions/openjson-transact-sql?view=sql-server-ver17).
JSON documents might have sub-elements and hierarchical data that can't be directly mapped into the standard relational columns. In this case, you can flatten JSON hierarchy by joining parent entity with sub-arrays.
In the following example, the second object in the array has sub-array representing person skills. Every sub-object can be parsed using additional `OPENJSON` function call:
SQL
Copy
```
DECLARE @json AS NVARCHAR (MAX);

SET @json = N'[
  {"id": 2, "info": {"name": "John", "surname": "Smith"}, "age": 25},
  {"id": 5, "info": {"name": "Jane", "surname": "Smith", "skills": ["SQL", "C#", "Azure"]}, "dob": "2005-11-04T12:00:00"}
]';

SELECT id,
       firstName,
       lastName,
       age,
       dateOfBirth,
       skill
FROM OPENJSON (@json) WITH (
    id INT 'strict $.id',
    firstName NVARCHAR (50) '$.info.name',
    lastName NVARCHAR (50) '$.info.surname',
    age INT,
    dateOfBirth DATETIME2 '$.dob',
    skills NVARCHAR (MAX) '$.info.skills' AS JSON
)
OUTER APPLY OPENJSON (skills) WITH (skill NVARCHAR (8) '$');

```

The `skills` array is returned in the first `OPENJSON` as original JSON text fragment and passed to another `OPENJSON` function using `APPLY` operator. The second `OPENJSON` function parses JSON array and return string values as single column rowset that will be joined with the result of the first `OPENJSON`.
Here's the result set.
Expand table
ID | firstName | lastName | age | dateOfBirth | skill
---|---|---|---|---|---
2 | John | Smith | 25 |  |
5 | Jane | Smith |  | 2005-11-04T12:00:00 | SQL
5 | Jane | Smith |  | 2005-11-04T12:00:00 | C#
5 | Jane | Smith |  | 2005-11-04T12:00:00 | Azure
`OUTER APPLY OPENJSON` joins first-level entity with sub-array and return flatten resultset. Due to JOIN, the second row is repeated for every skill.
[](https://learn.microsoft.com/en-us/sql/relational-databases/json/json-data-sql-server?view=sql-server-ver17#convert-sql-server-data-to-json-or-export-json)
### Convert SQL Server data to JSON or export JSON
Converting Azure Synapse Analytics data to JSON or exporting JSON isn't supported.
Format SQL Server data or the results of SQL queries as JSON by adding the `FOR JSON` clause to a `SELECT` statement. Use `FOR JSON` to delegate the formatting of JSON output from your client applications to SQL Server. For more information, see [Format query results as JSON with FOR JSON](https://learn.microsoft.com/en-us/sql/relational-databases/json/format-query-results-as-json-with-for-json-sql-server?view=sql-server-ver17).
The following example uses PATH mode with the `FOR JSON` clause:
SQL
Copy
```
SELECT id,
       firstName AS "info.name",
       lastName AS "info.surname",
       age,
       dateOfBirth AS dob
FROM People
FOR JSON PATH;

```

The `FOR JSON` clause formats SQL results as JSON text that can be provided to any app that understands JSON. The PATH option uses dot-separated aliases in the SELECT clause to nest objects in the query results.
Here's the result set.
JSON
Copy
```
[
  {
    "id": 2,
    "info": {
      "name": "John",
      "surname": "Smith"
    },
    "age": 25
  },
  {
    "id": 5,
    "info": {
      "name": "Jane",
      "surname": "Smith"
    },
    "dob": "2005-11-04T12:00:00"
  }
]

```

For more information, see [Format query results as JSON with FOR JSON](https://learn.microsoft.com/en-us/sql/relational-databases/json/format-query-results-as-json-with-for-json-sql-server?view=sql-server-ver17) and [SELECT - FOR Clause](https://learn.microsoft.com/en-us/sql/t-sql/queries/select-for-clause-transact-sql?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/relational-databases/json/json-data-sql-server?view=sql-server-ver17#json-data-from-aggregates)
### JSON data from aggregates
JSON aggregate functions enable construction of JSON objects or arrays based on an aggregate from SQL data.
  * [JSON_OBJECTAGG](https://learn.microsoft.com/en-us/sql/t-sql/functions/json-objectagg-transact-sql?view=sql-server-ver17) constructs a JSON **object** from an aggregation of SQL data or columns.
  * [JSON_ARRAYAGG](https://learn.microsoft.com/en-us/sql/t-sql/functions/json-arrayagg-transact-sql?view=sql-server-ver17) constructs a JSON **array** from an aggregation of SQL data or columns.


The `JSON_OBJECTAGG` and `JSON_ARRAYAGG` aggregate functions are generally available for Azure SQL Database, Azure SQL Managed Instance (with the **SQL Server 2025** or **Always-up-to-date** [update policy](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/update-policy)), and Fabric Data Warehouse, and in preview for SQL Server 2025 (17.x).
[](https://learn.microsoft.com/en-us/sql/relational-databases/json/json-data-sql-server?view=sql-server-ver17#use-cases-for-json-data-in-sql-server)
## Use cases for JSON data in SQL Server
JSON support in SQL Server and Azure SQL Database lets you combine relational and NoSQL concepts. You can easily transform relational to semi-structured data and vice-versa. JSON isn't a replacement for existing relational models, however. Here are some specific use cases that benefit from the JSON support in SQL Server and in SQL Database.
  * Simplify complex data models
Consider denormalizing your data model with JSON fields in place of multiple child tables.
  * Store retail and e-commerce data
Store info about products with a wide range of variable attributes in a denormalized model for flexibility.
  * Process log and telemetry data
Load, query, and analyze log data stored as JSON files with all the power of the Transact-SQL language.
  * Store semi-structured IoT data
When you need real-time analysis of IoT data, load the incoming data directly into the database instead of staging it in a storage location.
  * Simplify REST API development
Transform relational data from your database easily into the JSON format used by the REST APIs that support your web site.


[](https://learn.microsoft.com/en-us/sql/relational-databases/json/json-data-sql-server?view=sql-server-ver17#combine-relational-and-json-data)
## Combine relational and JSON data
SQL Server provides a hybrid model for storing and processing both relational and JSON data by using standard Transact-SQL language. You can organize collections of your JSON documents in tables, establish relationships between them, combine strongly typed scalar columns stored in tables with flexible key/value pairs stored in JSON columns, and query both scalar and JSON values in one or more tables by using full Transact-SQL.
JSON text is stored in **varchar** or **nvarchar** columns and is indexed as plain text. Any SQL Server feature or component that supports text supports JSON, so there are almost no constraints on interaction between JSON and other SQL Server features. You can store JSON in In-memory or Temporal tables, apply Row-Level Security predicates on JSON text, and so on.
Here are some use cases that show how you can use the built-in JSON support in SQL Server.
[](https://learn.microsoft.com/en-us/sql/relational-databases/json/json-data-sql-server?view=sql-server-ver17#store-and-index-json-data-in-sql-server)
## Store and index JSON data in SQL Server
JSON is a textual format so the JSON documents can be stored in **nvarchar** columns in a SQL Database. Since **nvarchar** type is supported in all SQL Server subsystems you can put JSON documents in tables with clustered columnstore indexes, memory optimized tables, or external files that can be read using OPENROWSET or PolyBase.
To learn more about your options for storing, indexing, and optimizing JSON data in SQL Server, see the following articles:
  * [Store JSON documents](https://learn.microsoft.com/en-us/sql/relational-databases/json/store-json-documents-in-sql-tables?view=sql-server-ver17)
  * [Index JSON data](https://learn.microsoft.com/en-us/sql/relational-databases/json/index-json-data?view=sql-server-ver17)
  * [Optimize JSON processing with in-memory OLTP](https://learn.microsoft.com/en-us/sql/relational-databases/json/optimize-json-processing-with-in-memory-oltp?view=sql-server-ver17)


[](https://learn.microsoft.com/en-us/sql/relational-databases/json/json-data-sql-server?view=sql-server-ver17#load-json-files-into-sql-server)
### Load JSON files into SQL Server
You can format information that's stored in files as standard JSON or line-delimited JSON. SQL Server can import the contents of JSON files, parse it by using the `OPENJSON` or `JSON_VALUE` functions, and load it into tables.
  * If your JSON documents are stored in local files, on shared network drives, or in Azure Files locations that can be accessed by SQL Server, you can use bulk import to load your JSON data into SQL Server.
  * If your line-delimited JSON files are stored in Azure Blob storage or the Hadoop file system, you can use PolyBase to load JSON text, parse it in Transact-SQL code, and load it into tables.


[](https://learn.microsoft.com/en-us/sql/relational-databases/json/json-data-sql-server?view=sql-server-ver17#import-json-data-into-sql-server-tables)
### Import JSON data into SQL Server tables
If you must load JSON data from an external service into SQL Server, you can use `OPENJSON` to import the data into SQL Server instead of parsing the data in the application layer.
In supported platforms, use the native **json** data type instead of **nvarchar(max)** for improved performance and more efficient storage.
SQL
Copy
```
DECLARE @jsonVariable AS NVARCHAR (MAX);

SET @jsonVariable = N'[
  {
    "Order": {
      "Number":"SO43659",
      "Date":"2011-05-31T00:00:00"
    },
    "AccountNumber":"AW29825",
    "Item": {
      "Price":2024.9940,
      "Quantity":1
    }
  },
  {
    "Order": {
      "Number":"SO43661",
      "Date":"2011-06-01T00:00:00"
    },
    "AccountNumber":"AW73565",
    "Item": {
      "Price":2024.9940,
      "Quantity":3
    }
  }
]';

-- INSERT INTO <sampleTable>
SELECT SalesOrderJsonData.*
FROM OPENJSON (@jsonVariable, N'$') WITH (
    Number VARCHAR (200) N'$.Order.Number',
    Date DATETIME N'$.Order.Date',
    Customer VARCHAR (200) N'$.AccountNumber',
    Quantity INT N'$.Item.Quantity'
) AS SalesOrderJsonData;

```

You can provide the content of the JSON variable by an external REST service, send it as a parameter from a client-side JavaScript framework, or load it from external files. You can easily insert, update, or merge results from JSON text into a SQL Server table.
[](https://learn.microsoft.com/en-us/sql/relational-databases/json/json-data-sql-server?view=sql-server-ver17#analyze-json-data-with-sql-queries)
## Analyze JSON data with SQL queries
If you must filter or aggregate JSON data for reporting purposes, you can use `OPENJSON` to transform JSON to relational format. You can then use standard Transact-SQL and built-in functions to prepare the reports.
SQL
Copy
```
SELECT Tab.Id,
       SalesOrderJsonData.Customer,
       SalesOrderJsonData.Date
FROM SalesOrderRecord AS Tab
CROSS APPLY OPENJSON (Tab.json, N'$.Orders.OrdersArray') WITH (
    Number VARCHAR (200) N'$.Order.Number',
    Date DATETIME N'$.Order.Date',
    Customer VARCHAR (200) N'$.AccountNumber',
    Quantity INT N'$.Item.Quantity'
) AS SalesOrderJsonData
WHERE JSON_VALUE(Tab.json, '$.Status') = N'Closed'
ORDER BY JSON_VALUE(Tab.json, '$.Group'),
         Tab.DateModified;

```

You can use both standard table columns and values from JSON text in the same query. You can add indexes on the `JSON_VALUE(Tab.json, '$.Status')` expression to improve the performance of the query. For more information, see [Index JSON data](https://learn.microsoft.com/en-us/sql/relational-databases/json/index-json-data?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/relational-databases/json/json-data-sql-server?view=sql-server-ver17#return-data-from-a-sql-server-table-formatted-as-json)
## Return data from a SQL Server table formatted as JSON
If you have a web service that takes data from the database layer and returns it in JSON format, or if you have JavaScript frameworks or libraries that accept data formatted as JSON, you can format JSON output directly in a SQL query. Instead of writing code or including a library to convert tabular query results and then serialize objects to JSON format, you can use `FOR JSON` to delegate the JSON formatting to SQL Server.
For example, you might want to generate JSON output that's compliant with the OData specification. The web service expects a request and response in the following format:
  * Request: `/Northwind/Northwind.svc/Products(1)?$select=ProductID,ProductName`
  * Response: `{"@odata.context": "https://services.odata.org/V4/Northwind/Northwind.svc/$metadata#Products(ProductID,ProductName)/$entity", "ProductID": 1, "ProductName": "Chai"}`


This OData URL represents a request for the ProductID and ProductName columns for the product with `ID` 1. You can use `FOR JSON` to format the output as expected in SQL Server.
SQL
Copy
```
SELECT 'https://services.odata.org/V4/Northwind/Northwind.svc/$metadata#Products(ProductID,ProductName)/$entity' AS '@odata.context',
       ProductID,
       Name AS ProductName
FROM Production.Product
WHERE ProductID = 1
FOR JSON AUTO;

```

The output of this query is JSON text that's fully compliant with the OData spec. Formatting and escaping are handled by SQL Server. SQL Server can also format query results in any format, such as OData JSON or GeoJSON.
[](https://learn.microsoft.com/en-us/sql/relational-databases/json/json-data-sql-server?view=sql-server-ver17#test-drive-built-in-json-support-with-the-adventureworks-sample-database)
## Test drive built-in JSON support with the AdventureWorks sample database
To get the AdventureWorks sample database, download at least the database file and the samples and scripts file from
After you restore the sample database to an instance of SQL Server, extract the samples file, and then open the `JSON Sample Queries procedures views and indexes.sql` file from the JSON folder. Run the scripts in this file to reformat some existing data as JSON data, test sample queries and reports over the JSON data, index the JSON data, and import and export JSON.
Here's what you can do with the scripts that are included in the file:
  1. Denormalize the existing schema to create columns of JSON data.
     * Store information from `SalesReasons`, `SalesOrderDetails`, `SalesPerson`, `Customer`, and other tables that contain information related to sales order into JSON columns in the `SalesOrder_json` table.
     * Store information from `EmailAddresses` and `PersonPhone` tables in the `Person_json` table as arrays of JSON objects.
  2. Create procedures and views that query JSON data.
  3. Index JSON data. Create indexes on JSON properties and full-text indexes.
  4. Import and export JSON. Create and run procedures that export the content of the `Person` and the `SalesOrder` tables as JSON results, and import and update the `Person` and the `SalesOrder` tables by using JSON input.
  5. Run query examples. Run some queries that call the stored procedures and views that you created in steps 2 and 4.
  6. Clean up scripts. Don't run this part if you want to keep the stored procedures and views that you created in steps 2 and 4.


[](https://learn.microsoft.com/en-us/sql/relational-databases/json/json-data-sql-server?view=sql-server-ver17#related-content)
## Related content
  * [SELECT - FOR Clause (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/queries/select-for-clause-transact-sql?view=sql-server-ver17)
  * [OPENJSON (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/functions/openjson-transact-sql?view=sql-server-ver17)
  * [JSON functions (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/functions/json-functions-transact-sql?view=sql-server-ver17)
  * [ISJSON (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/functions/isjson-transact-sql?view=sql-server-ver17)
  * [JSON_VALUE (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/functions/json-value-transact-sql?view=sql-server-ver17)
  * [JSON_OBJECT (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/functions/json-object-transact-sql?view=sql-server-ver17)
  * [JSON_ARRAY (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/functions/json-array-transact-sql?view=sql-server-ver17)
  * [JSON_QUERY (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/functions/json-query-transact-sql?view=sql-server-ver17)
  * [JSON_MODIFY (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/functions/json-modify-transact-sql?view=sql-server-ver17)


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
  * [ OPENJSON (Transact-SQL) - SQL Server ](https://learn.microsoft.com/en-us/sql/t-sql/functions/openjson-transact-sql?source=recommendations)
The OPENJSON table-valued function parses JSON text and returns objects and properties from the JSON input as rows and columns.
  * [ Solve Common Issues with JSON - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/json/solve-common-issues-with-json-in-sql-server?source=recommendations)
Solve common issues with JSON in the SQL Database Engine.
  * [ JSON_VALUE (Transact-SQL) - SQL Server ](https://learn.microsoft.com/en-us/sql/t-sql/functions/json-value-transact-sql?source=recommendations)
JSON_VALUE extracts a scalar value from a JSON string.
  * [ JSON_QUERY (Transact-SQL) - SQL Server ](https://learn.microsoft.com/en-us/sql/t-sql/functions/json-query-transact-sql?source=recommendations)
JSON_QUERY extracts an object or an array from a JSON string.
  * [ Parse and Transform JSON Data with OPENJSON - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/json/convert-json-data-to-rows-and-columns-with-openjson-sql-server?source=recommendations)
OPENJSON converts JSON into a set of rows and columns. Use it to run any SQL query on the returned data, or insert it into a SQL Server table.
  * [ Format Query Results as JSON with FOR JSON - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/json/format-query-results-as-json-with-for-json-sql-server?source=recommendations)
Format query results as JSON, or export data from SQL Server as JSON, by adding the FOR JSON clause to a SELECT statement.
  * [ JSON Functions (Transact-SQL) - SQL Server ](https://learn.microsoft.com/en-us/sql/t-sql/functions/json-functions-transact-sql?source=recommendations)
Use JSON functions to validate or change JSON text, or to extract simple or complex values.
  * [ ISJSON (Transact-SQL) - SQL Server ](https://learn.microsoft.com/en-us/sql/t-sql/functions/isjson-transact-sql?source=recommendations)
ISJSON tests whether a string contains valid JSON.


Show 5 more
Module
[ Store and Retrieve JSON Files - Training ](https://learn.microsoft.com/en-us/training/modules/store-retrieve-json-files/?source=recommendations)
Learn how to serialize and deserialize JavaScript Object Notation (JSON) strings using the JsonSerializer class, the JsonSerializerOptions class, and Data Transfer Objects.
Certification
[ Microsoft Certified: Azure Cosmos DB Developer Specialty - Certifications ](https://learn.microsoft.com/en-us/credentials/certifications/azure-cosmos-db-developer-specialty/?source=recommendations)
Write efficient queries, create indexing policies, manage, and provision resources in the SQL API and SDK with Microsoft Azure Cosmos DB.
Mar 8, 4 PM - Mar 8, 4 PM
Experiment with what's next in AI-driven apps and agent design
* * *
  * Last updated on 11/18/2025


##  In this article
  1. [Overview](https://learn.microsoft.com/en-us/sql/relational-databases/json/json-data-sql-server?view=sql-server-ver17#overview)
  2. [SQL Server 2025 changes](https://learn.microsoft.com/en-us/sql/relational-databases/json/json-data-sql-server?view=sql-server-ver17#sql-server-2025-changes)
  3. [Key JSON capabilities](https://learn.microsoft.com/en-us/sql/relational-databases/json/json-data-sql-server?view=sql-server-ver17#key-json-capabilities)
  4. [Use cases for JSON data in SQL Server](https://learn.microsoft.com/en-us/sql/relational-databases/json/json-data-sql-server?view=sql-server-ver17#use-cases-for-json-data-in-sql-server)
  5. [Combine relational and JSON data](https://learn.microsoft.com/en-us/sql/relational-databases/json/json-data-sql-server?view=sql-server-ver17#combine-relational-and-json-data)
  6. [Store and index JSON data in SQL Server](https://learn.microsoft.com/en-us/sql/relational-databases/json/json-data-sql-server?view=sql-server-ver17#store-and-index-json-data-in-sql-server)
  7. [Analyze JSON data with SQL queries](https://learn.microsoft.com/en-us/sql/relational-databases/json/json-data-sql-server?view=sql-server-ver17#analyze-json-data-with-sql-queries)
  8. [Return data from a SQL Server table formatted as JSON](https://learn.microsoft.com/en-us/sql/relational-databases/json/json-data-sql-server?view=sql-server-ver17#return-data-from-a-sql-server-table-formatted-as-json)
  9. [Test drive built-in JSON support with the AdventureWorks sample database](https://learn.microsoft.com/en-us/sql/relational-databases/json/json-data-sql-server?view=sql-server-ver17#test-drive-built-in-json-support-with-the-adventureworks-sample-database)
  10. [Related content](https://learn.microsoft.com/en-us/sql/relational-databases/json/json-data-sql-server?view=sql-server-ver17#related-content)


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
[ Sign in ](https://learn.microsoft.com/en-us/sql/relational-databases/json/json-data-sql-server?view=sql-server-ver17)
[English (United States)](https://learn.microsoft.com/en-us/locale?target=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fsql%2Frelational-databases%2Fjson%2Fjson-data-sql-server%3Fview%3Dsql-server-ver17)
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
