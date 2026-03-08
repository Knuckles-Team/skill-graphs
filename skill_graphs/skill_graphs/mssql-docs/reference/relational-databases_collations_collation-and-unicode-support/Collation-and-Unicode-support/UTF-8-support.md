## UTF-8 support
SQL Server 2019 (15.x) introduces full support for the widely used UTF-8 character encoding as an import or export encoding, and as database-level or column-level collation for string data. UTF-8 is allowed in the **char** and **varchar** data types, and it's enabled when you create or change an object's collation to a collation that has a _UTF8_ suffix. One example is changing `Latin1_General_100_CI_AS_SC` to `Latin1_General_100_CI_AS_SC_UTF8`.
UTF-8 is available only to Windows collations that support supplementary characters, as introduced in SQL Server 2012 (11.x). The **nchar** and **nvarchar** data types allow UCS-2 or UTF-16 encoding only, and they remain unchanged.
Azure SQL Database and Azure SQL Managed Instance also support UTF-8 on database and column level, while SQL Managed Instance supports this on a server level as well.
[](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#storage-differences-between-utf-8-and-utf-16)
### Storage differences between UTF-8 and UTF-16
The Unicode Consortium allocates to each character a unique code point, which is a value in the range 000000 - 10FFFF. With SQL Server 2019 (15.x), both UTF-8 and UTF-16 encodings are available to represent the full range:
  * With UTF-8 encoding, characters in the ASCII range (000000 - 00007F) require 1 byte, code points 000080 - 0007FF require 2 bytes, code points 000800 - 00FFFF require 3 bytes, and code points 0010000 - 0010FFFF require 4 bytes.
  * With UTF-16 encoding, code points 000000 - 00FFFF require 2 bytes, and code points 0010000 - 0010FFFF require 4 bytes.


The following table lists the encoding storage bytes for each character range and encoding type:
Expand table
Code range (hexadecimal) | Code range (decimal) | Storage bytes 1 with UTF-8 | Storage bytes 1 with UTF-16
---|---|---|---
000000 - 00007F | 0 - 127 | 1 | 2
000080 - 00009F
0000A0 - 0003FF
000400 - 0007FF | 128 - 159
160 - 1,023
1,024 - 2,047 | 2 | 2
000800 - 003FFF
004000 - 00FFFF | 2,048 - 16,383
16,384 - 65,535 | 3 | 2
010000 - 03FFFF 2

040000 - 10FFFF 2 | 65,536 - 262,143 2
262,144 - 1,114,111 2 | 4 | 4
1 _Storage bytes_ refer to the encoded byte length, not the data-type on-disk storage size. For more information about on-disk storage sizes, see [nchar and nvarchar](https://learn.microsoft.com/en-us/sql/t-sql/data-types/nchar-and-nvarchar-transact-sql?view=sql-server-ver17) and [char and varchar](https://learn.microsoft.com/en-us/sql/t-sql/data-types/char-and-varchar-transact-sql?view=sql-server-ver17).
2 The code point range for [supplementary characters](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#supplementary-characters).
It's a common perception, in [char and varchar](https://learn.microsoft.com/en-us/sql/t-sql/data-types/char-and-varchar-transact-sql?view=sql-server-ver17) or in [nchar and nvarchar](https://learn.microsoft.com/en-us/sql/t-sql/data-types/nchar-and-nvarchar-transact-sql?view=sql-server-ver17), that _n_ defines the number of characters. This is because, in the example of a **char(10)** column, 10 ASCII characters in the range 0 - 127 can be stored by using a collation such as `Latin1_General_100_CI_AI`, because each character in this range uses only 1 byte. However, in [char and varchar](https://learn.microsoft.com/en-us/sql/t-sql/data-types/char-and-varchar-transact-sql?view=sql-server-ver17), _n_ defines the string size in _bytes_ (0 - 8,000), and in [nchar and nvarchar](https://learn.microsoft.com/en-us/sql/t-sql/data-types/nchar-and-nvarchar-transact-sql?view=sql-server-ver17), _n_ defines the string size in _byte-pairs_ (0 - 4,000). _n_ never defines numbers of characters that can be stored.
Choosing the appropriate Unicode encoding and data type might give you significant storage savings or increase your current storage footprint, depending on the character set in use. For example, when you use a Latin collation that's UTF-8 enabled, such as `Latin1_General_100_CI_AI_SC_UTF8`, a **char(10)** column stores 10 bytes and can hold 10 ASCII characters in the range 0 - 127. But it can hold only five characters in the range 128 - 2047 and only three characters in the range 2048 - 65535. By comparison, because a **nchar(10)** column stores 10 byte-pairs (20 bytes), it can hold 10 characters in the range 0 - 65535.
Before you decide whether to use UTF-8 or UTF-16 encoding for a database or column, consider the distribution of string data that will be stored:
  * If it's mostly in the ASCII range 0 - 127 (such as English), each character requires 1 byte with UTF-8 and 2 bytes with UTF-16. Using UTF-8 provides storage benefits. Changing an existing column data type with ASCII characters in the range 0 - 127 from **nchar(10)** to **char(10)** , and using an UTF-8 enabled collation, translates into a 50 percent reduction in storage requirements. This reduction is because **nchar(10)** requires 20 bytes for storage, compared with **char(10)** , which requires 10 bytes for the same Unicode string representation.
  * Above the ASCII range, almost all Latin-based script, and Greek, Cyrillic, Coptic, Armenian, Hebrew, Arabic, Syriac, Tāna, and N'Ko, require 2 bytes per character in both UTF-8 and UTF-16. In these cases, there are no significant storage differences for comparable data types (for example, between using **char** or **nchar**).
  * If it's mostly East Asian script (such as Korean, Chinese, and Japanese), each character requires 3 bytes with UTF-8 and 2 bytes with UTF-16. Using UTF-16 provides storage benefits.
  * Characters in the range 010000 - 10FFFF require 4 bytes in both UTF-8 and UTF-16. In these cases, there are no storage differences for comparable data types (for example, between using **char** or **nchar**).


For other considerations, see [Write International Transact-SQL Statements](https://learn.microsoft.com/en-us/sql/relational-databases/collations/write-international-transact-sql-statements?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#convert-to-utf-8)
### Convert to UTF-8
Because in [char and varchar](https://learn.microsoft.com/en-us/sql/t-sql/data-types/char-and-varchar-transact-sql?view=sql-server-ver17) or in [nchar and nvarchar](https://learn.microsoft.com/en-us/sql/t-sql/data-types/nchar-and-nvarchar-transact-sql?view=sql-server-ver17), the _n_ defines the byte storage size, not the number of characters that can be stored, it's important to determine the data type size you must convert to. The characters that exceed the size are to be truncated.
For example, consider a column defined as **nvarchar(100)** that stores 180 bytes of Japanese characters. In this example, the column data is currently encoded using UCS-2 or UTF-16, which uses 2 bytes per character. Converting the column type to **varchar(200)** isn't sufficient to prevent data truncation, because the new data type can only store 200 bytes, but Japanese characters require 3 bytes when encoded in UTF-8. The column must be defined as **varchar(270)** to avoid data loss through data truncation.
Therefore, you must know in advance what the projected byte size for the column definition is, before converting existing data to UTF-8, and adjust the new data type size accordingly. Refer to the Transact-SQL script or the SQL Notebook in the [DATALENGTH](https://learn.microsoft.com/en-us/sql/t-sql/functions/datalength-transact-sql?view=sql-server-ver17) function and the [COLLATE](https://learn.microsoft.com/en-us/sql/t-sql/statements/collations?view=sql-server-ver17) statement, to determine the appropriate data length requirements for UTF-8 conversion operations in an existing database.
To change the column collation and data type in an existing table, use one of the methods described in [Set or Change the Column Collation](https://learn.microsoft.com/en-us/sql/relational-databases/collations/set-or-change-the-column-collation?view=sql-server-ver17).
To change the database collation, allowing new objects to inherit the database collation by default, or to change the server collation, allowing new databases to inherit the system collation by default, see the [Related tasks](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#related-tasks) section of this article.
[](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#related-tasks)
