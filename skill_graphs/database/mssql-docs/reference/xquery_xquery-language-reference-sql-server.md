Version SQL Server 2025
  * Analytics Platform System (PDW)
    * [2016-AU7](https://learn.microsoft.com/en-us/sql/xquery/xquery-language-reference-sql-server?view=aps-pdw-2016-au7)
    * [2016-AU6](https://learn.microsoft.com/en-us/sql/xquery/xquery-language-reference-sql-server?view=aps-pdw-2016)
  * [Azure SQL Database](https://learn.microsoft.com/en-us/sql/xquery/xquery-language-reference-sql-server?view=azuresqldb-current)
  * [Azure SQL Managed Instance](https://learn.microsoft.com/en-us/sql/xquery/xquery-language-reference-sql-server?view=azuresqldb-mi-current)
  * [Azure Synapse Analytics](https://learn.microsoft.com/en-us/sql/xquery/xquery-language-reference-sql-server?view=azure-sqldw-latest)
  * [Fabric Data Warehouse](https://learn.microsoft.com/en-us/sql/xquery/xquery-language-reference-sql-server?view=fabric)
  * [Fabric SQL database](https://learn.microsoft.com/en-us/sql/xquery/xquery-language-reference-sql-server?view=fabric-sqldb)
  * SQL Server
    * [2025](https://learn.microsoft.com/en-us/sql/xquery/xquery-language-reference-sql-server?view=sql-server-ver17)
    * [2022](https://learn.microsoft.com/en-us/sql/xquery/xquery-language-reference-sql-server?view=sql-server-ver16)
    * [2019](https://learn.microsoft.com/en-us/sql/xquery/xquery-language-reference-sql-server?view=sql-server-ver15)
    * [2017](https://learn.microsoft.com/en-us/sql/xquery/xquery-language-reference-sql-server?view=sql-server-2017)
    * [2016](https://learn.microsoft.com/en-us/sql/xquery/xquery-language-reference-sql-server?view=sql-server-2016)
  * SQL Server on Linux
    * [2025](https://learn.microsoft.com/en-us/sql/xquery/xquery-language-reference-sql-server?view=sql-server-linux-ver17)
    * [2022](https://learn.microsoft.com/en-us/sql/xquery/xquery-language-reference-sql-server?view=sql-server-linux-ver16)
    * [2019](https://learn.microsoft.com/en-us/sql/xquery/xquery-language-reference-sql-server?view=sql-server-linux-ver15)
    * [2017](https://learn.microsoft.com/en-us/sql/xquery/xquery-language-reference-sql-server?view=sql-server-linux-2017)


Search
Suggestions will filter as you type
  * [SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/?view=sql-server-ver17)
  * [Docs navigation tips](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17)
  * [Previous versions 2005-2014](https://learn.microsoft.com/en-us/sql/sql-server/previous-versions-sql-server?view=sql-server-ver17)
  *     * [What is SQL Server?](https://learn.microsoft.com/en-us/sql/sql-server/what-is-sql-server?view=sql-server-ver17)
    * [Connect to the Database Engine](https://learn.microsoft.com/en-us/sql/sql-server/connect-to-database-engine?view=sql-server-ver17)
  *     *       * [xQuery](https://learn.microsoft.com/en-us/sql/xquery/xquery-language-reference-sql-server?view=sql-server-ver17)
      * [Modules & Prologs - XQuery Prolog](https://learn.microsoft.com/en-us/sql/xquery/modules-and-prologs-xquery-prolog?view=sql-server-ver17)
      * [Modules & Prologs](https://learn.microsoft.com/en-us/sql/xquery/modules-and-prologs-xquery?view=sql-server-ver17)
      * [Type Casting Rules in XQuery](https://learn.microsoft.com/en-us/sql/xquery/type-casting-rules-in-xquery?view=sql-server-ver17)
      * [XQuery Operators Against the xml Data Type](https://learn.microsoft.com/en-us/sql/xquery/xquery-operators-against-the-xml-data-type?view=sql-server-ver17)


Download PDF
Table of contents  Exit editor mode
  1. [ Learn ](https://learn.microsoft.com/en-us/?view=sql-server-ver17)
  2. [ SQL ](https://learn.microsoft.com/en-us/sql/?view=sql-server-ver17)
  3. [ SQL Server ](https://learn.microsoft.com/en-us/sql/sql-server/?view=sql-server-ver17)


  1. [Learn](https://learn.microsoft.com/en-us/?view=sql-server-ver17)
  2. [SQL](https://learn.microsoft.com/en-us/sql/?view=sql-server-ver17)
  3. [SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/?view=sql-server-ver17)


Ask Learn Ask Learn Focus mode
Table of contents [ Read in English ](https://learn.microsoft.com/en-us/sql/xquery/xquery-language-reference-sql-server?view=sql-server-ver17) Add to Collections Add to plan
* * *
#### Share via
* * *
Copy Markdown Print
* * *
Note
Access to this page requires authorization. You can try [signing in](https://learn.microsoft.com/en-us/sql/xquery/xquery-language-reference-sql-server?view=sql-server-ver17) or changing directories.
Access to this page requires authorization. You can try changing directories.
# XQuery Language Reference (SQL Server)
Feedback
Summarize this article for me
##  In this article
  1. [In This Section](https://learn.microsoft.com/en-us/sql/xquery/xquery-language-reference-sql-server?view=sql-server-ver17#in-this-section)
  2. [See Also](https://learn.microsoft.com/en-us/sql/xquery/xquery-language-reference-sql-server?view=sql-server-ver17#see-also)


**Applies to:** ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to)
Transact-SQL supports a subset of the XQuery language that is used for querying the **xml** data type. This XQuery implementation is aligned with the July 2004 Working Draft of XQuery. The language is under development by the World Wide Web Consortium (W3C), with the participation of all major database vendors and also Microsoft. Because the W3C specifications may undergo future revisions before becoming a W3C recommendation, this implementation may be different from the final recommendation. This topic outlines the semantics and syntax of the subset of XQuery that is supported in SQL Server.
For more information, see the [W3C XQuery 1.0 Language Specification](https://go.microsoft.com/fwlink/?LinkId=48846).
XQuery is a language that can query structured or semi-structured XML data. With the **xml** data type support provided in the Database Engine, documents can be stored in a database and then queried by using XQuery.
XQuery is based on the existing XPath query language, with support added for better iteration, better sorting results, and the ability to construct the necessary XML. XQuery operates on the XQuery Data Model. This is an abstraction of XML documents, and the XQuery results that can be typed or untyped. The type information is based on the types provided by the W3C XML Schema language. If no typing information is available, XQuery handles the data as untyped. This is similar to how XPath version 1.0 handles XML.
To query an XML instance stored in a variable or column of **xml** type, you use the [xml Data Type Methods](https://learn.microsoft.com/en-us/sql/t-sql/xml/xml-data-type-methods?view=sql-server-ver17). For example, you can declare a variable of **xml** type and query it by using the **query()** method of the **xml** data type.
SQL
Copy
```
DECLARE @x xml
SET @x = '<ROOT><a>111</a></ROOT>'
SELECT @x.query('/ROOT/a')

```

In the following example, the query is specified against the Instructions column of **xml** type in ProductModel table in the AdventureWorks database.
SQL
Copy
```
SELECT Instructions.query('declare namespace AWMI="https://schemas.microsoft.com/sqlserver/2004/07/adventure-works/ProductModelManuInstructions";
    /AWMI:root/AWMI:Location[@LocationID=10]
') as Result
FROM  Production.ProductModel
WHERE ProductModelID=7

```

The XQuery includes the namespace declaration, `declare namespace``AWMI=...`, and the query expression, `/AWMI:root/AWMI:Location[@LocationID=10]`.
Note that the XQuery is specified against the Instructions column of **xml** type. The [query() method](https://learn.microsoft.com/en-us/sql/t-sql/xml/query-method-xml-data-type?view=sql-server-ver17) of the xml data type is used to specify the XQuery.
The following table lists the related topics that can help in understanding the implementation of XQuery in the Database Engine.
Expand table
Topic | Description
---|---
[XML Data (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/xml/xml-data-sql-server?view=sql-server-ver17) | Explains the support for the **xml** data type in the Database Engine and the methods you can use against this data type. The **xml** data type forms the input XQuery data model on which the XQuery expressions are executed.
[XML Schema Collections (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/xml/xml-schema-collections-sql-server?view=sql-server-ver17) | Describes how the XML instances stored in a database can be typed. This means you can associate an XML schema collection with the **xml** type column. All the instances stored in the column are validated and typed against the schema in the collection and provide the type information for XQuery.
The organization of this section is based on the World Wide Web Consortium (W3C) XQuery working draft specification. Some of the diagrams provided in this section are taken from that specification. This section compares the Microsoft XQuery implementation to the W3C specification, describes how Microsoft XQuery is different from the W3C and indicates what W3C features are not supported. The W3C specification is available at [http://www.w3.org/TR/2004/WD-xquery-20040723](https://go.microsoft.com/fwlink/?LinkId=48846).
[](https://learn.microsoft.com/en-us/sql/xquery/xquery-language-reference-sql-server?view=sql-server-ver17#in-this-section)
## In This Section
Expand table
Topic | Description
---|---
[XQuery Basics](https://learn.microsoft.com/en-us/sql/xquery/xquery-basics?view=sql-server-ver17) | Provides a basic overview of XQuery concepts, and also the expression evaluation (static and dynamic context), atomization, effective Boolean value, XQuery type system, sequence type matching, and error handling.
[XQuery Expressions](https://learn.microsoft.com/en-us/sql/xquery/xquery-expressions?view=sql-server-ver17) | Describes XQuery primary expressions, path expressions, sequence expressions, arithmetic comparison and logical expressions, XQuery construction, FLWOR expression, conditional and quantified expressions, and various expressions on sequence types.
[Modules and Prologs (XQuery)](https://learn.microsoft.com/en-us/sql/xquery/modules-and-prologs-xquery?view=sql-server-ver17) | Describes XQuery prolog.
[XQuery Functions against the xml Data Type](https://learn.microsoft.com/en-us/sql/xquery/xquery-functions-against-the-xml-data-type?view=sql-server-ver17) | Describes a list of the XQuery functions that are supported.
[XQuery Operators Against the xml Data Type](https://learn.microsoft.com/en-us/sql/xquery/xquery-operators-against-the-xml-data-type?view=sql-server-ver17) | Describes XQuery operators that are supported.
[Additional Sample XQueries Against the xml Data Type](https://learn.microsoft.com/en-us/sql/xquery/additional-sample-xqueries-against-the-xml-data-type?view=sql-server-ver17) | Provides additional XQuery samples.
[](https://learn.microsoft.com/en-us/sql/xquery/xquery-language-reference-sql-server?view=sql-server-ver17#see-also)
## See Also
[XML Data (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/xml/xml-data-sql-server?view=sql-server-ver17)
[XML Schema Collections (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/xml/xml-schema-collections-sql-server?view=sql-server-ver17)
[Examples of Bulk Import and Export of XML Documents (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/examples-of-bulk-import-and-export-of-xml-documents-sql-server?view=sql-server-ver17)
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
  * Last updated on 04/03/2023


Ask Learn is an AI assistant that can answer questions, clarify concepts, and define terms using trusted Microsoft documentation.
Please sign in to use Ask Learn.
[ Sign in ](https://learn.microsoft.com/en-us/sql/xquery/xquery-language-reference-sql-server?view=sql-server-ver17)
