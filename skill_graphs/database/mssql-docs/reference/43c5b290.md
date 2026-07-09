## Computed columns and timestamp columns
Values in the data file being imported for computed or **timestamp** columns are ignored, and SQL Server automatically assigns values. If the data file doesn't contain values for the computed or **timestamp** columns in the table, use a format file to specify that the computed or **timestamp** columns in the table should be skipped when importing data; SQL Server automatically assigns values for the column.
Computed and **timestamp** columns are bulk copied from SQL Server to a data file as usual.
[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#specify-identifiers-that-contain-spaces-or-quotation-marks)
