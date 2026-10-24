Version SQL Server 2025
  * Analytics Platform System (PDW)
    * [2016-AU7](https://learn.microsoft.com/en-us/sql/relational-databases/xml/xml-data-sql-server?view=aps-pdw-2016-au7)
    * [2016-AU6](https://learn.microsoft.com/en-us/sql/relational-databases/xml/xml-data-sql-server?view=aps-pdw-2016)
  * [Azure SQL Database](https://learn.microsoft.com/en-us/sql/relational-databases/xml/xml-data-sql-server?view=azuresqldb-current)
  * [Azure SQL Managed Instance](https://learn.microsoft.com/en-us/sql/relational-databases/xml/xml-data-sql-server?view=azuresqldb-mi-current)
  * [Azure Synapse Analytics](https://learn.microsoft.com/en-us/sql/relational-databases/xml/xml-data-sql-server?view=azure-sqldw-latest)
  * [Fabric Data Warehouse](https://learn.microsoft.com/en-us/sql/relational-databases/xml/xml-data-sql-server?view=fabric)
  * [Fabric SQL database](https://learn.microsoft.com/en-us/sql/relational-databases/xml/xml-data-sql-server?view=fabric-sqldb)
  * SQL Server
    * [2025](https://learn.microsoft.com/en-us/sql/relational-databases/xml/xml-data-sql-server?view=sql-server-ver17)
    * [2022](https://learn.microsoft.com/en-us/sql/relational-databases/xml/xml-data-sql-server?view=sql-server-ver16)
    * [2019](https://learn.microsoft.com/en-us/sql/relational-databases/xml/xml-data-sql-server?view=sql-server-ver15)
    * [2017](https://learn.microsoft.com/en-us/sql/relational-databases/xml/xml-data-sql-server?view=sql-server-2017)
    * [2016](https://learn.microsoft.com/en-us/sql/relational-databases/xml/xml-data-sql-server?view=sql-server-2016)
  * SQL Server on Linux
    * [2025](https://learn.microsoft.com/en-us/sql/relational-databases/xml/xml-data-sql-server?view=sql-server-linux-ver17)
    * [2022](https://learn.microsoft.com/en-us/sql/relational-databases/xml/xml-data-sql-server?view=sql-server-linux-ver16)
    * [2019](https://learn.microsoft.com/en-us/sql/relational-databases/xml/xml-data-sql-server?view=sql-server-linux-ver15)
    * [2017](https://learn.microsoft.com/en-us/sql/relational-databases/xml/xml-data-sql-server?view=sql-server-linux-2017)


Search
Suggestions will filter as you type
  * [SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/?view=sql-server-ver17)
  * [Docs navigation tips](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17)
  * [Previous versions 2005-2014](https://learn.microsoft.com/en-us/sql/sql-server/previous-versions-sql-server?view=sql-server-ver17)
  *     * [What is SQL Server?](https://learn.microsoft.com/en-us/sql/sql-server/what-is-sql-server?view=sql-server-ver17)
    * [Connect to the Database Engine](https://learn.microsoft.com/en-us/sql/sql-server/connect-to-database-engine?view=sql-server-ver17)
  *     * [Hierarchical Data](https://learn.microsoft.com/en-us/sql/relational-databases/hierarchical-data-sql-server?view=sql-server-ver17)
    *       * [XML data](https://learn.microsoft.com/en-us/sql/relational-databases/xml/xml-data-sql-server?view=sql-server-ver17)


Download PDF
Table of contents  Exit editor mode
  1. [ Learn ](https://learn.microsoft.com/en-us/?view=sql-server-ver17)
  2. [ SQL ](https://learn.microsoft.com/en-us/sql/?view=sql-server-ver17)
  3. [ SQL Server ](https://learn.microsoft.com/en-us/sql/sql-server/?view=sql-server-ver17)


  1. [Learn](https://learn.microsoft.com/en-us/?view=sql-server-ver17)
  2. [SQL](https://learn.microsoft.com/en-us/sql/?view=sql-server-ver17)
  3. [SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/?view=sql-server-ver17)


Ask Learn Ask Learn Focus mode
Table of contents [ Read in English ](https://learn.microsoft.com/en-us/sql/relational-databases/xml/xml-data-sql-server?view=sql-server-ver17) Add to Collections Add to plan
* * *
#### Share via
* * *
Copy Markdown Print
* * *
Note
Access to this page requires authorization. You can try [signing in](https://learn.microsoft.com/en-us/sql/relational-databases/xml/xml-data-sql-server?view=sql-server-ver17) or changing directories.
Access to this page requires authorization. You can try changing directories.
# XML data (SQL Server)
Feedback
Summarize this article for me
##  In this article
  1. [Next steps](https://learn.microsoft.com/en-us/sql/relational-databases/xml/xml-data-sql-server?view=sql-server-ver17#next-steps)
  2. [See also](https://learn.microsoft.com/en-us/sql/relational-databases/xml/xml-data-sql-server?view=sql-server-ver17#see-also)


**Applies to:** ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure SQL Database](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure SQL Managed Instance](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL database in Microsoft Fabric](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to)
SQL Server provides a powerful platform for developing rich applications for semi-structured data management. Support for XML is integrated into all the components in SQL Server in the following ways:
  * The **xml** data type. XML values can be stored natively in an **xml** data type column that can be typed according to a collection of XML schemas, or left untyped. You can index the XML column.
  * The ability to specify an XQuery query against XML data stored in columns and variables of the **xml** type.
  * Enhancements to OPENROWSET to allow bulk loading of XML data.
  * The FOR XML clause, to retrieve relational data in XML format.
  * The OPENXML function, to retrieve XML data in relational format.
  * XML compression provides a method to compress off-row XML data for both XML columns and indexes, improving capacity requirements. For more information, see [CREATE TABLE (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-table-transact-sql?view=sql-server-ver17) and [CREATE INDEX (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-index-transact-sql?view=sql-server-ver17). XML compression is available in SQL Server 2022 (16.x) and later versions, Azure SQL Database, and Azure SQL Managed Instance.


[](https://learn.microsoft.com/en-us/sql/relational-databases/xml/xml-data-sql-server?view=sql-server-ver17#next-steps)
## Next steps
  * [XML Data Type and Columns (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/xml/xml-data-type-and-columns-sql-server?view=sql-server-ver17)
  * [XML Indexes (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/xml/xml-indexes-sql-server?view=sql-server-ver17)
  * [XML Schema Collections (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/xml/xml-schema-collections-sql-server?view=sql-server-ver17)
  * [FOR XML (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/xml/for-xml-sql-server?view=sql-server-ver17)
  * [OPENXML (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/functions/openxml-transact-sql?view=sql-server-ver17)


[](https://learn.microsoft.com/en-us/sql/relational-databases/xml/xml-data-sql-server?view=sql-server-ver17#see-also)
## See also
  * [Examples of Bulk Import and Export of XML Documents (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/examples-of-bulk-import-and-export-of-xml-documents-sql-server?view=sql-server-ver17)
  * [XQuery Language Reference (SQL Server)](https://learn.microsoft.com/en-us/sql/xquery/xquery-language-reference-sql-server?view=sql-server-ver17)
  * [xml (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/xml/xml-transact-sql?view=sql-server-ver17)


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
  * [ Create XML data type variables and columns - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/xml/create-xml-data-type-variables-and-columns?source=recommendations)
Learn how to create columns and variables of the XML data type in SQL Server.
  * [ OPENXML (SQL Server) - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/xml/openxml-sql-server?source=recommendations)
Learn about the OPENXML statement in SQL Server that provides a rowset view of the internal representation of an XML document.
  * [ Load XML data - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/xml/load-xml-data?source=recommendations)
Learn several methods for transferring XML data into SQL Server databases.
  * [ xml data type and columns (SQL Server) - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/xml/xml-data-type-and-columns-sql-server?source=recommendations)
Learn about the advantages and limitations of the xml data type for storing XML data in SQL Server.
  * [ Create instances of XML data - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/xml/create-instances-of-xml-data?source=recommendations)
Learn how to create instances of XML data using bulk load, constant assignments, the SELECT statement and FOR XML clause, or by type casting string instances.
  * [ XML query options and preserved data - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/xml/retrieve-and-query-xml-data?source=recommendations)
Learn about the query options that must be specified when querying XML data, and about the parts of XML instances that aren't preserved when stored in databases.
  * [ xml (Transact-SQL) - SQL Server ](https://learn.microsoft.com/en-us/sql/t-sql/xml/xml-transact-sql?source=recommendations)
xml (Transact-SQL)
  * [ Compare Typed XML to Untyped XML - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/xml/compare-typed-xml-to-untyped-xml?source=recommendations)
Learn about the differences between typed and untyped XML.


Show 5 more
Certification
[ Microsoft Certified: Azure Cosmos DB Developer Specialty - Certifications ](https://learn.microsoft.com/en-us/credentials/certifications/azure-cosmos-db-developer-specialty/?source=recommendations)
Write efficient queries, create indexing policies, manage, and provision resources in the SQL API and SDK with Microsoft Azure Cosmos DB.
Mar 8, 4 PM - Mar 8, 4 PM
Experiment with what's next in AI-driven apps and agent design
* * *
  * Last updated on 01/30/2024


Ask Learn is an AI assistant that can answer questions, clarify concepts, and define terms using trusted Microsoft documentation.
Please sign in to use Ask Learn.
[ Sign in ](https://learn.microsoft.com/en-us/sql/relational-databases/xml/xml-data-sql-server?view=sql-server-ver17)
