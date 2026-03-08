## Log shipping
Log shipping is based on backup and restore, so there are no differences in the databases, file structures, and other elements for SQL Server on Windows Server versus SQL Server on Linux. You can configure log shipping between a Windows Server-based SQL Server installation and a Linux one, and between distributions of Linux. Everything else remains the same.
Just like with an AG, log shipping doesn't work when the source server is at a higher SQL Server major version, against a target that is at a lower major version.
[](https://learn.microsoft.com/en-us/sql/database-engine/sql-server-business-continuity-dr?view=sql-server-ver17#summary)
