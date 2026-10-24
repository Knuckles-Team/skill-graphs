## Collation terms
  * [Collation](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#collation)
    * [Collation sets](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#collation-sets)
    * [Collation levels](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#collation-levels)
  * [Locale](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#locale)
  * [Code page](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#code-page)
  * [Sort order](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#sort-order)


[](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#collation)
### Collation
A collation specifies the bit patterns that represent each character in a dataset. Collations also determine the rules that sort and compare data. SQL Server supports storing objects that have different collations in a single database. For non-Unicode columns, the collation setting specifies the code page for the data and which characters can be represented. The data that you move between non-Unicode columns must be converted from the source code page to the destination code page.
Transact-SQL statement results can vary when the statement is run in the context of different databases that have different collation settings. If possible, use a standardized collation for your organization. This way, you don't have to specify the collation in every character or Unicode expression. If you must work with objects that have different collation and code page settings, code your queries to consider the rules of collation precedence. For more information, see [Collation precedence](https://learn.microsoft.com/en-us/sql/t-sql/statements/collation-precedence-transact-sql?view=sql-server-ver17).
The options associated with a collation are case sensitivity, accent sensitivity, kana sensitivity, width sensitivity, and variation-selector sensitivity. SQL Server 2019 (15.x) introduces an additional option for
You can specify these options by appending them to the collation name. For example, the collation `Japanese_Bushu_Kakusu_100_CS_AS_KS_WS_SC_UTF8` is case-sensitive, accent-sensitive, kana-sensitive, width-sensitive, and UTF-8 encoded. As another example, the collation `Japanese_Bushu_Kakusu_140_CI_AI_KS_WS_VSS` is case-insensitive, accent-insensitive, kana-sensitive, width-sensitive, variation-selector-sensitive, and it uses a legacy code page for **varchar**.
The behavior associated with these various options is described in the following table:
Expand table
Option | Description
---|---
Case-sensitive (`_CS`) | Distinguishes between uppercase and lowercase letters. If this option is selected, lowercase letters sort ahead of their uppercase versions. If this option isn't selected, the collation is case-insensitive. That is, SQL Server considers the uppercase and lowercase versions of letters to be identical for sorting purposes. You can explicitly select case insensitivity by specifying `_CI`.
Accent-sensitive (`_AS`) | Distinguishes between accented and unaccented characters. For example, `a` isn't equal to `á`. If this option isn't selected, the collation is accent-insensitive. That is, SQL Server considers the accented and unaccented versions of letters to be identical for sorting purposes. You can explicitly select accent insensitivity by specifying `_AI`.
Kana-sensitive (`_KS`) | Distinguishes between the two types of Japanese kana characters: Hiragana and Katakana. If this option isn't selected, the collation is kana-insensitive. That is, SQL Server considers Hiragana and Katakana characters to be equal for sorting purposes. Omitting this option is the only method of specifying kana-insensitivity.
Width-sensitive (`_WS`) | Distinguishes between full-width and half-width characters. If this option isn't selected, SQL Server considers the full-width and half-width representation of the same character to be identical for sorting purposes. Omitting this option is the only method of specifying width-insensitivity.
Variation-selector-sensitive (`_VSS`) | Distinguishes between various ideographic variation selectors in the Japanese collations `Japanese_Bushu_Kakusu_140` and `Japanese_XJIS_140`, which are introduced in SQL Server 2017 (14.x). A variation sequence consists of a base character plus a variation selector. If this `_VSS` option isn't selected, the collation is variation-selector-insensitive, and the variation selector isn't considered in the comparison. That is, SQL Server considers characters built upon the same base character with differing variation selectors to be identical for sorting purposes. For more information, see

Variation-selector-sensitive (`_VSS`) collations aren't supported in full-text search indexes. Full-text search indexes support only Accent-Sensitive (`_AS`), Kana-sensitive (`_KS`), and Width-sensitive (`_WS`) options. SQL Server XML and [Common language runtime (CLR) integration](https://learn.microsoft.com/en-us/sql/relational-databases/clr-integration/common-language-runtime-integration-overview?view=sql-server-ver17) engines don't support (`_VSS`) Variation selectors.
Binary (`_BIN`) 1 | Sorts and compares data in SQL Server tables based on the bit patterns defined for each character. Binary sort order is case-sensitive and accent-sensitive. Binary is also the fastest sorting order. For more information, see the [Binary collations](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#Binary-collations) section in this article.
Binary-code point (`_BIN2`) 1 | Sorts and compares data in SQL Server tables based on Unicode code points for Unicode data. For non-Unicode data, Binary-code point uses comparisons that are identical to those for binary sorts.

The advantage of using a Binary-code point sort order is that no data resorting is required in applications that compare sorted SQL Server data. As a result, a Binary-code point sort order provides simpler application development and possible performance increases. For more information, see the [Binary collations](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#Binary-collations) section in this article.
UTF-8 (`_UTF8`) | Enables UTF-8 encoded data to be stored in SQL Server. If this option isn't selected, SQL Server uses the default non-Unicode encoding format for the applicable data types. For more information, see the [UTF-8 Support](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#utf8) section in this article.
1 If Binary or Binary-code point is selected, the Case-sensitive (`_CS`), Accent-sensitive (`_AS`), Kana-sensitive (`_KS`), and Width-sensitive (`_WS`) options aren't available.
[](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#examples-of-collation-options)
#### Examples of collation options
Each collation is combined as a series of suffixes to define case-, accent-, width-, or kana-sensitivity. The following examples describe sort order behavior for various combinations of suffixes.
Expand table
Windows collation suffix | Sort order description
---|---
`_BIN` 1 | Binary sort
`_BIN2` 1, 2 | Binary-code point sort order
`_CI_AI` 2 | Case-insensitive, accent-insensitive, kana-insensitive, width-insensitive
`_CI_AI_KS` 2 | Case-insensitive, accent-insensitive, kana-sensitive, width-insensitive
`_CI_AI_KS_WS` 2 | Case-insensitive, accent-insensitive, kana-sensitive, width-sensitive
`_CI_AI_WS` 2 | Case-insensitive, accent-insensitive, kana-insensitive, width-sensitive
`_CI_AS` 2 | Case-insensitive, accent-sensitive, kana-insensitive, width-insensitive
`_CI_AS_KS` 2 | Case-insensitive, accent-sensitive, kana-sensitive, width-insensitive
`_CI_AS_KS_WS` 2 | Case-insensitive, accent-sensitive, kana-sensitive, width-sensitive
`_CI_AS_WS` 2 | Case-insensitive, accent-sensitive, kana-insensitive, width-sensitive
`_CS_AI` 2 | Case-sensitive, accent-insensitive, kana-insensitive, width-insensitive
`_CS_AI_KS` 2 | Case-sensitive, accent-insensitive, kana-sensitive, width-insensitive
`_CS_AI_KS_WS` 2 | Case-sensitive, accent-insensitive, kana-sensitive, width-sensitive
`_CS_AI_WS` 2 | Case-sensitive, accent-insensitive, kana-insensitive, width-sensitive
`_CS_AS` 2 | Case-sensitive, accent-sensitive, kana-insensitive, width-insensitive
`_CS_AS_KS` 2 | Case-sensitive, accent-sensitive, kana-sensitive, width-insensitive
`_CS_AS_KS_WS` 2 | Case-sensitive, accent-sensitive, kana-sensitive, width-sensitive
`_CS_AS_WS` 2 | Case-sensitive, accent-sensitive, kana-insensitive, width-sensitive
1 If Binary or Binary-code point is selected, the Case-sensitive (`_CS`), Accent-sensitive (`_AS`), Kana-sensitive (`_KS`), and Width-sensitive (`_WS`) options aren't available.
2 Adding the UTF-8 option (`_UTF8`) enables you to encode Unicode data by using UTF-8. For more information, see the [UTF-8 Support](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#utf8) section in this article.
[](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#collation-sets)
### Collation sets
SQL Server supports the following collation sets:
  * [Windows collations](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#Windows-collations)
  * [Binary collations](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#Binary-collations)
  * [SQL Server collations](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#SQL-collations)


[](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#windows-collations)
#### Windows collations
Windows collations define rules for storing character data that are based on an associated Windows system locale. For a Windows collation, you can implement a comparison of non-Unicode data by using the same algorithm as that for Unicode data. The base Windows collation rules specify which alphabet or language is used when dictionary sorting is applied. The rules also specify the code page that's used to store non-Unicode character data. Both Unicode and non-Unicode sorting are compatible with string comparisons in a particular version of Windows. This provides consistency across data types within SQL Server, and it lets developers sort strings in their applications by using the same rules that are used by SQL Server. For more information, see [Windows collation name](https://learn.microsoft.com/en-us/sql/t-sql/statements/windows-collation-name-transact-sql?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#binary-collations)
#### Binary collations
Binary collations sort data based on the sequence of coded values that are defined by the locale and data type. They're case-sensitive. A binary collation in SQL Server defines the locale and the ANSI code page that are used. This enforces a binary sort order. Because they're relatively simple, binary collations help improve application performance. For non-Unicode data types, data comparisons are based on the code points that are defined on the ANSI code page. For Unicode data types, data comparisons are based on the Unicode code points. For binary collations on Unicode data types, the locale isn't considered in data sorts. For example, `Latin1_General_BIN` and `Japanese_BIN` yield identical sorting results when they're used on Unicode data. For more information, see [Windows collation name](https://learn.microsoft.com/en-us/sql/t-sql/statements/windows-collation-name-transact-sql?view=sql-server-ver17).
There are two types of binary collations in SQL Server:
  * The legacy `BIN` collations, which performed an incomplete code-point-to-code-point comparison for Unicode data. Legacy binary collations compared the first character as WCHAR, followed by a byte-by-byte comparison. In a BIN collation, only the first character is sorted according to the code point, and remaining characters are sorted according to their byte values.
  * The newer `BIN2` collations, which implement a pure code-point comparison. In a BIN2 collation, all characters are sorted according to their code points. Because the Intel platform is a little endian architecture, Unicode code characters are always stored byte-swapped.


[](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#sql-server-collations)
#### SQL Server collations
SQL Server collations (SQL_*) provide sort order compatibility with earlier versions of SQL Server. The dictionary sorting rules for non-Unicode data are incompatible with any sorting routine that's provided by Windows operating systems. However, sorting Unicode data is compatible with a particular version of Windows sorting rules. Because SQL Server collations use different comparison rules for non-Unicode and Unicode data, you see different results for comparisons of the same data, depending on the underlying data type.
For example, if you're using the SQL collation `SQL_Latin1_General_CP1_CI_AS`, the non-Unicode string `'a-c'` is less than the string `'ab'` because the hyphen (`-`) is sorted as a separate character that comes before `b`. However, if you convert these strings to Unicode and you perform the same comparison, the Unicode string `N'a-c'` is considered to be greater than `N'ab'`, because the Unicode sorting rules use a _word sort_ that ignores the hyphen.
For more information, see [SQL Server Collation Name](https://learn.microsoft.com/en-us/sql/t-sql/statements/sql-server-collation-name-transact-sql?view=sql-server-ver17).
During SQL Server setup, the default installation collation setting is determined by the operating system (OS) locale. You can change the server-level collation either during setup or by changing the OS locale before installation. For backward compatibility reasons, the default collation is set to the oldest available version that's associated with each specific locale. Therefore, this isn't always the recommended collation. To take full advantage of SQL Server features, change the default installation settings to use Windows collations. For example, for the OS locale "English (United States)" (code page 1252), the default collation during setup is `SQL_Latin1_General_CP1_CI_AS`, and it can be changed to its closest Windows collation counterpart, `Latin1_General_100_CI_AS_SC`.
When you upgrade an English-language instance of SQL Server, you can specify SQL Server collations (SQL_*) for compatibility with existing instances of SQL Server. Because the default collation for an instance of SQL Server is defined during setup, make sure that you specify the collation settings carefully when the following conditions are true:
  * Your application code depends on the behavior of previous SQL Server collations.
  * You must store character data that reflects multiple languages.


[](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#collation-levels)
### Collation levels
Setting collations are supported at the following levels of an instance of SQL Server:
  * [Server-level collations](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#Server-level-collations)
  * [Database-level collations](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#Database-level-collations)
  * [Column-level collations](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#Column-level-collations)
  * [Expression-level collations](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#Expression-level-collations)


[](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#server-level-collations)
#### Server-level collations
The default server collation is determined during SQL Server setup, and it becomes the default collation of the system databases and all user databases.
The following table shows the default collation designations, as determined by the operating system (OS) locale, including their Windows and SQL Language Code Identifiers (LCID):
Expand table
Windows locale | Windows LCID | SQL LCID | Default collation
---|---|---|---
Afrikaans (South Africa) | 0x0436 | 0x0409 | Latin1_General_CI_AS
Albanian (Albania) | 0x041c | 0x041c | Albanian_CI_AS
Alsatian (France) | 0x0484 | 0x0409 | Latin1_General_CI_AS
Amharic (Ethiopia) | 0x045e | 0x0409 | Latin1_General_CI_AS
Arabic (Algeria) | 0x1401 | 0x0401 | Arabic_CI_AS
Arabic (Bahrain) | 0x3c01 | 0x0401 | Arabic_CI_AS
Arabic (Egypt) | 0x0c01 | 0x0401 | Arabic_CI_AS
Arabic (Iraq) | 0x0801 | 0x0401 | Arabic_CI_AS
Arabic (Jordan) | 0x2c01 | 0x0401 | Arabic_CI_AS
Arabic (Kuwait) | 0x3401 | 0x0401 | Arabic_CI_AS
Arabic (Lebanon) | 0x3001 | 0x0401 | Arabic_CI_AS
Arabic (Libya) | 0x1001 | 0x0401 | Arabic_CI_AS
Arabic (Morocco) | 0x1801 | 0x0401 | Arabic_CI_AS
Arabic (Oman) | 0x2001 | 0x0401 | Arabic_CI_AS
Arabic (Qatar) | 0x4001 | 0x0401 | Arabic_CI_AS
Arabic (Saudi Arabia) | 0x0401 | 0x0401 | Arabic_CI_AS
Arabic (Syria) | 0x2801 | 0x0401 | Arabic_CI_AS
Arabic (Tunisia) | 0x1c01 | 0x0401 | Arabic_CI_AS
Arabic (U.A.E.) | 0x3801 | 0x0401 | Arabic_CI_AS
Arabic (Yemen) | 0x2401 | 0x0401 | Arabic_CI_AS
Armenian (Armenia) | 0x042b | 0x0419 | Latin1_General_CI_AS
Assamese (India) | 0x044d | 0x044d | Not available at server level
Azerbaijani (Azerbaijan, Cyrillic) | 0x082c | 0x082c | Deprecated, not available at server level
Azerbaijani (Azerbaijan, Latin) | 0x042c | 0x042c | Deprecated, not available at server level
Bashkir (Russia) | 0x046d | 0x046d | Latin1_General_CI_AI
Basque (Basque) | 0x042d | 0x0409 | Latin1_General_CI_AS
Belarusian (Belarus) | 0x0423 | 0x0419 | Cyrillic_General_CI_AS
Bangla (Bangladesh) | 0x0845 | 0x0445 | Not available at server level
Bengali (India) | 0x0445 | 0x0439 | Not available at server level
Bosnian (Bosnia and Herzegovina, Cyrillic) | 0x201a | 0x201a | Latin1_General_CI_AI
Bosnian (Bosnia and Herzegovina, Latin) | 0x141a | 0x141a | Latin1_General_CI_AI
Breton (France) | 0x047e | 0x047e | Latin1_General_CI_AI
Bulgarian (Bulgaria) | 0x0402 | 0x0419 | Cyrillic_General_CI_AS
Catalan (Catalan) | 0x0403 | 0x0409 | Latin1_General_CI_AS
Chinese (Hong Kong SAR, PRC) | 0x0c04 | 0x0404 | Chinese_Taiwan_Stroke_CI_AS
Chinese (Macao SAR) | 0x1404 | 0x1404 | Latin1_General_CI_AI
Chinese (Macao SAR) | 0x21404 | 0x21404 | Latin1_General_CI_AI
Chinese (PRC) | 0x0804 | 0x0804 | Chinese_PRC_CI_AS
Chinese (PRC) | 0x20804 | 0x20804 | Chinese_PRC_Stroke_CI_AS
Chinese (Singapore) | 0x1004 | 0x0804 | Chinese_PRC_CI_AS
Chinese (Singapore) | 0x21004 | 0x20804 | Chinese_PRC_Stroke_CI_AS
Chinese (Taiwan) | 0x30404 | 0x30404 | Chinese_Taiwan_Bopomofo_CI_AS
Chinese (Taiwan) | 0x0404 | 0x0404 | Chinese_Taiwan_Stroke_CI_AS
Corsican (France) | 0x0483 | 0x0483 | Latin1_General_CI_AI
Croatian (Bosnia and Herzegovina, Latin) | 0x101a | 0x041a | Croatian_CI_AS
Croatian (Croatia) | 0x041a | 0x041a | Croatian_CI_AS
Czech (Czech Republic) | 0x0405 | 0x0405 | Czech_CI_AS
Danish (Denmark) | 0x0406 | 0x0406 | Danish_Norwegian_CI_AS
Dari (Afghanistan) | 0x048c | 0x048c | Latin1_General_CI_AI
Divehi (Maldives) | 0x0465 | 0x0465 | Not available at server level
Dutch (Belgium) | 0x0813 | 0x0409 | Latin1_General_CI_AS
Dutch (Netherlands) | 0x0413 | 0x0409 | Latin1_General_CI_AS
English (Australia) | 0x0c09 | 0x0409 | Latin1_General_CI_AS
English (Belize) | 0x2809 | 0x0409 | Latin1_General_CI_AS
English (Canada) | 0x1009 | 0x0409 | Latin1_General_CI_AS
English (Caribbean) | 0x2409 | 0x0409 | Latin1_General_CI_AS
English (India) | 0x4009 | 0x0409 | Latin1_General_CI_AS
English (Ireland) | 0x1809 | 0x0409 | Latin1_General_CI_AS
English (Jamaica) | 0x2009 | 0x0409 | Latin1_General_CI_AS
English (Malaysia) | 0x4409 | 0x0409 | Latin1_General_CI_AS
English (New Zealand) | 0x1409 | 0x0409 | Latin1_General_CI_AS
English (Philippines) | 0x3409 | 0x0409 | Latin1_General_CI_AS
English (Singapore) | 0x4809 | 0x0409 | Latin1_General_CI_AS
English (South Africa) | 0x1c09 | 0x0409 | Latin1_General_CI_AS
English (Trinidad and Tobago) | 0x2c09 | 0x0409 | Latin1_General_CI_AS
English (United Kingdom) | 0x0809 | 0x0409 | Latin1_General_CI_AS
English (United States) | 0x0409 | 0x0409 | SQL_Latin1_General_CP1_CI_AS
English (Zimbabwe) | 0x3009 | 0x0409 | Latin1_General_CI_AS
Estonian (Estonia) | 0x0425 | 0x0425 | Estonian_CI_AS
Faroese (Faroe Islands) | 0x0438 | 0x0409 | Latin1_General_CI_AS
Filipino (Philippines) | 0x0464 | 0x0409 | Latin1_General_CI_AS
Finnish (Finland) | 0x040b | 0x040b | Finnish_Swedish_CI_AS
French (Belgium) | 0x080c | 0x040c | French_CI_AS
French (Canada) | 0x0c0c | 0x040c | French_CI_AS
French (France) | 0x040c | 0x040c | French_CI_AS
French (Luxembourg) | 0x140c | 0x040c | French_CI_AS
French (Monaco) | 0x180c | 0x040c | French_CI_AS
French (Switzerland) | 0x100c | 0x040c | French_CI_AS
Frisian (Netherlands) | 0x0462 | 0x0462 | Latin1_General_CI_AI
Galician | 0x0456 | 0x0409 | Latin1_General_CI_AS
Georgian (Georgia) | 0x10437 | 0x10437 | Georgian_Modern_Sort_CI_AS
Georgian (Georgia) | 0x0437 | 0x0419 | Latin1_General_CI_AS
German - Phone Book Sort (DIN) | 0x10407 | 0x10407 | German_PhoneBook_CI_AS
German (Austria) | 0x0c07 | 0x0409 | Latin1_General_CI_AS
German (Germany) | 0x0407 | 0x0409 | Latin1_General_CI_AS
German (Liechtenstein) | 0x1407 | 0x0409 | Latin1_General_CI_AS
German (Luxembourg) | 0x1007 | 0x0409 | Latin1_General_CI_AS
German (Switzerland) | 0x0807 | 0x0409 | Latin1_General_CI_AS
Greek (Greece) | 0x0408 | 0x0408 | Greek_CI_AS
Greenlandic (Greenland) | 0x046f | 0x0406 | Danish_Norwegian_CI_AS
Gujarati (India) | 0x0447 | 0x0439 | Not available at server level
Hausa (Nigeria, Latin) | 0x0468 | 0x0409 | Latin1_General_CI_AS
Hebrew (Israel) | 0x040d | 0x040d | Hebrew_CI_AS
Hindi (India) | 0x0439 | 0x0439 | Not available at server level
Hungarian (Hungary) | 0x040e | 0x040e | Hungarian_CI_AS
Hungarian Technical Sort | 0x1040e | 0x1040e | Hungarian_Technical_CI_AS
Icelandic (Iceland) | 0x040f | 0x040f | Icelandic_CI_AS
Igbo (Nigeria) | 0x0470 | 0x0409 | Latin1_General_CI_AS
Indonesian (Indonesia) | 0x0421 | 0x0409 | Latin1_General_CI_AS
Inuktitut (Canada, Latin) | 0x085d | 0x0409 | Latin1_General_CI_AS
Inuktitut (Syllabics) Canada | 0x045d | 0x045d | Latin1_General_CI_AI
Irish (Ireland) | 0x083c | 0x0409 | Latin1_General_CI_AS
Italian (Italy) | 0x0410 | 0x0409 | Latin1_General_CI_AS
Italian (Switzerland) | 0x0810 | 0x0409 | Latin1_General_CI_AS
Japanese (Japan XJIS) | 0x0411 | 0x0411 | Japanese_CI_AS
Japanese (Japan) | 0x040411 | 0x40411 | Latin1_General_CI_AI
Kannada (India) | 0x044b | 0x0439 | Not available at server level
Kazakh (Kazakhstan) | 0x043f | 0x043f | Kazakh_90_CI_AS
Khmer (Cambodia) | 0x0453 | 0x0453 | Not available at server level
K'iche (Guatemala) | 0x0486 | 0x0c0a | Modern_Spanish_CI_AS
Kinyarwanda (Rwanda) | 0x0487 | 0x0409 | Latin1_General_CI_AS
Konkani (India) | 0x0457 | 0x0439 | Not available at server level
Korean (Korea Dictionary Sort) | 0x0412 | 0x0412 | Korean_Wansung_CI_AS
Kyrgyz (Kyrgyzstan) | 0x0440 | 0x0419 | Cyrillic_General_CI_AS
Lao (Lao PDR) | 0x0454 | 0x0454 | Not available at server level
Latvian (Latvia) | 0x0426 | 0x0426 | Latvian_CI_AS
Lithuanian (Lithuania) | 0x0427 | 0x0427 | Lithuanian_CI_AS
Lower Sorbian (Germany) | 0x082e | 0x0409 | Latin1_General_CI_AS
Luxembourgish (Luxembourg) | 0x046e | 0x0409 | Latin1_General_CI_AS
Macedonian (North Macedonia) | 0x042f | 0x042f | Macedonian_FYROM_90_CI_AS
Malay (Brunei Darussalam) | 0x083e | 0x0409 | Latin1_General_CI_AS
Malay (Malaysia) | 0x043e | 0x0409 | Latin1_General_CI_AS
Malayalam (India) | 0x044c | 0x0439 | Not available at server level
Maltese (Malta) | 0x043a | 0x043a | Latin1_General_CI_AI
Maori (New Zealand) | 0x0481 | 0x0481 | Latin1_General_CI_AI
Mapudungun (Chile) | 0x047a | 0x047a | Latin1_General_CI_AI
Marathi (India) | 0x044e | 0x0439 | Not available at server level
Mohawk (Canada) | 0x047c | 0x047c | Latin1_General_CI_AI
Mongolian (Mongolia) | 0x0450 | 0x0419 | Cyrillic_General_CI_AS
Mongolian (PRC) | 0x0850 | 0x0419 | Cyrillic_General_CI_AS
Nepali (Nepal) | 0x0461 | 0x0461 | Not available at server level
Norwegian (Bokmål, Norway) | 0x0414 | 0x0414 | Latin1_General_CI_AI
Norwegian (Nynorsk, Norway) | 0x0814 | 0x0414 | Latin1_General_CI_AI
Occitan (France) | 0x0482 | 0x040c | French_CI_AS
Odia (India) | 0x0448 | 0x0439 | Not available at server level
Pashto (Afghanistan) | 0x0463 | 0x0463 | Not available at server level
Persian (Iran) | 0x0429 | 0x0429 | Latin1_General_CI_AI
Polish (Poland) | 0x0415 | 0x0415 | Polish_CI_AS
Portuguese (Brazil) | 0x0416 | 0x0409 | Latin1_General_CI_AS
Portuguese (Portugal) | 0x0816 | 0x0409 | Latin1_General_CI_AS
Punjabi (India) | 0x0446 | 0x0439 | Not available at server level
Quechua (Bolivia) | 0x046b | 0x0409 | Latin1_General_CI_AS
Quechua (Ecuador) | 0x086b | 0x0409 | Latin1_General_CI_AS
Quechua (Peru) | 0x0c6b | 0x0409 | Latin1_General_CI_AS
Romanian (Romania) | 0x0418 | 0x0418 | Romanian_CI_AS
Romansh (Switzerland) | 0x0417 | 0x0417 | Latin1_General_CI_AI
Russian (Russia) | 0x0419 | 0x0419 | Cyrillic_General_CI_AS
Sahka (Russia) | 0x0485 | 0x0485 | Latin1_General_CI_AI
Sami (Inari, Finland) | 0x243b | 0x083b | Latin1_General_CI_AI
Sami (Lule, Norway) | 0x103b | 0x043b | Latin1_General_CI_AI
Sami (Lule, Sweden) | 0x143b | 0x083b | Latin1_General_CI_AI
Sami (Northern, Finland) | 0x0c3b | 0x083b | Latin1_General_CI_AI
Sami (Northern, Norway) | 0x043b | 0x043b | Latin1_General_CI_AI
Sami (Northern, Sweden) | 0x083b | 0x083b | Latin1_General_CI_AI
Sami (Skolt, Finland) | 0x203b | 0x083b | Latin1_General_CI_AI
Sami (Southern, Norway) | 0x183b | 0x043b | Latin1_General_CI_AI
Sami (Southern, Sweden) | 0x1c3b | 0x083b | Latin1_General_CI_AI
Sanskrit (India) | 0x044f | 0x0439 | Not available at server level
Serbian (Bosnia and Herzegovina, Cyrillic) | 0x1c1a | 0x0c1a | Latin1_General_CI_AI
Serbian (Bosnia and Herzegovina, Latin) | 0x181a | 0x081a | Latin1_General_CI_AI
Serbian (Serbia, Cyrillic) | 0x0c1a | 0x0c1a | Latin1_General_CI_AI
Serbian (Serbia, Latin) | 0x081a | 0x081a | Latin1_General_CI_AI
Sesotho sa Leboa/Northern Sotho (South Africa) | 0x046c | 0x0409 | Latin1_General_CI_AS
Setswana/Tswana (South Africa) | 0x0432 | 0x0409 | Latin1_General_CI_AS
Sinhala (Sri Lanka) | 0x045b | 0x0439 | Not available at server level
Slovak (Slovakia) | 0x041b | 0x041b | Slovak_CI_AS
Slovenian (Slovenia) | 0x0424 | 0x0424 | Slovenian_CI_AS
Spanish (Argentina) | 0x2c0a | 0x0c0a | Modern_Spanish_CI_AS
Spanish (Bolivia) | 0x400a | 0x0c0a | Modern_Spanish_CI_AS
Spanish (Chile) | 0x340a | 0x0c0a | Modern_Spanish_CI_AS
Spanish (Colombia) | 0x240a | 0x0c0a | Modern_Spanish_CI_AS
Spanish (Costa Rica) | 0x140a | 0x0c0a | Modern_Spanish_CI_AS
Spanish (Dominican Republic) | 0x1c0a | 0x0c0a | Modern_Spanish_CI_AS
Spanish (Ecuador) | 0x300a | 0x0c0a | Modern_Spanish_CI_AS
Spanish (El Salvador) | 0x440a | 0x0c0a | Modern_Spanish_CI_AS
Spanish (Guatemala) | 0x100a | 0x0c0a | Modern_Spanish_CI_AS
Spanish (Honduras) | 0x480a | 0x0c0a | Modern_Spanish_CI_AS
Spanish (Mexico) | 0x080a | 0x0c0a | Modern_Spanish_CI_AS
Spanish (Nicaragua) | 0x4c0a | 0x0c0a | Modern_Spanish_CI_AS
Spanish (Panama) | 0x180a | 0x0c0a | Modern_Spanish_CI_AS
Spanish (Paraguay) | 0x3c0a | 0x0c0a | Modern_Spanish_CI_AS
Spanish (Peru) | 0x280a | 0x0c0a | Modern_Spanish_CI_AS
Spanish (Puerto Rico) | 0x500a | 0x0c0a | Modern_Spanish_CI_AS
Spanish (Spain) | 0x0c0a | 0x0c0a | Modern_Spanish_CI_AS
Spanish (Spain, Traditional Sort) | 0x040a | 0x040a | Traditional_Spanish_CI_AS
Spanish (United States) | 0x540a | 0x0409 | Latin1_General_CI_AS
Spanish (Uruguay) | 0x380a | 0x0c0a | Modern_Spanish_CI_AS
Spanish (Venezuela) | 0x200a | 0x0c0a | Modern_Spanish_CI_AS
Swahili (Kenya) | 0x0441 | 0x0409 | Latin1_General_CI_AS
Swedish (Finland) | 0x081d | 0x040b | Finnish_Swedish_CI_AS
Swedish (Sweden) | 0x041d | 0x040b | Finnish_Swedish_CI_AS
Syriac (Syria) | 0x045a | 0x045a | Not available at server level
Tajik (Tajikistan) | 0x0428 | 0x0419 | Cyrillic_General_CI_AS
Tamazight (Algeria, Latin) | 0x085f | 0x085f | Latin1_General_CI_AI
Tamil (India) | 0x0449 | 0x0439 | Not available at server level
Tatar (Russia) | 0x0444 | 0x0444 | Cyrillic_General_CI_AS
Telugu (India) | 0x044a | 0x0439 | Not available at server level
Thai (Thailand) | 0x041e | 0x041e | Thai_CI_AS
Tibetan (PRC) | 0x0451 | 0x0451 | Not available at server level
Turkish (Türkiye) | 0x041f | 0x041f | Turkish_CI_AS
Turkmen (Turkmenistan) | 0x0442 | 0x0442 | Latin1_General_CI_AI
Uighur (PRC) | 0x0480 | 0x0480 | Latin1_General_CI_AI
Ukrainian (Ukraine) | 0x0422 | 0x0422 | Ukrainian_CI_AS
Upper Sorbian (Germany) | 0x042e | 0x042e | Latin1_General_CI_AI
Urdu (Pakistan) | 0x0420 | 0x0420 | Latin1_General_CI_AI
Uzbek (Uzbekistan, Cyrillic) | 0x0843 | 0x0419 | Cyrillic_General_CI_AS
Uzbek (Uzbekistan, Latin) | 0x0443 | 0x0443 | Uzbek_Latin_90_CI_AS
Vietnamese (Vietnam) | 0x042a | 0x042a | Vietnamese_CI_AS
Welsh (United Kingdom) | 0x0452 | 0x0452 | Latin1_General_CI_AI
Wolof (Senegal) | 0x0488 | 0x040c | French_CI_AS
Xhosa/isiXhosa (South Africa) | 0x0434 | 0x0409 | Latin1_General_CI_AS
Yi (PRC) | 0x0478 | 0x0409 | Latin1_General_CI_AS
Yoruba (Nigeria) | 0x046a | 0x0409 | Latin1_General_CI_AS
Zulu/isiZulu (South Africa) | 0x0435 | 0x0409 | Latin1_General_CI_AS
After you assign a collation to the server, you can change it only by exporting all database objects and data, rebuilding the `master` database, and importing all database objects and data. Instead of changing the default collation of an instance of SQL Server, you can specify the desired collation when you create a new database or database column.
To query the server collation for an instance of SQL Server, use the `SERVERPROPERTY` function:
SQL
Copy
```
SELECT CONVERT (NVARCHAR (128), SERVERPROPERTY('collation'));

```

To query the server for all available collations, use the following `fn_helpcollations()` built-in function:
SQL
Copy
```
SELECT *
FROM sys.fn_helpcollations();

```

[](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#database-level-collations)
#### Database-level collations
When you create or modify a database, you can use the `COLLATE` clause of the `CREATE DATABASE` or `ALTER DATABASE` statement to specify the default database collation. If no collation is specified, the database is assigned the server collation.
You can't change the collation of system databases unless you change the collation for the server.
  * In SQL Server and Azure SQL Managed Instance, the database collation is used for all metadata in the database, and the collation is the default for all string columns, temporary objects, variable names, and any other strings used in the database.
  * In Azure SQL Database, there's no server collation, so each database has a collation for data and a collation for the catalog. The CATALOG_COLLATION is used for all metadata in the database, and the collation is the default for all string columns, temporary objects, variable names, and any other strings used in the database. The CATALOG_COLLATION is set upon creation and can't be changed.


When you change the collation of a user database, there can be collation conflicts when queries in the database access temporary tables. Temporary tables are always stored in the `tempdb` system database, which uses the collation for the instance. Queries that compare character data between the user database and `tempdb` might fail if the collations cause a conflict in evaluating the character data. You can resolve this issue by specifying the `COLLATE` clause in the query. For more information, see [COLLATE](https://learn.microsoft.com/en-us/sql/t-sql/statements/collations?view=sql-server-ver17).
You can change the collation of a user database by using an `ALTER DATABASE` statement similar to the following code sample:
SQL
Copy
```
ALTER DATABASE myDB COLLATE Greek_CS_AI;

```

Altering the database-level collation doesn't affect column-level or expression-level collations. It doesn't affect data in existing columns.
You can retrieve the current collation of a database by using a statement similar to the following code sample:
SQL
Copy
```
SELECT CONVERT (NVARCHAR (128), DATABASEPROPERTYEX('database_name', 'collation'));

```

[](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#column-level-collations)
#### Column-level collations
When you create or alter a table, you can specify collations for each character-string column by using the `COLLATE` clause. If you don't specify a collation, the column is assigned the default collation of the database.
You can change the collation of a column by using an `ALTER TABLE` statement similar to the following code sample:
SQL
Copy
```
ALTER TABLE myTable ALTER COLUMN mycol NVARCHAR (10) COLLATE Greek_CS_AI;

```

[](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#expression-level-collations)
#### Expression-level collations
Expression-level collations are set when a statement is run, and they affect the way a result set is returned. This enables `ORDER BY` sort results to be locale-specific. To implement expression-level collations, use a `COLLATE` clause such as the following code sample:
SQL
Copy
```
SELECT name
FROM customer
ORDER BY name COLLATE Latin1_General_CS_AI;

```

[](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#locale)
### Locale
A locale is a set of information that's associated with a location or a culture. The information can include the name and identifier of the spoken language, the script that's used to write the language, and cultural conventions. Collations can be associated with one or more locales. For more information, see [Locale IDs Assigned by Microsoft](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-lcid/a9eac961-e77d-41a6-90a5-ce1a8b0cdb9c).
[](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#code-page)
### Code page
A code page is an ordered set of characters of a given script in which a numeric index, or code point value, is associated with each character. A Windows code page is typically referred to as a _character set_ or a _charset_. Code pages are used to provide support for the character sets and keyboard layouts that are used by different Windows system locales.
[](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#sort-order)
### Sort order
Sort order specifies how data values are sorted. The order affects the results of data comparison. Data is sorted by using collations, and it can be optimized by using indexes.
[](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#unicode-support)
