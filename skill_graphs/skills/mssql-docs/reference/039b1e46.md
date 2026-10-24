## Character mode (`-c`) and native mode (`-n`) best practices
This section has recommendations for character mode (`-c`) and native mode (`-n`).
  * (Administrator/User) When possible, use native format (`-n`) to avoid the separator issue. Use the native format to export and import using SQL Server. Export data from SQL Server using the `-c` or `-w` option if you plan to export the data to a non-SQL Server database.
  * (Administrator) Verify data when using `bcp out`. For example, when you use `bcp out`, `bcp in`, and then `bcp out` verify that the data is properly exported and the terminator values aren't used as part of some data value. Consider overriding the default terminators (using `-t` and `-r` options) with random hexadecimal values to avoid conflicts between terminator values and data values.
  * (User) Use a long and unique terminator (any sequence of bytes or characters) to minimize the possibility of a conflict with the actual string value. This can be done by using the `-t` and `-r` options.


[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#examples)
