## Data validation
**bcp** now enforces data validation and data checks that can cause scripts to fail if they're executed on invalid data in a data file. For example, **bcp** now verifies that:
  * The native representations of float or real data types are valid.
  * Unicode data has an even-byte length.


Forms of invalid data that could be bulk imported in earlier versions of SQL Server can fail to load now; whereas, in earlier versions, the failure didn't occur until a client tried to access the invalid data. The added validation minimizes surprises when querying the data after bulkload.
[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#bulk-exporting-or-importing-sqlxml-documents)
