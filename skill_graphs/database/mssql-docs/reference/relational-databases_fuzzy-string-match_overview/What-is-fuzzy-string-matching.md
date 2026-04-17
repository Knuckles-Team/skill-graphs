# What is fuzzy string matching?
Feedback
Summarize this article for me
##  In this article
  1. [Fuzzy functions](https://learn.microsoft.com/en-us/sql/relational-databases/fuzzy-string-match/overview?view=fabric-sqldb&viewFallbackFrom=sql-server-ver17#fuzzy-functions)
  2. [Examples](https://learn.microsoft.com/en-us/sql/relational-databases/fuzzy-string-match/overview?view=fabric-sqldb&viewFallbackFrom=sql-server-ver17#examples)
  3. [Clean up](https://learn.microsoft.com/en-us/sql/relational-databases/fuzzy-string-match/overview?view=fabric-sqldb&viewFallbackFrom=sql-server-ver17#clean-up)
  4. [Related content](https://learn.microsoft.com/en-us/sql/relational-databases/fuzzy-string-match/overview?view=fabric-sqldb&viewFallbackFrom=sql-server-ver17#related-content)


**Applies to:** ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=fabric-sqldb) SQL Server 2025 (17.x) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=fabric-sqldb) [Azure SQL Database](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=fabric-sqldb#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=fabric-sqldb) [Azure SQL Managed Instance](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=fabric-sqldb#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=fabric-sqldb) [SQL database in Microsoft Fabric](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=fabric-sqldb#applies-to)
Use fuzzy, or approximate, string matching to check if two strings are similar, and calculate the difference between two strings. Use this capability to identify strings that might be different because of character corruption. Corruption includes spelling errors, transposed characters, missing characters, or abbreviations. Fuzzy string matching uses algorithms to detect similar sounding strings.
Fuzzy string matching is currently in preview for SQL Server 2025 (17.x) and requires enabling the [preview feature database scoped configuration](https://learn.microsoft.com/en-us/sql/t-sql/statements/alter-database-scoped-configuration-transact-sql?view=fabric-sqldb#preview-features).
Fuzzy string matching is available in Azure SQL Managed Instance with the **SQL Server 2025** or **Always-up-to-date** [update policy](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/update-policy).
[](https://learn.microsoft.com/en-us/sql/relational-databases/fuzzy-string-match/overview?view=fabric-sqldb&viewFallbackFrom=sql-server-ver17#fuzzy-functions)
## Fuzzy functions
Expand table
Function | Description
---|---
[EDIT_DISTANCE](https://learn.microsoft.com/en-us/sql/t-sql/functions/edit-distance-transact-sql?view=fabric-sqldb) | Calculates the number of insertions, deletions, substitutions, and transpositions needed to transform one string to another.
[EDIT_DISTANCE_SIMILARITY](https://learn.microsoft.com/en-us/sql/t-sql/functions/edit-distance-similarity-transact-sql?view=fabric-sqldb) | Calculates a similarity value ranging from 0 (indicating no match) to 100 (indicating full match).
[JARO_WINKLER_DISTANCE](https://learn.microsoft.com/en-us/sql/t-sql/functions/jaro-winkler-distance-transact-sql?view=fabric-sqldb) | Calculates the edit distance between two strings giving preference to strings that match from the beginning for a set prefix length.
[JARO_WINKLER_SIMILARITY](https://learn.microsoft.com/en-us/sql/t-sql/functions/jaro-winkler-similarity-transact-sql?view=fabric-sqldb) | Calculates a similarity value ranging from 0 (indicating no match) to 100 (indicating full match).
Currently, the functions don't adhere to the comparison semantics defined by collation settings, such as case insensitivity and other collation-specific rules. Once support for collation rules is implemented, the functions' output will reflect these semantics and might change accordingly.
[](https://learn.microsoft.com/en-us/sql/relational-databases/fuzzy-string-match/overview?view=fabric-sqldb&viewFallbackFrom=sql-server-ver17#examples)
## Examples
The following examples demonstrate the fuzzy string matching functions.
[](https://learn.microsoft.com/en-us/sql/relational-databases/fuzzy-string-match/overview?view=fabric-sqldb&viewFallbackFrom=sql-server-ver17#example-table)
### Example table
Before you can run example queries, create and populate an example table.
To create and populate the example table, connect to a non-production user database, and run the following script:
SQL
Copy
```
-- Step 1: Create the table
CREATE TABLE WordPairs
(
    WordID INT IDENTITY (1, 1) PRIMARY KEY, -- Auto-incrementing ID
    WordUK NVARCHAR (50), -- UK English word
    WordUS NVARCHAR (50)  -- US English word
);

-- Step 2: Insert the data
INSERT INTO WordPairs (WordUK, WordUS)
VALUES ('Colour', 'Color'),
       ('Flavour', 'Flavor'),
       ('Centre', 'Center'),
       ('Theatre', 'Theater'),
       ('Organise', 'Organize'),
       ('Analyse', 'Analyze'),
       ('Catalogue', 'Catalog'),
       ('Programme', 'Program'),
       ('Metre', 'Meter'),
       ('Honour', 'Honor'),
       ('Neighbour', 'Neighbor'),
       ('Travelling', 'Traveling'),
       ('Grey', 'Gray'),
       ('Defence', 'Defense'),
       ('Practise', 'Practice'), -- Verb form in UK
       ('Practice', 'Practice'), -- Noun form in both
       ('Aluminium', 'Aluminum'),
       ('Cheque', 'Check'); -- Bank cheque vs. check

```

[](https://learn.microsoft.com/en-us/sql/relational-databases/fuzzy-string-match/overview?view=fabric-sqldb&viewFallbackFrom=sql-server-ver17#example-edit_distance)
### Example _EDIT_DISTANCE_
SQL
Copy
```
SELECT WordUK,
       WordUS,
       EDIT_DISTANCE(WordUK, WordUS) AS Distance
FROM WordPairs
WHERE EDIT_DISTANCE(WordUK, WordUS) <= 2
ORDER BY Distance ASC;

```

Returns:
Output
Copy
```
WordUK                         WordUS                         Distance
------------------------------ ------------------------------ -----------
Practice                       Practice                       0
Aluminium                      Aluminum                       1
Honour                         Honor                          1
Neighbour                      Neighbor                       1
Travelling                     Traveling                      1
Grey                           Gray                           1
Defence                        Defense                        1
Practise                       Practice                       1
Colour                         Color                          1
Flavour                        Flavor                         1
Organise                       Organize                       1
Analyse                        Analyze                        1
Catalogue                      Catalog                        2
Programme                      Program                        2
Metre                          Meter                          2
Centre                         Center                         2
Theatre                        Theater                        2

```

[](https://learn.microsoft.com/en-us/sql/relational-databases/fuzzy-string-match/overview?view=fabric-sqldb&viewFallbackFrom=sql-server-ver17#example-edit_distance_similarity)
### Example _EDIT_DISTANCE_SIMILARITY_
SQL
Copy
```
SELECT WordUK,
       WordUS,
       EDIT_DISTANCE_SIMILARITY(WordUK, WordUS) AS Similarity
FROM WordPairs
WHERE EDIT_DISTANCE_SIMILARITY(WordUK, WordUS) >= 75
ORDER BY Similarity DESC;

```

Returns:
Output
Copy
```
WordUK                         WordUS                         Similarity
------------------------------ ------------------------------ -----------
Practice                       Practice                       100
Travelling                     Traveling                      90
Aluminium                      Aluminum                       89
Neighbour                      Neighbor                       89
Organise                       Organize                       88
Practise                       Practice                       88
Defence                        Defense                        86
Analyse                        Analyze                        86
Flavour                        Flavor                         86
Colour                         Color                          83
Honour                         Honor                          83
Catalogue                      Catalog                        78
Programme                      Program                        78
Grey                           Gray                           75

```

[](https://learn.microsoft.com/en-us/sql/relational-databases/fuzzy-string-match/overview?view=fabric-sqldb&viewFallbackFrom=sql-server-ver17#example-jaro_winkler_distance)
### Example _JARO_WINKLER_DISTANCE_
SQL
Copy
```
SELECT WordUK,
       WordUS,
       JARO_WINKLER_DISTANCE(WordUK, WordUS) AS Distance
FROM WordPairs
WHERE JARO_WINKLER_DISTANCE(WordUK, WordUS) <= .05
ORDER BY Distance ASC;

```

Returns:
Output
Copy
```
WordUK                         WordUS                         Distance
------------------------------ ------------------------------ -----------
Practice                       Practice                       0
Travelling                     Traveling                      0.02
Neighbour                      Neighbor                       0.0222222222222223
Aluminium                      Aluminum                       0.0222222222222223
Theatre                        Theater                        0.0285714285714286
Flavour                        Flavor                         0.0285714285714286
Centre                         Center                         0.0333333333333333
Colour                         Color                          0.0333333333333333
Honour                         Honor                          0.0333333333333333
Catalogue                      Catalog                        0.0444444444444444
Programme                      Program                        0.0444444444444444
Metre                          Meter                          0.0466666666666667

```

[](https://learn.microsoft.com/en-us/sql/relational-databases/fuzzy-string-match/overview?view=fabric-sqldb&viewFallbackFrom=sql-server-ver17#example-jaro_winkler_similarity)
### Example _JARO_WINKLER_SIMILARITY_
SQL
Copy
```
SELECT WordUK,
       WordUS,
       JARO_WINKLER_SIMILARITY(WordUK, WordUS) AS Similarity
FROM WordPairs
WHERE JARO_WINKLER_SIMILARITY(WordUK, WordUS) > 90
ORDER BY Similarity DESC;

```

Returns:
Output
Copy
```
WordUK                         WordUS                         Similarity
------------------------------ ------------------------------ -----------
Practice                       Practice                       100
Aluminium                      Aluminum                       98
Neighbour                      Neighbor                       98
Travelling                     Traveling                      98
Colour                         Color                          97
Flavour                        Flavor                         97
Centre                         Center                         97
Theatre                        Theater                        97
Honour                         Honor                          97
Catalogue                      Catalog                        96
Programme                      Program                        96
Metre                          Meter                          95
Organise                       Organize                       95
Practise                       Practice                       95
Analyse                        Analyze                        94
Defence                        Defense                        94

```

[](https://learn.microsoft.com/en-us/sql/relational-databases/fuzzy-string-match/overview?view=fabric-sqldb&viewFallbackFrom=sql-server-ver17#example-query-with-all-functions)
### Example query with all functions
The following query demonstrates all of the regular expression functions currently available.
SQL
Copy
```
SELECT T.source_string,
       T.target_string,
       EDIT_DISTANCE(T.source_string, T.target_string) AS ED_Distance,
       JARO_WINKLER_DISTANCE(T.source_string, T.target_string) AS JW_Distance,
       EDIT_DISTANCE_SIMILARITY(T.source_string, T.target_string) AS ED_Similarity,
       JARO_WINKLER_SIMILARITY(T.source_string, T.target_string) AS JW_Similarity
FROM (VALUES ('Black', 'Red'),
             ('Colour', 'Yellow'),
             ('Colour', 'Color'),
             ('Microsoft', 'Msft'),
             ('Regex', 'Regex')
     ) AS T(source_string, target_string);

```

Returns:
Output
Copy
```
source_string  target_string  ED_Distance    JW_Distance           ED_Similarity  JW_Similarity
-------------- -------------- -------------- --------------------- -------------- --------------
Black          Red            5              1                     0              0
Colour         Yellow         5              0.444444444444445     17             55
Colour         Color          1              0.0333333333333333    83             96
Microsoft      Msft           5              0.491666666666667     44             50
Regex          Regex          0              0                     100            100

```

[](https://learn.microsoft.com/en-us/sql/relational-databases/fuzzy-string-match/overview?view=fabric-sqldb&viewFallbackFrom=sql-server-ver17#clean-up)
## Clean up
After you're done using the example data, delete the example table:
SQL
Copy
```
IF OBJECT_ID('dbo.WordPairs', 'U') IS NOT NULL
BEGIN
    DROP TABLE dbo.WordPairs;
END

```

[](https://learn.microsoft.com/en-us/sql/relational-databases/fuzzy-string-match/overview?view=fabric-sqldb&viewFallbackFrom=sql-server-ver17#related-content)
## Related content
  * [EDIT_DISTANCE (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/functions/edit-distance-transact-sql?view=fabric-sqldb)
  * [EDIT_DISTANCE_SIMILARITY (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/functions/edit-distance-similarity-transact-sql?view=fabric-sqldb)
  * [JARO_WINKLER_DISTANCE (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/functions/jaro-winkler-distance-transact-sql?view=fabric-sqldb)
  * [JARO_WINKLER_SIMILARITY (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/functions/jaro-winkler-similarity-transact-sql?view=fabric-sqldb)


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
  * [ EDIT_DISTANCE (Transact-SQL) - SQL Server ](https://learn.microsoft.com/en-us/sql/t-sql/functions/edit-distance-transact-sql?source=recommendations)
EDIT_DISTANCE calculates the number of insertions, deletions, substitutions, and transpositions needed to transform one string to another.
  * [ JARO_WINKLER_SIMILARITY (Transact-SQL) - SQL Server ](https://learn.microsoft.com/en-us/sql/t-sql/functions/jaro-winkler-similarity-transact-sql?source=recommendations)
JARO_WINKLER_SIMILARITY calculates a similarity value ranging from 0 (indicating no match) to 100 (indicating full match).
  * [ EDIT_DISTANCE_SIMILARITY (Transact-SQL) - SQL Server ](https://learn.microsoft.com/en-us/sql/t-sql/functions/edit-distance-similarity-transact-sql?source=recommendations)
EDIT_DISTANCE_SIMILARITY calculates a similarity value ranging from 0 (indicating no match) to 100 (indicating full match).
  * [ JARO_WINKLER_DISTANCE (Transact-SQL) - SQL Server ](https://learn.microsoft.com/en-us/sql/t-sql/functions/jaro-winkler-distance-transact-sql?source=recommendations)
JARO_WINKLER_DISTANCE calculates the edit distance between two strings giving preference to strings that match from the beginning for a set prefix length.
  * [ sp_invoke_external_rest_endpoint (Transact-SQL) - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-invoke-external-rest-endpoint-transact-sql?source=recommendations)
The sp_invoke_external_rest_endpoint stored procedure invokes an HTTPS REST endpoint.
  * [ SOUNDEX (Transact-SQL) - SQL Server ](https://learn.microsoft.com/en-us/sql/t-sql/functions/soundex-transact-sql?source=recommendations)
SOUNDEX returns a four-character code to evaluate the similarity of two strings.


Show 3 more
Mar 8, 4 PM - Mar 8, 4 PM
Experiment with what's next in AI-driven apps and agent design
* * *
  * Last updated on 11/18/2025


##  In this article
  1. [Fuzzy functions](https://learn.microsoft.com/en-us/sql/relational-databases/fuzzy-string-match/overview?view=fabric-sqldb&viewFallbackFrom=sql-server-ver17#fuzzy-functions)
  2. [Examples](https://learn.microsoft.com/en-us/sql/relational-databases/fuzzy-string-match/overview?view=fabric-sqldb&viewFallbackFrom=sql-server-ver17#examples)
  3. [Clean up](https://learn.microsoft.com/en-us/sql/relational-databases/fuzzy-string-match/overview?view=fabric-sqldb&viewFallbackFrom=sql-server-ver17#clean-up)
  4. [Related content](https://learn.microsoft.com/en-us/sql/relational-databases/fuzzy-string-match/overview?view=fabric-sqldb&viewFallbackFrom=sql-server-ver17#related-content)


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
[ Sign in ](https://learn.microsoft.com/en-us/sql/relational-databases/fuzzy-string-match/overview?view=fabric-sqldb&viewFallbackFrom=sql-server-ver17)
[English (United States)](https://learn.microsoft.com/en-us/locale?target=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fsql%2Frelational-databases%2Ffuzzy-string-match%2Foverview%3Fview%3Dfabric-sqldb%26viewFallbackFrom%3Dsql-server-ver17)
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
