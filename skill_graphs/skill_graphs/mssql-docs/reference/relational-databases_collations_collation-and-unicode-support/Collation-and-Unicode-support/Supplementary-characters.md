## Supplementary characters
The Unicode Consortium allocates to each character a unique code point, which is a value in the range 000000 - 10FFFF. The most frequently used characters have code point values in the range 000000 - 00FFFF (65,536 characters) which fit into an 8-bit or 16-bit word in memory and on-disk. This range is usually designated as the Basic Multilingual Plane (BMP).
But the Unicode Consortium has established 16 additional "planes" of characters, each the same size as the BMP. This definition allows Unicode the potential to represent 1,114,112 characters (that is, 216 * 17 characters) within the code point range 000000 - 10FFFF. Characters with code point value larger than 00FFFF require two to four consecutive 8-bit words (UTF-8), or two consecutive 16-bit words (UTF-16). These characters located beyond the BMP are called _supplementary characters_ , and the additional consecutive 8-bit or 16-bit words are called _surrogate pairs_. For more information about supplementary characters, surrogates, and surrogate pairs, see
SQL Server provides data types such as **nchar** and **nvarchar** to store Unicode data in the BMP range (000000 - 00FFFF), which the Database Engine encodes using UCS-2.
SQL Server 2012 (11.x) introduced a new family of supplementary character (`_SC`) collations that can be used with the **nchar** , **nvarchar** , and **sql_variant** data types to represent the full Unicode character range (000000 - 10FFFF). For example: `Latin1_General_100_CI_AS_SC` or, if you're using a Japanese collation, `Japanese_Bushu_Kakusu_100_CI_AS_SC`.
SQL Server 2019 (15.x) extends supplementary character support to the **char** and **varchar** data types with the new [UTF-8 enabled](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#utf8) collations (`_UTF8`). These data types are also capable of representing the full Unicode character range.
Starting with SQL Server 2017 (14.x), all new collations automatically support supplementary characters.
If you use supplementary characters:
  * Supplementary characters can be used in ordering and comparison operations in collation versions 90 or greater.
  * All version 100 collations support linguistic sorting with supplementary characters.
  * Supplementary characters aren't supported for use in metadata, such as in names of database objects.
  * The SC flag can be applied to:
    * Version 90 collations
    * Version 100 collations
  * The SC flag can't be applied to:
    * Version 80 non-versioned Windows collations
    * The BIN or BIN2 binary collations
    * The SQL* collations
    * Version 140 collations (these don't need the SC flag, because they already support supplementary characters)


The following table compares the behavior of some string functions and string operators when they use supplementary characters with and without a supplementary character-aware (SCA) collation:
Expand table
String function or operator | With an SCA collation | Without an SCA collation
---|---|---
[CHARINDEX](https://learn.microsoft.com/en-us/sql/t-sql/functions/charindex-transact-sql?view=sql-server-ver17)

[LEN](https://learn.microsoft.com/en-us/sql/t-sql/functions/len-transact-sql?view=sql-server-ver17)
[PATINDEX](https://learn.microsoft.com/en-us/sql/t-sql/functions/patindex-transact-sql?view=sql-server-ver17) | The UTF-16 surrogate pair is counted as a single code point. | The UTF-16 surrogate pair is counted as two code points.
[LEFT](https://learn.microsoft.com/en-us/sql/t-sql/functions/left-transact-sql?view=sql-server-ver17)

[REPLACE](https://learn.microsoft.com/en-us/sql/t-sql/functions/replace-transact-sql?view=sql-server-ver17)
[REVERSE](https://learn.microsoft.com/en-us/sql/t-sql/functions/reverse-transact-sql?view=sql-server-ver17)
[RIGHT](https://learn.microsoft.com/en-us/sql/t-sql/functions/right-transact-sql?view=sql-server-ver17)
[SUBSTRING](https://learn.microsoft.com/en-us/sql/t-sql/functions/substring-transact-sql?view=sql-server-ver17)
[STUFF](https://learn.microsoft.com/en-us/sql/t-sql/functions/stuff-transact-sql?view=sql-server-ver17) | These functions treat each surrogate pair as a single code point and work as expected. | These functions might split any surrogate pairs and lead to unexpected results.
[NCHAR](https://learn.microsoft.com/en-us/sql/t-sql/functions/nchar-transact-sql?view=sql-server-ver17) | Returns the character that corresponds to the specified Unicode code point value in the range 0 - 0x10FFFF. If the specified value lies in the range 0 - 0xFFFF, one character is returned. For higher values, the corresponding surrogate is returned. | A value higher than 0xFFFF returns `NULL` instead of the corresponding surrogate.
[UNICODE](https://learn.microsoft.com/en-us/sql/t-sql/functions/unicode-transact-sql?view=sql-server-ver17) | Returns a UTF-16 code point in the range 0 - 0x10FFFF. | Returns a UCS-2 code point in the range 0 - 0xFFFF.
[Wildcard - match one character](https://learn.microsoft.com/en-us/sql/t-sql/language-elements/wildcard-match-one-character-transact-sql?view=sql-server-ver17)

[Wildcard - characters not to match](https://learn.microsoft.com/en-us/sql/t-sql/language-elements/wildcard-character-s-not-to-match-transact-sql?view=sql-server-ver17) | Supplementary characters are supported for all wildcard operations. | Supplementary characters aren't supported for these wildcard operations. Other wildcard operators are supported.
[](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#gb18030-support)
