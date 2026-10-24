## Complex script support
SQL Server can support inputting, storing, changing, and displaying complex scripts. Complex scripts include the following types:
  * Scripts that include the combination of both right-to-left and left-to-right text, such as a combination of Arabic and English text.
  * Scripts whose characters change shape depending on their position, or when combined with other characters, such as Arabic, Indic, and Thai characters.
  * Languages, such as Thai, that require internal dictionaries to recognize words because there are no breaks between them.


Database applications that interact with SQL Server must use controls that support complex scripts. Standard Windows form controls that are created in managed code are complex-script-enabled.
[](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#japanese-collations-added-in-sql-server-2017)
### Japanese collations added in SQL Server 2017
Starting with SQL Server 2017 (14.x), new Japanese collation families are supported, with the permutations of various options (`_CS`, `_AS`, `_KS`, `_WS`, and `_VSS`), as well as `_BIN` and `_BIN2`.
To list these collations, you can query the SQL Server Database Engine:
SQL
Copy
```
SELECT name,
       description
FROM sys.fn_helpcollations()
WHERE COLLATIONPROPERTY(name, 'Version') = 3;

```

All the new collations have built-in support for supplementary characters, so none of the new `140` collations has (or needs) the SC flag.
These collations are supported in Database Engine indexes, memory-optimized tables, columnstore indexes, and natively compiled modules.
[](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#collations-in-azure-sql-database)
