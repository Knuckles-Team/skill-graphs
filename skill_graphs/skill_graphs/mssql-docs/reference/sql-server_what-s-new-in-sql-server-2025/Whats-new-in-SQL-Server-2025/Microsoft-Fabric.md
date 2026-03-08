## Microsoft Fabric
Expand table
New feature or update | Details
---|---
[Mirroring in Fabric](https://learn.microsoft.com/en-us/fabric/database/mirrored-database/overview) | Continuously replicate data to Microsoft Fabric from SQL Server 2025 on-premises. Microsoft Fabric already includes mirroring from a variety of sources, including Azure SQL Database and Azure SQL Managed Instance. For more information on SQL Server 2025 database mirroring to Fabric, see [Mirrored SQL Server databases in Microsoft Fabric](https://learn.microsoft.com/en-us/fabric/database/mirrored-database/sql-server).
[](https://learn.microsoft.com/en-us/sql/sql-server/what-s-new-in-sql-server-2025?view=sql-server-ver17#fabric-mirroring-for-sql-server-2025)
### Fabric mirroring for SQL Server 2025
  * You can configure SQL Server resource governor to manage resource usage for Mirroring in Fabric for SQL Server 2025 (17.x). Each workload group is for a specific phase of mirroring.
For an example and to get started, see [Configure resource governor for Fabric mirroring](https://learn.microsoft.com/en-us/fabric/database/mirrored-database/sql-server-performance#resource-governor-for-sql-server-mirroring). For more information, see [Resource governor workload group](https://learn.microsoft.com/en-us/sql/relational-databases/resource-governor/resource-governor-workload-group?view=sql-server-ver17).
  * You can enable and configure the autoreseed feature for Fabric mirroring to prevent the transaction log from filling in SQL Server 2025 (17.x).
For an example and to get started, see [Configure automatic reseed](https://learn.microsoft.com/en-us/fabric/database/mirrored-database/sql-server-configure-automatic-reseed).
  * You can configure a maximum and lower bound of transactions to be processed by Fabric Mirroring in SQL Server 2025 (17.x).
For an example and to get started, see [Configure control scan performance](https://learn.microsoft.com/en-us/fabric/database/mirrored-database/sql-server-performance#control-scan-performance).


[](https://learn.microsoft.com/en-us/sql/sql-server/what-s-new-in-sql-server-2025?view=sql-server-ver17#sql-server-analysis-services)
