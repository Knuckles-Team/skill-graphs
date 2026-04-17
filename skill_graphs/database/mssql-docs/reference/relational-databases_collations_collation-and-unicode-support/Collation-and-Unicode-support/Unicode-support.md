## Unicode support
Unicode is a standard for mapping code points to characters. Because it's designed to cover all the characters of all the languages of the world, you don't need different code pages to handle different sets of characters.
[](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#unicode-basics)
### Unicode basics
Storing data in multiple languages within one database is difficult to manage when you use only character data and code pages. It's also difficult to find one code page for the database that can store all the required language-specific characters. Additionally, it's difficult to guarantee the correct translation of special characters when they're being read or updated by various clients that are running various code pages. Databases that support international clients should always use Unicode data types instead of non-Unicode data types.
For example, consider a database of customers in North America that must handle three major languages:
  * Spanish names and addresses for Mexico
  * French names and addresses for Quebec
  * English names and addresses for the rest of Canada and the United States


When you use only character columns and code pages, you must take care to ensure that the database is installed with a code page that will handle the characters of all three languages. You must also take care to guarantee the correct translation of characters from any of the languages when the characters are read by clients that are running a code page for another language.
The code pages that a client uses are determined by the operating system (OS) settings. To set client code pages on the Windows operating system, use **Regional Settings** in Control Panel.
It would be difficult to select a code page for character data types that will support all the characters that are required by a worldwide audience. The easiest way to manage character data in international databases is to always use a data type that supports Unicode.
[](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#unicode-data-types)
### Unicode data types
If you store character data that reflects multiple languages, use Unicode data types (**nchar** , **nvarchar** , and **ntext**) instead of non-Unicode data types (**char** , **varchar** , and **text**).
For Unicode data types, the Database Engine can represent up to 65,536 characters using UCS-2, or the full Unicode range (1,114,112 characters) if supplementary characters are used. For more information about enabling supplementary characters, see [Supplementary Characters](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#Supplementary_Characters).
Alternatively, starting with SQL Server 2019 (15.x), if a UTF-8 enabled collation (`_UTF8`) is used, previously non-Unicode data types (**char** and **varchar**) become Unicode data types using UTF-8 encoding. SQL Server 2019 (15.x) doesn't change the behavior of previously existing Unicode data types (**nchar** , **nvarchar** , and **ntext**), which continue to use UCS-2 or UTF-16 encoding. For more information, see [Storage differences between UTF-8 and UTF-16](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#storage_differences).
[](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#unicode-considerations)
### Unicode considerations
Significant limitations are associated with non-Unicode data types. This is because a non-Unicode computer is limited to using a single code page. You might experience performance gain by using Unicode, because it requires fewer code-page conversions. Unicode collations must be selected individually at the database, column, or expression level because they aren't supported at the server level.
When you move data from a server to a client, your server collation might not be recognized by older client drivers. This can occur when you move data from a Unicode server to a non-Unicode client. Your best option might be to upgrade the client operating system so that the underlying system collations are updated. If the client has database client software installed, you might consider applying a service update to the database client software.
You can also try to use a different collation for the data on the server. Choose a collation that maps to a code page on the client. To use the UTF-16 collations that are available in SQL Server (SQL Server 2012 (11.x) and later) to improve searching and sorting of some Unicode characters (Windows collations only), you can select either one of the supplementary characters (`_SC`) collations or one of the version 140 collations.
To use the UTF-8 collations that are available in SQL Server 2019 (15.x), and to improve searching and sorting of some Unicode characters (Windows collations only), you must select UTF-8 encoding-enabled collations (`_UTF8`).
  * The UTF8 flag can be applied to:
    * Linguistic collations that already support supplementary characters (`_SC`) or variation-selector-sensitive (`_VSS`) awareness
    * `BIN2` binary collation
  * The UTF8 flag can't be applied to:
    * Linguistic collations that don't support supplementary characters (`_SC`) or variation-selector-sensitive (`_VSS`) awareness
    * The `BIN` binary collations
    * The `SQL_*` collations


To evaluate issues that are related to using Unicode or non-Unicode data types, test your scenario to measure performance differences in your environment. It's a good practice to standardize the collation that's used on systems across your organization, and to deploy Unicode servers and clients wherever possible.
In many situations, SQL Server interacts with other servers or clients, and your organization might use multiple data-access standards between applications and server instances. SQL Server clients are one of two main types:
  * **Unicode clients** that use OLE DB and Open Database Connectivity (ODBC) version 3.7 or later.
  * **Non-Unicode clients** that use DB-Library and ODBC version 3.6 or earlier.


The following table provides information about using multilingual data with various combinations of Unicode and non-Unicode servers:
Expand table
Server | Client | Benefits or limitations
---|---|---
Unicode | Unicode | Because Unicode data is used throughout the system, this scenario provides the best performance and protection from corruption of retrieved data. This is the situation with ActiveX Data Objects (ADO), OLE DB, and ODBC version 3.7 or later.
Unicode | Non-Unicode | In this scenario, especially with connections between a server that's running a newer operating system and a client that's running an earlier version of SQL Server, or on an older operating system, there can be limitations or errors when you move data to a client computer. Unicode data on the server tries to map to a corresponding code page on the non-Unicode client to convert the data.
Non-Unicode | Unicode | This isn't an ideal configuration for using multilingual data. You can't write Unicode data to the non-Unicode server. Problems are likely to occur when data is sent to servers that are outside the server's code page.
Non-Unicode | Non-Unicode | This is a very limiting scenario for multilingual data. You can use only a single code page.
[](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#supplementary-characters)
