## Specify identifiers that contain spaces or quotation marks
SQL Server identifiers can include characters such as embedded spaces and quotation marks. Such identifiers must be treated as follows:
  * When you specify an identifier or file name that includes a space or quotation mark at the command prompt, enclose the identifier in quotation marks ("").
For example, the following `bcp out` command creates a data file named `Currency Types.dat`:
Windows Command Prompt
Copy
```
bcp AdventureWorks2022.Sales.Currency out "Currency Types.dat" -T -c

```

  * To specify a database name that contains a space or quotation mark, you must use the `-q` option.
  * For owner, table, or view names that contain embedded spaces or quotation marks, you can either:
    * Specify the `-q` option, or
    * Enclose the owner, table, or view name in brackets (`[]`) inside the quotation marks.


[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#data-validation)
