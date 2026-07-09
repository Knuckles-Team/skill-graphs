# Synonyms (Database Engine)
Feedback
Summarize this article for me
##  In this article
  1. [Synonyms and Schemas](https://learn.microsoft.com/en-us/sql/relational-databases/synonyms/synonyms-database-engine?view=sql-server-ver17#synonyms-and-schemas)
  2. [Granting Permissions on a Synonym](https://learn.microsoft.com/en-us/sql/relational-databases/synonyms/synonyms-database-engine?view=sql-server-ver17#granting-permissions-on-a-synonym)
  3. [Using Synonyms](https://learn.microsoft.com/en-us/sql/relational-databases/synonyms/synonyms-database-engine?view=sql-server-ver17#using-synonyms)
  4. [Getting Information About Synonyms](https://learn.microsoft.com/en-us/sql/relational-databases/synonyms/synonyms-database-engine?view=sql-server-ver17#getting-information-about-synonyms)
  5. [Related Content](https://learn.microsoft.com/en-us/sql/relational-databases/synonyms/synonyms-database-engine?view=sql-server-ver17#related-content)


**Applies to:** ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure SQL Database](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure SQL Managed Instance](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL database in Microsoft Fabric](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to)
A synonym is a database object that serves the following purposes:
  * Provides an alternative name for another database object, referred to as the base object, that can exist on a local or remote server.
  * Provides a layer of abstraction that protects a client application from changes made to the name or location of the base object.


For example, consider the **Employee** table of Adventure Works, located on a server named **Server1**. To reference this table from another server, **Server2** , a client application would have to use the four-part name **Server1.AdventureWorks.Person.Employee**. Also, if the location of the table were to change, for example, to another server, the client application would have to be modified to reflect that change.
To address both these issues, you can create a synonym, **EmpTable** in a dedicated or existing schema, **RemoteObjects** , on **Server2** for the **Employee** table on **Server1**. Now, the client application only has to use the two-part name, **RemoteObjects.EmpTable** , to reference the **Employee** table Server1. Also, if the location of the **Employee** table changes, you will have to modify the synonym, **EmpTable** , to point to the new location of the **Employee** table. Because there is no ALTER SYNONYM statement, you first have to drop the synonym, **RemoteObjects.EmpTable** , and then re-create the synonym with the same name, but now point the synonym to the new location of the **Employee** table.
A synonym belongs to a schema, and like other objects in a schema, the name of a synonym must be unique. You can create synonyms for the following database objects:
Assembly (CLR) stored procedure
Assembly (CLR) scalar function
Replication-filter-procedure
SQL scalar function
SQL inline-tabled-valued function
View
Assembly (CLR) table-valued function
Assembly (CLR) aggregate functions
SQL table-valued function
SQL stored procedure
Table* (User-defined)
*Includes local and global temporary tables
Four-part names for function base objects are not supported.
A synonym cannot be the base object for another synonym, and a synonym cannot reference a user-defined aggregate function.
The binding between a synonym and its base object is by name only. All existence, type, and permissions checking on the base object is deferred until run time. Therefore, the base object can be modified, dropped, or dropped and replaced by another object that has the same name as the original base object. For example, consider a synonym, **dbo.MyContacts** , that references the **Person.Contact** table in Adventure Works. If the **Contact** table is dropped and replaced by a view named **Person.Contact** , **MyContacts** now references the **Person.Contact** view.
References to synonyms are not schema-bound. Therefore, a synonym can be dropped at any time. However, by dropping a synonym, you run the risk of leaving dangling references to the synonym that was dropped. These references will only be found at run time.
[](https://learn.microsoft.com/en-us/sql/relational-databases/synonyms/synonyms-database-engine?view=sql-server-ver17#synonyms-and-schemas)
## Synonyms and Schemas
If you have a default schema that you do not own and want to create a synonym, you must qualify the synonym name with the name of a schema that you do own. For example, if you own a schema **S1** , but **S2** is your default schema and you use the CREATE SYNONYM statement, you must prefix the name of the synonym with the schema **S1** , instead of naming the synonym by using a single-part name. For more information about how to create synonyms, see [CREATE SYNONYM (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-synonym-transact-sql?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/relational-databases/synonyms/synonyms-database-engine?view=sql-server-ver17#granting-permissions-on-a-synonym)
## Granting Permissions on a Synonym
Only synonym owners, members of **db_owner** , or members of **db_ddladmin** can grant permission on a synonym.
You can `GRANT`, `DENY`, and `REVOKE` all or any of the following permissions on a synonym:
CONTROL
EXECUTE
SELECT
UPDATE
DELETE
INSERT
TAKE OWNERSHIP
VIEW DEFINITION
[](https://learn.microsoft.com/en-us/sql/relational-databases/synonyms/synonyms-database-engine?view=sql-server-ver17#using-synonyms)
## Using Synonyms
You can use synonyms in place of their referenced base object in several SQL statements and expression contexts. The following columns contain a list of these statements and expression contexts:
SELECT
UPDATE
EXECUTE
INSERT
DELETE
Sub-selects
When you are working with synonyms in the contexts previously stated, the base object is affected. For example, if a synonym references a base object that is a table and you insert a row into the synonym, you are actually inserting a row into the referenced table.
You cannot reference a synonym that is located on a linked server.
You can use a synonym as the parameter for the OBJECT_ID function; however, the function returns the object ID of the synonym, not the base object.
You cannot reference a synonym in a DDL statement. For example, the following statements, which reference a synonym named `dbo.MyProduct`, generate errors:
SQL
Copy
```
ALTER TABLE dbo.MyProduct
   ADD NewFlag int null;
EXEC ('ALTER TABLE dbo.MyProduct
   ADD NewFlag int null');

```

The following permission statements are associated only with the synonym and not the base object:
GRANT
REVOKE
DENY
Synonyms are not schema-bound and, therefore, cannot be referenced by the following schema-bound expression contexts:
CHECK constraints
Default expressions
Schema-bound views
Computed columns
Rule expressions
Schema-bound functions
For more information about schema-bound functions, see [Create User-defined Functions (Database Engine)](https://learn.microsoft.com/en-us/sql/relational-databases/user-defined-functions/create-user-defined-functions-database-engine?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/relational-databases/synonyms/synonyms-database-engine?view=sql-server-ver17#getting-information-about-synonyms)
## Getting Information About Synonyms
The `sys.synonyms` catalog view contains an entry for each synonym in a given database. This catalog view exposes synonym metadata such as the name of the synonym and the name of the base object. For more information, see [sys.synonyms (Transact-SQL)](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-synonyms-transact-sql?view=sql-server-ver17).
By using extended properties, you can add descriptive or instructional text, input masks, and formatting rules as properties of a synonym. Because the property is stored in the database, all applications that read the property can evaluate the object in the same way. For more information, see [sp_addextendedproperty (Transact-SQL)](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-addextendedproperty-transact-sql?view=sql-server-ver17).
To find the base type of the base object of a synonym, use the OBJECTPROPERTYEX function. For more information, see [OBJECTPROPERTYEX (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/functions/objectpropertyex-transact-sql?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/relational-databases/synonyms/synonyms-database-engine?view=sql-server-ver17#examples)
### Examples
The following example returns the base type of a synonym's base object that is a local object.
SQL
Copy
```
USE tempdb;
GO
CREATE SCHEMA SynSchema
GO
CREATE SYNONYM SynSchema.MyEmployee
FOR AdventureWorks2022.HumanResources.Employee;
GO
SELECT OBJECTPROPERTYEX(OBJECT_ID('SynSchema.MyEmployee'), 'BaseType') AS BaseType;

```

The following example returns the base type of a synonym's base object that is a remote object located on a server named `Server1`.
SQL
Copy
```
EXECUTE sp_addlinkedserver Server1;
GO
CREATE SYNONYM SynSchema.MyRemoteEmployee
FOR Server1.AdventureWorks2022.HumanResources.Employee;
GO
SELECT OBJECTPROPERTYEX(OBJECT_ID('MyRemoteEmployee'), 'BaseType') AS BaseType;
GO

```

[](https://learn.microsoft.com/en-us/sql/relational-databases/synonyms/synonyms-database-engine?view=sql-server-ver17#related-content)
## Related Content
[Create Synonyms](https://learn.microsoft.com/en-us/sql/relational-databases/synonyms/create-synonyms?view=sql-server-ver17)
[CREATE SYNONYM (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-synonym-transact-sql?view=sql-server-ver17)
[DROP SYNONYM (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/statements/drop-synonym-transact-sql?view=sql-server-ver17)
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
  * [ Create Synonyms - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/synonyms/create-synonyms?source=recommendations)
Create Synonyms
  * [ CREATE SYNONYM (Transact-SQL) - SQL Server ](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-synonym-transact-sql?source=recommendations)
The CREATE SYNONYM statement creates a new synonym.
  * [ sys.synonyms (Transact-SQL) - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-synonyms-transact-sql?source=recommendations)
sys.synonyms (Transact-SQL)
  * [ DROP SYNONYM (Transact-SQL) - SQL Server ](https://learn.microsoft.com/en-us/sql/t-sql/statements/drop-synonym-transact-sql?source=recommendations)
DROP SYNONYM (Transact-SQL)
  * [ TRUNCATE TABLE (Transact-SQL) - SQL Server ](https://learn.microsoft.com/en-us/sql/t-sql/statements/truncate-table-transact-sql?source=recommendations)
TRUNCATE TABLE removes all rows from a table or specified partitions of a table.
  * [ CREATE VIEW (Transact-SQL) - SQL Server ](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-view-transact-sql?source=recommendations)
CREATE VIEW creates a virtual table whose contents are defined by a query.
  * [ CREATE INDEX (Transact-SQL) - SQL Server ](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-index-transact-sql?source=recommendations)
The CREATE INDEX statement creates a relational index on a table or view.
  * [ DELETE (Transact-SQL) - SQL Server ](https://learn.microsoft.com/en-us/sql/t-sql/statements/delete-transact-sql?source=recommendations)
DELETE (Transact-SQL)


Show 5 more
Module
[ Create tables, views, and temporary objects - Training ](https://learn.microsoft.com/en-us/training/modules/create-tables-views-temporary-objects/?source=recommendations)
This content is a part of Create tables, views, and temporary objects.
Certification
[ Microsoft Certified: Azure Database Administrator Associate - Certifications ](https://learn.microsoft.com/en-us/credentials/certifications/azure-database-administrator-associate/?source=recommendations)
Administer an SQL Server database infrastructure for cloud, on-premises and hybrid relational databases using the Microsoft PaaS relational database offerings.
Mar 8, 4 PM - Mar 8, 4 PM
Experiment with what's next in AI-driven apps and agent design
* * *
  * Last updated on 11/18/2025


##  In this article
  1. [Synonyms and Schemas](https://learn.microsoft.com/en-us/sql/relational-databases/synonyms/synonyms-database-engine?view=sql-server-ver17#synonyms-and-schemas)
  2. [Granting Permissions on a Synonym](https://learn.microsoft.com/en-us/sql/relational-databases/synonyms/synonyms-database-engine?view=sql-server-ver17#granting-permissions-on-a-synonym)
  3. [Using Synonyms](https://learn.microsoft.com/en-us/sql/relational-databases/synonyms/synonyms-database-engine?view=sql-server-ver17#using-synonyms)
  4. [Getting Information About Synonyms](https://learn.microsoft.com/en-us/sql/relational-databases/synonyms/synonyms-database-engine?view=sql-server-ver17#getting-information-about-synonyms)
  5. [Related Content](https://learn.microsoft.com/en-us/sql/relational-databases/synonyms/synonyms-database-engine?view=sql-server-ver17#related-content)


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
[ Sign in ](https://learn.microsoft.com/en-us/sql/relational-databases/synonyms/synonyms-database-engine?view=sql-server-ver17)
[English (United States)](https://learn.microsoft.com/en-us/locale?target=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fsql%2Frelational-databases%2Fsynonyms%2Fsynonyms-database-engine%3Fview%3Dsql-server-ver17)
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
