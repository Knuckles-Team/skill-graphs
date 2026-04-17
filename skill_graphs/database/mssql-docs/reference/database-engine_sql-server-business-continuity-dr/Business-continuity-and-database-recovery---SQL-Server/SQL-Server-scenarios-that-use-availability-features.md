## SQL Server scenarios that use availability features
You can use Always On availability groups, failover cluster instances, and log shipping in different ways, and not just for availability. There are four main ways you can use the availability features:
  * High availability
  * Disaster recovery
  * Migrations and upgrades
  * Scaling out readable copies of one or more databases


The following sections describe the relevant features for each scenario. One feature not covered is [SQL Server replication](https://learn.microsoft.com/en-us/sql/relational-databases/replication/sql-server-replication?view=sql-server-ver17). While SQL Server replication isn't officially designated as an availability feature under the Always On umbrella, it's often used for making data redundant in certain scenarios. Merge replication isn't supported for SQL Server on Linux. For more information, see [SQL Server replication on Linux](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-replication?view=sql-server-ver17).
The SQL Server availability features don't replace the requirement to have a robust, well tested backup and restore strategy. A backup and restore strategy is the most fundamental building block of any availability solution.
[](https://learn.microsoft.com/en-us/sql/database-engine/sql-server-business-continuity-dr?view=sql-server-ver17#high-availability)
