## Bulk exporting or importing SQLXML documents
To bulk export or import SQLXML data, use one of the following data types in your format file.
Expand table
Data type | Effect
---|---
`SQLCHAR` or `SQLVARYCHAR` | The data is sent in the client code page or in the code page implied by the collation). The effect is the same as specifying the `-c` switch without specifying a format file.
`SQLNCHAR` or `SQLNVARCHAR` | The data is sent as Unicode. The effect is the same as specifying the `-w` switch without specifying a format file.
`SQLBINARY` or `SQLVARYBIN` | The data is sent without any conversion.
[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#permissions)
